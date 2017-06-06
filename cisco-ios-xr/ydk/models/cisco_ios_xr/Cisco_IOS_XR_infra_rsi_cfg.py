""" Cisco_IOS_XR_infra_rsi_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR infra\-rsi package configuration.

This module contains definitions
for the following management objects\:
  vrfs\: VRF configuration
  global\-af\: global af
  srlg\: srlg
  vrf\-groups\: vrf groups
  selective\-vrf\-download\: selective vrf download

This YANG module augments the
  Cisco\-IOS\-XR\-ifmgr\-cfg,
  Cisco\-IOS\-XR\-snmp\-agent\-cfg
modules with configuration data.

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class SrlgPriorityEnum(Enum):
    """
    SrlgPriorityEnum

    Srlg priority

    .. data:: critical = 0

    	Critical

    .. data:: high = 1

    	High

    .. data:: default = 2

    	Default

    .. data:: low = 3

    	Low

    .. data:: very_low = 4

    	Very low

    """

    critical = 0

    high = 1

    default = 2

    low = 3

    very_low = 4


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_rsi_cfg as meta
        return meta._meta_table['SrlgPriorityEnum']


class VrfAddressFamilyEnum(Enum):
    """
    VrfAddressFamilyEnum

    Vrf address family

    .. data:: ipv4 = 1

    	IPv4

    .. data:: ipv6 = 2

    	IPv6

    """

    ipv4 = 1

    ipv6 = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_rsi_cfg as meta
        return meta._meta_table['VrfAddressFamilyEnum']


class VrfSubAddressFamilyEnum(Enum):
    """
    VrfSubAddressFamilyEnum

    Vrf sub address family

    .. data:: unicast = 1

    	Unicast

    .. data:: multicast = 2

    	Multicast

    .. data:: flow_spec = 133

    	Flow spec

    """

    unicast = 1

    multicast = 2

    flow_spec = 133


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_rsi_cfg as meta
        return meta._meta_table['VrfSubAddressFamilyEnum']



class Vrfs(object):
    """
    VRF configuration
    
    .. attribute:: vrf
    
    	VRF configuration
    	**type**\: list of    :py:class:`Vrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.Vrfs.Vrf>`
    
    

    """

    _prefix = 'infra-rsi-cfg'
    _revision = '2016-12-19'

    def __init__(self):
        self.vrf = YList()
        self.vrf.parent = self
        self.vrf.name = 'vrf'


    class Vrf(object):
        """
        VRF configuration
        
        .. attribute:: vrf_name  <key>
        
        	VRF name
        	**type**\:  str
        
        	**length:** 1..32
        
        .. attribute:: afs
        
        	VRF address family configuration
        	**type**\:   :py:class:`Afs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.Vrfs.Vrf.Afs>`
        
        .. attribute:: create
        
        	VRF global configuration
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: description
        
        	A textual description of the VRF
        	**type**\:  str
        
        	**length:** 1..244
        
        .. attribute:: fallback_vrf
        
        	Fallback VRF
        	**type**\:  str
        
        	**length:** 1..32
        
        .. attribute:: mode_big
        
        	Configuration enable of big VRF
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: multicast_host
        
        	Multicast host stack configuration
        	**type**\:   :py:class:`MulticastHost <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.Vrfs.Vrf.MulticastHost>`
        
        .. attribute:: remote_route_filter_disable
        
        	For disabling remote route filtering for this VRF on core\-facing card
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: vpn_id
        
        	VPN\-ID for the VRF
        	**type**\:   :py:class:`VpnId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.Vrfs.Vrf.VpnId>`
        
        	**presence node**\: True
        
        

        """

        _prefix = 'infra-rsi-cfg'
        _revision = '2016-12-19'

        def __init__(self):
            self.parent = None
            self.vrf_name = None
            self.afs = Vrfs.Vrf.Afs()
            self.afs.parent = self
            self.create = None
            self.description = None
            self.fallback_vrf = None
            self.mode_big = None
            self.multicast_host = Vrfs.Vrf.MulticastHost()
            self.multicast_host.parent = self
            self.remote_route_filter_disable = None
            self.vpn_id = None


        class VpnId(object):
            """
            VPN\-ID for the VRF
            
            .. attribute:: vpn_index
            
            	Index of VPNID Index
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**mandatory**\: True
            
            .. attribute:: vpn_oui
            
            	OUI of VPNID OUI
            	**type**\:  int
            
            	**range:** 0..16777215
            
            	**mandatory**\: True
            
            .. attribute:: _is_presence
            
            	Is present if this instance represents presence container else not
            	**type**\: bool
            
            

            This class is a :ref:`presence class<presence-class>`

            """

            _prefix = 'infra-rsi-cfg'
            _revision = '2016-12-19'

            def __init__(self):
                self.parent = None
                self._is_presence = True
                self.vpn_index = None
                self.vpn_oui = None

            @property
            def _common_path(self):
                if self.parent is None:
                    raise YPYModelError('parent is not set . Cannot derive path.')

                return self.parent._common_path +'/Cisco-IOS-XR-infra-rsi-cfg:vpn-id'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self._is_presence:
                    return True
                if self.vpn_index is not None:
                    return True

                if self.vpn_oui is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_rsi_cfg as meta
                return meta._meta_table['Vrfs.Vrf.VpnId']['meta_info']


        class Afs(object):
            """
            VRF address family configuration
            
            .. attribute:: af
            
            	VRF address family configuration
            	**type**\: list of    :py:class:`Af <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.Vrfs.Vrf.Afs.Af>`
            
            

            """

            _prefix = 'infra-rsi-cfg'
            _revision = '2016-12-19'

            def __init__(self):
                self.parent = None
                self.af = YList()
                self.af.parent = self
                self.af.name = 'af'


            class Af(object):
                """
                VRF address family configuration
                
                .. attribute:: af_name  <key>
                
                	Address family
                	**type**\:   :py:class:`VrfAddressFamilyEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.VrfAddressFamilyEnum>`
                
                .. attribute:: saf_name  <key>
                
                	Sub\-Address family
                	**type**\:   :py:class:`VrfSubAddressFamilyEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.VrfSubAddressFamilyEnum>`
                
                .. attribute:: topology_name  <key>
                
                	Topology name
                	**type**\:  str
                
                	**length:** 1..244
                
                .. attribute:: bgp
                
                	BGP AF VRF config
                	**type**\:   :py:class:`Bgp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.Vrfs.Vrf.Afs.Af.Bgp>`
                
                .. attribute:: create
                
                	VRF configuration for a particular address family
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: maximum_prefix
                
                	Set maximum prefix limits
                	**type**\:   :py:class:`MaximumPrefix <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.Vrfs.Vrf.Afs.Af.MaximumPrefix>`
                
                	**presence node**\: True
                
                

                """

                _prefix = 'infra-rsi-cfg'
                _revision = '2016-12-19'

                def __init__(self):
                    self.parent = None
                    self.af_name = None
                    self.saf_name = None
                    self.topology_name = None
                    self.bgp = Vrfs.Vrf.Afs.Af.Bgp()
                    self.bgp.parent = self
                    self.create = None
                    self.maximum_prefix = None


                class MaximumPrefix(object):
                    """
                    Set maximum prefix limits
                    
                    .. attribute:: mid_threshold
                    
                    	Mid\-threshold (% of maximum)
                    	**type**\:  int
                    
                    	**range:** 1..100
                    
                    .. attribute:: prefix_limit
                    
                    	Set table's maximum prefix limit
                    	**type**\:  int
                    
                    	**range:** 32..5000000
                    
                    	**mandatory**\: True
                    
                    .. attribute:: _is_presence
                    
                    	Is present if this instance represents presence container else not
                    	**type**\: bool
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'ip-rib-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self._is_presence = True
                        self.mid_threshold = None
                        self.prefix_limit = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ip-rib-cfg:maximum-prefix'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self._is_presence:
                            return True
                        if self.mid_threshold is not None:
                            return True

                        if self.prefix_limit is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_rsi_cfg as meta
                        return meta._meta_table['Vrfs.Vrf.Afs.Af.MaximumPrefix']['meta_info']


                class Bgp(object):
                    """
                    BGP AF VRF config
                    
                    .. attribute:: export_route_policy
                    
                    	Route policy for export filtering
                    	**type**\:  str
                    
                    .. attribute:: export_route_targets
                    
                    	Export Route targets
                    	**type**\:   :py:class:`ExportRouteTargets <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.Vrfs.Vrf.Afs.Af.Bgp.ExportRouteTargets>`
                    
                    .. attribute:: export_vrf_options
                    
                    	Export VRF options
                    	**type**\:   :py:class:`ExportVrfOptions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.Vrfs.Vrf.Afs.Af.Bgp.ExportVrfOptions>`
                    
                    .. attribute:: global_to_vrf_import_route_policy
                    
                    	Route policy for global to vrf import filtering
                    	**type**\:   :py:class:`GlobalToVrfImportRoutePolicy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.Vrfs.Vrf.Afs.Af.Bgp.GlobalToVrfImportRoutePolicy>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: import_route_policy
                    
                    	Route policy for import filtering
                    	**type**\:  str
                    
                    .. attribute:: import_route_targets
                    
                    	Import Route targets
                    	**type**\:   :py:class:`ImportRouteTargets <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.Vrfs.Vrf.Afs.Af.Bgp.ImportRouteTargets>`
                    
                    .. attribute:: import_vrf_options
                    
                    	TRUE Enable advertising imported paths to PEsFALSE Disable advertising imported paths to PEs
                    	**type**\:  bool
                    
                    .. attribute:: vrf_to_global_export_route_policy
                    
                    	Route policy for vrf to global export filtering
                    	**type**\:   :py:class:`VrfToGlobalExportRoutePolicy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.Vrfs.Vrf.Afs.Af.Bgp.VrfToGlobalExportRoutePolicy>`
                    
                    	**presence node**\: True
                    
                    

                    """

                    _prefix = 'ipv4-bgp-cfg'
                    _revision = '2015-08-27'

                    def __init__(self):
                        self.parent = None
                        self.export_route_policy = None
                        self.export_route_targets = Vrfs.Vrf.Afs.Af.Bgp.ExportRouteTargets()
                        self.export_route_targets.parent = self
                        self.export_vrf_options = Vrfs.Vrf.Afs.Af.Bgp.ExportVrfOptions()
                        self.export_vrf_options.parent = self
                        self.global_to_vrf_import_route_policy = None
                        self.import_route_policy = None
                        self.import_route_targets = Vrfs.Vrf.Afs.Af.Bgp.ImportRouteTargets()
                        self.import_route_targets.parent = self
                        self.import_vrf_options = None
                        self.vrf_to_global_export_route_policy = None


                    class ImportRouteTargets(object):
                        """
                        Import Route targets
                        
                        .. attribute:: route_targets
                        
                        	Route target table
                        	**type**\:   :py:class:`RouteTargets <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.Vrfs.Vrf.Afs.Af.Bgp.ImportRouteTargets.RouteTargets>`
                        
                        

                        """

                        _prefix = 'ipv4-bgp-cfg'
                        _revision = '2015-08-27'

                        def __init__(self):
                            self.parent = None
                            self.route_targets = Vrfs.Vrf.Afs.Af.Bgp.ImportRouteTargets.RouteTargets()
                            self.route_targets.parent = self


                        class RouteTargets(object):
                            """
                            Route target table
                            
                            .. attribute:: route_target
                            
                            	Route target
                            	**type**\: list of    :py:class:`RouteTarget <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.Vrfs.Vrf.Afs.Af.Bgp.ImportRouteTargets.RouteTargets.RouteTarget>`
                            
                            

                            """

                            _prefix = 'ipv4-bgp-cfg'
                            _revision = '2015-08-27'

                            def __init__(self):
                                self.parent = None
                                self.route_target = YList()
                                self.route_target.parent = self
                                self.route_target.name = 'route_target'


                            class RouteTarget(object):
                                """
                                Route target
                                
                                .. attribute:: type  <key>
                                
                                	Type of RT
                                	**type**\:   :py:class:`BgpVrfRouteTargetEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg.BgpVrfRouteTargetEnum>`
                                
                                .. attribute:: as_or_four_byte_as
                                
                                	as or four byte as
                                	**type**\: list of    :py:class:`AsOrFourByteAs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.Vrfs.Vrf.Afs.Af.Bgp.ImportRouteTargets.RouteTargets.RouteTarget.AsOrFourByteAs>`
                                
                                .. attribute:: ipv4_address
                                
                                	ipv4 address
                                	**type**\: list of    :py:class:`Ipv4Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.Vrfs.Vrf.Afs.Af.Bgp.ImportRouteTargets.RouteTargets.RouteTarget.Ipv4Address>`
                                
                                

                                """

                                _prefix = 'ipv4-bgp-cfg'
                                _revision = '2015-08-27'

                                def __init__(self):
                                    self.parent = None
                                    self.type = None
                                    self.as_or_four_byte_as = YList()
                                    self.as_or_four_byte_as.parent = self
                                    self.as_or_four_byte_as.name = 'as_or_four_byte_as'
                                    self.ipv4_address = YList()
                                    self.ipv4_address.parent = self
                                    self.ipv4_address.name = 'ipv4_address'


                                class AsOrFourByteAs(object):
                                    """
                                    as or four byte as
                                    
                                    .. attribute:: as_xx  <key>
                                    
                                    	AS number
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: as_  <key>
                                    
                                    	AS number
                                    	**type**\:  int
                                    
                                    	**range:** 1..4294967295
                                    
                                    .. attribute:: as_index  <key>
                                    
                                    	AS number Index
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: stitching_rt  <key>
                                    
                                    	Stitching RT
                                    	**type**\:  int
                                    
                                    	**range:** 0..1
                                    
                                    

                                    """

                                    _prefix = 'ipv4-bgp-cfg'
                                    _revision = '2015-08-27'

                                    def __init__(self):
                                        self.parent = None
                                        self.as_xx = None
                                        self.as_ = None
                                        self.as_index = None
                                        self.stitching_rt = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')
                                        if self.as_xx is None:
                                            raise YPYModelError('Key property as_xx is None')
                                        if self.as_ is None:
                                            raise YPYModelError('Key property as_ is None')
                                        if self.as_index is None:
                                            raise YPYModelError('Key property as_index is None')
                                        if self.stitching_rt is None:
                                            raise YPYModelError('Key property stitching_rt is None')

                                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-bgp-cfg:as-or-four-byte-as[Cisco-IOS-XR-ipv4-bgp-cfg:as-xx = ' + str(self.as_xx) + '][Cisco-IOS-XR-ipv4-bgp-cfg:as = ' + str(self.as_) + '][Cisco-IOS-XR-ipv4-bgp-cfg:as-index = ' + str(self.as_index) + '][Cisco-IOS-XR-ipv4-bgp-cfg:stitching-rt = ' + str(self.stitching_rt) + ']'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if self.as_xx is not None:
                                            return True

                                        if self.as_ is not None:
                                            return True

                                        if self.as_index is not None:
                                            return True

                                        if self.stitching_rt is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_rsi_cfg as meta
                                        return meta._meta_table['Vrfs.Vrf.Afs.Af.Bgp.ImportRouteTargets.RouteTargets.RouteTarget.AsOrFourByteAs']['meta_info']


                                class Ipv4Address(object):
                                    """
                                    ipv4 address
                                    
                                    .. attribute:: address  <key>
                                    
                                    	IP address
                                    	**type**\:  str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    .. attribute:: address_index  <key>
                                    
                                    	IP address Index
                                    	**type**\:  int
                                    
                                    	**range:** 0..65535
                                    
                                    .. attribute:: stitching_rt  <key>
                                    
                                    	Stitching RT
                                    	**type**\:  int
                                    
                                    	**range:** 0..1
                                    
                                    

                                    """

                                    _prefix = 'ipv4-bgp-cfg'
                                    _revision = '2015-08-27'

                                    def __init__(self):
                                        self.parent = None
                                        self.address = None
                                        self.address_index = None
                                        self.stitching_rt = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')
                                        if self.address is None:
                                            raise YPYModelError('Key property address is None')
                                        if self.address_index is None:
                                            raise YPYModelError('Key property address_index is None')
                                        if self.stitching_rt is None:
                                            raise YPYModelError('Key property stitching_rt is None')

                                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-bgp-cfg:ipv4-address[Cisco-IOS-XR-ipv4-bgp-cfg:address = ' + str(self.address) + '][Cisco-IOS-XR-ipv4-bgp-cfg:address-index = ' + str(self.address_index) + '][Cisco-IOS-XR-ipv4-bgp-cfg:stitching-rt = ' + str(self.stitching_rt) + ']'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if self.address is not None:
                                            return True

                                        if self.address_index is not None:
                                            return True

                                        if self.stitching_rt is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_rsi_cfg as meta
                                        return meta._meta_table['Vrfs.Vrf.Afs.Af.Bgp.ImportRouteTargets.RouteTargets.RouteTarget.Ipv4Address']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')
                                    if self.type is None:
                                        raise YPYModelError('Key property type is None')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-bgp-cfg:route-target[Cisco-IOS-XR-ipv4-bgp-cfg:type = ' + str(self.type) + ']'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.type is not None:
                                        return True

                                    if self.as_or_four_byte_as is not None:
                                        for child_ref in self.as_or_four_byte_as:
                                            if child_ref._has_data():
                                                return True

                                    if self.ipv4_address is not None:
                                        for child_ref in self.ipv4_address:
                                            if child_ref._has_data():
                                                return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_rsi_cfg as meta
                                    return meta._meta_table['Vrfs.Vrf.Afs.Af.Bgp.ImportRouteTargets.RouteTargets.RouteTarget']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ipv4-bgp-cfg:route-targets'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.route_target is not None:
                                    for child_ref in self.route_target:
                                        if child_ref._has_data():
                                            return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_rsi_cfg as meta
                                return meta._meta_table['Vrfs.Vrf.Afs.Af.Bgp.ImportRouteTargets.RouteTargets']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv4-bgp-cfg:import-route-targets'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.route_targets is not None and self.route_targets._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_rsi_cfg as meta
                            return meta._meta_table['Vrfs.Vrf.Afs.Af.Bgp.ImportRouteTargets']['meta_info']


                    class ExportRouteTargets(object):
                        """
                        Export Route targets
                        
                        .. attribute:: route_targets
                        
                        	Route target table
                        	**type**\:   :py:class:`RouteTargets <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.Vrfs.Vrf.Afs.Af.Bgp.ExportRouteTargets.RouteTargets>`
                        
                        

                        """

                        _prefix = 'ipv4-bgp-cfg'
                        _revision = '2015-08-27'

                        def __init__(self):
                            self.parent = None
                            self.route_targets = Vrfs.Vrf.Afs.Af.Bgp.ExportRouteTargets.RouteTargets()
                            self.route_targets.parent = self


                        class RouteTargets(object):
                            """
                            Route target table
                            
                            .. attribute:: route_target
                            
                            	Route target
                            	**type**\: list of    :py:class:`RouteTarget <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.Vrfs.Vrf.Afs.Af.Bgp.ExportRouteTargets.RouteTargets.RouteTarget>`
                            
                            

                            """

                            _prefix = 'ipv4-bgp-cfg'
                            _revision = '2015-08-27'

                            def __init__(self):
                                self.parent = None
                                self.route_target = YList()
                                self.route_target.parent = self
                                self.route_target.name = 'route_target'


                            class RouteTarget(object):
                                """
                                Route target
                                
                                .. attribute:: type  <key>
                                
                                	Type of RT
                                	**type**\:   :py:class:`BgpVrfRouteTargetEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg.BgpVrfRouteTargetEnum>`
                                
                                .. attribute:: as_or_four_byte_as
                                
                                	as or four byte as
                                	**type**\: list of    :py:class:`AsOrFourByteAs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.Vrfs.Vrf.Afs.Af.Bgp.ExportRouteTargets.RouteTargets.RouteTarget.AsOrFourByteAs>`
                                
                                .. attribute:: ipv4_address
                                
                                	ipv4 address
                                	**type**\: list of    :py:class:`Ipv4Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.Vrfs.Vrf.Afs.Af.Bgp.ExportRouteTargets.RouteTargets.RouteTarget.Ipv4Address>`
                                
                                

                                """

                                _prefix = 'ipv4-bgp-cfg'
                                _revision = '2015-08-27'

                                def __init__(self):
                                    self.parent = None
                                    self.type = None
                                    self.as_or_four_byte_as = YList()
                                    self.as_or_four_byte_as.parent = self
                                    self.as_or_four_byte_as.name = 'as_or_four_byte_as'
                                    self.ipv4_address = YList()
                                    self.ipv4_address.parent = self
                                    self.ipv4_address.name = 'ipv4_address'


                                class AsOrFourByteAs(object):
                                    """
                                    as or four byte as
                                    
                                    .. attribute:: as_xx  <key>
                                    
                                    	AS number
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: as_  <key>
                                    
                                    	AS number
                                    	**type**\:  int
                                    
                                    	**range:** 1..4294967295
                                    
                                    .. attribute:: as_index  <key>
                                    
                                    	AS number Index
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: stitching_rt  <key>
                                    
                                    	Stitching RT
                                    	**type**\:  int
                                    
                                    	**range:** 0..1
                                    
                                    

                                    """

                                    _prefix = 'ipv4-bgp-cfg'
                                    _revision = '2015-08-27'

                                    def __init__(self):
                                        self.parent = None
                                        self.as_xx = None
                                        self.as_ = None
                                        self.as_index = None
                                        self.stitching_rt = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')
                                        if self.as_xx is None:
                                            raise YPYModelError('Key property as_xx is None')
                                        if self.as_ is None:
                                            raise YPYModelError('Key property as_ is None')
                                        if self.as_index is None:
                                            raise YPYModelError('Key property as_index is None')
                                        if self.stitching_rt is None:
                                            raise YPYModelError('Key property stitching_rt is None')

                                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-bgp-cfg:as-or-four-byte-as[Cisco-IOS-XR-ipv4-bgp-cfg:as-xx = ' + str(self.as_xx) + '][Cisco-IOS-XR-ipv4-bgp-cfg:as = ' + str(self.as_) + '][Cisco-IOS-XR-ipv4-bgp-cfg:as-index = ' + str(self.as_index) + '][Cisco-IOS-XR-ipv4-bgp-cfg:stitching-rt = ' + str(self.stitching_rt) + ']'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if self.as_xx is not None:
                                            return True

                                        if self.as_ is not None:
                                            return True

                                        if self.as_index is not None:
                                            return True

                                        if self.stitching_rt is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_rsi_cfg as meta
                                        return meta._meta_table['Vrfs.Vrf.Afs.Af.Bgp.ExportRouteTargets.RouteTargets.RouteTarget.AsOrFourByteAs']['meta_info']


                                class Ipv4Address(object):
                                    """
                                    ipv4 address
                                    
                                    .. attribute:: address  <key>
                                    
                                    	IP address
                                    	**type**\:  str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    .. attribute:: address_index  <key>
                                    
                                    	IP address Index
                                    	**type**\:  int
                                    
                                    	**range:** 0..65535
                                    
                                    .. attribute:: stitching_rt  <key>
                                    
                                    	Stitching RT
                                    	**type**\:  int
                                    
                                    	**range:** 0..1
                                    
                                    

                                    """

                                    _prefix = 'ipv4-bgp-cfg'
                                    _revision = '2015-08-27'

                                    def __init__(self):
                                        self.parent = None
                                        self.address = None
                                        self.address_index = None
                                        self.stitching_rt = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')
                                        if self.address is None:
                                            raise YPYModelError('Key property address is None')
                                        if self.address_index is None:
                                            raise YPYModelError('Key property address_index is None')
                                        if self.stitching_rt is None:
                                            raise YPYModelError('Key property stitching_rt is None')

                                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-bgp-cfg:ipv4-address[Cisco-IOS-XR-ipv4-bgp-cfg:address = ' + str(self.address) + '][Cisco-IOS-XR-ipv4-bgp-cfg:address-index = ' + str(self.address_index) + '][Cisco-IOS-XR-ipv4-bgp-cfg:stitching-rt = ' + str(self.stitching_rt) + ']'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if self.address is not None:
                                            return True

                                        if self.address_index is not None:
                                            return True

                                        if self.stitching_rt is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_rsi_cfg as meta
                                        return meta._meta_table['Vrfs.Vrf.Afs.Af.Bgp.ExportRouteTargets.RouteTargets.RouteTarget.Ipv4Address']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')
                                    if self.type is None:
                                        raise YPYModelError('Key property type is None')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-bgp-cfg:route-target[Cisco-IOS-XR-ipv4-bgp-cfg:type = ' + str(self.type) + ']'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.type is not None:
                                        return True

                                    if self.as_or_four_byte_as is not None:
                                        for child_ref in self.as_or_four_byte_as:
                                            if child_ref._has_data():
                                                return True

                                    if self.ipv4_address is not None:
                                        for child_ref in self.ipv4_address:
                                            if child_ref._has_data():
                                                return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_rsi_cfg as meta
                                    return meta._meta_table['Vrfs.Vrf.Afs.Af.Bgp.ExportRouteTargets.RouteTargets.RouteTarget']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ipv4-bgp-cfg:route-targets'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.route_target is not None:
                                    for child_ref in self.route_target:
                                        if child_ref._has_data():
                                            return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_rsi_cfg as meta
                                return meta._meta_table['Vrfs.Vrf.Afs.Af.Bgp.ExportRouteTargets.RouteTargets']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv4-bgp-cfg:export-route-targets'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.route_targets is not None and self.route_targets._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_rsi_cfg as meta
                            return meta._meta_table['Vrfs.Vrf.Afs.Af.Bgp.ExportRouteTargets']['meta_info']


                    class VrfToGlobalExportRoutePolicy(object):
                        """
                        Route policy for vrf to global export filtering
                        
                        .. attribute:: allow_imported_vpn
                        
                        	TRUE Enable imported VPN paths to be exported to Default VRF.FALSE Disable imported VPN paths to be exported to Default VRF
                        	**type**\:  bool
                        
                        .. attribute:: route_policy_name
                        
                        	Vrf to global export route policy
                        	**type**\:  str
                        
                        	**mandatory**\: True
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'ipv4-bgp-cfg'
                        _revision = '2015-08-27'

                        def __init__(self):
                            self.parent = None
                            self._is_presence = True
                            self.allow_imported_vpn = None
                            self.route_policy_name = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv4-bgp-cfg:vrf-to-global-export-route-policy'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self._is_presence:
                                return True
                            if self.allow_imported_vpn is not None:
                                return True

                            if self.route_policy_name is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_rsi_cfg as meta
                            return meta._meta_table['Vrfs.Vrf.Afs.Af.Bgp.VrfToGlobalExportRoutePolicy']['meta_info']


                    class ExportVrfOptions(object):
                        """
                        Export VRF options
                        
                        .. attribute:: allow_imported_vpn
                        
                        	TRUE Enable imported VPN paths to be exported to non\-default VRFFALSE Disable imported VPN paths to be exported to non\-default VRF
                        	**type**\:  bool
                        
                        .. attribute:: import_stitching_rt
                        
                        	TRUE Use stitchng RTs to import extranet pathsFALSE Use regular RTs to import extranet paths
                        	**type**\:  bool
                        
                        

                        """

                        _prefix = 'ipv4-bgp-cfg'
                        _revision = '2015-08-27'

                        def __init__(self):
                            self.parent = None
                            self.allow_imported_vpn = None
                            self.import_stitching_rt = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv4-bgp-cfg:export-vrf-options'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.allow_imported_vpn is not None:
                                return True

                            if self.import_stitching_rt is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_rsi_cfg as meta
                            return meta._meta_table['Vrfs.Vrf.Afs.Af.Bgp.ExportVrfOptions']['meta_info']


                    class GlobalToVrfImportRoutePolicy(object):
                        """
                        Route policy for global to vrf import filtering
                        
                        .. attribute:: advertise_as_vpn
                        
                        	TRUE Enable advertising imported paths to PEsFALSE Disable advertising imported paths to PEs
                        	**type**\:  bool
                        
                        .. attribute:: route_policy_name
                        
                        	Global to vrf import route policy
                        	**type**\:  str
                        
                        	**mandatory**\: True
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'ipv4-bgp-cfg'
                        _revision = '2015-08-27'

                        def __init__(self):
                            self.parent = None
                            self._is_presence = True
                            self.advertise_as_vpn = None
                            self.route_policy_name = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv4-bgp-cfg:global-to-vrf-import-route-policy'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self._is_presence:
                                return True
                            if self.advertise_as_vpn is not None:
                                return True

                            if self.route_policy_name is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_rsi_cfg as meta
                            return meta._meta_table['Vrfs.Vrf.Afs.Af.Bgp.GlobalToVrfImportRoutePolicy']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-bgp-cfg:bgp'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.export_route_policy is not None:
                            return True

                        if self.export_route_targets is not None and self.export_route_targets._has_data():
                            return True

                        if self.export_vrf_options is not None and self.export_vrf_options._has_data():
                            return True

                        if self.global_to_vrf_import_route_policy is not None and self.global_to_vrf_import_route_policy._has_data():
                            return True

                        if self.import_route_policy is not None:
                            return True

                        if self.import_route_targets is not None and self.import_route_targets._has_data():
                            return True

                        if self.import_vrf_options is not None:
                            return True

                        if self.vrf_to_global_export_route_policy is not None and self.vrf_to_global_export_route_policy._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_rsi_cfg as meta
                        return meta._meta_table['Vrfs.Vrf.Afs.Af.Bgp']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')
                    if self.af_name is None:
                        raise YPYModelError('Key property af_name is None')
                    if self.saf_name is None:
                        raise YPYModelError('Key property saf_name is None')
                    if self.topology_name is None:
                        raise YPYModelError('Key property topology_name is None')

                    return self.parent._common_path +'/Cisco-IOS-XR-infra-rsi-cfg:af[Cisco-IOS-XR-infra-rsi-cfg:af-name = ' + str(self.af_name) + '][Cisco-IOS-XR-infra-rsi-cfg:saf-name = ' + str(self.saf_name) + '][Cisco-IOS-XR-infra-rsi-cfg:topology-name = ' + str(self.topology_name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.af_name is not None:
                        return True

                    if self.saf_name is not None:
                        return True

                    if self.topology_name is not None:
                        return True

                    if self.bgp is not None and self.bgp._has_data():
                        return True

                    if self.create is not None:
                        return True

                    if self.maximum_prefix is not None and self.maximum_prefix._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_rsi_cfg as meta
                    return meta._meta_table['Vrfs.Vrf.Afs.Af']['meta_info']

            @property
            def _common_path(self):
                if self.parent is None:
                    raise YPYModelError('parent is not set . Cannot derive path.')

                return self.parent._common_path +'/Cisco-IOS-XR-infra-rsi-cfg:afs'

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
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_rsi_cfg as meta
                return meta._meta_table['Vrfs.Vrf.Afs']['meta_info']


        class MulticastHost(object):
            """
            Multicast host stack configuration
            
            .. attribute:: ipv4
            
            	IPv4 configuration
            	**type**\:   :py:class:`Ipv4 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.Vrfs.Vrf.MulticastHost.Ipv4>`
            
            .. attribute:: ipv6
            
            	IPv6 configuration
            	**type**\:   :py:class:`Ipv6 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.Vrfs.Vrf.MulticastHost.Ipv6>`
            
            

            """

            _prefix = 'ip-iarm-vrf-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.ipv4 = Vrfs.Vrf.MulticastHost.Ipv4()
                self.ipv4.parent = self
                self.ipv6 = Vrfs.Vrf.MulticastHost.Ipv6()
                self.ipv6.parent = self


            class Ipv4(object):
                """
                IPv4 configuration
                
                .. attribute:: interface
                
                	Default multicast host interface name
                	**type**\:  str
                
                	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                
                

                """

                _prefix = 'ip-iarm-vrf-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.interface = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ip-iarm-vrf-cfg:ipv4'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.interface is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_rsi_cfg as meta
                    return meta._meta_table['Vrfs.Vrf.MulticastHost.Ipv4']['meta_info']


            class Ipv6(object):
                """
                IPv6 configuration
                
                .. attribute:: interface
                
                	Default multicast host interface name
                	**type**\:  str
                
                	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                
                

                """

                _prefix = 'ip-iarm-vrf-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.interface = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ip-iarm-vrf-cfg:ipv6'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.interface is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_rsi_cfg as meta
                    return meta._meta_table['Vrfs.Vrf.MulticastHost.Ipv6']['meta_info']

            @property
            def _common_path(self):
                if self.parent is None:
                    raise YPYModelError('parent is not set . Cannot derive path.')

                return self.parent._common_path +'/Cisco-IOS-XR-ip-iarm-vrf-cfg:multicast-host'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.ipv4 is not None and self.ipv4._has_data():
                    return True

                if self.ipv6 is not None and self.ipv6._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_rsi_cfg as meta
                return meta._meta_table['Vrfs.Vrf.MulticastHost']['meta_info']

        @property
        def _common_path(self):
            if self.vrf_name is None:
                raise YPYModelError('Key property vrf_name is None')

            return '/Cisco-IOS-XR-infra-rsi-cfg:vrfs/Cisco-IOS-XR-infra-rsi-cfg:vrf[Cisco-IOS-XR-infra-rsi-cfg:vrf-name = ' + str(self.vrf_name) + ']'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.vrf_name is not None:
                return True

            if self.afs is not None and self.afs._has_data():
                return True

            if self.create is not None:
                return True

            if self.description is not None:
                return True

            if self.fallback_vrf is not None:
                return True

            if self.mode_big is not None:
                return True

            if self.multicast_host is not None and self.multicast_host._has_data():
                return True

            if self.remote_route_filter_disable is not None:
                return True

            if self.vpn_id is not None and self.vpn_id._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_rsi_cfg as meta
            return meta._meta_table['Vrfs.Vrf']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-infra-rsi-cfg:vrfs'

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
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_rsi_cfg as meta
        return meta._meta_table['Vrfs']['meta_info']


class GlobalAf(object):
    """
    global af
    
    .. attribute:: afs
    
    	VRF address family configuration
    	**type**\:   :py:class:`Afs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.GlobalAf.Afs>`
    
    

    """

    _prefix = 'infra-rsi-cfg'
    _revision = '2016-12-19'

    def __init__(self):
        self.afs = GlobalAf.Afs()
        self.afs.parent = self


    class Afs(object):
        """
        VRF address family configuration
        
        .. attribute:: af
        
        	VRF address family configuration
        	**type**\: list of    :py:class:`Af <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.GlobalAf.Afs.Af>`
        
        

        """

        _prefix = 'infra-rsi-cfg'
        _revision = '2016-12-19'

        def __init__(self):
            self.parent = None
            self.af = YList()
            self.af.parent = self
            self.af.name = 'af'


        class Af(object):
            """
            VRF address family configuration
            
            .. attribute:: af_name  <key>
            
            	Address family
            	**type**\:   :py:class:`VrfAddressFamilyEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.VrfAddressFamilyEnum>`
            
            .. attribute:: saf_name  <key>
            
            	Sub\-Address family
            	**type**\:   :py:class:`VrfSubAddressFamilyEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.VrfSubAddressFamilyEnum>`
            
            .. attribute:: topology_name  <key>
            
            	Topology name
            	**type**\:  str
            
            	**length:** 1..244
            
            .. attribute:: create
            
            	VRF configuration for a particular address family
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'infra-rsi-cfg'
            _revision = '2016-12-19'

            def __init__(self):
                self.parent = None
                self.af_name = None
                self.saf_name = None
                self.topology_name = None
                self.create = None

            @property
            def _common_path(self):
                if self.af_name is None:
                    raise YPYModelError('Key property af_name is None')
                if self.saf_name is None:
                    raise YPYModelError('Key property saf_name is None')
                if self.topology_name is None:
                    raise YPYModelError('Key property topology_name is None')

                return '/Cisco-IOS-XR-infra-rsi-cfg:global-af/Cisco-IOS-XR-infra-rsi-cfg:afs/Cisco-IOS-XR-infra-rsi-cfg:af[Cisco-IOS-XR-infra-rsi-cfg:af-name = ' + str(self.af_name) + '][Cisco-IOS-XR-infra-rsi-cfg:saf-name = ' + str(self.saf_name) + '][Cisco-IOS-XR-infra-rsi-cfg:topology-name = ' + str(self.topology_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.af_name is not None:
                    return True

                if self.saf_name is not None:
                    return True

                if self.topology_name is not None:
                    return True

                if self.create is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_rsi_cfg as meta
                return meta._meta_table['GlobalAf.Afs.Af']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-infra-rsi-cfg:global-af/Cisco-IOS-XR-infra-rsi-cfg:afs'

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
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_rsi_cfg as meta
            return meta._meta_table['GlobalAf.Afs']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-infra-rsi-cfg:global-af'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.afs is not None and self.afs._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_rsi_cfg as meta
        return meta._meta_table['GlobalAf']['meta_info']


class Srlg(object):
    """
    srlg
    
    .. attribute:: enable
    
    	Enable SRLG
    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
    
    .. attribute:: groups
    
    	Set of groups configured with SRLG
    	**type**\:   :py:class:`Groups <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.Srlg.Groups>`
    
    .. attribute:: inherit_nodes
    
    	Set of inherit nodes configured with SRLG
    	**type**\:   :py:class:`InheritNodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.Srlg.InheritNodes>`
    
    .. attribute:: interfaces
    
    	Set of interfaces configured with SRLG
    	**type**\:   :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.Srlg.Interfaces>`
    
    .. attribute:: srlg_names
    
    	Set of SRLG name configuration
    	**type**\:   :py:class:`SrlgNames <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.Srlg.SrlgNames>`
    
    

    """

    _prefix = 'infra-rsi-cfg'
    _revision = '2016-12-19'

    def __init__(self):
        self.enable = None
        self.groups = Srlg.Groups()
        self.groups.parent = self
        self.inherit_nodes = Srlg.InheritNodes()
        self.inherit_nodes.parent = self
        self.interfaces = Srlg.Interfaces()
        self.interfaces.parent = self
        self.srlg_names = Srlg.SrlgNames()
        self.srlg_names.parent = self


    class Interfaces(object):
        """
        Set of interfaces configured with SRLG
        
        .. attribute:: interface
        
        	Interface configurations
        	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.Srlg.Interfaces.Interface>`
        
        

        """

        _prefix = 'infra-rsi-cfg'
        _revision = '2016-12-19'

        def __init__(self):
            self.parent = None
            self.interface = YList()
            self.interface.parent = self
            self.interface.name = 'interface'


        class Interface(object):
            """
            Interface configurations
            
            .. attribute:: interface_name  <key>
            
            	Interface name
            	**type**\:  str
            
            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
            
            .. attribute:: enable
            
            	Enable SRLG interface
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: include_optical
            
            	Include optical configuration for an interface
            	**type**\:   :py:class:`IncludeOptical <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.Srlg.Interfaces.Interface.IncludeOptical>`
            
            .. attribute:: interface_group
            
            	Group configuration for an interface
            	**type**\:   :py:class:`InterfaceGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.Srlg.Interfaces.Interface.InterfaceGroup>`
            
            .. attribute:: interface_srlg_names
            
            	SRLG Name configuration for an interface
            	**type**\:   :py:class:`InterfaceSrlgNames <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.Srlg.Interfaces.Interface.InterfaceSrlgNames>`
            
            .. attribute:: values
            
            	SRLG Value configuration for an interface
            	**type**\:   :py:class:`Values <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.Srlg.Interfaces.Interface.Values>`
            
            

            """

            _prefix = 'infra-rsi-cfg'
            _revision = '2016-12-19'

            def __init__(self):
                self.parent = None
                self.interface_name = None
                self.enable = None
                self.include_optical = Srlg.Interfaces.Interface.IncludeOptical()
                self.include_optical.parent = self
                self.interface_group = Srlg.Interfaces.Interface.InterfaceGroup()
                self.interface_group.parent = self
                self.interface_srlg_names = Srlg.Interfaces.Interface.InterfaceSrlgNames()
                self.interface_srlg_names.parent = self
                self.values = Srlg.Interfaces.Interface.Values()
                self.values.parent = self


            class IncludeOptical(object):
                """
                Include optical configuration for an interface
                
                .. attribute:: enable
                
                	Enable SRLG interface include optical
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: priority
                
                	Priority for optical domain values
                	**type**\:   :py:class:`SrlgPriorityEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.SrlgPriorityEnum>`
                
                	**default value**\: default
                
                

                """

                _prefix = 'infra-rsi-cfg'
                _revision = '2016-12-19'

                def __init__(self):
                    self.parent = None
                    self.enable = None
                    self.priority = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-infra-rsi-cfg:include-optical'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.enable is not None:
                        return True

                    if self.priority is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_rsi_cfg as meta
                    return meta._meta_table['Srlg.Interfaces.Interface.IncludeOptical']['meta_info']


            class InterfaceGroup(object):
                """
                Group configuration for an interface
                
                .. attribute:: enable
                
                	Enable SRLG interface group submode
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: group_names
                
                	Set of group name under an interface
                	**type**\:   :py:class:`GroupNames <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.Srlg.Interfaces.Interface.InterfaceGroup.GroupNames>`
                
                

                """

                _prefix = 'infra-rsi-cfg'
                _revision = '2016-12-19'

                def __init__(self):
                    self.parent = None
                    self.enable = None
                    self.group_names = Srlg.Interfaces.Interface.InterfaceGroup.GroupNames()
                    self.group_names.parent = self


                class GroupNames(object):
                    """
                    Set of group name under an interface
                    
                    .. attribute:: group_name
                    
                    	Group name included under interface
                    	**type**\: list of    :py:class:`GroupName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.Srlg.Interfaces.Interface.InterfaceGroup.GroupNames.GroupName>`
                    
                    

                    """

                    _prefix = 'infra-rsi-cfg'
                    _revision = '2016-12-19'

                    def __init__(self):
                        self.parent = None
                        self.group_name = YList()
                        self.group_name.parent = self
                        self.group_name.name = 'group_name'


                    class GroupName(object):
                        """
                        Group name included under interface
                        
                        .. attribute:: group_name_index  <key>
                        
                        	Group name index
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: group_name
                        
                        	Group name
                        	**type**\:  str
                        
                        	**mandatory**\: True
                        
                        .. attribute:: srlg_priority
                        
                        	SRLG priority
                        	**type**\:   :py:class:`SrlgPriorityEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.SrlgPriorityEnum>`
                        
                        	**default value**\: default
                        
                        

                        """

                        _prefix = 'infra-rsi-cfg'
                        _revision = '2016-12-19'

                        def __init__(self):
                            self.parent = None
                            self.group_name_index = None
                            self.group_name = None
                            self.srlg_priority = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.group_name_index is None:
                                raise YPYModelError('Key property group_name_index is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-infra-rsi-cfg:group-name[Cisco-IOS-XR-infra-rsi-cfg:group-name-index = ' + str(self.group_name_index) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.group_name_index is not None:
                                return True

                            if self.group_name is not None:
                                return True

                            if self.srlg_priority is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_rsi_cfg as meta
                            return meta._meta_table['Srlg.Interfaces.Interface.InterfaceGroup.GroupNames.GroupName']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-infra-rsi-cfg:group-names'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.group_name is not None:
                            for child_ref in self.group_name:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_rsi_cfg as meta
                        return meta._meta_table['Srlg.Interfaces.Interface.InterfaceGroup.GroupNames']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-infra-rsi-cfg:interface-group'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.enable is not None:
                        return True

                    if self.group_names is not None and self.group_names._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_rsi_cfg as meta
                    return meta._meta_table['Srlg.Interfaces.Interface.InterfaceGroup']['meta_info']


            class Values(object):
                """
                SRLG Value configuration for an interface
                
                .. attribute:: value
                
                	SRLG value data
                	**type**\: list of    :py:class:`Value <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.Srlg.Interfaces.Interface.Values.Value>`
                
                

                """

                _prefix = 'infra-rsi-cfg'
                _revision = '2016-12-19'

                def __init__(self):
                    self.parent = None
                    self.value = YList()
                    self.value.parent = self
                    self.value.name = 'value'


                class Value(object):
                    """
                    SRLG value data
                    
                    .. attribute:: srlg_index  <key>
                    
                    	SRLG index
                    	**type**\:  int
                    
                    	**range:** 1..65535
                    
                    .. attribute:: srlg_priority
                    
                    	SRLG priority
                    	**type**\:   :py:class:`SrlgPriorityEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.SrlgPriorityEnum>`
                    
                    	**default value**\: default
                    
                    .. attribute:: srlg_value
                    
                    	SRLG value
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**mandatory**\: True
                    
                    

                    """

                    _prefix = 'infra-rsi-cfg'
                    _revision = '2016-12-19'

                    def __init__(self):
                        self.parent = None
                        self.srlg_index = None
                        self.srlg_priority = None
                        self.srlg_value = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.srlg_index is None:
                            raise YPYModelError('Key property srlg_index is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-infra-rsi-cfg:value[Cisco-IOS-XR-infra-rsi-cfg:srlg-index = ' + str(self.srlg_index) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.srlg_index is not None:
                            return True

                        if self.srlg_priority is not None:
                            return True

                        if self.srlg_value is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_rsi_cfg as meta
                        return meta._meta_table['Srlg.Interfaces.Interface.Values.Value']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-infra-rsi-cfg:values'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.value is not None:
                        for child_ref in self.value:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_rsi_cfg as meta
                    return meta._meta_table['Srlg.Interfaces.Interface.Values']['meta_info']


            class InterfaceSrlgNames(object):
                """
                SRLG Name configuration for an interface
                
                .. attribute:: interface_srlg_name
                
                	SRLG name data
                	**type**\: list of    :py:class:`InterfaceSrlgName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.Srlg.Interfaces.Interface.InterfaceSrlgNames.InterfaceSrlgName>`
                
                

                """

                _prefix = 'infra-rsi-cfg'
                _revision = '2016-12-19'

                def __init__(self):
                    self.parent = None
                    self.interface_srlg_name = YList()
                    self.interface_srlg_name.parent = self
                    self.interface_srlg_name.name = 'interface_srlg_name'


                class InterfaceSrlgName(object):
                    """
                    SRLG name data
                    
                    .. attribute:: srlg_name  <key>
                    
                    	SRLG name
                    	**type**\:  str
                    
                    	**length:** 1..64
                    
                    

                    """

                    _prefix = 'infra-rsi-cfg'
                    _revision = '2016-12-19'

                    def __init__(self):
                        self.parent = None
                        self.srlg_name = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.srlg_name is None:
                            raise YPYModelError('Key property srlg_name is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-infra-rsi-cfg:interface-srlg-name[Cisco-IOS-XR-infra-rsi-cfg:srlg-name = ' + str(self.srlg_name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.srlg_name is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_rsi_cfg as meta
                        return meta._meta_table['Srlg.Interfaces.Interface.InterfaceSrlgNames.InterfaceSrlgName']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-infra-rsi-cfg:interface-srlg-names'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.interface_srlg_name is not None:
                        for child_ref in self.interface_srlg_name:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_rsi_cfg as meta
                    return meta._meta_table['Srlg.Interfaces.Interface.InterfaceSrlgNames']['meta_info']

            @property
            def _common_path(self):
                if self.interface_name is None:
                    raise YPYModelError('Key property interface_name is None')

                return '/Cisco-IOS-XR-infra-rsi-cfg:srlg/Cisco-IOS-XR-infra-rsi-cfg:interfaces/Cisco-IOS-XR-infra-rsi-cfg:interface[Cisco-IOS-XR-infra-rsi-cfg:interface-name = ' + str(self.interface_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.interface_name is not None:
                    return True

                if self.enable is not None:
                    return True

                if self.include_optical is not None and self.include_optical._has_data():
                    return True

                if self.interface_group is not None and self.interface_group._has_data():
                    return True

                if self.interface_srlg_names is not None and self.interface_srlg_names._has_data():
                    return True

                if self.values is not None and self.values._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_rsi_cfg as meta
                return meta._meta_table['Srlg.Interfaces.Interface']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-infra-rsi-cfg:srlg/Cisco-IOS-XR-infra-rsi-cfg:interfaces'

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
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_rsi_cfg as meta
            return meta._meta_table['Srlg.Interfaces']['meta_info']


    class SrlgNames(object):
        """
        Set of SRLG name configuration
        
        .. attribute:: srlg_name
        
        	SRLG name configuration
        	**type**\: list of    :py:class:`SrlgName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.Srlg.SrlgNames.SrlgName>`
        
        

        """

        _prefix = 'infra-rsi-cfg'
        _revision = '2016-12-19'

        def __init__(self):
            self.parent = None
            self.srlg_name = YList()
            self.srlg_name.parent = self
            self.srlg_name.name = 'srlg_name'


        class SrlgName(object):
            """
            SRLG name configuration
            
            .. attribute:: srlg_name  <key>
            
            	SRLG name
            	**type**\:  str
            
            	**length:** 1..64
            
            .. attribute:: srlg_value
            
            	SRLG value
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**mandatory**\: True
            
            

            """

            _prefix = 'infra-rsi-cfg'
            _revision = '2016-12-19'

            def __init__(self):
                self.parent = None
                self.srlg_name = None
                self.srlg_value = None

            @property
            def _common_path(self):
                if self.srlg_name is None:
                    raise YPYModelError('Key property srlg_name is None')

                return '/Cisco-IOS-XR-infra-rsi-cfg:srlg/Cisco-IOS-XR-infra-rsi-cfg:srlg-names/Cisco-IOS-XR-infra-rsi-cfg:srlg-name[Cisco-IOS-XR-infra-rsi-cfg:srlg-name = ' + str(self.srlg_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.srlg_name is not None:
                    return True

                if self.srlg_value is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_rsi_cfg as meta
                return meta._meta_table['Srlg.SrlgNames.SrlgName']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-infra-rsi-cfg:srlg/Cisco-IOS-XR-infra-rsi-cfg:srlg-names'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.srlg_name is not None:
                for child_ref in self.srlg_name:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_rsi_cfg as meta
            return meta._meta_table['Srlg.SrlgNames']['meta_info']


    class Groups(object):
        """
        Set of groups configured with SRLG
        
        .. attribute:: group
        
        	Group configurations
        	**type**\: list of    :py:class:`Group <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.Srlg.Groups.Group>`
        
        

        """

        _prefix = 'infra-rsi-cfg'
        _revision = '2016-12-19'

        def __init__(self):
            self.parent = None
            self.group = YList()
            self.group.parent = self
            self.group.name = 'group'


        class Group(object):
            """
            Group configurations
            
            .. attribute:: group_name  <key>
            
            	Group name
            	**type**\:  str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: enable
            
            	Enable SRLG group
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: group_values
            
            	Set of SRLG values configured under a group
            	**type**\:   :py:class:`GroupValues <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.Srlg.Groups.Group.GroupValues>`
            
            

            """

            _prefix = 'infra-rsi-cfg'
            _revision = '2016-12-19'

            def __init__(self):
                self.parent = None
                self.group_name = None
                self.enable = None
                self.group_values = Srlg.Groups.Group.GroupValues()
                self.group_values.parent = self


            class GroupValues(object):
                """
                Set of SRLG values configured under a group
                
                .. attribute:: group_value
                
                	Group SRLG values with attribute
                	**type**\: list of    :py:class:`GroupValue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.Srlg.Groups.Group.GroupValues.GroupValue>`
                
                

                """

                _prefix = 'infra-rsi-cfg'
                _revision = '2016-12-19'

                def __init__(self):
                    self.parent = None
                    self.group_value = YList()
                    self.group_value.parent = self
                    self.group_value.name = 'group_value'


                class GroupValue(object):
                    """
                    Group SRLG values with attribute
                    
                    .. attribute:: srlg_index  <key>
                    
                    	SRLG index
                    	**type**\:  int
                    
                    	**range:** 1..65535
                    
                    .. attribute:: srlg_priority
                    
                    	SRLG priority
                    	**type**\:   :py:class:`SrlgPriorityEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.SrlgPriorityEnum>`
                    
                    	**default value**\: default
                    
                    .. attribute:: srlg_value
                    
                    	SRLG value
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**mandatory**\: True
                    
                    

                    """

                    _prefix = 'infra-rsi-cfg'
                    _revision = '2016-12-19'

                    def __init__(self):
                        self.parent = None
                        self.srlg_index = None
                        self.srlg_priority = None
                        self.srlg_value = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.srlg_index is None:
                            raise YPYModelError('Key property srlg_index is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-infra-rsi-cfg:group-value[Cisco-IOS-XR-infra-rsi-cfg:srlg-index = ' + str(self.srlg_index) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.srlg_index is not None:
                            return True

                        if self.srlg_priority is not None:
                            return True

                        if self.srlg_value is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_rsi_cfg as meta
                        return meta._meta_table['Srlg.Groups.Group.GroupValues.GroupValue']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-infra-rsi-cfg:group-values'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.group_value is not None:
                        for child_ref in self.group_value:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_rsi_cfg as meta
                    return meta._meta_table['Srlg.Groups.Group.GroupValues']['meta_info']

            @property
            def _common_path(self):
                if self.group_name is None:
                    raise YPYModelError('Key property group_name is None')

                return '/Cisco-IOS-XR-infra-rsi-cfg:srlg/Cisco-IOS-XR-infra-rsi-cfg:groups/Cisco-IOS-XR-infra-rsi-cfg:group[Cisco-IOS-XR-infra-rsi-cfg:group-name = ' + str(self.group_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.group_name is not None:
                    return True

                if self.enable is not None:
                    return True

                if self.group_values is not None and self.group_values._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_rsi_cfg as meta
                return meta._meta_table['Srlg.Groups.Group']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-infra-rsi-cfg:srlg/Cisco-IOS-XR-infra-rsi-cfg:groups'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.group is not None:
                for child_ref in self.group:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_rsi_cfg as meta
            return meta._meta_table['Srlg.Groups']['meta_info']


    class InheritNodes(object):
        """
        Set of inherit nodes configured with SRLG
        
        .. attribute:: inherit_node
        
        	Inherit node configurations
        	**type**\: list of    :py:class:`InheritNode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.Srlg.InheritNodes.InheritNode>`
        
        

        """

        _prefix = 'infra-rsi-cfg'
        _revision = '2016-12-19'

        def __init__(self):
            self.parent = None
            self.inherit_node = YList()
            self.inherit_node.parent = self
            self.inherit_node.name = 'inherit_node'


        class InheritNode(object):
            """
            Inherit node configurations
            
            .. attribute:: inherit_node_name  <key>
            
            	The inherit node name
            	**type**\:  str
            
            	**pattern:** ((([a\-zA\-Z0\-9\_]\*\\d+)\|(\\\*))/){2}(([a\-zA\-Z0\-9\_]\*\\d+)\|(\\\*))
            
            .. attribute:: enable
            
            	Enable SRLG inherit node
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: inherit_node_values
            
            	Set of SRLG values configured under an inherit node
            	**type**\:   :py:class:`InheritNodeValues <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.Srlg.InheritNodes.InheritNode.InheritNodeValues>`
            
            

            """

            _prefix = 'infra-rsi-cfg'
            _revision = '2016-12-19'

            def __init__(self):
                self.parent = None
                self.inherit_node_name = None
                self.enable = None
                self.inherit_node_values = Srlg.InheritNodes.InheritNode.InheritNodeValues()
                self.inherit_node_values.parent = self


            class InheritNodeValues(object):
                """
                Set of SRLG values configured under an inherit
                node
                
                .. attribute:: inherit_node_value
                
                	Inherit node SRLG value with attributes
                	**type**\: list of    :py:class:`InheritNodeValue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.Srlg.InheritNodes.InheritNode.InheritNodeValues.InheritNodeValue>`
                
                

                """

                _prefix = 'infra-rsi-cfg'
                _revision = '2016-12-19'

                def __init__(self):
                    self.parent = None
                    self.inherit_node_value = YList()
                    self.inherit_node_value.parent = self
                    self.inherit_node_value.name = 'inherit_node_value'


                class InheritNodeValue(object):
                    """
                    Inherit node SRLG value with attributes
                    
                    .. attribute:: srlg_index  <key>
                    
                    	SRLG index
                    	**type**\:  int
                    
                    	**range:** 1..65535
                    
                    .. attribute:: srlg_priority
                    
                    	SRLG priority
                    	**type**\:   :py:class:`SrlgPriorityEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.SrlgPriorityEnum>`
                    
                    	**default value**\: default
                    
                    .. attribute:: srlg_value
                    
                    	SRLG value
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**mandatory**\: True
                    
                    

                    """

                    _prefix = 'infra-rsi-cfg'
                    _revision = '2016-12-19'

                    def __init__(self):
                        self.parent = None
                        self.srlg_index = None
                        self.srlg_priority = None
                        self.srlg_value = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.srlg_index is None:
                            raise YPYModelError('Key property srlg_index is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-infra-rsi-cfg:inherit-node-value[Cisco-IOS-XR-infra-rsi-cfg:srlg-index = ' + str(self.srlg_index) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.srlg_index is not None:
                            return True

                        if self.srlg_priority is not None:
                            return True

                        if self.srlg_value is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_rsi_cfg as meta
                        return meta._meta_table['Srlg.InheritNodes.InheritNode.InheritNodeValues.InheritNodeValue']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-infra-rsi-cfg:inherit-node-values'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.inherit_node_value is not None:
                        for child_ref in self.inherit_node_value:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_rsi_cfg as meta
                    return meta._meta_table['Srlg.InheritNodes.InheritNode.InheritNodeValues']['meta_info']

            @property
            def _common_path(self):
                if self.inherit_node_name is None:
                    raise YPYModelError('Key property inherit_node_name is None')

                return '/Cisco-IOS-XR-infra-rsi-cfg:srlg/Cisco-IOS-XR-infra-rsi-cfg:inherit-nodes/Cisco-IOS-XR-infra-rsi-cfg:inherit-node[Cisco-IOS-XR-infra-rsi-cfg:inherit-node-name = ' + str(self.inherit_node_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.inherit_node_name is not None:
                    return True

                if self.enable is not None:
                    return True

                if self.inherit_node_values is not None and self.inherit_node_values._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_rsi_cfg as meta
                return meta._meta_table['Srlg.InheritNodes.InheritNode']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-infra-rsi-cfg:srlg/Cisco-IOS-XR-infra-rsi-cfg:inherit-nodes'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.inherit_node is not None:
                for child_ref in self.inherit_node:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_rsi_cfg as meta
            return meta._meta_table['Srlg.InheritNodes']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-infra-rsi-cfg:srlg'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.enable is not None:
            return True

        if self.groups is not None and self.groups._has_data():
            return True

        if self.inherit_nodes is not None and self.inherit_nodes._has_data():
            return True

        if self.interfaces is not None and self.interfaces._has_data():
            return True

        if self.srlg_names is not None and self.srlg_names._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_rsi_cfg as meta
        return meta._meta_table['Srlg']['meta_info']


class VrfGroups(object):
    """
    vrf groups
    
    .. attribute:: vrf_group
    
    	VRF group configuration
    	**type**\: list of    :py:class:`VrfGroup <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.VrfGroups.VrfGroup>`
    
    

    """

    _prefix = 'infra-rsi-cfg'
    _revision = '2016-12-19'

    def __init__(self):
        self.vrf_group = YList()
        self.vrf_group.parent = self
        self.vrf_group.name = 'vrf_group'


    class VrfGroup(object):
        """
        VRF group configuration
        
        .. attribute:: vrf_group_name  <key>
        
        	VRF group name
        	**type**\:  str
        
        	**length:** 1..32
        
        .. attribute:: enable
        
        	Enable VRF group
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: vrfs
        
        	Set of VRFs configured under a VRF group
        	**type**\:   :py:class:`Vrfs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.VrfGroups.VrfGroup.Vrfs>`
        
        

        """

        _prefix = 'infra-rsi-cfg'
        _revision = '2016-12-19'

        def __init__(self):
            self.parent = None
            self.vrf_group_name = None
            self.enable = None
            self.vrfs = VrfGroups.VrfGroup.Vrfs()
            self.vrfs.parent = self


        class Vrfs(object):
            """
            Set of VRFs configured under a VRF group
            
            .. attribute:: vrf
            
            	VRF configuration
            	**type**\: list of    :py:class:`Vrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg.VrfGroups.VrfGroup.Vrfs.Vrf>`
            
            

            """

            _prefix = 'infra-rsi-cfg'
            _revision = '2016-12-19'

            def __init__(self):
                self.parent = None
                self.vrf = YList()
                self.vrf.parent = self
                self.vrf.name = 'vrf'


            class Vrf(object):
                """
                VRF configuration
                
                .. attribute:: vrf_name  <key>
                
                	VRF name
                	**type**\:  str
                
                	**length:** 1..32
                
                

                """

                _prefix = 'infra-rsi-cfg'
                _revision = '2016-12-19'

                def __init__(self):
                    self.parent = None
                    self.vrf_name = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')
                    if self.vrf_name is None:
                        raise YPYModelError('Key property vrf_name is None')

                    return self.parent._common_path +'/Cisco-IOS-XR-infra-rsi-cfg:vrf[Cisco-IOS-XR-infra-rsi-cfg:vrf-name = ' + str(self.vrf_name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.vrf_name is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_rsi_cfg as meta
                    return meta._meta_table['VrfGroups.VrfGroup.Vrfs.Vrf']['meta_info']

            @property
            def _common_path(self):
                if self.parent is None:
                    raise YPYModelError('parent is not set . Cannot derive path.')

                return self.parent._common_path +'/Cisco-IOS-XR-infra-rsi-cfg:vrfs'

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
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_rsi_cfg as meta
                return meta._meta_table['VrfGroups.VrfGroup.Vrfs']['meta_info']

        @property
        def _common_path(self):
            if self.vrf_group_name is None:
                raise YPYModelError('Key property vrf_group_name is None')

            return '/Cisco-IOS-XR-infra-rsi-cfg:vrf-groups/Cisco-IOS-XR-infra-rsi-cfg:vrf-group[Cisco-IOS-XR-infra-rsi-cfg:vrf-group-name = ' + str(self.vrf_group_name) + ']'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.vrf_group_name is not None:
                return True

            if self.enable is not None:
                return True

            if self.vrfs is not None and self.vrfs._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_rsi_cfg as meta
            return meta._meta_table['VrfGroups.VrfGroup']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-infra-rsi-cfg:vrf-groups'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.vrf_group is not None:
            for child_ref in self.vrf_group:
                if child_ref._has_data():
                    return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_rsi_cfg as meta
        return meta._meta_table['VrfGroups']['meta_info']


class SelectiveVrfDownload(object):
    """
    selective vrf download
    
    .. attribute:: disable
    
    	Disable selective VRF download
    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
    
    

    """

    _prefix = 'infra-rsi-cfg'
    _revision = '2016-12-19'

    def __init__(self):
        self.disable = None

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-infra-rsi-cfg:selective-vrf-download'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.disable is not None:
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_rsi_cfg as meta
        return meta._meta_table['SelectiveVrfDownload']['meta_info']


