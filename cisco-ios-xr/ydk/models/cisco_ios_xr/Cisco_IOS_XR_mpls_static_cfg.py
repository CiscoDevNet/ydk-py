""" Cisco_IOS_XR_mpls_static_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR mpls\-static package configuration.

This module contains definitions
for the following management objects\:
  mpls\-static\: MPLS Static Configuration Data

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class MplsStaticAddressFamily(Enum):
    """
    MplsStaticAddressFamily (Enum Class)

    Mpls static address family

    .. data:: ipv4_unicast = 1

    	IPv4 Unicast

    """

    ipv4_unicast = Enum.YLeaf(1, "ipv4-unicast")


class MplsStaticLabelMode(Enum):
    """
    MplsStaticLabelMode (Enum Class)

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
    MplsStaticNhAddressFamily (Enum Class)

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
    MplsStaticNhMode (Enum Class)

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
    MplsStaticOutLabelTypes (Enum Class)

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
    MplsStaticPath (Enum Class)

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
    MplsStaticPathRole (Enum Class)

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
    
    .. attribute:: vrfs
    
    	VRF table
    	**type**\:  :py:class:`Vrfs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStatic.Vrfs>`
    
    .. attribute:: interfaces
    
    	MPLS Static Interface Table
    	**type**\:  :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStatic.Interfaces>`
    
    .. attribute:: default_vrf
    
    	Default VRF
    	**type**\:  :py:class:`DefaultVrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStatic.DefaultVrf>`
    
    .. attribute:: enable
    
    	MPLS Static Apply Enable
    	**type**\: :py:class:`Empty<ydk.types.Empty>`
    
    

    """

    _prefix = 'mpls-static-cfg'
    _revision = '2017-09-07'

    def __init__(self):
        super(MplsStatic, self).__init__()
        self._top_entity = None

        self.yang_name = "mpls-static"
        self.yang_parent_name = "Cisco-IOS-XR-mpls-static-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("vrfs", ("vrfs", MplsStatic.Vrfs)), ("interfaces", ("interfaces", MplsStatic.Interfaces)), ("default-vrf", ("default_vrf", MplsStatic.DefaultVrf))])
        self._leafs = OrderedDict([
            ('enable', (YLeaf(YType.empty, 'enable'), ['Empty'])),
        ])
        self.enable = None

        self.vrfs = MplsStatic.Vrfs()
        self.vrfs.parent = self
        self._children_name_map["vrfs"] = "vrfs"

        self.interfaces = MplsStatic.Interfaces()
        self.interfaces.parent = self
        self._children_name_map["interfaces"] = "interfaces"

        self.default_vrf = MplsStatic.DefaultVrf()
        self.default_vrf.parent = self
        self._children_name_map["default_vrf"] = "default-vrf"
        self._segment_path = lambda: "Cisco-IOS-XR-mpls-static-cfg:mpls-static"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(MplsStatic, ['enable'], name, value)


    class Vrfs(Entity):
        """
        VRF table
        
        .. attribute:: vrf
        
        	VRF Name
        	**type**\: list of  		 :py:class:`Vrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStatic.Vrfs.Vrf>`
        
        

        """

        _prefix = 'mpls-static-cfg'
        _revision = '2017-09-07'

        def __init__(self):
            super(MplsStatic.Vrfs, self).__init__()

            self.yang_name = "vrfs"
            self.yang_parent_name = "mpls-static"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("vrf", ("vrf", MplsStatic.Vrfs.Vrf))])
            self._leafs = OrderedDict()

            self.vrf = YList(self)
            self._segment_path = lambda: "vrfs"
            self._absolute_path = lambda: "Cisco-IOS-XR-mpls-static-cfg:mpls-static/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(MplsStatic.Vrfs, [], name, value)


        class Vrf(Entity):
            """
            VRF Name
            
            .. attribute:: vrf_name  (key)
            
            	VRF Name
            	**type**\: str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: label_switched_paths
            
            	Table of the Label Switched Paths
            	**type**\:  :py:class:`LabelSwitchedPaths <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStatic.Vrfs.Vrf.LabelSwitchedPaths>`
            
            .. attribute:: afs
            
            	Address Family Table
            	**type**\:  :py:class:`Afs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStatic.Vrfs.Vrf.Afs>`
            
            .. attribute:: enable
            
            	MPLS Static Apply Enable
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'mpls-static-cfg'
            _revision = '2017-09-07'

            def __init__(self):
                super(MplsStatic.Vrfs.Vrf, self).__init__()

                self.yang_name = "vrf"
                self.yang_parent_name = "vrfs"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['vrf_name']
                self._child_classes = OrderedDict([("label-switched-paths", ("label_switched_paths", MplsStatic.Vrfs.Vrf.LabelSwitchedPaths)), ("afs", ("afs", MplsStatic.Vrfs.Vrf.Afs))])
                self._leafs = OrderedDict([
                    ('vrf_name', (YLeaf(YType.str, 'vrf-name'), ['str'])),
                    ('enable', (YLeaf(YType.empty, 'enable'), ['Empty'])),
                ])
                self.vrf_name = None
                self.enable = None

                self.label_switched_paths = MplsStatic.Vrfs.Vrf.LabelSwitchedPaths()
                self.label_switched_paths.parent = self
                self._children_name_map["label_switched_paths"] = "label-switched-paths"

                self.afs = MplsStatic.Vrfs.Vrf.Afs()
                self.afs.parent = self
                self._children_name_map["afs"] = "afs"
                self._segment_path = lambda: "vrf" + "[vrf-name='" + str(self.vrf_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-mpls-static-cfg:mpls-static/vrfs/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(MplsStatic.Vrfs.Vrf, ['vrf_name', 'enable'], name, value)


            class LabelSwitchedPaths(Entity):
                """
                Table of the Label Switched Paths
                
                .. attribute:: label_switched_path
                
                	Label Switched Path
                	**type**\: list of  		 :py:class:`LabelSwitchedPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStatic.Vrfs.Vrf.LabelSwitchedPaths.LabelSwitchedPath>`
                
                

                """

                _prefix = 'mpls-static-cfg'
                _revision = '2017-09-07'

                def __init__(self):
                    super(MplsStatic.Vrfs.Vrf.LabelSwitchedPaths, self).__init__()

                    self.yang_name = "label-switched-paths"
                    self.yang_parent_name = "vrf"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("label-switched-path", ("label_switched_path", MplsStatic.Vrfs.Vrf.LabelSwitchedPaths.LabelSwitchedPath))])
                    self._leafs = OrderedDict()

                    self.label_switched_path = YList(self)
                    self._segment_path = lambda: "label-switched-paths"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsStatic.Vrfs.Vrf.LabelSwitchedPaths, [], name, value)


                class LabelSwitchedPath(Entity):
                    """
                    Label Switched Path
                    
                    .. attribute:: lsp_name  (key)
                    
                    	LSP Name
                    	**type**\: str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: backup_paths
                    
                    	Backup Path Parameters
                    	**type**\:  :py:class:`BackupPaths <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStatic.Vrfs.Vrf.LabelSwitchedPaths.LabelSwitchedPath.BackupPaths>`
                    
                    .. attribute:: in_label
                    
                    	MPLS Static Local Label Value
                    	**type**\:  :py:class:`InLabel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStatic.Vrfs.Vrf.LabelSwitchedPaths.LabelSwitchedPath.InLabel>`
                    
                    .. attribute:: enable
                    
                    	MPLS Static Apply Enable
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: paths
                    
                    	Forward Path Parameters
                    	**type**\:  :py:class:`Paths <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStatic.Vrfs.Vrf.LabelSwitchedPaths.LabelSwitchedPath.Paths>`
                    
                    

                    """

                    _prefix = 'mpls-static-cfg'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(MplsStatic.Vrfs.Vrf.LabelSwitchedPaths.LabelSwitchedPath, self).__init__()

                        self.yang_name = "label-switched-path"
                        self.yang_parent_name = "label-switched-paths"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['lsp_name']
                        self._child_classes = OrderedDict([("backup-paths", ("backup_paths", MplsStatic.Vrfs.Vrf.LabelSwitchedPaths.LabelSwitchedPath.BackupPaths)), ("in-label", ("in_label", MplsStatic.Vrfs.Vrf.LabelSwitchedPaths.LabelSwitchedPath.InLabel)), ("paths", ("paths", MplsStatic.Vrfs.Vrf.LabelSwitchedPaths.LabelSwitchedPath.Paths))])
                        self._leafs = OrderedDict([
                            ('lsp_name', (YLeaf(YType.str, 'lsp-name'), ['str'])),
                            ('enable', (YLeaf(YType.empty, 'enable'), ['Empty'])),
                        ])
                        self.lsp_name = None
                        self.enable = None

                        self.backup_paths = MplsStatic.Vrfs.Vrf.LabelSwitchedPaths.LabelSwitchedPath.BackupPaths()
                        self.backup_paths.parent = self
                        self._children_name_map["backup_paths"] = "backup-paths"

                        self.in_label = MplsStatic.Vrfs.Vrf.LabelSwitchedPaths.LabelSwitchedPath.InLabel()
                        self.in_label.parent = self
                        self._children_name_map["in_label"] = "in-label"

                        self.paths = MplsStatic.Vrfs.Vrf.LabelSwitchedPaths.LabelSwitchedPath.Paths()
                        self.paths.parent = self
                        self._children_name_map["paths"] = "paths"
                        self._segment_path = lambda: "label-switched-path" + "[lsp-name='" + str(self.lsp_name) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(MplsStatic.Vrfs.Vrf.LabelSwitchedPaths.LabelSwitchedPath, ['lsp_name', 'enable'], name, value)


                    class BackupPaths(Entity):
                        """
                        Backup Path Parameters
                        
                        .. attribute:: path
                        
                        	Path Information
                        	**type**\: list of  		 :py:class:`Path <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStatic.Vrfs.Vrf.LabelSwitchedPaths.LabelSwitchedPath.BackupPaths.Path>`
                        
                        

                        """

                        _prefix = 'mpls-static-cfg'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(MplsStatic.Vrfs.Vrf.LabelSwitchedPaths.LabelSwitchedPath.BackupPaths, self).__init__()

                            self.yang_name = "backup-paths"
                            self.yang_parent_name = "label-switched-path"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("path", ("path", MplsStatic.Vrfs.Vrf.LabelSwitchedPaths.LabelSwitchedPath.BackupPaths.Path))])
                            self._leafs = OrderedDict()

                            self.path = YList(self)
                            self._segment_path = lambda: "backup-paths"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(MplsStatic.Vrfs.Vrf.LabelSwitchedPaths.LabelSwitchedPath.BackupPaths, [], name, value)


                        class Path(Entity):
                            """
                            Path Information
                            
                            .. attribute:: path_id  (key)
                            
                            	Number of paths
                            	**type**\: int
                            
                            	**range:** 1..16
                            
                            .. attribute:: path_type
                            
                            	Type of Path (PopAndLookup, CrossConnect)
                            	**type**\:  :py:class:`MplsStaticPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStaticPath>`
                            
                            	**default value**\: cross-connect
                            
                            .. attribute:: label_type
                            
                            	Type of label (Outlabel, ExpNull or Pop)
                            	**type**\:  :py:class:`MplsStaticOutLabelTypes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStaticOutLabelTypes>`
                            
                            	**default value**\: none
                            
                            .. attribute:: next_hop_label
                            
                            	Outgoing/NH Label
                            	**type**\: int
                            
                            	**range:** 16..1048575
                            
                            	**default value**\: 16
                            
                            .. attribute:: next_hop_address
                            
                            	Next Hop IP Address
                            	**type**\: union of the below types:
                            
                            		**type**\: str
                            
                            			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            		**type**\: str
                            
                            			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: interface_name
                            
                            	Next hop Interface with form <Interface>R/S/I/P
                            	**type**\: str
                            
                            	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                            
                            .. attribute:: afi
                            
                            	Next hop Address Family
                            	**type**\:  :py:class:`MplsStaticNhAddressFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStaticNhAddressFamily>`
                            
                            	**default value**\: ipv4
                            
                            .. attribute:: metric
                            
                            	NH Path Metric
                            	**type**\: int
                            
                            	**range:** 0..254
                            
                            	**default value**\: 0
                            
                            .. attribute:: nh_mode
                            
                            	Next hop mode
                            	**type**\:  :py:class:`MplsStaticNhMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStaticNhMode>`
                            
                            	**default value**\: configured
                            
                            .. attribute:: path_role
                            
                            	Path Role
                            	**type**\:  :py:class:`MplsStaticPathRole <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStaticPathRole>`
                            
                            	**default value**\: primary
                            
                            .. attribute:: backup_id
                            
                            	Backup ID
                            	**type**\: int
                            
                            	**range:** 0..16
                            
                            	**default value**\: 0
                            
                            

                            """

                            _prefix = 'mpls-static-cfg'
                            _revision = '2017-09-07'

                            def __init__(self):
                                super(MplsStatic.Vrfs.Vrf.LabelSwitchedPaths.LabelSwitchedPath.BackupPaths.Path, self).__init__()

                                self.yang_name = "path"
                                self.yang_parent_name = "backup-paths"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['path_id']
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('path_id', (YLeaf(YType.uint32, 'path-id'), ['int'])),
                                    ('path_type', (YLeaf(YType.enumeration, 'path-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg', 'MplsStaticPath', '')])),
                                    ('label_type', (YLeaf(YType.enumeration, 'label-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg', 'MplsStaticOutLabelTypes', '')])),
                                    ('next_hop_label', (YLeaf(YType.uint32, 'next-hop-label'), ['int'])),
                                    ('next_hop_address', (YLeaf(YType.str, 'next-hop-address'), ['str','str'])),
                                    ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                                    ('afi', (YLeaf(YType.enumeration, 'afi'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg', 'MplsStaticNhAddressFamily', '')])),
                                    ('metric', (YLeaf(YType.uint32, 'metric'), ['int'])),
                                    ('nh_mode', (YLeaf(YType.enumeration, 'nh-mode'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg', 'MplsStaticNhMode', '')])),
                                    ('path_role', (YLeaf(YType.enumeration, 'path-role'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg', 'MplsStaticPathRole', '')])),
                                    ('backup_id', (YLeaf(YType.uint32, 'backup-id'), ['int'])),
                                ])
                                self.path_id = None
                                self.path_type = None
                                self.label_type = None
                                self.next_hop_label = None
                                self.next_hop_address = None
                                self.interface_name = None
                                self.afi = None
                                self.metric = None
                                self.nh_mode = None
                                self.path_role = None
                                self.backup_id = None
                                self._segment_path = lambda: "path" + "[path-id='" + str(self.path_id) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsStatic.Vrfs.Vrf.LabelSwitchedPaths.LabelSwitchedPath.BackupPaths.Path, ['path_id', 'path_type', 'label_type', 'next_hop_label', 'next_hop_address', 'interface_name', 'afi', 'metric', 'nh_mode', 'path_role', 'backup_id'], name, value)


                    class InLabel(Entity):
                        """
                        MPLS Static Local Label Value
                        
                        .. attribute:: in_label_value
                        
                        	Local Label
                        	**type**\: int
                        
                        	**range:** 16..1048575
                        
                        .. attribute:: label_mode
                        
                        	Label Mode (PerVRF, PerPrefix or LSP)
                        	**type**\:  :py:class:`MplsStaticLabelMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStaticLabelMode>`
                        
                        .. attribute:: prefix
                        
                        	Address (IPv4/6 depending on AFI)
                        	**type**\: union of the below types:
                        
                        		**type**\: str
                        
                        			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        		**type**\: str
                        
                        			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: prefix_length
                        
                        	Prefix length
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: tlh_mode
                        
                        	Top Label Hashing Mode
                        	**type**\: bool
                        
                        

                        """

                        _prefix = 'mpls-static-cfg'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(MplsStatic.Vrfs.Vrf.LabelSwitchedPaths.LabelSwitchedPath.InLabel, self).__init__()

                            self.yang_name = "in-label"
                            self.yang_parent_name = "label-switched-path"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('in_label_value', (YLeaf(YType.uint32, 'in-label-value'), ['int'])),
                                ('label_mode', (YLeaf(YType.enumeration, 'label-mode'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg', 'MplsStaticLabelMode', '')])),
                                ('prefix', (YLeaf(YType.str, 'prefix'), ['str','str'])),
                                ('prefix_length', (YLeaf(YType.uint32, 'prefix-length'), ['int'])),
                                ('tlh_mode', (YLeaf(YType.boolean, 'tlh-mode'), ['bool'])),
                            ])
                            self.in_label_value = None
                            self.label_mode = None
                            self.prefix = None
                            self.prefix_length = None
                            self.tlh_mode = None
                            self._segment_path = lambda: "in-label"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(MplsStatic.Vrfs.Vrf.LabelSwitchedPaths.LabelSwitchedPath.InLabel, ['in_label_value', 'label_mode', 'prefix', 'prefix_length', 'tlh_mode'], name, value)


                    class Paths(Entity):
                        """
                        Forward Path Parameters
                        
                        .. attribute:: path
                        
                        	Path Information
                        	**type**\: list of  		 :py:class:`Path <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStatic.Vrfs.Vrf.LabelSwitchedPaths.LabelSwitchedPath.Paths.Path>`
                        
                        

                        """

                        _prefix = 'mpls-static-cfg'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(MplsStatic.Vrfs.Vrf.LabelSwitchedPaths.LabelSwitchedPath.Paths, self).__init__()

                            self.yang_name = "paths"
                            self.yang_parent_name = "label-switched-path"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("path", ("path", MplsStatic.Vrfs.Vrf.LabelSwitchedPaths.LabelSwitchedPath.Paths.Path))])
                            self._leafs = OrderedDict()

                            self.path = YList(self)
                            self._segment_path = lambda: "paths"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(MplsStatic.Vrfs.Vrf.LabelSwitchedPaths.LabelSwitchedPath.Paths, [], name, value)


                        class Path(Entity):
                            """
                            Path Information
                            
                            .. attribute:: path_id  (key)
                            
                            	Number of paths
                            	**type**\: int
                            
                            	**range:** 1..16
                            
                            .. attribute:: path_type
                            
                            	Type of Path (PopAndLookup, CrossConnect)
                            	**type**\:  :py:class:`MplsStaticPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStaticPath>`
                            
                            	**default value**\: cross-connect
                            
                            .. attribute:: label_type
                            
                            	Type of label (Outlabel, ExpNull or Pop)
                            	**type**\:  :py:class:`MplsStaticOutLabelTypes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStaticOutLabelTypes>`
                            
                            	**default value**\: none
                            
                            .. attribute:: next_hop_label
                            
                            	Outgoing/NH Label
                            	**type**\: int
                            
                            	**range:** 16..1048575
                            
                            	**default value**\: 16
                            
                            .. attribute:: next_hop_address
                            
                            	Next Hop IP Address
                            	**type**\: union of the below types:
                            
                            		**type**\: str
                            
                            			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            		**type**\: str
                            
                            			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: interface_name
                            
                            	Next hop Interface with form <Interface>R/S/I/P
                            	**type**\: str
                            
                            	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                            
                            .. attribute:: afi
                            
                            	Next hop Address Family
                            	**type**\:  :py:class:`MplsStaticNhAddressFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStaticNhAddressFamily>`
                            
                            	**default value**\: ipv4
                            
                            .. attribute:: metric
                            
                            	NH Path Metric
                            	**type**\: int
                            
                            	**range:** 0..254
                            
                            	**default value**\: 0
                            
                            .. attribute:: nh_mode
                            
                            	Next hop mode
                            	**type**\:  :py:class:`MplsStaticNhMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStaticNhMode>`
                            
                            	**default value**\: configured
                            
                            .. attribute:: path_role
                            
                            	Path Role
                            	**type**\:  :py:class:`MplsStaticPathRole <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStaticPathRole>`
                            
                            	**default value**\: primary
                            
                            .. attribute:: backup_id
                            
                            	Backup ID
                            	**type**\: int
                            
                            	**range:** 0..16
                            
                            	**default value**\: 0
                            
                            

                            """

                            _prefix = 'mpls-static-cfg'
                            _revision = '2017-09-07'

                            def __init__(self):
                                super(MplsStatic.Vrfs.Vrf.LabelSwitchedPaths.LabelSwitchedPath.Paths.Path, self).__init__()

                                self.yang_name = "path"
                                self.yang_parent_name = "paths"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['path_id']
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('path_id', (YLeaf(YType.uint32, 'path-id'), ['int'])),
                                    ('path_type', (YLeaf(YType.enumeration, 'path-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg', 'MplsStaticPath', '')])),
                                    ('label_type', (YLeaf(YType.enumeration, 'label-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg', 'MplsStaticOutLabelTypes', '')])),
                                    ('next_hop_label', (YLeaf(YType.uint32, 'next-hop-label'), ['int'])),
                                    ('next_hop_address', (YLeaf(YType.str, 'next-hop-address'), ['str','str'])),
                                    ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                                    ('afi', (YLeaf(YType.enumeration, 'afi'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg', 'MplsStaticNhAddressFamily', '')])),
                                    ('metric', (YLeaf(YType.uint32, 'metric'), ['int'])),
                                    ('nh_mode', (YLeaf(YType.enumeration, 'nh-mode'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg', 'MplsStaticNhMode', '')])),
                                    ('path_role', (YLeaf(YType.enumeration, 'path-role'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg', 'MplsStaticPathRole', '')])),
                                    ('backup_id', (YLeaf(YType.uint32, 'backup-id'), ['int'])),
                                ])
                                self.path_id = None
                                self.path_type = None
                                self.label_type = None
                                self.next_hop_label = None
                                self.next_hop_address = None
                                self.interface_name = None
                                self.afi = None
                                self.metric = None
                                self.nh_mode = None
                                self.path_role = None
                                self.backup_id = None
                                self._segment_path = lambda: "path" + "[path-id='" + str(self.path_id) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsStatic.Vrfs.Vrf.LabelSwitchedPaths.LabelSwitchedPath.Paths.Path, ['path_id', 'path_type', 'label_type', 'next_hop_label', 'next_hop_address', 'interface_name', 'afi', 'metric', 'nh_mode', 'path_role', 'backup_id'], name, value)


            class Afs(Entity):
                """
                Address Family Table
                
                .. attribute:: af
                
                	Address Family
                	**type**\: list of  		 :py:class:`Af <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStatic.Vrfs.Vrf.Afs.Af>`
                
                

                """

                _prefix = 'mpls-static-cfg'
                _revision = '2017-09-07'

                def __init__(self):
                    super(MplsStatic.Vrfs.Vrf.Afs, self).__init__()

                    self.yang_name = "afs"
                    self.yang_parent_name = "vrf"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("af", ("af", MplsStatic.Vrfs.Vrf.Afs.Af))])
                    self._leafs = OrderedDict()

                    self.af = YList(self)
                    self._segment_path = lambda: "afs"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsStatic.Vrfs.Vrf.Afs, [], name, value)


                class Af(Entity):
                    """
                    Address Family
                    
                    .. attribute:: afi  (key)
                    
                    	Address Family
                    	**type**\:  :py:class:`MplsStaticAddressFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStaticAddressFamily>`
                    
                    .. attribute:: top_label_hash
                    
                    	Top Label Hash
                    	**type**\:  :py:class:`TopLabelHash <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStatic.Vrfs.Vrf.Afs.Af.TopLabelHash>`
                    
                    .. attribute:: local_labels
                    
                    	Local Label
                    	**type**\:  :py:class:`LocalLabels <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStatic.Vrfs.Vrf.Afs.Af.LocalLabels>`
                    
                    .. attribute:: enable
                    
                    	MPLS Static Apply Enable
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    

                    """

                    _prefix = 'mpls-static-cfg'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(MplsStatic.Vrfs.Vrf.Afs.Af, self).__init__()

                        self.yang_name = "af"
                        self.yang_parent_name = "afs"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['afi']
                        self._child_classes = OrderedDict([("top-label-hash", ("top_label_hash", MplsStatic.Vrfs.Vrf.Afs.Af.TopLabelHash)), ("local-labels", ("local_labels", MplsStatic.Vrfs.Vrf.Afs.Af.LocalLabels))])
                        self._leafs = OrderedDict([
                            ('afi', (YLeaf(YType.enumeration, 'afi'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg', 'MplsStaticAddressFamily', '')])),
                            ('enable', (YLeaf(YType.empty, 'enable'), ['Empty'])),
                        ])
                        self.afi = None
                        self.enable = None

                        self.top_label_hash = MplsStatic.Vrfs.Vrf.Afs.Af.TopLabelHash()
                        self.top_label_hash.parent = self
                        self._children_name_map["top_label_hash"] = "top-label-hash"

                        self.local_labels = MplsStatic.Vrfs.Vrf.Afs.Af.LocalLabels()
                        self.local_labels.parent = self
                        self._children_name_map["local_labels"] = "local-labels"
                        self._segment_path = lambda: "af" + "[afi='" + str(self.afi) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(MplsStatic.Vrfs.Vrf.Afs.Af, ['afi', 'enable'], name, value)


                    class TopLabelHash(Entity):
                        """
                        Top Label Hash
                        
                        .. attribute:: local_labels
                        
                        	Local Label
                        	**type**\:  :py:class:`LocalLabels <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStatic.Vrfs.Vrf.Afs.Af.TopLabelHash.LocalLabels>`
                        
                        

                        """

                        _prefix = 'mpls-static-cfg'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(MplsStatic.Vrfs.Vrf.Afs.Af.TopLabelHash, self).__init__()

                            self.yang_name = "top-label-hash"
                            self.yang_parent_name = "af"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("local-labels", ("local_labels", MplsStatic.Vrfs.Vrf.Afs.Af.TopLabelHash.LocalLabels))])
                            self._leafs = OrderedDict()

                            self.local_labels = MplsStatic.Vrfs.Vrf.Afs.Af.TopLabelHash.LocalLabels()
                            self.local_labels.parent = self
                            self._children_name_map["local_labels"] = "local-labels"
                            self._segment_path = lambda: "top-label-hash"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(MplsStatic.Vrfs.Vrf.Afs.Af.TopLabelHash, [], name, value)


                        class LocalLabels(Entity):
                            """
                            Local Label
                            
                            .. attribute:: local_label
                            
                            	Specify Local Label
                            	**type**\: list of  		 :py:class:`LocalLabel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStatic.Vrfs.Vrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel>`
                            
                            

                            """

                            _prefix = 'mpls-static-cfg'
                            _revision = '2017-09-07'

                            def __init__(self):
                                super(MplsStatic.Vrfs.Vrf.Afs.Af.TopLabelHash.LocalLabels, self).__init__()

                                self.yang_name = "local-labels"
                                self.yang_parent_name = "top-label-hash"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("local-label", ("local_label", MplsStatic.Vrfs.Vrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel))])
                                self._leafs = OrderedDict()

                                self.local_label = YList(self)
                                self._segment_path = lambda: "local-labels"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsStatic.Vrfs.Vrf.Afs.Af.TopLabelHash.LocalLabels, [], name, value)


                            class LocalLabel(Entity):
                                """
                                Specify Local Label
                                
                                .. attribute:: local_label_id  (key)
                                
                                	Local Label
                                	**type**\: int
                                
                                	**range:** 16..1048575
                                
                                .. attribute:: label_type
                                
                                	MPLS Static Local Label Value
                                	**type**\:  :py:class:`LabelType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStatic.Vrfs.Vrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel.LabelType>`
                                
                                .. attribute:: paths
                                
                                	Forward Path Parameters
                                	**type**\:  :py:class:`Paths <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStatic.Vrfs.Vrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel.Paths>`
                                
                                

                                """

                                _prefix = 'mpls-static-cfg'
                                _revision = '2017-09-07'

                                def __init__(self):
                                    super(MplsStatic.Vrfs.Vrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel, self).__init__()

                                    self.yang_name = "local-label"
                                    self.yang_parent_name = "local-labels"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['local_label_id']
                                    self._child_classes = OrderedDict([("label-type", ("label_type", MplsStatic.Vrfs.Vrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel.LabelType)), ("paths", ("paths", MplsStatic.Vrfs.Vrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel.Paths))])
                                    self._leafs = OrderedDict([
                                        ('local_label_id', (YLeaf(YType.uint32, 'local-label-id'), ['int'])),
                                    ])
                                    self.local_label_id = None

                                    self.label_type = MplsStatic.Vrfs.Vrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel.LabelType()
                                    self.label_type.parent = self
                                    self._children_name_map["label_type"] = "label-type"

                                    self.paths = MplsStatic.Vrfs.Vrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel.Paths()
                                    self.paths.parent = self
                                    self._children_name_map["paths"] = "paths"
                                    self._segment_path = lambda: "local-label" + "[local-label-id='" + str(self.local_label_id) + "']"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(MplsStatic.Vrfs.Vrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel, ['local_label_id'], name, value)


                                class LabelType(Entity):
                                    """
                                    MPLS Static Local Label Value
                                    
                                    .. attribute:: label_mode
                                    
                                    	Label Mode (PerVRF, PerPrefix or LSP)
                                    	**type**\:  :py:class:`MplsStaticLabelMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStaticLabelMode>`
                                    
                                    .. attribute:: prefix
                                    
                                    	Address (IPv4/6 depending on AFI)
                                    	**type**\: union of the below types:
                                    
                                    		**type**\: str
                                    
                                    			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    		**type**\: str
                                    
                                    			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                    
                                    .. attribute:: prefix_length
                                    
                                    	Prefix length
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'mpls-static-cfg'
                                    _revision = '2017-09-07'

                                    def __init__(self):
                                        super(MplsStatic.Vrfs.Vrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel.LabelType, self).__init__()

                                        self.yang_name = "label-type"
                                        self.yang_parent_name = "local-label"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('label_mode', (YLeaf(YType.enumeration, 'label-mode'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg', 'MplsStaticLabelMode', '')])),
                                            ('prefix', (YLeaf(YType.str, 'prefix'), ['str','str'])),
                                            ('prefix_length', (YLeaf(YType.uint32, 'prefix-length'), ['int'])),
                                        ])
                                        self.label_mode = None
                                        self.prefix = None
                                        self.prefix_length = None
                                        self._segment_path = lambda: "label-type"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(MplsStatic.Vrfs.Vrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel.LabelType, ['label_mode', 'prefix', 'prefix_length'], name, value)


                                class Paths(Entity):
                                    """
                                    Forward Path Parameters
                                    
                                    .. attribute:: path
                                    
                                    	Path Information
                                    	**type**\: list of  		 :py:class:`Path <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStatic.Vrfs.Vrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel.Paths.Path>`
                                    
                                    

                                    """

                                    _prefix = 'mpls-static-cfg'
                                    _revision = '2017-09-07'

                                    def __init__(self):
                                        super(MplsStatic.Vrfs.Vrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel.Paths, self).__init__()

                                        self.yang_name = "paths"
                                        self.yang_parent_name = "local-label"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("path", ("path", MplsStatic.Vrfs.Vrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel.Paths.Path))])
                                        self._leafs = OrderedDict()

                                        self.path = YList(self)
                                        self._segment_path = lambda: "paths"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(MplsStatic.Vrfs.Vrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel.Paths, [], name, value)


                                    class Path(Entity):
                                        """
                                        Path Information
                                        
                                        .. attribute:: path_id  (key)
                                        
                                        	Number of paths
                                        	**type**\: int
                                        
                                        	**range:** 1..16
                                        
                                        .. attribute:: path_type
                                        
                                        	Type of Path (PopAndLookup, CrossConnect)
                                        	**type**\:  :py:class:`MplsStaticPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStaticPath>`
                                        
                                        	**default value**\: cross-connect
                                        
                                        .. attribute:: label_type
                                        
                                        	Type of label (Outlabel, ExpNull or Pop)
                                        	**type**\:  :py:class:`MplsStaticOutLabelTypes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStaticOutLabelTypes>`
                                        
                                        	**default value**\: none
                                        
                                        .. attribute:: next_hop_label
                                        
                                        	Outgoing/NH Label
                                        	**type**\: int
                                        
                                        	**range:** 16..1048575
                                        
                                        	**default value**\: 16
                                        
                                        .. attribute:: next_hop_address
                                        
                                        	Next Hop IP Address
                                        	**type**\: union of the below types:
                                        
                                        		**type**\: str
                                        
                                        			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                        
                                        		**type**\: str
                                        
                                        			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                        
                                        .. attribute:: interface_name
                                        
                                        	Next hop Interface with form <Interface>R/S/I/P
                                        	**type**\: str
                                        
                                        	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                                        
                                        .. attribute:: afi
                                        
                                        	Next hop Address Family
                                        	**type**\:  :py:class:`MplsStaticNhAddressFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStaticNhAddressFamily>`
                                        
                                        	**default value**\: ipv4
                                        
                                        .. attribute:: metric
                                        
                                        	NH Path Metric
                                        	**type**\: int
                                        
                                        	**range:** 0..254
                                        
                                        	**default value**\: 0
                                        
                                        .. attribute:: nh_mode
                                        
                                        	Next hop mode
                                        	**type**\:  :py:class:`MplsStaticNhMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStaticNhMode>`
                                        
                                        	**default value**\: configured
                                        
                                        .. attribute:: path_role
                                        
                                        	Path Role
                                        	**type**\:  :py:class:`MplsStaticPathRole <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStaticPathRole>`
                                        
                                        	**default value**\: primary
                                        
                                        .. attribute:: backup_id
                                        
                                        	Backup ID
                                        	**type**\: int
                                        
                                        	**range:** 0..16
                                        
                                        	**default value**\: 0
                                        
                                        

                                        """

                                        _prefix = 'mpls-static-cfg'
                                        _revision = '2017-09-07'

                                        def __init__(self):
                                            super(MplsStatic.Vrfs.Vrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel.Paths.Path, self).__init__()

                                            self.yang_name = "path"
                                            self.yang_parent_name = "paths"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = ['path_id']
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('path_id', (YLeaf(YType.uint32, 'path-id'), ['int'])),
                                                ('path_type', (YLeaf(YType.enumeration, 'path-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg', 'MplsStaticPath', '')])),
                                                ('label_type', (YLeaf(YType.enumeration, 'label-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg', 'MplsStaticOutLabelTypes', '')])),
                                                ('next_hop_label', (YLeaf(YType.uint32, 'next-hop-label'), ['int'])),
                                                ('next_hop_address', (YLeaf(YType.str, 'next-hop-address'), ['str','str'])),
                                                ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                                                ('afi', (YLeaf(YType.enumeration, 'afi'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg', 'MplsStaticNhAddressFamily', '')])),
                                                ('metric', (YLeaf(YType.uint32, 'metric'), ['int'])),
                                                ('nh_mode', (YLeaf(YType.enumeration, 'nh-mode'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg', 'MplsStaticNhMode', '')])),
                                                ('path_role', (YLeaf(YType.enumeration, 'path-role'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg', 'MplsStaticPathRole', '')])),
                                                ('backup_id', (YLeaf(YType.uint32, 'backup-id'), ['int'])),
                                            ])
                                            self.path_id = None
                                            self.path_type = None
                                            self.label_type = None
                                            self.next_hop_label = None
                                            self.next_hop_address = None
                                            self.interface_name = None
                                            self.afi = None
                                            self.metric = None
                                            self.nh_mode = None
                                            self.path_role = None
                                            self.backup_id = None
                                            self._segment_path = lambda: "path" + "[path-id='" + str(self.path_id) + "']"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(MplsStatic.Vrfs.Vrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel.Paths.Path, ['path_id', 'path_type', 'label_type', 'next_hop_label', 'next_hop_address', 'interface_name', 'afi', 'metric', 'nh_mode', 'path_role', 'backup_id'], name, value)


                    class LocalLabels(Entity):
                        """
                        Local Label
                        
                        .. attribute:: local_label
                        
                        	Specify Local Label
                        	**type**\: list of  		 :py:class:`LocalLabel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStatic.Vrfs.Vrf.Afs.Af.LocalLabels.LocalLabel>`
                        
                        

                        """

                        _prefix = 'mpls-static-cfg'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(MplsStatic.Vrfs.Vrf.Afs.Af.LocalLabels, self).__init__()

                            self.yang_name = "local-labels"
                            self.yang_parent_name = "af"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("local-label", ("local_label", MplsStatic.Vrfs.Vrf.Afs.Af.LocalLabels.LocalLabel))])
                            self._leafs = OrderedDict()

                            self.local_label = YList(self)
                            self._segment_path = lambda: "local-labels"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(MplsStatic.Vrfs.Vrf.Afs.Af.LocalLabels, [], name, value)


                        class LocalLabel(Entity):
                            """
                            Specify Local Label
                            
                            .. attribute:: local_label_id  (key)
                            
                            	Local Label
                            	**type**\: int
                            
                            	**range:** 16..1048575
                            
                            .. attribute:: label_type
                            
                            	MPLS Static Local Label Value
                            	**type**\:  :py:class:`LabelType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStatic.Vrfs.Vrf.Afs.Af.LocalLabels.LocalLabel.LabelType>`
                            
                            .. attribute:: paths
                            
                            	Forward Path Parameters
                            	**type**\:  :py:class:`Paths <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStatic.Vrfs.Vrf.Afs.Af.LocalLabels.LocalLabel.Paths>`
                            
                            

                            """

                            _prefix = 'mpls-static-cfg'
                            _revision = '2017-09-07'

                            def __init__(self):
                                super(MplsStatic.Vrfs.Vrf.Afs.Af.LocalLabels.LocalLabel, self).__init__()

                                self.yang_name = "local-label"
                                self.yang_parent_name = "local-labels"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['local_label_id']
                                self._child_classes = OrderedDict([("label-type", ("label_type", MplsStatic.Vrfs.Vrf.Afs.Af.LocalLabels.LocalLabel.LabelType)), ("paths", ("paths", MplsStatic.Vrfs.Vrf.Afs.Af.LocalLabels.LocalLabel.Paths))])
                                self._leafs = OrderedDict([
                                    ('local_label_id', (YLeaf(YType.uint32, 'local-label-id'), ['int'])),
                                ])
                                self.local_label_id = None

                                self.label_type = MplsStatic.Vrfs.Vrf.Afs.Af.LocalLabels.LocalLabel.LabelType()
                                self.label_type.parent = self
                                self._children_name_map["label_type"] = "label-type"

                                self.paths = MplsStatic.Vrfs.Vrf.Afs.Af.LocalLabels.LocalLabel.Paths()
                                self.paths.parent = self
                                self._children_name_map["paths"] = "paths"
                                self._segment_path = lambda: "local-label" + "[local-label-id='" + str(self.local_label_id) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsStatic.Vrfs.Vrf.Afs.Af.LocalLabels.LocalLabel, ['local_label_id'], name, value)


                            class LabelType(Entity):
                                """
                                MPLS Static Local Label Value
                                
                                .. attribute:: label_mode
                                
                                	Label Mode (PerVRF, PerPrefix or LSP)
                                	**type**\:  :py:class:`MplsStaticLabelMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStaticLabelMode>`
                                
                                .. attribute:: prefix
                                
                                	Address (IPv4/6 depending on AFI)
                                	**type**\: union of the below types:
                                
                                		**type**\: str
                                
                                			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                		**type**\: str
                                
                                			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: prefix_length
                                
                                	Prefix length
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'mpls-static-cfg'
                                _revision = '2017-09-07'

                                def __init__(self):
                                    super(MplsStatic.Vrfs.Vrf.Afs.Af.LocalLabels.LocalLabel.LabelType, self).__init__()

                                    self.yang_name = "label-type"
                                    self.yang_parent_name = "local-label"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('label_mode', (YLeaf(YType.enumeration, 'label-mode'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg', 'MplsStaticLabelMode', '')])),
                                        ('prefix', (YLeaf(YType.str, 'prefix'), ['str','str'])),
                                        ('prefix_length', (YLeaf(YType.uint32, 'prefix-length'), ['int'])),
                                    ])
                                    self.label_mode = None
                                    self.prefix = None
                                    self.prefix_length = None
                                    self._segment_path = lambda: "label-type"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(MplsStatic.Vrfs.Vrf.Afs.Af.LocalLabels.LocalLabel.LabelType, ['label_mode', 'prefix', 'prefix_length'], name, value)


                            class Paths(Entity):
                                """
                                Forward Path Parameters
                                
                                .. attribute:: path
                                
                                	Path Information
                                	**type**\: list of  		 :py:class:`Path <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStatic.Vrfs.Vrf.Afs.Af.LocalLabels.LocalLabel.Paths.Path>`
                                
                                

                                """

                                _prefix = 'mpls-static-cfg'
                                _revision = '2017-09-07'

                                def __init__(self):
                                    super(MplsStatic.Vrfs.Vrf.Afs.Af.LocalLabels.LocalLabel.Paths, self).__init__()

                                    self.yang_name = "paths"
                                    self.yang_parent_name = "local-label"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("path", ("path", MplsStatic.Vrfs.Vrf.Afs.Af.LocalLabels.LocalLabel.Paths.Path))])
                                    self._leafs = OrderedDict()

                                    self.path = YList(self)
                                    self._segment_path = lambda: "paths"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(MplsStatic.Vrfs.Vrf.Afs.Af.LocalLabels.LocalLabel.Paths, [], name, value)


                                class Path(Entity):
                                    """
                                    Path Information
                                    
                                    .. attribute:: path_id  (key)
                                    
                                    	Number of paths
                                    	**type**\: int
                                    
                                    	**range:** 1..16
                                    
                                    .. attribute:: path_type
                                    
                                    	Type of Path (PopAndLookup, CrossConnect)
                                    	**type**\:  :py:class:`MplsStaticPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStaticPath>`
                                    
                                    	**default value**\: cross-connect
                                    
                                    .. attribute:: label_type
                                    
                                    	Type of label (Outlabel, ExpNull or Pop)
                                    	**type**\:  :py:class:`MplsStaticOutLabelTypes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStaticOutLabelTypes>`
                                    
                                    	**default value**\: none
                                    
                                    .. attribute:: next_hop_label
                                    
                                    	Outgoing/NH Label
                                    	**type**\: int
                                    
                                    	**range:** 16..1048575
                                    
                                    	**default value**\: 16
                                    
                                    .. attribute:: next_hop_address
                                    
                                    	Next Hop IP Address
                                    	**type**\: union of the below types:
                                    
                                    		**type**\: str
                                    
                                    			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    		**type**\: str
                                    
                                    			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                    
                                    .. attribute:: interface_name
                                    
                                    	Next hop Interface with form <Interface>R/S/I/P
                                    	**type**\: str
                                    
                                    	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                                    
                                    .. attribute:: afi
                                    
                                    	Next hop Address Family
                                    	**type**\:  :py:class:`MplsStaticNhAddressFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStaticNhAddressFamily>`
                                    
                                    	**default value**\: ipv4
                                    
                                    .. attribute:: metric
                                    
                                    	NH Path Metric
                                    	**type**\: int
                                    
                                    	**range:** 0..254
                                    
                                    	**default value**\: 0
                                    
                                    .. attribute:: nh_mode
                                    
                                    	Next hop mode
                                    	**type**\:  :py:class:`MplsStaticNhMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStaticNhMode>`
                                    
                                    	**default value**\: configured
                                    
                                    .. attribute:: path_role
                                    
                                    	Path Role
                                    	**type**\:  :py:class:`MplsStaticPathRole <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStaticPathRole>`
                                    
                                    	**default value**\: primary
                                    
                                    .. attribute:: backup_id
                                    
                                    	Backup ID
                                    	**type**\: int
                                    
                                    	**range:** 0..16
                                    
                                    	**default value**\: 0
                                    
                                    

                                    """

                                    _prefix = 'mpls-static-cfg'
                                    _revision = '2017-09-07'

                                    def __init__(self):
                                        super(MplsStatic.Vrfs.Vrf.Afs.Af.LocalLabels.LocalLabel.Paths.Path, self).__init__()

                                        self.yang_name = "path"
                                        self.yang_parent_name = "paths"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = ['path_id']
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('path_id', (YLeaf(YType.uint32, 'path-id'), ['int'])),
                                            ('path_type', (YLeaf(YType.enumeration, 'path-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg', 'MplsStaticPath', '')])),
                                            ('label_type', (YLeaf(YType.enumeration, 'label-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg', 'MplsStaticOutLabelTypes', '')])),
                                            ('next_hop_label', (YLeaf(YType.uint32, 'next-hop-label'), ['int'])),
                                            ('next_hop_address', (YLeaf(YType.str, 'next-hop-address'), ['str','str'])),
                                            ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                                            ('afi', (YLeaf(YType.enumeration, 'afi'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg', 'MplsStaticNhAddressFamily', '')])),
                                            ('metric', (YLeaf(YType.uint32, 'metric'), ['int'])),
                                            ('nh_mode', (YLeaf(YType.enumeration, 'nh-mode'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg', 'MplsStaticNhMode', '')])),
                                            ('path_role', (YLeaf(YType.enumeration, 'path-role'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg', 'MplsStaticPathRole', '')])),
                                            ('backup_id', (YLeaf(YType.uint32, 'backup-id'), ['int'])),
                                        ])
                                        self.path_id = None
                                        self.path_type = None
                                        self.label_type = None
                                        self.next_hop_label = None
                                        self.next_hop_address = None
                                        self.interface_name = None
                                        self.afi = None
                                        self.metric = None
                                        self.nh_mode = None
                                        self.path_role = None
                                        self.backup_id = None
                                        self._segment_path = lambda: "path" + "[path-id='" + str(self.path_id) + "']"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(MplsStatic.Vrfs.Vrf.Afs.Af.LocalLabels.LocalLabel.Paths.Path, ['path_id', 'path_type', 'label_type', 'next_hop_label', 'next_hop_address', 'interface_name', 'afi', 'metric', 'nh_mode', 'path_role', 'backup_id'], name, value)


    class Interfaces(Entity):
        """
        MPLS Static Interface Table
        
        .. attribute:: interface
        
        	MPLS Static Interface Enable
        	**type**\: list of  		 :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStatic.Interfaces.Interface>`
        
        

        """

        _prefix = 'mpls-static-cfg'
        _revision = '2017-09-07'

        def __init__(self):
            super(MplsStatic.Interfaces, self).__init__()

            self.yang_name = "interfaces"
            self.yang_parent_name = "mpls-static"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("interface", ("interface", MplsStatic.Interfaces.Interface))])
            self._leafs = OrderedDict()

            self.interface = YList(self)
            self._segment_path = lambda: "interfaces"
            self._absolute_path = lambda: "Cisco-IOS-XR-mpls-static-cfg:mpls-static/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(MplsStatic.Interfaces, [], name, value)


        class Interface(Entity):
            """
            MPLS Static Interface Enable
            
            .. attribute:: interface_name  (key)
            
            	Name of Interface
            	**type**\: str
            
            	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
            
            

            """

            _prefix = 'mpls-static-cfg'
            _revision = '2017-09-07'

            def __init__(self):
                super(MplsStatic.Interfaces.Interface, self).__init__()

                self.yang_name = "interface"
                self.yang_parent_name = "interfaces"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['interface_name']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                ])
                self.interface_name = None
                self._segment_path = lambda: "interface" + "[interface-name='" + str(self.interface_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-mpls-static-cfg:mpls-static/interfaces/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(MplsStatic.Interfaces.Interface, ['interface_name'], name, value)


    class DefaultVrf(Entity):
        """
        Default VRF
        
        .. attribute:: label_switched_paths
        
        	Table of the Label Switched Paths
        	**type**\:  :py:class:`LabelSwitchedPaths <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStatic.DefaultVrf.LabelSwitchedPaths>`
        
        .. attribute:: afs
        
        	Address Family Table
        	**type**\:  :py:class:`Afs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStatic.DefaultVrf.Afs>`
        
        .. attribute:: enable
        
        	MPLS Static Apply Enable
        	**type**\: :py:class:`Empty<ydk.types.Empty>`
        
        

        """

        _prefix = 'mpls-static-cfg'
        _revision = '2017-09-07'

        def __init__(self):
            super(MplsStatic.DefaultVrf, self).__init__()

            self.yang_name = "default-vrf"
            self.yang_parent_name = "mpls-static"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("label-switched-paths", ("label_switched_paths", MplsStatic.DefaultVrf.LabelSwitchedPaths)), ("afs", ("afs", MplsStatic.DefaultVrf.Afs))])
            self._leafs = OrderedDict([
                ('enable', (YLeaf(YType.empty, 'enable'), ['Empty'])),
            ])
            self.enable = None

            self.label_switched_paths = MplsStatic.DefaultVrf.LabelSwitchedPaths()
            self.label_switched_paths.parent = self
            self._children_name_map["label_switched_paths"] = "label-switched-paths"

            self.afs = MplsStatic.DefaultVrf.Afs()
            self.afs.parent = self
            self._children_name_map["afs"] = "afs"
            self._segment_path = lambda: "default-vrf"
            self._absolute_path = lambda: "Cisco-IOS-XR-mpls-static-cfg:mpls-static/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(MplsStatic.DefaultVrf, ['enable'], name, value)


        class LabelSwitchedPaths(Entity):
            """
            Table of the Label Switched Paths
            
            .. attribute:: label_switched_path
            
            	Label Switched Path
            	**type**\: list of  		 :py:class:`LabelSwitchedPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStatic.DefaultVrf.LabelSwitchedPaths.LabelSwitchedPath>`
            
            

            """

            _prefix = 'mpls-static-cfg'
            _revision = '2017-09-07'

            def __init__(self):
                super(MplsStatic.DefaultVrf.LabelSwitchedPaths, self).__init__()

                self.yang_name = "label-switched-paths"
                self.yang_parent_name = "default-vrf"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("label-switched-path", ("label_switched_path", MplsStatic.DefaultVrf.LabelSwitchedPaths.LabelSwitchedPath))])
                self._leafs = OrderedDict()

                self.label_switched_path = YList(self)
                self._segment_path = lambda: "label-switched-paths"
                self._absolute_path = lambda: "Cisco-IOS-XR-mpls-static-cfg:mpls-static/default-vrf/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(MplsStatic.DefaultVrf.LabelSwitchedPaths, [], name, value)


            class LabelSwitchedPath(Entity):
                """
                Label Switched Path
                
                .. attribute:: lsp_name  (key)
                
                	LSP Name
                	**type**\: str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: backup_paths
                
                	Backup Path Parameters
                	**type**\:  :py:class:`BackupPaths <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStatic.DefaultVrf.LabelSwitchedPaths.LabelSwitchedPath.BackupPaths>`
                
                .. attribute:: in_label
                
                	MPLS Static Local Label Value
                	**type**\:  :py:class:`InLabel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStatic.DefaultVrf.LabelSwitchedPaths.LabelSwitchedPath.InLabel>`
                
                .. attribute:: enable
                
                	MPLS Static Apply Enable
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: paths
                
                	Forward Path Parameters
                	**type**\:  :py:class:`Paths <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStatic.DefaultVrf.LabelSwitchedPaths.LabelSwitchedPath.Paths>`
                
                

                """

                _prefix = 'mpls-static-cfg'
                _revision = '2017-09-07'

                def __init__(self):
                    super(MplsStatic.DefaultVrf.LabelSwitchedPaths.LabelSwitchedPath, self).__init__()

                    self.yang_name = "label-switched-path"
                    self.yang_parent_name = "label-switched-paths"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['lsp_name']
                    self._child_classes = OrderedDict([("backup-paths", ("backup_paths", MplsStatic.DefaultVrf.LabelSwitchedPaths.LabelSwitchedPath.BackupPaths)), ("in-label", ("in_label", MplsStatic.DefaultVrf.LabelSwitchedPaths.LabelSwitchedPath.InLabel)), ("paths", ("paths", MplsStatic.DefaultVrf.LabelSwitchedPaths.LabelSwitchedPath.Paths))])
                    self._leafs = OrderedDict([
                        ('lsp_name', (YLeaf(YType.str, 'lsp-name'), ['str'])),
                        ('enable', (YLeaf(YType.empty, 'enable'), ['Empty'])),
                    ])
                    self.lsp_name = None
                    self.enable = None

                    self.backup_paths = MplsStatic.DefaultVrf.LabelSwitchedPaths.LabelSwitchedPath.BackupPaths()
                    self.backup_paths.parent = self
                    self._children_name_map["backup_paths"] = "backup-paths"

                    self.in_label = MplsStatic.DefaultVrf.LabelSwitchedPaths.LabelSwitchedPath.InLabel()
                    self.in_label.parent = self
                    self._children_name_map["in_label"] = "in-label"

                    self.paths = MplsStatic.DefaultVrf.LabelSwitchedPaths.LabelSwitchedPath.Paths()
                    self.paths.parent = self
                    self._children_name_map["paths"] = "paths"
                    self._segment_path = lambda: "label-switched-path" + "[lsp-name='" + str(self.lsp_name) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-mpls-static-cfg:mpls-static/default-vrf/label-switched-paths/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsStatic.DefaultVrf.LabelSwitchedPaths.LabelSwitchedPath, ['lsp_name', 'enable'], name, value)


                class BackupPaths(Entity):
                    """
                    Backup Path Parameters
                    
                    .. attribute:: path
                    
                    	Path Information
                    	**type**\: list of  		 :py:class:`Path <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStatic.DefaultVrf.LabelSwitchedPaths.LabelSwitchedPath.BackupPaths.Path>`
                    
                    

                    """

                    _prefix = 'mpls-static-cfg'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(MplsStatic.DefaultVrf.LabelSwitchedPaths.LabelSwitchedPath.BackupPaths, self).__init__()

                        self.yang_name = "backup-paths"
                        self.yang_parent_name = "label-switched-path"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("path", ("path", MplsStatic.DefaultVrf.LabelSwitchedPaths.LabelSwitchedPath.BackupPaths.Path))])
                        self._leafs = OrderedDict()

                        self.path = YList(self)
                        self._segment_path = lambda: "backup-paths"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(MplsStatic.DefaultVrf.LabelSwitchedPaths.LabelSwitchedPath.BackupPaths, [], name, value)


                    class Path(Entity):
                        """
                        Path Information
                        
                        .. attribute:: path_id  (key)
                        
                        	Number of paths
                        	**type**\: int
                        
                        	**range:** 1..16
                        
                        .. attribute:: path_type
                        
                        	Type of Path (PopAndLookup, CrossConnect)
                        	**type**\:  :py:class:`MplsStaticPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStaticPath>`
                        
                        	**default value**\: cross-connect
                        
                        .. attribute:: label_type
                        
                        	Type of label (Outlabel, ExpNull or Pop)
                        	**type**\:  :py:class:`MplsStaticOutLabelTypes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStaticOutLabelTypes>`
                        
                        	**default value**\: none
                        
                        .. attribute:: next_hop_label
                        
                        	Outgoing/NH Label
                        	**type**\: int
                        
                        	**range:** 16..1048575
                        
                        	**default value**\: 16
                        
                        .. attribute:: next_hop_address
                        
                        	Next Hop IP Address
                        	**type**\: union of the below types:
                        
                        		**type**\: str
                        
                        			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        		**type**\: str
                        
                        			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: interface_name
                        
                        	Next hop Interface with form <Interface>R/S/I/P
                        	**type**\: str
                        
                        	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                        
                        .. attribute:: afi
                        
                        	Next hop Address Family
                        	**type**\:  :py:class:`MplsStaticNhAddressFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStaticNhAddressFamily>`
                        
                        	**default value**\: ipv4
                        
                        .. attribute:: metric
                        
                        	NH Path Metric
                        	**type**\: int
                        
                        	**range:** 0..254
                        
                        	**default value**\: 0
                        
                        .. attribute:: nh_mode
                        
                        	Next hop mode
                        	**type**\:  :py:class:`MplsStaticNhMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStaticNhMode>`
                        
                        	**default value**\: configured
                        
                        .. attribute:: path_role
                        
                        	Path Role
                        	**type**\:  :py:class:`MplsStaticPathRole <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStaticPathRole>`
                        
                        	**default value**\: primary
                        
                        .. attribute:: backup_id
                        
                        	Backup ID
                        	**type**\: int
                        
                        	**range:** 0..16
                        
                        	**default value**\: 0
                        
                        

                        """

                        _prefix = 'mpls-static-cfg'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(MplsStatic.DefaultVrf.LabelSwitchedPaths.LabelSwitchedPath.BackupPaths.Path, self).__init__()

                            self.yang_name = "path"
                            self.yang_parent_name = "backup-paths"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['path_id']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('path_id', (YLeaf(YType.uint32, 'path-id'), ['int'])),
                                ('path_type', (YLeaf(YType.enumeration, 'path-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg', 'MplsStaticPath', '')])),
                                ('label_type', (YLeaf(YType.enumeration, 'label-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg', 'MplsStaticOutLabelTypes', '')])),
                                ('next_hop_label', (YLeaf(YType.uint32, 'next-hop-label'), ['int'])),
                                ('next_hop_address', (YLeaf(YType.str, 'next-hop-address'), ['str','str'])),
                                ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                                ('afi', (YLeaf(YType.enumeration, 'afi'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg', 'MplsStaticNhAddressFamily', '')])),
                                ('metric', (YLeaf(YType.uint32, 'metric'), ['int'])),
                                ('nh_mode', (YLeaf(YType.enumeration, 'nh-mode'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg', 'MplsStaticNhMode', '')])),
                                ('path_role', (YLeaf(YType.enumeration, 'path-role'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg', 'MplsStaticPathRole', '')])),
                                ('backup_id', (YLeaf(YType.uint32, 'backup-id'), ['int'])),
                            ])
                            self.path_id = None
                            self.path_type = None
                            self.label_type = None
                            self.next_hop_label = None
                            self.next_hop_address = None
                            self.interface_name = None
                            self.afi = None
                            self.metric = None
                            self.nh_mode = None
                            self.path_role = None
                            self.backup_id = None
                            self._segment_path = lambda: "path" + "[path-id='" + str(self.path_id) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(MplsStatic.DefaultVrf.LabelSwitchedPaths.LabelSwitchedPath.BackupPaths.Path, ['path_id', 'path_type', 'label_type', 'next_hop_label', 'next_hop_address', 'interface_name', 'afi', 'metric', 'nh_mode', 'path_role', 'backup_id'], name, value)


                class InLabel(Entity):
                    """
                    MPLS Static Local Label Value
                    
                    .. attribute:: in_label_value
                    
                    	Local Label
                    	**type**\: int
                    
                    	**range:** 16..1048575
                    
                    .. attribute:: label_mode
                    
                    	Label Mode (PerVRF, PerPrefix or LSP)
                    	**type**\:  :py:class:`MplsStaticLabelMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStaticLabelMode>`
                    
                    .. attribute:: prefix
                    
                    	Address (IPv4/6 depending on AFI)
                    	**type**\: union of the below types:
                    
                    		**type**\: str
                    
                    			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    		**type**\: str
                    
                    			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: prefix_length
                    
                    	Prefix length
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tlh_mode
                    
                    	Top Label Hashing Mode
                    	**type**\: bool
                    
                    

                    """

                    _prefix = 'mpls-static-cfg'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(MplsStatic.DefaultVrf.LabelSwitchedPaths.LabelSwitchedPath.InLabel, self).__init__()

                        self.yang_name = "in-label"
                        self.yang_parent_name = "label-switched-path"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('in_label_value', (YLeaf(YType.uint32, 'in-label-value'), ['int'])),
                            ('label_mode', (YLeaf(YType.enumeration, 'label-mode'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg', 'MplsStaticLabelMode', '')])),
                            ('prefix', (YLeaf(YType.str, 'prefix'), ['str','str'])),
                            ('prefix_length', (YLeaf(YType.uint32, 'prefix-length'), ['int'])),
                            ('tlh_mode', (YLeaf(YType.boolean, 'tlh-mode'), ['bool'])),
                        ])
                        self.in_label_value = None
                        self.label_mode = None
                        self.prefix = None
                        self.prefix_length = None
                        self.tlh_mode = None
                        self._segment_path = lambda: "in-label"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(MplsStatic.DefaultVrf.LabelSwitchedPaths.LabelSwitchedPath.InLabel, ['in_label_value', 'label_mode', 'prefix', 'prefix_length', 'tlh_mode'], name, value)


                class Paths(Entity):
                    """
                    Forward Path Parameters
                    
                    .. attribute:: path
                    
                    	Path Information
                    	**type**\: list of  		 :py:class:`Path <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStatic.DefaultVrf.LabelSwitchedPaths.LabelSwitchedPath.Paths.Path>`
                    
                    

                    """

                    _prefix = 'mpls-static-cfg'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(MplsStatic.DefaultVrf.LabelSwitchedPaths.LabelSwitchedPath.Paths, self).__init__()

                        self.yang_name = "paths"
                        self.yang_parent_name = "label-switched-path"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("path", ("path", MplsStatic.DefaultVrf.LabelSwitchedPaths.LabelSwitchedPath.Paths.Path))])
                        self._leafs = OrderedDict()

                        self.path = YList(self)
                        self._segment_path = lambda: "paths"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(MplsStatic.DefaultVrf.LabelSwitchedPaths.LabelSwitchedPath.Paths, [], name, value)


                    class Path(Entity):
                        """
                        Path Information
                        
                        .. attribute:: path_id  (key)
                        
                        	Number of paths
                        	**type**\: int
                        
                        	**range:** 1..16
                        
                        .. attribute:: path_type
                        
                        	Type of Path (PopAndLookup, CrossConnect)
                        	**type**\:  :py:class:`MplsStaticPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStaticPath>`
                        
                        	**default value**\: cross-connect
                        
                        .. attribute:: label_type
                        
                        	Type of label (Outlabel, ExpNull or Pop)
                        	**type**\:  :py:class:`MplsStaticOutLabelTypes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStaticOutLabelTypes>`
                        
                        	**default value**\: none
                        
                        .. attribute:: next_hop_label
                        
                        	Outgoing/NH Label
                        	**type**\: int
                        
                        	**range:** 16..1048575
                        
                        	**default value**\: 16
                        
                        .. attribute:: next_hop_address
                        
                        	Next Hop IP Address
                        	**type**\: union of the below types:
                        
                        		**type**\: str
                        
                        			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        		**type**\: str
                        
                        			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: interface_name
                        
                        	Next hop Interface with form <Interface>R/S/I/P
                        	**type**\: str
                        
                        	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                        
                        .. attribute:: afi
                        
                        	Next hop Address Family
                        	**type**\:  :py:class:`MplsStaticNhAddressFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStaticNhAddressFamily>`
                        
                        	**default value**\: ipv4
                        
                        .. attribute:: metric
                        
                        	NH Path Metric
                        	**type**\: int
                        
                        	**range:** 0..254
                        
                        	**default value**\: 0
                        
                        .. attribute:: nh_mode
                        
                        	Next hop mode
                        	**type**\:  :py:class:`MplsStaticNhMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStaticNhMode>`
                        
                        	**default value**\: configured
                        
                        .. attribute:: path_role
                        
                        	Path Role
                        	**type**\:  :py:class:`MplsStaticPathRole <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStaticPathRole>`
                        
                        	**default value**\: primary
                        
                        .. attribute:: backup_id
                        
                        	Backup ID
                        	**type**\: int
                        
                        	**range:** 0..16
                        
                        	**default value**\: 0
                        
                        

                        """

                        _prefix = 'mpls-static-cfg'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(MplsStatic.DefaultVrf.LabelSwitchedPaths.LabelSwitchedPath.Paths.Path, self).__init__()

                            self.yang_name = "path"
                            self.yang_parent_name = "paths"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['path_id']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('path_id', (YLeaf(YType.uint32, 'path-id'), ['int'])),
                                ('path_type', (YLeaf(YType.enumeration, 'path-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg', 'MplsStaticPath', '')])),
                                ('label_type', (YLeaf(YType.enumeration, 'label-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg', 'MplsStaticOutLabelTypes', '')])),
                                ('next_hop_label', (YLeaf(YType.uint32, 'next-hop-label'), ['int'])),
                                ('next_hop_address', (YLeaf(YType.str, 'next-hop-address'), ['str','str'])),
                                ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                                ('afi', (YLeaf(YType.enumeration, 'afi'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg', 'MplsStaticNhAddressFamily', '')])),
                                ('metric', (YLeaf(YType.uint32, 'metric'), ['int'])),
                                ('nh_mode', (YLeaf(YType.enumeration, 'nh-mode'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg', 'MplsStaticNhMode', '')])),
                                ('path_role', (YLeaf(YType.enumeration, 'path-role'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg', 'MplsStaticPathRole', '')])),
                                ('backup_id', (YLeaf(YType.uint32, 'backup-id'), ['int'])),
                            ])
                            self.path_id = None
                            self.path_type = None
                            self.label_type = None
                            self.next_hop_label = None
                            self.next_hop_address = None
                            self.interface_name = None
                            self.afi = None
                            self.metric = None
                            self.nh_mode = None
                            self.path_role = None
                            self.backup_id = None
                            self._segment_path = lambda: "path" + "[path-id='" + str(self.path_id) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(MplsStatic.DefaultVrf.LabelSwitchedPaths.LabelSwitchedPath.Paths.Path, ['path_id', 'path_type', 'label_type', 'next_hop_label', 'next_hop_address', 'interface_name', 'afi', 'metric', 'nh_mode', 'path_role', 'backup_id'], name, value)


        class Afs(Entity):
            """
            Address Family Table
            
            .. attribute:: af
            
            	Address Family
            	**type**\: list of  		 :py:class:`Af <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStatic.DefaultVrf.Afs.Af>`
            
            

            """

            _prefix = 'mpls-static-cfg'
            _revision = '2017-09-07'

            def __init__(self):
                super(MplsStatic.DefaultVrf.Afs, self).__init__()

                self.yang_name = "afs"
                self.yang_parent_name = "default-vrf"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("af", ("af", MplsStatic.DefaultVrf.Afs.Af))])
                self._leafs = OrderedDict()

                self.af = YList(self)
                self._segment_path = lambda: "afs"
                self._absolute_path = lambda: "Cisco-IOS-XR-mpls-static-cfg:mpls-static/default-vrf/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(MplsStatic.DefaultVrf.Afs, [], name, value)


            class Af(Entity):
                """
                Address Family
                
                .. attribute:: afi  (key)
                
                	Address Family
                	**type**\:  :py:class:`MplsStaticAddressFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStaticAddressFamily>`
                
                .. attribute:: top_label_hash
                
                	Top Label Hash
                	**type**\:  :py:class:`TopLabelHash <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStatic.DefaultVrf.Afs.Af.TopLabelHash>`
                
                .. attribute:: local_labels
                
                	Local Label
                	**type**\:  :py:class:`LocalLabels <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStatic.DefaultVrf.Afs.Af.LocalLabels>`
                
                .. attribute:: enable
                
                	MPLS Static Apply Enable
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                

                """

                _prefix = 'mpls-static-cfg'
                _revision = '2017-09-07'

                def __init__(self):
                    super(MplsStatic.DefaultVrf.Afs.Af, self).__init__()

                    self.yang_name = "af"
                    self.yang_parent_name = "afs"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['afi']
                    self._child_classes = OrderedDict([("top-label-hash", ("top_label_hash", MplsStatic.DefaultVrf.Afs.Af.TopLabelHash)), ("local-labels", ("local_labels", MplsStatic.DefaultVrf.Afs.Af.LocalLabels))])
                    self._leafs = OrderedDict([
                        ('afi', (YLeaf(YType.enumeration, 'afi'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg', 'MplsStaticAddressFamily', '')])),
                        ('enable', (YLeaf(YType.empty, 'enable'), ['Empty'])),
                    ])
                    self.afi = None
                    self.enable = None

                    self.top_label_hash = MplsStatic.DefaultVrf.Afs.Af.TopLabelHash()
                    self.top_label_hash.parent = self
                    self._children_name_map["top_label_hash"] = "top-label-hash"

                    self.local_labels = MplsStatic.DefaultVrf.Afs.Af.LocalLabels()
                    self.local_labels.parent = self
                    self._children_name_map["local_labels"] = "local-labels"
                    self._segment_path = lambda: "af" + "[afi='" + str(self.afi) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-mpls-static-cfg:mpls-static/default-vrf/afs/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsStatic.DefaultVrf.Afs.Af, ['afi', 'enable'], name, value)


                class TopLabelHash(Entity):
                    """
                    Top Label Hash
                    
                    .. attribute:: local_labels
                    
                    	Local Label
                    	**type**\:  :py:class:`LocalLabels <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStatic.DefaultVrf.Afs.Af.TopLabelHash.LocalLabels>`
                    
                    

                    """

                    _prefix = 'mpls-static-cfg'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(MplsStatic.DefaultVrf.Afs.Af.TopLabelHash, self).__init__()

                        self.yang_name = "top-label-hash"
                        self.yang_parent_name = "af"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("local-labels", ("local_labels", MplsStatic.DefaultVrf.Afs.Af.TopLabelHash.LocalLabels))])
                        self._leafs = OrderedDict()

                        self.local_labels = MplsStatic.DefaultVrf.Afs.Af.TopLabelHash.LocalLabels()
                        self.local_labels.parent = self
                        self._children_name_map["local_labels"] = "local-labels"
                        self._segment_path = lambda: "top-label-hash"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(MplsStatic.DefaultVrf.Afs.Af.TopLabelHash, [], name, value)


                    class LocalLabels(Entity):
                        """
                        Local Label
                        
                        .. attribute:: local_label
                        
                        	Specify Local Label
                        	**type**\: list of  		 :py:class:`LocalLabel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStatic.DefaultVrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel>`
                        
                        

                        """

                        _prefix = 'mpls-static-cfg'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(MplsStatic.DefaultVrf.Afs.Af.TopLabelHash.LocalLabels, self).__init__()

                            self.yang_name = "local-labels"
                            self.yang_parent_name = "top-label-hash"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("local-label", ("local_label", MplsStatic.DefaultVrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel))])
                            self._leafs = OrderedDict()

                            self.local_label = YList(self)
                            self._segment_path = lambda: "local-labels"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(MplsStatic.DefaultVrf.Afs.Af.TopLabelHash.LocalLabels, [], name, value)


                        class LocalLabel(Entity):
                            """
                            Specify Local Label
                            
                            .. attribute:: local_label_id  (key)
                            
                            	Local Label
                            	**type**\: int
                            
                            	**range:** 16..1048575
                            
                            .. attribute:: label_type
                            
                            	MPLS Static Local Label Value
                            	**type**\:  :py:class:`LabelType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStatic.DefaultVrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel.LabelType>`
                            
                            .. attribute:: paths
                            
                            	Forward Path Parameters
                            	**type**\:  :py:class:`Paths <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStatic.DefaultVrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel.Paths>`
                            
                            

                            """

                            _prefix = 'mpls-static-cfg'
                            _revision = '2017-09-07'

                            def __init__(self):
                                super(MplsStatic.DefaultVrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel, self).__init__()

                                self.yang_name = "local-label"
                                self.yang_parent_name = "local-labels"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['local_label_id']
                                self._child_classes = OrderedDict([("label-type", ("label_type", MplsStatic.DefaultVrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel.LabelType)), ("paths", ("paths", MplsStatic.DefaultVrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel.Paths))])
                                self._leafs = OrderedDict([
                                    ('local_label_id', (YLeaf(YType.uint32, 'local-label-id'), ['int'])),
                                ])
                                self.local_label_id = None

                                self.label_type = MplsStatic.DefaultVrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel.LabelType()
                                self.label_type.parent = self
                                self._children_name_map["label_type"] = "label-type"

                                self.paths = MplsStatic.DefaultVrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel.Paths()
                                self.paths.parent = self
                                self._children_name_map["paths"] = "paths"
                                self._segment_path = lambda: "local-label" + "[local-label-id='" + str(self.local_label_id) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsStatic.DefaultVrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel, ['local_label_id'], name, value)


                            class LabelType(Entity):
                                """
                                MPLS Static Local Label Value
                                
                                .. attribute:: label_mode
                                
                                	Label Mode (PerVRF, PerPrefix or LSP)
                                	**type**\:  :py:class:`MplsStaticLabelMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStaticLabelMode>`
                                
                                .. attribute:: prefix
                                
                                	Address (IPv4/6 depending on AFI)
                                	**type**\: union of the below types:
                                
                                		**type**\: str
                                
                                			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                		**type**\: str
                                
                                			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: prefix_length
                                
                                	Prefix length
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'mpls-static-cfg'
                                _revision = '2017-09-07'

                                def __init__(self):
                                    super(MplsStatic.DefaultVrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel.LabelType, self).__init__()

                                    self.yang_name = "label-type"
                                    self.yang_parent_name = "local-label"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('label_mode', (YLeaf(YType.enumeration, 'label-mode'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg', 'MplsStaticLabelMode', '')])),
                                        ('prefix', (YLeaf(YType.str, 'prefix'), ['str','str'])),
                                        ('prefix_length', (YLeaf(YType.uint32, 'prefix-length'), ['int'])),
                                    ])
                                    self.label_mode = None
                                    self.prefix = None
                                    self.prefix_length = None
                                    self._segment_path = lambda: "label-type"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(MplsStatic.DefaultVrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel.LabelType, ['label_mode', 'prefix', 'prefix_length'], name, value)


                            class Paths(Entity):
                                """
                                Forward Path Parameters
                                
                                .. attribute:: path
                                
                                	Path Information
                                	**type**\: list of  		 :py:class:`Path <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStatic.DefaultVrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel.Paths.Path>`
                                
                                

                                """

                                _prefix = 'mpls-static-cfg'
                                _revision = '2017-09-07'

                                def __init__(self):
                                    super(MplsStatic.DefaultVrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel.Paths, self).__init__()

                                    self.yang_name = "paths"
                                    self.yang_parent_name = "local-label"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("path", ("path", MplsStatic.DefaultVrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel.Paths.Path))])
                                    self._leafs = OrderedDict()

                                    self.path = YList(self)
                                    self._segment_path = lambda: "paths"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(MplsStatic.DefaultVrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel.Paths, [], name, value)


                                class Path(Entity):
                                    """
                                    Path Information
                                    
                                    .. attribute:: path_id  (key)
                                    
                                    	Number of paths
                                    	**type**\: int
                                    
                                    	**range:** 1..16
                                    
                                    .. attribute:: path_type
                                    
                                    	Type of Path (PopAndLookup, CrossConnect)
                                    	**type**\:  :py:class:`MplsStaticPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStaticPath>`
                                    
                                    	**default value**\: cross-connect
                                    
                                    .. attribute:: label_type
                                    
                                    	Type of label (Outlabel, ExpNull or Pop)
                                    	**type**\:  :py:class:`MplsStaticOutLabelTypes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStaticOutLabelTypes>`
                                    
                                    	**default value**\: none
                                    
                                    .. attribute:: next_hop_label
                                    
                                    	Outgoing/NH Label
                                    	**type**\: int
                                    
                                    	**range:** 16..1048575
                                    
                                    	**default value**\: 16
                                    
                                    .. attribute:: next_hop_address
                                    
                                    	Next Hop IP Address
                                    	**type**\: union of the below types:
                                    
                                    		**type**\: str
                                    
                                    			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    		**type**\: str
                                    
                                    			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                    
                                    .. attribute:: interface_name
                                    
                                    	Next hop Interface with form <Interface>R/S/I/P
                                    	**type**\: str
                                    
                                    	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                                    
                                    .. attribute:: afi
                                    
                                    	Next hop Address Family
                                    	**type**\:  :py:class:`MplsStaticNhAddressFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStaticNhAddressFamily>`
                                    
                                    	**default value**\: ipv4
                                    
                                    .. attribute:: metric
                                    
                                    	NH Path Metric
                                    	**type**\: int
                                    
                                    	**range:** 0..254
                                    
                                    	**default value**\: 0
                                    
                                    .. attribute:: nh_mode
                                    
                                    	Next hop mode
                                    	**type**\:  :py:class:`MplsStaticNhMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStaticNhMode>`
                                    
                                    	**default value**\: configured
                                    
                                    .. attribute:: path_role
                                    
                                    	Path Role
                                    	**type**\:  :py:class:`MplsStaticPathRole <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStaticPathRole>`
                                    
                                    	**default value**\: primary
                                    
                                    .. attribute:: backup_id
                                    
                                    	Backup ID
                                    	**type**\: int
                                    
                                    	**range:** 0..16
                                    
                                    	**default value**\: 0
                                    
                                    

                                    """

                                    _prefix = 'mpls-static-cfg'
                                    _revision = '2017-09-07'

                                    def __init__(self):
                                        super(MplsStatic.DefaultVrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel.Paths.Path, self).__init__()

                                        self.yang_name = "path"
                                        self.yang_parent_name = "paths"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = ['path_id']
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('path_id', (YLeaf(YType.uint32, 'path-id'), ['int'])),
                                            ('path_type', (YLeaf(YType.enumeration, 'path-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg', 'MplsStaticPath', '')])),
                                            ('label_type', (YLeaf(YType.enumeration, 'label-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg', 'MplsStaticOutLabelTypes', '')])),
                                            ('next_hop_label', (YLeaf(YType.uint32, 'next-hop-label'), ['int'])),
                                            ('next_hop_address', (YLeaf(YType.str, 'next-hop-address'), ['str','str'])),
                                            ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                                            ('afi', (YLeaf(YType.enumeration, 'afi'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg', 'MplsStaticNhAddressFamily', '')])),
                                            ('metric', (YLeaf(YType.uint32, 'metric'), ['int'])),
                                            ('nh_mode', (YLeaf(YType.enumeration, 'nh-mode'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg', 'MplsStaticNhMode', '')])),
                                            ('path_role', (YLeaf(YType.enumeration, 'path-role'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg', 'MplsStaticPathRole', '')])),
                                            ('backup_id', (YLeaf(YType.uint32, 'backup-id'), ['int'])),
                                        ])
                                        self.path_id = None
                                        self.path_type = None
                                        self.label_type = None
                                        self.next_hop_label = None
                                        self.next_hop_address = None
                                        self.interface_name = None
                                        self.afi = None
                                        self.metric = None
                                        self.nh_mode = None
                                        self.path_role = None
                                        self.backup_id = None
                                        self._segment_path = lambda: "path" + "[path-id='" + str(self.path_id) + "']"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(MplsStatic.DefaultVrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel.Paths.Path, ['path_id', 'path_type', 'label_type', 'next_hop_label', 'next_hop_address', 'interface_name', 'afi', 'metric', 'nh_mode', 'path_role', 'backup_id'], name, value)


                class LocalLabels(Entity):
                    """
                    Local Label
                    
                    .. attribute:: local_label
                    
                    	Specify Local Label
                    	**type**\: list of  		 :py:class:`LocalLabel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStatic.DefaultVrf.Afs.Af.LocalLabels.LocalLabel>`
                    
                    

                    """

                    _prefix = 'mpls-static-cfg'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(MplsStatic.DefaultVrf.Afs.Af.LocalLabels, self).__init__()

                        self.yang_name = "local-labels"
                        self.yang_parent_name = "af"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("local-label", ("local_label", MplsStatic.DefaultVrf.Afs.Af.LocalLabels.LocalLabel))])
                        self._leafs = OrderedDict()

                        self.local_label = YList(self)
                        self._segment_path = lambda: "local-labels"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(MplsStatic.DefaultVrf.Afs.Af.LocalLabels, [], name, value)


                    class LocalLabel(Entity):
                        """
                        Specify Local Label
                        
                        .. attribute:: local_label_id  (key)
                        
                        	Local Label
                        	**type**\: int
                        
                        	**range:** 16..1048575
                        
                        .. attribute:: label_type
                        
                        	MPLS Static Local Label Value
                        	**type**\:  :py:class:`LabelType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStatic.DefaultVrf.Afs.Af.LocalLabels.LocalLabel.LabelType>`
                        
                        .. attribute:: paths
                        
                        	Forward Path Parameters
                        	**type**\:  :py:class:`Paths <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStatic.DefaultVrf.Afs.Af.LocalLabels.LocalLabel.Paths>`
                        
                        

                        """

                        _prefix = 'mpls-static-cfg'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(MplsStatic.DefaultVrf.Afs.Af.LocalLabels.LocalLabel, self).__init__()

                            self.yang_name = "local-label"
                            self.yang_parent_name = "local-labels"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['local_label_id']
                            self._child_classes = OrderedDict([("label-type", ("label_type", MplsStatic.DefaultVrf.Afs.Af.LocalLabels.LocalLabel.LabelType)), ("paths", ("paths", MplsStatic.DefaultVrf.Afs.Af.LocalLabels.LocalLabel.Paths))])
                            self._leafs = OrderedDict([
                                ('local_label_id', (YLeaf(YType.uint32, 'local-label-id'), ['int'])),
                            ])
                            self.local_label_id = None

                            self.label_type = MplsStatic.DefaultVrf.Afs.Af.LocalLabels.LocalLabel.LabelType()
                            self.label_type.parent = self
                            self._children_name_map["label_type"] = "label-type"

                            self.paths = MplsStatic.DefaultVrf.Afs.Af.LocalLabels.LocalLabel.Paths()
                            self.paths.parent = self
                            self._children_name_map["paths"] = "paths"
                            self._segment_path = lambda: "local-label" + "[local-label-id='" + str(self.local_label_id) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(MplsStatic.DefaultVrf.Afs.Af.LocalLabels.LocalLabel, ['local_label_id'], name, value)


                        class LabelType(Entity):
                            """
                            MPLS Static Local Label Value
                            
                            .. attribute:: label_mode
                            
                            	Label Mode (PerVRF, PerPrefix or LSP)
                            	**type**\:  :py:class:`MplsStaticLabelMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStaticLabelMode>`
                            
                            .. attribute:: prefix
                            
                            	Address (IPv4/6 depending on AFI)
                            	**type**\: union of the below types:
                            
                            		**type**\: str
                            
                            			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            		**type**\: str
                            
                            			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: prefix_length
                            
                            	Prefix length
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'mpls-static-cfg'
                            _revision = '2017-09-07'

                            def __init__(self):
                                super(MplsStatic.DefaultVrf.Afs.Af.LocalLabels.LocalLabel.LabelType, self).__init__()

                                self.yang_name = "label-type"
                                self.yang_parent_name = "local-label"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('label_mode', (YLeaf(YType.enumeration, 'label-mode'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg', 'MplsStaticLabelMode', '')])),
                                    ('prefix', (YLeaf(YType.str, 'prefix'), ['str','str'])),
                                    ('prefix_length', (YLeaf(YType.uint32, 'prefix-length'), ['int'])),
                                ])
                                self.label_mode = None
                                self.prefix = None
                                self.prefix_length = None
                                self._segment_path = lambda: "label-type"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsStatic.DefaultVrf.Afs.Af.LocalLabels.LocalLabel.LabelType, ['label_mode', 'prefix', 'prefix_length'], name, value)


                        class Paths(Entity):
                            """
                            Forward Path Parameters
                            
                            .. attribute:: path
                            
                            	Path Information
                            	**type**\: list of  		 :py:class:`Path <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStatic.DefaultVrf.Afs.Af.LocalLabels.LocalLabel.Paths.Path>`
                            
                            

                            """

                            _prefix = 'mpls-static-cfg'
                            _revision = '2017-09-07'

                            def __init__(self):
                                super(MplsStatic.DefaultVrf.Afs.Af.LocalLabels.LocalLabel.Paths, self).__init__()

                                self.yang_name = "paths"
                                self.yang_parent_name = "local-label"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("path", ("path", MplsStatic.DefaultVrf.Afs.Af.LocalLabels.LocalLabel.Paths.Path))])
                                self._leafs = OrderedDict()

                                self.path = YList(self)
                                self._segment_path = lambda: "paths"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsStatic.DefaultVrf.Afs.Af.LocalLabels.LocalLabel.Paths, [], name, value)


                            class Path(Entity):
                                """
                                Path Information
                                
                                .. attribute:: path_id  (key)
                                
                                	Number of paths
                                	**type**\: int
                                
                                	**range:** 1..16
                                
                                .. attribute:: path_type
                                
                                	Type of Path (PopAndLookup, CrossConnect)
                                	**type**\:  :py:class:`MplsStaticPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStaticPath>`
                                
                                	**default value**\: cross-connect
                                
                                .. attribute:: label_type
                                
                                	Type of label (Outlabel, ExpNull or Pop)
                                	**type**\:  :py:class:`MplsStaticOutLabelTypes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStaticOutLabelTypes>`
                                
                                	**default value**\: none
                                
                                .. attribute:: next_hop_label
                                
                                	Outgoing/NH Label
                                	**type**\: int
                                
                                	**range:** 16..1048575
                                
                                	**default value**\: 16
                                
                                .. attribute:: next_hop_address
                                
                                	Next Hop IP Address
                                	**type**\: union of the below types:
                                
                                		**type**\: str
                                
                                			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                		**type**\: str
                                
                                			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: interface_name
                                
                                	Next hop Interface with form <Interface>R/S/I/P
                                	**type**\: str
                                
                                	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                                
                                .. attribute:: afi
                                
                                	Next hop Address Family
                                	**type**\:  :py:class:`MplsStaticNhAddressFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStaticNhAddressFamily>`
                                
                                	**default value**\: ipv4
                                
                                .. attribute:: metric
                                
                                	NH Path Metric
                                	**type**\: int
                                
                                	**range:** 0..254
                                
                                	**default value**\: 0
                                
                                .. attribute:: nh_mode
                                
                                	Next hop mode
                                	**type**\:  :py:class:`MplsStaticNhMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStaticNhMode>`
                                
                                	**default value**\: configured
                                
                                .. attribute:: path_role
                                
                                	Path Role
                                	**type**\:  :py:class:`MplsStaticPathRole <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStaticPathRole>`
                                
                                	**default value**\: primary
                                
                                .. attribute:: backup_id
                                
                                	Backup ID
                                	**type**\: int
                                
                                	**range:** 0..16
                                
                                	**default value**\: 0
                                
                                

                                """

                                _prefix = 'mpls-static-cfg'
                                _revision = '2017-09-07'

                                def __init__(self):
                                    super(MplsStatic.DefaultVrf.Afs.Af.LocalLabels.LocalLabel.Paths.Path, self).__init__()

                                    self.yang_name = "path"
                                    self.yang_parent_name = "paths"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['path_id']
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('path_id', (YLeaf(YType.uint32, 'path-id'), ['int'])),
                                        ('path_type', (YLeaf(YType.enumeration, 'path-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg', 'MplsStaticPath', '')])),
                                        ('label_type', (YLeaf(YType.enumeration, 'label-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg', 'MplsStaticOutLabelTypes', '')])),
                                        ('next_hop_label', (YLeaf(YType.uint32, 'next-hop-label'), ['int'])),
                                        ('next_hop_address', (YLeaf(YType.str, 'next-hop-address'), ['str','str'])),
                                        ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                                        ('afi', (YLeaf(YType.enumeration, 'afi'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg', 'MplsStaticNhAddressFamily', '')])),
                                        ('metric', (YLeaf(YType.uint32, 'metric'), ['int'])),
                                        ('nh_mode', (YLeaf(YType.enumeration, 'nh-mode'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg', 'MplsStaticNhMode', '')])),
                                        ('path_role', (YLeaf(YType.enumeration, 'path-role'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg', 'MplsStaticPathRole', '')])),
                                        ('backup_id', (YLeaf(YType.uint32, 'backup-id'), ['int'])),
                                    ])
                                    self.path_id = None
                                    self.path_type = None
                                    self.label_type = None
                                    self.next_hop_label = None
                                    self.next_hop_address = None
                                    self.interface_name = None
                                    self.afi = None
                                    self.metric = None
                                    self.nh_mode = None
                                    self.path_role = None
                                    self.backup_id = None
                                    self._segment_path = lambda: "path" + "[path-id='" + str(self.path_id) + "']"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(MplsStatic.DefaultVrf.Afs.Af.LocalLabels.LocalLabel.Paths.Path, ['path_id', 'path_type', 'label_type', 'next_hop_label', 'next_hop_address', 'interface_name', 'afi', 'metric', 'nh_mode', 'path_role', 'backup_id'], name, value)

    def clone_ptr(self):
        self._top_entity = MplsStatic()
        return self._top_entity

