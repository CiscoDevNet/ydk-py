""" Cisco_IOS_XR_ipv4_pim_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ipv4\-pim package configuration.

This module contains definitions
for the following management objects\:
  pim\: PIM configuration

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class PimMultipathEnum(Enum):
    """
    PimMultipathEnum

    Pim multipath

    .. data:: enable = 0

    	Enable PIM multipath

    .. data:: interface_hash = 1

    	Enable PIM multipath with interface based

    	hashing

    .. data:: source_hash = 2

    	Enable PIM multipath with source based hashing

    .. data:: source_next_hop_hash = 3

    	Enable PIM multipath with source next-hop

    	hashing

    .. data:: source_group_hash = 4

    	Enable PIM multipath with source, group based

    	hashing

    """

    enable = 0

    interface_hash = 1

    source_hash = 2

    source_next_hop_hash = 3

    source_group_hash = 4


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_pim_cfg as meta
        return meta._meta_table['PimMultipathEnum']


class PimProtocolModeEnum(Enum):
    """
    PimProtocolModeEnum

    Pim protocol mode

    .. data:: sm = 0

    	Sparse Mode

    .. data:: bidir = 1

    	Bidirectional

    """

    sm = 0

    bidir = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_pim_cfg as meta
        return meta._meta_table['PimProtocolModeEnum']



class Pim(object):
    """
    PIM configuration
    
    .. attribute:: default_context
    
    	Default Context
    	**type**\:   :py:class:`DefaultContext <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.DefaultContext>`
    
    	**presence node**\: True
    
    .. attribute:: vrfs
    
    	VRF table
    	**type**\:   :py:class:`Vrfs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.Vrfs>`
    
    .. attribute:: _is_presence
    
    	Is present if this instance represents presence container else not
    	**type**\: bool
    
    

    This class is a :ref:`presence class<presence-class>`

    """

    _prefix = 'ipv4-pim-cfg'
    _revision = '2016-06-01'

    def __init__(self):
        self._is_presence = True
        self.default_context = None
        self.vrfs = Pim.Vrfs()
        self.vrfs.parent = self


    class Vrfs(object):
        """
        VRF table
        
        .. attribute:: vrf
        
        	VRF name
        	**type**\: list of    :py:class:`Vrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.Vrfs.Vrf>`
        
        

        """

        _prefix = 'ipv4-pim-cfg'
        _revision = '2016-06-01'

        def __init__(self):
            self.parent = None
            self.vrf = YList()
            self.vrf.parent = self
            self.vrf.name = 'vrf'


        class Vrf(object):
            """
            VRF name
            
            .. attribute:: vrf_name  <key>
            
            	VRF name
            	**type**\:  str
            
            	**length:** 1..32
            
            .. attribute:: ipv4
            
            	IPV4 commands
            	**type**\:   :py:class:`Ipv4 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.Vrfs.Vrf.Ipv4>`
            
            .. attribute:: ipv6
            
            	IPV6 commands
            	**type**\:   :py:class:`Ipv6 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.Vrfs.Vrf.Ipv6>`
            
            

            """

            _prefix = 'ipv4-pim-cfg'
            _revision = '2016-06-01'

            def __init__(self):
                self.parent = None
                self.vrf_name = None
                self.ipv4 = Pim.Vrfs.Vrf.Ipv4()
                self.ipv4.parent = self
                self.ipv6 = Pim.Vrfs.Vrf.Ipv6()
                self.ipv6.parent = self


            class Ipv4(object):
                """
                IPV4 commands
                
                .. attribute:: accept_register
                
                	Access\-list which specifies unauthorized sources
                	**type**\:  str
                
                	**length:** 1..64
                
                .. attribute:: allow_rp
                
                	Enable allow\-rp filtering for SM joins
                	**type**\:   :py:class:`AllowRp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.Vrfs.Vrf.Ipv4.AllowRp>`
                
                	**presence node**\: True
                
                .. attribute:: auto_rp_disable
                
                	Disable Rendezvous Point discovery through the AutoRP protocol
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: bidir_rp_addresses
                
                	Configure Bidirectional PIM Rendezvous Point
                	**type**\:   :py:class:`BidirRpAddresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.Vrfs.Vrf.Ipv4.BidirRpAddresses>`
                
                .. attribute:: bsr
                
                	PIM BSR configuration
                	**type**\:   :py:class:`Bsr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.Vrfs.Vrf.Ipv4.Bsr>`
                
                .. attribute:: cj_multicast_only_frrs
                
                	Clone Join Multicast Only FRR
                	**type**\:   :py:class:`CjMulticastOnlyFrrs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.Vrfs.Vrf.Ipv4.CjMulticastOnlyFrrs>`
                
                .. attribute:: convergence
                
                	Configure convergence parameters
                	**type**\:   :py:class:`Convergence <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.Vrfs.Vrf.Ipv4.Convergence>`
                
                .. attribute:: cs_multicast_only_frrs
                
                	Clone Source Multicast Only FRR
                	**type**\:   :py:class:`CsMulticastOnlyFrrs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.Vrfs.Vrf.Ipv4.CsMulticastOnlyFrrs>`
                
                .. attribute:: inheritable_defaults
                
                	Inheritable defaults
                	**type**\:   :py:class:`InheritableDefaults <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.Vrfs.Vrf.Ipv4.InheritableDefaults>`
                
                .. attribute:: injects
                
                	Inject Explicit PIM RPF Vector Proxy's
                	**type**\:   :py:class:`Injects <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.Vrfs.Vrf.Ipv4.Injects>`
                
                .. attribute:: interfaces
                
                	Interface\-level Configuration
                	**type**\:   :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.Vrfs.Vrf.Ipv4.Interfaces>`
                
                .. attribute:: log_neighbor_changes
                
                	PIM neighbor state change logging is turned on if configured
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: maximum
                
                	Configure PIM State Limits
                	**type**\:   :py:class:`Maximum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.Vrfs.Vrf.Ipv4.Maximum>`
                
                .. attribute:: multicast_only_frr
                
                	Multicast Only FRR
                	**type**\:   :py:class:`MulticastOnlyFrr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.Vrfs.Vrf.Ipv4.MulticastOnlyFrr>`
                
                .. attribute:: multipath
                
                	Enable equal\-cost multipath routing
                	**type**\:   :py:class:`PimMultipathEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.PimMultipathEnum>`
                
                .. attribute:: neighbor_check_on_receive
                
                	Enable PIM neighbor checking when receiving PIM messages
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: neighbor_check_on_send
                
                	Enable PIM neighbor checking when sending join\-prunes
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: neighbor_filter
                
                	Access\-list of neighbors to be filtered
                	**type**\:  str
                
                	**length:** 1..64
                
                .. attribute:: old_register_checksum
                
                	Generate registers compatible with older IOS versions
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: paths
                
                	Inject PIM RPF Vector Proxy's
                	**type**\:   :py:class:`Paths <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.Vrfs.Vrf.Ipv4.Paths>`
                
                .. attribute:: register_source
                
                	Source address to use for register messages
                	**type**\:  str
                
                	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                
                .. attribute:: rp_static_deny
                
                	Configure static RP deny range
                	**type**\:  str
                
                	**length:** 1..64
                
                .. attribute:: rpf
                
                	Configure RPF options
                	**type**\:   :py:class:`Rpf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.Vrfs.Vrf.Ipv4.Rpf>`
                
                .. attribute:: rpf_vector_enable
                
                	Enable PIM RPF Vector Proxy's
                	**type**\:   :py:class:`RpfVectorEnable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.Vrfs.Vrf.Ipv4.RpfVectorEnable>`
                
                	**presence node**\: True
                
                .. attribute:: sg_expiry_timer
                
                	Configure expiry timer for S,G routes
                	**type**\:   :py:class:`SgExpiryTimer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.Vrfs.Vrf.Ipv4.SgExpiryTimer>`
                
                .. attribute:: sparse_mode_rp_addresses
                
                	Configure Sparse\-Mode Rendezvous Point
                	**type**\:   :py:class:`SparseModeRpAddresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.Vrfs.Vrf.Ipv4.SparseModeRpAddresses>`
                
                .. attribute:: spt_threshold_infinity
                
                	Configure threshold of infinity for switching to SPT on last\-hop
                	**type**\:  str
                
                .. attribute:: ssm
                
                	Configure IP Multicast SSM
                	**type**\:   :py:class:`Ssm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.Vrfs.Vrf.Ipv4.Ssm>`
                
                .. attribute:: ssm_allow_override
                
                	Allow SSM ranges to be overridden by more specific ranges
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: suppress_data_registers
                
                	Suppress data registers after initial state setup
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: suppress_rpf_prunes
                
                	Suppress prunes triggered as a result of RPF changes
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                

                """

                _prefix = 'ipv4-pim-cfg'
                _revision = '2016-06-01'

                def __init__(self):
                    self.parent = None
                    self.accept_register = None
                    self.allow_rp = None
                    self.auto_rp_disable = None
                    self.bidir_rp_addresses = Pim.Vrfs.Vrf.Ipv4.BidirRpAddresses()
                    self.bidir_rp_addresses.parent = self
                    self.bsr = Pim.Vrfs.Vrf.Ipv4.Bsr()
                    self.bsr.parent = self
                    self.cj_multicast_only_frrs = Pim.Vrfs.Vrf.Ipv4.CjMulticastOnlyFrrs()
                    self.cj_multicast_only_frrs.parent = self
                    self.convergence = Pim.Vrfs.Vrf.Ipv4.Convergence()
                    self.convergence.parent = self
                    self.cs_multicast_only_frrs = Pim.Vrfs.Vrf.Ipv4.CsMulticastOnlyFrrs()
                    self.cs_multicast_only_frrs.parent = self
                    self.inheritable_defaults = Pim.Vrfs.Vrf.Ipv4.InheritableDefaults()
                    self.inheritable_defaults.parent = self
                    self.injects = Pim.Vrfs.Vrf.Ipv4.Injects()
                    self.injects.parent = self
                    self.interfaces = Pim.Vrfs.Vrf.Ipv4.Interfaces()
                    self.interfaces.parent = self
                    self.log_neighbor_changes = None
                    self.maximum = Pim.Vrfs.Vrf.Ipv4.Maximum()
                    self.maximum.parent = self
                    self.multicast_only_frr = Pim.Vrfs.Vrf.Ipv4.MulticastOnlyFrr()
                    self.multicast_only_frr.parent = self
                    self.multipath = None
                    self.neighbor_check_on_receive = None
                    self.neighbor_check_on_send = None
                    self.neighbor_filter = None
                    self.old_register_checksum = None
                    self.paths = Pim.Vrfs.Vrf.Ipv4.Paths()
                    self.paths.parent = self
                    self.register_source = None
                    self.rp_static_deny = None
                    self.rpf = Pim.Vrfs.Vrf.Ipv4.Rpf()
                    self.rpf.parent = self
                    self.rpf_vector_enable = None
                    self.sg_expiry_timer = Pim.Vrfs.Vrf.Ipv4.SgExpiryTimer()
                    self.sg_expiry_timer.parent = self
                    self.sparse_mode_rp_addresses = Pim.Vrfs.Vrf.Ipv4.SparseModeRpAddresses()
                    self.sparse_mode_rp_addresses.parent = self
                    self.spt_threshold_infinity = None
                    self.ssm = Pim.Vrfs.Vrf.Ipv4.Ssm()
                    self.ssm.parent = self
                    self.ssm_allow_override = None
                    self.suppress_data_registers = None
                    self.suppress_rpf_prunes = None


                class SparseModeRpAddresses(object):
                    """
                    Configure Sparse\-Mode Rendezvous Point
                    
                    .. attribute:: sparse_mode_rp_address
                    
                    	Address of the Rendezvous Point
                    	**type**\: list of    :py:class:`SparseModeRpAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.Vrfs.Vrf.Ipv4.SparseModeRpAddresses.SparseModeRpAddress>`
                    
                    

                    """

                    _prefix = 'ipv4-pim-cfg'
                    _revision = '2016-06-01'

                    def __init__(self):
                        self.parent = None
                        self.sparse_mode_rp_address = YList()
                        self.sparse_mode_rp_address.parent = self
                        self.sparse_mode_rp_address.name = 'sparse_mode_rp_address'


                    class SparseModeRpAddress(object):
                        """
                        Address of the Rendezvous Point
                        
                        .. attribute:: rp_address  <key>
                        
                        	RP address of Rendezvous Point
                        	**type**\: one of the below types:
                        
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        .. attribute:: access_list_name
                        
                        	Access list of groups that should map to a  given RP
                        	**type**\:  str
                        
                        	**length:** 1..64
                        
                        .. attribute:: auto_rp_override
                        
                        	TRUE Indicates if static RP config overrides AutoRP and BSR
                        	**type**\:  bool
                        
                        

                        """

                        _prefix = 'ipv4-pim-cfg'
                        _revision = '2016-06-01'

                        def __init__(self):
                            self.parent = None
                            self.rp_address = None
                            self.access_list_name = None
                            self.auto_rp_override = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.rp_address is None:
                                raise YPYModelError('Key property rp_address is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv4-pim-cfg:sparse-mode-rp-address[Cisco-IOS-XR-ipv4-pim-cfg:rp-address = ' + str(self.rp_address) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.rp_address is not None:
                                return True

                            if self.access_list_name is not None:
                                return True

                            if self.auto_rp_override is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_pim_cfg as meta
                            return meta._meta_table['Pim.Vrfs.Vrf.Ipv4.SparseModeRpAddresses.SparseModeRpAddress']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-pim-cfg:sparse-mode-rp-addresses'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.sparse_mode_rp_address is not None:
                            for child_ref in self.sparse_mode_rp_address:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_pim_cfg as meta
                        return meta._meta_table['Pim.Vrfs.Vrf.Ipv4.SparseModeRpAddresses']['meta_info']


                class MulticastOnlyFrr(object):
                    """
                    Multicast Only FRR
                    
                    .. attribute:: enable
                    
                    	Enable Multicast Only FRR
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: flow_multicast_only_frr
                    
                    	Access\-list specifying SG that should do FLOW MOFRR
                    	**type**\:  str
                    
                    	**length:** 1..64
                    
                    .. attribute:: non_revertive_multicast_only_frr
                    
                    	Non\-revertive Multicast Only FRR
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: rib_multicast_only_frr
                    
                    	Access\-list specifying SG that should do RIB MOFRR
                    	**type**\:  str
                    
                    	**length:** 1..64
                    
                    

                    """

                    _prefix = 'ipv4-pim-cfg'
                    _revision = '2016-06-01'

                    def __init__(self):
                        self.parent = None
                        self.enable = None
                        self.flow_multicast_only_frr = None
                        self.non_revertive_multicast_only_frr = None
                        self.rib_multicast_only_frr = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-pim-cfg:multicast-only-frr'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.enable is not None:
                            return True

                        if self.flow_multicast_only_frr is not None:
                            return True

                        if self.non_revertive_multicast_only_frr is not None:
                            return True

                        if self.rib_multicast_only_frr is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_pim_cfg as meta
                        return meta._meta_table['Pim.Vrfs.Vrf.Ipv4.MulticastOnlyFrr']['meta_info']


                class CsMulticastOnlyFrrs(object):
                    """
                    Clone Source Multicast Only FRR
                    
                    .. attribute:: cs_multicast_only_frr
                    
                    	Clone Source Multicast Only FRR
                    	**type**\: list of    :py:class:`CsMulticastOnlyFrr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.Vrfs.Vrf.Ipv4.CsMulticastOnlyFrrs.CsMulticastOnlyFrr>`
                    
                    

                    """

                    _prefix = 'ipv4-pim-cfg'
                    _revision = '2016-06-01'

                    def __init__(self):
                        self.parent = None
                        self.cs_multicast_only_frr = YList()
                        self.cs_multicast_only_frr.parent = self
                        self.cs_multicast_only_frr.name = 'cs_multicast_only_frr'


                    class CsMulticastOnlyFrr(object):
                        """
                        Clone Source Multicast Only FRR
                        
                        .. attribute:: source  <key>
                        
                        	Original address
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: primary  <key>
                        
                        	Primary address
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: backup  <key>
                        
                        	Backup address
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: prefix_length  <key>
                        
                        	Masklen
                        	**type**\:  int
                        
                        	**range:** 0..32
                        
                        

                        """

                        _prefix = 'ipv4-pim-cfg'
                        _revision = '2016-06-01'

                        def __init__(self):
                            self.parent = None
                            self.source = None
                            self.primary = None
                            self.backup = None
                            self.prefix_length = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.source is None:
                                raise YPYModelError('Key property source is None')
                            if self.primary is None:
                                raise YPYModelError('Key property primary is None')
                            if self.backup is None:
                                raise YPYModelError('Key property backup is None')
                            if self.prefix_length is None:
                                raise YPYModelError('Key property prefix_length is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv4-pim-cfg:cs-multicast-only-frr[Cisco-IOS-XR-ipv4-pim-cfg:source = ' + str(self.source) + '][Cisco-IOS-XR-ipv4-pim-cfg:primary = ' + str(self.primary) + '][Cisco-IOS-XR-ipv4-pim-cfg:backup = ' + str(self.backup) + '][Cisco-IOS-XR-ipv4-pim-cfg:prefix-length = ' + str(self.prefix_length) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.source is not None:
                                return True

                            if self.primary is not None:
                                return True

                            if self.backup is not None:
                                return True

                            if self.prefix_length is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_pim_cfg as meta
                            return meta._meta_table['Pim.Vrfs.Vrf.Ipv4.CsMulticastOnlyFrrs.CsMulticastOnlyFrr']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-pim-cfg:cs-multicast-only-frrs'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.cs_multicast_only_frr is not None:
                            for child_ref in self.cs_multicast_only_frr:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_pim_cfg as meta
                        return meta._meta_table['Pim.Vrfs.Vrf.Ipv4.CsMulticastOnlyFrrs']['meta_info']


                class InheritableDefaults(object):
                    """
                    Inheritable defaults
                    
                    .. attribute:: convergency
                    
                    	Convergency timeout in seconds
                    	**type**\:  int
                    
                    	**range:** 1800..2400
                    
                    	**units**\: second
                    
                    .. attribute:: dr_priority
                    
                    	Hello DR priority, preference given to larger value
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: hello_interval
                    
                    	Hello interval in seconds
                    	**type**\:  int
                    
                    	**range:** 1..3600
                    
                    	**units**\: second
                    
                    .. attribute:: join_prune_mtu
                    
                    	Join\-Prune MTU in Bytes
                    	**type**\:  int
                    
                    	**range:** 576..65535
                    
                    	**units**\: byte
                    
                    .. attribute:: jp_interval
                    
                    	Join\-Prune interval in seconds
                    	**type**\:  int
                    
                    	**range:** 10..600
                    
                    	**units**\: second
                    
                    .. attribute:: override_interval
                    
                    	Override interval in milliseconds
                    	**type**\:  int
                    
                    	**range:** 400..65535
                    
                    	**units**\: millisecond
                    
                    .. attribute:: propagation_delay
                    
                    	Propagation delay in milli seconds
                    	**type**\:  int
                    
                    	**range:** 100..32767
                    
                    	**units**\: millisecond
                    
                    

                    """

                    _prefix = 'ipv4-pim-cfg'
                    _revision = '2016-06-01'

                    def __init__(self):
                        self.parent = None
                        self.convergency = None
                        self.dr_priority = None
                        self.hello_interval = None
                        self.join_prune_mtu = None
                        self.jp_interval = None
                        self.override_interval = None
                        self.propagation_delay = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-pim-cfg:inheritable-defaults'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.convergency is not None:
                            return True

                        if self.dr_priority is not None:
                            return True

                        if self.hello_interval is not None:
                            return True

                        if self.join_prune_mtu is not None:
                            return True

                        if self.jp_interval is not None:
                            return True

                        if self.override_interval is not None:
                            return True

                        if self.propagation_delay is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_pim_cfg as meta
                        return meta._meta_table['Pim.Vrfs.Vrf.Ipv4.InheritableDefaults']['meta_info']


                class Rpf(object):
                    """
                    Configure RPF options
                    
                    .. attribute:: route_policy
                    
                    	Route policy to select RPF topology
                    	**type**\:  str
                    
                    	**length:** 1..64
                    
                    

                    """

                    _prefix = 'ipv4-pim-cfg'
                    _revision = '2016-06-01'

                    def __init__(self):
                        self.parent = None
                        self.route_policy = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-pim-cfg:rpf'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.route_policy is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_pim_cfg as meta
                        return meta._meta_table['Pim.Vrfs.Vrf.Ipv4.Rpf']['meta_info']


                class Maximum(object):
                    """
                    Configure PIM State Limits
                    
                    .. attribute:: bsr_candidate_rp_cache
                    
                    	Override default maximum and threshold for BSR C\-RP cache setting
                    	**type**\:   :py:class:`BsrCandidateRpCache <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.Vrfs.Vrf.Ipv4.Maximum.BsrCandidateRpCache>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: bsr_group_mappings
                    
                    	Override default maximum and threshold for number of group mappings from BSR
                    	**type**\:   :py:class:`BsrGroupMappings <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.Vrfs.Vrf.Ipv4.Maximum.BsrGroupMappings>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: group_mappings_auto_rp
                    
                    	Override default maximum for number of group mappings from autorp mapping agent
                    	**type**\:   :py:class:`GroupMappingsAutoRp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.Vrfs.Vrf.Ipv4.Maximum.GroupMappingsAutoRp>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: register_states
                    
                    	Override default maximum for number of sparse\-mode source registers
                    	**type**\:   :py:class:`RegisterStates <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.Vrfs.Vrf.Ipv4.Maximum.RegisterStates>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: route_interfaces
                    
                    	Override default maximum for number of route\-interfaces
                    	**type**\:   :py:class:`RouteInterfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.Vrfs.Vrf.Ipv4.Maximum.RouteInterfaces>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: routes
                    
                    	Override default maximum for number of routes
                    	**type**\:   :py:class:`Routes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.Vrfs.Vrf.Ipv4.Maximum.Routes>`
                    
                    	**presence node**\: True
                    
                    

                    """

                    _prefix = 'ipv4-pim-cfg'
                    _revision = '2016-06-01'

                    def __init__(self):
                        self.parent = None
                        self.bsr_candidate_rp_cache = None
                        self.bsr_group_mappings = None
                        self.group_mappings_auto_rp = None
                        self.register_states = None
                        self.route_interfaces = None
                        self.routes = None


                    class GroupMappingsAutoRp(object):
                        """
                        Override default maximum for number of group
                        mappings from autorp mapping agent
                        
                        .. attribute:: maximum_group_ranges_auto_rp
                        
                        	Maximum number of PIM group mappings from autorp
                        	**type**\:  int
                        
                        	**range:** 1..10000
                        
                        	**mandatory**\: True
                        
                        .. attribute:: threshold_group_ranges_auto_rp
                        
                        	Warning threshold number of PIM group mappings from autorp
                        	**type**\:  int
                        
                        	**range:** 1..10000
                        
                        	**default value**\: 450
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'ipv4-pim-cfg'
                        _revision = '2016-06-01'

                        def __init__(self):
                            self.parent = None
                            self._is_presence = True
                            self.maximum_group_ranges_auto_rp = None
                            self.threshold_group_ranges_auto_rp = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv4-pim-cfg:group-mappings-auto-rp'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self._is_presence:
                                return True
                            if self.maximum_group_ranges_auto_rp is not None:
                                return True

                            if self.threshold_group_ranges_auto_rp is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_pim_cfg as meta
                            return meta._meta_table['Pim.Vrfs.Vrf.Ipv4.Maximum.GroupMappingsAutoRp']['meta_info']


                    class BsrGroupMappings(object):
                        """
                        Override default maximum and threshold for
                        number of group mappings from BSR
                        
                        .. attribute:: bsr_maximum_group_ranges
                        
                        	Maximum number of PIM group mappings from BSR
                        	**type**\:  int
                        
                        	**range:** 1..10000
                        
                        	**mandatory**\: True
                        
                        .. attribute:: warning_threshold
                        
                        	Set threshold to print warning
                        	**type**\:  int
                        
                        	**range:** 1..10000
                        
                        	**default value**\: 500
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'ipv4-pim-cfg'
                        _revision = '2016-06-01'

                        def __init__(self):
                            self.parent = None
                            self._is_presence = True
                            self.bsr_maximum_group_ranges = None
                            self.warning_threshold = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv4-pim-cfg:bsr-group-mappings'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self._is_presence:
                                return True
                            if self.bsr_maximum_group_ranges is not None:
                                return True

                            if self.warning_threshold is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_pim_cfg as meta
                            return meta._meta_table['Pim.Vrfs.Vrf.Ipv4.Maximum.BsrGroupMappings']['meta_info']


                    class RegisterStates(object):
                        """
                        Override default maximum for number of
                        sparse\-mode source registers
                        
                        .. attribute:: maximum_register_states
                        
                        	Maximum number of PIM Sparse\-Mode register states
                        	**type**\:  int
                        
                        	**range:** 0..75000
                        
                        	**mandatory**\: True
                        
                        .. attribute:: warning_threshold
                        
                        	Set threshold to print warning
                        	**type**\:  int
                        
                        	**range:** 0..75000
                        
                        	**default value**\: 20000
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'ipv4-pim-cfg'
                        _revision = '2016-06-01'

                        def __init__(self):
                            self.parent = None
                            self._is_presence = True
                            self.maximum_register_states = None
                            self.warning_threshold = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv4-pim-cfg:register-states'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self._is_presence:
                                return True
                            if self.maximum_register_states is not None:
                                return True

                            if self.warning_threshold is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_pim_cfg as meta
                            return meta._meta_table['Pim.Vrfs.Vrf.Ipv4.Maximum.RegisterStates']['meta_info']


                    class RouteInterfaces(object):
                        """
                        Override default maximum for number of
                        route\-interfaces
                        
                        .. attribute:: maximum_route_interfaces
                        
                        	Maximum number of PIM route\-interfaces
                        	**type**\:  int
                        
                        	**range:** 1..1100000
                        
                        	**mandatory**\: True
                        
                        .. attribute:: warning_threshold
                        
                        	Set threshold to print warning
                        	**type**\:  int
                        
                        	**range:** 1..1100000
                        
                        	**default value**\: 300000
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'ipv4-pim-cfg'
                        _revision = '2016-06-01'

                        def __init__(self):
                            self.parent = None
                            self._is_presence = True
                            self.maximum_route_interfaces = None
                            self.warning_threshold = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv4-pim-cfg:route-interfaces'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self._is_presence:
                                return True
                            if self.maximum_route_interfaces is not None:
                                return True

                            if self.warning_threshold is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_pim_cfg as meta
                            return meta._meta_table['Pim.Vrfs.Vrf.Ipv4.Maximum.RouteInterfaces']['meta_info']


                    class BsrCandidateRpCache(object):
                        """
                        Override default maximum and threshold for BSR
                        C\-RP cache setting
                        
                        .. attribute:: bsr_maximum_candidate_rp_cache
                        
                        	Maximum number of BSR C\-RP cache setting
                        	**type**\:  int
                        
                        	**range:** 1..10000
                        
                        	**mandatory**\: True
                        
                        .. attribute:: warning_threshold
                        
                        	Set threshold to print warning
                        	**type**\:  int
                        
                        	**range:** 1..10000
                        
                        	**default value**\: 100
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'ipv4-pim-cfg'
                        _revision = '2016-06-01'

                        def __init__(self):
                            self.parent = None
                            self._is_presence = True
                            self.bsr_maximum_candidate_rp_cache = None
                            self.warning_threshold = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv4-pim-cfg:bsr-candidate-rp-cache'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self._is_presence:
                                return True
                            if self.bsr_maximum_candidate_rp_cache is not None:
                                return True

                            if self.warning_threshold is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_pim_cfg as meta
                            return meta._meta_table['Pim.Vrfs.Vrf.Ipv4.Maximum.BsrCandidateRpCache']['meta_info']


                    class Routes(object):
                        """
                        Override default maximum for number of routes
                        
                        .. attribute:: maximum_routes
                        
                        	Maximum number of PIM routes
                        	**type**\:  int
                        
                        	**range:** 1..200000
                        
                        	**mandatory**\: True
                        
                        .. attribute:: warning_threshold
                        
                        	Set threshold to print warning
                        	**type**\:  int
                        
                        	**range:** 1..200000
                        
                        	**default value**\: 100000
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'ipv4-pim-cfg'
                        _revision = '2016-06-01'

                        def __init__(self):
                            self.parent = None
                            self._is_presence = True
                            self.maximum_routes = None
                            self.warning_threshold = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv4-pim-cfg:routes'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self._is_presence:
                                return True
                            if self.maximum_routes is not None:
                                return True

                            if self.warning_threshold is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_pim_cfg as meta
                            return meta._meta_table['Pim.Vrfs.Vrf.Ipv4.Maximum.Routes']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-pim-cfg:maximum'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.bsr_candidate_rp_cache is not None and self.bsr_candidate_rp_cache._has_data():
                            return True

                        if self.bsr_group_mappings is not None and self.bsr_group_mappings._has_data():
                            return True

                        if self.group_mappings_auto_rp is not None and self.group_mappings_auto_rp._has_data():
                            return True

                        if self.register_states is not None and self.register_states._has_data():
                            return True

                        if self.route_interfaces is not None and self.route_interfaces._has_data():
                            return True

                        if self.routes is not None and self.routes._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_pim_cfg as meta
                        return meta._meta_table['Pim.Vrfs.Vrf.Ipv4.Maximum']['meta_info']


                class SgExpiryTimer(object):
                    """
                    Configure expiry timer for S,G routes
                    
                    .. attribute:: access_list_name
                    
                    	Access\-list of applicable S,G routes
                    	**type**\:  str
                    
                    	**length:** 1..64
                    
                    .. attribute:: interval
                    
                    	(S,G) expiry time in seconds
                    	**type**\:  int
                    
                    	**range:** 40..57600
                    
                    	**units**\: second
                    
                    

                    """

                    _prefix = 'ipv4-pim-cfg'
                    _revision = '2016-06-01'

                    def __init__(self):
                        self.parent = None
                        self.access_list_name = None
                        self.interval = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-pim-cfg:sg-expiry-timer'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.access_list_name is not None:
                            return True

                        if self.interval is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_pim_cfg as meta
                        return meta._meta_table['Pim.Vrfs.Vrf.Ipv4.SgExpiryTimer']['meta_info']


                class RpfVectorEnable(object):
                    """
                    Enable PIM RPF Vector Proxy's
                    
                    .. attribute:: allow_ebgp
                    
                    	Allow RPF Vector origination over eBGP sessions
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: disable_ibgp
                    
                    	Disable RPF Vector origination over iBGP sessions
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: enable
                    
                    	RPF Vector is turned on if configured
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    	**mandatory**\: True
                    
                    .. attribute:: _is_presence
                    
                    	Is present if this instance represents presence container else not
                    	**type**\: bool
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'ipv4-pim-cfg'
                    _revision = '2016-06-01'

                    def __init__(self):
                        self.parent = None
                        self._is_presence = True
                        self.allow_ebgp = None
                        self.disable_ibgp = None
                        self.enable = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-pim-cfg:rpf-vector-enable'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self._is_presence:
                            return True
                        if self.allow_ebgp is not None:
                            return True

                        if self.disable_ibgp is not None:
                            return True

                        if self.enable is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_pim_cfg as meta
                        return meta._meta_table['Pim.Vrfs.Vrf.Ipv4.RpfVectorEnable']['meta_info']


                class Ssm(object):
                    """
                    Configure IP Multicast SSM
                    
                    .. attribute:: disable
                    
                    	TRUE if SSM is disabled on this router
                    	**type**\:  bool
                    
                    	**default value**\: false
                    
                    .. attribute:: range
                    
                    	Access list of groups enabled with SSM
                    	**type**\:  str
                    
                    	**length:** 1..64
                    
                    

                    """

                    _prefix = 'ipv4-pim-cfg'
                    _revision = '2016-06-01'

                    def __init__(self):
                        self.parent = None
                        self.disable = None
                        self.range = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-pim-cfg:ssm'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.disable is not None:
                            return True

                        if self.range is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_pim_cfg as meta
                        return meta._meta_table['Pim.Vrfs.Vrf.Ipv4.Ssm']['meta_info']


                class Injects(object):
                    """
                    Inject Explicit PIM RPF Vector Proxy's
                    
                    .. attribute:: inject
                    
                    	Inject Explicit PIM RPF Vector Proxy's
                    	**type**\: list of    :py:class:`Inject <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.Vrfs.Vrf.Ipv4.Injects.Inject>`
                    
                    

                    """

                    _prefix = 'ipv4-pim-cfg'
                    _revision = '2016-06-01'

                    def __init__(self):
                        self.parent = None
                        self.inject = YList()
                        self.inject.parent = self
                        self.inject.name = 'inject'


                    class Inject(object):
                        """
                        Inject Explicit PIM RPF Vector Proxy's
                        
                        .. attribute:: source_address  <key>
                        
                        	Source Address
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: prefix_length  <key>
                        
                        	Masklen
                        	**type**\:  int
                        
                        	**range:** 0..32
                        
                        .. attribute:: rpf_proxy_address
                        
                        	RPF Proxy Address
                        	**type**\:  list of str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        

                        """

                        _prefix = 'ipv4-pim-cfg'
                        _revision = '2016-06-01'

                        def __init__(self):
                            self.parent = None
                            self.source_address = None
                            self.prefix_length = None
                            self.rpf_proxy_address = YLeafList()
                            self.rpf_proxy_address.parent = self
                            self.rpf_proxy_address.name = 'rpf_proxy_address'

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.source_address is None:
                                raise YPYModelError('Key property source_address is None')
                            if self.prefix_length is None:
                                raise YPYModelError('Key property prefix_length is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv4-pim-cfg:inject[Cisco-IOS-XR-ipv4-pim-cfg:source-address = ' + str(self.source_address) + '][Cisco-IOS-XR-ipv4-pim-cfg:prefix-length = ' + str(self.prefix_length) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.source_address is not None:
                                return True

                            if self.prefix_length is not None:
                                return True

                            if self.rpf_proxy_address is not None:
                                for child in self.rpf_proxy_address:
                                    if child is not None:
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_pim_cfg as meta
                            return meta._meta_table['Pim.Vrfs.Vrf.Ipv4.Injects.Inject']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-pim-cfg:injects'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.inject is not None:
                            for child_ref in self.inject:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_pim_cfg as meta
                        return meta._meta_table['Pim.Vrfs.Vrf.Ipv4.Injects']['meta_info']


                class BidirRpAddresses(object):
                    """
                    Configure Bidirectional PIM Rendezvous Point
                    
                    .. attribute:: bidir_rp_address
                    
                    	Address of the Rendezvous Point
                    	**type**\: list of    :py:class:`BidirRpAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.Vrfs.Vrf.Ipv4.BidirRpAddresses.BidirRpAddress>`
                    
                    

                    """

                    _prefix = 'ipv4-pim-cfg'
                    _revision = '2016-06-01'

                    def __init__(self):
                        self.parent = None
                        self.bidir_rp_address = YList()
                        self.bidir_rp_address.parent = self
                        self.bidir_rp_address.name = 'bidir_rp_address'


                    class BidirRpAddress(object):
                        """
                        Address of the Rendezvous Point
                        
                        .. attribute:: rp_address  <key>
                        
                        	RP address of Rendezvous Point
                        	**type**\: one of the below types:
                        
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        .. attribute:: access_list_name
                        
                        	Access list of groups that should map to a given RP
                        	**type**\:  str
                        
                        	**length:** 1..64
                        
                        .. attribute:: auto_rp_override
                        
                        	TRUE Indicates if static RP config overrides AutoRP and BSR
                        	**type**\:  bool
                        
                        

                        """

                        _prefix = 'ipv4-pim-cfg'
                        _revision = '2016-06-01'

                        def __init__(self):
                            self.parent = None
                            self.rp_address = None
                            self.access_list_name = None
                            self.auto_rp_override = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.rp_address is None:
                                raise YPYModelError('Key property rp_address is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv4-pim-cfg:bidir-rp-address[Cisco-IOS-XR-ipv4-pim-cfg:rp-address = ' + str(self.rp_address) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.rp_address is not None:
                                return True

                            if self.access_list_name is not None:
                                return True

                            if self.auto_rp_override is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_pim_cfg as meta
                            return meta._meta_table['Pim.Vrfs.Vrf.Ipv4.BidirRpAddresses.BidirRpAddress']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-pim-cfg:bidir-rp-addresses'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.bidir_rp_address is not None:
                            for child_ref in self.bidir_rp_address:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_pim_cfg as meta
                        return meta._meta_table['Pim.Vrfs.Vrf.Ipv4.BidirRpAddresses']['meta_info']


                class Bsr(object):
                    """
                    PIM BSR configuration
                    
                    .. attribute:: candidate_bsr
                    
                    	PIM Candidate BSR configuration
                    	**type**\:   :py:class:`CandidateBsr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.Vrfs.Vrf.Ipv4.Bsr.CandidateBsr>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: candidate_rps
                    
                    	PIM RP configuration
                    	**type**\:   :py:class:`CandidateRps <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.Vrfs.Vrf.Ipv4.Bsr.CandidateRps>`
                    
                    

                    """

                    _prefix = 'ipv4-pim-cfg'
                    _revision = '2016-06-01'

                    def __init__(self):
                        self.parent = None
                        self.candidate_bsr = None
                        self.candidate_rps = Pim.Vrfs.Vrf.Ipv4.Bsr.CandidateRps()
                        self.candidate_rps.parent = self


                    class CandidateBsr(object):
                        """
                        PIM Candidate BSR configuration
                        
                        .. attribute:: address
                        
                        	BSR Address configured
                        	**type**\: one of the below types:
                        
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        	**mandatory**\: True
                        
                        
                        ----
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        	**mandatory**\: True
                        
                        
                        ----
                        .. attribute:: prefix_length
                        
                        	Hash Mask Length for this candidate BSR
                        	**type**\:  int
                        
                        	**range:** 0..32
                        
                        	**default value**\: 30
                        
                        .. attribute:: priority
                        
                        	Priority of the Candidate BSR
                        	**type**\:  int
                        
                        	**range:** 1..255
                        
                        	**default value**\: 1
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'ipv4-pim-cfg'
                        _revision = '2016-06-01'

                        def __init__(self):
                            self.parent = None
                            self._is_presence = True
                            self.address = None
                            self.prefix_length = None
                            self.priority = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv4-pim-cfg:candidate-bsr'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self._is_presence:
                                return True
                            if self.address is not None:
                                return True

                            if self.prefix_length is not None:
                                return True

                            if self.priority is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_pim_cfg as meta
                            return meta._meta_table['Pim.Vrfs.Vrf.Ipv4.Bsr.CandidateBsr']['meta_info']


                    class CandidateRps(object):
                        """
                        PIM RP configuration
                        
                        .. attribute:: candidate_rp
                        
                        	Address of PIM SM BSR Candidate\-RP
                        	**type**\: list of    :py:class:`CandidateRp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.Vrfs.Vrf.Ipv4.Bsr.CandidateRps.CandidateRp>`
                        
                        

                        """

                        _prefix = 'ipv4-pim-cfg'
                        _revision = '2016-06-01'

                        def __init__(self):
                            self.parent = None
                            self.candidate_rp = YList()
                            self.candidate_rp.parent = self
                            self.candidate_rp.name = 'candidate_rp'


                        class CandidateRp(object):
                            """
                            Address of PIM SM BSR Candidate\-RP
                            
                            .. attribute:: address  <key>
                            
                            	Address of Candidate\-RP
                            	**type**\: one of the below types:
                            
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            .. attribute:: mode  <key>
                            
                            	SM or Bidir
                            	**type**\:   :py:class:`PimProtocolModeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.PimProtocolModeEnum>`
                            
                            .. attribute:: group_list
                            
                            	Access\-list specifying the group range for the Candidate\-RP
                            	**type**\:  str
                            
                            	**length:** 1..64
                            
                            .. attribute:: interval
                            
                            	Advertisement interval
                            	**type**\:  int
                            
                            	**range:** 30..600
                            
                            	**default value**\: 60
                            
                            .. attribute:: priority
                            
                            	Priority of the CRP
                            	**type**\:  int
                            
                            	**range:** 1..255
                            
                            	**default value**\: 192
                            
                            

                            """

                            _prefix = 'ipv4-pim-cfg'
                            _revision = '2016-06-01'

                            def __init__(self):
                                self.parent = None
                                self.address = None
                                self.mode = None
                                self.group_list = None
                                self.interval = None
                                self.priority = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                if self.address is None:
                                    raise YPYModelError('Key property address is None')
                                if self.mode is None:
                                    raise YPYModelError('Key property mode is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-ipv4-pim-cfg:candidate-rp[Cisco-IOS-XR-ipv4-pim-cfg:address = ' + str(self.address) + '][Cisco-IOS-XR-ipv4-pim-cfg:mode = ' + str(self.mode) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.address is not None:
                                    return True

                                if self.mode is not None:
                                    return True

                                if self.group_list is not None:
                                    return True

                                if self.interval is not None:
                                    return True

                                if self.priority is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_pim_cfg as meta
                                return meta._meta_table['Pim.Vrfs.Vrf.Ipv4.Bsr.CandidateRps.CandidateRp']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv4-pim-cfg:candidate-rps'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.candidate_rp is not None:
                                for child_ref in self.candidate_rp:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_pim_cfg as meta
                            return meta._meta_table['Pim.Vrfs.Vrf.Ipv4.Bsr.CandidateRps']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-pim-cfg:bsr'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.candidate_bsr is not None and self.candidate_bsr._has_data():
                            return True

                        if self.candidate_rps is not None and self.candidate_rps._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_pim_cfg as meta
                        return meta._meta_table['Pim.Vrfs.Vrf.Ipv4.Bsr']['meta_info']


                class Paths(object):
                    """
                    Inject PIM RPF Vector Proxy's
                    
                    .. attribute:: path
                    
                    	Inject PIM RPF Vector Proxy's
                    	**type**\: list of    :py:class:`Path <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.Vrfs.Vrf.Ipv4.Paths.Path>`
                    
                    

                    """

                    _prefix = 'ipv4-pim-cfg'
                    _revision = '2016-06-01'

                    def __init__(self):
                        self.parent = None
                        self.path = YList()
                        self.path.parent = self
                        self.path.name = 'path'


                    class Path(object):
                        """
                        Inject PIM RPF Vector Proxy's
                        
                        .. attribute:: source_address  <key>
                        
                        	Source Address
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: prefix_length  <key>
                        
                        	Masklen
                        	**type**\:  int
                        
                        	**range:** 0..32
                        
                        .. attribute:: rpf_proxy_address
                        
                        	RPF Proxy Address
                        	**type**\:  list of str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        

                        """

                        _prefix = 'ipv4-pim-cfg'
                        _revision = '2016-06-01'

                        def __init__(self):
                            self.parent = None
                            self.source_address = None
                            self.prefix_length = None
                            self.rpf_proxy_address = YLeafList()
                            self.rpf_proxy_address.parent = self
                            self.rpf_proxy_address.name = 'rpf_proxy_address'

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.source_address is None:
                                raise YPYModelError('Key property source_address is None')
                            if self.prefix_length is None:
                                raise YPYModelError('Key property prefix_length is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv4-pim-cfg:path[Cisco-IOS-XR-ipv4-pim-cfg:source-address = ' + str(self.source_address) + '][Cisco-IOS-XR-ipv4-pim-cfg:prefix-length = ' + str(self.prefix_length) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.source_address is not None:
                                return True

                            if self.prefix_length is not None:
                                return True

                            if self.rpf_proxy_address is not None:
                                for child in self.rpf_proxy_address:
                                    if child is not None:
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_pim_cfg as meta
                            return meta._meta_table['Pim.Vrfs.Vrf.Ipv4.Paths.Path']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-pim-cfg:paths'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.path is not None:
                            for child_ref in self.path:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_pim_cfg as meta
                        return meta._meta_table['Pim.Vrfs.Vrf.Ipv4.Paths']['meta_info']


                class AllowRp(object):
                    """
                    Enable allow\-rp filtering for SM joins
                    
                    .. attribute:: group_list_name
                    
                    	Access\-list specifiying applicable groups
                    	**type**\:  str
                    
                    	**length:** 1..64
                    
                    .. attribute:: rp_list_name
                    
                    	Access\-list specifiying applicable RPs
                    	**type**\:  str
                    
                    	**length:** 1..64
                    
                    .. attribute:: _is_presence
                    
                    	Is present if this instance represents presence container else not
                    	**type**\: bool
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'ipv4-pim-cfg'
                    _revision = '2016-06-01'

                    def __init__(self):
                        self.parent = None
                        self._is_presence = True
                        self.group_list_name = None
                        self.rp_list_name = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-pim-cfg:allow-rp'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self._is_presence:
                            return True
                        if self.group_list_name is not None:
                            return True

                        if self.rp_list_name is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_pim_cfg as meta
                        return meta._meta_table['Pim.Vrfs.Vrf.Ipv4.AllowRp']['meta_info']


                class Convergence(object):
                    """
                    Configure convergence parameters
                    
                    .. attribute:: link_down_prune_delay
                    
                    	Delay prunes if route join state transitions to not\-joined on link down
                    	**type**\:  int
                    
                    	**range:** 0..60
                    
                    	**units**\: second
                    
                    .. attribute:: rpf_conflict_join_delay
                    
                    	Dampen first join if RPF path is through one of the downstream neighbor
                    	**type**\:  int
                    
                    	**range:** 0..15
                    
                    	**units**\: second
                    
                    

                    """

                    _prefix = 'ipv4-pim-cfg'
                    _revision = '2016-06-01'

                    def __init__(self):
                        self.parent = None
                        self.link_down_prune_delay = None
                        self.rpf_conflict_join_delay = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-pim-cfg:convergence'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.link_down_prune_delay is not None:
                            return True

                        if self.rpf_conflict_join_delay is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_pim_cfg as meta
                        return meta._meta_table['Pim.Vrfs.Vrf.Ipv4.Convergence']['meta_info']


                class Interfaces(object):
                    """
                    Interface\-level Configuration
                    
                    .. attribute:: interface
                    
                    	The name of the interface
                    	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.Vrfs.Vrf.Ipv4.Interfaces.Interface>`
                    
                    

                    """

                    _prefix = 'ipv4-pim-cfg'
                    _revision = '2016-06-01'

                    def __init__(self):
                        self.parent = None
                        self.interface = YList()
                        self.interface.parent = self
                        self.interface.name = 'interface'


                    class Interface(object):
                        """
                        The name of the interface
                        
                        .. attribute:: interface_name  <key>
                        
                        	The name of interface
                        	**type**\:  str
                        
                        	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                        
                        .. attribute:: bfd
                        
                        	BFD configuration
                        	**type**\:   :py:class:`Bfd <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.Vrfs.Vrf.Ipv4.Interfaces.Interface.Bfd>`
                        
                        .. attribute:: bsr_border
                        
                        	BSR Border configuration for Interface
                        	**type**\:  bool
                        
                        .. attribute:: dr_priority
                        
                        	Hello DR priority, preference given to larger value
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: enable
                        
                        	Enter PIM Interface processing
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: hello_interval
                        
                        	Hello interval in seconds
                        	**type**\:  int
                        
                        	**range:** 1..3600
                        
                        	**units**\: second
                        
                        .. attribute:: interface_enable
                        
                        	Enable PIM processing on the interface
                        	**type**\:  bool
                        
                        .. attribute:: join_prune_mtu
                        
                        	Join\-Prune MTU in Bytes
                        	**type**\:  int
                        
                        	**range:** 576..65535
                        
                        	**units**\: byte
                        
                        .. attribute:: jp_interval
                        
                        	Join\-Prune interval in seconds
                        	**type**\:  int
                        
                        	**range:** 10..600
                        
                        	**units**\: second
                        
                        .. attribute:: maximum_routes
                        
                        	Maximum number of allowed routes for this interface
                        	**type**\:   :py:class:`MaximumRoutes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.Vrfs.Vrf.Ipv4.Interfaces.Interface.MaximumRoutes>`
                        
                        	**presence node**\: True
                        
                        .. attribute:: neighbor_filter
                        
                        	Access\-list of neighbors to be filtered
                        	**type**\:  str
                        
                        	**length:** 1..64
                        
                        .. attribute:: override_interval
                        
                        	Override interval in milliseconds
                        	**type**\:  int
                        
                        	**range:** 400..65535
                        
                        	**units**\: millisecond
                        
                        .. attribute:: propagation_delay
                        
                        	Propagation delay in milli seconds
                        	**type**\:  int
                        
                        	**range:** 100..32767
                        
                        	**units**\: millisecond
                        
                        

                        """

                        _prefix = 'ipv4-pim-cfg'
                        _revision = '2016-06-01'

                        def __init__(self):
                            self.parent = None
                            self.interface_name = None
                            self.bfd = Pim.Vrfs.Vrf.Ipv4.Interfaces.Interface.Bfd()
                            self.bfd.parent = self
                            self.bsr_border = None
                            self.dr_priority = None
                            self.enable = None
                            self.hello_interval = None
                            self.interface_enable = None
                            self.join_prune_mtu = None
                            self.jp_interval = None
                            self.maximum_routes = None
                            self.neighbor_filter = None
                            self.override_interval = None
                            self.propagation_delay = None


                        class MaximumRoutes(object):
                            """
                            Maximum number of allowed routes for this
                            interface
                            
                            .. attribute:: access_list_name
                            
                            	Access\-list to account for
                            	**type**\:  str
                            
                            	**length:** 1..64
                            
                            .. attribute:: maximum
                            
                            	Maximum number of routes for this interface
                            	**type**\:  int
                            
                            	**range:** 1..1100000
                            
                            	**mandatory**\: True
                            
                            .. attribute:: warning_threshold
                            
                            	Set threshold to print warning
                            	**type**\:  int
                            
                            	**range:** 1..1100000
                            
                            .. attribute:: _is_presence
                            
                            	Is present if this instance represents presence container else not
                            	**type**\: bool
                            
                            

                            This class is a :ref:`presence class<presence-class>`

                            """

                            _prefix = 'ipv4-pim-cfg'
                            _revision = '2016-06-01'

                            def __init__(self):
                                self.parent = None
                                self._is_presence = True
                                self.access_list_name = None
                                self.maximum = None
                                self.warning_threshold = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ipv4-pim-cfg:maximum-routes'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self._is_presence:
                                    return True
                                if self.access_list_name is not None:
                                    return True

                                if self.maximum is not None:
                                    return True

                                if self.warning_threshold is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_pim_cfg as meta
                                return meta._meta_table['Pim.Vrfs.Vrf.Ipv4.Interfaces.Interface.MaximumRoutes']['meta_info']


                        class Bfd(object):
                            """
                            BFD configuration
                            
                            .. attribute:: detection_multiplier
                            
                            	Detection multiplier for BFD sessions created by PIM
                            	**type**\:  int
                            
                            	**range:** 2..50
                            
                            .. attribute:: enable
                            
                            	TRUE to enable BFD. FALSE to disable and to prevent inheritance from a parent
                            	**type**\:  bool
                            
                            .. attribute:: interval
                            
                            	Hello interval for BFD sessions created by PIM
                            	**type**\:  int
                            
                            	**range:** 3..30000
                            
                            	**units**\: millisecond
                            
                            

                            """

                            _prefix = 'ipv4-pim-cfg'
                            _revision = '2016-06-01'

                            def __init__(self):
                                self.parent = None
                                self.detection_multiplier = None
                                self.enable = None
                                self.interval = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ipv4-pim-cfg:bfd'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.detection_multiplier is not None:
                                    return True

                                if self.enable is not None:
                                    return True

                                if self.interval is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_pim_cfg as meta
                                return meta._meta_table['Pim.Vrfs.Vrf.Ipv4.Interfaces.Interface.Bfd']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.interface_name is None:
                                raise YPYModelError('Key property interface_name is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv4-pim-cfg:interface[Cisco-IOS-XR-ipv4-pim-cfg:interface-name = ' + str(self.interface_name) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.interface_name is not None:
                                return True

                            if self.bfd is not None and self.bfd._has_data():
                                return True

                            if self.bsr_border is not None:
                                return True

                            if self.dr_priority is not None:
                                return True

                            if self.enable is not None:
                                return True

                            if self.hello_interval is not None:
                                return True

                            if self.interface_enable is not None:
                                return True

                            if self.join_prune_mtu is not None:
                                return True

                            if self.jp_interval is not None:
                                return True

                            if self.maximum_routes is not None and self.maximum_routes._has_data():
                                return True

                            if self.neighbor_filter is not None:
                                return True

                            if self.override_interval is not None:
                                return True

                            if self.propagation_delay is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_pim_cfg as meta
                            return meta._meta_table['Pim.Vrfs.Vrf.Ipv4.Interfaces.Interface']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-pim-cfg:interfaces'

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
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_pim_cfg as meta
                        return meta._meta_table['Pim.Vrfs.Vrf.Ipv4.Interfaces']['meta_info']


                class CjMulticastOnlyFrrs(object):
                    """
                    Clone Join Multicast Only FRR
                    
                    .. attribute:: cj_multicast_only_frr
                    
                    	Clone Join Multicast Only FRR
                    	**type**\: list of    :py:class:`CjMulticastOnlyFrr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.Vrfs.Vrf.Ipv4.CjMulticastOnlyFrrs.CjMulticastOnlyFrr>`
                    
                    

                    """

                    _prefix = 'ipv4-pim-cfg'
                    _revision = '2016-06-01'

                    def __init__(self):
                        self.parent = None
                        self.cj_multicast_only_frr = YList()
                        self.cj_multicast_only_frr.parent = self
                        self.cj_multicast_only_frr.name = 'cj_multicast_only_frr'


                    class CjMulticastOnlyFrr(object):
                        """
                        Clone Join Multicast Only FRR
                        
                        .. attribute:: source  <key>
                        
                        	Original address
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: primary  <key>
                        
                        	Primary address
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: backup  <key>
                        
                        	Backup address
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: prefix_length  <key>
                        
                        	Masklen
                        	**type**\:  int
                        
                        	**range:** 0..32
                        
                        

                        """

                        _prefix = 'ipv4-pim-cfg'
                        _revision = '2016-06-01'

                        def __init__(self):
                            self.parent = None
                            self.source = None
                            self.primary = None
                            self.backup = None
                            self.prefix_length = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.source is None:
                                raise YPYModelError('Key property source is None')
                            if self.primary is None:
                                raise YPYModelError('Key property primary is None')
                            if self.backup is None:
                                raise YPYModelError('Key property backup is None')
                            if self.prefix_length is None:
                                raise YPYModelError('Key property prefix_length is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv4-pim-cfg:cj-multicast-only-frr[Cisco-IOS-XR-ipv4-pim-cfg:source = ' + str(self.source) + '][Cisco-IOS-XR-ipv4-pim-cfg:primary = ' + str(self.primary) + '][Cisco-IOS-XR-ipv4-pim-cfg:backup = ' + str(self.backup) + '][Cisco-IOS-XR-ipv4-pim-cfg:prefix-length = ' + str(self.prefix_length) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.source is not None:
                                return True

                            if self.primary is not None:
                                return True

                            if self.backup is not None:
                                return True

                            if self.prefix_length is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_pim_cfg as meta
                            return meta._meta_table['Pim.Vrfs.Vrf.Ipv4.CjMulticastOnlyFrrs.CjMulticastOnlyFrr']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-pim-cfg:cj-multicast-only-frrs'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.cj_multicast_only_frr is not None:
                            for child_ref in self.cj_multicast_only_frr:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_pim_cfg as meta
                        return meta._meta_table['Pim.Vrfs.Vrf.Ipv4.CjMulticastOnlyFrrs']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-pim-cfg:ipv4'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.accept_register is not None:
                        return True

                    if self.allow_rp is not None and self.allow_rp._has_data():
                        return True

                    if self.auto_rp_disable is not None:
                        return True

                    if self.bidir_rp_addresses is not None and self.bidir_rp_addresses._has_data():
                        return True

                    if self.bsr is not None and self.bsr._has_data():
                        return True

                    if self.cj_multicast_only_frrs is not None and self.cj_multicast_only_frrs._has_data():
                        return True

                    if self.convergence is not None and self.convergence._has_data():
                        return True

                    if self.cs_multicast_only_frrs is not None and self.cs_multicast_only_frrs._has_data():
                        return True

                    if self.inheritable_defaults is not None and self.inheritable_defaults._has_data():
                        return True

                    if self.injects is not None and self.injects._has_data():
                        return True

                    if self.interfaces is not None and self.interfaces._has_data():
                        return True

                    if self.log_neighbor_changes is not None:
                        return True

                    if self.maximum is not None and self.maximum._has_data():
                        return True

                    if self.multicast_only_frr is not None and self.multicast_only_frr._has_data():
                        return True

                    if self.multipath is not None:
                        return True

                    if self.neighbor_check_on_receive is not None:
                        return True

                    if self.neighbor_check_on_send is not None:
                        return True

                    if self.neighbor_filter is not None:
                        return True

                    if self.old_register_checksum is not None:
                        return True

                    if self.paths is not None and self.paths._has_data():
                        return True

                    if self.register_source is not None:
                        return True

                    if self.rp_static_deny is not None:
                        return True

                    if self.rpf is not None and self.rpf._has_data():
                        return True

                    if self.rpf_vector_enable is not None and self.rpf_vector_enable._has_data():
                        return True

                    if self.sg_expiry_timer is not None and self.sg_expiry_timer._has_data():
                        return True

                    if self.sparse_mode_rp_addresses is not None and self.sparse_mode_rp_addresses._has_data():
                        return True

                    if self.spt_threshold_infinity is not None:
                        return True

                    if self.ssm is not None and self.ssm._has_data():
                        return True

                    if self.ssm_allow_override is not None:
                        return True

                    if self.suppress_data_registers is not None:
                        return True

                    if self.suppress_rpf_prunes is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_pim_cfg as meta
                    return meta._meta_table['Pim.Vrfs.Vrf.Ipv4']['meta_info']


            class Ipv6(object):
                """
                IPV6 commands
                
                .. attribute:: accept_register
                
                	Access\-list which specifies unauthorized sources
                	**type**\:  str
                
                	**length:** 1..64
                
                .. attribute:: allow_rp
                
                	Enable allow\-rp filtering for SM joins
                	**type**\:   :py:class:`AllowRp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.Vrfs.Vrf.Ipv6.AllowRp>`
                
                	**presence node**\: True
                
                .. attribute:: bidir_rp_addresses
                
                	Configure Bidirectional PIM Rendezvous Point
                	**type**\:   :py:class:`BidirRpAddresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.Vrfs.Vrf.Ipv6.BidirRpAddresses>`
                
                .. attribute:: bsr
                
                	PIM BSR configuration
                	**type**\:   :py:class:`Bsr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.Vrfs.Vrf.Ipv6.Bsr>`
                
                .. attribute:: convergence
                
                	Configure convergence parameters
                	**type**\:   :py:class:`Convergence <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.Vrfs.Vrf.Ipv6.Convergence>`
                
                .. attribute:: embedded_rp_addresses
                
                	Set Embedded RP processing support
                	**type**\:   :py:class:`EmbeddedRpAddresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.Vrfs.Vrf.Ipv6.EmbeddedRpAddresses>`
                
                .. attribute:: embedded_rp_disable
                
                	Set Embedded RP processing support
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: inheritable_defaults
                
                	Inheritable defaults
                	**type**\:   :py:class:`InheritableDefaults <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.Vrfs.Vrf.Ipv6.InheritableDefaults>`
                
                .. attribute:: interfaces
                
                	Interface\-level Configuration
                	**type**\:   :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.Vrfs.Vrf.Ipv6.Interfaces>`
                
                .. attribute:: log_neighbor_changes
                
                	PIM neighbor state change logging is turned on if configured
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: maximum
                
                	Configure PIM State Limits
                	**type**\:   :py:class:`Maximum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.Vrfs.Vrf.Ipv6.Maximum>`
                
                .. attribute:: multipath
                
                	Enable equal\-cost multipath routing
                	**type**\:   :py:class:`PimMultipathEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.PimMultipathEnum>`
                
                .. attribute:: neighbor_check_on_receive
                
                	Enable PIM neighbor checking when receiving PIM messages
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: neighbor_check_on_send
                
                	Enable PIM neighbor checking when sending join\-prunes
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: neighbor_filter
                
                	Access\-list of neighbors to be filtered
                	**type**\:  str
                
                	**length:** 1..64
                
                .. attribute:: old_register_checksum
                
                	Generate registers compatible with older IOS versions
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: register_source
                
                	Source address to use for register messages
                	**type**\:  str
                
                	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                
                .. attribute:: rp_static_deny
                
                	Configure static RP deny range
                	**type**\:  str
                
                	**length:** 1..64
                
                .. attribute:: rpf
                
                	Configure RPF options
                	**type**\:   :py:class:`Rpf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.Vrfs.Vrf.Ipv6.Rpf>`
                
                .. attribute:: rpf_vector_enable
                
                	Enable PIM RPF Vector Proxy's
                	**type**\:   :py:class:`RpfVectorEnable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.Vrfs.Vrf.Ipv6.RpfVectorEnable>`
                
                	**presence node**\: True
                
                .. attribute:: sg_expiry_timer
                
                	Configure expiry timer for S,G routes
                	**type**\:   :py:class:`SgExpiryTimer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.Vrfs.Vrf.Ipv6.SgExpiryTimer>`
                
                .. attribute:: sparse_mode_rp_addresses
                
                	Configure Sparse\-Mode Rendezvous Point
                	**type**\:   :py:class:`SparseModeRpAddresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.Vrfs.Vrf.Ipv6.SparseModeRpAddresses>`
                
                .. attribute:: spt_threshold_infinity
                
                	Configure threshold of infinity for switching to SPT on last\-hop
                	**type**\:  str
                
                .. attribute:: ssm
                
                	Configure IP Multicast SSM
                	**type**\:   :py:class:`Ssm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.Vrfs.Vrf.Ipv6.Ssm>`
                
                .. attribute:: ssm_allow_override
                
                	Allow SSM ranges to be overridden by more specific ranges
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: suppress_data_registers
                
                	Suppress data registers after initial state setup
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: suppress_rpf_prunes
                
                	Suppress prunes triggered as a result of RPF changes
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                

                """

                _prefix = 'ipv4-pim-cfg'
                _revision = '2016-06-01'

                def __init__(self):
                    self.parent = None
                    self.accept_register = None
                    self.allow_rp = None
                    self.bidir_rp_addresses = Pim.Vrfs.Vrf.Ipv6.BidirRpAddresses()
                    self.bidir_rp_addresses.parent = self
                    self.bsr = Pim.Vrfs.Vrf.Ipv6.Bsr()
                    self.bsr.parent = self
                    self.convergence = Pim.Vrfs.Vrf.Ipv6.Convergence()
                    self.convergence.parent = self
                    self.embedded_rp_addresses = Pim.Vrfs.Vrf.Ipv6.EmbeddedRpAddresses()
                    self.embedded_rp_addresses.parent = self
                    self.embedded_rp_disable = None
                    self.inheritable_defaults = Pim.Vrfs.Vrf.Ipv6.InheritableDefaults()
                    self.inheritable_defaults.parent = self
                    self.interfaces = Pim.Vrfs.Vrf.Ipv6.Interfaces()
                    self.interfaces.parent = self
                    self.log_neighbor_changes = None
                    self.maximum = Pim.Vrfs.Vrf.Ipv6.Maximum()
                    self.maximum.parent = self
                    self.multipath = None
                    self.neighbor_check_on_receive = None
                    self.neighbor_check_on_send = None
                    self.neighbor_filter = None
                    self.old_register_checksum = None
                    self.register_source = None
                    self.rp_static_deny = None
                    self.rpf = Pim.Vrfs.Vrf.Ipv6.Rpf()
                    self.rpf.parent = self
                    self.rpf_vector_enable = None
                    self.sg_expiry_timer = Pim.Vrfs.Vrf.Ipv6.SgExpiryTimer()
                    self.sg_expiry_timer.parent = self
                    self.sparse_mode_rp_addresses = Pim.Vrfs.Vrf.Ipv6.SparseModeRpAddresses()
                    self.sparse_mode_rp_addresses.parent = self
                    self.spt_threshold_infinity = None
                    self.ssm = Pim.Vrfs.Vrf.Ipv6.Ssm()
                    self.ssm.parent = self
                    self.ssm_allow_override = None
                    self.suppress_data_registers = None
                    self.suppress_rpf_prunes = None


                class SparseModeRpAddresses(object):
                    """
                    Configure Sparse\-Mode Rendezvous Point
                    
                    .. attribute:: sparse_mode_rp_address
                    
                    	Address of the Rendezvous Point
                    	**type**\: list of    :py:class:`SparseModeRpAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.Vrfs.Vrf.Ipv6.SparseModeRpAddresses.SparseModeRpAddress>`
                    
                    

                    """

                    _prefix = 'ipv4-pim-cfg'
                    _revision = '2016-06-01'

                    def __init__(self):
                        self.parent = None
                        self.sparse_mode_rp_address = YList()
                        self.sparse_mode_rp_address.parent = self
                        self.sparse_mode_rp_address.name = 'sparse_mode_rp_address'


                    class SparseModeRpAddress(object):
                        """
                        Address of the Rendezvous Point
                        
                        .. attribute:: rp_address  <key>
                        
                        	RP address of Rendezvous Point
                        	**type**\: one of the below types:
                        
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        .. attribute:: access_list_name
                        
                        	Access list of groups that should map to a  given RP
                        	**type**\:  str
                        
                        	**length:** 1..64
                        
                        .. attribute:: auto_rp_override
                        
                        	TRUE Indicates if static RP config overrides AutoRP and BSR
                        	**type**\:  bool
                        
                        

                        """

                        _prefix = 'ipv4-pim-cfg'
                        _revision = '2016-06-01'

                        def __init__(self):
                            self.parent = None
                            self.rp_address = None
                            self.access_list_name = None
                            self.auto_rp_override = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.rp_address is None:
                                raise YPYModelError('Key property rp_address is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv4-pim-cfg:sparse-mode-rp-address[Cisco-IOS-XR-ipv4-pim-cfg:rp-address = ' + str(self.rp_address) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.rp_address is not None:
                                return True

                            if self.access_list_name is not None:
                                return True

                            if self.auto_rp_override is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_pim_cfg as meta
                            return meta._meta_table['Pim.Vrfs.Vrf.Ipv6.SparseModeRpAddresses.SparseModeRpAddress']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-pim-cfg:sparse-mode-rp-addresses'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.sparse_mode_rp_address is not None:
                            for child_ref in self.sparse_mode_rp_address:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_pim_cfg as meta
                        return meta._meta_table['Pim.Vrfs.Vrf.Ipv6.SparseModeRpAddresses']['meta_info']


                class InheritableDefaults(object):
                    """
                    Inheritable defaults
                    
                    .. attribute:: convergency
                    
                    	Convergency timeout in seconds
                    	**type**\:  int
                    
                    	**range:** 1800..2400
                    
                    	**units**\: second
                    
                    .. attribute:: dr_priority
                    
                    	Hello DR priority, preference given to larger value
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: hello_interval
                    
                    	Hello interval in seconds
                    	**type**\:  int
                    
                    	**range:** 1..3600
                    
                    	**units**\: second
                    
                    .. attribute:: join_prune_mtu
                    
                    	Join\-Prune MTU in Bytes
                    	**type**\:  int
                    
                    	**range:** 576..65535
                    
                    	**units**\: byte
                    
                    .. attribute:: jp_interval
                    
                    	Join\-Prune interval in seconds
                    	**type**\:  int
                    
                    	**range:** 10..600
                    
                    	**units**\: second
                    
                    .. attribute:: override_interval
                    
                    	Override interval in milliseconds
                    	**type**\:  int
                    
                    	**range:** 400..65535
                    
                    	**units**\: millisecond
                    
                    .. attribute:: propagation_delay
                    
                    	Propagation delay in milli seconds
                    	**type**\:  int
                    
                    	**range:** 100..32767
                    
                    	**units**\: millisecond
                    
                    

                    """

                    _prefix = 'ipv4-pim-cfg'
                    _revision = '2016-06-01'

                    def __init__(self):
                        self.parent = None
                        self.convergency = None
                        self.dr_priority = None
                        self.hello_interval = None
                        self.join_prune_mtu = None
                        self.jp_interval = None
                        self.override_interval = None
                        self.propagation_delay = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-pim-cfg:inheritable-defaults'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.convergency is not None:
                            return True

                        if self.dr_priority is not None:
                            return True

                        if self.hello_interval is not None:
                            return True

                        if self.join_prune_mtu is not None:
                            return True

                        if self.jp_interval is not None:
                            return True

                        if self.override_interval is not None:
                            return True

                        if self.propagation_delay is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_pim_cfg as meta
                        return meta._meta_table['Pim.Vrfs.Vrf.Ipv6.InheritableDefaults']['meta_info']


                class Rpf(object):
                    """
                    Configure RPF options
                    
                    .. attribute:: route_policy
                    
                    	Route policy to select RPF topology
                    	**type**\:  str
                    
                    	**length:** 1..64
                    
                    

                    """

                    _prefix = 'ipv4-pim-cfg'
                    _revision = '2016-06-01'

                    def __init__(self):
                        self.parent = None
                        self.route_policy = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-pim-cfg:rpf'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.route_policy is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_pim_cfg as meta
                        return meta._meta_table['Pim.Vrfs.Vrf.Ipv6.Rpf']['meta_info']


                class Maximum(object):
                    """
                    Configure PIM State Limits
                    
                    .. attribute:: bsr_candidate_rp_cache
                    
                    	Override default maximum and threshold for BSR C\-RP cache setting
                    	**type**\:   :py:class:`BsrCandidateRpCache <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.Vrfs.Vrf.Ipv6.Maximum.BsrCandidateRpCache>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: bsr_group_mappings
                    
                    	Override default maximum and threshold for number of group mappings from BSR
                    	**type**\:   :py:class:`BsrGroupMappings <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.Vrfs.Vrf.Ipv6.Maximum.BsrGroupMappings>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: group_mappings_auto_rp
                    
                    	Override default maximum for number of group mappings from autorp mapping agent
                    	**type**\:   :py:class:`GroupMappingsAutoRp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.Vrfs.Vrf.Ipv6.Maximum.GroupMappingsAutoRp>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: register_states
                    
                    	Override default maximum for number of sparse\-mode source registers
                    	**type**\:   :py:class:`RegisterStates <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.Vrfs.Vrf.Ipv6.Maximum.RegisterStates>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: route_interfaces
                    
                    	Override default maximum for number of route\-interfaces
                    	**type**\:   :py:class:`RouteInterfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.Vrfs.Vrf.Ipv6.Maximum.RouteInterfaces>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: routes
                    
                    	Override default maximum for number of routes
                    	**type**\:   :py:class:`Routes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.Vrfs.Vrf.Ipv6.Maximum.Routes>`
                    
                    	**presence node**\: True
                    
                    

                    """

                    _prefix = 'ipv4-pim-cfg'
                    _revision = '2016-06-01'

                    def __init__(self):
                        self.parent = None
                        self.bsr_candidate_rp_cache = None
                        self.bsr_group_mappings = None
                        self.group_mappings_auto_rp = None
                        self.register_states = None
                        self.route_interfaces = None
                        self.routes = None


                    class GroupMappingsAutoRp(object):
                        """
                        Override default maximum for number of group
                        mappings from autorp mapping agent
                        
                        .. attribute:: maximum_group_ranges_auto_rp
                        
                        	Maximum number of PIM group mappings from autorp
                        	**type**\:  int
                        
                        	**range:** 1..10000
                        
                        	**mandatory**\: True
                        
                        .. attribute:: threshold_group_ranges_auto_rp
                        
                        	Warning threshold number of PIM group mappings from autorp
                        	**type**\:  int
                        
                        	**range:** 1..10000
                        
                        	**default value**\: 450
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'ipv4-pim-cfg'
                        _revision = '2016-06-01'

                        def __init__(self):
                            self.parent = None
                            self._is_presence = True
                            self.maximum_group_ranges_auto_rp = None
                            self.threshold_group_ranges_auto_rp = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv4-pim-cfg:group-mappings-auto-rp'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self._is_presence:
                                return True
                            if self.maximum_group_ranges_auto_rp is not None:
                                return True

                            if self.threshold_group_ranges_auto_rp is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_pim_cfg as meta
                            return meta._meta_table['Pim.Vrfs.Vrf.Ipv6.Maximum.GroupMappingsAutoRp']['meta_info']


                    class BsrGroupMappings(object):
                        """
                        Override default maximum and threshold for
                        number of group mappings from BSR
                        
                        .. attribute:: bsr_maximum_group_ranges
                        
                        	Maximum number of PIM group mappings from BSR
                        	**type**\:  int
                        
                        	**range:** 1..10000
                        
                        	**mandatory**\: True
                        
                        .. attribute:: warning_threshold
                        
                        	Set threshold to print warning
                        	**type**\:  int
                        
                        	**range:** 1..10000
                        
                        	**default value**\: 500
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'ipv4-pim-cfg'
                        _revision = '2016-06-01'

                        def __init__(self):
                            self.parent = None
                            self._is_presence = True
                            self.bsr_maximum_group_ranges = None
                            self.warning_threshold = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv4-pim-cfg:bsr-group-mappings'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self._is_presence:
                                return True
                            if self.bsr_maximum_group_ranges is not None:
                                return True

                            if self.warning_threshold is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_pim_cfg as meta
                            return meta._meta_table['Pim.Vrfs.Vrf.Ipv6.Maximum.BsrGroupMappings']['meta_info']


                    class RegisterStates(object):
                        """
                        Override default maximum for number of
                        sparse\-mode source registers
                        
                        .. attribute:: maximum_register_states
                        
                        	Maximum number of PIM Sparse\-Mode register states
                        	**type**\:  int
                        
                        	**range:** 0..75000
                        
                        	**mandatory**\: True
                        
                        .. attribute:: warning_threshold
                        
                        	Set threshold to print warning
                        	**type**\:  int
                        
                        	**range:** 0..75000
                        
                        	**default value**\: 20000
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'ipv4-pim-cfg'
                        _revision = '2016-06-01'

                        def __init__(self):
                            self.parent = None
                            self._is_presence = True
                            self.maximum_register_states = None
                            self.warning_threshold = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv4-pim-cfg:register-states'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self._is_presence:
                                return True
                            if self.maximum_register_states is not None:
                                return True

                            if self.warning_threshold is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_pim_cfg as meta
                            return meta._meta_table['Pim.Vrfs.Vrf.Ipv6.Maximum.RegisterStates']['meta_info']


                    class RouteInterfaces(object):
                        """
                        Override default maximum for number of
                        route\-interfaces
                        
                        .. attribute:: maximum_route_interfaces
                        
                        	Maximum number of PIM route\-interfaces
                        	**type**\:  int
                        
                        	**range:** 1..1100000
                        
                        	**mandatory**\: True
                        
                        .. attribute:: warning_threshold
                        
                        	Set threshold to print warning
                        	**type**\:  int
                        
                        	**range:** 1..1100000
                        
                        	**default value**\: 300000
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'ipv4-pim-cfg'
                        _revision = '2016-06-01'

                        def __init__(self):
                            self.parent = None
                            self._is_presence = True
                            self.maximum_route_interfaces = None
                            self.warning_threshold = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv4-pim-cfg:route-interfaces'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self._is_presence:
                                return True
                            if self.maximum_route_interfaces is not None:
                                return True

                            if self.warning_threshold is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_pim_cfg as meta
                            return meta._meta_table['Pim.Vrfs.Vrf.Ipv6.Maximum.RouteInterfaces']['meta_info']


                    class BsrCandidateRpCache(object):
                        """
                        Override default maximum and threshold for BSR
                        C\-RP cache setting
                        
                        .. attribute:: bsr_maximum_candidate_rp_cache
                        
                        	Maximum number of BSR C\-RP cache setting
                        	**type**\:  int
                        
                        	**range:** 1..10000
                        
                        	**mandatory**\: True
                        
                        .. attribute:: warning_threshold
                        
                        	Set threshold to print warning
                        	**type**\:  int
                        
                        	**range:** 1..10000
                        
                        	**default value**\: 100
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'ipv4-pim-cfg'
                        _revision = '2016-06-01'

                        def __init__(self):
                            self.parent = None
                            self._is_presence = True
                            self.bsr_maximum_candidate_rp_cache = None
                            self.warning_threshold = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv4-pim-cfg:bsr-candidate-rp-cache'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self._is_presence:
                                return True
                            if self.bsr_maximum_candidate_rp_cache is not None:
                                return True

                            if self.warning_threshold is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_pim_cfg as meta
                            return meta._meta_table['Pim.Vrfs.Vrf.Ipv6.Maximum.BsrCandidateRpCache']['meta_info']


                    class Routes(object):
                        """
                        Override default maximum for number of routes
                        
                        .. attribute:: maximum_routes
                        
                        	Maximum number of PIM routes
                        	**type**\:  int
                        
                        	**range:** 1..200000
                        
                        	**mandatory**\: True
                        
                        .. attribute:: warning_threshold
                        
                        	Set threshold to print warning
                        	**type**\:  int
                        
                        	**range:** 1..200000
                        
                        	**default value**\: 100000
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'ipv4-pim-cfg'
                        _revision = '2016-06-01'

                        def __init__(self):
                            self.parent = None
                            self._is_presence = True
                            self.maximum_routes = None
                            self.warning_threshold = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv4-pim-cfg:routes'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self._is_presence:
                                return True
                            if self.maximum_routes is not None:
                                return True

                            if self.warning_threshold is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_pim_cfg as meta
                            return meta._meta_table['Pim.Vrfs.Vrf.Ipv6.Maximum.Routes']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-pim-cfg:maximum'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.bsr_candidate_rp_cache is not None and self.bsr_candidate_rp_cache._has_data():
                            return True

                        if self.bsr_group_mappings is not None and self.bsr_group_mappings._has_data():
                            return True

                        if self.group_mappings_auto_rp is not None and self.group_mappings_auto_rp._has_data():
                            return True

                        if self.register_states is not None and self.register_states._has_data():
                            return True

                        if self.route_interfaces is not None and self.route_interfaces._has_data():
                            return True

                        if self.routes is not None and self.routes._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_pim_cfg as meta
                        return meta._meta_table['Pim.Vrfs.Vrf.Ipv6.Maximum']['meta_info']


                class SgExpiryTimer(object):
                    """
                    Configure expiry timer for S,G routes
                    
                    .. attribute:: access_list_name
                    
                    	Access\-list of applicable S,G routes
                    	**type**\:  str
                    
                    	**length:** 1..64
                    
                    .. attribute:: interval
                    
                    	(S,G) expiry time in seconds
                    	**type**\:  int
                    
                    	**range:** 40..57600
                    
                    	**units**\: second
                    
                    

                    """

                    _prefix = 'ipv4-pim-cfg'
                    _revision = '2016-06-01'

                    def __init__(self):
                        self.parent = None
                        self.access_list_name = None
                        self.interval = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-pim-cfg:sg-expiry-timer'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.access_list_name is not None:
                            return True

                        if self.interval is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_pim_cfg as meta
                        return meta._meta_table['Pim.Vrfs.Vrf.Ipv6.SgExpiryTimer']['meta_info']


                class RpfVectorEnable(object):
                    """
                    Enable PIM RPF Vector Proxy's
                    
                    .. attribute:: allow_ebgp
                    
                    	Allow RPF Vector origination over eBGP sessions
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: disable_ibgp
                    
                    	Disable RPF Vector origination over iBGP sessions
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: enable
                    
                    	RPF Vector is turned on if configured
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    	**mandatory**\: True
                    
                    .. attribute:: _is_presence
                    
                    	Is present if this instance represents presence container else not
                    	**type**\: bool
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'ipv4-pim-cfg'
                    _revision = '2016-06-01'

                    def __init__(self):
                        self.parent = None
                        self._is_presence = True
                        self.allow_ebgp = None
                        self.disable_ibgp = None
                        self.enable = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-pim-cfg:rpf-vector-enable'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self._is_presence:
                            return True
                        if self.allow_ebgp is not None:
                            return True

                        if self.disable_ibgp is not None:
                            return True

                        if self.enable is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_pim_cfg as meta
                        return meta._meta_table['Pim.Vrfs.Vrf.Ipv6.RpfVectorEnable']['meta_info']


                class Ssm(object):
                    """
                    Configure IP Multicast SSM
                    
                    .. attribute:: disable
                    
                    	TRUE if SSM is disabled on this router
                    	**type**\:  bool
                    
                    	**default value**\: false
                    
                    .. attribute:: range
                    
                    	Access list of groups enabled with SSM
                    	**type**\:  str
                    
                    	**length:** 1..64
                    
                    

                    """

                    _prefix = 'ipv4-pim-cfg'
                    _revision = '2016-06-01'

                    def __init__(self):
                        self.parent = None
                        self.disable = None
                        self.range = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-pim-cfg:ssm'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.disable is not None:
                            return True

                        if self.range is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_pim_cfg as meta
                        return meta._meta_table['Pim.Vrfs.Vrf.Ipv6.Ssm']['meta_info']


                class BidirRpAddresses(object):
                    """
                    Configure Bidirectional PIM Rendezvous Point
                    
                    .. attribute:: bidir_rp_address
                    
                    	Address of the Rendezvous Point
                    	**type**\: list of    :py:class:`BidirRpAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.Vrfs.Vrf.Ipv6.BidirRpAddresses.BidirRpAddress>`
                    
                    

                    """

                    _prefix = 'ipv4-pim-cfg'
                    _revision = '2016-06-01'

                    def __init__(self):
                        self.parent = None
                        self.bidir_rp_address = YList()
                        self.bidir_rp_address.parent = self
                        self.bidir_rp_address.name = 'bidir_rp_address'


                    class BidirRpAddress(object):
                        """
                        Address of the Rendezvous Point
                        
                        .. attribute:: rp_address  <key>
                        
                        	RP address of Rendezvous Point
                        	**type**\: one of the below types:
                        
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        .. attribute:: access_list_name
                        
                        	Access list of groups that should map to a given RP
                        	**type**\:  str
                        
                        	**length:** 1..64
                        
                        .. attribute:: auto_rp_override
                        
                        	TRUE Indicates if static RP config overrides AutoRP and BSR
                        	**type**\:  bool
                        
                        

                        """

                        _prefix = 'ipv4-pim-cfg'
                        _revision = '2016-06-01'

                        def __init__(self):
                            self.parent = None
                            self.rp_address = None
                            self.access_list_name = None
                            self.auto_rp_override = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.rp_address is None:
                                raise YPYModelError('Key property rp_address is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv4-pim-cfg:bidir-rp-address[Cisco-IOS-XR-ipv4-pim-cfg:rp-address = ' + str(self.rp_address) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.rp_address is not None:
                                return True

                            if self.access_list_name is not None:
                                return True

                            if self.auto_rp_override is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_pim_cfg as meta
                            return meta._meta_table['Pim.Vrfs.Vrf.Ipv6.BidirRpAddresses.BidirRpAddress']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-pim-cfg:bidir-rp-addresses'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.bidir_rp_address is not None:
                            for child_ref in self.bidir_rp_address:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_pim_cfg as meta
                        return meta._meta_table['Pim.Vrfs.Vrf.Ipv6.BidirRpAddresses']['meta_info']


                class Bsr(object):
                    """
                    PIM BSR configuration
                    
                    .. attribute:: candidate_bsr
                    
                    	PIM Candidate BSR configuration
                    	**type**\:   :py:class:`CandidateBsr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.Vrfs.Vrf.Ipv6.Bsr.CandidateBsr>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: candidate_rps
                    
                    	PIM RP configuration
                    	**type**\:   :py:class:`CandidateRps <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.Vrfs.Vrf.Ipv6.Bsr.CandidateRps>`
                    
                    

                    """

                    _prefix = 'ipv4-pim-cfg'
                    _revision = '2016-06-01'

                    def __init__(self):
                        self.parent = None
                        self.candidate_bsr = None
                        self.candidate_rps = Pim.Vrfs.Vrf.Ipv6.Bsr.CandidateRps()
                        self.candidate_rps.parent = self


                    class CandidateBsr(object):
                        """
                        PIM Candidate BSR configuration
                        
                        .. attribute:: address
                        
                        	BSR Address configured
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        	**mandatory**\: True
                        
                        .. attribute:: prefix_length
                        
                        	Hash Mask Length for this candidate BSR
                        	**type**\:  int
                        
                        	**range:** 0..128
                        
                        	**default value**\: 126
                        
                        .. attribute:: priority
                        
                        	Priority of the Candidate BSR
                        	**type**\:  int
                        
                        	**range:** 1..255
                        
                        	**default value**\: 1
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'ipv4-pim-cfg'
                        _revision = '2016-06-01'

                        def __init__(self):
                            self.parent = None
                            self._is_presence = True
                            self.address = None
                            self.prefix_length = None
                            self.priority = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv4-pim-cfg:candidate-bsr'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self._is_presence:
                                return True
                            if self.address is not None:
                                return True

                            if self.prefix_length is not None:
                                return True

                            if self.priority is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_pim_cfg as meta
                            return meta._meta_table['Pim.Vrfs.Vrf.Ipv6.Bsr.CandidateBsr']['meta_info']


                    class CandidateRps(object):
                        """
                        PIM RP configuration
                        
                        .. attribute:: candidate_rp
                        
                        	Address of PIM SM BSR Candidate\-RP
                        	**type**\: list of    :py:class:`CandidateRp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.Vrfs.Vrf.Ipv6.Bsr.CandidateRps.CandidateRp>`
                        
                        

                        """

                        _prefix = 'ipv4-pim-cfg'
                        _revision = '2016-06-01'

                        def __init__(self):
                            self.parent = None
                            self.candidate_rp = YList()
                            self.candidate_rp.parent = self
                            self.candidate_rp.name = 'candidate_rp'


                        class CandidateRp(object):
                            """
                            Address of PIM SM BSR Candidate\-RP
                            
                            .. attribute:: address  <key>
                            
                            	Address of Candidate\-RP
                            	**type**\: one of the below types:
                            
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            .. attribute:: mode  <key>
                            
                            	SM or Bidir
                            	**type**\:   :py:class:`PimProtocolModeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.PimProtocolModeEnum>`
                            
                            .. attribute:: group_list
                            
                            	Access\-list specifying the group range for the Candidate\-RP
                            	**type**\:  str
                            
                            	**length:** 1..64
                            
                            .. attribute:: interval
                            
                            	Advertisement interval
                            	**type**\:  int
                            
                            	**range:** 30..600
                            
                            	**default value**\: 60
                            
                            .. attribute:: priority
                            
                            	Priority of the CRP
                            	**type**\:  int
                            
                            	**range:** 1..255
                            
                            	**default value**\: 192
                            
                            

                            """

                            _prefix = 'ipv4-pim-cfg'
                            _revision = '2016-06-01'

                            def __init__(self):
                                self.parent = None
                                self.address = None
                                self.mode = None
                                self.group_list = None
                                self.interval = None
                                self.priority = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                if self.address is None:
                                    raise YPYModelError('Key property address is None')
                                if self.mode is None:
                                    raise YPYModelError('Key property mode is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-ipv4-pim-cfg:candidate-rp[Cisco-IOS-XR-ipv4-pim-cfg:address = ' + str(self.address) + '][Cisco-IOS-XR-ipv4-pim-cfg:mode = ' + str(self.mode) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.address is not None:
                                    return True

                                if self.mode is not None:
                                    return True

                                if self.group_list is not None:
                                    return True

                                if self.interval is not None:
                                    return True

                                if self.priority is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_pim_cfg as meta
                                return meta._meta_table['Pim.Vrfs.Vrf.Ipv6.Bsr.CandidateRps.CandidateRp']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv4-pim-cfg:candidate-rps'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.candidate_rp is not None:
                                for child_ref in self.candidate_rp:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_pim_cfg as meta
                            return meta._meta_table['Pim.Vrfs.Vrf.Ipv6.Bsr.CandidateRps']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-pim-cfg:bsr'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.candidate_bsr is not None and self.candidate_bsr._has_data():
                            return True

                        if self.candidate_rps is not None and self.candidate_rps._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_pim_cfg as meta
                        return meta._meta_table['Pim.Vrfs.Vrf.Ipv6.Bsr']['meta_info']


                class AllowRp(object):
                    """
                    Enable allow\-rp filtering for SM joins
                    
                    .. attribute:: group_list_name
                    
                    	Access\-list specifiying applicable groups
                    	**type**\:  str
                    
                    	**length:** 1..64
                    
                    .. attribute:: rp_list_name
                    
                    	Access\-list specifiying applicable RPs
                    	**type**\:  str
                    
                    	**length:** 1..64
                    
                    .. attribute:: _is_presence
                    
                    	Is present if this instance represents presence container else not
                    	**type**\: bool
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'ipv4-pim-cfg'
                    _revision = '2016-06-01'

                    def __init__(self):
                        self.parent = None
                        self._is_presence = True
                        self.group_list_name = None
                        self.rp_list_name = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-pim-cfg:allow-rp'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self._is_presence:
                            return True
                        if self.group_list_name is not None:
                            return True

                        if self.rp_list_name is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_pim_cfg as meta
                        return meta._meta_table['Pim.Vrfs.Vrf.Ipv6.AllowRp']['meta_info']


                class EmbeddedRpAddresses(object):
                    """
                    Set Embedded RP processing support
                    
                    .. attribute:: embedded_rp_address
                    
                    	Set Embedded RP processing support
                    	**type**\: list of    :py:class:`EmbeddedRpAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.Vrfs.Vrf.Ipv6.EmbeddedRpAddresses.EmbeddedRpAddress>`
                    
                    

                    """

                    _prefix = 'ipv4-pim-cfg'
                    _revision = '2016-06-01'

                    def __init__(self):
                        self.parent = None
                        self.embedded_rp_address = YList()
                        self.embedded_rp_address.parent = self
                        self.embedded_rp_address.name = 'embedded_rp_address'


                    class EmbeddedRpAddress(object):
                        """
                        Set Embedded RP processing support
                        
                        .. attribute:: rp_address  <key>
                        
                        	RP address of the Rendezvous Point
                        	**type**\: one of the below types:
                        
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        .. attribute:: access_list_name
                        
                        	Access list of groups that should map to a given RP
                        	**type**\:  str
                        
                        	**length:** 1..64
                        
                        	**mandatory**\: True
                        
                        

                        """

                        _prefix = 'ipv4-pim-cfg'
                        _revision = '2016-06-01'

                        def __init__(self):
                            self.parent = None
                            self.rp_address = None
                            self.access_list_name = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.rp_address is None:
                                raise YPYModelError('Key property rp_address is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv4-pim-cfg:embedded-rp-address[Cisco-IOS-XR-ipv4-pim-cfg:rp-address = ' + str(self.rp_address) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.rp_address is not None:
                                return True

                            if self.access_list_name is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_pim_cfg as meta
                            return meta._meta_table['Pim.Vrfs.Vrf.Ipv6.EmbeddedRpAddresses.EmbeddedRpAddress']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-pim-cfg:embedded-rp-addresses'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.embedded_rp_address is not None:
                            for child_ref in self.embedded_rp_address:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_pim_cfg as meta
                        return meta._meta_table['Pim.Vrfs.Vrf.Ipv6.EmbeddedRpAddresses']['meta_info']


                class Convergence(object):
                    """
                    Configure convergence parameters
                    
                    .. attribute:: link_down_prune_delay
                    
                    	Delay prunes if route join state transitions to not\-joined on link down
                    	**type**\:  int
                    
                    	**range:** 0..60
                    
                    	**units**\: second
                    
                    .. attribute:: rpf_conflict_join_delay
                    
                    	Dampen first join if RPF path is through one of the downstream neighbor
                    	**type**\:  int
                    
                    	**range:** 0..15
                    
                    	**units**\: second
                    
                    

                    """

                    _prefix = 'ipv4-pim-cfg'
                    _revision = '2016-06-01'

                    def __init__(self):
                        self.parent = None
                        self.link_down_prune_delay = None
                        self.rpf_conflict_join_delay = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-pim-cfg:convergence'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.link_down_prune_delay is not None:
                            return True

                        if self.rpf_conflict_join_delay is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_pim_cfg as meta
                        return meta._meta_table['Pim.Vrfs.Vrf.Ipv6.Convergence']['meta_info']


                class Interfaces(object):
                    """
                    Interface\-level Configuration
                    
                    .. attribute:: interface
                    
                    	The name of the interface
                    	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.Vrfs.Vrf.Ipv6.Interfaces.Interface>`
                    
                    

                    """

                    _prefix = 'ipv4-pim-cfg'
                    _revision = '2016-06-01'

                    def __init__(self):
                        self.parent = None
                        self.interface = YList()
                        self.interface.parent = self
                        self.interface.name = 'interface'


                    class Interface(object):
                        """
                        The name of the interface
                        
                        .. attribute:: interface_name  <key>
                        
                        	The name of interface
                        	**type**\:  str
                        
                        	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                        
                        .. attribute:: bfd
                        
                        	BFD configuration
                        	**type**\:   :py:class:`Bfd <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.Vrfs.Vrf.Ipv6.Interfaces.Interface.Bfd>`
                        
                        .. attribute:: bsr_border
                        
                        	BSR Border configuration for Interface
                        	**type**\:  bool
                        
                        .. attribute:: dr_priority
                        
                        	Hello DR priority, preference given to larger value
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: enable
                        
                        	Enter PIM Interface processing
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: hello_interval
                        
                        	Hello interval in seconds
                        	**type**\:  int
                        
                        	**range:** 1..3600
                        
                        	**units**\: second
                        
                        .. attribute:: interface_enable
                        
                        	Enable PIM processing on the interface
                        	**type**\:  bool
                        
                        .. attribute:: join_prune_mtu
                        
                        	Join\-Prune MTU in Bytes
                        	**type**\:  int
                        
                        	**range:** 576..65535
                        
                        	**units**\: byte
                        
                        .. attribute:: jp_interval
                        
                        	Join\-Prune interval in seconds
                        	**type**\:  int
                        
                        	**range:** 10..600
                        
                        	**units**\: second
                        
                        .. attribute:: maximum_routes
                        
                        	Maximum number of allowed routes for this interface
                        	**type**\:   :py:class:`MaximumRoutes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.Vrfs.Vrf.Ipv6.Interfaces.Interface.MaximumRoutes>`
                        
                        	**presence node**\: True
                        
                        .. attribute:: neighbor_filter
                        
                        	Access\-list of neighbors to be filtered
                        	**type**\:  str
                        
                        	**length:** 1..64
                        
                        .. attribute:: override_interval
                        
                        	Override interval in milliseconds
                        	**type**\:  int
                        
                        	**range:** 400..65535
                        
                        	**units**\: millisecond
                        
                        .. attribute:: propagation_delay
                        
                        	Propagation delay in milli seconds
                        	**type**\:  int
                        
                        	**range:** 100..32767
                        
                        	**units**\: millisecond
                        
                        

                        """

                        _prefix = 'ipv4-pim-cfg'
                        _revision = '2016-06-01'

                        def __init__(self):
                            self.parent = None
                            self.interface_name = None
                            self.bfd = Pim.Vrfs.Vrf.Ipv6.Interfaces.Interface.Bfd()
                            self.bfd.parent = self
                            self.bsr_border = None
                            self.dr_priority = None
                            self.enable = None
                            self.hello_interval = None
                            self.interface_enable = None
                            self.join_prune_mtu = None
                            self.jp_interval = None
                            self.maximum_routes = None
                            self.neighbor_filter = None
                            self.override_interval = None
                            self.propagation_delay = None


                        class MaximumRoutes(object):
                            """
                            Maximum number of allowed routes for this
                            interface
                            
                            .. attribute:: access_list_name
                            
                            	Access\-list to account for
                            	**type**\:  str
                            
                            	**length:** 1..64
                            
                            .. attribute:: maximum
                            
                            	Maximum number of routes for this interface
                            	**type**\:  int
                            
                            	**range:** 1..1100000
                            
                            	**mandatory**\: True
                            
                            .. attribute:: warning_threshold
                            
                            	Set threshold to print warning
                            	**type**\:  int
                            
                            	**range:** 1..1100000
                            
                            .. attribute:: _is_presence
                            
                            	Is present if this instance represents presence container else not
                            	**type**\: bool
                            
                            

                            This class is a :ref:`presence class<presence-class>`

                            """

                            _prefix = 'ipv4-pim-cfg'
                            _revision = '2016-06-01'

                            def __init__(self):
                                self.parent = None
                                self._is_presence = True
                                self.access_list_name = None
                                self.maximum = None
                                self.warning_threshold = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ipv4-pim-cfg:maximum-routes'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self._is_presence:
                                    return True
                                if self.access_list_name is not None:
                                    return True

                                if self.maximum is not None:
                                    return True

                                if self.warning_threshold is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_pim_cfg as meta
                                return meta._meta_table['Pim.Vrfs.Vrf.Ipv6.Interfaces.Interface.MaximumRoutes']['meta_info']


                        class Bfd(object):
                            """
                            BFD configuration
                            
                            .. attribute:: detection_multiplier
                            
                            	Detection multiplier for BFD sessions created by PIM
                            	**type**\:  int
                            
                            	**range:** 2..50
                            
                            .. attribute:: enable
                            
                            	TRUE to enable BFD. FALSE to disable and to prevent inheritance from a parent
                            	**type**\:  bool
                            
                            .. attribute:: interval
                            
                            	Hello interval for BFD sessions created by PIM
                            	**type**\:  int
                            
                            	**range:** 3..30000
                            
                            	**units**\: millisecond
                            
                            

                            """

                            _prefix = 'ipv4-pim-cfg'
                            _revision = '2016-06-01'

                            def __init__(self):
                                self.parent = None
                                self.detection_multiplier = None
                                self.enable = None
                                self.interval = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ipv4-pim-cfg:bfd'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.detection_multiplier is not None:
                                    return True

                                if self.enable is not None:
                                    return True

                                if self.interval is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_pim_cfg as meta
                                return meta._meta_table['Pim.Vrfs.Vrf.Ipv6.Interfaces.Interface.Bfd']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.interface_name is None:
                                raise YPYModelError('Key property interface_name is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv4-pim-cfg:interface[Cisco-IOS-XR-ipv4-pim-cfg:interface-name = ' + str(self.interface_name) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.interface_name is not None:
                                return True

                            if self.bfd is not None and self.bfd._has_data():
                                return True

                            if self.bsr_border is not None:
                                return True

                            if self.dr_priority is not None:
                                return True

                            if self.enable is not None:
                                return True

                            if self.hello_interval is not None:
                                return True

                            if self.interface_enable is not None:
                                return True

                            if self.join_prune_mtu is not None:
                                return True

                            if self.jp_interval is not None:
                                return True

                            if self.maximum_routes is not None and self.maximum_routes._has_data():
                                return True

                            if self.neighbor_filter is not None:
                                return True

                            if self.override_interval is not None:
                                return True

                            if self.propagation_delay is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_pim_cfg as meta
                            return meta._meta_table['Pim.Vrfs.Vrf.Ipv6.Interfaces.Interface']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ipv4-pim-cfg:interfaces'

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
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_pim_cfg as meta
                        return meta._meta_table['Pim.Vrfs.Vrf.Ipv6.Interfaces']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ipv4-pim-cfg:ipv6'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.accept_register is not None:
                        return True

                    if self.allow_rp is not None and self.allow_rp._has_data():
                        return True

                    if self.bidir_rp_addresses is not None and self.bidir_rp_addresses._has_data():
                        return True

                    if self.bsr is not None and self.bsr._has_data():
                        return True

                    if self.convergence is not None and self.convergence._has_data():
                        return True

                    if self.embedded_rp_addresses is not None and self.embedded_rp_addresses._has_data():
                        return True

                    if self.embedded_rp_disable is not None:
                        return True

                    if self.inheritable_defaults is not None and self.inheritable_defaults._has_data():
                        return True

                    if self.interfaces is not None and self.interfaces._has_data():
                        return True

                    if self.log_neighbor_changes is not None:
                        return True

                    if self.maximum is not None and self.maximum._has_data():
                        return True

                    if self.multipath is not None:
                        return True

                    if self.neighbor_check_on_receive is not None:
                        return True

                    if self.neighbor_check_on_send is not None:
                        return True

                    if self.neighbor_filter is not None:
                        return True

                    if self.old_register_checksum is not None:
                        return True

                    if self.register_source is not None:
                        return True

                    if self.rp_static_deny is not None:
                        return True

                    if self.rpf is not None and self.rpf._has_data():
                        return True

                    if self.rpf_vector_enable is not None and self.rpf_vector_enable._has_data():
                        return True

                    if self.sg_expiry_timer is not None and self.sg_expiry_timer._has_data():
                        return True

                    if self.sparse_mode_rp_addresses is not None and self.sparse_mode_rp_addresses._has_data():
                        return True

                    if self.spt_threshold_infinity is not None:
                        return True

                    if self.ssm is not None and self.ssm._has_data():
                        return True

                    if self.ssm_allow_override is not None:
                        return True

                    if self.suppress_data_registers is not None:
                        return True

                    if self.suppress_rpf_prunes is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_pim_cfg as meta
                    return meta._meta_table['Pim.Vrfs.Vrf.Ipv6']['meta_info']

            @property
            def _common_path(self):
                if self.vrf_name is None:
                    raise YPYModelError('Key property vrf_name is None')

                return '/Cisco-IOS-XR-ipv4-pim-cfg:pim/Cisco-IOS-XR-ipv4-pim-cfg:vrfs/Cisco-IOS-XR-ipv4-pim-cfg:vrf[Cisco-IOS-XR-ipv4-pim-cfg:vrf-name = ' + str(self.vrf_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.vrf_name is not None:
                    return True

                if self.ipv4 is not None and self.ipv4._has_data():
                    return True

                if self.ipv6 is not None and self.ipv6._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_pim_cfg as meta
                return meta._meta_table['Pim.Vrfs.Vrf']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ipv4-pim-cfg:pim/Cisco-IOS-XR-ipv4-pim-cfg:vrfs'

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
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_pim_cfg as meta
            return meta._meta_table['Pim.Vrfs']['meta_info']


    class DefaultContext(object):
        """
        Default Context
        
        .. attribute:: ipv4
        
        	IPV4 commands
        	**type**\:   :py:class:`Ipv4 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.DefaultContext.Ipv4>`
        
        .. attribute:: ipv6
        
        	IPV6 commands
        	**type**\:   :py:class:`Ipv6 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.DefaultContext.Ipv6>`
        
        .. attribute:: _is_presence
        
        	Is present if this instance represents presence container else not
        	**type**\: bool
        
        

        This class is a :ref:`presence class<presence-class>`

        """

        _prefix = 'ipv4-pim-cfg'
        _revision = '2016-06-01'

        def __init__(self):
            self.parent = None
            self._is_presence = True
            self.ipv4 = Pim.DefaultContext.Ipv4()
            self.ipv4.parent = self
            self.ipv6 = Pim.DefaultContext.Ipv6()
            self.ipv6.parent = self


        class Ipv6(object):
            """
            IPV6 commands
            
            .. attribute:: accept_register
            
            	Access\-list which specifies unauthorized sources
            	**type**\:  str
            
            	**length:** 1..64
            
            .. attribute:: allow_rp
            
            	Enable allow\-rp filtering for SM joins
            	**type**\:   :py:class:`AllowRp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.DefaultContext.Ipv6.AllowRp>`
            
            	**presence node**\: True
            
            .. attribute:: bidir_rp_addresses
            
            	Configure Bidirectional PIM Rendezvous Point
            	**type**\:   :py:class:`BidirRpAddresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.DefaultContext.Ipv6.BidirRpAddresses>`
            
            .. attribute:: bsr
            
            	PIM BSR configuration
            	**type**\:   :py:class:`Bsr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.DefaultContext.Ipv6.Bsr>`
            
            .. attribute:: convergence
            
            	Configure convergence parameters
            	**type**\:   :py:class:`Convergence <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.DefaultContext.Ipv6.Convergence>`
            
            .. attribute:: embedded_rp_addresses
            
            	Set Embedded RP processing support
            	**type**\:   :py:class:`EmbeddedRpAddresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.DefaultContext.Ipv6.EmbeddedRpAddresses>`
            
            .. attribute:: embedded_rp_disable
            
            	Set Embedded RP processing support
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: inheritable_defaults
            
            	Inheritable defaults
            	**type**\:   :py:class:`InheritableDefaults <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.DefaultContext.Ipv6.InheritableDefaults>`
            
            .. attribute:: interfaces
            
            	Interface\-level Configuration
            	**type**\:   :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.DefaultContext.Ipv6.Interfaces>`
            
            .. attribute:: log_neighbor_changes
            
            	PIM neighbor state change logging is turned on if configured
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: maximum
            
            	Configure PIM State Limits
            	**type**\:   :py:class:`Maximum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.DefaultContext.Ipv6.Maximum>`
            
            .. attribute:: multipath
            
            	Enable equal\-cost multipath routing
            	**type**\:   :py:class:`PimMultipathEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.PimMultipathEnum>`
            
            .. attribute:: neighbor_check_on_receive
            
            	Enable PIM neighbor checking when receiving PIM messages
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: neighbor_check_on_send
            
            	Enable PIM neighbor checking when sending join\-prunes
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: neighbor_filter
            
            	Access\-list of neighbors to be filtered
            	**type**\:  str
            
            	**length:** 1..64
            
            .. attribute:: nsf
            
            	Configure Non\-stop forwarding (NSF) options
            	**type**\:   :py:class:`Nsf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.DefaultContext.Ipv6.Nsf>`
            
            .. attribute:: old_register_checksum
            
            	Generate registers compatible with older IOS versions
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: register_source
            
            	Source address to use for register messages
            	**type**\:  str
            
            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
            
            .. attribute:: rp_static_deny
            
            	Configure static RP deny range
            	**type**\:  str
            
            	**length:** 1..64
            
            .. attribute:: rpf
            
            	Configure RPF options
            	**type**\:   :py:class:`Rpf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.DefaultContext.Ipv6.Rpf>`
            
            .. attribute:: rpf_vector_enable
            
            	Enable PIM RPF Vector Proxy's
            	**type**\:   :py:class:`RpfVectorEnable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.DefaultContext.Ipv6.RpfVectorEnable>`
            
            	**presence node**\: True
            
            .. attribute:: sg_expiry_timer
            
            	Configure expiry timer for S,G routes
            	**type**\:   :py:class:`SgExpiryTimer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.DefaultContext.Ipv6.SgExpiryTimer>`
            
            .. attribute:: sparse_mode_rp_addresses
            
            	Configure Sparse\-Mode Rendezvous Point
            	**type**\:   :py:class:`SparseModeRpAddresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.DefaultContext.Ipv6.SparseModeRpAddresses>`
            
            .. attribute:: spt_threshold_infinity
            
            	Configure threshold of infinity for switching to SPT on last\-hop
            	**type**\:  str
            
            .. attribute:: ssm
            
            	Configure IP Multicast SSM
            	**type**\:   :py:class:`Ssm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.DefaultContext.Ipv6.Ssm>`
            
            .. attribute:: ssm_allow_override
            
            	Allow SSM ranges to be overridden by more specific ranges
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: suppress_data_registers
            
            	Suppress data registers after initial state setup
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: suppress_rpf_prunes
            
            	Suppress prunes triggered as a result of RPF changes
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'ipv4-pim-cfg'
            _revision = '2016-06-01'

            def __init__(self):
                self.parent = None
                self.accept_register = None
                self.allow_rp = None
                self.bidir_rp_addresses = Pim.DefaultContext.Ipv6.BidirRpAddresses()
                self.bidir_rp_addresses.parent = self
                self.bsr = Pim.DefaultContext.Ipv6.Bsr()
                self.bsr.parent = self
                self.convergence = Pim.DefaultContext.Ipv6.Convergence()
                self.convergence.parent = self
                self.embedded_rp_addresses = Pim.DefaultContext.Ipv6.EmbeddedRpAddresses()
                self.embedded_rp_addresses.parent = self
                self.embedded_rp_disable = None
                self.inheritable_defaults = Pim.DefaultContext.Ipv6.InheritableDefaults()
                self.inheritable_defaults.parent = self
                self.interfaces = Pim.DefaultContext.Ipv6.Interfaces()
                self.interfaces.parent = self
                self.log_neighbor_changes = None
                self.maximum = Pim.DefaultContext.Ipv6.Maximum()
                self.maximum.parent = self
                self.multipath = None
                self.neighbor_check_on_receive = None
                self.neighbor_check_on_send = None
                self.neighbor_filter = None
                self.nsf = Pim.DefaultContext.Ipv6.Nsf()
                self.nsf.parent = self
                self.old_register_checksum = None
                self.register_source = None
                self.rp_static_deny = None
                self.rpf = Pim.DefaultContext.Ipv6.Rpf()
                self.rpf.parent = self
                self.rpf_vector_enable = None
                self.sg_expiry_timer = Pim.DefaultContext.Ipv6.SgExpiryTimer()
                self.sg_expiry_timer.parent = self
                self.sparse_mode_rp_addresses = Pim.DefaultContext.Ipv6.SparseModeRpAddresses()
                self.sparse_mode_rp_addresses.parent = self
                self.spt_threshold_infinity = None
                self.ssm = Pim.DefaultContext.Ipv6.Ssm()
                self.ssm.parent = self
                self.ssm_allow_override = None
                self.suppress_data_registers = None
                self.suppress_rpf_prunes = None


            class Interfaces(object):
                """
                Interface\-level Configuration
                
                .. attribute:: interface
                
                	The name of the interface
                	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.DefaultContext.Ipv6.Interfaces.Interface>`
                
                

                """

                _prefix = 'ipv4-pim-cfg'
                _revision = '2016-06-01'

                def __init__(self):
                    self.parent = None
                    self.interface = YList()
                    self.interface.parent = self
                    self.interface.name = 'interface'


                class Interface(object):
                    """
                    The name of the interface
                    
                    .. attribute:: interface_name  <key>
                    
                    	The name of interface
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: bfd
                    
                    	BFD configuration
                    	**type**\:   :py:class:`Bfd <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.DefaultContext.Ipv6.Interfaces.Interface.Bfd>`
                    
                    .. attribute:: bsr_border
                    
                    	BSR Border configuration for Interface
                    	**type**\:  bool
                    
                    .. attribute:: dr_priority
                    
                    	Hello DR priority, preference given to larger value
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: enable
                    
                    	Enter PIM Interface processing
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: hello_interval
                    
                    	Hello interval in seconds
                    	**type**\:  int
                    
                    	**range:** 1..3600
                    
                    	**units**\: second
                    
                    .. attribute:: interface_enable
                    
                    	Enable PIM processing on the interface
                    	**type**\:  bool
                    
                    .. attribute:: join_prune_mtu
                    
                    	Join\-Prune MTU in Bytes
                    	**type**\:  int
                    
                    	**range:** 576..65535
                    
                    	**units**\: byte
                    
                    .. attribute:: jp_interval
                    
                    	Join\-Prune interval in seconds
                    	**type**\:  int
                    
                    	**range:** 10..600
                    
                    	**units**\: second
                    
                    .. attribute:: maximum_routes
                    
                    	Maximum number of allowed routes for this interface
                    	**type**\:   :py:class:`MaximumRoutes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.DefaultContext.Ipv6.Interfaces.Interface.MaximumRoutes>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: neighbor_filter
                    
                    	Access\-list of neighbors to be filtered
                    	**type**\:  str
                    
                    	**length:** 1..64
                    
                    .. attribute:: override_interval
                    
                    	Override interval in milliseconds
                    	**type**\:  int
                    
                    	**range:** 400..65535
                    
                    	**units**\: millisecond
                    
                    .. attribute:: propagation_delay
                    
                    	Propagation delay in milli seconds
                    	**type**\:  int
                    
                    	**range:** 100..32767
                    
                    	**units**\: millisecond
                    
                    

                    """

                    _prefix = 'ipv4-pim-cfg'
                    _revision = '2016-06-01'

                    def __init__(self):
                        self.parent = None
                        self.interface_name = None
                        self.bfd = Pim.DefaultContext.Ipv6.Interfaces.Interface.Bfd()
                        self.bfd.parent = self
                        self.bsr_border = None
                        self.dr_priority = None
                        self.enable = None
                        self.hello_interval = None
                        self.interface_enable = None
                        self.join_prune_mtu = None
                        self.jp_interval = None
                        self.maximum_routes = None
                        self.neighbor_filter = None
                        self.override_interval = None
                        self.propagation_delay = None


                    class MaximumRoutes(object):
                        """
                        Maximum number of allowed routes for this
                        interface
                        
                        .. attribute:: access_list_name
                        
                        	Access\-list to account for
                        	**type**\:  str
                        
                        	**length:** 1..64
                        
                        .. attribute:: maximum
                        
                        	Maximum number of routes for this interface
                        	**type**\:  int
                        
                        	**range:** 1..1100000
                        
                        	**mandatory**\: True
                        
                        .. attribute:: warning_threshold
                        
                        	Set threshold to print warning
                        	**type**\:  int
                        
                        	**range:** 1..1100000
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'ipv4-pim-cfg'
                        _revision = '2016-06-01'

                        def __init__(self):
                            self.parent = None
                            self._is_presence = True
                            self.access_list_name = None
                            self.maximum = None
                            self.warning_threshold = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv4-pim-cfg:maximum-routes'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self._is_presence:
                                return True
                            if self.access_list_name is not None:
                                return True

                            if self.maximum is not None:
                                return True

                            if self.warning_threshold is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_pim_cfg as meta
                            return meta._meta_table['Pim.DefaultContext.Ipv6.Interfaces.Interface.MaximumRoutes']['meta_info']


                    class Bfd(object):
                        """
                        BFD configuration
                        
                        .. attribute:: detection_multiplier
                        
                        	Detection multiplier for BFD sessions created by PIM
                        	**type**\:  int
                        
                        	**range:** 2..50
                        
                        .. attribute:: enable
                        
                        	TRUE to enable BFD. FALSE to disable and to prevent inheritance from a parent
                        	**type**\:  bool
                        
                        .. attribute:: interval
                        
                        	Hello interval for BFD sessions created by PIM
                        	**type**\:  int
                        
                        	**range:** 3..30000
                        
                        	**units**\: millisecond
                        
                        

                        """

                        _prefix = 'ipv4-pim-cfg'
                        _revision = '2016-06-01'

                        def __init__(self):
                            self.parent = None
                            self.detection_multiplier = None
                            self.enable = None
                            self.interval = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv4-pim-cfg:bfd'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.detection_multiplier is not None:
                                return True

                            if self.enable is not None:
                                return True

                            if self.interval is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_pim_cfg as meta
                            return meta._meta_table['Pim.DefaultContext.Ipv6.Interfaces.Interface.Bfd']['meta_info']

                    @property
                    def _common_path(self):
                        if self.interface_name is None:
                            raise YPYModelError('Key property interface_name is None')

                        return '/Cisco-IOS-XR-ipv4-pim-cfg:pim/Cisco-IOS-XR-ipv4-pim-cfg:default-context/Cisco-IOS-XR-ipv4-pim-cfg:ipv6/Cisco-IOS-XR-ipv4-pim-cfg:interfaces/Cisco-IOS-XR-ipv4-pim-cfg:interface[Cisco-IOS-XR-ipv4-pim-cfg:interface-name = ' + str(self.interface_name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.interface_name is not None:
                            return True

                        if self.bfd is not None and self.bfd._has_data():
                            return True

                        if self.bsr_border is not None:
                            return True

                        if self.dr_priority is not None:
                            return True

                        if self.enable is not None:
                            return True

                        if self.hello_interval is not None:
                            return True

                        if self.interface_enable is not None:
                            return True

                        if self.join_prune_mtu is not None:
                            return True

                        if self.jp_interval is not None:
                            return True

                        if self.maximum_routes is not None and self.maximum_routes._has_data():
                            return True

                        if self.neighbor_filter is not None:
                            return True

                        if self.override_interval is not None:
                            return True

                        if self.propagation_delay is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_pim_cfg as meta
                        return meta._meta_table['Pim.DefaultContext.Ipv6.Interfaces.Interface']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-ipv4-pim-cfg:pim/Cisco-IOS-XR-ipv4-pim-cfg:default-context/Cisco-IOS-XR-ipv4-pim-cfg:ipv6/Cisco-IOS-XR-ipv4-pim-cfg:interfaces'

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
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_pim_cfg as meta
                    return meta._meta_table['Pim.DefaultContext.Ipv6.Interfaces']['meta_info']


            class SparseModeRpAddresses(object):
                """
                Configure Sparse\-Mode Rendezvous Point
                
                .. attribute:: sparse_mode_rp_address
                
                	Address of the Rendezvous Point
                	**type**\: list of    :py:class:`SparseModeRpAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.DefaultContext.Ipv6.SparseModeRpAddresses.SparseModeRpAddress>`
                
                

                """

                _prefix = 'ipv4-pim-cfg'
                _revision = '2016-06-01'

                def __init__(self):
                    self.parent = None
                    self.sparse_mode_rp_address = YList()
                    self.sparse_mode_rp_address.parent = self
                    self.sparse_mode_rp_address.name = 'sparse_mode_rp_address'


                class SparseModeRpAddress(object):
                    """
                    Address of the Rendezvous Point
                    
                    .. attribute:: rp_address  <key>
                    
                    	RP address of Rendezvous Point
                    	**type**\: one of the below types:
                    
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    
                    ----
                    	**type**\:  str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    
                    ----
                    .. attribute:: access_list_name
                    
                    	Access list of groups that should map to a  given RP
                    	**type**\:  str
                    
                    	**length:** 1..64
                    
                    .. attribute:: auto_rp_override
                    
                    	TRUE Indicates if static RP config overrides AutoRP and BSR
                    	**type**\:  bool
                    
                    

                    """

                    _prefix = 'ipv4-pim-cfg'
                    _revision = '2016-06-01'

                    def __init__(self):
                        self.parent = None
                        self.rp_address = None
                        self.access_list_name = None
                        self.auto_rp_override = None

                    @property
                    def _common_path(self):
                        if self.rp_address is None:
                            raise YPYModelError('Key property rp_address is None')

                        return '/Cisco-IOS-XR-ipv4-pim-cfg:pim/Cisco-IOS-XR-ipv4-pim-cfg:default-context/Cisco-IOS-XR-ipv4-pim-cfg:ipv6/Cisco-IOS-XR-ipv4-pim-cfg:sparse-mode-rp-addresses/Cisco-IOS-XR-ipv4-pim-cfg:sparse-mode-rp-address[Cisco-IOS-XR-ipv4-pim-cfg:rp-address = ' + str(self.rp_address) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.rp_address is not None:
                            return True

                        if self.access_list_name is not None:
                            return True

                        if self.auto_rp_override is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_pim_cfg as meta
                        return meta._meta_table['Pim.DefaultContext.Ipv6.SparseModeRpAddresses.SparseModeRpAddress']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-ipv4-pim-cfg:pim/Cisco-IOS-XR-ipv4-pim-cfg:default-context/Cisco-IOS-XR-ipv4-pim-cfg:ipv6/Cisco-IOS-XR-ipv4-pim-cfg:sparse-mode-rp-addresses'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.sparse_mode_rp_address is not None:
                        for child_ref in self.sparse_mode_rp_address:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_pim_cfg as meta
                    return meta._meta_table['Pim.DefaultContext.Ipv6.SparseModeRpAddresses']['meta_info']


            class InheritableDefaults(object):
                """
                Inheritable defaults
                
                .. attribute:: convergency
                
                	Convergency timeout in seconds
                	**type**\:  int
                
                	**range:** 1800..2400
                
                	**units**\: second
                
                .. attribute:: dr_priority
                
                	Hello DR priority, preference given to larger value
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: hello_interval
                
                	Hello interval in seconds
                	**type**\:  int
                
                	**range:** 1..3600
                
                	**units**\: second
                
                .. attribute:: join_prune_mtu
                
                	Join\-Prune MTU in Bytes
                	**type**\:  int
                
                	**range:** 576..65535
                
                	**units**\: byte
                
                .. attribute:: jp_interval
                
                	Join\-Prune interval in seconds
                	**type**\:  int
                
                	**range:** 10..600
                
                	**units**\: second
                
                .. attribute:: override_interval
                
                	Override interval in milliseconds
                	**type**\:  int
                
                	**range:** 400..65535
                
                	**units**\: millisecond
                
                .. attribute:: propagation_delay
                
                	Propagation delay in milli seconds
                	**type**\:  int
                
                	**range:** 100..32767
                
                	**units**\: millisecond
                
                

                """

                _prefix = 'ipv4-pim-cfg'
                _revision = '2016-06-01'

                def __init__(self):
                    self.parent = None
                    self.convergency = None
                    self.dr_priority = None
                    self.hello_interval = None
                    self.join_prune_mtu = None
                    self.jp_interval = None
                    self.override_interval = None
                    self.propagation_delay = None

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-ipv4-pim-cfg:pim/Cisco-IOS-XR-ipv4-pim-cfg:default-context/Cisco-IOS-XR-ipv4-pim-cfg:ipv6/Cisco-IOS-XR-ipv4-pim-cfg:inheritable-defaults'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.convergency is not None:
                        return True

                    if self.dr_priority is not None:
                        return True

                    if self.hello_interval is not None:
                        return True

                    if self.join_prune_mtu is not None:
                        return True

                    if self.jp_interval is not None:
                        return True

                    if self.override_interval is not None:
                        return True

                    if self.propagation_delay is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_pim_cfg as meta
                    return meta._meta_table['Pim.DefaultContext.Ipv6.InheritableDefaults']['meta_info']


            class Rpf(object):
                """
                Configure RPF options
                
                .. attribute:: route_policy
                
                	Route policy to select RPF topology
                	**type**\:  str
                
                	**length:** 1..64
                
                

                """

                _prefix = 'ipv4-pim-cfg'
                _revision = '2016-06-01'

                def __init__(self):
                    self.parent = None
                    self.route_policy = None

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-ipv4-pim-cfg:pim/Cisco-IOS-XR-ipv4-pim-cfg:default-context/Cisco-IOS-XR-ipv4-pim-cfg:ipv6/Cisco-IOS-XR-ipv4-pim-cfg:rpf'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.route_policy is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_pim_cfg as meta
                    return meta._meta_table['Pim.DefaultContext.Ipv6.Rpf']['meta_info']


            class SgExpiryTimer(object):
                """
                Configure expiry timer for S,G routes
                
                .. attribute:: access_list_name
                
                	Access\-list of applicable S,G routes
                	**type**\:  str
                
                	**length:** 1..64
                
                .. attribute:: interval
                
                	(S,G) expiry time in seconds
                	**type**\:  int
                
                	**range:** 40..57600
                
                	**units**\: second
                
                

                """

                _prefix = 'ipv4-pim-cfg'
                _revision = '2016-06-01'

                def __init__(self):
                    self.parent = None
                    self.access_list_name = None
                    self.interval = None

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-ipv4-pim-cfg:pim/Cisco-IOS-XR-ipv4-pim-cfg:default-context/Cisco-IOS-XR-ipv4-pim-cfg:ipv6/Cisco-IOS-XR-ipv4-pim-cfg:sg-expiry-timer'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.access_list_name is not None:
                        return True

                    if self.interval is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_pim_cfg as meta
                    return meta._meta_table['Pim.DefaultContext.Ipv6.SgExpiryTimer']['meta_info']


            class RpfVectorEnable(object):
                """
                Enable PIM RPF Vector Proxy's
                
                .. attribute:: allow_ebgp
                
                	Allow RPF Vector origination over eBGP sessions
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: disable_ibgp
                
                	Disable RPF Vector origination over iBGP sessions
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: enable
                
                	RPF Vector is turned on if configured
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                	**mandatory**\: True
                
                .. attribute:: _is_presence
                
                	Is present if this instance represents presence container else not
                	**type**\: bool
                
                

                This class is a :ref:`presence class<presence-class>`

                """

                _prefix = 'ipv4-pim-cfg'
                _revision = '2016-06-01'

                def __init__(self):
                    self.parent = None
                    self._is_presence = True
                    self.allow_ebgp = None
                    self.disable_ibgp = None
                    self.enable = None

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-ipv4-pim-cfg:pim/Cisco-IOS-XR-ipv4-pim-cfg:default-context/Cisco-IOS-XR-ipv4-pim-cfg:ipv6/Cisco-IOS-XR-ipv4-pim-cfg:rpf-vector-enable'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self._is_presence:
                        return True
                    if self.allow_ebgp is not None:
                        return True

                    if self.disable_ibgp is not None:
                        return True

                    if self.enable is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_pim_cfg as meta
                    return meta._meta_table['Pim.DefaultContext.Ipv6.RpfVectorEnable']['meta_info']


            class Nsf(object):
                """
                Configure Non\-stop forwarding (NSF) options
                
                .. attribute:: lifetime
                
                	Override default maximum lifetime for PIM NSF mode
                	**type**\:  int
                
                	**range:** 10..600
                
                	**units**\: second
                
                

                """

                _prefix = 'ipv4-pim-cfg'
                _revision = '2016-06-01'

                def __init__(self):
                    self.parent = None
                    self.lifetime = None

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-ipv4-pim-cfg:pim/Cisco-IOS-XR-ipv4-pim-cfg:default-context/Cisco-IOS-XR-ipv4-pim-cfg:ipv6/Cisco-IOS-XR-ipv4-pim-cfg:nsf'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.lifetime is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_pim_cfg as meta
                    return meta._meta_table['Pim.DefaultContext.Ipv6.Nsf']['meta_info']


            class Maximum(object):
                """
                Configure PIM State Limits
                
                .. attribute:: bsr_candidate_rp_cache
                
                	Override default maximum and threshold for BSR C\-RP cache setting
                	**type**\:   :py:class:`BsrCandidateRpCache <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.DefaultContext.Ipv6.Maximum.BsrCandidateRpCache>`
                
                	**presence node**\: True
                
                .. attribute:: bsr_global_candidate_rp_cache
                
                	Override default global maximum and threshold for C\-RP set in BSR
                	**type**\:   :py:class:`BsrGlobalCandidateRpCache <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.DefaultContext.Ipv6.Maximum.BsrGlobalCandidateRpCache>`
                
                	**presence node**\: True
                
                .. attribute:: bsr_global_group_mappings
                
                	Override default global maximum and threshold for PIM group mapping ranges from BSR
                	**type**\:   :py:class:`BsrGlobalGroupMappings <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.DefaultContext.Ipv6.Maximum.BsrGlobalGroupMappings>`
                
                	**presence node**\: True
                
                .. attribute:: bsr_group_mappings
                
                	Override default maximum and threshold for number of group mappings from BSR
                	**type**\:   :py:class:`BsrGroupMappings <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.DefaultContext.Ipv6.Maximum.BsrGroupMappings>`
                
                	**presence node**\: True
                
                .. attribute:: global_group_mappings_auto_rp
                
                	Maximum for number of group mappings from autorp mapping agent
                	**type**\:   :py:class:`GlobalGroupMappingsAutoRp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.DefaultContext.Ipv6.Maximum.GlobalGroupMappingsAutoRp>`
                
                	**presence node**\: True
                
                .. attribute:: global_high_priority_packet_queue
                
                	Maximum packet queue size in bytes
                	**type**\:  int
                
                	**range:** 0..2147483648
                
                	**units**\: byte
                
                .. attribute:: global_low_priority_packet_queue
                
                	Maximum packet queue size in bytes
                	**type**\:  int
                
                	**range:** 0..2147483648
                
                	**units**\: byte
                
                .. attribute:: global_register_states
                
                	Override default maximum for number of sparse\-mode source registers
                	**type**\:   :py:class:`GlobalRegisterStates <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.DefaultContext.Ipv6.Maximum.GlobalRegisterStates>`
                
                	**presence node**\: True
                
                .. attribute:: global_route_interfaces
                
                	Override default maximum for number of route\-interfaces
                	**type**\:   :py:class:`GlobalRouteInterfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.DefaultContext.Ipv6.Maximum.GlobalRouteInterfaces>`
                
                	**presence node**\: True
                
                .. attribute:: global_routes
                
                	Override default maximum for number of routes
                	**type**\:   :py:class:`GlobalRoutes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.DefaultContext.Ipv6.Maximum.GlobalRoutes>`
                
                	**presence node**\: True
                
                .. attribute:: group_mappings_auto_rp
                
                	Override default maximum for number of group mappings from autorp mapping agent
                	**type**\:   :py:class:`GroupMappingsAutoRp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.DefaultContext.Ipv6.Maximum.GroupMappingsAutoRp>`
                
                	**presence node**\: True
                
                .. attribute:: register_states
                
                	Override default maximum for number of sparse\-mode source registers
                	**type**\:   :py:class:`RegisterStates <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.DefaultContext.Ipv6.Maximum.RegisterStates>`
                
                	**presence node**\: True
                
                .. attribute:: route_interfaces
                
                	Override default maximum for number of route\-interfaces
                	**type**\:   :py:class:`RouteInterfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.DefaultContext.Ipv6.Maximum.RouteInterfaces>`
                
                	**presence node**\: True
                
                .. attribute:: routes
                
                	Override default maximum for number of routes
                	**type**\:   :py:class:`Routes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.DefaultContext.Ipv6.Maximum.Routes>`
                
                	**presence node**\: True
                
                

                """

                _prefix = 'ipv4-pim-cfg'
                _revision = '2016-06-01'

                def __init__(self):
                    self.parent = None
                    self.bsr_candidate_rp_cache = None
                    self.bsr_global_candidate_rp_cache = None
                    self.bsr_global_group_mappings = None
                    self.bsr_group_mappings = None
                    self.global_group_mappings_auto_rp = None
                    self.global_high_priority_packet_queue = None
                    self.global_low_priority_packet_queue = None
                    self.global_register_states = None
                    self.global_route_interfaces = None
                    self.global_routes = None
                    self.group_mappings_auto_rp = None
                    self.register_states = None
                    self.route_interfaces = None
                    self.routes = None


                class BsrGlobalGroupMappings(object):
                    """
                    Override default global maximum and threshold
                    for PIM group mapping ranges from BSR
                    
                    .. attribute:: bsr_maximum_global_group_mappings
                    
                    	Global Maximum number of PIM group mapping ranges from BSR
                    	**type**\:  int
                    
                    	**range:** 1..10000
                    
                    	**mandatory**\: True
                    
                    .. attribute:: warning_threshold
                    
                    	Set threshold to print warning
                    	**type**\:  int
                    
                    	**range:** 1..10000
                    
                    	**default value**\: 500
                    
                    .. attribute:: _is_presence
                    
                    	Is present if this instance represents presence container else not
                    	**type**\: bool
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'ipv4-pim-cfg'
                    _revision = '2016-06-01'

                    def __init__(self):
                        self.parent = None
                        self._is_presence = True
                        self.bsr_maximum_global_group_mappings = None
                        self.warning_threshold = None

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-ipv4-pim-cfg:pim/Cisco-IOS-XR-ipv4-pim-cfg:default-context/Cisco-IOS-XR-ipv4-pim-cfg:ipv6/Cisco-IOS-XR-ipv4-pim-cfg:maximum/Cisco-IOS-XR-ipv4-pim-cfg:bsr-global-group-mappings'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self._is_presence:
                            return True
                        if self.bsr_maximum_global_group_mappings is not None:
                            return True

                        if self.warning_threshold is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_pim_cfg as meta
                        return meta._meta_table['Pim.DefaultContext.Ipv6.Maximum.BsrGlobalGroupMappings']['meta_info']


                class GlobalRoutes(object):
                    """
                    Override default maximum for number of routes
                    
                    .. attribute:: maximum_routes
                    
                    	Maximum number of PIM routes
                    	**type**\:  int
                    
                    	**range:** 1..200000
                    
                    	**mandatory**\: True
                    
                    .. attribute:: warning_threshold
                    
                    	Set threshold to print warning
                    	**type**\:  int
                    
                    	**range:** 1..200000
                    
                    	**default value**\: 100000
                    
                    .. attribute:: _is_presence
                    
                    	Is present if this instance represents presence container else not
                    	**type**\: bool
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'ipv4-pim-cfg'
                    _revision = '2016-06-01'

                    def __init__(self):
                        self.parent = None
                        self._is_presence = True
                        self.maximum_routes = None
                        self.warning_threshold = None

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-ipv4-pim-cfg:pim/Cisco-IOS-XR-ipv4-pim-cfg:default-context/Cisco-IOS-XR-ipv4-pim-cfg:ipv6/Cisco-IOS-XR-ipv4-pim-cfg:maximum/Cisco-IOS-XR-ipv4-pim-cfg:global-routes'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self._is_presence:
                            return True
                        if self.maximum_routes is not None:
                            return True

                        if self.warning_threshold is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_pim_cfg as meta
                        return meta._meta_table['Pim.DefaultContext.Ipv6.Maximum.GlobalRoutes']['meta_info']


                class GlobalGroupMappingsAutoRp(object):
                    """
                    Maximum for number of group mappings from
                    autorp mapping agent
                    
                    .. attribute:: maximum_global_group_ranges_auto_rp
                    
                    	Maximum number of PIM group mappings from autorp
                    	**type**\:  int
                    
                    	**range:** 1..10000
                    
                    	**mandatory**\: True
                    
                    .. attribute:: threshold_global_group_ranges_auto_rp
                    
                    	Warning threshold number of PIM group mappings from autorp
                    	**type**\:  int
                    
                    	**range:** 1..10000
                    
                    	**default value**\: 450
                    
                    .. attribute:: _is_presence
                    
                    	Is present if this instance represents presence container else not
                    	**type**\: bool
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'ipv4-pim-cfg'
                    _revision = '2016-06-01'

                    def __init__(self):
                        self.parent = None
                        self._is_presence = True
                        self.maximum_global_group_ranges_auto_rp = None
                        self.threshold_global_group_ranges_auto_rp = None

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-ipv4-pim-cfg:pim/Cisco-IOS-XR-ipv4-pim-cfg:default-context/Cisco-IOS-XR-ipv4-pim-cfg:ipv6/Cisco-IOS-XR-ipv4-pim-cfg:maximum/Cisco-IOS-XR-ipv4-pim-cfg:global-group-mappings-auto-rp'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self._is_presence:
                            return True
                        if self.maximum_global_group_ranges_auto_rp is not None:
                            return True

                        if self.threshold_global_group_ranges_auto_rp is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_pim_cfg as meta
                        return meta._meta_table['Pim.DefaultContext.Ipv6.Maximum.GlobalGroupMappingsAutoRp']['meta_info']


                class BsrGlobalCandidateRpCache(object):
                    """
                    Override default global maximum and threshold
                    for C\-RP set in BSR
                    
                    .. attribute:: bsr_maximum_global_candidate_rp_cache
                    
                    	Global Maximum number of PIM C\-RP Sets from BSR
                    	**type**\:  int
                    
                    	**range:** 1..10000
                    
                    	**mandatory**\: True
                    
                    .. attribute:: warning_threshold
                    
                    	Set threshold to print warning
                    	**type**\:  int
                    
                    	**range:** 1..10000
                    
                    	**default value**\: 100
                    
                    .. attribute:: _is_presence
                    
                    	Is present if this instance represents presence container else not
                    	**type**\: bool
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'ipv4-pim-cfg'
                    _revision = '2016-06-01'

                    def __init__(self):
                        self.parent = None
                        self._is_presence = True
                        self.bsr_maximum_global_candidate_rp_cache = None
                        self.warning_threshold = None

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-ipv4-pim-cfg:pim/Cisco-IOS-XR-ipv4-pim-cfg:default-context/Cisco-IOS-XR-ipv4-pim-cfg:ipv6/Cisco-IOS-XR-ipv4-pim-cfg:maximum/Cisco-IOS-XR-ipv4-pim-cfg:bsr-global-candidate-rp-cache'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self._is_presence:
                            return True
                        if self.bsr_maximum_global_candidate_rp_cache is not None:
                            return True

                        if self.warning_threshold is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_pim_cfg as meta
                        return meta._meta_table['Pim.DefaultContext.Ipv6.Maximum.BsrGlobalCandidateRpCache']['meta_info']


                class GlobalRegisterStates(object):
                    """
                    Override default maximum for number of
                    sparse\-mode source registers
                    
                    .. attribute:: maximum_register_states
                    
                    	Maximum number of PIM Sparse\-Mode register states
                    	**type**\:  int
                    
                    	**range:** 0..75000
                    
                    	**mandatory**\: True
                    
                    .. attribute:: warning_threshold
                    
                    	Set threshold to print warning
                    	**type**\:  int
                    
                    	**range:** 0..75000
                    
                    	**default value**\: 20000
                    
                    .. attribute:: _is_presence
                    
                    	Is present if this instance represents presence container else not
                    	**type**\: bool
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'ipv4-pim-cfg'
                    _revision = '2016-06-01'

                    def __init__(self):
                        self.parent = None
                        self._is_presence = True
                        self.maximum_register_states = None
                        self.warning_threshold = None

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-ipv4-pim-cfg:pim/Cisco-IOS-XR-ipv4-pim-cfg:default-context/Cisco-IOS-XR-ipv4-pim-cfg:ipv6/Cisco-IOS-XR-ipv4-pim-cfg:maximum/Cisco-IOS-XR-ipv4-pim-cfg:global-register-states'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self._is_presence:
                            return True
                        if self.maximum_register_states is not None:
                            return True

                        if self.warning_threshold is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_pim_cfg as meta
                        return meta._meta_table['Pim.DefaultContext.Ipv6.Maximum.GlobalRegisterStates']['meta_info']


                class GlobalRouteInterfaces(object):
                    """
                    Override default maximum for number of
                    route\-interfaces
                    
                    .. attribute:: maximum_route_interfaces
                    
                    	Maximum number of PIM route\-interfaces
                    	**type**\:  int
                    
                    	**range:** 1..1100000
                    
                    	**mandatory**\: True
                    
                    .. attribute:: warning_threshold
                    
                    	Set threshold to print warning
                    	**type**\:  int
                    
                    	**range:** 1..1100000
                    
                    	**default value**\: 300000
                    
                    .. attribute:: _is_presence
                    
                    	Is present if this instance represents presence container else not
                    	**type**\: bool
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'ipv4-pim-cfg'
                    _revision = '2016-06-01'

                    def __init__(self):
                        self.parent = None
                        self._is_presence = True
                        self.maximum_route_interfaces = None
                        self.warning_threshold = None

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-ipv4-pim-cfg:pim/Cisco-IOS-XR-ipv4-pim-cfg:default-context/Cisco-IOS-XR-ipv4-pim-cfg:ipv6/Cisco-IOS-XR-ipv4-pim-cfg:maximum/Cisco-IOS-XR-ipv4-pim-cfg:global-route-interfaces'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self._is_presence:
                            return True
                        if self.maximum_route_interfaces is not None:
                            return True

                        if self.warning_threshold is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_pim_cfg as meta
                        return meta._meta_table['Pim.DefaultContext.Ipv6.Maximum.GlobalRouteInterfaces']['meta_info']


                class GroupMappingsAutoRp(object):
                    """
                    Override default maximum for number of group
                    mappings from autorp mapping agent
                    
                    .. attribute:: maximum_group_ranges_auto_rp
                    
                    	Maximum number of PIM group mappings from autorp
                    	**type**\:  int
                    
                    	**range:** 1..10000
                    
                    	**mandatory**\: True
                    
                    .. attribute:: threshold_group_ranges_auto_rp
                    
                    	Warning threshold number of PIM group mappings from autorp
                    	**type**\:  int
                    
                    	**range:** 1..10000
                    
                    	**default value**\: 450
                    
                    .. attribute:: _is_presence
                    
                    	Is present if this instance represents presence container else not
                    	**type**\: bool
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'ipv4-pim-cfg'
                    _revision = '2016-06-01'

                    def __init__(self):
                        self.parent = None
                        self._is_presence = True
                        self.maximum_group_ranges_auto_rp = None
                        self.threshold_group_ranges_auto_rp = None

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-ipv4-pim-cfg:pim/Cisco-IOS-XR-ipv4-pim-cfg:default-context/Cisco-IOS-XR-ipv4-pim-cfg:ipv6/Cisco-IOS-XR-ipv4-pim-cfg:maximum/Cisco-IOS-XR-ipv4-pim-cfg:group-mappings-auto-rp'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self._is_presence:
                            return True
                        if self.maximum_group_ranges_auto_rp is not None:
                            return True

                        if self.threshold_group_ranges_auto_rp is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_pim_cfg as meta
                        return meta._meta_table['Pim.DefaultContext.Ipv6.Maximum.GroupMappingsAutoRp']['meta_info']


                class BsrGroupMappings(object):
                    """
                    Override default maximum and threshold for
                    number of group mappings from BSR
                    
                    .. attribute:: bsr_maximum_group_ranges
                    
                    	Maximum number of PIM group mappings from BSR
                    	**type**\:  int
                    
                    	**range:** 1..10000
                    
                    	**mandatory**\: True
                    
                    .. attribute:: warning_threshold
                    
                    	Set threshold to print warning
                    	**type**\:  int
                    
                    	**range:** 1..10000
                    
                    	**default value**\: 500
                    
                    .. attribute:: _is_presence
                    
                    	Is present if this instance represents presence container else not
                    	**type**\: bool
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'ipv4-pim-cfg'
                    _revision = '2016-06-01'

                    def __init__(self):
                        self.parent = None
                        self._is_presence = True
                        self.bsr_maximum_group_ranges = None
                        self.warning_threshold = None

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-ipv4-pim-cfg:pim/Cisco-IOS-XR-ipv4-pim-cfg:default-context/Cisco-IOS-XR-ipv4-pim-cfg:ipv6/Cisco-IOS-XR-ipv4-pim-cfg:maximum/Cisco-IOS-XR-ipv4-pim-cfg:bsr-group-mappings'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self._is_presence:
                            return True
                        if self.bsr_maximum_group_ranges is not None:
                            return True

                        if self.warning_threshold is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_pim_cfg as meta
                        return meta._meta_table['Pim.DefaultContext.Ipv6.Maximum.BsrGroupMappings']['meta_info']


                class RegisterStates(object):
                    """
                    Override default maximum for number of
                    sparse\-mode source registers
                    
                    .. attribute:: maximum_register_states
                    
                    	Maximum number of PIM Sparse\-Mode register states
                    	**type**\:  int
                    
                    	**range:** 0..75000
                    
                    	**mandatory**\: True
                    
                    .. attribute:: warning_threshold
                    
                    	Set threshold to print warning
                    	**type**\:  int
                    
                    	**range:** 0..75000
                    
                    	**default value**\: 20000
                    
                    .. attribute:: _is_presence
                    
                    	Is present if this instance represents presence container else not
                    	**type**\: bool
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'ipv4-pim-cfg'
                    _revision = '2016-06-01'

                    def __init__(self):
                        self.parent = None
                        self._is_presence = True
                        self.maximum_register_states = None
                        self.warning_threshold = None

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-ipv4-pim-cfg:pim/Cisco-IOS-XR-ipv4-pim-cfg:default-context/Cisco-IOS-XR-ipv4-pim-cfg:ipv6/Cisco-IOS-XR-ipv4-pim-cfg:maximum/Cisco-IOS-XR-ipv4-pim-cfg:register-states'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self._is_presence:
                            return True
                        if self.maximum_register_states is not None:
                            return True

                        if self.warning_threshold is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_pim_cfg as meta
                        return meta._meta_table['Pim.DefaultContext.Ipv6.Maximum.RegisterStates']['meta_info']


                class RouteInterfaces(object):
                    """
                    Override default maximum for number of
                    route\-interfaces
                    
                    .. attribute:: maximum_route_interfaces
                    
                    	Maximum number of PIM route\-interfaces
                    	**type**\:  int
                    
                    	**range:** 1..1100000
                    
                    	**mandatory**\: True
                    
                    .. attribute:: warning_threshold
                    
                    	Set threshold to print warning
                    	**type**\:  int
                    
                    	**range:** 1..1100000
                    
                    	**default value**\: 300000
                    
                    .. attribute:: _is_presence
                    
                    	Is present if this instance represents presence container else not
                    	**type**\: bool
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'ipv4-pim-cfg'
                    _revision = '2016-06-01'

                    def __init__(self):
                        self.parent = None
                        self._is_presence = True
                        self.maximum_route_interfaces = None
                        self.warning_threshold = None

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-ipv4-pim-cfg:pim/Cisco-IOS-XR-ipv4-pim-cfg:default-context/Cisco-IOS-XR-ipv4-pim-cfg:ipv6/Cisco-IOS-XR-ipv4-pim-cfg:maximum/Cisco-IOS-XR-ipv4-pim-cfg:route-interfaces'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self._is_presence:
                            return True
                        if self.maximum_route_interfaces is not None:
                            return True

                        if self.warning_threshold is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_pim_cfg as meta
                        return meta._meta_table['Pim.DefaultContext.Ipv6.Maximum.RouteInterfaces']['meta_info']


                class BsrCandidateRpCache(object):
                    """
                    Override default maximum and threshold for BSR
                    C\-RP cache setting
                    
                    .. attribute:: bsr_maximum_candidate_rp_cache
                    
                    	Maximum number of BSR C\-RP cache setting
                    	**type**\:  int
                    
                    	**range:** 1..10000
                    
                    	**mandatory**\: True
                    
                    .. attribute:: warning_threshold
                    
                    	Set threshold to print warning
                    	**type**\:  int
                    
                    	**range:** 1..10000
                    
                    	**default value**\: 100
                    
                    .. attribute:: _is_presence
                    
                    	Is present if this instance represents presence container else not
                    	**type**\: bool
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'ipv4-pim-cfg'
                    _revision = '2016-06-01'

                    def __init__(self):
                        self.parent = None
                        self._is_presence = True
                        self.bsr_maximum_candidate_rp_cache = None
                        self.warning_threshold = None

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-ipv4-pim-cfg:pim/Cisco-IOS-XR-ipv4-pim-cfg:default-context/Cisco-IOS-XR-ipv4-pim-cfg:ipv6/Cisco-IOS-XR-ipv4-pim-cfg:maximum/Cisco-IOS-XR-ipv4-pim-cfg:bsr-candidate-rp-cache'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self._is_presence:
                            return True
                        if self.bsr_maximum_candidate_rp_cache is not None:
                            return True

                        if self.warning_threshold is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_pim_cfg as meta
                        return meta._meta_table['Pim.DefaultContext.Ipv6.Maximum.BsrCandidateRpCache']['meta_info']


                class Routes(object):
                    """
                    Override default maximum for number of routes
                    
                    .. attribute:: maximum_routes
                    
                    	Maximum number of PIM routes
                    	**type**\:  int
                    
                    	**range:** 1..200000
                    
                    	**mandatory**\: True
                    
                    .. attribute:: warning_threshold
                    
                    	Set threshold to print warning
                    	**type**\:  int
                    
                    	**range:** 1..200000
                    
                    	**default value**\: 100000
                    
                    .. attribute:: _is_presence
                    
                    	Is present if this instance represents presence container else not
                    	**type**\: bool
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'ipv4-pim-cfg'
                    _revision = '2016-06-01'

                    def __init__(self):
                        self.parent = None
                        self._is_presence = True
                        self.maximum_routes = None
                        self.warning_threshold = None

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-ipv4-pim-cfg:pim/Cisco-IOS-XR-ipv4-pim-cfg:default-context/Cisco-IOS-XR-ipv4-pim-cfg:ipv6/Cisco-IOS-XR-ipv4-pim-cfg:maximum/Cisco-IOS-XR-ipv4-pim-cfg:routes'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self._is_presence:
                            return True
                        if self.maximum_routes is not None:
                            return True

                        if self.warning_threshold is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_pim_cfg as meta
                        return meta._meta_table['Pim.DefaultContext.Ipv6.Maximum.Routes']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-ipv4-pim-cfg:pim/Cisco-IOS-XR-ipv4-pim-cfg:default-context/Cisco-IOS-XR-ipv4-pim-cfg:ipv6/Cisco-IOS-XR-ipv4-pim-cfg:maximum'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.bsr_candidate_rp_cache is not None and self.bsr_candidate_rp_cache._has_data():
                        return True

                    if self.bsr_global_candidate_rp_cache is not None and self.bsr_global_candidate_rp_cache._has_data():
                        return True

                    if self.bsr_global_group_mappings is not None and self.bsr_global_group_mappings._has_data():
                        return True

                    if self.bsr_group_mappings is not None and self.bsr_group_mappings._has_data():
                        return True

                    if self.global_group_mappings_auto_rp is not None and self.global_group_mappings_auto_rp._has_data():
                        return True

                    if self.global_high_priority_packet_queue is not None:
                        return True

                    if self.global_low_priority_packet_queue is not None:
                        return True

                    if self.global_register_states is not None and self.global_register_states._has_data():
                        return True

                    if self.global_route_interfaces is not None and self.global_route_interfaces._has_data():
                        return True

                    if self.global_routes is not None and self.global_routes._has_data():
                        return True

                    if self.group_mappings_auto_rp is not None and self.group_mappings_auto_rp._has_data():
                        return True

                    if self.register_states is not None and self.register_states._has_data():
                        return True

                    if self.route_interfaces is not None and self.route_interfaces._has_data():
                        return True

                    if self.routes is not None and self.routes._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_pim_cfg as meta
                    return meta._meta_table['Pim.DefaultContext.Ipv6.Maximum']['meta_info']


            class Ssm(object):
                """
                Configure IP Multicast SSM
                
                .. attribute:: disable
                
                	TRUE if SSM is disabled on this router
                	**type**\:  bool
                
                	**default value**\: false
                
                .. attribute:: range
                
                	Access list of groups enabled with SSM
                	**type**\:  str
                
                	**length:** 1..64
                
                

                """

                _prefix = 'ipv4-pim-cfg'
                _revision = '2016-06-01'

                def __init__(self):
                    self.parent = None
                    self.disable = None
                    self.range = None

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-ipv4-pim-cfg:pim/Cisco-IOS-XR-ipv4-pim-cfg:default-context/Cisco-IOS-XR-ipv4-pim-cfg:ipv6/Cisco-IOS-XR-ipv4-pim-cfg:ssm'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.disable is not None:
                        return True

                    if self.range is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_pim_cfg as meta
                    return meta._meta_table['Pim.DefaultContext.Ipv6.Ssm']['meta_info']


            class BidirRpAddresses(object):
                """
                Configure Bidirectional PIM Rendezvous Point
                
                .. attribute:: bidir_rp_address
                
                	Address of the Rendezvous Point
                	**type**\: list of    :py:class:`BidirRpAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.DefaultContext.Ipv6.BidirRpAddresses.BidirRpAddress>`
                
                

                """

                _prefix = 'ipv4-pim-cfg'
                _revision = '2016-06-01'

                def __init__(self):
                    self.parent = None
                    self.bidir_rp_address = YList()
                    self.bidir_rp_address.parent = self
                    self.bidir_rp_address.name = 'bidir_rp_address'


                class BidirRpAddress(object):
                    """
                    Address of the Rendezvous Point
                    
                    .. attribute:: rp_address  <key>
                    
                    	RP address of Rendezvous Point
                    	**type**\: one of the below types:
                    
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    
                    ----
                    	**type**\:  str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    
                    ----
                    .. attribute:: access_list_name
                    
                    	Access list of groups that should map to a given RP
                    	**type**\:  str
                    
                    	**length:** 1..64
                    
                    .. attribute:: auto_rp_override
                    
                    	TRUE Indicates if static RP config overrides AutoRP and BSR
                    	**type**\:  bool
                    
                    

                    """

                    _prefix = 'ipv4-pim-cfg'
                    _revision = '2016-06-01'

                    def __init__(self):
                        self.parent = None
                        self.rp_address = None
                        self.access_list_name = None
                        self.auto_rp_override = None

                    @property
                    def _common_path(self):
                        if self.rp_address is None:
                            raise YPYModelError('Key property rp_address is None')

                        return '/Cisco-IOS-XR-ipv4-pim-cfg:pim/Cisco-IOS-XR-ipv4-pim-cfg:default-context/Cisco-IOS-XR-ipv4-pim-cfg:ipv6/Cisco-IOS-XR-ipv4-pim-cfg:bidir-rp-addresses/Cisco-IOS-XR-ipv4-pim-cfg:bidir-rp-address[Cisco-IOS-XR-ipv4-pim-cfg:rp-address = ' + str(self.rp_address) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.rp_address is not None:
                            return True

                        if self.access_list_name is not None:
                            return True

                        if self.auto_rp_override is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_pim_cfg as meta
                        return meta._meta_table['Pim.DefaultContext.Ipv6.BidirRpAddresses.BidirRpAddress']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-ipv4-pim-cfg:pim/Cisco-IOS-XR-ipv4-pim-cfg:default-context/Cisco-IOS-XR-ipv4-pim-cfg:ipv6/Cisco-IOS-XR-ipv4-pim-cfg:bidir-rp-addresses'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.bidir_rp_address is not None:
                        for child_ref in self.bidir_rp_address:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_pim_cfg as meta
                    return meta._meta_table['Pim.DefaultContext.Ipv6.BidirRpAddresses']['meta_info']


            class Bsr(object):
                """
                PIM BSR configuration
                
                .. attribute:: candidate_bsr
                
                	PIM Candidate BSR configuration
                	**type**\:   :py:class:`CandidateBsr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.DefaultContext.Ipv6.Bsr.CandidateBsr>`
                
                	**presence node**\: True
                
                .. attribute:: candidate_rps
                
                	PIM RP configuration
                	**type**\:   :py:class:`CandidateRps <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.DefaultContext.Ipv6.Bsr.CandidateRps>`
                
                

                """

                _prefix = 'ipv4-pim-cfg'
                _revision = '2016-06-01'

                def __init__(self):
                    self.parent = None
                    self.candidate_bsr = None
                    self.candidate_rps = Pim.DefaultContext.Ipv6.Bsr.CandidateRps()
                    self.candidate_rps.parent = self


                class CandidateBsr(object):
                    """
                    PIM Candidate BSR configuration
                    
                    .. attribute:: address
                    
                    	BSR Address configured
                    	**type**\:  str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    	**mandatory**\: True
                    
                    .. attribute:: prefix_length
                    
                    	Hash Mask Length for this candidate BSR
                    	**type**\:  int
                    
                    	**range:** 0..128
                    
                    	**default value**\: 126
                    
                    .. attribute:: priority
                    
                    	Priority of the Candidate BSR
                    	**type**\:  int
                    
                    	**range:** 1..255
                    
                    	**default value**\: 1
                    
                    .. attribute:: _is_presence
                    
                    	Is present if this instance represents presence container else not
                    	**type**\: bool
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'ipv4-pim-cfg'
                    _revision = '2016-06-01'

                    def __init__(self):
                        self.parent = None
                        self._is_presence = True
                        self.address = None
                        self.prefix_length = None
                        self.priority = None

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-ipv4-pim-cfg:pim/Cisco-IOS-XR-ipv4-pim-cfg:default-context/Cisco-IOS-XR-ipv4-pim-cfg:ipv6/Cisco-IOS-XR-ipv4-pim-cfg:bsr/Cisco-IOS-XR-ipv4-pim-cfg:candidate-bsr'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self._is_presence:
                            return True
                        if self.address is not None:
                            return True

                        if self.prefix_length is not None:
                            return True

                        if self.priority is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_pim_cfg as meta
                        return meta._meta_table['Pim.DefaultContext.Ipv6.Bsr.CandidateBsr']['meta_info']


                class CandidateRps(object):
                    """
                    PIM RP configuration
                    
                    .. attribute:: candidate_rp
                    
                    	Address of PIM SM BSR Candidate\-RP
                    	**type**\: list of    :py:class:`CandidateRp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.DefaultContext.Ipv6.Bsr.CandidateRps.CandidateRp>`
                    
                    

                    """

                    _prefix = 'ipv4-pim-cfg'
                    _revision = '2016-06-01'

                    def __init__(self):
                        self.parent = None
                        self.candidate_rp = YList()
                        self.candidate_rp.parent = self
                        self.candidate_rp.name = 'candidate_rp'


                    class CandidateRp(object):
                        """
                        Address of PIM SM BSR Candidate\-RP
                        
                        .. attribute:: address  <key>
                        
                        	Address of Candidate\-RP
                        	**type**\: one of the below types:
                        
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        .. attribute:: mode  <key>
                        
                        	SM or Bidir
                        	**type**\:   :py:class:`PimProtocolModeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.PimProtocolModeEnum>`
                        
                        .. attribute:: group_list
                        
                        	Access\-list specifying the group range for the Candidate\-RP
                        	**type**\:  str
                        
                        	**length:** 1..64
                        
                        .. attribute:: interval
                        
                        	Advertisement interval
                        	**type**\:  int
                        
                        	**range:** 30..600
                        
                        	**default value**\: 60
                        
                        .. attribute:: priority
                        
                        	Priority of the CRP
                        	**type**\:  int
                        
                        	**range:** 1..255
                        
                        	**default value**\: 192
                        
                        

                        """

                        _prefix = 'ipv4-pim-cfg'
                        _revision = '2016-06-01'

                        def __init__(self):
                            self.parent = None
                            self.address = None
                            self.mode = None
                            self.group_list = None
                            self.interval = None
                            self.priority = None

                        @property
                        def _common_path(self):
                            if self.address is None:
                                raise YPYModelError('Key property address is None')
                            if self.mode is None:
                                raise YPYModelError('Key property mode is None')

                            return '/Cisco-IOS-XR-ipv4-pim-cfg:pim/Cisco-IOS-XR-ipv4-pim-cfg:default-context/Cisco-IOS-XR-ipv4-pim-cfg:ipv6/Cisco-IOS-XR-ipv4-pim-cfg:bsr/Cisco-IOS-XR-ipv4-pim-cfg:candidate-rps/Cisco-IOS-XR-ipv4-pim-cfg:candidate-rp[Cisco-IOS-XR-ipv4-pim-cfg:address = ' + str(self.address) + '][Cisco-IOS-XR-ipv4-pim-cfg:mode = ' + str(self.mode) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.address is not None:
                                return True

                            if self.mode is not None:
                                return True

                            if self.group_list is not None:
                                return True

                            if self.interval is not None:
                                return True

                            if self.priority is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_pim_cfg as meta
                            return meta._meta_table['Pim.DefaultContext.Ipv6.Bsr.CandidateRps.CandidateRp']['meta_info']

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-ipv4-pim-cfg:pim/Cisco-IOS-XR-ipv4-pim-cfg:default-context/Cisco-IOS-XR-ipv4-pim-cfg:ipv6/Cisco-IOS-XR-ipv4-pim-cfg:bsr/Cisco-IOS-XR-ipv4-pim-cfg:candidate-rps'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.candidate_rp is not None:
                            for child_ref in self.candidate_rp:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_pim_cfg as meta
                        return meta._meta_table['Pim.DefaultContext.Ipv6.Bsr.CandidateRps']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-ipv4-pim-cfg:pim/Cisco-IOS-XR-ipv4-pim-cfg:default-context/Cisco-IOS-XR-ipv4-pim-cfg:ipv6/Cisco-IOS-XR-ipv4-pim-cfg:bsr'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.candidate_bsr is not None and self.candidate_bsr._has_data():
                        return True

                    if self.candidate_rps is not None and self.candidate_rps._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_pim_cfg as meta
                    return meta._meta_table['Pim.DefaultContext.Ipv6.Bsr']['meta_info']


            class AllowRp(object):
                """
                Enable allow\-rp filtering for SM joins
                
                .. attribute:: group_list_name
                
                	Access\-list specifiying applicable groups
                	**type**\:  str
                
                	**length:** 1..64
                
                .. attribute:: rp_list_name
                
                	Access\-list specifiying applicable RPs
                	**type**\:  str
                
                	**length:** 1..64
                
                .. attribute:: _is_presence
                
                	Is present if this instance represents presence container else not
                	**type**\: bool
                
                

                This class is a :ref:`presence class<presence-class>`

                """

                _prefix = 'ipv4-pim-cfg'
                _revision = '2016-06-01'

                def __init__(self):
                    self.parent = None
                    self._is_presence = True
                    self.group_list_name = None
                    self.rp_list_name = None

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-ipv4-pim-cfg:pim/Cisco-IOS-XR-ipv4-pim-cfg:default-context/Cisco-IOS-XR-ipv4-pim-cfg:ipv6/Cisco-IOS-XR-ipv4-pim-cfg:allow-rp'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self._is_presence:
                        return True
                    if self.group_list_name is not None:
                        return True

                    if self.rp_list_name is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_pim_cfg as meta
                    return meta._meta_table['Pim.DefaultContext.Ipv6.AllowRp']['meta_info']


            class EmbeddedRpAddresses(object):
                """
                Set Embedded RP processing support
                
                .. attribute:: embedded_rp_address
                
                	Set Embedded RP processing support
                	**type**\: list of    :py:class:`EmbeddedRpAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.DefaultContext.Ipv6.EmbeddedRpAddresses.EmbeddedRpAddress>`
                
                

                """

                _prefix = 'ipv4-pim-cfg'
                _revision = '2016-06-01'

                def __init__(self):
                    self.parent = None
                    self.embedded_rp_address = YList()
                    self.embedded_rp_address.parent = self
                    self.embedded_rp_address.name = 'embedded_rp_address'


                class EmbeddedRpAddress(object):
                    """
                    Set Embedded RP processing support
                    
                    .. attribute:: rp_address  <key>
                    
                    	RP address of the Rendezvous Point
                    	**type**\: one of the below types:
                    
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    
                    ----
                    	**type**\:  str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    
                    ----
                    .. attribute:: access_list_name
                    
                    	Access list of groups that should map to a given RP
                    	**type**\:  str
                    
                    	**length:** 1..64
                    
                    	**mandatory**\: True
                    
                    

                    """

                    _prefix = 'ipv4-pim-cfg'
                    _revision = '2016-06-01'

                    def __init__(self):
                        self.parent = None
                        self.rp_address = None
                        self.access_list_name = None

                    @property
                    def _common_path(self):
                        if self.rp_address is None:
                            raise YPYModelError('Key property rp_address is None')

                        return '/Cisco-IOS-XR-ipv4-pim-cfg:pim/Cisco-IOS-XR-ipv4-pim-cfg:default-context/Cisco-IOS-XR-ipv4-pim-cfg:ipv6/Cisco-IOS-XR-ipv4-pim-cfg:embedded-rp-addresses/Cisco-IOS-XR-ipv4-pim-cfg:embedded-rp-address[Cisco-IOS-XR-ipv4-pim-cfg:rp-address = ' + str(self.rp_address) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.rp_address is not None:
                            return True

                        if self.access_list_name is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_pim_cfg as meta
                        return meta._meta_table['Pim.DefaultContext.Ipv6.EmbeddedRpAddresses.EmbeddedRpAddress']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-ipv4-pim-cfg:pim/Cisco-IOS-XR-ipv4-pim-cfg:default-context/Cisco-IOS-XR-ipv4-pim-cfg:ipv6/Cisco-IOS-XR-ipv4-pim-cfg:embedded-rp-addresses'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.embedded_rp_address is not None:
                        for child_ref in self.embedded_rp_address:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_pim_cfg as meta
                    return meta._meta_table['Pim.DefaultContext.Ipv6.EmbeddedRpAddresses']['meta_info']


            class Convergence(object):
                """
                Configure convergence parameters
                
                .. attribute:: link_down_prune_delay
                
                	Delay prunes if route join state transitions to not\-joined on link down
                	**type**\:  int
                
                	**range:** 0..60
                
                	**units**\: second
                
                .. attribute:: rpf_conflict_join_delay
                
                	Dampen first join if RPF path is through one of the downstream neighbor
                	**type**\:  int
                
                	**range:** 0..15
                
                	**units**\: second
                
                

                """

                _prefix = 'ipv4-pim-cfg'
                _revision = '2016-06-01'

                def __init__(self):
                    self.parent = None
                    self.link_down_prune_delay = None
                    self.rpf_conflict_join_delay = None

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-ipv4-pim-cfg:pim/Cisco-IOS-XR-ipv4-pim-cfg:default-context/Cisco-IOS-XR-ipv4-pim-cfg:ipv6/Cisco-IOS-XR-ipv4-pim-cfg:convergence'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.link_down_prune_delay is not None:
                        return True

                    if self.rpf_conflict_join_delay is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_pim_cfg as meta
                    return meta._meta_table['Pim.DefaultContext.Ipv6.Convergence']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-ipv4-pim-cfg:pim/Cisco-IOS-XR-ipv4-pim-cfg:default-context/Cisco-IOS-XR-ipv4-pim-cfg:ipv6'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.accept_register is not None:
                    return True

                if self.allow_rp is not None and self.allow_rp._has_data():
                    return True

                if self.bidir_rp_addresses is not None and self.bidir_rp_addresses._has_data():
                    return True

                if self.bsr is not None and self.bsr._has_data():
                    return True

                if self.convergence is not None and self.convergence._has_data():
                    return True

                if self.embedded_rp_addresses is not None and self.embedded_rp_addresses._has_data():
                    return True

                if self.embedded_rp_disable is not None:
                    return True

                if self.inheritable_defaults is not None and self.inheritable_defaults._has_data():
                    return True

                if self.interfaces is not None and self.interfaces._has_data():
                    return True

                if self.log_neighbor_changes is not None:
                    return True

                if self.maximum is not None and self.maximum._has_data():
                    return True

                if self.multipath is not None:
                    return True

                if self.neighbor_check_on_receive is not None:
                    return True

                if self.neighbor_check_on_send is not None:
                    return True

                if self.neighbor_filter is not None:
                    return True

                if self.nsf is not None and self.nsf._has_data():
                    return True

                if self.old_register_checksum is not None:
                    return True

                if self.register_source is not None:
                    return True

                if self.rp_static_deny is not None:
                    return True

                if self.rpf is not None and self.rpf._has_data():
                    return True

                if self.rpf_vector_enable is not None and self.rpf_vector_enable._has_data():
                    return True

                if self.sg_expiry_timer is not None and self.sg_expiry_timer._has_data():
                    return True

                if self.sparse_mode_rp_addresses is not None and self.sparse_mode_rp_addresses._has_data():
                    return True

                if self.spt_threshold_infinity is not None:
                    return True

                if self.ssm is not None and self.ssm._has_data():
                    return True

                if self.ssm_allow_override is not None:
                    return True

                if self.suppress_data_registers is not None:
                    return True

                if self.suppress_rpf_prunes is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_pim_cfg as meta
                return meta._meta_table['Pim.DefaultContext.Ipv6']['meta_info']


        class Ipv4(object):
            """
            IPV4 commands
            
            .. attribute:: accept_register
            
            	Access\-list which specifies unauthorized sources
            	**type**\:  str
            
            	**length:** 1..64
            
            .. attribute:: allow_rp
            
            	Enable allow\-rp filtering for SM joins
            	**type**\:   :py:class:`AllowRp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.DefaultContext.Ipv4.AllowRp>`
            
            	**presence node**\: True
            
            .. attribute:: auto_rp_candidate_rps
            
            	Configure Candidate\-RPs
            	**type**\:   :py:class:`AutoRpCandidateRps <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.DefaultContext.Ipv4.AutoRpCandidateRps>`
            
            .. attribute:: auto_rp_disable
            
            	Disable Rendezvous Point discovery through the AutoRP protocol
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: auto_rp_mapping_agent
            
            	Configure AutoRP Mapping Agent
            	**type**\:   :py:class:`AutoRpMappingAgent <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.DefaultContext.Ipv4.AutoRpMappingAgent>`
            
            .. attribute:: bidir_rp_addresses
            
            	Configure Bidirectional PIM Rendezvous Point
            	**type**\:   :py:class:`BidirRpAddresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.DefaultContext.Ipv4.BidirRpAddresses>`
            
            .. attribute:: bsr
            
            	PIM BSR configuration
            	**type**\:   :py:class:`Bsr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.DefaultContext.Ipv4.Bsr>`
            
            .. attribute:: cj_multicast_only_frrs
            
            	Clone Join Multicast Only FRR
            	**type**\:   :py:class:`CjMulticastOnlyFrrs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.DefaultContext.Ipv4.CjMulticastOnlyFrrs>`
            
            .. attribute:: convergence
            
            	Configure convergence parameters
            	**type**\:   :py:class:`Convergence <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.DefaultContext.Ipv4.Convergence>`
            
            .. attribute:: cs_multicast_only_frrs
            
            	Clone Source Multicast Only FRR
            	**type**\:   :py:class:`CsMulticastOnlyFrrs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.DefaultContext.Ipv4.CsMulticastOnlyFrrs>`
            
            .. attribute:: inheritable_defaults
            
            	Inheritable defaults
            	**type**\:   :py:class:`InheritableDefaults <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.DefaultContext.Ipv4.InheritableDefaults>`
            
            .. attribute:: injects
            
            	Inject Explicit PIM RPF Vector Proxy's
            	**type**\:   :py:class:`Injects <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.DefaultContext.Ipv4.Injects>`
            
            .. attribute:: interfaces
            
            	Interface\-level Configuration
            	**type**\:   :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.DefaultContext.Ipv4.Interfaces>`
            
            .. attribute:: log_neighbor_changes
            
            	PIM neighbor state change logging is turned on if configured
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: maximum
            
            	Configure PIM State Limits
            	**type**\:   :py:class:`Maximum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.DefaultContext.Ipv4.Maximum>`
            
            .. attribute:: multicast_only_frr
            
            	Multicast Only FRR
            	**type**\:   :py:class:`MulticastOnlyFrr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.DefaultContext.Ipv4.MulticastOnlyFrr>`
            
            .. attribute:: multipath
            
            	Enable equal\-cost multipath routing
            	**type**\:   :py:class:`PimMultipathEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.PimMultipathEnum>`
            
            .. attribute:: neighbor_check_on_receive
            
            	Enable PIM neighbor checking when receiving PIM messages
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: neighbor_check_on_send
            
            	Enable PIM neighbor checking when sending join\-prunes
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: neighbor_filter
            
            	Access\-list of neighbors to be filtered
            	**type**\:  str
            
            	**length:** 1..64
            
            .. attribute:: nsf
            
            	Configure Non\-stop forwarding (NSF) options
            	**type**\:   :py:class:`Nsf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.DefaultContext.Ipv4.Nsf>`
            
            .. attribute:: old_register_checksum
            
            	Generate registers compatible with older IOS versions
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: paths
            
            	Inject PIM RPF Vector Proxy's
            	**type**\:   :py:class:`Paths <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.DefaultContext.Ipv4.Paths>`
            
            .. attribute:: register_source
            
            	Source address to use for register messages
            	**type**\:  str
            
            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
            
            .. attribute:: rp_static_deny
            
            	Configure static RP deny range
            	**type**\:  str
            
            	**length:** 1..64
            
            .. attribute:: rpf
            
            	Configure RPF options
            	**type**\:   :py:class:`Rpf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.DefaultContext.Ipv4.Rpf>`
            
            .. attribute:: rpf_redirect
            
            	Configure RPF\-redirect feature
            	**type**\:   :py:class:`RpfRedirect <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.DefaultContext.Ipv4.RpfRedirect>`
            
            .. attribute:: rpf_vector_enable
            
            	Enable PIM RPF Vector Proxy's
            	**type**\:   :py:class:`RpfVectorEnable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.DefaultContext.Ipv4.RpfVectorEnable>`
            
            	**presence node**\: True
            
            .. attribute:: sg_expiry_timer
            
            	Configure expiry timer for S,G routes
            	**type**\:   :py:class:`SgExpiryTimer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.DefaultContext.Ipv4.SgExpiryTimer>`
            
            .. attribute:: sparse_mode_rp_addresses
            
            	Configure Sparse\-Mode Rendezvous Point
            	**type**\:   :py:class:`SparseModeRpAddresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.DefaultContext.Ipv4.SparseModeRpAddresses>`
            
            .. attribute:: spt_threshold_infinity
            
            	Configure threshold of infinity for switching to SPT on last\-hop
            	**type**\:  str
            
            .. attribute:: ssm
            
            	Configure IP Multicast SSM
            	**type**\:   :py:class:`Ssm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.DefaultContext.Ipv4.Ssm>`
            
            .. attribute:: ssm_allow_override
            
            	Allow SSM ranges to be overridden by more specific ranges
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: suppress_data_registers
            
            	Suppress data registers after initial state setup
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: suppress_rpf_prunes
            
            	Suppress prunes triggered as a result of RPF changes
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'ipv4-pim-cfg'
            _revision = '2016-06-01'

            def __init__(self):
                self.parent = None
                self.accept_register = None
                self.allow_rp = None
                self.auto_rp_candidate_rps = Pim.DefaultContext.Ipv4.AutoRpCandidateRps()
                self.auto_rp_candidate_rps.parent = self
                self.auto_rp_disable = None
                self.auto_rp_mapping_agent = Pim.DefaultContext.Ipv4.AutoRpMappingAgent()
                self.auto_rp_mapping_agent.parent = self
                self.bidir_rp_addresses = Pim.DefaultContext.Ipv4.BidirRpAddresses()
                self.bidir_rp_addresses.parent = self
                self.bsr = Pim.DefaultContext.Ipv4.Bsr()
                self.bsr.parent = self
                self.cj_multicast_only_frrs = Pim.DefaultContext.Ipv4.CjMulticastOnlyFrrs()
                self.cj_multicast_only_frrs.parent = self
                self.convergence = Pim.DefaultContext.Ipv4.Convergence()
                self.convergence.parent = self
                self.cs_multicast_only_frrs = Pim.DefaultContext.Ipv4.CsMulticastOnlyFrrs()
                self.cs_multicast_only_frrs.parent = self
                self.inheritable_defaults = Pim.DefaultContext.Ipv4.InheritableDefaults()
                self.inheritable_defaults.parent = self
                self.injects = Pim.DefaultContext.Ipv4.Injects()
                self.injects.parent = self
                self.interfaces = Pim.DefaultContext.Ipv4.Interfaces()
                self.interfaces.parent = self
                self.log_neighbor_changes = None
                self.maximum = Pim.DefaultContext.Ipv4.Maximum()
                self.maximum.parent = self
                self.multicast_only_frr = Pim.DefaultContext.Ipv4.MulticastOnlyFrr()
                self.multicast_only_frr.parent = self
                self.multipath = None
                self.neighbor_check_on_receive = None
                self.neighbor_check_on_send = None
                self.neighbor_filter = None
                self.nsf = Pim.DefaultContext.Ipv4.Nsf()
                self.nsf.parent = self
                self.old_register_checksum = None
                self.paths = Pim.DefaultContext.Ipv4.Paths()
                self.paths.parent = self
                self.register_source = None
                self.rp_static_deny = None
                self.rpf = Pim.DefaultContext.Ipv4.Rpf()
                self.rpf.parent = self
                self.rpf_redirect = Pim.DefaultContext.Ipv4.RpfRedirect()
                self.rpf_redirect.parent = self
                self.rpf_vector_enable = None
                self.sg_expiry_timer = Pim.DefaultContext.Ipv4.SgExpiryTimer()
                self.sg_expiry_timer.parent = self
                self.sparse_mode_rp_addresses = Pim.DefaultContext.Ipv4.SparseModeRpAddresses()
                self.sparse_mode_rp_addresses.parent = self
                self.spt_threshold_infinity = None
                self.ssm = Pim.DefaultContext.Ipv4.Ssm()
                self.ssm.parent = self
                self.ssm_allow_override = None
                self.suppress_data_registers = None
                self.suppress_rpf_prunes = None


            class RpfRedirect(object):
                """
                Configure RPF\-redirect feature
                
                .. attribute:: route_policy
                
                	Route policy to select RPF topology
                	**type**\:  str
                
                	**length:** 1..64
                
                

                """

                _prefix = 'ipv4-pim-cfg'
                _revision = '2016-06-01'

                def __init__(self):
                    self.parent = None
                    self.route_policy = None

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-ipv4-pim-cfg:pim/Cisco-IOS-XR-ipv4-pim-cfg:default-context/Cisco-IOS-XR-ipv4-pim-cfg:ipv4/Cisco-IOS-XR-ipv4-pim-cfg:rpf-redirect'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.route_policy is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_pim_cfg as meta
                    return meta._meta_table['Pim.DefaultContext.Ipv4.RpfRedirect']['meta_info']


            class Interfaces(object):
                """
                Interface\-level Configuration
                
                .. attribute:: interface
                
                	The name of the interface
                	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.DefaultContext.Ipv4.Interfaces.Interface>`
                
                

                """

                _prefix = 'ipv4-pim-cfg'
                _revision = '2016-06-01'

                def __init__(self):
                    self.parent = None
                    self.interface = YList()
                    self.interface.parent = self
                    self.interface.name = 'interface'


                class Interface(object):
                    """
                    The name of the interface
                    
                    .. attribute:: interface_name  <key>
                    
                    	The name of interface
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: bfd
                    
                    	BFD configuration
                    	**type**\:   :py:class:`Bfd <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.DefaultContext.Ipv4.Interfaces.Interface.Bfd>`
                    
                    .. attribute:: bsr_border
                    
                    	BSR Border configuration for Interface
                    	**type**\:  bool
                    
                    .. attribute:: dr_priority
                    
                    	Hello DR priority, preference given to larger value
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: enable
                    
                    	Enter PIM Interface processing
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: hello_interval
                    
                    	Hello interval in seconds
                    	**type**\:  int
                    
                    	**range:** 1..3600
                    
                    	**units**\: second
                    
                    .. attribute:: interface_enable
                    
                    	Enable PIM processing on the interface
                    	**type**\:  bool
                    
                    .. attribute:: join_prune_mtu
                    
                    	Join\-Prune MTU in Bytes
                    	**type**\:  int
                    
                    	**range:** 576..65535
                    
                    	**units**\: byte
                    
                    .. attribute:: jp_interval
                    
                    	Join\-Prune interval in seconds
                    	**type**\:  int
                    
                    	**range:** 10..600
                    
                    	**units**\: second
                    
                    .. attribute:: maximum_routes
                    
                    	Maximum number of allowed routes for this interface
                    	**type**\:   :py:class:`MaximumRoutes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.DefaultContext.Ipv4.Interfaces.Interface.MaximumRoutes>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: neighbor_filter
                    
                    	Access\-list of neighbors to be filtered
                    	**type**\:  str
                    
                    	**length:** 1..64
                    
                    .. attribute:: override_interval
                    
                    	Override interval in milliseconds
                    	**type**\:  int
                    
                    	**range:** 400..65535
                    
                    	**units**\: millisecond
                    
                    .. attribute:: propagation_delay
                    
                    	Propagation delay in milli seconds
                    	**type**\:  int
                    
                    	**range:** 100..32767
                    
                    	**units**\: millisecond
                    
                    .. attribute:: redirect_bundle
                    
                    	Configure RPF\-redirect bundle for interface. Applicable for IPv4 only
                    	**type**\:   :py:class:`RedirectBundle <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.DefaultContext.Ipv4.Interfaces.Interface.RedirectBundle>`
                    
                    

                    """

                    _prefix = 'ipv4-pim-cfg'
                    _revision = '2016-06-01'

                    def __init__(self):
                        self.parent = None
                        self.interface_name = None
                        self.bfd = Pim.DefaultContext.Ipv4.Interfaces.Interface.Bfd()
                        self.bfd.parent = self
                        self.bsr_border = None
                        self.dr_priority = None
                        self.enable = None
                        self.hello_interval = None
                        self.interface_enable = None
                        self.join_prune_mtu = None
                        self.jp_interval = None
                        self.maximum_routes = None
                        self.neighbor_filter = None
                        self.override_interval = None
                        self.propagation_delay = None
                        self.redirect_bundle = Pim.DefaultContext.Ipv4.Interfaces.Interface.RedirectBundle()
                        self.redirect_bundle.parent = self


                    class RedirectBundle(object):
                        """
                        Configure RPF\-redirect bundle for interface.
                        Applicable for IPv4 only
                        
                        .. attribute:: bundle_name
                        
                        	Bundle name
                        	**type**\:  str
                        
                        	**length:** 1..32
                        
                        .. attribute:: interface_bandwidth
                        
                        	Interface bandwidth in Kbps
                        	**type**\:  int
                        
                        	**range:** 0..100000000
                        
                        	**units**\: kbit/s
                        
                        .. attribute:: threshold_bandwidth
                        
                        	Threshold bandwidth in Kbps
                        	**type**\:  int
                        
                        	**range:** 0..100000000
                        
                        	**units**\: kbit/s
                        
                        

                        """

                        _prefix = 'ipv4-pim-cfg'
                        _revision = '2016-06-01'

                        def __init__(self):
                            self.parent = None
                            self.bundle_name = None
                            self.interface_bandwidth = None
                            self.threshold_bandwidth = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv4-pim-cfg:redirect-bundle'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.bundle_name is not None:
                                return True

                            if self.interface_bandwidth is not None:
                                return True

                            if self.threshold_bandwidth is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_pim_cfg as meta
                            return meta._meta_table['Pim.DefaultContext.Ipv4.Interfaces.Interface.RedirectBundle']['meta_info']


                    class MaximumRoutes(object):
                        """
                        Maximum number of allowed routes for this
                        interface
                        
                        .. attribute:: access_list_name
                        
                        	Access\-list to account for
                        	**type**\:  str
                        
                        	**length:** 1..64
                        
                        .. attribute:: maximum
                        
                        	Maximum number of routes for this interface
                        	**type**\:  int
                        
                        	**range:** 1..1100000
                        
                        	**mandatory**\: True
                        
                        .. attribute:: warning_threshold
                        
                        	Set threshold to print warning
                        	**type**\:  int
                        
                        	**range:** 1..1100000
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'ipv4-pim-cfg'
                        _revision = '2016-06-01'

                        def __init__(self):
                            self.parent = None
                            self._is_presence = True
                            self.access_list_name = None
                            self.maximum = None
                            self.warning_threshold = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv4-pim-cfg:maximum-routes'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self._is_presence:
                                return True
                            if self.access_list_name is not None:
                                return True

                            if self.maximum is not None:
                                return True

                            if self.warning_threshold is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_pim_cfg as meta
                            return meta._meta_table['Pim.DefaultContext.Ipv4.Interfaces.Interface.MaximumRoutes']['meta_info']


                    class Bfd(object):
                        """
                        BFD configuration
                        
                        .. attribute:: detection_multiplier
                        
                        	Detection multiplier for BFD sessions created by PIM
                        	**type**\:  int
                        
                        	**range:** 2..50
                        
                        .. attribute:: enable
                        
                        	TRUE to enable BFD. FALSE to disable and to prevent inheritance from a parent
                        	**type**\:  bool
                        
                        .. attribute:: interval
                        
                        	Hello interval for BFD sessions created by PIM
                        	**type**\:  int
                        
                        	**range:** 3..30000
                        
                        	**units**\: millisecond
                        
                        

                        """

                        _prefix = 'ipv4-pim-cfg'
                        _revision = '2016-06-01'

                        def __init__(self):
                            self.parent = None
                            self.detection_multiplier = None
                            self.enable = None
                            self.interval = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ipv4-pim-cfg:bfd'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.detection_multiplier is not None:
                                return True

                            if self.enable is not None:
                                return True

                            if self.interval is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_pim_cfg as meta
                            return meta._meta_table['Pim.DefaultContext.Ipv4.Interfaces.Interface.Bfd']['meta_info']

                    @property
                    def _common_path(self):
                        if self.interface_name is None:
                            raise YPYModelError('Key property interface_name is None')

                        return '/Cisco-IOS-XR-ipv4-pim-cfg:pim/Cisco-IOS-XR-ipv4-pim-cfg:default-context/Cisco-IOS-XR-ipv4-pim-cfg:ipv4/Cisco-IOS-XR-ipv4-pim-cfg:interfaces/Cisco-IOS-XR-ipv4-pim-cfg:interface[Cisco-IOS-XR-ipv4-pim-cfg:interface-name = ' + str(self.interface_name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.interface_name is not None:
                            return True

                        if self.bfd is not None and self.bfd._has_data():
                            return True

                        if self.bsr_border is not None:
                            return True

                        if self.dr_priority is not None:
                            return True

                        if self.enable is not None:
                            return True

                        if self.hello_interval is not None:
                            return True

                        if self.interface_enable is not None:
                            return True

                        if self.join_prune_mtu is not None:
                            return True

                        if self.jp_interval is not None:
                            return True

                        if self.maximum_routes is not None and self.maximum_routes._has_data():
                            return True

                        if self.neighbor_filter is not None:
                            return True

                        if self.override_interval is not None:
                            return True

                        if self.propagation_delay is not None:
                            return True

                        if self.redirect_bundle is not None and self.redirect_bundle._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_pim_cfg as meta
                        return meta._meta_table['Pim.DefaultContext.Ipv4.Interfaces.Interface']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-ipv4-pim-cfg:pim/Cisco-IOS-XR-ipv4-pim-cfg:default-context/Cisco-IOS-XR-ipv4-pim-cfg:ipv4/Cisco-IOS-XR-ipv4-pim-cfg:interfaces'

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
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_pim_cfg as meta
                    return meta._meta_table['Pim.DefaultContext.Ipv4.Interfaces']['meta_info']


            class AutoRpCandidateRps(object):
                """
                Configure Candidate\-RPs
                
                .. attribute:: auto_rp_candidate_rp
                
                	Specifications for a Candidate\-RP
                	**type**\: list of    :py:class:`AutoRpCandidateRp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.DefaultContext.Ipv4.AutoRpCandidateRps.AutoRpCandidateRp>`
                
                

                """

                _prefix = 'ipv4-pim-cfg'
                _revision = '2016-06-01'

                def __init__(self):
                    self.parent = None
                    self.auto_rp_candidate_rp = YList()
                    self.auto_rp_candidate_rp.parent = self
                    self.auto_rp_candidate_rp.name = 'auto_rp_candidate_rp'


                class AutoRpCandidateRp(object):
                    """
                    Specifications for a Candidate\-RP
                    
                    .. attribute:: interface_name  <key>
                    
                    	Interface from which Candidate\-RP packets will be sourced
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: protocol_mode  <key>
                    
                    	Protocol Mode
                    	**type**\:   :py:class:`AutoRpProtocolModeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_autorp_datatypes.AutoRpProtocolModeEnum>`
                    
                    .. attribute:: access_list_name
                    
                    	Access\-list specifying the group range for the Candidate\-RP
                    	**type**\:  str
                    
                    	**length:** 1..64
                    
                    	**default value**\: 224-4
                    
                    .. attribute:: announce_period
                    
                    	Time between announcements <in seconds> 
                    	**type**\:  int
                    
                    	**range:** 1..600
                    
                    	**units**\: second
                    
                    	**default value**\: 60
                    
                    .. attribute:: ttl
                    
                    	TTL in Hops
                    	**type**\:  int
                    
                    	**range:** 1..255
                    
                    	**mandatory**\: True
                    
                    

                    """

                    _prefix = 'ipv4-pim-cfg'
                    _revision = '2016-06-01'

                    def __init__(self):
                        self.parent = None
                        self.interface_name = None
                        self.protocol_mode = None
                        self.access_list_name = None
                        self.announce_period = None
                        self.ttl = None

                    @property
                    def _common_path(self):
                        if self.interface_name is None:
                            raise YPYModelError('Key property interface_name is None')
                        if self.protocol_mode is None:
                            raise YPYModelError('Key property protocol_mode is None')

                        return '/Cisco-IOS-XR-ipv4-pim-cfg:pim/Cisco-IOS-XR-ipv4-pim-cfg:default-context/Cisco-IOS-XR-ipv4-pim-cfg:ipv4/Cisco-IOS-XR-ipv4-pim-cfg:auto-rp-candidate-rps/Cisco-IOS-XR-ipv4-pim-cfg:auto-rp-candidate-rp[Cisco-IOS-XR-ipv4-pim-cfg:interface-name = ' + str(self.interface_name) + '][Cisco-IOS-XR-ipv4-pim-cfg:protocol-mode = ' + str(self.protocol_mode) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.interface_name is not None:
                            return True

                        if self.protocol_mode is not None:
                            return True

                        if self.access_list_name is not None:
                            return True

                        if self.announce_period is not None:
                            return True

                        if self.ttl is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_pim_cfg as meta
                        return meta._meta_table['Pim.DefaultContext.Ipv4.AutoRpCandidateRps.AutoRpCandidateRp']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-ipv4-pim-cfg:pim/Cisco-IOS-XR-ipv4-pim-cfg:default-context/Cisco-IOS-XR-ipv4-pim-cfg:ipv4/Cisco-IOS-XR-ipv4-pim-cfg:auto-rp-candidate-rps'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.auto_rp_candidate_rp is not None:
                        for child_ref in self.auto_rp_candidate_rp:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_pim_cfg as meta
                    return meta._meta_table['Pim.DefaultContext.Ipv4.AutoRpCandidateRps']['meta_info']


            class AutoRpMappingAgent(object):
                """
                Configure AutoRP Mapping Agent
                
                .. attribute:: cache_limit
                
                	Mapping Agent cache size limit
                	**type**\:   :py:class:`CacheLimit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.DefaultContext.Ipv4.AutoRpMappingAgent.CacheLimit>`
                
                	**presence node**\: True
                
                .. attribute:: parameters
                
                	Specifications for Mapping Agent configured on this box
                	**type**\:   :py:class:`Parameters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.DefaultContext.Ipv4.AutoRpMappingAgent.Parameters>`
                
                	**presence node**\: True
                
                

                """

                _prefix = 'ipv4-pim-cfg'
                _revision = '2016-06-01'

                def __init__(self):
                    self.parent = None
                    self.cache_limit = None
                    self.parameters = None


                class Parameters(object):
                    """
                    Specifications for Mapping Agent configured
                    on this box
                    
                    .. attribute:: announce_period
                    
                    	Time between discovery messages <in seconds>
                    	**type**\:  int
                    
                    	**range:** 1..600
                    
                    	**units**\: second
                    
                    	**default value**\: 60
                    
                    .. attribute:: interface_name
                    
                    	Interface from which mapping packets will be sourced 
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    	**mandatory**\: True
                    
                    .. attribute:: ttl
                    
                    	TTL in Hops
                    	**type**\:  int
                    
                    	**range:** 1..255
                    
                    	**mandatory**\: True
                    
                    .. attribute:: _is_presence
                    
                    	Is present if this instance represents presence container else not
                    	**type**\: bool
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'ipv4-pim-cfg'
                    _revision = '2016-06-01'

                    def __init__(self):
                        self.parent = None
                        self._is_presence = True
                        self.announce_period = None
                        self.interface_name = None
                        self.ttl = None

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-ipv4-pim-cfg:pim/Cisco-IOS-XR-ipv4-pim-cfg:default-context/Cisco-IOS-XR-ipv4-pim-cfg:ipv4/Cisco-IOS-XR-ipv4-pim-cfg:auto-rp-mapping-agent/Cisco-IOS-XR-ipv4-pim-cfg:parameters'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self._is_presence:
                            return True
                        if self.announce_period is not None:
                            return True

                        if self.interface_name is not None:
                            return True

                        if self.ttl is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_pim_cfg as meta
                        return meta._meta_table['Pim.DefaultContext.Ipv4.AutoRpMappingAgent.Parameters']['meta_info']


                class CacheLimit(object):
                    """
                    Mapping Agent cache size limit
                    
                    .. attribute:: maximum_cache_entry
                    
                    	Maximum number of mapping cache entries
                    	**type**\:  int
                    
                    	**range:** 1..1000
                    
                    	**mandatory**\: True
                    
                    .. attribute:: threshold_cache_entry
                    
                    	Warning threshold number of cache entries
                    	**type**\:  int
                    
                    	**range:** 1..1000
                    
                    	**default value**\: 450
                    
                    .. attribute:: _is_presence
                    
                    	Is present if this instance represents presence container else not
                    	**type**\: bool
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'ipv4-pim-cfg'
                    _revision = '2016-06-01'

                    def __init__(self):
                        self.parent = None
                        self._is_presence = True
                        self.maximum_cache_entry = None
                        self.threshold_cache_entry = None

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-ipv4-pim-cfg:pim/Cisco-IOS-XR-ipv4-pim-cfg:default-context/Cisco-IOS-XR-ipv4-pim-cfg:ipv4/Cisco-IOS-XR-ipv4-pim-cfg:auto-rp-mapping-agent/Cisco-IOS-XR-ipv4-pim-cfg:cache-limit'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self._is_presence:
                            return True
                        if self.maximum_cache_entry is not None:
                            return True

                        if self.threshold_cache_entry is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_pim_cfg as meta
                        return meta._meta_table['Pim.DefaultContext.Ipv4.AutoRpMappingAgent.CacheLimit']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-ipv4-pim-cfg:pim/Cisco-IOS-XR-ipv4-pim-cfg:default-context/Cisco-IOS-XR-ipv4-pim-cfg:ipv4/Cisco-IOS-XR-ipv4-pim-cfg:auto-rp-mapping-agent'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.cache_limit is not None and self.cache_limit._has_data():
                        return True

                    if self.parameters is not None and self.parameters._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_pim_cfg as meta
                    return meta._meta_table['Pim.DefaultContext.Ipv4.AutoRpMappingAgent']['meta_info']


            class SparseModeRpAddresses(object):
                """
                Configure Sparse\-Mode Rendezvous Point
                
                .. attribute:: sparse_mode_rp_address
                
                	Address of the Rendezvous Point
                	**type**\: list of    :py:class:`SparseModeRpAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.DefaultContext.Ipv4.SparseModeRpAddresses.SparseModeRpAddress>`
                
                

                """

                _prefix = 'ipv4-pim-cfg'
                _revision = '2016-06-01'

                def __init__(self):
                    self.parent = None
                    self.sparse_mode_rp_address = YList()
                    self.sparse_mode_rp_address.parent = self
                    self.sparse_mode_rp_address.name = 'sparse_mode_rp_address'


                class SparseModeRpAddress(object):
                    """
                    Address of the Rendezvous Point
                    
                    .. attribute:: rp_address  <key>
                    
                    	RP address of Rendezvous Point
                    	**type**\: one of the below types:
                    
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    
                    ----
                    	**type**\:  str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    
                    ----
                    .. attribute:: access_list_name
                    
                    	Access list of groups that should map to a  given RP
                    	**type**\:  str
                    
                    	**length:** 1..64
                    
                    .. attribute:: auto_rp_override
                    
                    	TRUE Indicates if static RP config overrides AutoRP and BSR
                    	**type**\:  bool
                    
                    

                    """

                    _prefix = 'ipv4-pim-cfg'
                    _revision = '2016-06-01'

                    def __init__(self):
                        self.parent = None
                        self.rp_address = None
                        self.access_list_name = None
                        self.auto_rp_override = None

                    @property
                    def _common_path(self):
                        if self.rp_address is None:
                            raise YPYModelError('Key property rp_address is None')

                        return '/Cisco-IOS-XR-ipv4-pim-cfg:pim/Cisco-IOS-XR-ipv4-pim-cfg:default-context/Cisco-IOS-XR-ipv4-pim-cfg:ipv4/Cisco-IOS-XR-ipv4-pim-cfg:sparse-mode-rp-addresses/Cisco-IOS-XR-ipv4-pim-cfg:sparse-mode-rp-address[Cisco-IOS-XR-ipv4-pim-cfg:rp-address = ' + str(self.rp_address) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.rp_address is not None:
                            return True

                        if self.access_list_name is not None:
                            return True

                        if self.auto_rp_override is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_pim_cfg as meta
                        return meta._meta_table['Pim.DefaultContext.Ipv4.SparseModeRpAddresses.SparseModeRpAddress']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-ipv4-pim-cfg:pim/Cisco-IOS-XR-ipv4-pim-cfg:default-context/Cisco-IOS-XR-ipv4-pim-cfg:ipv4/Cisco-IOS-XR-ipv4-pim-cfg:sparse-mode-rp-addresses'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.sparse_mode_rp_address is not None:
                        for child_ref in self.sparse_mode_rp_address:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_pim_cfg as meta
                    return meta._meta_table['Pim.DefaultContext.Ipv4.SparseModeRpAddresses']['meta_info']


            class MulticastOnlyFrr(object):
                """
                Multicast Only FRR
                
                .. attribute:: enable
                
                	Enable Multicast Only FRR
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: flow_multicast_only_frr
                
                	Access\-list specifying SG that should do FLOW MOFRR
                	**type**\:  str
                
                	**length:** 1..64
                
                .. attribute:: non_revertive_multicast_only_frr
                
                	Non\-revertive Multicast Only FRR
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: rib_multicast_only_frr
                
                	Access\-list specifying SG that should do RIB MOFRR
                	**type**\:  str
                
                	**length:** 1..64
                
                

                """

                _prefix = 'ipv4-pim-cfg'
                _revision = '2016-06-01'

                def __init__(self):
                    self.parent = None
                    self.enable = None
                    self.flow_multicast_only_frr = None
                    self.non_revertive_multicast_only_frr = None
                    self.rib_multicast_only_frr = None

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-ipv4-pim-cfg:pim/Cisco-IOS-XR-ipv4-pim-cfg:default-context/Cisco-IOS-XR-ipv4-pim-cfg:ipv4/Cisco-IOS-XR-ipv4-pim-cfg:multicast-only-frr'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.enable is not None:
                        return True

                    if self.flow_multicast_only_frr is not None:
                        return True

                    if self.non_revertive_multicast_only_frr is not None:
                        return True

                    if self.rib_multicast_only_frr is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_pim_cfg as meta
                    return meta._meta_table['Pim.DefaultContext.Ipv4.MulticastOnlyFrr']['meta_info']


            class CsMulticastOnlyFrrs(object):
                """
                Clone Source Multicast Only FRR
                
                .. attribute:: cs_multicast_only_frr
                
                	Clone Source Multicast Only FRR
                	**type**\: list of    :py:class:`CsMulticastOnlyFrr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.DefaultContext.Ipv4.CsMulticastOnlyFrrs.CsMulticastOnlyFrr>`
                
                

                """

                _prefix = 'ipv4-pim-cfg'
                _revision = '2016-06-01'

                def __init__(self):
                    self.parent = None
                    self.cs_multicast_only_frr = YList()
                    self.cs_multicast_only_frr.parent = self
                    self.cs_multicast_only_frr.name = 'cs_multicast_only_frr'


                class CsMulticastOnlyFrr(object):
                    """
                    Clone Source Multicast Only FRR
                    
                    .. attribute:: source  <key>
                    
                    	Original address
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: primary  <key>
                    
                    	Primary address
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: backup  <key>
                    
                    	Backup address
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: prefix_length  <key>
                    
                    	Masklen
                    	**type**\:  int
                    
                    	**range:** 0..32
                    
                    

                    """

                    _prefix = 'ipv4-pim-cfg'
                    _revision = '2016-06-01'

                    def __init__(self):
                        self.parent = None
                        self.source = None
                        self.primary = None
                        self.backup = None
                        self.prefix_length = None

                    @property
                    def _common_path(self):
                        if self.source is None:
                            raise YPYModelError('Key property source is None')
                        if self.primary is None:
                            raise YPYModelError('Key property primary is None')
                        if self.backup is None:
                            raise YPYModelError('Key property backup is None')
                        if self.prefix_length is None:
                            raise YPYModelError('Key property prefix_length is None')

                        return '/Cisco-IOS-XR-ipv4-pim-cfg:pim/Cisco-IOS-XR-ipv4-pim-cfg:default-context/Cisco-IOS-XR-ipv4-pim-cfg:ipv4/Cisco-IOS-XR-ipv4-pim-cfg:cs-multicast-only-frrs/Cisco-IOS-XR-ipv4-pim-cfg:cs-multicast-only-frr[Cisco-IOS-XR-ipv4-pim-cfg:source = ' + str(self.source) + '][Cisco-IOS-XR-ipv4-pim-cfg:primary = ' + str(self.primary) + '][Cisco-IOS-XR-ipv4-pim-cfg:backup = ' + str(self.backup) + '][Cisco-IOS-XR-ipv4-pim-cfg:prefix-length = ' + str(self.prefix_length) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.source is not None:
                            return True

                        if self.primary is not None:
                            return True

                        if self.backup is not None:
                            return True

                        if self.prefix_length is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_pim_cfg as meta
                        return meta._meta_table['Pim.DefaultContext.Ipv4.CsMulticastOnlyFrrs.CsMulticastOnlyFrr']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-ipv4-pim-cfg:pim/Cisco-IOS-XR-ipv4-pim-cfg:default-context/Cisco-IOS-XR-ipv4-pim-cfg:ipv4/Cisco-IOS-XR-ipv4-pim-cfg:cs-multicast-only-frrs'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.cs_multicast_only_frr is not None:
                        for child_ref in self.cs_multicast_only_frr:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_pim_cfg as meta
                    return meta._meta_table['Pim.DefaultContext.Ipv4.CsMulticastOnlyFrrs']['meta_info']


            class InheritableDefaults(object):
                """
                Inheritable defaults
                
                .. attribute:: convergency
                
                	Convergency timeout in seconds
                	**type**\:  int
                
                	**range:** 1800..2400
                
                	**units**\: second
                
                .. attribute:: dr_priority
                
                	Hello DR priority, preference given to larger value
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: hello_interval
                
                	Hello interval in seconds
                	**type**\:  int
                
                	**range:** 1..3600
                
                	**units**\: second
                
                .. attribute:: join_prune_mtu
                
                	Join\-Prune MTU in Bytes
                	**type**\:  int
                
                	**range:** 576..65535
                
                	**units**\: byte
                
                .. attribute:: jp_interval
                
                	Join\-Prune interval in seconds
                	**type**\:  int
                
                	**range:** 10..600
                
                	**units**\: second
                
                .. attribute:: override_interval
                
                	Override interval in milliseconds
                	**type**\:  int
                
                	**range:** 400..65535
                
                	**units**\: millisecond
                
                .. attribute:: propagation_delay
                
                	Propagation delay in milli seconds
                	**type**\:  int
                
                	**range:** 100..32767
                
                	**units**\: millisecond
                
                

                """

                _prefix = 'ipv4-pim-cfg'
                _revision = '2016-06-01'

                def __init__(self):
                    self.parent = None
                    self.convergency = None
                    self.dr_priority = None
                    self.hello_interval = None
                    self.join_prune_mtu = None
                    self.jp_interval = None
                    self.override_interval = None
                    self.propagation_delay = None

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-ipv4-pim-cfg:pim/Cisco-IOS-XR-ipv4-pim-cfg:default-context/Cisco-IOS-XR-ipv4-pim-cfg:ipv4/Cisco-IOS-XR-ipv4-pim-cfg:inheritable-defaults'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.convergency is not None:
                        return True

                    if self.dr_priority is not None:
                        return True

                    if self.hello_interval is not None:
                        return True

                    if self.join_prune_mtu is not None:
                        return True

                    if self.jp_interval is not None:
                        return True

                    if self.override_interval is not None:
                        return True

                    if self.propagation_delay is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_pim_cfg as meta
                    return meta._meta_table['Pim.DefaultContext.Ipv4.InheritableDefaults']['meta_info']


            class Rpf(object):
                """
                Configure RPF options
                
                .. attribute:: route_policy
                
                	Route policy to select RPF topology
                	**type**\:  str
                
                	**length:** 1..64
                
                

                """

                _prefix = 'ipv4-pim-cfg'
                _revision = '2016-06-01'

                def __init__(self):
                    self.parent = None
                    self.route_policy = None

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-ipv4-pim-cfg:pim/Cisco-IOS-XR-ipv4-pim-cfg:default-context/Cisco-IOS-XR-ipv4-pim-cfg:ipv4/Cisco-IOS-XR-ipv4-pim-cfg:rpf'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.route_policy is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_pim_cfg as meta
                    return meta._meta_table['Pim.DefaultContext.Ipv4.Rpf']['meta_info']


            class SgExpiryTimer(object):
                """
                Configure expiry timer for S,G routes
                
                .. attribute:: access_list_name
                
                	Access\-list of applicable S,G routes
                	**type**\:  str
                
                	**length:** 1..64
                
                .. attribute:: interval
                
                	(S,G) expiry time in seconds
                	**type**\:  int
                
                	**range:** 40..57600
                
                	**units**\: second
                
                

                """

                _prefix = 'ipv4-pim-cfg'
                _revision = '2016-06-01'

                def __init__(self):
                    self.parent = None
                    self.access_list_name = None
                    self.interval = None

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-ipv4-pim-cfg:pim/Cisco-IOS-XR-ipv4-pim-cfg:default-context/Cisco-IOS-XR-ipv4-pim-cfg:ipv4/Cisco-IOS-XR-ipv4-pim-cfg:sg-expiry-timer'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.access_list_name is not None:
                        return True

                    if self.interval is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_pim_cfg as meta
                    return meta._meta_table['Pim.DefaultContext.Ipv4.SgExpiryTimer']['meta_info']


            class RpfVectorEnable(object):
                """
                Enable PIM RPF Vector Proxy's
                
                .. attribute:: allow_ebgp
                
                	Allow RPF Vector origination over eBGP sessions
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: disable_ibgp
                
                	Disable RPF Vector origination over iBGP sessions
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: enable
                
                	RPF Vector is turned on if configured
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                	**mandatory**\: True
                
                .. attribute:: _is_presence
                
                	Is present if this instance represents presence container else not
                	**type**\: bool
                
                

                This class is a :ref:`presence class<presence-class>`

                """

                _prefix = 'ipv4-pim-cfg'
                _revision = '2016-06-01'

                def __init__(self):
                    self.parent = None
                    self._is_presence = True
                    self.allow_ebgp = None
                    self.disable_ibgp = None
                    self.enable = None

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-ipv4-pim-cfg:pim/Cisco-IOS-XR-ipv4-pim-cfg:default-context/Cisco-IOS-XR-ipv4-pim-cfg:ipv4/Cisco-IOS-XR-ipv4-pim-cfg:rpf-vector-enable'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self._is_presence:
                        return True
                    if self.allow_ebgp is not None:
                        return True

                    if self.disable_ibgp is not None:
                        return True

                    if self.enable is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_pim_cfg as meta
                    return meta._meta_table['Pim.DefaultContext.Ipv4.RpfVectorEnable']['meta_info']


            class Nsf(object):
                """
                Configure Non\-stop forwarding (NSF) options
                
                .. attribute:: lifetime
                
                	Override default maximum lifetime for PIM NSF mode
                	**type**\:  int
                
                	**range:** 10..600
                
                	**units**\: second
                
                

                """

                _prefix = 'ipv4-pim-cfg'
                _revision = '2016-06-01'

                def __init__(self):
                    self.parent = None
                    self.lifetime = None

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-ipv4-pim-cfg:pim/Cisco-IOS-XR-ipv4-pim-cfg:default-context/Cisco-IOS-XR-ipv4-pim-cfg:ipv4/Cisco-IOS-XR-ipv4-pim-cfg:nsf'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.lifetime is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_pim_cfg as meta
                    return meta._meta_table['Pim.DefaultContext.Ipv4.Nsf']['meta_info']


            class Maximum(object):
                """
                Configure PIM State Limits
                
                .. attribute:: bsr_candidate_rp_cache
                
                	Override default maximum and threshold for BSR C\-RP cache setting
                	**type**\:   :py:class:`BsrCandidateRpCache <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.DefaultContext.Ipv4.Maximum.BsrCandidateRpCache>`
                
                	**presence node**\: True
                
                .. attribute:: bsr_global_candidate_rp_cache
                
                	Override default global maximum and threshold for C\-RP set in BSR
                	**type**\:   :py:class:`BsrGlobalCandidateRpCache <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.DefaultContext.Ipv4.Maximum.BsrGlobalCandidateRpCache>`
                
                	**presence node**\: True
                
                .. attribute:: bsr_global_group_mappings
                
                	Override default global maximum and threshold for PIM group mapping ranges from BSR
                	**type**\:   :py:class:`BsrGlobalGroupMappings <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.DefaultContext.Ipv4.Maximum.BsrGlobalGroupMappings>`
                
                	**presence node**\: True
                
                .. attribute:: bsr_group_mappings
                
                	Override default maximum and threshold for number of group mappings from BSR
                	**type**\:   :py:class:`BsrGroupMappings <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.DefaultContext.Ipv4.Maximum.BsrGroupMappings>`
                
                	**presence node**\: True
                
                .. attribute:: global_group_mappings_auto_rp
                
                	Maximum for number of group mappings from autorp mapping agent
                	**type**\:   :py:class:`GlobalGroupMappingsAutoRp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.DefaultContext.Ipv4.Maximum.GlobalGroupMappingsAutoRp>`
                
                	**presence node**\: True
                
                .. attribute:: global_high_priority_packet_queue
                
                	Maximum packet queue size in bytes
                	**type**\:  int
                
                	**range:** 0..2147483648
                
                	**units**\: byte
                
                .. attribute:: global_low_priority_packet_queue
                
                	Maximum packet queue size in bytes
                	**type**\:  int
                
                	**range:** 0..2147483648
                
                	**units**\: byte
                
                .. attribute:: global_register_states
                
                	Override default maximum for number of sparse\-mode source registers
                	**type**\:   :py:class:`GlobalRegisterStates <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.DefaultContext.Ipv4.Maximum.GlobalRegisterStates>`
                
                	**presence node**\: True
                
                .. attribute:: global_route_interfaces
                
                	Override default maximum for number of route\-interfaces
                	**type**\:   :py:class:`GlobalRouteInterfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.DefaultContext.Ipv4.Maximum.GlobalRouteInterfaces>`
                
                	**presence node**\: True
                
                .. attribute:: global_routes
                
                	Override default maximum for number of routes
                	**type**\:   :py:class:`GlobalRoutes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.DefaultContext.Ipv4.Maximum.GlobalRoutes>`
                
                	**presence node**\: True
                
                .. attribute:: group_mappings_auto_rp
                
                	Override default maximum for number of group mappings from autorp mapping agent
                	**type**\:   :py:class:`GroupMappingsAutoRp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.DefaultContext.Ipv4.Maximum.GroupMappingsAutoRp>`
                
                	**presence node**\: True
                
                .. attribute:: register_states
                
                	Override default maximum for number of sparse\-mode source registers
                	**type**\:   :py:class:`RegisterStates <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.DefaultContext.Ipv4.Maximum.RegisterStates>`
                
                	**presence node**\: True
                
                .. attribute:: route_interfaces
                
                	Override default maximum for number of route\-interfaces
                	**type**\:   :py:class:`RouteInterfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.DefaultContext.Ipv4.Maximum.RouteInterfaces>`
                
                	**presence node**\: True
                
                .. attribute:: routes
                
                	Override default maximum for number of routes
                	**type**\:   :py:class:`Routes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.DefaultContext.Ipv4.Maximum.Routes>`
                
                	**presence node**\: True
                
                

                """

                _prefix = 'ipv4-pim-cfg'
                _revision = '2016-06-01'

                def __init__(self):
                    self.parent = None
                    self.bsr_candidate_rp_cache = None
                    self.bsr_global_candidate_rp_cache = None
                    self.bsr_global_group_mappings = None
                    self.bsr_group_mappings = None
                    self.global_group_mappings_auto_rp = None
                    self.global_high_priority_packet_queue = None
                    self.global_low_priority_packet_queue = None
                    self.global_register_states = None
                    self.global_route_interfaces = None
                    self.global_routes = None
                    self.group_mappings_auto_rp = None
                    self.register_states = None
                    self.route_interfaces = None
                    self.routes = None


                class BsrGlobalGroupMappings(object):
                    """
                    Override default global maximum and threshold
                    for PIM group mapping ranges from BSR
                    
                    .. attribute:: bsr_maximum_global_group_mappings
                    
                    	Global Maximum number of PIM group mapping ranges from BSR
                    	**type**\:  int
                    
                    	**range:** 1..10000
                    
                    	**mandatory**\: True
                    
                    .. attribute:: warning_threshold
                    
                    	Set threshold to print warning
                    	**type**\:  int
                    
                    	**range:** 1..10000
                    
                    	**default value**\: 500
                    
                    .. attribute:: _is_presence
                    
                    	Is present if this instance represents presence container else not
                    	**type**\: bool
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'ipv4-pim-cfg'
                    _revision = '2016-06-01'

                    def __init__(self):
                        self.parent = None
                        self._is_presence = True
                        self.bsr_maximum_global_group_mappings = None
                        self.warning_threshold = None

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-ipv4-pim-cfg:pim/Cisco-IOS-XR-ipv4-pim-cfg:default-context/Cisco-IOS-XR-ipv4-pim-cfg:ipv4/Cisco-IOS-XR-ipv4-pim-cfg:maximum/Cisco-IOS-XR-ipv4-pim-cfg:bsr-global-group-mappings'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self._is_presence:
                            return True
                        if self.bsr_maximum_global_group_mappings is not None:
                            return True

                        if self.warning_threshold is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_pim_cfg as meta
                        return meta._meta_table['Pim.DefaultContext.Ipv4.Maximum.BsrGlobalGroupMappings']['meta_info']


                class GlobalRoutes(object):
                    """
                    Override default maximum for number of routes
                    
                    .. attribute:: maximum_routes
                    
                    	Maximum number of PIM routes
                    	**type**\:  int
                    
                    	**range:** 1..200000
                    
                    	**mandatory**\: True
                    
                    .. attribute:: warning_threshold
                    
                    	Set threshold to print warning
                    	**type**\:  int
                    
                    	**range:** 1..200000
                    
                    	**default value**\: 100000
                    
                    .. attribute:: _is_presence
                    
                    	Is present if this instance represents presence container else not
                    	**type**\: bool
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'ipv4-pim-cfg'
                    _revision = '2016-06-01'

                    def __init__(self):
                        self.parent = None
                        self._is_presence = True
                        self.maximum_routes = None
                        self.warning_threshold = None

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-ipv4-pim-cfg:pim/Cisco-IOS-XR-ipv4-pim-cfg:default-context/Cisco-IOS-XR-ipv4-pim-cfg:ipv4/Cisco-IOS-XR-ipv4-pim-cfg:maximum/Cisco-IOS-XR-ipv4-pim-cfg:global-routes'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self._is_presence:
                            return True
                        if self.maximum_routes is not None:
                            return True

                        if self.warning_threshold is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_pim_cfg as meta
                        return meta._meta_table['Pim.DefaultContext.Ipv4.Maximum.GlobalRoutes']['meta_info']


                class GlobalGroupMappingsAutoRp(object):
                    """
                    Maximum for number of group mappings from
                    autorp mapping agent
                    
                    .. attribute:: maximum_global_group_ranges_auto_rp
                    
                    	Maximum number of PIM group mappings from autorp
                    	**type**\:  int
                    
                    	**range:** 1..10000
                    
                    	**mandatory**\: True
                    
                    .. attribute:: threshold_global_group_ranges_auto_rp
                    
                    	Warning threshold number of PIM group mappings from autorp
                    	**type**\:  int
                    
                    	**range:** 1..10000
                    
                    	**default value**\: 450
                    
                    .. attribute:: _is_presence
                    
                    	Is present if this instance represents presence container else not
                    	**type**\: bool
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'ipv4-pim-cfg'
                    _revision = '2016-06-01'

                    def __init__(self):
                        self.parent = None
                        self._is_presence = True
                        self.maximum_global_group_ranges_auto_rp = None
                        self.threshold_global_group_ranges_auto_rp = None

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-ipv4-pim-cfg:pim/Cisco-IOS-XR-ipv4-pim-cfg:default-context/Cisco-IOS-XR-ipv4-pim-cfg:ipv4/Cisco-IOS-XR-ipv4-pim-cfg:maximum/Cisco-IOS-XR-ipv4-pim-cfg:global-group-mappings-auto-rp'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self._is_presence:
                            return True
                        if self.maximum_global_group_ranges_auto_rp is not None:
                            return True

                        if self.threshold_global_group_ranges_auto_rp is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_pim_cfg as meta
                        return meta._meta_table['Pim.DefaultContext.Ipv4.Maximum.GlobalGroupMappingsAutoRp']['meta_info']


                class BsrGlobalCandidateRpCache(object):
                    """
                    Override default global maximum and threshold
                    for C\-RP set in BSR
                    
                    .. attribute:: bsr_maximum_global_candidate_rp_cache
                    
                    	Global Maximum number of PIM C\-RP Sets from BSR
                    	**type**\:  int
                    
                    	**range:** 1..10000
                    
                    	**mandatory**\: True
                    
                    .. attribute:: warning_threshold
                    
                    	Set threshold to print warning
                    	**type**\:  int
                    
                    	**range:** 1..10000
                    
                    	**default value**\: 100
                    
                    .. attribute:: _is_presence
                    
                    	Is present if this instance represents presence container else not
                    	**type**\: bool
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'ipv4-pim-cfg'
                    _revision = '2016-06-01'

                    def __init__(self):
                        self.parent = None
                        self._is_presence = True
                        self.bsr_maximum_global_candidate_rp_cache = None
                        self.warning_threshold = None

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-ipv4-pim-cfg:pim/Cisco-IOS-XR-ipv4-pim-cfg:default-context/Cisco-IOS-XR-ipv4-pim-cfg:ipv4/Cisco-IOS-XR-ipv4-pim-cfg:maximum/Cisco-IOS-XR-ipv4-pim-cfg:bsr-global-candidate-rp-cache'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self._is_presence:
                            return True
                        if self.bsr_maximum_global_candidate_rp_cache is not None:
                            return True

                        if self.warning_threshold is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_pim_cfg as meta
                        return meta._meta_table['Pim.DefaultContext.Ipv4.Maximum.BsrGlobalCandidateRpCache']['meta_info']


                class GlobalRegisterStates(object):
                    """
                    Override default maximum for number of
                    sparse\-mode source registers
                    
                    .. attribute:: maximum_register_states
                    
                    	Maximum number of PIM Sparse\-Mode register states
                    	**type**\:  int
                    
                    	**range:** 0..75000
                    
                    	**mandatory**\: True
                    
                    .. attribute:: warning_threshold
                    
                    	Set threshold to print warning
                    	**type**\:  int
                    
                    	**range:** 0..75000
                    
                    	**default value**\: 20000
                    
                    .. attribute:: _is_presence
                    
                    	Is present if this instance represents presence container else not
                    	**type**\: bool
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'ipv4-pim-cfg'
                    _revision = '2016-06-01'

                    def __init__(self):
                        self.parent = None
                        self._is_presence = True
                        self.maximum_register_states = None
                        self.warning_threshold = None

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-ipv4-pim-cfg:pim/Cisco-IOS-XR-ipv4-pim-cfg:default-context/Cisco-IOS-XR-ipv4-pim-cfg:ipv4/Cisco-IOS-XR-ipv4-pim-cfg:maximum/Cisco-IOS-XR-ipv4-pim-cfg:global-register-states'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self._is_presence:
                            return True
                        if self.maximum_register_states is not None:
                            return True

                        if self.warning_threshold is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_pim_cfg as meta
                        return meta._meta_table['Pim.DefaultContext.Ipv4.Maximum.GlobalRegisterStates']['meta_info']


                class GlobalRouteInterfaces(object):
                    """
                    Override default maximum for number of
                    route\-interfaces
                    
                    .. attribute:: maximum_route_interfaces
                    
                    	Maximum number of PIM route\-interfaces
                    	**type**\:  int
                    
                    	**range:** 1..1100000
                    
                    	**mandatory**\: True
                    
                    .. attribute:: warning_threshold
                    
                    	Set threshold to print warning
                    	**type**\:  int
                    
                    	**range:** 1..1100000
                    
                    	**default value**\: 300000
                    
                    .. attribute:: _is_presence
                    
                    	Is present if this instance represents presence container else not
                    	**type**\: bool
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'ipv4-pim-cfg'
                    _revision = '2016-06-01'

                    def __init__(self):
                        self.parent = None
                        self._is_presence = True
                        self.maximum_route_interfaces = None
                        self.warning_threshold = None

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-ipv4-pim-cfg:pim/Cisco-IOS-XR-ipv4-pim-cfg:default-context/Cisco-IOS-XR-ipv4-pim-cfg:ipv4/Cisco-IOS-XR-ipv4-pim-cfg:maximum/Cisco-IOS-XR-ipv4-pim-cfg:global-route-interfaces'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self._is_presence:
                            return True
                        if self.maximum_route_interfaces is not None:
                            return True

                        if self.warning_threshold is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_pim_cfg as meta
                        return meta._meta_table['Pim.DefaultContext.Ipv4.Maximum.GlobalRouteInterfaces']['meta_info']


                class GroupMappingsAutoRp(object):
                    """
                    Override default maximum for number of group
                    mappings from autorp mapping agent
                    
                    .. attribute:: maximum_group_ranges_auto_rp
                    
                    	Maximum number of PIM group mappings from autorp
                    	**type**\:  int
                    
                    	**range:** 1..10000
                    
                    	**mandatory**\: True
                    
                    .. attribute:: threshold_group_ranges_auto_rp
                    
                    	Warning threshold number of PIM group mappings from autorp
                    	**type**\:  int
                    
                    	**range:** 1..10000
                    
                    	**default value**\: 450
                    
                    .. attribute:: _is_presence
                    
                    	Is present if this instance represents presence container else not
                    	**type**\: bool
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'ipv4-pim-cfg'
                    _revision = '2016-06-01'

                    def __init__(self):
                        self.parent = None
                        self._is_presence = True
                        self.maximum_group_ranges_auto_rp = None
                        self.threshold_group_ranges_auto_rp = None

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-ipv4-pim-cfg:pim/Cisco-IOS-XR-ipv4-pim-cfg:default-context/Cisco-IOS-XR-ipv4-pim-cfg:ipv4/Cisco-IOS-XR-ipv4-pim-cfg:maximum/Cisco-IOS-XR-ipv4-pim-cfg:group-mappings-auto-rp'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self._is_presence:
                            return True
                        if self.maximum_group_ranges_auto_rp is not None:
                            return True

                        if self.threshold_group_ranges_auto_rp is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_pim_cfg as meta
                        return meta._meta_table['Pim.DefaultContext.Ipv4.Maximum.GroupMappingsAutoRp']['meta_info']


                class BsrGroupMappings(object):
                    """
                    Override default maximum and threshold for
                    number of group mappings from BSR
                    
                    .. attribute:: bsr_maximum_group_ranges
                    
                    	Maximum number of PIM group mappings from BSR
                    	**type**\:  int
                    
                    	**range:** 1..10000
                    
                    	**mandatory**\: True
                    
                    .. attribute:: warning_threshold
                    
                    	Set threshold to print warning
                    	**type**\:  int
                    
                    	**range:** 1..10000
                    
                    	**default value**\: 500
                    
                    .. attribute:: _is_presence
                    
                    	Is present if this instance represents presence container else not
                    	**type**\: bool
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'ipv4-pim-cfg'
                    _revision = '2016-06-01'

                    def __init__(self):
                        self.parent = None
                        self._is_presence = True
                        self.bsr_maximum_group_ranges = None
                        self.warning_threshold = None

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-ipv4-pim-cfg:pim/Cisco-IOS-XR-ipv4-pim-cfg:default-context/Cisco-IOS-XR-ipv4-pim-cfg:ipv4/Cisco-IOS-XR-ipv4-pim-cfg:maximum/Cisco-IOS-XR-ipv4-pim-cfg:bsr-group-mappings'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self._is_presence:
                            return True
                        if self.bsr_maximum_group_ranges is not None:
                            return True

                        if self.warning_threshold is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_pim_cfg as meta
                        return meta._meta_table['Pim.DefaultContext.Ipv4.Maximum.BsrGroupMappings']['meta_info']


                class RegisterStates(object):
                    """
                    Override default maximum for number of
                    sparse\-mode source registers
                    
                    .. attribute:: maximum_register_states
                    
                    	Maximum number of PIM Sparse\-Mode register states
                    	**type**\:  int
                    
                    	**range:** 0..75000
                    
                    	**mandatory**\: True
                    
                    .. attribute:: warning_threshold
                    
                    	Set threshold to print warning
                    	**type**\:  int
                    
                    	**range:** 0..75000
                    
                    	**default value**\: 20000
                    
                    .. attribute:: _is_presence
                    
                    	Is present if this instance represents presence container else not
                    	**type**\: bool
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'ipv4-pim-cfg'
                    _revision = '2016-06-01'

                    def __init__(self):
                        self.parent = None
                        self._is_presence = True
                        self.maximum_register_states = None
                        self.warning_threshold = None

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-ipv4-pim-cfg:pim/Cisco-IOS-XR-ipv4-pim-cfg:default-context/Cisco-IOS-XR-ipv4-pim-cfg:ipv4/Cisco-IOS-XR-ipv4-pim-cfg:maximum/Cisco-IOS-XR-ipv4-pim-cfg:register-states'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self._is_presence:
                            return True
                        if self.maximum_register_states is not None:
                            return True

                        if self.warning_threshold is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_pim_cfg as meta
                        return meta._meta_table['Pim.DefaultContext.Ipv4.Maximum.RegisterStates']['meta_info']


                class RouteInterfaces(object):
                    """
                    Override default maximum for number of
                    route\-interfaces
                    
                    .. attribute:: maximum_route_interfaces
                    
                    	Maximum number of PIM route\-interfaces
                    	**type**\:  int
                    
                    	**range:** 1..1100000
                    
                    	**mandatory**\: True
                    
                    .. attribute:: warning_threshold
                    
                    	Set threshold to print warning
                    	**type**\:  int
                    
                    	**range:** 1..1100000
                    
                    	**default value**\: 300000
                    
                    .. attribute:: _is_presence
                    
                    	Is present if this instance represents presence container else not
                    	**type**\: bool
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'ipv4-pim-cfg'
                    _revision = '2016-06-01'

                    def __init__(self):
                        self.parent = None
                        self._is_presence = True
                        self.maximum_route_interfaces = None
                        self.warning_threshold = None

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-ipv4-pim-cfg:pim/Cisco-IOS-XR-ipv4-pim-cfg:default-context/Cisco-IOS-XR-ipv4-pim-cfg:ipv4/Cisco-IOS-XR-ipv4-pim-cfg:maximum/Cisco-IOS-XR-ipv4-pim-cfg:route-interfaces'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self._is_presence:
                            return True
                        if self.maximum_route_interfaces is not None:
                            return True

                        if self.warning_threshold is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_pim_cfg as meta
                        return meta._meta_table['Pim.DefaultContext.Ipv4.Maximum.RouteInterfaces']['meta_info']


                class BsrCandidateRpCache(object):
                    """
                    Override default maximum and threshold for BSR
                    C\-RP cache setting
                    
                    .. attribute:: bsr_maximum_candidate_rp_cache
                    
                    	Maximum number of BSR C\-RP cache setting
                    	**type**\:  int
                    
                    	**range:** 1..10000
                    
                    	**mandatory**\: True
                    
                    .. attribute:: warning_threshold
                    
                    	Set threshold to print warning
                    	**type**\:  int
                    
                    	**range:** 1..10000
                    
                    	**default value**\: 100
                    
                    .. attribute:: _is_presence
                    
                    	Is present if this instance represents presence container else not
                    	**type**\: bool
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'ipv4-pim-cfg'
                    _revision = '2016-06-01'

                    def __init__(self):
                        self.parent = None
                        self._is_presence = True
                        self.bsr_maximum_candidate_rp_cache = None
                        self.warning_threshold = None

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-ipv4-pim-cfg:pim/Cisco-IOS-XR-ipv4-pim-cfg:default-context/Cisco-IOS-XR-ipv4-pim-cfg:ipv4/Cisco-IOS-XR-ipv4-pim-cfg:maximum/Cisco-IOS-XR-ipv4-pim-cfg:bsr-candidate-rp-cache'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self._is_presence:
                            return True
                        if self.bsr_maximum_candidate_rp_cache is not None:
                            return True

                        if self.warning_threshold is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_pim_cfg as meta
                        return meta._meta_table['Pim.DefaultContext.Ipv4.Maximum.BsrCandidateRpCache']['meta_info']


                class Routes(object):
                    """
                    Override default maximum for number of routes
                    
                    .. attribute:: maximum_routes
                    
                    	Maximum number of PIM routes
                    	**type**\:  int
                    
                    	**range:** 1..200000
                    
                    	**mandatory**\: True
                    
                    .. attribute:: warning_threshold
                    
                    	Set threshold to print warning
                    	**type**\:  int
                    
                    	**range:** 1..200000
                    
                    	**default value**\: 100000
                    
                    .. attribute:: _is_presence
                    
                    	Is present if this instance represents presence container else not
                    	**type**\: bool
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'ipv4-pim-cfg'
                    _revision = '2016-06-01'

                    def __init__(self):
                        self.parent = None
                        self._is_presence = True
                        self.maximum_routes = None
                        self.warning_threshold = None

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-ipv4-pim-cfg:pim/Cisco-IOS-XR-ipv4-pim-cfg:default-context/Cisco-IOS-XR-ipv4-pim-cfg:ipv4/Cisco-IOS-XR-ipv4-pim-cfg:maximum/Cisco-IOS-XR-ipv4-pim-cfg:routes'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self._is_presence:
                            return True
                        if self.maximum_routes is not None:
                            return True

                        if self.warning_threshold is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_pim_cfg as meta
                        return meta._meta_table['Pim.DefaultContext.Ipv4.Maximum.Routes']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-ipv4-pim-cfg:pim/Cisco-IOS-XR-ipv4-pim-cfg:default-context/Cisco-IOS-XR-ipv4-pim-cfg:ipv4/Cisco-IOS-XR-ipv4-pim-cfg:maximum'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.bsr_candidate_rp_cache is not None and self.bsr_candidate_rp_cache._has_data():
                        return True

                    if self.bsr_global_candidate_rp_cache is not None and self.bsr_global_candidate_rp_cache._has_data():
                        return True

                    if self.bsr_global_group_mappings is not None and self.bsr_global_group_mappings._has_data():
                        return True

                    if self.bsr_group_mappings is not None and self.bsr_group_mappings._has_data():
                        return True

                    if self.global_group_mappings_auto_rp is not None and self.global_group_mappings_auto_rp._has_data():
                        return True

                    if self.global_high_priority_packet_queue is not None:
                        return True

                    if self.global_low_priority_packet_queue is not None:
                        return True

                    if self.global_register_states is not None and self.global_register_states._has_data():
                        return True

                    if self.global_route_interfaces is not None and self.global_route_interfaces._has_data():
                        return True

                    if self.global_routes is not None and self.global_routes._has_data():
                        return True

                    if self.group_mappings_auto_rp is not None and self.group_mappings_auto_rp._has_data():
                        return True

                    if self.register_states is not None and self.register_states._has_data():
                        return True

                    if self.route_interfaces is not None and self.route_interfaces._has_data():
                        return True

                    if self.routes is not None and self.routes._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_pim_cfg as meta
                    return meta._meta_table['Pim.DefaultContext.Ipv4.Maximum']['meta_info']


            class Ssm(object):
                """
                Configure IP Multicast SSM
                
                .. attribute:: disable
                
                	TRUE if SSM is disabled on this router
                	**type**\:  bool
                
                	**default value**\: false
                
                .. attribute:: range
                
                	Access list of groups enabled with SSM
                	**type**\:  str
                
                	**length:** 1..64
                
                

                """

                _prefix = 'ipv4-pim-cfg'
                _revision = '2016-06-01'

                def __init__(self):
                    self.parent = None
                    self.disable = None
                    self.range = None

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-ipv4-pim-cfg:pim/Cisco-IOS-XR-ipv4-pim-cfg:default-context/Cisco-IOS-XR-ipv4-pim-cfg:ipv4/Cisco-IOS-XR-ipv4-pim-cfg:ssm'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.disable is not None:
                        return True

                    if self.range is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_pim_cfg as meta
                    return meta._meta_table['Pim.DefaultContext.Ipv4.Ssm']['meta_info']


            class Injects(object):
                """
                Inject Explicit PIM RPF Vector Proxy's
                
                .. attribute:: inject
                
                	Inject Explicit PIM RPF Vector Proxy's
                	**type**\: list of    :py:class:`Inject <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.DefaultContext.Ipv4.Injects.Inject>`
                
                

                """

                _prefix = 'ipv4-pim-cfg'
                _revision = '2016-06-01'

                def __init__(self):
                    self.parent = None
                    self.inject = YList()
                    self.inject.parent = self
                    self.inject.name = 'inject'


                class Inject(object):
                    """
                    Inject Explicit PIM RPF Vector Proxy's
                    
                    .. attribute:: source_address  <key>
                    
                    	Source Address
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: prefix_length  <key>
                    
                    	Masklen
                    	**type**\:  int
                    
                    	**range:** 0..32
                    
                    .. attribute:: rpf_proxy_address
                    
                    	RPF Proxy Address
                    	**type**\:  list of str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    

                    """

                    _prefix = 'ipv4-pim-cfg'
                    _revision = '2016-06-01'

                    def __init__(self):
                        self.parent = None
                        self.source_address = None
                        self.prefix_length = None
                        self.rpf_proxy_address = YLeafList()
                        self.rpf_proxy_address.parent = self
                        self.rpf_proxy_address.name = 'rpf_proxy_address'

                    @property
                    def _common_path(self):
                        if self.source_address is None:
                            raise YPYModelError('Key property source_address is None')
                        if self.prefix_length is None:
                            raise YPYModelError('Key property prefix_length is None')

                        return '/Cisco-IOS-XR-ipv4-pim-cfg:pim/Cisco-IOS-XR-ipv4-pim-cfg:default-context/Cisco-IOS-XR-ipv4-pim-cfg:ipv4/Cisco-IOS-XR-ipv4-pim-cfg:injects/Cisco-IOS-XR-ipv4-pim-cfg:inject[Cisco-IOS-XR-ipv4-pim-cfg:source-address = ' + str(self.source_address) + '][Cisco-IOS-XR-ipv4-pim-cfg:prefix-length = ' + str(self.prefix_length) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.source_address is not None:
                            return True

                        if self.prefix_length is not None:
                            return True

                        if self.rpf_proxy_address is not None:
                            for child in self.rpf_proxy_address:
                                if child is not None:
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_pim_cfg as meta
                        return meta._meta_table['Pim.DefaultContext.Ipv4.Injects.Inject']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-ipv4-pim-cfg:pim/Cisco-IOS-XR-ipv4-pim-cfg:default-context/Cisco-IOS-XR-ipv4-pim-cfg:ipv4/Cisco-IOS-XR-ipv4-pim-cfg:injects'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.inject is not None:
                        for child_ref in self.inject:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_pim_cfg as meta
                    return meta._meta_table['Pim.DefaultContext.Ipv4.Injects']['meta_info']


            class BidirRpAddresses(object):
                """
                Configure Bidirectional PIM Rendezvous Point
                
                .. attribute:: bidir_rp_address
                
                	Address of the Rendezvous Point
                	**type**\: list of    :py:class:`BidirRpAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.DefaultContext.Ipv4.BidirRpAddresses.BidirRpAddress>`
                
                

                """

                _prefix = 'ipv4-pim-cfg'
                _revision = '2016-06-01'

                def __init__(self):
                    self.parent = None
                    self.bidir_rp_address = YList()
                    self.bidir_rp_address.parent = self
                    self.bidir_rp_address.name = 'bidir_rp_address'


                class BidirRpAddress(object):
                    """
                    Address of the Rendezvous Point
                    
                    .. attribute:: rp_address  <key>
                    
                    	RP address of Rendezvous Point
                    	**type**\: one of the below types:
                    
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    
                    ----
                    	**type**\:  str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    
                    ----
                    .. attribute:: access_list_name
                    
                    	Access list of groups that should map to a given RP
                    	**type**\:  str
                    
                    	**length:** 1..64
                    
                    .. attribute:: auto_rp_override
                    
                    	TRUE Indicates if static RP config overrides AutoRP and BSR
                    	**type**\:  bool
                    
                    

                    """

                    _prefix = 'ipv4-pim-cfg'
                    _revision = '2016-06-01'

                    def __init__(self):
                        self.parent = None
                        self.rp_address = None
                        self.access_list_name = None
                        self.auto_rp_override = None

                    @property
                    def _common_path(self):
                        if self.rp_address is None:
                            raise YPYModelError('Key property rp_address is None')

                        return '/Cisco-IOS-XR-ipv4-pim-cfg:pim/Cisco-IOS-XR-ipv4-pim-cfg:default-context/Cisco-IOS-XR-ipv4-pim-cfg:ipv4/Cisco-IOS-XR-ipv4-pim-cfg:bidir-rp-addresses/Cisco-IOS-XR-ipv4-pim-cfg:bidir-rp-address[Cisco-IOS-XR-ipv4-pim-cfg:rp-address = ' + str(self.rp_address) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.rp_address is not None:
                            return True

                        if self.access_list_name is not None:
                            return True

                        if self.auto_rp_override is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_pim_cfg as meta
                        return meta._meta_table['Pim.DefaultContext.Ipv4.BidirRpAddresses.BidirRpAddress']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-ipv4-pim-cfg:pim/Cisco-IOS-XR-ipv4-pim-cfg:default-context/Cisco-IOS-XR-ipv4-pim-cfg:ipv4/Cisco-IOS-XR-ipv4-pim-cfg:bidir-rp-addresses'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.bidir_rp_address is not None:
                        for child_ref in self.bidir_rp_address:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_pim_cfg as meta
                    return meta._meta_table['Pim.DefaultContext.Ipv4.BidirRpAddresses']['meta_info']


            class Bsr(object):
                """
                PIM BSR configuration
                
                .. attribute:: candidate_bsr
                
                	PIM Candidate BSR configuration
                	**type**\:   :py:class:`CandidateBsr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.DefaultContext.Ipv4.Bsr.CandidateBsr>`
                
                	**presence node**\: True
                
                .. attribute:: candidate_rps
                
                	PIM RP configuration
                	**type**\:   :py:class:`CandidateRps <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.DefaultContext.Ipv4.Bsr.CandidateRps>`
                
                

                """

                _prefix = 'ipv4-pim-cfg'
                _revision = '2016-06-01'

                def __init__(self):
                    self.parent = None
                    self.candidate_bsr = None
                    self.candidate_rps = Pim.DefaultContext.Ipv4.Bsr.CandidateRps()
                    self.candidate_rps.parent = self


                class CandidateBsr(object):
                    """
                    PIM Candidate BSR configuration
                    
                    .. attribute:: address
                    
                    	BSR Address configured
                    	**type**\: one of the below types:
                    
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    	**mandatory**\: True
                    
                    
                    ----
                    	**type**\:  str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    	**mandatory**\: True
                    
                    
                    ----
                    .. attribute:: prefix_length
                    
                    	Hash Mask Length for this candidate BSR
                    	**type**\:  int
                    
                    	**range:** 0..32
                    
                    	**default value**\: 30
                    
                    .. attribute:: priority
                    
                    	Priority of the Candidate BSR
                    	**type**\:  int
                    
                    	**range:** 1..255
                    
                    	**default value**\: 1
                    
                    .. attribute:: _is_presence
                    
                    	Is present if this instance represents presence container else not
                    	**type**\: bool
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'ipv4-pim-cfg'
                    _revision = '2016-06-01'

                    def __init__(self):
                        self.parent = None
                        self._is_presence = True
                        self.address = None
                        self.prefix_length = None
                        self.priority = None

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-ipv4-pim-cfg:pim/Cisco-IOS-XR-ipv4-pim-cfg:default-context/Cisco-IOS-XR-ipv4-pim-cfg:ipv4/Cisco-IOS-XR-ipv4-pim-cfg:bsr/Cisco-IOS-XR-ipv4-pim-cfg:candidate-bsr'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self._is_presence:
                            return True
                        if self.address is not None:
                            return True

                        if self.prefix_length is not None:
                            return True

                        if self.priority is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_pim_cfg as meta
                        return meta._meta_table['Pim.DefaultContext.Ipv4.Bsr.CandidateBsr']['meta_info']


                class CandidateRps(object):
                    """
                    PIM RP configuration
                    
                    .. attribute:: candidate_rp
                    
                    	Address of PIM SM BSR Candidate\-RP
                    	**type**\: list of    :py:class:`CandidateRp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.DefaultContext.Ipv4.Bsr.CandidateRps.CandidateRp>`
                    
                    

                    """

                    _prefix = 'ipv4-pim-cfg'
                    _revision = '2016-06-01'

                    def __init__(self):
                        self.parent = None
                        self.candidate_rp = YList()
                        self.candidate_rp.parent = self
                        self.candidate_rp.name = 'candidate_rp'


                    class CandidateRp(object):
                        """
                        Address of PIM SM BSR Candidate\-RP
                        
                        .. attribute:: address  <key>
                        
                        	Address of Candidate\-RP
                        	**type**\: one of the below types:
                        
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        .. attribute:: mode  <key>
                        
                        	SM or Bidir
                        	**type**\:   :py:class:`PimProtocolModeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.PimProtocolModeEnum>`
                        
                        .. attribute:: group_list
                        
                        	Access\-list specifying the group range for the Candidate\-RP
                        	**type**\:  str
                        
                        	**length:** 1..64
                        
                        .. attribute:: interval
                        
                        	Advertisement interval
                        	**type**\:  int
                        
                        	**range:** 30..600
                        
                        	**default value**\: 60
                        
                        .. attribute:: priority
                        
                        	Priority of the CRP
                        	**type**\:  int
                        
                        	**range:** 1..255
                        
                        	**default value**\: 192
                        
                        

                        """

                        _prefix = 'ipv4-pim-cfg'
                        _revision = '2016-06-01'

                        def __init__(self):
                            self.parent = None
                            self.address = None
                            self.mode = None
                            self.group_list = None
                            self.interval = None
                            self.priority = None

                        @property
                        def _common_path(self):
                            if self.address is None:
                                raise YPYModelError('Key property address is None')
                            if self.mode is None:
                                raise YPYModelError('Key property mode is None')

                            return '/Cisco-IOS-XR-ipv4-pim-cfg:pim/Cisco-IOS-XR-ipv4-pim-cfg:default-context/Cisco-IOS-XR-ipv4-pim-cfg:ipv4/Cisco-IOS-XR-ipv4-pim-cfg:bsr/Cisco-IOS-XR-ipv4-pim-cfg:candidate-rps/Cisco-IOS-XR-ipv4-pim-cfg:candidate-rp[Cisco-IOS-XR-ipv4-pim-cfg:address = ' + str(self.address) + '][Cisco-IOS-XR-ipv4-pim-cfg:mode = ' + str(self.mode) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.address is not None:
                                return True

                            if self.mode is not None:
                                return True

                            if self.group_list is not None:
                                return True

                            if self.interval is not None:
                                return True

                            if self.priority is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_pim_cfg as meta
                            return meta._meta_table['Pim.DefaultContext.Ipv4.Bsr.CandidateRps.CandidateRp']['meta_info']

                    @property
                    def _common_path(self):

                        return '/Cisco-IOS-XR-ipv4-pim-cfg:pim/Cisco-IOS-XR-ipv4-pim-cfg:default-context/Cisco-IOS-XR-ipv4-pim-cfg:ipv4/Cisco-IOS-XR-ipv4-pim-cfg:bsr/Cisco-IOS-XR-ipv4-pim-cfg:candidate-rps'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.candidate_rp is not None:
                            for child_ref in self.candidate_rp:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_pim_cfg as meta
                        return meta._meta_table['Pim.DefaultContext.Ipv4.Bsr.CandidateRps']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-ipv4-pim-cfg:pim/Cisco-IOS-XR-ipv4-pim-cfg:default-context/Cisco-IOS-XR-ipv4-pim-cfg:ipv4/Cisco-IOS-XR-ipv4-pim-cfg:bsr'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.candidate_bsr is not None and self.candidate_bsr._has_data():
                        return True

                    if self.candidate_rps is not None and self.candidate_rps._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_pim_cfg as meta
                    return meta._meta_table['Pim.DefaultContext.Ipv4.Bsr']['meta_info']


            class Paths(object):
                """
                Inject PIM RPF Vector Proxy's
                
                .. attribute:: path
                
                	Inject PIM RPF Vector Proxy's
                	**type**\: list of    :py:class:`Path <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.DefaultContext.Ipv4.Paths.Path>`
                
                

                """

                _prefix = 'ipv4-pim-cfg'
                _revision = '2016-06-01'

                def __init__(self):
                    self.parent = None
                    self.path = YList()
                    self.path.parent = self
                    self.path.name = 'path'


                class Path(object):
                    """
                    Inject PIM RPF Vector Proxy's
                    
                    .. attribute:: source_address  <key>
                    
                    	Source Address
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: prefix_length  <key>
                    
                    	Masklen
                    	**type**\:  int
                    
                    	**range:** 0..32
                    
                    .. attribute:: rpf_proxy_address
                    
                    	RPF Proxy Address
                    	**type**\:  list of str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    

                    """

                    _prefix = 'ipv4-pim-cfg'
                    _revision = '2016-06-01'

                    def __init__(self):
                        self.parent = None
                        self.source_address = None
                        self.prefix_length = None
                        self.rpf_proxy_address = YLeafList()
                        self.rpf_proxy_address.parent = self
                        self.rpf_proxy_address.name = 'rpf_proxy_address'

                    @property
                    def _common_path(self):
                        if self.source_address is None:
                            raise YPYModelError('Key property source_address is None')
                        if self.prefix_length is None:
                            raise YPYModelError('Key property prefix_length is None')

                        return '/Cisco-IOS-XR-ipv4-pim-cfg:pim/Cisco-IOS-XR-ipv4-pim-cfg:default-context/Cisco-IOS-XR-ipv4-pim-cfg:ipv4/Cisco-IOS-XR-ipv4-pim-cfg:paths/Cisco-IOS-XR-ipv4-pim-cfg:path[Cisco-IOS-XR-ipv4-pim-cfg:source-address = ' + str(self.source_address) + '][Cisco-IOS-XR-ipv4-pim-cfg:prefix-length = ' + str(self.prefix_length) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.source_address is not None:
                            return True

                        if self.prefix_length is not None:
                            return True

                        if self.rpf_proxy_address is not None:
                            for child in self.rpf_proxy_address:
                                if child is not None:
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_pim_cfg as meta
                        return meta._meta_table['Pim.DefaultContext.Ipv4.Paths.Path']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-ipv4-pim-cfg:pim/Cisco-IOS-XR-ipv4-pim-cfg:default-context/Cisco-IOS-XR-ipv4-pim-cfg:ipv4/Cisco-IOS-XR-ipv4-pim-cfg:paths'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.path is not None:
                        for child_ref in self.path:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_pim_cfg as meta
                    return meta._meta_table['Pim.DefaultContext.Ipv4.Paths']['meta_info']


            class AllowRp(object):
                """
                Enable allow\-rp filtering for SM joins
                
                .. attribute:: group_list_name
                
                	Access\-list specifiying applicable groups
                	**type**\:  str
                
                	**length:** 1..64
                
                .. attribute:: rp_list_name
                
                	Access\-list specifiying applicable RPs
                	**type**\:  str
                
                	**length:** 1..64
                
                .. attribute:: _is_presence
                
                	Is present if this instance represents presence container else not
                	**type**\: bool
                
                

                This class is a :ref:`presence class<presence-class>`

                """

                _prefix = 'ipv4-pim-cfg'
                _revision = '2016-06-01'

                def __init__(self):
                    self.parent = None
                    self._is_presence = True
                    self.group_list_name = None
                    self.rp_list_name = None

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-ipv4-pim-cfg:pim/Cisco-IOS-XR-ipv4-pim-cfg:default-context/Cisco-IOS-XR-ipv4-pim-cfg:ipv4/Cisco-IOS-XR-ipv4-pim-cfg:allow-rp'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self._is_presence:
                        return True
                    if self.group_list_name is not None:
                        return True

                    if self.rp_list_name is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_pim_cfg as meta
                    return meta._meta_table['Pim.DefaultContext.Ipv4.AllowRp']['meta_info']


            class Convergence(object):
                """
                Configure convergence parameters
                
                .. attribute:: link_down_prune_delay
                
                	Delay prunes if route join state transitions to not\-joined on link down
                	**type**\:  int
                
                	**range:** 0..60
                
                	**units**\: second
                
                .. attribute:: rpf_conflict_join_delay
                
                	Dampen first join if RPF path is through one of the downstream neighbor
                	**type**\:  int
                
                	**range:** 0..15
                
                	**units**\: second
                
                

                """

                _prefix = 'ipv4-pim-cfg'
                _revision = '2016-06-01'

                def __init__(self):
                    self.parent = None
                    self.link_down_prune_delay = None
                    self.rpf_conflict_join_delay = None

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-ipv4-pim-cfg:pim/Cisco-IOS-XR-ipv4-pim-cfg:default-context/Cisco-IOS-XR-ipv4-pim-cfg:ipv4/Cisco-IOS-XR-ipv4-pim-cfg:convergence'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.link_down_prune_delay is not None:
                        return True

                    if self.rpf_conflict_join_delay is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_pim_cfg as meta
                    return meta._meta_table['Pim.DefaultContext.Ipv4.Convergence']['meta_info']


            class CjMulticastOnlyFrrs(object):
                """
                Clone Join Multicast Only FRR
                
                .. attribute:: cj_multicast_only_frr
                
                	Clone Join Multicast Only FRR
                	**type**\: list of    :py:class:`CjMulticastOnlyFrr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.DefaultContext.Ipv4.CjMulticastOnlyFrrs.CjMulticastOnlyFrr>`
                
                

                """

                _prefix = 'ipv4-pim-cfg'
                _revision = '2016-06-01'

                def __init__(self):
                    self.parent = None
                    self.cj_multicast_only_frr = YList()
                    self.cj_multicast_only_frr.parent = self
                    self.cj_multicast_only_frr.name = 'cj_multicast_only_frr'


                class CjMulticastOnlyFrr(object):
                    """
                    Clone Join Multicast Only FRR
                    
                    .. attribute:: source  <key>
                    
                    	Original address
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: primary  <key>
                    
                    	Primary address
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: backup  <key>
                    
                    	Backup address
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: prefix_length  <key>
                    
                    	Masklen
                    	**type**\:  int
                    
                    	**range:** 0..32
                    
                    

                    """

                    _prefix = 'ipv4-pim-cfg'
                    _revision = '2016-06-01'

                    def __init__(self):
                        self.parent = None
                        self.source = None
                        self.primary = None
                        self.backup = None
                        self.prefix_length = None

                    @property
                    def _common_path(self):
                        if self.source is None:
                            raise YPYModelError('Key property source is None')
                        if self.primary is None:
                            raise YPYModelError('Key property primary is None')
                        if self.backup is None:
                            raise YPYModelError('Key property backup is None')
                        if self.prefix_length is None:
                            raise YPYModelError('Key property prefix_length is None')

                        return '/Cisco-IOS-XR-ipv4-pim-cfg:pim/Cisco-IOS-XR-ipv4-pim-cfg:default-context/Cisco-IOS-XR-ipv4-pim-cfg:ipv4/Cisco-IOS-XR-ipv4-pim-cfg:cj-multicast-only-frrs/Cisco-IOS-XR-ipv4-pim-cfg:cj-multicast-only-frr[Cisco-IOS-XR-ipv4-pim-cfg:source = ' + str(self.source) + '][Cisco-IOS-XR-ipv4-pim-cfg:primary = ' + str(self.primary) + '][Cisco-IOS-XR-ipv4-pim-cfg:backup = ' + str(self.backup) + '][Cisco-IOS-XR-ipv4-pim-cfg:prefix-length = ' + str(self.prefix_length) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.source is not None:
                            return True

                        if self.primary is not None:
                            return True

                        if self.backup is not None:
                            return True

                        if self.prefix_length is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_pim_cfg as meta
                        return meta._meta_table['Pim.DefaultContext.Ipv4.CjMulticastOnlyFrrs.CjMulticastOnlyFrr']['meta_info']

                @property
                def _common_path(self):

                    return '/Cisco-IOS-XR-ipv4-pim-cfg:pim/Cisco-IOS-XR-ipv4-pim-cfg:default-context/Cisco-IOS-XR-ipv4-pim-cfg:ipv4/Cisco-IOS-XR-ipv4-pim-cfg:cj-multicast-only-frrs'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.cj_multicast_only_frr is not None:
                        for child_ref in self.cj_multicast_only_frr:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_pim_cfg as meta
                    return meta._meta_table['Pim.DefaultContext.Ipv4.CjMulticastOnlyFrrs']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-ipv4-pim-cfg:pim/Cisco-IOS-XR-ipv4-pim-cfg:default-context/Cisco-IOS-XR-ipv4-pim-cfg:ipv4'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.accept_register is not None:
                    return True

                if self.allow_rp is not None and self.allow_rp._has_data():
                    return True

                if self.auto_rp_candidate_rps is not None and self.auto_rp_candidate_rps._has_data():
                    return True

                if self.auto_rp_disable is not None:
                    return True

                if self.auto_rp_mapping_agent is not None and self.auto_rp_mapping_agent._has_data():
                    return True

                if self.bidir_rp_addresses is not None and self.bidir_rp_addresses._has_data():
                    return True

                if self.bsr is not None and self.bsr._has_data():
                    return True

                if self.cj_multicast_only_frrs is not None and self.cj_multicast_only_frrs._has_data():
                    return True

                if self.convergence is not None and self.convergence._has_data():
                    return True

                if self.cs_multicast_only_frrs is not None and self.cs_multicast_only_frrs._has_data():
                    return True

                if self.inheritable_defaults is not None and self.inheritable_defaults._has_data():
                    return True

                if self.injects is not None and self.injects._has_data():
                    return True

                if self.interfaces is not None and self.interfaces._has_data():
                    return True

                if self.log_neighbor_changes is not None:
                    return True

                if self.maximum is not None and self.maximum._has_data():
                    return True

                if self.multicast_only_frr is not None and self.multicast_only_frr._has_data():
                    return True

                if self.multipath is not None:
                    return True

                if self.neighbor_check_on_receive is not None:
                    return True

                if self.neighbor_check_on_send is not None:
                    return True

                if self.neighbor_filter is not None:
                    return True

                if self.nsf is not None and self.nsf._has_data():
                    return True

                if self.old_register_checksum is not None:
                    return True

                if self.paths is not None and self.paths._has_data():
                    return True

                if self.register_source is not None:
                    return True

                if self.rp_static_deny is not None:
                    return True

                if self.rpf is not None and self.rpf._has_data():
                    return True

                if self.rpf_redirect is not None and self.rpf_redirect._has_data():
                    return True

                if self.rpf_vector_enable is not None and self.rpf_vector_enable._has_data():
                    return True

                if self.sg_expiry_timer is not None and self.sg_expiry_timer._has_data():
                    return True

                if self.sparse_mode_rp_addresses is not None and self.sparse_mode_rp_addresses._has_data():
                    return True

                if self.spt_threshold_infinity is not None:
                    return True

                if self.ssm is not None and self.ssm._has_data():
                    return True

                if self.ssm_allow_override is not None:
                    return True

                if self.suppress_data_registers is not None:
                    return True

                if self.suppress_rpf_prunes is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_pim_cfg as meta
                return meta._meta_table['Pim.DefaultContext.Ipv4']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ipv4-pim-cfg:pim/Cisco-IOS-XR-ipv4-pim-cfg:default-context'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self._is_presence:
                return True
            if self.ipv4 is not None and self.ipv4._has_data():
                return True

            if self.ipv6 is not None and self.ipv6._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_pim_cfg as meta
            return meta._meta_table['Pim.DefaultContext']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-ipv4-pim-cfg:pim'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self._is_presence:
            return True
        if self.default_context is not None and self.default_context._has_data():
            return True

        if self.vrfs is not None and self.vrfs._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_pim_cfg as meta
        return meta._meta_table['Pim']['meta_info']


