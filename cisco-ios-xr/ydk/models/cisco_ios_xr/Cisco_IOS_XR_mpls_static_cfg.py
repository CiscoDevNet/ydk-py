""" Cisco_IOS_XR_mpls_static_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR mpls\-static package configuration.

This module contains definitions
for the following management objects\:
  mpls\-static\: MPLS Static Configuration Data

Copyright (c) 2013\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class MplsStaticAddressFamily(Enum):
    """
    MplsStaticAddressFamily

    Mpls static address family

    .. data:: ipv4_unicast = 1

    	IPv4 Unicast

    """

    ipv4_unicast = Enum.YLeaf(1, "ipv4-unicast")


class MplsStaticLabelMode(Enum):
    """
    MplsStaticLabelMode

    Mpls static label mode

    .. data:: per_vrf = 1

    	Per VRF

    .. data:: per_prefix = 2

    	Per Prefix

    .. data:: lsp = 3

    	Cross connect

    """

    per_vrf = Enum.YLeaf(1, "per-vrf")

    per_prefix = Enum.YLeaf(2, "per-prefix")

    lsp = Enum.YLeaf(3, "lsp")


class MplsStaticNhAddressFamily(Enum):
    """
    MplsStaticNhAddressFamily

    Mpls static nh address family

    .. data:: ipv4 = 1

    	IPv4 Next Hop

    .. data:: ipv6 = 2

    	IPv6 Next Hop

    """

    ipv4 = Enum.YLeaf(1, "ipv4")

    ipv6 = Enum.YLeaf(2, "ipv6")


class MplsStaticNhMode(Enum):
    """
    MplsStaticNhMode

    Mpls static nh mode

    .. data:: configured = 0

    	Explicitly configured next hop path

    .. data:: resolve = 1

    	Resolvable next hop which will result in a path

    	set

    """

    configured = Enum.YLeaf(0, "configured")

    resolve = Enum.YLeaf(1, "resolve")


class MplsStaticOutLabelTypes(Enum):
    """
    MplsStaticOutLabelTypes

    Mpls static out label types

    .. data:: none = 0

    	None

    .. data:: out_label = 1

    	OutLabel

    .. data:: pop = 2

    	Pop

    .. data:: exp_null = 3

    	IPv4 explicit-null

    .. data:: ipv6_explicit_null = 4

    	IPv6 explicit-null

    """

    none = Enum.YLeaf(0, "none")

    out_label = Enum.YLeaf(1, "out-label")

    pop = Enum.YLeaf(2, "pop")

    exp_null = Enum.YLeaf(3, "exp-null")

    ipv6_explicit_null = Enum.YLeaf(4, "ipv6-explicit-null")


class MplsStaticPath(Enum):
    """
    MplsStaticPath

    Mpls static path

    .. data:: pop_and_lookup = 1

    	Pop and Lookup

    .. data:: cross_connect = 2

    	Crossconnect

    """

    pop_and_lookup = Enum.YLeaf(1, "pop-and-lookup")

    cross_connect = Enum.YLeaf(2, "cross-connect")


class MplsStaticPathRole(Enum):
    """
    MplsStaticPathRole

    Mpls static path role

    .. data:: primary = 0

    	Path is only for primary traffic

    .. data:: backup = 1

    	Path is only for backup traffic

    .. data:: primary_backup = 2

    	Path is for primary and backup traffic

    """

    primary = Enum.YLeaf(0, "primary")

    backup = Enum.YLeaf(1, "backup")

    primary_backup = Enum.YLeaf(2, "primary-backup")



class MplsStatic(Entity):
    """
    MPLS Static Configuration Data
    
    .. attribute:: default_vrf
    
    	Default VRF
    	**type**\:   :py:class:`DefaultVrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStatic.DefaultVrf>`
    
    .. attribute:: enable
    
    	MPLS Static Apply Enable
    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
    
    .. attribute:: interfaces
    
    	MPLS Static Interface Table
    	**type**\:   :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStatic.Interfaces>`
    
    .. attribute:: vrfs
    
    	VRF table
    	**type**\:   :py:class:`Vrfs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStatic.Vrfs>`
    
    

    """

    _prefix = 'mpls-static-cfg'
    _revision = '2017-05-01'

    def __init__(self):
        super(MplsStatic, self).__init__()
        self._top_entity = None

        self.yang_name = "mpls-static"
        self.yang_parent_name = "Cisco-IOS-XR-mpls-static-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {"default-vrf" : ("default_vrf", MplsStatic.DefaultVrf), "interfaces" : ("interfaces", MplsStatic.Interfaces), "vrfs" : ("vrfs", MplsStatic.Vrfs)}
        self._child_list_classes = {}

        self.enable = YLeaf(YType.empty, "enable")

        self.default_vrf = MplsStatic.DefaultVrf()
        self.default_vrf.parent = self
        self._children_name_map["default_vrf"] = "default-vrf"
        self._children_yang_names.add("default-vrf")

        self.interfaces = MplsStatic.Interfaces()
        self.interfaces.parent = self
        self._children_name_map["interfaces"] = "interfaces"
        self._children_yang_names.add("interfaces")

        self.vrfs = MplsStatic.Vrfs()
        self.vrfs.parent = self
        self._children_name_map["vrfs"] = "vrfs"
        self._children_yang_names.add("vrfs")
        self._segment_path = lambda: "Cisco-IOS-XR-mpls-static-cfg:mpls-static"

    def __setattr__(self, name, value):
        self._perform_setattr(MplsStatic, ['enable'], name, value)


    class DefaultVrf(Entity):
        """
        Default VRF
        
        .. attribute:: afs
        
        	Address Family Table
        	**type**\:   :py:class:`Afs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStatic.DefaultVrf.Afs>`
        
        .. attribute:: enable
        
        	MPLS Static Apply Enable
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: label_switched_paths
        
        	Table of the Label Switched Paths
        	**type**\:   :py:class:`LabelSwitchedPaths <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStatic.DefaultVrf.LabelSwitchedPaths>`
        
        

        """

        _prefix = 'mpls-static-cfg'
        _revision = '2017-05-01'

        def __init__(self):
            super(MplsStatic.DefaultVrf, self).__init__()

            self.yang_name = "default-vrf"
            self.yang_parent_name = "mpls-static"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {"afs" : ("afs", MplsStatic.DefaultVrf.Afs), "label-switched-paths" : ("label_switched_paths", MplsStatic.DefaultVrf.LabelSwitchedPaths)}
            self._child_list_classes = {}

            self.enable = YLeaf(YType.empty, "enable")

            self.afs = MplsStatic.DefaultVrf.Afs()
            self.afs.parent = self
            self._children_name_map["afs"] = "afs"
            self._children_yang_names.add("afs")

            self.label_switched_paths = MplsStatic.DefaultVrf.LabelSwitchedPaths()
            self.label_switched_paths.parent = self
            self._children_name_map["label_switched_paths"] = "label-switched-paths"
            self._children_yang_names.add("label-switched-paths")
            self._segment_path = lambda: "default-vrf"
            self._absolute_path = lambda: "Cisco-IOS-XR-mpls-static-cfg:mpls-static/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(MplsStatic.DefaultVrf, ['enable'], name, value)


        class Afs(Entity):
            """
            Address Family Table
            
            .. attribute:: af
            
            	Address Family
            	**type**\: list of    :py:class:`Af <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStatic.DefaultVrf.Afs.Af>`
            
            

            """

            _prefix = 'mpls-static-cfg'
            _revision = '2017-05-01'

            def __init__(self):
                super(MplsStatic.DefaultVrf.Afs, self).__init__()

                self.yang_name = "afs"
                self.yang_parent_name = "default-vrf"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {"af" : ("af", MplsStatic.DefaultVrf.Afs.Af)}

                self.af = YList(self)
                self._segment_path = lambda: "afs"
                self._absolute_path = lambda: "Cisco-IOS-XR-mpls-static-cfg:mpls-static/default-vrf/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(MplsStatic.DefaultVrf.Afs, [], name, value)


            class Af(Entity):
                """
                Address Family
                
                .. attribute:: afi  <key>
                
                	Address Family
                	**type**\:   :py:class:`MplsStaticAddressFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStaticAddressFamily>`
                
                .. attribute:: enable
                
                	MPLS Static Apply Enable
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: local_labels
                
                	Local Label
                	**type**\:   :py:class:`LocalLabels <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStatic.DefaultVrf.Afs.Af.LocalLabels>`
                
                .. attribute:: top_label_hash
                
                	Top Label Hash
                	**type**\:   :py:class:`TopLabelHash <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStatic.DefaultVrf.Afs.Af.TopLabelHash>`
                
                

                """

                _prefix = 'mpls-static-cfg'
                _revision = '2017-05-01'

                def __init__(self):
                    super(MplsStatic.DefaultVrf.Afs.Af, self).__init__()

                    self.yang_name = "af"
                    self.yang_parent_name = "afs"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {"local-labels" : ("local_labels", MplsStatic.DefaultVrf.Afs.Af.LocalLabels), "top-label-hash" : ("top_label_hash", MplsStatic.DefaultVrf.Afs.Af.TopLabelHash)}
                    self._child_list_classes = {}

                    self.afi = YLeaf(YType.enumeration, "afi")

                    self.enable = YLeaf(YType.empty, "enable")

                    self.local_labels = MplsStatic.DefaultVrf.Afs.Af.LocalLabels()
                    self.local_labels.parent = self
                    self._children_name_map["local_labels"] = "local-labels"
                    self._children_yang_names.add("local-labels")

                    self.top_label_hash = MplsStatic.DefaultVrf.Afs.Af.TopLabelHash()
                    self.top_label_hash.parent = self
                    self._children_name_map["top_label_hash"] = "top-label-hash"
                    self._children_yang_names.add("top-label-hash")
                    self._segment_path = lambda: "af" + "[afi='" + self.afi.get() + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-mpls-static-cfg:mpls-static/default-vrf/afs/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsStatic.DefaultVrf.Afs.Af, ['afi', 'enable'], name, value)


                class LocalLabels(Entity):
                    """
                    Local Label
                    
                    .. attribute:: local_label
                    
                    	Specify Local Label
                    	**type**\: list of    :py:class:`LocalLabel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStatic.DefaultVrf.Afs.Af.LocalLabels.LocalLabel>`
                    
                    

                    """

                    _prefix = 'mpls-static-cfg'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(MplsStatic.DefaultVrf.Afs.Af.LocalLabels, self).__init__()

                        self.yang_name = "local-labels"
                        self.yang_parent_name = "af"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {"local-label" : ("local_label", MplsStatic.DefaultVrf.Afs.Af.LocalLabels.LocalLabel)}

                        self.local_label = YList(self)
                        self._segment_path = lambda: "local-labels"

                    def __setattr__(self, name, value):
                        self._perform_setattr(MplsStatic.DefaultVrf.Afs.Af.LocalLabels, [], name, value)


                    class LocalLabel(Entity):
                        """
                        Specify Local Label
                        
                        .. attribute:: local_label_id  <key>
                        
                        	Local Label
                        	**type**\:  int
                        
                        	**range:** 16..1048575
                        
                        .. attribute:: label_type
                        
                        	MPLS Static Local Label Value
                        	**type**\:   :py:class:`LabelType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStatic.DefaultVrf.Afs.Af.LocalLabels.LocalLabel.LabelType>`
                        
                        .. attribute:: paths
                        
                        	Forward Path Parameters
                        	**type**\:   :py:class:`Paths <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStatic.DefaultVrf.Afs.Af.LocalLabels.LocalLabel.Paths>`
                        
                        

                        """

                        _prefix = 'mpls-static-cfg'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(MplsStatic.DefaultVrf.Afs.Af.LocalLabels.LocalLabel, self).__init__()

                            self.yang_name = "local-label"
                            self.yang_parent_name = "local-labels"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"label-type" : ("label_type", MplsStatic.DefaultVrf.Afs.Af.LocalLabels.LocalLabel.LabelType), "paths" : ("paths", MplsStatic.DefaultVrf.Afs.Af.LocalLabels.LocalLabel.Paths)}
                            self._child_list_classes = {}

                            self.local_label_id = YLeaf(YType.uint32, "local-label-id")

                            self.label_type = MplsStatic.DefaultVrf.Afs.Af.LocalLabels.LocalLabel.LabelType()
                            self.label_type.parent = self
                            self._children_name_map["label_type"] = "label-type"
                            self._children_yang_names.add("label-type")

                            self.paths = MplsStatic.DefaultVrf.Afs.Af.LocalLabels.LocalLabel.Paths()
                            self.paths.parent = self
                            self._children_name_map["paths"] = "paths"
                            self._children_yang_names.add("paths")
                            self._segment_path = lambda: "local-label" + "[local-label-id='" + self.local_label_id.get() + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(MplsStatic.DefaultVrf.Afs.Af.LocalLabels.LocalLabel, ['local_label_id'], name, value)


                        class LabelType(Entity):
                            """
                            MPLS Static Local Label Value
                            
                            .. attribute:: label_mode
                            
                            	Label Mode (PerVRF, PerPrefix or LSP)
                            	**type**\:   :py:class:`MplsStaticLabelMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStaticLabelMode>`
                            
                            .. attribute:: prefix
                            
                            	Address (IPv4/6 depending on AFI)
                            	**type**\: one of the below types:
                            
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            .. attribute:: prefix_length
                            
                            	Prefix length
                            	**type**\:  int
                            
                            	**range:** \-2147483648..2147483647
                            
                            

                            """

                            _prefix = 'mpls-static-cfg'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(MplsStatic.DefaultVrf.Afs.Af.LocalLabels.LocalLabel.LabelType, self).__init__()

                                self.yang_name = "label-type"
                                self.yang_parent_name = "local-label"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.label_mode = YLeaf(YType.enumeration, "label-mode")

                                self.prefix = YLeaf(YType.str, "prefix")

                                self.prefix_length = YLeaf(YType.int32, "prefix-length")
                                self._segment_path = lambda: "label-type"

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsStatic.DefaultVrf.Afs.Af.LocalLabels.LocalLabel.LabelType, ['label_mode', 'prefix', 'prefix_length'], name, value)


                        class Paths(Entity):
                            """
                            Forward Path Parameters
                            
                            .. attribute:: path
                            
                            	Path Information
                            	**type**\: list of    :py:class:`Path <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStatic.DefaultVrf.Afs.Af.LocalLabels.LocalLabel.Paths.Path>`
                            
                            

                            """

                            _prefix = 'mpls-static-cfg'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(MplsStatic.DefaultVrf.Afs.Af.LocalLabels.LocalLabel.Paths, self).__init__()

                                self.yang_name = "paths"
                                self.yang_parent_name = "local-label"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {"path" : ("path", MplsStatic.DefaultVrf.Afs.Af.LocalLabels.LocalLabel.Paths.Path)}

                                self.path = YList(self)
                                self._segment_path = lambda: "paths"

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsStatic.DefaultVrf.Afs.Af.LocalLabels.LocalLabel.Paths, [], name, value)


                            class Path(Entity):
                                """
                                Path Information
                                
                                .. attribute:: path_id  <key>
                                
                                	Number of paths
                                	**type**\:  int
                                
                                	**range:** 1..16
                                
                                .. attribute:: afi
                                
                                	Next hop Address Family
                                	**type**\:   :py:class:`MplsStaticNhAddressFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStaticNhAddressFamily>`
                                
                                	**default value**\: ipv4
                                
                                .. attribute:: backup_id
                                
                                	Backup ID
                                	**type**\:  int
                                
                                	**range:** 0..16
                                
                                	**default value**\: 0
                                
                                .. attribute:: interface_name
                                
                                	Next hop Interface with form <Interface>R/S/I/P
                                	**type**\:  str
                                
                                	**pattern:** [a\-zA\-Z0\-9./\-]+
                                
                                .. attribute:: label_type
                                
                                	Type of label (Outlabel, ExpNull or Pop)
                                	**type**\:   :py:class:`MplsStaticOutLabelTypes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStaticOutLabelTypes>`
                                
                                	**default value**\: none
                                
                                .. attribute:: metric
                                
                                	NH Path Metric
                                	**type**\:  int
                                
                                	**range:** 0..254
                                
                                	**default value**\: 0
                                
                                .. attribute:: next_hop_address
                                
                                	Next Hop IP Address
                                	**type**\: one of the below types:
                                
                                	**type**\:  str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                	**default value**\: 0.0.0.0
                                
                                
                                ----
                                	**type**\:  str
                                
                                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                
                                	**default value**\: 0.0.0.0
                                
                                
                                ----
                                .. attribute:: next_hop_label
                                
                                	Outgoing/NH Label
                                	**type**\:  int
                                
                                	**range:** 16..1048575
                                
                                	**default value**\: 16
                                
                                .. attribute:: nh_mode
                                
                                	Next hop mode
                                	**type**\:   :py:class:`MplsStaticNhMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStaticNhMode>`
                                
                                	**default value**\: configured
                                
                                .. attribute:: path_role
                                
                                	Path Role
                                	**type**\:   :py:class:`MplsStaticPathRole <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStaticPathRole>`
                                
                                	**default value**\: primary
                                
                                .. attribute:: path_type
                                
                                	Type of Path (PopAndLookup, CrossConnect)
                                	**type**\:   :py:class:`MplsStaticPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStaticPath>`
                                
                                	**default value**\: cross-connect
                                
                                

                                """

                                _prefix = 'mpls-static-cfg'
                                _revision = '2017-05-01'

                                def __init__(self):
                                    super(MplsStatic.DefaultVrf.Afs.Af.LocalLabels.LocalLabel.Paths.Path, self).__init__()

                                    self.yang_name = "path"
                                    self.yang_parent_name = "paths"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.path_id = YLeaf(YType.uint32, "path-id")

                                    self.afi = YLeaf(YType.enumeration, "afi")

                                    self.backup_id = YLeaf(YType.uint32, "backup-id")

                                    self.interface_name = YLeaf(YType.str, "interface-name")

                                    self.label_type = YLeaf(YType.enumeration, "label-type")

                                    self.metric = YLeaf(YType.uint32, "metric")

                                    self.next_hop_address = YLeaf(YType.str, "next-hop-address")

                                    self.next_hop_label = YLeaf(YType.uint32, "next-hop-label")

                                    self.nh_mode = YLeaf(YType.enumeration, "nh-mode")

                                    self.path_role = YLeaf(YType.enumeration, "path-role")

                                    self.path_type = YLeaf(YType.enumeration, "path-type")
                                    self._segment_path = lambda: "path" + "[path-id='" + self.path_id.get() + "']"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(MplsStatic.DefaultVrf.Afs.Af.LocalLabels.LocalLabel.Paths.Path, ['path_id', 'afi', 'backup_id', 'interface_name', 'label_type', 'metric', 'next_hop_address', 'next_hop_label', 'nh_mode', 'path_role', 'path_type'], name, value)


                class TopLabelHash(Entity):
                    """
                    Top Label Hash
                    
                    .. attribute:: local_labels
                    
                    	Local Label
                    	**type**\:   :py:class:`LocalLabels <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStatic.DefaultVrf.Afs.Af.TopLabelHash.LocalLabels>`
                    
                    

                    """

                    _prefix = 'mpls-static-cfg'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(MplsStatic.DefaultVrf.Afs.Af.TopLabelHash, self).__init__()

                        self.yang_name = "top-label-hash"
                        self.yang_parent_name = "af"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"local-labels" : ("local_labels", MplsStatic.DefaultVrf.Afs.Af.TopLabelHash.LocalLabels)}
                        self._child_list_classes = {}

                        self.local_labels = MplsStatic.DefaultVrf.Afs.Af.TopLabelHash.LocalLabels()
                        self.local_labels.parent = self
                        self._children_name_map["local_labels"] = "local-labels"
                        self._children_yang_names.add("local-labels")
                        self._segment_path = lambda: "top-label-hash"


                    class LocalLabels(Entity):
                        """
                        Local Label
                        
                        .. attribute:: local_label
                        
                        	Specify Local Label
                        	**type**\: list of    :py:class:`LocalLabel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStatic.DefaultVrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel>`
                        
                        

                        """

                        _prefix = 'mpls-static-cfg'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(MplsStatic.DefaultVrf.Afs.Af.TopLabelHash.LocalLabels, self).__init__()

                            self.yang_name = "local-labels"
                            self.yang_parent_name = "top-label-hash"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {"local-label" : ("local_label", MplsStatic.DefaultVrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel)}

                            self.local_label = YList(self)
                            self._segment_path = lambda: "local-labels"

                        def __setattr__(self, name, value):
                            self._perform_setattr(MplsStatic.DefaultVrf.Afs.Af.TopLabelHash.LocalLabels, [], name, value)


                        class LocalLabel(Entity):
                            """
                            Specify Local Label
                            
                            .. attribute:: local_label_id  <key>
                            
                            	Local Label
                            	**type**\:  int
                            
                            	**range:** 16..1048575
                            
                            .. attribute:: label_type
                            
                            	MPLS Static Local Label Value
                            	**type**\:   :py:class:`LabelType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStatic.DefaultVrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel.LabelType>`
                            
                            .. attribute:: paths
                            
                            	Forward Path Parameters
                            	**type**\:   :py:class:`Paths <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStatic.DefaultVrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel.Paths>`
                            
                            

                            """

                            _prefix = 'mpls-static-cfg'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(MplsStatic.DefaultVrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel, self).__init__()

                                self.yang_name = "local-label"
                                self.yang_parent_name = "local-labels"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {"label-type" : ("label_type", MplsStatic.DefaultVrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel.LabelType), "paths" : ("paths", MplsStatic.DefaultVrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel.Paths)}
                                self._child_list_classes = {}

                                self.local_label_id = YLeaf(YType.uint32, "local-label-id")

                                self.label_type = MplsStatic.DefaultVrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel.LabelType()
                                self.label_type.parent = self
                                self._children_name_map["label_type"] = "label-type"
                                self._children_yang_names.add("label-type")

                                self.paths = MplsStatic.DefaultVrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel.Paths()
                                self.paths.parent = self
                                self._children_name_map["paths"] = "paths"
                                self._children_yang_names.add("paths")
                                self._segment_path = lambda: "local-label" + "[local-label-id='" + self.local_label_id.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsStatic.DefaultVrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel, ['local_label_id'], name, value)


                            class LabelType(Entity):
                                """
                                MPLS Static Local Label Value
                                
                                .. attribute:: label_mode
                                
                                	Label Mode (PerVRF, PerPrefix or LSP)
                                	**type**\:   :py:class:`MplsStaticLabelMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStaticLabelMode>`
                                
                                .. attribute:: prefix
                                
                                	Address (IPv4/6 depending on AFI)
                                	**type**\: one of the below types:
                                
                                	**type**\:  str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                
                                ----
                                	**type**\:  str
                                
                                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                
                                
                                ----
                                .. attribute:: prefix_length
                                
                                	Prefix length
                                	**type**\:  int
                                
                                	**range:** \-2147483648..2147483647
                                
                                

                                """

                                _prefix = 'mpls-static-cfg'
                                _revision = '2017-05-01'

                                def __init__(self):
                                    super(MplsStatic.DefaultVrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel.LabelType, self).__init__()

                                    self.yang_name = "label-type"
                                    self.yang_parent_name = "local-label"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.label_mode = YLeaf(YType.enumeration, "label-mode")

                                    self.prefix = YLeaf(YType.str, "prefix")

                                    self.prefix_length = YLeaf(YType.int32, "prefix-length")
                                    self._segment_path = lambda: "label-type"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(MplsStatic.DefaultVrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel.LabelType, ['label_mode', 'prefix', 'prefix_length'], name, value)


                            class Paths(Entity):
                                """
                                Forward Path Parameters
                                
                                .. attribute:: path
                                
                                	Path Information
                                	**type**\: list of    :py:class:`Path <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStatic.DefaultVrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel.Paths.Path>`
                                
                                

                                """

                                _prefix = 'mpls-static-cfg'
                                _revision = '2017-05-01'

                                def __init__(self):
                                    super(MplsStatic.DefaultVrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel.Paths, self).__init__()

                                    self.yang_name = "paths"
                                    self.yang_parent_name = "local-label"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {"path" : ("path", MplsStatic.DefaultVrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel.Paths.Path)}

                                    self.path = YList(self)
                                    self._segment_path = lambda: "paths"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(MplsStatic.DefaultVrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel.Paths, [], name, value)


                                class Path(Entity):
                                    """
                                    Path Information
                                    
                                    .. attribute:: path_id  <key>
                                    
                                    	Number of paths
                                    	**type**\:  int
                                    
                                    	**range:** 1..16
                                    
                                    .. attribute:: afi
                                    
                                    	Next hop Address Family
                                    	**type**\:   :py:class:`MplsStaticNhAddressFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStaticNhAddressFamily>`
                                    
                                    	**default value**\: ipv4
                                    
                                    .. attribute:: backup_id
                                    
                                    	Backup ID
                                    	**type**\:  int
                                    
                                    	**range:** 0..16
                                    
                                    	**default value**\: 0
                                    
                                    .. attribute:: interface_name
                                    
                                    	Next hop Interface with form <Interface>R/S/I/P
                                    	**type**\:  str
                                    
                                    	**pattern:** [a\-zA\-Z0\-9./\-]+
                                    
                                    .. attribute:: label_type
                                    
                                    	Type of label (Outlabel, ExpNull or Pop)
                                    	**type**\:   :py:class:`MplsStaticOutLabelTypes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStaticOutLabelTypes>`
                                    
                                    	**default value**\: none
                                    
                                    .. attribute:: metric
                                    
                                    	NH Path Metric
                                    	**type**\:  int
                                    
                                    	**range:** 0..254
                                    
                                    	**default value**\: 0
                                    
                                    .. attribute:: next_hop_address
                                    
                                    	Next Hop IP Address
                                    	**type**\: one of the below types:
                                    
                                    	**type**\:  str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    	**default value**\: 0.0.0.0
                                    
                                    
                                    ----
                                    	**type**\:  str
                                    
                                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                    
                                    	**default value**\: 0.0.0.0
                                    
                                    
                                    ----
                                    .. attribute:: next_hop_label
                                    
                                    	Outgoing/NH Label
                                    	**type**\:  int
                                    
                                    	**range:** 16..1048575
                                    
                                    	**default value**\: 16
                                    
                                    .. attribute:: nh_mode
                                    
                                    	Next hop mode
                                    	**type**\:   :py:class:`MplsStaticNhMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStaticNhMode>`
                                    
                                    	**default value**\: configured
                                    
                                    .. attribute:: path_role
                                    
                                    	Path Role
                                    	**type**\:   :py:class:`MplsStaticPathRole <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStaticPathRole>`
                                    
                                    	**default value**\: primary
                                    
                                    .. attribute:: path_type
                                    
                                    	Type of Path (PopAndLookup, CrossConnect)
                                    	**type**\:   :py:class:`MplsStaticPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStaticPath>`
                                    
                                    	**default value**\: cross-connect
                                    
                                    

                                    """

                                    _prefix = 'mpls-static-cfg'
                                    _revision = '2017-05-01'

                                    def __init__(self):
                                        super(MplsStatic.DefaultVrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel.Paths.Path, self).__init__()

                                        self.yang_name = "path"
                                        self.yang_parent_name = "paths"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}

                                        self.path_id = YLeaf(YType.uint32, "path-id")

                                        self.afi = YLeaf(YType.enumeration, "afi")

                                        self.backup_id = YLeaf(YType.uint32, "backup-id")

                                        self.interface_name = YLeaf(YType.str, "interface-name")

                                        self.label_type = YLeaf(YType.enumeration, "label-type")

                                        self.metric = YLeaf(YType.uint32, "metric")

                                        self.next_hop_address = YLeaf(YType.str, "next-hop-address")

                                        self.next_hop_label = YLeaf(YType.uint32, "next-hop-label")

                                        self.nh_mode = YLeaf(YType.enumeration, "nh-mode")

                                        self.path_role = YLeaf(YType.enumeration, "path-role")

                                        self.path_type = YLeaf(YType.enumeration, "path-type")
                                        self._segment_path = lambda: "path" + "[path-id='" + self.path_id.get() + "']"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(MplsStatic.DefaultVrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel.Paths.Path, ['path_id', 'afi', 'backup_id', 'interface_name', 'label_type', 'metric', 'next_hop_address', 'next_hop_label', 'nh_mode', 'path_role', 'path_type'], name, value)


        class LabelSwitchedPaths(Entity):
            """
            Table of the Label Switched Paths
            
            .. attribute:: label_switched_path
            
            	Label Switched Path
            	**type**\: list of    :py:class:`LabelSwitchedPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStatic.DefaultVrf.LabelSwitchedPaths.LabelSwitchedPath>`
            
            

            """

            _prefix = 'mpls-static-cfg'
            _revision = '2017-05-01'

            def __init__(self):
                super(MplsStatic.DefaultVrf.LabelSwitchedPaths, self).__init__()

                self.yang_name = "label-switched-paths"
                self.yang_parent_name = "default-vrf"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {"label-switched-path" : ("label_switched_path", MplsStatic.DefaultVrf.LabelSwitchedPaths.LabelSwitchedPath)}

                self.label_switched_path = YList(self)
                self._segment_path = lambda: "label-switched-paths"
                self._absolute_path = lambda: "Cisco-IOS-XR-mpls-static-cfg:mpls-static/default-vrf/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(MplsStatic.DefaultVrf.LabelSwitchedPaths, [], name, value)


            class LabelSwitchedPath(Entity):
                """
                Label Switched Path
                
                .. attribute:: lsp_name  <key>
                
                	LSP Name
                	**type**\:  str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: backup_paths
                
                	Backup Path Parameters
                	**type**\:   :py:class:`BackupPaths <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStatic.DefaultVrf.LabelSwitchedPaths.LabelSwitchedPath.BackupPaths>`
                
                .. attribute:: enable
                
                	MPLS Static Apply Enable
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: in_label
                
                	MPLS Static Local Label Value
                	**type**\:   :py:class:`InLabel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStatic.DefaultVrf.LabelSwitchedPaths.LabelSwitchedPath.InLabel>`
                
                .. attribute:: paths
                
                	Forward Path Parameters
                	**type**\:   :py:class:`Paths <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStatic.DefaultVrf.LabelSwitchedPaths.LabelSwitchedPath.Paths>`
                
                

                """

                _prefix = 'mpls-static-cfg'
                _revision = '2017-05-01'

                def __init__(self):
                    super(MplsStatic.DefaultVrf.LabelSwitchedPaths.LabelSwitchedPath, self).__init__()

                    self.yang_name = "label-switched-path"
                    self.yang_parent_name = "label-switched-paths"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {"backup-paths" : ("backup_paths", MplsStatic.DefaultVrf.LabelSwitchedPaths.LabelSwitchedPath.BackupPaths), "in-label" : ("in_label", MplsStatic.DefaultVrf.LabelSwitchedPaths.LabelSwitchedPath.InLabel), "paths" : ("paths", MplsStatic.DefaultVrf.LabelSwitchedPaths.LabelSwitchedPath.Paths)}
                    self._child_list_classes = {}

                    self.lsp_name = YLeaf(YType.str, "lsp-name")

                    self.enable = YLeaf(YType.empty, "enable")

                    self.backup_paths = MplsStatic.DefaultVrf.LabelSwitchedPaths.LabelSwitchedPath.BackupPaths()
                    self.backup_paths.parent = self
                    self._children_name_map["backup_paths"] = "backup-paths"
                    self._children_yang_names.add("backup-paths")

                    self.in_label = MplsStatic.DefaultVrf.LabelSwitchedPaths.LabelSwitchedPath.InLabel()
                    self.in_label.parent = self
                    self._children_name_map["in_label"] = "in-label"
                    self._children_yang_names.add("in-label")

                    self.paths = MplsStatic.DefaultVrf.LabelSwitchedPaths.LabelSwitchedPath.Paths()
                    self.paths.parent = self
                    self._children_name_map["paths"] = "paths"
                    self._children_yang_names.add("paths")
                    self._segment_path = lambda: "label-switched-path" + "[lsp-name='" + self.lsp_name.get() + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-mpls-static-cfg:mpls-static/default-vrf/label-switched-paths/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsStatic.DefaultVrf.LabelSwitchedPaths.LabelSwitchedPath, ['lsp_name', 'enable'], name, value)


                class BackupPaths(Entity):
                    """
                    Backup Path Parameters
                    
                    .. attribute:: path
                    
                    	Path Information
                    	**type**\: list of    :py:class:`Path <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStatic.DefaultVrf.LabelSwitchedPaths.LabelSwitchedPath.BackupPaths.Path>`
                    
                    

                    """

                    _prefix = 'mpls-static-cfg'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(MplsStatic.DefaultVrf.LabelSwitchedPaths.LabelSwitchedPath.BackupPaths, self).__init__()

                        self.yang_name = "backup-paths"
                        self.yang_parent_name = "label-switched-path"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {"path" : ("path", MplsStatic.DefaultVrf.LabelSwitchedPaths.LabelSwitchedPath.BackupPaths.Path)}

                        self.path = YList(self)
                        self._segment_path = lambda: "backup-paths"

                    def __setattr__(self, name, value):
                        self._perform_setattr(MplsStatic.DefaultVrf.LabelSwitchedPaths.LabelSwitchedPath.BackupPaths, [], name, value)


                    class Path(Entity):
                        """
                        Path Information
                        
                        .. attribute:: path_id  <key>
                        
                        	Number of paths
                        	**type**\:  int
                        
                        	**range:** 1..16
                        
                        .. attribute:: afi
                        
                        	Next hop Address Family
                        	**type**\:   :py:class:`MplsStaticNhAddressFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStaticNhAddressFamily>`
                        
                        	**default value**\: ipv4
                        
                        .. attribute:: backup_id
                        
                        	Backup ID
                        	**type**\:  int
                        
                        	**range:** 0..16
                        
                        	**default value**\: 0
                        
                        .. attribute:: interface_name
                        
                        	Next hop Interface with form <Interface>R/S/I/P
                        	**type**\:  str
                        
                        	**pattern:** [a\-zA\-Z0\-9./\-]+
                        
                        .. attribute:: label_type
                        
                        	Type of label (Outlabel, ExpNull or Pop)
                        	**type**\:   :py:class:`MplsStaticOutLabelTypes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStaticOutLabelTypes>`
                        
                        	**default value**\: none
                        
                        .. attribute:: metric
                        
                        	NH Path Metric
                        	**type**\:  int
                        
                        	**range:** 0..254
                        
                        	**default value**\: 0
                        
                        .. attribute:: next_hop_address
                        
                        	Next Hop IP Address
                        	**type**\: one of the below types:
                        
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        	**default value**\: 0.0.0.0
                        
                        
                        ----
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        	**default value**\: 0.0.0.0
                        
                        
                        ----
                        .. attribute:: next_hop_label
                        
                        	Outgoing/NH Label
                        	**type**\:  int
                        
                        	**range:** 16..1048575
                        
                        	**default value**\: 16
                        
                        .. attribute:: nh_mode
                        
                        	Next hop mode
                        	**type**\:   :py:class:`MplsStaticNhMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStaticNhMode>`
                        
                        	**default value**\: configured
                        
                        .. attribute:: path_role
                        
                        	Path Role
                        	**type**\:   :py:class:`MplsStaticPathRole <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStaticPathRole>`
                        
                        	**default value**\: primary
                        
                        .. attribute:: path_type
                        
                        	Type of Path (PopAndLookup, CrossConnect)
                        	**type**\:   :py:class:`MplsStaticPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStaticPath>`
                        
                        	**default value**\: cross-connect
                        
                        

                        """

                        _prefix = 'mpls-static-cfg'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(MplsStatic.DefaultVrf.LabelSwitchedPaths.LabelSwitchedPath.BackupPaths.Path, self).__init__()

                            self.yang_name = "path"
                            self.yang_parent_name = "backup-paths"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.path_id = YLeaf(YType.uint32, "path-id")

                            self.afi = YLeaf(YType.enumeration, "afi")

                            self.backup_id = YLeaf(YType.uint32, "backup-id")

                            self.interface_name = YLeaf(YType.str, "interface-name")

                            self.label_type = YLeaf(YType.enumeration, "label-type")

                            self.metric = YLeaf(YType.uint32, "metric")

                            self.next_hop_address = YLeaf(YType.str, "next-hop-address")

                            self.next_hop_label = YLeaf(YType.uint32, "next-hop-label")

                            self.nh_mode = YLeaf(YType.enumeration, "nh-mode")

                            self.path_role = YLeaf(YType.enumeration, "path-role")

                            self.path_type = YLeaf(YType.enumeration, "path-type")
                            self._segment_path = lambda: "path" + "[path-id='" + self.path_id.get() + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(MplsStatic.DefaultVrf.LabelSwitchedPaths.LabelSwitchedPath.BackupPaths.Path, ['path_id', 'afi', 'backup_id', 'interface_name', 'label_type', 'metric', 'next_hop_address', 'next_hop_label', 'nh_mode', 'path_role', 'path_type'], name, value)


                class InLabel(Entity):
                    """
                    MPLS Static Local Label Value
                    
                    .. attribute:: in_label_value
                    
                    	Local Label
                    	**type**\:  int
                    
                    	**range:** 16..1048575
                    
                    .. attribute:: label_mode
                    
                    	Label Mode (PerVRF, PerPrefix or LSP)
                    	**type**\:   :py:class:`MplsStaticLabelMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStaticLabelMode>`
                    
                    .. attribute:: prefix
                    
                    	Address (IPv4/6 depending on AFI)
                    	**type**\: one of the below types:
                    
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    
                    ----
                    	**type**\:  str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    
                    ----
                    .. attribute:: prefix_length
                    
                    	Prefix length
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: tlh_mode
                    
                    	Top Label Hashing Mode
                    	**type**\:  bool
                    
                    

                    """

                    _prefix = 'mpls-static-cfg'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(MplsStatic.DefaultVrf.LabelSwitchedPaths.LabelSwitchedPath.InLabel, self).__init__()

                        self.yang_name = "in-label"
                        self.yang_parent_name = "label-switched-path"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.in_label_value = YLeaf(YType.uint32, "in-label-value")

                        self.label_mode = YLeaf(YType.enumeration, "label-mode")

                        self.prefix = YLeaf(YType.str, "prefix")

                        self.prefix_length = YLeaf(YType.int32, "prefix-length")

                        self.tlh_mode = YLeaf(YType.boolean, "tlh-mode")
                        self._segment_path = lambda: "in-label"

                    def __setattr__(self, name, value):
                        self._perform_setattr(MplsStatic.DefaultVrf.LabelSwitchedPaths.LabelSwitchedPath.InLabel, ['in_label_value', 'label_mode', 'prefix', 'prefix_length', 'tlh_mode'], name, value)


                class Paths(Entity):
                    """
                    Forward Path Parameters
                    
                    .. attribute:: path
                    
                    	Path Information
                    	**type**\: list of    :py:class:`Path <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStatic.DefaultVrf.LabelSwitchedPaths.LabelSwitchedPath.Paths.Path>`
                    
                    

                    """

                    _prefix = 'mpls-static-cfg'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(MplsStatic.DefaultVrf.LabelSwitchedPaths.LabelSwitchedPath.Paths, self).__init__()

                        self.yang_name = "paths"
                        self.yang_parent_name = "label-switched-path"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {"path" : ("path", MplsStatic.DefaultVrf.LabelSwitchedPaths.LabelSwitchedPath.Paths.Path)}

                        self.path = YList(self)
                        self._segment_path = lambda: "paths"

                    def __setattr__(self, name, value):
                        self._perform_setattr(MplsStatic.DefaultVrf.LabelSwitchedPaths.LabelSwitchedPath.Paths, [], name, value)


                    class Path(Entity):
                        """
                        Path Information
                        
                        .. attribute:: path_id  <key>
                        
                        	Number of paths
                        	**type**\:  int
                        
                        	**range:** 1..16
                        
                        .. attribute:: afi
                        
                        	Next hop Address Family
                        	**type**\:   :py:class:`MplsStaticNhAddressFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStaticNhAddressFamily>`
                        
                        	**default value**\: ipv4
                        
                        .. attribute:: backup_id
                        
                        	Backup ID
                        	**type**\:  int
                        
                        	**range:** 0..16
                        
                        	**default value**\: 0
                        
                        .. attribute:: interface_name
                        
                        	Next hop Interface with form <Interface>R/S/I/P
                        	**type**\:  str
                        
                        	**pattern:** [a\-zA\-Z0\-9./\-]+
                        
                        .. attribute:: label_type
                        
                        	Type of label (Outlabel, ExpNull or Pop)
                        	**type**\:   :py:class:`MplsStaticOutLabelTypes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStaticOutLabelTypes>`
                        
                        	**default value**\: none
                        
                        .. attribute:: metric
                        
                        	NH Path Metric
                        	**type**\:  int
                        
                        	**range:** 0..254
                        
                        	**default value**\: 0
                        
                        .. attribute:: next_hop_address
                        
                        	Next Hop IP Address
                        	**type**\: one of the below types:
                        
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        	**default value**\: 0.0.0.0
                        
                        
                        ----
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        	**default value**\: 0.0.0.0
                        
                        
                        ----
                        .. attribute:: next_hop_label
                        
                        	Outgoing/NH Label
                        	**type**\:  int
                        
                        	**range:** 16..1048575
                        
                        	**default value**\: 16
                        
                        .. attribute:: nh_mode
                        
                        	Next hop mode
                        	**type**\:   :py:class:`MplsStaticNhMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStaticNhMode>`
                        
                        	**default value**\: configured
                        
                        .. attribute:: path_role
                        
                        	Path Role
                        	**type**\:   :py:class:`MplsStaticPathRole <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStaticPathRole>`
                        
                        	**default value**\: primary
                        
                        .. attribute:: path_type
                        
                        	Type of Path (PopAndLookup, CrossConnect)
                        	**type**\:   :py:class:`MplsStaticPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStaticPath>`
                        
                        	**default value**\: cross-connect
                        
                        

                        """

                        _prefix = 'mpls-static-cfg'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(MplsStatic.DefaultVrf.LabelSwitchedPaths.LabelSwitchedPath.Paths.Path, self).__init__()

                            self.yang_name = "path"
                            self.yang_parent_name = "paths"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.path_id = YLeaf(YType.uint32, "path-id")

                            self.afi = YLeaf(YType.enumeration, "afi")

                            self.backup_id = YLeaf(YType.uint32, "backup-id")

                            self.interface_name = YLeaf(YType.str, "interface-name")

                            self.label_type = YLeaf(YType.enumeration, "label-type")

                            self.metric = YLeaf(YType.uint32, "metric")

                            self.next_hop_address = YLeaf(YType.str, "next-hop-address")

                            self.next_hop_label = YLeaf(YType.uint32, "next-hop-label")

                            self.nh_mode = YLeaf(YType.enumeration, "nh-mode")

                            self.path_role = YLeaf(YType.enumeration, "path-role")

                            self.path_type = YLeaf(YType.enumeration, "path-type")
                            self._segment_path = lambda: "path" + "[path-id='" + self.path_id.get() + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(MplsStatic.DefaultVrf.LabelSwitchedPaths.LabelSwitchedPath.Paths.Path, ['path_id', 'afi', 'backup_id', 'interface_name', 'label_type', 'metric', 'next_hop_address', 'next_hop_label', 'nh_mode', 'path_role', 'path_type'], name, value)


    class Interfaces(Entity):
        """
        MPLS Static Interface Table
        
        .. attribute:: interface
        
        	MPLS Static Interface Enable
        	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStatic.Interfaces.Interface>`
        
        

        """

        _prefix = 'mpls-static-cfg'
        _revision = '2017-05-01'

        def __init__(self):
            super(MplsStatic.Interfaces, self).__init__()

            self.yang_name = "interfaces"
            self.yang_parent_name = "mpls-static"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"interface" : ("interface", MplsStatic.Interfaces.Interface)}

            self.interface = YList(self)
            self._segment_path = lambda: "interfaces"
            self._absolute_path = lambda: "Cisco-IOS-XR-mpls-static-cfg:mpls-static/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(MplsStatic.Interfaces, [], name, value)


        class Interface(Entity):
            """
            MPLS Static Interface Enable
            
            .. attribute:: interface_name  <key>
            
            	Name of Interface
            	**type**\:  str
            
            	**pattern:** [a\-zA\-Z0\-9./\-]+
            
            

            """

            _prefix = 'mpls-static-cfg'
            _revision = '2017-05-01'

            def __init__(self):
                super(MplsStatic.Interfaces.Interface, self).__init__()

                self.yang_name = "interface"
                self.yang_parent_name = "interfaces"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.interface_name = YLeaf(YType.str, "interface-name")
                self._segment_path = lambda: "interface" + "[interface-name='" + self.interface_name.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-mpls-static-cfg:mpls-static/interfaces/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(MplsStatic.Interfaces.Interface, ['interface_name'], name, value)


    class Vrfs(Entity):
        """
        VRF table
        
        .. attribute:: vrf
        
        	VRF Name
        	**type**\: list of    :py:class:`Vrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStatic.Vrfs.Vrf>`
        
        

        """

        _prefix = 'mpls-static-cfg'
        _revision = '2017-05-01'

        def __init__(self):
            super(MplsStatic.Vrfs, self).__init__()

            self.yang_name = "vrfs"
            self.yang_parent_name = "mpls-static"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"vrf" : ("vrf", MplsStatic.Vrfs.Vrf)}

            self.vrf = YList(self)
            self._segment_path = lambda: "vrfs"
            self._absolute_path = lambda: "Cisco-IOS-XR-mpls-static-cfg:mpls-static/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(MplsStatic.Vrfs, [], name, value)


        class Vrf(Entity):
            """
            VRF Name
            
            .. attribute:: vrf_name  <key>
            
            	VRF Name
            	**type**\:  str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: afs
            
            	Address Family Table
            	**type**\:   :py:class:`Afs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStatic.Vrfs.Vrf.Afs>`
            
            .. attribute:: enable
            
            	MPLS Static Apply Enable
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: label_switched_paths
            
            	Table of the Label Switched Paths
            	**type**\:   :py:class:`LabelSwitchedPaths <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStatic.Vrfs.Vrf.LabelSwitchedPaths>`
            
            

            """

            _prefix = 'mpls-static-cfg'
            _revision = '2017-05-01'

            def __init__(self):
                super(MplsStatic.Vrfs.Vrf, self).__init__()

                self.yang_name = "vrf"
                self.yang_parent_name = "vrfs"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"afs" : ("afs", MplsStatic.Vrfs.Vrf.Afs), "label-switched-paths" : ("label_switched_paths", MplsStatic.Vrfs.Vrf.LabelSwitchedPaths)}
                self._child_list_classes = {}

                self.vrf_name = YLeaf(YType.str, "vrf-name")

                self.enable = YLeaf(YType.empty, "enable")

                self.afs = MplsStatic.Vrfs.Vrf.Afs()
                self.afs.parent = self
                self._children_name_map["afs"] = "afs"
                self._children_yang_names.add("afs")

                self.label_switched_paths = MplsStatic.Vrfs.Vrf.LabelSwitchedPaths()
                self.label_switched_paths.parent = self
                self._children_name_map["label_switched_paths"] = "label-switched-paths"
                self._children_yang_names.add("label-switched-paths")
                self._segment_path = lambda: "vrf" + "[vrf-name='" + self.vrf_name.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-mpls-static-cfg:mpls-static/vrfs/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(MplsStatic.Vrfs.Vrf, ['vrf_name', 'enable'], name, value)


            class Afs(Entity):
                """
                Address Family Table
                
                .. attribute:: af
                
                	Address Family
                	**type**\: list of    :py:class:`Af <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStatic.Vrfs.Vrf.Afs.Af>`
                
                

                """

                _prefix = 'mpls-static-cfg'
                _revision = '2017-05-01'

                def __init__(self):
                    super(MplsStatic.Vrfs.Vrf.Afs, self).__init__()

                    self.yang_name = "afs"
                    self.yang_parent_name = "vrf"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {"af" : ("af", MplsStatic.Vrfs.Vrf.Afs.Af)}

                    self.af = YList(self)
                    self._segment_path = lambda: "afs"

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsStatic.Vrfs.Vrf.Afs, [], name, value)


                class Af(Entity):
                    """
                    Address Family
                    
                    .. attribute:: afi  <key>
                    
                    	Address Family
                    	**type**\:   :py:class:`MplsStaticAddressFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStaticAddressFamily>`
                    
                    .. attribute:: enable
                    
                    	MPLS Static Apply Enable
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: local_labels
                    
                    	Local Label
                    	**type**\:   :py:class:`LocalLabels <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStatic.Vrfs.Vrf.Afs.Af.LocalLabels>`
                    
                    .. attribute:: top_label_hash
                    
                    	Top Label Hash
                    	**type**\:   :py:class:`TopLabelHash <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStatic.Vrfs.Vrf.Afs.Af.TopLabelHash>`
                    
                    

                    """

                    _prefix = 'mpls-static-cfg'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(MplsStatic.Vrfs.Vrf.Afs.Af, self).__init__()

                        self.yang_name = "af"
                        self.yang_parent_name = "afs"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"local-labels" : ("local_labels", MplsStatic.Vrfs.Vrf.Afs.Af.LocalLabels), "top-label-hash" : ("top_label_hash", MplsStatic.Vrfs.Vrf.Afs.Af.TopLabelHash)}
                        self._child_list_classes = {}

                        self.afi = YLeaf(YType.enumeration, "afi")

                        self.enable = YLeaf(YType.empty, "enable")

                        self.local_labels = MplsStatic.Vrfs.Vrf.Afs.Af.LocalLabels()
                        self.local_labels.parent = self
                        self._children_name_map["local_labels"] = "local-labels"
                        self._children_yang_names.add("local-labels")

                        self.top_label_hash = MplsStatic.Vrfs.Vrf.Afs.Af.TopLabelHash()
                        self.top_label_hash.parent = self
                        self._children_name_map["top_label_hash"] = "top-label-hash"
                        self._children_yang_names.add("top-label-hash")
                        self._segment_path = lambda: "af" + "[afi='" + self.afi.get() + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(MplsStatic.Vrfs.Vrf.Afs.Af, ['afi', 'enable'], name, value)


                    class LocalLabels(Entity):
                        """
                        Local Label
                        
                        .. attribute:: local_label
                        
                        	Specify Local Label
                        	**type**\: list of    :py:class:`LocalLabel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStatic.Vrfs.Vrf.Afs.Af.LocalLabels.LocalLabel>`
                        
                        

                        """

                        _prefix = 'mpls-static-cfg'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(MplsStatic.Vrfs.Vrf.Afs.Af.LocalLabels, self).__init__()

                            self.yang_name = "local-labels"
                            self.yang_parent_name = "af"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {"local-label" : ("local_label", MplsStatic.Vrfs.Vrf.Afs.Af.LocalLabels.LocalLabel)}

                            self.local_label = YList(self)
                            self._segment_path = lambda: "local-labels"

                        def __setattr__(self, name, value):
                            self._perform_setattr(MplsStatic.Vrfs.Vrf.Afs.Af.LocalLabels, [], name, value)


                        class LocalLabel(Entity):
                            """
                            Specify Local Label
                            
                            .. attribute:: local_label_id  <key>
                            
                            	Local Label
                            	**type**\:  int
                            
                            	**range:** 16..1048575
                            
                            .. attribute:: label_type
                            
                            	MPLS Static Local Label Value
                            	**type**\:   :py:class:`LabelType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStatic.Vrfs.Vrf.Afs.Af.LocalLabels.LocalLabel.LabelType>`
                            
                            .. attribute:: paths
                            
                            	Forward Path Parameters
                            	**type**\:   :py:class:`Paths <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStatic.Vrfs.Vrf.Afs.Af.LocalLabels.LocalLabel.Paths>`
                            
                            

                            """

                            _prefix = 'mpls-static-cfg'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(MplsStatic.Vrfs.Vrf.Afs.Af.LocalLabels.LocalLabel, self).__init__()

                                self.yang_name = "local-label"
                                self.yang_parent_name = "local-labels"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {"label-type" : ("label_type", MplsStatic.Vrfs.Vrf.Afs.Af.LocalLabels.LocalLabel.LabelType), "paths" : ("paths", MplsStatic.Vrfs.Vrf.Afs.Af.LocalLabels.LocalLabel.Paths)}
                                self._child_list_classes = {}

                                self.local_label_id = YLeaf(YType.uint32, "local-label-id")

                                self.label_type = MplsStatic.Vrfs.Vrf.Afs.Af.LocalLabels.LocalLabel.LabelType()
                                self.label_type.parent = self
                                self._children_name_map["label_type"] = "label-type"
                                self._children_yang_names.add("label-type")

                                self.paths = MplsStatic.Vrfs.Vrf.Afs.Af.LocalLabels.LocalLabel.Paths()
                                self.paths.parent = self
                                self._children_name_map["paths"] = "paths"
                                self._children_yang_names.add("paths")
                                self._segment_path = lambda: "local-label" + "[local-label-id='" + self.local_label_id.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsStatic.Vrfs.Vrf.Afs.Af.LocalLabels.LocalLabel, ['local_label_id'], name, value)


                            class LabelType(Entity):
                                """
                                MPLS Static Local Label Value
                                
                                .. attribute:: label_mode
                                
                                	Label Mode (PerVRF, PerPrefix or LSP)
                                	**type**\:   :py:class:`MplsStaticLabelMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStaticLabelMode>`
                                
                                .. attribute:: prefix
                                
                                	Address (IPv4/6 depending on AFI)
                                	**type**\: one of the below types:
                                
                                	**type**\:  str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                
                                ----
                                	**type**\:  str
                                
                                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                
                                
                                ----
                                .. attribute:: prefix_length
                                
                                	Prefix length
                                	**type**\:  int
                                
                                	**range:** \-2147483648..2147483647
                                
                                

                                """

                                _prefix = 'mpls-static-cfg'
                                _revision = '2017-05-01'

                                def __init__(self):
                                    super(MplsStatic.Vrfs.Vrf.Afs.Af.LocalLabels.LocalLabel.LabelType, self).__init__()

                                    self.yang_name = "label-type"
                                    self.yang_parent_name = "local-label"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.label_mode = YLeaf(YType.enumeration, "label-mode")

                                    self.prefix = YLeaf(YType.str, "prefix")

                                    self.prefix_length = YLeaf(YType.int32, "prefix-length")
                                    self._segment_path = lambda: "label-type"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(MplsStatic.Vrfs.Vrf.Afs.Af.LocalLabels.LocalLabel.LabelType, ['label_mode', 'prefix', 'prefix_length'], name, value)


                            class Paths(Entity):
                                """
                                Forward Path Parameters
                                
                                .. attribute:: path
                                
                                	Path Information
                                	**type**\: list of    :py:class:`Path <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStatic.Vrfs.Vrf.Afs.Af.LocalLabels.LocalLabel.Paths.Path>`
                                
                                

                                """

                                _prefix = 'mpls-static-cfg'
                                _revision = '2017-05-01'

                                def __init__(self):
                                    super(MplsStatic.Vrfs.Vrf.Afs.Af.LocalLabels.LocalLabel.Paths, self).__init__()

                                    self.yang_name = "paths"
                                    self.yang_parent_name = "local-label"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {"path" : ("path", MplsStatic.Vrfs.Vrf.Afs.Af.LocalLabels.LocalLabel.Paths.Path)}

                                    self.path = YList(self)
                                    self._segment_path = lambda: "paths"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(MplsStatic.Vrfs.Vrf.Afs.Af.LocalLabels.LocalLabel.Paths, [], name, value)


                                class Path(Entity):
                                    """
                                    Path Information
                                    
                                    .. attribute:: path_id  <key>
                                    
                                    	Number of paths
                                    	**type**\:  int
                                    
                                    	**range:** 1..16
                                    
                                    .. attribute:: afi
                                    
                                    	Next hop Address Family
                                    	**type**\:   :py:class:`MplsStaticNhAddressFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStaticNhAddressFamily>`
                                    
                                    	**default value**\: ipv4
                                    
                                    .. attribute:: backup_id
                                    
                                    	Backup ID
                                    	**type**\:  int
                                    
                                    	**range:** 0..16
                                    
                                    	**default value**\: 0
                                    
                                    .. attribute:: interface_name
                                    
                                    	Next hop Interface with form <Interface>R/S/I/P
                                    	**type**\:  str
                                    
                                    	**pattern:** [a\-zA\-Z0\-9./\-]+
                                    
                                    .. attribute:: label_type
                                    
                                    	Type of label (Outlabel, ExpNull or Pop)
                                    	**type**\:   :py:class:`MplsStaticOutLabelTypes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStaticOutLabelTypes>`
                                    
                                    	**default value**\: none
                                    
                                    .. attribute:: metric
                                    
                                    	NH Path Metric
                                    	**type**\:  int
                                    
                                    	**range:** 0..254
                                    
                                    	**default value**\: 0
                                    
                                    .. attribute:: next_hop_address
                                    
                                    	Next Hop IP Address
                                    	**type**\: one of the below types:
                                    
                                    	**type**\:  str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    	**default value**\: 0.0.0.0
                                    
                                    
                                    ----
                                    	**type**\:  str
                                    
                                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                    
                                    	**default value**\: 0.0.0.0
                                    
                                    
                                    ----
                                    .. attribute:: next_hop_label
                                    
                                    	Outgoing/NH Label
                                    	**type**\:  int
                                    
                                    	**range:** 16..1048575
                                    
                                    	**default value**\: 16
                                    
                                    .. attribute:: nh_mode
                                    
                                    	Next hop mode
                                    	**type**\:   :py:class:`MplsStaticNhMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStaticNhMode>`
                                    
                                    	**default value**\: configured
                                    
                                    .. attribute:: path_role
                                    
                                    	Path Role
                                    	**type**\:   :py:class:`MplsStaticPathRole <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStaticPathRole>`
                                    
                                    	**default value**\: primary
                                    
                                    .. attribute:: path_type
                                    
                                    	Type of Path (PopAndLookup, CrossConnect)
                                    	**type**\:   :py:class:`MplsStaticPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStaticPath>`
                                    
                                    	**default value**\: cross-connect
                                    
                                    

                                    """

                                    _prefix = 'mpls-static-cfg'
                                    _revision = '2017-05-01'

                                    def __init__(self):
                                        super(MplsStatic.Vrfs.Vrf.Afs.Af.LocalLabels.LocalLabel.Paths.Path, self).__init__()

                                        self.yang_name = "path"
                                        self.yang_parent_name = "paths"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}

                                        self.path_id = YLeaf(YType.uint32, "path-id")

                                        self.afi = YLeaf(YType.enumeration, "afi")

                                        self.backup_id = YLeaf(YType.uint32, "backup-id")

                                        self.interface_name = YLeaf(YType.str, "interface-name")

                                        self.label_type = YLeaf(YType.enumeration, "label-type")

                                        self.metric = YLeaf(YType.uint32, "metric")

                                        self.next_hop_address = YLeaf(YType.str, "next-hop-address")

                                        self.next_hop_label = YLeaf(YType.uint32, "next-hop-label")

                                        self.nh_mode = YLeaf(YType.enumeration, "nh-mode")

                                        self.path_role = YLeaf(YType.enumeration, "path-role")

                                        self.path_type = YLeaf(YType.enumeration, "path-type")
                                        self._segment_path = lambda: "path" + "[path-id='" + self.path_id.get() + "']"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(MplsStatic.Vrfs.Vrf.Afs.Af.LocalLabels.LocalLabel.Paths.Path, ['path_id', 'afi', 'backup_id', 'interface_name', 'label_type', 'metric', 'next_hop_address', 'next_hop_label', 'nh_mode', 'path_role', 'path_type'], name, value)


                    class TopLabelHash(Entity):
                        """
                        Top Label Hash
                        
                        .. attribute:: local_labels
                        
                        	Local Label
                        	**type**\:   :py:class:`LocalLabels <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStatic.Vrfs.Vrf.Afs.Af.TopLabelHash.LocalLabels>`
                        
                        

                        """

                        _prefix = 'mpls-static-cfg'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(MplsStatic.Vrfs.Vrf.Afs.Af.TopLabelHash, self).__init__()

                            self.yang_name = "top-label-hash"
                            self.yang_parent_name = "af"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"local-labels" : ("local_labels", MplsStatic.Vrfs.Vrf.Afs.Af.TopLabelHash.LocalLabels)}
                            self._child_list_classes = {}

                            self.local_labels = MplsStatic.Vrfs.Vrf.Afs.Af.TopLabelHash.LocalLabels()
                            self.local_labels.parent = self
                            self._children_name_map["local_labels"] = "local-labels"
                            self._children_yang_names.add("local-labels")
                            self._segment_path = lambda: "top-label-hash"


                        class LocalLabels(Entity):
                            """
                            Local Label
                            
                            .. attribute:: local_label
                            
                            	Specify Local Label
                            	**type**\: list of    :py:class:`LocalLabel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStatic.Vrfs.Vrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel>`
                            
                            

                            """

                            _prefix = 'mpls-static-cfg'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(MplsStatic.Vrfs.Vrf.Afs.Af.TopLabelHash.LocalLabels, self).__init__()

                                self.yang_name = "local-labels"
                                self.yang_parent_name = "top-label-hash"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {"local-label" : ("local_label", MplsStatic.Vrfs.Vrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel)}

                                self.local_label = YList(self)
                                self._segment_path = lambda: "local-labels"

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsStatic.Vrfs.Vrf.Afs.Af.TopLabelHash.LocalLabels, [], name, value)


                            class LocalLabel(Entity):
                                """
                                Specify Local Label
                                
                                .. attribute:: local_label_id  <key>
                                
                                	Local Label
                                	**type**\:  int
                                
                                	**range:** 16..1048575
                                
                                .. attribute:: label_type
                                
                                	MPLS Static Local Label Value
                                	**type**\:   :py:class:`LabelType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStatic.Vrfs.Vrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel.LabelType>`
                                
                                .. attribute:: paths
                                
                                	Forward Path Parameters
                                	**type**\:   :py:class:`Paths <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStatic.Vrfs.Vrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel.Paths>`
                                
                                

                                """

                                _prefix = 'mpls-static-cfg'
                                _revision = '2017-05-01'

                                def __init__(self):
                                    super(MplsStatic.Vrfs.Vrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel, self).__init__()

                                    self.yang_name = "local-label"
                                    self.yang_parent_name = "local-labels"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {"label-type" : ("label_type", MplsStatic.Vrfs.Vrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel.LabelType), "paths" : ("paths", MplsStatic.Vrfs.Vrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel.Paths)}
                                    self._child_list_classes = {}

                                    self.local_label_id = YLeaf(YType.uint32, "local-label-id")

                                    self.label_type = MplsStatic.Vrfs.Vrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel.LabelType()
                                    self.label_type.parent = self
                                    self._children_name_map["label_type"] = "label-type"
                                    self._children_yang_names.add("label-type")

                                    self.paths = MplsStatic.Vrfs.Vrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel.Paths()
                                    self.paths.parent = self
                                    self._children_name_map["paths"] = "paths"
                                    self._children_yang_names.add("paths")
                                    self._segment_path = lambda: "local-label" + "[local-label-id='" + self.local_label_id.get() + "']"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(MplsStatic.Vrfs.Vrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel, ['local_label_id'], name, value)


                                class LabelType(Entity):
                                    """
                                    MPLS Static Local Label Value
                                    
                                    .. attribute:: label_mode
                                    
                                    	Label Mode (PerVRF, PerPrefix or LSP)
                                    	**type**\:   :py:class:`MplsStaticLabelMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStaticLabelMode>`
                                    
                                    .. attribute:: prefix
                                    
                                    	Address (IPv4/6 depending on AFI)
                                    	**type**\: one of the below types:
                                    
                                    	**type**\:  str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    
                                    ----
                                    	**type**\:  str
                                    
                                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                    
                                    
                                    ----
                                    .. attribute:: prefix_length
                                    
                                    	Prefix length
                                    	**type**\:  int
                                    
                                    	**range:** \-2147483648..2147483647
                                    
                                    

                                    """

                                    _prefix = 'mpls-static-cfg'
                                    _revision = '2017-05-01'

                                    def __init__(self):
                                        super(MplsStatic.Vrfs.Vrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel.LabelType, self).__init__()

                                        self.yang_name = "label-type"
                                        self.yang_parent_name = "local-label"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {}

                                        self.label_mode = YLeaf(YType.enumeration, "label-mode")

                                        self.prefix = YLeaf(YType.str, "prefix")

                                        self.prefix_length = YLeaf(YType.int32, "prefix-length")
                                        self._segment_path = lambda: "label-type"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(MplsStatic.Vrfs.Vrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel.LabelType, ['label_mode', 'prefix', 'prefix_length'], name, value)


                                class Paths(Entity):
                                    """
                                    Forward Path Parameters
                                    
                                    .. attribute:: path
                                    
                                    	Path Information
                                    	**type**\: list of    :py:class:`Path <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStatic.Vrfs.Vrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel.Paths.Path>`
                                    
                                    

                                    """

                                    _prefix = 'mpls-static-cfg'
                                    _revision = '2017-05-01'

                                    def __init__(self):
                                        super(MplsStatic.Vrfs.Vrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel.Paths, self).__init__()

                                        self.yang_name = "paths"
                                        self.yang_parent_name = "local-label"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {}
                                        self._child_list_classes = {"path" : ("path", MplsStatic.Vrfs.Vrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel.Paths.Path)}

                                        self.path = YList(self)
                                        self._segment_path = lambda: "paths"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(MplsStatic.Vrfs.Vrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel.Paths, [], name, value)


                                    class Path(Entity):
                                        """
                                        Path Information
                                        
                                        .. attribute:: path_id  <key>
                                        
                                        	Number of paths
                                        	**type**\:  int
                                        
                                        	**range:** 1..16
                                        
                                        .. attribute:: afi
                                        
                                        	Next hop Address Family
                                        	**type**\:   :py:class:`MplsStaticNhAddressFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStaticNhAddressFamily>`
                                        
                                        	**default value**\: ipv4
                                        
                                        .. attribute:: backup_id
                                        
                                        	Backup ID
                                        	**type**\:  int
                                        
                                        	**range:** 0..16
                                        
                                        	**default value**\: 0
                                        
                                        .. attribute:: interface_name
                                        
                                        	Next hop Interface with form <Interface>R/S/I/P
                                        	**type**\:  str
                                        
                                        	**pattern:** [a\-zA\-Z0\-9./\-]+
                                        
                                        .. attribute:: label_type
                                        
                                        	Type of label (Outlabel, ExpNull or Pop)
                                        	**type**\:   :py:class:`MplsStaticOutLabelTypes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStaticOutLabelTypes>`
                                        
                                        	**default value**\: none
                                        
                                        .. attribute:: metric
                                        
                                        	NH Path Metric
                                        	**type**\:  int
                                        
                                        	**range:** 0..254
                                        
                                        	**default value**\: 0
                                        
                                        .. attribute:: next_hop_address
                                        
                                        	Next Hop IP Address
                                        	**type**\: one of the below types:
                                        
                                        	**type**\:  str
                                        
                                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                        
                                        	**default value**\: 0.0.0.0
                                        
                                        
                                        ----
                                        	**type**\:  str
                                        
                                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                        
                                        	**default value**\: 0.0.0.0
                                        
                                        
                                        ----
                                        .. attribute:: next_hop_label
                                        
                                        	Outgoing/NH Label
                                        	**type**\:  int
                                        
                                        	**range:** 16..1048575
                                        
                                        	**default value**\: 16
                                        
                                        .. attribute:: nh_mode
                                        
                                        	Next hop mode
                                        	**type**\:   :py:class:`MplsStaticNhMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStaticNhMode>`
                                        
                                        	**default value**\: configured
                                        
                                        .. attribute:: path_role
                                        
                                        	Path Role
                                        	**type**\:   :py:class:`MplsStaticPathRole <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStaticPathRole>`
                                        
                                        	**default value**\: primary
                                        
                                        .. attribute:: path_type
                                        
                                        	Type of Path (PopAndLookup, CrossConnect)
                                        	**type**\:   :py:class:`MplsStaticPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStaticPath>`
                                        
                                        	**default value**\: cross-connect
                                        
                                        

                                        """

                                        _prefix = 'mpls-static-cfg'
                                        _revision = '2017-05-01'

                                        def __init__(self):
                                            super(MplsStatic.Vrfs.Vrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel.Paths.Path, self).__init__()

                                            self.yang_name = "path"
                                            self.yang_parent_name = "paths"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self._child_container_classes = {}
                                            self._child_list_classes = {}

                                            self.path_id = YLeaf(YType.uint32, "path-id")

                                            self.afi = YLeaf(YType.enumeration, "afi")

                                            self.backup_id = YLeaf(YType.uint32, "backup-id")

                                            self.interface_name = YLeaf(YType.str, "interface-name")

                                            self.label_type = YLeaf(YType.enumeration, "label-type")

                                            self.metric = YLeaf(YType.uint32, "metric")

                                            self.next_hop_address = YLeaf(YType.str, "next-hop-address")

                                            self.next_hop_label = YLeaf(YType.uint32, "next-hop-label")

                                            self.nh_mode = YLeaf(YType.enumeration, "nh-mode")

                                            self.path_role = YLeaf(YType.enumeration, "path-role")

                                            self.path_type = YLeaf(YType.enumeration, "path-type")
                                            self._segment_path = lambda: "path" + "[path-id='" + self.path_id.get() + "']"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(MplsStatic.Vrfs.Vrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel.Paths.Path, ['path_id', 'afi', 'backup_id', 'interface_name', 'label_type', 'metric', 'next_hop_address', 'next_hop_label', 'nh_mode', 'path_role', 'path_type'], name, value)


            class LabelSwitchedPaths(Entity):
                """
                Table of the Label Switched Paths
                
                .. attribute:: label_switched_path
                
                	Label Switched Path
                	**type**\: list of    :py:class:`LabelSwitchedPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStatic.Vrfs.Vrf.LabelSwitchedPaths.LabelSwitchedPath>`
                
                

                """

                _prefix = 'mpls-static-cfg'
                _revision = '2017-05-01'

                def __init__(self):
                    super(MplsStatic.Vrfs.Vrf.LabelSwitchedPaths, self).__init__()

                    self.yang_name = "label-switched-paths"
                    self.yang_parent_name = "vrf"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {"label-switched-path" : ("label_switched_path", MplsStatic.Vrfs.Vrf.LabelSwitchedPaths.LabelSwitchedPath)}

                    self.label_switched_path = YList(self)
                    self._segment_path = lambda: "label-switched-paths"

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsStatic.Vrfs.Vrf.LabelSwitchedPaths, [], name, value)


                class LabelSwitchedPath(Entity):
                    """
                    Label Switched Path
                    
                    .. attribute:: lsp_name  <key>
                    
                    	LSP Name
                    	**type**\:  str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: backup_paths
                    
                    	Backup Path Parameters
                    	**type**\:   :py:class:`BackupPaths <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStatic.Vrfs.Vrf.LabelSwitchedPaths.LabelSwitchedPath.BackupPaths>`
                    
                    .. attribute:: enable
                    
                    	MPLS Static Apply Enable
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: in_label
                    
                    	MPLS Static Local Label Value
                    	**type**\:   :py:class:`InLabel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStatic.Vrfs.Vrf.LabelSwitchedPaths.LabelSwitchedPath.InLabel>`
                    
                    .. attribute:: paths
                    
                    	Forward Path Parameters
                    	**type**\:   :py:class:`Paths <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStatic.Vrfs.Vrf.LabelSwitchedPaths.LabelSwitchedPath.Paths>`
                    
                    

                    """

                    _prefix = 'mpls-static-cfg'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(MplsStatic.Vrfs.Vrf.LabelSwitchedPaths.LabelSwitchedPath, self).__init__()

                        self.yang_name = "label-switched-path"
                        self.yang_parent_name = "label-switched-paths"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"backup-paths" : ("backup_paths", MplsStatic.Vrfs.Vrf.LabelSwitchedPaths.LabelSwitchedPath.BackupPaths), "in-label" : ("in_label", MplsStatic.Vrfs.Vrf.LabelSwitchedPaths.LabelSwitchedPath.InLabel), "paths" : ("paths", MplsStatic.Vrfs.Vrf.LabelSwitchedPaths.LabelSwitchedPath.Paths)}
                        self._child_list_classes = {}

                        self.lsp_name = YLeaf(YType.str, "lsp-name")

                        self.enable = YLeaf(YType.empty, "enable")

                        self.backup_paths = MplsStatic.Vrfs.Vrf.LabelSwitchedPaths.LabelSwitchedPath.BackupPaths()
                        self.backup_paths.parent = self
                        self._children_name_map["backup_paths"] = "backup-paths"
                        self._children_yang_names.add("backup-paths")

                        self.in_label = MplsStatic.Vrfs.Vrf.LabelSwitchedPaths.LabelSwitchedPath.InLabel()
                        self.in_label.parent = self
                        self._children_name_map["in_label"] = "in-label"
                        self._children_yang_names.add("in-label")

                        self.paths = MplsStatic.Vrfs.Vrf.LabelSwitchedPaths.LabelSwitchedPath.Paths()
                        self.paths.parent = self
                        self._children_name_map["paths"] = "paths"
                        self._children_yang_names.add("paths")
                        self._segment_path = lambda: "label-switched-path" + "[lsp-name='" + self.lsp_name.get() + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(MplsStatic.Vrfs.Vrf.LabelSwitchedPaths.LabelSwitchedPath, ['lsp_name', 'enable'], name, value)


                    class BackupPaths(Entity):
                        """
                        Backup Path Parameters
                        
                        .. attribute:: path
                        
                        	Path Information
                        	**type**\: list of    :py:class:`Path <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStatic.Vrfs.Vrf.LabelSwitchedPaths.LabelSwitchedPath.BackupPaths.Path>`
                        
                        

                        """

                        _prefix = 'mpls-static-cfg'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(MplsStatic.Vrfs.Vrf.LabelSwitchedPaths.LabelSwitchedPath.BackupPaths, self).__init__()

                            self.yang_name = "backup-paths"
                            self.yang_parent_name = "label-switched-path"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {"path" : ("path", MplsStatic.Vrfs.Vrf.LabelSwitchedPaths.LabelSwitchedPath.BackupPaths.Path)}

                            self.path = YList(self)
                            self._segment_path = lambda: "backup-paths"

                        def __setattr__(self, name, value):
                            self._perform_setattr(MplsStatic.Vrfs.Vrf.LabelSwitchedPaths.LabelSwitchedPath.BackupPaths, [], name, value)


                        class Path(Entity):
                            """
                            Path Information
                            
                            .. attribute:: path_id  <key>
                            
                            	Number of paths
                            	**type**\:  int
                            
                            	**range:** 1..16
                            
                            .. attribute:: afi
                            
                            	Next hop Address Family
                            	**type**\:   :py:class:`MplsStaticNhAddressFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStaticNhAddressFamily>`
                            
                            	**default value**\: ipv4
                            
                            .. attribute:: backup_id
                            
                            	Backup ID
                            	**type**\:  int
                            
                            	**range:** 0..16
                            
                            	**default value**\: 0
                            
                            .. attribute:: interface_name
                            
                            	Next hop Interface with form <Interface>R/S/I/P
                            	**type**\:  str
                            
                            	**pattern:** [a\-zA\-Z0\-9./\-]+
                            
                            .. attribute:: label_type
                            
                            	Type of label (Outlabel, ExpNull or Pop)
                            	**type**\:   :py:class:`MplsStaticOutLabelTypes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStaticOutLabelTypes>`
                            
                            	**default value**\: none
                            
                            .. attribute:: metric
                            
                            	NH Path Metric
                            	**type**\:  int
                            
                            	**range:** 0..254
                            
                            	**default value**\: 0
                            
                            .. attribute:: next_hop_address
                            
                            	Next Hop IP Address
                            	**type**\: one of the below types:
                            
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            	**default value**\: 0.0.0.0
                            
                            
                            ----
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            	**default value**\: 0.0.0.0
                            
                            
                            ----
                            .. attribute:: next_hop_label
                            
                            	Outgoing/NH Label
                            	**type**\:  int
                            
                            	**range:** 16..1048575
                            
                            	**default value**\: 16
                            
                            .. attribute:: nh_mode
                            
                            	Next hop mode
                            	**type**\:   :py:class:`MplsStaticNhMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStaticNhMode>`
                            
                            	**default value**\: configured
                            
                            .. attribute:: path_role
                            
                            	Path Role
                            	**type**\:   :py:class:`MplsStaticPathRole <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStaticPathRole>`
                            
                            	**default value**\: primary
                            
                            .. attribute:: path_type
                            
                            	Type of Path (PopAndLookup, CrossConnect)
                            	**type**\:   :py:class:`MplsStaticPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStaticPath>`
                            
                            	**default value**\: cross-connect
                            
                            

                            """

                            _prefix = 'mpls-static-cfg'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(MplsStatic.Vrfs.Vrf.LabelSwitchedPaths.LabelSwitchedPath.BackupPaths.Path, self).__init__()

                                self.yang_name = "path"
                                self.yang_parent_name = "backup-paths"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.path_id = YLeaf(YType.uint32, "path-id")

                                self.afi = YLeaf(YType.enumeration, "afi")

                                self.backup_id = YLeaf(YType.uint32, "backup-id")

                                self.interface_name = YLeaf(YType.str, "interface-name")

                                self.label_type = YLeaf(YType.enumeration, "label-type")

                                self.metric = YLeaf(YType.uint32, "metric")

                                self.next_hop_address = YLeaf(YType.str, "next-hop-address")

                                self.next_hop_label = YLeaf(YType.uint32, "next-hop-label")

                                self.nh_mode = YLeaf(YType.enumeration, "nh-mode")

                                self.path_role = YLeaf(YType.enumeration, "path-role")

                                self.path_type = YLeaf(YType.enumeration, "path-type")
                                self._segment_path = lambda: "path" + "[path-id='" + self.path_id.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsStatic.Vrfs.Vrf.LabelSwitchedPaths.LabelSwitchedPath.BackupPaths.Path, ['path_id', 'afi', 'backup_id', 'interface_name', 'label_type', 'metric', 'next_hop_address', 'next_hop_label', 'nh_mode', 'path_role', 'path_type'], name, value)


                    class InLabel(Entity):
                        """
                        MPLS Static Local Label Value
                        
                        .. attribute:: in_label_value
                        
                        	Local Label
                        	**type**\:  int
                        
                        	**range:** 16..1048575
                        
                        .. attribute:: label_mode
                        
                        	Label Mode (PerVRF, PerPrefix or LSP)
                        	**type**\:   :py:class:`MplsStaticLabelMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStaticLabelMode>`
                        
                        .. attribute:: prefix
                        
                        	Address (IPv4/6 depending on AFI)
                        	**type**\: one of the below types:
                        
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        .. attribute:: prefix_length
                        
                        	Prefix length
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: tlh_mode
                        
                        	Top Label Hashing Mode
                        	**type**\:  bool
                        
                        

                        """

                        _prefix = 'mpls-static-cfg'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(MplsStatic.Vrfs.Vrf.LabelSwitchedPaths.LabelSwitchedPath.InLabel, self).__init__()

                            self.yang_name = "in-label"
                            self.yang_parent_name = "label-switched-path"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.in_label_value = YLeaf(YType.uint32, "in-label-value")

                            self.label_mode = YLeaf(YType.enumeration, "label-mode")

                            self.prefix = YLeaf(YType.str, "prefix")

                            self.prefix_length = YLeaf(YType.int32, "prefix-length")

                            self.tlh_mode = YLeaf(YType.boolean, "tlh-mode")
                            self._segment_path = lambda: "in-label"

                        def __setattr__(self, name, value):
                            self._perform_setattr(MplsStatic.Vrfs.Vrf.LabelSwitchedPaths.LabelSwitchedPath.InLabel, ['in_label_value', 'label_mode', 'prefix', 'prefix_length', 'tlh_mode'], name, value)


                    class Paths(Entity):
                        """
                        Forward Path Parameters
                        
                        .. attribute:: path
                        
                        	Path Information
                        	**type**\: list of    :py:class:`Path <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStatic.Vrfs.Vrf.LabelSwitchedPaths.LabelSwitchedPath.Paths.Path>`
                        
                        

                        """

                        _prefix = 'mpls-static-cfg'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(MplsStatic.Vrfs.Vrf.LabelSwitchedPaths.LabelSwitchedPath.Paths, self).__init__()

                            self.yang_name = "paths"
                            self.yang_parent_name = "label-switched-path"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {"path" : ("path", MplsStatic.Vrfs.Vrf.LabelSwitchedPaths.LabelSwitchedPath.Paths.Path)}

                            self.path = YList(self)
                            self._segment_path = lambda: "paths"

                        def __setattr__(self, name, value):
                            self._perform_setattr(MplsStatic.Vrfs.Vrf.LabelSwitchedPaths.LabelSwitchedPath.Paths, [], name, value)


                        class Path(Entity):
                            """
                            Path Information
                            
                            .. attribute:: path_id  <key>
                            
                            	Number of paths
                            	**type**\:  int
                            
                            	**range:** 1..16
                            
                            .. attribute:: afi
                            
                            	Next hop Address Family
                            	**type**\:   :py:class:`MplsStaticNhAddressFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStaticNhAddressFamily>`
                            
                            	**default value**\: ipv4
                            
                            .. attribute:: backup_id
                            
                            	Backup ID
                            	**type**\:  int
                            
                            	**range:** 0..16
                            
                            	**default value**\: 0
                            
                            .. attribute:: interface_name
                            
                            	Next hop Interface with form <Interface>R/S/I/P
                            	**type**\:  str
                            
                            	**pattern:** [a\-zA\-Z0\-9./\-]+
                            
                            .. attribute:: label_type
                            
                            	Type of label (Outlabel, ExpNull or Pop)
                            	**type**\:   :py:class:`MplsStaticOutLabelTypes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStaticOutLabelTypes>`
                            
                            	**default value**\: none
                            
                            .. attribute:: metric
                            
                            	NH Path Metric
                            	**type**\:  int
                            
                            	**range:** 0..254
                            
                            	**default value**\: 0
                            
                            .. attribute:: next_hop_address
                            
                            	Next Hop IP Address
                            	**type**\: one of the below types:
                            
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            	**default value**\: 0.0.0.0
                            
                            
                            ----
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            	**default value**\: 0.0.0.0
                            
                            
                            ----
                            .. attribute:: next_hop_label
                            
                            	Outgoing/NH Label
                            	**type**\:  int
                            
                            	**range:** 16..1048575
                            
                            	**default value**\: 16
                            
                            .. attribute:: nh_mode
                            
                            	Next hop mode
                            	**type**\:   :py:class:`MplsStaticNhMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStaticNhMode>`
                            
                            	**default value**\: configured
                            
                            .. attribute:: path_role
                            
                            	Path Role
                            	**type**\:   :py:class:`MplsStaticPathRole <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStaticPathRole>`
                            
                            	**default value**\: primary
                            
                            .. attribute:: path_type
                            
                            	Type of Path (PopAndLookup, CrossConnect)
                            	**type**\:   :py:class:`MplsStaticPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStaticPath>`
                            
                            	**default value**\: cross-connect
                            
                            

                            """

                            _prefix = 'mpls-static-cfg'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(MplsStatic.Vrfs.Vrf.LabelSwitchedPaths.LabelSwitchedPath.Paths.Path, self).__init__()

                                self.yang_name = "path"
                                self.yang_parent_name = "paths"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.path_id = YLeaf(YType.uint32, "path-id")

                                self.afi = YLeaf(YType.enumeration, "afi")

                                self.backup_id = YLeaf(YType.uint32, "backup-id")

                                self.interface_name = YLeaf(YType.str, "interface-name")

                                self.label_type = YLeaf(YType.enumeration, "label-type")

                                self.metric = YLeaf(YType.uint32, "metric")

                                self.next_hop_address = YLeaf(YType.str, "next-hop-address")

                                self.next_hop_label = YLeaf(YType.uint32, "next-hop-label")

                                self.nh_mode = YLeaf(YType.enumeration, "nh-mode")

                                self.path_role = YLeaf(YType.enumeration, "path-role")

                                self.path_type = YLeaf(YType.enumeration, "path-type")
                                self._segment_path = lambda: "path" + "[path-id='" + self.path_id.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsStatic.Vrfs.Vrf.LabelSwitchedPaths.LabelSwitchedPath.Paths.Path, ['path_id', 'afi', 'backup_id', 'interface_name', 'label_type', 'metric', 'next_hop_address', 'next_hop_label', 'nh_mode', 'path_role', 'path_type'], name, value)

    def clone_ptr(self):
        self._top_entity = MplsStatic()
        return self._top_entity

