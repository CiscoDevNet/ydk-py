""" Cisco_IOS_XR_mpls_static_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR mpls\-static package operational data.

This module contains definitions
for the following management objects\:
  mpls\-static\: MPLS STATIC operational data

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class MgmtMplsStaticLabelMode(Enum):
    """
    MgmtMplsStaticLabelMode (Enum Class)

    Mgmt mpls static label mode

    .. data:: none = 0

    	No Label Mode

    .. data:: per_prefix = 1

    	Per-prefix Label

    .. data:: per_vrf = 2

    	Per-VRF label

    .. data:: cross_connect = 3

    	Label with crossconnect

    """

    none = Enum.YLeaf(0, "none")

    per_prefix = Enum.YLeaf(1, "per-prefix")

    per_vrf = Enum.YLeaf(2, "per-vrf")

    cross_connect = Enum.YLeaf(3, "cross-connect")


class MgmtMplsStaticLabelStatus(Enum):
    """
    MgmtMplsStaticLabelStatus (Enum Class)

    Mgmt mpls static label status

    .. data:: not_created = 0

    	Label Not Created

    .. data:: vrf_down = 1

    	Label without active VRF

    .. data:: rewrite_vrf_down = 2

    	Rewrite without active VRF

    .. data:: lsd_disconnected = 3

    	LSD is disconnected

    .. data:: lsd_failed = 4

    	LSD operation failed

    .. data:: wait_for_lsd_reply = 5

    	Waiting for LSD operation

    .. data:: label_created = 6

    	Label Created

    .. data:: label_create_failed = 7

    	Label Creation Failed

    .. data:: label_rewrite_failed = 8

    	Rewrite Creation Failed

    .. data:: rewrite_next_hop_interface_down = 9

    	Rewrite NextHop Down 

    .. data:: label_discrepancy = 10

    	Label Discrepancy 

    .. data:: rewrite_discrepancy = 11

    	Rewrite Discrepancy 

    .. data:: rewrite_nexthop_unresolved = 12

    	Rewrite Nexthop Unresolved

    .. data:: label_status_unknown = 13

    	Label Status Unknown

    """

    not_created = Enum.YLeaf(0, "not-created")

    vrf_down = Enum.YLeaf(1, "vrf-down")

    rewrite_vrf_down = Enum.YLeaf(2, "rewrite-vrf-down")

    lsd_disconnected = Enum.YLeaf(3, "lsd-disconnected")

    lsd_failed = Enum.YLeaf(4, "lsd-failed")

    wait_for_lsd_reply = Enum.YLeaf(5, "wait-for-lsd-reply")

    label_created = Enum.YLeaf(6, "label-created")

    label_create_failed = Enum.YLeaf(7, "label-create-failed")

    label_rewrite_failed = Enum.YLeaf(8, "label-rewrite-failed")

    rewrite_next_hop_interface_down = Enum.YLeaf(9, "rewrite-next-hop-interface-down")

    label_discrepancy = Enum.YLeaf(10, "label-discrepancy")

    rewrite_discrepancy = Enum.YLeaf(11, "rewrite-discrepancy")

    rewrite_nexthop_unresolved = Enum.YLeaf(12, "rewrite-nexthop-unresolved")

    label_status_unknown = Enum.YLeaf(13, "label-status-unknown")


class MgmtMplsStaticPathStatus(Enum):
    """
    MgmtMplsStaticPathStatus (Enum Class)

    Mgmt mpls static path status

    .. data:: path_next_hop_none = 0

    	Path NextHop No Status

    .. data:: path_next_hop_interface_down = 1

    	Path NextHop Interface Down 

    .. data:: path_next_hop_valid = 2

    	Path NextHop Valid

    .. data:: resolve_failed = 3

    	Path NextHop Resolve Failed

    .. data:: frr_backup = 4

    	FRR Backup

    .. data:: backup = 5

    	Backup

    """

    path_next_hop_none = Enum.YLeaf(0, "path-next-hop-none")

    path_next_hop_interface_down = Enum.YLeaf(1, "path-next-hop-interface-down")

    path_next_hop_valid = Enum.YLeaf(2, "path-next-hop-valid")

    resolve_failed = Enum.YLeaf(3, "resolve-failed")

    frr_backup = Enum.YLeaf(4, "frr-backup")

    backup = Enum.YLeaf(5, "backup")


class MgmtStaticAddr(Enum):
    """
    MgmtStaticAddr (Enum Class)

    Mgmt static addr

    .. data:: not_applicable = 0

    	Not Applicable

    .. data:: ipv4 = 1

    	IPv4

    .. data:: ipv6 = 2

    	IPv6

    """

    not_applicable = Enum.YLeaf(0, "not-applicable")

    ipv4 = Enum.YLeaf(1, "ipv4")

    ipv6 = Enum.YLeaf(2, "ipv6")


class MgmtStaticLspAfi(Enum):
    """
    MgmtStaticLspAfi (Enum Class)

    Mgmt static lsp afi

    .. data:: not_applicable = 0

    	Not Applicable

    .. data:: ipv4 = 1

    	IPv4

    .. data:: ipv6 = 2

    	IPv6

    """

    not_applicable = Enum.YLeaf(0, "not-applicable")

    ipv4 = Enum.YLeaf(1, "ipv4")

    ipv6 = Enum.YLeaf(2, "ipv6")


class MgmtStaticPath(Enum):
    """
    MgmtStaticPath (Enum Class)

    Mgmt static path

    .. data:: cross_connect_path = 0

    	Crossconnect Path

    .. data:: pop_lookup_path = 1

    	Pop and Lookup Path

    """

    cross_connect_path = Enum.YLeaf(0, "cross-connect-path")

    pop_lookup_path = Enum.YLeaf(1, "pop-lookup-path")


class MplsStaticPathRole(Enum):
    """
    MplsStaticPathRole (Enum Class)

    Mpls static path role

    .. data:: primary = 0

    	Path is only for primary traffic

    .. data:: backup = 1

    	Path is only for backup traffic

    .. data:: primary_and_backup = 2

    	Path is for primary and backup traffic

    """

    primary = Enum.YLeaf(0, "primary")

    backup = Enum.YLeaf(1, "backup")

    primary_and_backup = Enum.YLeaf(2, "primary-and-backup")



class MplsStatic(Entity):
    """
    MPLS STATIC operational data
    
    .. attribute:: vrfs
    
    	VRF table
    	**type**\:  :py:class:`Vrfs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MplsStatic.Vrfs>`
    
    .. attribute:: summary
    
    	MPLS STATIC summary data
    	**type**\:  :py:class:`Summary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MplsStatic.Summary>`
    
    .. attribute:: local_labels
    
    	data for static local\-label table
    	**type**\:  :py:class:`LocalLabels <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MplsStatic.LocalLabels>`
    
    

    """

    _prefix = 'mpls-static-oper'
    _revision = '2017-05-01'

    def __init__(self):
        super(MplsStatic, self).__init__()
        self._top_entity = None

        self.yang_name = "mpls-static"
        self.yang_parent_name = "Cisco-IOS-XR-mpls-static-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("vrfs", ("vrfs", MplsStatic.Vrfs)), ("summary", ("summary", MplsStatic.Summary)), ("local-labels", ("local_labels", MplsStatic.LocalLabels))])
        self._leafs = OrderedDict()

        self.vrfs = MplsStatic.Vrfs()
        self.vrfs.parent = self
        self._children_name_map["vrfs"] = "vrfs"

        self.summary = MplsStatic.Summary()
        self.summary.parent = self
        self._children_name_map["summary"] = "summary"

        self.local_labels = MplsStatic.LocalLabels()
        self.local_labels.parent = self
        self._children_name_map["local_labels"] = "local-labels"
        self._segment_path = lambda: "Cisco-IOS-XR-mpls-static-oper:mpls-static"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(MplsStatic, [], name, value)


    class Vrfs(Entity):
        """
        VRF table
        
        .. attribute:: vrf
        
        	VRF Name
        	**type**\: list of  		 :py:class:`Vrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MplsStatic.Vrfs.Vrf>`
        
        

        """

        _prefix = 'mpls-static-oper'
        _revision = '2017-05-01'

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
            self._absolute_path = lambda: "Cisco-IOS-XR-mpls-static-oper:mpls-static/%s" % self._segment_path()
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
            
            .. attribute:: lsps
            
            	data for static lsp table
            	**type**\:  :py:class:`Lsps <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MplsStatic.Vrfs.Vrf.Lsps>`
            
            .. attribute:: local_labels
            
            	data for static local\-label table
            	**type**\:  :py:class:`LocalLabels <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MplsStatic.Vrfs.Vrf.LocalLabels>`
            
            

            """

            _prefix = 'mpls-static-oper'
            _revision = '2017-05-01'

            def __init__(self):
                super(MplsStatic.Vrfs.Vrf, self).__init__()

                self.yang_name = "vrf"
                self.yang_parent_name = "vrfs"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['vrf_name']
                self._child_classes = OrderedDict([("lsps", ("lsps", MplsStatic.Vrfs.Vrf.Lsps)), ("local-labels", ("local_labels", MplsStatic.Vrfs.Vrf.LocalLabels))])
                self._leafs = OrderedDict([
                    ('vrf_name', (YLeaf(YType.str, 'vrf-name'), ['str'])),
                ])
                self.vrf_name = None

                self.lsps = MplsStatic.Vrfs.Vrf.Lsps()
                self.lsps.parent = self
                self._children_name_map["lsps"] = "lsps"

                self.local_labels = MplsStatic.Vrfs.Vrf.LocalLabels()
                self.local_labels.parent = self
                self._children_name_map["local_labels"] = "local-labels"
                self._segment_path = lambda: "vrf" + "[vrf-name='" + str(self.vrf_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-mpls-static-oper:mpls-static/vrfs/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(MplsStatic.Vrfs.Vrf, ['vrf_name'], name, value)


            class Lsps(Entity):
                """
                data for static lsp table
                
                .. attribute:: lsp
                
                	Data for static lsp
                	**type**\: list of  		 :py:class:`Lsp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MplsStatic.Vrfs.Vrf.Lsps.Lsp>`
                
                

                """

                _prefix = 'mpls-static-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(MplsStatic.Vrfs.Vrf.Lsps, self).__init__()

                    self.yang_name = "lsps"
                    self.yang_parent_name = "vrf"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("lsp", ("lsp", MplsStatic.Vrfs.Vrf.Lsps.Lsp))])
                    self._leafs = OrderedDict()

                    self.lsp = YList(self)
                    self._segment_path = lambda: "lsps"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsStatic.Vrfs.Vrf.Lsps, [], name, value)


                class Lsp(Entity):
                    """
                    Data for static lsp
                    
                    .. attribute:: lsp_name  (key)
                    
                    	LSP Name
                    	**type**\: str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: label
                    
                    	Label Information
                    	**type**\:  :py:class:`Label <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MplsStatic.Vrfs.Vrf.Lsps.Lsp.Label>`
                    
                    .. attribute:: lsp_name_xr
                    
                    	LSP Name
                    	**type**\: str
                    
                    

                    """

                    _prefix = 'mpls-static-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(MplsStatic.Vrfs.Vrf.Lsps.Lsp, self).__init__()

                        self.yang_name = "lsp"
                        self.yang_parent_name = "lsps"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['lsp_name']
                        self._child_classes = OrderedDict([("label", ("label", MplsStatic.Vrfs.Vrf.Lsps.Lsp.Label))])
                        self._leafs = OrderedDict([
                            ('lsp_name', (YLeaf(YType.str, 'lsp-name'), ['str'])),
                            ('lsp_name_xr', (YLeaf(YType.str, 'lsp-name-xr'), ['str'])),
                        ])
                        self.lsp_name = None
                        self.lsp_name_xr = None

                        self.label = MplsStatic.Vrfs.Vrf.Lsps.Lsp.Label()
                        self.label.parent = self
                        self._children_name_map["label"] = "label"
                        self._segment_path = lambda: "lsp" + "[lsp-name='" + str(self.lsp_name) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(MplsStatic.Vrfs.Vrf.Lsps.Lsp, ['lsp_name', 'lsp_name_xr'], name, value)


                    class Label(Entity):
                        """
                        Label Information
                        
                        .. attribute:: prefix
                        
                        	Prefix Information
                        	**type**\:  :py:class:`Prefix <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MplsStatic.Vrfs.Vrf.Lsps.Lsp.Label.Prefix>`
                        
                        .. attribute:: pathset_resolve_nh
                        
                        	Primary pathset resolve\-nexthop IP Address
                        	**type**\:  :py:class:`PathsetResolveNh <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MplsStatic.Vrfs.Vrf.Lsps.Lsp.Label.PathsetResolveNh>`
                        
                        .. attribute:: backup_pathset_resolve_nh
                        
                        	Backup pathset resolve\-nexthop IP Address
                        	**type**\:  :py:class:`BackupPathsetResolveNh <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MplsStatic.Vrfs.Vrf.Lsps.Lsp.Label.BackupPathsetResolveNh>`
                        
                        .. attribute:: label
                        
                        	Label value
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: label_mode
                        
                        	Label Mode
                        	**type**\:  :py:class:`MgmtMplsStaticLabelMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MgmtMplsStaticLabelMode>`
                        
                        .. attribute:: label_status
                        
                        	Label Status
                        	**type**\:  :py:class:`MgmtMplsStaticLabelStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MgmtMplsStaticLabelStatus>`
                        
                        .. attribute:: vrf_name
                        
                        	VRF name
                        	**type**\: str
                        
                        .. attribute:: pathset_via_resolve
                        
                        	Primary Pathset as a result of resolve
                        	**type**\: bool
                        
                        .. attribute:: backup_pathset_via_resolve
                        
                        	Backup Pathset as a result of resolve
                        	**type**\: bool
                        
                        .. attribute:: address_family
                        
                        	Address Family
                        	**type**\:  :py:class:`MgmtStaticAddr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MgmtStaticAddr>`
                        
                        .. attribute:: path_info
                        
                        	Path Information
                        	**type**\: list of  		 :py:class:`PathInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MplsStatic.Vrfs.Vrf.Lsps.Lsp.Label.PathInfo>`
                        
                        .. attribute:: backup_path_info
                        
                        	Backup Path Information
                        	**type**\: list of  		 :py:class:`BackupPathInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MplsStatic.Vrfs.Vrf.Lsps.Lsp.Label.BackupPathInfo>`
                        
                        

                        """

                        _prefix = 'mpls-static-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(MplsStatic.Vrfs.Vrf.Lsps.Lsp.Label, self).__init__()

                            self.yang_name = "label"
                            self.yang_parent_name = "lsp"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("prefix", ("prefix", MplsStatic.Vrfs.Vrf.Lsps.Lsp.Label.Prefix)), ("pathset-resolve-nh", ("pathset_resolve_nh", MplsStatic.Vrfs.Vrf.Lsps.Lsp.Label.PathsetResolveNh)), ("backup-pathset-resolve-nh", ("backup_pathset_resolve_nh", MplsStatic.Vrfs.Vrf.Lsps.Lsp.Label.BackupPathsetResolveNh)), ("path-info", ("path_info", MplsStatic.Vrfs.Vrf.Lsps.Lsp.Label.PathInfo)), ("backup-path-info", ("backup_path_info", MplsStatic.Vrfs.Vrf.Lsps.Lsp.Label.BackupPathInfo))])
                            self._leafs = OrderedDict([
                                ('label', (YLeaf(YType.uint32, 'label'), ['int'])),
                                ('label_mode', (YLeaf(YType.enumeration, 'label-mode'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper', 'MgmtMplsStaticLabelMode', '')])),
                                ('label_status', (YLeaf(YType.enumeration, 'label-status'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper', 'MgmtMplsStaticLabelStatus', '')])),
                                ('vrf_name', (YLeaf(YType.str, 'vrf-name'), ['str'])),
                                ('pathset_via_resolve', (YLeaf(YType.boolean, 'pathset-via-resolve'), ['bool'])),
                                ('backup_pathset_via_resolve', (YLeaf(YType.boolean, 'backup-pathset-via-resolve'), ['bool'])),
                                ('address_family', (YLeaf(YType.enumeration, 'address-family'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper', 'MgmtStaticAddr', '')])),
                            ])
                            self.label = None
                            self.label_mode = None
                            self.label_status = None
                            self.vrf_name = None
                            self.pathset_via_resolve = None
                            self.backup_pathset_via_resolve = None
                            self.address_family = None

                            self.prefix = MplsStatic.Vrfs.Vrf.Lsps.Lsp.Label.Prefix()
                            self.prefix.parent = self
                            self._children_name_map["prefix"] = "prefix"

                            self.pathset_resolve_nh = MplsStatic.Vrfs.Vrf.Lsps.Lsp.Label.PathsetResolveNh()
                            self.pathset_resolve_nh.parent = self
                            self._children_name_map["pathset_resolve_nh"] = "pathset-resolve-nh"

                            self.backup_pathset_resolve_nh = MplsStatic.Vrfs.Vrf.Lsps.Lsp.Label.BackupPathsetResolveNh()
                            self.backup_pathset_resolve_nh.parent = self
                            self._children_name_map["backup_pathset_resolve_nh"] = "backup-pathset-resolve-nh"

                            self.path_info = YList(self)
                            self.backup_path_info = YList(self)
                            self._segment_path = lambda: "label"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(MplsStatic.Vrfs.Vrf.Lsps.Lsp.Label, ['label', 'label_mode', 'label_status', 'vrf_name', 'pathset_via_resolve', 'backup_pathset_via_resolve', 'address_family'], name, value)


                        class Prefix(Entity):
                            """
                            Prefix Information
                            
                            .. attribute:: prefix
                            
                            	Prefix
                            	**type**\:  :py:class:`Prefix_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MplsStatic.Vrfs.Vrf.Lsps.Lsp.Label.Prefix.Prefix_>`
                            
                            .. attribute:: prefix_length
                            
                            	Prefix length
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            

                            """

                            _prefix = 'mpls-static-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(MplsStatic.Vrfs.Vrf.Lsps.Lsp.Label.Prefix, self).__init__()

                                self.yang_name = "prefix"
                                self.yang_parent_name = "label"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("prefix", ("prefix", MplsStatic.Vrfs.Vrf.Lsps.Lsp.Label.Prefix.Prefix_))])
                                self._leafs = OrderedDict([
                                    ('prefix_length', (YLeaf(YType.uint8, 'prefix-length'), ['int'])),
                                ])
                                self.prefix_length = None

                                self.prefix = MplsStatic.Vrfs.Vrf.Lsps.Lsp.Label.Prefix.Prefix_()
                                self.prefix.parent = self
                                self._children_name_map["prefix"] = "prefix"
                                self._segment_path = lambda: "prefix"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsStatic.Vrfs.Vrf.Lsps.Lsp.Label.Prefix, ['prefix_length'], name, value)


                            class Prefix_(Entity):
                                """
                                Prefix
                                
                                .. attribute:: af_name
                                
                                	AFName
                                	**type**\:  :py:class:`MgmtStaticAddr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MgmtStaticAddr>`
                                
                                .. attribute:: ipv4_prefix
                                
                                	IPv4 context
                                	**type**\: str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: ipv6_prefix
                                
                                	IPv6 context
                                	**type**\: str
                                
                                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                
                                

                                """

                                _prefix = 'mpls-static-oper'
                                _revision = '2017-05-01'

                                def __init__(self):
                                    super(MplsStatic.Vrfs.Vrf.Lsps.Lsp.Label.Prefix.Prefix_, self).__init__()

                                    self.yang_name = "prefix"
                                    self.yang_parent_name = "prefix"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('af_name', (YLeaf(YType.enumeration, 'af-name'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper', 'MgmtStaticAddr', '')])),
                                        ('ipv4_prefix', (YLeaf(YType.str, 'ipv4-prefix'), ['str'])),
                                        ('ipv6_prefix', (YLeaf(YType.str, 'ipv6-prefix'), ['str'])),
                                    ])
                                    self.af_name = None
                                    self.ipv4_prefix = None
                                    self.ipv6_prefix = None
                                    self._segment_path = lambda: "prefix"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(MplsStatic.Vrfs.Vrf.Lsps.Lsp.Label.Prefix.Prefix_, ['af_name', 'ipv4_prefix', 'ipv6_prefix'], name, value)


                        class PathsetResolveNh(Entity):
                            """
                            Primary pathset resolve\-nexthop IP Address
                            
                            .. attribute:: af_name
                            
                            	AFName
                            	**type**\:  :py:class:`MgmtStaticAddr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MgmtStaticAddr>`
                            
                            .. attribute:: ipv4_prefix
                            
                            	IPv4 context
                            	**type**\: str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: ipv6_prefix
                            
                            	IPv6 context
                            	**type**\: str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            

                            """

                            _prefix = 'mpls-static-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(MplsStatic.Vrfs.Vrf.Lsps.Lsp.Label.PathsetResolveNh, self).__init__()

                                self.yang_name = "pathset-resolve-nh"
                                self.yang_parent_name = "label"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('af_name', (YLeaf(YType.enumeration, 'af-name'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper', 'MgmtStaticAddr', '')])),
                                    ('ipv4_prefix', (YLeaf(YType.str, 'ipv4-prefix'), ['str'])),
                                    ('ipv6_prefix', (YLeaf(YType.str, 'ipv6-prefix'), ['str'])),
                                ])
                                self.af_name = None
                                self.ipv4_prefix = None
                                self.ipv6_prefix = None
                                self._segment_path = lambda: "pathset-resolve-nh"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsStatic.Vrfs.Vrf.Lsps.Lsp.Label.PathsetResolveNh, ['af_name', 'ipv4_prefix', 'ipv6_prefix'], name, value)


                        class BackupPathsetResolveNh(Entity):
                            """
                            Backup pathset resolve\-nexthop IP Address
                            
                            .. attribute:: af_name
                            
                            	AFName
                            	**type**\:  :py:class:`MgmtStaticAddr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MgmtStaticAddr>`
                            
                            .. attribute:: ipv4_prefix
                            
                            	IPv4 context
                            	**type**\: str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: ipv6_prefix
                            
                            	IPv6 context
                            	**type**\: str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            

                            """

                            _prefix = 'mpls-static-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(MplsStatic.Vrfs.Vrf.Lsps.Lsp.Label.BackupPathsetResolveNh, self).__init__()

                                self.yang_name = "backup-pathset-resolve-nh"
                                self.yang_parent_name = "label"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('af_name', (YLeaf(YType.enumeration, 'af-name'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper', 'MgmtStaticAddr', '')])),
                                    ('ipv4_prefix', (YLeaf(YType.str, 'ipv4-prefix'), ['str'])),
                                    ('ipv6_prefix', (YLeaf(YType.str, 'ipv6-prefix'), ['str'])),
                                ])
                                self.af_name = None
                                self.ipv4_prefix = None
                                self.ipv6_prefix = None
                                self._segment_path = lambda: "backup-pathset-resolve-nh"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsStatic.Vrfs.Vrf.Lsps.Lsp.Label.BackupPathsetResolveNh, ['af_name', 'ipv4_prefix', 'ipv6_prefix'], name, value)


                        class PathInfo(Entity):
                            """
                            Path Information
                            
                            .. attribute:: nexthop
                            
                            	Nexthop information
                            	**type**\:  :py:class:`Nexthop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MplsStatic.Vrfs.Vrf.Lsps.Lsp.Label.PathInfo.Nexthop>`
                            
                            .. attribute:: path_number
                            
                            	Path Number
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: type
                            
                            	Path Type
                            	**type**\:  :py:class:`MgmtStaticPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MgmtStaticPath>`
                            
                            .. attribute:: path_role
                            
                            	Path Role
                            	**type**\:  :py:class:`MplsStaticPathRole <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MplsStaticPathRole>`
                            
                            .. attribute:: path_id
                            
                            	Path Id
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            .. attribute:: backup_id
                            
                            	Path Backup Id
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            .. attribute:: status
                            
                            	Path Status
                            	**type**\:  :py:class:`MgmtMplsStaticPathStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MgmtMplsStaticPathStatus>`
                            
                            

                            """

                            _prefix = 'mpls-static-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(MplsStatic.Vrfs.Vrf.Lsps.Lsp.Label.PathInfo, self).__init__()

                                self.yang_name = "path-info"
                                self.yang_parent_name = "label"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("nexthop", ("nexthop", MplsStatic.Vrfs.Vrf.Lsps.Lsp.Label.PathInfo.Nexthop))])
                                self._leafs = OrderedDict([
                                    ('path_number', (YLeaf(YType.uint32, 'path-number'), ['int'])),
                                    ('type', (YLeaf(YType.enumeration, 'type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper', 'MgmtStaticPath', '')])),
                                    ('path_role', (YLeaf(YType.enumeration, 'path-role'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper', 'MplsStaticPathRole', '')])),
                                    ('path_id', (YLeaf(YType.uint8, 'path-id'), ['int'])),
                                    ('backup_id', (YLeaf(YType.uint8, 'backup-id'), ['int'])),
                                    ('status', (YLeaf(YType.enumeration, 'status'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper', 'MgmtMplsStaticPathStatus', '')])),
                                ])
                                self.path_number = None
                                self.type = None
                                self.path_role = None
                                self.path_id = None
                                self.backup_id = None
                                self.status = None

                                self.nexthop = MplsStatic.Vrfs.Vrf.Lsps.Lsp.Label.PathInfo.Nexthop()
                                self.nexthop.parent = self
                                self._children_name_map["nexthop"] = "nexthop"
                                self._segment_path = lambda: "path-info"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsStatic.Vrfs.Vrf.Lsps.Lsp.Label.PathInfo, ['path_number', 'type', 'path_role', 'path_id', 'backup_id', 'status'], name, value)


                            class Nexthop(Entity):
                                """
                                Nexthop information
                                
                                .. attribute:: address
                                
                                	Next\-Hop IP Address
                                	**type**\:  :py:class:`Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MplsStatic.Vrfs.Vrf.Lsps.Lsp.Label.PathInfo.Nexthop.Address>`
                                
                                .. attribute:: label
                                
                                	Next\-Hop Label
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: interface_name
                                
                                	Next\-Hop Interface Name
                                	**type**\: str
                                
                                .. attribute:: afi
                                
                                	Next\-Hop AFI
                                	**type**\:  :py:class:`MgmtStaticLspAfi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MgmtStaticLspAfi>`
                                
                                

                                """

                                _prefix = 'mpls-static-oper'
                                _revision = '2017-05-01'

                                def __init__(self):
                                    super(MplsStatic.Vrfs.Vrf.Lsps.Lsp.Label.PathInfo.Nexthop, self).__init__()

                                    self.yang_name = "nexthop"
                                    self.yang_parent_name = "path-info"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("address", ("address", MplsStatic.Vrfs.Vrf.Lsps.Lsp.Label.PathInfo.Nexthop.Address))])
                                    self._leafs = OrderedDict([
                                        ('label', (YLeaf(YType.uint32, 'label'), ['int'])),
                                        ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                                        ('afi', (YLeaf(YType.enumeration, 'afi'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper', 'MgmtStaticLspAfi', '')])),
                                    ])
                                    self.label = None
                                    self.interface_name = None
                                    self.afi = None

                                    self.address = MplsStatic.Vrfs.Vrf.Lsps.Lsp.Label.PathInfo.Nexthop.Address()
                                    self.address.parent = self
                                    self._children_name_map["address"] = "address"
                                    self._segment_path = lambda: "nexthop"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(MplsStatic.Vrfs.Vrf.Lsps.Lsp.Label.PathInfo.Nexthop, ['label', 'interface_name', 'afi'], name, value)


                                class Address(Entity):
                                    """
                                    Next\-Hop IP Address
                                    
                                    .. attribute:: af_name
                                    
                                    	AFName
                                    	**type**\:  :py:class:`MgmtStaticAddr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MgmtStaticAddr>`
                                    
                                    .. attribute:: ipv4_prefix
                                    
                                    	IPv4 context
                                    	**type**\: str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    .. attribute:: ipv6_prefix
                                    
                                    	IPv6 context
                                    	**type**\: str
                                    
                                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                    
                                    

                                    """

                                    _prefix = 'mpls-static-oper'
                                    _revision = '2017-05-01'

                                    def __init__(self):
                                        super(MplsStatic.Vrfs.Vrf.Lsps.Lsp.Label.PathInfo.Nexthop.Address, self).__init__()

                                        self.yang_name = "address"
                                        self.yang_parent_name = "nexthop"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('af_name', (YLeaf(YType.enumeration, 'af-name'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper', 'MgmtStaticAddr', '')])),
                                            ('ipv4_prefix', (YLeaf(YType.str, 'ipv4-prefix'), ['str'])),
                                            ('ipv6_prefix', (YLeaf(YType.str, 'ipv6-prefix'), ['str'])),
                                        ])
                                        self.af_name = None
                                        self.ipv4_prefix = None
                                        self.ipv6_prefix = None
                                        self._segment_path = lambda: "address"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(MplsStatic.Vrfs.Vrf.Lsps.Lsp.Label.PathInfo.Nexthop.Address, ['af_name', 'ipv4_prefix', 'ipv6_prefix'], name, value)


                        class BackupPathInfo(Entity):
                            """
                            Backup Path Information
                            
                            .. attribute:: nexthop
                            
                            	Nexthop information
                            	**type**\:  :py:class:`Nexthop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MplsStatic.Vrfs.Vrf.Lsps.Lsp.Label.BackupPathInfo.Nexthop>`
                            
                            .. attribute:: path_number
                            
                            	Path Number
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: type
                            
                            	Path Type
                            	**type**\:  :py:class:`MgmtStaticPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MgmtStaticPath>`
                            
                            .. attribute:: path_role
                            
                            	Path Role
                            	**type**\:  :py:class:`MplsStaticPathRole <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MplsStaticPathRole>`
                            
                            .. attribute:: path_id
                            
                            	Path Id
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            .. attribute:: backup_id
                            
                            	Path Backup Id
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            .. attribute:: status
                            
                            	Path Status
                            	**type**\:  :py:class:`MgmtMplsStaticPathStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MgmtMplsStaticPathStatus>`
                            
                            

                            """

                            _prefix = 'mpls-static-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(MplsStatic.Vrfs.Vrf.Lsps.Lsp.Label.BackupPathInfo, self).__init__()

                                self.yang_name = "backup-path-info"
                                self.yang_parent_name = "label"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("nexthop", ("nexthop", MplsStatic.Vrfs.Vrf.Lsps.Lsp.Label.BackupPathInfo.Nexthop))])
                                self._leafs = OrderedDict([
                                    ('path_number', (YLeaf(YType.uint32, 'path-number'), ['int'])),
                                    ('type', (YLeaf(YType.enumeration, 'type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper', 'MgmtStaticPath', '')])),
                                    ('path_role', (YLeaf(YType.enumeration, 'path-role'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper', 'MplsStaticPathRole', '')])),
                                    ('path_id', (YLeaf(YType.uint8, 'path-id'), ['int'])),
                                    ('backup_id', (YLeaf(YType.uint8, 'backup-id'), ['int'])),
                                    ('status', (YLeaf(YType.enumeration, 'status'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper', 'MgmtMplsStaticPathStatus', '')])),
                                ])
                                self.path_number = None
                                self.type = None
                                self.path_role = None
                                self.path_id = None
                                self.backup_id = None
                                self.status = None

                                self.nexthop = MplsStatic.Vrfs.Vrf.Lsps.Lsp.Label.BackupPathInfo.Nexthop()
                                self.nexthop.parent = self
                                self._children_name_map["nexthop"] = "nexthop"
                                self._segment_path = lambda: "backup-path-info"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsStatic.Vrfs.Vrf.Lsps.Lsp.Label.BackupPathInfo, ['path_number', 'type', 'path_role', 'path_id', 'backup_id', 'status'], name, value)


                            class Nexthop(Entity):
                                """
                                Nexthop information
                                
                                .. attribute:: address
                                
                                	Next\-Hop IP Address
                                	**type**\:  :py:class:`Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MplsStatic.Vrfs.Vrf.Lsps.Lsp.Label.BackupPathInfo.Nexthop.Address>`
                                
                                .. attribute:: label
                                
                                	Next\-Hop Label
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: interface_name
                                
                                	Next\-Hop Interface Name
                                	**type**\: str
                                
                                .. attribute:: afi
                                
                                	Next\-Hop AFI
                                	**type**\:  :py:class:`MgmtStaticLspAfi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MgmtStaticLspAfi>`
                                
                                

                                """

                                _prefix = 'mpls-static-oper'
                                _revision = '2017-05-01'

                                def __init__(self):
                                    super(MplsStatic.Vrfs.Vrf.Lsps.Lsp.Label.BackupPathInfo.Nexthop, self).__init__()

                                    self.yang_name = "nexthop"
                                    self.yang_parent_name = "backup-path-info"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("address", ("address", MplsStatic.Vrfs.Vrf.Lsps.Lsp.Label.BackupPathInfo.Nexthop.Address))])
                                    self._leafs = OrderedDict([
                                        ('label', (YLeaf(YType.uint32, 'label'), ['int'])),
                                        ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                                        ('afi', (YLeaf(YType.enumeration, 'afi'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper', 'MgmtStaticLspAfi', '')])),
                                    ])
                                    self.label = None
                                    self.interface_name = None
                                    self.afi = None

                                    self.address = MplsStatic.Vrfs.Vrf.Lsps.Lsp.Label.BackupPathInfo.Nexthop.Address()
                                    self.address.parent = self
                                    self._children_name_map["address"] = "address"
                                    self._segment_path = lambda: "nexthop"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(MplsStatic.Vrfs.Vrf.Lsps.Lsp.Label.BackupPathInfo.Nexthop, ['label', 'interface_name', 'afi'], name, value)


                                class Address(Entity):
                                    """
                                    Next\-Hop IP Address
                                    
                                    .. attribute:: af_name
                                    
                                    	AFName
                                    	**type**\:  :py:class:`MgmtStaticAddr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MgmtStaticAddr>`
                                    
                                    .. attribute:: ipv4_prefix
                                    
                                    	IPv4 context
                                    	**type**\: str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    .. attribute:: ipv6_prefix
                                    
                                    	IPv6 context
                                    	**type**\: str
                                    
                                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                    
                                    

                                    """

                                    _prefix = 'mpls-static-oper'
                                    _revision = '2017-05-01'

                                    def __init__(self):
                                        super(MplsStatic.Vrfs.Vrf.Lsps.Lsp.Label.BackupPathInfo.Nexthop.Address, self).__init__()

                                        self.yang_name = "address"
                                        self.yang_parent_name = "nexthop"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('af_name', (YLeaf(YType.enumeration, 'af-name'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper', 'MgmtStaticAddr', '')])),
                                            ('ipv4_prefix', (YLeaf(YType.str, 'ipv4-prefix'), ['str'])),
                                            ('ipv6_prefix', (YLeaf(YType.str, 'ipv6-prefix'), ['str'])),
                                        ])
                                        self.af_name = None
                                        self.ipv4_prefix = None
                                        self.ipv6_prefix = None
                                        self._segment_path = lambda: "address"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(MplsStatic.Vrfs.Vrf.Lsps.Lsp.Label.BackupPathInfo.Nexthop.Address, ['af_name', 'ipv4_prefix', 'ipv6_prefix'], name, value)


            class LocalLabels(Entity):
                """
                data for static local\-label table
                
                .. attribute:: local_label
                
                	Data for static label
                	**type**\: list of  		 :py:class:`LocalLabel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MplsStatic.Vrfs.Vrf.LocalLabels.LocalLabel>`
                
                

                """

                _prefix = 'mpls-static-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(MplsStatic.Vrfs.Vrf.LocalLabels, self).__init__()

                    self.yang_name = "local-labels"
                    self.yang_parent_name = "vrf"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("local-label", ("local_label", MplsStatic.Vrfs.Vrf.LocalLabels.LocalLabel))])
                    self._leafs = OrderedDict()

                    self.local_label = YList(self)
                    self._segment_path = lambda: "local-labels"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsStatic.Vrfs.Vrf.LocalLabels, [], name, value)


                class LocalLabel(Entity):
                    """
                    Data for static label
                    
                    .. attribute:: local_label_id  (key)
                    
                    	Local Label
                    	**type**\: int
                    
                    	**range:** 16..1048575
                    
                    .. attribute:: prefix
                    
                    	Prefix Information
                    	**type**\:  :py:class:`Prefix <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MplsStatic.Vrfs.Vrf.LocalLabels.LocalLabel.Prefix>`
                    
                    .. attribute:: pathset_resolve_nh
                    
                    	Primary pathset resolve\-nexthop IP Address
                    	**type**\:  :py:class:`PathsetResolveNh <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MplsStatic.Vrfs.Vrf.LocalLabels.LocalLabel.PathsetResolveNh>`
                    
                    .. attribute:: backup_pathset_resolve_nh
                    
                    	Backup pathset resolve\-nexthop IP Address
                    	**type**\:  :py:class:`BackupPathsetResolveNh <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MplsStatic.Vrfs.Vrf.LocalLabels.LocalLabel.BackupPathsetResolveNh>`
                    
                    .. attribute:: label
                    
                    	Label value
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: label_mode
                    
                    	Label Mode
                    	**type**\:  :py:class:`MgmtMplsStaticLabelMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MgmtMplsStaticLabelMode>`
                    
                    .. attribute:: label_status
                    
                    	Label Status
                    	**type**\:  :py:class:`MgmtMplsStaticLabelStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MgmtMplsStaticLabelStatus>`
                    
                    .. attribute:: vrf_name
                    
                    	VRF name
                    	**type**\: str
                    
                    .. attribute:: pathset_via_resolve
                    
                    	Primary Pathset as a result of resolve
                    	**type**\: bool
                    
                    .. attribute:: backup_pathset_via_resolve
                    
                    	Backup Pathset as a result of resolve
                    	**type**\: bool
                    
                    .. attribute:: address_family
                    
                    	Address Family
                    	**type**\:  :py:class:`MgmtStaticAddr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MgmtStaticAddr>`
                    
                    .. attribute:: path_info
                    
                    	Path Information
                    	**type**\: list of  		 :py:class:`PathInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MplsStatic.Vrfs.Vrf.LocalLabels.LocalLabel.PathInfo>`
                    
                    .. attribute:: backup_path_info
                    
                    	Backup Path Information
                    	**type**\: list of  		 :py:class:`BackupPathInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MplsStatic.Vrfs.Vrf.LocalLabels.LocalLabel.BackupPathInfo>`
                    
                    

                    """

                    _prefix = 'mpls-static-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(MplsStatic.Vrfs.Vrf.LocalLabels.LocalLabel, self).__init__()

                        self.yang_name = "local-label"
                        self.yang_parent_name = "local-labels"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['local_label_id']
                        self._child_classes = OrderedDict([("prefix", ("prefix", MplsStatic.Vrfs.Vrf.LocalLabels.LocalLabel.Prefix)), ("pathset-resolve-nh", ("pathset_resolve_nh", MplsStatic.Vrfs.Vrf.LocalLabels.LocalLabel.PathsetResolveNh)), ("backup-pathset-resolve-nh", ("backup_pathset_resolve_nh", MplsStatic.Vrfs.Vrf.LocalLabels.LocalLabel.BackupPathsetResolveNh)), ("path-info", ("path_info", MplsStatic.Vrfs.Vrf.LocalLabels.LocalLabel.PathInfo)), ("backup-path-info", ("backup_path_info", MplsStatic.Vrfs.Vrf.LocalLabels.LocalLabel.BackupPathInfo))])
                        self._leafs = OrderedDict([
                            ('local_label_id', (YLeaf(YType.uint32, 'local-label-id'), ['int'])),
                            ('label', (YLeaf(YType.uint32, 'label'), ['int'])),
                            ('label_mode', (YLeaf(YType.enumeration, 'label-mode'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper', 'MgmtMplsStaticLabelMode', '')])),
                            ('label_status', (YLeaf(YType.enumeration, 'label-status'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper', 'MgmtMplsStaticLabelStatus', '')])),
                            ('vrf_name', (YLeaf(YType.str, 'vrf-name'), ['str'])),
                            ('pathset_via_resolve', (YLeaf(YType.boolean, 'pathset-via-resolve'), ['bool'])),
                            ('backup_pathset_via_resolve', (YLeaf(YType.boolean, 'backup-pathset-via-resolve'), ['bool'])),
                            ('address_family', (YLeaf(YType.enumeration, 'address-family'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper', 'MgmtStaticAddr', '')])),
                        ])
                        self.local_label_id = None
                        self.label = None
                        self.label_mode = None
                        self.label_status = None
                        self.vrf_name = None
                        self.pathset_via_resolve = None
                        self.backup_pathset_via_resolve = None
                        self.address_family = None

                        self.prefix = MplsStatic.Vrfs.Vrf.LocalLabels.LocalLabel.Prefix()
                        self.prefix.parent = self
                        self._children_name_map["prefix"] = "prefix"

                        self.pathset_resolve_nh = MplsStatic.Vrfs.Vrf.LocalLabels.LocalLabel.PathsetResolveNh()
                        self.pathset_resolve_nh.parent = self
                        self._children_name_map["pathset_resolve_nh"] = "pathset-resolve-nh"

                        self.backup_pathset_resolve_nh = MplsStatic.Vrfs.Vrf.LocalLabels.LocalLabel.BackupPathsetResolveNh()
                        self.backup_pathset_resolve_nh.parent = self
                        self._children_name_map["backup_pathset_resolve_nh"] = "backup-pathset-resolve-nh"

                        self.path_info = YList(self)
                        self.backup_path_info = YList(self)
                        self._segment_path = lambda: "local-label" + "[local-label-id='" + str(self.local_label_id) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(MplsStatic.Vrfs.Vrf.LocalLabels.LocalLabel, ['local_label_id', 'label', 'label_mode', 'label_status', 'vrf_name', 'pathset_via_resolve', 'backup_pathset_via_resolve', 'address_family'], name, value)


                    class Prefix(Entity):
                        """
                        Prefix Information
                        
                        .. attribute:: prefix
                        
                        	Prefix
                        	**type**\:  :py:class:`Prefix_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MplsStatic.Vrfs.Vrf.LocalLabels.LocalLabel.Prefix.Prefix_>`
                        
                        .. attribute:: prefix_length
                        
                        	Prefix length
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        

                        """

                        _prefix = 'mpls-static-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(MplsStatic.Vrfs.Vrf.LocalLabels.LocalLabel.Prefix, self).__init__()

                            self.yang_name = "prefix"
                            self.yang_parent_name = "local-label"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("prefix", ("prefix", MplsStatic.Vrfs.Vrf.LocalLabels.LocalLabel.Prefix.Prefix_))])
                            self._leafs = OrderedDict([
                                ('prefix_length', (YLeaf(YType.uint8, 'prefix-length'), ['int'])),
                            ])
                            self.prefix_length = None

                            self.prefix = MplsStatic.Vrfs.Vrf.LocalLabels.LocalLabel.Prefix.Prefix_()
                            self.prefix.parent = self
                            self._children_name_map["prefix"] = "prefix"
                            self._segment_path = lambda: "prefix"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(MplsStatic.Vrfs.Vrf.LocalLabels.LocalLabel.Prefix, ['prefix_length'], name, value)


                        class Prefix_(Entity):
                            """
                            Prefix
                            
                            .. attribute:: af_name
                            
                            	AFName
                            	**type**\:  :py:class:`MgmtStaticAddr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MgmtStaticAddr>`
                            
                            .. attribute:: ipv4_prefix
                            
                            	IPv4 context
                            	**type**\: str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: ipv6_prefix
                            
                            	IPv6 context
                            	**type**\: str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            

                            """

                            _prefix = 'mpls-static-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(MplsStatic.Vrfs.Vrf.LocalLabels.LocalLabel.Prefix.Prefix_, self).__init__()

                                self.yang_name = "prefix"
                                self.yang_parent_name = "prefix"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('af_name', (YLeaf(YType.enumeration, 'af-name'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper', 'MgmtStaticAddr', '')])),
                                    ('ipv4_prefix', (YLeaf(YType.str, 'ipv4-prefix'), ['str'])),
                                    ('ipv6_prefix', (YLeaf(YType.str, 'ipv6-prefix'), ['str'])),
                                ])
                                self.af_name = None
                                self.ipv4_prefix = None
                                self.ipv6_prefix = None
                                self._segment_path = lambda: "prefix"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsStatic.Vrfs.Vrf.LocalLabels.LocalLabel.Prefix.Prefix_, ['af_name', 'ipv4_prefix', 'ipv6_prefix'], name, value)


                    class PathsetResolveNh(Entity):
                        """
                        Primary pathset resolve\-nexthop IP Address
                        
                        .. attribute:: af_name
                        
                        	AFName
                        	**type**\:  :py:class:`MgmtStaticAddr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MgmtStaticAddr>`
                        
                        .. attribute:: ipv4_prefix
                        
                        	IPv4 context
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: ipv6_prefix
                        
                        	IPv6 context
                        	**type**\: str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        

                        """

                        _prefix = 'mpls-static-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(MplsStatic.Vrfs.Vrf.LocalLabels.LocalLabel.PathsetResolveNh, self).__init__()

                            self.yang_name = "pathset-resolve-nh"
                            self.yang_parent_name = "local-label"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('af_name', (YLeaf(YType.enumeration, 'af-name'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper', 'MgmtStaticAddr', '')])),
                                ('ipv4_prefix', (YLeaf(YType.str, 'ipv4-prefix'), ['str'])),
                                ('ipv6_prefix', (YLeaf(YType.str, 'ipv6-prefix'), ['str'])),
                            ])
                            self.af_name = None
                            self.ipv4_prefix = None
                            self.ipv6_prefix = None
                            self._segment_path = lambda: "pathset-resolve-nh"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(MplsStatic.Vrfs.Vrf.LocalLabels.LocalLabel.PathsetResolveNh, ['af_name', 'ipv4_prefix', 'ipv6_prefix'], name, value)


                    class BackupPathsetResolveNh(Entity):
                        """
                        Backup pathset resolve\-nexthop IP Address
                        
                        .. attribute:: af_name
                        
                        	AFName
                        	**type**\:  :py:class:`MgmtStaticAddr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MgmtStaticAddr>`
                        
                        .. attribute:: ipv4_prefix
                        
                        	IPv4 context
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: ipv6_prefix
                        
                        	IPv6 context
                        	**type**\: str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        

                        """

                        _prefix = 'mpls-static-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(MplsStatic.Vrfs.Vrf.LocalLabels.LocalLabel.BackupPathsetResolveNh, self).__init__()

                            self.yang_name = "backup-pathset-resolve-nh"
                            self.yang_parent_name = "local-label"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('af_name', (YLeaf(YType.enumeration, 'af-name'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper', 'MgmtStaticAddr', '')])),
                                ('ipv4_prefix', (YLeaf(YType.str, 'ipv4-prefix'), ['str'])),
                                ('ipv6_prefix', (YLeaf(YType.str, 'ipv6-prefix'), ['str'])),
                            ])
                            self.af_name = None
                            self.ipv4_prefix = None
                            self.ipv6_prefix = None
                            self._segment_path = lambda: "backup-pathset-resolve-nh"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(MplsStatic.Vrfs.Vrf.LocalLabels.LocalLabel.BackupPathsetResolveNh, ['af_name', 'ipv4_prefix', 'ipv6_prefix'], name, value)


                    class PathInfo(Entity):
                        """
                        Path Information
                        
                        .. attribute:: nexthop
                        
                        	Nexthop information
                        	**type**\:  :py:class:`Nexthop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MplsStatic.Vrfs.Vrf.LocalLabels.LocalLabel.PathInfo.Nexthop>`
                        
                        .. attribute:: path_number
                        
                        	Path Number
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: type
                        
                        	Path Type
                        	**type**\:  :py:class:`MgmtStaticPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MgmtStaticPath>`
                        
                        .. attribute:: path_role
                        
                        	Path Role
                        	**type**\:  :py:class:`MplsStaticPathRole <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MplsStaticPathRole>`
                        
                        .. attribute:: path_id
                        
                        	Path Id
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        .. attribute:: backup_id
                        
                        	Path Backup Id
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        .. attribute:: status
                        
                        	Path Status
                        	**type**\:  :py:class:`MgmtMplsStaticPathStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MgmtMplsStaticPathStatus>`
                        
                        

                        """

                        _prefix = 'mpls-static-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(MplsStatic.Vrfs.Vrf.LocalLabels.LocalLabel.PathInfo, self).__init__()

                            self.yang_name = "path-info"
                            self.yang_parent_name = "local-label"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("nexthop", ("nexthop", MplsStatic.Vrfs.Vrf.LocalLabels.LocalLabel.PathInfo.Nexthop))])
                            self._leafs = OrderedDict([
                                ('path_number', (YLeaf(YType.uint32, 'path-number'), ['int'])),
                                ('type', (YLeaf(YType.enumeration, 'type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper', 'MgmtStaticPath', '')])),
                                ('path_role', (YLeaf(YType.enumeration, 'path-role'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper', 'MplsStaticPathRole', '')])),
                                ('path_id', (YLeaf(YType.uint8, 'path-id'), ['int'])),
                                ('backup_id', (YLeaf(YType.uint8, 'backup-id'), ['int'])),
                                ('status', (YLeaf(YType.enumeration, 'status'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper', 'MgmtMplsStaticPathStatus', '')])),
                            ])
                            self.path_number = None
                            self.type = None
                            self.path_role = None
                            self.path_id = None
                            self.backup_id = None
                            self.status = None

                            self.nexthop = MplsStatic.Vrfs.Vrf.LocalLabels.LocalLabel.PathInfo.Nexthop()
                            self.nexthop.parent = self
                            self._children_name_map["nexthop"] = "nexthop"
                            self._segment_path = lambda: "path-info"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(MplsStatic.Vrfs.Vrf.LocalLabels.LocalLabel.PathInfo, ['path_number', 'type', 'path_role', 'path_id', 'backup_id', 'status'], name, value)


                        class Nexthop(Entity):
                            """
                            Nexthop information
                            
                            .. attribute:: address
                            
                            	Next\-Hop IP Address
                            	**type**\:  :py:class:`Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MplsStatic.Vrfs.Vrf.LocalLabels.LocalLabel.PathInfo.Nexthop.Address>`
                            
                            .. attribute:: label
                            
                            	Next\-Hop Label
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: interface_name
                            
                            	Next\-Hop Interface Name
                            	**type**\: str
                            
                            .. attribute:: afi
                            
                            	Next\-Hop AFI
                            	**type**\:  :py:class:`MgmtStaticLspAfi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MgmtStaticLspAfi>`
                            
                            

                            """

                            _prefix = 'mpls-static-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(MplsStatic.Vrfs.Vrf.LocalLabels.LocalLabel.PathInfo.Nexthop, self).__init__()

                                self.yang_name = "nexthop"
                                self.yang_parent_name = "path-info"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("address", ("address", MplsStatic.Vrfs.Vrf.LocalLabels.LocalLabel.PathInfo.Nexthop.Address))])
                                self._leafs = OrderedDict([
                                    ('label', (YLeaf(YType.uint32, 'label'), ['int'])),
                                    ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                                    ('afi', (YLeaf(YType.enumeration, 'afi'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper', 'MgmtStaticLspAfi', '')])),
                                ])
                                self.label = None
                                self.interface_name = None
                                self.afi = None

                                self.address = MplsStatic.Vrfs.Vrf.LocalLabels.LocalLabel.PathInfo.Nexthop.Address()
                                self.address.parent = self
                                self._children_name_map["address"] = "address"
                                self._segment_path = lambda: "nexthop"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsStatic.Vrfs.Vrf.LocalLabels.LocalLabel.PathInfo.Nexthop, ['label', 'interface_name', 'afi'], name, value)


                            class Address(Entity):
                                """
                                Next\-Hop IP Address
                                
                                .. attribute:: af_name
                                
                                	AFName
                                	**type**\:  :py:class:`MgmtStaticAddr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MgmtStaticAddr>`
                                
                                .. attribute:: ipv4_prefix
                                
                                	IPv4 context
                                	**type**\: str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: ipv6_prefix
                                
                                	IPv6 context
                                	**type**\: str
                                
                                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                
                                

                                """

                                _prefix = 'mpls-static-oper'
                                _revision = '2017-05-01'

                                def __init__(self):
                                    super(MplsStatic.Vrfs.Vrf.LocalLabels.LocalLabel.PathInfo.Nexthop.Address, self).__init__()

                                    self.yang_name = "address"
                                    self.yang_parent_name = "nexthop"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('af_name', (YLeaf(YType.enumeration, 'af-name'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper', 'MgmtStaticAddr', '')])),
                                        ('ipv4_prefix', (YLeaf(YType.str, 'ipv4-prefix'), ['str'])),
                                        ('ipv6_prefix', (YLeaf(YType.str, 'ipv6-prefix'), ['str'])),
                                    ])
                                    self.af_name = None
                                    self.ipv4_prefix = None
                                    self.ipv6_prefix = None
                                    self._segment_path = lambda: "address"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(MplsStatic.Vrfs.Vrf.LocalLabels.LocalLabel.PathInfo.Nexthop.Address, ['af_name', 'ipv4_prefix', 'ipv6_prefix'], name, value)


                    class BackupPathInfo(Entity):
                        """
                        Backup Path Information
                        
                        .. attribute:: nexthop
                        
                        	Nexthop information
                        	**type**\:  :py:class:`Nexthop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MplsStatic.Vrfs.Vrf.LocalLabels.LocalLabel.BackupPathInfo.Nexthop>`
                        
                        .. attribute:: path_number
                        
                        	Path Number
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: type
                        
                        	Path Type
                        	**type**\:  :py:class:`MgmtStaticPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MgmtStaticPath>`
                        
                        .. attribute:: path_role
                        
                        	Path Role
                        	**type**\:  :py:class:`MplsStaticPathRole <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MplsStaticPathRole>`
                        
                        .. attribute:: path_id
                        
                        	Path Id
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        .. attribute:: backup_id
                        
                        	Path Backup Id
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        .. attribute:: status
                        
                        	Path Status
                        	**type**\:  :py:class:`MgmtMplsStaticPathStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MgmtMplsStaticPathStatus>`
                        
                        

                        """

                        _prefix = 'mpls-static-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(MplsStatic.Vrfs.Vrf.LocalLabels.LocalLabel.BackupPathInfo, self).__init__()

                            self.yang_name = "backup-path-info"
                            self.yang_parent_name = "local-label"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("nexthop", ("nexthop", MplsStatic.Vrfs.Vrf.LocalLabels.LocalLabel.BackupPathInfo.Nexthop))])
                            self._leafs = OrderedDict([
                                ('path_number', (YLeaf(YType.uint32, 'path-number'), ['int'])),
                                ('type', (YLeaf(YType.enumeration, 'type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper', 'MgmtStaticPath', '')])),
                                ('path_role', (YLeaf(YType.enumeration, 'path-role'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper', 'MplsStaticPathRole', '')])),
                                ('path_id', (YLeaf(YType.uint8, 'path-id'), ['int'])),
                                ('backup_id', (YLeaf(YType.uint8, 'backup-id'), ['int'])),
                                ('status', (YLeaf(YType.enumeration, 'status'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper', 'MgmtMplsStaticPathStatus', '')])),
                            ])
                            self.path_number = None
                            self.type = None
                            self.path_role = None
                            self.path_id = None
                            self.backup_id = None
                            self.status = None

                            self.nexthop = MplsStatic.Vrfs.Vrf.LocalLabels.LocalLabel.BackupPathInfo.Nexthop()
                            self.nexthop.parent = self
                            self._children_name_map["nexthop"] = "nexthop"
                            self._segment_path = lambda: "backup-path-info"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(MplsStatic.Vrfs.Vrf.LocalLabels.LocalLabel.BackupPathInfo, ['path_number', 'type', 'path_role', 'path_id', 'backup_id', 'status'], name, value)


                        class Nexthop(Entity):
                            """
                            Nexthop information
                            
                            .. attribute:: address
                            
                            	Next\-Hop IP Address
                            	**type**\:  :py:class:`Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MplsStatic.Vrfs.Vrf.LocalLabels.LocalLabel.BackupPathInfo.Nexthop.Address>`
                            
                            .. attribute:: label
                            
                            	Next\-Hop Label
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: interface_name
                            
                            	Next\-Hop Interface Name
                            	**type**\: str
                            
                            .. attribute:: afi
                            
                            	Next\-Hop AFI
                            	**type**\:  :py:class:`MgmtStaticLspAfi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MgmtStaticLspAfi>`
                            
                            

                            """

                            _prefix = 'mpls-static-oper'
                            _revision = '2017-05-01'

                            def __init__(self):
                                super(MplsStatic.Vrfs.Vrf.LocalLabels.LocalLabel.BackupPathInfo.Nexthop, self).__init__()

                                self.yang_name = "nexthop"
                                self.yang_parent_name = "backup-path-info"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("address", ("address", MplsStatic.Vrfs.Vrf.LocalLabels.LocalLabel.BackupPathInfo.Nexthop.Address))])
                                self._leafs = OrderedDict([
                                    ('label', (YLeaf(YType.uint32, 'label'), ['int'])),
                                    ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                                    ('afi', (YLeaf(YType.enumeration, 'afi'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper', 'MgmtStaticLspAfi', '')])),
                                ])
                                self.label = None
                                self.interface_name = None
                                self.afi = None

                                self.address = MplsStatic.Vrfs.Vrf.LocalLabels.LocalLabel.BackupPathInfo.Nexthop.Address()
                                self.address.parent = self
                                self._children_name_map["address"] = "address"
                                self._segment_path = lambda: "nexthop"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(MplsStatic.Vrfs.Vrf.LocalLabels.LocalLabel.BackupPathInfo.Nexthop, ['label', 'interface_name', 'afi'], name, value)


                            class Address(Entity):
                                """
                                Next\-Hop IP Address
                                
                                .. attribute:: af_name
                                
                                	AFName
                                	**type**\:  :py:class:`MgmtStaticAddr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MgmtStaticAddr>`
                                
                                .. attribute:: ipv4_prefix
                                
                                	IPv4 context
                                	**type**\: str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: ipv6_prefix
                                
                                	IPv6 context
                                	**type**\: str
                                
                                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                
                                

                                """

                                _prefix = 'mpls-static-oper'
                                _revision = '2017-05-01'

                                def __init__(self):
                                    super(MplsStatic.Vrfs.Vrf.LocalLabels.LocalLabel.BackupPathInfo.Nexthop.Address, self).__init__()

                                    self.yang_name = "address"
                                    self.yang_parent_name = "nexthop"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('af_name', (YLeaf(YType.enumeration, 'af-name'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper', 'MgmtStaticAddr', '')])),
                                        ('ipv4_prefix', (YLeaf(YType.str, 'ipv4-prefix'), ['str'])),
                                        ('ipv6_prefix', (YLeaf(YType.str, 'ipv6-prefix'), ['str'])),
                                    ])
                                    self.af_name = None
                                    self.ipv4_prefix = None
                                    self.ipv6_prefix = None
                                    self._segment_path = lambda: "address"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(MplsStatic.Vrfs.Vrf.LocalLabels.LocalLabel.BackupPathInfo.Nexthop.Address, ['af_name', 'ipv4_prefix', 'ipv6_prefix'], name, value)


    class Summary(Entity):
        """
        MPLS STATIC summary data
        
        .. attribute:: lsp_count
        
        	Total Number of LSPs
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: label_count
        
        	Total Number of Labels
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: label_error_count
        
        	Total Number of Labels with Errors
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: label_discrepancy_count
        
        	Total Number of Labels with Discrepancies
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: vrf_count
        
        	Total Number of VRF configured
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: active_vrf_count
        
        	Total Number of Active VRF Active
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: interface_count
        
        	Total Number of Interface
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: interface_foward_reference_count
        
        	Total Number of Active Interface
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: mpls_enabled_interface_count
        
        	Total Number of MPLS enabled Interface
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipv4_res_nh_count
        
        	Total Number of IPv4 ResolveNextHops
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipv6_res_nh_count
        
        	Total Number of IPv6 ResoleNextHops
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: lsd_connected
        
        	LSD connection is up
        	**type**\: bool
        
        .. attribute:: im_connected
        
        	IM is connected
        	**type**\: bool
        
        .. attribute:: rsi_connected
        
        	RSI is connected
        	**type**\: bool
        
        .. attribute:: ribv4_connected
        
        	RIBv4 is connected
        	**type**\: bool
        
        .. attribute:: ribv6_connected
        
        	RIBv6 is connected
        	**type**\: bool
        
        

        """

        _prefix = 'mpls-static-oper'
        _revision = '2017-05-01'

        def __init__(self):
            super(MplsStatic.Summary, self).__init__()

            self.yang_name = "summary"
            self.yang_parent_name = "mpls-static"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('lsp_count', (YLeaf(YType.uint32, 'lsp-count'), ['int'])),
                ('label_count', (YLeaf(YType.uint32, 'label-count'), ['int'])),
                ('label_error_count', (YLeaf(YType.uint32, 'label-error-count'), ['int'])),
                ('label_discrepancy_count', (YLeaf(YType.uint32, 'label-discrepancy-count'), ['int'])),
                ('vrf_count', (YLeaf(YType.uint32, 'vrf-count'), ['int'])),
                ('active_vrf_count', (YLeaf(YType.uint32, 'active-vrf-count'), ['int'])),
                ('interface_count', (YLeaf(YType.uint32, 'interface-count'), ['int'])),
                ('interface_foward_reference_count', (YLeaf(YType.uint32, 'interface-foward-reference-count'), ['int'])),
                ('mpls_enabled_interface_count', (YLeaf(YType.uint32, 'mpls-enabled-interface-count'), ['int'])),
                ('ipv4_res_nh_count', (YLeaf(YType.uint32, 'ipv4-res-nh-count'), ['int'])),
                ('ipv6_res_nh_count', (YLeaf(YType.uint32, 'ipv6-res-nh-count'), ['int'])),
                ('lsd_connected', (YLeaf(YType.boolean, 'lsd-connected'), ['bool'])),
                ('im_connected', (YLeaf(YType.boolean, 'im-connected'), ['bool'])),
                ('rsi_connected', (YLeaf(YType.boolean, 'rsi-connected'), ['bool'])),
                ('ribv4_connected', (YLeaf(YType.boolean, 'ribv4-connected'), ['bool'])),
                ('ribv6_connected', (YLeaf(YType.boolean, 'ribv6-connected'), ['bool'])),
            ])
            self.lsp_count = None
            self.label_count = None
            self.label_error_count = None
            self.label_discrepancy_count = None
            self.vrf_count = None
            self.active_vrf_count = None
            self.interface_count = None
            self.interface_foward_reference_count = None
            self.mpls_enabled_interface_count = None
            self.ipv4_res_nh_count = None
            self.ipv6_res_nh_count = None
            self.lsd_connected = None
            self.im_connected = None
            self.rsi_connected = None
            self.ribv4_connected = None
            self.ribv6_connected = None
            self._segment_path = lambda: "summary"
            self._absolute_path = lambda: "Cisco-IOS-XR-mpls-static-oper:mpls-static/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(MplsStatic.Summary, ['lsp_count', 'label_count', 'label_error_count', 'label_discrepancy_count', 'vrf_count', 'active_vrf_count', 'interface_count', 'interface_foward_reference_count', 'mpls_enabled_interface_count', 'ipv4_res_nh_count', 'ipv6_res_nh_count', 'lsd_connected', 'im_connected', 'rsi_connected', 'ribv4_connected', 'ribv6_connected'], name, value)


    class LocalLabels(Entity):
        """
        data for static local\-label table
        
        .. attribute:: local_label
        
        	Data for static label
        	**type**\: list of  		 :py:class:`LocalLabel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MplsStatic.LocalLabels.LocalLabel>`
        
        

        """

        _prefix = 'mpls-static-oper'
        _revision = '2017-05-01'

        def __init__(self):
            super(MplsStatic.LocalLabels, self).__init__()

            self.yang_name = "local-labels"
            self.yang_parent_name = "mpls-static"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("local-label", ("local_label", MplsStatic.LocalLabels.LocalLabel))])
            self._leafs = OrderedDict()

            self.local_label = YList(self)
            self._segment_path = lambda: "local-labels"
            self._absolute_path = lambda: "Cisco-IOS-XR-mpls-static-oper:mpls-static/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(MplsStatic.LocalLabels, [], name, value)


        class LocalLabel(Entity):
            """
            Data for static label
            
            .. attribute:: local_label_id  (key)
            
            	Local Label
            	**type**\: int
            
            	**range:** 16..1048575
            
            .. attribute:: prefix
            
            	Prefix Information
            	**type**\:  :py:class:`Prefix <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MplsStatic.LocalLabels.LocalLabel.Prefix>`
            
            .. attribute:: pathset_resolve_nh
            
            	Primary pathset resolve\-nexthop IP Address
            	**type**\:  :py:class:`PathsetResolveNh <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MplsStatic.LocalLabels.LocalLabel.PathsetResolveNh>`
            
            .. attribute:: backup_pathset_resolve_nh
            
            	Backup pathset resolve\-nexthop IP Address
            	**type**\:  :py:class:`BackupPathsetResolveNh <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MplsStatic.LocalLabels.LocalLabel.BackupPathsetResolveNh>`
            
            .. attribute:: label
            
            	Label value
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: label_mode
            
            	Label Mode
            	**type**\:  :py:class:`MgmtMplsStaticLabelMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MgmtMplsStaticLabelMode>`
            
            .. attribute:: label_status
            
            	Label Status
            	**type**\:  :py:class:`MgmtMplsStaticLabelStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MgmtMplsStaticLabelStatus>`
            
            .. attribute:: vrf_name
            
            	VRF name
            	**type**\: str
            
            .. attribute:: pathset_via_resolve
            
            	Primary Pathset as a result of resolve
            	**type**\: bool
            
            .. attribute:: backup_pathset_via_resolve
            
            	Backup Pathset as a result of resolve
            	**type**\: bool
            
            .. attribute:: address_family
            
            	Address Family
            	**type**\:  :py:class:`MgmtStaticAddr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MgmtStaticAddr>`
            
            .. attribute:: path_info
            
            	Path Information
            	**type**\: list of  		 :py:class:`PathInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MplsStatic.LocalLabels.LocalLabel.PathInfo>`
            
            .. attribute:: backup_path_info
            
            	Backup Path Information
            	**type**\: list of  		 :py:class:`BackupPathInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MplsStatic.LocalLabels.LocalLabel.BackupPathInfo>`
            
            

            """

            _prefix = 'mpls-static-oper'
            _revision = '2017-05-01'

            def __init__(self):
                super(MplsStatic.LocalLabels.LocalLabel, self).__init__()

                self.yang_name = "local-label"
                self.yang_parent_name = "local-labels"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['local_label_id']
                self._child_classes = OrderedDict([("prefix", ("prefix", MplsStatic.LocalLabels.LocalLabel.Prefix)), ("pathset-resolve-nh", ("pathset_resolve_nh", MplsStatic.LocalLabels.LocalLabel.PathsetResolveNh)), ("backup-pathset-resolve-nh", ("backup_pathset_resolve_nh", MplsStatic.LocalLabels.LocalLabel.BackupPathsetResolveNh)), ("path-info", ("path_info", MplsStatic.LocalLabels.LocalLabel.PathInfo)), ("backup-path-info", ("backup_path_info", MplsStatic.LocalLabels.LocalLabel.BackupPathInfo))])
                self._leafs = OrderedDict([
                    ('local_label_id', (YLeaf(YType.uint32, 'local-label-id'), ['int'])),
                    ('label', (YLeaf(YType.uint32, 'label'), ['int'])),
                    ('label_mode', (YLeaf(YType.enumeration, 'label-mode'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper', 'MgmtMplsStaticLabelMode', '')])),
                    ('label_status', (YLeaf(YType.enumeration, 'label-status'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper', 'MgmtMplsStaticLabelStatus', '')])),
                    ('vrf_name', (YLeaf(YType.str, 'vrf-name'), ['str'])),
                    ('pathset_via_resolve', (YLeaf(YType.boolean, 'pathset-via-resolve'), ['bool'])),
                    ('backup_pathset_via_resolve', (YLeaf(YType.boolean, 'backup-pathset-via-resolve'), ['bool'])),
                    ('address_family', (YLeaf(YType.enumeration, 'address-family'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper', 'MgmtStaticAddr', '')])),
                ])
                self.local_label_id = None
                self.label = None
                self.label_mode = None
                self.label_status = None
                self.vrf_name = None
                self.pathset_via_resolve = None
                self.backup_pathset_via_resolve = None
                self.address_family = None

                self.prefix = MplsStatic.LocalLabels.LocalLabel.Prefix()
                self.prefix.parent = self
                self._children_name_map["prefix"] = "prefix"

                self.pathset_resolve_nh = MplsStatic.LocalLabels.LocalLabel.PathsetResolveNh()
                self.pathset_resolve_nh.parent = self
                self._children_name_map["pathset_resolve_nh"] = "pathset-resolve-nh"

                self.backup_pathset_resolve_nh = MplsStatic.LocalLabels.LocalLabel.BackupPathsetResolveNh()
                self.backup_pathset_resolve_nh.parent = self
                self._children_name_map["backup_pathset_resolve_nh"] = "backup-pathset-resolve-nh"

                self.path_info = YList(self)
                self.backup_path_info = YList(self)
                self._segment_path = lambda: "local-label" + "[local-label-id='" + str(self.local_label_id) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-mpls-static-oper:mpls-static/local-labels/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(MplsStatic.LocalLabels.LocalLabel, ['local_label_id', 'label', 'label_mode', 'label_status', 'vrf_name', 'pathset_via_resolve', 'backup_pathset_via_resolve', 'address_family'], name, value)


            class Prefix(Entity):
                """
                Prefix Information
                
                .. attribute:: prefix
                
                	Prefix
                	**type**\:  :py:class:`Prefix_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MplsStatic.LocalLabels.LocalLabel.Prefix.Prefix_>`
                
                .. attribute:: prefix_length
                
                	Prefix length
                	**type**\: int
                
                	**range:** 0..255
                
                

                """

                _prefix = 'mpls-static-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(MplsStatic.LocalLabels.LocalLabel.Prefix, self).__init__()

                    self.yang_name = "prefix"
                    self.yang_parent_name = "local-label"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("prefix", ("prefix", MplsStatic.LocalLabels.LocalLabel.Prefix.Prefix_))])
                    self._leafs = OrderedDict([
                        ('prefix_length', (YLeaf(YType.uint8, 'prefix-length'), ['int'])),
                    ])
                    self.prefix_length = None

                    self.prefix = MplsStatic.LocalLabels.LocalLabel.Prefix.Prefix_()
                    self.prefix.parent = self
                    self._children_name_map["prefix"] = "prefix"
                    self._segment_path = lambda: "prefix"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsStatic.LocalLabels.LocalLabel.Prefix, ['prefix_length'], name, value)


                class Prefix_(Entity):
                    """
                    Prefix
                    
                    .. attribute:: af_name
                    
                    	AFName
                    	**type**\:  :py:class:`MgmtStaticAddr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MgmtStaticAddr>`
                    
                    .. attribute:: ipv4_prefix
                    
                    	IPv4 context
                    	**type**\: str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: ipv6_prefix
                    
                    	IPv6 context
                    	**type**\: str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    

                    """

                    _prefix = 'mpls-static-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(MplsStatic.LocalLabels.LocalLabel.Prefix.Prefix_, self).__init__()

                        self.yang_name = "prefix"
                        self.yang_parent_name = "prefix"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('af_name', (YLeaf(YType.enumeration, 'af-name'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper', 'MgmtStaticAddr', '')])),
                            ('ipv4_prefix', (YLeaf(YType.str, 'ipv4-prefix'), ['str'])),
                            ('ipv6_prefix', (YLeaf(YType.str, 'ipv6-prefix'), ['str'])),
                        ])
                        self.af_name = None
                        self.ipv4_prefix = None
                        self.ipv6_prefix = None
                        self._segment_path = lambda: "prefix"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(MplsStatic.LocalLabels.LocalLabel.Prefix.Prefix_, ['af_name', 'ipv4_prefix', 'ipv6_prefix'], name, value)


            class PathsetResolveNh(Entity):
                """
                Primary pathset resolve\-nexthop IP Address
                
                .. attribute:: af_name
                
                	AFName
                	**type**\:  :py:class:`MgmtStaticAddr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MgmtStaticAddr>`
                
                .. attribute:: ipv4_prefix
                
                	IPv4 context
                	**type**\: str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: ipv6_prefix
                
                	IPv6 context
                	**type**\: str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                

                """

                _prefix = 'mpls-static-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(MplsStatic.LocalLabels.LocalLabel.PathsetResolveNh, self).__init__()

                    self.yang_name = "pathset-resolve-nh"
                    self.yang_parent_name = "local-label"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('af_name', (YLeaf(YType.enumeration, 'af-name'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper', 'MgmtStaticAddr', '')])),
                        ('ipv4_prefix', (YLeaf(YType.str, 'ipv4-prefix'), ['str'])),
                        ('ipv6_prefix', (YLeaf(YType.str, 'ipv6-prefix'), ['str'])),
                    ])
                    self.af_name = None
                    self.ipv4_prefix = None
                    self.ipv6_prefix = None
                    self._segment_path = lambda: "pathset-resolve-nh"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsStatic.LocalLabels.LocalLabel.PathsetResolveNh, ['af_name', 'ipv4_prefix', 'ipv6_prefix'], name, value)


            class BackupPathsetResolveNh(Entity):
                """
                Backup pathset resolve\-nexthop IP Address
                
                .. attribute:: af_name
                
                	AFName
                	**type**\:  :py:class:`MgmtStaticAddr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MgmtStaticAddr>`
                
                .. attribute:: ipv4_prefix
                
                	IPv4 context
                	**type**\: str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: ipv6_prefix
                
                	IPv6 context
                	**type**\: str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                

                """

                _prefix = 'mpls-static-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(MplsStatic.LocalLabels.LocalLabel.BackupPathsetResolveNh, self).__init__()

                    self.yang_name = "backup-pathset-resolve-nh"
                    self.yang_parent_name = "local-label"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('af_name', (YLeaf(YType.enumeration, 'af-name'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper', 'MgmtStaticAddr', '')])),
                        ('ipv4_prefix', (YLeaf(YType.str, 'ipv4-prefix'), ['str'])),
                        ('ipv6_prefix', (YLeaf(YType.str, 'ipv6-prefix'), ['str'])),
                    ])
                    self.af_name = None
                    self.ipv4_prefix = None
                    self.ipv6_prefix = None
                    self._segment_path = lambda: "backup-pathset-resolve-nh"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsStatic.LocalLabels.LocalLabel.BackupPathsetResolveNh, ['af_name', 'ipv4_prefix', 'ipv6_prefix'], name, value)


            class PathInfo(Entity):
                """
                Path Information
                
                .. attribute:: nexthop
                
                	Nexthop information
                	**type**\:  :py:class:`Nexthop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MplsStatic.LocalLabels.LocalLabel.PathInfo.Nexthop>`
                
                .. attribute:: path_number
                
                	Path Number
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: type
                
                	Path Type
                	**type**\:  :py:class:`MgmtStaticPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MgmtStaticPath>`
                
                .. attribute:: path_role
                
                	Path Role
                	**type**\:  :py:class:`MplsStaticPathRole <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MplsStaticPathRole>`
                
                .. attribute:: path_id
                
                	Path Id
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: backup_id
                
                	Path Backup Id
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: status
                
                	Path Status
                	**type**\:  :py:class:`MgmtMplsStaticPathStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MgmtMplsStaticPathStatus>`
                
                

                """

                _prefix = 'mpls-static-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(MplsStatic.LocalLabels.LocalLabel.PathInfo, self).__init__()

                    self.yang_name = "path-info"
                    self.yang_parent_name = "local-label"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("nexthop", ("nexthop", MplsStatic.LocalLabels.LocalLabel.PathInfo.Nexthop))])
                    self._leafs = OrderedDict([
                        ('path_number', (YLeaf(YType.uint32, 'path-number'), ['int'])),
                        ('type', (YLeaf(YType.enumeration, 'type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper', 'MgmtStaticPath', '')])),
                        ('path_role', (YLeaf(YType.enumeration, 'path-role'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper', 'MplsStaticPathRole', '')])),
                        ('path_id', (YLeaf(YType.uint8, 'path-id'), ['int'])),
                        ('backup_id', (YLeaf(YType.uint8, 'backup-id'), ['int'])),
                        ('status', (YLeaf(YType.enumeration, 'status'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper', 'MgmtMplsStaticPathStatus', '')])),
                    ])
                    self.path_number = None
                    self.type = None
                    self.path_role = None
                    self.path_id = None
                    self.backup_id = None
                    self.status = None

                    self.nexthop = MplsStatic.LocalLabels.LocalLabel.PathInfo.Nexthop()
                    self.nexthop.parent = self
                    self._children_name_map["nexthop"] = "nexthop"
                    self._segment_path = lambda: "path-info"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsStatic.LocalLabels.LocalLabel.PathInfo, ['path_number', 'type', 'path_role', 'path_id', 'backup_id', 'status'], name, value)


                class Nexthop(Entity):
                    """
                    Nexthop information
                    
                    .. attribute:: address
                    
                    	Next\-Hop IP Address
                    	**type**\:  :py:class:`Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MplsStatic.LocalLabels.LocalLabel.PathInfo.Nexthop.Address>`
                    
                    .. attribute:: label
                    
                    	Next\-Hop Label
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: interface_name
                    
                    	Next\-Hop Interface Name
                    	**type**\: str
                    
                    .. attribute:: afi
                    
                    	Next\-Hop AFI
                    	**type**\:  :py:class:`MgmtStaticLspAfi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MgmtStaticLspAfi>`
                    
                    

                    """

                    _prefix = 'mpls-static-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(MplsStatic.LocalLabels.LocalLabel.PathInfo.Nexthop, self).__init__()

                        self.yang_name = "nexthop"
                        self.yang_parent_name = "path-info"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("address", ("address", MplsStatic.LocalLabels.LocalLabel.PathInfo.Nexthop.Address))])
                        self._leafs = OrderedDict([
                            ('label', (YLeaf(YType.uint32, 'label'), ['int'])),
                            ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                            ('afi', (YLeaf(YType.enumeration, 'afi'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper', 'MgmtStaticLspAfi', '')])),
                        ])
                        self.label = None
                        self.interface_name = None
                        self.afi = None

                        self.address = MplsStatic.LocalLabels.LocalLabel.PathInfo.Nexthop.Address()
                        self.address.parent = self
                        self._children_name_map["address"] = "address"
                        self._segment_path = lambda: "nexthop"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(MplsStatic.LocalLabels.LocalLabel.PathInfo.Nexthop, ['label', 'interface_name', 'afi'], name, value)


                    class Address(Entity):
                        """
                        Next\-Hop IP Address
                        
                        .. attribute:: af_name
                        
                        	AFName
                        	**type**\:  :py:class:`MgmtStaticAddr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MgmtStaticAddr>`
                        
                        .. attribute:: ipv4_prefix
                        
                        	IPv4 context
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: ipv6_prefix
                        
                        	IPv6 context
                        	**type**\: str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        

                        """

                        _prefix = 'mpls-static-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(MplsStatic.LocalLabels.LocalLabel.PathInfo.Nexthop.Address, self).__init__()

                            self.yang_name = "address"
                            self.yang_parent_name = "nexthop"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('af_name', (YLeaf(YType.enumeration, 'af-name'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper', 'MgmtStaticAddr', '')])),
                                ('ipv4_prefix', (YLeaf(YType.str, 'ipv4-prefix'), ['str'])),
                                ('ipv6_prefix', (YLeaf(YType.str, 'ipv6-prefix'), ['str'])),
                            ])
                            self.af_name = None
                            self.ipv4_prefix = None
                            self.ipv6_prefix = None
                            self._segment_path = lambda: "address"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(MplsStatic.LocalLabels.LocalLabel.PathInfo.Nexthop.Address, ['af_name', 'ipv4_prefix', 'ipv6_prefix'], name, value)


            class BackupPathInfo(Entity):
                """
                Backup Path Information
                
                .. attribute:: nexthop
                
                	Nexthop information
                	**type**\:  :py:class:`Nexthop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MplsStatic.LocalLabels.LocalLabel.BackupPathInfo.Nexthop>`
                
                .. attribute:: path_number
                
                	Path Number
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: type
                
                	Path Type
                	**type**\:  :py:class:`MgmtStaticPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MgmtStaticPath>`
                
                .. attribute:: path_role
                
                	Path Role
                	**type**\:  :py:class:`MplsStaticPathRole <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MplsStaticPathRole>`
                
                .. attribute:: path_id
                
                	Path Id
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: backup_id
                
                	Path Backup Id
                	**type**\: int
                
                	**range:** 0..255
                
                .. attribute:: status
                
                	Path Status
                	**type**\:  :py:class:`MgmtMplsStaticPathStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MgmtMplsStaticPathStatus>`
                
                

                """

                _prefix = 'mpls-static-oper'
                _revision = '2017-05-01'

                def __init__(self):
                    super(MplsStatic.LocalLabels.LocalLabel.BackupPathInfo, self).__init__()

                    self.yang_name = "backup-path-info"
                    self.yang_parent_name = "local-label"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("nexthop", ("nexthop", MplsStatic.LocalLabels.LocalLabel.BackupPathInfo.Nexthop))])
                    self._leafs = OrderedDict([
                        ('path_number', (YLeaf(YType.uint32, 'path-number'), ['int'])),
                        ('type', (YLeaf(YType.enumeration, 'type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper', 'MgmtStaticPath', '')])),
                        ('path_role', (YLeaf(YType.enumeration, 'path-role'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper', 'MplsStaticPathRole', '')])),
                        ('path_id', (YLeaf(YType.uint8, 'path-id'), ['int'])),
                        ('backup_id', (YLeaf(YType.uint8, 'backup-id'), ['int'])),
                        ('status', (YLeaf(YType.enumeration, 'status'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper', 'MgmtMplsStaticPathStatus', '')])),
                    ])
                    self.path_number = None
                    self.type = None
                    self.path_role = None
                    self.path_id = None
                    self.backup_id = None
                    self.status = None

                    self.nexthop = MplsStatic.LocalLabels.LocalLabel.BackupPathInfo.Nexthop()
                    self.nexthop.parent = self
                    self._children_name_map["nexthop"] = "nexthop"
                    self._segment_path = lambda: "backup-path-info"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(MplsStatic.LocalLabels.LocalLabel.BackupPathInfo, ['path_number', 'type', 'path_role', 'path_id', 'backup_id', 'status'], name, value)


                class Nexthop(Entity):
                    """
                    Nexthop information
                    
                    .. attribute:: address
                    
                    	Next\-Hop IP Address
                    	**type**\:  :py:class:`Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MplsStatic.LocalLabels.LocalLabel.BackupPathInfo.Nexthop.Address>`
                    
                    .. attribute:: label
                    
                    	Next\-Hop Label
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: interface_name
                    
                    	Next\-Hop Interface Name
                    	**type**\: str
                    
                    .. attribute:: afi
                    
                    	Next\-Hop AFI
                    	**type**\:  :py:class:`MgmtStaticLspAfi <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MgmtStaticLspAfi>`
                    
                    

                    """

                    _prefix = 'mpls-static-oper'
                    _revision = '2017-05-01'

                    def __init__(self):
                        super(MplsStatic.LocalLabels.LocalLabel.BackupPathInfo.Nexthop, self).__init__()

                        self.yang_name = "nexthop"
                        self.yang_parent_name = "backup-path-info"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("address", ("address", MplsStatic.LocalLabels.LocalLabel.BackupPathInfo.Nexthop.Address))])
                        self._leafs = OrderedDict([
                            ('label', (YLeaf(YType.uint32, 'label'), ['int'])),
                            ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                            ('afi', (YLeaf(YType.enumeration, 'afi'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper', 'MgmtStaticLspAfi', '')])),
                        ])
                        self.label = None
                        self.interface_name = None
                        self.afi = None

                        self.address = MplsStatic.LocalLabels.LocalLabel.BackupPathInfo.Nexthop.Address()
                        self.address.parent = self
                        self._children_name_map["address"] = "address"
                        self._segment_path = lambda: "nexthop"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(MplsStatic.LocalLabels.LocalLabel.BackupPathInfo.Nexthop, ['label', 'interface_name', 'afi'], name, value)


                    class Address(Entity):
                        """
                        Next\-Hop IP Address
                        
                        .. attribute:: af_name
                        
                        	AFName
                        	**type**\:  :py:class:`MgmtStaticAddr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MgmtStaticAddr>`
                        
                        .. attribute:: ipv4_prefix
                        
                        	IPv4 context
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: ipv6_prefix
                        
                        	IPv6 context
                        	**type**\: str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        

                        """

                        _prefix = 'mpls-static-oper'
                        _revision = '2017-05-01'

                        def __init__(self):
                            super(MplsStatic.LocalLabels.LocalLabel.BackupPathInfo.Nexthop.Address, self).__init__()

                            self.yang_name = "address"
                            self.yang_parent_name = "nexthop"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('af_name', (YLeaf(YType.enumeration, 'af-name'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper', 'MgmtStaticAddr', '')])),
                                ('ipv4_prefix', (YLeaf(YType.str, 'ipv4-prefix'), ['str'])),
                                ('ipv6_prefix', (YLeaf(YType.str, 'ipv6-prefix'), ['str'])),
                            ])
                            self.af_name = None
                            self.ipv4_prefix = None
                            self.ipv6_prefix = None
                            self._segment_path = lambda: "address"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(MplsStatic.LocalLabels.LocalLabel.BackupPathInfo.Nexthop.Address, ['af_name', 'ipv4_prefix', 'ipv6_prefix'], name, value)

    def clone_ptr(self):
        self._top_entity = MplsStatic()
        return self._top_entity

