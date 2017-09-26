""" Cisco_IOS_XR_fia_hw_profile_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR fia\-hw\-profile package configuration.

This module contains definitions
for the following management objects\:
  hw\-module\-profile\-config\: none

Copyright (c) 2013\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class HwModuleProfileConfig(Entity):
    """
    none
    
    .. attribute:: fib_scale
    
    	Configure Fib for Scale for noTcam LC
    	**type**\:   :py:class:`FibScale <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_hw_profile_cfg.HwModuleProfileConfig.FibScale>`
    
    .. attribute:: profile
    
    	Configure profile
    	**type**\:   :py:class:`Profile <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_hw_profile_cfg.HwModuleProfileConfig.Profile>`
    
    .. attribute:: tcam
    
    	Configure Tcam
    	**type**\:   :py:class:`Tcam <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_hw_profile_cfg.HwModuleProfileConfig.Tcam>`
    
    

    """

    _prefix = 'fia-hw-profile-cfg'
    _revision = '2016-06-22'

    def __init__(self):
        super(HwModuleProfileConfig, self).__init__()
        self._top_entity = None

        self.yang_name = "hw-module-profile-config"
        self.yang_parent_name = "Cisco-IOS-XR-fia-hw-profile-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {"fib-scale" : ("fib_scale", HwModuleProfileConfig.FibScale), "profile" : ("profile", HwModuleProfileConfig.Profile), "tcam" : ("tcam", HwModuleProfileConfig.Tcam)}
        self._child_list_classes = {}

        self.fib_scale = HwModuleProfileConfig.FibScale()
        self.fib_scale.parent = self
        self._children_name_map["fib_scale"] = "fib-scale"
        self._children_yang_names.add("fib-scale")

        self.profile = HwModuleProfileConfig.Profile()
        self.profile.parent = self
        self._children_name_map["profile"] = "profile"
        self._children_yang_names.add("profile")

        self.tcam = HwModuleProfileConfig.Tcam()
        self.tcam.parent = self
        self._children_name_map["tcam"] = "tcam"
        self._children_yang_names.add("tcam")
        self._segment_path = lambda: "Cisco-IOS-XR-fia-hw-profile-cfg:hw-module-profile-config"


    class FibScale(Entity):
        """
        Configure Fib for Scale for noTcam LC.
        
        .. attribute:: ipv4_unicast_scale_no_tcam
        
        	IPv4 table for NOTCAM LC Scale
        	**type**\:   :py:class:`Ipv4UnicastScaleNoTcam <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_hw_profile_cfg.HwModuleProfileConfig.FibScale.Ipv4UnicastScaleNoTcam>`
        
        .. attribute:: ipv6_unicast_scale_no_tcam
        
        	IPv6 table for NOTCAM LC Scale
        	**type**\:   :py:class:`Ipv6UnicastScaleNoTcam <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_hw_profile_cfg.HwModuleProfileConfig.FibScale.Ipv6UnicastScaleNoTcam>`
        
        

        """

        _prefix = 'fia-hw-profile-cfg'
        _revision = '2016-06-22'

        def __init__(self):
            super(HwModuleProfileConfig.FibScale, self).__init__()

            self.yang_name = "fib-scale"
            self.yang_parent_name = "hw-module-profile-config"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {"ipv4-unicast-scale-no-tcam" : ("ipv4_unicast_scale_no_tcam", HwModuleProfileConfig.FibScale.Ipv4UnicastScaleNoTcam), "ipv6-unicast-scale-no-tcam" : ("ipv6_unicast_scale_no_tcam", HwModuleProfileConfig.FibScale.Ipv6UnicastScaleNoTcam)}
            self._child_list_classes = {}

            self.ipv4_unicast_scale_no_tcam = HwModuleProfileConfig.FibScale.Ipv4UnicastScaleNoTcam()
            self.ipv4_unicast_scale_no_tcam.parent = self
            self._children_name_map["ipv4_unicast_scale_no_tcam"] = "ipv4-unicast-scale-no-tcam"
            self._children_yang_names.add("ipv4-unicast-scale-no-tcam")

            self.ipv6_unicast_scale_no_tcam = HwModuleProfileConfig.FibScale.Ipv6UnicastScaleNoTcam()
            self.ipv6_unicast_scale_no_tcam.parent = self
            self._children_name_map["ipv6_unicast_scale_no_tcam"] = "ipv6-unicast-scale-no-tcam"
            self._children_yang_names.add("ipv6-unicast-scale-no-tcam")
            self._segment_path = lambda: "fib-scale"
            self._absolute_path = lambda: "Cisco-IOS-XR-fia-hw-profile-cfg:hw-module-profile-config/%s" % self._segment_path()


        class Ipv4UnicastScaleNoTcam(Entity):
            """
            IPv4 table for NOTCAM LC Scale.
            
            .. attribute:: scale_ipv4_no_tcam
            
            	Scale for IPv4 table for NoTCAM LC
            	**type**\:   :py:class:`ScaleIpv4NoTcam <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_hw_profile_cfg.HwModuleProfileConfig.FibScale.Ipv4UnicastScaleNoTcam.ScaleIpv4NoTcam>`
            
            

            """

            _prefix = 'fia-hw-profile-cfg'
            _revision = '2016-06-22'

            def __init__(self):
                super(HwModuleProfileConfig.FibScale.Ipv4UnicastScaleNoTcam, self).__init__()

                self.yang_name = "ipv4-unicast-scale-no-tcam"
                self.yang_parent_name = "fib-scale"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"scale-ipv4-no-tcam" : ("scale_ipv4_no_tcam", HwModuleProfileConfig.FibScale.Ipv4UnicastScaleNoTcam.ScaleIpv4NoTcam)}
                self._child_list_classes = {}

                self.scale_ipv4_no_tcam = HwModuleProfileConfig.FibScale.Ipv4UnicastScaleNoTcam.ScaleIpv4NoTcam()
                self.scale_ipv4_no_tcam.parent = self
                self._children_name_map["scale_ipv4_no_tcam"] = "scale-ipv4-no-tcam"
                self._children_yang_names.add("scale-ipv4-no-tcam")
                self._segment_path = lambda: "ipv4-unicast-scale-no-tcam"
                self._absolute_path = lambda: "Cisco-IOS-XR-fia-hw-profile-cfg:hw-module-profile-config/fib-scale/%s" % self._segment_path()


            class ScaleIpv4NoTcam(Entity):
                """
                Scale for IPv4 table for NoTCAM LC.
                
                .. attribute:: host_optimized_ipv4_no_tcam
                
                	Host\-optimized Scale for IPv4 table for NoTCAM LC
                	**type**\:  str
                
                .. attribute:: internet_optimized_ipv4_no_tcam
                
                	Internet\-optimized Scale for IPv4 table for NoTCAM LC
                	**type**\:  str
                
                

                """

                _prefix = 'fia-hw-profile-cfg'
                _revision = '2016-06-22'

                def __init__(self):
                    super(HwModuleProfileConfig.FibScale.Ipv4UnicastScaleNoTcam.ScaleIpv4NoTcam, self).__init__()

                    self.yang_name = "scale-ipv4-no-tcam"
                    self.yang_parent_name = "ipv4-unicast-scale-no-tcam"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.host_optimized_ipv4_no_tcam = YLeaf(YType.str, "host-optimized-ipv4-no-tcam")

                    self.internet_optimized_ipv4_no_tcam = YLeaf(YType.str, "internet-optimized-ipv4-no-tcam")
                    self._segment_path = lambda: "scale-ipv4-no-tcam"
                    self._absolute_path = lambda: "Cisco-IOS-XR-fia-hw-profile-cfg:hw-module-profile-config/fib-scale/ipv4-unicast-scale-no-tcam/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(HwModuleProfileConfig.FibScale.Ipv4UnicastScaleNoTcam.ScaleIpv4NoTcam, ['host_optimized_ipv4_no_tcam', 'internet_optimized_ipv4_no_tcam'], name, value)


        class Ipv6UnicastScaleNoTcam(Entity):
            """
            IPv6 table for NOTCAM LC Scale.
            
            .. attribute:: scale_ipv6_no_tcam
            
            	Scale for IPv6 table for NoTCAM LC
            	**type**\:   :py:class:`ScaleIpv6NoTcam <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_hw_profile_cfg.HwModuleProfileConfig.FibScale.Ipv6UnicastScaleNoTcam.ScaleIpv6NoTcam>`
            
            

            """

            _prefix = 'fia-hw-profile-cfg'
            _revision = '2016-06-22'

            def __init__(self):
                super(HwModuleProfileConfig.FibScale.Ipv6UnicastScaleNoTcam, self).__init__()

                self.yang_name = "ipv6-unicast-scale-no-tcam"
                self.yang_parent_name = "fib-scale"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"scale-ipv6-no-tcam" : ("scale_ipv6_no_tcam", HwModuleProfileConfig.FibScale.Ipv6UnicastScaleNoTcam.ScaleIpv6NoTcam)}
                self._child_list_classes = {}

                self.scale_ipv6_no_tcam = HwModuleProfileConfig.FibScale.Ipv6UnicastScaleNoTcam.ScaleIpv6NoTcam()
                self.scale_ipv6_no_tcam.parent = self
                self._children_name_map["scale_ipv6_no_tcam"] = "scale-ipv6-no-tcam"
                self._children_yang_names.add("scale-ipv6-no-tcam")
                self._segment_path = lambda: "ipv6-unicast-scale-no-tcam"
                self._absolute_path = lambda: "Cisco-IOS-XR-fia-hw-profile-cfg:hw-module-profile-config/fib-scale/%s" % self._segment_path()


            class ScaleIpv6NoTcam(Entity):
                """
                Scale for IPv6 table for NoTCAM LC.
                
                .. attribute:: internet_optimized_ipv6_no_tcam
                
                	Internet\-optimized Scale for IPv6 table for NoTCAM LC
                	**type**\:  str
                
                

                """

                _prefix = 'fia-hw-profile-cfg'
                _revision = '2016-06-22'

                def __init__(self):
                    super(HwModuleProfileConfig.FibScale.Ipv6UnicastScaleNoTcam.ScaleIpv6NoTcam, self).__init__()

                    self.yang_name = "scale-ipv6-no-tcam"
                    self.yang_parent_name = "ipv6-unicast-scale-no-tcam"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.internet_optimized_ipv6_no_tcam = YLeaf(YType.str, "internet-optimized-ipv6-no-tcam")
                    self._segment_path = lambda: "scale-ipv6-no-tcam"
                    self._absolute_path = lambda: "Cisco-IOS-XR-fia-hw-profile-cfg:hw-module-profile-config/fib-scale/ipv6-unicast-scale-no-tcam/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(HwModuleProfileConfig.FibScale.Ipv6UnicastScaleNoTcam.ScaleIpv6NoTcam, ['internet_optimized_ipv6_no_tcam'], name, value)


    class Profile(Entity):
        """
        Configure profile.
        
        .. attribute:: qos
        
        	Configure profile
        	**type**\:   :py:class:`Qos <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_hw_profile_cfg.HwModuleProfileConfig.Profile.Qos>`
        
        .. attribute:: stats
        
        	Configure stats
        	**type**\:   :py:class:`Stats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_hw_profile_cfg.HwModuleProfileConfig.Profile.Stats>`
        
        .. attribute:: tcam_table
        
        	Configure profile for TCAM LC cards
        	**type**\:   :py:class:`TcamTable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_hw_profile_cfg.HwModuleProfileConfig.Profile.TcamTable>`
        
        

        """

        _prefix = 'fia-hw-profile-cfg'
        _revision = '2016-06-22'

        def __init__(self):
            super(HwModuleProfileConfig.Profile, self).__init__()

            self.yang_name = "profile"
            self.yang_parent_name = "hw-module-profile-config"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {"qos" : ("qos", HwModuleProfileConfig.Profile.Qos), "stats" : ("stats", HwModuleProfileConfig.Profile.Stats), "tcam-table" : ("tcam_table", HwModuleProfileConfig.Profile.TcamTable)}
            self._child_list_classes = {}

            self.qos = HwModuleProfileConfig.Profile.Qos()
            self.qos.parent = self
            self._children_name_map["qos"] = "qos"
            self._children_yang_names.add("qos")

            self.stats = HwModuleProfileConfig.Profile.Stats()
            self.stats.parent = self
            self._children_name_map["stats"] = "stats"
            self._children_yang_names.add("stats")

            self.tcam_table = HwModuleProfileConfig.Profile.TcamTable()
            self.tcam_table.parent = self
            self._children_name_map["tcam_table"] = "tcam-table"
            self._children_yang_names.add("tcam-table")
            self._segment_path = lambda: "profile"
            self._absolute_path = lambda: "Cisco-IOS-XR-fia-hw-profile-cfg:hw-module-profile-config/%s" % self._segment_path()


        class Qos(Entity):
            """
            Configure profile.
            
            .. attribute:: class_maps
            
            	Configure Class Map Root
            	**type**\:   :py:class:`ClassMaps <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_hw_profile_cfg.HwModuleProfileConfig.Profile.Qos.ClassMaps>`
            
            .. attribute:: class_maps_root_def
            
            	Configure Class Maps Default
            	**type**\:   :py:class:`ClassMapsRootDef <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_hw_profile_cfg.HwModuleProfileConfig.Profile.Qos.ClassMapsRootDef>`
            
            .. attribute:: hqos_enable_all
            
            	Configure Hqos profile
            	**type**\:   :py:class:`HqosEnableAll <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_hw_profile_cfg.HwModuleProfileConfig.Profile.Qos.HqosEnableAll>`
            
            .. attribute:: ingress_model_root_def
            
            	Configure Ingress Model Default
            	**type**\:   :py:class:`IngressModelRootDef <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_hw_profile_cfg.HwModuleProfileConfig.Profile.Qos.IngressModelRootDef>`
            
            .. attribute:: ingress_models
            
            	Configure Ingress Model Root
            	**type**\:   :py:class:`IngressModels <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_hw_profile_cfg.HwModuleProfileConfig.Profile.Qos.IngressModels>`
            
            .. attribute:: trunks
            
            	Configure Max Trunk Size
            	**type**\:   :py:class:`Trunks <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_hw_profile_cfg.HwModuleProfileConfig.Profile.Qos.Trunks>`
            
            

            """

            _prefix = 'fia-hw-profile-cfg'
            _revision = '2016-06-22'

            def __init__(self):
                super(HwModuleProfileConfig.Profile.Qos, self).__init__()

                self.yang_name = "qos"
                self.yang_parent_name = "profile"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"class-maps" : ("class_maps", HwModuleProfileConfig.Profile.Qos.ClassMaps), "class-maps-root-def" : ("class_maps_root_def", HwModuleProfileConfig.Profile.Qos.ClassMapsRootDef), "hqos-enable-all" : ("hqos_enable_all", HwModuleProfileConfig.Profile.Qos.HqosEnableAll), "ingress-model-root-def" : ("ingress_model_root_def", HwModuleProfileConfig.Profile.Qos.IngressModelRootDef), "ingress-models" : ("ingress_models", HwModuleProfileConfig.Profile.Qos.IngressModels), "trunks" : ("trunks", HwModuleProfileConfig.Profile.Qos.Trunks)}
                self._child_list_classes = {}

                self.class_maps = HwModuleProfileConfig.Profile.Qos.ClassMaps()
                self.class_maps.parent = self
                self._children_name_map["class_maps"] = "class-maps"
                self._children_yang_names.add("class-maps")

                self.class_maps_root_def = HwModuleProfileConfig.Profile.Qos.ClassMapsRootDef()
                self.class_maps_root_def.parent = self
                self._children_name_map["class_maps_root_def"] = "class-maps-root-def"
                self._children_yang_names.add("class-maps-root-def")

                self.hqos_enable_all = HwModuleProfileConfig.Profile.Qos.HqosEnableAll()
                self.hqos_enable_all.parent = self
                self._children_name_map["hqos_enable_all"] = "hqos-enable-all"
                self._children_yang_names.add("hqos-enable-all")

                self.ingress_model_root_def = HwModuleProfileConfig.Profile.Qos.IngressModelRootDef()
                self.ingress_model_root_def.parent = self
                self._children_name_map["ingress_model_root_def"] = "ingress-model-root-def"
                self._children_yang_names.add("ingress-model-root-def")

                self.ingress_models = HwModuleProfileConfig.Profile.Qos.IngressModels()
                self.ingress_models.parent = self
                self._children_name_map["ingress_models"] = "ingress-models"
                self._children_yang_names.add("ingress-models")

                self.trunks = HwModuleProfileConfig.Profile.Qos.Trunks()
                self.trunks.parent = self
                self._children_name_map["trunks"] = "trunks"
                self._children_yang_names.add("trunks")
                self._segment_path = lambda: "qos"
                self._absolute_path = lambda: "Cisco-IOS-XR-fia-hw-profile-cfg:hw-module-profile-config/profile/%s" % self._segment_path()


            class ClassMaps(Entity):
                """
                Configure Class Map Root
                
                .. attribute:: class_map
                
                	Configure Class Maps
                	**type**\: list of    :py:class:`ClassMap <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_hw_profile_cfg.HwModuleProfileConfig.Profile.Qos.ClassMaps.ClassMap>`
                
                

                """

                _prefix = 'fia-hw-profile-cfg'
                _revision = '2016-06-22'

                def __init__(self):
                    super(HwModuleProfileConfig.Profile.Qos.ClassMaps, self).__init__()

                    self.yang_name = "class-maps"
                    self.yang_parent_name = "qos"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {"class-map" : ("class_map", HwModuleProfileConfig.Profile.Qos.ClassMaps.ClassMap)}

                    self.class_map = YList(self)
                    self._segment_path = lambda: "class-maps"
                    self._absolute_path = lambda: "Cisco-IOS-XR-fia-hw-profile-cfg:hw-module-profile-config/profile/qos/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(HwModuleProfileConfig.Profile.Qos.ClassMaps, [], name, value)


                class ClassMap(Entity):
                    """
                    Configure Class Maps
                    
                    .. attribute:: node_name  <key>
                    
                    	NodeName
                    	**type**\:  str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: class_map_size
                    
                    	Class Map Size
                    	**type**\: list of    :py:class:`ClassMapSize <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_hw_profile_cfg.HwModuleProfileConfig.Profile.Qos.ClassMaps.ClassMap.ClassMapSize>`
                    
                    

                    """

                    _prefix = 'fia-hw-profile-cfg'
                    _revision = '2016-06-22'

                    def __init__(self):
                        super(HwModuleProfileConfig.Profile.Qos.ClassMaps.ClassMap, self).__init__()

                        self.yang_name = "class-map"
                        self.yang_parent_name = "class-maps"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self._child_container_classes = {}
                        self._child_list_classes = {"class-map-size" : ("class_map_size", HwModuleProfileConfig.Profile.Qos.ClassMaps.ClassMap.ClassMapSize)}

                        self.node_name = YLeaf(YType.str, "node-name")

                        self.class_map_size = YList(self)
                        self._segment_path = lambda: "class-map" + "[node-name='" + self.node_name.get() + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-fia-hw-profile-cfg:hw-module-profile-config/profile/qos/class-maps/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(HwModuleProfileConfig.Profile.Qos.ClassMaps.ClassMap, ['node_name'], name, value)


                    class ClassMapSize(Entity):
                        """
                        Class Map Size
                        
                        .. attribute:: location  <key>
                        
                        	Location
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: class_map_size
                        
                        	ClassMapSize
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        	**mandatory**\: True
                        
                        

                        """

                        _prefix = 'fia-hw-profile-cfg'
                        _revision = '2016-06-22'

                        def __init__(self):
                            super(HwModuleProfileConfig.Profile.Qos.ClassMaps.ClassMap.ClassMapSize, self).__init__()

                            self.yang_name = "class-map-size"
                            self.yang_parent_name = "class-map"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.location = YLeaf(YType.int32, "location")

                            self.class_map_size = YLeaf(YType.int32, "class-map-size")
                            self._segment_path = lambda: "class-map-size" + "[location='" + self.location.get() + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(HwModuleProfileConfig.Profile.Qos.ClassMaps.ClassMap.ClassMapSize, ['location', 'class_map_size'], name, value)


            class ClassMapsRootDef(Entity):
                """
                Configure Class Maps Default
                
                .. attribute:: class_map_size_def
                
                	Class Map Size Default
                	**type**\:  int
                
                	**range:** \-2147483648..2147483647
                
                

                """

                _prefix = 'fia-hw-profile-cfg'
                _revision = '2016-06-22'

                def __init__(self):
                    super(HwModuleProfileConfig.Profile.Qos.ClassMapsRootDef, self).__init__()

                    self.yang_name = "class-maps-root-def"
                    self.yang_parent_name = "qos"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.class_map_size_def = YLeaf(YType.int32, "class-map-size-def")
                    self._segment_path = lambda: "class-maps-root-def"
                    self._absolute_path = lambda: "Cisco-IOS-XR-fia-hw-profile-cfg:hw-module-profile-config/profile/qos/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(HwModuleProfileConfig.Profile.Qos.ClassMapsRootDef, ['class_map_size_def'], name, value)


            class HqosEnableAll(Entity):
                """
                Configure Hqos profile
                
                .. attribute:: hqos_enable
                
                	 Hqos profile value
                	**type**\:  int
                
                	**range:** \-2147483648..2147483647
                
                

                """

                _prefix = 'fia-hw-profile-cfg'
                _revision = '2016-06-22'

                def __init__(self):
                    super(HwModuleProfileConfig.Profile.Qos.HqosEnableAll, self).__init__()

                    self.yang_name = "hqos-enable-all"
                    self.yang_parent_name = "qos"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.hqos_enable = YLeaf(YType.int32, "hqos-enable")
                    self._segment_path = lambda: "hqos-enable-all"
                    self._absolute_path = lambda: "Cisco-IOS-XR-fia-hw-profile-cfg:hw-module-profile-config/profile/qos/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(HwModuleProfileConfig.Profile.Qos.HqosEnableAll, ['hqos_enable'], name, value)


            class IngressModelRootDef(Entity):
                """
                Configure Ingress Model Default
                
                .. attribute:: ingress_model_leaf_def
                
                	Ingress Model Default
                	**type**\:  int
                
                	**range:** \-2147483648..2147483647
                
                

                """

                _prefix = 'fia-hw-profile-cfg'
                _revision = '2016-06-22'

                def __init__(self):
                    super(HwModuleProfileConfig.Profile.Qos.IngressModelRootDef, self).__init__()

                    self.yang_name = "ingress-model-root-def"
                    self.yang_parent_name = "qos"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.ingress_model_leaf_def = YLeaf(YType.int32, "ingress-model-leaf-def")
                    self._segment_path = lambda: "ingress-model-root-def"
                    self._absolute_path = lambda: "Cisco-IOS-XR-fia-hw-profile-cfg:hw-module-profile-config/profile/qos/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(HwModuleProfileConfig.Profile.Qos.IngressModelRootDef, ['ingress_model_leaf_def'], name, value)


            class IngressModels(Entity):
                """
                Configure Ingress Model Root
                
                .. attribute:: ingress_model
                
                	Configure Ingress Model
                	**type**\: list of    :py:class:`IngressModel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_hw_profile_cfg.HwModuleProfileConfig.Profile.Qos.IngressModels.IngressModel>`
                
                

                """

                _prefix = 'fia-hw-profile-cfg'
                _revision = '2016-06-22'

                def __init__(self):
                    super(HwModuleProfileConfig.Profile.Qos.IngressModels, self).__init__()

                    self.yang_name = "ingress-models"
                    self.yang_parent_name = "qos"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {"ingress-model" : ("ingress_model", HwModuleProfileConfig.Profile.Qos.IngressModels.IngressModel)}

                    self.ingress_model = YList(self)
                    self._segment_path = lambda: "ingress-models"
                    self._absolute_path = lambda: "Cisco-IOS-XR-fia-hw-profile-cfg:hw-module-profile-config/profile/qos/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(HwModuleProfileConfig.Profile.Qos.IngressModels, [], name, value)


                class IngressModel(Entity):
                    """
                    Configure Ingress Model
                    
                    .. attribute:: node_name  <key>
                    
                    	NodeName
                    	**type**\:  str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: ingress_model_leaf
                    
                    	Configure Ingress Model Leaf
                    	**type**\: list of    :py:class:`IngressModelLeaf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_hw_profile_cfg.HwModuleProfileConfig.Profile.Qos.IngressModels.IngressModel.IngressModelLeaf>`
                    
                    

                    """

                    _prefix = 'fia-hw-profile-cfg'
                    _revision = '2016-06-22'

                    def __init__(self):
                        super(HwModuleProfileConfig.Profile.Qos.IngressModels.IngressModel, self).__init__()

                        self.yang_name = "ingress-model"
                        self.yang_parent_name = "ingress-models"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self._child_container_classes = {}
                        self._child_list_classes = {"ingress-model-leaf" : ("ingress_model_leaf", HwModuleProfileConfig.Profile.Qos.IngressModels.IngressModel.IngressModelLeaf)}

                        self.node_name = YLeaf(YType.str, "node-name")

                        self.ingress_model_leaf = YList(self)
                        self._segment_path = lambda: "ingress-model" + "[node-name='" + self.node_name.get() + "']"
                        self._absolute_path = lambda: "Cisco-IOS-XR-fia-hw-profile-cfg:hw-module-profile-config/profile/qos/ingress-models/%s" % self._segment_path()

                    def __setattr__(self, name, value):
                        self._perform_setattr(HwModuleProfileConfig.Profile.Qos.IngressModels.IngressModel, ['node_name'], name, value)


                    class IngressModelLeaf(Entity):
                        """
                        Configure Ingress Model Leaf
                        
                        .. attribute:: location  <key>
                        
                        	Location
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: ingress_model_leaf
                        
                        	IngressModelLeaf
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        	**mandatory**\: True
                        
                        

                        """

                        _prefix = 'fia-hw-profile-cfg'
                        _revision = '2016-06-22'

                        def __init__(self):
                            super(HwModuleProfileConfig.Profile.Qos.IngressModels.IngressModel.IngressModelLeaf, self).__init__()

                            self.yang_name = "ingress-model-leaf"
                            self.yang_parent_name = "ingress-model"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.location = YLeaf(YType.int32, "location")

                            self.ingress_model_leaf = YLeaf(YType.int32, "ingress-model-leaf")
                            self._segment_path = lambda: "ingress-model-leaf" + "[location='" + self.location.get() + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(HwModuleProfileConfig.Profile.Qos.IngressModels.IngressModel.IngressModelLeaf, ['location', 'ingress_model_leaf'], name, value)


            class Trunks(Entity):
                """
                Configure Max Trunk Size
                
                .. attribute:: trunk_size
                
                	Max Trunk Size
                	**type**\:  int
                
                	**range:** \-2147483648..2147483647
                
                

                """

                _prefix = 'fia-hw-profile-cfg'
                _revision = '2016-06-22'

                def __init__(self):
                    super(HwModuleProfileConfig.Profile.Qos.Trunks, self).__init__()

                    self.yang_name = "trunks"
                    self.yang_parent_name = "qos"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.trunk_size = YLeaf(YType.int32, "trunk-size")
                    self._segment_path = lambda: "trunks"
                    self._absolute_path = lambda: "Cisco-IOS-XR-fia-hw-profile-cfg:hw-module-profile-config/profile/qos/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(HwModuleProfileConfig.Profile.Qos.Trunks, ['trunk_size'], name, value)


        class Stats(Entity):
            """
            Configure stats
            
            .. attribute:: counter_profile
            
            	Configure stats for qos\-enhanced and acl\-permit
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            

            """

            _prefix = 'fia-hw-profile-cfg'
            _revision = '2016-06-22'

            def __init__(self):
                super(HwModuleProfileConfig.Profile.Stats, self).__init__()

                self.yang_name = "stats"
                self.yang_parent_name = "profile"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.counter_profile = YLeaf(YType.int32, "counter-profile")
                self._segment_path = lambda: "stats"
                self._absolute_path = lambda: "Cisco-IOS-XR-fia-hw-profile-cfg:hw-module-profile-config/profile/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(HwModuleProfileConfig.Profile.Stats, ['counter_profile'], name, value)


        class TcamTable(Entity):
            """
            Configure profile for TCAM LC cards
            
            .. attribute:: fib_table
            
            	FIB table for TCAM LC cards
            	**type**\:   :py:class:`FibTable <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_hw_profile_cfg.HwModuleProfileConfig.Profile.TcamTable.FibTable>`
            
            

            """

            _prefix = 'fia-hw-profile-cfg'
            _revision = '2016-06-22'

            def __init__(self):
                super(HwModuleProfileConfig.Profile.TcamTable, self).__init__()

                self.yang_name = "tcam-table"
                self.yang_parent_name = "profile"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"fib-table" : ("fib_table", HwModuleProfileConfig.Profile.TcamTable.FibTable)}
                self._child_list_classes = {}

                self.fib_table = HwModuleProfileConfig.Profile.TcamTable.FibTable()
                self.fib_table.parent = self
                self._children_name_map["fib_table"] = "fib-table"
                self._children_yang_names.add("fib-table")
                self._segment_path = lambda: "tcam-table"
                self._absolute_path = lambda: "Cisco-IOS-XR-fia-hw-profile-cfg:hw-module-profile-config/profile/%s" % self._segment_path()


            class FibTable(Entity):
                """
                FIB table for TCAM LC cards
                
                .. attribute:: ipv4_address
                
                	IPv4 table for TCAM LC cards
                	**type**\:   :py:class:`Ipv4Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_hw_profile_cfg.HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv4Address>`
                
                .. attribute:: ipv6_address
                
                	IPv6 table for TCAM LC cards
                	**type**\:   :py:class:`Ipv6Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_hw_profile_cfg.HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv6Address>`
                
                

                """

                _prefix = 'fia-hw-profile-cfg'
                _revision = '2016-06-22'

                def __init__(self):
                    super(HwModuleProfileConfig.Profile.TcamTable.FibTable, self).__init__()

                    self.yang_name = "fib-table"
                    self.yang_parent_name = "tcam-table"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {"ipv4-address" : ("ipv4_address", HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv4Address), "ipv6-address" : ("ipv6_address", HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv6Address)}
                    self._child_list_classes = {}

                    self.ipv4_address = HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv4Address()
                    self.ipv4_address.parent = self
                    self._children_name_map["ipv4_address"] = "ipv4-address"
                    self._children_yang_names.add("ipv4-address")

                    self.ipv6_address = HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv6Address()
                    self.ipv6_address.parent = self
                    self._children_name_map["ipv6_address"] = "ipv6-address"
                    self._children_yang_names.add("ipv6-address")
                    self._segment_path = lambda: "fib-table"
                    self._absolute_path = lambda: "Cisco-IOS-XR-fia-hw-profile-cfg:hw-module-profile-config/profile/tcam-table/%s" % self._segment_path()


                class Ipv4Address(Entity):
                    """
                    IPv4 table for TCAM LC cards
                    
                    .. attribute:: ipv4_unicast
                    
                    	Unicast table for TCAM LC cards
                    	**type**\:   :py:class:`Ipv4Unicast <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_hw_profile_cfg.HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv4Address.Ipv4Unicast>`
                    
                    

                    """

                    _prefix = 'fia-hw-profile-cfg'
                    _revision = '2016-06-22'

                    def __init__(self):
                        super(HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv4Address, self).__init__()

                        self.yang_name = "ipv4-address"
                        self.yang_parent_name = "fib-table"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self._child_container_classes = {"ipv4-unicast" : ("ipv4_unicast", HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv4Address.Ipv4Unicast)}
                        self._child_list_classes = {}

                        self.ipv4_unicast = HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv4Address.Ipv4Unicast()
                        self.ipv4_unicast.parent = self
                        self._children_name_map["ipv4_unicast"] = "ipv4-unicast"
                        self._children_yang_names.add("ipv4-unicast")
                        self._segment_path = lambda: "ipv4-address"
                        self._absolute_path = lambda: "Cisco-IOS-XR-fia-hw-profile-cfg:hw-module-profile-config/profile/tcam-table/fib-table/%s" % self._segment_path()


                    class Ipv4Unicast(Entity):
                        """
                        Unicast table for TCAM LC cards
                        
                        .. attribute:: ipv4_unicast_percent
                        
                        	curve out percentage of TCAM table entries
                        	**type**\:  int
                        
                        	**range:** 0..100
                        
                        	**units**\: percentage
                        
                        .. attribute:: ipv4_unicast_prefix_lengths
                        
                        	IPv4 Unicast prefix 
                        	**type**\:   :py:class:`Ipv4UnicastPrefixLengths <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_hw_profile_cfg.HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv4Address.Ipv4Unicast.Ipv4UnicastPrefixLengths>`
                        
                        

                        """

                        _prefix = 'fia-hw-profile-cfg'
                        _revision = '2016-06-22'

                        def __init__(self):
                            super(HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv4Address.Ipv4Unicast, self).__init__()

                            self.yang_name = "ipv4-unicast"
                            self.yang_parent_name = "ipv4-address"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self._child_container_classes = {"ipv4-unicast-prefix-lengths" : ("ipv4_unicast_prefix_lengths", HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv4Address.Ipv4Unicast.Ipv4UnicastPrefixLengths)}
                            self._child_list_classes = {}

                            self.ipv4_unicast_percent = YLeaf(YType.uint32, "ipv4-unicast-percent")

                            self.ipv4_unicast_prefix_lengths = HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv4Address.Ipv4Unicast.Ipv4UnicastPrefixLengths()
                            self.ipv4_unicast_prefix_lengths.parent = self
                            self._children_name_map["ipv4_unicast_prefix_lengths"] = "ipv4-unicast-prefix-lengths"
                            self._children_yang_names.add("ipv4-unicast-prefix-lengths")
                            self._segment_path = lambda: "ipv4-unicast"
                            self._absolute_path = lambda: "Cisco-IOS-XR-fia-hw-profile-cfg:hw-module-profile-config/profile/tcam-table/fib-table/ipv4-address/%s" % self._segment_path()

                        def __setattr__(self, name, value):
                            self._perform_setattr(HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv4Address.Ipv4Unicast, ['ipv4_unicast_percent'], name, value)


                        class Ipv4UnicastPrefixLengths(Entity):
                            """
                            IPv4 Unicast prefix 
                            
                            .. attribute:: ipv4_unicast_prefix_length
                            
                            	IPv4 Unicast prefix length
                            	**type**\: list of    :py:class:`Ipv4UnicastPrefixLength <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_hw_profile_cfg.HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv4Address.Ipv4Unicast.Ipv4UnicastPrefixLengths.Ipv4UnicastPrefixLength>`
                            
                            

                            """

                            _prefix = 'fia-hw-profile-cfg'
                            _revision = '2016-06-22'

                            def __init__(self):
                                super(HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv4Address.Ipv4Unicast.Ipv4UnicastPrefixLengths, self).__init__()

                                self.yang_name = "ipv4-unicast-prefix-lengths"
                                self.yang_parent_name = "ipv4-unicast"
                                self.is_top_level_class = False
                                self.has_list_ancestor = False
                                self._child_container_classes = {}
                                self._child_list_classes = {"ipv4-unicast-prefix-length" : ("ipv4_unicast_prefix_length", HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv4Address.Ipv4Unicast.Ipv4UnicastPrefixLengths.Ipv4UnicastPrefixLength)}

                                self.ipv4_unicast_prefix_length = YList(self)
                                self._segment_path = lambda: "ipv4-unicast-prefix-lengths"
                                self._absolute_path = lambda: "Cisco-IOS-XR-fia-hw-profile-cfg:hw-module-profile-config/profile/tcam-table/fib-table/ipv4-address/ipv4-unicast/%s" % self._segment_path()

                            def __setattr__(self, name, value):
                                self._perform_setattr(HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv4Address.Ipv4Unicast.Ipv4UnicastPrefixLengths, [], name, value)


                            class Ipv4UnicastPrefixLength(Entity):
                                """
                                IPv4 Unicast prefix length
                                
                                .. attribute:: prefix_length  <key>
                                
                                	prefix length
                                	**type**\:  int
                                
                                	**range:** 0..32
                                
                                .. attribute:: ipv4_unicast_prefix_percent
                                
                                	curve out percentage of TCAM table entries
                                	**type**\:  str
                                
                                	**units**\: percentage
                                
                                

                                """

                                _prefix = 'fia-hw-profile-cfg'
                                _revision = '2016-06-22'

                                def __init__(self):
                                    super(HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv4Address.Ipv4Unicast.Ipv4UnicastPrefixLengths.Ipv4UnicastPrefixLength, self).__init__()

                                    self.yang_name = "ipv4-unicast-prefix-length"
                                    self.yang_parent_name = "ipv4-unicast-prefix-lengths"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = False
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.prefix_length = YLeaf(YType.uint32, "prefix-length")

                                    self.ipv4_unicast_prefix_percent = YLeaf(YType.str, "ipv4-unicast-prefix-percent")
                                    self._segment_path = lambda: "ipv4-unicast-prefix-length" + "[prefix-length='" + self.prefix_length.get() + "']"
                                    self._absolute_path = lambda: "Cisco-IOS-XR-fia-hw-profile-cfg:hw-module-profile-config/profile/tcam-table/fib-table/ipv4-address/ipv4-unicast/ipv4-unicast-prefix-lengths/%s" % self._segment_path()

                                def __setattr__(self, name, value):
                                    self._perform_setattr(HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv4Address.Ipv4Unicast.Ipv4UnicastPrefixLengths.Ipv4UnicastPrefixLength, ['prefix_length', 'ipv4_unicast_prefix_percent'], name, value)


                class Ipv6Address(Entity):
                    """
                    IPv6 table for TCAM LC cards
                    
                    .. attribute:: ipv6_unicast
                    
                    	Unicast table for TCAM LC cards
                    	**type**\:   :py:class:`Ipv6Unicast <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_hw_profile_cfg.HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv6Address.Ipv6Unicast>`
                    
                    

                    """

                    _prefix = 'fia-hw-profile-cfg'
                    _revision = '2016-06-22'

                    def __init__(self):
                        super(HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv6Address, self).__init__()

                        self.yang_name = "ipv6-address"
                        self.yang_parent_name = "fib-table"
                        self.is_top_level_class = False
                        self.has_list_ancestor = False
                        self._child_container_classes = {"ipv6-unicast" : ("ipv6_unicast", HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv6Address.Ipv6Unicast)}
                        self._child_list_classes = {}

                        self.ipv6_unicast = HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv6Address.Ipv6Unicast()
                        self.ipv6_unicast.parent = self
                        self._children_name_map["ipv6_unicast"] = "ipv6-unicast"
                        self._children_yang_names.add("ipv6-unicast")
                        self._segment_path = lambda: "ipv6-address"
                        self._absolute_path = lambda: "Cisco-IOS-XR-fia-hw-profile-cfg:hw-module-profile-config/profile/tcam-table/fib-table/%s" % self._segment_path()


                    class Ipv6Unicast(Entity):
                        """
                        Unicast table for TCAM LC cards
                        
                        .. attribute:: ipv6_unicast_percent
                        
                        	curve out percentage of TCAM table entries
                        	**type**\:  int
                        
                        	**range:** 0..100
                        
                        	**units**\: percentage
                        
                        .. attribute:: ipv6_unicast_prefix_lengths
                        
                        	IPv6 Unicast prefix 
                        	**type**\:   :py:class:`Ipv6UnicastPrefixLengths <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_hw_profile_cfg.HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv6Address.Ipv6Unicast.Ipv6UnicastPrefixLengths>`
                        
                        

                        """

                        _prefix = 'fia-hw-profile-cfg'
                        _revision = '2016-06-22'

                        def __init__(self):
                            super(HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv6Address.Ipv6Unicast, self).__init__()

                            self.yang_name = "ipv6-unicast"
                            self.yang_parent_name = "ipv6-address"
                            self.is_top_level_class = False
                            self.has_list_ancestor = False
                            self._child_container_classes = {"ipv6-unicast-prefix-lengths" : ("ipv6_unicast_prefix_lengths", HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv6Address.Ipv6Unicast.Ipv6UnicastPrefixLengths)}
                            self._child_list_classes = {}

                            self.ipv6_unicast_percent = YLeaf(YType.uint32, "ipv6-unicast-percent")

                            self.ipv6_unicast_prefix_lengths = HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv6Address.Ipv6Unicast.Ipv6UnicastPrefixLengths()
                            self.ipv6_unicast_prefix_lengths.parent = self
                            self._children_name_map["ipv6_unicast_prefix_lengths"] = "ipv6-unicast-prefix-lengths"
                            self._children_yang_names.add("ipv6-unicast-prefix-lengths")
                            self._segment_path = lambda: "ipv6-unicast"
                            self._absolute_path = lambda: "Cisco-IOS-XR-fia-hw-profile-cfg:hw-module-profile-config/profile/tcam-table/fib-table/ipv6-address/%s" % self._segment_path()

                        def __setattr__(self, name, value):
                            self._perform_setattr(HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv6Address.Ipv6Unicast, ['ipv6_unicast_percent'], name, value)


                        class Ipv6UnicastPrefixLengths(Entity):
                            """
                            IPv6 Unicast prefix 
                            
                            .. attribute:: ipv6_unicast_prefix_length
                            
                            	IPv6 Unicast prefix length
                            	**type**\: list of    :py:class:`Ipv6UnicastPrefixLength <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_hw_profile_cfg.HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv6Address.Ipv6Unicast.Ipv6UnicastPrefixLengths.Ipv6UnicastPrefixLength>`
                            
                            

                            """

                            _prefix = 'fia-hw-profile-cfg'
                            _revision = '2016-06-22'

                            def __init__(self):
                                super(HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv6Address.Ipv6Unicast.Ipv6UnicastPrefixLengths, self).__init__()

                                self.yang_name = "ipv6-unicast-prefix-lengths"
                                self.yang_parent_name = "ipv6-unicast"
                                self.is_top_level_class = False
                                self.has_list_ancestor = False
                                self._child_container_classes = {}
                                self._child_list_classes = {"ipv6-unicast-prefix-length" : ("ipv6_unicast_prefix_length", HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv6Address.Ipv6Unicast.Ipv6UnicastPrefixLengths.Ipv6UnicastPrefixLength)}

                                self.ipv6_unicast_prefix_length = YList(self)
                                self._segment_path = lambda: "ipv6-unicast-prefix-lengths"
                                self._absolute_path = lambda: "Cisco-IOS-XR-fia-hw-profile-cfg:hw-module-profile-config/profile/tcam-table/fib-table/ipv6-address/ipv6-unicast/%s" % self._segment_path()

                            def __setattr__(self, name, value):
                                self._perform_setattr(HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv6Address.Ipv6Unicast.Ipv6UnicastPrefixLengths, [], name, value)


                            class Ipv6UnicastPrefixLength(Entity):
                                """
                                IPv6 Unicast prefix length
                                
                                .. attribute:: prefix_length  <key>
                                
                                	prefix length
                                	**type**\:  int
                                
                                	**range:** 0..128
                                
                                .. attribute:: ipv6_unicast_prefix_percent
                                
                                	curve out percentage of TCAM table entries
                                	**type**\:  str
                                
                                	**units**\: percentage
                                
                                

                                """

                                _prefix = 'fia-hw-profile-cfg'
                                _revision = '2016-06-22'

                                def __init__(self):
                                    super(HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv6Address.Ipv6Unicast.Ipv6UnicastPrefixLengths.Ipv6UnicastPrefixLength, self).__init__()

                                    self.yang_name = "ipv6-unicast-prefix-length"
                                    self.yang_parent_name = "ipv6-unicast-prefix-lengths"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = False
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.prefix_length = YLeaf(YType.uint32, "prefix-length")

                                    self.ipv6_unicast_prefix_percent = YLeaf(YType.str, "ipv6-unicast-prefix-percent")
                                    self._segment_path = lambda: "ipv6-unicast-prefix-length" + "[prefix-length='" + self.prefix_length.get() + "']"
                                    self._absolute_path = lambda: "Cisco-IOS-XR-fia-hw-profile-cfg:hw-module-profile-config/profile/tcam-table/fib-table/ipv6-address/ipv6-unicast/ipv6-unicast-prefix-lengths/%s" % self._segment_path()

                                def __setattr__(self, name, value):
                                    self._perform_setattr(HwModuleProfileConfig.Profile.TcamTable.FibTable.Ipv6Address.Ipv6Unicast.Ipv6UnicastPrefixLengths.Ipv6UnicastPrefixLength, ['prefix_length', 'ipv6_unicast_prefix_percent'], name, value)


    class Tcam(Entity):
        """
        Configure Tcam.
        
        .. attribute:: fib_tcam_scale
        
        	Configure Fib iscale for Tcam
        	**type**\:   :py:class:`FibTcamScale <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_hw_profile_cfg.HwModuleProfileConfig.Tcam.FibTcamScale>`
        
        

        """

        _prefix = 'fia-hw-profile-cfg'
        _revision = '2016-06-22'

        def __init__(self):
            super(HwModuleProfileConfig.Tcam, self).__init__()

            self.yang_name = "tcam"
            self.yang_parent_name = "hw-module-profile-config"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {"fib-tcam-scale" : ("fib_tcam_scale", HwModuleProfileConfig.Tcam.FibTcamScale)}
            self._child_list_classes = {}

            self.fib_tcam_scale = HwModuleProfileConfig.Tcam.FibTcamScale()
            self.fib_tcam_scale.parent = self
            self._children_name_map["fib_tcam_scale"] = "fib-tcam-scale"
            self._children_yang_names.add("fib-tcam-scale")
            self._segment_path = lambda: "tcam"
            self._absolute_path = lambda: "Cisco-IOS-XR-fia-hw-profile-cfg:hw-module-profile-config/%s" % self._segment_path()


        class FibTcamScale(Entity):
            """
            Configure Fib iscale for Tcam.
            
            .. attribute:: ipv4_unicast_scale
            
            	IPv4 table for TCAM LC Scale
            	**type**\:   :py:class:`Ipv4UnicastScale <ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_hw_profile_cfg.HwModuleProfileConfig.Tcam.FibTcamScale.Ipv4UnicastScale>`
            
            

            """

            _prefix = 'fia-hw-profile-cfg'
            _revision = '2016-06-22'

            def __init__(self):
                super(HwModuleProfileConfig.Tcam.FibTcamScale, self).__init__()

                self.yang_name = "fib-tcam-scale"
                self.yang_parent_name = "tcam"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"ipv4-unicast-scale" : ("ipv4_unicast_scale", HwModuleProfileConfig.Tcam.FibTcamScale.Ipv4UnicastScale)}
                self._child_list_classes = {}

                self.ipv4_unicast_scale = HwModuleProfileConfig.Tcam.FibTcamScale.Ipv4UnicastScale()
                self.ipv4_unicast_scale.parent = self
                self._children_name_map["ipv4_unicast_scale"] = "ipv4-unicast-scale"
                self._children_yang_names.add("ipv4-unicast-scale")
                self._segment_path = lambda: "fib-tcam-scale"
                self._absolute_path = lambda: "Cisco-IOS-XR-fia-hw-profile-cfg:hw-module-profile-config/tcam/%s" % self._segment_path()


            class Ipv4UnicastScale(Entity):
                """
                IPv4 table for TCAM LC Scale.
                
                .. attribute:: ipv4_scale
                
                	Scale for IPv4 table for TCAM LC
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                

                """

                _prefix = 'fia-hw-profile-cfg'
                _revision = '2016-06-22'

                def __init__(self):
                    super(HwModuleProfileConfig.Tcam.FibTcamScale.Ipv4UnicastScale, self).__init__()

                    self.yang_name = "ipv4-unicast-scale"
                    self.yang_parent_name = "fib-tcam-scale"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.ipv4_scale = YLeaf(YType.empty, "ipv4-scale")
                    self._segment_path = lambda: "ipv4-unicast-scale"
                    self._absolute_path = lambda: "Cisco-IOS-XR-fia-hw-profile-cfg:hw-module-profile-config/tcam/fib-tcam-scale/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(HwModuleProfileConfig.Tcam.FibTcamScale.Ipv4UnicastScale, ['ipv4_scale'], name, value)

    def clone_ptr(self):
        self._top_entity = HwModuleProfileConfig()
        return self._top_entity

