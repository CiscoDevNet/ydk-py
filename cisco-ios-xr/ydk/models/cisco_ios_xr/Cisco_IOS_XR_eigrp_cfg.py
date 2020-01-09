""" Cisco_IOS_XR_eigrp_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR eigrp package configuration.

This module contains definitions
for the following management objects\:
  eigrp\: Configure Neighbor

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
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



class EigrpDelayUnit(Enum):
    """
    EigrpDelayUnit (Enum Class)

    Eigrp delay unit

    .. data:: ten_microsecond = 0

    	Delay in 10's of microsecond

    .. data:: picosecond = 1

    	Delay in picosecond

    """

    ten_microsecond = Enum.YLeaf(0, "ten-microsecond")

    picosecond = Enum.YLeaf(1, "picosecond")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_eigrp_cfg as meta
        return meta._meta_table['EigrpDelayUnit']


class EigrpDir(Enum):
    """
    EigrpDir (Enum Class)

    Eigrp dir

    .. data:: in_ = 1

    	inbound direction

    .. data:: out = 2

    	outbound direction

    """

    in_ = Enum.YLeaf(1, "in")

    out = Enum.YLeaf(2, "out")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_eigrp_cfg as meta
        return meta._meta_table['EigrpDir']


class EigrpMet(Enum):
    """
    EigrpMet (Enum Class)

    Eigrp met

    .. data:: maximum_hops = 1

    	Metric maxhops

    .. data:: weights = 2

    	Metric weights

    .. data:: rib_scale = 3

    	Metric ribscale

    .. data:: version = 4

    	Metric version

    """

    maximum_hops = Enum.YLeaf(1, "maximum-hops")

    weights = Enum.YLeaf(2, "weights")

    rib_scale = Enum.YLeaf(3, "rib-scale")

    version = Enum.YLeaf(4, "version")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_eigrp_cfg as meta
        return meta._meta_table['EigrpMet']


class EigrpMetricVersion(Enum):
    """
    EigrpMetricVersion (Enum Class)

    Eigrp metric version

    .. data:: Y_64bit = 0

    	64-bit metrics

    .. data:: Y_32bit = 1

    	32-bit metrics

    """

    Y_64bit = Enum.YLeaf(0, "64bit")

    Y_32bit = Enum.YLeaf(1, "32bit")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_eigrp_cfg as meta
        return meta._meta_table['EigrpMetricVersion']


class EigrpRedistProto(Enum):
    """
    EigrpRedistProto (Enum Class)

    Eigrp redist proto

    .. data:: bgp = 1

    	BGP routes

    .. data:: connected = 2

    	Connected routes

    .. data:: eigrp = 3

    	EIGRP routes

    .. data:: isis = 4

    	ISIS routes

    .. data:: ospf = 5

    	OSPF routes

    .. data:: rip = 6

    	RIP routes

    .. data:: static = 7

    	Static routes

    .. data:: ospfv3 = 8

    	OSPFv3 routes

    .. data:: subscriber = 9

    	Subscriber routes

    .. data:: application = 10

    	Application routes

    .. data:: mobile = 11

    	Mobile routes

    """

    bgp = Enum.YLeaf(1, "bgp")

    connected = Enum.YLeaf(2, "connected")

    eigrp = Enum.YLeaf(3, "eigrp")

    isis = Enum.YLeaf(4, "isis")

    ospf = Enum.YLeaf(5, "ospf")

    rip = Enum.YLeaf(6, "rip")

    static = Enum.YLeaf(7, "static")

    ospfv3 = Enum.YLeaf(8, "ospfv3")

    subscriber = Enum.YLeaf(9, "subscriber")

    application = Enum.YLeaf(10, "application")

    mobile = Enum.YLeaf(11, "mobile")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_eigrp_cfg as meta
        return meta._meta_table['EigrpRedistProto']


class EigrpSoo(Enum):
    """
    EigrpSoo (Enum Class)

    Eigrp soo

    .. data:: as_ = 1

    	AS:nn format

    .. data:: ipv4_address = 2

    	IPV4Address:nn format

    .. data:: four_byte_as = 3

    	AS2.AS:nn format

    """

    as_ = Enum.YLeaf(1, "as")

    ipv4_address = Enum.YLeaf(2, "ipv4-address")

    four_byte_as = Enum.YLeaf(3, "four-byte-as")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_eigrp_cfg as meta
        return meta._meta_table['EigrpSoo']


class EigrpStub(Enum):
    """
    EigrpStub (Enum Class)

    Eigrp stub

    .. data:: receive_only = 1

    	receive only

    .. data:: filtered = 2

    	filter some routes

    """

    receive_only = Enum.YLeaf(1, "receive-only")

    filtered = Enum.YLeaf(2, "filtered")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_eigrp_cfg as meta
        return meta._meta_table['EigrpStub']


class EigrpTimer(Enum):
    """
    EigrpTimer (Enum Class)

    Eigrp timer

    .. data:: active = 1

    	Active time

    .. data:: route_hold = 2

    	Route-hold time

    .. data:: signal = 3

    	Signal time

    .. data:: converge = 4

    	Converge time

    """

    active = Enum.YLeaf(1, "active")

    route_hold = Enum.YLeaf(2, "route-hold")

    signal = Enum.YLeaf(3, "signal")

    converge = Enum.YLeaf(4, "converge")


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_eigrp_cfg as meta
        return meta._meta_table['EigrpTimer']



class Eigrp(_Entity_):
    """
    Configure Neighbor
    
    .. attribute:: processes
    
    	Process related configuration
    	**type**\:  :py:class:`Processes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_cfg.Eigrp.Processes>`
    
    

    """

    _prefix = 'eigrp-cfg'
    _revision = '2018-06-15'

    def __init__(self):
        if sys.version_info > (3,):
            super().__init__()
        else:
            super(Eigrp, self).__init__()
        self._top_entity = None

        self.yang_name = "eigrp"
        self.yang_parent_name = "Cisco-IOS-XR-eigrp-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("processes", ("processes", Eigrp.Processes))])
        self._leafs = OrderedDict()

        self.processes = Eigrp.Processes()
        self.processes.parent = self
        self._children_name_map["processes"] = "processes"
        self._segment_path = lambda: "Cisco-IOS-XR-eigrp-cfg:eigrp"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Eigrp, [], name, value)


    class Processes(_Entity_):
        """
        Process related configuration
        
        .. attribute:: process
        
        	Configuration for a particular EIGRP process
        	**type**\: list of  		 :py:class:`Process <ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_cfg.Eigrp.Processes.Process>`
        
        

        """

        _prefix = 'eigrp-cfg'
        _revision = '2018-06-15'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(Eigrp.Processes, self).__init__()

            self.yang_name = "processes"
            self.yang_parent_name = "eigrp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("process", ("process", Eigrp.Processes.Process))])
            self._leafs = OrderedDict()

            self.process = YList(self)
            self._segment_path = lambda: "processes"
            self._absolute_path = lambda: "Cisco-IOS-XR-eigrp-cfg:eigrp/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Eigrp.Processes, [], name, value)


        class Process(_Entity_):
            """
            Configuration for a particular EIGRP process.
            
            .. attribute:: process_id  (key)
            
            	AS number (1 \- 65535) or Virutual instance name of the EIGRP process
            	**type**\: str
            
            	**length:** 1..32
            
            .. attribute:: vrfs
            
            	List of VRFs
            	**type**\:  :py:class:`Vrfs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_cfg.Eigrp.Processes.Process.Vrfs>`
            
            .. attribute:: default_vrf
            
            	Default VRF configuration.Deletion of this object also causes deletion of all objectsunder 'Process' associated with this process instance
            	**type**\:  :py:class:`DefaultVrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_cfg.Eigrp.Processes.Process.DefaultVrf>`
            
            .. attribute:: nsf_disable
            
            	Disable NSF for all address families under all VRF's. It takes precedence over the NSF related configuration in the address family submode
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'eigrp-cfg'
            _revision = '2018-06-15'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Eigrp.Processes.Process, self).__init__()

                self.yang_name = "process"
                self.yang_parent_name = "processes"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['process_id']
                self._child_classes = OrderedDict([("vrfs", ("vrfs", Eigrp.Processes.Process.Vrfs)), ("default-vrf", ("default_vrf", Eigrp.Processes.Process.DefaultVrf))])
                self._leafs = OrderedDict([
                    ('process_id', (YLeaf(YType.str, 'process-id'), ['str'])),
                    ('nsf_disable', (YLeaf(YType.empty, 'nsf-disable'), ['Empty'])),
                ])
                self.process_id = None
                self.nsf_disable = None

                self.vrfs = Eigrp.Processes.Process.Vrfs()
                self.vrfs.parent = self
                self._children_name_map["vrfs"] = "vrfs"

                self.default_vrf = Eigrp.Processes.Process.DefaultVrf()
                self.default_vrf.parent = self
                self._children_name_map["default_vrf"] = "default-vrf"
                self._segment_path = lambda: "process" + "[process-id='" + str(self.process_id) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-eigrp-cfg:eigrp/processes/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Eigrp.Processes.Process, ['process_id', 'nsf_disable'], name, value)


            class Vrfs(_Entity_):
                """
                List of VRFs
                
                .. attribute:: vrf
                
                	Non\-default VRF configuration.Deletion of this object also causes deletion of all objectsunder 'VRF' associated with this VRF instance
                	**type**\: list of  		 :py:class:`Vrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_cfg.Eigrp.Processes.Process.Vrfs.Vrf>`
                
                

                """

                _prefix = 'eigrp-cfg'
                _revision = '2018-06-15'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Eigrp.Processes.Process.Vrfs, self).__init__()

                    self.yang_name = "vrfs"
                    self.yang_parent_name = "process"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("vrf", ("vrf", Eigrp.Processes.Process.Vrfs.Vrf))])
                    self._leafs = OrderedDict()

                    self.vrf = YList(self)
                    self._segment_path = lambda: "vrfs"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Eigrp.Processes.Process.Vrfs, [], name, value)


                class Vrf(_Entity_):
                    """
                    Non\-default VRF configuration.Deletion of
                    this object also causes deletion of all
                    objectsunder 'VRF' associated with this VRF
                    instance.
                    
                    .. attribute:: vrf_name  (key)
                    
                    	VRF name
                    	**type**\: str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: afs
                    
                    	Address family list in a VRF
                    	**type**\:  :py:class:`Afs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_cfg.Eigrp.Processes.Process.Vrfs.Vrf.Afs>`
                    
                    .. attribute:: enable
                    
                    	Enable a non\-default VRF under the EIGRP process
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    

                    """

                    _prefix = 'eigrp-cfg'
                    _revision = '2018-06-15'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Eigrp.Processes.Process.Vrfs.Vrf, self).__init__()

                        self.yang_name = "vrf"
                        self.yang_parent_name = "vrfs"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['vrf_name']
                        self._child_classes = OrderedDict([("afs", ("afs", Eigrp.Processes.Process.Vrfs.Vrf.Afs))])
                        self._leafs = OrderedDict([
                            ('vrf_name', (YLeaf(YType.str, 'vrf-name'), ['str'])),
                            ('enable', (YLeaf(YType.empty, 'enable'), ['Empty'])),
                        ])
                        self.vrf_name = None
                        self.enable = None

                        self.afs = Eigrp.Processes.Process.Vrfs.Vrf.Afs()
                        self.afs.parent = self
                        self._children_name_map["afs"] = "afs"
                        self._segment_path = lambda: "vrf" + "[vrf-name='" + str(self.vrf_name) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Eigrp.Processes.Process.Vrfs.Vrf, ['vrf_name', 'enable'], name, value)


                    class Afs(_Entity_):
                        """
                        Address family list in a VRF
                        
                        .. attribute:: af
                        
                        	Configuration under an AF in a non\-default VRF context.Deletion of this object also causes deletion of all objectsunder 'AF' associated with this AF instance
                        	**type**\: list of  		 :py:class:`Af <ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_cfg.Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af>`
                        
                        

                        """

                        _prefix = 'eigrp-cfg'
                        _revision = '2018-06-15'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Eigrp.Processes.Process.Vrfs.Vrf.Afs, self).__init__()

                            self.yang_name = "afs"
                            self.yang_parent_name = "vrf"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("af", ("af", Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af))])
                            self._leafs = OrderedDict()

                            self.af = YList(self)
                            self._segment_path = lambda: "afs"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Eigrp.Processes.Process.Vrfs.Vrf.Afs, [], name, value)


                        class Af(_Entity_):
                            """
                            Configuration under an AF in a non\-default
                            VRF context.Deletion of this object also
                            causes deletion of all objectsunder 'AF'
                            associated with this AF instance.
                            
                            .. attribute:: af_name  (key)
                            
                            	Address Family
                            	**type**\:  :py:class:`EigrpAf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_datatypes.EigrpAf>`
                            
                            .. attribute:: all_neighbors_maximum_prefix
                            
                            	Maximum number of IP prefixes acceptable in aggregate, from neighbors
                            	**type**\:  :py:class:`AllNeighborsMaximumPrefix <ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_cfg.Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.AllNeighborsMaximumPrefix>`
                            
                            .. attribute:: redist_maximum_prefix
                            
                            	Maximum number of prefixes redistributed to protocol
                            	**type**\:  :py:class:`RedistMaximumPrefix <ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_cfg.Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.RedistMaximumPrefix>`
                            
                            .. attribute:: neighbor_maximum_prefixes
                            
                            	List of neighbors with prefix limits
                            	**type**\:  :py:class:`NeighborMaximumPrefixes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_cfg.Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.NeighborMaximumPrefixes>`
                            
                            .. attribute:: maximum_prefix
                            
                            	Maximum number of IP prefixes acceptable in aggregate
                            	**type**\:  :py:class:`MaximumPrefix <ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_cfg.Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.MaximumPrefix>`
                            
                            .. attribute:: enable
                            
                            	Enable an Address Family under a non\-default VRF
                            	**type**\: :py:class:`Empty<ydk.types.Empty>`
                            
                            .. attribute:: auto_summary
                            
                            	Enable Auto Summarization
                            	**type**\: :py:class:`Empty<ydk.types.Empty>`
                            
                            .. attribute:: stub
                            
                            	EIGRP stub configuration
                            	**type**\:  :py:class:`Stub <ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_cfg.Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Stub>`
                            
                            	**presence node**\: True
                            
                            .. attribute:: maximum_paths
                            
                            	number of paths
                            	**type**\: int
                            
                            	**range:** 1..32
                            
                            .. attribute:: redistributes
                            
                            	List of redistributed protocols
                            	**type**\:  :py:class:`Redistributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_cfg.Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Redistributes>`
                            
                            	**presence node**\: True
                            
                            .. attribute:: router_id
                            
                            	Set router ID
                            	**type**\: str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: log_neighbor_warnings
                            
                            	Enable/Disable neighbor state change warnings 
                            	**type**\: :py:class:`Empty<ydk.types.Empty>`
                            
                            .. attribute:: filter_policies
                            
                            	Inbound and outbound filter policies
                            	**type**\:  :py:class:`FilterPolicies <ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_cfg.Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.FilterPolicies>`
                            
                            .. attribute:: default_metric
                            
                            	Set metric of redistributed routes
                            	**type**\:  :py:class:`DefaultMetric <ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_cfg.Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.DefaultMetric>`
                            
                            .. attribute:: autonomous_system
                            
                            	Set the autonomous system of a VRF
                            	**type**\: int
                            
                            	**range:** 1..65535
                            
                            .. attribute:: variance
                            
                            	Control load balancing variance
                            	**type**\: int
                            
                            	**range:** 1..128
                            
                            .. attribute:: metrics
                            
                            	List of metric change behaviours
                            	**type**\:  :py:class:`Metrics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_cfg.Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Metrics>`
                            
                            .. attribute:: timers
                            
                            	List of timer configurations
                            	**type**\:  :py:class:`Timers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_cfg.Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Timers>`
                            
                            .. attribute:: nsf_disable
                            
                            	Disable NSF for this address family under this VRF
                            	**type**\: :py:class:`Empty<ydk.types.Empty>`
                            
                            .. attribute:: default_accepts
                            
                            	Candidate default policy table
                            	**type**\:  :py:class:`DefaultAccepts <ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_cfg.Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.DefaultAccepts>`
                            
                            .. attribute:: passive_interface_default
                            
                            	Suppress routing updates on all interfaces
                            	**type**\: :py:class:`Empty<ydk.types.Empty>`
                            
                            .. attribute:: interfaces
                            
                            	List of interfaces
                            	**type**\:  :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_cfg.Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Interfaces>`
                            
                            .. attribute:: distance
                            
                            	Set distance for EIGRP routes
                            	**type**\:  :py:class:`Distance <ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_cfg.Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Distance>`
                            
                            .. attribute:: log_neighbor_changes
                            
                            	Enable/Disable logginf of neighbor state changes
                            	**type**\: :py:class:`Empty<ydk.types.Empty>`
                            
                            

                            """

                            _prefix = 'eigrp-cfg'
                            _revision = '2018-06-15'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af, self).__init__()

                                self.yang_name = "af"
                                self.yang_parent_name = "afs"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['af_name']
                                self._child_classes = OrderedDict([("all-neighbors-maximum-prefix", ("all_neighbors_maximum_prefix", Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.AllNeighborsMaximumPrefix)), ("redist-maximum-prefix", ("redist_maximum_prefix", Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.RedistMaximumPrefix)), ("neighbor-maximum-prefixes", ("neighbor_maximum_prefixes", Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.NeighborMaximumPrefixes)), ("maximum-prefix", ("maximum_prefix", Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.MaximumPrefix)), ("stub", ("stub", Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Stub)), ("redistributes", ("redistributes", Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Redistributes)), ("filter-policies", ("filter_policies", Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.FilterPolicies)), ("default-metric", ("default_metric", Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.DefaultMetric)), ("metrics", ("metrics", Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Metrics)), ("timers", ("timers", Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Timers)), ("default-accepts", ("default_accepts", Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.DefaultAccepts)), ("interfaces", ("interfaces", Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Interfaces)), ("distance", ("distance", Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Distance))])
                                self._leafs = OrderedDict([
                                    ('af_name', (YLeaf(YType.enumeration, 'af-name'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_datatypes', 'EigrpAf', '')])),
                                    ('enable', (YLeaf(YType.empty, 'enable'), ['Empty'])),
                                    ('auto_summary', (YLeaf(YType.empty, 'auto-summary'), ['Empty'])),
                                    ('maximum_paths', (YLeaf(YType.uint32, 'maximum-paths'), ['int'])),
                                    ('router_id', (YLeaf(YType.str, 'router-id'), ['str'])),
                                    ('log_neighbor_warnings', (YLeaf(YType.empty, 'log-neighbor-warnings'), ['Empty'])),
                                    ('autonomous_system', (YLeaf(YType.uint32, 'autonomous-system'), ['int'])),
                                    ('variance', (YLeaf(YType.uint32, 'variance'), ['int'])),
                                    ('nsf_disable', (YLeaf(YType.empty, 'nsf-disable'), ['Empty'])),
                                    ('passive_interface_default', (YLeaf(YType.empty, 'passive-interface-default'), ['Empty'])),
                                    ('log_neighbor_changes', (YLeaf(YType.empty, 'log-neighbor-changes'), ['Empty'])),
                                ])
                                self.af_name = None
                                self.enable = None
                                self.auto_summary = None
                                self.maximum_paths = None
                                self.router_id = None
                                self.log_neighbor_warnings = None
                                self.autonomous_system = None
                                self.variance = None
                                self.nsf_disable = None
                                self.passive_interface_default = None
                                self.log_neighbor_changes = None

                                self.all_neighbors_maximum_prefix = Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.AllNeighborsMaximumPrefix()
                                self.all_neighbors_maximum_prefix.parent = self
                                self._children_name_map["all_neighbors_maximum_prefix"] = "all-neighbors-maximum-prefix"

                                self.redist_maximum_prefix = Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.RedistMaximumPrefix()
                                self.redist_maximum_prefix.parent = self
                                self._children_name_map["redist_maximum_prefix"] = "redist-maximum-prefix"

                                self.neighbor_maximum_prefixes = Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.NeighborMaximumPrefixes()
                                self.neighbor_maximum_prefixes.parent = self
                                self._children_name_map["neighbor_maximum_prefixes"] = "neighbor-maximum-prefixes"

                                self.maximum_prefix = Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.MaximumPrefix()
                                self.maximum_prefix.parent = self
                                self._children_name_map["maximum_prefix"] = "maximum-prefix"

                                self.stub = None
                                self._children_name_map["stub"] = "stub"

                                self.redistributes = None
                                self._children_name_map["redistributes"] = "redistributes"

                                self.filter_policies = Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.FilterPolicies()
                                self.filter_policies.parent = self
                                self._children_name_map["filter_policies"] = "filter-policies"

                                self.default_metric = Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.DefaultMetric()
                                self.default_metric.parent = self
                                self._children_name_map["default_metric"] = "default-metric"

                                self.metrics = Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Metrics()
                                self.metrics.parent = self
                                self._children_name_map["metrics"] = "metrics"

                                self.timers = Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Timers()
                                self.timers.parent = self
                                self._children_name_map["timers"] = "timers"

                                self.default_accepts = Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.DefaultAccepts()
                                self.default_accepts.parent = self
                                self._children_name_map["default_accepts"] = "default-accepts"

                                self.interfaces = Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Interfaces()
                                self.interfaces.parent = self
                                self._children_name_map["interfaces"] = "interfaces"

                                self.distance = Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Distance()
                                self.distance.parent = self
                                self._children_name_map["distance"] = "distance"
                                self._segment_path = lambda: "af" + "[af-name='" + str(self.af_name) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af, ['af_name', 'enable', 'auto_summary', 'maximum_paths', 'router_id', 'log_neighbor_warnings', 'autonomous_system', 'variance', 'nsf_disable', 'passive_interface_default', 'log_neighbor_changes'], name, value)


                            class AllNeighborsMaximumPrefix(_Entity_):
                                """
                                Maximum number of IP prefixes acceptable
                                in aggregate, from neighbors
                                
                                .. attribute:: max_prefix
                                
                                	Number of IP prefixes for maximum\-prefix limit
                                	**type**\: int
                                
                                	**range:** 1..4294967295
                                
                                .. attribute:: threshold
                                
                                	Configure threshold percentage for warnings
                                	**type**\: int
                                
                                	**range:** 1..100
                                
                                	**units**\: percentage
                                
                                .. attribute:: dampened
                                
                                	Enable decay penalty to be applied to time period
                                	**type**\: bool
                                
                                .. attribute:: reset_time
                                
                                	Time to reset restart count
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: restart
                                
                                	Shutdown time after hitting max\-prefix limit
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: restart_count
                                
                                	Restart count after hitting max\-prefix limit
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: warning_only
                                
                                	Only a warning is logged when prefix limit is reached
                                	**type**\: bool
                                
                                

                                """

                                _prefix = 'eigrp-cfg'
                                _revision = '2018-06-15'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.AllNeighborsMaximumPrefix, self).__init__()

                                    self.yang_name = "all-neighbors-maximum-prefix"
                                    self.yang_parent_name = "af"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('max_prefix', (YLeaf(YType.uint32, 'max-prefix'), ['int'])),
                                        ('threshold', (YLeaf(YType.uint32, 'threshold'), ['int'])),
                                        ('dampened', (YLeaf(YType.boolean, 'dampened'), ['bool'])),
                                        ('reset_time', (YLeaf(YType.uint32, 'reset-time'), ['int'])),
                                        ('restart', (YLeaf(YType.uint32, 'restart'), ['int'])),
                                        ('restart_count', (YLeaf(YType.uint32, 'restart-count'), ['int'])),
                                        ('warning_only', (YLeaf(YType.boolean, 'warning-only'), ['bool'])),
                                    ])
                                    self.max_prefix = None
                                    self.threshold = None
                                    self.dampened = None
                                    self.reset_time = None
                                    self.restart = None
                                    self.restart_count = None
                                    self.warning_only = None
                                    self._segment_path = lambda: "all-neighbors-maximum-prefix"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.AllNeighborsMaximumPrefix, ['max_prefix', 'threshold', 'dampened', 'reset_time', 'restart', 'restart_count', 'warning_only'], name, value)

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_eigrp_cfg as meta
                                    return meta._meta_table['Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.AllNeighborsMaximumPrefix']['meta_info']


                            class RedistMaximumPrefix(_Entity_):
                                """
                                Maximum number of prefixes redistributed
                                to protocol
                                
                                .. attribute:: max_prefix
                                
                                	Number of IP prefixes for maximum\-prefix limit
                                	**type**\: int
                                
                                	**range:** 1..4294967295
                                
                                .. attribute:: threshold
                                
                                	Configure threshold percentage for warnings
                                	**type**\: int
                                
                                	**range:** 1..100
                                
                                	**units**\: percentage
                                
                                .. attribute:: dampened
                                
                                	Enable decay penalty to be applied to time period
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: reset_time
                                
                                	Time to reset restart count
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: restart
                                
                                	Shutdown time after hitting max\-prefix limit
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: restart_count
                                
                                	Restart count after hitting max\-prefix limit
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: warning_only
                                
                                	Only a warning is logged when prefix limit is reached
                                	**type**\: bool
                                
                                

                                """

                                _prefix = 'eigrp-cfg'
                                _revision = '2018-06-15'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.RedistMaximumPrefix, self).__init__()

                                    self.yang_name = "redist-maximum-prefix"
                                    self.yang_parent_name = "af"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('max_prefix', (YLeaf(YType.uint32, 'max-prefix'), ['int'])),
                                        ('threshold', (YLeaf(YType.uint32, 'threshold'), ['int'])),
                                        ('dampened', (YLeaf(YType.uint32, 'dampened'), ['int'])),
                                        ('reset_time', (YLeaf(YType.uint32, 'reset-time'), ['int'])),
                                        ('restart', (YLeaf(YType.uint32, 'restart'), ['int'])),
                                        ('restart_count', (YLeaf(YType.uint32, 'restart-count'), ['int'])),
                                        ('warning_only', (YLeaf(YType.boolean, 'warning-only'), ['bool'])),
                                    ])
                                    self.max_prefix = None
                                    self.threshold = None
                                    self.dampened = None
                                    self.reset_time = None
                                    self.restart = None
                                    self.restart_count = None
                                    self.warning_only = None
                                    self._segment_path = lambda: "redist-maximum-prefix"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.RedistMaximumPrefix, ['max_prefix', 'threshold', 'dampened', 'reset_time', 'restart', 'restart_count', 'warning_only'], name, value)

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_eigrp_cfg as meta
                                    return meta._meta_table['Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.RedistMaximumPrefix']['meta_info']


                            class NeighborMaximumPrefixes(_Entity_):
                                """
                                List of neighbors with prefix limits
                                
                                .. attribute:: neighbor_maximum_prefix
                                
                                	Neighbor prefix limits configuration
                                	**type**\: list of  		 :py:class:`NeighborMaximumPrefix <ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_cfg.Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.NeighborMaximumPrefixes.NeighborMaximumPrefix>`
                                
                                

                                """

                                _prefix = 'eigrp-cfg'
                                _revision = '2018-06-15'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.NeighborMaximumPrefixes, self).__init__()

                                    self.yang_name = "neighbor-maximum-prefixes"
                                    self.yang_parent_name = "af"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("neighbor-maximum-prefix", ("neighbor_maximum_prefix", Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.NeighborMaximumPrefixes.NeighborMaximumPrefix))])
                                    self._leafs = OrderedDict()

                                    self.neighbor_maximum_prefix = YList(self)
                                    self._segment_path = lambda: "neighbor-maximum-prefixes"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.NeighborMaximumPrefixes, [], name, value)


                                class NeighborMaximumPrefix(_Entity_):
                                    """
                                    Neighbor prefix limits configuration
                                    
                                    .. attribute:: neighbor_address  (key)
                                    
                                    	Neighbor IP address
                                    	**type**\: union of the below types:
                                    
                                    		**type**\: str
                                    
                                    			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    		**type**\: str
                                    
                                    			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                    
                                    .. attribute:: max_prefix
                                    
                                    	Number of IP prefixes for maximum\-prefix limit
                                    	**type**\: int
                                    
                                    	**range:** 1..4294967295
                                    
                                    .. attribute:: threshold
                                    
                                    	Configure threshold percentage for warnings
                                    	**type**\: int
                                    
                                    	**range:** 1..100
                                    
                                    	**units**\: percentage
                                    
                                    .. attribute:: warning_only
                                    
                                    	Only a warning is logged when prefix limit is reached
                                    	**type**\: bool
                                    
                                    

                                    """

                                    _prefix = 'eigrp-cfg'
                                    _revision = '2018-06-15'

                                    def __init__(self):
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
                                            super(Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.NeighborMaximumPrefixes.NeighborMaximumPrefix, self).__init__()

                                        self.yang_name = "neighbor-maximum-prefix"
                                        self.yang_parent_name = "neighbor-maximum-prefixes"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = ['neighbor_address']
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('neighbor_address', (YLeaf(YType.str, 'neighbor-address'), ['str','str'])),
                                            ('max_prefix', (YLeaf(YType.uint32, 'max-prefix'), ['int'])),
                                            ('threshold', (YLeaf(YType.uint32, 'threshold'), ['int'])),
                                            ('warning_only', (YLeaf(YType.boolean, 'warning-only'), ['bool'])),
                                        ])
                                        self.neighbor_address = None
                                        self.max_prefix = None
                                        self.threshold = None
                                        self.warning_only = None
                                        self._segment_path = lambda: "neighbor-maximum-prefix" + "[neighbor-address='" + str(self.neighbor_address) + "']"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.NeighborMaximumPrefixes.NeighborMaximumPrefix, ['neighbor_address', 'max_prefix', 'threshold', 'warning_only'], name, value)

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_eigrp_cfg as meta
                                        return meta._meta_table['Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.NeighborMaximumPrefixes.NeighborMaximumPrefix']['meta_info']

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_eigrp_cfg as meta
                                    return meta._meta_table['Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.NeighborMaximumPrefixes']['meta_info']


                            class MaximumPrefix(_Entity_):
                                """
                                Maximum number of IP prefixes acceptable
                                in aggregate
                                
                                .. attribute:: max_prefix
                                
                                	Number of IP prefixes for maximum\-prefix limit
                                	**type**\: int
                                
                                	**range:** 1..4294967295
                                
                                .. attribute:: threshold
                                
                                	Configure threshold percentage for warnings
                                	**type**\: int
                                
                                	**range:** 1..100
                                
                                	**units**\: percentage
                                
                                .. attribute:: dampened
                                
                                	Enable decay penalty to be applied to time period
                                	**type**\: bool
                                
                                .. attribute:: reset_time
                                
                                	Time to reset restart count
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: restart
                                
                                	Shutdown time after hitting max\-prefix limit
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: restart_count
                                
                                	Restart count after hitting max\-prefix limit
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: warning_only
                                
                                	Only a warning is logged when prefix limit is reached
                                	**type**\: bool
                                
                                

                                """

                                _prefix = 'eigrp-cfg'
                                _revision = '2018-06-15'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.MaximumPrefix, self).__init__()

                                    self.yang_name = "maximum-prefix"
                                    self.yang_parent_name = "af"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('max_prefix', (YLeaf(YType.uint32, 'max-prefix'), ['int'])),
                                        ('threshold', (YLeaf(YType.uint32, 'threshold'), ['int'])),
                                        ('dampened', (YLeaf(YType.boolean, 'dampened'), ['bool'])),
                                        ('reset_time', (YLeaf(YType.uint32, 'reset-time'), ['int'])),
                                        ('restart', (YLeaf(YType.uint32, 'restart'), ['int'])),
                                        ('restart_count', (YLeaf(YType.uint32, 'restart-count'), ['int'])),
                                        ('warning_only', (YLeaf(YType.boolean, 'warning-only'), ['bool'])),
                                    ])
                                    self.max_prefix = None
                                    self.threshold = None
                                    self.dampened = None
                                    self.reset_time = None
                                    self.restart = None
                                    self.restart_count = None
                                    self.warning_only = None
                                    self._segment_path = lambda: "maximum-prefix"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.MaximumPrefix, ['max_prefix', 'threshold', 'dampened', 'reset_time', 'restart', 'restart_count', 'warning_only'], name, value)

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_eigrp_cfg as meta
                                    return meta._meta_table['Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.MaximumPrefix']['meta_info']


                            class Stub(_Entity_):
                                """
                                EIGRP stub configuration
                                
                                .. attribute:: type
                                
                                	Stub config type
                                	**type**\:  :py:class:`EigrpStub <ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_cfg.EigrpStub>`
                                
                                .. attribute:: connected
                                
                                	Do advertise connected routes
                                	**type**\: bool
                                
                                .. attribute:: redistributed
                                
                                	Do advertise redistributed routes
                                	**type**\: bool
                                
                                .. attribute:: static
                                
                                	Do advertise static routes
                                	**type**\: bool
                                
                                .. attribute:: summary
                                
                                	Do advertise summary routes
                                	**type**\: bool
                                
                                

                                This class is a :ref:`presence class<presence-class>`

                                """

                                _prefix = 'eigrp-cfg'
                                _revision = '2018-06-15'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Stub, self).__init__()

                                    self.yang_name = "stub"
                                    self.yang_parent_name = "af"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self.is_presence_container = True
                                    self._leafs = OrderedDict([
                                        ('type', (YLeaf(YType.enumeration, 'type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_cfg', 'EigrpStub', '')])),
                                        ('connected', (YLeaf(YType.boolean, 'connected'), ['bool'])),
                                        ('redistributed', (YLeaf(YType.boolean, 'redistributed'), ['bool'])),
                                        ('static', (YLeaf(YType.boolean, 'static'), ['bool'])),
                                        ('summary', (YLeaf(YType.boolean, 'summary'), ['bool'])),
                                    ])
                                    self.type = None
                                    self.connected = None
                                    self.redistributed = None
                                    self.static = None
                                    self.summary = None
                                    self._segment_path = lambda: "stub"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Stub, ['type', 'connected', 'redistributed', 'static', 'summary'], name, value)

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_eigrp_cfg as meta
                                    return meta._meta_table['Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Stub']['meta_info']


                            class Redistributes(_Entity_):
                                """
                                List of redistributed protocols
                                
                                .. attribute:: redistribute
                                
                                	Redistribute another protocol
                                	**type**\: list of  		 :py:class:`Redistribute <ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_cfg.Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Redistributes.Redistribute>`
                                
                                .. attribute:: redistribute_as_xx
                                
                                	Redistribute another protocol
                                	**type**\: list of  		 :py:class:`RedistributeAsXx <ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_cfg.Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Redistributes.RedistributeAsXx>`
                                
                                .. attribute:: redistribute_as_yy
                                
                                	Redistribute another protocol
                                	**type**\: list of  		 :py:class:`RedistributeAsYy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_cfg.Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Redistributes.RedistributeAsYy>`
                                
                                .. attribute:: redistribute_as_xx_as_yy
                                
                                	Redistribute another protocol
                                	**type**\: list of  		 :py:class:`RedistributeAsXxAsYy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_cfg.Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Redistributes.RedistributeAsXxAsYy>`
                                
                                .. attribute:: redistribute_tag_name
                                
                                	Redistribute another protocol
                                	**type**\: list of  		 :py:class:`RedistributeTagName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_cfg.Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Redistributes.RedistributeTagName>`
                                
                                .. attribute:: redistribute_as_xx_tag_name
                                
                                	Redistribute another protocol
                                	**type**\: list of  		 :py:class:`RedistributeAsXxTagName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_cfg.Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Redistributes.RedistributeAsXxTagName>`
                                
                                .. attribute:: redistribute_as_yy_tag_name
                                
                                	Redistribute another protocol
                                	**type**\: list of  		 :py:class:`RedistributeAsYyTagName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_cfg.Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Redistributes.RedistributeAsYyTagName>`
                                
                                .. attribute:: redistribute_as_xx_as_yy_tag_name
                                
                                	Redistribute another protocol
                                	**type**\: list of  		 :py:class:`RedistributeAsXxAsYyTagName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_cfg.Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Redistributes.RedistributeAsXxAsYyTagName>`
                                
                                

                                This class is a :ref:`presence class<presence-class>`

                                """

                                _prefix = 'eigrp-cfg'
                                _revision = '2018-06-15'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Redistributes, self).__init__()

                                    self.yang_name = "redistributes"
                                    self.yang_parent_name = "af"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("redistribute", ("redistribute", Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Redistributes.Redistribute)), ("redistribute-as-xx", ("redistribute_as_xx", Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Redistributes.RedistributeAsXx)), ("redistribute-as-yy", ("redistribute_as_yy", Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Redistributes.RedistributeAsYy)), ("redistribute-as-xx-as-yy", ("redistribute_as_xx_as_yy", Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Redistributes.RedistributeAsXxAsYy)), ("redistribute-tag-name", ("redistribute_tag_name", Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Redistributes.RedistributeTagName)), ("redistribute-as-xx-tag-name", ("redistribute_as_xx_tag_name", Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Redistributes.RedistributeAsXxTagName)), ("redistribute-as-yy-tag-name", ("redistribute_as_yy_tag_name", Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Redistributes.RedistributeAsYyTagName)), ("redistribute-as-xx-as-yy-tag-name", ("redistribute_as_xx_as_yy_tag_name", Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Redistributes.RedistributeAsXxAsYyTagName))])
                                    self.is_presence_container = True
                                    self._leafs = OrderedDict()

                                    self.redistribute = YList(self)
                                    self.redistribute_as_xx = YList(self)
                                    self.redistribute_as_yy = YList(self)
                                    self.redistribute_as_xx_as_yy = YList(self)
                                    self.redistribute_tag_name = YList(self)
                                    self.redistribute_as_xx_tag_name = YList(self)
                                    self.redistribute_as_yy_tag_name = YList(self)
                                    self.redistribute_as_xx_as_yy_tag_name = YList(self)
                                    self._segment_path = lambda: "redistributes"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Redistributes, [], name, value)


                                class Redistribute(_Entity_):
                                    """
                                    Redistribute another protocol
                                    
                                    .. attribute:: protocol_name  (key)
                                    
                                    	Redistributed protocol
                                    	**type**\:  :py:class:`EigrpRedistProto <ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_cfg.EigrpRedistProto>`
                                    
                                    .. attribute:: policy_name
                                    
                                    	Policy name
                                    	**type**\: str
                                    
                                    .. attribute:: policy_specified
                                    
                                    	TRUE if Policy has been specified
                                    	**type**\: bool
                                    
                                    	**mandatory**\: True
                                    
                                    

                                    """

                                    _prefix = 'eigrp-cfg'
                                    _revision = '2018-06-15'

                                    def __init__(self):
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
                                            super(Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Redistributes.Redistribute, self).__init__()

                                        self.yang_name = "redistribute"
                                        self.yang_parent_name = "redistributes"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = ['protocol_name']
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('protocol_name', (YLeaf(YType.enumeration, 'protocol-name'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_cfg', 'EigrpRedistProto', '')])),
                                            ('policy_name', (YLeaf(YType.str, 'policy-name'), ['str'])),
                                            ('policy_specified', (YLeaf(YType.boolean, 'policy-specified'), ['bool'])),
                                        ])
                                        self.protocol_name = None
                                        self.policy_name = None
                                        self.policy_specified = None
                                        self._segment_path = lambda: "redistribute" + "[protocol-name='" + str(self.protocol_name) + "']"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Redistributes.Redistribute, ['protocol_name', 'policy_name', 'policy_specified'], name, value)

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_eigrp_cfg as meta
                                        return meta._meta_table['Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Redistributes.Redistribute']['meta_info']


                                class RedistributeAsXx(_Entity_):
                                    """
                                    Redistribute another protocol
                                    
                                    .. attribute:: as_xx  (key)
                                    
                                    	Higher sixteen bits of 4\-byte BGP AS number
                                    	**type**\: int
                                    
                                    	**range:** 0..65535
                                    
                                    .. attribute:: protocol_name  (key)
                                    
                                    	Redistributed protocol
                                    	**type**\:  :py:class:`EigrpRedistProto <ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_cfg.EigrpRedistProto>`
                                    
                                    .. attribute:: policy_name
                                    
                                    	Policy name
                                    	**type**\: str
                                    
                                    .. attribute:: policy_specified
                                    
                                    	TRUE if Policy has been specified
                                    	**type**\: bool
                                    
                                    	**mandatory**\: True
                                    
                                    

                                    """

                                    _prefix = 'eigrp-cfg'
                                    _revision = '2018-06-15'

                                    def __init__(self):
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
                                            super(Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Redistributes.RedistributeAsXx, self).__init__()

                                        self.yang_name = "redistribute-as-xx"
                                        self.yang_parent_name = "redistributes"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = ['as_xx','protocol_name']
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('as_xx', (YLeaf(YType.uint32, 'as-xx'), ['int'])),
                                            ('protocol_name', (YLeaf(YType.enumeration, 'protocol-name'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_cfg', 'EigrpRedistProto', '')])),
                                            ('policy_name', (YLeaf(YType.str, 'policy-name'), ['str'])),
                                            ('policy_specified', (YLeaf(YType.boolean, 'policy-specified'), ['bool'])),
                                        ])
                                        self.as_xx = None
                                        self.protocol_name = None
                                        self.policy_name = None
                                        self.policy_specified = None
                                        self._segment_path = lambda: "redistribute-as-xx" + "[as-xx='" + str(self.as_xx) + "']" + "[protocol-name='" + str(self.protocol_name) + "']"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Redistributes.RedistributeAsXx, ['as_xx', 'protocol_name', 'policy_name', 'policy_specified'], name, value)

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_eigrp_cfg as meta
                                        return meta._meta_table['Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Redistributes.RedistributeAsXx']['meta_info']


                                class RedistributeAsYy(_Entity_):
                                    """
                                    Redistribute another protocol
                                    
                                    .. attribute:: as_yy  (key)
                                    
                                    	2\-byte or 4\-byte BGP AS Number
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: protocol_name  (key)
                                    
                                    	Redistributed protocol
                                    	**type**\:  :py:class:`EigrpRedistProto <ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_cfg.EigrpRedistProto>`
                                    
                                    .. attribute:: policy_name
                                    
                                    	Policy name
                                    	**type**\: str
                                    
                                    .. attribute:: policy_specified
                                    
                                    	TRUE if Policy has been specified
                                    	**type**\: bool
                                    
                                    	**mandatory**\: True
                                    
                                    

                                    """

                                    _prefix = 'eigrp-cfg'
                                    _revision = '2018-06-15'

                                    def __init__(self):
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
                                            super(Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Redistributes.RedistributeAsYy, self).__init__()

                                        self.yang_name = "redistribute-as-yy"
                                        self.yang_parent_name = "redistributes"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = ['as_yy','protocol_name']
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('as_yy', (YLeaf(YType.uint32, 'as-yy'), ['int'])),
                                            ('protocol_name', (YLeaf(YType.enumeration, 'protocol-name'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_cfg', 'EigrpRedistProto', '')])),
                                            ('policy_name', (YLeaf(YType.str, 'policy-name'), ['str'])),
                                            ('policy_specified', (YLeaf(YType.boolean, 'policy-specified'), ['bool'])),
                                        ])
                                        self.as_yy = None
                                        self.protocol_name = None
                                        self.policy_name = None
                                        self.policy_specified = None
                                        self._segment_path = lambda: "redistribute-as-yy" + "[as-yy='" + str(self.as_yy) + "']" + "[protocol-name='" + str(self.protocol_name) + "']"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Redistributes.RedistributeAsYy, ['as_yy', 'protocol_name', 'policy_name', 'policy_specified'], name, value)

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_eigrp_cfg as meta
                                        return meta._meta_table['Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Redistributes.RedistributeAsYy']['meta_info']


                                class RedistributeAsXxAsYy(_Entity_):
                                    """
                                    Redistribute another protocol
                                    
                                    .. attribute:: as_xx  (key)
                                    
                                    	Higher sixteen bits of 4\-byte BGP AS number
                                    	**type**\: int
                                    
                                    	**range:** 0..65535
                                    
                                    .. attribute:: as_yy  (key)
                                    
                                    	2\-byte or 4\-byte BGP AS Number
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: protocol_name  (key)
                                    
                                    	Redistributed protocol
                                    	**type**\:  :py:class:`EigrpRedistProto <ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_cfg.EigrpRedistProto>`
                                    
                                    .. attribute:: policy_name
                                    
                                    	Policy name
                                    	**type**\: str
                                    
                                    .. attribute:: policy_specified
                                    
                                    	TRUE if Policy has been specified
                                    	**type**\: bool
                                    
                                    	**mandatory**\: True
                                    
                                    

                                    """

                                    _prefix = 'eigrp-cfg'
                                    _revision = '2018-06-15'

                                    def __init__(self):
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
                                            super(Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Redistributes.RedistributeAsXxAsYy, self).__init__()

                                        self.yang_name = "redistribute-as-xx-as-yy"
                                        self.yang_parent_name = "redistributes"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = ['as_xx','as_yy','protocol_name']
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('as_xx', (YLeaf(YType.uint32, 'as-xx'), ['int'])),
                                            ('as_yy', (YLeaf(YType.uint32, 'as-yy'), ['int'])),
                                            ('protocol_name', (YLeaf(YType.enumeration, 'protocol-name'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_cfg', 'EigrpRedistProto', '')])),
                                            ('policy_name', (YLeaf(YType.str, 'policy-name'), ['str'])),
                                            ('policy_specified', (YLeaf(YType.boolean, 'policy-specified'), ['bool'])),
                                        ])
                                        self.as_xx = None
                                        self.as_yy = None
                                        self.protocol_name = None
                                        self.policy_name = None
                                        self.policy_specified = None
                                        self._segment_path = lambda: "redistribute-as-xx-as-yy" + "[as-xx='" + str(self.as_xx) + "']" + "[as-yy='" + str(self.as_yy) + "']" + "[protocol-name='" + str(self.protocol_name) + "']"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Redistributes.RedistributeAsXxAsYy, ['as_xx', 'as_yy', 'protocol_name', 'policy_name', 'policy_specified'], name, value)

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_eigrp_cfg as meta
                                        return meta._meta_table['Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Redistributes.RedistributeAsXxAsYy']['meta_info']


                                class RedistributeTagName(_Entity_):
                                    """
                                    Redistribute another protocol
                                    
                                    .. attribute:: tag_name  (key)
                                    
                                    	OSPF/OSPFv3/ISIS/OnePK Application tag name
                                    	**type**\: str
                                    
                                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                                    
                                    .. attribute:: protocol_name  (key)
                                    
                                    	Redistributed protocol
                                    	**type**\:  :py:class:`EigrpRedistProto <ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_cfg.EigrpRedistProto>`
                                    
                                    .. attribute:: policy_name
                                    
                                    	Policy name
                                    	**type**\: str
                                    
                                    .. attribute:: policy_specified
                                    
                                    	TRUE if Policy has been specified
                                    	**type**\: bool
                                    
                                    	**mandatory**\: True
                                    
                                    

                                    """

                                    _prefix = 'eigrp-cfg'
                                    _revision = '2018-06-15'

                                    def __init__(self):
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
                                            super(Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Redistributes.RedistributeTagName, self).__init__()

                                        self.yang_name = "redistribute-tag-name"
                                        self.yang_parent_name = "redistributes"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = ['tag_name','protocol_name']
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('tag_name', (YLeaf(YType.str, 'tag-name'), ['str'])),
                                            ('protocol_name', (YLeaf(YType.enumeration, 'protocol-name'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_cfg', 'EigrpRedistProto', '')])),
                                            ('policy_name', (YLeaf(YType.str, 'policy-name'), ['str'])),
                                            ('policy_specified', (YLeaf(YType.boolean, 'policy-specified'), ['bool'])),
                                        ])
                                        self.tag_name = None
                                        self.protocol_name = None
                                        self.policy_name = None
                                        self.policy_specified = None
                                        self._segment_path = lambda: "redistribute-tag-name" + "[tag-name='" + str(self.tag_name) + "']" + "[protocol-name='" + str(self.protocol_name) + "']"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Redistributes.RedistributeTagName, ['tag_name', 'protocol_name', 'policy_name', 'policy_specified'], name, value)

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_eigrp_cfg as meta
                                        return meta._meta_table['Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Redistributes.RedistributeTagName']['meta_info']


                                class RedistributeAsXxTagName(_Entity_):
                                    """
                                    Redistribute another protocol
                                    
                                    .. attribute:: as_xx  (key)
                                    
                                    	Higher sixteen bits of 4\-byte BGP AS number
                                    	**type**\: int
                                    
                                    	**range:** 0..65535
                                    
                                    .. attribute:: tag_name  (key)
                                    
                                    	OSPF/OSPFv3/ISIS/OnePK Application tag name
                                    	**type**\: str
                                    
                                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                                    
                                    .. attribute:: protocol_name  (key)
                                    
                                    	Redistributed protocol
                                    	**type**\:  :py:class:`EigrpRedistProto <ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_cfg.EigrpRedistProto>`
                                    
                                    .. attribute:: policy_name
                                    
                                    	Policy name
                                    	**type**\: str
                                    
                                    .. attribute:: policy_specified
                                    
                                    	TRUE if Policy has been specified
                                    	**type**\: bool
                                    
                                    	**mandatory**\: True
                                    
                                    

                                    """

                                    _prefix = 'eigrp-cfg'
                                    _revision = '2018-06-15'

                                    def __init__(self):
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
                                            super(Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Redistributes.RedistributeAsXxTagName, self).__init__()

                                        self.yang_name = "redistribute-as-xx-tag-name"
                                        self.yang_parent_name = "redistributes"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = ['as_xx','tag_name','protocol_name']
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('as_xx', (YLeaf(YType.uint32, 'as-xx'), ['int'])),
                                            ('tag_name', (YLeaf(YType.str, 'tag-name'), ['str'])),
                                            ('protocol_name', (YLeaf(YType.enumeration, 'protocol-name'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_cfg', 'EigrpRedistProto', '')])),
                                            ('policy_name', (YLeaf(YType.str, 'policy-name'), ['str'])),
                                            ('policy_specified', (YLeaf(YType.boolean, 'policy-specified'), ['bool'])),
                                        ])
                                        self.as_xx = None
                                        self.tag_name = None
                                        self.protocol_name = None
                                        self.policy_name = None
                                        self.policy_specified = None
                                        self._segment_path = lambda: "redistribute-as-xx-tag-name" + "[as-xx='" + str(self.as_xx) + "']" + "[tag-name='" + str(self.tag_name) + "']" + "[protocol-name='" + str(self.protocol_name) + "']"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Redistributes.RedistributeAsXxTagName, ['as_xx', 'tag_name', 'protocol_name', 'policy_name', 'policy_specified'], name, value)

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_eigrp_cfg as meta
                                        return meta._meta_table['Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Redistributes.RedistributeAsXxTagName']['meta_info']


                                class RedistributeAsYyTagName(_Entity_):
                                    """
                                    Redistribute another protocol
                                    
                                    .. attribute:: as_yy  (key)
                                    
                                    	2\-byte or 4\-byte BGP AS Number
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: tag_name  (key)
                                    
                                    	OSPF/OSPFv3/ISIS/OnePK Application tag name
                                    	**type**\: str
                                    
                                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                                    
                                    .. attribute:: protocol_name  (key)
                                    
                                    	Redistributed protocol
                                    	**type**\:  :py:class:`EigrpRedistProto <ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_cfg.EigrpRedistProto>`
                                    
                                    .. attribute:: policy_name
                                    
                                    	Policy name
                                    	**type**\: str
                                    
                                    .. attribute:: policy_specified
                                    
                                    	TRUE if Policy has been specified
                                    	**type**\: bool
                                    
                                    	**mandatory**\: True
                                    
                                    

                                    """

                                    _prefix = 'eigrp-cfg'
                                    _revision = '2018-06-15'

                                    def __init__(self):
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
                                            super(Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Redistributes.RedistributeAsYyTagName, self).__init__()

                                        self.yang_name = "redistribute-as-yy-tag-name"
                                        self.yang_parent_name = "redistributes"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = ['as_yy','tag_name','protocol_name']
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('as_yy', (YLeaf(YType.uint32, 'as-yy'), ['int'])),
                                            ('tag_name', (YLeaf(YType.str, 'tag-name'), ['str'])),
                                            ('protocol_name', (YLeaf(YType.enumeration, 'protocol-name'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_cfg', 'EigrpRedistProto', '')])),
                                            ('policy_name', (YLeaf(YType.str, 'policy-name'), ['str'])),
                                            ('policy_specified', (YLeaf(YType.boolean, 'policy-specified'), ['bool'])),
                                        ])
                                        self.as_yy = None
                                        self.tag_name = None
                                        self.protocol_name = None
                                        self.policy_name = None
                                        self.policy_specified = None
                                        self._segment_path = lambda: "redistribute-as-yy-tag-name" + "[as-yy='" + str(self.as_yy) + "']" + "[tag-name='" + str(self.tag_name) + "']" + "[protocol-name='" + str(self.protocol_name) + "']"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Redistributes.RedistributeAsYyTagName, ['as_yy', 'tag_name', 'protocol_name', 'policy_name', 'policy_specified'], name, value)

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_eigrp_cfg as meta
                                        return meta._meta_table['Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Redistributes.RedistributeAsYyTagName']['meta_info']


                                class RedistributeAsXxAsYyTagName(_Entity_):
                                    """
                                    Redistribute another protocol
                                    
                                    .. attribute:: as_xx  (key)
                                    
                                    	Higher sixteen bits of 4\-byte BGP AS number
                                    	**type**\: int
                                    
                                    	**range:** 0..65535
                                    
                                    .. attribute:: as_yy  (key)
                                    
                                    	2\-byte or 4\-byte BGP AS Number
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: tag_name  (key)
                                    
                                    	OSPF/OSPFv3/ISIS/OnePK Application tag name
                                    	**type**\: str
                                    
                                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                                    
                                    .. attribute:: protocol_name  (key)
                                    
                                    	Redistributed protocol
                                    	**type**\:  :py:class:`EigrpRedistProto <ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_cfg.EigrpRedistProto>`
                                    
                                    .. attribute:: policy_name
                                    
                                    	Policy name
                                    	**type**\: str
                                    
                                    .. attribute:: policy_specified
                                    
                                    	TRUE if Policy has been specified
                                    	**type**\: bool
                                    
                                    	**mandatory**\: True
                                    
                                    

                                    """

                                    _prefix = 'eigrp-cfg'
                                    _revision = '2018-06-15'

                                    def __init__(self):
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
                                            super(Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Redistributes.RedistributeAsXxAsYyTagName, self).__init__()

                                        self.yang_name = "redistribute-as-xx-as-yy-tag-name"
                                        self.yang_parent_name = "redistributes"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = ['as_xx','as_yy','tag_name','protocol_name']
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('as_xx', (YLeaf(YType.uint32, 'as-xx'), ['int'])),
                                            ('as_yy', (YLeaf(YType.uint32, 'as-yy'), ['int'])),
                                            ('tag_name', (YLeaf(YType.str, 'tag-name'), ['str'])),
                                            ('protocol_name', (YLeaf(YType.enumeration, 'protocol-name'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_cfg', 'EigrpRedistProto', '')])),
                                            ('policy_name', (YLeaf(YType.str, 'policy-name'), ['str'])),
                                            ('policy_specified', (YLeaf(YType.boolean, 'policy-specified'), ['bool'])),
                                        ])
                                        self.as_xx = None
                                        self.as_yy = None
                                        self.tag_name = None
                                        self.protocol_name = None
                                        self.policy_name = None
                                        self.policy_specified = None
                                        self._segment_path = lambda: "redistribute-as-xx-as-yy-tag-name" + "[as-xx='" + str(self.as_xx) + "']" + "[as-yy='" + str(self.as_yy) + "']" + "[tag-name='" + str(self.tag_name) + "']" + "[protocol-name='" + str(self.protocol_name) + "']"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Redistributes.RedistributeAsXxAsYyTagName, ['as_xx', 'as_yy', 'tag_name', 'protocol_name', 'policy_name', 'policy_specified'], name, value)

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_eigrp_cfg as meta
                                        return meta._meta_table['Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Redistributes.RedistributeAsXxAsYyTagName']['meta_info']

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_eigrp_cfg as meta
                                    return meta._meta_table['Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Redistributes']['meta_info']


                            class FilterPolicies(_Entity_):
                                """
                                Inbound and outbound filter policies
                                
                                .. attribute:: filter_policy
                                
                                	Inbound/outbound policies
                                	**type**\: list of  		 :py:class:`FilterPolicy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_cfg.Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.FilterPolicies.FilterPolicy>`
                                
                                

                                """

                                _prefix = 'eigrp-cfg'
                                _revision = '2018-06-15'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.FilterPolicies, self).__init__()

                                    self.yang_name = "filter-policies"
                                    self.yang_parent_name = "af"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("filter-policy", ("filter_policy", Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.FilterPolicies.FilterPolicy))])
                                    self._leafs = OrderedDict()

                                    self.filter_policy = YList(self)
                                    self._segment_path = lambda: "filter-policies"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.FilterPolicies, [], name, value)


                                class FilterPolicy(_Entity_):
                                    """
                                    Inbound/outbound policies
                                    
                                    .. attribute:: direction  (key)
                                    
                                    	Direction (in or out)
                                    	**type**\:  :py:class:`EigrpDir <ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_cfg.EigrpDir>`
                                    
                                    .. attribute:: policy_name
                                    
                                    	Policy name
                                    	**type**\: str
                                    
                                    	**mandatory**\: True
                                    
                                    

                                    """

                                    _prefix = 'eigrp-cfg'
                                    _revision = '2018-06-15'

                                    def __init__(self):
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
                                            super(Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.FilterPolicies.FilterPolicy, self).__init__()

                                        self.yang_name = "filter-policy"
                                        self.yang_parent_name = "filter-policies"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = ['direction']
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('direction', (YLeaf(YType.enumeration, 'direction'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_cfg', 'EigrpDir', '')])),
                                            ('policy_name', (YLeaf(YType.str, 'policy-name'), ['str'])),
                                        ])
                                        self.direction = None
                                        self.policy_name = None
                                        self._segment_path = lambda: "filter-policy" + "[direction='" + str(self.direction) + "']"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.FilterPolicies.FilterPolicy, ['direction', 'policy_name'], name, value)

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_eigrp_cfg as meta
                                        return meta._meta_table['Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.FilterPolicies.FilterPolicy']['meta_info']

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_eigrp_cfg as meta
                                    return meta._meta_table['Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.FilterPolicies']['meta_info']


                            class DefaultMetric(_Entity_):
                                """
                                Set metric of redistributed routes
                                
                                .. attribute:: bandwidth
                                
                                	Bandwidth in Kbits per second
                                	**type**\: int
                                
                                	**range:** 1..4294967295
                                
                                	**units**\: kbit/s
                                
                                .. attribute:: delay
                                
                                	Delay metric, in 10 microsecond units
                                	**type**\: int
                                
                                	**range:** 1..4294967295
                                
                                .. attribute:: reliability
                                
                                	Reliability metric where 255 is 100% reliable
                                	**type**\: int
                                
                                	**range:** 0..255
                                
                                .. attribute:: load
                                
                                	Effective bandwidth metric (Loading) where 255 is 100% loaded
                                	**type**\: int
                                
                                	**range:** 1..255
                                
                                .. attribute:: mtu
                                
                                	Maximum Transmission Unit metric of the path
                                	**type**\: int
                                
                                	**range:** 1..65535
                                
                                

                                """

                                _prefix = 'eigrp-cfg'
                                _revision = '2018-06-15'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.DefaultMetric, self).__init__()

                                    self.yang_name = "default-metric"
                                    self.yang_parent_name = "af"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('bandwidth', (YLeaf(YType.uint32, 'bandwidth'), ['int'])),
                                        ('delay', (YLeaf(YType.uint32, 'delay'), ['int'])),
                                        ('reliability', (YLeaf(YType.uint32, 'reliability'), ['int'])),
                                        ('load', (YLeaf(YType.uint32, 'load'), ['int'])),
                                        ('mtu', (YLeaf(YType.uint32, 'mtu'), ['int'])),
                                    ])
                                    self.bandwidth = None
                                    self.delay = None
                                    self.reliability = None
                                    self.load = None
                                    self.mtu = None
                                    self._segment_path = lambda: "default-metric"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.DefaultMetric, ['bandwidth', 'delay', 'reliability', 'load', 'mtu'], name, value)

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_eigrp_cfg as meta
                                    return meta._meta_table['Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.DefaultMetric']['meta_info']


                            class Metrics(_Entity_):
                                """
                                List of metric change behaviours
                                
                                .. attribute:: metric
                                
                                	Modify EIGRP routing metrics and parameters
                                	**type**\: list of  		 :py:class:`Metric <ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_cfg.Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Metrics.Metric>`
                                
                                

                                """

                                _prefix = 'eigrp-cfg'
                                _revision = '2018-06-15'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Metrics, self).__init__()

                                    self.yang_name = "metrics"
                                    self.yang_parent_name = "af"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("metric", ("metric", Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Metrics.Metric))])
                                    self._leafs = OrderedDict()

                                    self.metric = YList(self)
                                    self._segment_path = lambda: "metrics"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Metrics, [], name, value)


                                class Metric(_Entity_):
                                    """
                                    Modify EIGRP routing metrics and parameters
                                    
                                    .. attribute:: metric_name  (key)
                                    
                                    	Type of metric change
                                    	**type**\:  :py:class:`EigrpMet <ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_cfg.EigrpMet>`
                                    
                                    .. attribute:: max_hops
                                    
                                    	Hop count
                                    	**type**\: int
                                    
                                    	**range:** 1..255
                                    
                                    .. attribute:: tos
                                    
                                    	Type of Service (Only TOS 0 supported)
                                    	**type**\: int
                                    
                                    	**range:** 0..0
                                    
                                    .. attribute:: k1
                                    
                                    	K1
                                    	**type**\: int
                                    
                                    	**range:** 0..255
                                    
                                    .. attribute:: k2
                                    
                                    	K2
                                    	**type**\: int
                                    
                                    	**range:** 0..255
                                    
                                    .. attribute:: k3
                                    
                                    	K3
                                    	**type**\: int
                                    
                                    	**range:** 0..255
                                    
                                    .. attribute:: k4
                                    
                                    	K4
                                    	**type**\: int
                                    
                                    	**range:** 0..255
                                    
                                    .. attribute:: k5
                                    
                                    	K5
                                    	**type**\: int
                                    
                                    	**range:** 0..255
                                    
                                    .. attribute:: k6
                                    
                                    	K6
                                    	**type**\: int
                                    
                                    	**range:** 0..255
                                    
                                    .. attribute:: rib_scale
                                    
                                    	RIB scale
                                    	**type**\: int
                                    
                                    	**range:** 1..4294967295
                                    
                                    .. attribute:: metric_version
                                    
                                    	Metric version
                                    	**type**\:  :py:class:`EigrpMetricVersion <ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_cfg.EigrpMetricVersion>`
                                    
                                    

                                    """

                                    _prefix = 'eigrp-cfg'
                                    _revision = '2018-06-15'

                                    def __init__(self):
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
                                            super(Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Metrics.Metric, self).__init__()

                                        self.yang_name = "metric"
                                        self.yang_parent_name = "metrics"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = ['metric_name']
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('metric_name', (YLeaf(YType.enumeration, 'metric-name'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_cfg', 'EigrpMet', '')])),
                                            ('max_hops', (YLeaf(YType.uint32, 'max-hops'), ['int'])),
                                            ('tos', (YLeaf(YType.uint32, 'tos'), ['int'])),
                                            ('k1', (YLeaf(YType.uint32, 'k1'), ['int'])),
                                            ('k2', (YLeaf(YType.uint32, 'k2'), ['int'])),
                                            ('k3', (YLeaf(YType.uint32, 'k3'), ['int'])),
                                            ('k4', (YLeaf(YType.uint32, 'k4'), ['int'])),
                                            ('k5', (YLeaf(YType.uint32, 'k5'), ['int'])),
                                            ('k6', (YLeaf(YType.uint32, 'k6'), ['int'])),
                                            ('rib_scale', (YLeaf(YType.uint32, 'rib-scale'), ['int'])),
                                            ('metric_version', (YLeaf(YType.enumeration, 'metric-version'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_cfg', 'EigrpMetricVersion', '')])),
                                        ])
                                        self.metric_name = None
                                        self.max_hops = None
                                        self.tos = None
                                        self.k1 = None
                                        self.k2 = None
                                        self.k3 = None
                                        self.k4 = None
                                        self.k5 = None
                                        self.k6 = None
                                        self.rib_scale = None
                                        self.metric_version = None
                                        self._segment_path = lambda: "metric" + "[metric-name='" + str(self.metric_name) + "']"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Metrics.Metric, ['metric_name', 'max_hops', 'tos', 'k1', 'k2', 'k3', 'k4', 'k5', 'k6', 'rib_scale', 'metric_version'], name, value)

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_eigrp_cfg as meta
                                        return meta._meta_table['Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Metrics.Metric']['meta_info']

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_eigrp_cfg as meta
                                    return meta._meta_table['Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Metrics']['meta_info']


                            class Timers(_Entity_):
                                """
                                List of timer configurations
                                
                                .. attribute:: timer
                                
                                	Configure EIGRP timers
                                	**type**\: list of  		 :py:class:`Timer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_cfg.Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Timers.Timer>`
                                
                                

                                """

                                _prefix = 'eigrp-cfg'
                                _revision = '2018-06-15'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Timers, self).__init__()

                                    self.yang_name = "timers"
                                    self.yang_parent_name = "af"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("timer", ("timer", Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Timers.Timer))])
                                    self._leafs = OrderedDict()

                                    self.timer = YList(self)
                                    self._segment_path = lambda: "timers"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Timers, [], name, value)


                                class Timer(_Entity_):
                                    """
                                    Configure EIGRP timers
                                    
                                    .. attribute:: timer_type  (key)
                                    
                                    	Type of timer
                                    	**type**\:  :py:class:`EigrpTimer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_cfg.EigrpTimer>`
                                    
                                    .. attribute:: active_time
                                    
                                    	Active Time (in seconds)
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    	**units**\: second
                                    
                                    .. attribute:: hold_time
                                    
                                    	Hold time (in seconds)
                                    	**type**\: int
                                    
                                    	**range:** 20..6000
                                    
                                    	**units**\: second
                                    
                                    .. attribute:: signal_time
                                    
                                    	Signal time (in seconds)
                                    	**type**\: int
                                    
                                    	**range:** 10..30
                                    
                                    	**units**\: second
                                    
                                    .. attribute:: converge_time
                                    
                                    	Converge time (in seconds)
                                    	**type**\: int
                                    
                                    	**range:** 60..5000
                                    
                                    	**units**\: second
                                    
                                    

                                    """

                                    _prefix = 'eigrp-cfg'
                                    _revision = '2018-06-15'

                                    def __init__(self):
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
                                            super(Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Timers.Timer, self).__init__()

                                        self.yang_name = "timer"
                                        self.yang_parent_name = "timers"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = ['timer_type']
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('timer_type', (YLeaf(YType.enumeration, 'timer-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_cfg', 'EigrpTimer', '')])),
                                            ('active_time', (YLeaf(YType.uint32, 'active-time'), ['int'])),
                                            ('hold_time', (YLeaf(YType.uint32, 'hold-time'), ['int'])),
                                            ('signal_time', (YLeaf(YType.uint32, 'signal-time'), ['int'])),
                                            ('converge_time', (YLeaf(YType.uint32, 'converge-time'), ['int'])),
                                        ])
                                        self.timer_type = None
                                        self.active_time = None
                                        self.hold_time = None
                                        self.signal_time = None
                                        self.converge_time = None
                                        self._segment_path = lambda: "timer" + "[timer-type='" + str(self.timer_type) + "']"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Timers.Timer, ['timer_type', 'active_time', 'hold_time', 'signal_time', 'converge_time'], name, value)

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_eigrp_cfg as meta
                                        return meta._meta_table['Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Timers.Timer']['meta_info']

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_eigrp_cfg as meta
                                    return meta._meta_table['Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Timers']['meta_info']


                            class DefaultAccepts(_Entity_):
                                """
                                Candidate default policy table
                                
                                .. attribute:: default_accept
                                
                                	Candidate default behaviour
                                	**type**\: list of  		 :py:class:`DefaultAccept <ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_cfg.Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.DefaultAccepts.DefaultAccept>`
                                
                                

                                """

                                _prefix = 'eigrp-cfg'
                                _revision = '2018-06-15'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.DefaultAccepts, self).__init__()

                                    self.yang_name = "default-accepts"
                                    self.yang_parent_name = "af"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("default-accept", ("default_accept", Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.DefaultAccepts.DefaultAccept))])
                                    self._leafs = OrderedDict()

                                    self.default_accept = YList(self)
                                    self._segment_path = lambda: "default-accepts"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.DefaultAccepts, [], name, value)


                                class DefaultAccept(_Entity_):
                                    """
                                    Candidate default behaviour
                                    
                                    .. attribute:: direction  (key)
                                    
                                    	Direction (in or out)
                                    	**type**\:  :py:class:`EigrpDir <ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_cfg.EigrpDir>`
                                    
                                    .. attribute:: policy_name
                                    
                                    	Policy name
                                    	**type**\: str
                                    
                                    .. attribute:: policy_specified
                                    
                                    	TRUE if Policy has been specified
                                    	**type**\: bool
                                    
                                    	**mandatory**\: True
                                    
                                    

                                    """

                                    _prefix = 'eigrp-cfg'
                                    _revision = '2018-06-15'

                                    def __init__(self):
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
                                            super(Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.DefaultAccepts.DefaultAccept, self).__init__()

                                        self.yang_name = "default-accept"
                                        self.yang_parent_name = "default-accepts"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = ['direction']
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('direction', (YLeaf(YType.enumeration, 'direction'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_cfg', 'EigrpDir', '')])),
                                            ('policy_name', (YLeaf(YType.str, 'policy-name'), ['str'])),
                                            ('policy_specified', (YLeaf(YType.boolean, 'policy-specified'), ['bool'])),
                                        ])
                                        self.direction = None
                                        self.policy_name = None
                                        self.policy_specified = None
                                        self._segment_path = lambda: "default-accept" + "[direction='" + str(self.direction) + "']"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.DefaultAccepts.DefaultAccept, ['direction', 'policy_name', 'policy_specified'], name, value)

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_eigrp_cfg as meta
                                        return meta._meta_table['Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.DefaultAccepts.DefaultAccept']['meta_info']

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_eigrp_cfg as meta
                                    return meta._meta_table['Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.DefaultAccepts']['meta_info']


                            class Interfaces(_Entity_):
                                """
                                List of interfaces
                                
                                .. attribute:: interface
                                
                                	Configuration for an Interface.Deletion of this object also causes deletion of all objectsunder 'Interface' associated with this interface instance
                                	**type**\: list of  		 :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_cfg.Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Interfaces.Interface>`
                                
                                

                                """

                                _prefix = 'eigrp-cfg'
                                _revision = '2018-06-15'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Interfaces, self).__init__()

                                    self.yang_name = "interfaces"
                                    self.yang_parent_name = "af"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("interface", ("interface", Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Interfaces.Interface))])
                                    self._leafs = OrderedDict()

                                    self.interface = YList(self)
                                    self._segment_path = lambda: "interfaces"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Interfaces, [], name, value)


                                class Interface(_Entity_):
                                    """
                                    Configuration for an Interface.Deletion of this
                                    object also causes deletion of all objectsunder
                                    'Interface' associated with this interface
                                    instance.
                                    
                                    .. attribute:: interface_name  (key)
                                    
                                    	Interface name
                                    	**type**\: str
                                    
                                    	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                                    
                                    .. attribute:: interface_metric
                                    
                                    	Metric
                                    	**type**\:  :py:class:`InterfaceMetric <ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_cfg.Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Interfaces.Interface.InterfaceMetric>`
                                    
                                    .. attribute:: remote_neighbor
                                    
                                    	Remote\-Neighbors enabled, default is 65535
                                    	**type**\:  :py:class:`RemoteNeighbor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_cfg.Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Interfaces.Interface.RemoteNeighbor>`
                                    
                                    	**presence node**\: True
                                    
                                    .. attribute:: bfd
                                    
                                    	Configure BFD parameters
                                    	**type**\:  :py:class:`Bfd <ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_cfg.Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Interfaces.Interface.Bfd>`
                                    
                                    .. attribute:: site_of_origin
                                    
                                    	Configure Site\-of\-origin
                                    	**type**\:  :py:class:`SiteOfOrigin <ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_cfg.Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Interfaces.Interface.SiteOfOrigin>`
                                    
                                    .. attribute:: authentication
                                    
                                    	Authentication configuration
                                    	**type**\:  :py:class:`Authentication <ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_cfg.Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Interfaces.Interface.Authentication>`
                                    
                                    .. attribute:: summary_addresses
                                    
                                    	List of summary addresses under this interface
                                    	**type**\:  :py:class:`SummaryAddresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_cfg.Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Interfaces.Interface.SummaryAddresses>`
                                    
                                    .. attribute:: interface_filter_policies
                                    
                                    	List of filter policies
                                    	**type**\:  :py:class:`InterfaceFilterPolicies <ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_cfg.Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Interfaces.Interface.InterfaceFilterPolicies>`
                                    
                                    .. attribute:: interface_static_neighbors
                                    
                                    	List of Neighbors
                                    	**type**\:  :py:class:`InterfaceStaticNeighbors <ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_cfg.Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Interfaces.Interface.InterfaceStaticNeighbors>`
                                    
                                    .. attribute:: hold_time
                                    
                                    	Neighbor hold time (in seconds)
                                    	**type**\: int
                                    
                                    	**range:** 1..65535
                                    
                                    	**units**\: second
                                    
                                    .. attribute:: bandwidth_percent
                                    
                                    	Bandwidth limit
                                    	**type**\: int
                                    
                                    	**range:** 1..999999
                                    
                                    	**units**\: percentage
                                    
                                    .. attribute:: passive_interface
                                    
                                    	Suppress routing updates on an interface
                                    	**type**\: bool
                                    
                                    .. attribute:: hello_interval
                                    
                                    	Interval (in seconds)
                                    	**type**\: int
                                    
                                    	**range:** 1..65535
                                    
                                    	**units**\: second
                                    
                                    .. attribute:: next_hop_self
                                    
                                    	Disable next\-hop\-self
                                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                                    
                                    .. attribute:: enable
                                    
                                    	Enable Interface configuration
                                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                                    
                                    .. attribute:: split_horizon
                                    
                                    	Configure split horizon behaviour
                                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                                    
                                    

                                    """

                                    _prefix = 'eigrp-cfg'
                                    _revision = '2018-06-15'

                                    def __init__(self):
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
                                            super(Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Interfaces.Interface, self).__init__()

                                        self.yang_name = "interface"
                                        self.yang_parent_name = "interfaces"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = ['interface_name']
                                        self._child_classes = OrderedDict([("interface-metric", ("interface_metric", Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Interfaces.Interface.InterfaceMetric)), ("remote-neighbor", ("remote_neighbor", Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Interfaces.Interface.RemoteNeighbor)), ("bfd", ("bfd", Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Interfaces.Interface.Bfd)), ("site-of-origin", ("site_of_origin", Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Interfaces.Interface.SiteOfOrigin)), ("authentication", ("authentication", Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Interfaces.Interface.Authentication)), ("summary-addresses", ("summary_addresses", Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Interfaces.Interface.SummaryAddresses)), ("interface-filter-policies", ("interface_filter_policies", Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Interfaces.Interface.InterfaceFilterPolicies)), ("interface-static-neighbors", ("interface_static_neighbors", Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Interfaces.Interface.InterfaceStaticNeighbors))])
                                        self._leafs = OrderedDict([
                                            ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                                            ('hold_time', (YLeaf(YType.uint32, 'hold-time'), ['int'])),
                                            ('bandwidth_percent', (YLeaf(YType.uint32, 'bandwidth-percent'), ['int'])),
                                            ('passive_interface', (YLeaf(YType.boolean, 'passive-interface'), ['bool'])),
                                            ('hello_interval', (YLeaf(YType.uint32, 'hello-interval'), ['int'])),
                                            ('next_hop_self', (YLeaf(YType.empty, 'next-hop-self'), ['Empty'])),
                                            ('enable', (YLeaf(YType.empty, 'enable'), ['Empty'])),
                                            ('split_horizon', (YLeaf(YType.empty, 'split-horizon'), ['Empty'])),
                                        ])
                                        self.interface_name = None
                                        self.hold_time = None
                                        self.bandwidth_percent = None
                                        self.passive_interface = None
                                        self.hello_interval = None
                                        self.next_hop_self = None
                                        self.enable = None
                                        self.split_horizon = None

                                        self.interface_metric = Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Interfaces.Interface.InterfaceMetric()
                                        self.interface_metric.parent = self
                                        self._children_name_map["interface_metric"] = "interface-metric"

                                        self.remote_neighbor = None
                                        self._children_name_map["remote_neighbor"] = "remote-neighbor"

                                        self.bfd = Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Interfaces.Interface.Bfd()
                                        self.bfd.parent = self
                                        self._children_name_map["bfd"] = "bfd"

                                        self.site_of_origin = Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Interfaces.Interface.SiteOfOrigin()
                                        self.site_of_origin.parent = self
                                        self._children_name_map["site_of_origin"] = "site-of-origin"

                                        self.authentication = Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Interfaces.Interface.Authentication()
                                        self.authentication.parent = self
                                        self._children_name_map["authentication"] = "authentication"

                                        self.summary_addresses = Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Interfaces.Interface.SummaryAddresses()
                                        self.summary_addresses.parent = self
                                        self._children_name_map["summary_addresses"] = "summary-addresses"

                                        self.interface_filter_policies = Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Interfaces.Interface.InterfaceFilterPolicies()
                                        self.interface_filter_policies.parent = self
                                        self._children_name_map["interface_filter_policies"] = "interface-filter-policies"

                                        self.interface_static_neighbors = Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Interfaces.Interface.InterfaceStaticNeighbors()
                                        self.interface_static_neighbors.parent = self
                                        self._children_name_map["interface_static_neighbors"] = "interface-static-neighbors"
                                        self._segment_path = lambda: "interface" + "[interface-name='" + str(self.interface_name) + "']"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Interfaces.Interface, ['interface_name', 'hold_time', 'bandwidth_percent', 'passive_interface', 'hello_interval', 'next_hop_self', 'enable', 'split_horizon'], name, value)


                                    class InterfaceMetric(_Entity_):
                                        """
                                        Metric
                                        
                                        .. attribute:: bandwidth
                                        
                                        	Bandwidth in Kbits per second
                                        	**type**\: int
                                        
                                        	**range:** 1..4294967295
                                        
                                        	**units**\: kbit/s
                                        
                                        .. attribute:: delay
                                        
                                        	Delay metric, in 10 microsecond units (default) or picosecond units
                                        	**type**\: int
                                        
                                        	**range:** 1..4294967295
                                        
                                        .. attribute:: delay_unit
                                        
                                        	Delay unit
                                        	**type**\:  :py:class:`EigrpDelayUnit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_cfg.EigrpDelayUnit>`
                                        
                                        .. attribute:: reliability
                                        
                                        	Reliability metric where 255 is 100% reliable
                                        	**type**\: int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: load
                                        
                                        	Effective bandwidth metric (Loading) where 255 is 100% loaded
                                        	**type**\: int
                                        
                                        	**range:** 1..255
                                        
                                        

                                        """

                                        _prefix = 'eigrp-cfg'
                                        _revision = '2018-06-15'

                                        def __init__(self):
                                            if sys.version_info > (3,):
                                                super().__init__()
                                            else:
                                                super(Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Interfaces.Interface.InterfaceMetric, self).__init__()

                                            self.yang_name = "interface-metric"
                                            self.yang_parent_name = "interface"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('bandwidth', (YLeaf(YType.uint32, 'bandwidth'), ['int'])),
                                                ('delay', (YLeaf(YType.uint32, 'delay'), ['int'])),
                                                ('delay_unit', (YLeaf(YType.enumeration, 'delay-unit'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_cfg', 'EigrpDelayUnit', '')])),
                                                ('reliability', (YLeaf(YType.uint32, 'reliability'), ['int'])),
                                                ('load', (YLeaf(YType.uint32, 'load'), ['int'])),
                                            ])
                                            self.bandwidth = None
                                            self.delay = None
                                            self.delay_unit = None
                                            self.reliability = None
                                            self.load = None
                                            self._segment_path = lambda: "interface-metric"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Interfaces.Interface.InterfaceMetric, ['bandwidth', 'delay', 'delay_unit', 'reliability', 'load'], name, value)

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_eigrp_cfg as meta
                                            return meta._meta_table['Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Interfaces.Interface.InterfaceMetric']['meta_info']


                                    class RemoteNeighbor(_Entity_):
                                        """
                                        Remote\-Neighbors enabled, default is 65535
                                        
                                        .. attribute:: enable
                                        
                                        	Enable Remote neighbor unicast\-listen
                                        	**type**\: bool
                                        
                                        	**mandatory**\: True
                                        
                                        .. attribute:: allow_list
                                        
                                        	Policy name
                                        	**type**\: str
                                        
                                        .. attribute:: max_neighbors
                                        
                                        	Neighbor count
                                        	**type**\: int
                                        
                                        	**range:** 1..65535
                                        
                                        

                                        This class is a :ref:`presence class<presence-class>`

                                        """

                                        _prefix = 'eigrp-cfg'
                                        _revision = '2018-06-15'

                                        def __init__(self):
                                            if sys.version_info > (3,):
                                                super().__init__()
                                            else:
                                                super(Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Interfaces.Interface.RemoteNeighbor, self).__init__()

                                            self.yang_name = "remote-neighbor"
                                            self.yang_parent_name = "interface"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self.is_presence_container = True
                                            self._leafs = OrderedDict([
                                                ('enable', (YLeaf(YType.boolean, 'enable'), ['bool'])),
                                                ('allow_list', (YLeaf(YType.str, 'allow-list'), ['str'])),
                                                ('max_neighbors', (YLeaf(YType.uint32, 'max-neighbors'), ['int'])),
                                            ])
                                            self.enable = None
                                            self.allow_list = None
                                            self.max_neighbors = None
                                            self._segment_path = lambda: "remote-neighbor"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Interfaces.Interface.RemoteNeighbor, ['enable', 'allow_list', 'max_neighbors'], name, value)

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_eigrp_cfg as meta
                                            return meta._meta_table['Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Interfaces.Interface.RemoteNeighbor']['meta_info']


                                    class Bfd(_Entity_):
                                        """
                                        Configure BFD parameters
                                        
                                        .. attribute:: fast_detect
                                        
                                        	Enable BFD fast detection
                                        	**type**\: bool
                                        
                                        .. attribute:: detection_multiplier
                                        
                                        	Detect multiplier
                                        	**type**\: int
                                        
                                        	**range:** 2..50
                                        
                                        .. attribute:: interval
                                        
                                        	Hello interval in milli\-seconds
                                        	**type**\: int
                                        
                                        	**range:** 15..3000
                                        
                                        	**units**\: millisecond
                                        
                                        

                                        """

                                        _prefix = 'eigrp-cfg'
                                        _revision = '2018-06-15'

                                        def __init__(self):
                                            if sys.version_info > (3,):
                                                super().__init__()
                                            else:
                                                super(Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Interfaces.Interface.Bfd, self).__init__()

                                            self.yang_name = "bfd"
                                            self.yang_parent_name = "interface"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('fast_detect', (YLeaf(YType.boolean, 'fast-detect'), ['bool'])),
                                                ('detection_multiplier', (YLeaf(YType.uint32, 'detection-multiplier'), ['int'])),
                                                ('interval', (YLeaf(YType.uint32, 'interval'), ['int'])),
                                            ])
                                            self.fast_detect = None
                                            self.detection_multiplier = None
                                            self.interval = None
                                            self._segment_path = lambda: "bfd"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Interfaces.Interface.Bfd, ['fast_detect', 'detection_multiplier', 'interval'], name, value)

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_eigrp_cfg as meta
                                            return meta._meta_table['Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Interfaces.Interface.Bfd']['meta_info']


                                    class SiteOfOrigin(_Entity_):
                                        """
                                        Configure Site\-of\-origin
                                        
                                        .. attribute:: type
                                        
                                        	SoO type
                                        	**type**\:  :py:class:`EigrpSoo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_cfg.EigrpSoo>`
                                        
                                        .. attribute:: as_xx
                                        
                                        	Higher sixteen bits of 4\-byte BGP AS Number
                                        	**type**\: int
                                        
                                        	**range:** 0..65535
                                        
                                        .. attribute:: as_yy
                                        
                                        	2\-byte or 4\-byte BGP AS Number
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: index
                                        
                                        	AS Number Index
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: address
                                        
                                        	IPv4 address
                                        	**type**\: str
                                        
                                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                        
                                        .. attribute:: address_index
                                        
                                        	IPv4 address index
                                        	**type**\: int
                                        
                                        	**range:** 0..65535
                                        
                                        

                                        """

                                        _prefix = 'eigrp-cfg'
                                        _revision = '2018-06-15'

                                        def __init__(self):
                                            if sys.version_info > (3,):
                                                super().__init__()
                                            else:
                                                super(Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Interfaces.Interface.SiteOfOrigin, self).__init__()

                                            self.yang_name = "site-of-origin"
                                            self.yang_parent_name = "interface"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('type', (YLeaf(YType.enumeration, 'type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_cfg', 'EigrpSoo', '')])),
                                                ('as_xx', (YLeaf(YType.uint32, 'as-xx'), ['int'])),
                                                ('as_yy', (YLeaf(YType.uint32, 'as-yy'), ['int'])),
                                                ('index', (YLeaf(YType.uint32, 'index'), ['int'])),
                                                ('address', (YLeaf(YType.str, 'address'), ['str'])),
                                                ('address_index', (YLeaf(YType.uint32, 'address-index'), ['int'])),
                                            ])
                                            self.type = None
                                            self.as_xx = None
                                            self.as_yy = None
                                            self.index = None
                                            self.address = None
                                            self.address_index = None
                                            self._segment_path = lambda: "site-of-origin"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Interfaces.Interface.SiteOfOrigin, ['type', 'as_xx', 'as_yy', 'index', 'address', 'address_index'], name, value)

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_eigrp_cfg as meta
                                            return meta._meta_table['Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Interfaces.Interface.SiteOfOrigin']['meta_info']


                                    class Authentication(_Entity_):
                                        """
                                        Authentication configuration
                                        
                                        .. attribute:: keychain
                                        
                                        	Authentication keychain configuration
                                        	**type**\: str
                                        
                                        

                                        """

                                        _prefix = 'eigrp-cfg'
                                        _revision = '2018-06-15'

                                        def __init__(self):
                                            if sys.version_info > (3,):
                                                super().__init__()
                                            else:
                                                super(Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Interfaces.Interface.Authentication, self).__init__()

                                            self.yang_name = "authentication"
                                            self.yang_parent_name = "interface"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('keychain', (YLeaf(YType.str, 'keychain'), ['str'])),
                                            ])
                                            self.keychain = None
                                            self._segment_path = lambda: "authentication"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Interfaces.Interface.Authentication, ['keychain'], name, value)

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_eigrp_cfg as meta
                                            return meta._meta_table['Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Interfaces.Interface.Authentication']['meta_info']


                                    class SummaryAddresses(_Entity_):
                                        """
                                        List of summary addresses under this interface
                                        
                                        .. attribute:: summary_address
                                        
                                        	Summary address
                                        	**type**\: list of  		 :py:class:`SummaryAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_cfg.Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Interfaces.Interface.SummaryAddresses.SummaryAddress>`
                                        
                                        

                                        """

                                        _prefix = 'eigrp-cfg'
                                        _revision = '2018-06-15'

                                        def __init__(self):
                                            if sys.version_info > (3,):
                                                super().__init__()
                                            else:
                                                super(Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Interfaces.Interface.SummaryAddresses, self).__init__()

                                            self.yang_name = "summary-addresses"
                                            self.yang_parent_name = "interface"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([("summary-address", ("summary_address", Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Interfaces.Interface.SummaryAddresses.SummaryAddress))])
                                            self._leafs = OrderedDict()

                                            self.summary_address = YList(self)
                                            self._segment_path = lambda: "summary-addresses"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Interfaces.Interface.SummaryAddresses, [], name, value)


                                        class SummaryAddress(_Entity_):
                                            """
                                            Summary address
                                            
                                            .. attribute:: summary_address_addr  (key)
                                            
                                            	Summary Prefix (address part)
                                            	**type**\: union of the below types:
                                            
                                            		**type**\: str
                                            
                                            			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                            
                                            		**type**\: str
                                            
                                            			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                            
                                            .. attribute:: summary_address_prefix  (key)
                                            
                                            	Summary Prefix (prefix part)
                                            	**type**\: int
                                            
                                            	**range:** 0..128
                                            
                                            .. attribute:: distance
                                            
                                            	Administrative distance
                                            	**type**\: int
                                            
                                            	**range:** 1..255
                                            
                                            	**mandatory**\: True
                                            
                                            

                                            """

                                            _prefix = 'eigrp-cfg'
                                            _revision = '2018-06-15'

                                            def __init__(self):
                                                if sys.version_info > (3,):
                                                    super().__init__()
                                                else:
                                                    super(Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Interfaces.Interface.SummaryAddresses.SummaryAddress, self).__init__()

                                                self.yang_name = "summary-address"
                                                self.yang_parent_name = "summary-addresses"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = ['summary_address_addr','summary_address_prefix']
                                                self._child_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('summary_address_addr', (YLeaf(YType.str, 'summary-address-addr'), ['str','str'])),
                                                    ('summary_address_prefix', (YLeaf(YType.uint16, 'summary-address-prefix'), ['int'])),
                                                    ('distance', (YLeaf(YType.uint32, 'distance'), ['int'])),
                                                ])
                                                self.summary_address_addr = None
                                                self.summary_address_prefix = None
                                                self.distance = None
                                                self._segment_path = lambda: "summary-address" + "[summary-address-addr='" + str(self.summary_address_addr) + "']" + "[summary-address-prefix='" + str(self.summary_address_prefix) + "']"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Interfaces.Interface.SummaryAddresses.SummaryAddress, ['summary_address_addr', 'summary_address_prefix', 'distance'], name, value)

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_eigrp_cfg as meta
                                                return meta._meta_table['Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Interfaces.Interface.SummaryAddresses.SummaryAddress']['meta_info']

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_eigrp_cfg as meta
                                            return meta._meta_table['Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Interfaces.Interface.SummaryAddresses']['meta_info']


                                    class InterfaceFilterPolicies(_Entity_):
                                        """
                                        List of filter policies
                                        
                                        .. attribute:: interface_filter_policy
                                        
                                        	none
                                        	**type**\: list of  		 :py:class:`InterfaceFilterPolicy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_cfg.Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Interfaces.Interface.InterfaceFilterPolicies.InterfaceFilterPolicy>`
                                        
                                        

                                        """

                                        _prefix = 'eigrp-cfg'
                                        _revision = '2018-06-15'

                                        def __init__(self):
                                            if sys.version_info > (3,):
                                                super().__init__()
                                            else:
                                                super(Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Interfaces.Interface.InterfaceFilterPolicies, self).__init__()

                                            self.yang_name = "interface-filter-policies"
                                            self.yang_parent_name = "interface"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([("interface-filter-policy", ("interface_filter_policy", Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Interfaces.Interface.InterfaceFilterPolicies.InterfaceFilterPolicy))])
                                            self._leafs = OrderedDict()

                                            self.interface_filter_policy = YList(self)
                                            self._segment_path = lambda: "interface-filter-policies"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Interfaces.Interface.InterfaceFilterPolicies, [], name, value)


                                        class InterfaceFilterPolicy(_Entity_):
                                            """
                                            none
                                            
                                            .. attribute:: direction  (key)
                                            
                                            	Direction (in or out)
                                            	**type**\:  :py:class:`EigrpDir <ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_cfg.EigrpDir>`
                                            
                                            .. attribute:: policy_name
                                            
                                            	Policy name
                                            	**type**\: str
                                            
                                            	**mandatory**\: True
                                            
                                            

                                            """

                                            _prefix = 'eigrp-cfg'
                                            _revision = '2018-06-15'

                                            def __init__(self):
                                                if sys.version_info > (3,):
                                                    super().__init__()
                                                else:
                                                    super(Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Interfaces.Interface.InterfaceFilterPolicies.InterfaceFilterPolicy, self).__init__()

                                                self.yang_name = "interface-filter-policy"
                                                self.yang_parent_name = "interface-filter-policies"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = ['direction']
                                                self._child_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('direction', (YLeaf(YType.enumeration, 'direction'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_cfg', 'EigrpDir', '')])),
                                                    ('policy_name', (YLeaf(YType.str, 'policy-name'), ['str'])),
                                                ])
                                                self.direction = None
                                                self.policy_name = None
                                                self._segment_path = lambda: "interface-filter-policy" + "[direction='" + str(self.direction) + "']"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Interfaces.Interface.InterfaceFilterPolicies.InterfaceFilterPolicy, ['direction', 'policy_name'], name, value)

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_eigrp_cfg as meta
                                                return meta._meta_table['Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Interfaces.Interface.InterfaceFilterPolicies.InterfaceFilterPolicy']['meta_info']

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_eigrp_cfg as meta
                                            return meta._meta_table['Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Interfaces.Interface.InterfaceFilterPolicies']['meta_info']


                                    class InterfaceStaticNeighbors(_Entity_):
                                        """
                                        List of Neighbors
                                        
                                        .. attribute:: interface_static_neighbor
                                        
                                        	Configure Neighbor
                                        	**type**\: list of  		 :py:class:`InterfaceStaticNeighbor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_cfg.Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Interfaces.Interface.InterfaceStaticNeighbors.InterfaceStaticNeighbor>`
                                        
                                        

                                        """

                                        _prefix = 'eigrp-cfg'
                                        _revision = '2018-06-15'

                                        def __init__(self):
                                            if sys.version_info > (3,):
                                                super().__init__()
                                            else:
                                                super(Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Interfaces.Interface.InterfaceStaticNeighbors, self).__init__()

                                            self.yang_name = "interface-static-neighbors"
                                            self.yang_parent_name = "interface"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([("interface-static-neighbor", ("interface_static_neighbor", Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Interfaces.Interface.InterfaceStaticNeighbors.InterfaceStaticNeighbor))])
                                            self._leafs = OrderedDict()

                                            self.interface_static_neighbor = YList(self)
                                            self._segment_path = lambda: "interface-static-neighbors"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Interfaces.Interface.InterfaceStaticNeighbors, [], name, value)


                                        class InterfaceStaticNeighbor(_Entity_):
                                            """
                                            Configure Neighbor
                                            
                                            .. attribute:: neighbor_address  (key)
                                            
                                            	Neighbor IP address
                                            	**type**\: union of the below types:
                                            
                                            		**type**\: str
                                            
                                            			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                            
                                            		**type**\: str
                                            
                                            			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                            
                                            .. attribute:: max_hops
                                            
                                            	Number of hops
                                            	**type**\: int
                                            
                                            	**range:** 2..100
                                            
                                            	**mandatory**\: True
                                            
                                            

                                            """

                                            _prefix = 'eigrp-cfg'
                                            _revision = '2018-06-15'

                                            def __init__(self):
                                                if sys.version_info > (3,):
                                                    super().__init__()
                                                else:
                                                    super(Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Interfaces.Interface.InterfaceStaticNeighbors.InterfaceStaticNeighbor, self).__init__()

                                                self.yang_name = "interface-static-neighbor"
                                                self.yang_parent_name = "interface-static-neighbors"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = ['neighbor_address']
                                                self._child_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('neighbor_address', (YLeaf(YType.str, 'neighbor-address'), ['str','str'])),
                                                    ('max_hops', (YLeaf(YType.uint32, 'max-hops'), ['int'])),
                                                ])
                                                self.neighbor_address = None
                                                self.max_hops = None
                                                self._segment_path = lambda: "interface-static-neighbor" + "[neighbor-address='" + str(self.neighbor_address) + "']"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Interfaces.Interface.InterfaceStaticNeighbors.InterfaceStaticNeighbor, ['neighbor_address', 'max_hops'], name, value)

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_eigrp_cfg as meta
                                                return meta._meta_table['Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Interfaces.Interface.InterfaceStaticNeighbors.InterfaceStaticNeighbor']['meta_info']

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_eigrp_cfg as meta
                                            return meta._meta_table['Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Interfaces.Interface.InterfaceStaticNeighbors']['meta_info']

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_eigrp_cfg as meta
                                        return meta._meta_table['Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Interfaces.Interface']['meta_info']

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_eigrp_cfg as meta
                                    return meta._meta_table['Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Interfaces']['meta_info']


                            class Distance(_Entity_):
                                """
                                Set distance for EIGRP routes
                                
                                .. attribute:: internal_distance
                                
                                	Internal routes' distance
                                	**type**\: int
                                
                                	**range:** 1..255
                                
                                .. attribute:: external_distance
                                
                                	External routes' distance
                                	**type**\: int
                                
                                	**range:** 1..255
                                
                                

                                """

                                _prefix = 'eigrp-cfg'
                                _revision = '2018-06-15'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Distance, self).__init__()

                                    self.yang_name = "distance"
                                    self.yang_parent_name = "af"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('internal_distance', (YLeaf(YType.uint32, 'internal-distance'), ['int'])),
                                        ('external_distance', (YLeaf(YType.uint32, 'external-distance'), ['int'])),
                                    ])
                                    self.internal_distance = None
                                    self.external_distance = None
                                    self._segment_path = lambda: "distance"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Distance, ['internal_distance', 'external_distance'], name, value)

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_eigrp_cfg as meta
                                    return meta._meta_table['Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af.Distance']['meta_info']

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_eigrp_cfg as meta
                                return meta._meta_table['Eigrp.Processes.Process.Vrfs.Vrf.Afs.Af']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_eigrp_cfg as meta
                            return meta._meta_table['Eigrp.Processes.Process.Vrfs.Vrf.Afs']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_eigrp_cfg as meta
                        return meta._meta_table['Eigrp.Processes.Process.Vrfs.Vrf']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_eigrp_cfg as meta
                    return meta._meta_table['Eigrp.Processes.Process.Vrfs']['meta_info']


            class DefaultVrf(_Entity_):
                """
                Default VRF configuration.Deletion of this
                object also causes deletion of all
                objectsunder 'Process' associated with this
                process instance.
                
                .. attribute:: default_afs
                
                	Address family list in the default context
                	**type**\:  :py:class:`DefaultAfs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_cfg.Eigrp.Processes.Process.DefaultVrf.DefaultAfs>`
                
                .. attribute:: enable
                
                	Enable EIGRP Default VRF configurationDeletion of this object also causes deletion of all objectsunder 'Process' associated with this process instance
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                

                """

                _prefix = 'eigrp-cfg'
                _revision = '2018-06-15'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Eigrp.Processes.Process.DefaultVrf, self).__init__()

                    self.yang_name = "default-vrf"
                    self.yang_parent_name = "process"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("default-afs", ("default_afs", Eigrp.Processes.Process.DefaultVrf.DefaultAfs))])
                    self._leafs = OrderedDict([
                        ('enable', (YLeaf(YType.empty, 'enable'), ['Empty'])),
                    ])
                    self.enable = None

                    self.default_afs = Eigrp.Processes.Process.DefaultVrf.DefaultAfs()
                    self.default_afs.parent = self
                    self._children_name_map["default_afs"] = "default-afs"
                    self._segment_path = lambda: "default-vrf"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Eigrp.Processes.Process.DefaultVrf, ['enable'], name, value)


                class DefaultAfs(_Entity_):
                    """
                    Address family list in the default context
                    
                    .. attribute:: default_af
                    
                    	Configuration under an AF in the default context.Deletion of this object also causes deletion of all objectsunder 'DefaultAF' associated with this AF instance
                    	**type**\: list of  		 :py:class:`DefaultAf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_cfg.Eigrp.Processes.Process.DefaultVrf.DefaultAfs.DefaultAf>`
                    
                    

                    """

                    _prefix = 'eigrp-cfg'
                    _revision = '2018-06-15'

                    def __init__(self):
                        if sys.version_info > (3,):
                            super().__init__()
                        else:
                            super(Eigrp.Processes.Process.DefaultVrf.DefaultAfs, self).__init__()

                        self.yang_name = "default-afs"
                        self.yang_parent_name = "default-vrf"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("default-af", ("default_af", Eigrp.Processes.Process.DefaultVrf.DefaultAfs.DefaultAf))])
                        self._leafs = OrderedDict()

                        self.default_af = YList(self)
                        self._segment_path = lambda: "default-afs"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Eigrp.Processes.Process.DefaultVrf.DefaultAfs, [], name, value)


                    class DefaultAf(_Entity_):
                        """
                        Configuration under an AF in the default
                        context.Deletion of this object also causes
                        deletion of all objectsunder 'DefaultAF'
                        associated with this AF instance.
                        
                        .. attribute:: af_name  (key)
                        
                        	Address Family
                        	**type**\:  :py:class:`EigrpAf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_datatypes.EigrpAf>`
                        
                        .. attribute:: enable
                        
                        	Enable an Address Family under a default VRF
                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: auto_summary
                        
                        	Enable Auto Summarization
                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: stub
                        
                        	EIGRP stub configuration
                        	**type**\:  :py:class:`Stub <ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_cfg.Eigrp.Processes.Process.DefaultVrf.DefaultAfs.DefaultAf.Stub>`
                        
                        	**presence node**\: True
                        
                        .. attribute:: maximum_paths
                        
                        	number of paths
                        	**type**\: int
                        
                        	**range:** 1..32
                        
                        .. attribute:: redistributes
                        
                        	List of redistributed protocols
                        	**type**\:  :py:class:`Redistributes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_cfg.Eigrp.Processes.Process.DefaultVrf.DefaultAfs.DefaultAf.Redistributes>`
                        
                        	**presence node**\: True
                        
                        .. attribute:: router_id
                        
                        	Set router ID
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: log_neighbor_warnings
                        
                        	Enable/Disable neighbor state change warnings 
                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: filter_policies
                        
                        	Inbound and outbound filter policies
                        	**type**\:  :py:class:`FilterPolicies <ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_cfg.Eigrp.Processes.Process.DefaultVrf.DefaultAfs.DefaultAf.FilterPolicies>`
                        
                        .. attribute:: default_metric
                        
                        	Set metric of redistributed routes
                        	**type**\:  :py:class:`DefaultMetric <ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_cfg.Eigrp.Processes.Process.DefaultVrf.DefaultAfs.DefaultAf.DefaultMetric>`
                        
                        .. attribute:: autonomous_system
                        
                        	Set the autonomous system of a VRF
                        	**type**\: int
                        
                        	**range:** 1..65535
                        
                        .. attribute:: variance
                        
                        	Control load balancing variance
                        	**type**\: int
                        
                        	**range:** 1..128
                        
                        .. attribute:: metrics
                        
                        	List of metric change behaviours
                        	**type**\:  :py:class:`Metrics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_cfg.Eigrp.Processes.Process.DefaultVrf.DefaultAfs.DefaultAf.Metrics>`
                        
                        .. attribute:: timers
                        
                        	List of timer configurations
                        	**type**\:  :py:class:`Timers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_cfg.Eigrp.Processes.Process.DefaultVrf.DefaultAfs.DefaultAf.Timers>`
                        
                        .. attribute:: nsf_disable
                        
                        	Disable NSF for this address family under this VRF
                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: default_accepts
                        
                        	Candidate default policy table
                        	**type**\:  :py:class:`DefaultAccepts <ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_cfg.Eigrp.Processes.Process.DefaultVrf.DefaultAfs.DefaultAf.DefaultAccepts>`
                        
                        .. attribute:: passive_interface_default
                        
                        	Suppress routing updates on all interfaces
                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: interfaces
                        
                        	List of interfaces
                        	**type**\:  :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_cfg.Eigrp.Processes.Process.DefaultVrf.DefaultAfs.DefaultAf.Interfaces>`
                        
                        .. attribute:: distance
                        
                        	Set distance for EIGRP routes
                        	**type**\:  :py:class:`Distance <ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_cfg.Eigrp.Processes.Process.DefaultVrf.DefaultAfs.DefaultAf.Distance>`
                        
                        .. attribute:: log_neighbor_changes
                        
                        	Enable/Disable logginf of neighbor state changes
                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                        
                        

                        """

                        _prefix = 'eigrp-cfg'
                        _revision = '2018-06-15'

                        def __init__(self):
                            if sys.version_info > (3,):
                                super().__init__()
                            else:
                                super(Eigrp.Processes.Process.DefaultVrf.DefaultAfs.DefaultAf, self).__init__()

                            self.yang_name = "default-af"
                            self.yang_parent_name = "default-afs"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['af_name']
                            self._child_classes = OrderedDict([("stub", ("stub", Eigrp.Processes.Process.DefaultVrf.DefaultAfs.DefaultAf.Stub)), ("redistributes", ("redistributes", Eigrp.Processes.Process.DefaultVrf.DefaultAfs.DefaultAf.Redistributes)), ("filter-policies", ("filter_policies", Eigrp.Processes.Process.DefaultVrf.DefaultAfs.DefaultAf.FilterPolicies)), ("default-metric", ("default_metric", Eigrp.Processes.Process.DefaultVrf.DefaultAfs.DefaultAf.DefaultMetric)), ("metrics", ("metrics", Eigrp.Processes.Process.DefaultVrf.DefaultAfs.DefaultAf.Metrics)), ("timers", ("timers", Eigrp.Processes.Process.DefaultVrf.DefaultAfs.DefaultAf.Timers)), ("default-accepts", ("default_accepts", Eigrp.Processes.Process.DefaultVrf.DefaultAfs.DefaultAf.DefaultAccepts)), ("interfaces", ("interfaces", Eigrp.Processes.Process.DefaultVrf.DefaultAfs.DefaultAf.Interfaces)), ("distance", ("distance", Eigrp.Processes.Process.DefaultVrf.DefaultAfs.DefaultAf.Distance))])
                            self._leafs = OrderedDict([
                                ('af_name', (YLeaf(YType.enumeration, 'af-name'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_datatypes', 'EigrpAf', '')])),
                                ('enable', (YLeaf(YType.empty, 'enable'), ['Empty'])),
                                ('auto_summary', (YLeaf(YType.empty, 'auto-summary'), ['Empty'])),
                                ('maximum_paths', (YLeaf(YType.uint32, 'maximum-paths'), ['int'])),
                                ('router_id', (YLeaf(YType.str, 'router-id'), ['str'])),
                                ('log_neighbor_warnings', (YLeaf(YType.empty, 'log-neighbor-warnings'), ['Empty'])),
                                ('autonomous_system', (YLeaf(YType.uint32, 'autonomous-system'), ['int'])),
                                ('variance', (YLeaf(YType.uint32, 'variance'), ['int'])),
                                ('nsf_disable', (YLeaf(YType.empty, 'nsf-disable'), ['Empty'])),
                                ('passive_interface_default', (YLeaf(YType.empty, 'passive-interface-default'), ['Empty'])),
                                ('log_neighbor_changes', (YLeaf(YType.empty, 'log-neighbor-changes'), ['Empty'])),
                            ])
                            self.af_name = None
                            self.enable = None
                            self.auto_summary = None
                            self.maximum_paths = None
                            self.router_id = None
                            self.log_neighbor_warnings = None
                            self.autonomous_system = None
                            self.variance = None
                            self.nsf_disable = None
                            self.passive_interface_default = None
                            self.log_neighbor_changes = None

                            self.stub = None
                            self._children_name_map["stub"] = "stub"

                            self.redistributes = None
                            self._children_name_map["redistributes"] = "redistributes"

                            self.filter_policies = Eigrp.Processes.Process.DefaultVrf.DefaultAfs.DefaultAf.FilterPolicies()
                            self.filter_policies.parent = self
                            self._children_name_map["filter_policies"] = "filter-policies"

                            self.default_metric = Eigrp.Processes.Process.DefaultVrf.DefaultAfs.DefaultAf.DefaultMetric()
                            self.default_metric.parent = self
                            self._children_name_map["default_metric"] = "default-metric"

                            self.metrics = Eigrp.Processes.Process.DefaultVrf.DefaultAfs.DefaultAf.Metrics()
                            self.metrics.parent = self
                            self._children_name_map["metrics"] = "metrics"

                            self.timers = Eigrp.Processes.Process.DefaultVrf.DefaultAfs.DefaultAf.Timers()
                            self.timers.parent = self
                            self._children_name_map["timers"] = "timers"

                            self.default_accepts = Eigrp.Processes.Process.DefaultVrf.DefaultAfs.DefaultAf.DefaultAccepts()
                            self.default_accepts.parent = self
                            self._children_name_map["default_accepts"] = "default-accepts"

                            self.interfaces = Eigrp.Processes.Process.DefaultVrf.DefaultAfs.DefaultAf.Interfaces()
                            self.interfaces.parent = self
                            self._children_name_map["interfaces"] = "interfaces"

                            self.distance = Eigrp.Processes.Process.DefaultVrf.DefaultAfs.DefaultAf.Distance()
                            self.distance.parent = self
                            self._children_name_map["distance"] = "distance"
                            self._segment_path = lambda: "default-af" + "[af-name='" + str(self.af_name) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Eigrp.Processes.Process.DefaultVrf.DefaultAfs.DefaultAf, ['af_name', 'enable', 'auto_summary', 'maximum_paths', 'router_id', 'log_neighbor_warnings', 'autonomous_system', 'variance', 'nsf_disable', 'passive_interface_default', 'log_neighbor_changes'], name, value)


                        class Stub(_Entity_):
                            """
                            EIGRP stub configuration
                            
                            .. attribute:: type
                            
                            	Stub config type
                            	**type**\:  :py:class:`EigrpStub <ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_cfg.EigrpStub>`
                            
                            .. attribute:: connected
                            
                            	Do advertise connected routes
                            	**type**\: bool
                            
                            .. attribute:: redistributed
                            
                            	Do advertise redistributed routes
                            	**type**\: bool
                            
                            .. attribute:: static
                            
                            	Do advertise static routes
                            	**type**\: bool
                            
                            .. attribute:: summary
                            
                            	Do advertise summary routes
                            	**type**\: bool
                            
                            

                            This class is a :ref:`presence class<presence-class>`

                            """

                            _prefix = 'eigrp-cfg'
                            _revision = '2018-06-15'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Eigrp.Processes.Process.DefaultVrf.DefaultAfs.DefaultAf.Stub, self).__init__()

                                self.yang_name = "stub"
                                self.yang_parent_name = "default-af"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self.is_presence_container = True
                                self._leafs = OrderedDict([
                                    ('type', (YLeaf(YType.enumeration, 'type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_cfg', 'EigrpStub', '')])),
                                    ('connected', (YLeaf(YType.boolean, 'connected'), ['bool'])),
                                    ('redistributed', (YLeaf(YType.boolean, 'redistributed'), ['bool'])),
                                    ('static', (YLeaf(YType.boolean, 'static'), ['bool'])),
                                    ('summary', (YLeaf(YType.boolean, 'summary'), ['bool'])),
                                ])
                                self.type = None
                                self.connected = None
                                self.redistributed = None
                                self.static = None
                                self.summary = None
                                self._segment_path = lambda: "stub"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Eigrp.Processes.Process.DefaultVrf.DefaultAfs.DefaultAf.Stub, ['type', 'connected', 'redistributed', 'static', 'summary'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_eigrp_cfg as meta
                                return meta._meta_table['Eigrp.Processes.Process.DefaultVrf.DefaultAfs.DefaultAf.Stub']['meta_info']


                        class Redistributes(_Entity_):
                            """
                            List of redistributed protocols
                            
                            .. attribute:: redistribute
                            
                            	Redistribute another protocol
                            	**type**\: list of  		 :py:class:`Redistribute <ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_cfg.Eigrp.Processes.Process.DefaultVrf.DefaultAfs.DefaultAf.Redistributes.Redistribute>`
                            
                            .. attribute:: redistribute_as_xx
                            
                            	Redistribute another protocol
                            	**type**\: list of  		 :py:class:`RedistributeAsXx <ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_cfg.Eigrp.Processes.Process.DefaultVrf.DefaultAfs.DefaultAf.Redistributes.RedistributeAsXx>`
                            
                            .. attribute:: redistribute_as_yy
                            
                            	Redistribute another protocol
                            	**type**\: list of  		 :py:class:`RedistributeAsYy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_cfg.Eigrp.Processes.Process.DefaultVrf.DefaultAfs.DefaultAf.Redistributes.RedistributeAsYy>`
                            
                            .. attribute:: redistribute_as_xx_as_yy
                            
                            	Redistribute another protocol
                            	**type**\: list of  		 :py:class:`RedistributeAsXxAsYy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_cfg.Eigrp.Processes.Process.DefaultVrf.DefaultAfs.DefaultAf.Redistributes.RedistributeAsXxAsYy>`
                            
                            .. attribute:: redistribute_tag_name
                            
                            	Redistribute another protocol
                            	**type**\: list of  		 :py:class:`RedistributeTagName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_cfg.Eigrp.Processes.Process.DefaultVrf.DefaultAfs.DefaultAf.Redistributes.RedistributeTagName>`
                            
                            .. attribute:: redistribute_as_xx_tag_name
                            
                            	Redistribute another protocol
                            	**type**\: list of  		 :py:class:`RedistributeAsXxTagName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_cfg.Eigrp.Processes.Process.DefaultVrf.DefaultAfs.DefaultAf.Redistributes.RedistributeAsXxTagName>`
                            
                            .. attribute:: redistribute_as_yy_tag_name
                            
                            	Redistribute another protocol
                            	**type**\: list of  		 :py:class:`RedistributeAsYyTagName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_cfg.Eigrp.Processes.Process.DefaultVrf.DefaultAfs.DefaultAf.Redistributes.RedistributeAsYyTagName>`
                            
                            .. attribute:: redistribute_as_xx_as_yy_tag_name
                            
                            	Redistribute another protocol
                            	**type**\: list of  		 :py:class:`RedistributeAsXxAsYyTagName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_cfg.Eigrp.Processes.Process.DefaultVrf.DefaultAfs.DefaultAf.Redistributes.RedistributeAsXxAsYyTagName>`
                            
                            

                            This class is a :ref:`presence class<presence-class>`

                            """

                            _prefix = 'eigrp-cfg'
                            _revision = '2018-06-15'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Eigrp.Processes.Process.DefaultVrf.DefaultAfs.DefaultAf.Redistributes, self).__init__()

                                self.yang_name = "redistributes"
                                self.yang_parent_name = "default-af"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("redistribute", ("redistribute", Eigrp.Processes.Process.DefaultVrf.DefaultAfs.DefaultAf.Redistributes.Redistribute)), ("redistribute-as-xx", ("redistribute_as_xx", Eigrp.Processes.Process.DefaultVrf.DefaultAfs.DefaultAf.Redistributes.RedistributeAsXx)), ("redistribute-as-yy", ("redistribute_as_yy", Eigrp.Processes.Process.DefaultVrf.DefaultAfs.DefaultAf.Redistributes.RedistributeAsYy)), ("redistribute-as-xx-as-yy", ("redistribute_as_xx_as_yy", Eigrp.Processes.Process.DefaultVrf.DefaultAfs.DefaultAf.Redistributes.RedistributeAsXxAsYy)), ("redistribute-tag-name", ("redistribute_tag_name", Eigrp.Processes.Process.DefaultVrf.DefaultAfs.DefaultAf.Redistributes.RedistributeTagName)), ("redistribute-as-xx-tag-name", ("redistribute_as_xx_tag_name", Eigrp.Processes.Process.DefaultVrf.DefaultAfs.DefaultAf.Redistributes.RedistributeAsXxTagName)), ("redistribute-as-yy-tag-name", ("redistribute_as_yy_tag_name", Eigrp.Processes.Process.DefaultVrf.DefaultAfs.DefaultAf.Redistributes.RedistributeAsYyTagName)), ("redistribute-as-xx-as-yy-tag-name", ("redistribute_as_xx_as_yy_tag_name", Eigrp.Processes.Process.DefaultVrf.DefaultAfs.DefaultAf.Redistributes.RedistributeAsXxAsYyTagName))])
                                self.is_presence_container = True
                                self._leafs = OrderedDict()

                                self.redistribute = YList(self)
                                self.redistribute_as_xx = YList(self)
                                self.redistribute_as_yy = YList(self)
                                self.redistribute_as_xx_as_yy = YList(self)
                                self.redistribute_tag_name = YList(self)
                                self.redistribute_as_xx_tag_name = YList(self)
                                self.redistribute_as_yy_tag_name = YList(self)
                                self.redistribute_as_xx_as_yy_tag_name = YList(self)
                                self._segment_path = lambda: "redistributes"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Eigrp.Processes.Process.DefaultVrf.DefaultAfs.DefaultAf.Redistributes, [], name, value)


                            class Redistribute(_Entity_):
                                """
                                Redistribute another protocol
                                
                                .. attribute:: protocol_name  (key)
                                
                                	Redistributed protocol
                                	**type**\:  :py:class:`EigrpRedistProto <ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_cfg.EigrpRedistProto>`
                                
                                .. attribute:: policy_name
                                
                                	Policy name
                                	**type**\: str
                                
                                .. attribute:: policy_specified
                                
                                	TRUE if Policy has been specified
                                	**type**\: bool
                                
                                	**mandatory**\: True
                                
                                

                                """

                                _prefix = 'eigrp-cfg'
                                _revision = '2018-06-15'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(Eigrp.Processes.Process.DefaultVrf.DefaultAfs.DefaultAf.Redistributes.Redistribute, self).__init__()

                                    self.yang_name = "redistribute"
                                    self.yang_parent_name = "redistributes"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['protocol_name']
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('protocol_name', (YLeaf(YType.enumeration, 'protocol-name'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_cfg', 'EigrpRedistProto', '')])),
                                        ('policy_name', (YLeaf(YType.str, 'policy-name'), ['str'])),
                                        ('policy_specified', (YLeaf(YType.boolean, 'policy-specified'), ['bool'])),
                                    ])
                                    self.protocol_name = None
                                    self.policy_name = None
                                    self.policy_specified = None
                                    self._segment_path = lambda: "redistribute" + "[protocol-name='" + str(self.protocol_name) + "']"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Eigrp.Processes.Process.DefaultVrf.DefaultAfs.DefaultAf.Redistributes.Redistribute, ['protocol_name', 'policy_name', 'policy_specified'], name, value)

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_eigrp_cfg as meta
                                    return meta._meta_table['Eigrp.Processes.Process.DefaultVrf.DefaultAfs.DefaultAf.Redistributes.Redistribute']['meta_info']


                            class RedistributeAsXx(_Entity_):
                                """
                                Redistribute another protocol
                                
                                .. attribute:: as_xx  (key)
                                
                                	Higher sixteen bits of 4\-byte BGP AS number
                                	**type**\: int
                                
                                	**range:** 0..65535
                                
                                .. attribute:: protocol_name  (key)
                                
                                	Redistributed protocol
                                	**type**\:  :py:class:`EigrpRedistProto <ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_cfg.EigrpRedistProto>`
                                
                                .. attribute:: policy_name
                                
                                	Policy name
                                	**type**\: str
                                
                                .. attribute:: policy_specified
                                
                                	TRUE if Policy has been specified
                                	**type**\: bool
                                
                                	**mandatory**\: True
                                
                                

                                """

                                _prefix = 'eigrp-cfg'
                                _revision = '2018-06-15'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(Eigrp.Processes.Process.DefaultVrf.DefaultAfs.DefaultAf.Redistributes.RedistributeAsXx, self).__init__()

                                    self.yang_name = "redistribute-as-xx"
                                    self.yang_parent_name = "redistributes"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['as_xx','protocol_name']
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('as_xx', (YLeaf(YType.uint32, 'as-xx'), ['int'])),
                                        ('protocol_name', (YLeaf(YType.enumeration, 'protocol-name'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_cfg', 'EigrpRedistProto', '')])),
                                        ('policy_name', (YLeaf(YType.str, 'policy-name'), ['str'])),
                                        ('policy_specified', (YLeaf(YType.boolean, 'policy-specified'), ['bool'])),
                                    ])
                                    self.as_xx = None
                                    self.protocol_name = None
                                    self.policy_name = None
                                    self.policy_specified = None
                                    self._segment_path = lambda: "redistribute-as-xx" + "[as-xx='" + str(self.as_xx) + "']" + "[protocol-name='" + str(self.protocol_name) + "']"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Eigrp.Processes.Process.DefaultVrf.DefaultAfs.DefaultAf.Redistributes.RedistributeAsXx, ['as_xx', 'protocol_name', 'policy_name', 'policy_specified'], name, value)

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_eigrp_cfg as meta
                                    return meta._meta_table['Eigrp.Processes.Process.DefaultVrf.DefaultAfs.DefaultAf.Redistributes.RedistributeAsXx']['meta_info']


                            class RedistributeAsYy(_Entity_):
                                """
                                Redistribute another protocol
                                
                                .. attribute:: as_yy  (key)
                                
                                	2\-byte or 4\-byte BGP AS Number
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: protocol_name  (key)
                                
                                	Redistributed protocol
                                	**type**\:  :py:class:`EigrpRedistProto <ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_cfg.EigrpRedistProto>`
                                
                                .. attribute:: policy_name
                                
                                	Policy name
                                	**type**\: str
                                
                                .. attribute:: policy_specified
                                
                                	TRUE if Policy has been specified
                                	**type**\: bool
                                
                                	**mandatory**\: True
                                
                                

                                """

                                _prefix = 'eigrp-cfg'
                                _revision = '2018-06-15'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(Eigrp.Processes.Process.DefaultVrf.DefaultAfs.DefaultAf.Redistributes.RedistributeAsYy, self).__init__()

                                    self.yang_name = "redistribute-as-yy"
                                    self.yang_parent_name = "redistributes"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['as_yy','protocol_name']
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('as_yy', (YLeaf(YType.uint32, 'as-yy'), ['int'])),
                                        ('protocol_name', (YLeaf(YType.enumeration, 'protocol-name'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_cfg', 'EigrpRedistProto', '')])),
                                        ('policy_name', (YLeaf(YType.str, 'policy-name'), ['str'])),
                                        ('policy_specified', (YLeaf(YType.boolean, 'policy-specified'), ['bool'])),
                                    ])
                                    self.as_yy = None
                                    self.protocol_name = None
                                    self.policy_name = None
                                    self.policy_specified = None
                                    self._segment_path = lambda: "redistribute-as-yy" + "[as-yy='" + str(self.as_yy) + "']" + "[protocol-name='" + str(self.protocol_name) + "']"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Eigrp.Processes.Process.DefaultVrf.DefaultAfs.DefaultAf.Redistributes.RedistributeAsYy, ['as_yy', 'protocol_name', 'policy_name', 'policy_specified'], name, value)

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_eigrp_cfg as meta
                                    return meta._meta_table['Eigrp.Processes.Process.DefaultVrf.DefaultAfs.DefaultAf.Redistributes.RedistributeAsYy']['meta_info']


                            class RedistributeAsXxAsYy(_Entity_):
                                """
                                Redistribute another protocol
                                
                                .. attribute:: as_xx  (key)
                                
                                	Higher sixteen bits of 4\-byte BGP AS number
                                	**type**\: int
                                
                                	**range:** 0..65535
                                
                                .. attribute:: as_yy  (key)
                                
                                	2\-byte or 4\-byte BGP AS Number
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: protocol_name  (key)
                                
                                	Redistributed protocol
                                	**type**\:  :py:class:`EigrpRedistProto <ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_cfg.EigrpRedistProto>`
                                
                                .. attribute:: policy_name
                                
                                	Policy name
                                	**type**\: str
                                
                                .. attribute:: policy_specified
                                
                                	TRUE if Policy has been specified
                                	**type**\: bool
                                
                                	**mandatory**\: True
                                
                                

                                """

                                _prefix = 'eigrp-cfg'
                                _revision = '2018-06-15'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(Eigrp.Processes.Process.DefaultVrf.DefaultAfs.DefaultAf.Redistributes.RedistributeAsXxAsYy, self).__init__()

                                    self.yang_name = "redistribute-as-xx-as-yy"
                                    self.yang_parent_name = "redistributes"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['as_xx','as_yy','protocol_name']
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('as_xx', (YLeaf(YType.uint32, 'as-xx'), ['int'])),
                                        ('as_yy', (YLeaf(YType.uint32, 'as-yy'), ['int'])),
                                        ('protocol_name', (YLeaf(YType.enumeration, 'protocol-name'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_cfg', 'EigrpRedistProto', '')])),
                                        ('policy_name', (YLeaf(YType.str, 'policy-name'), ['str'])),
                                        ('policy_specified', (YLeaf(YType.boolean, 'policy-specified'), ['bool'])),
                                    ])
                                    self.as_xx = None
                                    self.as_yy = None
                                    self.protocol_name = None
                                    self.policy_name = None
                                    self.policy_specified = None
                                    self._segment_path = lambda: "redistribute-as-xx-as-yy" + "[as-xx='" + str(self.as_xx) + "']" + "[as-yy='" + str(self.as_yy) + "']" + "[protocol-name='" + str(self.protocol_name) + "']"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Eigrp.Processes.Process.DefaultVrf.DefaultAfs.DefaultAf.Redistributes.RedistributeAsXxAsYy, ['as_xx', 'as_yy', 'protocol_name', 'policy_name', 'policy_specified'], name, value)

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_eigrp_cfg as meta
                                    return meta._meta_table['Eigrp.Processes.Process.DefaultVrf.DefaultAfs.DefaultAf.Redistributes.RedistributeAsXxAsYy']['meta_info']


                            class RedistributeTagName(_Entity_):
                                """
                                Redistribute another protocol
                                
                                .. attribute:: tag_name  (key)
                                
                                	OSPF/OSPFv3/ISIS/OnePK Application tag name
                                	**type**\: str
                                
                                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                                
                                .. attribute:: protocol_name  (key)
                                
                                	Redistributed protocol
                                	**type**\:  :py:class:`EigrpRedistProto <ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_cfg.EigrpRedistProto>`
                                
                                .. attribute:: policy_name
                                
                                	Policy name
                                	**type**\: str
                                
                                .. attribute:: policy_specified
                                
                                	TRUE if Policy has been specified
                                	**type**\: bool
                                
                                	**mandatory**\: True
                                
                                

                                """

                                _prefix = 'eigrp-cfg'
                                _revision = '2018-06-15'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(Eigrp.Processes.Process.DefaultVrf.DefaultAfs.DefaultAf.Redistributes.RedistributeTagName, self).__init__()

                                    self.yang_name = "redistribute-tag-name"
                                    self.yang_parent_name = "redistributes"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['tag_name','protocol_name']
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('tag_name', (YLeaf(YType.str, 'tag-name'), ['str'])),
                                        ('protocol_name', (YLeaf(YType.enumeration, 'protocol-name'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_cfg', 'EigrpRedistProto', '')])),
                                        ('policy_name', (YLeaf(YType.str, 'policy-name'), ['str'])),
                                        ('policy_specified', (YLeaf(YType.boolean, 'policy-specified'), ['bool'])),
                                    ])
                                    self.tag_name = None
                                    self.protocol_name = None
                                    self.policy_name = None
                                    self.policy_specified = None
                                    self._segment_path = lambda: "redistribute-tag-name" + "[tag-name='" + str(self.tag_name) + "']" + "[protocol-name='" + str(self.protocol_name) + "']"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Eigrp.Processes.Process.DefaultVrf.DefaultAfs.DefaultAf.Redistributes.RedistributeTagName, ['tag_name', 'protocol_name', 'policy_name', 'policy_specified'], name, value)

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_eigrp_cfg as meta
                                    return meta._meta_table['Eigrp.Processes.Process.DefaultVrf.DefaultAfs.DefaultAf.Redistributes.RedistributeTagName']['meta_info']


                            class RedistributeAsXxTagName(_Entity_):
                                """
                                Redistribute another protocol
                                
                                .. attribute:: as_xx  (key)
                                
                                	Higher sixteen bits of 4\-byte BGP AS number
                                	**type**\: int
                                
                                	**range:** 0..65535
                                
                                .. attribute:: tag_name  (key)
                                
                                	OSPF/OSPFv3/ISIS/OnePK Application tag name
                                	**type**\: str
                                
                                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                                
                                .. attribute:: protocol_name  (key)
                                
                                	Redistributed protocol
                                	**type**\:  :py:class:`EigrpRedistProto <ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_cfg.EigrpRedistProto>`
                                
                                .. attribute:: policy_name
                                
                                	Policy name
                                	**type**\: str
                                
                                .. attribute:: policy_specified
                                
                                	TRUE if Policy has been specified
                                	**type**\: bool
                                
                                	**mandatory**\: True
                                
                                

                                """

                                _prefix = 'eigrp-cfg'
                                _revision = '2018-06-15'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(Eigrp.Processes.Process.DefaultVrf.DefaultAfs.DefaultAf.Redistributes.RedistributeAsXxTagName, self).__init__()

                                    self.yang_name = "redistribute-as-xx-tag-name"
                                    self.yang_parent_name = "redistributes"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['as_xx','tag_name','protocol_name']
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('as_xx', (YLeaf(YType.uint32, 'as-xx'), ['int'])),
                                        ('tag_name', (YLeaf(YType.str, 'tag-name'), ['str'])),
                                        ('protocol_name', (YLeaf(YType.enumeration, 'protocol-name'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_cfg', 'EigrpRedistProto', '')])),
                                        ('policy_name', (YLeaf(YType.str, 'policy-name'), ['str'])),
                                        ('policy_specified', (YLeaf(YType.boolean, 'policy-specified'), ['bool'])),
                                    ])
                                    self.as_xx = None
                                    self.tag_name = None
                                    self.protocol_name = None
                                    self.policy_name = None
                                    self.policy_specified = None
                                    self._segment_path = lambda: "redistribute-as-xx-tag-name" + "[as-xx='" + str(self.as_xx) + "']" + "[tag-name='" + str(self.tag_name) + "']" + "[protocol-name='" + str(self.protocol_name) + "']"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Eigrp.Processes.Process.DefaultVrf.DefaultAfs.DefaultAf.Redistributes.RedistributeAsXxTagName, ['as_xx', 'tag_name', 'protocol_name', 'policy_name', 'policy_specified'], name, value)

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_eigrp_cfg as meta
                                    return meta._meta_table['Eigrp.Processes.Process.DefaultVrf.DefaultAfs.DefaultAf.Redistributes.RedistributeAsXxTagName']['meta_info']


                            class RedistributeAsYyTagName(_Entity_):
                                """
                                Redistribute another protocol
                                
                                .. attribute:: as_yy  (key)
                                
                                	2\-byte or 4\-byte BGP AS Number
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: tag_name  (key)
                                
                                	OSPF/OSPFv3/ISIS/OnePK Application tag name
                                	**type**\: str
                                
                                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                                
                                .. attribute:: protocol_name  (key)
                                
                                	Redistributed protocol
                                	**type**\:  :py:class:`EigrpRedistProto <ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_cfg.EigrpRedistProto>`
                                
                                .. attribute:: policy_name
                                
                                	Policy name
                                	**type**\: str
                                
                                .. attribute:: policy_specified
                                
                                	TRUE if Policy has been specified
                                	**type**\: bool
                                
                                	**mandatory**\: True
                                
                                

                                """

                                _prefix = 'eigrp-cfg'
                                _revision = '2018-06-15'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(Eigrp.Processes.Process.DefaultVrf.DefaultAfs.DefaultAf.Redistributes.RedistributeAsYyTagName, self).__init__()

                                    self.yang_name = "redistribute-as-yy-tag-name"
                                    self.yang_parent_name = "redistributes"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['as_yy','tag_name','protocol_name']
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('as_yy', (YLeaf(YType.uint32, 'as-yy'), ['int'])),
                                        ('tag_name', (YLeaf(YType.str, 'tag-name'), ['str'])),
                                        ('protocol_name', (YLeaf(YType.enumeration, 'protocol-name'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_cfg', 'EigrpRedistProto', '')])),
                                        ('policy_name', (YLeaf(YType.str, 'policy-name'), ['str'])),
                                        ('policy_specified', (YLeaf(YType.boolean, 'policy-specified'), ['bool'])),
                                    ])
                                    self.as_yy = None
                                    self.tag_name = None
                                    self.protocol_name = None
                                    self.policy_name = None
                                    self.policy_specified = None
                                    self._segment_path = lambda: "redistribute-as-yy-tag-name" + "[as-yy='" + str(self.as_yy) + "']" + "[tag-name='" + str(self.tag_name) + "']" + "[protocol-name='" + str(self.protocol_name) + "']"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Eigrp.Processes.Process.DefaultVrf.DefaultAfs.DefaultAf.Redistributes.RedistributeAsYyTagName, ['as_yy', 'tag_name', 'protocol_name', 'policy_name', 'policy_specified'], name, value)

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_eigrp_cfg as meta
                                    return meta._meta_table['Eigrp.Processes.Process.DefaultVrf.DefaultAfs.DefaultAf.Redistributes.RedistributeAsYyTagName']['meta_info']


                            class RedistributeAsXxAsYyTagName(_Entity_):
                                """
                                Redistribute another protocol
                                
                                .. attribute:: as_xx  (key)
                                
                                	Higher sixteen bits of 4\-byte BGP AS number
                                	**type**\: int
                                
                                	**range:** 0..65535
                                
                                .. attribute:: as_yy  (key)
                                
                                	2\-byte or 4\-byte BGP AS Number
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: tag_name  (key)
                                
                                	OSPF/OSPFv3/ISIS/OnePK Application tag name
                                	**type**\: str
                                
                                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                                
                                .. attribute:: protocol_name  (key)
                                
                                	Redistributed protocol
                                	**type**\:  :py:class:`EigrpRedistProto <ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_cfg.EigrpRedistProto>`
                                
                                .. attribute:: policy_name
                                
                                	Policy name
                                	**type**\: str
                                
                                .. attribute:: policy_specified
                                
                                	TRUE if Policy has been specified
                                	**type**\: bool
                                
                                	**mandatory**\: True
                                
                                

                                """

                                _prefix = 'eigrp-cfg'
                                _revision = '2018-06-15'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(Eigrp.Processes.Process.DefaultVrf.DefaultAfs.DefaultAf.Redistributes.RedistributeAsXxAsYyTagName, self).__init__()

                                    self.yang_name = "redistribute-as-xx-as-yy-tag-name"
                                    self.yang_parent_name = "redistributes"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['as_xx','as_yy','tag_name','protocol_name']
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('as_xx', (YLeaf(YType.uint32, 'as-xx'), ['int'])),
                                        ('as_yy', (YLeaf(YType.uint32, 'as-yy'), ['int'])),
                                        ('tag_name', (YLeaf(YType.str, 'tag-name'), ['str'])),
                                        ('protocol_name', (YLeaf(YType.enumeration, 'protocol-name'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_cfg', 'EigrpRedistProto', '')])),
                                        ('policy_name', (YLeaf(YType.str, 'policy-name'), ['str'])),
                                        ('policy_specified', (YLeaf(YType.boolean, 'policy-specified'), ['bool'])),
                                    ])
                                    self.as_xx = None
                                    self.as_yy = None
                                    self.tag_name = None
                                    self.protocol_name = None
                                    self.policy_name = None
                                    self.policy_specified = None
                                    self._segment_path = lambda: "redistribute-as-xx-as-yy-tag-name" + "[as-xx='" + str(self.as_xx) + "']" + "[as-yy='" + str(self.as_yy) + "']" + "[tag-name='" + str(self.tag_name) + "']" + "[protocol-name='" + str(self.protocol_name) + "']"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Eigrp.Processes.Process.DefaultVrf.DefaultAfs.DefaultAf.Redistributes.RedistributeAsXxAsYyTagName, ['as_xx', 'as_yy', 'tag_name', 'protocol_name', 'policy_name', 'policy_specified'], name, value)

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_eigrp_cfg as meta
                                    return meta._meta_table['Eigrp.Processes.Process.DefaultVrf.DefaultAfs.DefaultAf.Redistributes.RedistributeAsXxAsYyTagName']['meta_info']

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_eigrp_cfg as meta
                                return meta._meta_table['Eigrp.Processes.Process.DefaultVrf.DefaultAfs.DefaultAf.Redistributes']['meta_info']


                        class FilterPolicies(_Entity_):
                            """
                            Inbound and outbound filter policies
                            
                            .. attribute:: filter_policy
                            
                            	Inbound/outbound policies
                            	**type**\: list of  		 :py:class:`FilterPolicy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_cfg.Eigrp.Processes.Process.DefaultVrf.DefaultAfs.DefaultAf.FilterPolicies.FilterPolicy>`
                            
                            

                            """

                            _prefix = 'eigrp-cfg'
                            _revision = '2018-06-15'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Eigrp.Processes.Process.DefaultVrf.DefaultAfs.DefaultAf.FilterPolicies, self).__init__()

                                self.yang_name = "filter-policies"
                                self.yang_parent_name = "default-af"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("filter-policy", ("filter_policy", Eigrp.Processes.Process.DefaultVrf.DefaultAfs.DefaultAf.FilterPolicies.FilterPolicy))])
                                self._leafs = OrderedDict()

                                self.filter_policy = YList(self)
                                self._segment_path = lambda: "filter-policies"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Eigrp.Processes.Process.DefaultVrf.DefaultAfs.DefaultAf.FilterPolicies, [], name, value)


                            class FilterPolicy(_Entity_):
                                """
                                Inbound/outbound policies
                                
                                .. attribute:: direction  (key)
                                
                                	Direction (in or out)
                                	**type**\:  :py:class:`EigrpDir <ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_cfg.EigrpDir>`
                                
                                .. attribute:: policy_name
                                
                                	Policy name
                                	**type**\: str
                                
                                	**mandatory**\: True
                                
                                

                                """

                                _prefix = 'eigrp-cfg'
                                _revision = '2018-06-15'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(Eigrp.Processes.Process.DefaultVrf.DefaultAfs.DefaultAf.FilterPolicies.FilterPolicy, self).__init__()

                                    self.yang_name = "filter-policy"
                                    self.yang_parent_name = "filter-policies"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['direction']
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('direction', (YLeaf(YType.enumeration, 'direction'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_cfg', 'EigrpDir', '')])),
                                        ('policy_name', (YLeaf(YType.str, 'policy-name'), ['str'])),
                                    ])
                                    self.direction = None
                                    self.policy_name = None
                                    self._segment_path = lambda: "filter-policy" + "[direction='" + str(self.direction) + "']"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Eigrp.Processes.Process.DefaultVrf.DefaultAfs.DefaultAf.FilterPolicies.FilterPolicy, ['direction', 'policy_name'], name, value)

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_eigrp_cfg as meta
                                    return meta._meta_table['Eigrp.Processes.Process.DefaultVrf.DefaultAfs.DefaultAf.FilterPolicies.FilterPolicy']['meta_info']

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_eigrp_cfg as meta
                                return meta._meta_table['Eigrp.Processes.Process.DefaultVrf.DefaultAfs.DefaultAf.FilterPolicies']['meta_info']


                        class DefaultMetric(_Entity_):
                            """
                            Set metric of redistributed routes
                            
                            .. attribute:: bandwidth
                            
                            	Bandwidth in Kbits per second
                            	**type**\: int
                            
                            	**range:** 1..4294967295
                            
                            	**units**\: kbit/s
                            
                            .. attribute:: delay
                            
                            	Delay metric, in 10 microsecond units
                            	**type**\: int
                            
                            	**range:** 1..4294967295
                            
                            .. attribute:: reliability
                            
                            	Reliability metric where 255 is 100% reliable
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            .. attribute:: load
                            
                            	Effective bandwidth metric (Loading) where 255 is 100% loaded
                            	**type**\: int
                            
                            	**range:** 1..255
                            
                            .. attribute:: mtu
                            
                            	Maximum Transmission Unit metric of the path
                            	**type**\: int
                            
                            	**range:** 1..65535
                            
                            

                            """

                            _prefix = 'eigrp-cfg'
                            _revision = '2018-06-15'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Eigrp.Processes.Process.DefaultVrf.DefaultAfs.DefaultAf.DefaultMetric, self).__init__()

                                self.yang_name = "default-metric"
                                self.yang_parent_name = "default-af"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('bandwidth', (YLeaf(YType.uint32, 'bandwidth'), ['int'])),
                                    ('delay', (YLeaf(YType.uint32, 'delay'), ['int'])),
                                    ('reliability', (YLeaf(YType.uint32, 'reliability'), ['int'])),
                                    ('load', (YLeaf(YType.uint32, 'load'), ['int'])),
                                    ('mtu', (YLeaf(YType.uint32, 'mtu'), ['int'])),
                                ])
                                self.bandwidth = None
                                self.delay = None
                                self.reliability = None
                                self.load = None
                                self.mtu = None
                                self._segment_path = lambda: "default-metric"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Eigrp.Processes.Process.DefaultVrf.DefaultAfs.DefaultAf.DefaultMetric, ['bandwidth', 'delay', 'reliability', 'load', 'mtu'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_eigrp_cfg as meta
                                return meta._meta_table['Eigrp.Processes.Process.DefaultVrf.DefaultAfs.DefaultAf.DefaultMetric']['meta_info']


                        class Metrics(_Entity_):
                            """
                            List of metric change behaviours
                            
                            .. attribute:: metric
                            
                            	Modify EIGRP routing metrics and parameters
                            	**type**\: list of  		 :py:class:`Metric <ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_cfg.Eigrp.Processes.Process.DefaultVrf.DefaultAfs.DefaultAf.Metrics.Metric>`
                            
                            

                            """

                            _prefix = 'eigrp-cfg'
                            _revision = '2018-06-15'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Eigrp.Processes.Process.DefaultVrf.DefaultAfs.DefaultAf.Metrics, self).__init__()

                                self.yang_name = "metrics"
                                self.yang_parent_name = "default-af"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("metric", ("metric", Eigrp.Processes.Process.DefaultVrf.DefaultAfs.DefaultAf.Metrics.Metric))])
                                self._leafs = OrderedDict()

                                self.metric = YList(self)
                                self._segment_path = lambda: "metrics"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Eigrp.Processes.Process.DefaultVrf.DefaultAfs.DefaultAf.Metrics, [], name, value)


                            class Metric(_Entity_):
                                """
                                Modify EIGRP routing metrics and parameters
                                
                                .. attribute:: metric_name  (key)
                                
                                	Type of metric change
                                	**type**\:  :py:class:`EigrpMet <ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_cfg.EigrpMet>`
                                
                                .. attribute:: max_hops
                                
                                	Hop count
                                	**type**\: int
                                
                                	**range:** 1..255
                                
                                .. attribute:: tos
                                
                                	Type of Service (Only TOS 0 supported)
                                	**type**\: int
                                
                                	**range:** 0..0
                                
                                .. attribute:: k1
                                
                                	K1
                                	**type**\: int
                                
                                	**range:** 0..255
                                
                                .. attribute:: k2
                                
                                	K2
                                	**type**\: int
                                
                                	**range:** 0..255
                                
                                .. attribute:: k3
                                
                                	K3
                                	**type**\: int
                                
                                	**range:** 0..255
                                
                                .. attribute:: k4
                                
                                	K4
                                	**type**\: int
                                
                                	**range:** 0..255
                                
                                .. attribute:: k5
                                
                                	K5
                                	**type**\: int
                                
                                	**range:** 0..255
                                
                                .. attribute:: k6
                                
                                	K6
                                	**type**\: int
                                
                                	**range:** 0..255
                                
                                .. attribute:: rib_scale
                                
                                	RIB scale
                                	**type**\: int
                                
                                	**range:** 1..4294967295
                                
                                .. attribute:: metric_version
                                
                                	Metric version
                                	**type**\:  :py:class:`EigrpMetricVersion <ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_cfg.EigrpMetricVersion>`
                                
                                

                                """

                                _prefix = 'eigrp-cfg'
                                _revision = '2018-06-15'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(Eigrp.Processes.Process.DefaultVrf.DefaultAfs.DefaultAf.Metrics.Metric, self).__init__()

                                    self.yang_name = "metric"
                                    self.yang_parent_name = "metrics"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['metric_name']
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('metric_name', (YLeaf(YType.enumeration, 'metric-name'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_cfg', 'EigrpMet', '')])),
                                        ('max_hops', (YLeaf(YType.uint32, 'max-hops'), ['int'])),
                                        ('tos', (YLeaf(YType.uint32, 'tos'), ['int'])),
                                        ('k1', (YLeaf(YType.uint32, 'k1'), ['int'])),
                                        ('k2', (YLeaf(YType.uint32, 'k2'), ['int'])),
                                        ('k3', (YLeaf(YType.uint32, 'k3'), ['int'])),
                                        ('k4', (YLeaf(YType.uint32, 'k4'), ['int'])),
                                        ('k5', (YLeaf(YType.uint32, 'k5'), ['int'])),
                                        ('k6', (YLeaf(YType.uint32, 'k6'), ['int'])),
                                        ('rib_scale', (YLeaf(YType.uint32, 'rib-scale'), ['int'])),
                                        ('metric_version', (YLeaf(YType.enumeration, 'metric-version'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_cfg', 'EigrpMetricVersion', '')])),
                                    ])
                                    self.metric_name = None
                                    self.max_hops = None
                                    self.tos = None
                                    self.k1 = None
                                    self.k2 = None
                                    self.k3 = None
                                    self.k4 = None
                                    self.k5 = None
                                    self.k6 = None
                                    self.rib_scale = None
                                    self.metric_version = None
                                    self._segment_path = lambda: "metric" + "[metric-name='" + str(self.metric_name) + "']"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Eigrp.Processes.Process.DefaultVrf.DefaultAfs.DefaultAf.Metrics.Metric, ['metric_name', 'max_hops', 'tos', 'k1', 'k2', 'k3', 'k4', 'k5', 'k6', 'rib_scale', 'metric_version'], name, value)

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_eigrp_cfg as meta
                                    return meta._meta_table['Eigrp.Processes.Process.DefaultVrf.DefaultAfs.DefaultAf.Metrics.Metric']['meta_info']

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_eigrp_cfg as meta
                                return meta._meta_table['Eigrp.Processes.Process.DefaultVrf.DefaultAfs.DefaultAf.Metrics']['meta_info']


                        class Timers(_Entity_):
                            """
                            List of timer configurations
                            
                            .. attribute:: timer
                            
                            	Configure EIGRP timers
                            	**type**\: list of  		 :py:class:`Timer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_cfg.Eigrp.Processes.Process.DefaultVrf.DefaultAfs.DefaultAf.Timers.Timer>`
                            
                            

                            """

                            _prefix = 'eigrp-cfg'
                            _revision = '2018-06-15'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Eigrp.Processes.Process.DefaultVrf.DefaultAfs.DefaultAf.Timers, self).__init__()

                                self.yang_name = "timers"
                                self.yang_parent_name = "default-af"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("timer", ("timer", Eigrp.Processes.Process.DefaultVrf.DefaultAfs.DefaultAf.Timers.Timer))])
                                self._leafs = OrderedDict()

                                self.timer = YList(self)
                                self._segment_path = lambda: "timers"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Eigrp.Processes.Process.DefaultVrf.DefaultAfs.DefaultAf.Timers, [], name, value)


                            class Timer(_Entity_):
                                """
                                Configure EIGRP timers
                                
                                .. attribute:: timer_type  (key)
                                
                                	Type of timer
                                	**type**\:  :py:class:`EigrpTimer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_cfg.EigrpTimer>`
                                
                                .. attribute:: active_time
                                
                                	Active Time (in seconds)
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**units**\: second
                                
                                .. attribute:: hold_time
                                
                                	Hold time (in seconds)
                                	**type**\: int
                                
                                	**range:** 20..6000
                                
                                	**units**\: second
                                
                                .. attribute:: signal_time
                                
                                	Signal time (in seconds)
                                	**type**\: int
                                
                                	**range:** 10..30
                                
                                	**units**\: second
                                
                                .. attribute:: converge_time
                                
                                	Converge time (in seconds)
                                	**type**\: int
                                
                                	**range:** 60..5000
                                
                                	**units**\: second
                                
                                

                                """

                                _prefix = 'eigrp-cfg'
                                _revision = '2018-06-15'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(Eigrp.Processes.Process.DefaultVrf.DefaultAfs.DefaultAf.Timers.Timer, self).__init__()

                                    self.yang_name = "timer"
                                    self.yang_parent_name = "timers"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['timer_type']
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('timer_type', (YLeaf(YType.enumeration, 'timer-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_cfg', 'EigrpTimer', '')])),
                                        ('active_time', (YLeaf(YType.uint32, 'active-time'), ['int'])),
                                        ('hold_time', (YLeaf(YType.uint32, 'hold-time'), ['int'])),
                                        ('signal_time', (YLeaf(YType.uint32, 'signal-time'), ['int'])),
                                        ('converge_time', (YLeaf(YType.uint32, 'converge-time'), ['int'])),
                                    ])
                                    self.timer_type = None
                                    self.active_time = None
                                    self.hold_time = None
                                    self.signal_time = None
                                    self.converge_time = None
                                    self._segment_path = lambda: "timer" + "[timer-type='" + str(self.timer_type) + "']"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Eigrp.Processes.Process.DefaultVrf.DefaultAfs.DefaultAf.Timers.Timer, ['timer_type', 'active_time', 'hold_time', 'signal_time', 'converge_time'], name, value)

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_eigrp_cfg as meta
                                    return meta._meta_table['Eigrp.Processes.Process.DefaultVrf.DefaultAfs.DefaultAf.Timers.Timer']['meta_info']

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_eigrp_cfg as meta
                                return meta._meta_table['Eigrp.Processes.Process.DefaultVrf.DefaultAfs.DefaultAf.Timers']['meta_info']


                        class DefaultAccepts(_Entity_):
                            """
                            Candidate default policy table
                            
                            .. attribute:: default_accept
                            
                            	Candidate default behaviour
                            	**type**\: list of  		 :py:class:`DefaultAccept <ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_cfg.Eigrp.Processes.Process.DefaultVrf.DefaultAfs.DefaultAf.DefaultAccepts.DefaultAccept>`
                            
                            

                            """

                            _prefix = 'eigrp-cfg'
                            _revision = '2018-06-15'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Eigrp.Processes.Process.DefaultVrf.DefaultAfs.DefaultAf.DefaultAccepts, self).__init__()

                                self.yang_name = "default-accepts"
                                self.yang_parent_name = "default-af"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("default-accept", ("default_accept", Eigrp.Processes.Process.DefaultVrf.DefaultAfs.DefaultAf.DefaultAccepts.DefaultAccept))])
                                self._leafs = OrderedDict()

                                self.default_accept = YList(self)
                                self._segment_path = lambda: "default-accepts"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Eigrp.Processes.Process.DefaultVrf.DefaultAfs.DefaultAf.DefaultAccepts, [], name, value)


                            class DefaultAccept(_Entity_):
                                """
                                Candidate default behaviour
                                
                                .. attribute:: direction  (key)
                                
                                	Direction (in or out)
                                	**type**\:  :py:class:`EigrpDir <ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_cfg.EigrpDir>`
                                
                                .. attribute:: policy_name
                                
                                	Policy name
                                	**type**\: str
                                
                                .. attribute:: policy_specified
                                
                                	TRUE if Policy has been specified
                                	**type**\: bool
                                
                                	**mandatory**\: True
                                
                                

                                """

                                _prefix = 'eigrp-cfg'
                                _revision = '2018-06-15'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(Eigrp.Processes.Process.DefaultVrf.DefaultAfs.DefaultAf.DefaultAccepts.DefaultAccept, self).__init__()

                                    self.yang_name = "default-accept"
                                    self.yang_parent_name = "default-accepts"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['direction']
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('direction', (YLeaf(YType.enumeration, 'direction'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_cfg', 'EigrpDir', '')])),
                                        ('policy_name', (YLeaf(YType.str, 'policy-name'), ['str'])),
                                        ('policy_specified', (YLeaf(YType.boolean, 'policy-specified'), ['bool'])),
                                    ])
                                    self.direction = None
                                    self.policy_name = None
                                    self.policy_specified = None
                                    self._segment_path = lambda: "default-accept" + "[direction='" + str(self.direction) + "']"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Eigrp.Processes.Process.DefaultVrf.DefaultAfs.DefaultAf.DefaultAccepts.DefaultAccept, ['direction', 'policy_name', 'policy_specified'], name, value)

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_eigrp_cfg as meta
                                    return meta._meta_table['Eigrp.Processes.Process.DefaultVrf.DefaultAfs.DefaultAf.DefaultAccepts.DefaultAccept']['meta_info']

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_eigrp_cfg as meta
                                return meta._meta_table['Eigrp.Processes.Process.DefaultVrf.DefaultAfs.DefaultAf.DefaultAccepts']['meta_info']


                        class Interfaces(_Entity_):
                            """
                            List of interfaces
                            
                            .. attribute:: interface
                            
                            	Configuration for an Interface.Deletion of this object also causes deletion of all objectsunder 'Interface' associated with this interface instance
                            	**type**\: list of  		 :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_cfg.Eigrp.Processes.Process.DefaultVrf.DefaultAfs.DefaultAf.Interfaces.Interface>`
                            
                            

                            """

                            _prefix = 'eigrp-cfg'
                            _revision = '2018-06-15'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Eigrp.Processes.Process.DefaultVrf.DefaultAfs.DefaultAf.Interfaces, self).__init__()

                                self.yang_name = "interfaces"
                                self.yang_parent_name = "default-af"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("interface", ("interface", Eigrp.Processes.Process.DefaultVrf.DefaultAfs.DefaultAf.Interfaces.Interface))])
                                self._leafs = OrderedDict()

                                self.interface = YList(self)
                                self._segment_path = lambda: "interfaces"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Eigrp.Processes.Process.DefaultVrf.DefaultAfs.DefaultAf.Interfaces, [], name, value)


                            class Interface(_Entity_):
                                """
                                Configuration for an Interface.Deletion of this
                                object also causes deletion of all objectsunder
                                'Interface' associated with this interface
                                instance.
                                
                                .. attribute:: interface_name  (key)
                                
                                	Interface name
                                	**type**\: str
                                
                                	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                                
                                .. attribute:: interface_metric
                                
                                	Metric
                                	**type**\:  :py:class:`InterfaceMetric <ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_cfg.Eigrp.Processes.Process.DefaultVrf.DefaultAfs.DefaultAf.Interfaces.Interface.InterfaceMetric>`
                                
                                .. attribute:: remote_neighbor
                                
                                	Remote\-Neighbors enabled, default is 65535
                                	**type**\:  :py:class:`RemoteNeighbor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_cfg.Eigrp.Processes.Process.DefaultVrf.DefaultAfs.DefaultAf.Interfaces.Interface.RemoteNeighbor>`
                                
                                	**presence node**\: True
                                
                                .. attribute:: bfd
                                
                                	Configure BFD parameters
                                	**type**\:  :py:class:`Bfd <ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_cfg.Eigrp.Processes.Process.DefaultVrf.DefaultAfs.DefaultAf.Interfaces.Interface.Bfd>`
                                
                                .. attribute:: site_of_origin
                                
                                	Configure Site\-of\-origin
                                	**type**\:  :py:class:`SiteOfOrigin <ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_cfg.Eigrp.Processes.Process.DefaultVrf.DefaultAfs.DefaultAf.Interfaces.Interface.SiteOfOrigin>`
                                
                                .. attribute:: authentication
                                
                                	Authentication configuration
                                	**type**\:  :py:class:`Authentication <ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_cfg.Eigrp.Processes.Process.DefaultVrf.DefaultAfs.DefaultAf.Interfaces.Interface.Authentication>`
                                
                                .. attribute:: summary_addresses
                                
                                	List of summary addresses under this interface
                                	**type**\:  :py:class:`SummaryAddresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_cfg.Eigrp.Processes.Process.DefaultVrf.DefaultAfs.DefaultAf.Interfaces.Interface.SummaryAddresses>`
                                
                                .. attribute:: interface_filter_policies
                                
                                	List of filter policies
                                	**type**\:  :py:class:`InterfaceFilterPolicies <ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_cfg.Eigrp.Processes.Process.DefaultVrf.DefaultAfs.DefaultAf.Interfaces.Interface.InterfaceFilterPolicies>`
                                
                                .. attribute:: interface_static_neighbors
                                
                                	List of Neighbors
                                	**type**\:  :py:class:`InterfaceStaticNeighbors <ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_cfg.Eigrp.Processes.Process.DefaultVrf.DefaultAfs.DefaultAf.Interfaces.Interface.InterfaceStaticNeighbors>`
                                
                                .. attribute:: hold_time
                                
                                	Neighbor hold time (in seconds)
                                	**type**\: int
                                
                                	**range:** 1..65535
                                
                                	**units**\: second
                                
                                .. attribute:: bandwidth_percent
                                
                                	Bandwidth limit
                                	**type**\: int
                                
                                	**range:** 1..999999
                                
                                	**units**\: percentage
                                
                                .. attribute:: passive_interface
                                
                                	Suppress routing updates on an interface
                                	**type**\: bool
                                
                                .. attribute:: hello_interval
                                
                                	Interval (in seconds)
                                	**type**\: int
                                
                                	**range:** 1..65535
                                
                                	**units**\: second
                                
                                .. attribute:: next_hop_self
                                
                                	Disable next\-hop\-self
                                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                                
                                .. attribute:: enable
                                
                                	Enable Interface configuration
                                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                                
                                .. attribute:: split_horizon
                                
                                	Configure split horizon behaviour
                                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                                
                                

                                """

                                _prefix = 'eigrp-cfg'
                                _revision = '2018-06-15'

                                def __init__(self):
                                    if sys.version_info > (3,):
                                        super().__init__()
                                    else:
                                        super(Eigrp.Processes.Process.DefaultVrf.DefaultAfs.DefaultAf.Interfaces.Interface, self).__init__()

                                    self.yang_name = "interface"
                                    self.yang_parent_name = "interfaces"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['interface_name']
                                    self._child_classes = OrderedDict([("interface-metric", ("interface_metric", Eigrp.Processes.Process.DefaultVrf.DefaultAfs.DefaultAf.Interfaces.Interface.InterfaceMetric)), ("remote-neighbor", ("remote_neighbor", Eigrp.Processes.Process.DefaultVrf.DefaultAfs.DefaultAf.Interfaces.Interface.RemoteNeighbor)), ("bfd", ("bfd", Eigrp.Processes.Process.DefaultVrf.DefaultAfs.DefaultAf.Interfaces.Interface.Bfd)), ("site-of-origin", ("site_of_origin", Eigrp.Processes.Process.DefaultVrf.DefaultAfs.DefaultAf.Interfaces.Interface.SiteOfOrigin)), ("authentication", ("authentication", Eigrp.Processes.Process.DefaultVrf.DefaultAfs.DefaultAf.Interfaces.Interface.Authentication)), ("summary-addresses", ("summary_addresses", Eigrp.Processes.Process.DefaultVrf.DefaultAfs.DefaultAf.Interfaces.Interface.SummaryAddresses)), ("interface-filter-policies", ("interface_filter_policies", Eigrp.Processes.Process.DefaultVrf.DefaultAfs.DefaultAf.Interfaces.Interface.InterfaceFilterPolicies)), ("interface-static-neighbors", ("interface_static_neighbors", Eigrp.Processes.Process.DefaultVrf.DefaultAfs.DefaultAf.Interfaces.Interface.InterfaceStaticNeighbors))])
                                    self._leafs = OrderedDict([
                                        ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                                        ('hold_time', (YLeaf(YType.uint32, 'hold-time'), ['int'])),
                                        ('bandwidth_percent', (YLeaf(YType.uint32, 'bandwidth-percent'), ['int'])),
                                        ('passive_interface', (YLeaf(YType.boolean, 'passive-interface'), ['bool'])),
                                        ('hello_interval', (YLeaf(YType.uint32, 'hello-interval'), ['int'])),
                                        ('next_hop_self', (YLeaf(YType.empty, 'next-hop-self'), ['Empty'])),
                                        ('enable', (YLeaf(YType.empty, 'enable'), ['Empty'])),
                                        ('split_horizon', (YLeaf(YType.empty, 'split-horizon'), ['Empty'])),
                                    ])
                                    self.interface_name = None
                                    self.hold_time = None
                                    self.bandwidth_percent = None
                                    self.passive_interface = None
                                    self.hello_interval = None
                                    self.next_hop_self = None
                                    self.enable = None
                                    self.split_horizon = None

                                    self.interface_metric = Eigrp.Processes.Process.DefaultVrf.DefaultAfs.DefaultAf.Interfaces.Interface.InterfaceMetric()
                                    self.interface_metric.parent = self
                                    self._children_name_map["interface_metric"] = "interface-metric"

                                    self.remote_neighbor = None
                                    self._children_name_map["remote_neighbor"] = "remote-neighbor"

                                    self.bfd = Eigrp.Processes.Process.DefaultVrf.DefaultAfs.DefaultAf.Interfaces.Interface.Bfd()
                                    self.bfd.parent = self
                                    self._children_name_map["bfd"] = "bfd"

                                    self.site_of_origin = Eigrp.Processes.Process.DefaultVrf.DefaultAfs.DefaultAf.Interfaces.Interface.SiteOfOrigin()
                                    self.site_of_origin.parent = self
                                    self._children_name_map["site_of_origin"] = "site-of-origin"

                                    self.authentication = Eigrp.Processes.Process.DefaultVrf.DefaultAfs.DefaultAf.Interfaces.Interface.Authentication()
                                    self.authentication.parent = self
                                    self._children_name_map["authentication"] = "authentication"

                                    self.summary_addresses = Eigrp.Processes.Process.DefaultVrf.DefaultAfs.DefaultAf.Interfaces.Interface.SummaryAddresses()
                                    self.summary_addresses.parent = self
                                    self._children_name_map["summary_addresses"] = "summary-addresses"

                                    self.interface_filter_policies = Eigrp.Processes.Process.DefaultVrf.DefaultAfs.DefaultAf.Interfaces.Interface.InterfaceFilterPolicies()
                                    self.interface_filter_policies.parent = self
                                    self._children_name_map["interface_filter_policies"] = "interface-filter-policies"

                                    self.interface_static_neighbors = Eigrp.Processes.Process.DefaultVrf.DefaultAfs.DefaultAf.Interfaces.Interface.InterfaceStaticNeighbors()
                                    self.interface_static_neighbors.parent = self
                                    self._children_name_map["interface_static_neighbors"] = "interface-static-neighbors"
                                    self._segment_path = lambda: "interface" + "[interface-name='" + str(self.interface_name) + "']"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Eigrp.Processes.Process.DefaultVrf.DefaultAfs.DefaultAf.Interfaces.Interface, ['interface_name', 'hold_time', 'bandwidth_percent', 'passive_interface', 'hello_interval', 'next_hop_self', 'enable', 'split_horizon'], name, value)


                                class InterfaceMetric(_Entity_):
                                    """
                                    Metric
                                    
                                    .. attribute:: bandwidth
                                    
                                    	Bandwidth in Kbits per second
                                    	**type**\: int
                                    
                                    	**range:** 1..4294967295
                                    
                                    	**units**\: kbit/s
                                    
                                    .. attribute:: delay
                                    
                                    	Delay metric, in 10 microsecond units (default) or picosecond units
                                    	**type**\: int
                                    
                                    	**range:** 1..4294967295
                                    
                                    .. attribute:: delay_unit
                                    
                                    	Delay unit
                                    	**type**\:  :py:class:`EigrpDelayUnit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_cfg.EigrpDelayUnit>`
                                    
                                    .. attribute:: reliability
                                    
                                    	Reliability metric where 255 is 100% reliable
                                    	**type**\: int
                                    
                                    	**range:** 0..255
                                    
                                    .. attribute:: load
                                    
                                    	Effective bandwidth metric (Loading) where 255 is 100% loaded
                                    	**type**\: int
                                    
                                    	**range:** 1..255
                                    
                                    

                                    """

                                    _prefix = 'eigrp-cfg'
                                    _revision = '2018-06-15'

                                    def __init__(self):
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
                                            super(Eigrp.Processes.Process.DefaultVrf.DefaultAfs.DefaultAf.Interfaces.Interface.InterfaceMetric, self).__init__()

                                        self.yang_name = "interface-metric"
                                        self.yang_parent_name = "interface"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('bandwidth', (YLeaf(YType.uint32, 'bandwidth'), ['int'])),
                                            ('delay', (YLeaf(YType.uint32, 'delay'), ['int'])),
                                            ('delay_unit', (YLeaf(YType.enumeration, 'delay-unit'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_cfg', 'EigrpDelayUnit', '')])),
                                            ('reliability', (YLeaf(YType.uint32, 'reliability'), ['int'])),
                                            ('load', (YLeaf(YType.uint32, 'load'), ['int'])),
                                        ])
                                        self.bandwidth = None
                                        self.delay = None
                                        self.delay_unit = None
                                        self.reliability = None
                                        self.load = None
                                        self._segment_path = lambda: "interface-metric"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Eigrp.Processes.Process.DefaultVrf.DefaultAfs.DefaultAf.Interfaces.Interface.InterfaceMetric, ['bandwidth', 'delay', 'delay_unit', 'reliability', 'load'], name, value)

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_eigrp_cfg as meta
                                        return meta._meta_table['Eigrp.Processes.Process.DefaultVrf.DefaultAfs.DefaultAf.Interfaces.Interface.InterfaceMetric']['meta_info']


                                class RemoteNeighbor(_Entity_):
                                    """
                                    Remote\-Neighbors enabled, default is 65535
                                    
                                    .. attribute:: enable
                                    
                                    	Enable Remote neighbor unicast\-listen
                                    	**type**\: bool
                                    
                                    	**mandatory**\: True
                                    
                                    .. attribute:: allow_list
                                    
                                    	Policy name
                                    	**type**\: str
                                    
                                    .. attribute:: max_neighbors
                                    
                                    	Neighbor count
                                    	**type**\: int
                                    
                                    	**range:** 1..65535
                                    
                                    

                                    This class is a :ref:`presence class<presence-class>`

                                    """

                                    _prefix = 'eigrp-cfg'
                                    _revision = '2018-06-15'

                                    def __init__(self):
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
                                            super(Eigrp.Processes.Process.DefaultVrf.DefaultAfs.DefaultAf.Interfaces.Interface.RemoteNeighbor, self).__init__()

                                        self.yang_name = "remote-neighbor"
                                        self.yang_parent_name = "interface"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self.is_presence_container = True
                                        self._leafs = OrderedDict([
                                            ('enable', (YLeaf(YType.boolean, 'enable'), ['bool'])),
                                            ('allow_list', (YLeaf(YType.str, 'allow-list'), ['str'])),
                                            ('max_neighbors', (YLeaf(YType.uint32, 'max-neighbors'), ['int'])),
                                        ])
                                        self.enable = None
                                        self.allow_list = None
                                        self.max_neighbors = None
                                        self._segment_path = lambda: "remote-neighbor"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Eigrp.Processes.Process.DefaultVrf.DefaultAfs.DefaultAf.Interfaces.Interface.RemoteNeighbor, ['enable', 'allow_list', 'max_neighbors'], name, value)

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_eigrp_cfg as meta
                                        return meta._meta_table['Eigrp.Processes.Process.DefaultVrf.DefaultAfs.DefaultAf.Interfaces.Interface.RemoteNeighbor']['meta_info']


                                class Bfd(_Entity_):
                                    """
                                    Configure BFD parameters
                                    
                                    .. attribute:: fast_detect
                                    
                                    	Enable BFD fast detection
                                    	**type**\: bool
                                    
                                    .. attribute:: detection_multiplier
                                    
                                    	Detect multiplier
                                    	**type**\: int
                                    
                                    	**range:** 2..50
                                    
                                    .. attribute:: interval
                                    
                                    	Hello interval in milli\-seconds
                                    	**type**\: int
                                    
                                    	**range:** 15..3000
                                    
                                    	**units**\: millisecond
                                    
                                    

                                    """

                                    _prefix = 'eigrp-cfg'
                                    _revision = '2018-06-15'

                                    def __init__(self):
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
                                            super(Eigrp.Processes.Process.DefaultVrf.DefaultAfs.DefaultAf.Interfaces.Interface.Bfd, self).__init__()

                                        self.yang_name = "bfd"
                                        self.yang_parent_name = "interface"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('fast_detect', (YLeaf(YType.boolean, 'fast-detect'), ['bool'])),
                                            ('detection_multiplier', (YLeaf(YType.uint32, 'detection-multiplier'), ['int'])),
                                            ('interval', (YLeaf(YType.uint32, 'interval'), ['int'])),
                                        ])
                                        self.fast_detect = None
                                        self.detection_multiplier = None
                                        self.interval = None
                                        self._segment_path = lambda: "bfd"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Eigrp.Processes.Process.DefaultVrf.DefaultAfs.DefaultAf.Interfaces.Interface.Bfd, ['fast_detect', 'detection_multiplier', 'interval'], name, value)

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_eigrp_cfg as meta
                                        return meta._meta_table['Eigrp.Processes.Process.DefaultVrf.DefaultAfs.DefaultAf.Interfaces.Interface.Bfd']['meta_info']


                                class SiteOfOrigin(_Entity_):
                                    """
                                    Configure Site\-of\-origin
                                    
                                    .. attribute:: type
                                    
                                    	SoO type
                                    	**type**\:  :py:class:`EigrpSoo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_cfg.EigrpSoo>`
                                    
                                    .. attribute:: as_xx
                                    
                                    	Higher sixteen bits of 4\-byte BGP AS Number
                                    	**type**\: int
                                    
                                    	**range:** 0..65535
                                    
                                    .. attribute:: as_yy
                                    
                                    	2\-byte or 4\-byte BGP AS Number
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: index
                                    
                                    	AS Number Index
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: address
                                    
                                    	IPv4 address
                                    	**type**\: str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    .. attribute:: address_index
                                    
                                    	IPv4 address index
                                    	**type**\: int
                                    
                                    	**range:** 0..65535
                                    
                                    

                                    """

                                    _prefix = 'eigrp-cfg'
                                    _revision = '2018-06-15'

                                    def __init__(self):
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
                                            super(Eigrp.Processes.Process.DefaultVrf.DefaultAfs.DefaultAf.Interfaces.Interface.SiteOfOrigin, self).__init__()

                                        self.yang_name = "site-of-origin"
                                        self.yang_parent_name = "interface"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('type', (YLeaf(YType.enumeration, 'type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_cfg', 'EigrpSoo', '')])),
                                            ('as_xx', (YLeaf(YType.uint32, 'as-xx'), ['int'])),
                                            ('as_yy', (YLeaf(YType.uint32, 'as-yy'), ['int'])),
                                            ('index', (YLeaf(YType.uint32, 'index'), ['int'])),
                                            ('address', (YLeaf(YType.str, 'address'), ['str'])),
                                            ('address_index', (YLeaf(YType.uint32, 'address-index'), ['int'])),
                                        ])
                                        self.type = None
                                        self.as_xx = None
                                        self.as_yy = None
                                        self.index = None
                                        self.address = None
                                        self.address_index = None
                                        self._segment_path = lambda: "site-of-origin"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Eigrp.Processes.Process.DefaultVrf.DefaultAfs.DefaultAf.Interfaces.Interface.SiteOfOrigin, ['type', 'as_xx', 'as_yy', 'index', 'address', 'address_index'], name, value)

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_eigrp_cfg as meta
                                        return meta._meta_table['Eigrp.Processes.Process.DefaultVrf.DefaultAfs.DefaultAf.Interfaces.Interface.SiteOfOrigin']['meta_info']


                                class Authentication(_Entity_):
                                    """
                                    Authentication configuration
                                    
                                    .. attribute:: keychain
                                    
                                    	Authentication keychain configuration
                                    	**type**\: str
                                    
                                    

                                    """

                                    _prefix = 'eigrp-cfg'
                                    _revision = '2018-06-15'

                                    def __init__(self):
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
                                            super(Eigrp.Processes.Process.DefaultVrf.DefaultAfs.DefaultAf.Interfaces.Interface.Authentication, self).__init__()

                                        self.yang_name = "authentication"
                                        self.yang_parent_name = "interface"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('keychain', (YLeaf(YType.str, 'keychain'), ['str'])),
                                        ])
                                        self.keychain = None
                                        self._segment_path = lambda: "authentication"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Eigrp.Processes.Process.DefaultVrf.DefaultAfs.DefaultAf.Interfaces.Interface.Authentication, ['keychain'], name, value)

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_eigrp_cfg as meta
                                        return meta._meta_table['Eigrp.Processes.Process.DefaultVrf.DefaultAfs.DefaultAf.Interfaces.Interface.Authentication']['meta_info']


                                class SummaryAddresses(_Entity_):
                                    """
                                    List of summary addresses under this interface
                                    
                                    .. attribute:: summary_address
                                    
                                    	Summary address
                                    	**type**\: list of  		 :py:class:`SummaryAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_cfg.Eigrp.Processes.Process.DefaultVrf.DefaultAfs.DefaultAf.Interfaces.Interface.SummaryAddresses.SummaryAddress>`
                                    
                                    

                                    """

                                    _prefix = 'eigrp-cfg'
                                    _revision = '2018-06-15'

                                    def __init__(self):
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
                                            super(Eigrp.Processes.Process.DefaultVrf.DefaultAfs.DefaultAf.Interfaces.Interface.SummaryAddresses, self).__init__()

                                        self.yang_name = "summary-addresses"
                                        self.yang_parent_name = "interface"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("summary-address", ("summary_address", Eigrp.Processes.Process.DefaultVrf.DefaultAfs.DefaultAf.Interfaces.Interface.SummaryAddresses.SummaryAddress))])
                                        self._leafs = OrderedDict()

                                        self.summary_address = YList(self)
                                        self._segment_path = lambda: "summary-addresses"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Eigrp.Processes.Process.DefaultVrf.DefaultAfs.DefaultAf.Interfaces.Interface.SummaryAddresses, [], name, value)


                                    class SummaryAddress(_Entity_):
                                        """
                                        Summary address
                                        
                                        .. attribute:: summary_address_addr  (key)
                                        
                                        	Summary Prefix (address part)
                                        	**type**\: union of the below types:
                                        
                                        		**type**\: str
                                        
                                        			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                        
                                        		**type**\: str
                                        
                                        			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                        
                                        .. attribute:: summary_address_prefix  (key)
                                        
                                        	Summary Prefix (prefix part)
                                        	**type**\: int
                                        
                                        	**range:** 0..128
                                        
                                        .. attribute:: distance
                                        
                                        	Administrative distance
                                        	**type**\: int
                                        
                                        	**range:** 1..255
                                        
                                        	**mandatory**\: True
                                        
                                        

                                        """

                                        _prefix = 'eigrp-cfg'
                                        _revision = '2018-06-15'

                                        def __init__(self):
                                            if sys.version_info > (3,):
                                                super().__init__()
                                            else:
                                                super(Eigrp.Processes.Process.DefaultVrf.DefaultAfs.DefaultAf.Interfaces.Interface.SummaryAddresses.SummaryAddress, self).__init__()

                                            self.yang_name = "summary-address"
                                            self.yang_parent_name = "summary-addresses"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = ['summary_address_addr','summary_address_prefix']
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('summary_address_addr', (YLeaf(YType.str, 'summary-address-addr'), ['str','str'])),
                                                ('summary_address_prefix', (YLeaf(YType.uint16, 'summary-address-prefix'), ['int'])),
                                                ('distance', (YLeaf(YType.uint32, 'distance'), ['int'])),
                                            ])
                                            self.summary_address_addr = None
                                            self.summary_address_prefix = None
                                            self.distance = None
                                            self._segment_path = lambda: "summary-address" + "[summary-address-addr='" + str(self.summary_address_addr) + "']" + "[summary-address-prefix='" + str(self.summary_address_prefix) + "']"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Eigrp.Processes.Process.DefaultVrf.DefaultAfs.DefaultAf.Interfaces.Interface.SummaryAddresses.SummaryAddress, ['summary_address_addr', 'summary_address_prefix', 'distance'], name, value)

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_eigrp_cfg as meta
                                            return meta._meta_table['Eigrp.Processes.Process.DefaultVrf.DefaultAfs.DefaultAf.Interfaces.Interface.SummaryAddresses.SummaryAddress']['meta_info']

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_eigrp_cfg as meta
                                        return meta._meta_table['Eigrp.Processes.Process.DefaultVrf.DefaultAfs.DefaultAf.Interfaces.Interface.SummaryAddresses']['meta_info']


                                class InterfaceFilterPolicies(_Entity_):
                                    """
                                    List of filter policies
                                    
                                    .. attribute:: interface_filter_policy
                                    
                                    	none
                                    	**type**\: list of  		 :py:class:`InterfaceFilterPolicy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_cfg.Eigrp.Processes.Process.DefaultVrf.DefaultAfs.DefaultAf.Interfaces.Interface.InterfaceFilterPolicies.InterfaceFilterPolicy>`
                                    
                                    

                                    """

                                    _prefix = 'eigrp-cfg'
                                    _revision = '2018-06-15'

                                    def __init__(self):
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
                                            super(Eigrp.Processes.Process.DefaultVrf.DefaultAfs.DefaultAf.Interfaces.Interface.InterfaceFilterPolicies, self).__init__()

                                        self.yang_name = "interface-filter-policies"
                                        self.yang_parent_name = "interface"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("interface-filter-policy", ("interface_filter_policy", Eigrp.Processes.Process.DefaultVrf.DefaultAfs.DefaultAf.Interfaces.Interface.InterfaceFilterPolicies.InterfaceFilterPolicy))])
                                        self._leafs = OrderedDict()

                                        self.interface_filter_policy = YList(self)
                                        self._segment_path = lambda: "interface-filter-policies"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Eigrp.Processes.Process.DefaultVrf.DefaultAfs.DefaultAf.Interfaces.Interface.InterfaceFilterPolicies, [], name, value)


                                    class InterfaceFilterPolicy(_Entity_):
                                        """
                                        none
                                        
                                        .. attribute:: direction  (key)
                                        
                                        	Direction (in or out)
                                        	**type**\:  :py:class:`EigrpDir <ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_cfg.EigrpDir>`
                                        
                                        .. attribute:: policy_name
                                        
                                        	Policy name
                                        	**type**\: str
                                        
                                        	**mandatory**\: True
                                        
                                        

                                        """

                                        _prefix = 'eigrp-cfg'
                                        _revision = '2018-06-15'

                                        def __init__(self):
                                            if sys.version_info > (3,):
                                                super().__init__()
                                            else:
                                                super(Eigrp.Processes.Process.DefaultVrf.DefaultAfs.DefaultAf.Interfaces.Interface.InterfaceFilterPolicies.InterfaceFilterPolicy, self).__init__()

                                            self.yang_name = "interface-filter-policy"
                                            self.yang_parent_name = "interface-filter-policies"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = ['direction']
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('direction', (YLeaf(YType.enumeration, 'direction'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_cfg', 'EigrpDir', '')])),
                                                ('policy_name', (YLeaf(YType.str, 'policy-name'), ['str'])),
                                            ])
                                            self.direction = None
                                            self.policy_name = None
                                            self._segment_path = lambda: "interface-filter-policy" + "[direction='" + str(self.direction) + "']"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Eigrp.Processes.Process.DefaultVrf.DefaultAfs.DefaultAf.Interfaces.Interface.InterfaceFilterPolicies.InterfaceFilterPolicy, ['direction', 'policy_name'], name, value)

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_eigrp_cfg as meta
                                            return meta._meta_table['Eigrp.Processes.Process.DefaultVrf.DefaultAfs.DefaultAf.Interfaces.Interface.InterfaceFilterPolicies.InterfaceFilterPolicy']['meta_info']

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_eigrp_cfg as meta
                                        return meta._meta_table['Eigrp.Processes.Process.DefaultVrf.DefaultAfs.DefaultAf.Interfaces.Interface.InterfaceFilterPolicies']['meta_info']


                                class InterfaceStaticNeighbors(_Entity_):
                                    """
                                    List of Neighbors
                                    
                                    .. attribute:: interface_static_neighbor
                                    
                                    	Configure Neighbor
                                    	**type**\: list of  		 :py:class:`InterfaceStaticNeighbor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_eigrp_cfg.Eigrp.Processes.Process.DefaultVrf.DefaultAfs.DefaultAf.Interfaces.Interface.InterfaceStaticNeighbors.InterfaceStaticNeighbor>`
                                    
                                    

                                    """

                                    _prefix = 'eigrp-cfg'
                                    _revision = '2018-06-15'

                                    def __init__(self):
                                        if sys.version_info > (3,):
                                            super().__init__()
                                        else:
                                            super(Eigrp.Processes.Process.DefaultVrf.DefaultAfs.DefaultAf.Interfaces.Interface.InterfaceStaticNeighbors, self).__init__()

                                        self.yang_name = "interface-static-neighbors"
                                        self.yang_parent_name = "interface"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("interface-static-neighbor", ("interface_static_neighbor", Eigrp.Processes.Process.DefaultVrf.DefaultAfs.DefaultAf.Interfaces.Interface.InterfaceStaticNeighbors.InterfaceStaticNeighbor))])
                                        self._leafs = OrderedDict()

                                        self.interface_static_neighbor = YList(self)
                                        self._segment_path = lambda: "interface-static-neighbors"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Eigrp.Processes.Process.DefaultVrf.DefaultAfs.DefaultAf.Interfaces.Interface.InterfaceStaticNeighbors, [], name, value)


                                    class InterfaceStaticNeighbor(_Entity_):
                                        """
                                        Configure Neighbor
                                        
                                        .. attribute:: neighbor_address  (key)
                                        
                                        	Neighbor IP address
                                        	**type**\: union of the below types:
                                        
                                        		**type**\: str
                                        
                                        			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                        
                                        		**type**\: str
                                        
                                        			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                        
                                        .. attribute:: max_hops
                                        
                                        	Number of hops
                                        	**type**\: int
                                        
                                        	**range:** 2..100
                                        
                                        	**mandatory**\: True
                                        
                                        

                                        """

                                        _prefix = 'eigrp-cfg'
                                        _revision = '2018-06-15'

                                        def __init__(self):
                                            if sys.version_info > (3,):
                                                super().__init__()
                                            else:
                                                super(Eigrp.Processes.Process.DefaultVrf.DefaultAfs.DefaultAf.Interfaces.Interface.InterfaceStaticNeighbors.InterfaceStaticNeighbor, self).__init__()

                                            self.yang_name = "interface-static-neighbor"
                                            self.yang_parent_name = "interface-static-neighbors"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = ['neighbor_address']
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('neighbor_address', (YLeaf(YType.str, 'neighbor-address'), ['str','str'])),
                                                ('max_hops', (YLeaf(YType.uint32, 'max-hops'), ['int'])),
                                            ])
                                            self.neighbor_address = None
                                            self.max_hops = None
                                            self._segment_path = lambda: "interface-static-neighbor" + "[neighbor-address='" + str(self.neighbor_address) + "']"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Eigrp.Processes.Process.DefaultVrf.DefaultAfs.DefaultAf.Interfaces.Interface.InterfaceStaticNeighbors.InterfaceStaticNeighbor, ['neighbor_address', 'max_hops'], name, value)

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_eigrp_cfg as meta
                                            return meta._meta_table['Eigrp.Processes.Process.DefaultVrf.DefaultAfs.DefaultAf.Interfaces.Interface.InterfaceStaticNeighbors.InterfaceStaticNeighbor']['meta_info']

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_eigrp_cfg as meta
                                        return meta._meta_table['Eigrp.Processes.Process.DefaultVrf.DefaultAfs.DefaultAf.Interfaces.Interface.InterfaceStaticNeighbors']['meta_info']

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_eigrp_cfg as meta
                                    return meta._meta_table['Eigrp.Processes.Process.DefaultVrf.DefaultAfs.DefaultAf.Interfaces.Interface']['meta_info']

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_eigrp_cfg as meta
                                return meta._meta_table['Eigrp.Processes.Process.DefaultVrf.DefaultAfs.DefaultAf.Interfaces']['meta_info']


                        class Distance(_Entity_):
                            """
                            Set distance for EIGRP routes
                            
                            .. attribute:: internal_distance
                            
                            	Internal routes' distance
                            	**type**\: int
                            
                            	**range:** 1..255
                            
                            .. attribute:: external_distance
                            
                            	External routes' distance
                            	**type**\: int
                            
                            	**range:** 1..255
                            
                            

                            """

                            _prefix = 'eigrp-cfg'
                            _revision = '2018-06-15'

                            def __init__(self):
                                if sys.version_info > (3,):
                                    super().__init__()
                                else:
                                    super(Eigrp.Processes.Process.DefaultVrf.DefaultAfs.DefaultAf.Distance, self).__init__()

                                self.yang_name = "distance"
                                self.yang_parent_name = "default-af"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('internal_distance', (YLeaf(YType.uint32, 'internal-distance'), ['int'])),
                                    ('external_distance', (YLeaf(YType.uint32, 'external-distance'), ['int'])),
                                ])
                                self.internal_distance = None
                                self.external_distance = None
                                self._segment_path = lambda: "distance"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Eigrp.Processes.Process.DefaultVrf.DefaultAfs.DefaultAf.Distance, ['internal_distance', 'external_distance'], name, value)

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_eigrp_cfg as meta
                                return meta._meta_table['Eigrp.Processes.Process.DefaultVrf.DefaultAfs.DefaultAf.Distance']['meta_info']

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_eigrp_cfg as meta
                            return meta._meta_table['Eigrp.Processes.Process.DefaultVrf.DefaultAfs.DefaultAf']['meta_info']

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_eigrp_cfg as meta
                        return meta._meta_table['Eigrp.Processes.Process.DefaultVrf.DefaultAfs']['meta_info']

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_eigrp_cfg as meta
                    return meta._meta_table['Eigrp.Processes.Process.DefaultVrf']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_eigrp_cfg as meta
                return meta._meta_table['Eigrp.Processes.Process']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_eigrp_cfg as meta
            return meta._meta_table['Eigrp.Processes']['meta_info']

    def clone_ptr(self):
        self._top_entity = Eigrp()
        return self._top_entity

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_eigrp_cfg as meta
        return meta._meta_table['Eigrp']['meta_info']


