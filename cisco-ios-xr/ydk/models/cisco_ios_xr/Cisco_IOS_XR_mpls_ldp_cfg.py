""" Cisco_IOS_XR_mpls_ldp_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR mpls\-ldp package configuration.

This module contains definitions
for the following management objects\:
  mpls\-ldp\: MPLS LDP configuration

This YANG module augments the
  Cisco\-IOS\-XR\-snmp\-agent\-cfg
module with configuration data.

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
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


class MplsLdpAdvertiseBgpacl(Enum):
    """
    MplsLdpAdvertiseBgpacl

    Mpls ldp advertise bgpacl

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
    _revision = '2015-11-09'

    def __init__(self):
        super(MplsLdp, self).__init__()
        self._top_entity = None

        self.yang_name = "mpls-ldp"
        self.yang_parent_name = "Cisco-IOS-XR-mpls-ldp-cfg"

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

    def __setattr__(self, name, value):
        self._check_monkey_patching_error(name, value)
        with _handle_type_error():
            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                    "Please use list append or extend method."
                                    .format(value))
            if isinstance(value, Enum.YLeaf):
                value = value.name
            if name in ("enable") and name in self.__dict__:
                if isinstance(value, YLeaf):
                    self.__dict__[name].set(value.get())
                elif isinstance(value, YLeafList):
                    super(MplsLdp, self).__setattr__(name, value)
                else:
                    self.__dict__[name].set(value)
            else:
                if hasattr(value, "parent") and name != "parent":
                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                        value.parent = self
                    elif value.parent is None and value.yang_name in self._children_yang_names:
                        value.parent = self
                super(MplsLdp, self).__setattr__(name, value)


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
        _revision = '2015-11-09'

        def __init__(self):
            super(MplsLdp.DefaultVrf, self).__init__()

            self.yang_name = "default-vrf"
            self.yang_parent_name = "mpls-ldp"

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


        class Afs(Entity):
            """
            Address Family specific configuration for MPLS
            LDP
            
            .. attribute:: af
            
            	Configure data for given Address Family
            	**type**\: list of    :py:class:`Af <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.DefaultVrf.Afs.Af>`
            
            

            """

            _prefix = 'mpls-ldp-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(MplsLdp.DefaultVrf.Afs, self).__init__()

                self.yang_name = "afs"
                self.yang_parent_name = "default-vrf"

                self.af = YList(self)

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in () and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(MplsLdp.DefaultVrf.Afs, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(MplsLdp.DefaultVrf.Afs, self).__setattr__(name, value)


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
                _revision = '2015-11-09'

                def __init__(self):
                    super(MplsLdp.DefaultVrf.Afs.Af, self).__init__()

                    self.yang_name = "af"
                    self.yang_parent_name = "afs"

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

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("af_name",
                                    "enable") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(MplsLdp.DefaultVrf.Afs.Af, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(MplsLdp.DefaultVrf.Afs.Af, self).__setattr__(name, value)


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
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(MplsLdp.DefaultVrf.Afs.Af.Label, self).__init__()

                        self.yang_name = "label"
                        self.yang_parent_name = "af"

                        self.local = MplsLdp.DefaultVrf.Afs.Af.Label.Local()
                        self.local.parent = self
                        self._children_name_map["local"] = "local"
                        self._children_yang_names.add("local")

                        self.remote = MplsLdp.DefaultVrf.Afs.Af.Label.Remote()
                        self.remote.parent = self
                        self._children_name_map["remote"] = "remote"
                        self._children_yang_names.add("remote")


                    class Remote(Entity):
                        """
                        Configure remote/peer label policies and
                        control
                        
                        .. attribute:: accept
                        
                        	Configure inbound label acceptance
                        	**type**\:   :py:class:`Accept <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.DefaultVrf.Afs.Af.Label.Remote.Accept>`
                        
                        

                        """

                        _prefix = 'mpls-ldp-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(MplsLdp.DefaultVrf.Afs.Af.Label.Remote, self).__init__()

                            self.yang_name = "remote"
                            self.yang_parent_name = "label"

                            self.accept = MplsLdp.DefaultVrf.Afs.Af.Label.Remote.Accept()
                            self.accept.parent = self
                            self._children_name_map["accept"] = "accept"
                            self._children_yang_names.add("accept")


                        class Accept(Entity):
                            """
                            Configure inbound label acceptance
                            
                            .. attribute:: peer_accept_policies
                            
                            	Configuration related to neighbors for inbound label acceptance
                            	**type**\:   :py:class:`PeerAcceptPolicies <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.DefaultVrf.Afs.Af.Label.Remote.Accept.PeerAcceptPolicies>`
                            
                            

                            """

                            _prefix = 'mpls-ldp-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(MplsLdp.DefaultVrf.Afs.Af.Label.Remote.Accept, self).__init__()

                                self.yang_name = "accept"
                                self.yang_parent_name = "remote"

                                self.peer_accept_policies = MplsLdp.DefaultVrf.Afs.Af.Label.Remote.Accept.PeerAcceptPolicies()
                                self.peer_accept_policies.parent = self
                                self._children_name_map["peer_accept_policies"] = "peer-accept-policies"
                                self._children_yang_names.add("peer-accept-policies")


                            class PeerAcceptPolicies(Entity):
                                """
                                Configuration related to neighbors for
                                inbound label acceptance
                                
                                .. attribute:: peer_accept_policy
                                
                                	Control acceptance of labels from a neighbor for prefix(es) using ACL
                                	**type**\: list of    :py:class:`PeerAcceptPolicy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.DefaultVrf.Afs.Af.Label.Remote.Accept.PeerAcceptPolicies.PeerAcceptPolicy>`
                                
                                

                                """

                                _prefix = 'mpls-ldp-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(MplsLdp.DefaultVrf.Afs.Af.Label.Remote.Accept.PeerAcceptPolicies, self).__init__()

                                    self.yang_name = "peer-accept-policies"
                                    self.yang_parent_name = "accept"

                                    self.peer_accept_policy = YList(self)

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in () and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(MplsLdp.DefaultVrf.Afs.Af.Label.Remote.Accept.PeerAcceptPolicies, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(MplsLdp.DefaultVrf.Afs.Af.Label.Remote.Accept.PeerAcceptPolicies, self).__setattr__(name, value)


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
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(MplsLdp.DefaultVrf.Afs.Af.Label.Remote.Accept.PeerAcceptPolicies.PeerAcceptPolicy, self).__init__()

                                        self.yang_name = "peer-accept-policy"
                                        self.yang_parent_name = "peer-accept-policies"

                                        self.lsr_id = YLeaf(YType.str, "lsr-id")

                                        self.label_space_id = YLeaf(YType.uint32, "label-space-id")

                                        self.prefix_acl_name = YLeaf(YType.str, "prefix-acl-name")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("lsr_id",
                                                        "label_space_id",
                                                        "prefix_acl_name") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(MplsLdp.DefaultVrf.Afs.Af.Label.Remote.Accept.PeerAcceptPolicies.PeerAcceptPolicy, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(MplsLdp.DefaultVrf.Afs.Af.Label.Remote.Accept.PeerAcceptPolicies.PeerAcceptPolicy, self).__setattr__(name, value)

                                    def has_data(self):
                                        return (
                                            self.lsr_id.is_set or
                                            self.label_space_id.is_set or
                                            self.prefix_acl_name.is_set)

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.lsr_id.yfilter != YFilter.not_set or
                                            self.label_space_id.yfilter != YFilter.not_set or
                                            self.prefix_acl_name.yfilter != YFilter.not_set)

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "peer-accept-policy" + "[lsr-id='" + self.lsr_id.get() + "']" + "[label-space-id='" + self.label_space_id.get() + "']" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()
                                        if (self.lsr_id.is_set or self.lsr_id.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.lsr_id.get_name_leafdata())
                                        if (self.label_space_id.is_set or self.label_space_id.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.label_space_id.get_name_leafdata())
                                        if (self.prefix_acl_name.is_set or self.prefix_acl_name.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.prefix_acl_name.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "lsr-id" or name == "label-space-id" or name == "prefix-acl-name"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "lsr-id"):
                                            self.lsr_id = value
                                            self.lsr_id.value_namespace = name_space
                                            self.lsr_id.value_namespace_prefix = name_space_prefix
                                        if(value_path == "label-space-id"):
                                            self.label_space_id = value
                                            self.label_space_id.value_namespace = name_space
                                            self.label_space_id.value_namespace_prefix = name_space_prefix
                                        if(value_path == "prefix-acl-name"):
                                            self.prefix_acl_name = value
                                            self.prefix_acl_name.value_namespace = name_space
                                            self.prefix_acl_name.value_namespace_prefix = name_space_prefix

                                def has_data(self):
                                    for c in self.peer_accept_policy:
                                        if (c.has_data()):
                                            return True
                                    return False

                                def has_operation(self):
                                    for c in self.peer_accept_policy:
                                        if (c.has_operation()):
                                            return True
                                    return self.yfilter != YFilter.not_set

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "peer-accept-policies" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    if (child_yang_name == "peer-accept-policy"):
                                        for c in self.peer_accept_policy:
                                            segment = c.get_segment_path()
                                            if (segment_path == segment):
                                                return c
                                        c = MplsLdp.DefaultVrf.Afs.Af.Label.Remote.Accept.PeerAcceptPolicies.PeerAcceptPolicy()
                                        c.parent = self
                                        local_reference_key = "ydk::seg::%s" % segment_path
                                        self._local_refs[local_reference_key] = c
                                        self.peer_accept_policy.append(c)
                                        return c

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "peer-accept-policy"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    pass

                            def has_data(self):
                                return (self.peer_accept_policies is not None and self.peer_accept_policies.has_data())

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    (self.peer_accept_policies is not None and self.peer_accept_policies.has_operation()))

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "accept" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                if (child_yang_name == "peer-accept-policies"):
                                    if (self.peer_accept_policies is None):
                                        self.peer_accept_policies = MplsLdp.DefaultVrf.Afs.Af.Label.Remote.Accept.PeerAcceptPolicies()
                                        self.peer_accept_policies.parent = self
                                        self._children_name_map["peer_accept_policies"] = "peer-accept-policies"
                                    return self.peer_accept_policies

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "peer-accept-policies"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                pass

                        def has_data(self):
                            return (self.accept is not None and self.accept.has_data())

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                (self.accept is not None and self.accept.has_operation()))

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "remote" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "accept"):
                                if (self.accept is None):
                                    self.accept = MplsLdp.DefaultVrf.Afs.Af.Label.Remote.Accept()
                                    self.accept.parent = self
                                    self._children_name_map["accept"] = "accept"
                                return self.accept

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "accept"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            pass


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
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(MplsLdp.DefaultVrf.Afs.Af.Label.Local, self).__init__()

                            self.yang_name = "local"
                            self.yang_parent_name = "label"

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

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("default_route",
                                            "implicit_null_override") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(MplsLdp.DefaultVrf.Afs.Af.Label.Local, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(MplsLdp.DefaultVrf.Afs.Af.Label.Local, self).__setattr__(name, value)


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
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(MplsLdp.DefaultVrf.Afs.Af.Label.Local.Advertise, self).__init__()

                                self.yang_name = "advertise"
                                self.yang_parent_name = "local"

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

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("disable") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(MplsLdp.DefaultVrf.Afs.Af.Label.Local.Advertise, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(MplsLdp.DefaultVrf.Afs.Af.Label.Local.Advertise, self).__setattr__(name, value)


                            class PeerAdvertisePolicies(Entity):
                                """
                                Configure peer centric outbound label
                                advertisement using ACL
                                
                                .. attribute:: peer_advertise_policy
                                
                                	Control advertisement of prefix(es) using ACL
                                	**type**\: list of    :py:class:`PeerAdvertisePolicy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.DefaultVrf.Afs.Af.Label.Local.Advertise.PeerAdvertisePolicies.PeerAdvertisePolicy>`
                                
                                

                                """

                                _prefix = 'mpls-ldp-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(MplsLdp.DefaultVrf.Afs.Af.Label.Local.Advertise.PeerAdvertisePolicies, self).__init__()

                                    self.yang_name = "peer-advertise-policies"
                                    self.yang_parent_name = "advertise"

                                    self.peer_advertise_policy = YList(self)

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in () and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(MplsLdp.DefaultVrf.Afs.Af.Label.Local.Advertise.PeerAdvertisePolicies, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(MplsLdp.DefaultVrf.Afs.Af.Label.Local.Advertise.PeerAdvertisePolicies, self).__setattr__(name, value)


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
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(MplsLdp.DefaultVrf.Afs.Af.Label.Local.Advertise.PeerAdvertisePolicies.PeerAdvertisePolicy, self).__init__()

                                        self.yang_name = "peer-advertise-policy"
                                        self.yang_parent_name = "peer-advertise-policies"

                                        self.lsr_id = YLeaf(YType.str, "lsr-id")

                                        self.label_space_id = YLeaf(YType.uint32, "label-space-id")

                                        self.prefix_acl_name = YLeaf(YType.str, "prefix-acl-name")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("lsr_id",
                                                        "label_space_id",
                                                        "prefix_acl_name") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(MplsLdp.DefaultVrf.Afs.Af.Label.Local.Advertise.PeerAdvertisePolicies.PeerAdvertisePolicy, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(MplsLdp.DefaultVrf.Afs.Af.Label.Local.Advertise.PeerAdvertisePolicies.PeerAdvertisePolicy, self).__setattr__(name, value)

                                    def has_data(self):
                                        return (
                                            self.lsr_id.is_set or
                                            self.label_space_id.is_set or
                                            self.prefix_acl_name.is_set)

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.lsr_id.yfilter != YFilter.not_set or
                                            self.label_space_id.yfilter != YFilter.not_set or
                                            self.prefix_acl_name.yfilter != YFilter.not_set)

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "peer-advertise-policy" + "[lsr-id='" + self.lsr_id.get() + "']" + "[label-space-id='" + self.label_space_id.get() + "']" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()
                                        if (self.lsr_id.is_set or self.lsr_id.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.lsr_id.get_name_leafdata())
                                        if (self.label_space_id.is_set or self.label_space_id.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.label_space_id.get_name_leafdata())
                                        if (self.prefix_acl_name.is_set or self.prefix_acl_name.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.prefix_acl_name.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "lsr-id" or name == "label-space-id" or name == "prefix-acl-name"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "lsr-id"):
                                            self.lsr_id = value
                                            self.lsr_id.value_namespace = name_space
                                            self.lsr_id.value_namespace_prefix = name_space_prefix
                                        if(value_path == "label-space-id"):
                                            self.label_space_id = value
                                            self.label_space_id.value_namespace = name_space
                                            self.label_space_id.value_namespace_prefix = name_space_prefix
                                        if(value_path == "prefix-acl-name"):
                                            self.prefix_acl_name = value
                                            self.prefix_acl_name.value_namespace = name_space
                                            self.prefix_acl_name.value_namespace_prefix = name_space_prefix

                                def has_data(self):
                                    for c in self.peer_advertise_policy:
                                        if (c.has_data()):
                                            return True
                                    return False

                                def has_operation(self):
                                    for c in self.peer_advertise_policy:
                                        if (c.has_operation()):
                                            return True
                                    return self.yfilter != YFilter.not_set

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "peer-advertise-policies" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    if (child_yang_name == "peer-advertise-policy"):
                                        for c in self.peer_advertise_policy:
                                            segment = c.get_segment_path()
                                            if (segment_path == segment):
                                                return c
                                        c = MplsLdp.DefaultVrf.Afs.Af.Label.Local.Advertise.PeerAdvertisePolicies.PeerAdvertisePolicy()
                                        c.parent = self
                                        local_reference_key = "ydk::seg::%s" % segment_path
                                        self._local_refs[local_reference_key] = c
                                        self.peer_advertise_policy.append(c)
                                        return c

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "peer-advertise-policy"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    pass


                            class PrefixAdvertisePolicies(Entity):
                                """
                                Configure prefix centric outbound label
                                advertisement using ACL
                                
                                .. attribute:: prefix_advertise_policy
                                
                                	Control advertisement of prefix(es) using ACL
                                	**type**\: list of    :py:class:`PrefixAdvertisePolicy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.DefaultVrf.Afs.Af.Label.Local.Advertise.PrefixAdvertisePolicies.PrefixAdvertisePolicy>`
                                
                                

                                """

                                _prefix = 'mpls-ldp-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(MplsLdp.DefaultVrf.Afs.Af.Label.Local.Advertise.PrefixAdvertisePolicies, self).__init__()

                                    self.yang_name = "prefix-advertise-policies"
                                    self.yang_parent_name = "advertise"

                                    self.prefix_advertise_policy = YList(self)

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in () and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(MplsLdp.DefaultVrf.Afs.Af.Label.Local.Advertise.PrefixAdvertisePolicies, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(MplsLdp.DefaultVrf.Afs.Af.Label.Local.Advertise.PrefixAdvertisePolicies, self).__setattr__(name, value)


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
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(MplsLdp.DefaultVrf.Afs.Af.Label.Local.Advertise.PrefixAdvertisePolicies.PrefixAdvertisePolicy, self).__init__()

                                        self.yang_name = "prefix-advertise-policy"
                                        self.yang_parent_name = "prefix-advertise-policies"

                                        self.prefix_acl_name = YLeaf(YType.str, "prefix-acl-name")

                                        self.advertise_type = YLeaf(YType.enumeration, "advertise-type")

                                        self.peer_acl_name = YLeaf(YType.str, "peer-acl-name")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("prefix_acl_name",
                                                        "advertise_type",
                                                        "peer_acl_name") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(MplsLdp.DefaultVrf.Afs.Af.Label.Local.Advertise.PrefixAdvertisePolicies.PrefixAdvertisePolicy, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(MplsLdp.DefaultVrf.Afs.Af.Label.Local.Advertise.PrefixAdvertisePolicies.PrefixAdvertisePolicy, self).__setattr__(name, value)

                                    def has_data(self):
                                        return (
                                            self.prefix_acl_name.is_set or
                                            self.advertise_type.is_set or
                                            self.peer_acl_name.is_set)

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.prefix_acl_name.yfilter != YFilter.not_set or
                                            self.advertise_type.yfilter != YFilter.not_set or
                                            self.peer_acl_name.yfilter != YFilter.not_set)

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "prefix-advertise-policy" + "[prefix-acl-name='" + self.prefix_acl_name.get() + "']" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()
                                        if (self.prefix_acl_name.is_set or self.prefix_acl_name.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.prefix_acl_name.get_name_leafdata())
                                        if (self.advertise_type.is_set or self.advertise_type.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.advertise_type.get_name_leafdata())
                                        if (self.peer_acl_name.is_set or self.peer_acl_name.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.peer_acl_name.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "prefix-acl-name" or name == "advertise-type" or name == "peer-acl-name"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "prefix-acl-name"):
                                            self.prefix_acl_name = value
                                            self.prefix_acl_name.value_namespace = name_space
                                            self.prefix_acl_name.value_namespace_prefix = name_space_prefix
                                        if(value_path == "advertise-type"):
                                            self.advertise_type = value
                                            self.advertise_type.value_namespace = name_space
                                            self.advertise_type.value_namespace_prefix = name_space_prefix
                                        if(value_path == "peer-acl-name"):
                                            self.peer_acl_name = value
                                            self.peer_acl_name.value_namespace = name_space
                                            self.peer_acl_name.value_namespace_prefix = name_space_prefix

                                def has_data(self):
                                    for c in self.prefix_advertise_policy:
                                        if (c.has_data()):
                                            return True
                                    return False

                                def has_operation(self):
                                    for c in self.prefix_advertise_policy:
                                        if (c.has_operation()):
                                            return True
                                    return self.yfilter != YFilter.not_set

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "prefix-advertise-policies" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    if (child_yang_name == "prefix-advertise-policy"):
                                        for c in self.prefix_advertise_policy:
                                            segment = c.get_segment_path()
                                            if (segment_path == segment):
                                                return c
                                        c = MplsLdp.DefaultVrf.Afs.Af.Label.Local.Advertise.PrefixAdvertisePolicies.PrefixAdvertisePolicy()
                                        c.parent = self
                                        local_reference_key = "ydk::seg::%s" % segment_path
                                        self._local_refs[local_reference_key] = c
                                        self.prefix_advertise_policy.append(c)
                                        return c

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "prefix-advertise-policy"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    pass


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
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(MplsLdp.DefaultVrf.Afs.Af.Label.Local.Advertise.ExplicitNull, self).__init__()

                                    self.yang_name = "explicit-null"
                                    self.yang_parent_name = "advertise"

                                    self.explicit_null_type = YLeaf(YType.enumeration, "explicit-null-type")

                                    self.peer_acl_name = YLeaf(YType.str, "peer-acl-name")

                                    self.prefix_acl_name = YLeaf(YType.str, "prefix-acl-name")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("explicit_null_type",
                                                    "peer_acl_name",
                                                    "prefix_acl_name") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(MplsLdp.DefaultVrf.Afs.Af.Label.Local.Advertise.ExplicitNull, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(MplsLdp.DefaultVrf.Afs.Af.Label.Local.Advertise.ExplicitNull, self).__setattr__(name, value)

                                def has_data(self):
                                    return (
                                        self.explicit_null_type.is_set or
                                        self.peer_acl_name.is_set or
                                        self.prefix_acl_name.is_set)

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.explicit_null_type.yfilter != YFilter.not_set or
                                        self.peer_acl_name.yfilter != YFilter.not_set or
                                        self.prefix_acl_name.yfilter != YFilter.not_set)

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "explicit-null" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.explicit_null_type.is_set or self.explicit_null_type.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.explicit_null_type.get_name_leafdata())
                                    if (self.peer_acl_name.is_set or self.peer_acl_name.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.peer_acl_name.get_name_leafdata())
                                    if (self.prefix_acl_name.is_set or self.prefix_acl_name.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.prefix_acl_name.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "explicit-null-type" or name == "peer-acl-name" or name == "prefix-acl-name"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "explicit-null-type"):
                                        self.explicit_null_type = value
                                        self.explicit_null_type.value_namespace = name_space
                                        self.explicit_null_type.value_namespace_prefix = name_space_prefix
                                    if(value_path == "peer-acl-name"):
                                        self.peer_acl_name = value
                                        self.peer_acl_name.value_namespace = name_space
                                        self.peer_acl_name.value_namespace_prefix = name_space_prefix
                                    if(value_path == "prefix-acl-name"):
                                        self.prefix_acl_name = value
                                        self.prefix_acl_name.value_namespace = name_space
                                        self.prefix_acl_name.value_namespace_prefix = name_space_prefix


                            class Interfaces(Entity):
                                """
                                Configure outbound label advertisement for
                                an interface
                                
                                .. attribute:: interface
                                
                                	Control advertisement of interface's host IP address
                                	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.DefaultVrf.Afs.Af.Label.Local.Advertise.Interfaces.Interface>`
                                
                                

                                """

                                _prefix = 'mpls-ldp-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(MplsLdp.DefaultVrf.Afs.Af.Label.Local.Advertise.Interfaces, self).__init__()

                                    self.yang_name = "interfaces"
                                    self.yang_parent_name = "advertise"

                                    self.interface = YList(self)

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in () and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(MplsLdp.DefaultVrf.Afs.Af.Label.Local.Advertise.Interfaces, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(MplsLdp.DefaultVrf.Afs.Af.Label.Local.Advertise.Interfaces, self).__setattr__(name, value)


                                class Interface(Entity):
                                    """
                                    Control advertisement of interface's host
                                    IP address
                                    
                                    .. attribute:: interface_name  <key>
                                    
                                    	Name of interface
                                    	**type**\:  str
                                    
                                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                                    
                                    

                                    """

                                    _prefix = 'mpls-ldp-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(MplsLdp.DefaultVrf.Afs.Af.Label.Local.Advertise.Interfaces.Interface, self).__init__()

                                        self.yang_name = "interface"
                                        self.yang_parent_name = "interfaces"

                                        self.interface_name = YLeaf(YType.str, "interface-name")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("interface_name") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(MplsLdp.DefaultVrf.Afs.Af.Label.Local.Advertise.Interfaces.Interface, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(MplsLdp.DefaultVrf.Afs.Af.Label.Local.Advertise.Interfaces.Interface, self).__setattr__(name, value)

                                    def has_data(self):
                                        return self.interface_name.is_set

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.interface_name.yfilter != YFilter.not_set)

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "interface" + "[interface-name='" + self.interface_name.get() + "']" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()
                                        if (self.interface_name.is_set or self.interface_name.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.interface_name.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "interface-name"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "interface-name"):
                                            self.interface_name = value
                                            self.interface_name.value_namespace = name_space
                                            self.interface_name.value_namespace_prefix = name_space_prefix

                                def has_data(self):
                                    for c in self.interface:
                                        if (c.has_data()):
                                            return True
                                    return False

                                def has_operation(self):
                                    for c in self.interface:
                                        if (c.has_operation()):
                                            return True
                                    return self.yfilter != YFilter.not_set

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "interfaces" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    if (child_yang_name == "interface"):
                                        for c in self.interface:
                                            segment = c.get_segment_path()
                                            if (segment_path == segment):
                                                return c
                                        c = MplsLdp.DefaultVrf.Afs.Af.Label.Local.Advertise.Interfaces.Interface()
                                        c.parent = self
                                        local_reference_key = "ydk::seg::%s" % segment_path
                                        self._local_refs[local_reference_key] = c
                                        self.interface.append(c)
                                        return c

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "interface"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    pass

                            def has_data(self):
                                return (
                                    self.disable.is_set or
                                    (self.explicit_null is not None and self.explicit_null.has_data()) or
                                    (self.interfaces is not None and self.interfaces.has_data()) or
                                    (self.peer_advertise_policies is not None and self.peer_advertise_policies.has_data()) or
                                    (self.prefix_advertise_policies is not None and self.prefix_advertise_policies.has_data()))

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.disable.yfilter != YFilter.not_set or
                                    (self.explicit_null is not None and self.explicit_null.has_operation()) or
                                    (self.interfaces is not None and self.interfaces.has_operation()) or
                                    (self.peer_advertise_policies is not None and self.peer_advertise_policies.has_operation()) or
                                    (self.prefix_advertise_policies is not None and self.prefix_advertise_policies.has_operation()))

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "advertise" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.disable.is_set or self.disable.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.disable.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                if (child_yang_name == "explicit-null"):
                                    if (self.explicit_null is None):
                                        self.explicit_null = MplsLdp.DefaultVrf.Afs.Af.Label.Local.Advertise.ExplicitNull()
                                        self.explicit_null.parent = self
                                        self._children_name_map["explicit_null"] = "explicit-null"
                                    return self.explicit_null

                                if (child_yang_name == "interfaces"):
                                    if (self.interfaces is None):
                                        self.interfaces = MplsLdp.DefaultVrf.Afs.Af.Label.Local.Advertise.Interfaces()
                                        self.interfaces.parent = self
                                        self._children_name_map["interfaces"] = "interfaces"
                                    return self.interfaces

                                if (child_yang_name == "peer-advertise-policies"):
                                    if (self.peer_advertise_policies is None):
                                        self.peer_advertise_policies = MplsLdp.DefaultVrf.Afs.Af.Label.Local.Advertise.PeerAdvertisePolicies()
                                        self.peer_advertise_policies.parent = self
                                        self._children_name_map["peer_advertise_policies"] = "peer-advertise-policies"
                                    return self.peer_advertise_policies

                                if (child_yang_name == "prefix-advertise-policies"):
                                    if (self.prefix_advertise_policies is None):
                                        self.prefix_advertise_policies = MplsLdp.DefaultVrf.Afs.Af.Label.Local.Advertise.PrefixAdvertisePolicies()
                                        self.prefix_advertise_policies.parent = self
                                        self._children_name_map["prefix_advertise_policies"] = "prefix-advertise-policies"
                                    return self.prefix_advertise_policies

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "explicit-null" or name == "interfaces" or name == "peer-advertise-policies" or name == "prefix-advertise-policies" or name == "disable"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "disable"):
                                    self.disable = value
                                    self.disable.value_namespace = name_space
                                    self.disable.value_namespace_prefix = name_space_prefix


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
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(MplsLdp.DefaultVrf.Afs.Af.Label.Local.Allocate, self).__init__()

                                self.yang_name = "allocate"
                                self.yang_parent_name = "local"

                                self.allocation_type = YLeaf(YType.enumeration, "allocation-type")

                                self.prefix_acl_name = YLeaf(YType.str, "prefix-acl-name")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("allocation_type",
                                                "prefix_acl_name") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(MplsLdp.DefaultVrf.Afs.Af.Label.Local.Allocate, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(MplsLdp.DefaultVrf.Afs.Af.Label.Local.Allocate, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.allocation_type.is_set or
                                    self.prefix_acl_name.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.allocation_type.yfilter != YFilter.not_set or
                                    self.prefix_acl_name.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "allocate" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.allocation_type.is_set or self.allocation_type.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.allocation_type.get_name_leafdata())
                                if (self.prefix_acl_name.is_set or self.prefix_acl_name.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.prefix_acl_name.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "allocation-type" or name == "prefix-acl-name"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "allocation-type"):
                                    self.allocation_type = value
                                    self.allocation_type.value_namespace = name_space
                                    self.allocation_type.value_namespace_prefix = name_space_prefix
                                if(value_path == "prefix-acl-name"):
                                    self.prefix_acl_name = value
                                    self.prefix_acl_name.value_namespace = name_space
                                    self.prefix_acl_name.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            return (
                                self.default_route.is_set or
                                self.implicit_null_override.is_set or
                                (self.advertise is not None and self.advertise.has_data()) or
                                (self.allocate is not None and self.allocate.has_data()))

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.default_route.yfilter != YFilter.not_set or
                                self.implicit_null_override.yfilter != YFilter.not_set or
                                (self.advertise is not None and self.advertise.has_operation()) or
                                (self.allocate is not None and self.allocate.has_operation()))

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "local" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.default_route.is_set or self.default_route.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.default_route.get_name_leafdata())
                            if (self.implicit_null_override.is_set or self.implicit_null_override.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.implicit_null_override.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "advertise"):
                                if (self.advertise is None):
                                    self.advertise = MplsLdp.DefaultVrf.Afs.Af.Label.Local.Advertise()
                                    self.advertise.parent = self
                                    self._children_name_map["advertise"] = "advertise"
                                return self.advertise

                            if (child_yang_name == "allocate"):
                                if (self.allocate is None):
                                    self.allocate = MplsLdp.DefaultVrf.Afs.Af.Label.Local.Allocate()
                                    self.allocate.parent = self
                                    self._children_name_map["allocate"] = "allocate"
                                return self.allocate

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "advertise" or name == "allocate" or name == "default-route" or name == "implicit-null-override"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "default-route"):
                                self.default_route = value
                                self.default_route.value_namespace = name_space
                                self.default_route.value_namespace_prefix = name_space_prefix
                            if(value_path == "implicit-null-override"):
                                self.implicit_null_override = value
                                self.implicit_null_override.value_namespace = name_space
                                self.implicit_null_override.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        return (
                            (self.local is not None and self.local.has_data()) or
                            (self.remote is not None and self.remote.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            (self.local is not None and self.local.has_operation()) or
                            (self.remote is not None and self.remote.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "label" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "local"):
                            if (self.local is None):
                                self.local = MplsLdp.DefaultVrf.Afs.Af.Label.Local()
                                self.local.parent = self
                                self._children_name_map["local"] = "local"
                            return self.local

                        if (child_yang_name == "remote"):
                            if (self.remote is None):
                                self.remote = MplsLdp.DefaultVrf.Afs.Af.Label.Remote()
                                self.remote.parent = self
                                self._children_name_map["remote"] = "remote"
                            return self.remote

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "local" or name == "remote"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass


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
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(MplsLdp.DefaultVrf.Afs.Af.Discovery, self).__init__()

                        self.yang_name = "discovery"
                        self.yang_parent_name = "af"

                        self.transport_address = YLeaf(YType.str, "transport-address")

                        self.targeted_hello_accept = MplsLdp.DefaultVrf.Afs.Af.Discovery.TargetedHelloAccept()
                        self.targeted_hello_accept.parent = self
                        self._children_name_map["targeted_hello_accept"] = "targeted-hello-accept"
                        self._children_yang_names.add("targeted-hello-accept")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("transport_address") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(MplsLdp.DefaultVrf.Afs.Af.Discovery, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(MplsLdp.DefaultVrf.Afs.Af.Discovery, self).__setattr__(name, value)


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
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(MplsLdp.DefaultVrf.Afs.Af.Discovery.TargetedHelloAccept, self).__init__()

                            self.yang_name = "targeted-hello-accept"
                            self.yang_parent_name = "discovery"

                            self.accept_type = YLeaf(YType.enumeration, "accept-type")

                            self.peer_acl_name = YLeaf(YType.str, "peer-acl-name")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("accept_type",
                                            "peer_acl_name") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(MplsLdp.DefaultVrf.Afs.Af.Discovery.TargetedHelloAccept, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(MplsLdp.DefaultVrf.Afs.Af.Discovery.TargetedHelloAccept, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.accept_type.is_set or
                                self.peer_acl_name.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.accept_type.yfilter != YFilter.not_set or
                                self.peer_acl_name.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "targeted-hello-accept" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.accept_type.is_set or self.accept_type.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.accept_type.get_name_leafdata())
                            if (self.peer_acl_name.is_set or self.peer_acl_name.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.peer_acl_name.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "accept-type" or name == "peer-acl-name"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "accept-type"):
                                self.accept_type = value
                                self.accept_type.value_namespace = name_space
                                self.accept_type.value_namespace_prefix = name_space_prefix
                            if(value_path == "peer-acl-name"):
                                self.peer_acl_name = value
                                self.peer_acl_name.value_namespace = name_space
                                self.peer_acl_name.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        return (
                            self.transport_address.is_set or
                            (self.targeted_hello_accept is not None and self.targeted_hello_accept.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.transport_address.yfilter != YFilter.not_set or
                            (self.targeted_hello_accept is not None and self.targeted_hello_accept.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "discovery" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.transport_address.is_set or self.transport_address.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.transport_address.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "targeted-hello-accept"):
                            if (self.targeted_hello_accept is None):
                                self.targeted_hello_accept = MplsLdp.DefaultVrf.Afs.Af.Discovery.TargetedHelloAccept()
                                self.targeted_hello_accept.parent = self
                                self._children_name_map["targeted_hello_accept"] = "targeted-hello-accept"
                            return self.targeted_hello_accept

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "targeted-hello-accept" or name == "transport-address"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "transport-address"):
                            self.transport_address = value
                            self.transport_address.value_namespace = name_space
                            self.transport_address.value_namespace_prefix = name_space_prefix


                class TrafficEngineering(Entity):
                    """
                    MPLS Traffic Engingeering parameters for LDP
                    
                    .. attribute:: auto_tunnel_mesh
                    
                    	MPLS Traffic Engineering auto\-tunnel mesh parameters for LDP
                    	**type**\:   :py:class:`AutoTunnelMesh <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.DefaultVrf.Afs.Af.TrafficEngineering.AutoTunnelMesh>`
                    
                    

                    """

                    _prefix = 'mpls-ldp-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(MplsLdp.DefaultVrf.Afs.Af.TrafficEngineering, self).__init__()

                        self.yang_name = "traffic-engineering"
                        self.yang_parent_name = "af"

                        self.auto_tunnel_mesh = MplsLdp.DefaultVrf.Afs.Af.TrafficEngineering.AutoTunnelMesh()
                        self.auto_tunnel_mesh.parent = self
                        self._children_name_map["auto_tunnel_mesh"] = "auto-tunnel-mesh"
                        self._children_yang_names.add("auto-tunnel-mesh")


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
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(MplsLdp.DefaultVrf.Afs.Af.TrafficEngineering.AutoTunnelMesh, self).__init__()

                            self.yang_name = "auto-tunnel-mesh"
                            self.yang_parent_name = "traffic-engineering"

                            self.group_all = YLeaf(YType.empty, "group-all")

                            self.group_ids = MplsLdp.DefaultVrf.Afs.Af.TrafficEngineering.AutoTunnelMesh.GroupIds()
                            self.group_ids.parent = self
                            self._children_name_map["group_ids"] = "group-ids"
                            self._children_yang_names.add("group-ids")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("group_all") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(MplsLdp.DefaultVrf.Afs.Af.TrafficEngineering.AutoTunnelMesh, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(MplsLdp.DefaultVrf.Afs.Af.TrafficEngineering.AutoTunnelMesh, self).__setattr__(name, value)


                        class GroupIds(Entity):
                            """
                            Enable interfaces in specific MPLS TE
                            auto\-tunnel mesh\-groups
                            
                            .. attribute:: group_id
                            
                            	Auto\-mesh group identifier to enable
                            	**type**\: list of    :py:class:`GroupId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.DefaultVrf.Afs.Af.TrafficEngineering.AutoTunnelMesh.GroupIds.GroupId>`
                            
                            

                            """

                            _prefix = 'mpls-ldp-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(MplsLdp.DefaultVrf.Afs.Af.TrafficEngineering.AutoTunnelMesh.GroupIds, self).__init__()

                                self.yang_name = "group-ids"
                                self.yang_parent_name = "auto-tunnel-mesh"

                                self.group_id = YList(self)

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in () and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(MplsLdp.DefaultVrf.Afs.Af.TrafficEngineering.AutoTunnelMesh.GroupIds, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(MplsLdp.DefaultVrf.Afs.Af.TrafficEngineering.AutoTunnelMesh.GroupIds, self).__setattr__(name, value)


                            class GroupId(Entity):
                                """
                                Auto\-mesh group identifier to enable
                                
                                .. attribute:: mesh_group_id  <key>
                                
                                	Mesh group ID
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'mpls-ldp-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(MplsLdp.DefaultVrf.Afs.Af.TrafficEngineering.AutoTunnelMesh.GroupIds.GroupId, self).__init__()

                                    self.yang_name = "group-id"
                                    self.yang_parent_name = "group-ids"

                                    self.mesh_group_id = YLeaf(YType.uint32, "mesh-group-id")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("mesh_group_id") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(MplsLdp.DefaultVrf.Afs.Af.TrafficEngineering.AutoTunnelMesh.GroupIds.GroupId, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(MplsLdp.DefaultVrf.Afs.Af.TrafficEngineering.AutoTunnelMesh.GroupIds.GroupId, self).__setattr__(name, value)

                                def has_data(self):
                                    return self.mesh_group_id.is_set

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.mesh_group_id.yfilter != YFilter.not_set)

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "group-id" + "[mesh-group-id='" + self.mesh_group_id.get() + "']" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.mesh_group_id.is_set or self.mesh_group_id.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.mesh_group_id.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "mesh-group-id"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "mesh-group-id"):
                                        self.mesh_group_id = value
                                        self.mesh_group_id.value_namespace = name_space
                                        self.mesh_group_id.value_namespace_prefix = name_space_prefix

                            def has_data(self):
                                for c in self.group_id:
                                    if (c.has_data()):
                                        return True
                                return False

                            def has_operation(self):
                                for c in self.group_id:
                                    if (c.has_operation()):
                                        return True
                                return self.yfilter != YFilter.not_set

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "group-ids" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                if (child_yang_name == "group-id"):
                                    for c in self.group_id:
                                        segment = c.get_segment_path()
                                        if (segment_path == segment):
                                            return c
                                    c = MplsLdp.DefaultVrf.Afs.Af.TrafficEngineering.AutoTunnelMesh.GroupIds.GroupId()
                                    c.parent = self
                                    local_reference_key = "ydk::seg::%s" % segment_path
                                    self._local_refs[local_reference_key] = c
                                    self.group_id.append(c)
                                    return c

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "group-id"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                pass

                        def has_data(self):
                            return (
                                self.group_all.is_set or
                                (self.group_ids is not None and self.group_ids.has_data()))

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.group_all.yfilter != YFilter.not_set or
                                (self.group_ids is not None and self.group_ids.has_operation()))

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "auto-tunnel-mesh" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.group_all.is_set or self.group_all.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.group_all.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "group-ids"):
                                if (self.group_ids is None):
                                    self.group_ids = MplsLdp.DefaultVrf.Afs.Af.TrafficEngineering.AutoTunnelMesh.GroupIds()
                                    self.group_ids.parent = self
                                    self._children_name_map["group_ids"] = "group-ids"
                                return self.group_ids

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "group-ids" or name == "group-all"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "group-all"):
                                self.group_all = value
                                self.group_all.value_namespace = name_space
                                self.group_all.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        return (self.auto_tunnel_mesh is not None and self.auto_tunnel_mesh.has_data())

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            (self.auto_tunnel_mesh is not None and self.auto_tunnel_mesh.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "traffic-engineering" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "auto-tunnel-mesh"):
                            if (self.auto_tunnel_mesh is None):
                                self.auto_tunnel_mesh = MplsLdp.DefaultVrf.Afs.Af.TrafficEngineering.AutoTunnelMesh()
                                self.auto_tunnel_mesh.parent = self
                                self._children_name_map["auto_tunnel_mesh"] = "auto-tunnel-mesh"
                            return self.auto_tunnel_mesh

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "auto-tunnel-mesh"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass


                class Neighbor(Entity):
                    """
                    Configuration related to Neighbors
                    
                    .. attribute:: addresses
                    
                    	Configuration related to neighbors using neighbor address
                    	**type**\:   :py:class:`Addresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.DefaultVrf.Afs.Af.Neighbor.Addresses>`
                    
                    

                    """

                    _prefix = 'mpls-ldp-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(MplsLdp.DefaultVrf.Afs.Af.Neighbor, self).__init__()

                        self.yang_name = "neighbor"
                        self.yang_parent_name = "af"

                        self.addresses = MplsLdp.DefaultVrf.Afs.Af.Neighbor.Addresses()
                        self.addresses.parent = self
                        self._children_name_map["addresses"] = "addresses"
                        self._children_yang_names.add("addresses")


                    class Addresses(Entity):
                        """
                        Configuration related to neighbors using
                        neighbor address
                        
                        .. attribute:: address
                        
                        	IP address based configuration related to a neighbor
                        	**type**\: list of    :py:class:`Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.DefaultVrf.Afs.Af.Neighbor.Addresses.Address>`
                        
                        

                        """

                        _prefix = 'mpls-ldp-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(MplsLdp.DefaultVrf.Afs.Af.Neighbor.Addresses, self).__init__()

                            self.yang_name = "addresses"
                            self.yang_parent_name = "neighbor"

                            self.address = YList(self)

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in () and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(MplsLdp.DefaultVrf.Afs.Af.Neighbor.Addresses, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(MplsLdp.DefaultVrf.Afs.Af.Neighbor.Addresses, self).__setattr__(name, value)


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
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(MplsLdp.DefaultVrf.Afs.Af.Neighbor.Addresses.Address, self).__init__()

                                self.yang_name = "address"
                                self.yang_parent_name = "addresses"

                                self.ip_address = YLeaf(YType.str, "ip-address")

                                self.targeted = YLeaf(YType.empty, "targeted")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("ip_address",
                                                "targeted") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(MplsLdp.DefaultVrf.Afs.Af.Neighbor.Addresses.Address, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(MplsLdp.DefaultVrf.Afs.Af.Neighbor.Addresses.Address, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.ip_address.is_set or
                                    self.targeted.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.ip_address.yfilter != YFilter.not_set or
                                    self.targeted.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "address" + "[ip-address='" + self.ip_address.get() + "']" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.ip_address.is_set or self.ip_address.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.ip_address.get_name_leafdata())
                                if (self.targeted.is_set or self.targeted.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.targeted.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "ip-address" or name == "targeted"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "ip-address"):
                                    self.ip_address = value
                                    self.ip_address.value_namespace = name_space
                                    self.ip_address.value_namespace_prefix = name_space_prefix
                                if(value_path == "targeted"):
                                    self.targeted = value
                                    self.targeted.value_namespace = name_space
                                    self.targeted.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            for c in self.address:
                                if (c.has_data()):
                                    return True
                            return False

                        def has_operation(self):
                            for c in self.address:
                                if (c.has_operation()):
                                    return True
                            return self.yfilter != YFilter.not_set

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "addresses" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "address"):
                                for c in self.address:
                                    segment = c.get_segment_path()
                                    if (segment_path == segment):
                                        return c
                                c = MplsLdp.DefaultVrf.Afs.Af.Neighbor.Addresses.Address()
                                c.parent = self
                                local_reference_key = "ydk::seg::%s" % segment_path
                                self._local_refs[local_reference_key] = c
                                self.address.append(c)
                                return c

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "address"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            pass

                    def has_data(self):
                        return (self.addresses is not None and self.addresses.has_data())

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            (self.addresses is not None and self.addresses.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "neighbor" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "addresses"):
                            if (self.addresses is None):
                                self.addresses = MplsLdp.DefaultVrf.Afs.Af.Neighbor.Addresses()
                                self.addresses.parent = self
                                self._children_name_map["addresses"] = "addresses"
                            return self.addresses

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "addresses"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass


                class RedistributionProtocol(Entity):
                    """
                    MPLS LDP configuration for protocol
                    redistribution
                    
                    .. attribute:: bgp
                    
                    	MPLS LDP configuration for protocol redistribution
                    	**type**\:   :py:class:`Bgp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.DefaultVrf.Afs.Af.RedistributionProtocol.Bgp>`
                    
                    

                    """

                    _prefix = 'mpls-ldp-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(MplsLdp.DefaultVrf.Afs.Af.RedistributionProtocol, self).__init__()

                        self.yang_name = "redistribution-protocol"
                        self.yang_parent_name = "af"

                        self.bgp = MplsLdp.DefaultVrf.Afs.Af.RedistributionProtocol.Bgp()
                        self.bgp.parent = self
                        self._children_name_map["bgp"] = "bgp"
                        self._children_yang_names.add("bgp")


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
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(MplsLdp.DefaultVrf.Afs.Af.RedistributionProtocol.Bgp, self).__init__()

                            self.yang_name = "bgp"
                            self.yang_parent_name = "redistribution-protocol"

                            self.advertise_to = MplsLdp.DefaultVrf.Afs.Af.RedistributionProtocol.Bgp.AdvertiseTo()
                            self.advertise_to.parent = self
                            self._children_name_map["advertise_to"] = "advertise-to"
                            self._children_yang_names.add("advertise-to")

                            self.as_ = MplsLdp.DefaultVrf.Afs.Af.RedistributionProtocol.Bgp.As_()
                            self.as_.parent = self
                            self._children_name_map["as_"] = "as"
                            self._children_yang_names.add("as")


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
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(MplsLdp.DefaultVrf.Afs.Af.RedistributionProtocol.Bgp.As_, self).__init__()

                                self.yang_name = "as"
                                self.yang_parent_name = "bgp"

                                self.as_xx = YLeaf(YType.uint32, "as-xx")

                                self.as_yy = YLeaf(YType.uint32, "as-yy")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("as_xx",
                                                "as_yy") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(MplsLdp.DefaultVrf.Afs.Af.RedistributionProtocol.Bgp.As_, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(MplsLdp.DefaultVrf.Afs.Af.RedistributionProtocol.Bgp.As_, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.as_xx.is_set or
                                    self.as_yy.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.as_xx.yfilter != YFilter.not_set or
                                    self.as_yy.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "as" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.as_xx.is_set or self.as_xx.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.as_xx.get_name_leafdata())
                                if (self.as_yy.is_set or self.as_yy.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.as_yy.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "as-xx" or name == "as-yy"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "as-xx"):
                                    self.as_xx = value
                                    self.as_xx.value_namespace = name_space
                                    self.as_xx.value_namespace_prefix = name_space_prefix
                                if(value_path == "as-yy"):
                                    self.as_yy = value
                                    self.as_yy.value_namespace = name_space
                                    self.as_yy.value_namespace_prefix = name_space_prefix


                        class AdvertiseTo(Entity):
                            """
                            ACL containing list of neighbors for BGP
                            route redistribution
                            
                            .. attribute:: peer_acl_name
                            
                            	Name of peer ACL
                            	**type**\:  str
                            
                            .. attribute:: type
                            
                            	advertise to peer acl type
                            	**type**\:   :py:class:`MplsLdpAdvertiseBgpacl <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdpAdvertiseBgpacl>`
                            
                            

                            """

                            _prefix = 'mpls-ldp-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(MplsLdp.DefaultVrf.Afs.Af.RedistributionProtocol.Bgp.AdvertiseTo, self).__init__()

                                self.yang_name = "advertise-to"
                                self.yang_parent_name = "bgp"

                                self.peer_acl_name = YLeaf(YType.str, "peer-acl-name")

                                self.type = YLeaf(YType.enumeration, "type")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("peer_acl_name",
                                                "type") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(MplsLdp.DefaultVrf.Afs.Af.RedistributionProtocol.Bgp.AdvertiseTo, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(MplsLdp.DefaultVrf.Afs.Af.RedistributionProtocol.Bgp.AdvertiseTo, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.peer_acl_name.is_set or
                                    self.type.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.peer_acl_name.yfilter != YFilter.not_set or
                                    self.type.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "advertise-to" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.peer_acl_name.is_set or self.peer_acl_name.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.peer_acl_name.get_name_leafdata())
                                if (self.type.is_set or self.type.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.type.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "peer-acl-name" or name == "type"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "peer-acl-name"):
                                    self.peer_acl_name = value
                                    self.peer_acl_name.value_namespace = name_space
                                    self.peer_acl_name.value_namespace_prefix = name_space_prefix
                                if(value_path == "type"):
                                    self.type = value
                                    self.type.value_namespace = name_space
                                    self.type.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            return (
                                (self.advertise_to is not None and self.advertise_to.has_data()) or
                                (self.as_ is not None and self.as_.has_data()))

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                (self.advertise_to is not None and self.advertise_to.has_operation()) or
                                (self.as_ is not None and self.as_.has_operation()))

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "bgp" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "advertise-to"):
                                if (self.advertise_to is None):
                                    self.advertise_to = MplsLdp.DefaultVrf.Afs.Af.RedistributionProtocol.Bgp.AdvertiseTo()
                                    self.advertise_to.parent = self
                                    self._children_name_map["advertise_to"] = "advertise-to"
                                return self.advertise_to

                            if (child_yang_name == "as"):
                                if (self.as_ is None):
                                    self.as_ = MplsLdp.DefaultVrf.Afs.Af.RedistributionProtocol.Bgp.As_()
                                    self.as_.parent = self
                                    self._children_name_map["as_"] = "as"
                                return self.as_

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "advertise-to" or name == "as"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            pass

                    def has_data(self):
                        return (self.bgp is not None and self.bgp.has_data())

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            (self.bgp is not None and self.bgp.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "redistribution-protocol" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "bgp"):
                            if (self.bgp is None):
                                self.bgp = MplsLdp.DefaultVrf.Afs.Af.RedistributionProtocol.Bgp()
                                self.bgp.parent = self
                                self._children_name_map["bgp"] = "bgp"
                            return self.bgp

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "bgp"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass

                def has_data(self):
                    return (
                        self.af_name.is_set or
                        self.enable.is_set or
                        (self.discovery is not None and self.discovery.has_data()) or
                        (self.label is not None and self.label.has_data()) or
                        (self.neighbor is not None and self.neighbor.has_data()) or
                        (self.redistribution_protocol is not None and self.redistribution_protocol.has_data()) or
                        (self.traffic_engineering is not None and self.traffic_engineering.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.af_name.yfilter != YFilter.not_set or
                        self.enable.yfilter != YFilter.not_set or
                        (self.discovery is not None and self.discovery.has_operation()) or
                        (self.label is not None and self.label.has_operation()) or
                        (self.neighbor is not None and self.neighbor.has_operation()) or
                        (self.redistribution_protocol is not None and self.redistribution_protocol.has_operation()) or
                        (self.traffic_engineering is not None and self.traffic_engineering.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "af" + "[af-name='" + self.af_name.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-mpls-ldp-cfg:mpls-ldp/default-vrf/afs/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.af_name.is_set or self.af_name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.af_name.get_name_leafdata())
                    if (self.enable.is_set or self.enable.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.enable.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "discovery"):
                        if (self.discovery is None):
                            self.discovery = MplsLdp.DefaultVrf.Afs.Af.Discovery()
                            self.discovery.parent = self
                            self._children_name_map["discovery"] = "discovery"
                        return self.discovery

                    if (child_yang_name == "label"):
                        if (self.label is None):
                            self.label = MplsLdp.DefaultVrf.Afs.Af.Label()
                            self.label.parent = self
                            self._children_name_map["label"] = "label"
                        return self.label

                    if (child_yang_name == "neighbor"):
                        if (self.neighbor is None):
                            self.neighbor = MplsLdp.DefaultVrf.Afs.Af.Neighbor()
                            self.neighbor.parent = self
                            self._children_name_map["neighbor"] = "neighbor"
                        return self.neighbor

                    if (child_yang_name == "redistribution-protocol"):
                        if (self.redistribution_protocol is None):
                            self.redistribution_protocol = MplsLdp.DefaultVrf.Afs.Af.RedistributionProtocol()
                            self.redistribution_protocol.parent = self
                            self._children_name_map["redistribution_protocol"] = "redistribution-protocol"
                        return self.redistribution_protocol

                    if (child_yang_name == "traffic-engineering"):
                        if (self.traffic_engineering is None):
                            self.traffic_engineering = MplsLdp.DefaultVrf.Afs.Af.TrafficEngineering()
                            self.traffic_engineering.parent = self
                            self._children_name_map["traffic_engineering"] = "traffic-engineering"
                        return self.traffic_engineering

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "discovery" or name == "label" or name == "neighbor" or name == "redistribution-protocol" or name == "traffic-engineering" or name == "af-name" or name == "enable"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "af-name"):
                        self.af_name = value
                        self.af_name.value_namespace = name_space
                        self.af_name.value_namespace_prefix = name_space_prefix
                    if(value_path == "enable"):
                        self.enable = value
                        self.enable.value_namespace = name_space
                        self.enable.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.af:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.af:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "afs" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-mpls-ldp-cfg:mpls-ldp/default-vrf/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "af"):
                    for c in self.af:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = MplsLdp.DefaultVrf.Afs.Af()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.af.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "af"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass


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
            _revision = '2015-11-09'

            def __init__(self):
                super(MplsLdp.DefaultVrf.Global_, self).__init__()

                self.yang_name = "global"
                self.yang_parent_name = "default-vrf"

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

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("router_id") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(MplsLdp.DefaultVrf.Global_, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(MplsLdp.DefaultVrf.Global_, self).__setattr__(name, value)


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
                _revision = '2015-11-09'

                def __init__(self):
                    super(MplsLdp.DefaultVrf.Global_.Session, self).__init__()

                    self.yang_name = "session"
                    self.yang_parent_name = "global"

                    self.downstream_on_demand = MplsLdp.DefaultVrf.Global_.Session.DownstreamOnDemand()
                    self.downstream_on_demand.parent = self
                    self._children_name_map["downstream_on_demand"] = "downstream-on-demand"
                    self._children_yang_names.add("downstream-on-demand")

                    self.protection = MplsLdp.DefaultVrf.Global_.Session.Protection()
                    self.protection.parent = self
                    self._children_name_map["protection"] = "protection"
                    self._children_yang_names.add("protection")


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
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(MplsLdp.DefaultVrf.Global_.Session.Protection, self).__init__()

                        self.yang_name = "protection"
                        self.yang_parent_name = "session"

                        self.duration = YLeaf(YType.uint32, "duration")

                        self.peer_acl_name = YLeaf(YType.str, "peer-acl-name")

                        self.protection_type = YLeaf(YType.enumeration, "protection-type")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("duration",
                                        "peer_acl_name",
                                        "protection_type") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(MplsLdp.DefaultVrf.Global_.Session.Protection, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(MplsLdp.DefaultVrf.Global_.Session.Protection, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.duration.is_set or
                            self.peer_acl_name.is_set or
                            self.protection_type.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.duration.yfilter != YFilter.not_set or
                            self.peer_acl_name.yfilter != YFilter.not_set or
                            self.protection_type.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "protection" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            path_buffer = "Cisco-IOS-XR-mpls-ldp-cfg:mpls-ldp/default-vrf/global/session/%s" % self.get_segment_path()
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.duration.is_set or self.duration.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.duration.get_name_leafdata())
                        if (self.peer_acl_name.is_set or self.peer_acl_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.peer_acl_name.get_name_leafdata())
                        if (self.protection_type.is_set or self.protection_type.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.protection_type.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "duration" or name == "peer-acl-name" or name == "protection-type"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "duration"):
                            self.duration = value
                            self.duration.value_namespace = name_space
                            self.duration.value_namespace_prefix = name_space_prefix
                        if(value_path == "peer-acl-name"):
                            self.peer_acl_name = value
                            self.peer_acl_name.value_namespace = name_space
                            self.peer_acl_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "protection-type"):
                            self.protection_type = value
                            self.protection_type.value_namespace = name_space
                            self.protection_type.value_namespace_prefix = name_space_prefix


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
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(MplsLdp.DefaultVrf.Global_.Session.DownstreamOnDemand, self).__init__()

                        self.yang_name = "downstream-on-demand"
                        self.yang_parent_name = "session"

                        self.peer_acl_name = YLeaf(YType.str, "peer-acl-name")

                        self.type = YLeaf(YType.enumeration, "type")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("peer_acl_name",
                                        "type") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(MplsLdp.DefaultVrf.Global_.Session.DownstreamOnDemand, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(MplsLdp.DefaultVrf.Global_.Session.DownstreamOnDemand, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.peer_acl_name.is_set or
                            self.type.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.peer_acl_name.yfilter != YFilter.not_set or
                            self.type.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "downstream-on-demand" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            path_buffer = "Cisco-IOS-XR-mpls-ldp-cfg:mpls-ldp/default-vrf/global/session/%s" % self.get_segment_path()
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.peer_acl_name.is_set or self.peer_acl_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.peer_acl_name.get_name_leafdata())
                        if (self.type.is_set or self.type.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.type.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "peer-acl-name" or name == "type"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "peer-acl-name"):
                            self.peer_acl_name = value
                            self.peer_acl_name.value_namespace = name_space
                            self.peer_acl_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "type"):
                            self.type = value
                            self.type.value_namespace = name_space
                            self.type.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    return (
                        (self.downstream_on_demand is not None and self.downstream_on_demand.has_data()) or
                        (self.protection is not None and self.protection.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        (self.downstream_on_demand is not None and self.downstream_on_demand.has_operation()) or
                        (self.protection is not None and self.protection.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "session" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-mpls-ldp-cfg:mpls-ldp/default-vrf/global/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "downstream-on-demand"):
                        if (self.downstream_on_demand is None):
                            self.downstream_on_demand = MplsLdp.DefaultVrf.Global_.Session.DownstreamOnDemand()
                            self.downstream_on_demand.parent = self
                            self._children_name_map["downstream_on_demand"] = "downstream-on-demand"
                        return self.downstream_on_demand

                    if (child_yang_name == "protection"):
                        if (self.protection is None):
                            self.protection = MplsLdp.DefaultVrf.Global_.Session.Protection()
                            self.protection.parent = self
                            self._children_name_map["protection"] = "protection"
                        return self.protection

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "downstream-on-demand" or name == "protection"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


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
                _revision = '2015-11-09'

                def __init__(self):
                    super(MplsLdp.DefaultVrf.Global_.Neighbor, self).__init__()

                    self.yang_name = "neighbor"
                    self.yang_parent_name = "global"

                    self.password = YLeaf(YType.str, "password")

                    self.dual_stack = MplsLdp.DefaultVrf.Global_.Neighbor.DualStack()
                    self.dual_stack.parent = self
                    self._children_name_map["dual_stack"] = "dual-stack"
                    self._children_yang_names.add("dual-stack")

                    self.ldp_ids = MplsLdp.DefaultVrf.Global_.Neighbor.LdpIds()
                    self.ldp_ids.parent = self
                    self._children_name_map["ldp_ids"] = "ldp-ids"
                    self._children_yang_names.add("ldp-ids")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("password") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(MplsLdp.DefaultVrf.Global_.Neighbor, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(MplsLdp.DefaultVrf.Global_.Neighbor, self).__setattr__(name, value)


                class LdpIds(Entity):
                    """
                    Configuration related to Neighbors using LDP
                    Id
                    
                    .. attribute:: ldp_id
                    
                    	LDP ID based configuration related to a neigbor
                    	**type**\: list of    :py:class:`LdpId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.DefaultVrf.Global_.Neighbor.LdpIds.LdpId>`
                    
                    

                    """

                    _prefix = 'mpls-ldp-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(MplsLdp.DefaultVrf.Global_.Neighbor.LdpIds, self).__init__()

                        self.yang_name = "ldp-ids"
                        self.yang_parent_name = "neighbor"

                        self.ldp_id = YList(self)

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in () and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(MplsLdp.DefaultVrf.Global_.Neighbor.LdpIds, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(MplsLdp.DefaultVrf.Global_.Neighbor.LdpIds, self).__setattr__(name, value)


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
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(MplsLdp.DefaultVrf.Global_.Neighbor.LdpIds.LdpId, self).__init__()

                            self.yang_name = "ldp-id"
                            self.yang_parent_name = "ldp-ids"

                            self.lsr_id = YLeaf(YType.str, "lsr-id")

                            self.label_space_id = YLeaf(YType.uint32, "label-space-id")

                            self.password = MplsLdp.DefaultVrf.Global_.Neighbor.LdpIds.LdpId.Password()
                            self.password.parent = self
                            self._children_name_map["password"] = "password"
                            self._children_yang_names.add("password")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("lsr_id",
                                            "label_space_id") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(MplsLdp.DefaultVrf.Global_.Neighbor.LdpIds.LdpId, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(MplsLdp.DefaultVrf.Global_.Neighbor.LdpIds.LdpId, self).__setattr__(name, value)


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
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(MplsLdp.DefaultVrf.Global_.Neighbor.LdpIds.LdpId.Password, self).__init__()

                                self.yang_name = "password"
                                self.yang_parent_name = "ldp-id"

                                self.command_type = YLeaf(YType.enumeration, "command-type")

                                self.password = YLeaf(YType.str, "password")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("command_type",
                                                "password") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(MplsLdp.DefaultVrf.Global_.Neighbor.LdpIds.LdpId.Password, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(MplsLdp.DefaultVrf.Global_.Neighbor.LdpIds.LdpId.Password, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.command_type.is_set or
                                    self.password.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.command_type.yfilter != YFilter.not_set or
                                    self.password.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "password" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.command_type.is_set or self.command_type.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.command_type.get_name_leafdata())
                                if (self.password.is_set or self.password.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.password.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "command-type" or name == "password"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "command-type"):
                                    self.command_type = value
                                    self.command_type.value_namespace = name_space
                                    self.command_type.value_namespace_prefix = name_space_prefix
                                if(value_path == "password"):
                                    self.password = value
                                    self.password.value_namespace = name_space
                                    self.password.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            return (
                                self.lsr_id.is_set or
                                self.label_space_id.is_set or
                                (self.password is not None and self.password.has_data()))

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.lsr_id.yfilter != YFilter.not_set or
                                self.label_space_id.yfilter != YFilter.not_set or
                                (self.password is not None and self.password.has_operation()))

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "ldp-id" + "[lsr-id='" + self.lsr_id.get() + "']" + "[label-space-id='" + self.label_space_id.get() + "']" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                path_buffer = "Cisco-IOS-XR-mpls-ldp-cfg:mpls-ldp/default-vrf/global/neighbor/ldp-ids/%s" % self.get_segment_path()
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.lsr_id.is_set or self.lsr_id.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.lsr_id.get_name_leafdata())
                            if (self.label_space_id.is_set or self.label_space_id.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.label_space_id.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "password"):
                                if (self.password is None):
                                    self.password = MplsLdp.DefaultVrf.Global_.Neighbor.LdpIds.LdpId.Password()
                                    self.password.parent = self
                                    self._children_name_map["password"] = "password"
                                return self.password

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "password" or name == "lsr-id" or name == "label-space-id"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "lsr-id"):
                                self.lsr_id = value
                                self.lsr_id.value_namespace = name_space
                                self.lsr_id.value_namespace_prefix = name_space_prefix
                            if(value_path == "label-space-id"):
                                self.label_space_id = value
                                self.label_space_id.value_namespace = name_space
                                self.label_space_id.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.ldp_id:
                            if (c.has_data()):
                                return True
                        return False

                    def has_operation(self):
                        for c in self.ldp_id:
                            if (c.has_operation()):
                                return True
                        return self.yfilter != YFilter.not_set

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "ldp-ids" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            path_buffer = "Cisco-IOS-XR-mpls-ldp-cfg:mpls-ldp/default-vrf/global/neighbor/%s" % self.get_segment_path()
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "ldp-id"):
                            for c in self.ldp_id:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = MplsLdp.DefaultVrf.Global_.Neighbor.LdpIds.LdpId()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.ldp_id.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "ldp-id"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass


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
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(MplsLdp.DefaultVrf.Global_.Neighbor.DualStack, self).__init__()

                        self.yang_name = "dual-stack"
                        self.yang_parent_name = "neighbor"

                        self.tlv_compliance = YLeaf(YType.empty, "tlv-compliance")

                        self.transport_connection = MplsLdp.DefaultVrf.Global_.Neighbor.DualStack.TransportConnection()
                        self.transport_connection.parent = self
                        self._children_name_map["transport_connection"] = "transport-connection"
                        self._children_yang_names.add("transport-connection")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("tlv_compliance") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(MplsLdp.DefaultVrf.Global_.Neighbor.DualStack, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(MplsLdp.DefaultVrf.Global_.Neighbor.DualStack, self).__setattr__(name, value)


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
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(MplsLdp.DefaultVrf.Global_.Neighbor.DualStack.TransportConnection, self).__init__()

                            self.yang_name = "transport-connection"
                            self.yang_parent_name = "dual-stack"

                            self.max_wait = YLeaf(YType.uint32, "max-wait")

                            self.prefer = MplsLdp.DefaultVrf.Global_.Neighbor.DualStack.TransportConnection.Prefer()
                            self.prefer.parent = self
                            self._children_name_map["prefer"] = "prefer"
                            self._children_yang_names.add("prefer")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("max_wait") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(MplsLdp.DefaultVrf.Global_.Neighbor.DualStack.TransportConnection, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(MplsLdp.DefaultVrf.Global_.Neighbor.DualStack.TransportConnection, self).__setattr__(name, value)


                        class Prefer(Entity):
                            """
                            Configuration related to neighbor
                            dual\-stack xport\-connection preference
                            
                            .. attribute:: ipv4
                            
                            	Configuration related to neighbor dual\-stack xport\-connection preference ipv4
                            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                            
                            

                            """

                            _prefix = 'mpls-ldp-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(MplsLdp.DefaultVrf.Global_.Neighbor.DualStack.TransportConnection.Prefer, self).__init__()

                                self.yang_name = "prefer"
                                self.yang_parent_name = "transport-connection"

                                self.ipv4 = YLeaf(YType.empty, "ipv4")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("ipv4") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(MplsLdp.DefaultVrf.Global_.Neighbor.DualStack.TransportConnection.Prefer, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(MplsLdp.DefaultVrf.Global_.Neighbor.DualStack.TransportConnection.Prefer, self).__setattr__(name, value)

                            def has_data(self):
                                return self.ipv4.is_set

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.ipv4.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "prefer" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    path_buffer = "Cisco-IOS-XR-mpls-ldp-cfg:mpls-ldp/default-vrf/global/neighbor/dual-stack/transport-connection/%s" % self.get_segment_path()
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.ipv4.is_set or self.ipv4.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.ipv4.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "ipv4"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "ipv4"):
                                    self.ipv4 = value
                                    self.ipv4.value_namespace = name_space
                                    self.ipv4.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            return (
                                self.max_wait.is_set or
                                (self.prefer is not None and self.prefer.has_data()))

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.max_wait.yfilter != YFilter.not_set or
                                (self.prefer is not None and self.prefer.has_operation()))

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "transport-connection" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                path_buffer = "Cisco-IOS-XR-mpls-ldp-cfg:mpls-ldp/default-vrf/global/neighbor/dual-stack/%s" % self.get_segment_path()
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.max_wait.is_set or self.max_wait.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.max_wait.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "prefer"):
                                if (self.prefer is None):
                                    self.prefer = MplsLdp.DefaultVrf.Global_.Neighbor.DualStack.TransportConnection.Prefer()
                                    self.prefer.parent = self
                                    self._children_name_map["prefer"] = "prefer"
                                return self.prefer

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "prefer" or name == "max-wait"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "max-wait"):
                                self.max_wait = value
                                self.max_wait.value_namespace = name_space
                                self.max_wait.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        return (
                            self.tlv_compliance.is_set or
                            (self.transport_connection is not None and self.transport_connection.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.tlv_compliance.yfilter != YFilter.not_set or
                            (self.transport_connection is not None and self.transport_connection.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "dual-stack" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            path_buffer = "Cisco-IOS-XR-mpls-ldp-cfg:mpls-ldp/default-vrf/global/neighbor/%s" % self.get_segment_path()
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.tlv_compliance.is_set or self.tlv_compliance.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.tlv_compliance.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "transport-connection"):
                            if (self.transport_connection is None):
                                self.transport_connection = MplsLdp.DefaultVrf.Global_.Neighbor.DualStack.TransportConnection()
                                self.transport_connection.parent = self
                                self._children_name_map["transport_connection"] = "transport-connection"
                            return self.transport_connection

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "transport-connection" or name == "tlv-compliance"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "tlv-compliance"):
                            self.tlv_compliance = value
                            self.tlv_compliance.value_namespace = name_space
                            self.tlv_compliance.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    return (
                        self.password.is_set or
                        (self.dual_stack is not None and self.dual_stack.has_data()) or
                        (self.ldp_ids is not None and self.ldp_ids.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.password.yfilter != YFilter.not_set or
                        (self.dual_stack is not None and self.dual_stack.has_operation()) or
                        (self.ldp_ids is not None and self.ldp_ids.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "neighbor" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-mpls-ldp-cfg:mpls-ldp/default-vrf/global/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.password.is_set or self.password.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.password.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "dual-stack"):
                        if (self.dual_stack is None):
                            self.dual_stack = MplsLdp.DefaultVrf.Global_.Neighbor.DualStack()
                            self.dual_stack.parent = self
                            self._children_name_map["dual_stack"] = "dual-stack"
                        return self.dual_stack

                    if (child_yang_name == "ldp-ids"):
                        if (self.ldp_ids is None):
                            self.ldp_ids = MplsLdp.DefaultVrf.Global_.Neighbor.LdpIds()
                            self.ldp_ids.parent = self
                            self._children_name_map["ldp_ids"] = "ldp-ids"
                        return self.ldp_ids

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "dual-stack" or name == "ldp-ids" or name == "password"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "password"):
                        self.password = value
                        self.password.value_namespace = name_space
                        self.password.value_namespace_prefix = name_space_prefix


            class GracefulRestart(Entity):
                """
                Configuration for per\-VRF LDP Graceful Restart
                parameters
                
                .. attribute:: helper_peer
                
                	Configure parameters related to GR peer(s) opearating in helper mode
                	**type**\:   :py:class:`HelperPeer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.DefaultVrf.Global_.GracefulRestart.HelperPeer>`
                
                

                """

                _prefix = 'mpls-ldp-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(MplsLdp.DefaultVrf.Global_.GracefulRestart, self).__init__()

                    self.yang_name = "graceful-restart"
                    self.yang_parent_name = "global"

                    self.helper_peer = MplsLdp.DefaultVrf.Global_.GracefulRestart.HelperPeer()
                    self.helper_peer.parent = self
                    self._children_name_map["helper_peer"] = "helper-peer"
                    self._children_yang_names.add("helper-peer")


                class HelperPeer(Entity):
                    """
                    Configure parameters related to GR peer(s)
                    opearating in helper mode
                    
                    .. attribute:: maintain_on_local_reset
                    
                    	Maintain the state of a GR peer upon a local reset
                    	**type**\:  str
                    
                    

                    """

                    _prefix = 'mpls-ldp-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(MplsLdp.DefaultVrf.Global_.GracefulRestart.HelperPeer, self).__init__()

                        self.yang_name = "helper-peer"
                        self.yang_parent_name = "graceful-restart"

                        self.maintain_on_local_reset = YLeaf(YType.str, "maintain-on-local-reset")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("maintain_on_local_reset") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(MplsLdp.DefaultVrf.Global_.GracefulRestart.HelperPeer, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(MplsLdp.DefaultVrf.Global_.GracefulRestart.HelperPeer, self).__setattr__(name, value)

                    def has_data(self):
                        return self.maintain_on_local_reset.is_set

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.maintain_on_local_reset.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "helper-peer" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            path_buffer = "Cisco-IOS-XR-mpls-ldp-cfg:mpls-ldp/default-vrf/global/graceful-restart/%s" % self.get_segment_path()
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.maintain_on_local_reset.is_set or self.maintain_on_local_reset.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.maintain_on_local_reset.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "maintain-on-local-reset"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "maintain-on-local-reset"):
                            self.maintain_on_local_reset = value
                            self.maintain_on_local_reset.value_namespace = name_space
                            self.maintain_on_local_reset.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    return (self.helper_peer is not None and self.helper_peer.has_data())

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        (self.helper_peer is not None and self.helper_peer.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "graceful-restart" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-mpls-ldp-cfg:mpls-ldp/default-vrf/global/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "helper-peer"):
                        if (self.helper_peer is None):
                            self.helper_peer = MplsLdp.DefaultVrf.Global_.GracefulRestart.HelperPeer()
                            self.helper_peer.parent = self
                            self._children_name_map["helper_peer"] = "helper-peer"
                        return self.helper_peer

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "helper-peer"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass

            def has_data(self):
                return (
                    self.router_id.is_set or
                    (self.graceful_restart is not None and self.graceful_restart.has_data()) or
                    (self.neighbor is not None and self.neighbor.has_data()) or
                    (self.session is not None and self.session.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.router_id.yfilter != YFilter.not_set or
                    (self.graceful_restart is not None and self.graceful_restart.has_operation()) or
                    (self.neighbor is not None and self.neighbor.has_operation()) or
                    (self.session is not None and self.session.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "global" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-mpls-ldp-cfg:mpls-ldp/default-vrf/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.router_id.is_set or self.router_id.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.router_id.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "graceful-restart"):
                    if (self.graceful_restart is None):
                        self.graceful_restart = MplsLdp.DefaultVrf.Global_.GracefulRestart()
                        self.graceful_restart.parent = self
                        self._children_name_map["graceful_restart"] = "graceful-restart"
                    return self.graceful_restart

                if (child_yang_name == "neighbor"):
                    if (self.neighbor is None):
                        self.neighbor = MplsLdp.DefaultVrf.Global_.Neighbor()
                        self.neighbor.parent = self
                        self._children_name_map["neighbor"] = "neighbor"
                    return self.neighbor

                if (child_yang_name == "session"):
                    if (self.session is None):
                        self.session = MplsLdp.DefaultVrf.Global_.Session()
                        self.session.parent = self
                        self._children_name_map["session"] = "session"
                    return self.session

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "graceful-restart" or name == "neighbor" or name == "session" or name == "router-id"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "router-id"):
                    self.router_id = value
                    self.router_id.value_namespace = name_space
                    self.router_id.value_namespace_prefix = name_space_prefix


        class Interfaces(Entity):
            """
            MPLS LDP configuration pertaining to interfaces
            
            .. attribute:: interface
            
            	MPLS LDP configuration for a particular interface
            	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.DefaultVrf.Interfaces.Interface>`
            
            

            """

            _prefix = 'mpls-ldp-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(MplsLdp.DefaultVrf.Interfaces, self).__init__()

                self.yang_name = "interfaces"
                self.yang_parent_name = "default-vrf"

                self.interface = YList(self)

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in () and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(MplsLdp.DefaultVrf.Interfaces, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(MplsLdp.DefaultVrf.Interfaces, self).__setattr__(name, value)


            class Interface(Entity):
                """
                MPLS LDP configuration for a particular
                interface
                
                .. attribute:: interface_name  <key>
                
                	Name of interface
                	**type**\:  str
                
                	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                
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
                _revision = '2015-11-09'

                def __init__(self):
                    super(MplsLdp.DefaultVrf.Interfaces.Interface, self).__init__()

                    self.yang_name = "interface"
                    self.yang_parent_name = "interfaces"

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

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("interface_name",
                                    "enable") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(MplsLdp.DefaultVrf.Interfaces.Interface, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(MplsLdp.DefaultVrf.Interfaces.Interface, self).__setattr__(name, value)


                class Afs(Entity):
                    """
                    Address Family specific configuration for
                    MPLS LDP intf
                    
                    .. attribute:: af
                    
                    	Configure data for given Address Family
                    	**type**\: list of    :py:class:`Af <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.DefaultVrf.Interfaces.Interface.Afs.Af>`
                    
                    

                    """

                    _prefix = 'mpls-ldp-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(MplsLdp.DefaultVrf.Interfaces.Interface.Afs, self).__init__()

                        self.yang_name = "afs"
                        self.yang_parent_name = "interface"

                        self.af = YList(self)

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in () and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(MplsLdp.DefaultVrf.Interfaces.Interface.Afs, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(MplsLdp.DefaultVrf.Interfaces.Interface.Afs, self).__setattr__(name, value)


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
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(MplsLdp.DefaultVrf.Interfaces.Interface.Afs.Af, self).__init__()

                            self.yang_name = "af"
                            self.yang_parent_name = "afs"

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

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("af_name",
                                            "enable") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(MplsLdp.DefaultVrf.Interfaces.Interface.Afs.Af, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(MplsLdp.DefaultVrf.Interfaces.Interface.Afs.Af, self).__setattr__(name, value)


                        class Discovery(Entity):
                            """
                            Configure interface discovery parameters
                            
                            .. attribute:: transport_address
                            
                            	MPLS LDP configuration for interface discovery transportaddress
                            	**type**\:   :py:class:`TransportAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.DefaultVrf.Interfaces.Interface.Afs.Af.Discovery.TransportAddress>`
                            
                            

                            """

                            _prefix = 'mpls-ldp-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(MplsLdp.DefaultVrf.Interfaces.Interface.Afs.Af.Discovery, self).__init__()

                                self.yang_name = "discovery"
                                self.yang_parent_name = "af"

                                self.transport_address = MplsLdp.DefaultVrf.Interfaces.Interface.Afs.Af.Discovery.TransportAddress()
                                self.transport_address.parent = self
                                self._children_name_map["transport_address"] = "transport-address"
                                self._children_yang_names.add("transport-address")


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
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(MplsLdp.DefaultVrf.Interfaces.Interface.Afs.Af.Discovery.TransportAddress, self).__init__()

                                    self.yang_name = "transport-address"
                                    self.yang_parent_name = "discovery"

                                    self.address = YLeaf(YType.str, "address")

                                    self.address_type = YLeaf(YType.enumeration, "address-type")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("address",
                                                    "address_type") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(MplsLdp.DefaultVrf.Interfaces.Interface.Afs.Af.Discovery.TransportAddress, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(MplsLdp.DefaultVrf.Interfaces.Interface.Afs.Af.Discovery.TransportAddress, self).__setattr__(name, value)

                                def has_data(self):
                                    return (
                                        self.address.is_set or
                                        self.address_type.is_set)

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.address.yfilter != YFilter.not_set or
                                        self.address_type.yfilter != YFilter.not_set)

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "transport-address" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.address.is_set or self.address.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.address.get_name_leafdata())
                                    if (self.address_type.is_set or self.address_type.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.address_type.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "address" or name == "address-type"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "address"):
                                        self.address = value
                                        self.address.value_namespace = name_space
                                        self.address.value_namespace_prefix = name_space_prefix
                                    if(value_path == "address-type"):
                                        self.address_type = value
                                        self.address_type.value_namespace = name_space
                                        self.address_type.value_namespace_prefix = name_space_prefix

                            def has_data(self):
                                return (self.transport_address is not None and self.transport_address.has_data())

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    (self.transport_address is not None and self.transport_address.has_operation()))

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "discovery" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                if (child_yang_name == "transport-address"):
                                    if (self.transport_address is None):
                                        self.transport_address = MplsLdp.DefaultVrf.Interfaces.Interface.Afs.Af.Discovery.TransportAddress()
                                        self.transport_address.parent = self
                                        self._children_name_map["transport_address"] = "transport-address"
                                    return self.transport_address

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "transport-address"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                pass


                        class Igp(Entity):
                            """
                            LDP interface IGP configuration
                            
                            .. attribute:: disable_auto_config
                            
                            	Disable IGP Auto\-config on this interface
                            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                            
                            

                            """

                            _prefix = 'mpls-ldp-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(MplsLdp.DefaultVrf.Interfaces.Interface.Afs.Af.Igp, self).__init__()

                                self.yang_name = "igp"
                                self.yang_parent_name = "af"

                                self.disable_auto_config = YLeaf(YType.empty, "disable-auto-config")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("disable_auto_config") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(MplsLdp.DefaultVrf.Interfaces.Interface.Afs.Af.Igp, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(MplsLdp.DefaultVrf.Interfaces.Interface.Afs.Af.Igp, self).__setattr__(name, value)

                            def has_data(self):
                                return self.disable_auto_config.is_set

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.disable_auto_config.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "igp" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.disable_auto_config.is_set or self.disable_auto_config.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.disable_auto_config.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "disable-auto-config"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "disable-auto-config"):
                                    self.disable_auto_config = value
                                    self.disable_auto_config.value_namespace = name_space
                                    self.disable_auto_config.value_namespace_prefix = name_space_prefix


                        class Mldp(Entity):
                            """
                            Interface configuration parameters for mLDP
                            
                            .. attribute:: disable
                            
                            	Disable mLDP on LDP enabled interface
                            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                            
                            

                            """

                            _prefix = 'mpls-ldp-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(MplsLdp.DefaultVrf.Interfaces.Interface.Afs.Af.Mldp, self).__init__()

                                self.yang_name = "mldp"
                                self.yang_parent_name = "af"

                                self.disable = YLeaf(YType.empty, "disable")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("disable") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(MplsLdp.DefaultVrf.Interfaces.Interface.Afs.Af.Mldp, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(MplsLdp.DefaultVrf.Interfaces.Interface.Afs.Af.Mldp, self).__setattr__(name, value)

                            def has_data(self):
                                return self.disable.is_set

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.disable.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "mldp" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.disable.is_set or self.disable.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.disable.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "disable"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "disable"):
                                    self.disable = value
                                    self.disable.value_namespace = name_space
                                    self.disable.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            return (
                                self.af_name.is_set or
                                self.enable.is_set or
                                (self.discovery is not None and self.discovery.has_data()) or
                                (self.igp is not None and self.igp.has_data()) or
                                (self.mldp is not None and self.mldp.has_data()))

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.af_name.yfilter != YFilter.not_set or
                                self.enable.yfilter != YFilter.not_set or
                                (self.discovery is not None and self.discovery.has_operation()) or
                                (self.igp is not None and self.igp.has_operation()) or
                                (self.mldp is not None and self.mldp.has_operation()))

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "af" + "[af-name='" + self.af_name.get() + "']" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.af_name.is_set or self.af_name.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.af_name.get_name_leafdata())
                            if (self.enable.is_set or self.enable.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.enable.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "discovery"):
                                if (self.discovery is None):
                                    self.discovery = MplsLdp.DefaultVrf.Interfaces.Interface.Afs.Af.Discovery()
                                    self.discovery.parent = self
                                    self._children_name_map["discovery"] = "discovery"
                                return self.discovery

                            if (child_yang_name == "igp"):
                                if (self.igp is None):
                                    self.igp = MplsLdp.DefaultVrf.Interfaces.Interface.Afs.Af.Igp()
                                    self.igp.parent = self
                                    self._children_name_map["igp"] = "igp"
                                return self.igp

                            if (child_yang_name == "mldp"):
                                if (self.mldp is None):
                                    self.mldp = MplsLdp.DefaultVrf.Interfaces.Interface.Afs.Af.Mldp()
                                    self.mldp.parent = self
                                    self._children_name_map["mldp"] = "mldp"
                                return self.mldp

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "discovery" or name == "igp" or name == "mldp" or name == "af-name" or name == "enable"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "af-name"):
                                self.af_name = value
                                self.af_name.value_namespace = name_space
                                self.af_name.value_namespace_prefix = name_space_prefix
                            if(value_path == "enable"):
                                self.enable = value
                                self.enable.value_namespace = name_space
                                self.enable.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.af:
                            if (c.has_data()):
                                return True
                        return False

                    def has_operation(self):
                        for c in self.af:
                            if (c.has_operation()):
                                return True
                        return self.yfilter != YFilter.not_set

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "afs" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "af"):
                            for c in self.af:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = MplsLdp.DefaultVrf.Interfaces.Interface.Afs.Af()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.af.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "af"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass


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
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(MplsLdp.DefaultVrf.Interfaces.Interface.Global_, self).__init__()

                        self.yang_name = "global"
                        self.yang_parent_name = "interface"

                        self.discovery = MplsLdp.DefaultVrf.Interfaces.Interface.Global_.Discovery()
                        self.discovery.parent = self
                        self._children_name_map["discovery"] = "discovery"
                        self._children_yang_names.add("discovery")

                        self.igp = MplsLdp.DefaultVrf.Interfaces.Interface.Global_.Igp()
                        self.igp.parent = self
                        self._children_name_map["igp"] = "igp"
                        self._children_yang_names.add("igp")


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
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(MplsLdp.DefaultVrf.Interfaces.Interface.Global_.Discovery, self).__init__()

                            self.yang_name = "discovery"
                            self.yang_parent_name = "global"

                            self.disable_quick_start = YLeaf(YType.empty, "disable-quick-start")

                            self.link_hello = MplsLdp.DefaultVrf.Interfaces.Interface.Global_.Discovery.LinkHello()
                            self.link_hello.parent = self
                            self._children_name_map["link_hello"] = "link-hello"
                            self._children_yang_names.add("link-hello")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("disable_quick_start") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(MplsLdp.DefaultVrf.Interfaces.Interface.Global_.Discovery, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(MplsLdp.DefaultVrf.Interfaces.Interface.Global_.Discovery, self).__setattr__(name, value)


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
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(MplsLdp.DefaultVrf.Interfaces.Interface.Global_.Discovery.LinkHello, self).__init__()

                                self.yang_name = "link-hello"
                                self.yang_parent_name = "discovery"

                                self.dual_stack = YLeaf(YType.enumeration, "dual-stack")

                                self.hold_time = YLeaf(YType.uint32, "hold-time")

                                self.interval = YLeaf(YType.uint32, "interval")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("dual_stack",
                                                "hold_time",
                                                "interval") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(MplsLdp.DefaultVrf.Interfaces.Interface.Global_.Discovery.LinkHello, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(MplsLdp.DefaultVrf.Interfaces.Interface.Global_.Discovery.LinkHello, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.dual_stack.is_set or
                                    self.hold_time.is_set or
                                    self.interval.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.dual_stack.yfilter != YFilter.not_set or
                                    self.hold_time.yfilter != YFilter.not_set or
                                    self.interval.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "link-hello" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.dual_stack.is_set or self.dual_stack.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.dual_stack.get_name_leafdata())
                                if (self.hold_time.is_set or self.hold_time.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.hold_time.get_name_leafdata())
                                if (self.interval.is_set or self.interval.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.interval.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "dual-stack" or name == "hold-time" or name == "interval"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "dual-stack"):
                                    self.dual_stack = value
                                    self.dual_stack.value_namespace = name_space
                                    self.dual_stack.value_namespace_prefix = name_space_prefix
                                if(value_path == "hold-time"):
                                    self.hold_time = value
                                    self.hold_time.value_namespace = name_space
                                    self.hold_time.value_namespace_prefix = name_space_prefix
                                if(value_path == "interval"):
                                    self.interval = value
                                    self.interval.value_namespace = name_space
                                    self.interval.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            return (
                                self.disable_quick_start.is_set or
                                (self.link_hello is not None and self.link_hello.has_data()))

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.disable_quick_start.yfilter != YFilter.not_set or
                                (self.link_hello is not None and self.link_hello.has_operation()))

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "discovery" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.disable_quick_start.is_set or self.disable_quick_start.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.disable_quick_start.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "link-hello"):
                                if (self.link_hello is None):
                                    self.link_hello = MplsLdp.DefaultVrf.Interfaces.Interface.Global_.Discovery.LinkHello()
                                    self.link_hello.parent = self
                                    self._children_name_map["link_hello"] = "link-hello"
                                return self.link_hello

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "link-hello" or name == "disable-quick-start"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "disable-quick-start"):
                                self.disable_quick_start = value
                                self.disable_quick_start.value_namespace = name_space
                                self.disable_quick_start.value_namespace_prefix = name_space_prefix


                    class Igp(Entity):
                        """
                        LDP IGP configuration
                        
                        .. attribute:: sync
                        
                        	LDP IGP synchronization
                        	**type**\:   :py:class:`Sync <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.DefaultVrf.Interfaces.Interface.Global_.Igp.Sync>`
                        
                        

                        """

                        _prefix = 'mpls-ldp-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(MplsLdp.DefaultVrf.Interfaces.Interface.Global_.Igp, self).__init__()

                            self.yang_name = "igp"
                            self.yang_parent_name = "global"

                            self.sync = MplsLdp.DefaultVrf.Interfaces.Interface.Global_.Igp.Sync()
                            self.sync.parent = self
                            self._children_name_map["sync"] = "sync"
                            self._children_yang_names.add("sync")


                        class Sync(Entity):
                            """
                            LDP IGP synchronization
                            
                            .. attribute:: delay
                            
                            	LDP IGP synchronization delay time
                            	**type**\:   :py:class:`Delay <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.DefaultVrf.Interfaces.Interface.Global_.Igp.Sync.Delay>`
                            
                            

                            """

                            _prefix = 'mpls-ldp-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(MplsLdp.DefaultVrf.Interfaces.Interface.Global_.Igp.Sync, self).__init__()

                                self.yang_name = "sync"
                                self.yang_parent_name = "igp"

                                self.delay = MplsLdp.DefaultVrf.Interfaces.Interface.Global_.Igp.Sync.Delay()
                                self.delay.parent = self
                                self._children_name_map["delay"] = "delay"
                                self._children_yang_names.add("delay")


                            class Delay(Entity):
                                """
                                LDP IGP synchronization delay time
                                
                                .. attribute:: on_session_up
                                
                                	Interface sync up delay after session up
                                	**type**\:   :py:class:`OnSessionUp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.DefaultVrf.Interfaces.Interface.Global_.Igp.Sync.Delay.OnSessionUp>`
                                
                                

                                """

                                _prefix = 'mpls-ldp-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(MplsLdp.DefaultVrf.Interfaces.Interface.Global_.Igp.Sync.Delay, self).__init__()

                                    self.yang_name = "delay"
                                    self.yang_parent_name = "sync"

                                    self.on_session_up = MplsLdp.DefaultVrf.Interfaces.Interface.Global_.Igp.Sync.Delay.OnSessionUp()
                                    self.on_session_up.parent = self
                                    self._children_name_map["on_session_up"] = "on-session-up"
                                    self._children_yang_names.add("on-session-up")


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
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(MplsLdp.DefaultVrf.Interfaces.Interface.Global_.Igp.Sync.Delay.OnSessionUp, self).__init__()

                                        self.yang_name = "on-session-up"
                                        self.yang_parent_name = "delay"

                                        self.disable = YLeaf(YType.empty, "disable")

                                        self.timeout = YLeaf(YType.uint32, "timeout")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("disable",
                                                        "timeout") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(MplsLdp.DefaultVrf.Interfaces.Interface.Global_.Igp.Sync.Delay.OnSessionUp, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(MplsLdp.DefaultVrf.Interfaces.Interface.Global_.Igp.Sync.Delay.OnSessionUp, self).__setattr__(name, value)

                                    def has_data(self):
                                        return (
                                            self.disable.is_set or
                                            self.timeout.is_set)

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.disable.yfilter != YFilter.not_set or
                                            self.timeout.yfilter != YFilter.not_set)

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "on-session-up" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()
                                        if (self.disable.is_set or self.disable.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.disable.get_name_leafdata())
                                        if (self.timeout.is_set or self.timeout.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.timeout.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "disable" or name == "timeout"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "disable"):
                                            self.disable = value
                                            self.disable.value_namespace = name_space
                                            self.disable.value_namespace_prefix = name_space_prefix
                                        if(value_path == "timeout"):
                                            self.timeout = value
                                            self.timeout.value_namespace = name_space
                                            self.timeout.value_namespace_prefix = name_space_prefix

                                def has_data(self):
                                    return (self.on_session_up is not None and self.on_session_up.has_data())

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        (self.on_session_up is not None and self.on_session_up.has_operation()))

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "delay" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    if (child_yang_name == "on-session-up"):
                                        if (self.on_session_up is None):
                                            self.on_session_up = MplsLdp.DefaultVrf.Interfaces.Interface.Global_.Igp.Sync.Delay.OnSessionUp()
                                            self.on_session_up.parent = self
                                            self._children_name_map["on_session_up"] = "on-session-up"
                                        return self.on_session_up

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "on-session-up"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    pass

                            def has_data(self):
                                return (self.delay is not None and self.delay.has_data())

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    (self.delay is not None and self.delay.has_operation()))

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "sync" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                if (child_yang_name == "delay"):
                                    if (self.delay is None):
                                        self.delay = MplsLdp.DefaultVrf.Interfaces.Interface.Global_.Igp.Sync.Delay()
                                        self.delay.parent = self
                                        self._children_name_map["delay"] = "delay"
                                    return self.delay

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "delay"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                pass

                        def has_data(self):
                            return (self.sync is not None and self.sync.has_data())

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                (self.sync is not None and self.sync.has_operation()))

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "igp" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "sync"):
                                if (self.sync is None):
                                    self.sync = MplsLdp.DefaultVrf.Interfaces.Interface.Global_.Igp.Sync()
                                    self.sync.parent = self
                                    self._children_name_map["sync"] = "sync"
                                return self.sync

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "sync"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            pass

                    def has_data(self):
                        return (
                            (self.discovery is not None and self.discovery.has_data()) or
                            (self.igp is not None and self.igp.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            (self.discovery is not None and self.discovery.has_operation()) or
                            (self.igp is not None and self.igp.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "global" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "discovery"):
                            if (self.discovery is None):
                                self.discovery = MplsLdp.DefaultVrf.Interfaces.Interface.Global_.Discovery()
                                self.discovery.parent = self
                                self._children_name_map["discovery"] = "discovery"
                            return self.discovery

                        if (child_yang_name == "igp"):
                            if (self.igp is None):
                                self.igp = MplsLdp.DefaultVrf.Interfaces.Interface.Global_.Igp()
                                self.igp.parent = self
                                self._children_name_map["igp"] = "igp"
                            return self.igp

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "discovery" or name == "igp"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass

                def has_data(self):
                    return (
                        self.interface_name.is_set or
                        self.enable.is_set or
                        (self.afs is not None and self.afs.has_data()) or
                        (self.global_ is not None and self.global_.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.interface_name.yfilter != YFilter.not_set or
                        self.enable.yfilter != YFilter.not_set or
                        (self.afs is not None and self.afs.has_operation()) or
                        (self.global_ is not None and self.global_.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "interface" + "[interface-name='" + self.interface_name.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-mpls-ldp-cfg:mpls-ldp/default-vrf/interfaces/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.interface_name.is_set or self.interface_name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.interface_name.get_name_leafdata())
                    if (self.enable.is_set or self.enable.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.enable.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "afs"):
                        if (self.afs is None):
                            self.afs = MplsLdp.DefaultVrf.Interfaces.Interface.Afs()
                            self.afs.parent = self
                            self._children_name_map["afs"] = "afs"
                        return self.afs

                    if (child_yang_name == "global"):
                        if (self.global_ is None):
                            self.global_ = MplsLdp.DefaultVrf.Interfaces.Interface.Global_()
                            self.global_.parent = self
                            self._children_name_map["global_"] = "global"
                        return self.global_

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "afs" or name == "global" or name == "interface-name" or name == "enable"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "interface-name"):
                        self.interface_name = value
                        self.interface_name.value_namespace = name_space
                        self.interface_name.value_namespace_prefix = name_space_prefix
                    if(value_path == "enable"):
                        self.enable = value
                        self.enable.value_namespace = name_space
                        self.enable.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.interface:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.interface:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "interfaces" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-mpls-ldp-cfg:mpls-ldp/default-vrf/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "interface"):
                    for c in self.interface:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = MplsLdp.DefaultVrf.Interfaces.Interface()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.interface.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "interface"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass

        def has_data(self):
            return (
                (self.afs is not None and self.afs.has_data()) or
                (self.global_ is not None and self.global_.has_data()) or
                (self.interfaces is not None and self.interfaces.has_data()))

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                (self.afs is not None and self.afs.has_operation()) or
                (self.global_ is not None and self.global_.has_operation()) or
                (self.interfaces is not None and self.interfaces.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "default-vrf" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-mpls-ldp-cfg:mpls-ldp/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "afs"):
                if (self.afs is None):
                    self.afs = MplsLdp.DefaultVrf.Afs()
                    self.afs.parent = self
                    self._children_name_map["afs"] = "afs"
                return self.afs

            if (child_yang_name == "global"):
                if (self.global_ is None):
                    self.global_ = MplsLdp.DefaultVrf.Global_()
                    self.global_.parent = self
                    self._children_name_map["global_"] = "global"
                return self.global_

            if (child_yang_name == "interfaces"):
                if (self.interfaces is None):
                    self.interfaces = MplsLdp.DefaultVrf.Interfaces()
                    self.interfaces.parent = self
                    self._children_name_map["interfaces"] = "interfaces"
                return self.interfaces

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "afs" or name == "global" or name == "interfaces"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Vrfs(Entity):
        """
        VRF Table attribute configuration for MPLS LDP
        
        .. attribute:: vrf
        
        	VRF attribute configuration for MPLS LDP
        	**type**\: list of    :py:class:`Vrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.Vrfs.Vrf>`
        
        

        """

        _prefix = 'mpls-ldp-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(MplsLdp.Vrfs, self).__init__()

            self.yang_name = "vrfs"
            self.yang_parent_name = "mpls-ldp"

            self.vrf = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(MplsLdp.Vrfs, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(MplsLdp.Vrfs, self).__setattr__(name, value)


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
            _revision = '2015-11-09'

            def __init__(self):
                super(MplsLdp.Vrfs.Vrf, self).__init__()

                self.yang_name = "vrf"
                self.yang_parent_name = "vrfs"

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

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("vrf_name",
                                "enable") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(MplsLdp.Vrfs.Vrf, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(MplsLdp.Vrfs.Vrf, self).__setattr__(name, value)


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
                _revision = '2015-11-09'

                def __init__(self):
                    super(MplsLdp.Vrfs.Vrf.Global_, self).__init__()

                    self.yang_name = "global"
                    self.yang_parent_name = "vrf"

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

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("router_id") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(MplsLdp.Vrfs.Vrf.Global_, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(MplsLdp.Vrfs.Vrf.Global_, self).__setattr__(name, value)


                class Session(Entity):
                    """
                    LDP Session parameters
                    
                    .. attribute:: downstream_on_demand
                    
                    	ACL with the list of neighbors configured for Downstream on Demand
                    	**type**\:   :py:class:`DownstreamOnDemand <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.Vrfs.Vrf.Global_.Session.DownstreamOnDemand>`
                    
                    

                    """

                    _prefix = 'mpls-ldp-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(MplsLdp.Vrfs.Vrf.Global_.Session, self).__init__()

                        self.yang_name = "session"
                        self.yang_parent_name = "global"

                        self.downstream_on_demand = MplsLdp.Vrfs.Vrf.Global_.Session.DownstreamOnDemand()
                        self.downstream_on_demand.parent = self
                        self._children_name_map["downstream_on_demand"] = "downstream-on-demand"
                        self._children_yang_names.add("downstream-on-demand")


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
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(MplsLdp.Vrfs.Vrf.Global_.Session.DownstreamOnDemand, self).__init__()

                            self.yang_name = "downstream-on-demand"
                            self.yang_parent_name = "session"

                            self.peer_acl_name = YLeaf(YType.str, "peer-acl-name")

                            self.type = YLeaf(YType.enumeration, "type")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("peer_acl_name",
                                            "type") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(MplsLdp.Vrfs.Vrf.Global_.Session.DownstreamOnDemand, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(MplsLdp.Vrfs.Vrf.Global_.Session.DownstreamOnDemand, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.peer_acl_name.is_set or
                                self.type.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.peer_acl_name.yfilter != YFilter.not_set or
                                self.type.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "downstream-on-demand" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.peer_acl_name.is_set or self.peer_acl_name.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.peer_acl_name.get_name_leafdata())
                            if (self.type.is_set or self.type.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.type.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "peer-acl-name" or name == "type"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "peer-acl-name"):
                                self.peer_acl_name = value
                                self.peer_acl_name.value_namespace = name_space
                                self.peer_acl_name.value_namespace_prefix = name_space_prefix
                            if(value_path == "type"):
                                self.type = value
                                self.type.value_namespace = name_space
                                self.type.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        return (self.downstream_on_demand is not None and self.downstream_on_demand.has_data())

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            (self.downstream_on_demand is not None and self.downstream_on_demand.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "session" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "downstream-on-demand"):
                            if (self.downstream_on_demand is None):
                                self.downstream_on_demand = MplsLdp.Vrfs.Vrf.Global_.Session.DownstreamOnDemand()
                                self.downstream_on_demand.parent = self
                                self._children_name_map["downstream_on_demand"] = "downstream-on-demand"
                            return self.downstream_on_demand

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "downstream-on-demand"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass


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
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(MplsLdp.Vrfs.Vrf.Global_.Neighbor, self).__init__()

                        self.yang_name = "neighbor"
                        self.yang_parent_name = "global"

                        self.password = YLeaf(YType.str, "password")

                        self.ldp_ids = MplsLdp.Vrfs.Vrf.Global_.Neighbor.LdpIds()
                        self.ldp_ids.parent = self
                        self._children_name_map["ldp_ids"] = "ldp-ids"
                        self._children_yang_names.add("ldp-ids")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("password") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(MplsLdp.Vrfs.Vrf.Global_.Neighbor, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(MplsLdp.Vrfs.Vrf.Global_.Neighbor, self).__setattr__(name, value)


                    class LdpIds(Entity):
                        """
                        Configuration related to Neighbors using LDP
                        Id
                        
                        .. attribute:: ldp_id
                        
                        	LDP ID based configuration related to a neigbor
                        	**type**\: list of    :py:class:`LdpId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.Vrfs.Vrf.Global_.Neighbor.LdpIds.LdpId>`
                        
                        

                        """

                        _prefix = 'mpls-ldp-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(MplsLdp.Vrfs.Vrf.Global_.Neighbor.LdpIds, self).__init__()

                            self.yang_name = "ldp-ids"
                            self.yang_parent_name = "neighbor"

                            self.ldp_id = YList(self)

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in () and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(MplsLdp.Vrfs.Vrf.Global_.Neighbor.LdpIds, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(MplsLdp.Vrfs.Vrf.Global_.Neighbor.LdpIds, self).__setattr__(name, value)


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
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(MplsLdp.Vrfs.Vrf.Global_.Neighbor.LdpIds.LdpId, self).__init__()

                                self.yang_name = "ldp-id"
                                self.yang_parent_name = "ldp-ids"

                                self.lsr_id = YLeaf(YType.str, "lsr-id")

                                self.label_space_id = YLeaf(YType.uint32, "label-space-id")

                                self.password = MplsLdp.Vrfs.Vrf.Global_.Neighbor.LdpIds.LdpId.Password()
                                self.password.parent = self
                                self._children_name_map["password"] = "password"
                                self._children_yang_names.add("password")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("lsr_id",
                                                "label_space_id") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(MplsLdp.Vrfs.Vrf.Global_.Neighbor.LdpIds.LdpId, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(MplsLdp.Vrfs.Vrf.Global_.Neighbor.LdpIds.LdpId, self).__setattr__(name, value)


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
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(MplsLdp.Vrfs.Vrf.Global_.Neighbor.LdpIds.LdpId.Password, self).__init__()

                                    self.yang_name = "password"
                                    self.yang_parent_name = "ldp-id"

                                    self.command_type = YLeaf(YType.enumeration, "command-type")

                                    self.password = YLeaf(YType.str, "password")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("command_type",
                                                    "password") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(MplsLdp.Vrfs.Vrf.Global_.Neighbor.LdpIds.LdpId.Password, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(MplsLdp.Vrfs.Vrf.Global_.Neighbor.LdpIds.LdpId.Password, self).__setattr__(name, value)

                                def has_data(self):
                                    return (
                                        self.command_type.is_set or
                                        self.password.is_set)

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.command_type.yfilter != YFilter.not_set or
                                        self.password.yfilter != YFilter.not_set)

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "password" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.command_type.is_set or self.command_type.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.command_type.get_name_leafdata())
                                    if (self.password.is_set or self.password.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.password.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "command-type" or name == "password"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "command-type"):
                                        self.command_type = value
                                        self.command_type.value_namespace = name_space
                                        self.command_type.value_namespace_prefix = name_space_prefix
                                    if(value_path == "password"):
                                        self.password = value
                                        self.password.value_namespace = name_space
                                        self.password.value_namespace_prefix = name_space_prefix

                            def has_data(self):
                                return (
                                    self.lsr_id.is_set or
                                    self.label_space_id.is_set or
                                    (self.password is not None and self.password.has_data()))

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.lsr_id.yfilter != YFilter.not_set or
                                    self.label_space_id.yfilter != YFilter.not_set or
                                    (self.password is not None and self.password.has_operation()))

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "ldp-id" + "[lsr-id='" + self.lsr_id.get() + "']" + "[label-space-id='" + self.label_space_id.get() + "']" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.lsr_id.is_set or self.lsr_id.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.lsr_id.get_name_leafdata())
                                if (self.label_space_id.is_set or self.label_space_id.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.label_space_id.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                if (child_yang_name == "password"):
                                    if (self.password is None):
                                        self.password = MplsLdp.Vrfs.Vrf.Global_.Neighbor.LdpIds.LdpId.Password()
                                        self.password.parent = self
                                        self._children_name_map["password"] = "password"
                                    return self.password

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "password" or name == "lsr-id" or name == "label-space-id"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "lsr-id"):
                                    self.lsr_id = value
                                    self.lsr_id.value_namespace = name_space
                                    self.lsr_id.value_namespace_prefix = name_space_prefix
                                if(value_path == "label-space-id"):
                                    self.label_space_id = value
                                    self.label_space_id.value_namespace = name_space
                                    self.label_space_id.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            for c in self.ldp_id:
                                if (c.has_data()):
                                    return True
                            return False

                        def has_operation(self):
                            for c in self.ldp_id:
                                if (c.has_operation()):
                                    return True
                            return self.yfilter != YFilter.not_set

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "ldp-ids" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "ldp-id"):
                                for c in self.ldp_id:
                                    segment = c.get_segment_path()
                                    if (segment_path == segment):
                                        return c
                                c = MplsLdp.Vrfs.Vrf.Global_.Neighbor.LdpIds.LdpId()
                                c.parent = self
                                local_reference_key = "ydk::seg::%s" % segment_path
                                self._local_refs[local_reference_key] = c
                                self.ldp_id.append(c)
                                return c

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "ldp-id"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            pass

                    def has_data(self):
                        return (
                            self.password.is_set or
                            (self.ldp_ids is not None and self.ldp_ids.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.password.yfilter != YFilter.not_set or
                            (self.ldp_ids is not None and self.ldp_ids.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "neighbor" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.password.is_set or self.password.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.password.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "ldp-ids"):
                            if (self.ldp_ids is None):
                                self.ldp_ids = MplsLdp.Vrfs.Vrf.Global_.Neighbor.LdpIds()
                                self.ldp_ids.parent = self
                                self._children_name_map["ldp_ids"] = "ldp-ids"
                            return self.ldp_ids

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "ldp-ids" or name == "password"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "password"):
                            self.password = value
                            self.password.value_namespace = name_space
                            self.password.value_namespace_prefix = name_space_prefix


                class GracefulRestart(Entity):
                    """
                    Configuration for per\-VRF LDP Graceful
                    Restart parameters
                    
                    .. attribute:: helper_peer
                    
                    	Configure parameters related to GR peer(s) opearating in helper mode
                    	**type**\:   :py:class:`HelperPeer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.Vrfs.Vrf.Global_.GracefulRestart.HelperPeer>`
                    
                    

                    """

                    _prefix = 'mpls-ldp-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(MplsLdp.Vrfs.Vrf.Global_.GracefulRestart, self).__init__()

                        self.yang_name = "graceful-restart"
                        self.yang_parent_name = "global"

                        self.helper_peer = MplsLdp.Vrfs.Vrf.Global_.GracefulRestart.HelperPeer()
                        self.helper_peer.parent = self
                        self._children_name_map["helper_peer"] = "helper-peer"
                        self._children_yang_names.add("helper-peer")


                    class HelperPeer(Entity):
                        """
                        Configure parameters related to GR peer(s)
                        opearating in helper mode
                        
                        .. attribute:: maintain_on_local_reset
                        
                        	Maintain the state of a GR peer upon a local reset
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'mpls-ldp-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(MplsLdp.Vrfs.Vrf.Global_.GracefulRestart.HelperPeer, self).__init__()

                            self.yang_name = "helper-peer"
                            self.yang_parent_name = "graceful-restart"

                            self.maintain_on_local_reset = YLeaf(YType.str, "maintain-on-local-reset")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("maintain_on_local_reset") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(MplsLdp.Vrfs.Vrf.Global_.GracefulRestart.HelperPeer, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(MplsLdp.Vrfs.Vrf.Global_.GracefulRestart.HelperPeer, self).__setattr__(name, value)

                        def has_data(self):
                            return self.maintain_on_local_reset.is_set

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.maintain_on_local_reset.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "helper-peer" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.maintain_on_local_reset.is_set or self.maintain_on_local_reset.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.maintain_on_local_reset.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "maintain-on-local-reset"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "maintain-on-local-reset"):
                                self.maintain_on_local_reset = value
                                self.maintain_on_local_reset.value_namespace = name_space
                                self.maintain_on_local_reset.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        return (self.helper_peer is not None and self.helper_peer.has_data())

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            (self.helper_peer is not None and self.helper_peer.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "graceful-restart" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "helper-peer"):
                            if (self.helper_peer is None):
                                self.helper_peer = MplsLdp.Vrfs.Vrf.Global_.GracefulRestart.HelperPeer()
                                self.helper_peer.parent = self
                                self._children_name_map["helper_peer"] = "helper-peer"
                            return self.helper_peer

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "helper-peer"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass

                def has_data(self):
                    return (
                        self.router_id.is_set or
                        (self.graceful_restart is not None and self.graceful_restart.has_data()) or
                        (self.neighbor is not None and self.neighbor.has_data()) or
                        (self.session is not None and self.session.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.router_id.yfilter != YFilter.not_set or
                        (self.graceful_restart is not None and self.graceful_restart.has_operation()) or
                        (self.neighbor is not None and self.neighbor.has_operation()) or
                        (self.session is not None and self.session.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "global" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.router_id.is_set or self.router_id.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.router_id.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "graceful-restart"):
                        if (self.graceful_restart is None):
                            self.graceful_restart = MplsLdp.Vrfs.Vrf.Global_.GracefulRestart()
                            self.graceful_restart.parent = self
                            self._children_name_map["graceful_restart"] = "graceful-restart"
                        return self.graceful_restart

                    if (child_yang_name == "neighbor"):
                        if (self.neighbor is None):
                            self.neighbor = MplsLdp.Vrfs.Vrf.Global_.Neighbor()
                            self.neighbor.parent = self
                            self._children_name_map["neighbor"] = "neighbor"
                        return self.neighbor

                    if (child_yang_name == "session"):
                        if (self.session is None):
                            self.session = MplsLdp.Vrfs.Vrf.Global_.Session()
                            self.session.parent = self
                            self._children_name_map["session"] = "session"
                        return self.session

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "graceful-restart" or name == "neighbor" or name == "session" or name == "router-id"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "router-id"):
                        self.router_id = value
                        self.router_id.value_namespace = name_space
                        self.router_id.value_namespace_prefix = name_space_prefix


            class Afs(Entity):
                """
                Address Family specific configuration for MPLS
                LDP vrf
                
                .. attribute:: af
                
                	Configure data for given Address Family
                	**type**\: list of    :py:class:`Af <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.Vrfs.Vrf.Afs.Af>`
                
                

                """

                _prefix = 'mpls-ldp-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(MplsLdp.Vrfs.Vrf.Afs, self).__init__()

                    self.yang_name = "afs"
                    self.yang_parent_name = "vrf"

                    self.af = YList(self)

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in () and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(MplsLdp.Vrfs.Vrf.Afs, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(MplsLdp.Vrfs.Vrf.Afs, self).__setattr__(name, value)


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
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(MplsLdp.Vrfs.Vrf.Afs.Af, self).__init__()

                        self.yang_name = "af"
                        self.yang_parent_name = "afs"

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

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("af_name",
                                        "enable") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(MplsLdp.Vrfs.Vrf.Afs.Af, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(MplsLdp.Vrfs.Vrf.Afs.Af, self).__setattr__(name, value)


                    class Discovery(Entity):
                        """
                        Configure Discovery parameters
                        
                        .. attribute:: transport_address
                        
                        	Global discovery transport address for address family
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'mpls-ldp-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(MplsLdp.Vrfs.Vrf.Afs.Af.Discovery, self).__init__()

                            self.yang_name = "discovery"
                            self.yang_parent_name = "af"

                            self.transport_address = YLeaf(YType.str, "transport-address")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("transport_address") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(MplsLdp.Vrfs.Vrf.Afs.Af.Discovery, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(MplsLdp.Vrfs.Vrf.Afs.Af.Discovery, self).__setattr__(name, value)

                        def has_data(self):
                            return self.transport_address.is_set

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.transport_address.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "discovery" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.transport_address.is_set or self.transport_address.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.transport_address.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "transport-address"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "transport-address"):
                                self.transport_address = value
                                self.transport_address.value_namespace = name_space
                                self.transport_address.value_namespace_prefix = name_space_prefix


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
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(MplsLdp.Vrfs.Vrf.Afs.Af.Label, self).__init__()

                            self.yang_name = "label"
                            self.yang_parent_name = "af"

                            self.local = MplsLdp.Vrfs.Vrf.Afs.Af.Label.Local()
                            self.local.parent = self
                            self._children_name_map["local"] = "local"
                            self._children_yang_names.add("local")

                            self.remote = MplsLdp.Vrfs.Vrf.Afs.Af.Label.Remote()
                            self.remote.parent = self
                            self._children_name_map["remote"] = "remote"
                            self._children_yang_names.add("remote")


                        class Remote(Entity):
                            """
                            Configure remote/peer label policies and
                            control
                            
                            .. attribute:: accept
                            
                            	Configure inbound label acceptance
                            	**type**\:   :py:class:`Accept <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.Vrfs.Vrf.Afs.Af.Label.Remote.Accept>`
                            
                            

                            """

                            _prefix = 'mpls-ldp-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(MplsLdp.Vrfs.Vrf.Afs.Af.Label.Remote, self).__init__()

                                self.yang_name = "remote"
                                self.yang_parent_name = "label"

                                self.accept = MplsLdp.Vrfs.Vrf.Afs.Af.Label.Remote.Accept()
                                self.accept.parent = self
                                self._children_name_map["accept"] = "accept"
                                self._children_yang_names.add("accept")


                            class Accept(Entity):
                                """
                                Configure inbound label acceptance
                                
                                .. attribute:: peer_accept_policies
                                
                                	Configuration related to Neighbors for inbound label acceptance
                                	**type**\:   :py:class:`PeerAcceptPolicies <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.Vrfs.Vrf.Afs.Af.Label.Remote.Accept.PeerAcceptPolicies>`
                                
                                

                                """

                                _prefix = 'mpls-ldp-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(MplsLdp.Vrfs.Vrf.Afs.Af.Label.Remote.Accept, self).__init__()

                                    self.yang_name = "accept"
                                    self.yang_parent_name = "remote"

                                    self.peer_accept_policies = MplsLdp.Vrfs.Vrf.Afs.Af.Label.Remote.Accept.PeerAcceptPolicies()
                                    self.peer_accept_policies.parent = self
                                    self._children_name_map["peer_accept_policies"] = "peer-accept-policies"
                                    self._children_yang_names.add("peer-accept-policies")


                                class PeerAcceptPolicies(Entity):
                                    """
                                    Configuration related to Neighbors for
                                    inbound label acceptance
                                    
                                    .. attribute:: peer_accept_policy
                                    
                                    	Control acceptasnce of labels from a neighbor for prefix(es) using ACL
                                    	**type**\: list of    :py:class:`PeerAcceptPolicy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.Vrfs.Vrf.Afs.Af.Label.Remote.Accept.PeerAcceptPolicies.PeerAcceptPolicy>`
                                    
                                    

                                    """

                                    _prefix = 'mpls-ldp-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(MplsLdp.Vrfs.Vrf.Afs.Af.Label.Remote.Accept.PeerAcceptPolicies, self).__init__()

                                        self.yang_name = "peer-accept-policies"
                                        self.yang_parent_name = "accept"

                                        self.peer_accept_policy = YList(self)

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in () and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(MplsLdp.Vrfs.Vrf.Afs.Af.Label.Remote.Accept.PeerAcceptPolicies, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(MplsLdp.Vrfs.Vrf.Afs.Af.Label.Remote.Accept.PeerAcceptPolicies, self).__setattr__(name, value)


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
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(MplsLdp.Vrfs.Vrf.Afs.Af.Label.Remote.Accept.PeerAcceptPolicies.PeerAcceptPolicy, self).__init__()

                                            self.yang_name = "peer-accept-policy"
                                            self.yang_parent_name = "peer-accept-policies"

                                            self.label_space_id = YLeaf(YType.uint32, "label-space-id")

                                            self.peer_accept_policy_data = MplsLdp.Vrfs.Vrf.Afs.Af.Label.Remote.Accept.PeerAcceptPolicies.PeerAcceptPolicy.PeerAcceptPolicyData()
                                            self.peer_accept_policy_data.parent = self
                                            self._children_name_map["peer_accept_policy_data"] = "peer-accept-policy-data"
                                            self._children_yang_names.add("peer-accept-policy-data")

                                            self.lsr_id = YList(self)

                                        def __setattr__(self, name, value):
                                            self._check_monkey_patching_error(name, value)
                                            with _handle_type_error():
                                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                        "Please use list append or extend method."
                                                                        .format(value))
                                                if isinstance(value, Enum.YLeaf):
                                                    value = value.name
                                                if name in ("label_space_id") and name in self.__dict__:
                                                    if isinstance(value, YLeaf):
                                                        self.__dict__[name].set(value.get())
                                                    elif isinstance(value, YLeafList):
                                                        super(MplsLdp.Vrfs.Vrf.Afs.Af.Label.Remote.Accept.PeerAcceptPolicies.PeerAcceptPolicy, self).__setattr__(name, value)
                                                    else:
                                                        self.__dict__[name].set(value)
                                                else:
                                                    if hasattr(value, "parent") and name != "parent":
                                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                            value.parent = self
                                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                                            value.parent = self
                                                    super(MplsLdp.Vrfs.Vrf.Afs.Af.Label.Remote.Accept.PeerAcceptPolicies.PeerAcceptPolicy, self).__setattr__(name, value)


                                        class PeerAcceptPolicyData(Entity):
                                            """
                                            Data container.
                                            
                                            .. attribute:: prefix_acl_name
                                            
                                            	Name of prefix ACL
                                            	**type**\:  str
                                            
                                            	**mandatory**\: True
                                            
                                            

                                            """

                                            _prefix = 'mpls-ldp-cfg'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                super(MplsLdp.Vrfs.Vrf.Afs.Af.Label.Remote.Accept.PeerAcceptPolicies.PeerAcceptPolicy.PeerAcceptPolicyData, self).__init__()

                                                self.yang_name = "peer-accept-policy-data"
                                                self.yang_parent_name = "peer-accept-policy"

                                                self.prefix_acl_name = YLeaf(YType.str, "prefix-acl-name")

                                            def __setattr__(self, name, value):
                                                self._check_monkey_patching_error(name, value)
                                                with _handle_type_error():
                                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                            "Please use list append or extend method."
                                                                            .format(value))
                                                    if isinstance(value, Enum.YLeaf):
                                                        value = value.name
                                                    if name in ("prefix_acl_name") and name in self.__dict__:
                                                        if isinstance(value, YLeaf):
                                                            self.__dict__[name].set(value.get())
                                                        elif isinstance(value, YLeafList):
                                                            super(MplsLdp.Vrfs.Vrf.Afs.Af.Label.Remote.Accept.PeerAcceptPolicies.PeerAcceptPolicy.PeerAcceptPolicyData, self).__setattr__(name, value)
                                                        else:
                                                            self.__dict__[name].set(value)
                                                    else:
                                                        if hasattr(value, "parent") and name != "parent":
                                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                                value.parent = self
                                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                                value.parent = self
                                                        super(MplsLdp.Vrfs.Vrf.Afs.Af.Label.Remote.Accept.PeerAcceptPolicies.PeerAcceptPolicy.PeerAcceptPolicyData, self).__setattr__(name, value)

                                            def has_data(self):
                                                return self.prefix_acl_name.is_set

                                            def has_operation(self):
                                                return (
                                                    self.yfilter != YFilter.not_set or
                                                    self.prefix_acl_name.yfilter != YFilter.not_set)

                                            def get_segment_path(self):
                                                path_buffer = ""
                                                path_buffer = "peer-accept-policy-data" + path_buffer

                                                return path_buffer

                                            def get_entity_path(self, ancestor):
                                                path_buffer = ""
                                                if (ancestor is None):
                                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                                else:
                                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                                leaf_name_data = LeafDataList()
                                                if (self.prefix_acl_name.is_set or self.prefix_acl_name.yfilter != YFilter.not_set):
                                                    leaf_name_data.append(self.prefix_acl_name.get_name_leafdata())

                                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                                return entity_path

                                            def get_child_by_name(self, child_yang_name, segment_path):
                                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                                if child is not None:
                                                    return child

                                                return None

                                            def has_leaf_or_child_of_name(self, name):
                                                if(name == "prefix-acl-name"):
                                                    return True
                                                return False

                                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                                if(value_path == "prefix-acl-name"):
                                                    self.prefix_acl_name = value
                                                    self.prefix_acl_name.value_namespace = name_space
                                                    self.prefix_acl_name.value_namespace_prefix = name_space_prefix


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
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                super(MplsLdp.Vrfs.Vrf.Afs.Af.Label.Remote.Accept.PeerAcceptPolicies.PeerAcceptPolicy.LsrId, self).__init__()

                                                self.yang_name = "lsr-id"
                                                self.yang_parent_name = "peer-accept-policy"

                                                self.lsr_id = YLeaf(YType.str, "lsr-id")

                                                self.prefix_acl_name = YLeaf(YType.str, "prefix-acl-name")

                                            def __setattr__(self, name, value):
                                                self._check_monkey_patching_error(name, value)
                                                with _handle_type_error():
                                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                            "Please use list append or extend method."
                                                                            .format(value))
                                                    if isinstance(value, Enum.YLeaf):
                                                        value = value.name
                                                    if name in ("lsr_id",
                                                                "prefix_acl_name") and name in self.__dict__:
                                                        if isinstance(value, YLeaf):
                                                            self.__dict__[name].set(value.get())
                                                        elif isinstance(value, YLeafList):
                                                            super(MplsLdp.Vrfs.Vrf.Afs.Af.Label.Remote.Accept.PeerAcceptPolicies.PeerAcceptPolicy.LsrId, self).__setattr__(name, value)
                                                        else:
                                                            self.__dict__[name].set(value)
                                                    else:
                                                        if hasattr(value, "parent") and name != "parent":
                                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                                value.parent = self
                                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                                value.parent = self
                                                        super(MplsLdp.Vrfs.Vrf.Afs.Af.Label.Remote.Accept.PeerAcceptPolicies.PeerAcceptPolicy.LsrId, self).__setattr__(name, value)

                                            def has_data(self):
                                                return (
                                                    self.lsr_id.is_set or
                                                    self.prefix_acl_name.is_set)

                                            def has_operation(self):
                                                return (
                                                    self.yfilter != YFilter.not_set or
                                                    self.lsr_id.yfilter != YFilter.not_set or
                                                    self.prefix_acl_name.yfilter != YFilter.not_set)

                                            def get_segment_path(self):
                                                path_buffer = ""
                                                path_buffer = "lsr-id" + "[lsr-id='" + self.lsr_id.get() + "']" + path_buffer

                                                return path_buffer

                                            def get_entity_path(self, ancestor):
                                                path_buffer = ""
                                                if (ancestor is None):
                                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                                else:
                                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                                leaf_name_data = LeafDataList()
                                                if (self.lsr_id.is_set or self.lsr_id.yfilter != YFilter.not_set):
                                                    leaf_name_data.append(self.lsr_id.get_name_leafdata())
                                                if (self.prefix_acl_name.is_set or self.prefix_acl_name.yfilter != YFilter.not_set):
                                                    leaf_name_data.append(self.prefix_acl_name.get_name_leafdata())

                                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                                return entity_path

                                            def get_child_by_name(self, child_yang_name, segment_path):
                                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                                if child is not None:
                                                    return child

                                                return None

                                            def has_leaf_or_child_of_name(self, name):
                                                if(name == "lsr-id" or name == "prefix-acl-name"):
                                                    return True
                                                return False

                                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                                if(value_path == "lsr-id"):
                                                    self.lsr_id = value
                                                    self.lsr_id.value_namespace = name_space
                                                    self.lsr_id.value_namespace_prefix = name_space_prefix
                                                if(value_path == "prefix-acl-name"):
                                                    self.prefix_acl_name = value
                                                    self.prefix_acl_name.value_namespace = name_space
                                                    self.prefix_acl_name.value_namespace_prefix = name_space_prefix

                                        def has_data(self):
                                            for c in self.lsr_id:
                                                if (c.has_data()):
                                                    return True
                                            return (
                                                self.label_space_id.is_set or
                                                (self.peer_accept_policy_data is not None and self.peer_accept_policy_data.has_data()))

                                        def has_operation(self):
                                            for c in self.lsr_id:
                                                if (c.has_operation()):
                                                    return True
                                            return (
                                                self.yfilter != YFilter.not_set or
                                                self.label_space_id.yfilter != YFilter.not_set or
                                                (self.peer_accept_policy_data is not None and self.peer_accept_policy_data.has_operation()))

                                        def get_segment_path(self):
                                            path_buffer = ""
                                            path_buffer = "peer-accept-policy" + "[label-space-id='" + self.label_space_id.get() + "']" + path_buffer

                                            return path_buffer

                                        def get_entity_path(self, ancestor):
                                            path_buffer = ""
                                            if (ancestor is None):
                                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                            else:
                                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                            leaf_name_data = LeafDataList()
                                            if (self.label_space_id.is_set or self.label_space_id.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.label_space_id.get_name_leafdata())

                                            entity_path = EntityPath(path_buffer, leaf_name_data)
                                            return entity_path

                                        def get_child_by_name(self, child_yang_name, segment_path):
                                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                            if child is not None:
                                                return child

                                            if (child_yang_name == "lsr-id"):
                                                for c in self.lsr_id:
                                                    segment = c.get_segment_path()
                                                    if (segment_path == segment):
                                                        return c
                                                c = MplsLdp.Vrfs.Vrf.Afs.Af.Label.Remote.Accept.PeerAcceptPolicies.PeerAcceptPolicy.LsrId()
                                                c.parent = self
                                                local_reference_key = "ydk::seg::%s" % segment_path
                                                self._local_refs[local_reference_key] = c
                                                self.lsr_id.append(c)
                                                return c

                                            if (child_yang_name == "peer-accept-policy-data"):
                                                if (self.peer_accept_policy_data is None):
                                                    self.peer_accept_policy_data = MplsLdp.Vrfs.Vrf.Afs.Af.Label.Remote.Accept.PeerAcceptPolicies.PeerAcceptPolicy.PeerAcceptPolicyData()
                                                    self.peer_accept_policy_data.parent = self
                                                    self._children_name_map["peer_accept_policy_data"] = "peer-accept-policy-data"
                                                return self.peer_accept_policy_data

                                            return None

                                        def has_leaf_or_child_of_name(self, name):
                                            if(name == "lsr-id" or name == "peer-accept-policy-data" or name == "label-space-id"):
                                                return True
                                            return False

                                        def set_value(self, value_path, value, name_space, name_space_prefix):
                                            if(value_path == "label-space-id"):
                                                self.label_space_id = value
                                                self.label_space_id.value_namespace = name_space
                                                self.label_space_id.value_namespace_prefix = name_space_prefix

                                    def has_data(self):
                                        for c in self.peer_accept_policy:
                                            if (c.has_data()):
                                                return True
                                        return False

                                    def has_operation(self):
                                        for c in self.peer_accept_policy:
                                            if (c.has_operation()):
                                                return True
                                        return self.yfilter != YFilter.not_set

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "peer-accept-policies" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        if (child_yang_name == "peer-accept-policy"):
                                            for c in self.peer_accept_policy:
                                                segment = c.get_segment_path()
                                                if (segment_path == segment):
                                                    return c
                                            c = MplsLdp.Vrfs.Vrf.Afs.Af.Label.Remote.Accept.PeerAcceptPolicies.PeerAcceptPolicy()
                                            c.parent = self
                                            local_reference_key = "ydk::seg::%s" % segment_path
                                            self._local_refs[local_reference_key] = c
                                            self.peer_accept_policy.append(c)
                                            return c

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "peer-accept-policy"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        pass

                                def has_data(self):
                                    return (self.peer_accept_policies is not None and self.peer_accept_policies.has_data())

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        (self.peer_accept_policies is not None and self.peer_accept_policies.has_operation()))

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "accept" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    if (child_yang_name == "peer-accept-policies"):
                                        if (self.peer_accept_policies is None):
                                            self.peer_accept_policies = MplsLdp.Vrfs.Vrf.Afs.Af.Label.Remote.Accept.PeerAcceptPolicies()
                                            self.peer_accept_policies.parent = self
                                            self._children_name_map["peer_accept_policies"] = "peer-accept-policies"
                                        return self.peer_accept_policies

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "peer-accept-policies"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    pass

                            def has_data(self):
                                return (self.accept is not None and self.accept.has_data())

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    (self.accept is not None and self.accept.has_operation()))

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "remote" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                if (child_yang_name == "accept"):
                                    if (self.accept is None):
                                        self.accept = MplsLdp.Vrfs.Vrf.Afs.Af.Label.Remote.Accept()
                                        self.accept.parent = self
                                        self._children_name_map["accept"] = "accept"
                                    return self.accept

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "accept"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                pass


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
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(MplsLdp.Vrfs.Vrf.Afs.Af.Label.Local, self).__init__()

                                self.yang_name = "local"
                                self.yang_parent_name = "label"

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

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("default_route",
                                                "implicit_null_override") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(MplsLdp.Vrfs.Vrf.Afs.Af.Label.Local, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(MplsLdp.Vrfs.Vrf.Afs.Af.Label.Local, self).__setattr__(name, value)


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
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(MplsLdp.Vrfs.Vrf.Afs.Af.Label.Local.Advertise, self).__init__()

                                    self.yang_name = "advertise"
                                    self.yang_parent_name = "local"

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

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("disable") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(MplsLdp.Vrfs.Vrf.Afs.Af.Label.Local.Advertise, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(MplsLdp.Vrfs.Vrf.Afs.Af.Label.Local.Advertise, self).__setattr__(name, value)


                                class PeerAdvertisePolicies(Entity):
                                    """
                                    Configure peer centric outbound label
                                    advertisement using ACL
                                    
                                    .. attribute:: peer_advertise_policy
                                    
                                    	Control advertisement of prefix(es) using ACL
                                    	**type**\: list of    :py:class:`PeerAdvertisePolicy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.Vrfs.Vrf.Afs.Af.Label.Local.Advertise.PeerAdvertisePolicies.PeerAdvertisePolicy>`
                                    
                                    

                                    """

                                    _prefix = 'mpls-ldp-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(MplsLdp.Vrfs.Vrf.Afs.Af.Label.Local.Advertise.PeerAdvertisePolicies, self).__init__()

                                        self.yang_name = "peer-advertise-policies"
                                        self.yang_parent_name = "advertise"

                                        self.peer_advertise_policy = YList(self)

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in () and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(MplsLdp.Vrfs.Vrf.Afs.Af.Label.Local.Advertise.PeerAdvertisePolicies, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(MplsLdp.Vrfs.Vrf.Afs.Af.Label.Local.Advertise.PeerAdvertisePolicies, self).__setattr__(name, value)


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
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(MplsLdp.Vrfs.Vrf.Afs.Af.Label.Local.Advertise.PeerAdvertisePolicies.PeerAdvertisePolicy, self).__init__()

                                            self.yang_name = "peer-advertise-policy"
                                            self.yang_parent_name = "peer-advertise-policies"

                                            self.label_space_id = YLeaf(YType.uint32, "label-space-id")

                                            self.peer_advertise_policy_data = MplsLdp.Vrfs.Vrf.Afs.Af.Label.Local.Advertise.PeerAdvertisePolicies.PeerAdvertisePolicy.PeerAdvertisePolicyData()
                                            self.peer_advertise_policy_data.parent = self
                                            self._children_name_map["peer_advertise_policy_data"] = "peer-advertise-policy-data"
                                            self._children_yang_names.add("peer-advertise-policy-data")

                                            self.lsr_id = YList(self)

                                        def __setattr__(self, name, value):
                                            self._check_monkey_patching_error(name, value)
                                            with _handle_type_error():
                                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                        "Please use list append or extend method."
                                                                        .format(value))
                                                if isinstance(value, Enum.YLeaf):
                                                    value = value.name
                                                if name in ("label_space_id") and name in self.__dict__:
                                                    if isinstance(value, YLeaf):
                                                        self.__dict__[name].set(value.get())
                                                    elif isinstance(value, YLeafList):
                                                        super(MplsLdp.Vrfs.Vrf.Afs.Af.Label.Local.Advertise.PeerAdvertisePolicies.PeerAdvertisePolicy, self).__setattr__(name, value)
                                                    else:
                                                        self.__dict__[name].set(value)
                                                else:
                                                    if hasattr(value, "parent") and name != "parent":
                                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                            value.parent = self
                                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                                            value.parent = self
                                                    super(MplsLdp.Vrfs.Vrf.Afs.Af.Label.Local.Advertise.PeerAdvertisePolicies.PeerAdvertisePolicy, self).__setattr__(name, value)


                                        class PeerAdvertisePolicyData(Entity):
                                            """
                                            Data container.
                                            
                                            .. attribute:: prefix_acl_name
                                            
                                            	Name of prefix ACL
                                            	**type**\:  str
                                            
                                            	**mandatory**\: True
                                            
                                            

                                            """

                                            _prefix = 'mpls-ldp-cfg'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                super(MplsLdp.Vrfs.Vrf.Afs.Af.Label.Local.Advertise.PeerAdvertisePolicies.PeerAdvertisePolicy.PeerAdvertisePolicyData, self).__init__()

                                                self.yang_name = "peer-advertise-policy-data"
                                                self.yang_parent_name = "peer-advertise-policy"

                                                self.prefix_acl_name = YLeaf(YType.str, "prefix-acl-name")

                                            def __setattr__(self, name, value):
                                                self._check_monkey_patching_error(name, value)
                                                with _handle_type_error():
                                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                            "Please use list append or extend method."
                                                                            .format(value))
                                                    if isinstance(value, Enum.YLeaf):
                                                        value = value.name
                                                    if name in ("prefix_acl_name") and name in self.__dict__:
                                                        if isinstance(value, YLeaf):
                                                            self.__dict__[name].set(value.get())
                                                        elif isinstance(value, YLeafList):
                                                            super(MplsLdp.Vrfs.Vrf.Afs.Af.Label.Local.Advertise.PeerAdvertisePolicies.PeerAdvertisePolicy.PeerAdvertisePolicyData, self).__setattr__(name, value)
                                                        else:
                                                            self.__dict__[name].set(value)
                                                    else:
                                                        if hasattr(value, "parent") and name != "parent":
                                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                                value.parent = self
                                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                                value.parent = self
                                                        super(MplsLdp.Vrfs.Vrf.Afs.Af.Label.Local.Advertise.PeerAdvertisePolicies.PeerAdvertisePolicy.PeerAdvertisePolicyData, self).__setattr__(name, value)

                                            def has_data(self):
                                                return self.prefix_acl_name.is_set

                                            def has_operation(self):
                                                return (
                                                    self.yfilter != YFilter.not_set or
                                                    self.prefix_acl_name.yfilter != YFilter.not_set)

                                            def get_segment_path(self):
                                                path_buffer = ""
                                                path_buffer = "peer-advertise-policy-data" + path_buffer

                                                return path_buffer

                                            def get_entity_path(self, ancestor):
                                                path_buffer = ""
                                                if (ancestor is None):
                                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                                else:
                                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                                leaf_name_data = LeafDataList()
                                                if (self.prefix_acl_name.is_set or self.prefix_acl_name.yfilter != YFilter.not_set):
                                                    leaf_name_data.append(self.prefix_acl_name.get_name_leafdata())

                                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                                return entity_path

                                            def get_child_by_name(self, child_yang_name, segment_path):
                                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                                if child is not None:
                                                    return child

                                                return None

                                            def has_leaf_or_child_of_name(self, name):
                                                if(name == "prefix-acl-name"):
                                                    return True
                                                return False

                                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                                if(value_path == "prefix-acl-name"):
                                                    self.prefix_acl_name = value
                                                    self.prefix_acl_name.value_namespace = name_space
                                                    self.prefix_acl_name.value_namespace_prefix = name_space_prefix


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
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                super(MplsLdp.Vrfs.Vrf.Afs.Af.Label.Local.Advertise.PeerAdvertisePolicies.PeerAdvertisePolicy.LsrId, self).__init__()

                                                self.yang_name = "lsr-id"
                                                self.yang_parent_name = "peer-advertise-policy"

                                                self.lsr_id = YLeaf(YType.str, "lsr-id")

                                                self.prefix_acl_name = YLeaf(YType.str, "prefix-acl-name")

                                            def __setattr__(self, name, value):
                                                self._check_monkey_patching_error(name, value)
                                                with _handle_type_error():
                                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                            "Please use list append or extend method."
                                                                            .format(value))
                                                    if isinstance(value, Enum.YLeaf):
                                                        value = value.name
                                                    if name in ("lsr_id",
                                                                "prefix_acl_name") and name in self.__dict__:
                                                        if isinstance(value, YLeaf):
                                                            self.__dict__[name].set(value.get())
                                                        elif isinstance(value, YLeafList):
                                                            super(MplsLdp.Vrfs.Vrf.Afs.Af.Label.Local.Advertise.PeerAdvertisePolicies.PeerAdvertisePolicy.LsrId, self).__setattr__(name, value)
                                                        else:
                                                            self.__dict__[name].set(value)
                                                    else:
                                                        if hasattr(value, "parent") and name != "parent":
                                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                                value.parent = self
                                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                                value.parent = self
                                                        super(MplsLdp.Vrfs.Vrf.Afs.Af.Label.Local.Advertise.PeerAdvertisePolicies.PeerAdvertisePolicy.LsrId, self).__setattr__(name, value)

                                            def has_data(self):
                                                return (
                                                    self.lsr_id.is_set or
                                                    self.prefix_acl_name.is_set)

                                            def has_operation(self):
                                                return (
                                                    self.yfilter != YFilter.not_set or
                                                    self.lsr_id.yfilter != YFilter.not_set or
                                                    self.prefix_acl_name.yfilter != YFilter.not_set)

                                            def get_segment_path(self):
                                                path_buffer = ""
                                                path_buffer = "lsr-id" + "[lsr-id='" + self.lsr_id.get() + "']" + path_buffer

                                                return path_buffer

                                            def get_entity_path(self, ancestor):
                                                path_buffer = ""
                                                if (ancestor is None):
                                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                                else:
                                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                                leaf_name_data = LeafDataList()
                                                if (self.lsr_id.is_set or self.lsr_id.yfilter != YFilter.not_set):
                                                    leaf_name_data.append(self.lsr_id.get_name_leafdata())
                                                if (self.prefix_acl_name.is_set or self.prefix_acl_name.yfilter != YFilter.not_set):
                                                    leaf_name_data.append(self.prefix_acl_name.get_name_leafdata())

                                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                                return entity_path

                                            def get_child_by_name(self, child_yang_name, segment_path):
                                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                                if child is not None:
                                                    return child

                                                return None

                                            def has_leaf_or_child_of_name(self, name):
                                                if(name == "lsr-id" or name == "prefix-acl-name"):
                                                    return True
                                                return False

                                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                                if(value_path == "lsr-id"):
                                                    self.lsr_id = value
                                                    self.lsr_id.value_namespace = name_space
                                                    self.lsr_id.value_namespace_prefix = name_space_prefix
                                                if(value_path == "prefix-acl-name"):
                                                    self.prefix_acl_name = value
                                                    self.prefix_acl_name.value_namespace = name_space
                                                    self.prefix_acl_name.value_namespace_prefix = name_space_prefix

                                        def has_data(self):
                                            for c in self.lsr_id:
                                                if (c.has_data()):
                                                    return True
                                            return (
                                                self.label_space_id.is_set or
                                                (self.peer_advertise_policy_data is not None and self.peer_advertise_policy_data.has_data()))

                                        def has_operation(self):
                                            for c in self.lsr_id:
                                                if (c.has_operation()):
                                                    return True
                                            return (
                                                self.yfilter != YFilter.not_set or
                                                self.label_space_id.yfilter != YFilter.not_set or
                                                (self.peer_advertise_policy_data is not None and self.peer_advertise_policy_data.has_operation()))

                                        def get_segment_path(self):
                                            path_buffer = ""
                                            path_buffer = "peer-advertise-policy" + "[label-space-id='" + self.label_space_id.get() + "']" + path_buffer

                                            return path_buffer

                                        def get_entity_path(self, ancestor):
                                            path_buffer = ""
                                            if (ancestor is None):
                                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                            else:
                                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                            leaf_name_data = LeafDataList()
                                            if (self.label_space_id.is_set or self.label_space_id.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.label_space_id.get_name_leafdata())

                                            entity_path = EntityPath(path_buffer, leaf_name_data)
                                            return entity_path

                                        def get_child_by_name(self, child_yang_name, segment_path):
                                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                            if child is not None:
                                                return child

                                            if (child_yang_name == "lsr-id"):
                                                for c in self.lsr_id:
                                                    segment = c.get_segment_path()
                                                    if (segment_path == segment):
                                                        return c
                                                c = MplsLdp.Vrfs.Vrf.Afs.Af.Label.Local.Advertise.PeerAdvertisePolicies.PeerAdvertisePolicy.LsrId()
                                                c.parent = self
                                                local_reference_key = "ydk::seg::%s" % segment_path
                                                self._local_refs[local_reference_key] = c
                                                self.lsr_id.append(c)
                                                return c

                                            if (child_yang_name == "peer-advertise-policy-data"):
                                                if (self.peer_advertise_policy_data is None):
                                                    self.peer_advertise_policy_data = MplsLdp.Vrfs.Vrf.Afs.Af.Label.Local.Advertise.PeerAdvertisePolicies.PeerAdvertisePolicy.PeerAdvertisePolicyData()
                                                    self.peer_advertise_policy_data.parent = self
                                                    self._children_name_map["peer_advertise_policy_data"] = "peer-advertise-policy-data"
                                                return self.peer_advertise_policy_data

                                            return None

                                        def has_leaf_or_child_of_name(self, name):
                                            if(name == "lsr-id" or name == "peer-advertise-policy-data" or name == "label-space-id"):
                                                return True
                                            return False

                                        def set_value(self, value_path, value, name_space, name_space_prefix):
                                            if(value_path == "label-space-id"):
                                                self.label_space_id = value
                                                self.label_space_id.value_namespace = name_space
                                                self.label_space_id.value_namespace_prefix = name_space_prefix

                                    def has_data(self):
                                        for c in self.peer_advertise_policy:
                                            if (c.has_data()):
                                                return True
                                        return False

                                    def has_operation(self):
                                        for c in self.peer_advertise_policy:
                                            if (c.has_operation()):
                                                return True
                                        return self.yfilter != YFilter.not_set

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "peer-advertise-policies" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        if (child_yang_name == "peer-advertise-policy"):
                                            for c in self.peer_advertise_policy:
                                                segment = c.get_segment_path()
                                                if (segment_path == segment):
                                                    return c
                                            c = MplsLdp.Vrfs.Vrf.Afs.Af.Label.Local.Advertise.PeerAdvertisePolicies.PeerAdvertisePolicy()
                                            c.parent = self
                                            local_reference_key = "ydk::seg::%s" % segment_path
                                            self._local_refs[local_reference_key] = c
                                            self.peer_advertise_policy.append(c)
                                            return c

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "peer-advertise-policy"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        pass


                                class Interfaces(Entity):
                                    """
                                    Configure outbound label advertisement
                                    for an interface
                                    
                                    .. attribute:: interface
                                    
                                    	Control advertisement of interface's host IP address
                                    	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.Vrfs.Vrf.Afs.Af.Label.Local.Advertise.Interfaces.Interface>`
                                    
                                    

                                    """

                                    _prefix = 'mpls-ldp-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(MplsLdp.Vrfs.Vrf.Afs.Af.Label.Local.Advertise.Interfaces, self).__init__()

                                        self.yang_name = "interfaces"
                                        self.yang_parent_name = "advertise"

                                        self.interface = YList(self)

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in () and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(MplsLdp.Vrfs.Vrf.Afs.Af.Label.Local.Advertise.Interfaces, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(MplsLdp.Vrfs.Vrf.Afs.Af.Label.Local.Advertise.Interfaces, self).__setattr__(name, value)


                                    class Interface(Entity):
                                        """
                                        Control advertisement of interface's
                                        host IP address
                                        
                                        .. attribute:: interface_name  <key>
                                        
                                        	Name of interface
                                        	**type**\:  str
                                        
                                        	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                                        
                                        

                                        """

                                        _prefix = 'mpls-ldp-cfg'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(MplsLdp.Vrfs.Vrf.Afs.Af.Label.Local.Advertise.Interfaces.Interface, self).__init__()

                                            self.yang_name = "interface"
                                            self.yang_parent_name = "interfaces"

                                            self.interface_name = YLeaf(YType.str, "interface-name")

                                        def __setattr__(self, name, value):
                                            self._check_monkey_patching_error(name, value)
                                            with _handle_type_error():
                                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                        "Please use list append or extend method."
                                                                        .format(value))
                                                if isinstance(value, Enum.YLeaf):
                                                    value = value.name
                                                if name in ("interface_name") and name in self.__dict__:
                                                    if isinstance(value, YLeaf):
                                                        self.__dict__[name].set(value.get())
                                                    elif isinstance(value, YLeafList):
                                                        super(MplsLdp.Vrfs.Vrf.Afs.Af.Label.Local.Advertise.Interfaces.Interface, self).__setattr__(name, value)
                                                    else:
                                                        self.__dict__[name].set(value)
                                                else:
                                                    if hasattr(value, "parent") and name != "parent":
                                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                            value.parent = self
                                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                                            value.parent = self
                                                    super(MplsLdp.Vrfs.Vrf.Afs.Af.Label.Local.Advertise.Interfaces.Interface, self).__setattr__(name, value)

                                        def has_data(self):
                                            return self.interface_name.is_set

                                        def has_operation(self):
                                            return (
                                                self.yfilter != YFilter.not_set or
                                                self.interface_name.yfilter != YFilter.not_set)

                                        def get_segment_path(self):
                                            path_buffer = ""
                                            path_buffer = "interface" + "[interface-name='" + self.interface_name.get() + "']" + path_buffer

                                            return path_buffer

                                        def get_entity_path(self, ancestor):
                                            path_buffer = ""
                                            if (ancestor is None):
                                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                            else:
                                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                            leaf_name_data = LeafDataList()
                                            if (self.interface_name.is_set or self.interface_name.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.interface_name.get_name_leafdata())

                                            entity_path = EntityPath(path_buffer, leaf_name_data)
                                            return entity_path

                                        def get_child_by_name(self, child_yang_name, segment_path):
                                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                            if child is not None:
                                                return child

                                            return None

                                        def has_leaf_or_child_of_name(self, name):
                                            if(name == "interface-name"):
                                                return True
                                            return False

                                        def set_value(self, value_path, value, name_space, name_space_prefix):
                                            if(value_path == "interface-name"):
                                                self.interface_name = value
                                                self.interface_name.value_namespace = name_space
                                                self.interface_name.value_namespace_prefix = name_space_prefix

                                    def has_data(self):
                                        for c in self.interface:
                                            if (c.has_data()):
                                                return True
                                        return False

                                    def has_operation(self):
                                        for c in self.interface:
                                            if (c.has_operation()):
                                                return True
                                        return self.yfilter != YFilter.not_set

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "interfaces" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        if (child_yang_name == "interface"):
                                            for c in self.interface:
                                                segment = c.get_segment_path()
                                                if (segment_path == segment):
                                                    return c
                                            c = MplsLdp.Vrfs.Vrf.Afs.Af.Label.Local.Advertise.Interfaces.Interface()
                                            c.parent = self
                                            local_reference_key = "ydk::seg::%s" % segment_path
                                            self._local_refs[local_reference_key] = c
                                            self.interface.append(c)
                                            return c

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "interface"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        pass


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
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(MplsLdp.Vrfs.Vrf.Afs.Af.Label.Local.Advertise.ExplicitNull, self).__init__()

                                        self.yang_name = "explicit-null"
                                        self.yang_parent_name = "advertise"

                                        self.explicit_null_type = YLeaf(YType.enumeration, "explicit-null-type")

                                        self.peer_acl_name = YLeaf(YType.str, "peer-acl-name")

                                        self.prefix_acl_name = YLeaf(YType.str, "prefix-acl-name")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("explicit_null_type",
                                                        "peer_acl_name",
                                                        "prefix_acl_name") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(MplsLdp.Vrfs.Vrf.Afs.Af.Label.Local.Advertise.ExplicitNull, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(MplsLdp.Vrfs.Vrf.Afs.Af.Label.Local.Advertise.ExplicitNull, self).__setattr__(name, value)

                                    def has_data(self):
                                        return (
                                            self.explicit_null_type.is_set or
                                            self.peer_acl_name.is_set or
                                            self.prefix_acl_name.is_set)

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.explicit_null_type.yfilter != YFilter.not_set or
                                            self.peer_acl_name.yfilter != YFilter.not_set or
                                            self.prefix_acl_name.yfilter != YFilter.not_set)

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "explicit-null" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()
                                        if (self.explicit_null_type.is_set or self.explicit_null_type.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.explicit_null_type.get_name_leafdata())
                                        if (self.peer_acl_name.is_set or self.peer_acl_name.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.peer_acl_name.get_name_leafdata())
                                        if (self.prefix_acl_name.is_set or self.prefix_acl_name.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.prefix_acl_name.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "explicit-null-type" or name == "peer-acl-name" or name == "prefix-acl-name"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "explicit-null-type"):
                                            self.explicit_null_type = value
                                            self.explicit_null_type.value_namespace = name_space
                                            self.explicit_null_type.value_namespace_prefix = name_space_prefix
                                        if(value_path == "peer-acl-name"):
                                            self.peer_acl_name = value
                                            self.peer_acl_name.value_namespace = name_space
                                            self.peer_acl_name.value_namespace_prefix = name_space_prefix
                                        if(value_path == "prefix-acl-name"):
                                            self.prefix_acl_name = value
                                            self.prefix_acl_name.value_namespace = name_space
                                            self.prefix_acl_name.value_namespace_prefix = name_space_prefix

                                def has_data(self):
                                    return (
                                        self.disable.is_set or
                                        (self.explicit_null is not None and self.explicit_null.has_data()) or
                                        (self.interfaces is not None and self.interfaces.has_data()) or
                                        (self.peer_advertise_policies is not None and self.peer_advertise_policies.has_data()))

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.disable.yfilter != YFilter.not_set or
                                        (self.explicit_null is not None and self.explicit_null.has_operation()) or
                                        (self.interfaces is not None and self.interfaces.has_operation()) or
                                        (self.peer_advertise_policies is not None and self.peer_advertise_policies.has_operation()))

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "advertise" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.disable.is_set or self.disable.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.disable.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    if (child_yang_name == "explicit-null"):
                                        if (self.explicit_null is None):
                                            self.explicit_null = MplsLdp.Vrfs.Vrf.Afs.Af.Label.Local.Advertise.ExplicitNull()
                                            self.explicit_null.parent = self
                                            self._children_name_map["explicit_null"] = "explicit-null"
                                        return self.explicit_null

                                    if (child_yang_name == "interfaces"):
                                        if (self.interfaces is None):
                                            self.interfaces = MplsLdp.Vrfs.Vrf.Afs.Af.Label.Local.Advertise.Interfaces()
                                            self.interfaces.parent = self
                                            self._children_name_map["interfaces"] = "interfaces"
                                        return self.interfaces

                                    if (child_yang_name == "peer-advertise-policies"):
                                        if (self.peer_advertise_policies is None):
                                            self.peer_advertise_policies = MplsLdp.Vrfs.Vrf.Afs.Af.Label.Local.Advertise.PeerAdvertisePolicies()
                                            self.peer_advertise_policies.parent = self
                                            self._children_name_map["peer_advertise_policies"] = "peer-advertise-policies"
                                        return self.peer_advertise_policies

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "explicit-null" or name == "interfaces" or name == "peer-advertise-policies" or name == "disable"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "disable"):
                                        self.disable = value
                                        self.disable.value_namespace = name_space
                                        self.disable.value_namespace_prefix = name_space_prefix


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
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(MplsLdp.Vrfs.Vrf.Afs.Af.Label.Local.Allocate, self).__init__()

                                    self.yang_name = "allocate"
                                    self.yang_parent_name = "local"

                                    self.allocation_type = YLeaf(YType.enumeration, "allocation-type")

                                    self.prefix_acl_name = YLeaf(YType.str, "prefix-acl-name")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("allocation_type",
                                                    "prefix_acl_name") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(MplsLdp.Vrfs.Vrf.Afs.Af.Label.Local.Allocate, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(MplsLdp.Vrfs.Vrf.Afs.Af.Label.Local.Allocate, self).__setattr__(name, value)

                                def has_data(self):
                                    return (
                                        self.allocation_type.is_set or
                                        self.prefix_acl_name.is_set)

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.allocation_type.yfilter != YFilter.not_set or
                                        self.prefix_acl_name.yfilter != YFilter.not_set)

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "allocate" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.allocation_type.is_set or self.allocation_type.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.allocation_type.get_name_leafdata())
                                    if (self.prefix_acl_name.is_set or self.prefix_acl_name.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.prefix_acl_name.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "allocation-type" or name == "prefix-acl-name"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "allocation-type"):
                                        self.allocation_type = value
                                        self.allocation_type.value_namespace = name_space
                                        self.allocation_type.value_namespace_prefix = name_space_prefix
                                    if(value_path == "prefix-acl-name"):
                                        self.prefix_acl_name = value
                                        self.prefix_acl_name.value_namespace = name_space
                                        self.prefix_acl_name.value_namespace_prefix = name_space_prefix

                            def has_data(self):
                                return (
                                    self.default_route.is_set or
                                    self.implicit_null_override.is_set or
                                    (self.advertise is not None and self.advertise.has_data()) or
                                    (self.allocate is not None and self.allocate.has_data()))

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.default_route.yfilter != YFilter.not_set or
                                    self.implicit_null_override.yfilter != YFilter.not_set or
                                    (self.advertise is not None and self.advertise.has_operation()) or
                                    (self.allocate is not None and self.allocate.has_operation()))

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "local" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.default_route.is_set or self.default_route.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.default_route.get_name_leafdata())
                                if (self.implicit_null_override.is_set or self.implicit_null_override.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.implicit_null_override.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                if (child_yang_name == "advertise"):
                                    if (self.advertise is None):
                                        self.advertise = MplsLdp.Vrfs.Vrf.Afs.Af.Label.Local.Advertise()
                                        self.advertise.parent = self
                                        self._children_name_map["advertise"] = "advertise"
                                    return self.advertise

                                if (child_yang_name == "allocate"):
                                    if (self.allocate is None):
                                        self.allocate = MplsLdp.Vrfs.Vrf.Afs.Af.Label.Local.Allocate()
                                        self.allocate.parent = self
                                        self._children_name_map["allocate"] = "allocate"
                                    return self.allocate

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "advertise" or name == "allocate" or name == "default-route" or name == "implicit-null-override"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "default-route"):
                                    self.default_route = value
                                    self.default_route.value_namespace = name_space
                                    self.default_route.value_namespace_prefix = name_space_prefix
                                if(value_path == "implicit-null-override"):
                                    self.implicit_null_override = value
                                    self.implicit_null_override.value_namespace = name_space
                                    self.implicit_null_override.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            return (
                                (self.local is not None and self.local.has_data()) or
                                (self.remote is not None and self.remote.has_data()))

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                (self.local is not None and self.local.has_operation()) or
                                (self.remote is not None and self.remote.has_operation()))

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "label" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "local"):
                                if (self.local is None):
                                    self.local = MplsLdp.Vrfs.Vrf.Afs.Af.Label.Local()
                                    self.local.parent = self
                                    self._children_name_map["local"] = "local"
                                return self.local

                            if (child_yang_name == "remote"):
                                if (self.remote is None):
                                    self.remote = MplsLdp.Vrfs.Vrf.Afs.Af.Label.Remote()
                                    self.remote.parent = self
                                    self._children_name_map["remote"] = "remote"
                                return self.remote

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "local" or name == "remote"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            pass

                    def has_data(self):
                        return (
                            self.af_name.is_set or
                            self.enable.is_set or
                            (self.discovery is not None and self.discovery.has_data()) or
                            (self.label is not None and self.label.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.af_name.yfilter != YFilter.not_set or
                            self.enable.yfilter != YFilter.not_set or
                            (self.discovery is not None and self.discovery.has_operation()) or
                            (self.label is not None and self.label.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "af" + "[af-name='" + self.af_name.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.af_name.is_set or self.af_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.af_name.get_name_leafdata())
                        if (self.enable.is_set or self.enable.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.enable.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "discovery"):
                            if (self.discovery is None):
                                self.discovery = MplsLdp.Vrfs.Vrf.Afs.Af.Discovery()
                                self.discovery.parent = self
                                self._children_name_map["discovery"] = "discovery"
                            return self.discovery

                        if (child_yang_name == "label"):
                            if (self.label is None):
                                self.label = MplsLdp.Vrfs.Vrf.Afs.Af.Label()
                                self.label.parent = self
                                self._children_name_map["label"] = "label"
                            return self.label

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "discovery" or name == "label" or name == "af-name" or name == "enable"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "af-name"):
                            self.af_name = value
                            self.af_name.value_namespace = name_space
                            self.af_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "enable"):
                            self.enable = value
                            self.enable.value_namespace = name_space
                            self.enable.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.af:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.af:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "afs" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "af"):
                        for c in self.af:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = MplsLdp.Vrfs.Vrf.Afs.Af()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.af.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "af"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class Interfaces(Entity):
                """
                MPLS LDP configuration pertaining to
                interfaces
                
                .. attribute:: interface
                
                	MPLS LDP configuration for a particular interface
                	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.Vrfs.Vrf.Interfaces.Interface>`
                
                

                """

                _prefix = 'mpls-ldp-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(MplsLdp.Vrfs.Vrf.Interfaces, self).__init__()

                    self.yang_name = "interfaces"
                    self.yang_parent_name = "vrf"

                    self.interface = YList(self)

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in () and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(MplsLdp.Vrfs.Vrf.Interfaces, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(MplsLdp.Vrfs.Vrf.Interfaces, self).__setattr__(name, value)


                class Interface(Entity):
                    """
                    MPLS LDP configuration for a particular
                    interface
                    
                    .. attribute:: interface_name  <key>
                    
                    	Name of interface
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: afs
                    
                    	Address Family specific configuration for MPLS LDP vrf intf
                    	**type**\:   :py:class:`Afs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.Vrfs.Vrf.Interfaces.Interface.Afs>`
                    
                    .. attribute:: enable
                    
                    	Enable Label Distribution Protocol (LDP) on thisinterface
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    

                    """

                    _prefix = 'mpls-ldp-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(MplsLdp.Vrfs.Vrf.Interfaces.Interface, self).__init__()

                        self.yang_name = "interface"
                        self.yang_parent_name = "interfaces"

                        self.interface_name = YLeaf(YType.str, "interface-name")

                        self.enable = YLeaf(YType.empty, "enable")

                        self.afs = MplsLdp.Vrfs.Vrf.Interfaces.Interface.Afs()
                        self.afs.parent = self
                        self._children_name_map["afs"] = "afs"
                        self._children_yang_names.add("afs")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("interface_name",
                                        "enable") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(MplsLdp.Vrfs.Vrf.Interfaces.Interface, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(MplsLdp.Vrfs.Vrf.Interfaces.Interface, self).__setattr__(name, value)


                    class Afs(Entity):
                        """
                        Address Family specific configuration for
                        MPLS LDP vrf intf
                        
                        .. attribute:: af
                        
                        	Configure data for given Address Family
                        	**type**\: list of    :py:class:`Af <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.Vrfs.Vrf.Interfaces.Interface.Afs.Af>`
                        
                        

                        """

                        _prefix = 'mpls-ldp-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(MplsLdp.Vrfs.Vrf.Interfaces.Interface.Afs, self).__init__()

                            self.yang_name = "afs"
                            self.yang_parent_name = "interface"

                            self.af = YList(self)

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in () and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(MplsLdp.Vrfs.Vrf.Interfaces.Interface.Afs, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(MplsLdp.Vrfs.Vrf.Interfaces.Interface.Afs, self).__setattr__(name, value)


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
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(MplsLdp.Vrfs.Vrf.Interfaces.Interface.Afs.Af, self).__init__()

                                self.yang_name = "af"
                                self.yang_parent_name = "afs"

                                self.af_name = YLeaf(YType.enumeration, "af-name")

                                self.enable = YLeaf(YType.empty, "enable")

                                self.discovery = MplsLdp.Vrfs.Vrf.Interfaces.Interface.Afs.Af.Discovery()
                                self.discovery.parent = self
                                self._children_name_map["discovery"] = "discovery"
                                self._children_yang_names.add("discovery")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("af_name",
                                                "enable") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(MplsLdp.Vrfs.Vrf.Interfaces.Interface.Afs.Af, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(MplsLdp.Vrfs.Vrf.Interfaces.Interface.Afs.Af, self).__setattr__(name, value)


                            class Discovery(Entity):
                                """
                                Configure interface discovery parameters
                                
                                .. attribute:: transport_address
                                
                                	MPLS LDP configuration for interface discovery transportaddress
                                	**type**\:   :py:class:`TransportAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.Vrfs.Vrf.Interfaces.Interface.Afs.Af.Discovery.TransportAddress>`
                                
                                

                                """

                                _prefix = 'mpls-ldp-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(MplsLdp.Vrfs.Vrf.Interfaces.Interface.Afs.Af.Discovery, self).__init__()

                                    self.yang_name = "discovery"
                                    self.yang_parent_name = "af"

                                    self.transport_address = MplsLdp.Vrfs.Vrf.Interfaces.Interface.Afs.Af.Discovery.TransportAddress()
                                    self.transport_address.parent = self
                                    self._children_name_map["transport_address"] = "transport-address"
                                    self._children_yang_names.add("transport-address")


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
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(MplsLdp.Vrfs.Vrf.Interfaces.Interface.Afs.Af.Discovery.TransportAddress, self).__init__()

                                        self.yang_name = "transport-address"
                                        self.yang_parent_name = "discovery"

                                        self.address = YLeaf(YType.str, "address")

                                        self.address_type = YLeaf(YType.enumeration, "address-type")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("address",
                                                        "address_type") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(MplsLdp.Vrfs.Vrf.Interfaces.Interface.Afs.Af.Discovery.TransportAddress, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(MplsLdp.Vrfs.Vrf.Interfaces.Interface.Afs.Af.Discovery.TransportAddress, self).__setattr__(name, value)

                                    def has_data(self):
                                        return (
                                            self.address.is_set or
                                            self.address_type.is_set)

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.address.yfilter != YFilter.not_set or
                                            self.address_type.yfilter != YFilter.not_set)

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "transport-address" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()
                                        if (self.address.is_set or self.address.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.address.get_name_leafdata())
                                        if (self.address_type.is_set or self.address_type.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.address_type.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "address" or name == "address-type"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "address"):
                                            self.address = value
                                            self.address.value_namespace = name_space
                                            self.address.value_namespace_prefix = name_space_prefix
                                        if(value_path == "address-type"):
                                            self.address_type = value
                                            self.address_type.value_namespace = name_space
                                            self.address_type.value_namespace_prefix = name_space_prefix

                                def has_data(self):
                                    return (self.transport_address is not None and self.transport_address.has_data())

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        (self.transport_address is not None and self.transport_address.has_operation()))

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "discovery" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    if (child_yang_name == "transport-address"):
                                        if (self.transport_address is None):
                                            self.transport_address = MplsLdp.Vrfs.Vrf.Interfaces.Interface.Afs.Af.Discovery.TransportAddress()
                                            self.transport_address.parent = self
                                            self._children_name_map["transport_address"] = "transport-address"
                                        return self.transport_address

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "transport-address"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    pass

                            def has_data(self):
                                return (
                                    self.af_name.is_set or
                                    self.enable.is_set or
                                    (self.discovery is not None and self.discovery.has_data()))

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.af_name.yfilter != YFilter.not_set or
                                    self.enable.yfilter != YFilter.not_set or
                                    (self.discovery is not None and self.discovery.has_operation()))

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "af" + "[af-name='" + self.af_name.get() + "']" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.af_name.is_set or self.af_name.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.af_name.get_name_leafdata())
                                if (self.enable.is_set or self.enable.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.enable.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                if (child_yang_name == "discovery"):
                                    if (self.discovery is None):
                                        self.discovery = MplsLdp.Vrfs.Vrf.Interfaces.Interface.Afs.Af.Discovery()
                                        self.discovery.parent = self
                                        self._children_name_map["discovery"] = "discovery"
                                    return self.discovery

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "discovery" or name == "af-name" or name == "enable"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "af-name"):
                                    self.af_name = value
                                    self.af_name.value_namespace = name_space
                                    self.af_name.value_namespace_prefix = name_space_prefix
                                if(value_path == "enable"):
                                    self.enable = value
                                    self.enable.value_namespace = name_space
                                    self.enable.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            for c in self.af:
                                if (c.has_data()):
                                    return True
                            return False

                        def has_operation(self):
                            for c in self.af:
                                if (c.has_operation()):
                                    return True
                            return self.yfilter != YFilter.not_set

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "afs" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "af"):
                                for c in self.af:
                                    segment = c.get_segment_path()
                                    if (segment_path == segment):
                                        return c
                                c = MplsLdp.Vrfs.Vrf.Interfaces.Interface.Afs.Af()
                                c.parent = self
                                local_reference_key = "ydk::seg::%s" % segment_path
                                self._local_refs[local_reference_key] = c
                                self.af.append(c)
                                return c

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "af"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            pass

                    def has_data(self):
                        return (
                            self.interface_name.is_set or
                            self.enable.is_set or
                            (self.afs is not None and self.afs.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.interface_name.yfilter != YFilter.not_set or
                            self.enable.yfilter != YFilter.not_set or
                            (self.afs is not None and self.afs.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "interface" + "[interface-name='" + self.interface_name.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.interface_name.is_set or self.interface_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.interface_name.get_name_leafdata())
                        if (self.enable.is_set or self.enable.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.enable.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "afs"):
                            if (self.afs is None):
                                self.afs = MplsLdp.Vrfs.Vrf.Interfaces.Interface.Afs()
                                self.afs.parent = self
                                self._children_name_map["afs"] = "afs"
                            return self.afs

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "afs" or name == "interface-name" or name == "enable"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "interface-name"):
                            self.interface_name = value
                            self.interface_name.value_namespace = name_space
                            self.interface_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "enable"):
                            self.enable = value
                            self.enable.value_namespace = name_space
                            self.enable.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.interface:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.interface:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "interfaces" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "interface"):
                        for c in self.interface:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = MplsLdp.Vrfs.Vrf.Interfaces.Interface()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.interface.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "interface"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass

            def has_data(self):
                return (
                    self.vrf_name.is_set or
                    self.enable.is_set or
                    (self.afs is not None and self.afs.has_data()) or
                    (self.global_ is not None and self.global_.has_data()) or
                    (self.interfaces is not None and self.interfaces.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.vrf_name.yfilter != YFilter.not_set or
                    self.enable.yfilter != YFilter.not_set or
                    (self.afs is not None and self.afs.has_operation()) or
                    (self.global_ is not None and self.global_.has_operation()) or
                    (self.interfaces is not None and self.interfaces.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "vrf" + "[vrf-name='" + self.vrf_name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-mpls-ldp-cfg:mpls-ldp/vrfs/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.vrf_name.is_set or self.vrf_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vrf_name.get_name_leafdata())
                if (self.enable.is_set or self.enable.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.enable.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "afs"):
                    if (self.afs is None):
                        self.afs = MplsLdp.Vrfs.Vrf.Afs()
                        self.afs.parent = self
                        self._children_name_map["afs"] = "afs"
                    return self.afs

                if (child_yang_name == "global"):
                    if (self.global_ is None):
                        self.global_ = MplsLdp.Vrfs.Vrf.Global_()
                        self.global_.parent = self
                        self._children_name_map["global_"] = "global"
                    return self.global_

                if (child_yang_name == "interfaces"):
                    if (self.interfaces is None):
                        self.interfaces = MplsLdp.Vrfs.Vrf.Interfaces()
                        self.interfaces.parent = self
                        self._children_name_map["interfaces"] = "interfaces"
                    return self.interfaces

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "afs" or name == "global" or name == "interfaces" or name == "vrf-name" or name == "enable"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "vrf-name"):
                    self.vrf_name = value
                    self.vrf_name.value_namespace = name_space
                    self.vrf_name.value_namespace_prefix = name_space_prefix
                if(value_path == "enable"):
                    self.enable = value
                    self.enable.value_namespace = name_space
                    self.enable.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.vrf:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.vrf:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "vrfs" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-mpls-ldp-cfg:mpls-ldp/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "vrf"):
                for c in self.vrf:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = MplsLdp.Vrfs.Vrf()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.vrf.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "vrf"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


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
        _revision = '2015-11-09'

        def __init__(self):
            super(MplsLdp.Global_, self).__init__()

            self.yang_name = "global"
            self.yang_parent_name = "mpls-ldp"

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

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("disable_implicit_ipv4",
                            "ltrace_buf_multiplier") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(MplsLdp.Global_, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(MplsLdp.Global_, self).__setattr__(name, value)


        class EntropyLabel(Entity):
            """
            Configure for LDP Entropy\-Label
            
            .. attribute:: enable
            
            	none
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'mpls-ldp-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(MplsLdp.Global_.EntropyLabel, self).__init__()

                self.yang_name = "entropy-label"
                self.yang_parent_name = "global"

                self.enable = YLeaf(YType.empty, "enable")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("enable") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(MplsLdp.Global_.EntropyLabel, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(MplsLdp.Global_.EntropyLabel, self).__setattr__(name, value)

            def has_data(self):
                return self.enable.is_set

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.enable.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "entropy-label" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-mpls-ldp-cfg:mpls-ldp/global/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.enable.is_set or self.enable.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.enable.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "enable"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "enable"):
                    self.enable = value
                    self.enable.value_namespace = name_space
                    self.enable.value_namespace_prefix = name_space_prefix


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
            _revision = '2015-11-09'

            def __init__(self):
                super(MplsLdp.Global_.Session, self).__init__()

                self.yang_name = "session"
                self.yang_parent_name = "global"

                self.hold_time = YLeaf(YType.uint32, "hold-time")

                self.backoff_time = MplsLdp.Global_.Session.BackoffTime()
                self.backoff_time.parent = self
                self._children_name_map["backoff_time"] = "backoff-time"
                self._children_yang_names.add("backoff-time")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("hold_time") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(MplsLdp.Global_.Session, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(MplsLdp.Global_.Session, self).__setattr__(name, value)


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
                _revision = '2015-11-09'

                def __init__(self):
                    super(MplsLdp.Global_.Session.BackoffTime, self).__init__()

                    self.yang_name = "backoff-time"
                    self.yang_parent_name = "session"

                    self.initial_backoff_time = YLeaf(YType.uint32, "initial-backoff-time")

                    self.max_backoff_time = YLeaf(YType.uint32, "max-backoff-time")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("initial_backoff_time",
                                    "max_backoff_time") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(MplsLdp.Global_.Session.BackoffTime, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(MplsLdp.Global_.Session.BackoffTime, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.initial_backoff_time.is_set or
                        self.max_backoff_time.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.initial_backoff_time.yfilter != YFilter.not_set or
                        self.max_backoff_time.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "backoff-time" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-mpls-ldp-cfg:mpls-ldp/global/session/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.initial_backoff_time.is_set or self.initial_backoff_time.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.initial_backoff_time.get_name_leafdata())
                    if (self.max_backoff_time.is_set or self.max_backoff_time.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.max_backoff_time.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "initial-backoff-time" or name == "max-backoff-time"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "initial-backoff-time"):
                        self.initial_backoff_time = value
                        self.initial_backoff_time.value_namespace = name_space
                        self.initial_backoff_time.value_namespace_prefix = name_space_prefix
                    if(value_path == "max-backoff-time"):
                        self.max_backoff_time = value
                        self.max_backoff_time.value_namespace = name_space
                        self.max_backoff_time.value_namespace_prefix = name_space_prefix

            def has_data(self):
                return (
                    self.hold_time.is_set or
                    (self.backoff_time is not None and self.backoff_time.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.hold_time.yfilter != YFilter.not_set or
                    (self.backoff_time is not None and self.backoff_time.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "session" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-mpls-ldp-cfg:mpls-ldp/global/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.hold_time.is_set or self.hold_time.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.hold_time.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "backoff-time"):
                    if (self.backoff_time is None):
                        self.backoff_time = MplsLdp.Global_.Session.BackoffTime()
                        self.backoff_time.parent = self
                        self._children_name_map["backoff_time"] = "backoff-time"
                    return self.backoff_time

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "backoff-time" or name == "hold-time"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "hold-time"):
                    self.hold_time = value
                    self.hold_time.value_namespace = name_space
                    self.hold_time.value_namespace_prefix = name_space_prefix


        class Igp(Entity):
            """
            LDP IGP configuration
            
            .. attribute:: sync
            
            	LDP IGP synchronization
            	**type**\:   :py:class:`Sync <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.Global_.Igp.Sync>`
            
            

            """

            _prefix = 'mpls-ldp-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(MplsLdp.Global_.Igp, self).__init__()

                self.yang_name = "igp"
                self.yang_parent_name = "global"

                self.sync = MplsLdp.Global_.Igp.Sync()
                self.sync.parent = self
                self._children_name_map["sync"] = "sync"
                self._children_yang_names.add("sync")


            class Sync(Entity):
                """
                LDP IGP synchronization
                
                .. attribute:: delay
                
                	LDP IGP synchronization delay time
                	**type**\:   :py:class:`Delay <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.Global_.Igp.Sync.Delay>`
                
                

                """

                _prefix = 'mpls-ldp-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(MplsLdp.Global_.Igp.Sync, self).__init__()

                    self.yang_name = "sync"
                    self.yang_parent_name = "igp"

                    self.delay = MplsLdp.Global_.Igp.Sync.Delay()
                    self.delay.parent = self
                    self._children_name_map["delay"] = "delay"
                    self._children_yang_names.add("delay")


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
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(MplsLdp.Global_.Igp.Sync.Delay, self).__init__()

                        self.yang_name = "delay"
                        self.yang_parent_name = "sync"

                        self.on_proc_restart = YLeaf(YType.uint32, "on-proc-restart")

                        self.on_session_up = YLeaf(YType.uint32, "on-session-up")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("on_proc_restart",
                                        "on_session_up") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(MplsLdp.Global_.Igp.Sync.Delay, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(MplsLdp.Global_.Igp.Sync.Delay, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.on_proc_restart.is_set or
                            self.on_session_up.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.on_proc_restart.yfilter != YFilter.not_set or
                            self.on_session_up.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "delay" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            path_buffer = "Cisco-IOS-XR-mpls-ldp-cfg:mpls-ldp/global/igp/sync/%s" % self.get_segment_path()
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.on_proc_restart.is_set or self.on_proc_restart.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.on_proc_restart.get_name_leafdata())
                        if (self.on_session_up.is_set or self.on_session_up.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.on_session_up.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "on-proc-restart" or name == "on-session-up"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "on-proc-restart"):
                            self.on_proc_restart = value
                            self.on_proc_restart.value_namespace = name_space
                            self.on_proc_restart.value_namespace_prefix = name_space_prefix
                        if(value_path == "on-session-up"):
                            self.on_session_up = value
                            self.on_session_up.value_namespace = name_space
                            self.on_session_up.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    return (self.delay is not None and self.delay.has_data())

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        (self.delay is not None and self.delay.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "sync" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-mpls-ldp-cfg:mpls-ldp/global/igp/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "delay"):
                        if (self.delay is None):
                            self.delay = MplsLdp.Global_.Igp.Sync.Delay()
                            self.delay.parent = self
                            self._children_name_map["delay"] = "delay"
                        return self.delay

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "delay"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass

            def has_data(self):
                return (self.sync is not None and self.sync.has_data())

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    (self.sync is not None and self.sync.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "igp" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-mpls-ldp-cfg:mpls-ldp/global/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "sync"):
                    if (self.sync is None):
                        self.sync = MplsLdp.Global_.Igp.Sync()
                        self.sync.parent = self
                        self._children_name_map["sync"] = "sync"
                    return self.sync

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "sync"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass


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
            _revision = '2015-11-09'

            def __init__(self):
                super(MplsLdp.Global_.EnableLogging, self).__init__()

                self.yang_name = "enable-logging"
                self.yang_parent_name = "global"

                self.adjacency = YLeaf(YType.empty, "adjacency")

                self.gr_session_changes = YLeaf(YType.empty, "gr-session-changes")

                self.neighbor_changes = YLeaf(YType.empty, "neighbor-changes")

                self.nsr = YLeaf(YType.empty, "nsr")

                self.session_protection = YLeaf(YType.empty, "session-protection")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("adjacency",
                                "gr_session_changes",
                                "neighbor_changes",
                                "nsr",
                                "session_protection") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(MplsLdp.Global_.EnableLogging, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(MplsLdp.Global_.EnableLogging, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.adjacency.is_set or
                    self.gr_session_changes.is_set or
                    self.neighbor_changes.is_set or
                    self.nsr.is_set or
                    self.session_protection.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.adjacency.yfilter != YFilter.not_set or
                    self.gr_session_changes.yfilter != YFilter.not_set or
                    self.neighbor_changes.yfilter != YFilter.not_set or
                    self.nsr.yfilter != YFilter.not_set or
                    self.session_protection.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "enable-logging" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-mpls-ldp-cfg:mpls-ldp/global/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.adjacency.is_set or self.adjacency.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.adjacency.get_name_leafdata())
                if (self.gr_session_changes.is_set or self.gr_session_changes.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.gr_session_changes.get_name_leafdata())
                if (self.neighbor_changes.is_set or self.neighbor_changes.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.neighbor_changes.get_name_leafdata())
                if (self.nsr.is_set or self.nsr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nsr.get_name_leafdata())
                if (self.session_protection.is_set or self.session_protection.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.session_protection.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "adjacency" or name == "gr-session-changes" or name == "neighbor-changes" or name == "nsr" or name == "session-protection"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "adjacency"):
                    self.adjacency = value
                    self.adjacency.value_namespace = name_space
                    self.adjacency.value_namespace_prefix = name_space_prefix
                if(value_path == "gr-session-changes"):
                    self.gr_session_changes = value
                    self.gr_session_changes.value_namespace = name_space
                    self.gr_session_changes.value_namespace_prefix = name_space_prefix
                if(value_path == "neighbor-changes"):
                    self.neighbor_changes = value
                    self.neighbor_changes.value_namespace = name_space
                    self.neighbor_changes.value_namespace_prefix = name_space_prefix
                if(value_path == "nsr"):
                    self.nsr = value
                    self.nsr.value_namespace = name_space
                    self.nsr.value_namespace_prefix = name_space_prefix
                if(value_path == "session-protection"):
                    self.session_protection = value
                    self.session_protection.value_namespace = name_space
                    self.session_protection.value_namespace_prefix = name_space_prefix


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
            _revision = '2015-11-09'

            def __init__(self):
                super(MplsLdp.Global_.Signalling, self).__init__()

                self.yang_name = "signalling"
                self.yang_parent_name = "global"

                self.dscp = YLeaf(YType.uint32, "dscp")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("dscp") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(MplsLdp.Global_.Signalling, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(MplsLdp.Global_.Signalling, self).__setattr__(name, value)

            def has_data(self):
                return self.dscp.is_set

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.dscp.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "signalling" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-mpls-ldp-cfg:mpls-ldp/global/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.dscp.is_set or self.dscp.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.dscp.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "dscp"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "dscp"):
                    self.dscp = value
                    self.dscp.value_namespace = name_space
                    self.dscp.value_namespace_prefix = name_space_prefix


        class Nsr(Entity):
            """
            Configure LDP Non\-Stop Routing
            
            .. attribute:: enable
            
            	none
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'mpls-ldp-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(MplsLdp.Global_.Nsr, self).__init__()

                self.yang_name = "nsr"
                self.yang_parent_name = "global"

                self.enable = YLeaf(YType.empty, "enable")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("enable") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(MplsLdp.Global_.Nsr, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(MplsLdp.Global_.Nsr, self).__setattr__(name, value)

            def has_data(self):
                return self.enable.is_set

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.enable.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "nsr" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-mpls-ldp-cfg:mpls-ldp/global/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.enable.is_set or self.enable.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.enable.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "enable"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "enable"):
                    self.enable = value
                    self.enable.value_namespace = name_space
                    self.enable.value_namespace_prefix = name_space_prefix


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
            _revision = '2015-11-09'

            def __init__(self):
                super(MplsLdp.Global_.GracefulRestart, self).__init__()

                self.yang_name = "graceful-restart"
                self.yang_parent_name = "global"

                self.enable = YLeaf(YType.empty, "enable")

                self.forwarding_hold_time = YLeaf(YType.uint32, "forwarding-hold-time")

                self.reconnect_timeout = YLeaf(YType.uint32, "reconnect-timeout")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("enable",
                                "forwarding_hold_time",
                                "reconnect_timeout") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(MplsLdp.Global_.GracefulRestart, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(MplsLdp.Global_.GracefulRestart, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.enable.is_set or
                    self.forwarding_hold_time.is_set or
                    self.reconnect_timeout.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.enable.yfilter != YFilter.not_set or
                    self.forwarding_hold_time.yfilter != YFilter.not_set or
                    self.reconnect_timeout.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "graceful-restart" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-mpls-ldp-cfg:mpls-ldp/global/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.enable.is_set or self.enable.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.enable.get_name_leafdata())
                if (self.forwarding_hold_time.is_set or self.forwarding_hold_time.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.forwarding_hold_time.get_name_leafdata())
                if (self.reconnect_timeout.is_set or self.reconnect_timeout.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.reconnect_timeout.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "enable" or name == "forwarding-hold-time" or name == "reconnect-timeout"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "enable"):
                    self.enable = value
                    self.enable.value_namespace = name_space
                    self.enable.value_namespace_prefix = name_space_prefix
                if(value_path == "forwarding-hold-time"):
                    self.forwarding_hold_time = value
                    self.forwarding_hold_time.value_namespace = name_space
                    self.forwarding_hold_time.value_namespace_prefix = name_space_prefix
                if(value_path == "reconnect-timeout"):
                    self.reconnect_timeout = value
                    self.reconnect_timeout.value_namespace = name_space
                    self.reconnect_timeout.value_namespace_prefix = name_space_prefix


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
            _revision = '2015-11-09'

            def __init__(self):
                super(MplsLdp.Global_.Discovery, self).__init__()

                self.yang_name = "discovery"
                self.yang_parent_name = "global"

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

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("disable_instance_tlv",
                                "disable_quick_start") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(MplsLdp.Global_.Discovery, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(MplsLdp.Global_.Discovery, self).__setattr__(name, value)


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
                _revision = '2015-11-09'

                def __init__(self):
                    super(MplsLdp.Global_.Discovery.LinkHello, self).__init__()

                    self.yang_name = "link-hello"
                    self.yang_parent_name = "discovery"

                    self.hold_time = YLeaf(YType.uint32, "hold-time")

                    self.interval = YLeaf(YType.uint32, "interval")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("hold_time",
                                    "interval") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(MplsLdp.Global_.Discovery.LinkHello, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(MplsLdp.Global_.Discovery.LinkHello, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.hold_time.is_set or
                        self.interval.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.hold_time.yfilter != YFilter.not_set or
                        self.interval.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "link-hello" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-mpls-ldp-cfg:mpls-ldp/global/discovery/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.hold_time.is_set or self.hold_time.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.hold_time.get_name_leafdata())
                    if (self.interval.is_set or self.interval.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.interval.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "hold-time" or name == "interval"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "hold-time"):
                        self.hold_time = value
                        self.hold_time.value_namespace = name_space
                        self.hold_time.value_namespace_prefix = name_space_prefix
                    if(value_path == "interval"):
                        self.interval = value
                        self.interval.value_namespace = name_space
                        self.interval.value_namespace_prefix = name_space_prefix


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
                _revision = '2015-11-09'

                def __init__(self):
                    super(MplsLdp.Global_.Discovery.TargetedHello, self).__init__()

                    self.yang_name = "targeted-hello"
                    self.yang_parent_name = "discovery"

                    self.hold_time = YLeaf(YType.uint32, "hold-time")

                    self.interval = YLeaf(YType.uint32, "interval")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("hold_time",
                                    "interval") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(MplsLdp.Global_.Discovery.TargetedHello, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(MplsLdp.Global_.Discovery.TargetedHello, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.hold_time.is_set or
                        self.interval.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.hold_time.yfilter != YFilter.not_set or
                        self.interval.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "targeted-hello" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-mpls-ldp-cfg:mpls-ldp/global/discovery/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.hold_time.is_set or self.hold_time.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.hold_time.get_name_leafdata())
                    if (self.interval.is_set or self.interval.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.interval.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "hold-time" or name == "interval"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "hold-time"):
                        self.hold_time = value
                        self.hold_time.value_namespace = name_space
                        self.hold_time.value_namespace_prefix = name_space_prefix
                    if(value_path == "interval"):
                        self.interval = value
                        self.interval.value_namespace = name_space
                        self.interval.value_namespace_prefix = name_space_prefix

            def has_data(self):
                return (
                    self.disable_instance_tlv.is_set or
                    self.disable_quick_start.is_set or
                    (self.link_hello is not None and self.link_hello.has_data()) or
                    (self.targeted_hello is not None and self.targeted_hello.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.disable_instance_tlv.yfilter != YFilter.not_set or
                    self.disable_quick_start.yfilter != YFilter.not_set or
                    (self.link_hello is not None and self.link_hello.has_operation()) or
                    (self.targeted_hello is not None and self.targeted_hello.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "discovery" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-mpls-ldp-cfg:mpls-ldp/global/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.disable_instance_tlv.is_set or self.disable_instance_tlv.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.disable_instance_tlv.get_name_leafdata())
                if (self.disable_quick_start.is_set or self.disable_quick_start.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.disable_quick_start.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "link-hello"):
                    if (self.link_hello is None):
                        self.link_hello = MplsLdp.Global_.Discovery.LinkHello()
                        self.link_hello.parent = self
                        self._children_name_map["link_hello"] = "link-hello"
                    return self.link_hello

                if (child_yang_name == "targeted-hello"):
                    if (self.targeted_hello is None):
                        self.targeted_hello = MplsLdp.Global_.Discovery.TargetedHello()
                        self.targeted_hello.parent = self
                        self._children_name_map["targeted_hello"] = "targeted-hello"
                    return self.targeted_hello

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "link-hello" or name == "targeted-hello" or name == "disable-instance-tlv" or name == "disable-quick-start"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "disable-instance-tlv"):
                    self.disable_instance_tlv = value
                    self.disable_instance_tlv.value_namespace = name_space
                    self.disable_instance_tlv.value_namespace_prefix = name_space_prefix
                if(value_path == "disable-quick-start"):
                    self.disable_quick_start = value
                    self.disable_quick_start.value_namespace = name_space
                    self.disable_quick_start.value_namespace_prefix = name_space_prefix


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
            _revision = '2015-11-09'

            def __init__(self):
                super(MplsLdp.Global_.Mldp, self).__init__()

                self.yang_name = "mldp"
                self.yang_parent_name = "global"

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

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("enable") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(MplsLdp.Global_.Mldp, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(MplsLdp.Global_.Mldp, self).__setattr__(name, value)


            class Vrfs(Entity):
                """
                VRF Table attribute configuration for MPLS LDP
                
                .. attribute:: vrf
                
                	VRF attribute configuration for MPLS LDP
                	**type**\: list of    :py:class:`Vrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.Global_.Mldp.Vrfs.Vrf>`
                
                

                """

                _prefix = 'mpls-ldp-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(MplsLdp.Global_.Mldp.Vrfs, self).__init__()

                    self.yang_name = "vrfs"
                    self.yang_parent_name = "mldp"

                    self.vrf = YList(self)

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in () and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(MplsLdp.Global_.Mldp.Vrfs, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(MplsLdp.Global_.Mldp.Vrfs, self).__setattr__(name, value)


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
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(MplsLdp.Global_.Mldp.Vrfs.Vrf, self).__init__()

                        self.yang_name = "vrf"
                        self.yang_parent_name = "vrfs"

                        self.vrf_name = YLeaf(YType.str, "vrf-name")

                        self.enable = YLeaf(YType.empty, "enable")

                        self.afs = MplsLdp.Global_.Mldp.Vrfs.Vrf.Afs()
                        self.afs.parent = self
                        self._children_name_map["afs"] = "afs"
                        self._children_yang_names.add("afs")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("vrf_name",
                                        "enable") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(MplsLdp.Global_.Mldp.Vrfs.Vrf, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(MplsLdp.Global_.Mldp.Vrfs.Vrf, self).__setattr__(name, value)


                    class Afs(Entity):
                        """
                        Address Family specific operational data
                        
                        .. attribute:: af
                        
                        	Operational data for given Address Family
                        	**type**\: list of    :py:class:`Af <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.Global_.Mldp.Vrfs.Vrf.Afs.Af>`
                        
                        

                        """

                        _prefix = 'mpls-ldp-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(MplsLdp.Global_.Mldp.Vrfs.Vrf.Afs, self).__init__()

                            self.yang_name = "afs"
                            self.yang_parent_name = "vrf"

                            self.af = YList(self)

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in () and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(MplsLdp.Global_.Mldp.Vrfs.Vrf.Afs, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(MplsLdp.Global_.Mldp.Vrfs.Vrf.Afs, self).__setattr__(name, value)


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
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(MplsLdp.Global_.Mldp.Vrfs.Vrf.Afs.Af, self).__init__()

                                self.yang_name = "af"
                                self.yang_parent_name = "afs"

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

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("af_name",
                                                "enable",
                                                "mldp_rib_unicast_always") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(MplsLdp.Global_.Mldp.Vrfs.Vrf.Afs.Af, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(MplsLdp.Global_.Mldp.Vrfs.Vrf.Afs.Af, self).__setattr__(name, value)


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
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(MplsLdp.Global_.Mldp.Vrfs.Vrf.Afs.Af.RecursiveForwarding, self).__init__()

                                    self.yang_name = "recursive-forwarding"
                                    self.yang_parent_name = "af"

                                    self.enable = YLeaf(YType.empty, "enable")

                                    self.policy = YLeaf(YType.str, "policy")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("enable",
                                                    "policy") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(MplsLdp.Global_.Mldp.Vrfs.Vrf.Afs.Af.RecursiveForwarding, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(MplsLdp.Global_.Mldp.Vrfs.Vrf.Afs.Af.RecursiveForwarding, self).__setattr__(name, value)

                                def has_data(self):
                                    return (
                                        self.enable.is_set or
                                        self.policy.is_set)

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.enable.yfilter != YFilter.not_set or
                                        self.policy.yfilter != YFilter.not_set)

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "recursive-forwarding" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.enable.is_set or self.enable.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.enable.get_name_leafdata())
                                    if (self.policy.is_set or self.policy.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.policy.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "enable" or name == "policy"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "enable"):
                                        self.enable = value
                                        self.enable.value_namespace = name_space
                                        self.enable.value_namespace_prefix = name_space_prefix
                                    if(value_path == "policy"):
                                        self.policy = value
                                        self.policy.value_namespace = name_space
                                        self.policy.value_namespace_prefix = name_space_prefix


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
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(MplsLdp.Global_.Mldp.Vrfs.Vrf.Afs.Af.MldpRecursiveFec, self).__init__()

                                    self.yang_name = "mldp-recursive-fec"
                                    self.yang_parent_name = "af"

                                    self.enable = YLeaf(YType.empty, "enable")

                                    self.policy = YLeaf(YType.str, "policy")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("enable",
                                                    "policy") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(MplsLdp.Global_.Mldp.Vrfs.Vrf.Afs.Af.MldpRecursiveFec, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(MplsLdp.Global_.Mldp.Vrfs.Vrf.Afs.Af.MldpRecursiveFec, self).__setattr__(name, value)

                                def has_data(self):
                                    return (
                                        self.enable.is_set or
                                        self.policy.is_set)

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.enable.yfilter != YFilter.not_set or
                                        self.policy.yfilter != YFilter.not_set)

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "mldp-recursive-fec" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.enable.is_set or self.enable.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.enable.get_name_leafdata())
                                    if (self.policy.is_set or self.policy.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.policy.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "enable" or name == "policy"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "enable"):
                                        self.enable = value
                                        self.enable.value_namespace = name_space
                                        self.enable.value_namespace_prefix = name_space_prefix
                                    if(value_path == "policy"):
                                        self.policy = value
                                        self.policy.value_namespace = name_space
                                        self.policy.value_namespace_prefix = name_space_prefix


                            class NeighborPolicies(Entity):
                                """
                                MLDP neighbor policies
                                
                                .. attribute:: neighbor_policy
                                
                                	Route Policy
                                	**type**\: list of    :py:class:`NeighborPolicy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.Global_.Mldp.Vrfs.Vrf.Afs.Af.NeighborPolicies.NeighborPolicy>`
                                
                                

                                """

                                _prefix = 'mpls-ldp-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(MplsLdp.Global_.Mldp.Vrfs.Vrf.Afs.Af.NeighborPolicies, self).__init__()

                                    self.yang_name = "neighbor-policies"
                                    self.yang_parent_name = "af"

                                    self.neighbor_policy = YList(self)

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in () and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(MplsLdp.Global_.Mldp.Vrfs.Vrf.Afs.Af.NeighborPolicies, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(MplsLdp.Global_.Mldp.Vrfs.Vrf.Afs.Af.NeighborPolicies, self).__setattr__(name, value)


                                class NeighborPolicy(Entity):
                                    """
                                    Route Policy
                                    
                                    .. attribute:: root_address  <key>
                                    
                                    	Neighbor Address
                                    	**type**\: one of the below types:
                                    
                                    	**type**\:  str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    
                                    ----
                                    	**type**\:  str
                                    
                                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                    
                                    
                                    ----
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
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(MplsLdp.Global_.Mldp.Vrfs.Vrf.Afs.Af.NeighborPolicies.NeighborPolicy, self).__init__()

                                        self.yang_name = "neighbor-policy"
                                        self.yang_parent_name = "neighbor-policies"

                                        self.root_address = YLeaf(YType.str, "root-address")

                                        self.policy_mode = YLeaf(YType.enumeration, "policy-mode")

                                        self.route_policy = YLeaf(YType.str, "route-policy")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("root_address",
                                                        "policy_mode",
                                                        "route_policy") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(MplsLdp.Global_.Mldp.Vrfs.Vrf.Afs.Af.NeighborPolicies.NeighborPolicy, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(MplsLdp.Global_.Mldp.Vrfs.Vrf.Afs.Af.NeighborPolicies.NeighborPolicy, self).__setattr__(name, value)

                                    def has_data(self):
                                        return (
                                            self.root_address.is_set or
                                            self.policy_mode.is_set or
                                            self.route_policy.is_set)

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.root_address.yfilter != YFilter.not_set or
                                            self.policy_mode.yfilter != YFilter.not_set or
                                            self.route_policy.yfilter != YFilter.not_set)

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "neighbor-policy" + "[root-address='" + self.root_address.get() + "']" + "[policy-mode='" + self.policy_mode.get() + "']" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()
                                        if (self.root_address.is_set or self.root_address.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.root_address.get_name_leafdata())
                                        if (self.policy_mode.is_set or self.policy_mode.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.policy_mode.get_name_leafdata())
                                        if (self.route_policy.is_set or self.route_policy.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.route_policy.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "root-address" or name == "policy-mode" or name == "route-policy"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "root-address"):
                                            self.root_address = value
                                            self.root_address.value_namespace = name_space
                                            self.root_address.value_namespace_prefix = name_space_prefix
                                        if(value_path == "policy-mode"):
                                            self.policy_mode = value
                                            self.policy_mode.value_namespace = name_space
                                            self.policy_mode.value_namespace_prefix = name_space_prefix
                                        if(value_path == "route-policy"):
                                            self.route_policy = value
                                            self.route_policy.value_namespace = name_space
                                            self.route_policy.value_namespace_prefix = name_space_prefix

                                def has_data(self):
                                    for c in self.neighbor_policy:
                                        if (c.has_data()):
                                            return True
                                    return False

                                def has_operation(self):
                                    for c in self.neighbor_policy:
                                        if (c.has_operation()):
                                            return True
                                    return self.yfilter != YFilter.not_set

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "neighbor-policies" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    if (child_yang_name == "neighbor-policy"):
                                        for c in self.neighbor_policy:
                                            segment = c.get_segment_path()
                                            if (segment_path == segment):
                                                return c
                                        c = MplsLdp.Global_.Mldp.Vrfs.Vrf.Afs.Af.NeighborPolicies.NeighborPolicy()
                                        c.parent = self
                                        local_reference_key = "ydk::seg::%s" % segment_path
                                        self._local_refs[local_reference_key] = c
                                        self.neighbor_policy.append(c)
                                        return c

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "neighbor-policy"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    pass


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
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(MplsLdp.Global_.Mldp.Vrfs.Vrf.Afs.Af.MoFrr, self).__init__()

                                    self.yang_name = "mo-frr"
                                    self.yang_parent_name = "af"

                                    self.enable = YLeaf(YType.empty, "enable")

                                    self.policy = YLeaf(YType.str, "policy")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("enable",
                                                    "policy") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(MplsLdp.Global_.Mldp.Vrfs.Vrf.Afs.Af.MoFrr, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(MplsLdp.Global_.Mldp.Vrfs.Vrf.Afs.Af.MoFrr, self).__setattr__(name, value)

                                def has_data(self):
                                    return (
                                        self.enable.is_set or
                                        self.policy.is_set)

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.enable.yfilter != YFilter.not_set or
                                        self.policy.yfilter != YFilter.not_set)

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "mo-frr" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.enable.is_set or self.enable.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.enable.get_name_leafdata())
                                    if (self.policy.is_set or self.policy.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.policy.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "enable" or name == "policy"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "enable"):
                                        self.enable = value
                                        self.enable.value_namespace = name_space
                                        self.enable.value_namespace_prefix = name_space_prefix
                                    if(value_path == "policy"):
                                        self.policy = value
                                        self.policy.value_namespace = name_space
                                        self.policy.value_namespace_prefix = name_space_prefix


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
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(MplsLdp.Global_.Mldp.Vrfs.Vrf.Afs.Af.MakeBeforeBreak, self).__init__()

                                    self.yang_name = "make-before-break"
                                    self.yang_parent_name = "af"

                                    self.policy = YLeaf(YType.str, "policy")

                                    self.signaling = MplsLdp.Global_.Mldp.Vrfs.Vrf.Afs.Af.MakeBeforeBreak.Signaling()
                                    self.signaling.parent = self
                                    self._children_name_map["signaling"] = "signaling"
                                    self._children_yang_names.add("signaling")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("policy") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(MplsLdp.Global_.Mldp.Vrfs.Vrf.Afs.Af.MakeBeforeBreak, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(MplsLdp.Global_.Mldp.Vrfs.Vrf.Afs.Af.MakeBeforeBreak, self).__setattr__(name, value)


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
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(MplsLdp.Global_.Mldp.Vrfs.Vrf.Afs.Af.MakeBeforeBreak.Signaling, self).__init__()

                                        self.yang_name = "signaling"
                                        self.yang_parent_name = "make-before-break"

                                        self.delete_delay = YLeaf(YType.uint32, "delete-delay")

                                        self.forward_delay = YLeaf(YType.uint32, "forward-delay")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("delete_delay",
                                                        "forward_delay") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(MplsLdp.Global_.Mldp.Vrfs.Vrf.Afs.Af.MakeBeforeBreak.Signaling, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(MplsLdp.Global_.Mldp.Vrfs.Vrf.Afs.Af.MakeBeforeBreak.Signaling, self).__setattr__(name, value)

                                    def has_data(self):
                                        return (
                                            self.delete_delay.is_set or
                                            self.forward_delay.is_set)

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.delete_delay.yfilter != YFilter.not_set or
                                            self.forward_delay.yfilter != YFilter.not_set)

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "signaling" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()
                                        if (self.delete_delay.is_set or self.delete_delay.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.delete_delay.get_name_leafdata())
                                        if (self.forward_delay.is_set or self.forward_delay.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.forward_delay.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "delete-delay" or name == "forward-delay"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "delete-delay"):
                                            self.delete_delay = value
                                            self.delete_delay.value_namespace = name_space
                                            self.delete_delay.value_namespace_prefix = name_space_prefix
                                        if(value_path == "forward-delay"):
                                            self.forward_delay = value
                                            self.forward_delay.value_namespace = name_space
                                            self.forward_delay.value_namespace_prefix = name_space_prefix

                                def has_data(self):
                                    return (
                                        self.policy.is_set or
                                        (self.signaling is not None and self.signaling.has_data()))

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.policy.yfilter != YFilter.not_set or
                                        (self.signaling is not None and self.signaling.has_operation()))

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "make-before-break" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.policy.is_set or self.policy.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.policy.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    if (child_yang_name == "signaling"):
                                        if (self.signaling is None):
                                            self.signaling = MplsLdp.Global_.Mldp.Vrfs.Vrf.Afs.Af.MakeBeforeBreak.Signaling()
                                            self.signaling.parent = self
                                            self._children_name_map["signaling"] = "signaling"
                                        return self.signaling

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "signaling" or name == "policy"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "policy"):
                                        self.policy = value
                                        self.policy.value_namespace = name_space
                                        self.policy.value_namespace_prefix = name_space_prefix


                            class Csc(Entity):
                                """
                                MPLS mLDP CSC
                                
                                .. attribute:: enable
                                
                                	Enable MPLS mLDP CSC
                                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                                
                                

                                """

                                _prefix = 'mpls-ldp-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(MplsLdp.Global_.Mldp.Vrfs.Vrf.Afs.Af.Csc, self).__init__()

                                    self.yang_name = "csc"
                                    self.yang_parent_name = "af"

                                    self.enable = YLeaf(YType.empty, "enable")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("enable") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(MplsLdp.Global_.Mldp.Vrfs.Vrf.Afs.Af.Csc, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(MplsLdp.Global_.Mldp.Vrfs.Vrf.Afs.Af.Csc, self).__setattr__(name, value)

                                def has_data(self):
                                    return self.enable.is_set

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.enable.yfilter != YFilter.not_set)

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "csc" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.enable.is_set or self.enable.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.enable.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "enable"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "enable"):
                                        self.enable = value
                                        self.enable.value_namespace = name_space
                                        self.enable.value_namespace_prefix = name_space_prefix

                            def has_data(self):
                                return (
                                    self.af_name.is_set or
                                    self.enable.is_set or
                                    self.mldp_rib_unicast_always.is_set or
                                    (self.csc is not None and self.csc.has_data()) or
                                    (self.make_before_break is not None and self.make_before_break.has_data()) or
                                    (self.mldp_recursive_fec is not None and self.mldp_recursive_fec.has_data()) or
                                    (self.mo_frr is not None and self.mo_frr.has_data()) or
                                    (self.neighbor_policies is not None and self.neighbor_policies.has_data()) or
                                    (self.recursive_forwarding is not None and self.recursive_forwarding.has_data()))

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.af_name.yfilter != YFilter.not_set or
                                    self.enable.yfilter != YFilter.not_set or
                                    self.mldp_rib_unicast_always.yfilter != YFilter.not_set or
                                    (self.csc is not None and self.csc.has_operation()) or
                                    (self.make_before_break is not None and self.make_before_break.has_operation()) or
                                    (self.mldp_recursive_fec is not None and self.mldp_recursive_fec.has_operation()) or
                                    (self.mo_frr is not None and self.mo_frr.has_operation()) or
                                    (self.neighbor_policies is not None and self.neighbor_policies.has_operation()) or
                                    (self.recursive_forwarding is not None and self.recursive_forwarding.has_operation()))

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "af" + "[af-name='" + self.af_name.get() + "']" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.af_name.is_set or self.af_name.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.af_name.get_name_leafdata())
                                if (self.enable.is_set or self.enable.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.enable.get_name_leafdata())
                                if (self.mldp_rib_unicast_always.is_set or self.mldp_rib_unicast_always.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.mldp_rib_unicast_always.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                if (child_yang_name == "csc"):
                                    if (self.csc is None):
                                        self.csc = MplsLdp.Global_.Mldp.Vrfs.Vrf.Afs.Af.Csc()
                                        self.csc.parent = self
                                        self._children_name_map["csc"] = "csc"
                                    return self.csc

                                if (child_yang_name == "make-before-break"):
                                    if (self.make_before_break is None):
                                        self.make_before_break = MplsLdp.Global_.Mldp.Vrfs.Vrf.Afs.Af.MakeBeforeBreak()
                                        self.make_before_break.parent = self
                                        self._children_name_map["make_before_break"] = "make-before-break"
                                    return self.make_before_break

                                if (child_yang_name == "mldp-recursive-fec"):
                                    if (self.mldp_recursive_fec is None):
                                        self.mldp_recursive_fec = MplsLdp.Global_.Mldp.Vrfs.Vrf.Afs.Af.MldpRecursiveFec()
                                        self.mldp_recursive_fec.parent = self
                                        self._children_name_map["mldp_recursive_fec"] = "mldp-recursive-fec"
                                    return self.mldp_recursive_fec

                                if (child_yang_name == "mo-frr"):
                                    if (self.mo_frr is None):
                                        self.mo_frr = MplsLdp.Global_.Mldp.Vrfs.Vrf.Afs.Af.MoFrr()
                                        self.mo_frr.parent = self
                                        self._children_name_map["mo_frr"] = "mo-frr"
                                    return self.mo_frr

                                if (child_yang_name == "neighbor-policies"):
                                    if (self.neighbor_policies is None):
                                        self.neighbor_policies = MplsLdp.Global_.Mldp.Vrfs.Vrf.Afs.Af.NeighborPolicies()
                                        self.neighbor_policies.parent = self
                                        self._children_name_map["neighbor_policies"] = "neighbor-policies"
                                    return self.neighbor_policies

                                if (child_yang_name == "recursive-forwarding"):
                                    if (self.recursive_forwarding is None):
                                        self.recursive_forwarding = MplsLdp.Global_.Mldp.Vrfs.Vrf.Afs.Af.RecursiveForwarding()
                                        self.recursive_forwarding.parent = self
                                        self._children_name_map["recursive_forwarding"] = "recursive-forwarding"
                                    return self.recursive_forwarding

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "csc" or name == "make-before-break" or name == "mldp-recursive-fec" or name == "mo-frr" or name == "neighbor-policies" or name == "recursive-forwarding" or name == "af-name" or name == "enable" or name == "mldp-rib-unicast-always"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "af-name"):
                                    self.af_name = value
                                    self.af_name.value_namespace = name_space
                                    self.af_name.value_namespace_prefix = name_space_prefix
                                if(value_path == "enable"):
                                    self.enable = value
                                    self.enable.value_namespace = name_space
                                    self.enable.value_namespace_prefix = name_space_prefix
                                if(value_path == "mldp-rib-unicast-always"):
                                    self.mldp_rib_unicast_always = value
                                    self.mldp_rib_unicast_always.value_namespace = name_space
                                    self.mldp_rib_unicast_always.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            for c in self.af:
                                if (c.has_data()):
                                    return True
                            return False

                        def has_operation(self):
                            for c in self.af:
                                if (c.has_operation()):
                                    return True
                            return self.yfilter != YFilter.not_set

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "afs" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "af"):
                                for c in self.af:
                                    segment = c.get_segment_path()
                                    if (segment_path == segment):
                                        return c
                                c = MplsLdp.Global_.Mldp.Vrfs.Vrf.Afs.Af()
                                c.parent = self
                                local_reference_key = "ydk::seg::%s" % segment_path
                                self._local_refs[local_reference_key] = c
                                self.af.append(c)
                                return c

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "af"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            pass

                    def has_data(self):
                        return (
                            self.vrf_name.is_set or
                            self.enable.is_set or
                            (self.afs is not None and self.afs.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.vrf_name.yfilter != YFilter.not_set or
                            self.enable.yfilter != YFilter.not_set or
                            (self.afs is not None and self.afs.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "vrf" + "[vrf-name='" + self.vrf_name.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            path_buffer = "Cisco-IOS-XR-mpls-ldp-cfg:mpls-ldp/global/mldp/vrfs/%s" % self.get_segment_path()
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.vrf_name.is_set or self.vrf_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.vrf_name.get_name_leafdata())
                        if (self.enable.is_set or self.enable.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.enable.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "afs"):
                            if (self.afs is None):
                                self.afs = MplsLdp.Global_.Mldp.Vrfs.Vrf.Afs()
                                self.afs.parent = self
                                self._children_name_map["afs"] = "afs"
                            return self.afs

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "afs" or name == "vrf-name" or name == "enable"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "vrf-name"):
                            self.vrf_name = value
                            self.vrf_name.value_namespace = name_space
                            self.vrf_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "enable"):
                            self.enable = value
                            self.enable.value_namespace = name_space
                            self.enable.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.vrf:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.vrf:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "vrfs" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-mpls-ldp-cfg:mpls-ldp/global/mldp/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "vrf"):
                        for c in self.vrf:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = MplsLdp.Global_.Mldp.Vrfs.Vrf()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.vrf.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "vrf"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class DefaultVrf(Entity):
                """
                Default VRF attribute configuration for mLDP
                
                .. attribute:: afs
                
                	Address Family specific operational data
                	**type**\:   :py:class:`Afs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.Global_.Mldp.DefaultVrf.Afs>`
                
                

                """

                _prefix = 'mpls-ldp-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(MplsLdp.Global_.Mldp.DefaultVrf, self).__init__()

                    self.yang_name = "default-vrf"
                    self.yang_parent_name = "mldp"

                    self.afs = MplsLdp.Global_.Mldp.DefaultVrf.Afs()
                    self.afs.parent = self
                    self._children_name_map["afs"] = "afs"
                    self._children_yang_names.add("afs")


                class Afs(Entity):
                    """
                    Address Family specific operational data
                    
                    .. attribute:: af
                    
                    	Operational data for given Address Family
                    	**type**\: list of    :py:class:`Af <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.Global_.Mldp.DefaultVrf.Afs.Af>`
                    
                    

                    """

                    _prefix = 'mpls-ldp-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(MplsLdp.Global_.Mldp.DefaultVrf.Afs, self).__init__()

                        self.yang_name = "afs"
                        self.yang_parent_name = "default-vrf"

                        self.af = YList(self)

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in () and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(MplsLdp.Global_.Mldp.DefaultVrf.Afs, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(MplsLdp.Global_.Mldp.DefaultVrf.Afs, self).__setattr__(name, value)


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
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(MplsLdp.Global_.Mldp.DefaultVrf.Afs.Af, self).__init__()

                            self.yang_name = "af"
                            self.yang_parent_name = "afs"

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

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("af_name",
                                            "enable",
                                            "mldp_rib_unicast_always") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(MplsLdp.Global_.Mldp.DefaultVrf.Afs.Af, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(MplsLdp.Global_.Mldp.DefaultVrf.Afs.Af, self).__setattr__(name, value)


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
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(MplsLdp.Global_.Mldp.DefaultVrf.Afs.Af.RecursiveForwarding, self).__init__()

                                self.yang_name = "recursive-forwarding"
                                self.yang_parent_name = "af"

                                self.enable = YLeaf(YType.empty, "enable")

                                self.policy = YLeaf(YType.str, "policy")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("enable",
                                                "policy") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(MplsLdp.Global_.Mldp.DefaultVrf.Afs.Af.RecursiveForwarding, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(MplsLdp.Global_.Mldp.DefaultVrf.Afs.Af.RecursiveForwarding, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.enable.is_set or
                                    self.policy.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.enable.yfilter != YFilter.not_set or
                                    self.policy.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "recursive-forwarding" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.enable.is_set or self.enable.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.enable.get_name_leafdata())
                                if (self.policy.is_set or self.policy.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.policy.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "enable" or name == "policy"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "enable"):
                                    self.enable = value
                                    self.enable.value_namespace = name_space
                                    self.enable.value_namespace_prefix = name_space_prefix
                                if(value_path == "policy"):
                                    self.policy = value
                                    self.policy.value_namespace = name_space
                                    self.policy.value_namespace_prefix = name_space_prefix


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
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(MplsLdp.Global_.Mldp.DefaultVrf.Afs.Af.MldpRecursiveFec, self).__init__()

                                self.yang_name = "mldp-recursive-fec"
                                self.yang_parent_name = "af"

                                self.enable = YLeaf(YType.empty, "enable")

                                self.policy = YLeaf(YType.str, "policy")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("enable",
                                                "policy") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(MplsLdp.Global_.Mldp.DefaultVrf.Afs.Af.MldpRecursiveFec, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(MplsLdp.Global_.Mldp.DefaultVrf.Afs.Af.MldpRecursiveFec, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.enable.is_set or
                                    self.policy.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.enable.yfilter != YFilter.not_set or
                                    self.policy.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "mldp-recursive-fec" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.enable.is_set or self.enable.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.enable.get_name_leafdata())
                                if (self.policy.is_set or self.policy.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.policy.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "enable" or name == "policy"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "enable"):
                                    self.enable = value
                                    self.enable.value_namespace = name_space
                                    self.enable.value_namespace_prefix = name_space_prefix
                                if(value_path == "policy"):
                                    self.policy = value
                                    self.policy.value_namespace = name_space
                                    self.policy.value_namespace_prefix = name_space_prefix


                        class NeighborPolicies(Entity):
                            """
                            MLDP neighbor policies
                            
                            .. attribute:: neighbor_policy
                            
                            	Route Policy
                            	**type**\: list of    :py:class:`NeighborPolicy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.Global_.Mldp.DefaultVrf.Afs.Af.NeighborPolicies.NeighborPolicy>`
                            
                            

                            """

                            _prefix = 'mpls-ldp-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(MplsLdp.Global_.Mldp.DefaultVrf.Afs.Af.NeighborPolicies, self).__init__()

                                self.yang_name = "neighbor-policies"
                                self.yang_parent_name = "af"

                                self.neighbor_policy = YList(self)

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in () and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(MplsLdp.Global_.Mldp.DefaultVrf.Afs.Af.NeighborPolicies, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(MplsLdp.Global_.Mldp.DefaultVrf.Afs.Af.NeighborPolicies, self).__setattr__(name, value)


                            class NeighborPolicy(Entity):
                                """
                                Route Policy
                                
                                .. attribute:: root_address  <key>
                                
                                	Neighbor Address
                                	**type**\: one of the below types:
                                
                                	**type**\:  str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                
                                ----
                                	**type**\:  str
                                
                                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                
                                
                                ----
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
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(MplsLdp.Global_.Mldp.DefaultVrf.Afs.Af.NeighborPolicies.NeighborPolicy, self).__init__()

                                    self.yang_name = "neighbor-policy"
                                    self.yang_parent_name = "neighbor-policies"

                                    self.root_address = YLeaf(YType.str, "root-address")

                                    self.policy_mode = YLeaf(YType.enumeration, "policy-mode")

                                    self.route_policy = YLeaf(YType.str, "route-policy")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("root_address",
                                                    "policy_mode",
                                                    "route_policy") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(MplsLdp.Global_.Mldp.DefaultVrf.Afs.Af.NeighborPolicies.NeighborPolicy, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(MplsLdp.Global_.Mldp.DefaultVrf.Afs.Af.NeighborPolicies.NeighborPolicy, self).__setattr__(name, value)

                                def has_data(self):
                                    return (
                                        self.root_address.is_set or
                                        self.policy_mode.is_set or
                                        self.route_policy.is_set)

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.root_address.yfilter != YFilter.not_set or
                                        self.policy_mode.yfilter != YFilter.not_set or
                                        self.route_policy.yfilter != YFilter.not_set)

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "neighbor-policy" + "[root-address='" + self.root_address.get() + "']" + "[policy-mode='" + self.policy_mode.get() + "']" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.root_address.is_set or self.root_address.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.root_address.get_name_leafdata())
                                    if (self.policy_mode.is_set or self.policy_mode.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.policy_mode.get_name_leafdata())
                                    if (self.route_policy.is_set or self.route_policy.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.route_policy.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "root-address" or name == "policy-mode" or name == "route-policy"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "root-address"):
                                        self.root_address = value
                                        self.root_address.value_namespace = name_space
                                        self.root_address.value_namespace_prefix = name_space_prefix
                                    if(value_path == "policy-mode"):
                                        self.policy_mode = value
                                        self.policy_mode.value_namespace = name_space
                                        self.policy_mode.value_namespace_prefix = name_space_prefix
                                    if(value_path == "route-policy"):
                                        self.route_policy = value
                                        self.route_policy.value_namespace = name_space
                                        self.route_policy.value_namespace_prefix = name_space_prefix

                            def has_data(self):
                                for c in self.neighbor_policy:
                                    if (c.has_data()):
                                        return True
                                return False

                            def has_operation(self):
                                for c in self.neighbor_policy:
                                    if (c.has_operation()):
                                        return True
                                return self.yfilter != YFilter.not_set

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "neighbor-policies" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                if (child_yang_name == "neighbor-policy"):
                                    for c in self.neighbor_policy:
                                        segment = c.get_segment_path()
                                        if (segment_path == segment):
                                            return c
                                    c = MplsLdp.Global_.Mldp.DefaultVrf.Afs.Af.NeighborPolicies.NeighborPolicy()
                                    c.parent = self
                                    local_reference_key = "ydk::seg::%s" % segment_path
                                    self._local_refs[local_reference_key] = c
                                    self.neighbor_policy.append(c)
                                    return c

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "neighbor-policy"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                pass


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
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(MplsLdp.Global_.Mldp.DefaultVrf.Afs.Af.MoFrr, self).__init__()

                                self.yang_name = "mo-frr"
                                self.yang_parent_name = "af"

                                self.enable = YLeaf(YType.empty, "enable")

                                self.policy = YLeaf(YType.str, "policy")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("enable",
                                                "policy") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(MplsLdp.Global_.Mldp.DefaultVrf.Afs.Af.MoFrr, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(MplsLdp.Global_.Mldp.DefaultVrf.Afs.Af.MoFrr, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.enable.is_set or
                                    self.policy.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.enable.yfilter != YFilter.not_set or
                                    self.policy.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "mo-frr" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.enable.is_set or self.enable.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.enable.get_name_leafdata())
                                if (self.policy.is_set or self.policy.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.policy.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "enable" or name == "policy"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "enable"):
                                    self.enable = value
                                    self.enable.value_namespace = name_space
                                    self.enable.value_namespace_prefix = name_space_prefix
                                if(value_path == "policy"):
                                    self.policy = value
                                    self.policy.value_namespace = name_space
                                    self.policy.value_namespace_prefix = name_space_prefix


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
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(MplsLdp.Global_.Mldp.DefaultVrf.Afs.Af.MakeBeforeBreak, self).__init__()

                                self.yang_name = "make-before-break"
                                self.yang_parent_name = "af"

                                self.policy = YLeaf(YType.str, "policy")

                                self.signaling = MplsLdp.Global_.Mldp.DefaultVrf.Afs.Af.MakeBeforeBreak.Signaling()
                                self.signaling.parent = self
                                self._children_name_map["signaling"] = "signaling"
                                self._children_yang_names.add("signaling")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("policy") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(MplsLdp.Global_.Mldp.DefaultVrf.Afs.Af.MakeBeforeBreak, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(MplsLdp.Global_.Mldp.DefaultVrf.Afs.Af.MakeBeforeBreak, self).__setattr__(name, value)


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
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(MplsLdp.Global_.Mldp.DefaultVrf.Afs.Af.MakeBeforeBreak.Signaling, self).__init__()

                                    self.yang_name = "signaling"
                                    self.yang_parent_name = "make-before-break"

                                    self.delete_delay = YLeaf(YType.uint32, "delete-delay")

                                    self.forward_delay = YLeaf(YType.uint32, "forward-delay")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("delete_delay",
                                                    "forward_delay") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(MplsLdp.Global_.Mldp.DefaultVrf.Afs.Af.MakeBeforeBreak.Signaling, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(MplsLdp.Global_.Mldp.DefaultVrf.Afs.Af.MakeBeforeBreak.Signaling, self).__setattr__(name, value)

                                def has_data(self):
                                    return (
                                        self.delete_delay.is_set or
                                        self.forward_delay.is_set)

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.delete_delay.yfilter != YFilter.not_set or
                                        self.forward_delay.yfilter != YFilter.not_set)

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "signaling" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.delete_delay.is_set or self.delete_delay.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.delete_delay.get_name_leafdata())
                                    if (self.forward_delay.is_set or self.forward_delay.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.forward_delay.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "delete-delay" or name == "forward-delay"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "delete-delay"):
                                        self.delete_delay = value
                                        self.delete_delay.value_namespace = name_space
                                        self.delete_delay.value_namespace_prefix = name_space_prefix
                                    if(value_path == "forward-delay"):
                                        self.forward_delay = value
                                        self.forward_delay.value_namespace = name_space
                                        self.forward_delay.value_namespace_prefix = name_space_prefix

                            def has_data(self):
                                return (
                                    self.policy.is_set or
                                    (self.signaling is not None and self.signaling.has_data()))

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.policy.yfilter != YFilter.not_set or
                                    (self.signaling is not None and self.signaling.has_operation()))

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "make-before-break" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.policy.is_set or self.policy.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.policy.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                if (child_yang_name == "signaling"):
                                    if (self.signaling is None):
                                        self.signaling = MplsLdp.Global_.Mldp.DefaultVrf.Afs.Af.MakeBeforeBreak.Signaling()
                                        self.signaling.parent = self
                                        self._children_name_map["signaling"] = "signaling"
                                    return self.signaling

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "signaling" or name == "policy"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "policy"):
                                    self.policy = value
                                    self.policy.value_namespace = name_space
                                    self.policy.value_namespace_prefix = name_space_prefix


                        class Csc(Entity):
                            """
                            MPLS mLDP CSC
                            
                            .. attribute:: enable
                            
                            	Enable MPLS mLDP CSC
                            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                            
                            

                            """

                            _prefix = 'mpls-ldp-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(MplsLdp.Global_.Mldp.DefaultVrf.Afs.Af.Csc, self).__init__()

                                self.yang_name = "csc"
                                self.yang_parent_name = "af"

                                self.enable = YLeaf(YType.empty, "enable")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("enable") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(MplsLdp.Global_.Mldp.DefaultVrf.Afs.Af.Csc, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(MplsLdp.Global_.Mldp.DefaultVrf.Afs.Af.Csc, self).__setattr__(name, value)

                            def has_data(self):
                                return self.enable.is_set

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.enable.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "csc" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.enable.is_set or self.enable.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.enable.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "enable"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "enable"):
                                    self.enable = value
                                    self.enable.value_namespace = name_space
                                    self.enable.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            return (
                                self.af_name.is_set or
                                self.enable.is_set or
                                self.mldp_rib_unicast_always.is_set or
                                (self.csc is not None and self.csc.has_data()) or
                                (self.make_before_break is not None and self.make_before_break.has_data()) or
                                (self.mldp_recursive_fec is not None and self.mldp_recursive_fec.has_data()) or
                                (self.mo_frr is not None and self.mo_frr.has_data()) or
                                (self.neighbor_policies is not None and self.neighbor_policies.has_data()) or
                                (self.recursive_forwarding is not None and self.recursive_forwarding.has_data()))

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.af_name.yfilter != YFilter.not_set or
                                self.enable.yfilter != YFilter.not_set or
                                self.mldp_rib_unicast_always.yfilter != YFilter.not_set or
                                (self.csc is not None and self.csc.has_operation()) or
                                (self.make_before_break is not None and self.make_before_break.has_operation()) or
                                (self.mldp_recursive_fec is not None and self.mldp_recursive_fec.has_operation()) or
                                (self.mo_frr is not None and self.mo_frr.has_operation()) or
                                (self.neighbor_policies is not None and self.neighbor_policies.has_operation()) or
                                (self.recursive_forwarding is not None and self.recursive_forwarding.has_operation()))

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "af" + "[af-name='" + self.af_name.get() + "']" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                path_buffer = "Cisco-IOS-XR-mpls-ldp-cfg:mpls-ldp/global/mldp/default-vrf/afs/%s" % self.get_segment_path()
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.af_name.is_set or self.af_name.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.af_name.get_name_leafdata())
                            if (self.enable.is_set or self.enable.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.enable.get_name_leafdata())
                            if (self.mldp_rib_unicast_always.is_set or self.mldp_rib_unicast_always.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.mldp_rib_unicast_always.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "csc"):
                                if (self.csc is None):
                                    self.csc = MplsLdp.Global_.Mldp.DefaultVrf.Afs.Af.Csc()
                                    self.csc.parent = self
                                    self._children_name_map["csc"] = "csc"
                                return self.csc

                            if (child_yang_name == "make-before-break"):
                                if (self.make_before_break is None):
                                    self.make_before_break = MplsLdp.Global_.Mldp.DefaultVrf.Afs.Af.MakeBeforeBreak()
                                    self.make_before_break.parent = self
                                    self._children_name_map["make_before_break"] = "make-before-break"
                                return self.make_before_break

                            if (child_yang_name == "mldp-recursive-fec"):
                                if (self.mldp_recursive_fec is None):
                                    self.mldp_recursive_fec = MplsLdp.Global_.Mldp.DefaultVrf.Afs.Af.MldpRecursiveFec()
                                    self.mldp_recursive_fec.parent = self
                                    self._children_name_map["mldp_recursive_fec"] = "mldp-recursive-fec"
                                return self.mldp_recursive_fec

                            if (child_yang_name == "mo-frr"):
                                if (self.mo_frr is None):
                                    self.mo_frr = MplsLdp.Global_.Mldp.DefaultVrf.Afs.Af.MoFrr()
                                    self.mo_frr.parent = self
                                    self._children_name_map["mo_frr"] = "mo-frr"
                                return self.mo_frr

                            if (child_yang_name == "neighbor-policies"):
                                if (self.neighbor_policies is None):
                                    self.neighbor_policies = MplsLdp.Global_.Mldp.DefaultVrf.Afs.Af.NeighborPolicies()
                                    self.neighbor_policies.parent = self
                                    self._children_name_map["neighbor_policies"] = "neighbor-policies"
                                return self.neighbor_policies

                            if (child_yang_name == "recursive-forwarding"):
                                if (self.recursive_forwarding is None):
                                    self.recursive_forwarding = MplsLdp.Global_.Mldp.DefaultVrf.Afs.Af.RecursiveForwarding()
                                    self.recursive_forwarding.parent = self
                                    self._children_name_map["recursive_forwarding"] = "recursive-forwarding"
                                return self.recursive_forwarding

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "csc" or name == "make-before-break" or name == "mldp-recursive-fec" or name == "mo-frr" or name == "neighbor-policies" or name == "recursive-forwarding" or name == "af-name" or name == "enable" or name == "mldp-rib-unicast-always"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "af-name"):
                                self.af_name = value
                                self.af_name.value_namespace = name_space
                                self.af_name.value_namespace_prefix = name_space_prefix
                            if(value_path == "enable"):
                                self.enable = value
                                self.enable.value_namespace = name_space
                                self.enable.value_namespace_prefix = name_space_prefix
                            if(value_path == "mldp-rib-unicast-always"):
                                self.mldp_rib_unicast_always = value
                                self.mldp_rib_unicast_always.value_namespace = name_space
                                self.mldp_rib_unicast_always.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.af:
                            if (c.has_data()):
                                return True
                        return False

                    def has_operation(self):
                        for c in self.af:
                            if (c.has_operation()):
                                return True
                        return self.yfilter != YFilter.not_set

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "afs" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            path_buffer = "Cisco-IOS-XR-mpls-ldp-cfg:mpls-ldp/global/mldp/default-vrf/%s" % self.get_segment_path()
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "af"):
                            for c in self.af:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = MplsLdp.Global_.Mldp.DefaultVrf.Afs.Af()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.af.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "af"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass

                def has_data(self):
                    return (self.afs is not None and self.afs.has_data())

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        (self.afs is not None and self.afs.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "default-vrf" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-mpls-ldp-cfg:mpls-ldp/global/mldp/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "afs"):
                        if (self.afs is None):
                            self.afs = MplsLdp.Global_.Mldp.DefaultVrf.Afs()
                            self.afs.parent = self
                            self._children_name_map["afs"] = "afs"
                        return self.afs

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "afs"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class MldpGlobal(Entity):
                """
                Global configuration for mLDP
                
                .. attribute:: logging
                
                	MPLS mLDP logging
                	**type**\:   :py:class:`Logging <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.Global_.Mldp.MldpGlobal.Logging>`
                
                

                """

                _prefix = 'mpls-ldp-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(MplsLdp.Global_.Mldp.MldpGlobal, self).__init__()

                    self.yang_name = "mldp-global"
                    self.yang_parent_name = "mldp"

                    self.logging = MplsLdp.Global_.Mldp.MldpGlobal.Logging()
                    self.logging.parent = self
                    self._children_name_map["logging"] = "logging"
                    self._children_yang_names.add("logging")


                class Logging(Entity):
                    """
                    MPLS mLDP logging
                    
                    .. attribute:: notifications
                    
                    	MPLS mLDP logging notifications
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    

                    """

                    _prefix = 'mpls-ldp-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(MplsLdp.Global_.Mldp.MldpGlobal.Logging, self).__init__()

                        self.yang_name = "logging"
                        self.yang_parent_name = "mldp-global"

                        self.notifications = YLeaf(YType.empty, "notifications")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("notifications") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(MplsLdp.Global_.Mldp.MldpGlobal.Logging, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(MplsLdp.Global_.Mldp.MldpGlobal.Logging, self).__setattr__(name, value)

                    def has_data(self):
                        return self.notifications.is_set

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.notifications.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "logging" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            path_buffer = "Cisco-IOS-XR-mpls-ldp-cfg:mpls-ldp/global/mldp/mldp-global/%s" % self.get_segment_path()
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.notifications.is_set or self.notifications.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.notifications.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "notifications"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "notifications"):
                            self.notifications = value
                            self.notifications.value_namespace = name_space
                            self.notifications.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    return (self.logging is not None and self.logging.has_data())

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        (self.logging is not None and self.logging.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "mldp-global" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-mpls-ldp-cfg:mpls-ldp/global/mldp/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "logging"):
                        if (self.logging is None):
                            self.logging = MplsLdp.Global_.Mldp.MldpGlobal.Logging()
                            self.logging.parent = self
                            self._children_name_map["logging"] = "logging"
                        return self.logging

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "logging"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass

            def has_data(self):
                return (
                    self.enable.is_set or
                    (self.default_vrf is not None and self.default_vrf.has_data()) or
                    (self.mldp_global is not None and self.mldp_global.has_data()) or
                    (self.vrfs is not None and self.vrfs.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.enable.yfilter != YFilter.not_set or
                    (self.default_vrf is not None and self.default_vrf.has_operation()) or
                    (self.mldp_global is not None and self.mldp_global.has_operation()) or
                    (self.vrfs is not None and self.vrfs.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "mldp" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-mpls-ldp-cfg:mpls-ldp/global/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.enable.is_set or self.enable.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.enable.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "default-vrf"):
                    if (self.default_vrf is None):
                        self.default_vrf = MplsLdp.Global_.Mldp.DefaultVrf()
                        self.default_vrf.parent = self
                        self._children_name_map["default_vrf"] = "default-vrf"
                    return self.default_vrf

                if (child_yang_name == "mldp-global"):
                    if (self.mldp_global is None):
                        self.mldp_global = MplsLdp.Global_.Mldp.MldpGlobal()
                        self.mldp_global.parent = self
                        self._children_name_map["mldp_global"] = "mldp-global"
                    return self.mldp_global

                if (child_yang_name == "vrfs"):
                    if (self.vrfs is None):
                        self.vrfs = MplsLdp.Global_.Mldp.Vrfs()
                        self.vrfs.parent = self
                        self._children_name_map["vrfs"] = "vrfs"
                    return self.vrfs

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "default-vrf" or name == "mldp-global" or name == "vrfs" or name == "enable"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "enable"):
                    self.enable = value
                    self.enable.value_namespace = name_space
                    self.enable.value_namespace_prefix = name_space_prefix

        def has_data(self):
            return (
                self.disable_implicit_ipv4.is_set or
                self.ltrace_buf_multiplier.is_set or
                (self.discovery is not None and self.discovery.has_data()) or
                (self.enable_logging is not None and self.enable_logging.has_data()) or
                (self.entropy_label is not None and self.entropy_label.has_data()) or
                (self.graceful_restart is not None and self.graceful_restart.has_data()) or
                (self.igp is not None and self.igp.has_data()) or
                (self.mldp is not None and self.mldp.has_data()) or
                (self.nsr is not None and self.nsr.has_data()) or
                (self.session is not None and self.session.has_data()) or
                (self.signalling is not None and self.signalling.has_data()))

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.disable_implicit_ipv4.yfilter != YFilter.not_set or
                self.ltrace_buf_multiplier.yfilter != YFilter.not_set or
                (self.discovery is not None and self.discovery.has_operation()) or
                (self.enable_logging is not None and self.enable_logging.has_operation()) or
                (self.entropy_label is not None and self.entropy_label.has_operation()) or
                (self.graceful_restart is not None and self.graceful_restart.has_operation()) or
                (self.igp is not None and self.igp.has_operation()) or
                (self.mldp is not None and self.mldp.has_operation()) or
                (self.nsr is not None and self.nsr.has_operation()) or
                (self.session is not None and self.session.has_operation()) or
                (self.signalling is not None and self.signalling.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "global" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-mpls-ldp-cfg:mpls-ldp/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.disable_implicit_ipv4.is_set or self.disable_implicit_ipv4.yfilter != YFilter.not_set):
                leaf_name_data.append(self.disable_implicit_ipv4.get_name_leafdata())
            if (self.ltrace_buf_multiplier.is_set or self.ltrace_buf_multiplier.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ltrace_buf_multiplier.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "discovery"):
                if (self.discovery is None):
                    self.discovery = MplsLdp.Global_.Discovery()
                    self.discovery.parent = self
                    self._children_name_map["discovery"] = "discovery"
                return self.discovery

            if (child_yang_name == "enable-logging"):
                if (self.enable_logging is None):
                    self.enable_logging = MplsLdp.Global_.EnableLogging()
                    self.enable_logging.parent = self
                    self._children_name_map["enable_logging"] = "enable-logging"
                return self.enable_logging

            if (child_yang_name == "entropy-label"):
                if (self.entropy_label is None):
                    self.entropy_label = MplsLdp.Global_.EntropyLabel()
                    self.entropy_label.parent = self
                    self._children_name_map["entropy_label"] = "entropy-label"
                return self.entropy_label

            if (child_yang_name == "graceful-restart"):
                if (self.graceful_restart is None):
                    self.graceful_restart = MplsLdp.Global_.GracefulRestart()
                    self.graceful_restart.parent = self
                    self._children_name_map["graceful_restart"] = "graceful-restart"
                return self.graceful_restart

            if (child_yang_name == "igp"):
                if (self.igp is None):
                    self.igp = MplsLdp.Global_.Igp()
                    self.igp.parent = self
                    self._children_name_map["igp"] = "igp"
                return self.igp

            if (child_yang_name == "mldp"):
                if (self.mldp is None):
                    self.mldp = MplsLdp.Global_.Mldp()
                    self.mldp.parent = self
                    self._children_name_map["mldp"] = "mldp"
                return self.mldp

            if (child_yang_name == "nsr"):
                if (self.nsr is None):
                    self.nsr = MplsLdp.Global_.Nsr()
                    self.nsr.parent = self
                    self._children_name_map["nsr"] = "nsr"
                return self.nsr

            if (child_yang_name == "session"):
                if (self.session is None):
                    self.session = MplsLdp.Global_.Session()
                    self.session.parent = self
                    self._children_name_map["session"] = "session"
                return self.session

            if (child_yang_name == "signalling"):
                if (self.signalling is None):
                    self.signalling = MplsLdp.Global_.Signalling()
                    self.signalling.parent = self
                    self._children_name_map["signalling"] = "signalling"
                return self.signalling

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "discovery" or name == "enable-logging" or name == "entropy-label" or name == "graceful-restart" or name == "igp" or name == "mldp" or name == "nsr" or name == "session" or name == "signalling" or name == "disable-implicit-ipv4" or name == "ltrace-buf-multiplier"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "disable-implicit-ipv4"):
                self.disable_implicit_ipv4 = value
                self.disable_implicit_ipv4.value_namespace = name_space
                self.disable_implicit_ipv4.value_namespace_prefix = name_space_prefix
            if(value_path == "ltrace-buf-multiplier"):
                self.ltrace_buf_multiplier = value
                self.ltrace_buf_multiplier.value_namespace = name_space
                self.ltrace_buf_multiplier.value_namespace_prefix = name_space_prefix

    def has_data(self):
        return (
            self.enable.is_set or
            (self.default_vrf is not None and self.default_vrf.has_data()) or
            (self.global_ is not None and self.global_.has_data()) or
            (self.vrfs is not None and self.vrfs.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            self.enable.yfilter != YFilter.not_set or
            (self.default_vrf is not None and self.default_vrf.has_operation()) or
            (self.global_ is not None and self.global_.has_operation()) or
            (self.vrfs is not None and self.vrfs.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-mpls-ldp-cfg:mpls-ldp" + path_buffer

        return path_buffer

    def get_entity_path(self, ancestor):
        path_buffer = ""
        if (not ancestor is None):
            raise YPYModelError("ancestor has to be None for top-level node")

        path_buffer = self.get_segment_path()
        leaf_name_data = LeafDataList()
        if (self.enable.is_set or self.enable.yfilter != YFilter.not_set):
            leaf_name_data.append(self.enable.get_name_leafdata())

        entity_path = EntityPath(path_buffer, leaf_name_data)
        return entity_path

    def get_child_by_name(self, child_yang_name, segment_path):
        child = self._get_child_by_seg_name([child_yang_name, segment_path])
        if child is not None:
            return child

        if (child_yang_name == "default-vrf"):
            if (self.default_vrf is None):
                self.default_vrf = MplsLdp.DefaultVrf()
                self.default_vrf.parent = self
                self._children_name_map["default_vrf"] = "default-vrf"
            return self.default_vrf

        if (child_yang_name == "global"):
            if (self.global_ is None):
                self.global_ = MplsLdp.Global_()
                self.global_.parent = self
                self._children_name_map["global_"] = "global"
            return self.global_

        if (child_yang_name == "vrfs"):
            if (self.vrfs is None):
                self.vrfs = MplsLdp.Vrfs()
                self.vrfs.parent = self
                self._children_name_map["vrfs"] = "vrfs"
            return self.vrfs

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "default-vrf" or name == "global" or name == "vrfs" or name == "enable"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        if(value_path == "enable"):
            self.enable = value
            self.enable.value_namespace = name_space
            self.enable.value_namespace_prefix = name_space_prefix

    def clone_ptr(self):
        self._top_entity = MplsLdp()
        return self._top_entity

