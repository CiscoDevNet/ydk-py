""" Cisco_IOS_XR_ipv4_pim_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ipv4\-pim package configuration.

This module contains definitions
for the following management objects\:
  pim\: PIM configuration

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class PimMultipath(Enum):
    """
    PimMultipath (Enum Class)

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

    enable = Enum.YLeaf(0, "enable")

    interface_hash = Enum.YLeaf(1, "interface-hash")

    source_hash = Enum.YLeaf(2, "source-hash")

    source_next_hop_hash = Enum.YLeaf(3, "source-next-hop-hash")

    source_group_hash = Enum.YLeaf(4, "source-group-hash")


class PimProtocolMode(Enum):
    """
    PimProtocolMode (Enum Class)

    Pim protocol mode

    .. data:: sm = 0

    	Sparse Mode

    .. data:: bidir = 1

    	Bidirectional

    """

    sm = Enum.YLeaf(0, "sm")

    bidir = Enum.YLeaf(1, "bidir")



class Pim(Entity):
    """
    PIM configuration
    
    .. attribute:: vrfs
    
    	VRF table
    	**type**\:  :py:class:`Vrfs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.Vrfs>`
    
    .. attribute:: default_context
    
    	Default Context
    	**type**\:  :py:class:`DefaultContext <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.DefaultContext>`
    
    

    """

    _prefix = 'ipv4-pim-cfg'
    _revision = '2017-10-15'

    def __init__(self):
        super(Pim, self).__init__()
        self._top_entity = None

        self.yang_name = "pim"
        self.yang_parent_name = "Cisco-IOS-XR-ipv4-pim-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("vrfs", ("vrfs", Pim.Vrfs)), ("default-context", ("default_context", Pim.DefaultContext))])
        self._leafs = OrderedDict()

        self.vrfs = Pim.Vrfs()
        self.vrfs.parent = self
        self._children_name_map["vrfs"] = "vrfs"

        self.default_context = Pim.DefaultContext()
        self.default_context.parent = self
        self._children_name_map["default_context"] = "default-context"
        self._segment_path = lambda: "Cisco-IOS-XR-ipv4-pim-cfg:pim"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Pim, [], name, value)


    class Vrfs(Entity):
        """
        VRF table
        
        .. attribute:: vrf
        
        	VRF name
        	**type**\: list of  		 :py:class:`Vrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.Vrfs.Vrf>`
        
        

        """

        _prefix = 'ipv4-pim-cfg'
        _revision = '2017-10-15'

        def __init__(self):
            super(Pim.Vrfs, self).__init__()

            self.yang_name = "vrfs"
            self.yang_parent_name = "pim"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("vrf", ("vrf", Pim.Vrfs.Vrf))])
            self._leafs = OrderedDict()

            self.vrf = YList(self)
            self._segment_path = lambda: "vrfs"
            self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-pim-cfg:pim/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Pim.Vrfs, [], name, value)


        class Vrf(Entity):
            """
            VRF name
            
            .. attribute:: vrf_name  (key)
            
            	VRF name
            	**type**\: str
            
            	**length:** 1..32
            
            .. attribute:: ipv4
            
            	IPV4 commands
            	**type**\:  :py:class:`Ipv4 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.Vrfs.Vrf.Ipv4>`
            
            .. attribute:: ipv6
            
            	IPV6 commands
            	**type**\:  :py:class:`Ipv6 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.Vrfs.Vrf.Ipv6>`
            
            

            """

            _prefix = 'ipv4-pim-cfg'
            _revision = '2017-10-15'

            def __init__(self):
                super(Pim.Vrfs.Vrf, self).__init__()

                self.yang_name = "vrf"
                self.yang_parent_name = "vrfs"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['vrf_name']
                self._child_classes = OrderedDict([("ipv4", ("ipv4", Pim.Vrfs.Vrf.Ipv4)), ("ipv6", ("ipv6", Pim.Vrfs.Vrf.Ipv6))])
                self._leafs = OrderedDict([
                    ('vrf_name', (YLeaf(YType.str, 'vrf-name'), ['str'])),
                ])
                self.vrf_name = None

                self.ipv4 = Pim.Vrfs.Vrf.Ipv4()
                self.ipv4.parent = self
                self._children_name_map["ipv4"] = "ipv4"

                self.ipv6 = Pim.Vrfs.Vrf.Ipv6()
                self.ipv6.parent = self
                self._children_name_map["ipv6"] = "ipv6"
                self._segment_path = lambda: "vrf" + "[vrf-name='" + str(self.vrf_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-pim-cfg:pim/vrfs/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Pim.Vrfs.Vrf, ['vrf_name'], name, value)


            class Ipv4(Entity):
                """
                IPV4 commands
                
                .. attribute:: neighbor_check_on_receive
                
                	Enable PIM neighbor checking when receiving PIM messages
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: old_register_checksum
                
                	Generate registers compatible with older IOS versions
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: sparse_mode_rp_addresses
                
                	Configure Sparse\-Mode Rendezvous Point
                	**type**\:  :py:class:`SparseModeRpAddresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.Vrfs.Vrf.Ipv4.SparseModeRpAddresses>`
                
                .. attribute:: neighbor_filter
                
                	Access\-list of neighbors to be filtered
                	**type**\: str
                
                	**length:** 1..64
                
                .. attribute:: inheritable_defaults
                
                	Inheritable defaults
                	**type**\:  :py:class:`InheritableDefaults <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.Vrfs.Vrf.Ipv4.InheritableDefaults>`
                
                .. attribute:: spt_threshold_infinity
                
                	Configure threshold of infinity for switching to SPT on last\-hop
                	**type**\: str
                
                .. attribute:: log_neighbor_changes
                
                	PIM neighbor state change logging is turned on if configured
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: rpf
                
                	Configure RPF options
                	**type**\:  :py:class:`Rpf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.Vrfs.Vrf.Ipv4.Rpf>`
                
                .. attribute:: register_source
                
                	Source address to use for register messages
                	**type**\: str
                
                	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                
                .. attribute:: maximum
                
                	Configure PIM State Limits
                	**type**\:  :py:class:`Maximum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.Vrfs.Vrf.Ipv4.Maximum>`
                
                .. attribute:: accept_register
                
                	Access\-list which specifies unauthorized sources
                	**type**\: str
                
                	**length:** 1..64
                
                .. attribute:: sg_expiry_timer
                
                	Configure expiry timer for S,G routes
                	**type**\:  :py:class:`SgExpiryTimer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.Vrfs.Vrf.Ipv4.SgExpiryTimer>`
                
                .. attribute:: rpf_vector_enable
                
                	Enable PIM RPF Vector Proxy's
                	**type**\:  :py:class:`RpfVectorEnable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.Vrfs.Vrf.Ipv4.RpfVectorEnable>`
                
                	**presence node**\: True
                
                .. attribute:: suppress_rpf_prunes
                
                	Suppress prunes triggered as a result of RPF changes
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: ssm
                
                	Configure IP Multicast SSM
                	**type**\:  :py:class:`Ssm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.Vrfs.Vrf.Ipv4.Ssm>`
                
                .. attribute:: injects
                
                	Inject Explicit PIM RPF Vector Proxy's
                	**type**\:  :py:class:`Injects <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.Vrfs.Vrf.Ipv4.Injects>`
                
                .. attribute:: bidir_rp_addresses
                
                	Configure Bidirectional PIM Rendezvous Point
                	**type**\:  :py:class:`BidirRpAddresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.Vrfs.Vrf.Ipv4.BidirRpAddresses>`
                
                .. attribute:: ssm_allow_override
                
                	Allow SSM ranges to be overridden by more specific ranges
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: bsr
                
                	PIM BSR configuration
                	**type**\:  :py:class:`Bsr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.Vrfs.Vrf.Ipv4.Bsr>`
                
                .. attribute:: mofrr
                
                	Multicast Only Fast Re\-Route
                	**type**\:  :py:class:`Mofrr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.Vrfs.Vrf.Ipv4.Mofrr>`
                
                .. attribute:: multipath
                
                	Enable equal\-cost multipath routing
                	**type**\:  :py:class:`PimMultipath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.PimMultipath>`
                
                .. attribute:: rp_static_deny
                
                	Configure static RP deny range
                	**type**\: str
                
                	**length:** 1..64
                
                .. attribute:: paths
                
                	Inject PIM RPF Vector Proxy's
                	**type**\:  :py:class:`Paths <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.Vrfs.Vrf.Ipv4.Paths>`
                
                .. attribute:: allow_rp
                
                	Enable allow\-rp filtering for SM joins
                	**type**\:  :py:class:`AllowRp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.Vrfs.Vrf.Ipv4.AllowRp>`
                
                	**presence node**\: True
                
                .. attribute:: suppress_data_registers
                
                	Suppress data registers after initial state setup
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: neighbor_check_on_send
                
                	Enable PIM neighbor checking when sending join\-prunes
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: convergence
                
                	Configure convergence parameters
                	**type**\:  :py:class:`Convergence <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.Vrfs.Vrf.Ipv4.Convergence>`
                
                .. attribute:: interfaces
                
                	Interface\-level Configuration
                	**type**\:  :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.Vrfs.Vrf.Ipv4.Interfaces>`
                
                .. attribute:: auto_rp_disable
                
                	Disable Rendezvous Point discovery through the AutoRP protocol
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                

                """

                _prefix = 'ipv4-pim-cfg'
                _revision = '2017-10-15'

                def __init__(self):
                    super(Pim.Vrfs.Vrf.Ipv4, self).__init__()

                    self.yang_name = "ipv4"
                    self.yang_parent_name = "vrf"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("sparse-mode-rp-addresses", ("sparse_mode_rp_addresses", Pim.Vrfs.Vrf.Ipv4.SparseModeRpAddresses)), ("inheritable-defaults", ("inheritable_defaults", Pim.Vrfs.Vrf.Ipv4.InheritableDefaults)), ("rpf", ("rpf", Pim.Vrfs.Vrf.Ipv4.Rpf)), ("maximum", ("maximum", Pim.Vrfs.Vrf.Ipv4.Maximum)), ("sg-expiry-timer", ("sg_expiry_timer", Pim.Vrfs.Vrf.Ipv4.SgExpiryTimer)), ("rpf-vector-enable", ("rpf_vector_enable", Pim.Vrfs.Vrf.Ipv4.RpfVectorEnable)), ("ssm", ("ssm", Pim.Vrfs.Vrf.Ipv4.Ssm)), ("injects", ("injects", Pim.Vrfs.Vrf.Ipv4.Injects)), ("bidir-rp-addresses", ("bidir_rp_addresses", Pim.Vrfs.Vrf.Ipv4.BidirRpAddresses)), ("bsr", ("bsr", Pim.Vrfs.Vrf.Ipv4.Bsr)), ("mofrr", ("mofrr", Pim.Vrfs.Vrf.Ipv4.Mofrr)), ("paths", ("paths", Pim.Vrfs.Vrf.Ipv4.Paths)), ("allow-rp", ("allow_rp", Pim.Vrfs.Vrf.Ipv4.AllowRp)), ("convergence", ("convergence", Pim.Vrfs.Vrf.Ipv4.Convergence)), ("interfaces", ("interfaces", Pim.Vrfs.Vrf.Ipv4.Interfaces))])
                    self._leafs = OrderedDict([
                        ('neighbor_check_on_receive', (YLeaf(YType.empty, 'neighbor-check-on-receive'), ['Empty'])),
                        ('old_register_checksum', (YLeaf(YType.empty, 'old-register-checksum'), ['Empty'])),
                        ('neighbor_filter', (YLeaf(YType.str, 'neighbor-filter'), ['str'])),
                        ('spt_threshold_infinity', (YLeaf(YType.str, 'spt-threshold-infinity'), ['str'])),
                        ('log_neighbor_changes', (YLeaf(YType.empty, 'log-neighbor-changes'), ['Empty'])),
                        ('register_source', (YLeaf(YType.str, 'register-source'), ['str'])),
                        ('accept_register', (YLeaf(YType.str, 'accept-register'), ['str'])),
                        ('suppress_rpf_prunes', (YLeaf(YType.empty, 'suppress-rpf-prunes'), ['Empty'])),
                        ('ssm_allow_override', (YLeaf(YType.empty, 'ssm-allow-override'), ['Empty'])),
                        ('multipath', (YLeaf(YType.enumeration, 'multipath'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg', 'PimMultipath', '')])),
                        ('rp_static_deny', (YLeaf(YType.str, 'rp-static-deny'), ['str'])),
                        ('suppress_data_registers', (YLeaf(YType.empty, 'suppress-data-registers'), ['Empty'])),
                        ('neighbor_check_on_send', (YLeaf(YType.empty, 'neighbor-check-on-send'), ['Empty'])),
                        ('auto_rp_disable', (YLeaf(YType.empty, 'auto-rp-disable'), ['Empty'])),
                    ])
                    self.neighbor_check_on_receive = None
                    self.old_register_checksum = None
                    self.neighbor_filter = None
                    self.spt_threshold_infinity = None
                    self.log_neighbor_changes = None
                    self.register_source = None
                    self.accept_register = None
                    self.suppress_rpf_prunes = None
                    self.ssm_allow_override = None
                    self.multipath = None
                    self.rp_static_deny = None
                    self.suppress_data_registers = None
                    self.neighbor_check_on_send = None
                    self.auto_rp_disable = None

                    self.sparse_mode_rp_addresses = Pim.Vrfs.Vrf.Ipv4.SparseModeRpAddresses()
                    self.sparse_mode_rp_addresses.parent = self
                    self._children_name_map["sparse_mode_rp_addresses"] = "sparse-mode-rp-addresses"

                    self.inheritable_defaults = Pim.Vrfs.Vrf.Ipv4.InheritableDefaults()
                    self.inheritable_defaults.parent = self
                    self._children_name_map["inheritable_defaults"] = "inheritable-defaults"

                    self.rpf = Pim.Vrfs.Vrf.Ipv4.Rpf()
                    self.rpf.parent = self
                    self._children_name_map["rpf"] = "rpf"

                    self.maximum = Pim.Vrfs.Vrf.Ipv4.Maximum()
                    self.maximum.parent = self
                    self._children_name_map["maximum"] = "maximum"

                    self.sg_expiry_timer = Pim.Vrfs.Vrf.Ipv4.SgExpiryTimer()
                    self.sg_expiry_timer.parent = self
                    self._children_name_map["sg_expiry_timer"] = "sg-expiry-timer"

                    self.rpf_vector_enable = None
                    self._children_name_map["rpf_vector_enable"] = "rpf-vector-enable"

                    self.ssm = Pim.Vrfs.Vrf.Ipv4.Ssm()
                    self.ssm.parent = self
                    self._children_name_map["ssm"] = "ssm"

                    self.injects = Pim.Vrfs.Vrf.Ipv4.Injects()
                    self.injects.parent = self
                    self._children_name_map["injects"] = "injects"

                    self.bidir_rp_addresses = Pim.Vrfs.Vrf.Ipv4.BidirRpAddresses()
                    self.bidir_rp_addresses.parent = self
                    self._children_name_map["bidir_rp_addresses"] = "bidir-rp-addresses"

                    self.bsr = Pim.Vrfs.Vrf.Ipv4.Bsr()
                    self.bsr.parent = self
                    self._children_name_map["bsr"] = "bsr"

                    self.mofrr = Pim.Vrfs.Vrf.Ipv4.Mofrr()
                    self.mofrr.parent = self
                    self._children_name_map["mofrr"] = "mofrr"

                    self.paths = Pim.Vrfs.Vrf.Ipv4.Paths()
                    self.paths.parent = self
                    self._children_name_map["paths"] = "paths"

                    self.allow_rp = None
                    self._children_name_map["allow_rp"] = "allow-rp"

                    self.convergence = Pim.Vrfs.Vrf.Ipv4.Convergence()
                    self.convergence.parent = self
                    self._children_name_map["convergence"] = "convergence"

                    self.interfaces = Pim.Vrfs.Vrf.Ipv4.Interfaces()
                    self.interfaces.parent = self
                    self._children_name_map["interfaces"] = "interfaces"
                    self._segment_path = lambda: "ipv4"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Pim.Vrfs.Vrf.Ipv4, ['neighbor_check_on_receive', 'old_register_checksum', 'neighbor_filter', 'spt_threshold_infinity', 'log_neighbor_changes', 'register_source', 'accept_register', 'suppress_rpf_prunes', 'ssm_allow_override', 'multipath', 'rp_static_deny', 'suppress_data_registers', 'neighbor_check_on_send', 'auto_rp_disable'], name, value)


                class SparseModeRpAddresses(Entity):
                    """
                    Configure Sparse\-Mode Rendezvous Point
                    
                    .. attribute:: sparse_mode_rp_address
                    
                    	Address of the Rendezvous Point
                    	**type**\: list of  		 :py:class:`SparseModeRpAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.Vrfs.Vrf.Ipv4.SparseModeRpAddresses.SparseModeRpAddress>`
                    
                    

                    """

                    _prefix = 'ipv4-pim-cfg'
                    _revision = '2017-10-15'

                    def __init__(self):
                        super(Pim.Vrfs.Vrf.Ipv4.SparseModeRpAddresses, self).__init__()

                        self.yang_name = "sparse-mode-rp-addresses"
                        self.yang_parent_name = "ipv4"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("sparse-mode-rp-address", ("sparse_mode_rp_address", Pim.Vrfs.Vrf.Ipv4.SparseModeRpAddresses.SparseModeRpAddress))])
                        self._leafs = OrderedDict()

                        self.sparse_mode_rp_address = YList(self)
                        self._segment_path = lambda: "sparse-mode-rp-addresses"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Pim.Vrfs.Vrf.Ipv4.SparseModeRpAddresses, [], name, value)


                    class SparseModeRpAddress(Entity):
                        """
                        Address of the Rendezvous Point
                        
                        .. attribute:: rp_address  (key)
                        
                        	RP address of Rendezvous Point
                        	**type**\: union of the below types:
                        
                        		**type**\: str
                        
                        			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        		**type**\: str
                        
                        			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: access_list_name
                        
                        	Access list of groups that should map to a  given RP
                        	**type**\: str
                        
                        	**length:** 1..64
                        
                        .. attribute:: auto_rp_override
                        
                        	TRUE Indicates if static RP config overrides AutoRP and BSR
                        	**type**\: bool
                        
                        

                        """

                        _prefix = 'ipv4-pim-cfg'
                        _revision = '2017-10-15'

                        def __init__(self):
                            super(Pim.Vrfs.Vrf.Ipv4.SparseModeRpAddresses.SparseModeRpAddress, self).__init__()

                            self.yang_name = "sparse-mode-rp-address"
                            self.yang_parent_name = "sparse-mode-rp-addresses"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['rp_address']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('rp_address', (YLeaf(YType.str, 'rp-address'), ['str','str'])),
                                ('access_list_name', (YLeaf(YType.str, 'access-list-name'), ['str'])),
                                ('auto_rp_override', (YLeaf(YType.boolean, 'auto-rp-override'), ['bool'])),
                            ])
                            self.rp_address = None
                            self.access_list_name = None
                            self.auto_rp_override = None
                            self._segment_path = lambda: "sparse-mode-rp-address" + "[rp-address='" + str(self.rp_address) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Pim.Vrfs.Vrf.Ipv4.SparseModeRpAddresses.SparseModeRpAddress, ['rp_address', 'access_list_name', 'auto_rp_override'], name, value)


                class InheritableDefaults(Entity):
                    """
                    Inheritable defaults
                    
                    .. attribute:: convergence_timeout
                    
                    	Convergency timeout in seconds
                    	**type**\: int
                    
                    	**range:** 1800..2400
                    
                    	**units**\: second
                    
                    .. attribute:: hello_interval
                    
                    	Hello interval in seconds
                    	**type**\: int
                    
                    	**range:** 1..3600
                    
                    	**units**\: second
                    
                    .. attribute:: propagation_delay
                    
                    	Propagation delay in milli seconds
                    	**type**\: int
                    
                    	**range:** 100..32767
                    
                    	**units**\: millisecond
                    
                    .. attribute:: dr_priority
                    
                    	Hello DR priority, preference given to larger value
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: join_prune_mtu
                    
                    	Join\-Prune MTU in Bytes
                    	**type**\: int
                    
                    	**range:** 576..65535
                    
                    	**units**\: byte
                    
                    .. attribute:: jp_interval
                    
                    	Join\-Prune interval in seconds
                    	**type**\: int
                    
                    	**range:** 10..600
                    
                    	**units**\: second
                    
                    .. attribute:: override_interval
                    
                    	Override interval in milliseconds
                    	**type**\: int
                    
                    	**range:** 400..65535
                    
                    	**units**\: millisecond
                    
                    

                    """

                    _prefix = 'ipv4-pim-cfg'
                    _revision = '2017-10-15'

                    def __init__(self):
                        super(Pim.Vrfs.Vrf.Ipv4.InheritableDefaults, self).__init__()

                        self.yang_name = "inheritable-defaults"
                        self.yang_parent_name = "ipv4"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('convergence_timeout', (YLeaf(YType.uint32, 'convergence-timeout'), ['int'])),
                            ('hello_interval', (YLeaf(YType.uint32, 'hello-interval'), ['int'])),
                            ('propagation_delay', (YLeaf(YType.uint32, 'propagation-delay'), ['int'])),
                            ('dr_priority', (YLeaf(YType.uint32, 'dr-priority'), ['int'])),
                            ('join_prune_mtu', (YLeaf(YType.uint32, 'join-prune-mtu'), ['int'])),
                            ('jp_interval', (YLeaf(YType.uint32, 'jp-interval'), ['int'])),
                            ('override_interval', (YLeaf(YType.uint32, 'override-interval'), ['int'])),
                        ])
                        self.convergence_timeout = None
                        self.hello_interval = None
                        self.propagation_delay = None
                        self.dr_priority = None
                        self.join_prune_mtu = None
                        self.jp_interval = None
                        self.override_interval = None
                        self._segment_path = lambda: "inheritable-defaults"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Pim.Vrfs.Vrf.Ipv4.InheritableDefaults, ['convergence_timeout', 'hello_interval', 'propagation_delay', 'dr_priority', 'join_prune_mtu', 'jp_interval', 'override_interval'], name, value)


                class Rpf(Entity):
                    """
                    Configure RPF options
                    
                    .. attribute:: route_policy
                    
                    	Route policy to select RPF topology
                    	**type**\: str
                    
                    	**length:** 1..64
                    
                    

                    """

                    _prefix = 'ipv4-pim-cfg'
                    _revision = '2017-10-15'

                    def __init__(self):
                        super(Pim.Vrfs.Vrf.Ipv4.Rpf, self).__init__()

                        self.yang_name = "rpf"
                        self.yang_parent_name = "ipv4"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('route_policy', (YLeaf(YType.str, 'route-policy'), ['str'])),
                        ])
                        self.route_policy = None
                        self._segment_path = lambda: "rpf"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Pim.Vrfs.Vrf.Ipv4.Rpf, ['route_policy'], name, value)


                class Maximum(Entity):
                    """
                    Configure PIM State Limits
                    
                    .. attribute:: group_mappings_auto_rp
                    
                    	Override default maximum for number of group mappings from autorp mapping agent
                    	**type**\:  :py:class:`GroupMappingsAutoRp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.Vrfs.Vrf.Ipv4.Maximum.GroupMappingsAutoRp>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: bsr_group_mappings
                    
                    	Override default maximum and threshold for number of group mappings from BSR
                    	**type**\:  :py:class:`BsrGroupMappings <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.Vrfs.Vrf.Ipv4.Maximum.BsrGroupMappings>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: register_states
                    
                    	Override default maximum for number of sparse\-mode source registers
                    	**type**\:  :py:class:`RegisterStates <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.Vrfs.Vrf.Ipv4.Maximum.RegisterStates>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: route_interfaces
                    
                    	Override default maximum for number of route\-interfaces
                    	**type**\:  :py:class:`RouteInterfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.Vrfs.Vrf.Ipv4.Maximum.RouteInterfaces>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: bsr_candidate_rp_cache
                    
                    	Override default maximum and threshold for BSR C\-RP cache setting
                    	**type**\:  :py:class:`BsrCandidateRpCache <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.Vrfs.Vrf.Ipv4.Maximum.BsrCandidateRpCache>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: routes
                    
                    	Override default maximum for number of routes
                    	**type**\:  :py:class:`Routes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.Vrfs.Vrf.Ipv4.Maximum.Routes>`
                    
                    	**presence node**\: True
                    
                    

                    """

                    _prefix = 'ipv4-pim-cfg'
                    _revision = '2017-10-15'

                    def __init__(self):
                        super(Pim.Vrfs.Vrf.Ipv4.Maximum, self).__init__()

                        self.yang_name = "maximum"
                        self.yang_parent_name = "ipv4"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("group-mappings-auto-rp", ("group_mappings_auto_rp", Pim.Vrfs.Vrf.Ipv4.Maximum.GroupMappingsAutoRp)), ("bsr-group-mappings", ("bsr_group_mappings", Pim.Vrfs.Vrf.Ipv4.Maximum.BsrGroupMappings)), ("register-states", ("register_states", Pim.Vrfs.Vrf.Ipv4.Maximum.RegisterStates)), ("route-interfaces", ("route_interfaces", Pim.Vrfs.Vrf.Ipv4.Maximum.RouteInterfaces)), ("bsr-candidate-rp-cache", ("bsr_candidate_rp_cache", Pim.Vrfs.Vrf.Ipv4.Maximum.BsrCandidateRpCache)), ("routes", ("routes", Pim.Vrfs.Vrf.Ipv4.Maximum.Routes))])
                        self._leafs = OrderedDict()

                        self.group_mappings_auto_rp = None
                        self._children_name_map["group_mappings_auto_rp"] = "group-mappings-auto-rp"

                        self.bsr_group_mappings = None
                        self._children_name_map["bsr_group_mappings"] = "bsr-group-mappings"

                        self.register_states = None
                        self._children_name_map["register_states"] = "register-states"

                        self.route_interfaces = None
                        self._children_name_map["route_interfaces"] = "route-interfaces"

                        self.bsr_candidate_rp_cache = None
                        self._children_name_map["bsr_candidate_rp_cache"] = "bsr-candidate-rp-cache"

                        self.routes = None
                        self._children_name_map["routes"] = "routes"
                        self._segment_path = lambda: "maximum"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Pim.Vrfs.Vrf.Ipv4.Maximum, [], name, value)


                    class GroupMappingsAutoRp(Entity):
                        """
                        Override default maximum for number of group
                        mappings from autorp mapping agent
                        
                        .. attribute:: maximum_group_ranges_auto_rp
                        
                        	Maximum number of PIM group mappings from autorp
                        	**type**\: int
                        
                        	**range:** 1..10000
                        
                        	**mandatory**\: True
                        
                        .. attribute:: threshold_group_ranges_auto_rp
                        
                        	Warning threshold number of PIM group mappings from autorp
                        	**type**\: int
                        
                        	**range:** 1..10000
                        
                        	**default value**\: 450
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'ipv4-pim-cfg'
                        _revision = '2017-10-15'

                        def __init__(self):
                            super(Pim.Vrfs.Vrf.Ipv4.Maximum.GroupMappingsAutoRp, self).__init__()

                            self.yang_name = "group-mappings-auto-rp"
                            self.yang_parent_name = "maximum"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self.is_presence_container = True
                            self._leafs = OrderedDict([
                                ('maximum_group_ranges_auto_rp', (YLeaf(YType.uint32, 'maximum-group-ranges-auto-rp'), ['int'])),
                                ('threshold_group_ranges_auto_rp', (YLeaf(YType.uint32, 'threshold-group-ranges-auto-rp'), ['int'])),
                            ])
                            self.maximum_group_ranges_auto_rp = None
                            self.threshold_group_ranges_auto_rp = None
                            self._segment_path = lambda: "group-mappings-auto-rp"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Pim.Vrfs.Vrf.Ipv4.Maximum.GroupMappingsAutoRp, ['maximum_group_ranges_auto_rp', 'threshold_group_ranges_auto_rp'], name, value)


                    class BsrGroupMappings(Entity):
                        """
                        Override default maximum and threshold for
                        number of group mappings from BSR
                        
                        .. attribute:: bsr_maximum_group_ranges
                        
                        	Maximum number of PIM group mappings from BSR
                        	**type**\: int
                        
                        	**range:** 1..10000
                        
                        	**mandatory**\: True
                        
                        .. attribute:: warning_threshold
                        
                        	Set threshold to print warning
                        	**type**\: int
                        
                        	**range:** 1..10000
                        
                        	**default value**\: 500
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'ipv4-pim-cfg'
                        _revision = '2017-10-15'

                        def __init__(self):
                            super(Pim.Vrfs.Vrf.Ipv4.Maximum.BsrGroupMappings, self).__init__()

                            self.yang_name = "bsr-group-mappings"
                            self.yang_parent_name = "maximum"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self.is_presence_container = True
                            self._leafs = OrderedDict([
                                ('bsr_maximum_group_ranges', (YLeaf(YType.uint32, 'bsr-maximum-group-ranges'), ['int'])),
                                ('warning_threshold', (YLeaf(YType.uint32, 'warning-threshold'), ['int'])),
                            ])
                            self.bsr_maximum_group_ranges = None
                            self.warning_threshold = None
                            self._segment_path = lambda: "bsr-group-mappings"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Pim.Vrfs.Vrf.Ipv4.Maximum.BsrGroupMappings, ['bsr_maximum_group_ranges', 'warning_threshold'], name, value)


                    class RegisterStates(Entity):
                        """
                        Override default maximum for number of
                        sparse\-mode source registers
                        
                        .. attribute:: maximum_register_states
                        
                        	Maximum number of PIM Sparse\-Mode register states
                        	**type**\: int
                        
                        	**range:** 0..75000
                        
                        	**mandatory**\: True
                        
                        .. attribute:: warning_threshold
                        
                        	Set threshold to print warning
                        	**type**\: int
                        
                        	**range:** 0..75000
                        
                        	**default value**\: 20000
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'ipv4-pim-cfg'
                        _revision = '2017-10-15'

                        def __init__(self):
                            super(Pim.Vrfs.Vrf.Ipv4.Maximum.RegisterStates, self).__init__()

                            self.yang_name = "register-states"
                            self.yang_parent_name = "maximum"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self.is_presence_container = True
                            self._leafs = OrderedDict([
                                ('maximum_register_states', (YLeaf(YType.uint32, 'maximum-register-states'), ['int'])),
                                ('warning_threshold', (YLeaf(YType.uint32, 'warning-threshold'), ['int'])),
                            ])
                            self.maximum_register_states = None
                            self.warning_threshold = None
                            self._segment_path = lambda: "register-states"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Pim.Vrfs.Vrf.Ipv4.Maximum.RegisterStates, ['maximum_register_states', 'warning_threshold'], name, value)


                    class RouteInterfaces(Entity):
                        """
                        Override default maximum for number of
                        route\-interfaces
                        
                        .. attribute:: maximum_route_interfaces
                        
                        	Maximum number of PIM route\-interfaces
                        	**type**\: int
                        
                        	**range:** 1..1100000
                        
                        	**mandatory**\: True
                        
                        .. attribute:: warning_threshold
                        
                        	Set threshold to print warning
                        	**type**\: int
                        
                        	**range:** 1..1100000
                        
                        	**default value**\: 300000
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'ipv4-pim-cfg'
                        _revision = '2017-10-15'

                        def __init__(self):
                            super(Pim.Vrfs.Vrf.Ipv4.Maximum.RouteInterfaces, self).__init__()

                            self.yang_name = "route-interfaces"
                            self.yang_parent_name = "maximum"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self.is_presence_container = True
                            self._leafs = OrderedDict([
                                ('maximum_route_interfaces', (YLeaf(YType.uint32, 'maximum-route-interfaces'), ['int'])),
                                ('warning_threshold', (YLeaf(YType.uint32, 'warning-threshold'), ['int'])),
                            ])
                            self.maximum_route_interfaces = None
                            self.warning_threshold = None
                            self._segment_path = lambda: "route-interfaces"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Pim.Vrfs.Vrf.Ipv4.Maximum.RouteInterfaces, ['maximum_route_interfaces', 'warning_threshold'], name, value)


                    class BsrCandidateRpCache(Entity):
                        """
                        Override default maximum and threshold for BSR
                        C\-RP cache setting
                        
                        .. attribute:: bsr_maximum_candidate_rp_cache
                        
                        	Maximum number of BSR C\-RP cache setting
                        	**type**\: int
                        
                        	**range:** 1..10000
                        
                        	**mandatory**\: True
                        
                        .. attribute:: warning_threshold
                        
                        	Set threshold to print warning
                        	**type**\: int
                        
                        	**range:** 1..10000
                        
                        	**default value**\: 100
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'ipv4-pim-cfg'
                        _revision = '2017-10-15'

                        def __init__(self):
                            super(Pim.Vrfs.Vrf.Ipv4.Maximum.BsrCandidateRpCache, self).__init__()

                            self.yang_name = "bsr-candidate-rp-cache"
                            self.yang_parent_name = "maximum"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self.is_presence_container = True
                            self._leafs = OrderedDict([
                                ('bsr_maximum_candidate_rp_cache', (YLeaf(YType.uint32, 'bsr-maximum-candidate-rp-cache'), ['int'])),
                                ('warning_threshold', (YLeaf(YType.uint32, 'warning-threshold'), ['int'])),
                            ])
                            self.bsr_maximum_candidate_rp_cache = None
                            self.warning_threshold = None
                            self._segment_path = lambda: "bsr-candidate-rp-cache"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Pim.Vrfs.Vrf.Ipv4.Maximum.BsrCandidateRpCache, ['bsr_maximum_candidate_rp_cache', 'warning_threshold'], name, value)


                    class Routes(Entity):
                        """
                        Override default maximum for number of routes
                        
                        .. attribute:: maximum_routes
                        
                        	Maximum number of PIM routes
                        	**type**\: int
                        
                        	**range:** 1..200000
                        
                        	**mandatory**\: True
                        
                        .. attribute:: warning_threshold
                        
                        	Set threshold to print warning
                        	**type**\: int
                        
                        	**range:** 1..200000
                        
                        	**default value**\: 100000
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'ipv4-pim-cfg'
                        _revision = '2017-10-15'

                        def __init__(self):
                            super(Pim.Vrfs.Vrf.Ipv4.Maximum.Routes, self).__init__()

                            self.yang_name = "routes"
                            self.yang_parent_name = "maximum"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self.is_presence_container = True
                            self._leafs = OrderedDict([
                                ('maximum_routes', (YLeaf(YType.uint32, 'maximum-routes'), ['int'])),
                                ('warning_threshold', (YLeaf(YType.uint32, 'warning-threshold'), ['int'])),
                            ])
                            self.maximum_routes = None
                            self.warning_threshold = None
                            self._segment_path = lambda: "routes"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Pim.Vrfs.Vrf.Ipv4.Maximum.Routes, ['maximum_routes', 'warning_threshold'], name, value)


                class SgExpiryTimer(Entity):
                    """
                    Configure expiry timer for S,G routes
                    
                    .. attribute:: interval
                    
                    	(S,G) expiry time in seconds
                    	**type**\: int
                    
                    	**range:** 40..57600
                    
                    	**units**\: second
                    
                    .. attribute:: access_list_name
                    
                    	Access\-list of applicable S,G routes
                    	**type**\: str
                    
                    	**length:** 1..64
                    
                    

                    """

                    _prefix = 'ipv4-pim-cfg'
                    _revision = '2017-10-15'

                    def __init__(self):
                        super(Pim.Vrfs.Vrf.Ipv4.SgExpiryTimer, self).__init__()

                        self.yang_name = "sg-expiry-timer"
                        self.yang_parent_name = "ipv4"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('interval', (YLeaf(YType.uint32, 'interval'), ['int'])),
                            ('access_list_name', (YLeaf(YType.str, 'access-list-name'), ['str'])),
                        ])
                        self.interval = None
                        self.access_list_name = None
                        self._segment_path = lambda: "sg-expiry-timer"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Pim.Vrfs.Vrf.Ipv4.SgExpiryTimer, ['interval', 'access_list_name'], name, value)


                class RpfVectorEnable(Entity):
                    """
                    Enable PIM RPF Vector Proxy's
                    
                    .. attribute:: enable
                    
                    	RPF Vector is turned on if configured
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    	**mandatory**\: True
                    
                    .. attribute:: allow_ebgp
                    
                    	Allow RPF Vector origination over eBGP sessions
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: disable_ibgp
                    
                    	Disable RPF Vector origination over iBGP sessions
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: use_standard_encoding
                    
                    	Use RPF Vector RFC compliant encoding
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'ipv4-pim-cfg'
                    _revision = '2017-10-15'

                    def __init__(self):
                        super(Pim.Vrfs.Vrf.Ipv4.RpfVectorEnable, self).__init__()

                        self.yang_name = "rpf-vector-enable"
                        self.yang_parent_name = "ipv4"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self.is_presence_container = True
                        self._leafs = OrderedDict([
                            ('enable', (YLeaf(YType.empty, 'enable'), ['Empty'])),
                            ('allow_ebgp', (YLeaf(YType.empty, 'allow-ebgp'), ['Empty'])),
                            ('disable_ibgp', (YLeaf(YType.empty, 'disable-ibgp'), ['Empty'])),
                            ('use_standard_encoding', (YLeaf(YType.empty, 'use-standard-encoding'), ['Empty'])),
                        ])
                        self.enable = None
                        self.allow_ebgp = None
                        self.disable_ibgp = None
                        self.use_standard_encoding = None
                        self._segment_path = lambda: "rpf-vector-enable"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Pim.Vrfs.Vrf.Ipv4.RpfVectorEnable, ['enable', 'allow_ebgp', 'disable_ibgp', 'use_standard_encoding'], name, value)


                class Ssm(Entity):
                    """
                    Configure IP Multicast SSM
                    
                    .. attribute:: disable
                    
                    	TRUE if SSM is disabled on this router
                    	**type**\: bool
                    
                    	**default value**\: false
                    
                    .. attribute:: range
                    
                    	Access list of groups enabled with SSM
                    	**type**\: str
                    
                    	**length:** 1..64
                    
                    

                    """

                    _prefix = 'ipv4-pim-cfg'
                    _revision = '2017-10-15'

                    def __init__(self):
                        super(Pim.Vrfs.Vrf.Ipv4.Ssm, self).__init__()

                        self.yang_name = "ssm"
                        self.yang_parent_name = "ipv4"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('disable', (YLeaf(YType.boolean, 'disable'), ['bool'])),
                            ('range', (YLeaf(YType.str, 'range'), ['str'])),
                        ])
                        self.disable = None
                        self.range = None
                        self._segment_path = lambda: "ssm"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Pim.Vrfs.Vrf.Ipv4.Ssm, ['disable', 'range'], name, value)


                class Injects(Entity):
                    """
                    Inject Explicit PIM RPF Vector Proxy's
                    
                    .. attribute:: inject
                    
                    	Inject Explicit PIM RPF Vector Proxy's
                    	**type**\: list of  		 :py:class:`Inject <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.Vrfs.Vrf.Ipv4.Injects.Inject>`
                    
                    

                    """

                    _prefix = 'ipv4-pim-cfg'
                    _revision = '2017-10-15'

                    def __init__(self):
                        super(Pim.Vrfs.Vrf.Ipv4.Injects, self).__init__()

                        self.yang_name = "injects"
                        self.yang_parent_name = "ipv4"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("inject", ("inject", Pim.Vrfs.Vrf.Ipv4.Injects.Inject))])
                        self._leafs = OrderedDict()

                        self.inject = YList(self)
                        self._segment_path = lambda: "injects"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Pim.Vrfs.Vrf.Ipv4.Injects, [], name, value)


                    class Inject(Entity):
                        """
                        Inject Explicit PIM RPF Vector Proxy's
                        
                        .. attribute:: source_address  (key)
                        
                        	Source Address
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: prefix_length  (key)
                        
                        	Masklen
                        	**type**\: int
                        
                        	**range:** 0..32
                        
                        .. attribute:: rpf_proxy_address
                        
                        	RPF Proxy Address
                        	**type**\: list of str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        

                        """

                        _prefix = 'ipv4-pim-cfg'
                        _revision = '2017-10-15'

                        def __init__(self):
                            super(Pim.Vrfs.Vrf.Ipv4.Injects.Inject, self).__init__()

                            self.yang_name = "inject"
                            self.yang_parent_name = "injects"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['source_address','prefix_length']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('source_address', (YLeaf(YType.str, 'source-address'), ['str'])),
                                ('prefix_length', (YLeaf(YType.uint8, 'prefix-length'), ['int'])),
                                ('rpf_proxy_address', (YLeafList(YType.str, 'rpf-proxy-address'), ['str'])),
                            ])
                            self.source_address = None
                            self.prefix_length = None
                            self.rpf_proxy_address = []
                            self._segment_path = lambda: "inject" + "[source-address='" + str(self.source_address) + "']" + "[prefix-length='" + str(self.prefix_length) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Pim.Vrfs.Vrf.Ipv4.Injects.Inject, ['source_address', 'prefix_length', 'rpf_proxy_address'], name, value)


                class BidirRpAddresses(Entity):
                    """
                    Configure Bidirectional PIM Rendezvous Point
                    
                    .. attribute:: bidir_rp_address
                    
                    	Address of the Rendezvous Point
                    	**type**\: list of  		 :py:class:`BidirRpAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.Vrfs.Vrf.Ipv4.BidirRpAddresses.BidirRpAddress>`
                    
                    

                    """

                    _prefix = 'ipv4-pim-cfg'
                    _revision = '2017-10-15'

                    def __init__(self):
                        super(Pim.Vrfs.Vrf.Ipv4.BidirRpAddresses, self).__init__()

                        self.yang_name = "bidir-rp-addresses"
                        self.yang_parent_name = "ipv4"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("bidir-rp-address", ("bidir_rp_address", Pim.Vrfs.Vrf.Ipv4.BidirRpAddresses.BidirRpAddress))])
                        self._leafs = OrderedDict()

                        self.bidir_rp_address = YList(self)
                        self._segment_path = lambda: "bidir-rp-addresses"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Pim.Vrfs.Vrf.Ipv4.BidirRpAddresses, [], name, value)


                    class BidirRpAddress(Entity):
                        """
                        Address of the Rendezvous Point
                        
                        .. attribute:: rp_address  (key)
                        
                        	RP address of Rendezvous Point
                        	**type**\: union of the below types:
                        
                        		**type**\: str
                        
                        			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        		**type**\: str
                        
                        			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: access_list_name
                        
                        	Access list of groups that should map to a given RP
                        	**type**\: str
                        
                        	**length:** 1..64
                        
                        .. attribute:: auto_rp_override
                        
                        	TRUE Indicates if static RP config overrides AutoRP and BSR
                        	**type**\: bool
                        
                        

                        """

                        _prefix = 'ipv4-pim-cfg'
                        _revision = '2017-10-15'

                        def __init__(self):
                            super(Pim.Vrfs.Vrf.Ipv4.BidirRpAddresses.BidirRpAddress, self).__init__()

                            self.yang_name = "bidir-rp-address"
                            self.yang_parent_name = "bidir-rp-addresses"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['rp_address']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('rp_address', (YLeaf(YType.str, 'rp-address'), ['str','str'])),
                                ('access_list_name', (YLeaf(YType.str, 'access-list-name'), ['str'])),
                                ('auto_rp_override', (YLeaf(YType.boolean, 'auto-rp-override'), ['bool'])),
                            ])
                            self.rp_address = None
                            self.access_list_name = None
                            self.auto_rp_override = None
                            self._segment_path = lambda: "bidir-rp-address" + "[rp-address='" + str(self.rp_address) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Pim.Vrfs.Vrf.Ipv4.BidirRpAddresses.BidirRpAddress, ['rp_address', 'access_list_name', 'auto_rp_override'], name, value)


                class Bsr(Entity):
                    """
                    PIM BSR configuration
                    
                    .. attribute:: candidate_bsr
                    
                    	PIM Candidate BSR configuration
                    	**type**\:  :py:class:`CandidateBsr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.Vrfs.Vrf.Ipv4.Bsr.CandidateBsr>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: candidate_rps
                    
                    	PIM RP configuration
                    	**type**\:  :py:class:`CandidateRps <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.Vrfs.Vrf.Ipv4.Bsr.CandidateRps>`
                    
                    

                    """

                    _prefix = 'ipv4-pim-cfg'
                    _revision = '2017-10-15'

                    def __init__(self):
                        super(Pim.Vrfs.Vrf.Ipv4.Bsr, self).__init__()

                        self.yang_name = "bsr"
                        self.yang_parent_name = "ipv4"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("candidate-bsr", ("candidate_bsr", Pim.Vrfs.Vrf.Ipv4.Bsr.CandidateBsr)), ("candidate-rps", ("candidate_rps", Pim.Vrfs.Vrf.Ipv4.Bsr.CandidateRps))])
                        self._leafs = OrderedDict()

                        self.candidate_bsr = None
                        self._children_name_map["candidate_bsr"] = "candidate-bsr"

                        self.candidate_rps = Pim.Vrfs.Vrf.Ipv4.Bsr.CandidateRps()
                        self.candidate_rps.parent = self
                        self._children_name_map["candidate_rps"] = "candidate-rps"
                        self._segment_path = lambda: "bsr"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Pim.Vrfs.Vrf.Ipv4.Bsr, [], name, value)


                    class CandidateBsr(Entity):
                        """
                        PIM Candidate BSR configuration
                        
                        .. attribute:: address
                        
                        	BSR Address configured
                        	**type**\: union of the below types:
                        
                        		**type**\: str
                        
                        			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        		**type**\: str
                        
                        			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        	**mandatory**\: True
                        
                        .. attribute:: prefix_length
                        
                        	Hash Mask Length for this candidate BSR
                        	**type**\: int
                        
                        	**range:** 0..32
                        
                        	**default value**\: 30
                        
                        .. attribute:: priority
                        
                        	Priority of the Candidate BSR
                        	**type**\: int
                        
                        	**range:** 1..255
                        
                        	**default value**\: 1
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'ipv4-pim-cfg'
                        _revision = '2017-10-15'

                        def __init__(self):
                            super(Pim.Vrfs.Vrf.Ipv4.Bsr.CandidateBsr, self).__init__()

                            self.yang_name = "candidate-bsr"
                            self.yang_parent_name = "bsr"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self.is_presence_container = True
                            self._leafs = OrderedDict([
                                ('address', (YLeaf(YType.str, 'address'), ['str','str'])),
                                ('prefix_length', (YLeaf(YType.uint8, 'prefix-length'), ['int'])),
                                ('priority', (YLeaf(YType.uint32, 'priority'), ['int'])),
                            ])
                            self.address = None
                            self.prefix_length = None
                            self.priority = None
                            self._segment_path = lambda: "candidate-bsr"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Pim.Vrfs.Vrf.Ipv4.Bsr.CandidateBsr, ['address', 'prefix_length', 'priority'], name, value)


                    class CandidateRps(Entity):
                        """
                        PIM RP configuration
                        
                        .. attribute:: candidate_rp
                        
                        	Address of PIM SM BSR Candidate\-RP
                        	**type**\: list of  		 :py:class:`CandidateRp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.Vrfs.Vrf.Ipv4.Bsr.CandidateRps.CandidateRp>`
                        
                        

                        """

                        _prefix = 'ipv4-pim-cfg'
                        _revision = '2017-10-15'

                        def __init__(self):
                            super(Pim.Vrfs.Vrf.Ipv4.Bsr.CandidateRps, self).__init__()

                            self.yang_name = "candidate-rps"
                            self.yang_parent_name = "bsr"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("candidate-rp", ("candidate_rp", Pim.Vrfs.Vrf.Ipv4.Bsr.CandidateRps.CandidateRp))])
                            self._leafs = OrderedDict()

                            self.candidate_rp = YList(self)
                            self._segment_path = lambda: "candidate-rps"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Pim.Vrfs.Vrf.Ipv4.Bsr.CandidateRps, [], name, value)


                        class CandidateRp(Entity):
                            """
                            Address of PIM SM BSR Candidate\-RP
                            
                            .. attribute:: address  (key)
                            
                            	Address of Candidate\-RP
                            	**type**\: union of the below types:
                            
                            		**type**\: str
                            
                            			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            		**type**\: str
                            
                            			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: mode  (key)
                            
                            	SM or Bidir
                            	**type**\:  :py:class:`PimProtocolMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.PimProtocolMode>`
                            
                            .. attribute:: group_list
                            
                            	Access\-list specifying the group range for the Candidate\-RP
                            	**type**\: str
                            
                            	**length:** 1..64
                            
                            .. attribute:: priority
                            
                            	Priority of the CRP
                            	**type**\: int
                            
                            	**range:** 1..255
                            
                            	**default value**\: 192
                            
                            .. attribute:: interval
                            
                            	Advertisement interval
                            	**type**\: int
                            
                            	**range:** 30..600
                            
                            	**default value**\: 60
                            
                            

                            """

                            _prefix = 'ipv4-pim-cfg'
                            _revision = '2017-10-15'

                            def __init__(self):
                                super(Pim.Vrfs.Vrf.Ipv4.Bsr.CandidateRps.CandidateRp, self).__init__()

                                self.yang_name = "candidate-rp"
                                self.yang_parent_name = "candidate-rps"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['address','mode']
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('address', (YLeaf(YType.str, 'address'), ['str','str'])),
                                    ('mode', (YLeaf(YType.enumeration, 'mode'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg', 'PimProtocolMode', '')])),
                                    ('group_list', (YLeaf(YType.str, 'group-list'), ['str'])),
                                    ('priority', (YLeaf(YType.uint32, 'priority'), ['int'])),
                                    ('interval', (YLeaf(YType.uint32, 'interval'), ['int'])),
                                ])
                                self.address = None
                                self.mode = None
                                self.group_list = None
                                self.priority = None
                                self.interval = None
                                self._segment_path = lambda: "candidate-rp" + "[address='" + str(self.address) + "']" + "[mode='" + str(self.mode) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Pim.Vrfs.Vrf.Ipv4.Bsr.CandidateRps.CandidateRp, ['address', 'mode', 'group_list', 'priority', 'interval'], name, value)


                class Mofrr(Entity):
                    """
                    Multicast Only Fast Re\-Route
                    
                    .. attribute:: clone_joins
                    
                    	Clone multicast joins
                    	**type**\:  :py:class:`CloneJoins <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.Vrfs.Vrf.Ipv4.Mofrr.CloneJoins>`
                    
                    .. attribute:: clone_sources
                    
                    	Clone multicast traffic
                    	**type**\:  :py:class:`CloneSources <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.Vrfs.Vrf.Ipv4.Mofrr.CloneSources>`
                    
                    .. attribute:: rib
                    
                    	Access\-list specifying SG that should do RIB MOFRR
                    	**type**\: str
                    
                    	**length:** 1..64
                    
                    .. attribute:: non_revertive
                    
                    	Non\-revertive Multicast Only Fast Re\-Route
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: enable
                    
                    	Enable Multicast Only FRR
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: flow
                    
                    	Access\-list specifying SG that should do FLOW MOFRR
                    	**type**\: str
                    
                    	**length:** 1..64
                    
                    

                    """

                    _prefix = 'ipv4-pim-cfg'
                    _revision = '2017-10-15'

                    def __init__(self):
                        super(Pim.Vrfs.Vrf.Ipv4.Mofrr, self).__init__()

                        self.yang_name = "mofrr"
                        self.yang_parent_name = "ipv4"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("clone-joins", ("clone_joins", Pim.Vrfs.Vrf.Ipv4.Mofrr.CloneJoins)), ("clone-sources", ("clone_sources", Pim.Vrfs.Vrf.Ipv4.Mofrr.CloneSources))])
                        self._leafs = OrderedDict([
                            ('rib', (YLeaf(YType.str, 'rib'), ['str'])),
                            ('non_revertive', (YLeaf(YType.empty, 'non-revertive'), ['Empty'])),
                            ('enable', (YLeaf(YType.empty, 'enable'), ['Empty'])),
                            ('flow', (YLeaf(YType.str, 'flow'), ['str'])),
                        ])
                        self.rib = None
                        self.non_revertive = None
                        self.enable = None
                        self.flow = None

                        self.clone_joins = Pim.Vrfs.Vrf.Ipv4.Mofrr.CloneJoins()
                        self.clone_joins.parent = self
                        self._children_name_map["clone_joins"] = "clone-joins"

                        self.clone_sources = Pim.Vrfs.Vrf.Ipv4.Mofrr.CloneSources()
                        self.clone_sources.parent = self
                        self._children_name_map["clone_sources"] = "clone-sources"
                        self._segment_path = lambda: "mofrr"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Pim.Vrfs.Vrf.Ipv4.Mofrr, ['rib', 'non_revertive', 'enable', 'flow'], name, value)


                    class CloneJoins(Entity):
                        """
                        Clone multicast joins
                        
                        .. attribute:: clone_join
                        
                        	Clone S,G joins as S1,G joins and S2,G joins
                        	**type**\: list of  		 :py:class:`CloneJoin <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.Vrfs.Vrf.Ipv4.Mofrr.CloneJoins.CloneJoin>`
                        
                        

                        """

                        _prefix = 'ipv4-pim-cfg'
                        _revision = '2017-10-15'

                        def __init__(self):
                            super(Pim.Vrfs.Vrf.Ipv4.Mofrr.CloneJoins, self).__init__()

                            self.yang_name = "clone-joins"
                            self.yang_parent_name = "mofrr"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("clone-join", ("clone_join", Pim.Vrfs.Vrf.Ipv4.Mofrr.CloneJoins.CloneJoin))])
                            self._leafs = OrderedDict()

                            self.clone_join = YList(self)
                            self._segment_path = lambda: "clone-joins"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Pim.Vrfs.Vrf.Ipv4.Mofrr.CloneJoins, [], name, value)


                        class CloneJoin(Entity):
                            """
                            Clone S,G joins as S1,G joins and S2,G joins
                            
                            .. attribute:: source  (key)
                            
                            	Original source address (S)
                            	**type**\: str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: primary  (key)
                            
                            	Primary cloned address (S1)
                            	**type**\: str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: backup  (key)
                            
                            	Backup cloned address (S2)
                            	**type**\: str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: prefix_length  (key)
                            
                            	Mask length
                            	**type**\: int
                            
                            	**range:** 0..32
                            
                            

                            """

                            _prefix = 'ipv4-pim-cfg'
                            _revision = '2017-10-15'

                            def __init__(self):
                                super(Pim.Vrfs.Vrf.Ipv4.Mofrr.CloneJoins.CloneJoin, self).__init__()

                                self.yang_name = "clone-join"
                                self.yang_parent_name = "clone-joins"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['source','primary','backup','prefix_length']
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('source', (YLeaf(YType.str, 'source'), ['str'])),
                                    ('primary', (YLeaf(YType.str, 'primary'), ['str'])),
                                    ('backup', (YLeaf(YType.str, 'backup'), ['str'])),
                                    ('prefix_length', (YLeaf(YType.uint8, 'prefix-length'), ['int'])),
                                ])
                                self.source = None
                                self.primary = None
                                self.backup = None
                                self.prefix_length = None
                                self._segment_path = lambda: "clone-join" + "[source='" + str(self.source) + "']" + "[primary='" + str(self.primary) + "']" + "[backup='" + str(self.backup) + "']" + "[prefix-length='" + str(self.prefix_length) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Pim.Vrfs.Vrf.Ipv4.Mofrr.CloneJoins.CloneJoin, ['source', 'primary', 'backup', 'prefix_length'], name, value)


                    class CloneSources(Entity):
                        """
                        Clone multicast traffic
                        
                        .. attribute:: clone_source
                        
                        	Clone S,G traffic as S1,G traffic and S2,G traffic
                        	**type**\: list of  		 :py:class:`CloneSource <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.Vrfs.Vrf.Ipv4.Mofrr.CloneSources.CloneSource>`
                        
                        

                        """

                        _prefix = 'ipv4-pim-cfg'
                        _revision = '2017-10-15'

                        def __init__(self):
                            super(Pim.Vrfs.Vrf.Ipv4.Mofrr.CloneSources, self).__init__()

                            self.yang_name = "clone-sources"
                            self.yang_parent_name = "mofrr"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("clone-source", ("clone_source", Pim.Vrfs.Vrf.Ipv4.Mofrr.CloneSources.CloneSource))])
                            self._leafs = OrderedDict()

                            self.clone_source = YList(self)
                            self._segment_path = lambda: "clone-sources"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Pim.Vrfs.Vrf.Ipv4.Mofrr.CloneSources, [], name, value)


                        class CloneSource(Entity):
                            """
                            Clone S,G traffic as S1,G traffic and S2,G
                            traffic
                            
                            .. attribute:: source  (key)
                            
                            	Original source address (S)
                            	**type**\: str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: primary  (key)
                            
                            	Primary cloned address (S1)
                            	**type**\: str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: backup  (key)
                            
                            	Backup cloned address (S2)
                            	**type**\: str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: prefix_length  (key)
                            
                            	Mask length
                            	**type**\: int
                            
                            	**range:** 0..32
                            
                            

                            """

                            _prefix = 'ipv4-pim-cfg'
                            _revision = '2017-10-15'

                            def __init__(self):
                                super(Pim.Vrfs.Vrf.Ipv4.Mofrr.CloneSources.CloneSource, self).__init__()

                                self.yang_name = "clone-source"
                                self.yang_parent_name = "clone-sources"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['source','primary','backup','prefix_length']
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('source', (YLeaf(YType.str, 'source'), ['str'])),
                                    ('primary', (YLeaf(YType.str, 'primary'), ['str'])),
                                    ('backup', (YLeaf(YType.str, 'backup'), ['str'])),
                                    ('prefix_length', (YLeaf(YType.uint8, 'prefix-length'), ['int'])),
                                ])
                                self.source = None
                                self.primary = None
                                self.backup = None
                                self.prefix_length = None
                                self._segment_path = lambda: "clone-source" + "[source='" + str(self.source) + "']" + "[primary='" + str(self.primary) + "']" + "[backup='" + str(self.backup) + "']" + "[prefix-length='" + str(self.prefix_length) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Pim.Vrfs.Vrf.Ipv4.Mofrr.CloneSources.CloneSource, ['source', 'primary', 'backup', 'prefix_length'], name, value)


                class Paths(Entity):
                    """
                    Inject PIM RPF Vector Proxy's
                    
                    .. attribute:: path
                    
                    	Inject PIM RPF Vector Proxy's
                    	**type**\: list of  		 :py:class:`Path <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.Vrfs.Vrf.Ipv4.Paths.Path>`
                    
                    

                    """

                    _prefix = 'ipv4-pim-cfg'
                    _revision = '2017-10-15'

                    def __init__(self):
                        super(Pim.Vrfs.Vrf.Ipv4.Paths, self).__init__()

                        self.yang_name = "paths"
                        self.yang_parent_name = "ipv4"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("path", ("path", Pim.Vrfs.Vrf.Ipv4.Paths.Path))])
                        self._leafs = OrderedDict()

                        self.path = YList(self)
                        self._segment_path = lambda: "paths"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Pim.Vrfs.Vrf.Ipv4.Paths, [], name, value)


                    class Path(Entity):
                        """
                        Inject PIM RPF Vector Proxy's
                        
                        .. attribute:: source_address  (key)
                        
                        	Source Address
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: prefix_length  (key)
                        
                        	Masklen
                        	**type**\: int
                        
                        	**range:** 0..32
                        
                        .. attribute:: rpf_proxy_address
                        
                        	RPF Proxy Address
                        	**type**\: list of str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        

                        """

                        _prefix = 'ipv4-pim-cfg'
                        _revision = '2017-10-15'

                        def __init__(self):
                            super(Pim.Vrfs.Vrf.Ipv4.Paths.Path, self).__init__()

                            self.yang_name = "path"
                            self.yang_parent_name = "paths"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['source_address','prefix_length']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('source_address', (YLeaf(YType.str, 'source-address'), ['str'])),
                                ('prefix_length', (YLeaf(YType.uint8, 'prefix-length'), ['int'])),
                                ('rpf_proxy_address', (YLeafList(YType.str, 'rpf-proxy-address'), ['str'])),
                            ])
                            self.source_address = None
                            self.prefix_length = None
                            self.rpf_proxy_address = []
                            self._segment_path = lambda: "path" + "[source-address='" + str(self.source_address) + "']" + "[prefix-length='" + str(self.prefix_length) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Pim.Vrfs.Vrf.Ipv4.Paths.Path, ['source_address', 'prefix_length', 'rpf_proxy_address'], name, value)


                class AllowRp(Entity):
                    """
                    Enable allow\-rp filtering for SM joins
                    
                    .. attribute:: rp_list_name
                    
                    	Access\-list specifiying applicable RPs
                    	**type**\: str
                    
                    	**length:** 1..64
                    
                    .. attribute:: group_list_name
                    
                    	Access\-list specifiying applicable groups
                    	**type**\: str
                    
                    	**length:** 1..64
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'ipv4-pim-cfg'
                    _revision = '2017-10-15'

                    def __init__(self):
                        super(Pim.Vrfs.Vrf.Ipv4.AllowRp, self).__init__()

                        self.yang_name = "allow-rp"
                        self.yang_parent_name = "ipv4"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self.is_presence_container = True
                        self._leafs = OrderedDict([
                            ('rp_list_name', (YLeaf(YType.str, 'rp-list-name'), ['str'])),
                            ('group_list_name', (YLeaf(YType.str, 'group-list-name'), ['str'])),
                        ])
                        self.rp_list_name = None
                        self.group_list_name = None
                        self._segment_path = lambda: "allow-rp"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Pim.Vrfs.Vrf.Ipv4.AllowRp, ['rp_list_name', 'group_list_name'], name, value)


                class Convergence(Entity):
                    """
                    Configure convergence parameters
                    
                    .. attribute:: rpf_conflict_join_delay
                    
                    	Dampen first join if RPF path is through one of the downstream neighbor
                    	**type**\: int
                    
                    	**range:** 0..15
                    
                    	**units**\: second
                    
                    .. attribute:: link_down_prune_delay
                    
                    	Delay prunes if route join state transitions to not\-joined on link down
                    	**type**\: int
                    
                    	**range:** 0..60
                    
                    	**units**\: second
                    
                    

                    """

                    _prefix = 'ipv4-pim-cfg'
                    _revision = '2017-10-15'

                    def __init__(self):
                        super(Pim.Vrfs.Vrf.Ipv4.Convergence, self).__init__()

                        self.yang_name = "convergence"
                        self.yang_parent_name = "ipv4"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('rpf_conflict_join_delay', (YLeaf(YType.uint32, 'rpf-conflict-join-delay'), ['int'])),
                            ('link_down_prune_delay', (YLeaf(YType.uint32, 'link-down-prune-delay'), ['int'])),
                        ])
                        self.rpf_conflict_join_delay = None
                        self.link_down_prune_delay = None
                        self._segment_path = lambda: "convergence"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Pim.Vrfs.Vrf.Ipv4.Convergence, ['rpf_conflict_join_delay', 'link_down_prune_delay'], name, value)


                class Interfaces(Entity):
                    """
                    Interface\-level Configuration
                    
                    .. attribute:: interface
                    
                    	The name of the interface
                    	**type**\: list of  		 :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.Vrfs.Vrf.Ipv4.Interfaces.Interface>`
                    
                    

                    """

                    _prefix = 'ipv4-pim-cfg'
                    _revision = '2017-10-15'

                    def __init__(self):
                        super(Pim.Vrfs.Vrf.Ipv4.Interfaces, self).__init__()

                        self.yang_name = "interfaces"
                        self.yang_parent_name = "ipv4"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("interface", ("interface", Pim.Vrfs.Vrf.Ipv4.Interfaces.Interface))])
                        self._leafs = OrderedDict()

                        self.interface = YList(self)
                        self._segment_path = lambda: "interfaces"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Pim.Vrfs.Vrf.Ipv4.Interfaces, [], name, value)


                    class Interface(Entity):
                        """
                        The name of the interface
                        
                        .. attribute:: interface_name  (key)
                        
                        	The name of interface
                        	**type**\: str
                        
                        	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                        
                        .. attribute:: enable
                        
                        	Enter PIM Interface processing
                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: neighbor_filter
                        
                        	Access\-list of neighbors to be filtered
                        	**type**\: str
                        
                        	**length:** 1..64
                        
                        .. attribute:: hello_interval
                        
                        	Hello interval in seconds
                        	**type**\: int
                        
                        	**range:** 1..3600
                        
                        	**units**\: second
                        
                        .. attribute:: bsr_border
                        
                        	BSR Border configuration for Interface
                        	**type**\: bool
                        
                        .. attribute:: maximum_routes
                        
                        	Maximum number of allowed routes for this interface
                        	**type**\:  :py:class:`MaximumRoutes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.Vrfs.Vrf.Ipv4.Interfaces.Interface.MaximumRoutes>`
                        
                        	**presence node**\: True
                        
                        .. attribute:: propagation_delay
                        
                        	Propagation delay in milli seconds
                        	**type**\: int
                        
                        	**range:** 100..32767
                        
                        	**units**\: millisecond
                        
                        .. attribute:: bfd
                        
                        	BFD configuration
                        	**type**\:  :py:class:`Bfd <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.Vrfs.Vrf.Ipv4.Interfaces.Interface.Bfd>`
                        
                        .. attribute:: dr_priority
                        
                        	Hello DR priority, preference given to larger value
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: join_prune_mtu
                        
                        	Join\-Prune MTU in Bytes
                        	**type**\: int
                        
                        	**range:** 576..65535
                        
                        	**units**\: byte
                        
                        .. attribute:: interface_enable
                        
                        	Enable PIM processing on the interface
                        	**type**\: bool
                        
                        .. attribute:: jp_interval
                        
                        	Join\-Prune interval in seconds
                        	**type**\: int
                        
                        	**range:** 10..600
                        
                        	**units**\: second
                        
                        .. attribute:: override_interval
                        
                        	Override interval in milliseconds
                        	**type**\: int
                        
                        	**range:** 400..65535
                        
                        	**units**\: millisecond
                        
                        

                        """

                        _prefix = 'ipv4-pim-cfg'
                        _revision = '2017-10-15'

                        def __init__(self):
                            super(Pim.Vrfs.Vrf.Ipv4.Interfaces.Interface, self).__init__()

                            self.yang_name = "interface"
                            self.yang_parent_name = "interfaces"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['interface_name']
                            self._child_classes = OrderedDict([("maximum-routes", ("maximum_routes", Pim.Vrfs.Vrf.Ipv4.Interfaces.Interface.MaximumRoutes)), ("bfd", ("bfd", Pim.Vrfs.Vrf.Ipv4.Interfaces.Interface.Bfd))])
                            self._leafs = OrderedDict([
                                ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                                ('enable', (YLeaf(YType.empty, 'enable'), ['Empty'])),
                                ('neighbor_filter', (YLeaf(YType.str, 'neighbor-filter'), ['str'])),
                                ('hello_interval', (YLeaf(YType.uint32, 'hello-interval'), ['int'])),
                                ('bsr_border', (YLeaf(YType.boolean, 'bsr-border'), ['bool'])),
                                ('propagation_delay', (YLeaf(YType.uint32, 'propagation-delay'), ['int'])),
                                ('dr_priority', (YLeaf(YType.uint32, 'dr-priority'), ['int'])),
                                ('join_prune_mtu', (YLeaf(YType.uint32, 'join-prune-mtu'), ['int'])),
                                ('interface_enable', (YLeaf(YType.boolean, 'interface-enable'), ['bool'])),
                                ('jp_interval', (YLeaf(YType.uint32, 'jp-interval'), ['int'])),
                                ('override_interval', (YLeaf(YType.uint32, 'override-interval'), ['int'])),
                            ])
                            self.interface_name = None
                            self.enable = None
                            self.neighbor_filter = None
                            self.hello_interval = None
                            self.bsr_border = None
                            self.propagation_delay = None
                            self.dr_priority = None
                            self.join_prune_mtu = None
                            self.interface_enable = None
                            self.jp_interval = None
                            self.override_interval = None

                            self.maximum_routes = None
                            self._children_name_map["maximum_routes"] = "maximum-routes"

                            self.bfd = Pim.Vrfs.Vrf.Ipv4.Interfaces.Interface.Bfd()
                            self.bfd.parent = self
                            self._children_name_map["bfd"] = "bfd"
                            self._segment_path = lambda: "interface" + "[interface-name='" + str(self.interface_name) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Pim.Vrfs.Vrf.Ipv4.Interfaces.Interface, ['interface_name', 'enable', 'neighbor_filter', 'hello_interval', 'bsr_border', 'propagation_delay', 'dr_priority', 'join_prune_mtu', 'interface_enable', 'jp_interval', 'override_interval'], name, value)


                        class MaximumRoutes(Entity):
                            """
                            Maximum number of allowed routes for this
                            interface
                            
                            .. attribute:: maximum
                            
                            	Maximum number of routes for this interface
                            	**type**\: int
                            
                            	**range:** 1..1100000
                            
                            	**mandatory**\: True
                            
                            .. attribute:: warning_threshold
                            
                            	Set threshold to print warning
                            	**type**\: int
                            
                            	**range:** 1..1100000
                            
                            .. attribute:: access_list_name
                            
                            	Access\-list to account for
                            	**type**\: str
                            
                            	**length:** 1..64
                            
                            

                            This class is a :ref:`presence class<presence-class>`

                            """

                            _prefix = 'ipv4-pim-cfg'
                            _revision = '2017-10-15'

                            def __init__(self):
                                super(Pim.Vrfs.Vrf.Ipv4.Interfaces.Interface.MaximumRoutes, self).__init__()

                                self.yang_name = "maximum-routes"
                                self.yang_parent_name = "interface"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self.is_presence_container = True
                                self._leafs = OrderedDict([
                                    ('maximum', (YLeaf(YType.uint32, 'maximum'), ['int'])),
                                    ('warning_threshold', (YLeaf(YType.uint32, 'warning-threshold'), ['int'])),
                                    ('access_list_name', (YLeaf(YType.str, 'access-list-name'), ['str'])),
                                ])
                                self.maximum = None
                                self.warning_threshold = None
                                self.access_list_name = None
                                self._segment_path = lambda: "maximum-routes"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Pim.Vrfs.Vrf.Ipv4.Interfaces.Interface.MaximumRoutes, ['maximum', 'warning_threshold', 'access_list_name'], name, value)


                        class Bfd(Entity):
                            """
                            BFD configuration
                            
                            .. attribute:: detection_multiplier
                            
                            	Detection multiplier for BFD sessions created by PIM
                            	**type**\: int
                            
                            	**range:** 2..50
                            
                            .. attribute:: interval
                            
                            	Hello interval for BFD sessions created by PIM
                            	**type**\: int
                            
                            	**range:** 3..30000
                            
                            	**units**\: millisecond
                            
                            .. attribute:: enable
                            
                            	TRUE to enable BFD. FALSE to disable and to prevent inheritance from a parent
                            	**type**\: bool
                            
                            

                            """

                            _prefix = 'ipv4-pim-cfg'
                            _revision = '2017-10-15'

                            def __init__(self):
                                super(Pim.Vrfs.Vrf.Ipv4.Interfaces.Interface.Bfd, self).__init__()

                                self.yang_name = "bfd"
                                self.yang_parent_name = "interface"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('detection_multiplier', (YLeaf(YType.uint32, 'detection-multiplier'), ['int'])),
                                    ('interval', (YLeaf(YType.uint32, 'interval'), ['int'])),
                                    ('enable', (YLeaf(YType.boolean, 'enable'), ['bool'])),
                                ])
                                self.detection_multiplier = None
                                self.interval = None
                                self.enable = None
                                self._segment_path = lambda: "bfd"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Pim.Vrfs.Vrf.Ipv4.Interfaces.Interface.Bfd, ['detection_multiplier', 'interval', 'enable'], name, value)


            class Ipv6(Entity):
                """
                IPV6 commands
                
                .. attribute:: neighbor_check_on_receive
                
                	Enable PIM neighbor checking when receiving PIM messages
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: old_register_checksum
                
                	Generate registers compatible with older IOS versions
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: sparse_mode_rp_addresses
                
                	Configure Sparse\-Mode Rendezvous Point
                	**type**\:  :py:class:`SparseModeRpAddresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.Vrfs.Vrf.Ipv6.SparseModeRpAddresses>`
                
                .. attribute:: neighbor_filter
                
                	Access\-list of neighbors to be filtered
                	**type**\: str
                
                	**length:** 1..64
                
                .. attribute:: inheritable_defaults
                
                	Inheritable defaults
                	**type**\:  :py:class:`InheritableDefaults <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.Vrfs.Vrf.Ipv6.InheritableDefaults>`
                
                .. attribute:: spt_threshold_infinity
                
                	Configure threshold of infinity for switching to SPT on last\-hop
                	**type**\: str
                
                .. attribute:: log_neighbor_changes
                
                	PIM neighbor state change logging is turned on if configured
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: rpf
                
                	Configure RPF options
                	**type**\:  :py:class:`Rpf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.Vrfs.Vrf.Ipv6.Rpf>`
                
                .. attribute:: register_source
                
                	Source address to use for register messages
                	**type**\: str
                
                	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                
                .. attribute:: maximum
                
                	Configure PIM State Limits
                	**type**\:  :py:class:`Maximum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.Vrfs.Vrf.Ipv6.Maximum>`
                
                .. attribute:: accept_register
                
                	Access\-list which specifies unauthorized sources
                	**type**\: str
                
                	**length:** 1..64
                
                .. attribute:: sg_expiry_timer
                
                	Configure expiry timer for S,G routes
                	**type**\:  :py:class:`SgExpiryTimer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.Vrfs.Vrf.Ipv6.SgExpiryTimer>`
                
                .. attribute:: rpf_vector_enable
                
                	Enable PIM RPF Vector Proxy's
                	**type**\:  :py:class:`RpfVectorEnable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.Vrfs.Vrf.Ipv6.RpfVectorEnable>`
                
                	**presence node**\: True
                
                .. attribute:: embedded_rp_disable
                
                	Set Embedded RP processing support
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: suppress_rpf_prunes
                
                	Suppress prunes triggered as a result of RPF changes
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: ssm
                
                	Configure IP Multicast SSM
                	**type**\:  :py:class:`Ssm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.Vrfs.Vrf.Ipv6.Ssm>`
                
                .. attribute:: bidir_rp_addresses
                
                	Configure Bidirectional PIM Rendezvous Point
                	**type**\:  :py:class:`BidirRpAddresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.Vrfs.Vrf.Ipv6.BidirRpAddresses>`
                
                .. attribute:: ssm_allow_override
                
                	Allow SSM ranges to be overridden by more specific ranges
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: multipath
                
                	Enable equal\-cost multipath routing
                	**type**\:  :py:class:`PimMultipath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.PimMultipath>`
                
                .. attribute:: bsr
                
                	PIM BSR configuration
                	**type**\:  :py:class:`Bsr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.Vrfs.Vrf.Ipv6.Bsr>`
                
                .. attribute:: rp_static_deny
                
                	Configure static RP deny range
                	**type**\: str
                
                	**length:** 1..64
                
                .. attribute:: allow_rp
                
                	Enable allow\-rp filtering for SM joins
                	**type**\:  :py:class:`AllowRp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.Vrfs.Vrf.Ipv6.AllowRp>`
                
                	**presence node**\: True
                
                .. attribute:: suppress_data_registers
                
                	Suppress data registers after initial state setup
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: neighbor_check_on_send
                
                	Enable PIM neighbor checking when sending join\-prunes
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: embedded_rp_addresses
                
                	Set Embedded RP processing support
                	**type**\:  :py:class:`EmbeddedRpAddresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.Vrfs.Vrf.Ipv6.EmbeddedRpAddresses>`
                
                .. attribute:: convergence
                
                	Configure convergence parameters
                	**type**\:  :py:class:`Convergence <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.Vrfs.Vrf.Ipv6.Convergence>`
                
                .. attribute:: interfaces
                
                	Interface\-level Configuration
                	**type**\:  :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.Vrfs.Vrf.Ipv6.Interfaces>`
                
                

                """

                _prefix = 'ipv4-pim-cfg'
                _revision = '2017-10-15'

                def __init__(self):
                    super(Pim.Vrfs.Vrf.Ipv6, self).__init__()

                    self.yang_name = "ipv6"
                    self.yang_parent_name = "vrf"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("sparse-mode-rp-addresses", ("sparse_mode_rp_addresses", Pim.Vrfs.Vrf.Ipv6.SparseModeRpAddresses)), ("inheritable-defaults", ("inheritable_defaults", Pim.Vrfs.Vrf.Ipv6.InheritableDefaults)), ("rpf", ("rpf", Pim.Vrfs.Vrf.Ipv6.Rpf)), ("maximum", ("maximum", Pim.Vrfs.Vrf.Ipv6.Maximum)), ("sg-expiry-timer", ("sg_expiry_timer", Pim.Vrfs.Vrf.Ipv6.SgExpiryTimer)), ("rpf-vector-enable", ("rpf_vector_enable", Pim.Vrfs.Vrf.Ipv6.RpfVectorEnable)), ("ssm", ("ssm", Pim.Vrfs.Vrf.Ipv6.Ssm)), ("bidir-rp-addresses", ("bidir_rp_addresses", Pim.Vrfs.Vrf.Ipv6.BidirRpAddresses)), ("bsr", ("bsr", Pim.Vrfs.Vrf.Ipv6.Bsr)), ("allow-rp", ("allow_rp", Pim.Vrfs.Vrf.Ipv6.AllowRp)), ("embedded-rp-addresses", ("embedded_rp_addresses", Pim.Vrfs.Vrf.Ipv6.EmbeddedRpAddresses)), ("convergence", ("convergence", Pim.Vrfs.Vrf.Ipv6.Convergence)), ("interfaces", ("interfaces", Pim.Vrfs.Vrf.Ipv6.Interfaces))])
                    self._leafs = OrderedDict([
                        ('neighbor_check_on_receive', (YLeaf(YType.empty, 'neighbor-check-on-receive'), ['Empty'])),
                        ('old_register_checksum', (YLeaf(YType.empty, 'old-register-checksum'), ['Empty'])),
                        ('neighbor_filter', (YLeaf(YType.str, 'neighbor-filter'), ['str'])),
                        ('spt_threshold_infinity', (YLeaf(YType.str, 'spt-threshold-infinity'), ['str'])),
                        ('log_neighbor_changes', (YLeaf(YType.empty, 'log-neighbor-changes'), ['Empty'])),
                        ('register_source', (YLeaf(YType.str, 'register-source'), ['str'])),
                        ('accept_register', (YLeaf(YType.str, 'accept-register'), ['str'])),
                        ('embedded_rp_disable', (YLeaf(YType.empty, 'embedded-rp-disable'), ['Empty'])),
                        ('suppress_rpf_prunes', (YLeaf(YType.empty, 'suppress-rpf-prunes'), ['Empty'])),
                        ('ssm_allow_override', (YLeaf(YType.empty, 'ssm-allow-override'), ['Empty'])),
                        ('multipath', (YLeaf(YType.enumeration, 'multipath'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg', 'PimMultipath', '')])),
                        ('rp_static_deny', (YLeaf(YType.str, 'rp-static-deny'), ['str'])),
                        ('suppress_data_registers', (YLeaf(YType.empty, 'suppress-data-registers'), ['Empty'])),
                        ('neighbor_check_on_send', (YLeaf(YType.empty, 'neighbor-check-on-send'), ['Empty'])),
                    ])
                    self.neighbor_check_on_receive = None
                    self.old_register_checksum = None
                    self.neighbor_filter = None
                    self.spt_threshold_infinity = None
                    self.log_neighbor_changes = None
                    self.register_source = None
                    self.accept_register = None
                    self.embedded_rp_disable = None
                    self.suppress_rpf_prunes = None
                    self.ssm_allow_override = None
                    self.multipath = None
                    self.rp_static_deny = None
                    self.suppress_data_registers = None
                    self.neighbor_check_on_send = None

                    self.sparse_mode_rp_addresses = Pim.Vrfs.Vrf.Ipv6.SparseModeRpAddresses()
                    self.sparse_mode_rp_addresses.parent = self
                    self._children_name_map["sparse_mode_rp_addresses"] = "sparse-mode-rp-addresses"

                    self.inheritable_defaults = Pim.Vrfs.Vrf.Ipv6.InheritableDefaults()
                    self.inheritable_defaults.parent = self
                    self._children_name_map["inheritable_defaults"] = "inheritable-defaults"

                    self.rpf = Pim.Vrfs.Vrf.Ipv6.Rpf()
                    self.rpf.parent = self
                    self._children_name_map["rpf"] = "rpf"

                    self.maximum = Pim.Vrfs.Vrf.Ipv6.Maximum()
                    self.maximum.parent = self
                    self._children_name_map["maximum"] = "maximum"

                    self.sg_expiry_timer = Pim.Vrfs.Vrf.Ipv6.SgExpiryTimer()
                    self.sg_expiry_timer.parent = self
                    self._children_name_map["sg_expiry_timer"] = "sg-expiry-timer"

                    self.rpf_vector_enable = None
                    self._children_name_map["rpf_vector_enable"] = "rpf-vector-enable"

                    self.ssm = Pim.Vrfs.Vrf.Ipv6.Ssm()
                    self.ssm.parent = self
                    self._children_name_map["ssm"] = "ssm"

                    self.bidir_rp_addresses = Pim.Vrfs.Vrf.Ipv6.BidirRpAddresses()
                    self.bidir_rp_addresses.parent = self
                    self._children_name_map["bidir_rp_addresses"] = "bidir-rp-addresses"

                    self.bsr = Pim.Vrfs.Vrf.Ipv6.Bsr()
                    self.bsr.parent = self
                    self._children_name_map["bsr"] = "bsr"

                    self.allow_rp = None
                    self._children_name_map["allow_rp"] = "allow-rp"

                    self.embedded_rp_addresses = Pim.Vrfs.Vrf.Ipv6.EmbeddedRpAddresses()
                    self.embedded_rp_addresses.parent = self
                    self._children_name_map["embedded_rp_addresses"] = "embedded-rp-addresses"

                    self.convergence = Pim.Vrfs.Vrf.Ipv6.Convergence()
                    self.convergence.parent = self
                    self._children_name_map["convergence"] = "convergence"

                    self.interfaces = Pim.Vrfs.Vrf.Ipv6.Interfaces()
                    self.interfaces.parent = self
                    self._children_name_map["interfaces"] = "interfaces"
                    self._segment_path = lambda: "ipv6"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Pim.Vrfs.Vrf.Ipv6, ['neighbor_check_on_receive', 'old_register_checksum', 'neighbor_filter', 'spt_threshold_infinity', 'log_neighbor_changes', 'register_source', 'accept_register', 'embedded_rp_disable', 'suppress_rpf_prunes', 'ssm_allow_override', 'multipath', 'rp_static_deny', 'suppress_data_registers', 'neighbor_check_on_send'], name, value)


                class SparseModeRpAddresses(Entity):
                    """
                    Configure Sparse\-Mode Rendezvous Point
                    
                    .. attribute:: sparse_mode_rp_address
                    
                    	Address of the Rendezvous Point
                    	**type**\: list of  		 :py:class:`SparseModeRpAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.Vrfs.Vrf.Ipv6.SparseModeRpAddresses.SparseModeRpAddress>`
                    
                    

                    """

                    _prefix = 'ipv4-pim-cfg'
                    _revision = '2017-10-15'

                    def __init__(self):
                        super(Pim.Vrfs.Vrf.Ipv6.SparseModeRpAddresses, self).__init__()

                        self.yang_name = "sparse-mode-rp-addresses"
                        self.yang_parent_name = "ipv6"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("sparse-mode-rp-address", ("sparse_mode_rp_address", Pim.Vrfs.Vrf.Ipv6.SparseModeRpAddresses.SparseModeRpAddress))])
                        self._leafs = OrderedDict()

                        self.sparse_mode_rp_address = YList(self)
                        self._segment_path = lambda: "sparse-mode-rp-addresses"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Pim.Vrfs.Vrf.Ipv6.SparseModeRpAddresses, [], name, value)


                    class SparseModeRpAddress(Entity):
                        """
                        Address of the Rendezvous Point
                        
                        .. attribute:: rp_address  (key)
                        
                        	RP address of Rendezvous Point
                        	**type**\: union of the below types:
                        
                        		**type**\: str
                        
                        			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        		**type**\: str
                        
                        			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: access_list_name
                        
                        	Access list of groups that should map to a  given RP
                        	**type**\: str
                        
                        	**length:** 1..64
                        
                        .. attribute:: auto_rp_override
                        
                        	TRUE Indicates if static RP config overrides AutoRP and BSR
                        	**type**\: bool
                        
                        

                        """

                        _prefix = 'ipv4-pim-cfg'
                        _revision = '2017-10-15'

                        def __init__(self):
                            super(Pim.Vrfs.Vrf.Ipv6.SparseModeRpAddresses.SparseModeRpAddress, self).__init__()

                            self.yang_name = "sparse-mode-rp-address"
                            self.yang_parent_name = "sparse-mode-rp-addresses"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['rp_address']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('rp_address', (YLeaf(YType.str, 'rp-address'), ['str','str'])),
                                ('access_list_name', (YLeaf(YType.str, 'access-list-name'), ['str'])),
                                ('auto_rp_override', (YLeaf(YType.boolean, 'auto-rp-override'), ['bool'])),
                            ])
                            self.rp_address = None
                            self.access_list_name = None
                            self.auto_rp_override = None
                            self._segment_path = lambda: "sparse-mode-rp-address" + "[rp-address='" + str(self.rp_address) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Pim.Vrfs.Vrf.Ipv6.SparseModeRpAddresses.SparseModeRpAddress, ['rp_address', 'access_list_name', 'auto_rp_override'], name, value)


                class InheritableDefaults(Entity):
                    """
                    Inheritable defaults
                    
                    .. attribute:: convergence_timeout
                    
                    	Convergency timeout in seconds
                    	**type**\: int
                    
                    	**range:** 1800..2400
                    
                    	**units**\: second
                    
                    .. attribute:: hello_interval
                    
                    	Hello interval in seconds
                    	**type**\: int
                    
                    	**range:** 1..3600
                    
                    	**units**\: second
                    
                    .. attribute:: propagation_delay
                    
                    	Propagation delay in milli seconds
                    	**type**\: int
                    
                    	**range:** 100..32767
                    
                    	**units**\: millisecond
                    
                    .. attribute:: dr_priority
                    
                    	Hello DR priority, preference given to larger value
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: join_prune_mtu
                    
                    	Join\-Prune MTU in Bytes
                    	**type**\: int
                    
                    	**range:** 576..65535
                    
                    	**units**\: byte
                    
                    .. attribute:: jp_interval
                    
                    	Join\-Prune interval in seconds
                    	**type**\: int
                    
                    	**range:** 10..600
                    
                    	**units**\: second
                    
                    .. attribute:: override_interval
                    
                    	Override interval in milliseconds
                    	**type**\: int
                    
                    	**range:** 400..65535
                    
                    	**units**\: millisecond
                    
                    

                    """

                    _prefix = 'ipv4-pim-cfg'
                    _revision = '2017-10-15'

                    def __init__(self):
                        super(Pim.Vrfs.Vrf.Ipv6.InheritableDefaults, self).__init__()

                        self.yang_name = "inheritable-defaults"
                        self.yang_parent_name = "ipv6"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('convergence_timeout', (YLeaf(YType.uint32, 'convergence-timeout'), ['int'])),
                            ('hello_interval', (YLeaf(YType.uint32, 'hello-interval'), ['int'])),
                            ('propagation_delay', (YLeaf(YType.uint32, 'propagation-delay'), ['int'])),
                            ('dr_priority', (YLeaf(YType.uint32, 'dr-priority'), ['int'])),
                            ('join_prune_mtu', (YLeaf(YType.uint32, 'join-prune-mtu'), ['int'])),
                            ('jp_interval', (YLeaf(YType.uint32, 'jp-interval'), ['int'])),
                            ('override_interval', (YLeaf(YType.uint32, 'override-interval'), ['int'])),
                        ])
                        self.convergence_timeout = None
                        self.hello_interval = None
                        self.propagation_delay = None
                        self.dr_priority = None
                        self.join_prune_mtu = None
                        self.jp_interval = None
                        self.override_interval = None
                        self._segment_path = lambda: "inheritable-defaults"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Pim.Vrfs.Vrf.Ipv6.InheritableDefaults, ['convergence_timeout', 'hello_interval', 'propagation_delay', 'dr_priority', 'join_prune_mtu', 'jp_interval', 'override_interval'], name, value)


                class Rpf(Entity):
                    """
                    Configure RPF options
                    
                    .. attribute:: route_policy
                    
                    	Route policy to select RPF topology
                    	**type**\: str
                    
                    	**length:** 1..64
                    
                    

                    """

                    _prefix = 'ipv4-pim-cfg'
                    _revision = '2017-10-15'

                    def __init__(self):
                        super(Pim.Vrfs.Vrf.Ipv6.Rpf, self).__init__()

                        self.yang_name = "rpf"
                        self.yang_parent_name = "ipv6"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('route_policy', (YLeaf(YType.str, 'route-policy'), ['str'])),
                        ])
                        self.route_policy = None
                        self._segment_path = lambda: "rpf"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Pim.Vrfs.Vrf.Ipv6.Rpf, ['route_policy'], name, value)


                class Maximum(Entity):
                    """
                    Configure PIM State Limits
                    
                    .. attribute:: group_mappings_auto_rp
                    
                    	Override default maximum for number of group mappings from autorp mapping agent
                    	**type**\:  :py:class:`GroupMappingsAutoRp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.Vrfs.Vrf.Ipv6.Maximum.GroupMappingsAutoRp>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: bsr_group_mappings
                    
                    	Override default maximum and threshold for number of group mappings from BSR
                    	**type**\:  :py:class:`BsrGroupMappings <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.Vrfs.Vrf.Ipv6.Maximum.BsrGroupMappings>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: register_states
                    
                    	Override default maximum for number of sparse\-mode source registers
                    	**type**\:  :py:class:`RegisterStates <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.Vrfs.Vrf.Ipv6.Maximum.RegisterStates>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: route_interfaces
                    
                    	Override default maximum for number of route\-interfaces
                    	**type**\:  :py:class:`RouteInterfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.Vrfs.Vrf.Ipv6.Maximum.RouteInterfaces>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: bsr_candidate_rp_cache
                    
                    	Override default maximum and threshold for BSR C\-RP cache setting
                    	**type**\:  :py:class:`BsrCandidateRpCache <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.Vrfs.Vrf.Ipv6.Maximum.BsrCandidateRpCache>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: routes
                    
                    	Override default maximum for number of routes
                    	**type**\:  :py:class:`Routes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.Vrfs.Vrf.Ipv6.Maximum.Routes>`
                    
                    	**presence node**\: True
                    
                    

                    """

                    _prefix = 'ipv4-pim-cfg'
                    _revision = '2017-10-15'

                    def __init__(self):
                        super(Pim.Vrfs.Vrf.Ipv6.Maximum, self).__init__()

                        self.yang_name = "maximum"
                        self.yang_parent_name = "ipv6"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("group-mappings-auto-rp", ("group_mappings_auto_rp", Pim.Vrfs.Vrf.Ipv6.Maximum.GroupMappingsAutoRp)), ("bsr-group-mappings", ("bsr_group_mappings", Pim.Vrfs.Vrf.Ipv6.Maximum.BsrGroupMappings)), ("register-states", ("register_states", Pim.Vrfs.Vrf.Ipv6.Maximum.RegisterStates)), ("route-interfaces", ("route_interfaces", Pim.Vrfs.Vrf.Ipv6.Maximum.RouteInterfaces)), ("bsr-candidate-rp-cache", ("bsr_candidate_rp_cache", Pim.Vrfs.Vrf.Ipv6.Maximum.BsrCandidateRpCache)), ("routes", ("routes", Pim.Vrfs.Vrf.Ipv6.Maximum.Routes))])
                        self._leafs = OrderedDict()

                        self.group_mappings_auto_rp = None
                        self._children_name_map["group_mappings_auto_rp"] = "group-mappings-auto-rp"

                        self.bsr_group_mappings = None
                        self._children_name_map["bsr_group_mappings"] = "bsr-group-mappings"

                        self.register_states = None
                        self._children_name_map["register_states"] = "register-states"

                        self.route_interfaces = None
                        self._children_name_map["route_interfaces"] = "route-interfaces"

                        self.bsr_candidate_rp_cache = None
                        self._children_name_map["bsr_candidate_rp_cache"] = "bsr-candidate-rp-cache"

                        self.routes = None
                        self._children_name_map["routes"] = "routes"
                        self._segment_path = lambda: "maximum"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Pim.Vrfs.Vrf.Ipv6.Maximum, [], name, value)


                    class GroupMappingsAutoRp(Entity):
                        """
                        Override default maximum for number of group
                        mappings from autorp mapping agent
                        
                        .. attribute:: maximum_group_ranges_auto_rp
                        
                        	Maximum number of PIM group mappings from autorp
                        	**type**\: int
                        
                        	**range:** 1..10000
                        
                        	**mandatory**\: True
                        
                        .. attribute:: threshold_group_ranges_auto_rp
                        
                        	Warning threshold number of PIM group mappings from autorp
                        	**type**\: int
                        
                        	**range:** 1..10000
                        
                        	**default value**\: 450
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'ipv4-pim-cfg'
                        _revision = '2017-10-15'

                        def __init__(self):
                            super(Pim.Vrfs.Vrf.Ipv6.Maximum.GroupMappingsAutoRp, self).__init__()

                            self.yang_name = "group-mappings-auto-rp"
                            self.yang_parent_name = "maximum"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self.is_presence_container = True
                            self._leafs = OrderedDict([
                                ('maximum_group_ranges_auto_rp', (YLeaf(YType.uint32, 'maximum-group-ranges-auto-rp'), ['int'])),
                                ('threshold_group_ranges_auto_rp', (YLeaf(YType.uint32, 'threshold-group-ranges-auto-rp'), ['int'])),
                            ])
                            self.maximum_group_ranges_auto_rp = None
                            self.threshold_group_ranges_auto_rp = None
                            self._segment_path = lambda: "group-mappings-auto-rp"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Pim.Vrfs.Vrf.Ipv6.Maximum.GroupMappingsAutoRp, ['maximum_group_ranges_auto_rp', 'threshold_group_ranges_auto_rp'], name, value)


                    class BsrGroupMappings(Entity):
                        """
                        Override default maximum and threshold for
                        number of group mappings from BSR
                        
                        .. attribute:: bsr_maximum_group_ranges
                        
                        	Maximum number of PIM group mappings from BSR
                        	**type**\: int
                        
                        	**range:** 1..10000
                        
                        	**mandatory**\: True
                        
                        .. attribute:: warning_threshold
                        
                        	Set threshold to print warning
                        	**type**\: int
                        
                        	**range:** 1..10000
                        
                        	**default value**\: 500
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'ipv4-pim-cfg'
                        _revision = '2017-10-15'

                        def __init__(self):
                            super(Pim.Vrfs.Vrf.Ipv6.Maximum.BsrGroupMappings, self).__init__()

                            self.yang_name = "bsr-group-mappings"
                            self.yang_parent_name = "maximum"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self.is_presence_container = True
                            self._leafs = OrderedDict([
                                ('bsr_maximum_group_ranges', (YLeaf(YType.uint32, 'bsr-maximum-group-ranges'), ['int'])),
                                ('warning_threshold', (YLeaf(YType.uint32, 'warning-threshold'), ['int'])),
                            ])
                            self.bsr_maximum_group_ranges = None
                            self.warning_threshold = None
                            self._segment_path = lambda: "bsr-group-mappings"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Pim.Vrfs.Vrf.Ipv6.Maximum.BsrGroupMappings, ['bsr_maximum_group_ranges', 'warning_threshold'], name, value)


                    class RegisterStates(Entity):
                        """
                        Override default maximum for number of
                        sparse\-mode source registers
                        
                        .. attribute:: maximum_register_states
                        
                        	Maximum number of PIM Sparse\-Mode register states
                        	**type**\: int
                        
                        	**range:** 0..75000
                        
                        	**mandatory**\: True
                        
                        .. attribute:: warning_threshold
                        
                        	Set threshold to print warning
                        	**type**\: int
                        
                        	**range:** 0..75000
                        
                        	**default value**\: 20000
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'ipv4-pim-cfg'
                        _revision = '2017-10-15'

                        def __init__(self):
                            super(Pim.Vrfs.Vrf.Ipv6.Maximum.RegisterStates, self).__init__()

                            self.yang_name = "register-states"
                            self.yang_parent_name = "maximum"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self.is_presence_container = True
                            self._leafs = OrderedDict([
                                ('maximum_register_states', (YLeaf(YType.uint32, 'maximum-register-states'), ['int'])),
                                ('warning_threshold', (YLeaf(YType.uint32, 'warning-threshold'), ['int'])),
                            ])
                            self.maximum_register_states = None
                            self.warning_threshold = None
                            self._segment_path = lambda: "register-states"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Pim.Vrfs.Vrf.Ipv6.Maximum.RegisterStates, ['maximum_register_states', 'warning_threshold'], name, value)


                    class RouteInterfaces(Entity):
                        """
                        Override default maximum for number of
                        route\-interfaces
                        
                        .. attribute:: maximum_route_interfaces
                        
                        	Maximum number of PIM route\-interfaces
                        	**type**\: int
                        
                        	**range:** 1..1100000
                        
                        	**mandatory**\: True
                        
                        .. attribute:: warning_threshold
                        
                        	Set threshold to print warning
                        	**type**\: int
                        
                        	**range:** 1..1100000
                        
                        	**default value**\: 300000
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'ipv4-pim-cfg'
                        _revision = '2017-10-15'

                        def __init__(self):
                            super(Pim.Vrfs.Vrf.Ipv6.Maximum.RouteInterfaces, self).__init__()

                            self.yang_name = "route-interfaces"
                            self.yang_parent_name = "maximum"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self.is_presence_container = True
                            self._leafs = OrderedDict([
                                ('maximum_route_interfaces', (YLeaf(YType.uint32, 'maximum-route-interfaces'), ['int'])),
                                ('warning_threshold', (YLeaf(YType.uint32, 'warning-threshold'), ['int'])),
                            ])
                            self.maximum_route_interfaces = None
                            self.warning_threshold = None
                            self._segment_path = lambda: "route-interfaces"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Pim.Vrfs.Vrf.Ipv6.Maximum.RouteInterfaces, ['maximum_route_interfaces', 'warning_threshold'], name, value)


                    class BsrCandidateRpCache(Entity):
                        """
                        Override default maximum and threshold for BSR
                        C\-RP cache setting
                        
                        .. attribute:: bsr_maximum_candidate_rp_cache
                        
                        	Maximum number of BSR C\-RP cache setting
                        	**type**\: int
                        
                        	**range:** 1..10000
                        
                        	**mandatory**\: True
                        
                        .. attribute:: warning_threshold
                        
                        	Set threshold to print warning
                        	**type**\: int
                        
                        	**range:** 1..10000
                        
                        	**default value**\: 100
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'ipv4-pim-cfg'
                        _revision = '2017-10-15'

                        def __init__(self):
                            super(Pim.Vrfs.Vrf.Ipv6.Maximum.BsrCandidateRpCache, self).__init__()

                            self.yang_name = "bsr-candidate-rp-cache"
                            self.yang_parent_name = "maximum"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self.is_presence_container = True
                            self._leafs = OrderedDict([
                                ('bsr_maximum_candidate_rp_cache', (YLeaf(YType.uint32, 'bsr-maximum-candidate-rp-cache'), ['int'])),
                                ('warning_threshold', (YLeaf(YType.uint32, 'warning-threshold'), ['int'])),
                            ])
                            self.bsr_maximum_candidate_rp_cache = None
                            self.warning_threshold = None
                            self._segment_path = lambda: "bsr-candidate-rp-cache"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Pim.Vrfs.Vrf.Ipv6.Maximum.BsrCandidateRpCache, ['bsr_maximum_candidate_rp_cache', 'warning_threshold'], name, value)


                    class Routes(Entity):
                        """
                        Override default maximum for number of routes
                        
                        .. attribute:: maximum_routes
                        
                        	Maximum number of PIM routes
                        	**type**\: int
                        
                        	**range:** 1..200000
                        
                        	**mandatory**\: True
                        
                        .. attribute:: warning_threshold
                        
                        	Set threshold to print warning
                        	**type**\: int
                        
                        	**range:** 1..200000
                        
                        	**default value**\: 100000
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'ipv4-pim-cfg'
                        _revision = '2017-10-15'

                        def __init__(self):
                            super(Pim.Vrfs.Vrf.Ipv6.Maximum.Routes, self).__init__()

                            self.yang_name = "routes"
                            self.yang_parent_name = "maximum"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self.is_presence_container = True
                            self._leafs = OrderedDict([
                                ('maximum_routes', (YLeaf(YType.uint32, 'maximum-routes'), ['int'])),
                                ('warning_threshold', (YLeaf(YType.uint32, 'warning-threshold'), ['int'])),
                            ])
                            self.maximum_routes = None
                            self.warning_threshold = None
                            self._segment_path = lambda: "routes"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Pim.Vrfs.Vrf.Ipv6.Maximum.Routes, ['maximum_routes', 'warning_threshold'], name, value)


                class SgExpiryTimer(Entity):
                    """
                    Configure expiry timer for S,G routes
                    
                    .. attribute:: interval
                    
                    	(S,G) expiry time in seconds
                    	**type**\: int
                    
                    	**range:** 40..57600
                    
                    	**units**\: second
                    
                    .. attribute:: access_list_name
                    
                    	Access\-list of applicable S,G routes
                    	**type**\: str
                    
                    	**length:** 1..64
                    
                    

                    """

                    _prefix = 'ipv4-pim-cfg'
                    _revision = '2017-10-15'

                    def __init__(self):
                        super(Pim.Vrfs.Vrf.Ipv6.SgExpiryTimer, self).__init__()

                        self.yang_name = "sg-expiry-timer"
                        self.yang_parent_name = "ipv6"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('interval', (YLeaf(YType.uint32, 'interval'), ['int'])),
                            ('access_list_name', (YLeaf(YType.str, 'access-list-name'), ['str'])),
                        ])
                        self.interval = None
                        self.access_list_name = None
                        self._segment_path = lambda: "sg-expiry-timer"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Pim.Vrfs.Vrf.Ipv6.SgExpiryTimer, ['interval', 'access_list_name'], name, value)


                class RpfVectorEnable(Entity):
                    """
                    Enable PIM RPF Vector Proxy's
                    
                    .. attribute:: enable
                    
                    	RPF Vector is turned on if configured
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    	**mandatory**\: True
                    
                    .. attribute:: allow_ebgp
                    
                    	Allow RPF Vector origination over eBGP sessions
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: disable_ibgp
                    
                    	Disable RPF Vector origination over iBGP sessions
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: use_standard_encoding
                    
                    	Use RPF Vector RFC compliant encoding
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'ipv4-pim-cfg'
                    _revision = '2017-10-15'

                    def __init__(self):
                        super(Pim.Vrfs.Vrf.Ipv6.RpfVectorEnable, self).__init__()

                        self.yang_name = "rpf-vector-enable"
                        self.yang_parent_name = "ipv6"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self.is_presence_container = True
                        self._leafs = OrderedDict([
                            ('enable', (YLeaf(YType.empty, 'enable'), ['Empty'])),
                            ('allow_ebgp', (YLeaf(YType.empty, 'allow-ebgp'), ['Empty'])),
                            ('disable_ibgp', (YLeaf(YType.empty, 'disable-ibgp'), ['Empty'])),
                            ('use_standard_encoding', (YLeaf(YType.empty, 'use-standard-encoding'), ['Empty'])),
                        ])
                        self.enable = None
                        self.allow_ebgp = None
                        self.disable_ibgp = None
                        self.use_standard_encoding = None
                        self._segment_path = lambda: "rpf-vector-enable"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Pim.Vrfs.Vrf.Ipv6.RpfVectorEnable, ['enable', 'allow_ebgp', 'disable_ibgp', 'use_standard_encoding'], name, value)


                class Ssm(Entity):
                    """
                    Configure IP Multicast SSM
                    
                    .. attribute:: disable
                    
                    	TRUE if SSM is disabled on this router
                    	**type**\: bool
                    
                    	**default value**\: false
                    
                    .. attribute:: range
                    
                    	Access list of groups enabled with SSM
                    	**type**\: str
                    
                    	**length:** 1..64
                    
                    

                    """

                    _prefix = 'ipv4-pim-cfg'
                    _revision = '2017-10-15'

                    def __init__(self):
                        super(Pim.Vrfs.Vrf.Ipv6.Ssm, self).__init__()

                        self.yang_name = "ssm"
                        self.yang_parent_name = "ipv6"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('disable', (YLeaf(YType.boolean, 'disable'), ['bool'])),
                            ('range', (YLeaf(YType.str, 'range'), ['str'])),
                        ])
                        self.disable = None
                        self.range = None
                        self._segment_path = lambda: "ssm"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Pim.Vrfs.Vrf.Ipv6.Ssm, ['disable', 'range'], name, value)


                class BidirRpAddresses(Entity):
                    """
                    Configure Bidirectional PIM Rendezvous Point
                    
                    .. attribute:: bidir_rp_address
                    
                    	Address of the Rendezvous Point
                    	**type**\: list of  		 :py:class:`BidirRpAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.Vrfs.Vrf.Ipv6.BidirRpAddresses.BidirRpAddress>`
                    
                    

                    """

                    _prefix = 'ipv4-pim-cfg'
                    _revision = '2017-10-15'

                    def __init__(self):
                        super(Pim.Vrfs.Vrf.Ipv6.BidirRpAddresses, self).__init__()

                        self.yang_name = "bidir-rp-addresses"
                        self.yang_parent_name = "ipv6"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("bidir-rp-address", ("bidir_rp_address", Pim.Vrfs.Vrf.Ipv6.BidirRpAddresses.BidirRpAddress))])
                        self._leafs = OrderedDict()

                        self.bidir_rp_address = YList(self)
                        self._segment_path = lambda: "bidir-rp-addresses"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Pim.Vrfs.Vrf.Ipv6.BidirRpAddresses, [], name, value)


                    class BidirRpAddress(Entity):
                        """
                        Address of the Rendezvous Point
                        
                        .. attribute:: rp_address  (key)
                        
                        	RP address of Rendezvous Point
                        	**type**\: union of the below types:
                        
                        		**type**\: str
                        
                        			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        		**type**\: str
                        
                        			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: access_list_name
                        
                        	Access list of groups that should map to a given RP
                        	**type**\: str
                        
                        	**length:** 1..64
                        
                        .. attribute:: auto_rp_override
                        
                        	TRUE Indicates if static RP config overrides AutoRP and BSR
                        	**type**\: bool
                        
                        

                        """

                        _prefix = 'ipv4-pim-cfg'
                        _revision = '2017-10-15'

                        def __init__(self):
                            super(Pim.Vrfs.Vrf.Ipv6.BidirRpAddresses.BidirRpAddress, self).__init__()

                            self.yang_name = "bidir-rp-address"
                            self.yang_parent_name = "bidir-rp-addresses"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['rp_address']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('rp_address', (YLeaf(YType.str, 'rp-address'), ['str','str'])),
                                ('access_list_name', (YLeaf(YType.str, 'access-list-name'), ['str'])),
                                ('auto_rp_override', (YLeaf(YType.boolean, 'auto-rp-override'), ['bool'])),
                            ])
                            self.rp_address = None
                            self.access_list_name = None
                            self.auto_rp_override = None
                            self._segment_path = lambda: "bidir-rp-address" + "[rp-address='" + str(self.rp_address) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Pim.Vrfs.Vrf.Ipv6.BidirRpAddresses.BidirRpAddress, ['rp_address', 'access_list_name', 'auto_rp_override'], name, value)


                class Bsr(Entity):
                    """
                    PIM BSR configuration
                    
                    .. attribute:: candidate_bsr
                    
                    	PIM Candidate BSR configuration
                    	**type**\:  :py:class:`CandidateBsr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.Vrfs.Vrf.Ipv6.Bsr.CandidateBsr>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: candidate_rps
                    
                    	PIM RP configuration
                    	**type**\:  :py:class:`CandidateRps <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.Vrfs.Vrf.Ipv6.Bsr.CandidateRps>`
                    
                    

                    """

                    _prefix = 'ipv4-pim-cfg'
                    _revision = '2017-10-15'

                    def __init__(self):
                        super(Pim.Vrfs.Vrf.Ipv6.Bsr, self).__init__()

                        self.yang_name = "bsr"
                        self.yang_parent_name = "ipv6"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("candidate-bsr", ("candidate_bsr", Pim.Vrfs.Vrf.Ipv6.Bsr.CandidateBsr)), ("candidate-rps", ("candidate_rps", Pim.Vrfs.Vrf.Ipv6.Bsr.CandidateRps))])
                        self._leafs = OrderedDict()

                        self.candidate_bsr = None
                        self._children_name_map["candidate_bsr"] = "candidate-bsr"

                        self.candidate_rps = Pim.Vrfs.Vrf.Ipv6.Bsr.CandidateRps()
                        self.candidate_rps.parent = self
                        self._children_name_map["candidate_rps"] = "candidate-rps"
                        self._segment_path = lambda: "bsr"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Pim.Vrfs.Vrf.Ipv6.Bsr, [], name, value)


                    class CandidateBsr(Entity):
                        """
                        PIM Candidate BSR configuration
                        
                        .. attribute:: address
                        
                        	BSR Address configured
                        	**type**\: str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        	**mandatory**\: True
                        
                        .. attribute:: prefix_length
                        
                        	Hash Mask Length for this candidate BSR
                        	**type**\: int
                        
                        	**range:** 0..128
                        
                        	**default value**\: 126
                        
                        .. attribute:: priority
                        
                        	Priority of the Candidate BSR
                        	**type**\: int
                        
                        	**range:** 1..255
                        
                        	**default value**\: 1
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'ipv4-pim-cfg'
                        _revision = '2017-10-15'

                        def __init__(self):
                            super(Pim.Vrfs.Vrf.Ipv6.Bsr.CandidateBsr, self).__init__()

                            self.yang_name = "candidate-bsr"
                            self.yang_parent_name = "bsr"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self.is_presence_container = True
                            self._leafs = OrderedDict([
                                ('address', (YLeaf(YType.str, 'address'), ['str'])),
                                ('prefix_length', (YLeaf(YType.uint8, 'prefix-length'), ['int'])),
                                ('priority', (YLeaf(YType.uint32, 'priority'), ['int'])),
                            ])
                            self.address = None
                            self.prefix_length = None
                            self.priority = None
                            self._segment_path = lambda: "candidate-bsr"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Pim.Vrfs.Vrf.Ipv6.Bsr.CandidateBsr, ['address', 'prefix_length', 'priority'], name, value)


                    class CandidateRps(Entity):
                        """
                        PIM RP configuration
                        
                        .. attribute:: candidate_rp
                        
                        	Address of PIM SM BSR Candidate\-RP
                        	**type**\: list of  		 :py:class:`CandidateRp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.Vrfs.Vrf.Ipv6.Bsr.CandidateRps.CandidateRp>`
                        
                        

                        """

                        _prefix = 'ipv4-pim-cfg'
                        _revision = '2017-10-15'

                        def __init__(self):
                            super(Pim.Vrfs.Vrf.Ipv6.Bsr.CandidateRps, self).__init__()

                            self.yang_name = "candidate-rps"
                            self.yang_parent_name = "bsr"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("candidate-rp", ("candidate_rp", Pim.Vrfs.Vrf.Ipv6.Bsr.CandidateRps.CandidateRp))])
                            self._leafs = OrderedDict()

                            self.candidate_rp = YList(self)
                            self._segment_path = lambda: "candidate-rps"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Pim.Vrfs.Vrf.Ipv6.Bsr.CandidateRps, [], name, value)


                        class CandidateRp(Entity):
                            """
                            Address of PIM SM BSR Candidate\-RP
                            
                            .. attribute:: address  (key)
                            
                            	Address of Candidate\-RP
                            	**type**\: union of the below types:
                            
                            		**type**\: str
                            
                            			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            		**type**\: str
                            
                            			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: mode  (key)
                            
                            	SM or Bidir
                            	**type**\:  :py:class:`PimProtocolMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.PimProtocolMode>`
                            
                            .. attribute:: group_list
                            
                            	Access\-list specifying the group range for the Candidate\-RP
                            	**type**\: str
                            
                            	**length:** 1..64
                            
                            .. attribute:: priority
                            
                            	Priority of the CRP
                            	**type**\: int
                            
                            	**range:** 1..255
                            
                            	**default value**\: 192
                            
                            .. attribute:: interval
                            
                            	Advertisement interval
                            	**type**\: int
                            
                            	**range:** 30..600
                            
                            	**default value**\: 60
                            
                            

                            """

                            _prefix = 'ipv4-pim-cfg'
                            _revision = '2017-10-15'

                            def __init__(self):
                                super(Pim.Vrfs.Vrf.Ipv6.Bsr.CandidateRps.CandidateRp, self).__init__()

                                self.yang_name = "candidate-rp"
                                self.yang_parent_name = "candidate-rps"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['address','mode']
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('address', (YLeaf(YType.str, 'address'), ['str','str'])),
                                    ('mode', (YLeaf(YType.enumeration, 'mode'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg', 'PimProtocolMode', '')])),
                                    ('group_list', (YLeaf(YType.str, 'group-list'), ['str'])),
                                    ('priority', (YLeaf(YType.uint32, 'priority'), ['int'])),
                                    ('interval', (YLeaf(YType.uint32, 'interval'), ['int'])),
                                ])
                                self.address = None
                                self.mode = None
                                self.group_list = None
                                self.priority = None
                                self.interval = None
                                self._segment_path = lambda: "candidate-rp" + "[address='" + str(self.address) + "']" + "[mode='" + str(self.mode) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Pim.Vrfs.Vrf.Ipv6.Bsr.CandidateRps.CandidateRp, ['address', 'mode', 'group_list', 'priority', 'interval'], name, value)


                class AllowRp(Entity):
                    """
                    Enable allow\-rp filtering for SM joins
                    
                    .. attribute:: rp_list_name
                    
                    	Access\-list specifiying applicable RPs
                    	**type**\: str
                    
                    	**length:** 1..64
                    
                    .. attribute:: group_list_name
                    
                    	Access\-list specifiying applicable groups
                    	**type**\: str
                    
                    	**length:** 1..64
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'ipv4-pim-cfg'
                    _revision = '2017-10-15'

                    def __init__(self):
                        super(Pim.Vrfs.Vrf.Ipv6.AllowRp, self).__init__()

                        self.yang_name = "allow-rp"
                        self.yang_parent_name = "ipv6"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self.is_presence_container = True
                        self._leafs = OrderedDict([
                            ('rp_list_name', (YLeaf(YType.str, 'rp-list-name'), ['str'])),
                            ('group_list_name', (YLeaf(YType.str, 'group-list-name'), ['str'])),
                        ])
                        self.rp_list_name = None
                        self.group_list_name = None
                        self._segment_path = lambda: "allow-rp"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Pim.Vrfs.Vrf.Ipv6.AllowRp, ['rp_list_name', 'group_list_name'], name, value)


                class EmbeddedRpAddresses(Entity):
                    """
                    Set Embedded RP processing support
                    
                    .. attribute:: embedded_rp_address
                    
                    	Set Embedded RP processing support
                    	**type**\: list of  		 :py:class:`EmbeddedRpAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.Vrfs.Vrf.Ipv6.EmbeddedRpAddresses.EmbeddedRpAddress>`
                    
                    

                    """

                    _prefix = 'ipv4-pim-cfg'
                    _revision = '2017-10-15'

                    def __init__(self):
                        super(Pim.Vrfs.Vrf.Ipv6.EmbeddedRpAddresses, self).__init__()

                        self.yang_name = "embedded-rp-addresses"
                        self.yang_parent_name = "ipv6"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("embedded-rp-address", ("embedded_rp_address", Pim.Vrfs.Vrf.Ipv6.EmbeddedRpAddresses.EmbeddedRpAddress))])
                        self._leafs = OrderedDict()

                        self.embedded_rp_address = YList(self)
                        self._segment_path = lambda: "embedded-rp-addresses"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Pim.Vrfs.Vrf.Ipv6.EmbeddedRpAddresses, [], name, value)


                    class EmbeddedRpAddress(Entity):
                        """
                        Set Embedded RP processing support
                        
                        .. attribute:: rp_address  (key)
                        
                        	RP address of the Rendezvous Point
                        	**type**\: union of the below types:
                        
                        		**type**\: str
                        
                        			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        		**type**\: str
                        
                        			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: access_list_name
                        
                        	Access list of groups that should map to a given RP
                        	**type**\: str
                        
                        	**length:** 1..64
                        
                        	**mandatory**\: True
                        
                        

                        """

                        _prefix = 'ipv4-pim-cfg'
                        _revision = '2017-10-15'

                        def __init__(self):
                            super(Pim.Vrfs.Vrf.Ipv6.EmbeddedRpAddresses.EmbeddedRpAddress, self).__init__()

                            self.yang_name = "embedded-rp-address"
                            self.yang_parent_name = "embedded-rp-addresses"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['rp_address']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('rp_address', (YLeaf(YType.str, 'rp-address'), ['str','str'])),
                                ('access_list_name', (YLeaf(YType.str, 'access-list-name'), ['str'])),
                            ])
                            self.rp_address = None
                            self.access_list_name = None
                            self._segment_path = lambda: "embedded-rp-address" + "[rp-address='" + str(self.rp_address) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Pim.Vrfs.Vrf.Ipv6.EmbeddedRpAddresses.EmbeddedRpAddress, ['rp_address', 'access_list_name'], name, value)


                class Convergence(Entity):
                    """
                    Configure convergence parameters
                    
                    .. attribute:: rpf_conflict_join_delay
                    
                    	Dampen first join if RPF path is through one of the downstream neighbor
                    	**type**\: int
                    
                    	**range:** 0..15
                    
                    	**units**\: second
                    
                    .. attribute:: link_down_prune_delay
                    
                    	Delay prunes if route join state transitions to not\-joined on link down
                    	**type**\: int
                    
                    	**range:** 0..60
                    
                    	**units**\: second
                    
                    

                    """

                    _prefix = 'ipv4-pim-cfg'
                    _revision = '2017-10-15'

                    def __init__(self):
                        super(Pim.Vrfs.Vrf.Ipv6.Convergence, self).__init__()

                        self.yang_name = "convergence"
                        self.yang_parent_name = "ipv6"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('rpf_conflict_join_delay', (YLeaf(YType.uint32, 'rpf-conflict-join-delay'), ['int'])),
                            ('link_down_prune_delay', (YLeaf(YType.uint32, 'link-down-prune-delay'), ['int'])),
                        ])
                        self.rpf_conflict_join_delay = None
                        self.link_down_prune_delay = None
                        self._segment_path = lambda: "convergence"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Pim.Vrfs.Vrf.Ipv6.Convergence, ['rpf_conflict_join_delay', 'link_down_prune_delay'], name, value)


                class Interfaces(Entity):
                    """
                    Interface\-level Configuration
                    
                    .. attribute:: interface
                    
                    	The name of the interface
                    	**type**\: list of  		 :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.Vrfs.Vrf.Ipv6.Interfaces.Interface>`
                    
                    

                    """

                    _prefix = 'ipv4-pim-cfg'
                    _revision = '2017-10-15'

                    def __init__(self):
                        super(Pim.Vrfs.Vrf.Ipv6.Interfaces, self).__init__()

                        self.yang_name = "interfaces"
                        self.yang_parent_name = "ipv6"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("interface", ("interface", Pim.Vrfs.Vrf.Ipv6.Interfaces.Interface))])
                        self._leafs = OrderedDict()

                        self.interface = YList(self)
                        self._segment_path = lambda: "interfaces"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Pim.Vrfs.Vrf.Ipv6.Interfaces, [], name, value)


                    class Interface(Entity):
                        """
                        The name of the interface
                        
                        .. attribute:: interface_name  (key)
                        
                        	The name of interface
                        	**type**\: str
                        
                        	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                        
                        .. attribute:: enable
                        
                        	Enter PIM Interface processing
                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: neighbor_filter
                        
                        	Access\-list of neighbors to be filtered
                        	**type**\: str
                        
                        	**length:** 1..64
                        
                        .. attribute:: hello_interval
                        
                        	Hello interval in seconds
                        	**type**\: int
                        
                        	**range:** 1..3600
                        
                        	**units**\: second
                        
                        .. attribute:: bsr_border
                        
                        	BSR Border configuration for Interface
                        	**type**\: bool
                        
                        .. attribute:: maximum_routes
                        
                        	Maximum number of allowed routes for this interface
                        	**type**\:  :py:class:`MaximumRoutes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.Vrfs.Vrf.Ipv6.Interfaces.Interface.MaximumRoutes>`
                        
                        	**presence node**\: True
                        
                        .. attribute:: propagation_delay
                        
                        	Propagation delay in milli seconds
                        	**type**\: int
                        
                        	**range:** 100..32767
                        
                        	**units**\: millisecond
                        
                        .. attribute:: bfd
                        
                        	BFD configuration
                        	**type**\:  :py:class:`Bfd <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.Vrfs.Vrf.Ipv6.Interfaces.Interface.Bfd>`
                        
                        .. attribute:: dr_priority
                        
                        	Hello DR priority, preference given to larger value
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: join_prune_mtu
                        
                        	Join\-Prune MTU in Bytes
                        	**type**\: int
                        
                        	**range:** 576..65535
                        
                        	**units**\: byte
                        
                        .. attribute:: interface_enable
                        
                        	Enable PIM processing on the interface
                        	**type**\: bool
                        
                        .. attribute:: jp_interval
                        
                        	Join\-Prune interval in seconds
                        	**type**\: int
                        
                        	**range:** 10..600
                        
                        	**units**\: second
                        
                        .. attribute:: override_interval
                        
                        	Override interval in milliseconds
                        	**type**\: int
                        
                        	**range:** 400..65535
                        
                        	**units**\: millisecond
                        
                        

                        """

                        _prefix = 'ipv4-pim-cfg'
                        _revision = '2017-10-15'

                        def __init__(self):
                            super(Pim.Vrfs.Vrf.Ipv6.Interfaces.Interface, self).__init__()

                            self.yang_name = "interface"
                            self.yang_parent_name = "interfaces"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['interface_name']
                            self._child_classes = OrderedDict([("maximum-routes", ("maximum_routes", Pim.Vrfs.Vrf.Ipv6.Interfaces.Interface.MaximumRoutes)), ("bfd", ("bfd", Pim.Vrfs.Vrf.Ipv6.Interfaces.Interface.Bfd))])
                            self._leafs = OrderedDict([
                                ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                                ('enable', (YLeaf(YType.empty, 'enable'), ['Empty'])),
                                ('neighbor_filter', (YLeaf(YType.str, 'neighbor-filter'), ['str'])),
                                ('hello_interval', (YLeaf(YType.uint32, 'hello-interval'), ['int'])),
                                ('bsr_border', (YLeaf(YType.boolean, 'bsr-border'), ['bool'])),
                                ('propagation_delay', (YLeaf(YType.uint32, 'propagation-delay'), ['int'])),
                                ('dr_priority', (YLeaf(YType.uint32, 'dr-priority'), ['int'])),
                                ('join_prune_mtu', (YLeaf(YType.uint32, 'join-prune-mtu'), ['int'])),
                                ('interface_enable', (YLeaf(YType.boolean, 'interface-enable'), ['bool'])),
                                ('jp_interval', (YLeaf(YType.uint32, 'jp-interval'), ['int'])),
                                ('override_interval', (YLeaf(YType.uint32, 'override-interval'), ['int'])),
                            ])
                            self.interface_name = None
                            self.enable = None
                            self.neighbor_filter = None
                            self.hello_interval = None
                            self.bsr_border = None
                            self.propagation_delay = None
                            self.dr_priority = None
                            self.join_prune_mtu = None
                            self.interface_enable = None
                            self.jp_interval = None
                            self.override_interval = None

                            self.maximum_routes = None
                            self._children_name_map["maximum_routes"] = "maximum-routes"

                            self.bfd = Pim.Vrfs.Vrf.Ipv6.Interfaces.Interface.Bfd()
                            self.bfd.parent = self
                            self._children_name_map["bfd"] = "bfd"
                            self._segment_path = lambda: "interface" + "[interface-name='" + str(self.interface_name) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Pim.Vrfs.Vrf.Ipv6.Interfaces.Interface, ['interface_name', 'enable', 'neighbor_filter', 'hello_interval', 'bsr_border', 'propagation_delay', 'dr_priority', 'join_prune_mtu', 'interface_enable', 'jp_interval', 'override_interval'], name, value)


                        class MaximumRoutes(Entity):
                            """
                            Maximum number of allowed routes for this
                            interface
                            
                            .. attribute:: maximum
                            
                            	Maximum number of routes for this interface
                            	**type**\: int
                            
                            	**range:** 1..1100000
                            
                            	**mandatory**\: True
                            
                            .. attribute:: warning_threshold
                            
                            	Set threshold to print warning
                            	**type**\: int
                            
                            	**range:** 1..1100000
                            
                            .. attribute:: access_list_name
                            
                            	Access\-list to account for
                            	**type**\: str
                            
                            	**length:** 1..64
                            
                            

                            This class is a :ref:`presence class<presence-class>`

                            """

                            _prefix = 'ipv4-pim-cfg'
                            _revision = '2017-10-15'

                            def __init__(self):
                                super(Pim.Vrfs.Vrf.Ipv6.Interfaces.Interface.MaximumRoutes, self).__init__()

                                self.yang_name = "maximum-routes"
                                self.yang_parent_name = "interface"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self.is_presence_container = True
                                self._leafs = OrderedDict([
                                    ('maximum', (YLeaf(YType.uint32, 'maximum'), ['int'])),
                                    ('warning_threshold', (YLeaf(YType.uint32, 'warning-threshold'), ['int'])),
                                    ('access_list_name', (YLeaf(YType.str, 'access-list-name'), ['str'])),
                                ])
                                self.maximum = None
                                self.warning_threshold = None
                                self.access_list_name = None
                                self._segment_path = lambda: "maximum-routes"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Pim.Vrfs.Vrf.Ipv6.Interfaces.Interface.MaximumRoutes, ['maximum', 'warning_threshold', 'access_list_name'], name, value)


                        class Bfd(Entity):
                            """
                            BFD configuration
                            
                            .. attribute:: detection_multiplier
                            
                            	Detection multiplier for BFD sessions created by PIM
                            	**type**\: int
                            
                            	**range:** 2..50
                            
                            .. attribute:: interval
                            
                            	Hello interval for BFD sessions created by PIM
                            	**type**\: int
                            
                            	**range:** 3..30000
                            
                            	**units**\: millisecond
                            
                            .. attribute:: enable
                            
                            	TRUE to enable BFD. FALSE to disable and to prevent inheritance from a parent
                            	**type**\: bool
                            
                            

                            """

                            _prefix = 'ipv4-pim-cfg'
                            _revision = '2017-10-15'

                            def __init__(self):
                                super(Pim.Vrfs.Vrf.Ipv6.Interfaces.Interface.Bfd, self).__init__()

                                self.yang_name = "bfd"
                                self.yang_parent_name = "interface"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('detection_multiplier', (YLeaf(YType.uint32, 'detection-multiplier'), ['int'])),
                                    ('interval', (YLeaf(YType.uint32, 'interval'), ['int'])),
                                    ('enable', (YLeaf(YType.boolean, 'enable'), ['bool'])),
                                ])
                                self.detection_multiplier = None
                                self.interval = None
                                self.enable = None
                                self._segment_path = lambda: "bfd"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Pim.Vrfs.Vrf.Ipv6.Interfaces.Interface.Bfd, ['detection_multiplier', 'interval', 'enable'], name, value)


    class DefaultContext(Entity):
        """
        Default Context
        
        .. attribute:: ipv6
        
        	IPV6 commands
        	**type**\:  :py:class:`Ipv6 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.DefaultContext.Ipv6>`
        
        .. attribute:: ipv4
        
        	IPV4 commands
        	**type**\:  :py:class:`Ipv4 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.DefaultContext.Ipv4>`
        
        

        """

        _prefix = 'ipv4-pim-cfg'
        _revision = '2017-10-15'

        def __init__(self):
            super(Pim.DefaultContext, self).__init__()

            self.yang_name = "default-context"
            self.yang_parent_name = "pim"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("ipv6", ("ipv6", Pim.DefaultContext.Ipv6)), ("ipv4", ("ipv4", Pim.DefaultContext.Ipv4))])
            self._leafs = OrderedDict()

            self.ipv6 = Pim.DefaultContext.Ipv6()
            self.ipv6.parent = self
            self._children_name_map["ipv6"] = "ipv6"

            self.ipv4 = Pim.DefaultContext.Ipv4()
            self.ipv4.parent = self
            self._children_name_map["ipv4"] = "ipv4"
            self._segment_path = lambda: "default-context"
            self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-pim-cfg:pim/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Pim.DefaultContext, [], name, value)


        class Ipv6(Entity):
            """
            IPV6 commands
            
            .. attribute:: interfaces
            
            	Interface\-level Configuration
            	**type**\:  :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.DefaultContext.Ipv6.Interfaces>`
            
            .. attribute:: neighbor_check_on_receive
            
            	Enable PIM neighbor checking when receiving PIM messages
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: old_register_checksum
            
            	Generate registers compatible with older IOS versions
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: sparse_mode_rp_addresses
            
            	Configure Sparse\-Mode Rendezvous Point
            	**type**\:  :py:class:`SparseModeRpAddresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.DefaultContext.Ipv6.SparseModeRpAddresses>`
            
            .. attribute:: neighbor_filter
            
            	Access\-list of neighbors to be filtered
            	**type**\: str
            
            	**length:** 1..64
            
            .. attribute:: inheritable_defaults
            
            	Inheritable defaults
            	**type**\:  :py:class:`InheritableDefaults <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.DefaultContext.Ipv6.InheritableDefaults>`
            
            .. attribute:: spt_threshold_infinity
            
            	Configure threshold of infinity for switching to SPT on last\-hop
            	**type**\: str
            
            .. attribute:: log_neighbor_changes
            
            	PIM neighbor state change logging is turned on if configured
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: rpf
            
            	Configure RPF options
            	**type**\:  :py:class:`Rpf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.DefaultContext.Ipv6.Rpf>`
            
            .. attribute:: register_source
            
            	Source address to use for register messages
            	**type**\: str
            
            	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
            
            .. attribute:: accept_register
            
            	Access\-list which specifies unauthorized sources
            	**type**\: str
            
            	**length:** 1..64
            
            .. attribute:: sg_expiry_timer
            
            	Configure expiry timer for S,G routes
            	**type**\:  :py:class:`SgExpiryTimer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.DefaultContext.Ipv6.SgExpiryTimer>`
            
            .. attribute:: rpf_vector_enable
            
            	Enable PIM RPF Vector Proxy's
            	**type**\:  :py:class:`RpfVectorEnable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.DefaultContext.Ipv6.RpfVectorEnable>`
            
            	**presence node**\: True
            
            .. attribute:: nsf
            
            	Configure Non\-stop forwarding (NSF) options
            	**type**\:  :py:class:`Nsf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.DefaultContext.Ipv6.Nsf>`
            
            .. attribute:: embedded_rp_disable
            
            	Set Embedded RP processing support
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: suppress_rpf_prunes
            
            	Suppress prunes triggered as a result of RPF changes
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: maximum
            
            	Configure PIM State Limits
            	**type**\:  :py:class:`Maximum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.DefaultContext.Ipv6.Maximum>`
            
            .. attribute:: ssm
            
            	Configure IP Multicast SSM
            	**type**\:  :py:class:`Ssm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.DefaultContext.Ipv6.Ssm>`
            
            .. attribute:: bidir_rp_addresses
            
            	Configure Bidirectional PIM Rendezvous Point
            	**type**\:  :py:class:`BidirRpAddresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.DefaultContext.Ipv6.BidirRpAddresses>`
            
            .. attribute:: ssm_allow_override
            
            	Allow SSM ranges to be overridden by more specific ranges
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: multipath
            
            	Enable equal\-cost multipath routing
            	**type**\:  :py:class:`PimMultipath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.PimMultipath>`
            
            .. attribute:: bsr
            
            	PIM BSR configuration
            	**type**\:  :py:class:`Bsr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.DefaultContext.Ipv6.Bsr>`
            
            .. attribute:: rp_static_deny
            
            	Configure static RP deny range
            	**type**\: str
            
            	**length:** 1..64
            
            .. attribute:: allow_rp
            
            	Enable allow\-rp filtering for SM joins
            	**type**\:  :py:class:`AllowRp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.DefaultContext.Ipv6.AllowRp>`
            
            	**presence node**\: True
            
            .. attribute:: suppress_data_registers
            
            	Suppress data registers after initial state setup
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: neighbor_check_on_send
            
            	Enable PIM neighbor checking when sending join\-prunes
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: embedded_rp_addresses
            
            	Set Embedded RP processing support
            	**type**\:  :py:class:`EmbeddedRpAddresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.DefaultContext.Ipv6.EmbeddedRpAddresses>`
            
            .. attribute:: convergence
            
            	Configure convergence parameters
            	**type**\:  :py:class:`Convergence <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.DefaultContext.Ipv6.Convergence>`
            
            

            """

            _prefix = 'ipv4-pim-cfg'
            _revision = '2017-10-15'

            def __init__(self):
                super(Pim.DefaultContext.Ipv6, self).__init__()

                self.yang_name = "ipv6"
                self.yang_parent_name = "default-context"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("interfaces", ("interfaces", Pim.DefaultContext.Ipv6.Interfaces)), ("sparse-mode-rp-addresses", ("sparse_mode_rp_addresses", Pim.DefaultContext.Ipv6.SparseModeRpAddresses)), ("inheritable-defaults", ("inheritable_defaults", Pim.DefaultContext.Ipv6.InheritableDefaults)), ("rpf", ("rpf", Pim.DefaultContext.Ipv6.Rpf)), ("sg-expiry-timer", ("sg_expiry_timer", Pim.DefaultContext.Ipv6.SgExpiryTimer)), ("rpf-vector-enable", ("rpf_vector_enable", Pim.DefaultContext.Ipv6.RpfVectorEnable)), ("nsf", ("nsf", Pim.DefaultContext.Ipv6.Nsf)), ("maximum", ("maximum", Pim.DefaultContext.Ipv6.Maximum)), ("ssm", ("ssm", Pim.DefaultContext.Ipv6.Ssm)), ("bidir-rp-addresses", ("bidir_rp_addresses", Pim.DefaultContext.Ipv6.BidirRpAddresses)), ("bsr", ("bsr", Pim.DefaultContext.Ipv6.Bsr)), ("allow-rp", ("allow_rp", Pim.DefaultContext.Ipv6.AllowRp)), ("embedded-rp-addresses", ("embedded_rp_addresses", Pim.DefaultContext.Ipv6.EmbeddedRpAddresses)), ("convergence", ("convergence", Pim.DefaultContext.Ipv6.Convergence))])
                self._leafs = OrderedDict([
                    ('neighbor_check_on_receive', (YLeaf(YType.empty, 'neighbor-check-on-receive'), ['Empty'])),
                    ('old_register_checksum', (YLeaf(YType.empty, 'old-register-checksum'), ['Empty'])),
                    ('neighbor_filter', (YLeaf(YType.str, 'neighbor-filter'), ['str'])),
                    ('spt_threshold_infinity', (YLeaf(YType.str, 'spt-threshold-infinity'), ['str'])),
                    ('log_neighbor_changes', (YLeaf(YType.empty, 'log-neighbor-changes'), ['Empty'])),
                    ('register_source', (YLeaf(YType.str, 'register-source'), ['str'])),
                    ('accept_register', (YLeaf(YType.str, 'accept-register'), ['str'])),
                    ('embedded_rp_disable', (YLeaf(YType.empty, 'embedded-rp-disable'), ['Empty'])),
                    ('suppress_rpf_prunes', (YLeaf(YType.empty, 'suppress-rpf-prunes'), ['Empty'])),
                    ('ssm_allow_override', (YLeaf(YType.empty, 'ssm-allow-override'), ['Empty'])),
                    ('multipath', (YLeaf(YType.enumeration, 'multipath'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg', 'PimMultipath', '')])),
                    ('rp_static_deny', (YLeaf(YType.str, 'rp-static-deny'), ['str'])),
                    ('suppress_data_registers', (YLeaf(YType.empty, 'suppress-data-registers'), ['Empty'])),
                    ('neighbor_check_on_send', (YLeaf(YType.empty, 'neighbor-check-on-send'), ['Empty'])),
                ])
                self.neighbor_check_on_receive = None
                self.old_register_checksum = None
                self.neighbor_filter = None
                self.spt_threshold_infinity = None
                self.log_neighbor_changes = None
                self.register_source = None
                self.accept_register = None
                self.embedded_rp_disable = None
                self.suppress_rpf_prunes = None
                self.ssm_allow_override = None
                self.multipath = None
                self.rp_static_deny = None
                self.suppress_data_registers = None
                self.neighbor_check_on_send = None

                self.interfaces = Pim.DefaultContext.Ipv6.Interfaces()
                self.interfaces.parent = self
                self._children_name_map["interfaces"] = "interfaces"

                self.sparse_mode_rp_addresses = Pim.DefaultContext.Ipv6.SparseModeRpAddresses()
                self.sparse_mode_rp_addresses.parent = self
                self._children_name_map["sparse_mode_rp_addresses"] = "sparse-mode-rp-addresses"

                self.inheritable_defaults = Pim.DefaultContext.Ipv6.InheritableDefaults()
                self.inheritable_defaults.parent = self
                self._children_name_map["inheritable_defaults"] = "inheritable-defaults"

                self.rpf = Pim.DefaultContext.Ipv6.Rpf()
                self.rpf.parent = self
                self._children_name_map["rpf"] = "rpf"

                self.sg_expiry_timer = Pim.DefaultContext.Ipv6.SgExpiryTimer()
                self.sg_expiry_timer.parent = self
                self._children_name_map["sg_expiry_timer"] = "sg-expiry-timer"

                self.rpf_vector_enable = None
                self._children_name_map["rpf_vector_enable"] = "rpf-vector-enable"

                self.nsf = Pim.DefaultContext.Ipv6.Nsf()
                self.nsf.parent = self
                self._children_name_map["nsf"] = "nsf"

                self.maximum = Pim.DefaultContext.Ipv6.Maximum()
                self.maximum.parent = self
                self._children_name_map["maximum"] = "maximum"

                self.ssm = Pim.DefaultContext.Ipv6.Ssm()
                self.ssm.parent = self
                self._children_name_map["ssm"] = "ssm"

                self.bidir_rp_addresses = Pim.DefaultContext.Ipv6.BidirRpAddresses()
                self.bidir_rp_addresses.parent = self
                self._children_name_map["bidir_rp_addresses"] = "bidir-rp-addresses"

                self.bsr = Pim.DefaultContext.Ipv6.Bsr()
                self.bsr.parent = self
                self._children_name_map["bsr"] = "bsr"

                self.allow_rp = None
                self._children_name_map["allow_rp"] = "allow-rp"

                self.embedded_rp_addresses = Pim.DefaultContext.Ipv6.EmbeddedRpAddresses()
                self.embedded_rp_addresses.parent = self
                self._children_name_map["embedded_rp_addresses"] = "embedded-rp-addresses"

                self.convergence = Pim.DefaultContext.Ipv6.Convergence()
                self.convergence.parent = self
                self._children_name_map["convergence"] = "convergence"
                self._segment_path = lambda: "ipv6"
                self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-pim-cfg:pim/default-context/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Pim.DefaultContext.Ipv6, ['neighbor_check_on_receive', 'old_register_checksum', 'neighbor_filter', 'spt_threshold_infinity', 'log_neighbor_changes', 'register_source', 'accept_register', 'embedded_rp_disable', 'suppress_rpf_prunes', 'ssm_allow_override', 'multipath', 'rp_static_deny', 'suppress_data_registers', 'neighbor_check_on_send'], name, value)


            class Interfaces(Entity):
                """
                Interface\-level Configuration
                
                .. attribute:: interface
                
                	The name of the interface
                	**type**\: list of  		 :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.DefaultContext.Ipv6.Interfaces.Interface>`
                
                

                """

                _prefix = 'ipv4-pim-cfg'
                _revision = '2017-10-15'

                def __init__(self):
                    super(Pim.DefaultContext.Ipv6.Interfaces, self).__init__()

                    self.yang_name = "interfaces"
                    self.yang_parent_name = "ipv6"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("interface", ("interface", Pim.DefaultContext.Ipv6.Interfaces.Interface))])
                    self._leafs = OrderedDict()

                    self.interface = YList(self)
                    self._segment_path = lambda: "interfaces"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-pim-cfg:pim/default-context/ipv6/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Pim.DefaultContext.Ipv6.Interfaces, [], name, value)


                class Interface(Entity):
                    """
                    The name of the interface
                    
                    .. attribute:: interface_name  (key)
                    
                    	The name of interface
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                    
                    .. attribute:: enable
                    
                    	Enter PIM Interface processing
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: neighbor_filter
                    
                    	Access\-list of neighbors to be filtered
                    	**type**\: str
                    
                    	**length:** 1..64
                    
                    .. attribute:: hello_interval
                    
                    	Hello interval in seconds
                    	**type**\: int
                    
                    	**range:** 1..3600
                    
                    	**units**\: second
                    
                    .. attribute:: bsr_border
                    
                    	BSR Border configuration for Interface
                    	**type**\: bool
                    
                    .. attribute:: maximum_routes
                    
                    	Maximum number of allowed routes for this interface
                    	**type**\:  :py:class:`MaximumRoutes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.DefaultContext.Ipv6.Interfaces.Interface.MaximumRoutes>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: propagation_delay
                    
                    	Propagation delay in milli seconds
                    	**type**\: int
                    
                    	**range:** 100..32767
                    
                    	**units**\: millisecond
                    
                    .. attribute:: bfd
                    
                    	BFD configuration
                    	**type**\:  :py:class:`Bfd <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.DefaultContext.Ipv6.Interfaces.Interface.Bfd>`
                    
                    .. attribute:: dr_priority
                    
                    	Hello DR priority, preference given to larger value
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: join_prune_mtu
                    
                    	Join\-Prune MTU in Bytes
                    	**type**\: int
                    
                    	**range:** 576..65535
                    
                    	**units**\: byte
                    
                    .. attribute:: interface_enable
                    
                    	Enable PIM processing on the interface
                    	**type**\: bool
                    
                    .. attribute:: jp_interval
                    
                    	Join\-Prune interval in seconds
                    	**type**\: int
                    
                    	**range:** 10..600
                    
                    	**units**\: second
                    
                    .. attribute:: override_interval
                    
                    	Override interval in milliseconds
                    	**type**\: int
                    
                    	**range:** 400..65535
                    
                    	**units**\: millisecond
                    
                    

                    """

                    _prefix = 'ipv4-pim-cfg'
                    _revision = '2017-10-15'

                    def __init__(self):
                        super(Pim.DefaultContext.Ipv6.Interfaces.Interface, self).__init__()

                        self.yang_name = "interface"
                        self.yang_parent_name = "interfaces"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['interface_name']
                        self._child_classes = OrderedDict([("maximum-routes", ("maximum_routes", Pim.DefaultContext.Ipv6.Interfaces.Interface.MaximumRoutes)), ("bfd", ("bfd", Pim.DefaultContext.Ipv6.Interfaces.Interface.Bfd))])
                        self._leafs = OrderedDict([
                            ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                            ('enable', (YLeaf(YType.empty, 'enable'), ['Empty'])),
                            ('neighbor_filter', (YLeaf(YType.str, 'neighbor-filter'), ['str'])),
                            ('hello_interval', (YLeaf(YType.uint32, 'hello-interval'), ['int'])),
                            ('bsr_border', (YLeaf(YType.boolean, 'bsr-border'), ['bool'])),
                            ('propagation_delay', (YLeaf(YType.uint32, 'propagation-delay'), ['int'])),
                            ('dr_priority', (YLeaf(YType.uint32, 'dr-priority'), ['int'])),
                            ('join_prune_mtu', (YLeaf(YType.uint32, 'join-prune-mtu'), ['int'])),
                            ('interface_enable', (YLeaf(YType.boolean, 'interface-enable'), ['bool'])),
                            ('jp_interval', (YLeaf(YType.uint32, 'jp-interval'), ['int'])),
                            ('override_interval', (YLeaf(YType.uint32, 'override-interval'), ['int'])),
                        ])
                        self.interface_name = None
                        self.enable = None
                        self.neighbor_filter = None
                        self.hello_interval = None
                        self.bsr_border = None
                        self.propagation_delay = None
                        self.dr_priority = None
                        self.join_prune_mtu = None
                        self.interface_enable = None
                        self.jp_interval = None
                        self.override_interval = None

                        self.maximum_routes = None
                        self._children_name_map["maximum_routes"] = "maximum-routes"

                        self.bfd = Pim.DefaultContext.Ipv6.Interfaces.Interface.Bfd()
                        self.bfd.parent = self
                        self._children_name_map["bfd"] = "bfd"
                        self._segment_path = lambda: "interface" + "[interface-name='" + str(self.interface_name) + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-pim-cfg:pim/default-context/ipv6/interfaces/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Pim.DefaultContext.Ipv6.Interfaces.Interface, ['interface_name', 'enable', 'neighbor_filter', 'hello_interval', 'bsr_border', 'propagation_delay', 'dr_priority', 'join_prune_mtu', 'interface_enable', 'jp_interval', 'override_interval'], name, value)


                    class MaximumRoutes(Entity):
                        """
                        Maximum number of allowed routes for this
                        interface
                        
                        .. attribute:: maximum
                        
                        	Maximum number of routes for this interface
                        	**type**\: int
                        
                        	**range:** 1..1100000
                        
                        	**mandatory**\: True
                        
                        .. attribute:: warning_threshold
                        
                        	Set threshold to print warning
                        	**type**\: int
                        
                        	**range:** 1..1100000
                        
                        .. attribute:: access_list_name
                        
                        	Access\-list to account for
                        	**type**\: str
                        
                        	**length:** 1..64
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'ipv4-pim-cfg'
                        _revision = '2017-10-15'

                        def __init__(self):
                            super(Pim.DefaultContext.Ipv6.Interfaces.Interface.MaximumRoutes, self).__init__()

                            self.yang_name = "maximum-routes"
                            self.yang_parent_name = "interface"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self.is_presence_container = True
                            self._leafs = OrderedDict([
                                ('maximum', (YLeaf(YType.uint32, 'maximum'), ['int'])),
                                ('warning_threshold', (YLeaf(YType.uint32, 'warning-threshold'), ['int'])),
                                ('access_list_name', (YLeaf(YType.str, 'access-list-name'), ['str'])),
                            ])
                            self.maximum = None
                            self.warning_threshold = None
                            self.access_list_name = None
                            self._segment_path = lambda: "maximum-routes"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Pim.DefaultContext.Ipv6.Interfaces.Interface.MaximumRoutes, ['maximum', 'warning_threshold', 'access_list_name'], name, value)


                    class Bfd(Entity):
                        """
                        BFD configuration
                        
                        .. attribute:: detection_multiplier
                        
                        	Detection multiplier for BFD sessions created by PIM
                        	**type**\: int
                        
                        	**range:** 2..50
                        
                        .. attribute:: interval
                        
                        	Hello interval for BFD sessions created by PIM
                        	**type**\: int
                        
                        	**range:** 3..30000
                        
                        	**units**\: millisecond
                        
                        .. attribute:: enable
                        
                        	TRUE to enable BFD. FALSE to disable and to prevent inheritance from a parent
                        	**type**\: bool
                        
                        

                        """

                        _prefix = 'ipv4-pim-cfg'
                        _revision = '2017-10-15'

                        def __init__(self):
                            super(Pim.DefaultContext.Ipv6.Interfaces.Interface.Bfd, self).__init__()

                            self.yang_name = "bfd"
                            self.yang_parent_name = "interface"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('detection_multiplier', (YLeaf(YType.uint32, 'detection-multiplier'), ['int'])),
                                ('interval', (YLeaf(YType.uint32, 'interval'), ['int'])),
                                ('enable', (YLeaf(YType.boolean, 'enable'), ['bool'])),
                            ])
                            self.detection_multiplier = None
                            self.interval = None
                            self.enable = None
                            self._segment_path = lambda: "bfd"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Pim.DefaultContext.Ipv6.Interfaces.Interface.Bfd, ['detection_multiplier', 'interval', 'enable'], name, value)


            class SparseModeRpAddresses(Entity):
                """
                Configure Sparse\-Mode Rendezvous Point
                
                .. attribute:: sparse_mode_rp_address
                
                	Address of the Rendezvous Point
                	**type**\: list of  		 :py:class:`SparseModeRpAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.DefaultContext.Ipv6.SparseModeRpAddresses.SparseModeRpAddress>`
                
                

                """

                _prefix = 'ipv4-pim-cfg'
                _revision = '2017-10-15'

                def __init__(self):
                    super(Pim.DefaultContext.Ipv6.SparseModeRpAddresses, self).__init__()

                    self.yang_name = "sparse-mode-rp-addresses"
                    self.yang_parent_name = "ipv6"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("sparse-mode-rp-address", ("sparse_mode_rp_address", Pim.DefaultContext.Ipv6.SparseModeRpAddresses.SparseModeRpAddress))])
                    self._leafs = OrderedDict()

                    self.sparse_mode_rp_address = YList(self)
                    self._segment_path = lambda: "sparse-mode-rp-addresses"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-pim-cfg:pim/default-context/ipv6/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Pim.DefaultContext.Ipv6.SparseModeRpAddresses, [], name, value)


                class SparseModeRpAddress(Entity):
                    """
                    Address of the Rendezvous Point
                    
                    .. attribute:: rp_address  (key)
                    
                    	RP address of Rendezvous Point
                    	**type**\: union of the below types:
                    
                    		**type**\: str
                    
                    			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    		**type**\: str
                    
                    			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: access_list_name
                    
                    	Access list of groups that should map to a  given RP
                    	**type**\: str
                    
                    	**length:** 1..64
                    
                    .. attribute:: auto_rp_override
                    
                    	TRUE Indicates if static RP config overrides AutoRP and BSR
                    	**type**\: bool
                    
                    

                    """

                    _prefix = 'ipv4-pim-cfg'
                    _revision = '2017-10-15'

                    def __init__(self):
                        super(Pim.DefaultContext.Ipv6.SparseModeRpAddresses.SparseModeRpAddress, self).__init__()

                        self.yang_name = "sparse-mode-rp-address"
                        self.yang_parent_name = "sparse-mode-rp-addresses"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['rp_address']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('rp_address', (YLeaf(YType.str, 'rp-address'), ['str','str'])),
                            ('access_list_name', (YLeaf(YType.str, 'access-list-name'), ['str'])),
                            ('auto_rp_override', (YLeaf(YType.boolean, 'auto-rp-override'), ['bool'])),
                        ])
                        self.rp_address = None
                        self.access_list_name = None
                        self.auto_rp_override = None
                        self._segment_path = lambda: "sparse-mode-rp-address" + "[rp-address='" + str(self.rp_address) + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-pim-cfg:pim/default-context/ipv6/sparse-mode-rp-addresses/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Pim.DefaultContext.Ipv6.SparseModeRpAddresses.SparseModeRpAddress, ['rp_address', 'access_list_name', 'auto_rp_override'], name, value)


            class InheritableDefaults(Entity):
                """
                Inheritable defaults
                
                .. attribute:: convergence_timeout
                
                	Convergency timeout in seconds
                	**type**\: int
                
                	**range:** 1800..2400
                
                	**units**\: second
                
                .. attribute:: hello_interval
                
                	Hello interval in seconds
                	**type**\: int
                
                	**range:** 1..3600
                
                	**units**\: second
                
                .. attribute:: propagation_delay
                
                	Propagation delay in milli seconds
                	**type**\: int
                
                	**range:** 100..32767
                
                	**units**\: millisecond
                
                .. attribute:: dr_priority
                
                	Hello DR priority, preference given to larger value
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: join_prune_mtu
                
                	Join\-Prune MTU in Bytes
                	**type**\: int
                
                	**range:** 576..65535
                
                	**units**\: byte
                
                .. attribute:: jp_interval
                
                	Join\-Prune interval in seconds
                	**type**\: int
                
                	**range:** 10..600
                
                	**units**\: second
                
                .. attribute:: override_interval
                
                	Override interval in milliseconds
                	**type**\: int
                
                	**range:** 400..65535
                
                	**units**\: millisecond
                
                

                """

                _prefix = 'ipv4-pim-cfg'
                _revision = '2017-10-15'

                def __init__(self):
                    super(Pim.DefaultContext.Ipv6.InheritableDefaults, self).__init__()

                    self.yang_name = "inheritable-defaults"
                    self.yang_parent_name = "ipv6"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('convergence_timeout', (YLeaf(YType.uint32, 'convergence-timeout'), ['int'])),
                        ('hello_interval', (YLeaf(YType.uint32, 'hello-interval'), ['int'])),
                        ('propagation_delay', (YLeaf(YType.uint32, 'propagation-delay'), ['int'])),
                        ('dr_priority', (YLeaf(YType.uint32, 'dr-priority'), ['int'])),
                        ('join_prune_mtu', (YLeaf(YType.uint32, 'join-prune-mtu'), ['int'])),
                        ('jp_interval', (YLeaf(YType.uint32, 'jp-interval'), ['int'])),
                        ('override_interval', (YLeaf(YType.uint32, 'override-interval'), ['int'])),
                    ])
                    self.convergence_timeout = None
                    self.hello_interval = None
                    self.propagation_delay = None
                    self.dr_priority = None
                    self.join_prune_mtu = None
                    self.jp_interval = None
                    self.override_interval = None
                    self._segment_path = lambda: "inheritable-defaults"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-pim-cfg:pim/default-context/ipv6/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Pim.DefaultContext.Ipv6.InheritableDefaults, ['convergence_timeout', 'hello_interval', 'propagation_delay', 'dr_priority', 'join_prune_mtu', 'jp_interval', 'override_interval'], name, value)


            class Rpf(Entity):
                """
                Configure RPF options
                
                .. attribute:: route_policy
                
                	Route policy to select RPF topology
                	**type**\: str
                
                	**length:** 1..64
                
                

                """

                _prefix = 'ipv4-pim-cfg'
                _revision = '2017-10-15'

                def __init__(self):
                    super(Pim.DefaultContext.Ipv6.Rpf, self).__init__()

                    self.yang_name = "rpf"
                    self.yang_parent_name = "ipv6"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('route_policy', (YLeaf(YType.str, 'route-policy'), ['str'])),
                    ])
                    self.route_policy = None
                    self._segment_path = lambda: "rpf"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-pim-cfg:pim/default-context/ipv6/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Pim.DefaultContext.Ipv6.Rpf, ['route_policy'], name, value)


            class SgExpiryTimer(Entity):
                """
                Configure expiry timer for S,G routes
                
                .. attribute:: interval
                
                	(S,G) expiry time in seconds
                	**type**\: int
                
                	**range:** 40..57600
                
                	**units**\: second
                
                .. attribute:: access_list_name
                
                	Access\-list of applicable S,G routes
                	**type**\: str
                
                	**length:** 1..64
                
                

                """

                _prefix = 'ipv4-pim-cfg'
                _revision = '2017-10-15'

                def __init__(self):
                    super(Pim.DefaultContext.Ipv6.SgExpiryTimer, self).__init__()

                    self.yang_name = "sg-expiry-timer"
                    self.yang_parent_name = "ipv6"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('interval', (YLeaf(YType.uint32, 'interval'), ['int'])),
                        ('access_list_name', (YLeaf(YType.str, 'access-list-name'), ['str'])),
                    ])
                    self.interval = None
                    self.access_list_name = None
                    self._segment_path = lambda: "sg-expiry-timer"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-pim-cfg:pim/default-context/ipv6/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Pim.DefaultContext.Ipv6.SgExpiryTimer, ['interval', 'access_list_name'], name, value)


            class RpfVectorEnable(Entity):
                """
                Enable PIM RPF Vector Proxy's
                
                .. attribute:: enable
                
                	RPF Vector is turned on if configured
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                	**mandatory**\: True
                
                .. attribute:: allow_ebgp
                
                	Allow RPF Vector origination over eBGP sessions
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: disable_ibgp
                
                	Disable RPF Vector origination over iBGP sessions
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: use_standard_encoding
                
                	Use RPF Vector RFC compliant encoding
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                

                This class is a :ref:`presence class<presence-class>`

                """

                _prefix = 'ipv4-pim-cfg'
                _revision = '2017-10-15'

                def __init__(self):
                    super(Pim.DefaultContext.Ipv6.RpfVectorEnable, self).__init__()

                    self.yang_name = "rpf-vector-enable"
                    self.yang_parent_name = "ipv6"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self.is_presence_container = True
                    self._leafs = OrderedDict([
                        ('enable', (YLeaf(YType.empty, 'enable'), ['Empty'])),
                        ('allow_ebgp', (YLeaf(YType.empty, 'allow-ebgp'), ['Empty'])),
                        ('disable_ibgp', (YLeaf(YType.empty, 'disable-ibgp'), ['Empty'])),
                        ('use_standard_encoding', (YLeaf(YType.empty, 'use-standard-encoding'), ['Empty'])),
                    ])
                    self.enable = None
                    self.allow_ebgp = None
                    self.disable_ibgp = None
                    self.use_standard_encoding = None
                    self._segment_path = lambda: "rpf-vector-enable"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-pim-cfg:pim/default-context/ipv6/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Pim.DefaultContext.Ipv6.RpfVectorEnable, ['enable', 'allow_ebgp', 'disable_ibgp', 'use_standard_encoding'], name, value)


            class Nsf(Entity):
                """
                Configure Non\-stop forwarding (NSF) options
                
                .. attribute:: lifetime
                
                	Override default maximum lifetime for PIM NSF mode
                	**type**\: int
                
                	**range:** 10..600
                
                	**units**\: second
                
                

                """

                _prefix = 'ipv4-pim-cfg'
                _revision = '2017-10-15'

                def __init__(self):
                    super(Pim.DefaultContext.Ipv6.Nsf, self).__init__()

                    self.yang_name = "nsf"
                    self.yang_parent_name = "ipv6"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('lifetime', (YLeaf(YType.uint32, 'lifetime'), ['int'])),
                    ])
                    self.lifetime = None
                    self._segment_path = lambda: "nsf"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-pim-cfg:pim/default-context/ipv6/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Pim.DefaultContext.Ipv6.Nsf, ['lifetime'], name, value)


            class Maximum(Entity):
                """
                Configure PIM State Limits
                
                .. attribute:: bsr_global_group_mappings
                
                	Override default global maximum and threshold for PIM group mapping ranges from BSR
                	**type**\:  :py:class:`BsrGlobalGroupMappings <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.DefaultContext.Ipv6.Maximum.BsrGlobalGroupMappings>`
                
                	**presence node**\: True
                
                .. attribute:: global_routes
                
                	Override default maximum for number of routes
                	**type**\:  :py:class:`GlobalRoutes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.DefaultContext.Ipv6.Maximum.GlobalRoutes>`
                
                	**presence node**\: True
                
                .. attribute:: global_group_mappings_auto_rp
                
                	Maximum for number of group mappings from autorp mapping agent
                	**type**\:  :py:class:`GlobalGroupMappingsAutoRp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.DefaultContext.Ipv6.Maximum.GlobalGroupMappingsAutoRp>`
                
                	**presence node**\: True
                
                .. attribute:: bsr_global_candidate_rp_cache
                
                	Override default global maximum and threshold for C\-RP set in BSR
                	**type**\:  :py:class:`BsrGlobalCandidateRpCache <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.DefaultContext.Ipv6.Maximum.BsrGlobalCandidateRpCache>`
                
                	**presence node**\: True
                
                .. attribute:: global_register_states
                
                	Override default maximum for number of sparse\-mode source registers
                	**type**\:  :py:class:`GlobalRegisterStates <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.DefaultContext.Ipv6.Maximum.GlobalRegisterStates>`
                
                	**presence node**\: True
                
                .. attribute:: global_route_interfaces
                
                	Override default maximum for number of route\-interfaces
                	**type**\:  :py:class:`GlobalRouteInterfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.DefaultContext.Ipv6.Maximum.GlobalRouteInterfaces>`
                
                	**presence node**\: True
                
                .. attribute:: global_low_priority_packet_queue
                
                	Maximum packet queue size in bytes
                	**type**\: int
                
                	**range:** 0..2147483648
                
                	**units**\: byte
                
                .. attribute:: global_high_priority_packet_queue
                
                	Maximum packet queue size in bytes
                	**type**\: int
                
                	**range:** 0..2147483648
                
                	**units**\: byte
                
                .. attribute:: group_mappings_auto_rp
                
                	Override default maximum for number of group mappings from autorp mapping agent
                	**type**\:  :py:class:`GroupMappingsAutoRp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.DefaultContext.Ipv6.Maximum.GroupMappingsAutoRp>`
                
                	**presence node**\: True
                
                .. attribute:: bsr_group_mappings
                
                	Override default maximum and threshold for number of group mappings from BSR
                	**type**\:  :py:class:`BsrGroupMappings <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.DefaultContext.Ipv6.Maximum.BsrGroupMappings>`
                
                	**presence node**\: True
                
                .. attribute:: register_states
                
                	Override default maximum for number of sparse\-mode source registers
                	**type**\:  :py:class:`RegisterStates <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.DefaultContext.Ipv6.Maximum.RegisterStates>`
                
                	**presence node**\: True
                
                .. attribute:: route_interfaces
                
                	Override default maximum for number of route\-interfaces
                	**type**\:  :py:class:`RouteInterfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.DefaultContext.Ipv6.Maximum.RouteInterfaces>`
                
                	**presence node**\: True
                
                .. attribute:: bsr_candidate_rp_cache
                
                	Override default maximum and threshold for BSR C\-RP cache setting
                	**type**\:  :py:class:`BsrCandidateRpCache <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.DefaultContext.Ipv6.Maximum.BsrCandidateRpCache>`
                
                	**presence node**\: True
                
                .. attribute:: routes
                
                	Override default maximum for number of routes
                	**type**\:  :py:class:`Routes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.DefaultContext.Ipv6.Maximum.Routes>`
                
                	**presence node**\: True
                
                

                """

                _prefix = 'ipv4-pim-cfg'
                _revision = '2017-10-15'

                def __init__(self):
                    super(Pim.DefaultContext.Ipv6.Maximum, self).__init__()

                    self.yang_name = "maximum"
                    self.yang_parent_name = "ipv6"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("bsr-global-group-mappings", ("bsr_global_group_mappings", Pim.DefaultContext.Ipv6.Maximum.BsrGlobalGroupMappings)), ("global-routes", ("global_routes", Pim.DefaultContext.Ipv6.Maximum.GlobalRoutes)), ("global-group-mappings-auto-rp", ("global_group_mappings_auto_rp", Pim.DefaultContext.Ipv6.Maximum.GlobalGroupMappingsAutoRp)), ("bsr-global-candidate-rp-cache", ("bsr_global_candidate_rp_cache", Pim.DefaultContext.Ipv6.Maximum.BsrGlobalCandidateRpCache)), ("global-register-states", ("global_register_states", Pim.DefaultContext.Ipv6.Maximum.GlobalRegisterStates)), ("global-route-interfaces", ("global_route_interfaces", Pim.DefaultContext.Ipv6.Maximum.GlobalRouteInterfaces)), ("group-mappings-auto-rp", ("group_mappings_auto_rp", Pim.DefaultContext.Ipv6.Maximum.GroupMappingsAutoRp)), ("bsr-group-mappings", ("bsr_group_mappings", Pim.DefaultContext.Ipv6.Maximum.BsrGroupMappings)), ("register-states", ("register_states", Pim.DefaultContext.Ipv6.Maximum.RegisterStates)), ("route-interfaces", ("route_interfaces", Pim.DefaultContext.Ipv6.Maximum.RouteInterfaces)), ("bsr-candidate-rp-cache", ("bsr_candidate_rp_cache", Pim.DefaultContext.Ipv6.Maximum.BsrCandidateRpCache)), ("routes", ("routes", Pim.DefaultContext.Ipv6.Maximum.Routes))])
                    self._leafs = OrderedDict([
                        ('global_low_priority_packet_queue', (YLeaf(YType.uint32, 'global-low-priority-packet-queue'), ['int'])),
                        ('global_high_priority_packet_queue', (YLeaf(YType.uint32, 'global-high-priority-packet-queue'), ['int'])),
                    ])
                    self.global_low_priority_packet_queue = None
                    self.global_high_priority_packet_queue = None

                    self.bsr_global_group_mappings = None
                    self._children_name_map["bsr_global_group_mappings"] = "bsr-global-group-mappings"

                    self.global_routes = None
                    self._children_name_map["global_routes"] = "global-routes"

                    self.global_group_mappings_auto_rp = None
                    self._children_name_map["global_group_mappings_auto_rp"] = "global-group-mappings-auto-rp"

                    self.bsr_global_candidate_rp_cache = None
                    self._children_name_map["bsr_global_candidate_rp_cache"] = "bsr-global-candidate-rp-cache"

                    self.global_register_states = None
                    self._children_name_map["global_register_states"] = "global-register-states"

                    self.global_route_interfaces = None
                    self._children_name_map["global_route_interfaces"] = "global-route-interfaces"

                    self.group_mappings_auto_rp = None
                    self._children_name_map["group_mappings_auto_rp"] = "group-mappings-auto-rp"

                    self.bsr_group_mappings = None
                    self._children_name_map["bsr_group_mappings"] = "bsr-group-mappings"

                    self.register_states = None
                    self._children_name_map["register_states"] = "register-states"

                    self.route_interfaces = None
                    self._children_name_map["route_interfaces"] = "route-interfaces"

                    self.bsr_candidate_rp_cache = None
                    self._children_name_map["bsr_candidate_rp_cache"] = "bsr-candidate-rp-cache"

                    self.routes = None
                    self._children_name_map["routes"] = "routes"
                    self._segment_path = lambda: "maximum"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-pim-cfg:pim/default-context/ipv6/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Pim.DefaultContext.Ipv6.Maximum, ['global_low_priority_packet_queue', 'global_high_priority_packet_queue'], name, value)


                class BsrGlobalGroupMappings(Entity):
                    """
                    Override default global maximum and threshold
                    for PIM group mapping ranges from BSR
                    
                    .. attribute:: bsr_maximum_global_group_mappings
                    
                    	Global Maximum number of PIM group mapping ranges from BSR
                    	**type**\: int
                    
                    	**range:** 1..10000
                    
                    	**mandatory**\: True
                    
                    .. attribute:: warning_threshold
                    
                    	Set threshold to print warning
                    	**type**\: int
                    
                    	**range:** 1..10000
                    
                    	**default value**\: 500
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'ipv4-pim-cfg'
                    _revision = '2017-10-15'

                    def __init__(self):
                        super(Pim.DefaultContext.Ipv6.Maximum.BsrGlobalGroupMappings, self).__init__()

                        self.yang_name = "bsr-global-group-mappings"
                        self.yang_parent_name = "maximum"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self.is_presence_container = True
                        self._leafs = OrderedDict([
                            ('bsr_maximum_global_group_mappings', (YLeaf(YType.uint32, 'bsr-maximum-global-group-mappings'), ['int'])),
                            ('warning_threshold', (YLeaf(YType.uint32, 'warning-threshold'), ['int'])),
                        ])
                        self.bsr_maximum_global_group_mappings = None
                        self.warning_threshold = None
                        self._segment_path = lambda: "bsr-global-group-mappings"
                        self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-pim-cfg:pim/default-context/ipv6/maximum/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Pim.DefaultContext.Ipv6.Maximum.BsrGlobalGroupMappings, ['bsr_maximum_global_group_mappings', 'warning_threshold'], name, value)


                class GlobalRoutes(Entity):
                    """
                    Override default maximum for number of routes
                    
                    .. attribute:: maximum_routes
                    
                    	Maximum number of PIM routes
                    	**type**\: int
                    
                    	**range:** 1..200000
                    
                    	**mandatory**\: True
                    
                    .. attribute:: warning_threshold
                    
                    	Set threshold to print warning
                    	**type**\: int
                    
                    	**range:** 1..200000
                    
                    	**default value**\: 100000
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'ipv4-pim-cfg'
                    _revision = '2017-10-15'

                    def __init__(self):
                        super(Pim.DefaultContext.Ipv6.Maximum.GlobalRoutes, self).__init__()

                        self.yang_name = "global-routes"
                        self.yang_parent_name = "maximum"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self.is_presence_container = True
                        self._leafs = OrderedDict([
                            ('maximum_routes', (YLeaf(YType.uint32, 'maximum-routes'), ['int'])),
                            ('warning_threshold', (YLeaf(YType.uint32, 'warning-threshold'), ['int'])),
                        ])
                        self.maximum_routes = None
                        self.warning_threshold = None
                        self._segment_path = lambda: "global-routes"
                        self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-pim-cfg:pim/default-context/ipv6/maximum/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Pim.DefaultContext.Ipv6.Maximum.GlobalRoutes, ['maximum_routes', 'warning_threshold'], name, value)


                class GlobalGroupMappingsAutoRp(Entity):
                    """
                    Maximum for number of group mappings from
                    autorp mapping agent
                    
                    .. attribute:: maximum_global_group_ranges_auto_rp
                    
                    	Maximum number of PIM group mappings from autorp
                    	**type**\: int
                    
                    	**range:** 1..10000
                    
                    	**mandatory**\: True
                    
                    .. attribute:: threshold_global_group_ranges_auto_rp
                    
                    	Warning threshold number of PIM group mappings from autorp
                    	**type**\: int
                    
                    	**range:** 1..10000
                    
                    	**default value**\: 450
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'ipv4-pim-cfg'
                    _revision = '2017-10-15'

                    def __init__(self):
                        super(Pim.DefaultContext.Ipv6.Maximum.GlobalGroupMappingsAutoRp, self).__init__()

                        self.yang_name = "global-group-mappings-auto-rp"
                        self.yang_parent_name = "maximum"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self.is_presence_container = True
                        self._leafs = OrderedDict([
                            ('maximum_global_group_ranges_auto_rp', (YLeaf(YType.uint32, 'maximum-global-group-ranges-auto-rp'), ['int'])),
                            ('threshold_global_group_ranges_auto_rp', (YLeaf(YType.uint32, 'threshold-global-group-ranges-auto-rp'), ['int'])),
                        ])
                        self.maximum_global_group_ranges_auto_rp = None
                        self.threshold_global_group_ranges_auto_rp = None
                        self._segment_path = lambda: "global-group-mappings-auto-rp"
                        self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-pim-cfg:pim/default-context/ipv6/maximum/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Pim.DefaultContext.Ipv6.Maximum.GlobalGroupMappingsAutoRp, ['maximum_global_group_ranges_auto_rp', 'threshold_global_group_ranges_auto_rp'], name, value)


                class BsrGlobalCandidateRpCache(Entity):
                    """
                    Override default global maximum and threshold
                    for C\-RP set in BSR
                    
                    .. attribute:: bsr_maximum_global_candidate_rp_cache
                    
                    	Global Maximum number of PIM C\-RP Sets from BSR
                    	**type**\: int
                    
                    	**range:** 1..10000
                    
                    	**mandatory**\: True
                    
                    .. attribute:: warning_threshold
                    
                    	Set threshold to print warning
                    	**type**\: int
                    
                    	**range:** 1..10000
                    
                    	**default value**\: 100
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'ipv4-pim-cfg'
                    _revision = '2017-10-15'

                    def __init__(self):
                        super(Pim.DefaultContext.Ipv6.Maximum.BsrGlobalCandidateRpCache, self).__init__()

                        self.yang_name = "bsr-global-candidate-rp-cache"
                        self.yang_parent_name = "maximum"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self.is_presence_container = True
                        self._leafs = OrderedDict([
                            ('bsr_maximum_global_candidate_rp_cache', (YLeaf(YType.uint32, 'bsr-maximum-global-candidate-rp-cache'), ['int'])),
                            ('warning_threshold', (YLeaf(YType.uint32, 'warning-threshold'), ['int'])),
                        ])
                        self.bsr_maximum_global_candidate_rp_cache = None
                        self.warning_threshold = None
                        self._segment_path = lambda: "bsr-global-candidate-rp-cache"
                        self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-pim-cfg:pim/default-context/ipv6/maximum/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Pim.DefaultContext.Ipv6.Maximum.BsrGlobalCandidateRpCache, ['bsr_maximum_global_candidate_rp_cache', 'warning_threshold'], name, value)


                class GlobalRegisterStates(Entity):
                    """
                    Override default maximum for number of
                    sparse\-mode source registers
                    
                    .. attribute:: maximum_register_states
                    
                    	Maximum number of PIM Sparse\-Mode register states
                    	**type**\: int
                    
                    	**range:** 0..75000
                    
                    	**mandatory**\: True
                    
                    .. attribute:: warning_threshold
                    
                    	Set threshold to print warning
                    	**type**\: int
                    
                    	**range:** 0..75000
                    
                    	**default value**\: 20000
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'ipv4-pim-cfg'
                    _revision = '2017-10-15'

                    def __init__(self):
                        super(Pim.DefaultContext.Ipv6.Maximum.GlobalRegisterStates, self).__init__()

                        self.yang_name = "global-register-states"
                        self.yang_parent_name = "maximum"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self.is_presence_container = True
                        self._leafs = OrderedDict([
                            ('maximum_register_states', (YLeaf(YType.uint32, 'maximum-register-states'), ['int'])),
                            ('warning_threshold', (YLeaf(YType.uint32, 'warning-threshold'), ['int'])),
                        ])
                        self.maximum_register_states = None
                        self.warning_threshold = None
                        self._segment_path = lambda: "global-register-states"
                        self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-pim-cfg:pim/default-context/ipv6/maximum/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Pim.DefaultContext.Ipv6.Maximum.GlobalRegisterStates, ['maximum_register_states', 'warning_threshold'], name, value)


                class GlobalRouteInterfaces(Entity):
                    """
                    Override default maximum for number of
                    route\-interfaces
                    
                    .. attribute:: maximum_route_interfaces
                    
                    	Maximum number of PIM route\-interfaces
                    	**type**\: int
                    
                    	**range:** 1..1100000
                    
                    	**mandatory**\: True
                    
                    .. attribute:: warning_threshold
                    
                    	Set threshold to print warning
                    	**type**\: int
                    
                    	**range:** 1..1100000
                    
                    	**default value**\: 300000
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'ipv4-pim-cfg'
                    _revision = '2017-10-15'

                    def __init__(self):
                        super(Pim.DefaultContext.Ipv6.Maximum.GlobalRouteInterfaces, self).__init__()

                        self.yang_name = "global-route-interfaces"
                        self.yang_parent_name = "maximum"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self.is_presence_container = True
                        self._leafs = OrderedDict([
                            ('maximum_route_interfaces', (YLeaf(YType.uint32, 'maximum-route-interfaces'), ['int'])),
                            ('warning_threshold', (YLeaf(YType.uint32, 'warning-threshold'), ['int'])),
                        ])
                        self.maximum_route_interfaces = None
                        self.warning_threshold = None
                        self._segment_path = lambda: "global-route-interfaces"
                        self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-pim-cfg:pim/default-context/ipv6/maximum/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Pim.DefaultContext.Ipv6.Maximum.GlobalRouteInterfaces, ['maximum_route_interfaces', 'warning_threshold'], name, value)


                class GroupMappingsAutoRp(Entity):
                    """
                    Override default maximum for number of group
                    mappings from autorp mapping agent
                    
                    .. attribute:: maximum_group_ranges_auto_rp
                    
                    	Maximum number of PIM group mappings from autorp
                    	**type**\: int
                    
                    	**range:** 1..10000
                    
                    	**mandatory**\: True
                    
                    .. attribute:: threshold_group_ranges_auto_rp
                    
                    	Warning threshold number of PIM group mappings from autorp
                    	**type**\: int
                    
                    	**range:** 1..10000
                    
                    	**default value**\: 450
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'ipv4-pim-cfg'
                    _revision = '2017-10-15'

                    def __init__(self):
                        super(Pim.DefaultContext.Ipv6.Maximum.GroupMappingsAutoRp, self).__init__()

                        self.yang_name = "group-mappings-auto-rp"
                        self.yang_parent_name = "maximum"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self.is_presence_container = True
                        self._leafs = OrderedDict([
                            ('maximum_group_ranges_auto_rp', (YLeaf(YType.uint32, 'maximum-group-ranges-auto-rp'), ['int'])),
                            ('threshold_group_ranges_auto_rp', (YLeaf(YType.uint32, 'threshold-group-ranges-auto-rp'), ['int'])),
                        ])
                        self.maximum_group_ranges_auto_rp = None
                        self.threshold_group_ranges_auto_rp = None
                        self._segment_path = lambda: "group-mappings-auto-rp"
                        self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-pim-cfg:pim/default-context/ipv6/maximum/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Pim.DefaultContext.Ipv6.Maximum.GroupMappingsAutoRp, ['maximum_group_ranges_auto_rp', 'threshold_group_ranges_auto_rp'], name, value)


                class BsrGroupMappings(Entity):
                    """
                    Override default maximum and threshold for
                    number of group mappings from BSR
                    
                    .. attribute:: bsr_maximum_group_ranges
                    
                    	Maximum number of PIM group mappings from BSR
                    	**type**\: int
                    
                    	**range:** 1..10000
                    
                    	**mandatory**\: True
                    
                    .. attribute:: warning_threshold
                    
                    	Set threshold to print warning
                    	**type**\: int
                    
                    	**range:** 1..10000
                    
                    	**default value**\: 500
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'ipv4-pim-cfg'
                    _revision = '2017-10-15'

                    def __init__(self):
                        super(Pim.DefaultContext.Ipv6.Maximum.BsrGroupMappings, self).__init__()

                        self.yang_name = "bsr-group-mappings"
                        self.yang_parent_name = "maximum"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self.is_presence_container = True
                        self._leafs = OrderedDict([
                            ('bsr_maximum_group_ranges', (YLeaf(YType.uint32, 'bsr-maximum-group-ranges'), ['int'])),
                            ('warning_threshold', (YLeaf(YType.uint32, 'warning-threshold'), ['int'])),
                        ])
                        self.bsr_maximum_group_ranges = None
                        self.warning_threshold = None
                        self._segment_path = lambda: "bsr-group-mappings"
                        self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-pim-cfg:pim/default-context/ipv6/maximum/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Pim.DefaultContext.Ipv6.Maximum.BsrGroupMappings, ['bsr_maximum_group_ranges', 'warning_threshold'], name, value)


                class RegisterStates(Entity):
                    """
                    Override default maximum for number of
                    sparse\-mode source registers
                    
                    .. attribute:: maximum_register_states
                    
                    	Maximum number of PIM Sparse\-Mode register states
                    	**type**\: int
                    
                    	**range:** 0..75000
                    
                    	**mandatory**\: True
                    
                    .. attribute:: warning_threshold
                    
                    	Set threshold to print warning
                    	**type**\: int
                    
                    	**range:** 0..75000
                    
                    	**default value**\: 20000
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'ipv4-pim-cfg'
                    _revision = '2017-10-15'

                    def __init__(self):
                        super(Pim.DefaultContext.Ipv6.Maximum.RegisterStates, self).__init__()

                        self.yang_name = "register-states"
                        self.yang_parent_name = "maximum"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self.is_presence_container = True
                        self._leafs = OrderedDict([
                            ('maximum_register_states', (YLeaf(YType.uint32, 'maximum-register-states'), ['int'])),
                            ('warning_threshold', (YLeaf(YType.uint32, 'warning-threshold'), ['int'])),
                        ])
                        self.maximum_register_states = None
                        self.warning_threshold = None
                        self._segment_path = lambda: "register-states"
                        self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-pim-cfg:pim/default-context/ipv6/maximum/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Pim.DefaultContext.Ipv6.Maximum.RegisterStates, ['maximum_register_states', 'warning_threshold'], name, value)


                class RouteInterfaces(Entity):
                    """
                    Override default maximum for number of
                    route\-interfaces
                    
                    .. attribute:: maximum_route_interfaces
                    
                    	Maximum number of PIM route\-interfaces
                    	**type**\: int
                    
                    	**range:** 1..1100000
                    
                    	**mandatory**\: True
                    
                    .. attribute:: warning_threshold
                    
                    	Set threshold to print warning
                    	**type**\: int
                    
                    	**range:** 1..1100000
                    
                    	**default value**\: 300000
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'ipv4-pim-cfg'
                    _revision = '2017-10-15'

                    def __init__(self):
                        super(Pim.DefaultContext.Ipv6.Maximum.RouteInterfaces, self).__init__()

                        self.yang_name = "route-interfaces"
                        self.yang_parent_name = "maximum"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self.is_presence_container = True
                        self._leafs = OrderedDict([
                            ('maximum_route_interfaces', (YLeaf(YType.uint32, 'maximum-route-interfaces'), ['int'])),
                            ('warning_threshold', (YLeaf(YType.uint32, 'warning-threshold'), ['int'])),
                        ])
                        self.maximum_route_interfaces = None
                        self.warning_threshold = None
                        self._segment_path = lambda: "route-interfaces"
                        self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-pim-cfg:pim/default-context/ipv6/maximum/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Pim.DefaultContext.Ipv6.Maximum.RouteInterfaces, ['maximum_route_interfaces', 'warning_threshold'], name, value)


                class BsrCandidateRpCache(Entity):
                    """
                    Override default maximum and threshold for BSR
                    C\-RP cache setting
                    
                    .. attribute:: bsr_maximum_candidate_rp_cache
                    
                    	Maximum number of BSR C\-RP cache setting
                    	**type**\: int
                    
                    	**range:** 1..10000
                    
                    	**mandatory**\: True
                    
                    .. attribute:: warning_threshold
                    
                    	Set threshold to print warning
                    	**type**\: int
                    
                    	**range:** 1..10000
                    
                    	**default value**\: 100
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'ipv4-pim-cfg'
                    _revision = '2017-10-15'

                    def __init__(self):
                        super(Pim.DefaultContext.Ipv6.Maximum.BsrCandidateRpCache, self).__init__()

                        self.yang_name = "bsr-candidate-rp-cache"
                        self.yang_parent_name = "maximum"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self.is_presence_container = True
                        self._leafs = OrderedDict([
                            ('bsr_maximum_candidate_rp_cache', (YLeaf(YType.uint32, 'bsr-maximum-candidate-rp-cache'), ['int'])),
                            ('warning_threshold', (YLeaf(YType.uint32, 'warning-threshold'), ['int'])),
                        ])
                        self.bsr_maximum_candidate_rp_cache = None
                        self.warning_threshold = None
                        self._segment_path = lambda: "bsr-candidate-rp-cache"
                        self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-pim-cfg:pim/default-context/ipv6/maximum/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Pim.DefaultContext.Ipv6.Maximum.BsrCandidateRpCache, ['bsr_maximum_candidate_rp_cache', 'warning_threshold'], name, value)


                class Routes(Entity):
                    """
                    Override default maximum for number of routes
                    
                    .. attribute:: maximum_routes
                    
                    	Maximum number of PIM routes
                    	**type**\: int
                    
                    	**range:** 1..200000
                    
                    	**mandatory**\: True
                    
                    .. attribute:: warning_threshold
                    
                    	Set threshold to print warning
                    	**type**\: int
                    
                    	**range:** 1..200000
                    
                    	**default value**\: 100000
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'ipv4-pim-cfg'
                    _revision = '2017-10-15'

                    def __init__(self):
                        super(Pim.DefaultContext.Ipv6.Maximum.Routes, self).__init__()

                        self.yang_name = "routes"
                        self.yang_parent_name = "maximum"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self.is_presence_container = True
                        self._leafs = OrderedDict([
                            ('maximum_routes', (YLeaf(YType.uint32, 'maximum-routes'), ['int'])),
                            ('warning_threshold', (YLeaf(YType.uint32, 'warning-threshold'), ['int'])),
                        ])
                        self.maximum_routes = None
                        self.warning_threshold = None
                        self._segment_path = lambda: "routes"
                        self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-pim-cfg:pim/default-context/ipv6/maximum/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Pim.DefaultContext.Ipv6.Maximum.Routes, ['maximum_routes', 'warning_threshold'], name, value)


            class Ssm(Entity):
                """
                Configure IP Multicast SSM
                
                .. attribute:: disable
                
                	TRUE if SSM is disabled on this router
                	**type**\: bool
                
                	**default value**\: false
                
                .. attribute:: range
                
                	Access list of groups enabled with SSM
                	**type**\: str
                
                	**length:** 1..64
                
                

                """

                _prefix = 'ipv4-pim-cfg'
                _revision = '2017-10-15'

                def __init__(self):
                    super(Pim.DefaultContext.Ipv6.Ssm, self).__init__()

                    self.yang_name = "ssm"
                    self.yang_parent_name = "ipv6"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('disable', (YLeaf(YType.boolean, 'disable'), ['bool'])),
                        ('range', (YLeaf(YType.str, 'range'), ['str'])),
                    ])
                    self.disable = None
                    self.range = None
                    self._segment_path = lambda: "ssm"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-pim-cfg:pim/default-context/ipv6/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Pim.DefaultContext.Ipv6.Ssm, ['disable', 'range'], name, value)


            class BidirRpAddresses(Entity):
                """
                Configure Bidirectional PIM Rendezvous Point
                
                .. attribute:: bidir_rp_address
                
                	Address of the Rendezvous Point
                	**type**\: list of  		 :py:class:`BidirRpAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.DefaultContext.Ipv6.BidirRpAddresses.BidirRpAddress>`
                
                

                """

                _prefix = 'ipv4-pim-cfg'
                _revision = '2017-10-15'

                def __init__(self):
                    super(Pim.DefaultContext.Ipv6.BidirRpAddresses, self).__init__()

                    self.yang_name = "bidir-rp-addresses"
                    self.yang_parent_name = "ipv6"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("bidir-rp-address", ("bidir_rp_address", Pim.DefaultContext.Ipv6.BidirRpAddresses.BidirRpAddress))])
                    self._leafs = OrderedDict()

                    self.bidir_rp_address = YList(self)
                    self._segment_path = lambda: "bidir-rp-addresses"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-pim-cfg:pim/default-context/ipv6/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Pim.DefaultContext.Ipv6.BidirRpAddresses, [], name, value)


                class BidirRpAddress(Entity):
                    """
                    Address of the Rendezvous Point
                    
                    .. attribute:: rp_address  (key)
                    
                    	RP address of Rendezvous Point
                    	**type**\: union of the below types:
                    
                    		**type**\: str
                    
                    			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    		**type**\: str
                    
                    			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: access_list_name
                    
                    	Access list of groups that should map to a given RP
                    	**type**\: str
                    
                    	**length:** 1..64
                    
                    .. attribute:: auto_rp_override
                    
                    	TRUE Indicates if static RP config overrides AutoRP and BSR
                    	**type**\: bool
                    
                    

                    """

                    _prefix = 'ipv4-pim-cfg'
                    _revision = '2017-10-15'

                    def __init__(self):
                        super(Pim.DefaultContext.Ipv6.BidirRpAddresses.BidirRpAddress, self).__init__()

                        self.yang_name = "bidir-rp-address"
                        self.yang_parent_name = "bidir-rp-addresses"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['rp_address']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('rp_address', (YLeaf(YType.str, 'rp-address'), ['str','str'])),
                            ('access_list_name', (YLeaf(YType.str, 'access-list-name'), ['str'])),
                            ('auto_rp_override', (YLeaf(YType.boolean, 'auto-rp-override'), ['bool'])),
                        ])
                        self.rp_address = None
                        self.access_list_name = None
                        self.auto_rp_override = None
                        self._segment_path = lambda: "bidir-rp-address" + "[rp-address='" + str(self.rp_address) + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-pim-cfg:pim/default-context/ipv6/bidir-rp-addresses/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Pim.DefaultContext.Ipv6.BidirRpAddresses.BidirRpAddress, ['rp_address', 'access_list_name', 'auto_rp_override'], name, value)


            class Bsr(Entity):
                """
                PIM BSR configuration
                
                .. attribute:: candidate_bsr
                
                	PIM Candidate BSR configuration
                	**type**\:  :py:class:`CandidateBsr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.DefaultContext.Ipv6.Bsr.CandidateBsr>`
                
                	**presence node**\: True
                
                .. attribute:: candidate_rps
                
                	PIM RP configuration
                	**type**\:  :py:class:`CandidateRps <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.DefaultContext.Ipv6.Bsr.CandidateRps>`
                
                

                """

                _prefix = 'ipv4-pim-cfg'
                _revision = '2017-10-15'

                def __init__(self):
                    super(Pim.DefaultContext.Ipv6.Bsr, self).__init__()

                    self.yang_name = "bsr"
                    self.yang_parent_name = "ipv6"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("candidate-bsr", ("candidate_bsr", Pim.DefaultContext.Ipv6.Bsr.CandidateBsr)), ("candidate-rps", ("candidate_rps", Pim.DefaultContext.Ipv6.Bsr.CandidateRps))])
                    self._leafs = OrderedDict()

                    self.candidate_bsr = None
                    self._children_name_map["candidate_bsr"] = "candidate-bsr"

                    self.candidate_rps = Pim.DefaultContext.Ipv6.Bsr.CandidateRps()
                    self.candidate_rps.parent = self
                    self._children_name_map["candidate_rps"] = "candidate-rps"
                    self._segment_path = lambda: "bsr"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-pim-cfg:pim/default-context/ipv6/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Pim.DefaultContext.Ipv6.Bsr, [], name, value)


                class CandidateBsr(Entity):
                    """
                    PIM Candidate BSR configuration
                    
                    .. attribute:: address
                    
                    	BSR Address configured
                    	**type**\: str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    	**mandatory**\: True
                    
                    .. attribute:: prefix_length
                    
                    	Hash Mask Length for this candidate BSR
                    	**type**\: int
                    
                    	**range:** 0..128
                    
                    	**default value**\: 126
                    
                    .. attribute:: priority
                    
                    	Priority of the Candidate BSR
                    	**type**\: int
                    
                    	**range:** 1..255
                    
                    	**default value**\: 1
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'ipv4-pim-cfg'
                    _revision = '2017-10-15'

                    def __init__(self):
                        super(Pim.DefaultContext.Ipv6.Bsr.CandidateBsr, self).__init__()

                        self.yang_name = "candidate-bsr"
                        self.yang_parent_name = "bsr"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self.is_presence_container = True
                        self._leafs = OrderedDict([
                            ('address', (YLeaf(YType.str, 'address'), ['str'])),
                            ('prefix_length', (YLeaf(YType.uint8, 'prefix-length'), ['int'])),
                            ('priority', (YLeaf(YType.uint32, 'priority'), ['int'])),
                        ])
                        self.address = None
                        self.prefix_length = None
                        self.priority = None
                        self._segment_path = lambda: "candidate-bsr"
                        self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-pim-cfg:pim/default-context/ipv6/bsr/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Pim.DefaultContext.Ipv6.Bsr.CandidateBsr, ['address', 'prefix_length', 'priority'], name, value)


                class CandidateRps(Entity):
                    """
                    PIM RP configuration
                    
                    .. attribute:: candidate_rp
                    
                    	Address of PIM SM BSR Candidate\-RP
                    	**type**\: list of  		 :py:class:`CandidateRp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.DefaultContext.Ipv6.Bsr.CandidateRps.CandidateRp>`
                    
                    

                    """

                    _prefix = 'ipv4-pim-cfg'
                    _revision = '2017-10-15'

                    def __init__(self):
                        super(Pim.DefaultContext.Ipv6.Bsr.CandidateRps, self).__init__()

                        self.yang_name = "candidate-rps"
                        self.yang_parent_name = "bsr"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("candidate-rp", ("candidate_rp", Pim.DefaultContext.Ipv6.Bsr.CandidateRps.CandidateRp))])
                        self._leafs = OrderedDict()

                        self.candidate_rp = YList(self)
                        self._segment_path = lambda: "candidate-rps"
                        self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-pim-cfg:pim/default-context/ipv6/bsr/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Pim.DefaultContext.Ipv6.Bsr.CandidateRps, [], name, value)


                    class CandidateRp(Entity):
                        """
                        Address of PIM SM BSR Candidate\-RP
                        
                        .. attribute:: address  (key)
                        
                        	Address of Candidate\-RP
                        	**type**\: union of the below types:
                        
                        		**type**\: str
                        
                        			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        		**type**\: str
                        
                        			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: mode  (key)
                        
                        	SM or Bidir
                        	**type**\:  :py:class:`PimProtocolMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.PimProtocolMode>`
                        
                        .. attribute:: group_list
                        
                        	Access\-list specifying the group range for the Candidate\-RP
                        	**type**\: str
                        
                        	**length:** 1..64
                        
                        .. attribute:: priority
                        
                        	Priority of the CRP
                        	**type**\: int
                        
                        	**range:** 1..255
                        
                        	**default value**\: 192
                        
                        .. attribute:: interval
                        
                        	Advertisement interval
                        	**type**\: int
                        
                        	**range:** 30..600
                        
                        	**default value**\: 60
                        
                        

                        """

                        _prefix = 'ipv4-pim-cfg'
                        _revision = '2017-10-15'

                        def __init__(self):
                            super(Pim.DefaultContext.Ipv6.Bsr.CandidateRps.CandidateRp, self).__init__()

                            self.yang_name = "candidate-rp"
                            self.yang_parent_name = "candidate-rps"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = ['address','mode']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('address', (YLeaf(YType.str, 'address'), ['str','str'])),
                                ('mode', (YLeaf(YType.enumeration, 'mode'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg', 'PimProtocolMode', '')])),
                                ('group_list', (YLeaf(YType.str, 'group-list'), ['str'])),
                                ('priority', (YLeaf(YType.uint32, 'priority'), ['int'])),
                                ('interval', (YLeaf(YType.uint32, 'interval'), ['int'])),
                            ])
                            self.address = None
                            self.mode = None
                            self.group_list = None
                            self.priority = None
                            self.interval = None
                            self._segment_path = lambda: "candidate-rp" + "[address='" + str(self.address) + "']" + "[mode='" + str(self.mode) + "']"
                            self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-pim-cfg:pim/default-context/ipv6/bsr/candidate-rps/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Pim.DefaultContext.Ipv6.Bsr.CandidateRps.CandidateRp, ['address', 'mode', 'group_list', 'priority', 'interval'], name, value)


            class AllowRp(Entity):
                """
                Enable allow\-rp filtering for SM joins
                
                .. attribute:: rp_list_name
                
                	Access\-list specifiying applicable RPs
                	**type**\: str
                
                	**length:** 1..64
                
                .. attribute:: group_list_name
                
                	Access\-list specifiying applicable groups
                	**type**\: str
                
                	**length:** 1..64
                
                

                This class is a :ref:`presence class<presence-class>`

                """

                _prefix = 'ipv4-pim-cfg'
                _revision = '2017-10-15'

                def __init__(self):
                    super(Pim.DefaultContext.Ipv6.AllowRp, self).__init__()

                    self.yang_name = "allow-rp"
                    self.yang_parent_name = "ipv6"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self.is_presence_container = True
                    self._leafs = OrderedDict([
                        ('rp_list_name', (YLeaf(YType.str, 'rp-list-name'), ['str'])),
                        ('group_list_name', (YLeaf(YType.str, 'group-list-name'), ['str'])),
                    ])
                    self.rp_list_name = None
                    self.group_list_name = None
                    self._segment_path = lambda: "allow-rp"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-pim-cfg:pim/default-context/ipv6/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Pim.DefaultContext.Ipv6.AllowRp, ['rp_list_name', 'group_list_name'], name, value)


            class EmbeddedRpAddresses(Entity):
                """
                Set Embedded RP processing support
                
                .. attribute:: embedded_rp_address
                
                	Set Embedded RP processing support
                	**type**\: list of  		 :py:class:`EmbeddedRpAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.DefaultContext.Ipv6.EmbeddedRpAddresses.EmbeddedRpAddress>`
                
                

                """

                _prefix = 'ipv4-pim-cfg'
                _revision = '2017-10-15'

                def __init__(self):
                    super(Pim.DefaultContext.Ipv6.EmbeddedRpAddresses, self).__init__()

                    self.yang_name = "embedded-rp-addresses"
                    self.yang_parent_name = "ipv6"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("embedded-rp-address", ("embedded_rp_address", Pim.DefaultContext.Ipv6.EmbeddedRpAddresses.EmbeddedRpAddress))])
                    self._leafs = OrderedDict()

                    self.embedded_rp_address = YList(self)
                    self._segment_path = lambda: "embedded-rp-addresses"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-pim-cfg:pim/default-context/ipv6/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Pim.DefaultContext.Ipv6.EmbeddedRpAddresses, [], name, value)


                class EmbeddedRpAddress(Entity):
                    """
                    Set Embedded RP processing support
                    
                    .. attribute:: rp_address  (key)
                    
                    	RP address of the Rendezvous Point
                    	**type**\: union of the below types:
                    
                    		**type**\: str
                    
                    			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    		**type**\: str
                    
                    			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: access_list_name
                    
                    	Access list of groups that should map to a given RP
                    	**type**\: str
                    
                    	**length:** 1..64
                    
                    	**mandatory**\: True
                    
                    

                    """

                    _prefix = 'ipv4-pim-cfg'
                    _revision = '2017-10-15'

                    def __init__(self):
                        super(Pim.DefaultContext.Ipv6.EmbeddedRpAddresses.EmbeddedRpAddress, self).__init__()

                        self.yang_name = "embedded-rp-address"
                        self.yang_parent_name = "embedded-rp-addresses"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['rp_address']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('rp_address', (YLeaf(YType.str, 'rp-address'), ['str','str'])),
                            ('access_list_name', (YLeaf(YType.str, 'access-list-name'), ['str'])),
                        ])
                        self.rp_address = None
                        self.access_list_name = None
                        self._segment_path = lambda: "embedded-rp-address" + "[rp-address='" + str(self.rp_address) + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-pim-cfg:pim/default-context/ipv6/embedded-rp-addresses/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Pim.DefaultContext.Ipv6.EmbeddedRpAddresses.EmbeddedRpAddress, ['rp_address', 'access_list_name'], name, value)


            class Convergence(Entity):
                """
                Configure convergence parameters
                
                .. attribute:: rpf_conflict_join_delay
                
                	Dampen first join if RPF path is through one of the downstream neighbor
                	**type**\: int
                
                	**range:** 0..15
                
                	**units**\: second
                
                .. attribute:: link_down_prune_delay
                
                	Delay prunes if route join state transitions to not\-joined on link down
                	**type**\: int
                
                	**range:** 0..60
                
                	**units**\: second
                
                

                """

                _prefix = 'ipv4-pim-cfg'
                _revision = '2017-10-15'

                def __init__(self):
                    super(Pim.DefaultContext.Ipv6.Convergence, self).__init__()

                    self.yang_name = "convergence"
                    self.yang_parent_name = "ipv6"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('rpf_conflict_join_delay', (YLeaf(YType.uint32, 'rpf-conflict-join-delay'), ['int'])),
                        ('link_down_prune_delay', (YLeaf(YType.uint32, 'link-down-prune-delay'), ['int'])),
                    ])
                    self.rpf_conflict_join_delay = None
                    self.link_down_prune_delay = None
                    self._segment_path = lambda: "convergence"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-pim-cfg:pim/default-context/ipv6/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Pim.DefaultContext.Ipv6.Convergence, ['rpf_conflict_join_delay', 'link_down_prune_delay'], name, value)


        class Ipv4(Entity):
            """
            IPV4 commands
            
            .. attribute:: rpf_redirect
            
            	Configure RPF\-redirect feature
            	**type**\:  :py:class:`RpfRedirect <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.DefaultContext.Ipv4.RpfRedirect>`
            
            .. attribute:: interfaces
            
            	Interface\-level Configuration
            	**type**\:  :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.DefaultContext.Ipv4.Interfaces>`
            
            .. attribute:: auto_rp_candidate_rps
            
            	Configure Candidate\-RPs
            	**type**\:  :py:class:`AutoRpCandidateRps <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.DefaultContext.Ipv4.AutoRpCandidateRps>`
            
            .. attribute:: auto_rp_mapping_agent
            
            	Configure AutoRP Mapping Agent
            	**type**\:  :py:class:`AutoRpMappingAgent <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.DefaultContext.Ipv4.AutoRpMappingAgent>`
            
            .. attribute:: neighbor_check_on_receive
            
            	Enable PIM neighbor checking when receiving PIM messages
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: old_register_checksum
            
            	Generate registers compatible with older IOS versions
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: sparse_mode_rp_addresses
            
            	Configure Sparse\-Mode Rendezvous Point
            	**type**\:  :py:class:`SparseModeRpAddresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.DefaultContext.Ipv4.SparseModeRpAddresses>`
            
            .. attribute:: neighbor_filter
            
            	Access\-list of neighbors to be filtered
            	**type**\: str
            
            	**length:** 1..64
            
            .. attribute:: inheritable_defaults
            
            	Inheritable defaults
            	**type**\:  :py:class:`InheritableDefaults <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.DefaultContext.Ipv4.InheritableDefaults>`
            
            .. attribute:: spt_threshold_infinity
            
            	Configure threshold of infinity for switching to SPT on last\-hop
            	**type**\: str
            
            .. attribute:: log_neighbor_changes
            
            	PIM neighbor state change logging is turned on if configured
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: rpf
            
            	Configure RPF options
            	**type**\:  :py:class:`Rpf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.DefaultContext.Ipv4.Rpf>`
            
            .. attribute:: register_source
            
            	Source address to use for register messages
            	**type**\: str
            
            	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
            
            .. attribute:: accept_register
            
            	Access\-list which specifies unauthorized sources
            	**type**\: str
            
            	**length:** 1..64
            
            .. attribute:: sg_expiry_timer
            
            	Configure expiry timer for S,G routes
            	**type**\:  :py:class:`SgExpiryTimer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.DefaultContext.Ipv4.SgExpiryTimer>`
            
            .. attribute:: rpf_vector_enable
            
            	Enable PIM RPF Vector Proxy's
            	**type**\:  :py:class:`RpfVectorEnable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.DefaultContext.Ipv4.RpfVectorEnable>`
            
            	**presence node**\: True
            
            .. attribute:: nsf
            
            	Configure Non\-stop forwarding (NSF) options
            	**type**\:  :py:class:`Nsf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.DefaultContext.Ipv4.Nsf>`
            
            .. attribute:: suppress_rpf_prunes
            
            	Suppress prunes triggered as a result of RPF changes
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: maximum
            
            	Configure PIM State Limits
            	**type**\:  :py:class:`Maximum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.DefaultContext.Ipv4.Maximum>`
            
            .. attribute:: ssm
            
            	Configure IP Multicast SSM
            	**type**\:  :py:class:`Ssm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.DefaultContext.Ipv4.Ssm>`
            
            .. attribute:: injects
            
            	Inject Explicit PIM RPF Vector Proxy's
            	**type**\:  :py:class:`Injects <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.DefaultContext.Ipv4.Injects>`
            
            .. attribute:: bidir_rp_addresses
            
            	Configure Bidirectional PIM Rendezvous Point
            	**type**\:  :py:class:`BidirRpAddresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.DefaultContext.Ipv4.BidirRpAddresses>`
            
            .. attribute:: ssm_allow_override
            
            	Allow SSM ranges to be overridden by more specific ranges
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: bsr
            
            	PIM BSR configuration
            	**type**\:  :py:class:`Bsr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.DefaultContext.Ipv4.Bsr>`
            
            .. attribute:: mofrr
            
            	Multicast Only Fast Re\-Route
            	**type**\:  :py:class:`Mofrr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.DefaultContext.Ipv4.Mofrr>`
            
            .. attribute:: multipath
            
            	Enable equal\-cost multipath routing
            	**type**\:  :py:class:`PimMultipath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.PimMultipath>`
            
            .. attribute:: rp_static_deny
            
            	Configure static RP deny range
            	**type**\: str
            
            	**length:** 1..64
            
            .. attribute:: paths
            
            	Inject PIM RPF Vector Proxy's
            	**type**\:  :py:class:`Paths <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.DefaultContext.Ipv4.Paths>`
            
            .. attribute:: allow_rp
            
            	Enable allow\-rp filtering for SM joins
            	**type**\:  :py:class:`AllowRp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.DefaultContext.Ipv4.AllowRp>`
            
            	**presence node**\: True
            
            .. attribute:: suppress_data_registers
            
            	Suppress data registers after initial state setup
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: neighbor_check_on_send
            
            	Enable PIM neighbor checking when sending join\-prunes
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: convergence
            
            	Configure convergence parameters
            	**type**\:  :py:class:`Convergence <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.DefaultContext.Ipv4.Convergence>`
            
            .. attribute:: auto_rp_disable
            
            	Disable Rendezvous Point discovery through the AutoRP protocol
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'ipv4-pim-cfg'
            _revision = '2017-10-15'

            def __init__(self):
                super(Pim.DefaultContext.Ipv4, self).__init__()

                self.yang_name = "ipv4"
                self.yang_parent_name = "default-context"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("rpf-redirect", ("rpf_redirect", Pim.DefaultContext.Ipv4.RpfRedirect)), ("interfaces", ("interfaces", Pim.DefaultContext.Ipv4.Interfaces)), ("auto-rp-candidate-rps", ("auto_rp_candidate_rps", Pim.DefaultContext.Ipv4.AutoRpCandidateRps)), ("auto-rp-mapping-agent", ("auto_rp_mapping_agent", Pim.DefaultContext.Ipv4.AutoRpMappingAgent)), ("sparse-mode-rp-addresses", ("sparse_mode_rp_addresses", Pim.DefaultContext.Ipv4.SparseModeRpAddresses)), ("inheritable-defaults", ("inheritable_defaults", Pim.DefaultContext.Ipv4.InheritableDefaults)), ("rpf", ("rpf", Pim.DefaultContext.Ipv4.Rpf)), ("sg-expiry-timer", ("sg_expiry_timer", Pim.DefaultContext.Ipv4.SgExpiryTimer)), ("rpf-vector-enable", ("rpf_vector_enable", Pim.DefaultContext.Ipv4.RpfVectorEnable)), ("nsf", ("nsf", Pim.DefaultContext.Ipv4.Nsf)), ("maximum", ("maximum", Pim.DefaultContext.Ipv4.Maximum)), ("ssm", ("ssm", Pim.DefaultContext.Ipv4.Ssm)), ("injects", ("injects", Pim.DefaultContext.Ipv4.Injects)), ("bidir-rp-addresses", ("bidir_rp_addresses", Pim.DefaultContext.Ipv4.BidirRpAddresses)), ("bsr", ("bsr", Pim.DefaultContext.Ipv4.Bsr)), ("mofrr", ("mofrr", Pim.DefaultContext.Ipv4.Mofrr)), ("paths", ("paths", Pim.DefaultContext.Ipv4.Paths)), ("allow-rp", ("allow_rp", Pim.DefaultContext.Ipv4.AllowRp)), ("convergence", ("convergence", Pim.DefaultContext.Ipv4.Convergence))])
                self._leafs = OrderedDict([
                    ('neighbor_check_on_receive', (YLeaf(YType.empty, 'neighbor-check-on-receive'), ['Empty'])),
                    ('old_register_checksum', (YLeaf(YType.empty, 'old-register-checksum'), ['Empty'])),
                    ('neighbor_filter', (YLeaf(YType.str, 'neighbor-filter'), ['str'])),
                    ('spt_threshold_infinity', (YLeaf(YType.str, 'spt-threshold-infinity'), ['str'])),
                    ('log_neighbor_changes', (YLeaf(YType.empty, 'log-neighbor-changes'), ['Empty'])),
                    ('register_source', (YLeaf(YType.str, 'register-source'), ['str'])),
                    ('accept_register', (YLeaf(YType.str, 'accept-register'), ['str'])),
                    ('suppress_rpf_prunes', (YLeaf(YType.empty, 'suppress-rpf-prunes'), ['Empty'])),
                    ('ssm_allow_override', (YLeaf(YType.empty, 'ssm-allow-override'), ['Empty'])),
                    ('multipath', (YLeaf(YType.enumeration, 'multipath'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg', 'PimMultipath', '')])),
                    ('rp_static_deny', (YLeaf(YType.str, 'rp-static-deny'), ['str'])),
                    ('suppress_data_registers', (YLeaf(YType.empty, 'suppress-data-registers'), ['Empty'])),
                    ('neighbor_check_on_send', (YLeaf(YType.empty, 'neighbor-check-on-send'), ['Empty'])),
                    ('auto_rp_disable', (YLeaf(YType.empty, 'auto-rp-disable'), ['Empty'])),
                ])
                self.neighbor_check_on_receive = None
                self.old_register_checksum = None
                self.neighbor_filter = None
                self.spt_threshold_infinity = None
                self.log_neighbor_changes = None
                self.register_source = None
                self.accept_register = None
                self.suppress_rpf_prunes = None
                self.ssm_allow_override = None
                self.multipath = None
                self.rp_static_deny = None
                self.suppress_data_registers = None
                self.neighbor_check_on_send = None
                self.auto_rp_disable = None

                self.rpf_redirect = Pim.DefaultContext.Ipv4.RpfRedirect()
                self.rpf_redirect.parent = self
                self._children_name_map["rpf_redirect"] = "rpf-redirect"

                self.interfaces = Pim.DefaultContext.Ipv4.Interfaces()
                self.interfaces.parent = self
                self._children_name_map["interfaces"] = "interfaces"

                self.auto_rp_candidate_rps = Pim.DefaultContext.Ipv4.AutoRpCandidateRps()
                self.auto_rp_candidate_rps.parent = self
                self._children_name_map["auto_rp_candidate_rps"] = "auto-rp-candidate-rps"

                self.auto_rp_mapping_agent = Pim.DefaultContext.Ipv4.AutoRpMappingAgent()
                self.auto_rp_mapping_agent.parent = self
                self._children_name_map["auto_rp_mapping_agent"] = "auto-rp-mapping-agent"

                self.sparse_mode_rp_addresses = Pim.DefaultContext.Ipv4.SparseModeRpAddresses()
                self.sparse_mode_rp_addresses.parent = self
                self._children_name_map["sparse_mode_rp_addresses"] = "sparse-mode-rp-addresses"

                self.inheritable_defaults = Pim.DefaultContext.Ipv4.InheritableDefaults()
                self.inheritable_defaults.parent = self
                self._children_name_map["inheritable_defaults"] = "inheritable-defaults"

                self.rpf = Pim.DefaultContext.Ipv4.Rpf()
                self.rpf.parent = self
                self._children_name_map["rpf"] = "rpf"

                self.sg_expiry_timer = Pim.DefaultContext.Ipv4.SgExpiryTimer()
                self.sg_expiry_timer.parent = self
                self._children_name_map["sg_expiry_timer"] = "sg-expiry-timer"

                self.rpf_vector_enable = None
                self._children_name_map["rpf_vector_enable"] = "rpf-vector-enable"

                self.nsf = Pim.DefaultContext.Ipv4.Nsf()
                self.nsf.parent = self
                self._children_name_map["nsf"] = "nsf"

                self.maximum = Pim.DefaultContext.Ipv4.Maximum()
                self.maximum.parent = self
                self._children_name_map["maximum"] = "maximum"

                self.ssm = Pim.DefaultContext.Ipv4.Ssm()
                self.ssm.parent = self
                self._children_name_map["ssm"] = "ssm"

                self.injects = Pim.DefaultContext.Ipv4.Injects()
                self.injects.parent = self
                self._children_name_map["injects"] = "injects"

                self.bidir_rp_addresses = Pim.DefaultContext.Ipv4.BidirRpAddresses()
                self.bidir_rp_addresses.parent = self
                self._children_name_map["bidir_rp_addresses"] = "bidir-rp-addresses"

                self.bsr = Pim.DefaultContext.Ipv4.Bsr()
                self.bsr.parent = self
                self._children_name_map["bsr"] = "bsr"

                self.mofrr = Pim.DefaultContext.Ipv4.Mofrr()
                self.mofrr.parent = self
                self._children_name_map["mofrr"] = "mofrr"

                self.paths = Pim.DefaultContext.Ipv4.Paths()
                self.paths.parent = self
                self._children_name_map["paths"] = "paths"

                self.allow_rp = None
                self._children_name_map["allow_rp"] = "allow-rp"

                self.convergence = Pim.DefaultContext.Ipv4.Convergence()
                self.convergence.parent = self
                self._children_name_map["convergence"] = "convergence"
                self._segment_path = lambda: "ipv4"
                self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-pim-cfg:pim/default-context/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Pim.DefaultContext.Ipv4, ['neighbor_check_on_receive', 'old_register_checksum', 'neighbor_filter', 'spt_threshold_infinity', 'log_neighbor_changes', 'register_source', 'accept_register', 'suppress_rpf_prunes', 'ssm_allow_override', 'multipath', 'rp_static_deny', 'suppress_data_registers', 'neighbor_check_on_send', 'auto_rp_disable'], name, value)


            class RpfRedirect(Entity):
                """
                Configure RPF\-redirect feature
                
                .. attribute:: route_policy
                
                	Route policy to select RPF topology
                	**type**\: str
                
                	**length:** 1..64
                
                

                """

                _prefix = 'ipv4-pim-cfg'
                _revision = '2017-10-15'

                def __init__(self):
                    super(Pim.DefaultContext.Ipv4.RpfRedirect, self).__init__()

                    self.yang_name = "rpf-redirect"
                    self.yang_parent_name = "ipv4"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('route_policy', (YLeaf(YType.str, 'route-policy'), ['str'])),
                    ])
                    self.route_policy = None
                    self._segment_path = lambda: "rpf-redirect"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-pim-cfg:pim/default-context/ipv4/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Pim.DefaultContext.Ipv4.RpfRedirect, ['route_policy'], name, value)


            class Interfaces(Entity):
                """
                Interface\-level Configuration
                
                .. attribute:: interface
                
                	The name of the interface
                	**type**\: list of  		 :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.DefaultContext.Ipv4.Interfaces.Interface>`
                
                

                """

                _prefix = 'ipv4-pim-cfg'
                _revision = '2017-10-15'

                def __init__(self):
                    super(Pim.DefaultContext.Ipv4.Interfaces, self).__init__()

                    self.yang_name = "interfaces"
                    self.yang_parent_name = "ipv4"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("interface", ("interface", Pim.DefaultContext.Ipv4.Interfaces.Interface))])
                    self._leafs = OrderedDict()

                    self.interface = YList(self)
                    self._segment_path = lambda: "interfaces"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-pim-cfg:pim/default-context/ipv4/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Pim.DefaultContext.Ipv4.Interfaces, [], name, value)


                class Interface(Entity):
                    """
                    The name of the interface
                    
                    .. attribute:: interface_name  (key)
                    
                    	The name of interface
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                    
                    .. attribute:: redirect_bundle
                    
                    	Configure RPF\-redirect bundle for interface. Applicable for IPv4 only
                    	**type**\:  :py:class:`RedirectBundle <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.DefaultContext.Ipv4.Interfaces.Interface.RedirectBundle>`
                    
                    .. attribute:: enable
                    
                    	Enter PIM Interface processing
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: neighbor_filter
                    
                    	Access\-list of neighbors to be filtered
                    	**type**\: str
                    
                    	**length:** 1..64
                    
                    .. attribute:: hello_interval
                    
                    	Hello interval in seconds
                    	**type**\: int
                    
                    	**range:** 1..3600
                    
                    	**units**\: second
                    
                    .. attribute:: bsr_border
                    
                    	BSR Border configuration for Interface
                    	**type**\: bool
                    
                    .. attribute:: maximum_routes
                    
                    	Maximum number of allowed routes for this interface
                    	**type**\:  :py:class:`MaximumRoutes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.DefaultContext.Ipv4.Interfaces.Interface.MaximumRoutes>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: propagation_delay
                    
                    	Propagation delay in milli seconds
                    	**type**\: int
                    
                    	**range:** 100..32767
                    
                    	**units**\: millisecond
                    
                    .. attribute:: bfd
                    
                    	BFD configuration
                    	**type**\:  :py:class:`Bfd <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.DefaultContext.Ipv4.Interfaces.Interface.Bfd>`
                    
                    .. attribute:: dr_priority
                    
                    	Hello DR priority, preference given to larger value
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: join_prune_mtu
                    
                    	Join\-Prune MTU in Bytes
                    	**type**\: int
                    
                    	**range:** 576..65535
                    
                    	**units**\: byte
                    
                    .. attribute:: interface_enable
                    
                    	Enable PIM processing on the interface
                    	**type**\: bool
                    
                    .. attribute:: jp_interval
                    
                    	Join\-Prune interval in seconds
                    	**type**\: int
                    
                    	**range:** 10..600
                    
                    	**units**\: second
                    
                    .. attribute:: override_interval
                    
                    	Override interval in milliseconds
                    	**type**\: int
                    
                    	**range:** 400..65535
                    
                    	**units**\: millisecond
                    
                    

                    """

                    _prefix = 'ipv4-pim-cfg'
                    _revision = '2017-10-15'

                    def __init__(self):
                        super(Pim.DefaultContext.Ipv4.Interfaces.Interface, self).__init__()

                        self.yang_name = "interface"
                        self.yang_parent_name = "interfaces"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['interface_name']
                        self._child_classes = OrderedDict([("redirect-bundle", ("redirect_bundle", Pim.DefaultContext.Ipv4.Interfaces.Interface.RedirectBundle)), ("maximum-routes", ("maximum_routes", Pim.DefaultContext.Ipv4.Interfaces.Interface.MaximumRoutes)), ("bfd", ("bfd", Pim.DefaultContext.Ipv4.Interfaces.Interface.Bfd))])
                        self._leafs = OrderedDict([
                            ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                            ('enable', (YLeaf(YType.empty, 'enable'), ['Empty'])),
                            ('neighbor_filter', (YLeaf(YType.str, 'neighbor-filter'), ['str'])),
                            ('hello_interval', (YLeaf(YType.uint32, 'hello-interval'), ['int'])),
                            ('bsr_border', (YLeaf(YType.boolean, 'bsr-border'), ['bool'])),
                            ('propagation_delay', (YLeaf(YType.uint32, 'propagation-delay'), ['int'])),
                            ('dr_priority', (YLeaf(YType.uint32, 'dr-priority'), ['int'])),
                            ('join_prune_mtu', (YLeaf(YType.uint32, 'join-prune-mtu'), ['int'])),
                            ('interface_enable', (YLeaf(YType.boolean, 'interface-enable'), ['bool'])),
                            ('jp_interval', (YLeaf(YType.uint32, 'jp-interval'), ['int'])),
                            ('override_interval', (YLeaf(YType.uint32, 'override-interval'), ['int'])),
                        ])
                        self.interface_name = None
                        self.enable = None
                        self.neighbor_filter = None
                        self.hello_interval = None
                        self.bsr_border = None
                        self.propagation_delay = None
                        self.dr_priority = None
                        self.join_prune_mtu = None
                        self.interface_enable = None
                        self.jp_interval = None
                        self.override_interval = None

                        self.redirect_bundle = Pim.DefaultContext.Ipv4.Interfaces.Interface.RedirectBundle()
                        self.redirect_bundle.parent = self
                        self._children_name_map["redirect_bundle"] = "redirect-bundle"

                        self.maximum_routes = None
                        self._children_name_map["maximum_routes"] = "maximum-routes"

                        self.bfd = Pim.DefaultContext.Ipv4.Interfaces.Interface.Bfd()
                        self.bfd.parent = self
                        self._children_name_map["bfd"] = "bfd"
                        self._segment_path = lambda: "interface" + "[interface-name='" + str(self.interface_name) + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-pim-cfg:pim/default-context/ipv4/interfaces/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Pim.DefaultContext.Ipv4.Interfaces.Interface, ['interface_name', 'enable', 'neighbor_filter', 'hello_interval', 'bsr_border', 'propagation_delay', 'dr_priority', 'join_prune_mtu', 'interface_enable', 'jp_interval', 'override_interval'], name, value)


                    class RedirectBundle(Entity):
                        """
                        Configure RPF\-redirect bundle for interface.
                        Applicable for IPv4 only
                        
                        .. attribute:: bundle_name
                        
                        	Bundle name
                        	**type**\: str
                        
                        	**length:** 1..32
                        
                        .. attribute:: interface_bandwidth
                        
                        	Interface bandwidth in Kbps
                        	**type**\: int
                        
                        	**range:** 0..100000000
                        
                        	**units**\: kbit/s
                        
                        .. attribute:: threshold_bandwidth
                        
                        	Threshold bandwidth in Kbps
                        	**type**\: int
                        
                        	**range:** 0..100000000
                        
                        	**units**\: kbit/s
                        
                        

                        """

                        _prefix = 'ipv4-pim-cfg'
                        _revision = '2017-10-15'

                        def __init__(self):
                            super(Pim.DefaultContext.Ipv4.Interfaces.Interface.RedirectBundle, self).__init__()

                            self.yang_name = "redirect-bundle"
                            self.yang_parent_name = "interface"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('bundle_name', (YLeaf(YType.str, 'bundle-name'), ['str'])),
                                ('interface_bandwidth', (YLeaf(YType.uint32, 'interface-bandwidth'), ['int'])),
                                ('threshold_bandwidth', (YLeaf(YType.uint32, 'threshold-bandwidth'), ['int'])),
                            ])
                            self.bundle_name = None
                            self.interface_bandwidth = None
                            self.threshold_bandwidth = None
                            self._segment_path = lambda: "redirect-bundle"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Pim.DefaultContext.Ipv4.Interfaces.Interface.RedirectBundle, ['bundle_name', 'interface_bandwidth', 'threshold_bandwidth'], name, value)


                    class MaximumRoutes(Entity):
                        """
                        Maximum number of allowed routes for this
                        interface
                        
                        .. attribute:: maximum
                        
                        	Maximum number of routes for this interface
                        	**type**\: int
                        
                        	**range:** 1..1100000
                        
                        	**mandatory**\: True
                        
                        .. attribute:: warning_threshold
                        
                        	Set threshold to print warning
                        	**type**\: int
                        
                        	**range:** 1..1100000
                        
                        .. attribute:: access_list_name
                        
                        	Access\-list to account for
                        	**type**\: str
                        
                        	**length:** 1..64
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'ipv4-pim-cfg'
                        _revision = '2017-10-15'

                        def __init__(self):
                            super(Pim.DefaultContext.Ipv4.Interfaces.Interface.MaximumRoutes, self).__init__()

                            self.yang_name = "maximum-routes"
                            self.yang_parent_name = "interface"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self.is_presence_container = True
                            self._leafs = OrderedDict([
                                ('maximum', (YLeaf(YType.uint32, 'maximum'), ['int'])),
                                ('warning_threshold', (YLeaf(YType.uint32, 'warning-threshold'), ['int'])),
                                ('access_list_name', (YLeaf(YType.str, 'access-list-name'), ['str'])),
                            ])
                            self.maximum = None
                            self.warning_threshold = None
                            self.access_list_name = None
                            self._segment_path = lambda: "maximum-routes"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Pim.DefaultContext.Ipv4.Interfaces.Interface.MaximumRoutes, ['maximum', 'warning_threshold', 'access_list_name'], name, value)


                    class Bfd(Entity):
                        """
                        BFD configuration
                        
                        .. attribute:: detection_multiplier
                        
                        	Detection multiplier for BFD sessions created by PIM
                        	**type**\: int
                        
                        	**range:** 2..50
                        
                        .. attribute:: interval
                        
                        	Hello interval for BFD sessions created by PIM
                        	**type**\: int
                        
                        	**range:** 3..30000
                        
                        	**units**\: millisecond
                        
                        .. attribute:: enable
                        
                        	TRUE to enable BFD. FALSE to disable and to prevent inheritance from a parent
                        	**type**\: bool
                        
                        

                        """

                        _prefix = 'ipv4-pim-cfg'
                        _revision = '2017-10-15'

                        def __init__(self):
                            super(Pim.DefaultContext.Ipv4.Interfaces.Interface.Bfd, self).__init__()

                            self.yang_name = "bfd"
                            self.yang_parent_name = "interface"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('detection_multiplier', (YLeaf(YType.uint32, 'detection-multiplier'), ['int'])),
                                ('interval', (YLeaf(YType.uint32, 'interval'), ['int'])),
                                ('enable', (YLeaf(YType.boolean, 'enable'), ['bool'])),
                            ])
                            self.detection_multiplier = None
                            self.interval = None
                            self.enable = None
                            self._segment_path = lambda: "bfd"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Pim.DefaultContext.Ipv4.Interfaces.Interface.Bfd, ['detection_multiplier', 'interval', 'enable'], name, value)


            class AutoRpCandidateRps(Entity):
                """
                Configure Candidate\-RPs
                
                .. attribute:: auto_rp_candidate_rp
                
                	Specifications for a Candidate\-RP
                	**type**\: list of  		 :py:class:`AutoRpCandidateRp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.DefaultContext.Ipv4.AutoRpCandidateRps.AutoRpCandidateRp>`
                
                

                """

                _prefix = 'ipv4-pim-cfg'
                _revision = '2017-10-15'

                def __init__(self):
                    super(Pim.DefaultContext.Ipv4.AutoRpCandidateRps, self).__init__()

                    self.yang_name = "auto-rp-candidate-rps"
                    self.yang_parent_name = "ipv4"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("auto-rp-candidate-rp", ("auto_rp_candidate_rp", Pim.DefaultContext.Ipv4.AutoRpCandidateRps.AutoRpCandidateRp))])
                    self._leafs = OrderedDict()

                    self.auto_rp_candidate_rp = YList(self)
                    self._segment_path = lambda: "auto-rp-candidate-rps"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-pim-cfg:pim/default-context/ipv4/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Pim.DefaultContext.Ipv4.AutoRpCandidateRps, [], name, value)


                class AutoRpCandidateRp(Entity):
                    """
                    Specifications for a Candidate\-RP
                    
                    .. attribute:: interface_name  (key)
                    
                    	Interface from which Candidate\-RP packets will be sourced
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                    
                    .. attribute:: protocol_mode  (key)
                    
                    	Protocol Mode
                    	**type**\:  :py:class:`AutoRpProtocolMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_autorp_datatypes.AutoRpProtocolMode>`
                    
                    .. attribute:: ttl
                    
                    	TTL in Hops
                    	**type**\: int
                    
                    	**range:** 1..255
                    
                    	**mandatory**\: True
                    
                    .. attribute:: access_list_name
                    
                    	Access\-list specifying the group range for the Candidate\-RP
                    	**type**\: str
                    
                    	**length:** 1..64
                    
                    	**default value**\: 224-4
                    
                    .. attribute:: announce_period
                    
                    	Time between announcements <in seconds> 
                    	**type**\: int
                    
                    	**range:** 1..600
                    
                    	**units**\: second
                    
                    	**default value**\: 60
                    
                    

                    """

                    _prefix = 'ipv4-pim-cfg'
                    _revision = '2017-10-15'

                    def __init__(self):
                        super(Pim.DefaultContext.Ipv4.AutoRpCandidateRps.AutoRpCandidateRp, self).__init__()

                        self.yang_name = "auto-rp-candidate-rp"
                        self.yang_parent_name = "auto-rp-candidate-rps"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['interface_name','protocol_mode']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                            ('protocol_mode', (YLeaf(YType.enumeration, 'protocol-mode'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_autorp_datatypes', 'AutoRpProtocolMode', '')])),
                            ('ttl', (YLeaf(YType.uint32, 'ttl'), ['int'])),
                            ('access_list_name', (YLeaf(YType.str, 'access-list-name'), ['str'])),
                            ('announce_period', (YLeaf(YType.uint32, 'announce-period'), ['int'])),
                        ])
                        self.interface_name = None
                        self.protocol_mode = None
                        self.ttl = None
                        self.access_list_name = None
                        self.announce_period = None
                        self._segment_path = lambda: "auto-rp-candidate-rp" + "[interface-name='" + str(self.interface_name) + "']" + "[protocol-mode='" + str(self.protocol_mode) + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-pim-cfg:pim/default-context/ipv4/auto-rp-candidate-rps/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Pim.DefaultContext.Ipv4.AutoRpCandidateRps.AutoRpCandidateRp, ['interface_name', 'protocol_mode', 'ttl', 'access_list_name', 'announce_period'], name, value)


            class AutoRpMappingAgent(Entity):
                """
                Configure AutoRP Mapping Agent
                
                .. attribute:: parameters
                
                	Specifications for Mapping Agent configured on this box
                	**type**\:  :py:class:`Parameters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.DefaultContext.Ipv4.AutoRpMappingAgent.Parameters>`
                
                	**presence node**\: True
                
                .. attribute:: cache_limit
                
                	Mapping Agent cache size limit
                	**type**\:  :py:class:`CacheLimit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.DefaultContext.Ipv4.AutoRpMappingAgent.CacheLimit>`
                
                	**presence node**\: True
                
                

                """

                _prefix = 'ipv4-pim-cfg'
                _revision = '2017-10-15'

                def __init__(self):
                    super(Pim.DefaultContext.Ipv4.AutoRpMappingAgent, self).__init__()

                    self.yang_name = "auto-rp-mapping-agent"
                    self.yang_parent_name = "ipv4"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("parameters", ("parameters", Pim.DefaultContext.Ipv4.AutoRpMappingAgent.Parameters)), ("cache-limit", ("cache_limit", Pim.DefaultContext.Ipv4.AutoRpMappingAgent.CacheLimit))])
                    self._leafs = OrderedDict()

                    self.parameters = None
                    self._children_name_map["parameters"] = "parameters"

                    self.cache_limit = None
                    self._children_name_map["cache_limit"] = "cache-limit"
                    self._segment_path = lambda: "auto-rp-mapping-agent"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-pim-cfg:pim/default-context/ipv4/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Pim.DefaultContext.Ipv4.AutoRpMappingAgent, [], name, value)


                class Parameters(Entity):
                    """
                    Specifications for Mapping Agent configured
                    on this box
                    
                    .. attribute:: interface_name
                    
                    	Interface from which mapping packets will be sourced 
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                    
                    	**mandatory**\: True
                    
                    .. attribute:: ttl
                    
                    	TTL in Hops
                    	**type**\: int
                    
                    	**range:** 1..255
                    
                    	**mandatory**\: True
                    
                    .. attribute:: announce_period
                    
                    	Time between discovery messages <in seconds>
                    	**type**\: int
                    
                    	**range:** 1..600
                    
                    	**units**\: second
                    
                    	**default value**\: 60
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'ipv4-pim-cfg'
                    _revision = '2017-10-15'

                    def __init__(self):
                        super(Pim.DefaultContext.Ipv4.AutoRpMappingAgent.Parameters, self).__init__()

                        self.yang_name = "parameters"
                        self.yang_parent_name = "auto-rp-mapping-agent"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self.is_presence_container = True
                        self._leafs = OrderedDict([
                            ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                            ('ttl', (YLeaf(YType.uint32, 'ttl'), ['int'])),
                            ('announce_period', (YLeaf(YType.uint32, 'announce-period'), ['int'])),
                        ])
                        self.interface_name = None
                        self.ttl = None
                        self.announce_period = None
                        self._segment_path = lambda: "parameters"
                        self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-pim-cfg:pim/default-context/ipv4/auto-rp-mapping-agent/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Pim.DefaultContext.Ipv4.AutoRpMappingAgent.Parameters, ['interface_name', 'ttl', 'announce_period'], name, value)


                class CacheLimit(Entity):
                    """
                    Mapping Agent cache size limit
                    
                    .. attribute:: maximum_cache_entry
                    
                    	Maximum number of mapping cache entries
                    	**type**\: int
                    
                    	**range:** 1..1000
                    
                    	**mandatory**\: True
                    
                    .. attribute:: threshold_cache_entry
                    
                    	Warning threshold number of cache entries
                    	**type**\: int
                    
                    	**range:** 1..1000
                    
                    	**default value**\: 450
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'ipv4-pim-cfg'
                    _revision = '2017-10-15'

                    def __init__(self):
                        super(Pim.DefaultContext.Ipv4.AutoRpMappingAgent.CacheLimit, self).__init__()

                        self.yang_name = "cache-limit"
                        self.yang_parent_name = "auto-rp-mapping-agent"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self.is_presence_container = True
                        self._leafs = OrderedDict([
                            ('maximum_cache_entry', (YLeaf(YType.uint32, 'maximum-cache-entry'), ['int'])),
                            ('threshold_cache_entry', (YLeaf(YType.uint32, 'threshold-cache-entry'), ['int'])),
                        ])
                        self.maximum_cache_entry = None
                        self.threshold_cache_entry = None
                        self._segment_path = lambda: "cache-limit"
                        self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-pim-cfg:pim/default-context/ipv4/auto-rp-mapping-agent/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Pim.DefaultContext.Ipv4.AutoRpMappingAgent.CacheLimit, ['maximum_cache_entry', 'threshold_cache_entry'], name, value)


            class SparseModeRpAddresses(Entity):
                """
                Configure Sparse\-Mode Rendezvous Point
                
                .. attribute:: sparse_mode_rp_address
                
                	Address of the Rendezvous Point
                	**type**\: list of  		 :py:class:`SparseModeRpAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.DefaultContext.Ipv4.SparseModeRpAddresses.SparseModeRpAddress>`
                
                

                """

                _prefix = 'ipv4-pim-cfg'
                _revision = '2017-10-15'

                def __init__(self):
                    super(Pim.DefaultContext.Ipv4.SparseModeRpAddresses, self).__init__()

                    self.yang_name = "sparse-mode-rp-addresses"
                    self.yang_parent_name = "ipv4"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("sparse-mode-rp-address", ("sparse_mode_rp_address", Pim.DefaultContext.Ipv4.SparseModeRpAddresses.SparseModeRpAddress))])
                    self._leafs = OrderedDict()

                    self.sparse_mode_rp_address = YList(self)
                    self._segment_path = lambda: "sparse-mode-rp-addresses"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-pim-cfg:pim/default-context/ipv4/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Pim.DefaultContext.Ipv4.SparseModeRpAddresses, [], name, value)


                class SparseModeRpAddress(Entity):
                    """
                    Address of the Rendezvous Point
                    
                    .. attribute:: rp_address  (key)
                    
                    	RP address of Rendezvous Point
                    	**type**\: union of the below types:
                    
                    		**type**\: str
                    
                    			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    		**type**\: str
                    
                    			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: access_list_name
                    
                    	Access list of groups that should map to a  given RP
                    	**type**\: str
                    
                    	**length:** 1..64
                    
                    .. attribute:: auto_rp_override
                    
                    	TRUE Indicates if static RP config overrides AutoRP and BSR
                    	**type**\: bool
                    
                    

                    """

                    _prefix = 'ipv4-pim-cfg'
                    _revision = '2017-10-15'

                    def __init__(self):
                        super(Pim.DefaultContext.Ipv4.SparseModeRpAddresses.SparseModeRpAddress, self).__init__()

                        self.yang_name = "sparse-mode-rp-address"
                        self.yang_parent_name = "sparse-mode-rp-addresses"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['rp_address']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('rp_address', (YLeaf(YType.str, 'rp-address'), ['str','str'])),
                            ('access_list_name', (YLeaf(YType.str, 'access-list-name'), ['str'])),
                            ('auto_rp_override', (YLeaf(YType.boolean, 'auto-rp-override'), ['bool'])),
                        ])
                        self.rp_address = None
                        self.access_list_name = None
                        self.auto_rp_override = None
                        self._segment_path = lambda: "sparse-mode-rp-address" + "[rp-address='" + str(self.rp_address) + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-pim-cfg:pim/default-context/ipv4/sparse-mode-rp-addresses/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Pim.DefaultContext.Ipv4.SparseModeRpAddresses.SparseModeRpAddress, ['rp_address', 'access_list_name', 'auto_rp_override'], name, value)


            class InheritableDefaults(Entity):
                """
                Inheritable defaults
                
                .. attribute:: convergence_timeout
                
                	Convergency timeout in seconds
                	**type**\: int
                
                	**range:** 1800..2400
                
                	**units**\: second
                
                .. attribute:: hello_interval
                
                	Hello interval in seconds
                	**type**\: int
                
                	**range:** 1..3600
                
                	**units**\: second
                
                .. attribute:: propagation_delay
                
                	Propagation delay in milli seconds
                	**type**\: int
                
                	**range:** 100..32767
                
                	**units**\: millisecond
                
                .. attribute:: dr_priority
                
                	Hello DR priority, preference given to larger value
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: join_prune_mtu
                
                	Join\-Prune MTU in Bytes
                	**type**\: int
                
                	**range:** 576..65535
                
                	**units**\: byte
                
                .. attribute:: jp_interval
                
                	Join\-Prune interval in seconds
                	**type**\: int
                
                	**range:** 10..600
                
                	**units**\: second
                
                .. attribute:: override_interval
                
                	Override interval in milliseconds
                	**type**\: int
                
                	**range:** 400..65535
                
                	**units**\: millisecond
                
                

                """

                _prefix = 'ipv4-pim-cfg'
                _revision = '2017-10-15'

                def __init__(self):
                    super(Pim.DefaultContext.Ipv4.InheritableDefaults, self).__init__()

                    self.yang_name = "inheritable-defaults"
                    self.yang_parent_name = "ipv4"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('convergence_timeout', (YLeaf(YType.uint32, 'convergence-timeout'), ['int'])),
                        ('hello_interval', (YLeaf(YType.uint32, 'hello-interval'), ['int'])),
                        ('propagation_delay', (YLeaf(YType.uint32, 'propagation-delay'), ['int'])),
                        ('dr_priority', (YLeaf(YType.uint32, 'dr-priority'), ['int'])),
                        ('join_prune_mtu', (YLeaf(YType.uint32, 'join-prune-mtu'), ['int'])),
                        ('jp_interval', (YLeaf(YType.uint32, 'jp-interval'), ['int'])),
                        ('override_interval', (YLeaf(YType.uint32, 'override-interval'), ['int'])),
                    ])
                    self.convergence_timeout = None
                    self.hello_interval = None
                    self.propagation_delay = None
                    self.dr_priority = None
                    self.join_prune_mtu = None
                    self.jp_interval = None
                    self.override_interval = None
                    self._segment_path = lambda: "inheritable-defaults"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-pim-cfg:pim/default-context/ipv4/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Pim.DefaultContext.Ipv4.InheritableDefaults, ['convergence_timeout', 'hello_interval', 'propagation_delay', 'dr_priority', 'join_prune_mtu', 'jp_interval', 'override_interval'], name, value)


            class Rpf(Entity):
                """
                Configure RPF options
                
                .. attribute:: route_policy
                
                	Route policy to select RPF topology
                	**type**\: str
                
                	**length:** 1..64
                
                

                """

                _prefix = 'ipv4-pim-cfg'
                _revision = '2017-10-15'

                def __init__(self):
                    super(Pim.DefaultContext.Ipv4.Rpf, self).__init__()

                    self.yang_name = "rpf"
                    self.yang_parent_name = "ipv4"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('route_policy', (YLeaf(YType.str, 'route-policy'), ['str'])),
                    ])
                    self.route_policy = None
                    self._segment_path = lambda: "rpf"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-pim-cfg:pim/default-context/ipv4/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Pim.DefaultContext.Ipv4.Rpf, ['route_policy'], name, value)


            class SgExpiryTimer(Entity):
                """
                Configure expiry timer for S,G routes
                
                .. attribute:: interval
                
                	(S,G) expiry time in seconds
                	**type**\: int
                
                	**range:** 40..57600
                
                	**units**\: second
                
                .. attribute:: access_list_name
                
                	Access\-list of applicable S,G routes
                	**type**\: str
                
                	**length:** 1..64
                
                

                """

                _prefix = 'ipv4-pim-cfg'
                _revision = '2017-10-15'

                def __init__(self):
                    super(Pim.DefaultContext.Ipv4.SgExpiryTimer, self).__init__()

                    self.yang_name = "sg-expiry-timer"
                    self.yang_parent_name = "ipv4"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('interval', (YLeaf(YType.uint32, 'interval'), ['int'])),
                        ('access_list_name', (YLeaf(YType.str, 'access-list-name'), ['str'])),
                    ])
                    self.interval = None
                    self.access_list_name = None
                    self._segment_path = lambda: "sg-expiry-timer"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-pim-cfg:pim/default-context/ipv4/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Pim.DefaultContext.Ipv4.SgExpiryTimer, ['interval', 'access_list_name'], name, value)


            class RpfVectorEnable(Entity):
                """
                Enable PIM RPF Vector Proxy's
                
                .. attribute:: enable
                
                	RPF Vector is turned on if configured
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                	**mandatory**\: True
                
                .. attribute:: allow_ebgp
                
                	Allow RPF Vector origination over eBGP sessions
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: disable_ibgp
                
                	Disable RPF Vector origination over iBGP sessions
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: use_standard_encoding
                
                	Use RPF Vector RFC compliant encoding
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                

                This class is a :ref:`presence class<presence-class>`

                """

                _prefix = 'ipv4-pim-cfg'
                _revision = '2017-10-15'

                def __init__(self):
                    super(Pim.DefaultContext.Ipv4.RpfVectorEnable, self).__init__()

                    self.yang_name = "rpf-vector-enable"
                    self.yang_parent_name = "ipv4"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self.is_presence_container = True
                    self._leafs = OrderedDict([
                        ('enable', (YLeaf(YType.empty, 'enable'), ['Empty'])),
                        ('allow_ebgp', (YLeaf(YType.empty, 'allow-ebgp'), ['Empty'])),
                        ('disable_ibgp', (YLeaf(YType.empty, 'disable-ibgp'), ['Empty'])),
                        ('use_standard_encoding', (YLeaf(YType.empty, 'use-standard-encoding'), ['Empty'])),
                    ])
                    self.enable = None
                    self.allow_ebgp = None
                    self.disable_ibgp = None
                    self.use_standard_encoding = None
                    self._segment_path = lambda: "rpf-vector-enable"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-pim-cfg:pim/default-context/ipv4/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Pim.DefaultContext.Ipv4.RpfVectorEnable, ['enable', 'allow_ebgp', 'disable_ibgp', 'use_standard_encoding'], name, value)


            class Nsf(Entity):
                """
                Configure Non\-stop forwarding (NSF) options
                
                .. attribute:: lifetime
                
                	Override default maximum lifetime for PIM NSF mode
                	**type**\: int
                
                	**range:** 10..600
                
                	**units**\: second
                
                

                """

                _prefix = 'ipv4-pim-cfg'
                _revision = '2017-10-15'

                def __init__(self):
                    super(Pim.DefaultContext.Ipv4.Nsf, self).__init__()

                    self.yang_name = "nsf"
                    self.yang_parent_name = "ipv4"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('lifetime', (YLeaf(YType.uint32, 'lifetime'), ['int'])),
                    ])
                    self.lifetime = None
                    self._segment_path = lambda: "nsf"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-pim-cfg:pim/default-context/ipv4/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Pim.DefaultContext.Ipv4.Nsf, ['lifetime'], name, value)


            class Maximum(Entity):
                """
                Configure PIM State Limits
                
                .. attribute:: bsr_global_group_mappings
                
                	Override default global maximum and threshold for PIM group mapping ranges from BSR
                	**type**\:  :py:class:`BsrGlobalGroupMappings <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.DefaultContext.Ipv4.Maximum.BsrGlobalGroupMappings>`
                
                	**presence node**\: True
                
                .. attribute:: global_routes
                
                	Override default maximum for number of routes
                	**type**\:  :py:class:`GlobalRoutes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.DefaultContext.Ipv4.Maximum.GlobalRoutes>`
                
                	**presence node**\: True
                
                .. attribute:: global_group_mappings_auto_rp
                
                	Maximum for number of group mappings from autorp mapping agent
                	**type**\:  :py:class:`GlobalGroupMappingsAutoRp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.DefaultContext.Ipv4.Maximum.GlobalGroupMappingsAutoRp>`
                
                	**presence node**\: True
                
                .. attribute:: bsr_global_candidate_rp_cache
                
                	Override default global maximum and threshold for C\-RP set in BSR
                	**type**\:  :py:class:`BsrGlobalCandidateRpCache <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.DefaultContext.Ipv4.Maximum.BsrGlobalCandidateRpCache>`
                
                	**presence node**\: True
                
                .. attribute:: global_register_states
                
                	Override default maximum for number of sparse\-mode source registers
                	**type**\:  :py:class:`GlobalRegisterStates <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.DefaultContext.Ipv4.Maximum.GlobalRegisterStates>`
                
                	**presence node**\: True
                
                .. attribute:: global_route_interfaces
                
                	Override default maximum for number of route\-interfaces
                	**type**\:  :py:class:`GlobalRouteInterfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.DefaultContext.Ipv4.Maximum.GlobalRouteInterfaces>`
                
                	**presence node**\: True
                
                .. attribute:: global_low_priority_packet_queue
                
                	Maximum packet queue size in bytes
                	**type**\: int
                
                	**range:** 0..2147483648
                
                	**units**\: byte
                
                .. attribute:: global_high_priority_packet_queue
                
                	Maximum packet queue size in bytes
                	**type**\: int
                
                	**range:** 0..2147483648
                
                	**units**\: byte
                
                .. attribute:: group_mappings_auto_rp
                
                	Override default maximum for number of group mappings from autorp mapping agent
                	**type**\:  :py:class:`GroupMappingsAutoRp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.DefaultContext.Ipv4.Maximum.GroupMappingsAutoRp>`
                
                	**presence node**\: True
                
                .. attribute:: bsr_group_mappings
                
                	Override default maximum and threshold for number of group mappings from BSR
                	**type**\:  :py:class:`BsrGroupMappings <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.DefaultContext.Ipv4.Maximum.BsrGroupMappings>`
                
                	**presence node**\: True
                
                .. attribute:: register_states
                
                	Override default maximum for number of sparse\-mode source registers
                	**type**\:  :py:class:`RegisterStates <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.DefaultContext.Ipv4.Maximum.RegisterStates>`
                
                	**presence node**\: True
                
                .. attribute:: route_interfaces
                
                	Override default maximum for number of route\-interfaces
                	**type**\:  :py:class:`RouteInterfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.DefaultContext.Ipv4.Maximum.RouteInterfaces>`
                
                	**presence node**\: True
                
                .. attribute:: bsr_candidate_rp_cache
                
                	Override default maximum and threshold for BSR C\-RP cache setting
                	**type**\:  :py:class:`BsrCandidateRpCache <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.DefaultContext.Ipv4.Maximum.BsrCandidateRpCache>`
                
                	**presence node**\: True
                
                .. attribute:: routes
                
                	Override default maximum for number of routes
                	**type**\:  :py:class:`Routes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.DefaultContext.Ipv4.Maximum.Routes>`
                
                	**presence node**\: True
                
                

                """

                _prefix = 'ipv4-pim-cfg'
                _revision = '2017-10-15'

                def __init__(self):
                    super(Pim.DefaultContext.Ipv4.Maximum, self).__init__()

                    self.yang_name = "maximum"
                    self.yang_parent_name = "ipv4"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("bsr-global-group-mappings", ("bsr_global_group_mappings", Pim.DefaultContext.Ipv4.Maximum.BsrGlobalGroupMappings)), ("global-routes", ("global_routes", Pim.DefaultContext.Ipv4.Maximum.GlobalRoutes)), ("global-group-mappings-auto-rp", ("global_group_mappings_auto_rp", Pim.DefaultContext.Ipv4.Maximum.GlobalGroupMappingsAutoRp)), ("bsr-global-candidate-rp-cache", ("bsr_global_candidate_rp_cache", Pim.DefaultContext.Ipv4.Maximum.BsrGlobalCandidateRpCache)), ("global-register-states", ("global_register_states", Pim.DefaultContext.Ipv4.Maximum.GlobalRegisterStates)), ("global-route-interfaces", ("global_route_interfaces", Pim.DefaultContext.Ipv4.Maximum.GlobalRouteInterfaces)), ("group-mappings-auto-rp", ("group_mappings_auto_rp", Pim.DefaultContext.Ipv4.Maximum.GroupMappingsAutoRp)), ("bsr-group-mappings", ("bsr_group_mappings", Pim.DefaultContext.Ipv4.Maximum.BsrGroupMappings)), ("register-states", ("register_states", Pim.DefaultContext.Ipv4.Maximum.RegisterStates)), ("route-interfaces", ("route_interfaces", Pim.DefaultContext.Ipv4.Maximum.RouteInterfaces)), ("bsr-candidate-rp-cache", ("bsr_candidate_rp_cache", Pim.DefaultContext.Ipv4.Maximum.BsrCandidateRpCache)), ("routes", ("routes", Pim.DefaultContext.Ipv4.Maximum.Routes))])
                    self._leafs = OrderedDict([
                        ('global_low_priority_packet_queue', (YLeaf(YType.uint32, 'global-low-priority-packet-queue'), ['int'])),
                        ('global_high_priority_packet_queue', (YLeaf(YType.uint32, 'global-high-priority-packet-queue'), ['int'])),
                    ])
                    self.global_low_priority_packet_queue = None
                    self.global_high_priority_packet_queue = None

                    self.bsr_global_group_mappings = None
                    self._children_name_map["bsr_global_group_mappings"] = "bsr-global-group-mappings"

                    self.global_routes = None
                    self._children_name_map["global_routes"] = "global-routes"

                    self.global_group_mappings_auto_rp = None
                    self._children_name_map["global_group_mappings_auto_rp"] = "global-group-mappings-auto-rp"

                    self.bsr_global_candidate_rp_cache = None
                    self._children_name_map["bsr_global_candidate_rp_cache"] = "bsr-global-candidate-rp-cache"

                    self.global_register_states = None
                    self._children_name_map["global_register_states"] = "global-register-states"

                    self.global_route_interfaces = None
                    self._children_name_map["global_route_interfaces"] = "global-route-interfaces"

                    self.group_mappings_auto_rp = None
                    self._children_name_map["group_mappings_auto_rp"] = "group-mappings-auto-rp"

                    self.bsr_group_mappings = None
                    self._children_name_map["bsr_group_mappings"] = "bsr-group-mappings"

                    self.register_states = None
                    self._children_name_map["register_states"] = "register-states"

                    self.route_interfaces = None
                    self._children_name_map["route_interfaces"] = "route-interfaces"

                    self.bsr_candidate_rp_cache = None
                    self._children_name_map["bsr_candidate_rp_cache"] = "bsr-candidate-rp-cache"

                    self.routes = None
                    self._children_name_map["routes"] = "routes"
                    self._segment_path = lambda: "maximum"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-pim-cfg:pim/default-context/ipv4/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Pim.DefaultContext.Ipv4.Maximum, ['global_low_priority_packet_queue', 'global_high_priority_packet_queue'], name, value)


                class BsrGlobalGroupMappings(Entity):
                    """
                    Override default global maximum and threshold
                    for PIM group mapping ranges from BSR
                    
                    .. attribute:: bsr_maximum_global_group_mappings
                    
                    	Global Maximum number of PIM group mapping ranges from BSR
                    	**type**\: int
                    
                    	**range:** 1..10000
                    
                    	**mandatory**\: True
                    
                    .. attribute:: warning_threshold
                    
                    	Set threshold to print warning
                    	**type**\: int
                    
                    	**range:** 1..10000
                    
                    	**default value**\: 500
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'ipv4-pim-cfg'
                    _revision = '2017-10-15'

                    def __init__(self):
                        super(Pim.DefaultContext.Ipv4.Maximum.BsrGlobalGroupMappings, self).__init__()

                        self.yang_name = "bsr-global-group-mappings"
                        self.yang_parent_name = "maximum"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self.is_presence_container = True
                        self._leafs = OrderedDict([
                            ('bsr_maximum_global_group_mappings', (YLeaf(YType.uint32, 'bsr-maximum-global-group-mappings'), ['int'])),
                            ('warning_threshold', (YLeaf(YType.uint32, 'warning-threshold'), ['int'])),
                        ])
                        self.bsr_maximum_global_group_mappings = None
                        self.warning_threshold = None
                        self._segment_path = lambda: "bsr-global-group-mappings"
                        self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-pim-cfg:pim/default-context/ipv4/maximum/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Pim.DefaultContext.Ipv4.Maximum.BsrGlobalGroupMappings, ['bsr_maximum_global_group_mappings', 'warning_threshold'], name, value)


                class GlobalRoutes(Entity):
                    """
                    Override default maximum for number of routes
                    
                    .. attribute:: maximum_routes
                    
                    	Maximum number of PIM routes
                    	**type**\: int
                    
                    	**range:** 1..200000
                    
                    	**mandatory**\: True
                    
                    .. attribute:: warning_threshold
                    
                    	Set threshold to print warning
                    	**type**\: int
                    
                    	**range:** 1..200000
                    
                    	**default value**\: 100000
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'ipv4-pim-cfg'
                    _revision = '2017-10-15'

                    def __init__(self):
                        super(Pim.DefaultContext.Ipv4.Maximum.GlobalRoutes, self).__init__()

                        self.yang_name = "global-routes"
                        self.yang_parent_name = "maximum"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self.is_presence_container = True
                        self._leafs = OrderedDict([
                            ('maximum_routes', (YLeaf(YType.uint32, 'maximum-routes'), ['int'])),
                            ('warning_threshold', (YLeaf(YType.uint32, 'warning-threshold'), ['int'])),
                        ])
                        self.maximum_routes = None
                        self.warning_threshold = None
                        self._segment_path = lambda: "global-routes"
                        self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-pim-cfg:pim/default-context/ipv4/maximum/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Pim.DefaultContext.Ipv4.Maximum.GlobalRoutes, ['maximum_routes', 'warning_threshold'], name, value)


                class GlobalGroupMappingsAutoRp(Entity):
                    """
                    Maximum for number of group mappings from
                    autorp mapping agent
                    
                    .. attribute:: maximum_global_group_ranges_auto_rp
                    
                    	Maximum number of PIM group mappings from autorp
                    	**type**\: int
                    
                    	**range:** 1..10000
                    
                    	**mandatory**\: True
                    
                    .. attribute:: threshold_global_group_ranges_auto_rp
                    
                    	Warning threshold number of PIM group mappings from autorp
                    	**type**\: int
                    
                    	**range:** 1..10000
                    
                    	**default value**\: 450
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'ipv4-pim-cfg'
                    _revision = '2017-10-15'

                    def __init__(self):
                        super(Pim.DefaultContext.Ipv4.Maximum.GlobalGroupMappingsAutoRp, self).__init__()

                        self.yang_name = "global-group-mappings-auto-rp"
                        self.yang_parent_name = "maximum"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self.is_presence_container = True
                        self._leafs = OrderedDict([
                            ('maximum_global_group_ranges_auto_rp', (YLeaf(YType.uint32, 'maximum-global-group-ranges-auto-rp'), ['int'])),
                            ('threshold_global_group_ranges_auto_rp', (YLeaf(YType.uint32, 'threshold-global-group-ranges-auto-rp'), ['int'])),
                        ])
                        self.maximum_global_group_ranges_auto_rp = None
                        self.threshold_global_group_ranges_auto_rp = None
                        self._segment_path = lambda: "global-group-mappings-auto-rp"
                        self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-pim-cfg:pim/default-context/ipv4/maximum/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Pim.DefaultContext.Ipv4.Maximum.GlobalGroupMappingsAutoRp, ['maximum_global_group_ranges_auto_rp', 'threshold_global_group_ranges_auto_rp'], name, value)


                class BsrGlobalCandidateRpCache(Entity):
                    """
                    Override default global maximum and threshold
                    for C\-RP set in BSR
                    
                    .. attribute:: bsr_maximum_global_candidate_rp_cache
                    
                    	Global Maximum number of PIM C\-RP Sets from BSR
                    	**type**\: int
                    
                    	**range:** 1..10000
                    
                    	**mandatory**\: True
                    
                    .. attribute:: warning_threshold
                    
                    	Set threshold to print warning
                    	**type**\: int
                    
                    	**range:** 1..10000
                    
                    	**default value**\: 100
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'ipv4-pim-cfg'
                    _revision = '2017-10-15'

                    def __init__(self):
                        super(Pim.DefaultContext.Ipv4.Maximum.BsrGlobalCandidateRpCache, self).__init__()

                        self.yang_name = "bsr-global-candidate-rp-cache"
                        self.yang_parent_name = "maximum"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self.is_presence_container = True
                        self._leafs = OrderedDict([
                            ('bsr_maximum_global_candidate_rp_cache', (YLeaf(YType.uint32, 'bsr-maximum-global-candidate-rp-cache'), ['int'])),
                            ('warning_threshold', (YLeaf(YType.uint32, 'warning-threshold'), ['int'])),
                        ])
                        self.bsr_maximum_global_candidate_rp_cache = None
                        self.warning_threshold = None
                        self._segment_path = lambda: "bsr-global-candidate-rp-cache"
                        self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-pim-cfg:pim/default-context/ipv4/maximum/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Pim.DefaultContext.Ipv4.Maximum.BsrGlobalCandidateRpCache, ['bsr_maximum_global_candidate_rp_cache', 'warning_threshold'], name, value)


                class GlobalRegisterStates(Entity):
                    """
                    Override default maximum for number of
                    sparse\-mode source registers
                    
                    .. attribute:: maximum_register_states
                    
                    	Maximum number of PIM Sparse\-Mode register states
                    	**type**\: int
                    
                    	**range:** 0..75000
                    
                    	**mandatory**\: True
                    
                    .. attribute:: warning_threshold
                    
                    	Set threshold to print warning
                    	**type**\: int
                    
                    	**range:** 0..75000
                    
                    	**default value**\: 20000
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'ipv4-pim-cfg'
                    _revision = '2017-10-15'

                    def __init__(self):
                        super(Pim.DefaultContext.Ipv4.Maximum.GlobalRegisterStates, self).__init__()

                        self.yang_name = "global-register-states"
                        self.yang_parent_name = "maximum"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self.is_presence_container = True
                        self._leafs = OrderedDict([
                            ('maximum_register_states', (YLeaf(YType.uint32, 'maximum-register-states'), ['int'])),
                            ('warning_threshold', (YLeaf(YType.uint32, 'warning-threshold'), ['int'])),
                        ])
                        self.maximum_register_states = None
                        self.warning_threshold = None
                        self._segment_path = lambda: "global-register-states"
                        self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-pim-cfg:pim/default-context/ipv4/maximum/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Pim.DefaultContext.Ipv4.Maximum.GlobalRegisterStates, ['maximum_register_states', 'warning_threshold'], name, value)


                class GlobalRouteInterfaces(Entity):
                    """
                    Override default maximum for number of
                    route\-interfaces
                    
                    .. attribute:: maximum_route_interfaces
                    
                    	Maximum number of PIM route\-interfaces
                    	**type**\: int
                    
                    	**range:** 1..1100000
                    
                    	**mandatory**\: True
                    
                    .. attribute:: warning_threshold
                    
                    	Set threshold to print warning
                    	**type**\: int
                    
                    	**range:** 1..1100000
                    
                    	**default value**\: 300000
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'ipv4-pim-cfg'
                    _revision = '2017-10-15'

                    def __init__(self):
                        super(Pim.DefaultContext.Ipv4.Maximum.GlobalRouteInterfaces, self).__init__()

                        self.yang_name = "global-route-interfaces"
                        self.yang_parent_name = "maximum"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self.is_presence_container = True
                        self._leafs = OrderedDict([
                            ('maximum_route_interfaces', (YLeaf(YType.uint32, 'maximum-route-interfaces'), ['int'])),
                            ('warning_threshold', (YLeaf(YType.uint32, 'warning-threshold'), ['int'])),
                        ])
                        self.maximum_route_interfaces = None
                        self.warning_threshold = None
                        self._segment_path = lambda: "global-route-interfaces"
                        self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-pim-cfg:pim/default-context/ipv4/maximum/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Pim.DefaultContext.Ipv4.Maximum.GlobalRouteInterfaces, ['maximum_route_interfaces', 'warning_threshold'], name, value)


                class GroupMappingsAutoRp(Entity):
                    """
                    Override default maximum for number of group
                    mappings from autorp mapping agent
                    
                    .. attribute:: maximum_group_ranges_auto_rp
                    
                    	Maximum number of PIM group mappings from autorp
                    	**type**\: int
                    
                    	**range:** 1..10000
                    
                    	**mandatory**\: True
                    
                    .. attribute:: threshold_group_ranges_auto_rp
                    
                    	Warning threshold number of PIM group mappings from autorp
                    	**type**\: int
                    
                    	**range:** 1..10000
                    
                    	**default value**\: 450
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'ipv4-pim-cfg'
                    _revision = '2017-10-15'

                    def __init__(self):
                        super(Pim.DefaultContext.Ipv4.Maximum.GroupMappingsAutoRp, self).__init__()

                        self.yang_name = "group-mappings-auto-rp"
                        self.yang_parent_name = "maximum"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self.is_presence_container = True
                        self._leafs = OrderedDict([
                            ('maximum_group_ranges_auto_rp', (YLeaf(YType.uint32, 'maximum-group-ranges-auto-rp'), ['int'])),
                            ('threshold_group_ranges_auto_rp', (YLeaf(YType.uint32, 'threshold-group-ranges-auto-rp'), ['int'])),
                        ])
                        self.maximum_group_ranges_auto_rp = None
                        self.threshold_group_ranges_auto_rp = None
                        self._segment_path = lambda: "group-mappings-auto-rp"
                        self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-pim-cfg:pim/default-context/ipv4/maximum/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Pim.DefaultContext.Ipv4.Maximum.GroupMappingsAutoRp, ['maximum_group_ranges_auto_rp', 'threshold_group_ranges_auto_rp'], name, value)


                class BsrGroupMappings(Entity):
                    """
                    Override default maximum and threshold for
                    number of group mappings from BSR
                    
                    .. attribute:: bsr_maximum_group_ranges
                    
                    	Maximum number of PIM group mappings from BSR
                    	**type**\: int
                    
                    	**range:** 1..10000
                    
                    	**mandatory**\: True
                    
                    .. attribute:: warning_threshold
                    
                    	Set threshold to print warning
                    	**type**\: int
                    
                    	**range:** 1..10000
                    
                    	**default value**\: 500
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'ipv4-pim-cfg'
                    _revision = '2017-10-15'

                    def __init__(self):
                        super(Pim.DefaultContext.Ipv4.Maximum.BsrGroupMappings, self).__init__()

                        self.yang_name = "bsr-group-mappings"
                        self.yang_parent_name = "maximum"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self.is_presence_container = True
                        self._leafs = OrderedDict([
                            ('bsr_maximum_group_ranges', (YLeaf(YType.uint32, 'bsr-maximum-group-ranges'), ['int'])),
                            ('warning_threshold', (YLeaf(YType.uint32, 'warning-threshold'), ['int'])),
                        ])
                        self.bsr_maximum_group_ranges = None
                        self.warning_threshold = None
                        self._segment_path = lambda: "bsr-group-mappings"
                        self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-pim-cfg:pim/default-context/ipv4/maximum/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Pim.DefaultContext.Ipv4.Maximum.BsrGroupMappings, ['bsr_maximum_group_ranges', 'warning_threshold'], name, value)


                class RegisterStates(Entity):
                    """
                    Override default maximum for number of
                    sparse\-mode source registers
                    
                    .. attribute:: maximum_register_states
                    
                    	Maximum number of PIM Sparse\-Mode register states
                    	**type**\: int
                    
                    	**range:** 0..75000
                    
                    	**mandatory**\: True
                    
                    .. attribute:: warning_threshold
                    
                    	Set threshold to print warning
                    	**type**\: int
                    
                    	**range:** 0..75000
                    
                    	**default value**\: 20000
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'ipv4-pim-cfg'
                    _revision = '2017-10-15'

                    def __init__(self):
                        super(Pim.DefaultContext.Ipv4.Maximum.RegisterStates, self).__init__()

                        self.yang_name = "register-states"
                        self.yang_parent_name = "maximum"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self.is_presence_container = True
                        self._leafs = OrderedDict([
                            ('maximum_register_states', (YLeaf(YType.uint32, 'maximum-register-states'), ['int'])),
                            ('warning_threshold', (YLeaf(YType.uint32, 'warning-threshold'), ['int'])),
                        ])
                        self.maximum_register_states = None
                        self.warning_threshold = None
                        self._segment_path = lambda: "register-states"
                        self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-pim-cfg:pim/default-context/ipv4/maximum/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Pim.DefaultContext.Ipv4.Maximum.RegisterStates, ['maximum_register_states', 'warning_threshold'], name, value)


                class RouteInterfaces(Entity):
                    """
                    Override default maximum for number of
                    route\-interfaces
                    
                    .. attribute:: maximum_route_interfaces
                    
                    	Maximum number of PIM route\-interfaces
                    	**type**\: int
                    
                    	**range:** 1..1100000
                    
                    	**mandatory**\: True
                    
                    .. attribute:: warning_threshold
                    
                    	Set threshold to print warning
                    	**type**\: int
                    
                    	**range:** 1..1100000
                    
                    	**default value**\: 300000
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'ipv4-pim-cfg'
                    _revision = '2017-10-15'

                    def __init__(self):
                        super(Pim.DefaultContext.Ipv4.Maximum.RouteInterfaces, self).__init__()

                        self.yang_name = "route-interfaces"
                        self.yang_parent_name = "maximum"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self.is_presence_container = True
                        self._leafs = OrderedDict([
                            ('maximum_route_interfaces', (YLeaf(YType.uint32, 'maximum-route-interfaces'), ['int'])),
                            ('warning_threshold', (YLeaf(YType.uint32, 'warning-threshold'), ['int'])),
                        ])
                        self.maximum_route_interfaces = None
                        self.warning_threshold = None
                        self._segment_path = lambda: "route-interfaces"
                        self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-pim-cfg:pim/default-context/ipv4/maximum/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Pim.DefaultContext.Ipv4.Maximum.RouteInterfaces, ['maximum_route_interfaces', 'warning_threshold'], name, value)


                class BsrCandidateRpCache(Entity):
                    """
                    Override default maximum and threshold for BSR
                    C\-RP cache setting
                    
                    .. attribute:: bsr_maximum_candidate_rp_cache
                    
                    	Maximum number of BSR C\-RP cache setting
                    	**type**\: int
                    
                    	**range:** 1..10000
                    
                    	**mandatory**\: True
                    
                    .. attribute:: warning_threshold
                    
                    	Set threshold to print warning
                    	**type**\: int
                    
                    	**range:** 1..10000
                    
                    	**default value**\: 100
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'ipv4-pim-cfg'
                    _revision = '2017-10-15'

                    def __init__(self):
                        super(Pim.DefaultContext.Ipv4.Maximum.BsrCandidateRpCache, self).__init__()

                        self.yang_name = "bsr-candidate-rp-cache"
                        self.yang_parent_name = "maximum"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self.is_presence_container = True
                        self._leafs = OrderedDict([
                            ('bsr_maximum_candidate_rp_cache', (YLeaf(YType.uint32, 'bsr-maximum-candidate-rp-cache'), ['int'])),
                            ('warning_threshold', (YLeaf(YType.uint32, 'warning-threshold'), ['int'])),
                        ])
                        self.bsr_maximum_candidate_rp_cache = None
                        self.warning_threshold = None
                        self._segment_path = lambda: "bsr-candidate-rp-cache"
                        self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-pim-cfg:pim/default-context/ipv4/maximum/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Pim.DefaultContext.Ipv4.Maximum.BsrCandidateRpCache, ['bsr_maximum_candidate_rp_cache', 'warning_threshold'], name, value)


                class Routes(Entity):
                    """
                    Override default maximum for number of routes
                    
                    .. attribute:: maximum_routes
                    
                    	Maximum number of PIM routes
                    	**type**\: int
                    
                    	**range:** 1..200000
                    
                    	**mandatory**\: True
                    
                    .. attribute:: warning_threshold
                    
                    	Set threshold to print warning
                    	**type**\: int
                    
                    	**range:** 1..200000
                    
                    	**default value**\: 100000
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'ipv4-pim-cfg'
                    _revision = '2017-10-15'

                    def __init__(self):
                        super(Pim.DefaultContext.Ipv4.Maximum.Routes, self).__init__()

                        self.yang_name = "routes"
                        self.yang_parent_name = "maximum"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self.is_presence_container = True
                        self._leafs = OrderedDict([
                            ('maximum_routes', (YLeaf(YType.uint32, 'maximum-routes'), ['int'])),
                            ('warning_threshold', (YLeaf(YType.uint32, 'warning-threshold'), ['int'])),
                        ])
                        self.maximum_routes = None
                        self.warning_threshold = None
                        self._segment_path = lambda: "routes"
                        self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-pim-cfg:pim/default-context/ipv4/maximum/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Pim.DefaultContext.Ipv4.Maximum.Routes, ['maximum_routes', 'warning_threshold'], name, value)


            class Ssm(Entity):
                """
                Configure IP Multicast SSM
                
                .. attribute:: disable
                
                	TRUE if SSM is disabled on this router
                	**type**\: bool
                
                	**default value**\: false
                
                .. attribute:: range
                
                	Access list of groups enabled with SSM
                	**type**\: str
                
                	**length:** 1..64
                
                

                """

                _prefix = 'ipv4-pim-cfg'
                _revision = '2017-10-15'

                def __init__(self):
                    super(Pim.DefaultContext.Ipv4.Ssm, self).__init__()

                    self.yang_name = "ssm"
                    self.yang_parent_name = "ipv4"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('disable', (YLeaf(YType.boolean, 'disable'), ['bool'])),
                        ('range', (YLeaf(YType.str, 'range'), ['str'])),
                    ])
                    self.disable = None
                    self.range = None
                    self._segment_path = lambda: "ssm"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-pim-cfg:pim/default-context/ipv4/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Pim.DefaultContext.Ipv4.Ssm, ['disable', 'range'], name, value)


            class Injects(Entity):
                """
                Inject Explicit PIM RPF Vector Proxy's
                
                .. attribute:: inject
                
                	Inject Explicit PIM RPF Vector Proxy's
                	**type**\: list of  		 :py:class:`Inject <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.DefaultContext.Ipv4.Injects.Inject>`
                
                

                """

                _prefix = 'ipv4-pim-cfg'
                _revision = '2017-10-15'

                def __init__(self):
                    super(Pim.DefaultContext.Ipv4.Injects, self).__init__()

                    self.yang_name = "injects"
                    self.yang_parent_name = "ipv4"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("inject", ("inject", Pim.DefaultContext.Ipv4.Injects.Inject))])
                    self._leafs = OrderedDict()

                    self.inject = YList(self)
                    self._segment_path = lambda: "injects"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-pim-cfg:pim/default-context/ipv4/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Pim.DefaultContext.Ipv4.Injects, [], name, value)


                class Inject(Entity):
                    """
                    Inject Explicit PIM RPF Vector Proxy's
                    
                    .. attribute:: source_address  (key)
                    
                    	Source Address
                    	**type**\: str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: prefix_length  (key)
                    
                    	Masklen
                    	**type**\: int
                    
                    	**range:** 0..32
                    
                    .. attribute:: rpf_proxy_address
                    
                    	RPF Proxy Address
                    	**type**\: list of str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    

                    """

                    _prefix = 'ipv4-pim-cfg'
                    _revision = '2017-10-15'

                    def __init__(self):
                        super(Pim.DefaultContext.Ipv4.Injects.Inject, self).__init__()

                        self.yang_name = "inject"
                        self.yang_parent_name = "injects"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['source_address','prefix_length']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('source_address', (YLeaf(YType.str, 'source-address'), ['str'])),
                            ('prefix_length', (YLeaf(YType.uint8, 'prefix-length'), ['int'])),
                            ('rpf_proxy_address', (YLeafList(YType.str, 'rpf-proxy-address'), ['str'])),
                        ])
                        self.source_address = None
                        self.prefix_length = None
                        self.rpf_proxy_address = []
                        self._segment_path = lambda: "inject" + "[source-address='" + str(self.source_address) + "']" + "[prefix-length='" + str(self.prefix_length) + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-pim-cfg:pim/default-context/ipv4/injects/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Pim.DefaultContext.Ipv4.Injects.Inject, ['source_address', 'prefix_length', 'rpf_proxy_address'], name, value)


            class BidirRpAddresses(Entity):
                """
                Configure Bidirectional PIM Rendezvous Point
                
                .. attribute:: bidir_rp_address
                
                	Address of the Rendezvous Point
                	**type**\: list of  		 :py:class:`BidirRpAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.DefaultContext.Ipv4.BidirRpAddresses.BidirRpAddress>`
                
                

                """

                _prefix = 'ipv4-pim-cfg'
                _revision = '2017-10-15'

                def __init__(self):
                    super(Pim.DefaultContext.Ipv4.BidirRpAddresses, self).__init__()

                    self.yang_name = "bidir-rp-addresses"
                    self.yang_parent_name = "ipv4"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("bidir-rp-address", ("bidir_rp_address", Pim.DefaultContext.Ipv4.BidirRpAddresses.BidirRpAddress))])
                    self._leafs = OrderedDict()

                    self.bidir_rp_address = YList(self)
                    self._segment_path = lambda: "bidir-rp-addresses"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-pim-cfg:pim/default-context/ipv4/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Pim.DefaultContext.Ipv4.BidirRpAddresses, [], name, value)


                class BidirRpAddress(Entity):
                    """
                    Address of the Rendezvous Point
                    
                    .. attribute:: rp_address  (key)
                    
                    	RP address of Rendezvous Point
                    	**type**\: union of the below types:
                    
                    		**type**\: str
                    
                    			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    		**type**\: str
                    
                    			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: access_list_name
                    
                    	Access list of groups that should map to a given RP
                    	**type**\: str
                    
                    	**length:** 1..64
                    
                    .. attribute:: auto_rp_override
                    
                    	TRUE Indicates if static RP config overrides AutoRP and BSR
                    	**type**\: bool
                    
                    

                    """

                    _prefix = 'ipv4-pim-cfg'
                    _revision = '2017-10-15'

                    def __init__(self):
                        super(Pim.DefaultContext.Ipv4.BidirRpAddresses.BidirRpAddress, self).__init__()

                        self.yang_name = "bidir-rp-address"
                        self.yang_parent_name = "bidir-rp-addresses"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['rp_address']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('rp_address', (YLeaf(YType.str, 'rp-address'), ['str','str'])),
                            ('access_list_name', (YLeaf(YType.str, 'access-list-name'), ['str'])),
                            ('auto_rp_override', (YLeaf(YType.boolean, 'auto-rp-override'), ['bool'])),
                        ])
                        self.rp_address = None
                        self.access_list_name = None
                        self.auto_rp_override = None
                        self._segment_path = lambda: "bidir-rp-address" + "[rp-address='" + str(self.rp_address) + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-pim-cfg:pim/default-context/ipv4/bidir-rp-addresses/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Pim.DefaultContext.Ipv4.BidirRpAddresses.BidirRpAddress, ['rp_address', 'access_list_name', 'auto_rp_override'], name, value)


            class Bsr(Entity):
                """
                PIM BSR configuration
                
                .. attribute:: candidate_bsr
                
                	PIM Candidate BSR configuration
                	**type**\:  :py:class:`CandidateBsr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.DefaultContext.Ipv4.Bsr.CandidateBsr>`
                
                	**presence node**\: True
                
                .. attribute:: candidate_rps
                
                	PIM RP configuration
                	**type**\:  :py:class:`CandidateRps <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.DefaultContext.Ipv4.Bsr.CandidateRps>`
                
                

                """

                _prefix = 'ipv4-pim-cfg'
                _revision = '2017-10-15'

                def __init__(self):
                    super(Pim.DefaultContext.Ipv4.Bsr, self).__init__()

                    self.yang_name = "bsr"
                    self.yang_parent_name = "ipv4"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("candidate-bsr", ("candidate_bsr", Pim.DefaultContext.Ipv4.Bsr.CandidateBsr)), ("candidate-rps", ("candidate_rps", Pim.DefaultContext.Ipv4.Bsr.CandidateRps))])
                    self._leafs = OrderedDict()

                    self.candidate_bsr = None
                    self._children_name_map["candidate_bsr"] = "candidate-bsr"

                    self.candidate_rps = Pim.DefaultContext.Ipv4.Bsr.CandidateRps()
                    self.candidate_rps.parent = self
                    self._children_name_map["candidate_rps"] = "candidate-rps"
                    self._segment_path = lambda: "bsr"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-pim-cfg:pim/default-context/ipv4/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Pim.DefaultContext.Ipv4.Bsr, [], name, value)


                class CandidateBsr(Entity):
                    """
                    PIM Candidate BSR configuration
                    
                    .. attribute:: address
                    
                    	BSR Address configured
                    	**type**\: union of the below types:
                    
                    		**type**\: str
                    
                    			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    		**type**\: str
                    
                    			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    	**mandatory**\: True
                    
                    .. attribute:: prefix_length
                    
                    	Hash Mask Length for this candidate BSR
                    	**type**\: int
                    
                    	**range:** 0..32
                    
                    	**default value**\: 30
                    
                    .. attribute:: priority
                    
                    	Priority of the Candidate BSR
                    	**type**\: int
                    
                    	**range:** 1..255
                    
                    	**default value**\: 1
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'ipv4-pim-cfg'
                    _revision = '2017-10-15'

                    def __init__(self):
                        super(Pim.DefaultContext.Ipv4.Bsr.CandidateBsr, self).__init__()

                        self.yang_name = "candidate-bsr"
                        self.yang_parent_name = "bsr"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self.is_presence_container = True
                        self._leafs = OrderedDict([
                            ('address', (YLeaf(YType.str, 'address'), ['str','str'])),
                            ('prefix_length', (YLeaf(YType.uint8, 'prefix-length'), ['int'])),
                            ('priority', (YLeaf(YType.uint32, 'priority'), ['int'])),
                        ])
                        self.address = None
                        self.prefix_length = None
                        self.priority = None
                        self._segment_path = lambda: "candidate-bsr"
                        self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-pim-cfg:pim/default-context/ipv4/bsr/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Pim.DefaultContext.Ipv4.Bsr.CandidateBsr, ['address', 'prefix_length', 'priority'], name, value)


                class CandidateRps(Entity):
                    """
                    PIM RP configuration
                    
                    .. attribute:: candidate_rp
                    
                    	Address of PIM SM BSR Candidate\-RP
                    	**type**\: list of  		 :py:class:`CandidateRp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.DefaultContext.Ipv4.Bsr.CandidateRps.CandidateRp>`
                    
                    

                    """

                    _prefix = 'ipv4-pim-cfg'
                    _revision = '2017-10-15'

                    def __init__(self):
                        super(Pim.DefaultContext.Ipv4.Bsr.CandidateRps, self).__init__()

                        self.yang_name = "candidate-rps"
                        self.yang_parent_name = "bsr"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("candidate-rp", ("candidate_rp", Pim.DefaultContext.Ipv4.Bsr.CandidateRps.CandidateRp))])
                        self._leafs = OrderedDict()

                        self.candidate_rp = YList(self)
                        self._segment_path = lambda: "candidate-rps"
                        self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-pim-cfg:pim/default-context/ipv4/bsr/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Pim.DefaultContext.Ipv4.Bsr.CandidateRps, [], name, value)


                    class CandidateRp(Entity):
                        """
                        Address of PIM SM BSR Candidate\-RP
                        
                        .. attribute:: address  (key)
                        
                        	Address of Candidate\-RP
                        	**type**\: union of the below types:
                        
                        		**type**\: str
                        
                        			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        		**type**\: str
                        
                        			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: mode  (key)
                        
                        	SM or Bidir
                        	**type**\:  :py:class:`PimProtocolMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.PimProtocolMode>`
                        
                        .. attribute:: group_list
                        
                        	Access\-list specifying the group range for the Candidate\-RP
                        	**type**\: str
                        
                        	**length:** 1..64
                        
                        .. attribute:: priority
                        
                        	Priority of the CRP
                        	**type**\: int
                        
                        	**range:** 1..255
                        
                        	**default value**\: 192
                        
                        .. attribute:: interval
                        
                        	Advertisement interval
                        	**type**\: int
                        
                        	**range:** 30..600
                        
                        	**default value**\: 60
                        
                        

                        """

                        _prefix = 'ipv4-pim-cfg'
                        _revision = '2017-10-15'

                        def __init__(self):
                            super(Pim.DefaultContext.Ipv4.Bsr.CandidateRps.CandidateRp, self).__init__()

                            self.yang_name = "candidate-rp"
                            self.yang_parent_name = "candidate-rps"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = ['address','mode']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('address', (YLeaf(YType.str, 'address'), ['str','str'])),
                                ('mode', (YLeaf(YType.enumeration, 'mode'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg', 'PimProtocolMode', '')])),
                                ('group_list', (YLeaf(YType.str, 'group-list'), ['str'])),
                                ('priority', (YLeaf(YType.uint32, 'priority'), ['int'])),
                                ('interval', (YLeaf(YType.uint32, 'interval'), ['int'])),
                            ])
                            self.address = None
                            self.mode = None
                            self.group_list = None
                            self.priority = None
                            self.interval = None
                            self._segment_path = lambda: "candidate-rp" + "[address='" + str(self.address) + "']" + "[mode='" + str(self.mode) + "']"
                            self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-pim-cfg:pim/default-context/ipv4/bsr/candidate-rps/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Pim.DefaultContext.Ipv4.Bsr.CandidateRps.CandidateRp, ['address', 'mode', 'group_list', 'priority', 'interval'], name, value)


            class Mofrr(Entity):
                """
                Multicast Only Fast Re\-Route
                
                .. attribute:: clone_joins
                
                	Clone multicast joins
                	**type**\:  :py:class:`CloneJoins <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.DefaultContext.Ipv4.Mofrr.CloneJoins>`
                
                .. attribute:: clone_sources
                
                	Clone multicast traffic
                	**type**\:  :py:class:`CloneSources <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.DefaultContext.Ipv4.Mofrr.CloneSources>`
                
                .. attribute:: rib
                
                	Access\-list specifying SG that should do RIB MOFRR
                	**type**\: str
                
                	**length:** 1..64
                
                .. attribute:: non_revertive
                
                	Non\-revertive Multicast Only Fast Re\-Route
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: enable
                
                	Enable Multicast Only FRR
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: flow
                
                	Access\-list specifying SG that should do FLOW MOFRR
                	**type**\: str
                
                	**length:** 1..64
                
                

                """

                _prefix = 'ipv4-pim-cfg'
                _revision = '2017-10-15'

                def __init__(self):
                    super(Pim.DefaultContext.Ipv4.Mofrr, self).__init__()

                    self.yang_name = "mofrr"
                    self.yang_parent_name = "ipv4"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("clone-joins", ("clone_joins", Pim.DefaultContext.Ipv4.Mofrr.CloneJoins)), ("clone-sources", ("clone_sources", Pim.DefaultContext.Ipv4.Mofrr.CloneSources))])
                    self._leafs = OrderedDict([
                        ('rib', (YLeaf(YType.str, 'rib'), ['str'])),
                        ('non_revertive', (YLeaf(YType.empty, 'non-revertive'), ['Empty'])),
                        ('enable', (YLeaf(YType.empty, 'enable'), ['Empty'])),
                        ('flow', (YLeaf(YType.str, 'flow'), ['str'])),
                    ])
                    self.rib = None
                    self.non_revertive = None
                    self.enable = None
                    self.flow = None

                    self.clone_joins = Pim.DefaultContext.Ipv4.Mofrr.CloneJoins()
                    self.clone_joins.parent = self
                    self._children_name_map["clone_joins"] = "clone-joins"

                    self.clone_sources = Pim.DefaultContext.Ipv4.Mofrr.CloneSources()
                    self.clone_sources.parent = self
                    self._children_name_map["clone_sources"] = "clone-sources"
                    self._segment_path = lambda: "mofrr"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-pim-cfg:pim/default-context/ipv4/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Pim.DefaultContext.Ipv4.Mofrr, ['rib', 'non_revertive', 'enable', 'flow'], name, value)


                class CloneJoins(Entity):
                    """
                    Clone multicast joins
                    
                    .. attribute:: clone_join
                    
                    	Clone S,G joins as S1,G joins and S2,G joins
                    	**type**\: list of  		 :py:class:`CloneJoin <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.DefaultContext.Ipv4.Mofrr.CloneJoins.CloneJoin>`
                    
                    

                    """

                    _prefix = 'ipv4-pim-cfg'
                    _revision = '2017-10-15'

                    def __init__(self):
                        super(Pim.DefaultContext.Ipv4.Mofrr.CloneJoins, self).__init__()

                        self.yang_name = "clone-joins"
                        self.yang_parent_name = "mofrr"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("clone-join", ("clone_join", Pim.DefaultContext.Ipv4.Mofrr.CloneJoins.CloneJoin))])
                        self._leafs = OrderedDict()

                        self.clone_join = YList(self)
                        self._segment_path = lambda: "clone-joins"
                        self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-pim-cfg:pim/default-context/ipv4/mofrr/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Pim.DefaultContext.Ipv4.Mofrr.CloneJoins, [], name, value)


                    class CloneJoin(Entity):
                        """
                        Clone S,G joins as S1,G joins and S2,G joins
                        
                        .. attribute:: source  (key)
                        
                        	Original source address (S)
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: primary  (key)
                        
                        	Primary cloned address (S1)
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: backup  (key)
                        
                        	Backup cloned address (S2)
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: prefix_length  (key)
                        
                        	Mask length
                        	**type**\: int
                        
                        	**range:** 0..32
                        
                        

                        """

                        _prefix = 'ipv4-pim-cfg'
                        _revision = '2017-10-15'

                        def __init__(self):
                            super(Pim.DefaultContext.Ipv4.Mofrr.CloneJoins.CloneJoin, self).__init__()

                            self.yang_name = "clone-join"
                            self.yang_parent_name = "clone-joins"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = ['source','primary','backup','prefix_length']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('source', (YLeaf(YType.str, 'source'), ['str'])),
                                ('primary', (YLeaf(YType.str, 'primary'), ['str'])),
                                ('backup', (YLeaf(YType.str, 'backup'), ['str'])),
                                ('prefix_length', (YLeaf(YType.uint8, 'prefix-length'), ['int'])),
                            ])
                            self.source = None
                            self.primary = None
                            self.backup = None
                            self.prefix_length = None
                            self._segment_path = lambda: "clone-join" + "[source='" + str(self.source) + "']" + "[primary='" + str(self.primary) + "']" + "[backup='" + str(self.backup) + "']" + "[prefix-length='" + str(self.prefix_length) + "']"
                            self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-pim-cfg:pim/default-context/ipv4/mofrr/clone-joins/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Pim.DefaultContext.Ipv4.Mofrr.CloneJoins.CloneJoin, ['source', 'primary', 'backup', 'prefix_length'], name, value)


                class CloneSources(Entity):
                    """
                    Clone multicast traffic
                    
                    .. attribute:: clone_source
                    
                    	Clone S,G traffic as S1,G traffic and S2,G traffic
                    	**type**\: list of  		 :py:class:`CloneSource <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.DefaultContext.Ipv4.Mofrr.CloneSources.CloneSource>`
                    
                    

                    """

                    _prefix = 'ipv4-pim-cfg'
                    _revision = '2017-10-15'

                    def __init__(self):
                        super(Pim.DefaultContext.Ipv4.Mofrr.CloneSources, self).__init__()

                        self.yang_name = "clone-sources"
                        self.yang_parent_name = "mofrr"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("clone-source", ("clone_source", Pim.DefaultContext.Ipv4.Mofrr.CloneSources.CloneSource))])
                        self._leafs = OrderedDict()

                        self.clone_source = YList(self)
                        self._segment_path = lambda: "clone-sources"
                        self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-pim-cfg:pim/default-context/ipv4/mofrr/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Pim.DefaultContext.Ipv4.Mofrr.CloneSources, [], name, value)


                    class CloneSource(Entity):
                        """
                        Clone S,G traffic as S1,G traffic and S2,G
                        traffic
                        
                        .. attribute:: source  (key)
                        
                        	Original source address (S)
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: primary  (key)
                        
                        	Primary cloned address (S1)
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: backup  (key)
                        
                        	Backup cloned address (S2)
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: prefix_length  (key)
                        
                        	Mask length
                        	**type**\: int
                        
                        	**range:** 0..32
                        
                        

                        """

                        _prefix = 'ipv4-pim-cfg'
                        _revision = '2017-10-15'

                        def __init__(self):
                            super(Pim.DefaultContext.Ipv4.Mofrr.CloneSources.CloneSource, self).__init__()

                            self.yang_name = "clone-source"
                            self.yang_parent_name = "clone-sources"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self.ylist_key_names = ['source','primary','backup','prefix_length']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('source', (YLeaf(YType.str, 'source'), ['str'])),
                                ('primary', (YLeaf(YType.str, 'primary'), ['str'])),
                                ('backup', (YLeaf(YType.str, 'backup'), ['str'])),
                                ('prefix_length', (YLeaf(YType.uint8, 'prefix-length'), ['int'])),
                            ])
                            self.source = None
                            self.primary = None
                            self.backup = None
                            self.prefix_length = None
                            self._segment_path = lambda: "clone-source" + "[source='" + str(self.source) + "']" + "[primary='" + str(self.primary) + "']" + "[backup='" + str(self.backup) + "']" + "[prefix-length='" + str(self.prefix_length) + "']"
                            self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-pim-cfg:pim/default-context/ipv4/mofrr/clone-sources/%s" % self._segment_path()
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Pim.DefaultContext.Ipv4.Mofrr.CloneSources.CloneSource, ['source', 'primary', 'backup', 'prefix_length'], name, value)


            class Paths(Entity):
                """
                Inject PIM RPF Vector Proxy's
                
                .. attribute:: path
                
                	Inject PIM RPF Vector Proxy's
                	**type**\: list of  		 :py:class:`Path <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg.Pim.DefaultContext.Ipv4.Paths.Path>`
                
                

                """

                _prefix = 'ipv4-pim-cfg'
                _revision = '2017-10-15'

                def __init__(self):
                    super(Pim.DefaultContext.Ipv4.Paths, self).__init__()

                    self.yang_name = "paths"
                    self.yang_parent_name = "ipv4"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("path", ("path", Pim.DefaultContext.Ipv4.Paths.Path))])
                    self._leafs = OrderedDict()

                    self.path = YList(self)
                    self._segment_path = lambda: "paths"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-pim-cfg:pim/default-context/ipv4/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Pim.DefaultContext.Ipv4.Paths, [], name, value)


                class Path(Entity):
                    """
                    Inject PIM RPF Vector Proxy's
                    
                    .. attribute:: source_address  (key)
                    
                    	Source Address
                    	**type**\: str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: prefix_length  (key)
                    
                    	Masklen
                    	**type**\: int
                    
                    	**range:** 0..32
                    
                    .. attribute:: rpf_proxy_address
                    
                    	RPF Proxy Address
                    	**type**\: list of str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    

                    """

                    _prefix = 'ipv4-pim-cfg'
                    _revision = '2017-10-15'

                    def __init__(self):
                        super(Pim.DefaultContext.Ipv4.Paths.Path, self).__init__()

                        self.yang_name = "path"
                        self.yang_parent_name = "paths"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self.ylist_key_names = ['source_address','prefix_length']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('source_address', (YLeaf(YType.str, 'source-address'), ['str'])),
                            ('prefix_length', (YLeaf(YType.uint8, 'prefix-length'), ['int'])),
                            ('rpf_proxy_address', (YLeafList(YType.str, 'rpf-proxy-address'), ['str'])),
                        ])
                        self.source_address = None
                        self.prefix_length = None
                        self.rpf_proxy_address = []
                        self._segment_path = lambda: "path" + "[source-address='" + str(self.source_address) + "']" + "[prefix-length='" + str(self.prefix_length) + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-pim-cfg:pim/default-context/ipv4/paths/%s" % self._segment_path()
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Pim.DefaultContext.Ipv4.Paths.Path, ['source_address', 'prefix_length', 'rpf_proxy_address'], name, value)


            class AllowRp(Entity):
                """
                Enable allow\-rp filtering for SM joins
                
                .. attribute:: rp_list_name
                
                	Access\-list specifiying applicable RPs
                	**type**\: str
                
                	**length:** 1..64
                
                .. attribute:: group_list_name
                
                	Access\-list specifiying applicable groups
                	**type**\: str
                
                	**length:** 1..64
                
                

                This class is a :ref:`presence class<presence-class>`

                """

                _prefix = 'ipv4-pim-cfg'
                _revision = '2017-10-15'

                def __init__(self):
                    super(Pim.DefaultContext.Ipv4.AllowRp, self).__init__()

                    self.yang_name = "allow-rp"
                    self.yang_parent_name = "ipv4"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self.is_presence_container = True
                    self._leafs = OrderedDict([
                        ('rp_list_name', (YLeaf(YType.str, 'rp-list-name'), ['str'])),
                        ('group_list_name', (YLeaf(YType.str, 'group-list-name'), ['str'])),
                    ])
                    self.rp_list_name = None
                    self.group_list_name = None
                    self._segment_path = lambda: "allow-rp"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-pim-cfg:pim/default-context/ipv4/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Pim.DefaultContext.Ipv4.AllowRp, ['rp_list_name', 'group_list_name'], name, value)


            class Convergence(Entity):
                """
                Configure convergence parameters
                
                .. attribute:: rpf_conflict_join_delay
                
                	Dampen first join if RPF path is through one of the downstream neighbor
                	**type**\: int
                
                	**range:** 0..15
                
                	**units**\: second
                
                .. attribute:: link_down_prune_delay
                
                	Delay prunes if route join state transitions to not\-joined on link down
                	**type**\: int
                
                	**range:** 0..60
                
                	**units**\: second
                
                

                """

                _prefix = 'ipv4-pim-cfg'
                _revision = '2017-10-15'

                def __init__(self):
                    super(Pim.DefaultContext.Ipv4.Convergence, self).__init__()

                    self.yang_name = "convergence"
                    self.yang_parent_name = "ipv4"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('rpf_conflict_join_delay', (YLeaf(YType.uint32, 'rpf-conflict-join-delay'), ['int'])),
                        ('link_down_prune_delay', (YLeaf(YType.uint32, 'link-down-prune-delay'), ['int'])),
                    ])
                    self.rpf_conflict_join_delay = None
                    self.link_down_prune_delay = None
                    self._segment_path = lambda: "convergence"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-pim-cfg:pim/default-context/ipv4/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Pim.DefaultContext.Ipv4.Convergence, ['rpf_conflict_join_delay', 'link_down_prune_delay'], name, value)

    def clone_ptr(self):
        self._top_entity = Pim()
        return self._top_entity

