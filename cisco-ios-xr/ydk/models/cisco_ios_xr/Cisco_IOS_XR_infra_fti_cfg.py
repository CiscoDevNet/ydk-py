""" Cisco_IOS_XR_infra_fti_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR infra\-fti package configuration.

This module contains definitions
for the following management objects\:
  dci\-fabric\-interconnect\: Configure FTI
    parameters/sub\-parameters

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class DciFabricInterconnect(Entity):
    """
    Configure FTI parameters/sub\-parameters
    
    .. attribute:: fabrics
    
    	Configure fabric parameters
    	**type**\:  :py:class:`Fabrics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_fti_cfg.DciFabricInterconnect.Fabrics>`
    
    .. attribute:: acp
    
    	Configure Auto Config Pool parameters
    	**type**\:  :py:class:`Acp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_fti_cfg.DciFabricInterconnect.Acp>`
    
    .. attribute:: identity
    
    	Identity (Loopback IP address)<x.x.x.x>
    	**type**\: str
    
    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
    
    

    """

    _prefix = 'infra-fti-cfg'
    _revision = '2017-11-13'

    def __init__(self):
        super(DciFabricInterconnect, self).__init__()
        self._top_entity = None

        self.yang_name = "dci-fabric-interconnect"
        self.yang_parent_name = "Cisco-IOS-XR-infra-fti-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("fabrics", ("fabrics", DciFabricInterconnect.Fabrics)), ("acp", ("acp", DciFabricInterconnect.Acp))])
        self._leafs = OrderedDict([
            ('identity', (YLeaf(YType.str, 'identity'), ['str'])),
        ])
        self.identity = None

        self.fabrics = DciFabricInterconnect.Fabrics()
        self.fabrics.parent = self
        self._children_name_map["fabrics"] = "fabrics"

        self.acp = DciFabricInterconnect.Acp()
        self.acp.parent = self
        self._children_name_map["acp"] = "acp"
        self._segment_path = lambda: "Cisco-IOS-XR-infra-fti-cfg:dci-fabric-interconnect"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(DciFabricInterconnect, ['identity'], name, value)


    class Fabrics(Entity):
        """
        Configure fabric parameters
        
        .. attribute:: fabric
        
        	Enter fabric identifier
        	**type**\: list of  		 :py:class:`Fabric <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_fti_cfg.DciFabricInterconnect.Fabrics.Fabric>`
        
        

        """

        _prefix = 'infra-fti-cfg'
        _revision = '2017-11-13'

        def __init__(self):
            super(DciFabricInterconnect.Fabrics, self).__init__()

            self.yang_name = "fabrics"
            self.yang_parent_name = "dci-fabric-interconnect"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("fabric", ("fabric", DciFabricInterconnect.Fabrics.Fabric))])
            self._leafs = OrderedDict()

            self.fabric = YList(self)
            self._segment_path = lambda: "fabrics"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-fti-cfg:dci-fabric-interconnect/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(DciFabricInterconnect.Fabrics, [], name, value)


        class Fabric(Entity):
            """
            Enter fabric identifier
            
            .. attribute:: id1  (key)
            
            	fabric identifier
            	**type**\: int
            
            	**range:** 1000..9999
            
            .. attribute:: controllers
            
            	Enter Opflex peer info
            	**type**\:  :py:class:`Controllers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_fti_cfg.DciFabricInterconnect.Fabrics.Fabric.Controllers>`
            
            .. attribute:: ssl
            
            	Disabled or Path to certificate
            	**type**\: str
            
            

            """

            _prefix = 'infra-fti-cfg'
            _revision = '2017-11-13'

            def __init__(self):
                super(DciFabricInterconnect.Fabrics.Fabric, self).__init__()

                self.yang_name = "fabric"
                self.yang_parent_name = "fabrics"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['id1']
                self._child_classes = OrderedDict([("controllers", ("controllers", DciFabricInterconnect.Fabrics.Fabric.Controllers))])
                self._leafs = OrderedDict([
                    ('id1', (YLeaf(YType.uint32, 'id1'), ['int'])),
                    ('ssl', (YLeaf(YType.str, 'ssl'), ['str'])),
                ])
                self.id1 = None
                self.ssl = None

                self.controllers = DciFabricInterconnect.Fabrics.Fabric.Controllers()
                self.controllers.parent = self
                self._children_name_map["controllers"] = "controllers"
                self._segment_path = lambda: "fabric" + "[id1='" + str(self.id1) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-fti-cfg:dci-fabric-interconnect/fabrics/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(DciFabricInterconnect.Fabrics.Fabric, ['id1', 'ssl'], name, value)


            class Controllers(Entity):
                """
                Enter Opflex peer info
                
                .. attribute:: controller
                
                	Enter Spine IP address
                	**type**\: list of  		 :py:class:`Controller <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_fti_cfg.DciFabricInterconnect.Fabrics.Fabric.Controllers.Controller>`
                
                

                """

                _prefix = 'infra-fti-cfg'
                _revision = '2017-11-13'

                def __init__(self):
                    super(DciFabricInterconnect.Fabrics.Fabric.Controllers, self).__init__()

                    self.yang_name = "controllers"
                    self.yang_parent_name = "fabric"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("controller", ("controller", DciFabricInterconnect.Fabrics.Fabric.Controllers.Controller))])
                    self._leafs = OrderedDict()

                    self.controller = YList(self)
                    self._segment_path = lambda: "controllers"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(DciFabricInterconnect.Fabrics.Fabric.Controllers, [], name, value)


                class Controller(Entity):
                    """
                    Enter Spine IP address
                    
                    .. attribute:: ip1  (key)
                    
                    	Enter Spine IP address
                    	**type**\: str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    

                    """

                    _prefix = 'infra-fti-cfg'
                    _revision = '2017-11-13'

                    def __init__(self):
                        super(DciFabricInterconnect.Fabrics.Fabric.Controllers.Controller, self).__init__()

                        self.yang_name = "controller"
                        self.yang_parent_name = "controllers"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['ip1']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('ip1', (YLeaf(YType.str, 'ip1'), ['str'])),
                        ])
                        self.ip1 = None
                        self._segment_path = lambda: "controller" + "[ip1='" + str(self.ip1) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(DciFabricInterconnect.Fabrics.Fabric.Controllers.Controller, ['ip1'], name, value)






    class Acp(Entity):
        """
        Configure Auto Config Pool parameters
        
        .. attribute:: bd_range
        
        	Specify BD pool range
        	**type**\:  :py:class:`BdRange <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_fti_cfg.DciFabricInterconnect.Acp.BdRange>`
        
        .. attribute:: vni_range
        
        	Specify VNI pool range
        	**type**\:  :py:class:`VniRange <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_fti_cfg.DciFabricInterconnect.Acp.VniRange>`
        
        .. attribute:: bvi_range
        
        	Specify BVI pool range
        	**type**\:  :py:class:`BviRange <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_fti_cfg.DciFabricInterconnect.Acp.BviRange>`
        
        .. attribute:: vrfs
        
        	Configure local VRF parameters
        	**type**\:  :py:class:`Vrfs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_fti_cfg.DciFabricInterconnect.Acp.Vrfs>`
        
        .. attribute:: nve_id
        
        	Specify NVE interface id
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: bgp_as
        
        	Specify BGP AS number
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: bg_name
        
        	Specify Bridge\-group name
        	**type**\: str
        
        

        """

        _prefix = 'infra-fti-cfg'
        _revision = '2017-11-13'

        def __init__(self):
            super(DciFabricInterconnect.Acp, self).__init__()

            self.yang_name = "acp"
            self.yang_parent_name = "dci-fabric-interconnect"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("bd-range", ("bd_range", DciFabricInterconnect.Acp.BdRange)), ("vni-range", ("vni_range", DciFabricInterconnect.Acp.VniRange)), ("bvi-range", ("bvi_range", DciFabricInterconnect.Acp.BviRange)), ("vrfs", ("vrfs", DciFabricInterconnect.Acp.Vrfs))])
            self._leafs = OrderedDict([
                ('nve_id', (YLeaf(YType.uint32, 'nve-id'), ['int'])),
                ('bgp_as', (YLeaf(YType.uint32, 'bgp-as'), ['int'])),
                ('bg_name', (YLeaf(YType.str, 'bg-name'), ['str'])),
            ])
            self.nve_id = None
            self.bgp_as = None
            self.bg_name = None

            self.bd_range = DciFabricInterconnect.Acp.BdRange()
            self.bd_range.parent = self
            self._children_name_map["bd_range"] = "bd-range"

            self.vni_range = DciFabricInterconnect.Acp.VniRange()
            self.vni_range.parent = self
            self._children_name_map["vni_range"] = "vni-range"

            self.bvi_range = DciFabricInterconnect.Acp.BviRange()
            self.bvi_range.parent = self
            self._children_name_map["bvi_range"] = "bvi-range"

            self.vrfs = DciFabricInterconnect.Acp.Vrfs()
            self.vrfs.parent = self
            self._children_name_map["vrfs"] = "vrfs"
            self._segment_path = lambda: "acp"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-fti-cfg:dci-fabric-interconnect/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(DciFabricInterconnect.Acp, ['nve_id', 'bgp_as', 'bg_name'], name, value)


        class BdRange(Entity):
            """
            Specify BD pool range
            
            .. attribute:: bd_min
            
            	BD Range\:min value
            	**type**\: int
            
            	**range:** 1..4000
            
            .. attribute:: bd_max
            
            	BD Range\:max value
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'infra-fti-cfg'
            _revision = '2017-11-13'

            def __init__(self):
                super(DciFabricInterconnect.Acp.BdRange, self).__init__()

                self.yang_name = "bd-range"
                self.yang_parent_name = "acp"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('bd_min', (YLeaf(YType.uint32, 'bd-min'), ['int'])),
                    ('bd_max', (YLeaf(YType.uint32, 'bd-max'), ['int'])),
                ])
                self.bd_min = None
                self.bd_max = None
                self._segment_path = lambda: "bd-range"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-fti-cfg:dci-fabric-interconnect/acp/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(DciFabricInterconnect.Acp.BdRange, ['bd_min', 'bd_max'], name, value)



        class VniRange(Entity):
            """
            Specify VNI pool range
            
            .. attribute:: vni_min
            
            	VNI Range\:min value
            	**type**\: int
            
            	**range:** 1..4000
            
            .. attribute:: vni_max
            
            	VNI Range\:max value
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'infra-fti-cfg'
            _revision = '2017-11-13'

            def __init__(self):
                super(DciFabricInterconnect.Acp.VniRange, self).__init__()

                self.yang_name = "vni-range"
                self.yang_parent_name = "acp"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('vni_min', (YLeaf(YType.uint32, 'vni-min'), ['int'])),
                    ('vni_max', (YLeaf(YType.uint32, 'vni-max'), ['int'])),
                ])
                self.vni_min = None
                self.vni_max = None
                self._segment_path = lambda: "vni-range"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-fti-cfg:dci-fabric-interconnect/acp/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(DciFabricInterconnect.Acp.VniRange, ['vni_min', 'vni_max'], name, value)



        class BviRange(Entity):
            """
            Specify BVI pool range
            
            .. attribute:: bvi_min
            
            	BVI Range\:min value
            	**type**\: int
            
            	**range:** 1..4000
            
            .. attribute:: bvi_max
            
            	BVI Range\:max value
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'infra-fti-cfg'
            _revision = '2017-11-13'

            def __init__(self):
                super(DciFabricInterconnect.Acp.BviRange, self).__init__()

                self.yang_name = "bvi-range"
                self.yang_parent_name = "acp"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('bvi_min', (YLeaf(YType.uint32, 'bvi-min'), ['int'])),
                    ('bvi_max', (YLeaf(YType.uint32, 'bvi-max'), ['int'])),
                ])
                self.bvi_min = None
                self.bvi_max = None
                self._segment_path = lambda: "bvi-range"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-fti-cfg:dci-fabric-interconnect/acp/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(DciFabricInterconnect.Acp.BviRange, ['bvi_min', 'bvi_max'], name, value)



        class Vrfs(Entity):
            """
            Configure local VRF parameters
            
            .. attribute:: vrf
            
            	vrf name
            	**type**\: list of  		 :py:class:`Vrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_fti_cfg.DciFabricInterconnect.Acp.Vrfs.Vrf>`
            
            

            """

            _prefix = 'infra-fti-cfg'
            _revision = '2017-11-13'

            def __init__(self):
                super(DciFabricInterconnect.Acp.Vrfs, self).__init__()

                self.yang_name = "vrfs"
                self.yang_parent_name = "acp"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("vrf", ("vrf", DciFabricInterconnect.Acp.Vrfs.Vrf))])
                self._leafs = OrderedDict()

                self.vrf = YList(self)
                self._segment_path = lambda: "vrfs"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-fti-cfg:dci-fabric-interconnect/acp/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(DciFabricInterconnect.Acp.Vrfs, [], name, value)


            class Vrf(Entity):
                """
                vrf name
                
                .. attribute:: vrf_name  (key)
                
                	vrf name
                	**type**\: str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: bvi_vrf_ip
                
                	BVI override IP address
                	**type**\: str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                

                """

                _prefix = 'infra-fti-cfg'
                _revision = '2017-11-13'

                def __init__(self):
                    super(DciFabricInterconnect.Acp.Vrfs.Vrf, self).__init__()

                    self.yang_name = "vrf"
                    self.yang_parent_name = "vrfs"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['vrf_name']
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('vrf_name', (YLeaf(YType.str, 'vrf-name'), ['str'])),
                        ('bvi_vrf_ip', (YLeaf(YType.str, 'bvi-vrf-ip'), ['str'])),
                    ])
                    self.vrf_name = None
                    self.bvi_vrf_ip = None
                    self._segment_path = lambda: "vrf" + "[vrf-name='" + str(self.vrf_name) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-infra-fti-cfg:dci-fabric-interconnect/acp/vrfs/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(DciFabricInterconnect.Acp.Vrfs.Vrf, ['vrf_name', 'bvi_vrf_ip'], name, value)




    def clone_ptr(self):
        self._top_entity = DciFabricInterconnect()
        return self._top_entity



