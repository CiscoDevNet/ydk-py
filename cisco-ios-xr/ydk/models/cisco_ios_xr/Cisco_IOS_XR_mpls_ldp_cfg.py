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


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class MldpPolicyModeEnum(Enum):
    """
    MldpPolicyModeEnum

    Mldp policy mode

    .. data:: inbound = 1

    	Inbound route policy

    .. data:: outbound = 2

    	Outbound route policy

    """

    inbound = 1

    outbound = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_ldp_cfg as meta
        return meta._meta_table['MldpPolicyModeEnum']


class MplsLdpAdvertiseBgpaclEnum(Enum):
    """
    MplsLdpAdvertiseBgpaclEnum

    Mpls ldp advertise bgpacl

    .. data:: peer_acl = 1

    	BGP prefixes advertised to peers permitted by

    	ACL

    """

    peer_acl = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_ldp_cfg as meta
        return meta._meta_table['MplsLdpAdvertiseBgpaclEnum']


class MplsLdpDownstreamOnDemandEnum(Enum):
    """
    MplsLdpDownstreamOnDemandEnum

    Mpls ldp downstream on demand

    .. data:: peer_acl = 1

    	Downstream on Demand peers permitted by ACL

    """

    peer_acl = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_ldp_cfg as meta
        return meta._meta_table['MplsLdpDownstreamOnDemandEnum']


class MplsLdpExpNullEnum(Enum):
    """
    MplsLdpExpNullEnum

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

    all = 1

    for_ = 2

    to = 3

    for_to = 4


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_ldp_cfg as meta
        return meta._meta_table['MplsLdpExpNullEnum']


class MplsLdpLabelAdvertiseEnum(Enum):
    """
    MplsLdpLabelAdvertiseEnum

    Mpls ldp label advertise

    .. data:: for_ = 1

    	Advertise label for prefix(es) permitted by

    	prefix ACL

    .. data:: for_to = 2

    	Advertise label for prefix(es) permitted by

    	prefix ACL to peer(s) permitted by peer ACL

    """

    for_ = 1

    for_to = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_ldp_cfg as meta
        return meta._meta_table['MplsLdpLabelAdvertiseEnum']


class MplsLdpLabelAllocationEnum(Enum):
    """
    MplsLdpLabelAllocationEnum

    Mpls ldp label allocation

    .. data:: acl = 1

    	Allocate label for prefixes permitted by ACL

    .. data:: host = 2

    	Allocate label for host routes only

    """

    acl = 1

    host = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_ldp_cfg as meta
        return meta._meta_table['MplsLdpLabelAllocationEnum']


class MplsLdpNbrPasswordEnum(Enum):
    """
    MplsLdpNbrPasswordEnum

    Mpls ldp nbr password

    .. data:: disable = 1

    	Disable the global default password for this

    	neighbor

    .. data:: specified = 2

    	Specify a password for this neighbor

    """

    disable = 1

    specified = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_ldp_cfg as meta
        return meta._meta_table['MplsLdpNbrPasswordEnum']


class MplsLdpSessionProtectionEnum(Enum):
    """
    MplsLdpSessionProtectionEnum

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

    all = 1

    for_ = 2

    all_with_duration = 3

    for_with_duration = 4

    all_with_forever = 5

    for_with_forever = 6


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_ldp_cfg as meta
        return meta._meta_table['MplsLdpSessionProtectionEnum']


class MplsLdpTargetedAcceptEnum(Enum):
    """
    MplsLdpTargetedAcceptEnum

    Mpls ldp targeted accept

    .. data:: all = 1

    	Accept targeted hello from all

    .. data:: from_ = 2

    	Accept targeted hello from peer ACL

    """

    all = 1

    from_ = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_ldp_cfg as meta
        return meta._meta_table['MplsLdpTargetedAcceptEnum']


class MplsLdpTransportAddressEnum(Enum):
    """
    MplsLdpTransportAddressEnum

    Mpls ldp transport address

    .. data:: interface = 1

    	Use interface IP address

    .. data:: address = 2

    	Use given IP address

    """

    interface = 1

    address = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_ldp_cfg as meta
        return meta._meta_table['MplsLdpTransportAddressEnum']


class MplsLdpafNameEnum(Enum):
    """
    MplsLdpafNameEnum

    Mpls ldpaf name

    .. data:: ipv4 = 4

    	IPv4

    .. data:: ipv6 = 6

    	IPv6

    """

    ipv4 = 4

    ipv6 = 6


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_ldp_cfg as meta
        return meta._meta_table['MplsLdpafNameEnum']



class MplsLdp(object):
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
        self.default_vrf = MplsLdp.DefaultVrf()
        self.default_vrf.parent = self
        self.enable = None
        self.global_ = MplsLdp.Global_()
        self.global_.parent = self
        self.vrfs = MplsLdp.Vrfs()
        self.vrfs.parent = self


    class DefaultVrf(object):
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
            self.parent = None
            self.afs = MplsLdp.DefaultVrf.Afs()
            self.afs.parent = self
            self.global_ = MplsLdp.DefaultVrf.Global_()
            self.global_.parent = self
            self.interfaces = MplsLdp.DefaultVrf.Interfaces()
            self.interfaces.parent = self


        class Afs(object):
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
                self.parent = None
                self.af = YList()
                self.af.parent = self
                self.af.name = 'af'


            class Af(object):
                """
                Configure data for given Address Family
                
                .. attribute:: af_name  <key>
                
                	Address Family type
                	**type**\:   :py:class:`MplsLdpafNameEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdpafNameEnum>`
                
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
                    self.parent = None
                    self.af_name = None
                    self.discovery = MplsLdp.DefaultVrf.Afs.Af.Discovery()
                    self.discovery.parent = self
                    self.enable = None
                    self.label = MplsLdp.DefaultVrf.Afs.Af.Label()
                    self.label.parent = self
                    self.neighbor = MplsLdp.DefaultVrf.Afs.Af.Neighbor()
                    self.neighbor.parent = self
                    self.redistribution_protocol = MplsLdp.DefaultVrf.Afs.Af.RedistributionProtocol()
                    self.redistribution_protocol.parent = self
                    self.traffic_engineering = MplsLdp.DefaultVrf.Afs.Af.TrafficEngineering()
                    self.traffic_engineering.parent = self


                class Label(object):
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
                        self.parent = None
                        self.local = MplsLdp.DefaultVrf.Afs.Af.Label.Local()
                        self.local.parent = self
                        self.remote = MplsLdp.DefaultVrf.Afs.Af.Label.Remote()
                        self.remote.parent = self


                    class Remote(object):
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
                            self.parent = None
                            self.accept = MplsLdp.DefaultVrf.Afs.Af.Label.Remote.Accept()
                            self.accept.parent = self


                        class Accept(object):
                            """
                            Configure inbound label acceptance
                            
                            .. attribute:: peer_accept_policies
                            
                            	Configuration related to neighbors for inbound label acceptance
                            	**type**\:   :py:class:`PeerAcceptPolicies <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.DefaultVrf.Afs.Af.Label.Remote.Accept.PeerAcceptPolicies>`
                            
                            

                            """

                            _prefix = 'mpls-ldp-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.peer_accept_policies = MplsLdp.DefaultVrf.Afs.Af.Label.Remote.Accept.PeerAcceptPolicies()
                                self.peer_accept_policies.parent = self


                            class PeerAcceptPolicies(object):
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
                                    self.parent = None
                                    self.peer_accept_policy = YList()
                                    self.peer_accept_policy.parent = self
                                    self.peer_accept_policy.name = 'peer_accept_policy'


                                class PeerAcceptPolicy(object):
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
                                        self.parent = None
                                        self.lsr_id = None
                                        self.label_space_id = None
                                        self.prefix_acl_name = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')
                                        if self.lsr_id is None:
                                            raise YPYModelError('Key property lsr_id is None')
                                        if self.label_space_id is None:
                                            raise YPYModelError('Key property label_space_id is None')

                                        return self.parent._common_path +'/Cisco-IOS-XR-mpls-ldp-cfg:peer-accept-policy[Cisco-IOS-XR-mpls-ldp-cfg:lsr-id = ' + str(self.lsr_id) + '][Cisco-IOS-XR-mpls-ldp-cfg:label-space-id = ' + str(self.label_space_id) + ']'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if self.lsr_id is not None:
                                            return True

                                        if self.label_space_id is not None:
                                            return True

                                        if self.prefix_acl_name is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_ldp_cfg as meta
                                        return meta._meta_table['MplsLdp.DefaultVrf.Afs.Af.Label.Remote.Accept.PeerAcceptPolicies.PeerAcceptPolicy']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-mpls-ldp-cfg:peer-accept-policies'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.peer_accept_policy is not None:
                                        for child_ref in self.peer_accept_policy:
                                            if child_ref._has_data():
                                                return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_ldp_cfg as meta
                                    return meta._meta_table['MplsLdp.DefaultVrf.Afs.Af.Label.Remote.Accept.PeerAcceptPolicies']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-mpls-ldp-cfg:accept'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.peer_accept_policies is not None and self.peer_accept_policies._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_ldp_cfg as meta
                                return meta._meta_table['MplsLdp.DefaultVrf.Afs.Af.Label.Remote.Accept']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-mpls-ldp-cfg:remote'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.accept is not None and self.accept._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_ldp_cfg as meta
                            return meta._meta_table['MplsLdp.DefaultVrf.Afs.Af.Label.Remote']['meta_info']


                    class Local(object):
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
                            self.parent = None
                            self.advertise = MplsLdp.DefaultVrf.Afs.Af.Label.Local.Advertise()
                            self.advertise.parent = self
                            self.allocate = MplsLdp.DefaultVrf.Afs.Af.Label.Local.Allocate()
                            self.allocate.parent = self
                            self.default_route = None
                            self.implicit_null_override = None


                        class Advertise(object):
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
                                self.parent = None
                                self.disable = None
                                self.explicit_null = MplsLdp.DefaultVrf.Afs.Af.Label.Local.Advertise.ExplicitNull()
                                self.explicit_null.parent = self
                                self.interfaces = MplsLdp.DefaultVrf.Afs.Af.Label.Local.Advertise.Interfaces()
                                self.interfaces.parent = self
                                self.peer_advertise_policies = MplsLdp.DefaultVrf.Afs.Af.Label.Local.Advertise.PeerAdvertisePolicies()
                                self.peer_advertise_policies.parent = self
                                self.prefix_advertise_policies = MplsLdp.DefaultVrf.Afs.Af.Label.Local.Advertise.PrefixAdvertisePolicies()
                                self.prefix_advertise_policies.parent = self


                            class PeerAdvertisePolicies(object):
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
                                    self.parent = None
                                    self.peer_advertise_policy = YList()
                                    self.peer_advertise_policy.parent = self
                                    self.peer_advertise_policy.name = 'peer_advertise_policy'


                                class PeerAdvertisePolicy(object):
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
                                        self.parent = None
                                        self.lsr_id = None
                                        self.label_space_id = None
                                        self.prefix_acl_name = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')
                                        if self.lsr_id is None:
                                            raise YPYModelError('Key property lsr_id is None')
                                        if self.label_space_id is None:
                                            raise YPYModelError('Key property label_space_id is None')

                                        return self.parent._common_path +'/Cisco-IOS-XR-mpls-ldp-cfg:peer-advertise-policy[Cisco-IOS-XR-mpls-ldp-cfg:lsr-id = ' + str(self.lsr_id) + '][Cisco-IOS-XR-mpls-ldp-cfg:label-space-id = ' + str(self.label_space_id) + ']'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if self.lsr_id is not None:
                                            return True

                                        if self.label_space_id is not None:
                                            return True

                                        if self.prefix_acl_name is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_ldp_cfg as meta
                                        return meta._meta_table['MplsLdp.DefaultVrf.Afs.Af.Label.Local.Advertise.PeerAdvertisePolicies.PeerAdvertisePolicy']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-mpls-ldp-cfg:peer-advertise-policies'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.peer_advertise_policy is not None:
                                        for child_ref in self.peer_advertise_policy:
                                            if child_ref._has_data():
                                                return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_ldp_cfg as meta
                                    return meta._meta_table['MplsLdp.DefaultVrf.Afs.Af.Label.Local.Advertise.PeerAdvertisePolicies']['meta_info']


                            class PrefixAdvertisePolicies(object):
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
                                    self.parent = None
                                    self.prefix_advertise_policy = YList()
                                    self.prefix_advertise_policy.parent = self
                                    self.prefix_advertise_policy.name = 'prefix_advertise_policy'


                                class PrefixAdvertisePolicy(object):
                                    """
                                    Control advertisement of prefix(es) using
                                    ACL
                                    
                                    .. attribute:: prefix_acl_name  <key>
                                    
                                    	Name of prefix ACL
                                    	**type**\:  str
                                    
                                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                                    
                                    .. attribute:: advertise_type
                                    
                                    	Label advertise type
                                    	**type**\:   :py:class:`MplsLdpLabelAdvertiseEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdpLabelAdvertiseEnum>`
                                    
                                    .. attribute:: peer_acl_name
                                    
                                    	Name of peer ACL
                                    	**type**\:  str
                                    
                                    

                                    """

                                    _prefix = 'mpls-ldp-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.prefix_acl_name = None
                                        self.advertise_type = None
                                        self.peer_acl_name = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')
                                        if self.prefix_acl_name is None:
                                            raise YPYModelError('Key property prefix_acl_name is None')

                                        return self.parent._common_path +'/Cisco-IOS-XR-mpls-ldp-cfg:prefix-advertise-policy[Cisco-IOS-XR-mpls-ldp-cfg:prefix-acl-name = ' + str(self.prefix_acl_name) + ']'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if self.prefix_acl_name is not None:
                                            return True

                                        if self.advertise_type is not None:
                                            return True

                                        if self.peer_acl_name is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_ldp_cfg as meta
                                        return meta._meta_table['MplsLdp.DefaultVrf.Afs.Af.Label.Local.Advertise.PrefixAdvertisePolicies.PrefixAdvertisePolicy']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-mpls-ldp-cfg:prefix-advertise-policies'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.prefix_advertise_policy is not None:
                                        for child_ref in self.prefix_advertise_policy:
                                            if child_ref._has_data():
                                                return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_ldp_cfg as meta
                                    return meta._meta_table['MplsLdp.DefaultVrf.Afs.Af.Label.Local.Advertise.PrefixAdvertisePolicies']['meta_info']


                            class ExplicitNull(object):
                                """
                                Configure advertisment of explicit\-null
                                for connected prefixes.
                                
                                .. attribute:: explicit_null_type
                                
                                	Explicit Null command variant
                                	**type**\:   :py:class:`MplsLdpExpNullEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdpExpNullEnum>`
                                
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
                                    self.parent = None
                                    self.explicit_null_type = None
                                    self.peer_acl_name = None
                                    self.prefix_acl_name = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-mpls-ldp-cfg:explicit-null'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.explicit_null_type is not None:
                                        return True

                                    if self.peer_acl_name is not None:
                                        return True

                                    if self.prefix_acl_name is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_ldp_cfg as meta
                                    return meta._meta_table['MplsLdp.DefaultVrf.Afs.Af.Label.Local.Advertise.ExplicitNull']['meta_info']


                            class Interfaces(object):
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
                                    self.parent = None
                                    self.interface = YList()
                                    self.interface.parent = self
                                    self.interface.name = 'interface'


                                class Interface(object):
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
                                        self.parent = None
                                        self.interface_name = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')
                                        if self.interface_name is None:
                                            raise YPYModelError('Key property interface_name is None')

                                        return self.parent._common_path +'/Cisco-IOS-XR-mpls-ldp-cfg:interface[Cisco-IOS-XR-mpls-ldp-cfg:interface-name = ' + str(self.interface_name) + ']'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if self.interface_name is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_ldp_cfg as meta
                                        return meta._meta_table['MplsLdp.DefaultVrf.Afs.Af.Label.Local.Advertise.Interfaces.Interface']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-mpls-ldp-cfg:interfaces'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.interface is not None:
                                        for child_ref in self.interface:
                                            if child_ref._has_data():
                                                return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_ldp_cfg as meta
                                    return meta._meta_table['MplsLdp.DefaultVrf.Afs.Af.Label.Local.Advertise.Interfaces']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-mpls-ldp-cfg:advertise'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.disable is not None:
                                    return True

                                if self.explicit_null is not None and self.explicit_null._has_data():
                                    return True

                                if self.interfaces is not None and self.interfaces._has_data():
                                    return True

                                if self.peer_advertise_policies is not None and self.peer_advertise_policies._has_data():
                                    return True

                                if self.prefix_advertise_policies is not None and self.prefix_advertise_policies._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_ldp_cfg as meta
                                return meta._meta_table['MplsLdp.DefaultVrf.Afs.Af.Label.Local.Advertise']['meta_info']


                        class Allocate(object):
                            """
                            Control local label allocation for
                            prefix(es)
                            
                            .. attribute:: allocation_type
                            
                            	Label allocation type
                            	**type**\:   :py:class:`MplsLdpLabelAllocationEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdpLabelAllocationEnum>`
                            
                            .. attribute:: prefix_acl_name
                            
                            	Name of prefix ACL
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'mpls-ldp-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.allocation_type = None
                                self.prefix_acl_name = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-mpls-ldp-cfg:allocate'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.allocation_type is not None:
                                    return True

                                if self.prefix_acl_name is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_ldp_cfg as meta
                                return meta._meta_table['MplsLdp.DefaultVrf.Afs.Af.Label.Local.Allocate']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-mpls-ldp-cfg:local'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.advertise is not None and self.advertise._has_data():
                                return True

                            if self.allocate is not None and self.allocate._has_data():
                                return True

                            if self.default_route is not None:
                                return True

                            if self.implicit_null_override is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_ldp_cfg as meta
                            return meta._meta_table['MplsLdp.DefaultVrf.Afs.Af.Label.Local']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-mpls-ldp-cfg:label'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.local is not None and self.local._has_data():
                            return True

                        if self.remote is not None and self.remote._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_ldp_cfg as meta
                        return meta._meta_table['MplsLdp.DefaultVrf.Afs.Af.Label']['meta_info']


                class Discovery(object):
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
                        self.parent = None
                        self.targeted_hello_accept = MplsLdp.DefaultVrf.Afs.Af.Discovery.TargetedHelloAccept()
                        self.targeted_hello_accept.parent = self
                        self.transport_address = None


                    class TargetedHelloAccept(object):
                        """
                        Configure acceptance from and responding to
                        targeted hellos.
                        
                        .. attribute:: accept_type
                        
                        	Type of acceptance
                        	**type**\:   :py:class:`MplsLdpTargetedAcceptEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdpTargetedAcceptEnum>`
                        
                        .. attribute:: peer_acl_name
                        
                        	Name of peer ACL
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'mpls-ldp-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.accept_type = None
                            self.peer_acl_name = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-mpls-ldp-cfg:targeted-hello-accept'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.accept_type is not None:
                                return True

                            if self.peer_acl_name is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_ldp_cfg as meta
                            return meta._meta_table['MplsLdp.DefaultVrf.Afs.Af.Discovery.TargetedHelloAccept']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-mpls-ldp-cfg:discovery'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.targeted_hello_accept is not None and self.targeted_hello_accept._has_data():
                            return True

                        if self.transport_address is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_ldp_cfg as meta
                        return meta._meta_table['MplsLdp.DefaultVrf.Afs.Af.Discovery']['meta_info']


                class TrafficEngineering(object):
                    """
                    MPLS Traffic Engingeering parameters for LDP
                    
                    .. attribute:: auto_tunnel_mesh
                    
                    	MPLS Traffic Engineering auto\-tunnel mesh parameters for LDP
                    	**type**\:   :py:class:`AutoTunnelMesh <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.DefaultVrf.Afs.Af.TrafficEngineering.AutoTunnelMesh>`
                    
                    

                    """

                    _prefix = 'mpls-ldp-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.auto_tunnel_mesh = MplsLdp.DefaultVrf.Afs.Af.TrafficEngineering.AutoTunnelMesh()
                        self.auto_tunnel_mesh.parent = self


                    class AutoTunnelMesh(object):
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
                            self.parent = None
                            self.group_all = None
                            self.group_ids = MplsLdp.DefaultVrf.Afs.Af.TrafficEngineering.AutoTunnelMesh.GroupIds()
                            self.group_ids.parent = self


                        class GroupIds(object):
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
                                self.parent = None
                                self.group_id = YList()
                                self.group_id.parent = self
                                self.group_id.name = 'group_id'


                            class GroupId(object):
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
                                    self.parent = None
                                    self.mesh_group_id = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')
                                    if self.mesh_group_id is None:
                                        raise YPYModelError('Key property mesh_group_id is None')

                                    return self.parent._common_path +'/Cisco-IOS-XR-mpls-ldp-cfg:group-id[Cisco-IOS-XR-mpls-ldp-cfg:mesh-group-id = ' + str(self.mesh_group_id) + ']'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.mesh_group_id is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_ldp_cfg as meta
                                    return meta._meta_table['MplsLdp.DefaultVrf.Afs.Af.TrafficEngineering.AutoTunnelMesh.GroupIds.GroupId']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-mpls-ldp-cfg:group-ids'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.group_id is not None:
                                    for child_ref in self.group_id:
                                        if child_ref._has_data():
                                            return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_ldp_cfg as meta
                                return meta._meta_table['MplsLdp.DefaultVrf.Afs.Af.TrafficEngineering.AutoTunnelMesh.GroupIds']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-mpls-ldp-cfg:auto-tunnel-mesh'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.group_all is not None:
                                return True

                            if self.group_ids is not None and self.group_ids._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_ldp_cfg as meta
                            return meta._meta_table['MplsLdp.DefaultVrf.Afs.Af.TrafficEngineering.AutoTunnelMesh']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-mpls-ldp-cfg:traffic-engineering'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.auto_tunnel_mesh is not None and self.auto_tunnel_mesh._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_ldp_cfg as meta
                        return meta._meta_table['MplsLdp.DefaultVrf.Afs.Af.TrafficEngineering']['meta_info']


                class Neighbor(object):
                    """
                    Configuration related to Neighbors
                    
                    .. attribute:: addresses
                    
                    	Configuration related to neighbors using neighbor address
                    	**type**\:   :py:class:`Addresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.DefaultVrf.Afs.Af.Neighbor.Addresses>`
                    
                    

                    """

                    _prefix = 'mpls-ldp-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.addresses = MplsLdp.DefaultVrf.Afs.Af.Neighbor.Addresses()
                        self.addresses.parent = self


                    class Addresses(object):
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
                            self.parent = None
                            self.address = YList()
                            self.address.parent = self
                            self.address.name = 'address'


                        class Address(object):
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
                                self.parent = None
                                self.ip_address = None
                                self.targeted = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                if self.ip_address is None:
                                    raise YPYModelError('Key property ip_address is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-mpls-ldp-cfg:address[Cisco-IOS-XR-mpls-ldp-cfg:ip-address = ' + str(self.ip_address) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.ip_address is not None:
                                    return True

                                if self.targeted is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_ldp_cfg as meta
                                return meta._meta_table['MplsLdp.DefaultVrf.Afs.Af.Neighbor.Addresses.Address']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-mpls-ldp-cfg:addresses'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.address is not None:
                                for child_ref in self.address:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_ldp_cfg as meta
                            return meta._meta_table['MplsLdp.DefaultVrf.Afs.Af.Neighbor.Addresses']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-mpls-ldp-cfg:neighbor'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.addresses is not None and self.addresses._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_ldp_cfg as meta
                        return meta._meta_table['MplsLdp.DefaultVrf.Afs.Af.Neighbor']['meta_info']


                class RedistributionProtocol(object):
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
                        self.parent = None
                        self.bgp = MplsLdp.DefaultVrf.Afs.Af.RedistributionProtocol.Bgp()
                        self.bgp.parent = self


                    class Bgp(object):
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
                            self.parent = None
                            self.advertise_to = MplsLdp.DefaultVrf.Afs.Af.RedistributionProtocol.Bgp.AdvertiseTo()
                            self.advertise_to.parent = self
                            self.as_ = MplsLdp.DefaultVrf.Afs.Af.RedistributionProtocol.Bgp.As_()
                            self.as_.parent = self


                        class As_(object):
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
                                self.parent = None
                                self.as_xx = None
                                self.as_yy = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-mpls-ldp-cfg:as'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.as_xx is not None:
                                    return True

                                if self.as_yy is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_ldp_cfg as meta
                                return meta._meta_table['MplsLdp.DefaultVrf.Afs.Af.RedistributionProtocol.Bgp.As_']['meta_info']


                        class AdvertiseTo(object):
                            """
                            ACL containing list of neighbors for BGP
                            route redistribution
                            
                            .. attribute:: peer_acl_name
                            
                            	Name of peer ACL
                            	**type**\:  str
                            
                            .. attribute:: type
                            
                            	advertise to peer acl type
                            	**type**\:   :py:class:`MplsLdpAdvertiseBgpaclEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdpAdvertiseBgpaclEnum>`
                            
                            

                            """

                            _prefix = 'mpls-ldp-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.peer_acl_name = None
                                self.type = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-mpls-ldp-cfg:advertise-to'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.peer_acl_name is not None:
                                    return True

                                if self.type is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_ldp_cfg as meta
                                return meta._meta_table['MplsLdp.DefaultVrf.Afs.Af.RedistributionProtocol.Bgp.AdvertiseTo']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-mpls-ldp-cfg:bgp'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.advertise_to is not None and self.advertise_to._has_data():
                                return True

                            if self.as_ is not None and self.as_._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_ldp_cfg as meta
                            return meta._meta_table['MplsLdp.DefaultVrf.Afs.Af.RedistributionProtocol.Bgp']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-mpls-ldp-cfg:redistribution-protocol'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.bgp is not None and self.bgp._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_ldp_cfg as meta
                        return meta._meta_table['MplsLdp.DefaultVrf.Afs.Af.RedistributionProtocol']['meta_info']

                @property
                def _common_path(self):
                    if self.af_name is None:
                        raise YPYModelError('Key property af_name is None')

                    return '/Cisco-IOS-XR-mpls-ldp-cfg:mpls-ldp/Cisco-IOS-XR-mpls-ldp-cfg:default-vrf/Cisco-IOS-XR-mpls-ldp-cfg:afs/Cisco-IOS-XR-mpls-ldp-cfg:af[Cisco-IOS-XR-mpls-ldp-cfg:af-name = ' + str(self.af_name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.af_name is not None:
                        return True

                    if self.discovery is not None and self.discovery._has_data():
                        return True

                    if self.enable is not None:
                        return True

                    if self.label is not None and self.label._has_data():
                        return True

                    if self.neighbor is not None and self.neighbor._has_data():
                        return True

                    if self.redistribution_protocol is not None and self.redistribution_protocol._has_data():
                        return True

                    if self.traffic_engineering is not None and self.traffic_engineering._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_ldp_cfg as meta
                    return meta._meta_table['MplsLdp.DefaultVrf.Afs.Af']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-mpls-ldp-cfg:mpls-ldp/Cisco-IOS-XR-mpls-ldp-cfg:default-vrf/Cisco-IOS-XR-mpls-ldp-cfg:afs'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.af is not None:
                    for child_ref in self.af:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_ldp_cfg as meta
                return meta._meta_table['MplsLdp.DefaultVrf.Afs']['meta_info']


        class Global_(object):
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
                self.parent = None
                self.graceful_restart = MplsLdp.DefaultVrf.Global_.GracefulRestart()
                self.graceful_restart.parent = self
                self.neighbor = MplsLdp.DefaultVrf.Global_.Neighbor()
                self.neighbor.parent = self
                self.router_id = None
                self.session = MplsLdp.DefaultVrf.Global_.Session()
                self.session.parent = self


            class Session(object):
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
                    self.parent = None
                    self.downstream_on_demand = MplsLdp.DefaultVrf.Global_.Session.DownstreamOnDemand()
                    self.downstream_on_demand.parent = self
                    self.protection = MplsLdp.DefaultVrf.Global_.Session.Protection()
                    self.protection.parent = self


                class Protection(object):
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
                    	**type**\:   :py:class:`MplsLdpSessionProtectionEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdpSessionProtectionEnum>`
                    
                    

                    """

                    _prefix = 'mpls-ldp-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.duration = None
                        self.peer_acl_name = None
                        self.protection_type = None

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-mpls-ldp-cfg:mpls-ldp/Cisco-IOS-XR-mpls-ldp-cfg:default-vrf/Cisco-IOS-XR-mpls-ldp-cfg:global/Cisco-IOS-XR-mpls-ldp-cfg:session/Cisco-IOS-XR-mpls-ldp-cfg:protection'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.duration is not None:
                            return True

                        if self.peer_acl_name is not None:
                            return True

                        if self.protection_type is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_ldp_cfg as meta
                        return meta._meta_table['MplsLdp.DefaultVrf.Global_.Session.Protection']['meta_info']


                class DownstreamOnDemand(object):
                    """
                    ACL with the list of neighbors configured for
                    Downstream on Demand
                    
                    .. attribute:: peer_acl_name
                    
                    	Name of peer ACL
                    	**type**\:  str
                    
                    .. attribute:: type
                    
                    	Downstream on demand type
                    	**type**\:   :py:class:`MplsLdpDownstreamOnDemandEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdpDownstreamOnDemandEnum>`
                    
                    

                    """

                    _prefix = 'mpls-ldp-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.peer_acl_name = None
                        self.type = None

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-mpls-ldp-cfg:mpls-ldp/Cisco-IOS-XR-mpls-ldp-cfg:default-vrf/Cisco-IOS-XR-mpls-ldp-cfg:global/Cisco-IOS-XR-mpls-ldp-cfg:session/Cisco-IOS-XR-mpls-ldp-cfg:downstream-on-demand'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.peer_acl_name is not None:
                            return True

                        if self.type is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_ldp_cfg as meta
                        return meta._meta_table['MplsLdp.DefaultVrf.Global_.Session.DownstreamOnDemand']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-mpls-ldp-cfg:mpls-ldp/Cisco-IOS-XR-mpls-ldp-cfg:default-vrf/Cisco-IOS-XR-mpls-ldp-cfg:global/Cisco-IOS-XR-mpls-ldp-cfg:session'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.downstream_on_demand is not None and self.downstream_on_demand._has_data():
                        return True

                    if self.protection is not None and self.protection._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_ldp_cfg as meta
                    return meta._meta_table['MplsLdp.DefaultVrf.Global_.Session']['meta_info']


            class Neighbor(object):
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
                    self.parent = None
                    self.dual_stack = MplsLdp.DefaultVrf.Global_.Neighbor.DualStack()
                    self.dual_stack.parent = self
                    self.ldp_ids = MplsLdp.DefaultVrf.Global_.Neighbor.LdpIds()
                    self.ldp_ids.parent = self
                    self.password = None


                class LdpIds(object):
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
                        self.parent = None
                        self.ldp_id = YList()
                        self.ldp_id.parent = self
                        self.ldp_id.name = 'ldp_id'


                    class LdpId(object):
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
                            self.parent = None
                            self.lsr_id = None
                            self.label_space_id = None
                            self.password = MplsLdp.DefaultVrf.Global_.Neighbor.LdpIds.LdpId.Password()
                            self.password.parent = self


                        class Password(object):
                            """
                            Password for MD5 authentication for this
                            neighbor
                            
                            .. attribute:: command_type
                            
                            	Command type for password configuration
                            	**type**\:   :py:class:`MplsLdpNbrPasswordEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdpNbrPasswordEnum>`
                            
                            .. attribute:: password
                            
                            	The neighbor password
                            	**type**\:  str
                            
                            	**pattern:** (!.+)\|([^!].+)
                            
                            

                            """

                            _prefix = 'mpls-ldp-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.command_type = None
                                self.password = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-mpls-ldp-cfg:password'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.command_type is not None:
                                    return True

                                if self.password is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_ldp_cfg as meta
                                return meta._meta_table['MplsLdp.DefaultVrf.Global_.Neighbor.LdpIds.LdpId.Password']['meta_info']

                        @property
                        def _common_path(self):
                            if self.lsr_id is None:
                                raise YPYModelError('Key property lsr_id is None')
                            if self.label_space_id is None:
                                raise YPYModelError('Key property label_space_id is None')

                            return '/Cisco-IOS-XR-mpls-ldp-cfg:mpls-ldp/Cisco-IOS-XR-mpls-ldp-cfg:default-vrf/Cisco-IOS-XR-mpls-ldp-cfg:global/Cisco-IOS-XR-mpls-ldp-cfg:neighbor/Cisco-IOS-XR-mpls-ldp-cfg:ldp-ids/Cisco-IOS-XR-mpls-ldp-cfg:ldp-id[Cisco-IOS-XR-mpls-ldp-cfg:lsr-id = ' + str(self.lsr_id) + '][Cisco-IOS-XR-mpls-ldp-cfg:label-space-id = ' + str(self.label_space_id) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.lsr_id is not None:
                                return True

                            if self.label_space_id is not None:
                                return True

                            if self.password is not None and self.password._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_ldp_cfg as meta
                            return meta._meta_table['MplsLdp.DefaultVrf.Global_.Neighbor.LdpIds.LdpId']['meta_info']

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-mpls-ldp-cfg:mpls-ldp/Cisco-IOS-XR-mpls-ldp-cfg:default-vrf/Cisco-IOS-XR-mpls-ldp-cfg:global/Cisco-IOS-XR-mpls-ldp-cfg:neighbor/Cisco-IOS-XR-mpls-ldp-cfg:ldp-ids'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.ldp_id is not None:
                            for child_ref in self.ldp_id:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_ldp_cfg as meta
                        return meta._meta_table['MplsLdp.DefaultVrf.Global_.Neighbor.LdpIds']['meta_info']


                class DualStack(object):
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
                        self.parent = None
                        self.tlv_compliance = None
                        self.transport_connection = MplsLdp.DefaultVrf.Global_.Neighbor.DualStack.TransportConnection()
                        self.transport_connection.parent = self


                    class TransportConnection(object):
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
                            self.parent = None
                            self.max_wait = None
                            self.prefer = MplsLdp.DefaultVrf.Global_.Neighbor.DualStack.TransportConnection.Prefer()
                            self.prefer.parent = self


                        class Prefer(object):
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
                                self.parent = None
                                self.ipv4 = None

                            @property
                            def _common_path(self):

                                return '/Cisco-IOS-XR-mpls-ldp-cfg:mpls-ldp/Cisco-IOS-XR-mpls-ldp-cfg:default-vrf/Cisco-IOS-XR-mpls-ldp-cfg:global/Cisco-IOS-XR-mpls-ldp-cfg:neighbor/Cisco-IOS-XR-mpls-ldp-cfg:dual-stack/Cisco-IOS-XR-mpls-ldp-cfg:transport-connection/Cisco-IOS-XR-mpls-ldp-cfg:prefer'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.ipv4 is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_ldp_cfg as meta
                                return meta._meta_table['MplsLdp.DefaultVrf.Global_.Neighbor.DualStack.TransportConnection.Prefer']['meta_info']

                        @property
                        def _common_path(self):

                            return '/Cisco-IOS-XR-mpls-ldp-cfg:mpls-ldp/Cisco-IOS-XR-mpls-ldp-cfg:default-vrf/Cisco-IOS-XR-mpls-ldp-cfg:global/Cisco-IOS-XR-mpls-ldp-cfg:neighbor/Cisco-IOS-XR-mpls-ldp-cfg:dual-stack/Cisco-IOS-XR-mpls-ldp-cfg:transport-connection'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.max_wait is not None:
                                return True

                            if self.prefer is not None and self.prefer._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_ldp_cfg as meta
                            return meta._meta_table['MplsLdp.DefaultVrf.Global_.Neighbor.DualStack.TransportConnection']['meta_info']

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-mpls-ldp-cfg:mpls-ldp/Cisco-IOS-XR-mpls-ldp-cfg:default-vrf/Cisco-IOS-XR-mpls-ldp-cfg:global/Cisco-IOS-XR-mpls-ldp-cfg:neighbor/Cisco-IOS-XR-mpls-ldp-cfg:dual-stack'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.tlv_compliance is not None:
                            return True

                        if self.transport_connection is not None and self.transport_connection._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_ldp_cfg as meta
                        return meta._meta_table['MplsLdp.DefaultVrf.Global_.Neighbor.DualStack']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-mpls-ldp-cfg:mpls-ldp/Cisco-IOS-XR-mpls-ldp-cfg:default-vrf/Cisco-IOS-XR-mpls-ldp-cfg:global/Cisco-IOS-XR-mpls-ldp-cfg:neighbor'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.dual_stack is not None and self.dual_stack._has_data():
                        return True

                    if self.ldp_ids is not None and self.ldp_ids._has_data():
                        return True

                    if self.password is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_ldp_cfg as meta
                    return meta._meta_table['MplsLdp.DefaultVrf.Global_.Neighbor']['meta_info']


            class GracefulRestart(object):
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
                    self.parent = None
                    self.helper_peer = MplsLdp.DefaultVrf.Global_.GracefulRestart.HelperPeer()
                    self.helper_peer.parent = self


                class HelperPeer(object):
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
                        self.parent = None
                        self.maintain_on_local_reset = None

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-mpls-ldp-cfg:mpls-ldp/Cisco-IOS-XR-mpls-ldp-cfg:default-vrf/Cisco-IOS-XR-mpls-ldp-cfg:global/Cisco-IOS-XR-mpls-ldp-cfg:graceful-restart/Cisco-IOS-XR-mpls-ldp-cfg:helper-peer'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.maintain_on_local_reset is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_ldp_cfg as meta
                        return meta._meta_table['MplsLdp.DefaultVrf.Global_.GracefulRestart.HelperPeer']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-mpls-ldp-cfg:mpls-ldp/Cisco-IOS-XR-mpls-ldp-cfg:default-vrf/Cisco-IOS-XR-mpls-ldp-cfg:global/Cisco-IOS-XR-mpls-ldp-cfg:graceful-restart'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.helper_peer is not None and self.helper_peer._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_ldp_cfg as meta
                    return meta._meta_table['MplsLdp.DefaultVrf.Global_.GracefulRestart']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-mpls-ldp-cfg:mpls-ldp/Cisco-IOS-XR-mpls-ldp-cfg:default-vrf/Cisco-IOS-XR-mpls-ldp-cfg:global'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.graceful_restart is not None and self.graceful_restart._has_data():
                    return True

                if self.neighbor is not None and self.neighbor._has_data():
                    return True

                if self.router_id is not None:
                    return True

                if self.session is not None and self.session._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_ldp_cfg as meta
                return meta._meta_table['MplsLdp.DefaultVrf.Global_']['meta_info']


        class Interfaces(object):
            """
            MPLS LDP configuration pertaining to interfaces
            
            .. attribute:: interface
            
            	MPLS LDP configuration for a particular interface
            	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.DefaultVrf.Interfaces.Interface>`
            
            

            """

            _prefix = 'mpls-ldp-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.interface = YList()
                self.interface.parent = self
                self.interface.name = 'interface'


            class Interface(object):
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
                    self.parent = None
                    self.interface_name = None
                    self.afs = MplsLdp.DefaultVrf.Interfaces.Interface.Afs()
                    self.afs.parent = self
                    self.enable = None
                    self.global_ = MplsLdp.DefaultVrf.Interfaces.Interface.Global_()
                    self.global_.parent = self


                class Afs(object):
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
                        self.parent = None
                        self.af = YList()
                        self.af.parent = self
                        self.af.name = 'af'


                    class Af(object):
                        """
                        Configure data for given Address Family
                        
                        .. attribute:: af_name  <key>
                        
                        	Address Family name
                        	**type**\:   :py:class:`MplsLdpafNameEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdpafNameEnum>`
                        
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
                            self.parent = None
                            self.af_name = None
                            self.discovery = MplsLdp.DefaultVrf.Interfaces.Interface.Afs.Af.Discovery()
                            self.discovery.parent = self
                            self.enable = None
                            self.igp = MplsLdp.DefaultVrf.Interfaces.Interface.Afs.Af.Igp()
                            self.igp.parent = self
                            self.mldp = MplsLdp.DefaultVrf.Interfaces.Interface.Afs.Af.Mldp()
                            self.mldp.parent = self


                        class Discovery(object):
                            """
                            Configure interface discovery parameters
                            
                            .. attribute:: transport_address
                            
                            	MPLS LDP configuration for interface discovery transportaddress
                            	**type**\:   :py:class:`TransportAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.DefaultVrf.Interfaces.Interface.Afs.Af.Discovery.TransportAddress>`
                            
                            

                            """

                            _prefix = 'mpls-ldp-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.transport_address = MplsLdp.DefaultVrf.Interfaces.Interface.Afs.Af.Discovery.TransportAddress()
                                self.transport_address.parent = self


                            class TransportAddress(object):
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
                                	**type**\:   :py:class:`MplsLdpTransportAddressEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdpTransportAddressEnum>`
                                
                                

                                """

                                _prefix = 'mpls-ldp-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.address = None
                                    self.address_type = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-mpls-ldp-cfg:transport-address'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.address is not None:
                                        return True

                                    if self.address_type is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_ldp_cfg as meta
                                    return meta._meta_table['MplsLdp.DefaultVrf.Interfaces.Interface.Afs.Af.Discovery.TransportAddress']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-mpls-ldp-cfg:discovery'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.transport_address is not None and self.transport_address._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_ldp_cfg as meta
                                return meta._meta_table['MplsLdp.DefaultVrf.Interfaces.Interface.Afs.Af.Discovery']['meta_info']


                        class Igp(object):
                            """
                            LDP interface IGP configuration
                            
                            .. attribute:: disable_auto_config
                            
                            	Disable IGP Auto\-config on this interface
                            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                            
                            

                            """

                            _prefix = 'mpls-ldp-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.disable_auto_config = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-mpls-ldp-cfg:igp'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.disable_auto_config is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_ldp_cfg as meta
                                return meta._meta_table['MplsLdp.DefaultVrf.Interfaces.Interface.Afs.Af.Igp']['meta_info']


                        class Mldp(object):
                            """
                            Interface configuration parameters for mLDP
                            
                            .. attribute:: disable
                            
                            	Disable mLDP on LDP enabled interface
                            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                            
                            

                            """

                            _prefix = 'mpls-ldp-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.disable = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-mpls-ldp-cfg:mldp'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.disable is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_ldp_cfg as meta
                                return meta._meta_table['MplsLdp.DefaultVrf.Interfaces.Interface.Afs.Af.Mldp']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.af_name is None:
                                raise YPYModelError('Key property af_name is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-mpls-ldp-cfg:af[Cisco-IOS-XR-mpls-ldp-cfg:af-name = ' + str(self.af_name) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.af_name is not None:
                                return True

                            if self.discovery is not None and self.discovery._has_data():
                                return True

                            if self.enable is not None:
                                return True

                            if self.igp is not None and self.igp._has_data():
                                return True

                            if self.mldp is not None and self.mldp._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_ldp_cfg as meta
                            return meta._meta_table['MplsLdp.DefaultVrf.Interfaces.Interface.Afs.Af']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-mpls-ldp-cfg:afs'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.af is not None:
                            for child_ref in self.af:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_ldp_cfg as meta
                        return meta._meta_table['MplsLdp.DefaultVrf.Interfaces.Interface.Afs']['meta_info']


                class Global_(object):
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
                        self.parent = None
                        self.discovery = MplsLdp.DefaultVrf.Interfaces.Interface.Global_.Discovery()
                        self.discovery.parent = self
                        self.igp = MplsLdp.DefaultVrf.Interfaces.Interface.Global_.Igp()
                        self.igp.parent = self


                    class Discovery(object):
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
                            self.parent = None
                            self.disable_quick_start = None
                            self.link_hello = MplsLdp.DefaultVrf.Interfaces.Interface.Global_.Discovery.LinkHello()
                            self.link_hello.parent = self


                        class LinkHello(object):
                            """
                            LDP Link Hellos
                            
                            .. attribute:: dual_stack
                            
                            	Dual Stack Address Family Preference
                            	**type**\:   :py:class:`MplsLdpafNameEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdpafNameEnum>`
                            
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
                                self.parent = None
                                self.dual_stack = None
                                self.hold_time = None
                                self.interval = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-mpls-ldp-cfg:link-hello'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.dual_stack is not None:
                                    return True

                                if self.hold_time is not None:
                                    return True

                                if self.interval is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_ldp_cfg as meta
                                return meta._meta_table['MplsLdp.DefaultVrf.Interfaces.Interface.Global_.Discovery.LinkHello']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-mpls-ldp-cfg:discovery'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.disable_quick_start is not None:
                                return True

                            if self.link_hello is not None and self.link_hello._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_ldp_cfg as meta
                            return meta._meta_table['MplsLdp.DefaultVrf.Interfaces.Interface.Global_.Discovery']['meta_info']


                    class Igp(object):
                        """
                        LDP IGP configuration
                        
                        .. attribute:: sync
                        
                        	LDP IGP synchronization
                        	**type**\:   :py:class:`Sync <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.DefaultVrf.Interfaces.Interface.Global_.Igp.Sync>`
                        
                        

                        """

                        _prefix = 'mpls-ldp-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.sync = MplsLdp.DefaultVrf.Interfaces.Interface.Global_.Igp.Sync()
                            self.sync.parent = self


                        class Sync(object):
                            """
                            LDP IGP synchronization
                            
                            .. attribute:: delay
                            
                            	LDP IGP synchronization delay time
                            	**type**\:   :py:class:`Delay <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.DefaultVrf.Interfaces.Interface.Global_.Igp.Sync.Delay>`
                            
                            

                            """

                            _prefix = 'mpls-ldp-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.delay = MplsLdp.DefaultVrf.Interfaces.Interface.Global_.Igp.Sync.Delay()
                                self.delay.parent = self


                            class Delay(object):
                                """
                                LDP IGP synchronization delay time
                                
                                .. attribute:: on_session_up
                                
                                	Interface sync up delay after session up
                                	**type**\:   :py:class:`OnSessionUp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.DefaultVrf.Interfaces.Interface.Global_.Igp.Sync.Delay.OnSessionUp>`
                                
                                

                                """

                                _prefix = 'mpls-ldp-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.on_session_up = MplsLdp.DefaultVrf.Interfaces.Interface.Global_.Igp.Sync.Delay.OnSessionUp()
                                    self.on_session_up.parent = self


                                class OnSessionUp(object):
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
                                        self.parent = None
                                        self.disable = None
                                        self.timeout = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-mpls-ldp-cfg:on-session-up'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if self.disable is not None:
                                            return True

                                        if self.timeout is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_ldp_cfg as meta
                                        return meta._meta_table['MplsLdp.DefaultVrf.Interfaces.Interface.Global_.Igp.Sync.Delay.OnSessionUp']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-mpls-ldp-cfg:delay'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.on_session_up is not None and self.on_session_up._has_data():
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_ldp_cfg as meta
                                    return meta._meta_table['MplsLdp.DefaultVrf.Interfaces.Interface.Global_.Igp.Sync.Delay']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-mpls-ldp-cfg:sync'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.delay is not None and self.delay._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_ldp_cfg as meta
                                return meta._meta_table['MplsLdp.DefaultVrf.Interfaces.Interface.Global_.Igp.Sync']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-mpls-ldp-cfg:igp'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.sync is not None and self.sync._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_ldp_cfg as meta
                            return meta._meta_table['MplsLdp.DefaultVrf.Interfaces.Interface.Global_.Igp']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-mpls-ldp-cfg:global'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.discovery is not None and self.discovery._has_data():
                            return True

                        if self.igp is not None and self.igp._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_ldp_cfg as meta
                        return meta._meta_table['MplsLdp.DefaultVrf.Interfaces.Interface.Global_']['meta_info']

                @property
                def _common_path(self):
                    if self.interface_name is None:
                        raise YPYModelError('Key property interface_name is None')

                    return '/Cisco-IOS-XR-mpls-ldp-cfg:mpls-ldp/Cisco-IOS-XR-mpls-ldp-cfg:default-vrf/Cisco-IOS-XR-mpls-ldp-cfg:interfaces/Cisco-IOS-XR-mpls-ldp-cfg:interface[Cisco-IOS-XR-mpls-ldp-cfg:interface-name = ' + str(self.interface_name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.interface_name is not None:
                        return True

                    if self.afs is not None and self.afs._has_data():
                        return True

                    if self.enable is not None:
                        return True

                    if self.global_ is not None and self.global_._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_ldp_cfg as meta
                    return meta._meta_table['MplsLdp.DefaultVrf.Interfaces.Interface']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-mpls-ldp-cfg:mpls-ldp/Cisco-IOS-XR-mpls-ldp-cfg:default-vrf/Cisco-IOS-XR-mpls-ldp-cfg:interfaces'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.interface is not None:
                    for child_ref in self.interface:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_ldp_cfg as meta
                return meta._meta_table['MplsLdp.DefaultVrf.Interfaces']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-mpls-ldp-cfg:mpls-ldp/Cisco-IOS-XR-mpls-ldp-cfg:default-vrf'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.afs is not None and self.afs._has_data():
                return True

            if self.global_ is not None and self.global_._has_data():
                return True

            if self.interfaces is not None and self.interfaces._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_ldp_cfg as meta
            return meta._meta_table['MplsLdp.DefaultVrf']['meta_info']


    class Vrfs(object):
        """
        VRF Table attribute configuration for MPLS LDP
        
        .. attribute:: vrf
        
        	VRF attribute configuration for MPLS LDP
        	**type**\: list of    :py:class:`Vrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.Vrfs.Vrf>`
        
        

        """

        _prefix = 'mpls-ldp-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.vrf = YList()
            self.vrf.parent = self
            self.vrf.name = 'vrf'


        class Vrf(object):
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
                self.parent = None
                self.vrf_name = None
                self.afs = MplsLdp.Vrfs.Vrf.Afs()
                self.afs.parent = self
                self.enable = None
                self.global_ = MplsLdp.Vrfs.Vrf.Global_()
                self.global_.parent = self
                self.interfaces = MplsLdp.Vrfs.Vrf.Interfaces()
                self.interfaces.parent = self


            class Global_(object):
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
                    self.parent = None
                    self.graceful_restart = MplsLdp.Vrfs.Vrf.Global_.GracefulRestart()
                    self.graceful_restart.parent = self
                    self.neighbor = MplsLdp.Vrfs.Vrf.Global_.Neighbor()
                    self.neighbor.parent = self
                    self.router_id = None
                    self.session = MplsLdp.Vrfs.Vrf.Global_.Session()
                    self.session.parent = self


                class Session(object):
                    """
                    LDP Session parameters
                    
                    .. attribute:: downstream_on_demand
                    
                    	ACL with the list of neighbors configured for Downstream on Demand
                    	**type**\:   :py:class:`DownstreamOnDemand <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.Vrfs.Vrf.Global_.Session.DownstreamOnDemand>`
                    
                    

                    """

                    _prefix = 'mpls-ldp-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.downstream_on_demand = MplsLdp.Vrfs.Vrf.Global_.Session.DownstreamOnDemand()
                        self.downstream_on_demand.parent = self


                    class DownstreamOnDemand(object):
                        """
                        ACL with the list of neighbors configured
                        for Downstream on Demand
                        
                        .. attribute:: peer_acl_name
                        
                        	Name of peer ACL
                        	**type**\:  str
                        
                        .. attribute:: type
                        
                        	Downstream on demand type
                        	**type**\:   :py:class:`MplsLdpDownstreamOnDemandEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdpDownstreamOnDemandEnum>`
                        
                        

                        """

                        _prefix = 'mpls-ldp-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.peer_acl_name = None
                            self.type = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-mpls-ldp-cfg:downstream-on-demand'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.peer_acl_name is not None:
                                return True

                            if self.type is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_ldp_cfg as meta
                            return meta._meta_table['MplsLdp.Vrfs.Vrf.Global_.Session.DownstreamOnDemand']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-mpls-ldp-cfg:session'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.downstream_on_demand is not None and self.downstream_on_demand._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_ldp_cfg as meta
                        return meta._meta_table['MplsLdp.Vrfs.Vrf.Global_.Session']['meta_info']


                class Neighbor(object):
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
                        self.parent = None
                        self.ldp_ids = MplsLdp.Vrfs.Vrf.Global_.Neighbor.LdpIds()
                        self.ldp_ids.parent = self
                        self.password = None


                    class LdpIds(object):
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
                            self.parent = None
                            self.ldp_id = YList()
                            self.ldp_id.parent = self
                            self.ldp_id.name = 'ldp_id'


                        class LdpId(object):
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
                                self.parent = None
                                self.lsr_id = None
                                self.label_space_id = None
                                self.password = MplsLdp.Vrfs.Vrf.Global_.Neighbor.LdpIds.LdpId.Password()
                                self.password.parent = self


                            class Password(object):
                                """
                                Password for MD5 authentication for this
                                neighbor
                                
                                .. attribute:: command_type
                                
                                	Command type for password configuration
                                	**type**\:   :py:class:`MplsLdpNbrPasswordEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdpNbrPasswordEnum>`
                                
                                .. attribute:: password
                                
                                	The neighbor password
                                	**type**\:  str
                                
                                	**pattern:** (!.+)\|([^!].+)
                                
                                

                                """

                                _prefix = 'mpls-ldp-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.command_type = None
                                    self.password = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-mpls-ldp-cfg:password'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.command_type is not None:
                                        return True

                                    if self.password is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_ldp_cfg as meta
                                    return meta._meta_table['MplsLdp.Vrfs.Vrf.Global_.Neighbor.LdpIds.LdpId.Password']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                if self.lsr_id is None:
                                    raise YPYModelError('Key property lsr_id is None')
                                if self.label_space_id is None:
                                    raise YPYModelError('Key property label_space_id is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-mpls-ldp-cfg:ldp-id[Cisco-IOS-XR-mpls-ldp-cfg:lsr-id = ' + str(self.lsr_id) + '][Cisco-IOS-XR-mpls-ldp-cfg:label-space-id = ' + str(self.label_space_id) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.lsr_id is not None:
                                    return True

                                if self.label_space_id is not None:
                                    return True

                                if self.password is not None and self.password._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_ldp_cfg as meta
                                return meta._meta_table['MplsLdp.Vrfs.Vrf.Global_.Neighbor.LdpIds.LdpId']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-mpls-ldp-cfg:ldp-ids'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.ldp_id is not None:
                                for child_ref in self.ldp_id:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_ldp_cfg as meta
                            return meta._meta_table['MplsLdp.Vrfs.Vrf.Global_.Neighbor.LdpIds']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-mpls-ldp-cfg:neighbor'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.ldp_ids is not None and self.ldp_ids._has_data():
                            return True

                        if self.password is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_ldp_cfg as meta
                        return meta._meta_table['MplsLdp.Vrfs.Vrf.Global_.Neighbor']['meta_info']


                class GracefulRestart(object):
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
                        self.parent = None
                        self.helper_peer = MplsLdp.Vrfs.Vrf.Global_.GracefulRestart.HelperPeer()
                        self.helper_peer.parent = self


                    class HelperPeer(object):
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
                            self.parent = None
                            self.maintain_on_local_reset = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-mpls-ldp-cfg:helper-peer'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.maintain_on_local_reset is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_ldp_cfg as meta
                            return meta._meta_table['MplsLdp.Vrfs.Vrf.Global_.GracefulRestart.HelperPeer']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-mpls-ldp-cfg:graceful-restart'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.helper_peer is not None and self.helper_peer._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_ldp_cfg as meta
                        return meta._meta_table['MplsLdp.Vrfs.Vrf.Global_.GracefulRestart']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-mpls-ldp-cfg:global'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.graceful_restart is not None and self.graceful_restart._has_data():
                        return True

                    if self.neighbor is not None and self.neighbor._has_data():
                        return True

                    if self.router_id is not None:
                        return True

                    if self.session is not None and self.session._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_ldp_cfg as meta
                    return meta._meta_table['MplsLdp.Vrfs.Vrf.Global_']['meta_info']


            class Afs(object):
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
                    self.parent = None
                    self.af = YList()
                    self.af.parent = self
                    self.af.name = 'af'


                class Af(object):
                    """
                    Configure data for given Address Family
                    
                    .. attribute:: af_name  <key>
                    
                    	Address Family name
                    	**type**\:   :py:class:`MplsLdpafNameEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdpafNameEnum>`
                    
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
                        self.parent = None
                        self.af_name = None
                        self.discovery = MplsLdp.Vrfs.Vrf.Afs.Af.Discovery()
                        self.discovery.parent = self
                        self.enable = None
                        self.label = MplsLdp.Vrfs.Vrf.Afs.Af.Label()
                        self.label.parent = self


                    class Discovery(object):
                        """
                        Configure Discovery parameters
                        
                        .. attribute:: transport_address
                        
                        	Global discovery transport address for address family
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'mpls-ldp-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.transport_address = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-mpls-ldp-cfg:discovery'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.transport_address is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_ldp_cfg as meta
                            return meta._meta_table['MplsLdp.Vrfs.Vrf.Afs.Af.Discovery']['meta_info']


                    class Label(object):
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
                            self.parent = None
                            self.local = MplsLdp.Vrfs.Vrf.Afs.Af.Label.Local()
                            self.local.parent = self
                            self.remote = MplsLdp.Vrfs.Vrf.Afs.Af.Label.Remote()
                            self.remote.parent = self


                        class Remote(object):
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
                                self.parent = None
                                self.accept = MplsLdp.Vrfs.Vrf.Afs.Af.Label.Remote.Accept()
                                self.accept.parent = self


                            class Accept(object):
                                """
                                Configure inbound label acceptance
                                
                                .. attribute:: peer_accept_policies
                                
                                	Configuration related to Neighbors for inbound label acceptance
                                	**type**\:   :py:class:`PeerAcceptPolicies <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.Vrfs.Vrf.Afs.Af.Label.Remote.Accept.PeerAcceptPolicies>`
                                
                                

                                """

                                _prefix = 'mpls-ldp-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.peer_accept_policies = MplsLdp.Vrfs.Vrf.Afs.Af.Label.Remote.Accept.PeerAcceptPolicies()
                                    self.peer_accept_policies.parent = self


                                class PeerAcceptPolicies(object):
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
                                        self.parent = None
                                        self.peer_accept_policy = YList()
                                        self.peer_accept_policy.parent = self
                                        self.peer_accept_policy.name = 'peer_accept_policy'


                                    class PeerAcceptPolicy(object):
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
                                            self.parent = None
                                            self.label_space_id = None
                                            self.lsr_id = YList()
                                            self.lsr_id.parent = self
                                            self.lsr_id.name = 'lsr_id'
                                            self.peer_accept_policy_data = MplsLdp.Vrfs.Vrf.Afs.Af.Label.Remote.Accept.PeerAcceptPolicies.PeerAcceptPolicy.PeerAcceptPolicyData()
                                            self.peer_accept_policy_data.parent = self


                                        class PeerAcceptPolicyData(object):
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
                                                self.parent = None
                                                self.prefix_acl_name = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-mpls-ldp-cfg:peer-accept-policy-data'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return True

                                            def _has_data(self):
                                                if self.prefix_acl_name is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_ldp_cfg as meta
                                                return meta._meta_table['MplsLdp.Vrfs.Vrf.Afs.Af.Label.Remote.Accept.PeerAcceptPolicies.PeerAcceptPolicy.PeerAcceptPolicyData']['meta_info']


                                        class LsrId(object):
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
                                                self.parent = None
                                                self.lsr_id = None
                                                self.prefix_acl_name = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                                if self.lsr_id is None:
                                                    raise YPYModelError('Key property lsr_id is None')

                                                return self.parent._common_path +'/Cisco-IOS-XR-mpls-ldp-cfg:lsr-id[Cisco-IOS-XR-mpls-ldp-cfg:lsr-id = ' + str(self.lsr_id) + ']'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return True

                                            def _has_data(self):
                                                if self.lsr_id is not None:
                                                    return True

                                                if self.prefix_acl_name is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_ldp_cfg as meta
                                                return meta._meta_table['MplsLdp.Vrfs.Vrf.Afs.Af.Label.Remote.Accept.PeerAcceptPolicies.PeerAcceptPolicy.LsrId']['meta_info']

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')
                                            if self.label_space_id is None:
                                                raise YPYModelError('Key property label_space_id is None')

                                            return self.parent._common_path +'/Cisco-IOS-XR-mpls-ldp-cfg:peer-accept-policy[Cisco-IOS-XR-mpls-ldp-cfg:label-space-id = ' + str(self.label_space_id) + ']'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return True

                                        def _has_data(self):
                                            if self.label_space_id is not None:
                                                return True

                                            if self.lsr_id is not None:
                                                for child_ref in self.lsr_id:
                                                    if child_ref._has_data():
                                                        return True

                                            if self.peer_accept_policy_data is not None and self.peer_accept_policy_data._has_data():
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_ldp_cfg as meta
                                            return meta._meta_table['MplsLdp.Vrfs.Vrf.Afs.Af.Label.Remote.Accept.PeerAcceptPolicies.PeerAcceptPolicy']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-mpls-ldp-cfg:peer-accept-policies'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if self.peer_accept_policy is not None:
                                            for child_ref in self.peer_accept_policy:
                                                if child_ref._has_data():
                                                    return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_ldp_cfg as meta
                                        return meta._meta_table['MplsLdp.Vrfs.Vrf.Afs.Af.Label.Remote.Accept.PeerAcceptPolicies']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-mpls-ldp-cfg:accept'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.peer_accept_policies is not None and self.peer_accept_policies._has_data():
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_ldp_cfg as meta
                                    return meta._meta_table['MplsLdp.Vrfs.Vrf.Afs.Af.Label.Remote.Accept']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-mpls-ldp-cfg:remote'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.accept is not None and self.accept._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_ldp_cfg as meta
                                return meta._meta_table['MplsLdp.Vrfs.Vrf.Afs.Af.Label.Remote']['meta_info']


                        class Local(object):
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
                                self.parent = None
                                self.advertise = MplsLdp.Vrfs.Vrf.Afs.Af.Label.Local.Advertise()
                                self.advertise.parent = self
                                self.allocate = MplsLdp.Vrfs.Vrf.Afs.Af.Label.Local.Allocate()
                                self.allocate.parent = self
                                self.default_route = None
                                self.implicit_null_override = None


                            class Advertise(object):
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
                                    self.parent = None
                                    self.disable = None
                                    self.explicit_null = MplsLdp.Vrfs.Vrf.Afs.Af.Label.Local.Advertise.ExplicitNull()
                                    self.explicit_null.parent = self
                                    self.interfaces = MplsLdp.Vrfs.Vrf.Afs.Af.Label.Local.Advertise.Interfaces()
                                    self.interfaces.parent = self
                                    self.peer_advertise_policies = MplsLdp.Vrfs.Vrf.Afs.Af.Label.Local.Advertise.PeerAdvertisePolicies()
                                    self.peer_advertise_policies.parent = self


                                class PeerAdvertisePolicies(object):
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
                                        self.parent = None
                                        self.peer_advertise_policy = YList()
                                        self.peer_advertise_policy.parent = self
                                        self.peer_advertise_policy.name = 'peer_advertise_policy'


                                    class PeerAdvertisePolicy(object):
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
                                            self.parent = None
                                            self.label_space_id = None
                                            self.lsr_id = YList()
                                            self.lsr_id.parent = self
                                            self.lsr_id.name = 'lsr_id'
                                            self.peer_advertise_policy_data = MplsLdp.Vrfs.Vrf.Afs.Af.Label.Local.Advertise.PeerAdvertisePolicies.PeerAdvertisePolicy.PeerAdvertisePolicyData()
                                            self.peer_advertise_policy_data.parent = self


                                        class PeerAdvertisePolicyData(object):
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
                                                self.parent = None
                                                self.prefix_acl_name = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-mpls-ldp-cfg:peer-advertise-policy-data'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return True

                                            def _has_data(self):
                                                if self.prefix_acl_name is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_ldp_cfg as meta
                                                return meta._meta_table['MplsLdp.Vrfs.Vrf.Afs.Af.Label.Local.Advertise.PeerAdvertisePolicies.PeerAdvertisePolicy.PeerAdvertisePolicyData']['meta_info']


                                        class LsrId(object):
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
                                                self.parent = None
                                                self.lsr_id = None
                                                self.prefix_acl_name = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                                if self.lsr_id is None:
                                                    raise YPYModelError('Key property lsr_id is None')

                                                return self.parent._common_path +'/Cisco-IOS-XR-mpls-ldp-cfg:lsr-id[Cisco-IOS-XR-mpls-ldp-cfg:lsr-id = ' + str(self.lsr_id) + ']'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return True

                                            def _has_data(self):
                                                if self.lsr_id is not None:
                                                    return True

                                                if self.prefix_acl_name is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_ldp_cfg as meta
                                                return meta._meta_table['MplsLdp.Vrfs.Vrf.Afs.Af.Label.Local.Advertise.PeerAdvertisePolicies.PeerAdvertisePolicy.LsrId']['meta_info']

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')
                                            if self.label_space_id is None:
                                                raise YPYModelError('Key property label_space_id is None')

                                            return self.parent._common_path +'/Cisco-IOS-XR-mpls-ldp-cfg:peer-advertise-policy[Cisco-IOS-XR-mpls-ldp-cfg:label-space-id = ' + str(self.label_space_id) + ']'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return True

                                        def _has_data(self):
                                            if self.label_space_id is not None:
                                                return True

                                            if self.lsr_id is not None:
                                                for child_ref in self.lsr_id:
                                                    if child_ref._has_data():
                                                        return True

                                            if self.peer_advertise_policy_data is not None and self.peer_advertise_policy_data._has_data():
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_ldp_cfg as meta
                                            return meta._meta_table['MplsLdp.Vrfs.Vrf.Afs.Af.Label.Local.Advertise.PeerAdvertisePolicies.PeerAdvertisePolicy']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-mpls-ldp-cfg:peer-advertise-policies'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if self.peer_advertise_policy is not None:
                                            for child_ref in self.peer_advertise_policy:
                                                if child_ref._has_data():
                                                    return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_ldp_cfg as meta
                                        return meta._meta_table['MplsLdp.Vrfs.Vrf.Afs.Af.Label.Local.Advertise.PeerAdvertisePolicies']['meta_info']


                                class Interfaces(object):
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
                                        self.parent = None
                                        self.interface = YList()
                                        self.interface.parent = self
                                        self.interface.name = 'interface'


                                    class Interface(object):
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
                                            self.parent = None
                                            self.interface_name = None

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')
                                            if self.interface_name is None:
                                                raise YPYModelError('Key property interface_name is None')

                                            return self.parent._common_path +'/Cisco-IOS-XR-mpls-ldp-cfg:interface[Cisco-IOS-XR-mpls-ldp-cfg:interface-name = ' + str(self.interface_name) + ']'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return True

                                        def _has_data(self):
                                            if self.interface_name is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_ldp_cfg as meta
                                            return meta._meta_table['MplsLdp.Vrfs.Vrf.Afs.Af.Label.Local.Advertise.Interfaces.Interface']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-mpls-ldp-cfg:interfaces'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if self.interface is not None:
                                            for child_ref in self.interface:
                                                if child_ref._has_data():
                                                    return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_ldp_cfg as meta
                                        return meta._meta_table['MplsLdp.Vrfs.Vrf.Afs.Af.Label.Local.Advertise.Interfaces']['meta_info']


                                class ExplicitNull(object):
                                    """
                                    Configure advertisment of explicit\-null
                                    for connected prefixes.
                                    
                                    .. attribute:: explicit_null_type
                                    
                                    	Explicit Null command variant
                                    	**type**\:   :py:class:`MplsLdpExpNullEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdpExpNullEnum>`
                                    
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
                                        self.parent = None
                                        self.explicit_null_type = None
                                        self.peer_acl_name = None
                                        self.prefix_acl_name = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-mpls-ldp-cfg:explicit-null'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if self.explicit_null_type is not None:
                                            return True

                                        if self.peer_acl_name is not None:
                                            return True

                                        if self.prefix_acl_name is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_ldp_cfg as meta
                                        return meta._meta_table['MplsLdp.Vrfs.Vrf.Afs.Af.Label.Local.Advertise.ExplicitNull']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-mpls-ldp-cfg:advertise'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.disable is not None:
                                        return True

                                    if self.explicit_null is not None and self.explicit_null._has_data():
                                        return True

                                    if self.interfaces is not None and self.interfaces._has_data():
                                        return True

                                    if self.peer_advertise_policies is not None and self.peer_advertise_policies._has_data():
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_ldp_cfg as meta
                                    return meta._meta_table['MplsLdp.Vrfs.Vrf.Afs.Af.Label.Local.Advertise']['meta_info']


                            class Allocate(object):
                                """
                                Control local label allocation for
                                prefix(es)
                                
                                .. attribute:: allocation_type
                                
                                	Label allocation type
                                	**type**\:   :py:class:`MplsLdpLabelAllocationEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdpLabelAllocationEnum>`
                                
                                .. attribute:: prefix_acl_name
                                
                                	Name of prefix ACL
                                	**type**\:  str
                                
                                

                                """

                                _prefix = 'mpls-ldp-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.allocation_type = None
                                    self.prefix_acl_name = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-mpls-ldp-cfg:allocate'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.allocation_type is not None:
                                        return True

                                    if self.prefix_acl_name is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_ldp_cfg as meta
                                    return meta._meta_table['MplsLdp.Vrfs.Vrf.Afs.Af.Label.Local.Allocate']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-mpls-ldp-cfg:local'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.advertise is not None and self.advertise._has_data():
                                    return True

                                if self.allocate is not None and self.allocate._has_data():
                                    return True

                                if self.default_route is not None:
                                    return True

                                if self.implicit_null_override is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_ldp_cfg as meta
                                return meta._meta_table['MplsLdp.Vrfs.Vrf.Afs.Af.Label.Local']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-mpls-ldp-cfg:label'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.local is not None and self.local._has_data():
                                return True

                            if self.remote is not None and self.remote._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_ldp_cfg as meta
                            return meta._meta_table['MplsLdp.Vrfs.Vrf.Afs.Af.Label']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.af_name is None:
                            raise YPYModelError('Key property af_name is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-mpls-ldp-cfg:af[Cisco-IOS-XR-mpls-ldp-cfg:af-name = ' + str(self.af_name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.af_name is not None:
                            return True

                        if self.discovery is not None and self.discovery._has_data():
                            return True

                        if self.enable is not None:
                            return True

                        if self.label is not None and self.label._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_ldp_cfg as meta
                        return meta._meta_table['MplsLdp.Vrfs.Vrf.Afs.Af']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-mpls-ldp-cfg:afs'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.af is not None:
                        for child_ref in self.af:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_ldp_cfg as meta
                    return meta._meta_table['MplsLdp.Vrfs.Vrf.Afs']['meta_info']


            class Interfaces(object):
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
                    self.parent = None
                    self.interface = YList()
                    self.interface.parent = self
                    self.interface.name = 'interface'


                class Interface(object):
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
                        self.parent = None
                        self.interface_name = None
                        self.afs = MplsLdp.Vrfs.Vrf.Interfaces.Interface.Afs()
                        self.afs.parent = self
                        self.enable = None


                    class Afs(object):
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
                            self.parent = None
                            self.af = YList()
                            self.af.parent = self
                            self.af.name = 'af'


                        class Af(object):
                            """
                            Configure data for given Address Family
                            
                            .. attribute:: af_name  <key>
                            
                            	Address Family name
                            	**type**\:   :py:class:`MplsLdpafNameEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdpafNameEnum>`
                            
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
                                self.parent = None
                                self.af_name = None
                                self.discovery = MplsLdp.Vrfs.Vrf.Interfaces.Interface.Afs.Af.Discovery()
                                self.discovery.parent = self
                                self.enable = None


                            class Discovery(object):
                                """
                                Configure interface discovery parameters
                                
                                .. attribute:: transport_address
                                
                                	MPLS LDP configuration for interface discovery transportaddress
                                	**type**\:   :py:class:`TransportAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.Vrfs.Vrf.Interfaces.Interface.Afs.Af.Discovery.TransportAddress>`
                                
                                

                                """

                                _prefix = 'mpls-ldp-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.transport_address = MplsLdp.Vrfs.Vrf.Interfaces.Interface.Afs.Af.Discovery.TransportAddress()
                                    self.transport_address.parent = self


                                class TransportAddress(object):
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
                                    	**type**\:   :py:class:`MplsLdpTransportAddressEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdpTransportAddressEnum>`
                                    
                                    

                                    """

                                    _prefix = 'mpls-ldp-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.address = None
                                        self.address_type = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-mpls-ldp-cfg:transport-address'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if self.address is not None:
                                            return True

                                        if self.address_type is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_ldp_cfg as meta
                                        return meta._meta_table['MplsLdp.Vrfs.Vrf.Interfaces.Interface.Afs.Af.Discovery.TransportAddress']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-mpls-ldp-cfg:discovery'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.transport_address is not None and self.transport_address._has_data():
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_ldp_cfg as meta
                                    return meta._meta_table['MplsLdp.Vrfs.Vrf.Interfaces.Interface.Afs.Af.Discovery']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                if self.af_name is None:
                                    raise YPYModelError('Key property af_name is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-mpls-ldp-cfg:af[Cisco-IOS-XR-mpls-ldp-cfg:af-name = ' + str(self.af_name) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.af_name is not None:
                                    return True

                                if self.discovery is not None and self.discovery._has_data():
                                    return True

                                if self.enable is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_ldp_cfg as meta
                                return meta._meta_table['MplsLdp.Vrfs.Vrf.Interfaces.Interface.Afs.Af']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-mpls-ldp-cfg:afs'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.af is not None:
                                for child_ref in self.af:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_ldp_cfg as meta
                            return meta._meta_table['MplsLdp.Vrfs.Vrf.Interfaces.Interface.Afs']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.interface_name is None:
                            raise YPYModelError('Key property interface_name is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-mpls-ldp-cfg:interface[Cisco-IOS-XR-mpls-ldp-cfg:interface-name = ' + str(self.interface_name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.interface_name is not None:
                            return True

                        if self.afs is not None and self.afs._has_data():
                            return True

                        if self.enable is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_ldp_cfg as meta
                        return meta._meta_table['MplsLdp.Vrfs.Vrf.Interfaces.Interface']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-mpls-ldp-cfg:interfaces'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.interface is not None:
                        for child_ref in self.interface:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_ldp_cfg as meta
                    return meta._meta_table['MplsLdp.Vrfs.Vrf.Interfaces']['meta_info']

            @property
            def _common_path(self):
                if self.vrf_name is None:
                    raise YPYModelError('Key property vrf_name is None')

                return '/Cisco-IOS-XR-mpls-ldp-cfg:mpls-ldp/Cisco-IOS-XR-mpls-ldp-cfg:vrfs/Cisco-IOS-XR-mpls-ldp-cfg:vrf[Cisco-IOS-XR-mpls-ldp-cfg:vrf-name = ' + str(self.vrf_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.vrf_name is not None:
                    return True

                if self.afs is not None and self.afs._has_data():
                    return True

                if self.enable is not None:
                    return True

                if self.global_ is not None and self.global_._has_data():
                    return True

                if self.interfaces is not None and self.interfaces._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_ldp_cfg as meta
                return meta._meta_table['MplsLdp.Vrfs.Vrf']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-mpls-ldp-cfg:mpls-ldp/Cisco-IOS-XR-mpls-ldp-cfg:vrfs'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.vrf is not None:
                for child_ref in self.vrf:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_ldp_cfg as meta
            return meta._meta_table['MplsLdp.Vrfs']['meta_info']


    class Global_(object):
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
            self.parent = None
            self.disable_implicit_ipv4 = None
            self.discovery = MplsLdp.Global_.Discovery()
            self.discovery.parent = self
            self.enable_logging = MplsLdp.Global_.EnableLogging()
            self.enable_logging.parent = self
            self.entropy_label = MplsLdp.Global_.EntropyLabel()
            self.entropy_label.parent = self
            self.graceful_restart = MplsLdp.Global_.GracefulRestart()
            self.graceful_restart.parent = self
            self.igp = MplsLdp.Global_.Igp()
            self.igp.parent = self
            self.ltrace_buf_multiplier = None
            self.mldp = MplsLdp.Global_.Mldp()
            self.mldp.parent = self
            self.nsr = MplsLdp.Global_.Nsr()
            self.nsr.parent = self
            self.session = MplsLdp.Global_.Session()
            self.session.parent = self
            self.signalling = MplsLdp.Global_.Signalling()
            self.signalling.parent = self


        class EntropyLabel(object):
            """
            Configure for LDP Entropy\-Label
            
            .. attribute:: enable
            
            	none
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'mpls-ldp-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.enable = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-mpls-ldp-cfg:mpls-ldp/Cisco-IOS-XR-mpls-ldp-cfg:global/Cisco-IOS-XR-mpls-ldp-cfg:entropy-label'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.enable is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_ldp_cfg as meta
                return meta._meta_table['MplsLdp.Global_.EntropyLabel']['meta_info']


        class Session(object):
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
                self.parent = None
                self.backoff_time = MplsLdp.Global_.Session.BackoffTime()
                self.backoff_time.parent = self
                self.hold_time = None


            class BackoffTime(object):
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
                    self.parent = None
                    self.initial_backoff_time = None
                    self.max_backoff_time = None

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-mpls-ldp-cfg:mpls-ldp/Cisco-IOS-XR-mpls-ldp-cfg:global/Cisco-IOS-XR-mpls-ldp-cfg:session/Cisco-IOS-XR-mpls-ldp-cfg:backoff-time'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.initial_backoff_time is not None:
                        return True

                    if self.max_backoff_time is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_ldp_cfg as meta
                    return meta._meta_table['MplsLdp.Global_.Session.BackoffTime']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-mpls-ldp-cfg:mpls-ldp/Cisco-IOS-XR-mpls-ldp-cfg:global/Cisco-IOS-XR-mpls-ldp-cfg:session'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.backoff_time is not None and self.backoff_time._has_data():
                    return True

                if self.hold_time is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_ldp_cfg as meta
                return meta._meta_table['MplsLdp.Global_.Session']['meta_info']


        class Igp(object):
            """
            LDP IGP configuration
            
            .. attribute:: sync
            
            	LDP IGP synchronization
            	**type**\:   :py:class:`Sync <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.Global_.Igp.Sync>`
            
            

            """

            _prefix = 'mpls-ldp-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.sync = MplsLdp.Global_.Igp.Sync()
                self.sync.parent = self


            class Sync(object):
                """
                LDP IGP synchronization
                
                .. attribute:: delay
                
                	LDP IGP synchronization delay time
                	**type**\:   :py:class:`Delay <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.Global_.Igp.Sync.Delay>`
                
                

                """

                _prefix = 'mpls-ldp-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.delay = MplsLdp.Global_.Igp.Sync.Delay()
                    self.delay.parent = self


                class Delay(object):
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
                        self.parent = None
                        self.on_proc_restart = None
                        self.on_session_up = None

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-mpls-ldp-cfg:mpls-ldp/Cisco-IOS-XR-mpls-ldp-cfg:global/Cisco-IOS-XR-mpls-ldp-cfg:igp/Cisco-IOS-XR-mpls-ldp-cfg:sync/Cisco-IOS-XR-mpls-ldp-cfg:delay'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.on_proc_restart is not None:
                            return True

                        if self.on_session_up is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_ldp_cfg as meta
                        return meta._meta_table['MplsLdp.Global_.Igp.Sync.Delay']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-mpls-ldp-cfg:mpls-ldp/Cisco-IOS-XR-mpls-ldp-cfg:global/Cisco-IOS-XR-mpls-ldp-cfg:igp/Cisco-IOS-XR-mpls-ldp-cfg:sync'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.delay is not None and self.delay._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_ldp_cfg as meta
                    return meta._meta_table['MplsLdp.Global_.Igp.Sync']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-mpls-ldp-cfg:mpls-ldp/Cisco-IOS-XR-mpls-ldp-cfg:global/Cisco-IOS-XR-mpls-ldp-cfg:igp'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.sync is not None and self.sync._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_ldp_cfg as meta
                return meta._meta_table['MplsLdp.Global_.Igp']['meta_info']


        class EnableLogging(object):
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
                self.parent = None
                self.adjacency = None
                self.gr_session_changes = None
                self.neighbor_changes = None
                self.nsr = None
                self.session_protection = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-mpls-ldp-cfg:mpls-ldp/Cisco-IOS-XR-mpls-ldp-cfg:global/Cisco-IOS-XR-mpls-ldp-cfg:enable-logging'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.adjacency is not None:
                    return True

                if self.gr_session_changes is not None:
                    return True

                if self.neighbor_changes is not None:
                    return True

                if self.nsr is not None:
                    return True

                if self.session_protection is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_ldp_cfg as meta
                return meta._meta_table['MplsLdp.Global_.EnableLogging']['meta_info']


        class Signalling(object):
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
                self.parent = None
                self.dscp = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-mpls-ldp-cfg:mpls-ldp/Cisco-IOS-XR-mpls-ldp-cfg:global/Cisco-IOS-XR-mpls-ldp-cfg:signalling'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.dscp is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_ldp_cfg as meta
                return meta._meta_table['MplsLdp.Global_.Signalling']['meta_info']


        class Nsr(object):
            """
            Configure LDP Non\-Stop Routing
            
            .. attribute:: enable
            
            	none
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'mpls-ldp-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.enable = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-mpls-ldp-cfg:mpls-ldp/Cisco-IOS-XR-mpls-ldp-cfg:global/Cisco-IOS-XR-mpls-ldp-cfg:nsr'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.enable is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_ldp_cfg as meta
                return meta._meta_table['MplsLdp.Global_.Nsr']['meta_info']


        class GracefulRestart(object):
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
                self.parent = None
                self.enable = None
                self.forwarding_hold_time = None
                self.reconnect_timeout = None

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-mpls-ldp-cfg:mpls-ldp/Cisco-IOS-XR-mpls-ldp-cfg:global/Cisco-IOS-XR-mpls-ldp-cfg:graceful-restart'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.enable is not None:
                    return True

                if self.forwarding_hold_time is not None:
                    return True

                if self.reconnect_timeout is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_ldp_cfg as meta
                return meta._meta_table['MplsLdp.Global_.GracefulRestart']['meta_info']


        class Discovery(object):
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
                self.parent = None
                self.disable_instance_tlv = None
                self.disable_quick_start = None
                self.link_hello = MplsLdp.Global_.Discovery.LinkHello()
                self.link_hello.parent = self
                self.targeted_hello = MplsLdp.Global_.Discovery.TargetedHello()
                self.targeted_hello.parent = self


            class LinkHello(object):
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
                    self.parent = None
                    self.hold_time = None
                    self.interval = None

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-mpls-ldp-cfg:mpls-ldp/Cisco-IOS-XR-mpls-ldp-cfg:global/Cisco-IOS-XR-mpls-ldp-cfg:discovery/Cisco-IOS-XR-mpls-ldp-cfg:link-hello'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.hold_time is not None:
                        return True

                    if self.interval is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_ldp_cfg as meta
                    return meta._meta_table['MplsLdp.Global_.Discovery.LinkHello']['meta_info']


            class TargetedHello(object):
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
                    self.parent = None
                    self.hold_time = None
                    self.interval = None

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-mpls-ldp-cfg:mpls-ldp/Cisco-IOS-XR-mpls-ldp-cfg:global/Cisco-IOS-XR-mpls-ldp-cfg:discovery/Cisco-IOS-XR-mpls-ldp-cfg:targeted-hello'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.hold_time is not None:
                        return True

                    if self.interval is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_ldp_cfg as meta
                    return meta._meta_table['MplsLdp.Global_.Discovery.TargetedHello']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-mpls-ldp-cfg:mpls-ldp/Cisco-IOS-XR-mpls-ldp-cfg:global/Cisco-IOS-XR-mpls-ldp-cfg:discovery'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.disable_instance_tlv is not None:
                    return True

                if self.disable_quick_start is not None:
                    return True

                if self.link_hello is not None and self.link_hello._has_data():
                    return True

                if self.targeted_hello is not None and self.targeted_hello._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_ldp_cfg as meta
                return meta._meta_table['MplsLdp.Global_.Discovery']['meta_info']


        class Mldp(object):
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
                self.parent = None
                self.default_vrf = MplsLdp.Global_.Mldp.DefaultVrf()
                self.default_vrf.parent = self
                self.enable = None
                self.mldp_global = MplsLdp.Global_.Mldp.MldpGlobal()
                self.mldp_global.parent = self
                self.vrfs = MplsLdp.Global_.Mldp.Vrfs()
                self.vrfs.parent = self


            class Vrfs(object):
                """
                VRF Table attribute configuration for MPLS LDP
                
                .. attribute:: vrf
                
                	VRF attribute configuration for MPLS LDP
                	**type**\: list of    :py:class:`Vrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.Global_.Mldp.Vrfs.Vrf>`
                
                

                """

                _prefix = 'mpls-ldp-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.vrf = YList()
                    self.vrf.parent = self
                    self.vrf.name = 'vrf'


                class Vrf(object):
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
                        self.parent = None
                        self.vrf_name = None
                        self.afs = MplsLdp.Global_.Mldp.Vrfs.Vrf.Afs()
                        self.afs.parent = self
                        self.enable = None


                    class Afs(object):
                        """
                        Address Family specific operational data
                        
                        .. attribute:: af
                        
                        	Operational data for given Address Family
                        	**type**\: list of    :py:class:`Af <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.Global_.Mldp.Vrfs.Vrf.Afs.Af>`
                        
                        

                        """

                        _prefix = 'mpls-ldp-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.af = YList()
                            self.af.parent = self
                            self.af.name = 'af'


                        class Af(object):
                            """
                            Operational data for given Address Family
                            
                            .. attribute:: af_name  <key>
                            
                            	Address Family name
                            	**type**\:   :py:class:`MplsLdpafNameEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdpafNameEnum>`
                            
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
                                self.parent = None
                                self.af_name = None
                                self.csc = MplsLdp.Global_.Mldp.Vrfs.Vrf.Afs.Af.Csc()
                                self.csc.parent = self
                                self.enable = None
                                self.make_before_break = MplsLdp.Global_.Mldp.Vrfs.Vrf.Afs.Af.MakeBeforeBreak()
                                self.make_before_break.parent = self
                                self.mldp_recursive_fec = MplsLdp.Global_.Mldp.Vrfs.Vrf.Afs.Af.MldpRecursiveFec()
                                self.mldp_recursive_fec.parent = self
                                self.mldp_rib_unicast_always = None
                                self.mo_frr = MplsLdp.Global_.Mldp.Vrfs.Vrf.Afs.Af.MoFrr()
                                self.mo_frr.parent = self
                                self.neighbor_policies = MplsLdp.Global_.Mldp.Vrfs.Vrf.Afs.Af.NeighborPolicies()
                                self.neighbor_policies.parent = self
                                self.recursive_forwarding = MplsLdp.Global_.Mldp.Vrfs.Vrf.Afs.Af.RecursiveForwarding()
                                self.recursive_forwarding.parent = self


                            class RecursiveForwarding(object):
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
                                    self.parent = None
                                    self.enable = None
                                    self.policy = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-mpls-ldp-cfg:recursive-forwarding'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.enable is not None:
                                        return True

                                    if self.policy is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_ldp_cfg as meta
                                    return meta._meta_table['MplsLdp.Global_.Mldp.Vrfs.Vrf.Afs.Af.RecursiveForwarding']['meta_info']


                            class MldpRecursiveFec(object):
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
                                    self.parent = None
                                    self.enable = None
                                    self.policy = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-mpls-ldp-cfg:mldp-recursive-fec'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.enable is not None:
                                        return True

                                    if self.policy is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_ldp_cfg as meta
                                    return meta._meta_table['MplsLdp.Global_.Mldp.Vrfs.Vrf.Afs.Af.MldpRecursiveFec']['meta_info']


                            class NeighborPolicies(object):
                                """
                                MLDP neighbor policies
                                
                                .. attribute:: neighbor_policy
                                
                                	Route Policy
                                	**type**\: list of    :py:class:`NeighborPolicy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.Global_.Mldp.Vrfs.Vrf.Afs.Af.NeighborPolicies.NeighborPolicy>`
                                
                                

                                """

                                _prefix = 'mpls-ldp-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.neighbor_policy = YList()
                                    self.neighbor_policy.parent = self
                                    self.neighbor_policy.name = 'neighbor_policy'


                                class NeighborPolicy(object):
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
                                    	**type**\:   :py:class:`MldpPolicyModeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MldpPolicyModeEnum>`
                                    
                                    .. attribute:: route_policy
                                    
                                    	Route policy name
                                    	**type**\:  str
                                    
                                    	**length:** 1..64
                                    
                                    	**mandatory**\: True
                                    
                                    

                                    """

                                    _prefix = 'mpls-ldp-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.root_address = None
                                        self.policy_mode = None
                                        self.route_policy = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')
                                        if self.root_address is None:
                                            raise YPYModelError('Key property root_address is None')
                                        if self.policy_mode is None:
                                            raise YPYModelError('Key property policy_mode is None')

                                        return self.parent._common_path +'/Cisco-IOS-XR-mpls-ldp-cfg:neighbor-policy[Cisco-IOS-XR-mpls-ldp-cfg:root-address = ' + str(self.root_address) + '][Cisco-IOS-XR-mpls-ldp-cfg:policy-mode = ' + str(self.policy_mode) + ']'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if self.root_address is not None:
                                            return True

                                        if self.policy_mode is not None:
                                            return True

                                        if self.route_policy is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_ldp_cfg as meta
                                        return meta._meta_table['MplsLdp.Global_.Mldp.Vrfs.Vrf.Afs.Af.NeighborPolicies.NeighborPolicy']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-mpls-ldp-cfg:neighbor-policies'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.neighbor_policy is not None:
                                        for child_ref in self.neighbor_policy:
                                            if child_ref._has_data():
                                                return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_ldp_cfg as meta
                                    return meta._meta_table['MplsLdp.Global_.Mldp.Vrfs.Vrf.Afs.Af.NeighborPolicies']['meta_info']


                            class MoFrr(object):
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
                                    self.parent = None
                                    self.enable = None
                                    self.policy = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-mpls-ldp-cfg:mo-frr'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.enable is not None:
                                        return True

                                    if self.policy is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_ldp_cfg as meta
                                    return meta._meta_table['MplsLdp.Global_.Mldp.Vrfs.Vrf.Afs.Af.MoFrr']['meta_info']


                            class MakeBeforeBreak(object):
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
                                    self.parent = None
                                    self.policy = None
                                    self.signaling = MplsLdp.Global_.Mldp.Vrfs.Vrf.Afs.Af.MakeBeforeBreak.Signaling()
                                    self.signaling.parent = self


                                class Signaling(object):
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
                                        self.parent = None
                                        self.delete_delay = None
                                        self.forward_delay = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-mpls-ldp-cfg:signaling'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if self.delete_delay is not None:
                                            return True

                                        if self.forward_delay is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_ldp_cfg as meta
                                        return meta._meta_table['MplsLdp.Global_.Mldp.Vrfs.Vrf.Afs.Af.MakeBeforeBreak.Signaling']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-mpls-ldp-cfg:make-before-break'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.policy is not None:
                                        return True

                                    if self.signaling is not None and self.signaling._has_data():
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_ldp_cfg as meta
                                    return meta._meta_table['MplsLdp.Global_.Mldp.Vrfs.Vrf.Afs.Af.MakeBeforeBreak']['meta_info']


                            class Csc(object):
                                """
                                MPLS mLDP CSC
                                
                                .. attribute:: enable
                                
                                	Enable MPLS mLDP CSC
                                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                                
                                

                                """

                                _prefix = 'mpls-ldp-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.enable = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-mpls-ldp-cfg:csc'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.enable is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_ldp_cfg as meta
                                    return meta._meta_table['MplsLdp.Global_.Mldp.Vrfs.Vrf.Afs.Af.Csc']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                if self.af_name is None:
                                    raise YPYModelError('Key property af_name is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-mpls-ldp-cfg:af[Cisco-IOS-XR-mpls-ldp-cfg:af-name = ' + str(self.af_name) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.af_name is not None:
                                    return True

                                if self.csc is not None and self.csc._has_data():
                                    return True

                                if self.enable is not None:
                                    return True

                                if self.make_before_break is not None and self.make_before_break._has_data():
                                    return True

                                if self.mldp_recursive_fec is not None and self.mldp_recursive_fec._has_data():
                                    return True

                                if self.mldp_rib_unicast_always is not None:
                                    return True

                                if self.mo_frr is not None and self.mo_frr._has_data():
                                    return True

                                if self.neighbor_policies is not None and self.neighbor_policies._has_data():
                                    return True

                                if self.recursive_forwarding is not None and self.recursive_forwarding._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_ldp_cfg as meta
                                return meta._meta_table['MplsLdp.Global_.Mldp.Vrfs.Vrf.Afs.Af']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-mpls-ldp-cfg:afs'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.af is not None:
                                for child_ref in self.af:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_ldp_cfg as meta
                            return meta._meta_table['MplsLdp.Global_.Mldp.Vrfs.Vrf.Afs']['meta_info']

                    @property
                    def _common_path(self):
                        if self.vrf_name is None:
                            raise YPYModelError('Key property vrf_name is None')

                        return '/Cisco-IOS-XR-mpls-ldp-cfg:mpls-ldp/Cisco-IOS-XR-mpls-ldp-cfg:global/Cisco-IOS-XR-mpls-ldp-cfg:mldp/Cisco-IOS-XR-mpls-ldp-cfg:vrfs/Cisco-IOS-XR-mpls-ldp-cfg:vrf[Cisco-IOS-XR-mpls-ldp-cfg:vrf-name = ' + str(self.vrf_name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.vrf_name is not None:
                            return True

                        if self.afs is not None and self.afs._has_data():
                            return True

                        if self.enable is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_ldp_cfg as meta
                        return meta._meta_table['MplsLdp.Global_.Mldp.Vrfs.Vrf']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-mpls-ldp-cfg:mpls-ldp/Cisco-IOS-XR-mpls-ldp-cfg:global/Cisco-IOS-XR-mpls-ldp-cfg:mldp/Cisco-IOS-XR-mpls-ldp-cfg:vrfs'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.vrf is not None:
                        for child_ref in self.vrf:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_ldp_cfg as meta
                    return meta._meta_table['MplsLdp.Global_.Mldp.Vrfs']['meta_info']


            class DefaultVrf(object):
                """
                Default VRF attribute configuration for mLDP
                
                .. attribute:: afs
                
                	Address Family specific operational data
                	**type**\:   :py:class:`Afs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.Global_.Mldp.DefaultVrf.Afs>`
                
                

                """

                _prefix = 'mpls-ldp-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.afs = MplsLdp.Global_.Mldp.DefaultVrf.Afs()
                    self.afs.parent = self


                class Afs(object):
                    """
                    Address Family specific operational data
                    
                    .. attribute:: af
                    
                    	Operational data for given Address Family
                    	**type**\: list of    :py:class:`Af <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.Global_.Mldp.DefaultVrf.Afs.Af>`
                    
                    

                    """

                    _prefix = 'mpls-ldp-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.af = YList()
                        self.af.parent = self
                        self.af.name = 'af'


                    class Af(object):
                        """
                        Operational data for given Address Family
                        
                        .. attribute:: af_name  <key>
                        
                        	Address Family name
                        	**type**\:   :py:class:`MplsLdpafNameEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdpafNameEnum>`
                        
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
                            self.parent = None
                            self.af_name = None
                            self.csc = MplsLdp.Global_.Mldp.DefaultVrf.Afs.Af.Csc()
                            self.csc.parent = self
                            self.enable = None
                            self.make_before_break = MplsLdp.Global_.Mldp.DefaultVrf.Afs.Af.MakeBeforeBreak()
                            self.make_before_break.parent = self
                            self.mldp_recursive_fec = MplsLdp.Global_.Mldp.DefaultVrf.Afs.Af.MldpRecursiveFec()
                            self.mldp_recursive_fec.parent = self
                            self.mldp_rib_unicast_always = None
                            self.mo_frr = MplsLdp.Global_.Mldp.DefaultVrf.Afs.Af.MoFrr()
                            self.mo_frr.parent = self
                            self.neighbor_policies = MplsLdp.Global_.Mldp.DefaultVrf.Afs.Af.NeighborPolicies()
                            self.neighbor_policies.parent = self
                            self.recursive_forwarding = MplsLdp.Global_.Mldp.DefaultVrf.Afs.Af.RecursiveForwarding()
                            self.recursive_forwarding.parent = self


                        class RecursiveForwarding(object):
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
                                self.parent = None
                                self.enable = None
                                self.policy = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-mpls-ldp-cfg:recursive-forwarding'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.enable is not None:
                                    return True

                                if self.policy is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_ldp_cfg as meta
                                return meta._meta_table['MplsLdp.Global_.Mldp.DefaultVrf.Afs.Af.RecursiveForwarding']['meta_info']


                        class MldpRecursiveFec(object):
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
                                self.parent = None
                                self.enable = None
                                self.policy = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-mpls-ldp-cfg:mldp-recursive-fec'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.enable is not None:
                                    return True

                                if self.policy is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_ldp_cfg as meta
                                return meta._meta_table['MplsLdp.Global_.Mldp.DefaultVrf.Afs.Af.MldpRecursiveFec']['meta_info']


                        class NeighborPolicies(object):
                            """
                            MLDP neighbor policies
                            
                            .. attribute:: neighbor_policy
                            
                            	Route Policy
                            	**type**\: list of    :py:class:`NeighborPolicy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.Global_.Mldp.DefaultVrf.Afs.Af.NeighborPolicies.NeighborPolicy>`
                            
                            

                            """

                            _prefix = 'mpls-ldp-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.neighbor_policy = YList()
                                self.neighbor_policy.parent = self
                                self.neighbor_policy.name = 'neighbor_policy'


                            class NeighborPolicy(object):
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
                                	**type**\:   :py:class:`MldpPolicyModeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MldpPolicyModeEnum>`
                                
                                .. attribute:: route_policy
                                
                                	Route policy name
                                	**type**\:  str
                                
                                	**length:** 1..64
                                
                                	**mandatory**\: True
                                
                                

                                """

                                _prefix = 'mpls-ldp-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.root_address = None
                                    self.policy_mode = None
                                    self.route_policy = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')
                                    if self.root_address is None:
                                        raise YPYModelError('Key property root_address is None')
                                    if self.policy_mode is None:
                                        raise YPYModelError('Key property policy_mode is None')

                                    return self.parent._common_path +'/Cisco-IOS-XR-mpls-ldp-cfg:neighbor-policy[Cisco-IOS-XR-mpls-ldp-cfg:root-address = ' + str(self.root_address) + '][Cisco-IOS-XR-mpls-ldp-cfg:policy-mode = ' + str(self.policy_mode) + ']'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.root_address is not None:
                                        return True

                                    if self.policy_mode is not None:
                                        return True

                                    if self.route_policy is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_ldp_cfg as meta
                                    return meta._meta_table['MplsLdp.Global_.Mldp.DefaultVrf.Afs.Af.NeighborPolicies.NeighborPolicy']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-mpls-ldp-cfg:neighbor-policies'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.neighbor_policy is not None:
                                    for child_ref in self.neighbor_policy:
                                        if child_ref._has_data():
                                            return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_ldp_cfg as meta
                                return meta._meta_table['MplsLdp.Global_.Mldp.DefaultVrf.Afs.Af.NeighborPolicies']['meta_info']


                        class MoFrr(object):
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
                                self.parent = None
                                self.enable = None
                                self.policy = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-mpls-ldp-cfg:mo-frr'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.enable is not None:
                                    return True

                                if self.policy is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_ldp_cfg as meta
                                return meta._meta_table['MplsLdp.Global_.Mldp.DefaultVrf.Afs.Af.MoFrr']['meta_info']


                        class MakeBeforeBreak(object):
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
                                self.parent = None
                                self.policy = None
                                self.signaling = MplsLdp.Global_.Mldp.DefaultVrf.Afs.Af.MakeBeforeBreak.Signaling()
                                self.signaling.parent = self


                            class Signaling(object):
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
                                    self.parent = None
                                    self.delete_delay = None
                                    self.forward_delay = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-mpls-ldp-cfg:signaling'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.delete_delay is not None:
                                        return True

                                    if self.forward_delay is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_ldp_cfg as meta
                                    return meta._meta_table['MplsLdp.Global_.Mldp.DefaultVrf.Afs.Af.MakeBeforeBreak.Signaling']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-mpls-ldp-cfg:make-before-break'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.policy is not None:
                                    return True

                                if self.signaling is not None and self.signaling._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_ldp_cfg as meta
                                return meta._meta_table['MplsLdp.Global_.Mldp.DefaultVrf.Afs.Af.MakeBeforeBreak']['meta_info']


                        class Csc(object):
                            """
                            MPLS mLDP CSC
                            
                            .. attribute:: enable
                            
                            	Enable MPLS mLDP CSC
                            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                            
                            

                            """

                            _prefix = 'mpls-ldp-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.enable = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-mpls-ldp-cfg:csc'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.enable is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_ldp_cfg as meta
                                return meta._meta_table['MplsLdp.Global_.Mldp.DefaultVrf.Afs.Af.Csc']['meta_info']

                        @property
                        def _common_path(self):
                            if self.af_name is None:
                                raise YPYModelError('Key property af_name is None')

                            return '/Cisco-IOS-XR-mpls-ldp-cfg:mpls-ldp/Cisco-IOS-XR-mpls-ldp-cfg:global/Cisco-IOS-XR-mpls-ldp-cfg:mldp/Cisco-IOS-XR-mpls-ldp-cfg:default-vrf/Cisco-IOS-XR-mpls-ldp-cfg:afs/Cisco-IOS-XR-mpls-ldp-cfg:af[Cisco-IOS-XR-mpls-ldp-cfg:af-name = ' + str(self.af_name) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.af_name is not None:
                                return True

                            if self.csc is not None and self.csc._has_data():
                                return True

                            if self.enable is not None:
                                return True

                            if self.make_before_break is not None and self.make_before_break._has_data():
                                return True

                            if self.mldp_recursive_fec is not None and self.mldp_recursive_fec._has_data():
                                return True

                            if self.mldp_rib_unicast_always is not None:
                                return True

                            if self.mo_frr is not None and self.mo_frr._has_data():
                                return True

                            if self.neighbor_policies is not None and self.neighbor_policies._has_data():
                                return True

                            if self.recursive_forwarding is not None and self.recursive_forwarding._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_ldp_cfg as meta
                            return meta._meta_table['MplsLdp.Global_.Mldp.DefaultVrf.Afs.Af']['meta_info']

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-mpls-ldp-cfg:mpls-ldp/Cisco-IOS-XR-mpls-ldp-cfg:global/Cisco-IOS-XR-mpls-ldp-cfg:mldp/Cisco-IOS-XR-mpls-ldp-cfg:default-vrf/Cisco-IOS-XR-mpls-ldp-cfg:afs'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.af is not None:
                            for child_ref in self.af:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_ldp_cfg as meta
                        return meta._meta_table['MplsLdp.Global_.Mldp.DefaultVrf.Afs']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-mpls-ldp-cfg:mpls-ldp/Cisco-IOS-XR-mpls-ldp-cfg:global/Cisco-IOS-XR-mpls-ldp-cfg:mldp/Cisco-IOS-XR-mpls-ldp-cfg:default-vrf'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.afs is not None and self.afs._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_ldp_cfg as meta
                    return meta._meta_table['MplsLdp.Global_.Mldp.DefaultVrf']['meta_info']


            class MldpGlobal(object):
                """
                Global configuration for mLDP
                
                .. attribute:: logging
                
                	MPLS mLDP logging
                	**type**\:   :py:class:`Logging <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg.MplsLdp.Global_.Mldp.MldpGlobal.Logging>`
                
                

                """

                _prefix = 'mpls-ldp-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.logging = MplsLdp.Global_.Mldp.MldpGlobal.Logging()
                    self.logging.parent = self


                class Logging(object):
                    """
                    MPLS mLDP logging
                    
                    .. attribute:: notifications
                    
                    	MPLS mLDP logging notifications
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    

                    """

                    _prefix = 'mpls-ldp-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.notifications = None

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-mpls-ldp-cfg:mpls-ldp/Cisco-IOS-XR-mpls-ldp-cfg:global/Cisco-IOS-XR-mpls-ldp-cfg:mldp/Cisco-IOS-XR-mpls-ldp-cfg:mldp-global/Cisco-IOS-XR-mpls-ldp-cfg:logging'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.notifications is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_ldp_cfg as meta
                        return meta._meta_table['MplsLdp.Global_.Mldp.MldpGlobal.Logging']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-mpls-ldp-cfg:mpls-ldp/Cisco-IOS-XR-mpls-ldp-cfg:global/Cisco-IOS-XR-mpls-ldp-cfg:mldp/Cisco-IOS-XR-mpls-ldp-cfg:mldp-global'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.logging is not None and self.logging._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_ldp_cfg as meta
                    return meta._meta_table['MplsLdp.Global_.Mldp.MldpGlobal']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-mpls-ldp-cfg:mpls-ldp/Cisco-IOS-XR-mpls-ldp-cfg:global/Cisco-IOS-XR-mpls-ldp-cfg:mldp'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.default_vrf is not None and self.default_vrf._has_data():
                    return True

                if self.enable is not None:
                    return True

                if self.mldp_global is not None and self.mldp_global._has_data():
                    return True

                if self.vrfs is not None and self.vrfs._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_ldp_cfg as meta
                return meta._meta_table['MplsLdp.Global_.Mldp']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-mpls-ldp-cfg:mpls-ldp/Cisco-IOS-XR-mpls-ldp-cfg:global'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.disable_implicit_ipv4 is not None:
                return True

            if self.discovery is not None and self.discovery._has_data():
                return True

            if self.enable_logging is not None and self.enable_logging._has_data():
                return True

            if self.entropy_label is not None and self.entropy_label._has_data():
                return True

            if self.graceful_restart is not None and self.graceful_restart._has_data():
                return True

            if self.igp is not None and self.igp._has_data():
                return True

            if self.ltrace_buf_multiplier is not None:
                return True

            if self.mldp is not None and self.mldp._has_data():
                return True

            if self.nsr is not None and self.nsr._has_data():
                return True

            if self.session is not None and self.session._has_data():
                return True

            if self.signalling is not None and self.signalling._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_ldp_cfg as meta
            return meta._meta_table['MplsLdp.Global_']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-mpls-ldp-cfg:mpls-ldp'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.default_vrf is not None and self.default_vrf._has_data():
            return True

        if self.enable is not None:
            return True

        if self.global_ is not None and self.global_._has_data():
            return True

        if self.vrfs is not None and self.vrfs._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_ldp_cfg as meta
        return meta._meta_table['MplsLdp']['meta_info']


