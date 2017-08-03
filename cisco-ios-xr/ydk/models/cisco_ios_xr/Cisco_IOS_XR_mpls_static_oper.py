""" Cisco_IOS_XR_mpls_static_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR mpls\-static package operational data.

This module contains definitions
for the following management objects\:
  mpls\-static\: MPLS STATIC operational data

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class MgmtMplsStaticLabelMode(Enum):
    """
    MgmtMplsStaticLabelMode

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
    MgmtMplsStaticLabelStatus

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

    .. data:: label_status_unknown = 12

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

    label_status_unknown = Enum.YLeaf(12, "label-status-unknown")


class MgmtMplsStaticPathStatus(Enum):
    """
    MgmtMplsStaticPathStatus

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
    MgmtStaticAddr

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


class MgmtStaticPath(Enum):
    """
    MgmtStaticPath

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
    MplsStaticPathRole

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
    
    .. attribute:: local_labels
    
    	data for static local\-label table
    	**type**\:   :py:class:`LocalLabels <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MplsStatic.LocalLabels>`
    
    .. attribute:: summary
    
    	MPLS STATIC summary data
    	**type**\:   :py:class:`Summary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MplsStatic.Summary>`
    
    .. attribute:: vrfs
    
    	VRF table
    	**type**\:   :py:class:`Vrfs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MplsStatic.Vrfs>`
    
    

    """

    _prefix = 'mpls-static-oper'
    _revision = '2015-11-09'

    def __init__(self):
        super(MplsStatic, self).__init__()
        self._top_entity = None

        self.yang_name = "mpls-static"
        self.yang_parent_name = "Cisco-IOS-XR-mpls-static-oper"

        self.local_labels = MplsStatic.LocalLabels()
        self.local_labels.parent = self
        self._children_name_map["local_labels"] = "local-labels"
        self._children_yang_names.add("local-labels")

        self.summary = MplsStatic.Summary()
        self.summary.parent = self
        self._children_name_map["summary"] = "summary"
        self._children_yang_names.add("summary")

        self.vrfs = MplsStatic.Vrfs()
        self.vrfs.parent = self
        self._children_name_map["vrfs"] = "vrfs"
        self._children_yang_names.add("vrfs")


    class Vrfs(Entity):
        """
        VRF table
        
        .. attribute:: vrf
        
        	VRF Name
        	**type**\: list of    :py:class:`Vrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MplsStatic.Vrfs.Vrf>`
        
        

        """

        _prefix = 'mpls-static-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(MplsStatic.Vrfs, self).__init__()

            self.yang_name = "vrfs"
            self.yang_parent_name = "mpls-static"

            self.vrf = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(MplsStatic.Vrfs, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(MplsStatic.Vrfs, self).__setattr__(name, value)


        class Vrf(Entity):
            """
            VRF Name
            
            .. attribute:: vrf_name  <key>
            
            	VRF Name
            	**type**\:  str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: local_labels
            
            	data for static local\-label table
            	**type**\:   :py:class:`LocalLabels <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MplsStatic.Vrfs.Vrf.LocalLabels>`
            
            .. attribute:: lsps
            
            	data for static lsp table
            	**type**\:   :py:class:`Lsps <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MplsStatic.Vrfs.Vrf.Lsps>`
            
            

            """

            _prefix = 'mpls-static-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(MplsStatic.Vrfs.Vrf, self).__init__()

                self.yang_name = "vrf"
                self.yang_parent_name = "vrfs"

                self.vrf_name = YLeaf(YType.str, "vrf-name")

                self.local_labels = MplsStatic.Vrfs.Vrf.LocalLabels()
                self.local_labels.parent = self
                self._children_name_map["local_labels"] = "local-labels"
                self._children_yang_names.add("local-labels")

                self.lsps = MplsStatic.Vrfs.Vrf.Lsps()
                self.lsps.parent = self
                self._children_name_map["lsps"] = "lsps"
                self._children_yang_names.add("lsps")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("vrf_name") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(MplsStatic.Vrfs.Vrf, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(MplsStatic.Vrfs.Vrf, self).__setattr__(name, value)


            class Lsps(Entity):
                """
                data for static lsp table
                
                .. attribute:: lsp
                
                	Data for static lsp
                	**type**\: list of    :py:class:`Lsp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MplsStatic.Vrfs.Vrf.Lsps.Lsp>`
                
                

                """

                _prefix = 'mpls-static-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(MplsStatic.Vrfs.Vrf.Lsps, self).__init__()

                    self.yang_name = "lsps"
                    self.yang_parent_name = "vrf"

                    self.lsp = YList(self)

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in () and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(MplsStatic.Vrfs.Vrf.Lsps, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(MplsStatic.Vrfs.Vrf.Lsps, self).__setattr__(name, value)


                class Lsp(Entity):
                    """
                    Data for static lsp
                    
                    .. attribute:: lsp_name  <key>
                    
                    	LSP Name
                    	**type**\:  str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: label
                    
                    	Label Information
                    	**type**\:   :py:class:`Label <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MplsStatic.Vrfs.Vrf.Lsps.Lsp.Label>`
                    
                    .. attribute:: lsp_name_xr
                    
                    	LSP Name
                    	**type**\:  str
                    
                    

                    """

                    _prefix = 'mpls-static-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(MplsStatic.Vrfs.Vrf.Lsps.Lsp, self).__init__()

                        self.yang_name = "lsp"
                        self.yang_parent_name = "lsps"

                        self.lsp_name = YLeaf(YType.str, "lsp-name")

                        self.lsp_name_xr = YLeaf(YType.str, "lsp-name-xr")

                        self.label = MplsStatic.Vrfs.Vrf.Lsps.Lsp.Label()
                        self.label.parent = self
                        self._children_name_map["label"] = "label"
                        self._children_yang_names.add("label")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("lsp_name",
                                        "lsp_name_xr") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(MplsStatic.Vrfs.Vrf.Lsps.Lsp, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(MplsStatic.Vrfs.Vrf.Lsps.Lsp, self).__setattr__(name, value)


                    class Label(Entity):
                        """
                        Label Information
                        
                        .. attribute:: address_family
                        
                        	Address Family
                        	**type**\:   :py:class:`MgmtStaticAddr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MgmtStaticAddr>`
                        
                        .. attribute:: backup_path_info
                        
                        	Backup Path Information
                        	**type**\: list of    :py:class:`BackupPathInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MplsStatic.Vrfs.Vrf.Lsps.Lsp.Label.BackupPathInfo>`
                        
                        .. attribute:: backup_pathset_resolve_nh
                        
                        	Backup pathset resolve\-nexthop IP Address
                        	**type**\:   :py:class:`BackupPathsetResolveNh <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MplsStatic.Vrfs.Vrf.Lsps.Lsp.Label.BackupPathsetResolveNh>`
                        
                        .. attribute:: backup_pathset_via_resolve
                        
                        	Backup Pathset as a result of resolve
                        	**type**\:  bool
                        
                        .. attribute:: label
                        
                        	Label value
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: label_mode
                        
                        	Label Mode
                        	**type**\:   :py:class:`MgmtMplsStaticLabelMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MgmtMplsStaticLabelMode>`
                        
                        .. attribute:: label_status
                        
                        	Label Status
                        	**type**\:   :py:class:`MgmtMplsStaticLabelStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MgmtMplsStaticLabelStatus>`
                        
                        .. attribute:: path_info
                        
                        	Path Information
                        	**type**\: list of    :py:class:`PathInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MplsStatic.Vrfs.Vrf.Lsps.Lsp.Label.PathInfo>`
                        
                        .. attribute:: pathset_resolve_nh
                        
                        	Primary pathset resolve\-nexthop IP Address
                        	**type**\:   :py:class:`PathsetResolveNh <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MplsStatic.Vrfs.Vrf.Lsps.Lsp.Label.PathsetResolveNh>`
                        
                        .. attribute:: pathset_via_resolve
                        
                        	Primary Pathset as a result of resolve
                        	**type**\:  bool
                        
                        .. attribute:: prefix
                        
                        	Prefix Information
                        	**type**\:   :py:class:`Prefix <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MplsStatic.Vrfs.Vrf.Lsps.Lsp.Label.Prefix>`
                        
                        .. attribute:: vrf_name
                        
                        	VRF name
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'mpls-static-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(MplsStatic.Vrfs.Vrf.Lsps.Lsp.Label, self).__init__()

                            self.yang_name = "label"
                            self.yang_parent_name = "lsp"

                            self.address_family = YLeaf(YType.enumeration, "address-family")

                            self.backup_pathset_via_resolve = YLeaf(YType.boolean, "backup-pathset-via-resolve")

                            self.label = YLeaf(YType.uint32, "label")

                            self.label_mode = YLeaf(YType.enumeration, "label-mode")

                            self.label_status = YLeaf(YType.enumeration, "label-status")

                            self.pathset_via_resolve = YLeaf(YType.boolean, "pathset-via-resolve")

                            self.vrf_name = YLeaf(YType.str, "vrf-name")

                            self.backup_pathset_resolve_nh = MplsStatic.Vrfs.Vrf.Lsps.Lsp.Label.BackupPathsetResolveNh()
                            self.backup_pathset_resolve_nh.parent = self
                            self._children_name_map["backup_pathset_resolve_nh"] = "backup-pathset-resolve-nh"
                            self._children_yang_names.add("backup-pathset-resolve-nh")

                            self.pathset_resolve_nh = MplsStatic.Vrfs.Vrf.Lsps.Lsp.Label.PathsetResolveNh()
                            self.pathset_resolve_nh.parent = self
                            self._children_name_map["pathset_resolve_nh"] = "pathset-resolve-nh"
                            self._children_yang_names.add("pathset-resolve-nh")

                            self.prefix = MplsStatic.Vrfs.Vrf.Lsps.Lsp.Label.Prefix()
                            self.prefix.parent = self
                            self._children_name_map["prefix"] = "prefix"
                            self._children_yang_names.add("prefix")

                            self.backup_path_info = YList(self)
                            self.path_info = YList(self)

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("address_family",
                                            "backup_pathset_via_resolve",
                                            "label",
                                            "label_mode",
                                            "label_status",
                                            "pathset_via_resolve",
                                            "vrf_name") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(MplsStatic.Vrfs.Vrf.Lsps.Lsp.Label, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(MplsStatic.Vrfs.Vrf.Lsps.Lsp.Label, self).__setattr__(name, value)


                        class Prefix(Entity):
                            """
                            Prefix Information
                            
                            .. attribute:: prefix
                            
                            	Prefix
                            	**type**\:   :py:class:`Prefix <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MplsStatic.Vrfs.Vrf.Lsps.Lsp.Label.Prefix.Prefix>`
                            
                            .. attribute:: prefix_length
                            
                            	Prefix length
                            	**type**\:  int
                            
                            	**range:** 0..255
                            
                            

                            """

                            _prefix = 'mpls-static-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(MplsStatic.Vrfs.Vrf.Lsps.Lsp.Label.Prefix, self).__init__()

                                self.yang_name = "prefix"
                                self.yang_parent_name = "label"

                                self.prefix_length = YLeaf(YType.uint8, "prefix-length")

                                self.prefix = MplsStatic.Vrfs.Vrf.Lsps.Lsp.Label.Prefix.Prefix()
                                self.prefix.parent = self
                                self._children_name_map["prefix"] = "prefix"
                                self._children_yang_names.add("prefix")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("prefix_length") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(MplsStatic.Vrfs.Vrf.Lsps.Lsp.Label.Prefix, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(MplsStatic.Vrfs.Vrf.Lsps.Lsp.Label.Prefix, self).__setattr__(name, value)


                            class Prefix(Entity):
                                """
                                Prefix
                                
                                .. attribute:: af_name
                                
                                	AFName
                                	**type**\:   :py:class:`MgmtStaticAddr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MgmtStaticAddr>`
                                
                                .. attribute:: ipv4_prefix
                                
                                	IPv4 context
                                	**type**\:  str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: ipv6_prefix
                                
                                	IPv6 context
                                	**type**\:  str
                                
                                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                
                                

                                """

                                _prefix = 'mpls-static-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(MplsStatic.Vrfs.Vrf.Lsps.Lsp.Label.Prefix.Prefix, self).__init__()

                                    self.yang_name = "prefix"
                                    self.yang_parent_name = "prefix"

                                    self.af_name = YLeaf(YType.enumeration, "af-name")

                                    self.ipv4_prefix = YLeaf(YType.str, "ipv4-prefix")

                                    self.ipv6_prefix = YLeaf(YType.str, "ipv6-prefix")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("af_name",
                                                    "ipv4_prefix",
                                                    "ipv6_prefix") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(MplsStatic.Vrfs.Vrf.Lsps.Lsp.Label.Prefix.Prefix, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(MplsStatic.Vrfs.Vrf.Lsps.Lsp.Label.Prefix.Prefix, self).__setattr__(name, value)

                                def has_data(self):
                                    return (
                                        self.af_name.is_set or
                                        self.ipv4_prefix.is_set or
                                        self.ipv6_prefix.is_set)

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.af_name.yfilter != YFilter.not_set or
                                        self.ipv4_prefix.yfilter != YFilter.not_set or
                                        self.ipv6_prefix.yfilter != YFilter.not_set)

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "prefix" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.af_name.is_set or self.af_name.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.af_name.get_name_leafdata())
                                    if (self.ipv4_prefix.is_set or self.ipv4_prefix.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.ipv4_prefix.get_name_leafdata())
                                    if (self.ipv6_prefix.is_set or self.ipv6_prefix.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.ipv6_prefix.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "af-name" or name == "ipv4-prefix" or name == "ipv6-prefix"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "af-name"):
                                        self.af_name = value
                                        self.af_name.value_namespace = name_space
                                        self.af_name.value_namespace_prefix = name_space_prefix
                                    if(value_path == "ipv4-prefix"):
                                        self.ipv4_prefix = value
                                        self.ipv4_prefix.value_namespace = name_space
                                        self.ipv4_prefix.value_namespace_prefix = name_space_prefix
                                    if(value_path == "ipv6-prefix"):
                                        self.ipv6_prefix = value
                                        self.ipv6_prefix.value_namespace = name_space
                                        self.ipv6_prefix.value_namespace_prefix = name_space_prefix

                            def has_data(self):
                                return (
                                    self.prefix_length.is_set or
                                    (self.prefix is not None and self.prefix.has_data()))

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.prefix_length.yfilter != YFilter.not_set or
                                    (self.prefix is not None and self.prefix.has_operation()))

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "prefix" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.prefix_length.is_set or self.prefix_length.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.prefix_length.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                if (child_yang_name == "prefix"):
                                    if (self.prefix is None):
                                        self.prefix = MplsStatic.Vrfs.Vrf.Lsps.Lsp.Label.Prefix.Prefix()
                                        self.prefix.parent = self
                                        self._children_name_map["prefix"] = "prefix"
                                    return self.prefix

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "prefix" or name == "prefix-length"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "prefix-length"):
                                    self.prefix_length = value
                                    self.prefix_length.value_namespace = name_space
                                    self.prefix_length.value_namespace_prefix = name_space_prefix


                        class PathsetResolveNh(Entity):
                            """
                            Primary pathset resolve\-nexthop IP Address
                            
                            .. attribute:: af_name
                            
                            	AFName
                            	**type**\:   :py:class:`MgmtStaticAddr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MgmtStaticAddr>`
                            
                            .. attribute:: ipv4_prefix
                            
                            	IPv4 context
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: ipv6_prefix
                            
                            	IPv6 context
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            

                            """

                            _prefix = 'mpls-static-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(MplsStatic.Vrfs.Vrf.Lsps.Lsp.Label.PathsetResolveNh, self).__init__()

                                self.yang_name = "pathset-resolve-nh"
                                self.yang_parent_name = "label"

                                self.af_name = YLeaf(YType.enumeration, "af-name")

                                self.ipv4_prefix = YLeaf(YType.str, "ipv4-prefix")

                                self.ipv6_prefix = YLeaf(YType.str, "ipv6-prefix")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("af_name",
                                                "ipv4_prefix",
                                                "ipv6_prefix") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(MplsStatic.Vrfs.Vrf.Lsps.Lsp.Label.PathsetResolveNh, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(MplsStatic.Vrfs.Vrf.Lsps.Lsp.Label.PathsetResolveNh, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.af_name.is_set or
                                    self.ipv4_prefix.is_set or
                                    self.ipv6_prefix.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.af_name.yfilter != YFilter.not_set or
                                    self.ipv4_prefix.yfilter != YFilter.not_set or
                                    self.ipv6_prefix.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "pathset-resolve-nh" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.af_name.is_set or self.af_name.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.af_name.get_name_leafdata())
                                if (self.ipv4_prefix.is_set or self.ipv4_prefix.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.ipv4_prefix.get_name_leafdata())
                                if (self.ipv6_prefix.is_set or self.ipv6_prefix.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.ipv6_prefix.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "af-name" or name == "ipv4-prefix" or name == "ipv6-prefix"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "af-name"):
                                    self.af_name = value
                                    self.af_name.value_namespace = name_space
                                    self.af_name.value_namespace_prefix = name_space_prefix
                                if(value_path == "ipv4-prefix"):
                                    self.ipv4_prefix = value
                                    self.ipv4_prefix.value_namespace = name_space
                                    self.ipv4_prefix.value_namespace_prefix = name_space_prefix
                                if(value_path == "ipv6-prefix"):
                                    self.ipv6_prefix = value
                                    self.ipv6_prefix.value_namespace = name_space
                                    self.ipv6_prefix.value_namespace_prefix = name_space_prefix


                        class BackupPathsetResolveNh(Entity):
                            """
                            Backup pathset resolve\-nexthop IP Address
                            
                            .. attribute:: af_name
                            
                            	AFName
                            	**type**\:   :py:class:`MgmtStaticAddr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MgmtStaticAddr>`
                            
                            .. attribute:: ipv4_prefix
                            
                            	IPv4 context
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: ipv6_prefix
                            
                            	IPv6 context
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            

                            """

                            _prefix = 'mpls-static-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(MplsStatic.Vrfs.Vrf.Lsps.Lsp.Label.BackupPathsetResolveNh, self).__init__()

                                self.yang_name = "backup-pathset-resolve-nh"
                                self.yang_parent_name = "label"

                                self.af_name = YLeaf(YType.enumeration, "af-name")

                                self.ipv4_prefix = YLeaf(YType.str, "ipv4-prefix")

                                self.ipv6_prefix = YLeaf(YType.str, "ipv6-prefix")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("af_name",
                                                "ipv4_prefix",
                                                "ipv6_prefix") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(MplsStatic.Vrfs.Vrf.Lsps.Lsp.Label.BackupPathsetResolveNh, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(MplsStatic.Vrfs.Vrf.Lsps.Lsp.Label.BackupPathsetResolveNh, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.af_name.is_set or
                                    self.ipv4_prefix.is_set or
                                    self.ipv6_prefix.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.af_name.yfilter != YFilter.not_set or
                                    self.ipv4_prefix.yfilter != YFilter.not_set or
                                    self.ipv6_prefix.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "backup-pathset-resolve-nh" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.af_name.is_set or self.af_name.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.af_name.get_name_leafdata())
                                if (self.ipv4_prefix.is_set or self.ipv4_prefix.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.ipv4_prefix.get_name_leafdata())
                                if (self.ipv6_prefix.is_set or self.ipv6_prefix.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.ipv6_prefix.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "af-name" or name == "ipv4-prefix" or name == "ipv6-prefix"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "af-name"):
                                    self.af_name = value
                                    self.af_name.value_namespace = name_space
                                    self.af_name.value_namespace_prefix = name_space_prefix
                                if(value_path == "ipv4-prefix"):
                                    self.ipv4_prefix = value
                                    self.ipv4_prefix.value_namespace = name_space
                                    self.ipv4_prefix.value_namespace_prefix = name_space_prefix
                                if(value_path == "ipv6-prefix"):
                                    self.ipv6_prefix = value
                                    self.ipv6_prefix.value_namespace = name_space
                                    self.ipv6_prefix.value_namespace_prefix = name_space_prefix


                        class PathInfo(Entity):
                            """
                            Path Information
                            
                            .. attribute:: backup_id
                            
                            	Path Backup Id
                            	**type**\:  int
                            
                            	**range:** 0..255
                            
                            .. attribute:: nexthop
                            
                            	Nexthop information
                            	**type**\:   :py:class:`Nexthop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MplsStatic.Vrfs.Vrf.Lsps.Lsp.Label.PathInfo.Nexthop>`
                            
                            .. attribute:: path_id
                            
                            	Path Id
                            	**type**\:  int
                            
                            	**range:** 0..255
                            
                            .. attribute:: path_number
                            
                            	Path Number
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: path_role
                            
                            	Path Role
                            	**type**\:   :py:class:`MplsStaticPathRole <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MplsStaticPathRole>`
                            
                            .. attribute:: status
                            
                            	Path Status
                            	**type**\:   :py:class:`MgmtMplsStaticPathStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MgmtMplsStaticPathStatus>`
                            
                            .. attribute:: type
                            
                            	Path Type
                            	**type**\:   :py:class:`MgmtStaticPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MgmtStaticPath>`
                            
                            

                            """

                            _prefix = 'mpls-static-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(MplsStatic.Vrfs.Vrf.Lsps.Lsp.Label.PathInfo, self).__init__()

                                self.yang_name = "path-info"
                                self.yang_parent_name = "label"

                                self.backup_id = YLeaf(YType.uint8, "backup-id")

                                self.path_id = YLeaf(YType.uint8, "path-id")

                                self.path_number = YLeaf(YType.uint32, "path-number")

                                self.path_role = YLeaf(YType.enumeration, "path-role")

                                self.status = YLeaf(YType.enumeration, "status")

                                self.type = YLeaf(YType.enumeration, "type")

                                self.nexthop = MplsStatic.Vrfs.Vrf.Lsps.Lsp.Label.PathInfo.Nexthop()
                                self.nexthop.parent = self
                                self._children_name_map["nexthop"] = "nexthop"
                                self._children_yang_names.add("nexthop")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("backup_id",
                                                "path_id",
                                                "path_number",
                                                "path_role",
                                                "status",
                                                "type") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(MplsStatic.Vrfs.Vrf.Lsps.Lsp.Label.PathInfo, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(MplsStatic.Vrfs.Vrf.Lsps.Lsp.Label.PathInfo, self).__setattr__(name, value)


                            class Nexthop(Entity):
                                """
                                Nexthop information
                                
                                .. attribute:: address
                                
                                	Next\-Hop IP Address
                                	**type**\:   :py:class:`Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MplsStatic.Vrfs.Vrf.Lsps.Lsp.Label.PathInfo.Nexthop.Address>`
                                
                                .. attribute:: afi
                                
                                	Next\-Hop AFI
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: interface_name
                                
                                	Next\-Hop Interface Name
                                	**type**\:  str
                                
                                .. attribute:: label
                                
                                	Next\-Hop Label
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'mpls-static-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(MplsStatic.Vrfs.Vrf.Lsps.Lsp.Label.PathInfo.Nexthop, self).__init__()

                                    self.yang_name = "nexthop"
                                    self.yang_parent_name = "path-info"

                                    self.afi = YLeaf(YType.uint32, "afi")

                                    self.interface_name = YLeaf(YType.str, "interface-name")

                                    self.label = YLeaf(YType.uint32, "label")

                                    self.address = MplsStatic.Vrfs.Vrf.Lsps.Lsp.Label.PathInfo.Nexthop.Address()
                                    self.address.parent = self
                                    self._children_name_map["address"] = "address"
                                    self._children_yang_names.add("address")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("afi",
                                                    "interface_name",
                                                    "label") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(MplsStatic.Vrfs.Vrf.Lsps.Lsp.Label.PathInfo.Nexthop, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(MplsStatic.Vrfs.Vrf.Lsps.Lsp.Label.PathInfo.Nexthop, self).__setattr__(name, value)


                                class Address(Entity):
                                    """
                                    Next\-Hop IP Address
                                    
                                    .. attribute:: af_name
                                    
                                    	AFName
                                    	**type**\:   :py:class:`MgmtStaticAddr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MgmtStaticAddr>`
                                    
                                    .. attribute:: ipv4_prefix
                                    
                                    	IPv4 context
                                    	**type**\:  str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    .. attribute:: ipv6_prefix
                                    
                                    	IPv6 context
                                    	**type**\:  str
                                    
                                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                    
                                    

                                    """

                                    _prefix = 'mpls-static-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(MplsStatic.Vrfs.Vrf.Lsps.Lsp.Label.PathInfo.Nexthop.Address, self).__init__()

                                        self.yang_name = "address"
                                        self.yang_parent_name = "nexthop"

                                        self.af_name = YLeaf(YType.enumeration, "af-name")

                                        self.ipv4_prefix = YLeaf(YType.str, "ipv4-prefix")

                                        self.ipv6_prefix = YLeaf(YType.str, "ipv6-prefix")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("af_name",
                                                        "ipv4_prefix",
                                                        "ipv6_prefix") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(MplsStatic.Vrfs.Vrf.Lsps.Lsp.Label.PathInfo.Nexthop.Address, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(MplsStatic.Vrfs.Vrf.Lsps.Lsp.Label.PathInfo.Nexthop.Address, self).__setattr__(name, value)

                                    def has_data(self):
                                        return (
                                            self.af_name.is_set or
                                            self.ipv4_prefix.is_set or
                                            self.ipv6_prefix.is_set)

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.af_name.yfilter != YFilter.not_set or
                                            self.ipv4_prefix.yfilter != YFilter.not_set or
                                            self.ipv6_prefix.yfilter != YFilter.not_set)

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "address" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()
                                        if (self.af_name.is_set or self.af_name.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.af_name.get_name_leafdata())
                                        if (self.ipv4_prefix.is_set or self.ipv4_prefix.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.ipv4_prefix.get_name_leafdata())
                                        if (self.ipv6_prefix.is_set or self.ipv6_prefix.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.ipv6_prefix.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "af-name" or name == "ipv4-prefix" or name == "ipv6-prefix"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "af-name"):
                                            self.af_name = value
                                            self.af_name.value_namespace = name_space
                                            self.af_name.value_namespace_prefix = name_space_prefix
                                        if(value_path == "ipv4-prefix"):
                                            self.ipv4_prefix = value
                                            self.ipv4_prefix.value_namespace = name_space
                                            self.ipv4_prefix.value_namespace_prefix = name_space_prefix
                                        if(value_path == "ipv6-prefix"):
                                            self.ipv6_prefix = value
                                            self.ipv6_prefix.value_namespace = name_space
                                            self.ipv6_prefix.value_namespace_prefix = name_space_prefix

                                def has_data(self):
                                    return (
                                        self.afi.is_set or
                                        self.interface_name.is_set or
                                        self.label.is_set or
                                        (self.address is not None and self.address.has_data()))

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.afi.yfilter != YFilter.not_set or
                                        self.interface_name.yfilter != YFilter.not_set or
                                        self.label.yfilter != YFilter.not_set or
                                        (self.address is not None and self.address.has_operation()))

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "nexthop" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.afi.is_set or self.afi.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.afi.get_name_leafdata())
                                    if (self.interface_name.is_set or self.interface_name.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.interface_name.get_name_leafdata())
                                    if (self.label.is_set or self.label.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.label.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    if (child_yang_name == "address"):
                                        if (self.address is None):
                                            self.address = MplsStatic.Vrfs.Vrf.Lsps.Lsp.Label.PathInfo.Nexthop.Address()
                                            self.address.parent = self
                                            self._children_name_map["address"] = "address"
                                        return self.address

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "address" or name == "afi" or name == "interface-name" or name == "label"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "afi"):
                                        self.afi = value
                                        self.afi.value_namespace = name_space
                                        self.afi.value_namespace_prefix = name_space_prefix
                                    if(value_path == "interface-name"):
                                        self.interface_name = value
                                        self.interface_name.value_namespace = name_space
                                        self.interface_name.value_namespace_prefix = name_space_prefix
                                    if(value_path == "label"):
                                        self.label = value
                                        self.label.value_namespace = name_space
                                        self.label.value_namespace_prefix = name_space_prefix

                            def has_data(self):
                                return (
                                    self.backup_id.is_set or
                                    self.path_id.is_set or
                                    self.path_number.is_set or
                                    self.path_role.is_set or
                                    self.status.is_set or
                                    self.type.is_set or
                                    (self.nexthop is not None and self.nexthop.has_data()))

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.backup_id.yfilter != YFilter.not_set or
                                    self.path_id.yfilter != YFilter.not_set or
                                    self.path_number.yfilter != YFilter.not_set or
                                    self.path_role.yfilter != YFilter.not_set or
                                    self.status.yfilter != YFilter.not_set or
                                    self.type.yfilter != YFilter.not_set or
                                    (self.nexthop is not None and self.nexthop.has_operation()))

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "path-info" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.backup_id.is_set or self.backup_id.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.backup_id.get_name_leafdata())
                                if (self.path_id.is_set or self.path_id.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.path_id.get_name_leafdata())
                                if (self.path_number.is_set or self.path_number.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.path_number.get_name_leafdata())
                                if (self.path_role.is_set or self.path_role.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.path_role.get_name_leafdata())
                                if (self.status.is_set or self.status.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.status.get_name_leafdata())
                                if (self.type.is_set or self.type.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.type.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                if (child_yang_name == "nexthop"):
                                    if (self.nexthop is None):
                                        self.nexthop = MplsStatic.Vrfs.Vrf.Lsps.Lsp.Label.PathInfo.Nexthop()
                                        self.nexthop.parent = self
                                        self._children_name_map["nexthop"] = "nexthop"
                                    return self.nexthop

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "nexthop" or name == "backup-id" or name == "path-id" or name == "path-number" or name == "path-role" or name == "status" or name == "type"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "backup-id"):
                                    self.backup_id = value
                                    self.backup_id.value_namespace = name_space
                                    self.backup_id.value_namespace_prefix = name_space_prefix
                                if(value_path == "path-id"):
                                    self.path_id = value
                                    self.path_id.value_namespace = name_space
                                    self.path_id.value_namespace_prefix = name_space_prefix
                                if(value_path == "path-number"):
                                    self.path_number = value
                                    self.path_number.value_namespace = name_space
                                    self.path_number.value_namespace_prefix = name_space_prefix
                                if(value_path == "path-role"):
                                    self.path_role = value
                                    self.path_role.value_namespace = name_space
                                    self.path_role.value_namespace_prefix = name_space_prefix
                                if(value_path == "status"):
                                    self.status = value
                                    self.status.value_namespace = name_space
                                    self.status.value_namespace_prefix = name_space_prefix
                                if(value_path == "type"):
                                    self.type = value
                                    self.type.value_namespace = name_space
                                    self.type.value_namespace_prefix = name_space_prefix


                        class BackupPathInfo(Entity):
                            """
                            Backup Path Information
                            
                            .. attribute:: backup_id
                            
                            	Path Backup Id
                            	**type**\:  int
                            
                            	**range:** 0..255
                            
                            .. attribute:: nexthop
                            
                            	Nexthop information
                            	**type**\:   :py:class:`Nexthop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MplsStatic.Vrfs.Vrf.Lsps.Lsp.Label.BackupPathInfo.Nexthop>`
                            
                            .. attribute:: path_id
                            
                            	Path Id
                            	**type**\:  int
                            
                            	**range:** 0..255
                            
                            .. attribute:: path_number
                            
                            	Path Number
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: path_role
                            
                            	Path Role
                            	**type**\:   :py:class:`MplsStaticPathRole <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MplsStaticPathRole>`
                            
                            .. attribute:: status
                            
                            	Path Status
                            	**type**\:   :py:class:`MgmtMplsStaticPathStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MgmtMplsStaticPathStatus>`
                            
                            .. attribute:: type
                            
                            	Path Type
                            	**type**\:   :py:class:`MgmtStaticPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MgmtStaticPath>`
                            
                            

                            """

                            _prefix = 'mpls-static-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(MplsStatic.Vrfs.Vrf.Lsps.Lsp.Label.BackupPathInfo, self).__init__()

                                self.yang_name = "backup-path-info"
                                self.yang_parent_name = "label"

                                self.backup_id = YLeaf(YType.uint8, "backup-id")

                                self.path_id = YLeaf(YType.uint8, "path-id")

                                self.path_number = YLeaf(YType.uint32, "path-number")

                                self.path_role = YLeaf(YType.enumeration, "path-role")

                                self.status = YLeaf(YType.enumeration, "status")

                                self.type = YLeaf(YType.enumeration, "type")

                                self.nexthop = MplsStatic.Vrfs.Vrf.Lsps.Lsp.Label.BackupPathInfo.Nexthop()
                                self.nexthop.parent = self
                                self._children_name_map["nexthop"] = "nexthop"
                                self._children_yang_names.add("nexthop")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("backup_id",
                                                "path_id",
                                                "path_number",
                                                "path_role",
                                                "status",
                                                "type") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(MplsStatic.Vrfs.Vrf.Lsps.Lsp.Label.BackupPathInfo, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(MplsStatic.Vrfs.Vrf.Lsps.Lsp.Label.BackupPathInfo, self).__setattr__(name, value)


                            class Nexthop(Entity):
                                """
                                Nexthop information
                                
                                .. attribute:: address
                                
                                	Next\-Hop IP Address
                                	**type**\:   :py:class:`Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MplsStatic.Vrfs.Vrf.Lsps.Lsp.Label.BackupPathInfo.Nexthop.Address>`
                                
                                .. attribute:: afi
                                
                                	Next\-Hop AFI
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: interface_name
                                
                                	Next\-Hop Interface Name
                                	**type**\:  str
                                
                                .. attribute:: label
                                
                                	Next\-Hop Label
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'mpls-static-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(MplsStatic.Vrfs.Vrf.Lsps.Lsp.Label.BackupPathInfo.Nexthop, self).__init__()

                                    self.yang_name = "nexthop"
                                    self.yang_parent_name = "backup-path-info"

                                    self.afi = YLeaf(YType.uint32, "afi")

                                    self.interface_name = YLeaf(YType.str, "interface-name")

                                    self.label = YLeaf(YType.uint32, "label")

                                    self.address = MplsStatic.Vrfs.Vrf.Lsps.Lsp.Label.BackupPathInfo.Nexthop.Address()
                                    self.address.parent = self
                                    self._children_name_map["address"] = "address"
                                    self._children_yang_names.add("address")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("afi",
                                                    "interface_name",
                                                    "label") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(MplsStatic.Vrfs.Vrf.Lsps.Lsp.Label.BackupPathInfo.Nexthop, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(MplsStatic.Vrfs.Vrf.Lsps.Lsp.Label.BackupPathInfo.Nexthop, self).__setattr__(name, value)


                                class Address(Entity):
                                    """
                                    Next\-Hop IP Address
                                    
                                    .. attribute:: af_name
                                    
                                    	AFName
                                    	**type**\:   :py:class:`MgmtStaticAddr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MgmtStaticAddr>`
                                    
                                    .. attribute:: ipv4_prefix
                                    
                                    	IPv4 context
                                    	**type**\:  str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    .. attribute:: ipv6_prefix
                                    
                                    	IPv6 context
                                    	**type**\:  str
                                    
                                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                    
                                    

                                    """

                                    _prefix = 'mpls-static-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(MplsStatic.Vrfs.Vrf.Lsps.Lsp.Label.BackupPathInfo.Nexthop.Address, self).__init__()

                                        self.yang_name = "address"
                                        self.yang_parent_name = "nexthop"

                                        self.af_name = YLeaf(YType.enumeration, "af-name")

                                        self.ipv4_prefix = YLeaf(YType.str, "ipv4-prefix")

                                        self.ipv6_prefix = YLeaf(YType.str, "ipv6-prefix")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("af_name",
                                                        "ipv4_prefix",
                                                        "ipv6_prefix") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(MplsStatic.Vrfs.Vrf.Lsps.Lsp.Label.BackupPathInfo.Nexthop.Address, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(MplsStatic.Vrfs.Vrf.Lsps.Lsp.Label.BackupPathInfo.Nexthop.Address, self).__setattr__(name, value)

                                    def has_data(self):
                                        return (
                                            self.af_name.is_set or
                                            self.ipv4_prefix.is_set or
                                            self.ipv6_prefix.is_set)

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.af_name.yfilter != YFilter.not_set or
                                            self.ipv4_prefix.yfilter != YFilter.not_set or
                                            self.ipv6_prefix.yfilter != YFilter.not_set)

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "address" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()
                                        if (self.af_name.is_set or self.af_name.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.af_name.get_name_leafdata())
                                        if (self.ipv4_prefix.is_set or self.ipv4_prefix.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.ipv4_prefix.get_name_leafdata())
                                        if (self.ipv6_prefix.is_set or self.ipv6_prefix.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.ipv6_prefix.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "af-name" or name == "ipv4-prefix" or name == "ipv6-prefix"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "af-name"):
                                            self.af_name = value
                                            self.af_name.value_namespace = name_space
                                            self.af_name.value_namespace_prefix = name_space_prefix
                                        if(value_path == "ipv4-prefix"):
                                            self.ipv4_prefix = value
                                            self.ipv4_prefix.value_namespace = name_space
                                            self.ipv4_prefix.value_namespace_prefix = name_space_prefix
                                        if(value_path == "ipv6-prefix"):
                                            self.ipv6_prefix = value
                                            self.ipv6_prefix.value_namespace = name_space
                                            self.ipv6_prefix.value_namespace_prefix = name_space_prefix

                                def has_data(self):
                                    return (
                                        self.afi.is_set or
                                        self.interface_name.is_set or
                                        self.label.is_set or
                                        (self.address is not None and self.address.has_data()))

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.afi.yfilter != YFilter.not_set or
                                        self.interface_name.yfilter != YFilter.not_set or
                                        self.label.yfilter != YFilter.not_set or
                                        (self.address is not None and self.address.has_operation()))

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "nexthop" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.afi.is_set or self.afi.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.afi.get_name_leafdata())
                                    if (self.interface_name.is_set or self.interface_name.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.interface_name.get_name_leafdata())
                                    if (self.label.is_set or self.label.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.label.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    if (child_yang_name == "address"):
                                        if (self.address is None):
                                            self.address = MplsStatic.Vrfs.Vrf.Lsps.Lsp.Label.BackupPathInfo.Nexthop.Address()
                                            self.address.parent = self
                                            self._children_name_map["address"] = "address"
                                        return self.address

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "address" or name == "afi" or name == "interface-name" or name == "label"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "afi"):
                                        self.afi = value
                                        self.afi.value_namespace = name_space
                                        self.afi.value_namespace_prefix = name_space_prefix
                                    if(value_path == "interface-name"):
                                        self.interface_name = value
                                        self.interface_name.value_namespace = name_space
                                        self.interface_name.value_namespace_prefix = name_space_prefix
                                    if(value_path == "label"):
                                        self.label = value
                                        self.label.value_namespace = name_space
                                        self.label.value_namespace_prefix = name_space_prefix

                            def has_data(self):
                                return (
                                    self.backup_id.is_set or
                                    self.path_id.is_set or
                                    self.path_number.is_set or
                                    self.path_role.is_set or
                                    self.status.is_set or
                                    self.type.is_set or
                                    (self.nexthop is not None and self.nexthop.has_data()))

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.backup_id.yfilter != YFilter.not_set or
                                    self.path_id.yfilter != YFilter.not_set or
                                    self.path_number.yfilter != YFilter.not_set or
                                    self.path_role.yfilter != YFilter.not_set or
                                    self.status.yfilter != YFilter.not_set or
                                    self.type.yfilter != YFilter.not_set or
                                    (self.nexthop is not None and self.nexthop.has_operation()))

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "backup-path-info" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.backup_id.is_set or self.backup_id.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.backup_id.get_name_leafdata())
                                if (self.path_id.is_set or self.path_id.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.path_id.get_name_leafdata())
                                if (self.path_number.is_set or self.path_number.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.path_number.get_name_leafdata())
                                if (self.path_role.is_set or self.path_role.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.path_role.get_name_leafdata())
                                if (self.status.is_set or self.status.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.status.get_name_leafdata())
                                if (self.type.is_set or self.type.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.type.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                if (child_yang_name == "nexthop"):
                                    if (self.nexthop is None):
                                        self.nexthop = MplsStatic.Vrfs.Vrf.Lsps.Lsp.Label.BackupPathInfo.Nexthop()
                                        self.nexthop.parent = self
                                        self._children_name_map["nexthop"] = "nexthop"
                                    return self.nexthop

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "nexthop" or name == "backup-id" or name == "path-id" or name == "path-number" or name == "path-role" or name == "status" or name == "type"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "backup-id"):
                                    self.backup_id = value
                                    self.backup_id.value_namespace = name_space
                                    self.backup_id.value_namespace_prefix = name_space_prefix
                                if(value_path == "path-id"):
                                    self.path_id = value
                                    self.path_id.value_namespace = name_space
                                    self.path_id.value_namespace_prefix = name_space_prefix
                                if(value_path == "path-number"):
                                    self.path_number = value
                                    self.path_number.value_namespace = name_space
                                    self.path_number.value_namespace_prefix = name_space_prefix
                                if(value_path == "path-role"):
                                    self.path_role = value
                                    self.path_role.value_namespace = name_space
                                    self.path_role.value_namespace_prefix = name_space_prefix
                                if(value_path == "status"):
                                    self.status = value
                                    self.status.value_namespace = name_space
                                    self.status.value_namespace_prefix = name_space_prefix
                                if(value_path == "type"):
                                    self.type = value
                                    self.type.value_namespace = name_space
                                    self.type.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            for c in self.backup_path_info:
                                if (c.has_data()):
                                    return True
                            for c in self.path_info:
                                if (c.has_data()):
                                    return True
                            return (
                                self.address_family.is_set or
                                self.backup_pathset_via_resolve.is_set or
                                self.label.is_set or
                                self.label_mode.is_set or
                                self.label_status.is_set or
                                self.pathset_via_resolve.is_set or
                                self.vrf_name.is_set or
                                (self.backup_pathset_resolve_nh is not None and self.backup_pathset_resolve_nh.has_data()) or
                                (self.pathset_resolve_nh is not None and self.pathset_resolve_nh.has_data()) or
                                (self.prefix is not None and self.prefix.has_data()))

                        def has_operation(self):
                            for c in self.backup_path_info:
                                if (c.has_operation()):
                                    return True
                            for c in self.path_info:
                                if (c.has_operation()):
                                    return True
                            return (
                                self.yfilter != YFilter.not_set or
                                self.address_family.yfilter != YFilter.not_set or
                                self.backup_pathset_via_resolve.yfilter != YFilter.not_set or
                                self.label.yfilter != YFilter.not_set or
                                self.label_mode.yfilter != YFilter.not_set or
                                self.label_status.yfilter != YFilter.not_set or
                                self.pathset_via_resolve.yfilter != YFilter.not_set or
                                self.vrf_name.yfilter != YFilter.not_set or
                                (self.backup_pathset_resolve_nh is not None and self.backup_pathset_resolve_nh.has_operation()) or
                                (self.pathset_resolve_nh is not None and self.pathset_resolve_nh.has_operation()) or
                                (self.prefix is not None and self.prefix.has_operation()))

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "label" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.address_family.is_set or self.address_family.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.address_family.get_name_leafdata())
                            if (self.backup_pathset_via_resolve.is_set or self.backup_pathset_via_resolve.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.backup_pathset_via_resolve.get_name_leafdata())
                            if (self.label.is_set or self.label.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.label.get_name_leafdata())
                            if (self.label_mode.is_set or self.label_mode.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.label_mode.get_name_leafdata())
                            if (self.label_status.is_set or self.label_status.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.label_status.get_name_leafdata())
                            if (self.pathset_via_resolve.is_set or self.pathset_via_resolve.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.pathset_via_resolve.get_name_leafdata())
                            if (self.vrf_name.is_set or self.vrf_name.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.vrf_name.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "backup-path-info"):
                                for c in self.backup_path_info:
                                    segment = c.get_segment_path()
                                    if (segment_path == segment):
                                        return c
                                c = MplsStatic.Vrfs.Vrf.Lsps.Lsp.Label.BackupPathInfo()
                                c.parent = self
                                local_reference_key = "ydk::seg::%s" % segment_path
                                self._local_refs[local_reference_key] = c
                                self.backup_path_info.append(c)
                                return c

                            if (child_yang_name == "backup-pathset-resolve-nh"):
                                if (self.backup_pathset_resolve_nh is None):
                                    self.backup_pathset_resolve_nh = MplsStatic.Vrfs.Vrf.Lsps.Lsp.Label.BackupPathsetResolveNh()
                                    self.backup_pathset_resolve_nh.parent = self
                                    self._children_name_map["backup_pathset_resolve_nh"] = "backup-pathset-resolve-nh"
                                return self.backup_pathset_resolve_nh

                            if (child_yang_name == "path-info"):
                                for c in self.path_info:
                                    segment = c.get_segment_path()
                                    if (segment_path == segment):
                                        return c
                                c = MplsStatic.Vrfs.Vrf.Lsps.Lsp.Label.PathInfo()
                                c.parent = self
                                local_reference_key = "ydk::seg::%s" % segment_path
                                self._local_refs[local_reference_key] = c
                                self.path_info.append(c)
                                return c

                            if (child_yang_name == "pathset-resolve-nh"):
                                if (self.pathset_resolve_nh is None):
                                    self.pathset_resolve_nh = MplsStatic.Vrfs.Vrf.Lsps.Lsp.Label.PathsetResolveNh()
                                    self.pathset_resolve_nh.parent = self
                                    self._children_name_map["pathset_resolve_nh"] = "pathset-resolve-nh"
                                return self.pathset_resolve_nh

                            if (child_yang_name == "prefix"):
                                if (self.prefix is None):
                                    self.prefix = MplsStatic.Vrfs.Vrf.Lsps.Lsp.Label.Prefix()
                                    self.prefix.parent = self
                                    self._children_name_map["prefix"] = "prefix"
                                return self.prefix

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "backup-path-info" or name == "backup-pathset-resolve-nh" or name == "path-info" or name == "pathset-resolve-nh" or name == "prefix" or name == "address-family" or name == "backup-pathset-via-resolve" or name == "label" or name == "label-mode" or name == "label-status" or name == "pathset-via-resolve" or name == "vrf-name"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "address-family"):
                                self.address_family = value
                                self.address_family.value_namespace = name_space
                                self.address_family.value_namespace_prefix = name_space_prefix
                            if(value_path == "backup-pathset-via-resolve"):
                                self.backup_pathset_via_resolve = value
                                self.backup_pathset_via_resolve.value_namespace = name_space
                                self.backup_pathset_via_resolve.value_namespace_prefix = name_space_prefix
                            if(value_path == "label"):
                                self.label = value
                                self.label.value_namespace = name_space
                                self.label.value_namespace_prefix = name_space_prefix
                            if(value_path == "label-mode"):
                                self.label_mode = value
                                self.label_mode.value_namespace = name_space
                                self.label_mode.value_namespace_prefix = name_space_prefix
                            if(value_path == "label-status"):
                                self.label_status = value
                                self.label_status.value_namespace = name_space
                                self.label_status.value_namespace_prefix = name_space_prefix
                            if(value_path == "pathset-via-resolve"):
                                self.pathset_via_resolve = value
                                self.pathset_via_resolve.value_namespace = name_space
                                self.pathset_via_resolve.value_namespace_prefix = name_space_prefix
                            if(value_path == "vrf-name"):
                                self.vrf_name = value
                                self.vrf_name.value_namespace = name_space
                                self.vrf_name.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        return (
                            self.lsp_name.is_set or
                            self.lsp_name_xr.is_set or
                            (self.label is not None and self.label.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.lsp_name.yfilter != YFilter.not_set or
                            self.lsp_name_xr.yfilter != YFilter.not_set or
                            (self.label is not None and self.label.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "lsp" + "[lsp-name='" + self.lsp_name.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.lsp_name.is_set or self.lsp_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.lsp_name.get_name_leafdata())
                        if (self.lsp_name_xr.is_set or self.lsp_name_xr.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.lsp_name_xr.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "label"):
                            if (self.label is None):
                                self.label = MplsStatic.Vrfs.Vrf.Lsps.Lsp.Label()
                                self.label.parent = self
                                self._children_name_map["label"] = "label"
                            return self.label

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "label" or name == "lsp-name" or name == "lsp-name-xr"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "lsp-name"):
                            self.lsp_name = value
                            self.lsp_name.value_namespace = name_space
                            self.lsp_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "lsp-name-xr"):
                            self.lsp_name_xr = value
                            self.lsp_name_xr.value_namespace = name_space
                            self.lsp_name_xr.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.lsp:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.lsp:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "lsps" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "lsp"):
                        for c in self.lsp:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = MplsStatic.Vrfs.Vrf.Lsps.Lsp()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.lsp.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "lsp"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class LocalLabels(Entity):
                """
                data for static local\-label table
                
                .. attribute:: local_label
                
                	Data for static label
                	**type**\: list of    :py:class:`LocalLabel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MplsStatic.Vrfs.Vrf.LocalLabels.LocalLabel>`
                
                

                """

                _prefix = 'mpls-static-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(MplsStatic.Vrfs.Vrf.LocalLabels, self).__init__()

                    self.yang_name = "local-labels"
                    self.yang_parent_name = "vrf"

                    self.local_label = YList(self)

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in () and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(MplsStatic.Vrfs.Vrf.LocalLabels, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(MplsStatic.Vrfs.Vrf.LocalLabels, self).__setattr__(name, value)


                class LocalLabel(Entity):
                    """
                    Data for static label
                    
                    .. attribute:: local_label_id  <key>
                    
                    	Local Label
                    	**type**\:  int
                    
                    	**range:** 16..1048575
                    
                    .. attribute:: address_family
                    
                    	Address Family
                    	**type**\:   :py:class:`MgmtStaticAddr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MgmtStaticAddr>`
                    
                    .. attribute:: backup_path_info
                    
                    	Backup Path Information
                    	**type**\: list of    :py:class:`BackupPathInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MplsStatic.Vrfs.Vrf.LocalLabels.LocalLabel.BackupPathInfo>`
                    
                    .. attribute:: backup_pathset_resolve_nh
                    
                    	Backup pathset resolve\-nexthop IP Address
                    	**type**\:   :py:class:`BackupPathsetResolveNh <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MplsStatic.Vrfs.Vrf.LocalLabels.LocalLabel.BackupPathsetResolveNh>`
                    
                    .. attribute:: backup_pathset_via_resolve
                    
                    	Backup Pathset as a result of resolve
                    	**type**\:  bool
                    
                    .. attribute:: label
                    
                    	Label value
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: label_mode
                    
                    	Label Mode
                    	**type**\:   :py:class:`MgmtMplsStaticLabelMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MgmtMplsStaticLabelMode>`
                    
                    .. attribute:: label_status
                    
                    	Label Status
                    	**type**\:   :py:class:`MgmtMplsStaticLabelStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MgmtMplsStaticLabelStatus>`
                    
                    .. attribute:: path_info
                    
                    	Path Information
                    	**type**\: list of    :py:class:`PathInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MplsStatic.Vrfs.Vrf.LocalLabels.LocalLabel.PathInfo>`
                    
                    .. attribute:: pathset_resolve_nh
                    
                    	Primary pathset resolve\-nexthop IP Address
                    	**type**\:   :py:class:`PathsetResolveNh <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MplsStatic.Vrfs.Vrf.LocalLabels.LocalLabel.PathsetResolveNh>`
                    
                    .. attribute:: pathset_via_resolve
                    
                    	Primary Pathset as a result of resolve
                    	**type**\:  bool
                    
                    .. attribute:: prefix
                    
                    	Prefix Information
                    	**type**\:   :py:class:`Prefix <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MplsStatic.Vrfs.Vrf.LocalLabels.LocalLabel.Prefix>`
                    
                    .. attribute:: vrf_name
                    
                    	VRF name
                    	**type**\:  str
                    
                    

                    """

                    _prefix = 'mpls-static-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(MplsStatic.Vrfs.Vrf.LocalLabels.LocalLabel, self).__init__()

                        self.yang_name = "local-label"
                        self.yang_parent_name = "local-labels"

                        self.local_label_id = YLeaf(YType.uint32, "local-label-id")

                        self.address_family = YLeaf(YType.enumeration, "address-family")

                        self.backup_pathset_via_resolve = YLeaf(YType.boolean, "backup-pathset-via-resolve")

                        self.label = YLeaf(YType.uint32, "label")

                        self.label_mode = YLeaf(YType.enumeration, "label-mode")

                        self.label_status = YLeaf(YType.enumeration, "label-status")

                        self.pathset_via_resolve = YLeaf(YType.boolean, "pathset-via-resolve")

                        self.vrf_name = YLeaf(YType.str, "vrf-name")

                        self.backup_pathset_resolve_nh = MplsStatic.Vrfs.Vrf.LocalLabels.LocalLabel.BackupPathsetResolveNh()
                        self.backup_pathset_resolve_nh.parent = self
                        self._children_name_map["backup_pathset_resolve_nh"] = "backup-pathset-resolve-nh"
                        self._children_yang_names.add("backup-pathset-resolve-nh")

                        self.pathset_resolve_nh = MplsStatic.Vrfs.Vrf.LocalLabels.LocalLabel.PathsetResolveNh()
                        self.pathset_resolve_nh.parent = self
                        self._children_name_map["pathset_resolve_nh"] = "pathset-resolve-nh"
                        self._children_yang_names.add("pathset-resolve-nh")

                        self.prefix = MplsStatic.Vrfs.Vrf.LocalLabels.LocalLabel.Prefix()
                        self.prefix.parent = self
                        self._children_name_map["prefix"] = "prefix"
                        self._children_yang_names.add("prefix")

                        self.backup_path_info = YList(self)
                        self.path_info = YList(self)

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("local_label_id",
                                        "address_family",
                                        "backup_pathset_via_resolve",
                                        "label",
                                        "label_mode",
                                        "label_status",
                                        "pathset_via_resolve",
                                        "vrf_name") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(MplsStatic.Vrfs.Vrf.LocalLabels.LocalLabel, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(MplsStatic.Vrfs.Vrf.LocalLabels.LocalLabel, self).__setattr__(name, value)


                    class Prefix(Entity):
                        """
                        Prefix Information
                        
                        .. attribute:: prefix
                        
                        	Prefix
                        	**type**\:   :py:class:`Prefix <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MplsStatic.Vrfs.Vrf.LocalLabels.LocalLabel.Prefix.Prefix>`
                        
                        .. attribute:: prefix_length
                        
                        	Prefix length
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        

                        """

                        _prefix = 'mpls-static-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(MplsStatic.Vrfs.Vrf.LocalLabels.LocalLabel.Prefix, self).__init__()

                            self.yang_name = "prefix"
                            self.yang_parent_name = "local-label"

                            self.prefix_length = YLeaf(YType.uint8, "prefix-length")

                            self.prefix = MplsStatic.Vrfs.Vrf.LocalLabels.LocalLabel.Prefix.Prefix()
                            self.prefix.parent = self
                            self._children_name_map["prefix"] = "prefix"
                            self._children_yang_names.add("prefix")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("prefix_length") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(MplsStatic.Vrfs.Vrf.LocalLabels.LocalLabel.Prefix, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(MplsStatic.Vrfs.Vrf.LocalLabels.LocalLabel.Prefix, self).__setattr__(name, value)


                        class Prefix(Entity):
                            """
                            Prefix
                            
                            .. attribute:: af_name
                            
                            	AFName
                            	**type**\:   :py:class:`MgmtStaticAddr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MgmtStaticAddr>`
                            
                            .. attribute:: ipv4_prefix
                            
                            	IPv4 context
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: ipv6_prefix
                            
                            	IPv6 context
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            

                            """

                            _prefix = 'mpls-static-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(MplsStatic.Vrfs.Vrf.LocalLabels.LocalLabel.Prefix.Prefix, self).__init__()

                                self.yang_name = "prefix"
                                self.yang_parent_name = "prefix"

                                self.af_name = YLeaf(YType.enumeration, "af-name")

                                self.ipv4_prefix = YLeaf(YType.str, "ipv4-prefix")

                                self.ipv6_prefix = YLeaf(YType.str, "ipv6-prefix")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("af_name",
                                                "ipv4_prefix",
                                                "ipv6_prefix") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(MplsStatic.Vrfs.Vrf.LocalLabels.LocalLabel.Prefix.Prefix, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(MplsStatic.Vrfs.Vrf.LocalLabels.LocalLabel.Prefix.Prefix, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.af_name.is_set or
                                    self.ipv4_prefix.is_set or
                                    self.ipv6_prefix.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.af_name.yfilter != YFilter.not_set or
                                    self.ipv4_prefix.yfilter != YFilter.not_set or
                                    self.ipv6_prefix.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "prefix" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.af_name.is_set or self.af_name.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.af_name.get_name_leafdata())
                                if (self.ipv4_prefix.is_set or self.ipv4_prefix.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.ipv4_prefix.get_name_leafdata())
                                if (self.ipv6_prefix.is_set or self.ipv6_prefix.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.ipv6_prefix.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "af-name" or name == "ipv4-prefix" or name == "ipv6-prefix"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "af-name"):
                                    self.af_name = value
                                    self.af_name.value_namespace = name_space
                                    self.af_name.value_namespace_prefix = name_space_prefix
                                if(value_path == "ipv4-prefix"):
                                    self.ipv4_prefix = value
                                    self.ipv4_prefix.value_namespace = name_space
                                    self.ipv4_prefix.value_namespace_prefix = name_space_prefix
                                if(value_path == "ipv6-prefix"):
                                    self.ipv6_prefix = value
                                    self.ipv6_prefix.value_namespace = name_space
                                    self.ipv6_prefix.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            return (
                                self.prefix_length.is_set or
                                (self.prefix is not None and self.prefix.has_data()))

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.prefix_length.yfilter != YFilter.not_set or
                                (self.prefix is not None and self.prefix.has_operation()))

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "prefix" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.prefix_length.is_set or self.prefix_length.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.prefix_length.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "prefix"):
                                if (self.prefix is None):
                                    self.prefix = MplsStatic.Vrfs.Vrf.LocalLabels.LocalLabel.Prefix.Prefix()
                                    self.prefix.parent = self
                                    self._children_name_map["prefix"] = "prefix"
                                return self.prefix

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "prefix" or name == "prefix-length"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "prefix-length"):
                                self.prefix_length = value
                                self.prefix_length.value_namespace = name_space
                                self.prefix_length.value_namespace_prefix = name_space_prefix


                    class PathsetResolveNh(Entity):
                        """
                        Primary pathset resolve\-nexthop IP Address
                        
                        .. attribute:: af_name
                        
                        	AFName
                        	**type**\:   :py:class:`MgmtStaticAddr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MgmtStaticAddr>`
                        
                        .. attribute:: ipv4_prefix
                        
                        	IPv4 context
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: ipv6_prefix
                        
                        	IPv6 context
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        

                        """

                        _prefix = 'mpls-static-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(MplsStatic.Vrfs.Vrf.LocalLabels.LocalLabel.PathsetResolveNh, self).__init__()

                            self.yang_name = "pathset-resolve-nh"
                            self.yang_parent_name = "local-label"

                            self.af_name = YLeaf(YType.enumeration, "af-name")

                            self.ipv4_prefix = YLeaf(YType.str, "ipv4-prefix")

                            self.ipv6_prefix = YLeaf(YType.str, "ipv6-prefix")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("af_name",
                                            "ipv4_prefix",
                                            "ipv6_prefix") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(MplsStatic.Vrfs.Vrf.LocalLabels.LocalLabel.PathsetResolveNh, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(MplsStatic.Vrfs.Vrf.LocalLabels.LocalLabel.PathsetResolveNh, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.af_name.is_set or
                                self.ipv4_prefix.is_set or
                                self.ipv6_prefix.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.af_name.yfilter != YFilter.not_set or
                                self.ipv4_prefix.yfilter != YFilter.not_set or
                                self.ipv6_prefix.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "pathset-resolve-nh" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.af_name.is_set or self.af_name.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.af_name.get_name_leafdata())
                            if (self.ipv4_prefix.is_set or self.ipv4_prefix.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.ipv4_prefix.get_name_leafdata())
                            if (self.ipv6_prefix.is_set or self.ipv6_prefix.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.ipv6_prefix.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "af-name" or name == "ipv4-prefix" or name == "ipv6-prefix"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "af-name"):
                                self.af_name = value
                                self.af_name.value_namespace = name_space
                                self.af_name.value_namespace_prefix = name_space_prefix
                            if(value_path == "ipv4-prefix"):
                                self.ipv4_prefix = value
                                self.ipv4_prefix.value_namespace = name_space
                                self.ipv4_prefix.value_namespace_prefix = name_space_prefix
                            if(value_path == "ipv6-prefix"):
                                self.ipv6_prefix = value
                                self.ipv6_prefix.value_namespace = name_space
                                self.ipv6_prefix.value_namespace_prefix = name_space_prefix


                    class BackupPathsetResolveNh(Entity):
                        """
                        Backup pathset resolve\-nexthop IP Address
                        
                        .. attribute:: af_name
                        
                        	AFName
                        	**type**\:   :py:class:`MgmtStaticAddr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MgmtStaticAddr>`
                        
                        .. attribute:: ipv4_prefix
                        
                        	IPv4 context
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: ipv6_prefix
                        
                        	IPv6 context
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        

                        """

                        _prefix = 'mpls-static-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(MplsStatic.Vrfs.Vrf.LocalLabels.LocalLabel.BackupPathsetResolveNh, self).__init__()

                            self.yang_name = "backup-pathset-resolve-nh"
                            self.yang_parent_name = "local-label"

                            self.af_name = YLeaf(YType.enumeration, "af-name")

                            self.ipv4_prefix = YLeaf(YType.str, "ipv4-prefix")

                            self.ipv6_prefix = YLeaf(YType.str, "ipv6-prefix")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("af_name",
                                            "ipv4_prefix",
                                            "ipv6_prefix") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(MplsStatic.Vrfs.Vrf.LocalLabels.LocalLabel.BackupPathsetResolveNh, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(MplsStatic.Vrfs.Vrf.LocalLabels.LocalLabel.BackupPathsetResolveNh, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.af_name.is_set or
                                self.ipv4_prefix.is_set or
                                self.ipv6_prefix.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.af_name.yfilter != YFilter.not_set or
                                self.ipv4_prefix.yfilter != YFilter.not_set or
                                self.ipv6_prefix.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "backup-pathset-resolve-nh" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.af_name.is_set or self.af_name.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.af_name.get_name_leafdata())
                            if (self.ipv4_prefix.is_set or self.ipv4_prefix.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.ipv4_prefix.get_name_leafdata())
                            if (self.ipv6_prefix.is_set or self.ipv6_prefix.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.ipv6_prefix.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "af-name" or name == "ipv4-prefix" or name == "ipv6-prefix"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "af-name"):
                                self.af_name = value
                                self.af_name.value_namespace = name_space
                                self.af_name.value_namespace_prefix = name_space_prefix
                            if(value_path == "ipv4-prefix"):
                                self.ipv4_prefix = value
                                self.ipv4_prefix.value_namespace = name_space
                                self.ipv4_prefix.value_namespace_prefix = name_space_prefix
                            if(value_path == "ipv6-prefix"):
                                self.ipv6_prefix = value
                                self.ipv6_prefix.value_namespace = name_space
                                self.ipv6_prefix.value_namespace_prefix = name_space_prefix


                    class PathInfo(Entity):
                        """
                        Path Information
                        
                        .. attribute:: backup_id
                        
                        	Path Backup Id
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: nexthop
                        
                        	Nexthop information
                        	**type**\:   :py:class:`Nexthop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MplsStatic.Vrfs.Vrf.LocalLabels.LocalLabel.PathInfo.Nexthop>`
                        
                        .. attribute:: path_id
                        
                        	Path Id
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: path_number
                        
                        	Path Number
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: path_role
                        
                        	Path Role
                        	**type**\:   :py:class:`MplsStaticPathRole <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MplsStaticPathRole>`
                        
                        .. attribute:: status
                        
                        	Path Status
                        	**type**\:   :py:class:`MgmtMplsStaticPathStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MgmtMplsStaticPathStatus>`
                        
                        .. attribute:: type
                        
                        	Path Type
                        	**type**\:   :py:class:`MgmtStaticPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MgmtStaticPath>`
                        
                        

                        """

                        _prefix = 'mpls-static-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(MplsStatic.Vrfs.Vrf.LocalLabels.LocalLabel.PathInfo, self).__init__()

                            self.yang_name = "path-info"
                            self.yang_parent_name = "local-label"

                            self.backup_id = YLeaf(YType.uint8, "backup-id")

                            self.path_id = YLeaf(YType.uint8, "path-id")

                            self.path_number = YLeaf(YType.uint32, "path-number")

                            self.path_role = YLeaf(YType.enumeration, "path-role")

                            self.status = YLeaf(YType.enumeration, "status")

                            self.type = YLeaf(YType.enumeration, "type")

                            self.nexthop = MplsStatic.Vrfs.Vrf.LocalLabels.LocalLabel.PathInfo.Nexthop()
                            self.nexthop.parent = self
                            self._children_name_map["nexthop"] = "nexthop"
                            self._children_yang_names.add("nexthop")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("backup_id",
                                            "path_id",
                                            "path_number",
                                            "path_role",
                                            "status",
                                            "type") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(MplsStatic.Vrfs.Vrf.LocalLabels.LocalLabel.PathInfo, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(MplsStatic.Vrfs.Vrf.LocalLabels.LocalLabel.PathInfo, self).__setattr__(name, value)


                        class Nexthop(Entity):
                            """
                            Nexthop information
                            
                            .. attribute:: address
                            
                            	Next\-Hop IP Address
                            	**type**\:   :py:class:`Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MplsStatic.Vrfs.Vrf.LocalLabels.LocalLabel.PathInfo.Nexthop.Address>`
                            
                            .. attribute:: afi
                            
                            	Next\-Hop AFI
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: interface_name
                            
                            	Next\-Hop Interface Name
                            	**type**\:  str
                            
                            .. attribute:: label
                            
                            	Next\-Hop Label
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'mpls-static-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(MplsStatic.Vrfs.Vrf.LocalLabels.LocalLabel.PathInfo.Nexthop, self).__init__()

                                self.yang_name = "nexthop"
                                self.yang_parent_name = "path-info"

                                self.afi = YLeaf(YType.uint32, "afi")

                                self.interface_name = YLeaf(YType.str, "interface-name")

                                self.label = YLeaf(YType.uint32, "label")

                                self.address = MplsStatic.Vrfs.Vrf.LocalLabels.LocalLabel.PathInfo.Nexthop.Address()
                                self.address.parent = self
                                self._children_name_map["address"] = "address"
                                self._children_yang_names.add("address")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("afi",
                                                "interface_name",
                                                "label") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(MplsStatic.Vrfs.Vrf.LocalLabels.LocalLabel.PathInfo.Nexthop, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(MplsStatic.Vrfs.Vrf.LocalLabels.LocalLabel.PathInfo.Nexthop, self).__setattr__(name, value)


                            class Address(Entity):
                                """
                                Next\-Hop IP Address
                                
                                .. attribute:: af_name
                                
                                	AFName
                                	**type**\:   :py:class:`MgmtStaticAddr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MgmtStaticAddr>`
                                
                                .. attribute:: ipv4_prefix
                                
                                	IPv4 context
                                	**type**\:  str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: ipv6_prefix
                                
                                	IPv6 context
                                	**type**\:  str
                                
                                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                
                                

                                """

                                _prefix = 'mpls-static-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(MplsStatic.Vrfs.Vrf.LocalLabels.LocalLabel.PathInfo.Nexthop.Address, self).__init__()

                                    self.yang_name = "address"
                                    self.yang_parent_name = "nexthop"

                                    self.af_name = YLeaf(YType.enumeration, "af-name")

                                    self.ipv4_prefix = YLeaf(YType.str, "ipv4-prefix")

                                    self.ipv6_prefix = YLeaf(YType.str, "ipv6-prefix")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("af_name",
                                                    "ipv4_prefix",
                                                    "ipv6_prefix") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(MplsStatic.Vrfs.Vrf.LocalLabels.LocalLabel.PathInfo.Nexthop.Address, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(MplsStatic.Vrfs.Vrf.LocalLabels.LocalLabel.PathInfo.Nexthop.Address, self).__setattr__(name, value)

                                def has_data(self):
                                    return (
                                        self.af_name.is_set or
                                        self.ipv4_prefix.is_set or
                                        self.ipv6_prefix.is_set)

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.af_name.yfilter != YFilter.not_set or
                                        self.ipv4_prefix.yfilter != YFilter.not_set or
                                        self.ipv6_prefix.yfilter != YFilter.not_set)

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "address" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.af_name.is_set or self.af_name.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.af_name.get_name_leafdata())
                                    if (self.ipv4_prefix.is_set or self.ipv4_prefix.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.ipv4_prefix.get_name_leafdata())
                                    if (self.ipv6_prefix.is_set or self.ipv6_prefix.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.ipv6_prefix.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "af-name" or name == "ipv4-prefix" or name == "ipv6-prefix"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "af-name"):
                                        self.af_name = value
                                        self.af_name.value_namespace = name_space
                                        self.af_name.value_namespace_prefix = name_space_prefix
                                    if(value_path == "ipv4-prefix"):
                                        self.ipv4_prefix = value
                                        self.ipv4_prefix.value_namespace = name_space
                                        self.ipv4_prefix.value_namespace_prefix = name_space_prefix
                                    if(value_path == "ipv6-prefix"):
                                        self.ipv6_prefix = value
                                        self.ipv6_prefix.value_namespace = name_space
                                        self.ipv6_prefix.value_namespace_prefix = name_space_prefix

                            def has_data(self):
                                return (
                                    self.afi.is_set or
                                    self.interface_name.is_set or
                                    self.label.is_set or
                                    (self.address is not None and self.address.has_data()))

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.afi.yfilter != YFilter.not_set or
                                    self.interface_name.yfilter != YFilter.not_set or
                                    self.label.yfilter != YFilter.not_set or
                                    (self.address is not None and self.address.has_operation()))

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "nexthop" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.afi.is_set or self.afi.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.afi.get_name_leafdata())
                                if (self.interface_name.is_set or self.interface_name.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.interface_name.get_name_leafdata())
                                if (self.label.is_set or self.label.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.label.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                if (child_yang_name == "address"):
                                    if (self.address is None):
                                        self.address = MplsStatic.Vrfs.Vrf.LocalLabels.LocalLabel.PathInfo.Nexthop.Address()
                                        self.address.parent = self
                                        self._children_name_map["address"] = "address"
                                    return self.address

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "address" or name == "afi" or name == "interface-name" or name == "label"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "afi"):
                                    self.afi = value
                                    self.afi.value_namespace = name_space
                                    self.afi.value_namespace_prefix = name_space_prefix
                                if(value_path == "interface-name"):
                                    self.interface_name = value
                                    self.interface_name.value_namespace = name_space
                                    self.interface_name.value_namespace_prefix = name_space_prefix
                                if(value_path == "label"):
                                    self.label = value
                                    self.label.value_namespace = name_space
                                    self.label.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            return (
                                self.backup_id.is_set or
                                self.path_id.is_set or
                                self.path_number.is_set or
                                self.path_role.is_set or
                                self.status.is_set or
                                self.type.is_set or
                                (self.nexthop is not None and self.nexthop.has_data()))

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.backup_id.yfilter != YFilter.not_set or
                                self.path_id.yfilter != YFilter.not_set or
                                self.path_number.yfilter != YFilter.not_set or
                                self.path_role.yfilter != YFilter.not_set or
                                self.status.yfilter != YFilter.not_set or
                                self.type.yfilter != YFilter.not_set or
                                (self.nexthop is not None and self.nexthop.has_operation()))

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "path-info" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.backup_id.is_set or self.backup_id.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.backup_id.get_name_leafdata())
                            if (self.path_id.is_set or self.path_id.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.path_id.get_name_leafdata())
                            if (self.path_number.is_set or self.path_number.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.path_number.get_name_leafdata())
                            if (self.path_role.is_set or self.path_role.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.path_role.get_name_leafdata())
                            if (self.status.is_set or self.status.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.status.get_name_leafdata())
                            if (self.type.is_set or self.type.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.type.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "nexthop"):
                                if (self.nexthop is None):
                                    self.nexthop = MplsStatic.Vrfs.Vrf.LocalLabels.LocalLabel.PathInfo.Nexthop()
                                    self.nexthop.parent = self
                                    self._children_name_map["nexthop"] = "nexthop"
                                return self.nexthop

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "nexthop" or name == "backup-id" or name == "path-id" or name == "path-number" or name == "path-role" or name == "status" or name == "type"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "backup-id"):
                                self.backup_id = value
                                self.backup_id.value_namespace = name_space
                                self.backup_id.value_namespace_prefix = name_space_prefix
                            if(value_path == "path-id"):
                                self.path_id = value
                                self.path_id.value_namespace = name_space
                                self.path_id.value_namespace_prefix = name_space_prefix
                            if(value_path == "path-number"):
                                self.path_number = value
                                self.path_number.value_namespace = name_space
                                self.path_number.value_namespace_prefix = name_space_prefix
                            if(value_path == "path-role"):
                                self.path_role = value
                                self.path_role.value_namespace = name_space
                                self.path_role.value_namespace_prefix = name_space_prefix
                            if(value_path == "status"):
                                self.status = value
                                self.status.value_namespace = name_space
                                self.status.value_namespace_prefix = name_space_prefix
                            if(value_path == "type"):
                                self.type = value
                                self.type.value_namespace = name_space
                                self.type.value_namespace_prefix = name_space_prefix


                    class BackupPathInfo(Entity):
                        """
                        Backup Path Information
                        
                        .. attribute:: backup_id
                        
                        	Path Backup Id
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: nexthop
                        
                        	Nexthop information
                        	**type**\:   :py:class:`Nexthop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MplsStatic.Vrfs.Vrf.LocalLabels.LocalLabel.BackupPathInfo.Nexthop>`
                        
                        .. attribute:: path_id
                        
                        	Path Id
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        .. attribute:: path_number
                        
                        	Path Number
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: path_role
                        
                        	Path Role
                        	**type**\:   :py:class:`MplsStaticPathRole <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MplsStaticPathRole>`
                        
                        .. attribute:: status
                        
                        	Path Status
                        	**type**\:   :py:class:`MgmtMplsStaticPathStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MgmtMplsStaticPathStatus>`
                        
                        .. attribute:: type
                        
                        	Path Type
                        	**type**\:   :py:class:`MgmtStaticPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MgmtStaticPath>`
                        
                        

                        """

                        _prefix = 'mpls-static-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(MplsStatic.Vrfs.Vrf.LocalLabels.LocalLabel.BackupPathInfo, self).__init__()

                            self.yang_name = "backup-path-info"
                            self.yang_parent_name = "local-label"

                            self.backup_id = YLeaf(YType.uint8, "backup-id")

                            self.path_id = YLeaf(YType.uint8, "path-id")

                            self.path_number = YLeaf(YType.uint32, "path-number")

                            self.path_role = YLeaf(YType.enumeration, "path-role")

                            self.status = YLeaf(YType.enumeration, "status")

                            self.type = YLeaf(YType.enumeration, "type")

                            self.nexthop = MplsStatic.Vrfs.Vrf.LocalLabels.LocalLabel.BackupPathInfo.Nexthop()
                            self.nexthop.parent = self
                            self._children_name_map["nexthop"] = "nexthop"
                            self._children_yang_names.add("nexthop")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("backup_id",
                                            "path_id",
                                            "path_number",
                                            "path_role",
                                            "status",
                                            "type") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(MplsStatic.Vrfs.Vrf.LocalLabels.LocalLabel.BackupPathInfo, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(MplsStatic.Vrfs.Vrf.LocalLabels.LocalLabel.BackupPathInfo, self).__setattr__(name, value)


                        class Nexthop(Entity):
                            """
                            Nexthop information
                            
                            .. attribute:: address
                            
                            	Next\-Hop IP Address
                            	**type**\:   :py:class:`Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MplsStatic.Vrfs.Vrf.LocalLabels.LocalLabel.BackupPathInfo.Nexthop.Address>`
                            
                            .. attribute:: afi
                            
                            	Next\-Hop AFI
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: interface_name
                            
                            	Next\-Hop Interface Name
                            	**type**\:  str
                            
                            .. attribute:: label
                            
                            	Next\-Hop Label
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'mpls-static-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(MplsStatic.Vrfs.Vrf.LocalLabels.LocalLabel.BackupPathInfo.Nexthop, self).__init__()

                                self.yang_name = "nexthop"
                                self.yang_parent_name = "backup-path-info"

                                self.afi = YLeaf(YType.uint32, "afi")

                                self.interface_name = YLeaf(YType.str, "interface-name")

                                self.label = YLeaf(YType.uint32, "label")

                                self.address = MplsStatic.Vrfs.Vrf.LocalLabels.LocalLabel.BackupPathInfo.Nexthop.Address()
                                self.address.parent = self
                                self._children_name_map["address"] = "address"
                                self._children_yang_names.add("address")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("afi",
                                                "interface_name",
                                                "label") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(MplsStatic.Vrfs.Vrf.LocalLabels.LocalLabel.BackupPathInfo.Nexthop, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(MplsStatic.Vrfs.Vrf.LocalLabels.LocalLabel.BackupPathInfo.Nexthop, self).__setattr__(name, value)


                            class Address(Entity):
                                """
                                Next\-Hop IP Address
                                
                                .. attribute:: af_name
                                
                                	AFName
                                	**type**\:   :py:class:`MgmtStaticAddr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MgmtStaticAddr>`
                                
                                .. attribute:: ipv4_prefix
                                
                                	IPv4 context
                                	**type**\:  str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: ipv6_prefix
                                
                                	IPv6 context
                                	**type**\:  str
                                
                                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                
                                

                                """

                                _prefix = 'mpls-static-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(MplsStatic.Vrfs.Vrf.LocalLabels.LocalLabel.BackupPathInfo.Nexthop.Address, self).__init__()

                                    self.yang_name = "address"
                                    self.yang_parent_name = "nexthop"

                                    self.af_name = YLeaf(YType.enumeration, "af-name")

                                    self.ipv4_prefix = YLeaf(YType.str, "ipv4-prefix")

                                    self.ipv6_prefix = YLeaf(YType.str, "ipv6-prefix")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("af_name",
                                                    "ipv4_prefix",
                                                    "ipv6_prefix") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(MplsStatic.Vrfs.Vrf.LocalLabels.LocalLabel.BackupPathInfo.Nexthop.Address, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(MplsStatic.Vrfs.Vrf.LocalLabels.LocalLabel.BackupPathInfo.Nexthop.Address, self).__setattr__(name, value)

                                def has_data(self):
                                    return (
                                        self.af_name.is_set or
                                        self.ipv4_prefix.is_set or
                                        self.ipv6_prefix.is_set)

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.af_name.yfilter != YFilter.not_set or
                                        self.ipv4_prefix.yfilter != YFilter.not_set or
                                        self.ipv6_prefix.yfilter != YFilter.not_set)

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "address" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.af_name.is_set or self.af_name.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.af_name.get_name_leafdata())
                                    if (self.ipv4_prefix.is_set or self.ipv4_prefix.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.ipv4_prefix.get_name_leafdata())
                                    if (self.ipv6_prefix.is_set or self.ipv6_prefix.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.ipv6_prefix.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "af-name" or name == "ipv4-prefix" or name == "ipv6-prefix"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "af-name"):
                                        self.af_name = value
                                        self.af_name.value_namespace = name_space
                                        self.af_name.value_namespace_prefix = name_space_prefix
                                    if(value_path == "ipv4-prefix"):
                                        self.ipv4_prefix = value
                                        self.ipv4_prefix.value_namespace = name_space
                                        self.ipv4_prefix.value_namespace_prefix = name_space_prefix
                                    if(value_path == "ipv6-prefix"):
                                        self.ipv6_prefix = value
                                        self.ipv6_prefix.value_namespace = name_space
                                        self.ipv6_prefix.value_namespace_prefix = name_space_prefix

                            def has_data(self):
                                return (
                                    self.afi.is_set or
                                    self.interface_name.is_set or
                                    self.label.is_set or
                                    (self.address is not None and self.address.has_data()))

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.afi.yfilter != YFilter.not_set or
                                    self.interface_name.yfilter != YFilter.not_set or
                                    self.label.yfilter != YFilter.not_set or
                                    (self.address is not None and self.address.has_operation()))

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "nexthop" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.afi.is_set or self.afi.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.afi.get_name_leafdata())
                                if (self.interface_name.is_set or self.interface_name.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.interface_name.get_name_leafdata())
                                if (self.label.is_set or self.label.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.label.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                if (child_yang_name == "address"):
                                    if (self.address is None):
                                        self.address = MplsStatic.Vrfs.Vrf.LocalLabels.LocalLabel.BackupPathInfo.Nexthop.Address()
                                        self.address.parent = self
                                        self._children_name_map["address"] = "address"
                                    return self.address

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "address" or name == "afi" or name == "interface-name" or name == "label"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "afi"):
                                    self.afi = value
                                    self.afi.value_namespace = name_space
                                    self.afi.value_namespace_prefix = name_space_prefix
                                if(value_path == "interface-name"):
                                    self.interface_name = value
                                    self.interface_name.value_namespace = name_space
                                    self.interface_name.value_namespace_prefix = name_space_prefix
                                if(value_path == "label"):
                                    self.label = value
                                    self.label.value_namespace = name_space
                                    self.label.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            return (
                                self.backup_id.is_set or
                                self.path_id.is_set or
                                self.path_number.is_set or
                                self.path_role.is_set or
                                self.status.is_set or
                                self.type.is_set or
                                (self.nexthop is not None and self.nexthop.has_data()))

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.backup_id.yfilter != YFilter.not_set or
                                self.path_id.yfilter != YFilter.not_set or
                                self.path_number.yfilter != YFilter.not_set or
                                self.path_role.yfilter != YFilter.not_set or
                                self.status.yfilter != YFilter.not_set or
                                self.type.yfilter != YFilter.not_set or
                                (self.nexthop is not None and self.nexthop.has_operation()))

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "backup-path-info" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.backup_id.is_set or self.backup_id.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.backup_id.get_name_leafdata())
                            if (self.path_id.is_set or self.path_id.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.path_id.get_name_leafdata())
                            if (self.path_number.is_set or self.path_number.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.path_number.get_name_leafdata())
                            if (self.path_role.is_set or self.path_role.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.path_role.get_name_leafdata())
                            if (self.status.is_set or self.status.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.status.get_name_leafdata())
                            if (self.type.is_set or self.type.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.type.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "nexthop"):
                                if (self.nexthop is None):
                                    self.nexthop = MplsStatic.Vrfs.Vrf.LocalLabels.LocalLabel.BackupPathInfo.Nexthop()
                                    self.nexthop.parent = self
                                    self._children_name_map["nexthop"] = "nexthop"
                                return self.nexthop

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "nexthop" or name == "backup-id" or name == "path-id" or name == "path-number" or name == "path-role" or name == "status" or name == "type"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "backup-id"):
                                self.backup_id = value
                                self.backup_id.value_namespace = name_space
                                self.backup_id.value_namespace_prefix = name_space_prefix
                            if(value_path == "path-id"):
                                self.path_id = value
                                self.path_id.value_namespace = name_space
                                self.path_id.value_namespace_prefix = name_space_prefix
                            if(value_path == "path-number"):
                                self.path_number = value
                                self.path_number.value_namespace = name_space
                                self.path_number.value_namespace_prefix = name_space_prefix
                            if(value_path == "path-role"):
                                self.path_role = value
                                self.path_role.value_namespace = name_space
                                self.path_role.value_namespace_prefix = name_space_prefix
                            if(value_path == "status"):
                                self.status = value
                                self.status.value_namespace = name_space
                                self.status.value_namespace_prefix = name_space_prefix
                            if(value_path == "type"):
                                self.type = value
                                self.type.value_namespace = name_space
                                self.type.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.backup_path_info:
                            if (c.has_data()):
                                return True
                        for c in self.path_info:
                            if (c.has_data()):
                                return True
                        return (
                            self.local_label_id.is_set or
                            self.address_family.is_set or
                            self.backup_pathset_via_resolve.is_set or
                            self.label.is_set or
                            self.label_mode.is_set or
                            self.label_status.is_set or
                            self.pathset_via_resolve.is_set or
                            self.vrf_name.is_set or
                            (self.backup_pathset_resolve_nh is not None and self.backup_pathset_resolve_nh.has_data()) or
                            (self.pathset_resolve_nh is not None and self.pathset_resolve_nh.has_data()) or
                            (self.prefix is not None and self.prefix.has_data()))

                    def has_operation(self):
                        for c in self.backup_path_info:
                            if (c.has_operation()):
                                return True
                        for c in self.path_info:
                            if (c.has_operation()):
                                return True
                        return (
                            self.yfilter != YFilter.not_set or
                            self.local_label_id.yfilter != YFilter.not_set or
                            self.address_family.yfilter != YFilter.not_set or
                            self.backup_pathset_via_resolve.yfilter != YFilter.not_set or
                            self.label.yfilter != YFilter.not_set or
                            self.label_mode.yfilter != YFilter.not_set or
                            self.label_status.yfilter != YFilter.not_set or
                            self.pathset_via_resolve.yfilter != YFilter.not_set or
                            self.vrf_name.yfilter != YFilter.not_set or
                            (self.backup_pathset_resolve_nh is not None and self.backup_pathset_resolve_nh.has_operation()) or
                            (self.pathset_resolve_nh is not None and self.pathset_resolve_nh.has_operation()) or
                            (self.prefix is not None and self.prefix.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "local-label" + "[local-label-id='" + self.local_label_id.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.local_label_id.is_set or self.local_label_id.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.local_label_id.get_name_leafdata())
                        if (self.address_family.is_set or self.address_family.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.address_family.get_name_leafdata())
                        if (self.backup_pathset_via_resolve.is_set or self.backup_pathset_via_resolve.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.backup_pathset_via_resolve.get_name_leafdata())
                        if (self.label.is_set or self.label.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.label.get_name_leafdata())
                        if (self.label_mode.is_set or self.label_mode.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.label_mode.get_name_leafdata())
                        if (self.label_status.is_set or self.label_status.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.label_status.get_name_leafdata())
                        if (self.pathset_via_resolve.is_set or self.pathset_via_resolve.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.pathset_via_resolve.get_name_leafdata())
                        if (self.vrf_name.is_set or self.vrf_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.vrf_name.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "backup-path-info"):
                            for c in self.backup_path_info:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = MplsStatic.Vrfs.Vrf.LocalLabels.LocalLabel.BackupPathInfo()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.backup_path_info.append(c)
                            return c

                        if (child_yang_name == "backup-pathset-resolve-nh"):
                            if (self.backup_pathset_resolve_nh is None):
                                self.backup_pathset_resolve_nh = MplsStatic.Vrfs.Vrf.LocalLabels.LocalLabel.BackupPathsetResolveNh()
                                self.backup_pathset_resolve_nh.parent = self
                                self._children_name_map["backup_pathset_resolve_nh"] = "backup-pathset-resolve-nh"
                            return self.backup_pathset_resolve_nh

                        if (child_yang_name == "path-info"):
                            for c in self.path_info:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = MplsStatic.Vrfs.Vrf.LocalLabels.LocalLabel.PathInfo()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.path_info.append(c)
                            return c

                        if (child_yang_name == "pathset-resolve-nh"):
                            if (self.pathset_resolve_nh is None):
                                self.pathset_resolve_nh = MplsStatic.Vrfs.Vrf.LocalLabels.LocalLabel.PathsetResolveNh()
                                self.pathset_resolve_nh.parent = self
                                self._children_name_map["pathset_resolve_nh"] = "pathset-resolve-nh"
                            return self.pathset_resolve_nh

                        if (child_yang_name == "prefix"):
                            if (self.prefix is None):
                                self.prefix = MplsStatic.Vrfs.Vrf.LocalLabels.LocalLabel.Prefix()
                                self.prefix.parent = self
                                self._children_name_map["prefix"] = "prefix"
                            return self.prefix

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "backup-path-info" or name == "backup-pathset-resolve-nh" or name == "path-info" or name == "pathset-resolve-nh" or name == "prefix" or name == "local-label-id" or name == "address-family" or name == "backup-pathset-via-resolve" or name == "label" or name == "label-mode" or name == "label-status" or name == "pathset-via-resolve" or name == "vrf-name"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "local-label-id"):
                            self.local_label_id = value
                            self.local_label_id.value_namespace = name_space
                            self.local_label_id.value_namespace_prefix = name_space_prefix
                        if(value_path == "address-family"):
                            self.address_family = value
                            self.address_family.value_namespace = name_space
                            self.address_family.value_namespace_prefix = name_space_prefix
                        if(value_path == "backup-pathset-via-resolve"):
                            self.backup_pathset_via_resolve = value
                            self.backup_pathset_via_resolve.value_namespace = name_space
                            self.backup_pathset_via_resolve.value_namespace_prefix = name_space_prefix
                        if(value_path == "label"):
                            self.label = value
                            self.label.value_namespace = name_space
                            self.label.value_namespace_prefix = name_space_prefix
                        if(value_path == "label-mode"):
                            self.label_mode = value
                            self.label_mode.value_namespace = name_space
                            self.label_mode.value_namespace_prefix = name_space_prefix
                        if(value_path == "label-status"):
                            self.label_status = value
                            self.label_status.value_namespace = name_space
                            self.label_status.value_namespace_prefix = name_space_prefix
                        if(value_path == "pathset-via-resolve"):
                            self.pathset_via_resolve = value
                            self.pathset_via_resolve.value_namespace = name_space
                            self.pathset_via_resolve.value_namespace_prefix = name_space_prefix
                        if(value_path == "vrf-name"):
                            self.vrf_name = value
                            self.vrf_name.value_namespace = name_space
                            self.vrf_name.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.local_label:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.local_label:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "local-labels" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "local-label"):
                        for c in self.local_label:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = MplsStatic.Vrfs.Vrf.LocalLabels.LocalLabel()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.local_label.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "local-label"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass

            def has_data(self):
                return (
                    self.vrf_name.is_set or
                    (self.local_labels is not None and self.local_labels.has_data()) or
                    (self.lsps is not None and self.lsps.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.vrf_name.yfilter != YFilter.not_set or
                    (self.local_labels is not None and self.local_labels.has_operation()) or
                    (self.lsps is not None and self.lsps.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "vrf" + "[vrf-name='" + self.vrf_name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-mpls-static-oper:mpls-static/vrfs/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.vrf_name.is_set or self.vrf_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vrf_name.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "local-labels"):
                    if (self.local_labels is None):
                        self.local_labels = MplsStatic.Vrfs.Vrf.LocalLabels()
                        self.local_labels.parent = self
                        self._children_name_map["local_labels"] = "local-labels"
                    return self.local_labels

                if (child_yang_name == "lsps"):
                    if (self.lsps is None):
                        self.lsps = MplsStatic.Vrfs.Vrf.Lsps()
                        self.lsps.parent = self
                        self._children_name_map["lsps"] = "lsps"
                    return self.lsps

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "local-labels" or name == "lsps" or name == "vrf-name"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "vrf-name"):
                    self.vrf_name = value
                    self.vrf_name.value_namespace = name_space
                    self.vrf_name.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.vrf:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.vrf:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "vrfs" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-mpls-static-oper:mpls-static/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "vrf"):
                for c in self.vrf:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = MplsStatic.Vrfs.Vrf()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.vrf.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "vrf"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Summary(Entity):
        """
        MPLS STATIC summary data
        
        .. attribute:: active_vrf_count
        
        	Total Number of Active VRF Active
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: im_connected
        
        	IM is connected
        	**type**\:  bool
        
        .. attribute:: interface_count
        
        	Total Number of Interface
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: interface_foward_reference_count
        
        	Total Number of Active Interface
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipv4_route_count
        
        	Total Number of IPv4 Routes
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipv6_route_count
        
        	Total Number of IPv6 Routes
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: label_count
        
        	Total Number of Labels
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: label_discrepancy_count
        
        	Total Number of Labels with Discrepancies
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: label_error_count
        
        	Total Number of Labels with Errors
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: lsd_connected
        
        	LSD connection is up
        	**type**\:  bool
        
        .. attribute:: mpls_enabled_interface_count
        
        	Total Number of MPLS enabled Interface
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: ribv4_connected
        
        	RIBv4 is connected
        	**type**\:  bool
        
        .. attribute:: ribv6_connected
        
        	RIBv6 is connected
        	**type**\:  bool
        
        .. attribute:: rsi_connected
        
        	RSI is connected
        	**type**\:  bool
        
        .. attribute:: vrf_count
        
        	Total Number of VRF configured
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'mpls-static-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(MplsStatic.Summary, self).__init__()

            self.yang_name = "summary"
            self.yang_parent_name = "mpls-static"

            self.active_vrf_count = YLeaf(YType.uint32, "active-vrf-count")

            self.im_connected = YLeaf(YType.boolean, "im-connected")

            self.interface_count = YLeaf(YType.uint32, "interface-count")

            self.interface_foward_reference_count = YLeaf(YType.uint32, "interface-foward-reference-count")

            self.ipv4_route_count = YLeaf(YType.uint32, "ipv4-route-count")

            self.ipv6_route_count = YLeaf(YType.uint32, "ipv6-route-count")

            self.label_count = YLeaf(YType.uint32, "label-count")

            self.label_discrepancy_count = YLeaf(YType.uint32, "label-discrepancy-count")

            self.label_error_count = YLeaf(YType.uint32, "label-error-count")

            self.lsd_connected = YLeaf(YType.boolean, "lsd-connected")

            self.mpls_enabled_interface_count = YLeaf(YType.uint32, "mpls-enabled-interface-count")

            self.ribv4_connected = YLeaf(YType.boolean, "ribv4-connected")

            self.ribv6_connected = YLeaf(YType.boolean, "ribv6-connected")

            self.rsi_connected = YLeaf(YType.boolean, "rsi-connected")

            self.vrf_count = YLeaf(YType.uint32, "vrf-count")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("active_vrf_count",
                            "im_connected",
                            "interface_count",
                            "interface_foward_reference_count",
                            "ipv4_route_count",
                            "ipv6_route_count",
                            "label_count",
                            "label_discrepancy_count",
                            "label_error_count",
                            "lsd_connected",
                            "mpls_enabled_interface_count",
                            "ribv4_connected",
                            "ribv6_connected",
                            "rsi_connected",
                            "vrf_count") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(MplsStatic.Summary, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(MplsStatic.Summary, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.active_vrf_count.is_set or
                self.im_connected.is_set or
                self.interface_count.is_set or
                self.interface_foward_reference_count.is_set or
                self.ipv4_route_count.is_set or
                self.ipv6_route_count.is_set or
                self.label_count.is_set or
                self.label_discrepancy_count.is_set or
                self.label_error_count.is_set or
                self.lsd_connected.is_set or
                self.mpls_enabled_interface_count.is_set or
                self.ribv4_connected.is_set or
                self.ribv6_connected.is_set or
                self.rsi_connected.is_set or
                self.vrf_count.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.active_vrf_count.yfilter != YFilter.not_set or
                self.im_connected.yfilter != YFilter.not_set or
                self.interface_count.yfilter != YFilter.not_set or
                self.interface_foward_reference_count.yfilter != YFilter.not_set or
                self.ipv4_route_count.yfilter != YFilter.not_set or
                self.ipv6_route_count.yfilter != YFilter.not_set or
                self.label_count.yfilter != YFilter.not_set or
                self.label_discrepancy_count.yfilter != YFilter.not_set or
                self.label_error_count.yfilter != YFilter.not_set or
                self.lsd_connected.yfilter != YFilter.not_set or
                self.mpls_enabled_interface_count.yfilter != YFilter.not_set or
                self.ribv4_connected.yfilter != YFilter.not_set or
                self.ribv6_connected.yfilter != YFilter.not_set or
                self.rsi_connected.yfilter != YFilter.not_set or
                self.vrf_count.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "summary" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-mpls-static-oper:mpls-static/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.active_vrf_count.is_set or self.active_vrf_count.yfilter != YFilter.not_set):
                leaf_name_data.append(self.active_vrf_count.get_name_leafdata())
            if (self.im_connected.is_set or self.im_connected.yfilter != YFilter.not_set):
                leaf_name_data.append(self.im_connected.get_name_leafdata())
            if (self.interface_count.is_set or self.interface_count.yfilter != YFilter.not_set):
                leaf_name_data.append(self.interface_count.get_name_leafdata())
            if (self.interface_foward_reference_count.is_set or self.interface_foward_reference_count.yfilter != YFilter.not_set):
                leaf_name_data.append(self.interface_foward_reference_count.get_name_leafdata())
            if (self.ipv4_route_count.is_set or self.ipv4_route_count.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ipv4_route_count.get_name_leafdata())
            if (self.ipv6_route_count.is_set or self.ipv6_route_count.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ipv6_route_count.get_name_leafdata())
            if (self.label_count.is_set or self.label_count.yfilter != YFilter.not_set):
                leaf_name_data.append(self.label_count.get_name_leafdata())
            if (self.label_discrepancy_count.is_set or self.label_discrepancy_count.yfilter != YFilter.not_set):
                leaf_name_data.append(self.label_discrepancy_count.get_name_leafdata())
            if (self.label_error_count.is_set or self.label_error_count.yfilter != YFilter.not_set):
                leaf_name_data.append(self.label_error_count.get_name_leafdata())
            if (self.lsd_connected.is_set or self.lsd_connected.yfilter != YFilter.not_set):
                leaf_name_data.append(self.lsd_connected.get_name_leafdata())
            if (self.mpls_enabled_interface_count.is_set or self.mpls_enabled_interface_count.yfilter != YFilter.not_set):
                leaf_name_data.append(self.mpls_enabled_interface_count.get_name_leafdata())
            if (self.ribv4_connected.is_set or self.ribv4_connected.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ribv4_connected.get_name_leafdata())
            if (self.ribv6_connected.is_set or self.ribv6_connected.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ribv6_connected.get_name_leafdata())
            if (self.rsi_connected.is_set or self.rsi_connected.yfilter != YFilter.not_set):
                leaf_name_data.append(self.rsi_connected.get_name_leafdata())
            if (self.vrf_count.is_set or self.vrf_count.yfilter != YFilter.not_set):
                leaf_name_data.append(self.vrf_count.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "active-vrf-count" or name == "im-connected" or name == "interface-count" or name == "interface-foward-reference-count" or name == "ipv4-route-count" or name == "ipv6-route-count" or name == "label-count" or name == "label-discrepancy-count" or name == "label-error-count" or name == "lsd-connected" or name == "mpls-enabled-interface-count" or name == "ribv4-connected" or name == "ribv6-connected" or name == "rsi-connected" or name == "vrf-count"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "active-vrf-count"):
                self.active_vrf_count = value
                self.active_vrf_count.value_namespace = name_space
                self.active_vrf_count.value_namespace_prefix = name_space_prefix
            if(value_path == "im-connected"):
                self.im_connected = value
                self.im_connected.value_namespace = name_space
                self.im_connected.value_namespace_prefix = name_space_prefix
            if(value_path == "interface-count"):
                self.interface_count = value
                self.interface_count.value_namespace = name_space
                self.interface_count.value_namespace_prefix = name_space_prefix
            if(value_path == "interface-foward-reference-count"):
                self.interface_foward_reference_count = value
                self.interface_foward_reference_count.value_namespace = name_space
                self.interface_foward_reference_count.value_namespace_prefix = name_space_prefix
            if(value_path == "ipv4-route-count"):
                self.ipv4_route_count = value
                self.ipv4_route_count.value_namespace = name_space
                self.ipv4_route_count.value_namespace_prefix = name_space_prefix
            if(value_path == "ipv6-route-count"):
                self.ipv6_route_count = value
                self.ipv6_route_count.value_namespace = name_space
                self.ipv6_route_count.value_namespace_prefix = name_space_prefix
            if(value_path == "label-count"):
                self.label_count = value
                self.label_count.value_namespace = name_space
                self.label_count.value_namespace_prefix = name_space_prefix
            if(value_path == "label-discrepancy-count"):
                self.label_discrepancy_count = value
                self.label_discrepancy_count.value_namespace = name_space
                self.label_discrepancy_count.value_namespace_prefix = name_space_prefix
            if(value_path == "label-error-count"):
                self.label_error_count = value
                self.label_error_count.value_namespace = name_space
                self.label_error_count.value_namespace_prefix = name_space_prefix
            if(value_path == "lsd-connected"):
                self.lsd_connected = value
                self.lsd_connected.value_namespace = name_space
                self.lsd_connected.value_namespace_prefix = name_space_prefix
            if(value_path == "mpls-enabled-interface-count"):
                self.mpls_enabled_interface_count = value
                self.mpls_enabled_interface_count.value_namespace = name_space
                self.mpls_enabled_interface_count.value_namespace_prefix = name_space_prefix
            if(value_path == "ribv4-connected"):
                self.ribv4_connected = value
                self.ribv4_connected.value_namespace = name_space
                self.ribv4_connected.value_namespace_prefix = name_space_prefix
            if(value_path == "ribv6-connected"):
                self.ribv6_connected = value
                self.ribv6_connected.value_namespace = name_space
                self.ribv6_connected.value_namespace_prefix = name_space_prefix
            if(value_path == "rsi-connected"):
                self.rsi_connected = value
                self.rsi_connected.value_namespace = name_space
                self.rsi_connected.value_namespace_prefix = name_space_prefix
            if(value_path == "vrf-count"):
                self.vrf_count = value
                self.vrf_count.value_namespace = name_space
                self.vrf_count.value_namespace_prefix = name_space_prefix


    class LocalLabels(Entity):
        """
        data for static local\-label table
        
        .. attribute:: local_label
        
        	Data for static label
        	**type**\: list of    :py:class:`LocalLabel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MplsStatic.LocalLabels.LocalLabel>`
        
        

        """

        _prefix = 'mpls-static-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(MplsStatic.LocalLabels, self).__init__()

            self.yang_name = "local-labels"
            self.yang_parent_name = "mpls-static"

            self.local_label = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(MplsStatic.LocalLabels, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(MplsStatic.LocalLabels, self).__setattr__(name, value)


        class LocalLabel(Entity):
            """
            Data for static label
            
            .. attribute:: local_label_id  <key>
            
            	Local Label
            	**type**\:  int
            
            	**range:** 16..1048575
            
            .. attribute:: address_family
            
            	Address Family
            	**type**\:   :py:class:`MgmtStaticAddr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MgmtStaticAddr>`
            
            .. attribute:: backup_path_info
            
            	Backup Path Information
            	**type**\: list of    :py:class:`BackupPathInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MplsStatic.LocalLabels.LocalLabel.BackupPathInfo>`
            
            .. attribute:: backup_pathset_resolve_nh
            
            	Backup pathset resolve\-nexthop IP Address
            	**type**\:   :py:class:`BackupPathsetResolveNh <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MplsStatic.LocalLabels.LocalLabel.BackupPathsetResolveNh>`
            
            .. attribute:: backup_pathset_via_resolve
            
            	Backup Pathset as a result of resolve
            	**type**\:  bool
            
            .. attribute:: label
            
            	Label value
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: label_mode
            
            	Label Mode
            	**type**\:   :py:class:`MgmtMplsStaticLabelMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MgmtMplsStaticLabelMode>`
            
            .. attribute:: label_status
            
            	Label Status
            	**type**\:   :py:class:`MgmtMplsStaticLabelStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MgmtMplsStaticLabelStatus>`
            
            .. attribute:: path_info
            
            	Path Information
            	**type**\: list of    :py:class:`PathInfo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MplsStatic.LocalLabels.LocalLabel.PathInfo>`
            
            .. attribute:: pathset_resolve_nh
            
            	Primary pathset resolve\-nexthop IP Address
            	**type**\:   :py:class:`PathsetResolveNh <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MplsStatic.LocalLabels.LocalLabel.PathsetResolveNh>`
            
            .. attribute:: pathset_via_resolve
            
            	Primary Pathset as a result of resolve
            	**type**\:  bool
            
            .. attribute:: prefix
            
            	Prefix Information
            	**type**\:   :py:class:`Prefix <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MplsStatic.LocalLabels.LocalLabel.Prefix>`
            
            .. attribute:: vrf_name
            
            	VRF name
            	**type**\:  str
            
            

            """

            _prefix = 'mpls-static-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(MplsStatic.LocalLabels.LocalLabel, self).__init__()

                self.yang_name = "local-label"
                self.yang_parent_name = "local-labels"

                self.local_label_id = YLeaf(YType.uint32, "local-label-id")

                self.address_family = YLeaf(YType.enumeration, "address-family")

                self.backup_pathset_via_resolve = YLeaf(YType.boolean, "backup-pathset-via-resolve")

                self.label = YLeaf(YType.uint32, "label")

                self.label_mode = YLeaf(YType.enumeration, "label-mode")

                self.label_status = YLeaf(YType.enumeration, "label-status")

                self.pathset_via_resolve = YLeaf(YType.boolean, "pathset-via-resolve")

                self.vrf_name = YLeaf(YType.str, "vrf-name")

                self.backup_pathset_resolve_nh = MplsStatic.LocalLabels.LocalLabel.BackupPathsetResolveNh()
                self.backup_pathset_resolve_nh.parent = self
                self._children_name_map["backup_pathset_resolve_nh"] = "backup-pathset-resolve-nh"
                self._children_yang_names.add("backup-pathset-resolve-nh")

                self.pathset_resolve_nh = MplsStatic.LocalLabels.LocalLabel.PathsetResolveNh()
                self.pathset_resolve_nh.parent = self
                self._children_name_map["pathset_resolve_nh"] = "pathset-resolve-nh"
                self._children_yang_names.add("pathset-resolve-nh")

                self.prefix = MplsStatic.LocalLabels.LocalLabel.Prefix()
                self.prefix.parent = self
                self._children_name_map["prefix"] = "prefix"
                self._children_yang_names.add("prefix")

                self.backup_path_info = YList(self)
                self.path_info = YList(self)

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("local_label_id",
                                "address_family",
                                "backup_pathset_via_resolve",
                                "label",
                                "label_mode",
                                "label_status",
                                "pathset_via_resolve",
                                "vrf_name") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(MplsStatic.LocalLabels.LocalLabel, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(MplsStatic.LocalLabels.LocalLabel, self).__setattr__(name, value)


            class Prefix(Entity):
                """
                Prefix Information
                
                .. attribute:: prefix
                
                	Prefix
                	**type**\:   :py:class:`Prefix <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MplsStatic.LocalLabels.LocalLabel.Prefix.Prefix>`
                
                .. attribute:: prefix_length
                
                	Prefix length
                	**type**\:  int
                
                	**range:** 0..255
                
                

                """

                _prefix = 'mpls-static-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(MplsStatic.LocalLabels.LocalLabel.Prefix, self).__init__()

                    self.yang_name = "prefix"
                    self.yang_parent_name = "local-label"

                    self.prefix_length = YLeaf(YType.uint8, "prefix-length")

                    self.prefix = MplsStatic.LocalLabels.LocalLabel.Prefix.Prefix()
                    self.prefix.parent = self
                    self._children_name_map["prefix"] = "prefix"
                    self._children_yang_names.add("prefix")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("prefix_length") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(MplsStatic.LocalLabels.LocalLabel.Prefix, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(MplsStatic.LocalLabels.LocalLabel.Prefix, self).__setattr__(name, value)


                class Prefix(Entity):
                    """
                    Prefix
                    
                    .. attribute:: af_name
                    
                    	AFName
                    	**type**\:   :py:class:`MgmtStaticAddr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MgmtStaticAddr>`
                    
                    .. attribute:: ipv4_prefix
                    
                    	IPv4 context
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: ipv6_prefix
                    
                    	IPv6 context
                    	**type**\:  str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    

                    """

                    _prefix = 'mpls-static-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(MplsStatic.LocalLabels.LocalLabel.Prefix.Prefix, self).__init__()

                        self.yang_name = "prefix"
                        self.yang_parent_name = "prefix"

                        self.af_name = YLeaf(YType.enumeration, "af-name")

                        self.ipv4_prefix = YLeaf(YType.str, "ipv4-prefix")

                        self.ipv6_prefix = YLeaf(YType.str, "ipv6-prefix")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("af_name",
                                        "ipv4_prefix",
                                        "ipv6_prefix") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(MplsStatic.LocalLabels.LocalLabel.Prefix.Prefix, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(MplsStatic.LocalLabels.LocalLabel.Prefix.Prefix, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.af_name.is_set or
                            self.ipv4_prefix.is_set or
                            self.ipv6_prefix.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.af_name.yfilter != YFilter.not_set or
                            self.ipv4_prefix.yfilter != YFilter.not_set or
                            self.ipv6_prefix.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "prefix" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.af_name.is_set or self.af_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.af_name.get_name_leafdata())
                        if (self.ipv4_prefix.is_set or self.ipv4_prefix.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.ipv4_prefix.get_name_leafdata())
                        if (self.ipv6_prefix.is_set or self.ipv6_prefix.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.ipv6_prefix.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "af-name" or name == "ipv4-prefix" or name == "ipv6-prefix"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "af-name"):
                            self.af_name = value
                            self.af_name.value_namespace = name_space
                            self.af_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "ipv4-prefix"):
                            self.ipv4_prefix = value
                            self.ipv4_prefix.value_namespace = name_space
                            self.ipv4_prefix.value_namespace_prefix = name_space_prefix
                        if(value_path == "ipv6-prefix"):
                            self.ipv6_prefix = value
                            self.ipv6_prefix.value_namespace = name_space
                            self.ipv6_prefix.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    return (
                        self.prefix_length.is_set or
                        (self.prefix is not None and self.prefix.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.prefix_length.yfilter != YFilter.not_set or
                        (self.prefix is not None and self.prefix.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "prefix" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.prefix_length.is_set or self.prefix_length.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.prefix_length.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "prefix"):
                        if (self.prefix is None):
                            self.prefix = MplsStatic.LocalLabels.LocalLabel.Prefix.Prefix()
                            self.prefix.parent = self
                            self._children_name_map["prefix"] = "prefix"
                        return self.prefix

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "prefix" or name == "prefix-length"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "prefix-length"):
                        self.prefix_length = value
                        self.prefix_length.value_namespace = name_space
                        self.prefix_length.value_namespace_prefix = name_space_prefix


            class PathsetResolveNh(Entity):
                """
                Primary pathset resolve\-nexthop IP Address
                
                .. attribute:: af_name
                
                	AFName
                	**type**\:   :py:class:`MgmtStaticAddr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MgmtStaticAddr>`
                
                .. attribute:: ipv4_prefix
                
                	IPv4 context
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: ipv6_prefix
                
                	IPv6 context
                	**type**\:  str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                

                """

                _prefix = 'mpls-static-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(MplsStatic.LocalLabels.LocalLabel.PathsetResolveNh, self).__init__()

                    self.yang_name = "pathset-resolve-nh"
                    self.yang_parent_name = "local-label"

                    self.af_name = YLeaf(YType.enumeration, "af-name")

                    self.ipv4_prefix = YLeaf(YType.str, "ipv4-prefix")

                    self.ipv6_prefix = YLeaf(YType.str, "ipv6-prefix")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("af_name",
                                    "ipv4_prefix",
                                    "ipv6_prefix") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(MplsStatic.LocalLabels.LocalLabel.PathsetResolveNh, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(MplsStatic.LocalLabels.LocalLabel.PathsetResolveNh, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.af_name.is_set or
                        self.ipv4_prefix.is_set or
                        self.ipv6_prefix.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.af_name.yfilter != YFilter.not_set or
                        self.ipv4_prefix.yfilter != YFilter.not_set or
                        self.ipv6_prefix.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "pathset-resolve-nh" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.af_name.is_set or self.af_name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.af_name.get_name_leafdata())
                    if (self.ipv4_prefix.is_set or self.ipv4_prefix.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.ipv4_prefix.get_name_leafdata())
                    if (self.ipv6_prefix.is_set or self.ipv6_prefix.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.ipv6_prefix.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "af-name" or name == "ipv4-prefix" or name == "ipv6-prefix"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "af-name"):
                        self.af_name = value
                        self.af_name.value_namespace = name_space
                        self.af_name.value_namespace_prefix = name_space_prefix
                    if(value_path == "ipv4-prefix"):
                        self.ipv4_prefix = value
                        self.ipv4_prefix.value_namespace = name_space
                        self.ipv4_prefix.value_namespace_prefix = name_space_prefix
                    if(value_path == "ipv6-prefix"):
                        self.ipv6_prefix = value
                        self.ipv6_prefix.value_namespace = name_space
                        self.ipv6_prefix.value_namespace_prefix = name_space_prefix


            class BackupPathsetResolveNh(Entity):
                """
                Backup pathset resolve\-nexthop IP Address
                
                .. attribute:: af_name
                
                	AFName
                	**type**\:   :py:class:`MgmtStaticAddr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MgmtStaticAddr>`
                
                .. attribute:: ipv4_prefix
                
                	IPv4 context
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: ipv6_prefix
                
                	IPv6 context
                	**type**\:  str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                

                """

                _prefix = 'mpls-static-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(MplsStatic.LocalLabels.LocalLabel.BackupPathsetResolveNh, self).__init__()

                    self.yang_name = "backup-pathset-resolve-nh"
                    self.yang_parent_name = "local-label"

                    self.af_name = YLeaf(YType.enumeration, "af-name")

                    self.ipv4_prefix = YLeaf(YType.str, "ipv4-prefix")

                    self.ipv6_prefix = YLeaf(YType.str, "ipv6-prefix")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("af_name",
                                    "ipv4_prefix",
                                    "ipv6_prefix") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(MplsStatic.LocalLabels.LocalLabel.BackupPathsetResolveNh, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(MplsStatic.LocalLabels.LocalLabel.BackupPathsetResolveNh, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.af_name.is_set or
                        self.ipv4_prefix.is_set or
                        self.ipv6_prefix.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.af_name.yfilter != YFilter.not_set or
                        self.ipv4_prefix.yfilter != YFilter.not_set or
                        self.ipv6_prefix.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "backup-pathset-resolve-nh" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.af_name.is_set or self.af_name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.af_name.get_name_leafdata())
                    if (self.ipv4_prefix.is_set or self.ipv4_prefix.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.ipv4_prefix.get_name_leafdata())
                    if (self.ipv6_prefix.is_set or self.ipv6_prefix.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.ipv6_prefix.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "af-name" or name == "ipv4-prefix" or name == "ipv6-prefix"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "af-name"):
                        self.af_name = value
                        self.af_name.value_namespace = name_space
                        self.af_name.value_namespace_prefix = name_space_prefix
                    if(value_path == "ipv4-prefix"):
                        self.ipv4_prefix = value
                        self.ipv4_prefix.value_namespace = name_space
                        self.ipv4_prefix.value_namespace_prefix = name_space_prefix
                    if(value_path == "ipv6-prefix"):
                        self.ipv6_prefix = value
                        self.ipv6_prefix.value_namespace = name_space
                        self.ipv6_prefix.value_namespace_prefix = name_space_prefix


            class PathInfo(Entity):
                """
                Path Information
                
                .. attribute:: backup_id
                
                	Path Backup Id
                	**type**\:  int
                
                	**range:** 0..255
                
                .. attribute:: nexthop
                
                	Nexthop information
                	**type**\:   :py:class:`Nexthop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MplsStatic.LocalLabels.LocalLabel.PathInfo.Nexthop>`
                
                .. attribute:: path_id
                
                	Path Id
                	**type**\:  int
                
                	**range:** 0..255
                
                .. attribute:: path_number
                
                	Path Number
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: path_role
                
                	Path Role
                	**type**\:   :py:class:`MplsStaticPathRole <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MplsStaticPathRole>`
                
                .. attribute:: status
                
                	Path Status
                	**type**\:   :py:class:`MgmtMplsStaticPathStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MgmtMplsStaticPathStatus>`
                
                .. attribute:: type
                
                	Path Type
                	**type**\:   :py:class:`MgmtStaticPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MgmtStaticPath>`
                
                

                """

                _prefix = 'mpls-static-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(MplsStatic.LocalLabels.LocalLabel.PathInfo, self).__init__()

                    self.yang_name = "path-info"
                    self.yang_parent_name = "local-label"

                    self.backup_id = YLeaf(YType.uint8, "backup-id")

                    self.path_id = YLeaf(YType.uint8, "path-id")

                    self.path_number = YLeaf(YType.uint32, "path-number")

                    self.path_role = YLeaf(YType.enumeration, "path-role")

                    self.status = YLeaf(YType.enumeration, "status")

                    self.type = YLeaf(YType.enumeration, "type")

                    self.nexthop = MplsStatic.LocalLabels.LocalLabel.PathInfo.Nexthop()
                    self.nexthop.parent = self
                    self._children_name_map["nexthop"] = "nexthop"
                    self._children_yang_names.add("nexthop")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("backup_id",
                                    "path_id",
                                    "path_number",
                                    "path_role",
                                    "status",
                                    "type") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(MplsStatic.LocalLabels.LocalLabel.PathInfo, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(MplsStatic.LocalLabels.LocalLabel.PathInfo, self).__setattr__(name, value)


                class Nexthop(Entity):
                    """
                    Nexthop information
                    
                    .. attribute:: address
                    
                    	Next\-Hop IP Address
                    	**type**\:   :py:class:`Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MplsStatic.LocalLabels.LocalLabel.PathInfo.Nexthop.Address>`
                    
                    .. attribute:: afi
                    
                    	Next\-Hop AFI
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: interface_name
                    
                    	Next\-Hop Interface Name
                    	**type**\:  str
                    
                    .. attribute:: label
                    
                    	Next\-Hop Label
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'mpls-static-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(MplsStatic.LocalLabels.LocalLabel.PathInfo.Nexthop, self).__init__()

                        self.yang_name = "nexthop"
                        self.yang_parent_name = "path-info"

                        self.afi = YLeaf(YType.uint32, "afi")

                        self.interface_name = YLeaf(YType.str, "interface-name")

                        self.label = YLeaf(YType.uint32, "label")

                        self.address = MplsStatic.LocalLabels.LocalLabel.PathInfo.Nexthop.Address()
                        self.address.parent = self
                        self._children_name_map["address"] = "address"
                        self._children_yang_names.add("address")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("afi",
                                        "interface_name",
                                        "label") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(MplsStatic.LocalLabels.LocalLabel.PathInfo.Nexthop, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(MplsStatic.LocalLabels.LocalLabel.PathInfo.Nexthop, self).__setattr__(name, value)


                    class Address(Entity):
                        """
                        Next\-Hop IP Address
                        
                        .. attribute:: af_name
                        
                        	AFName
                        	**type**\:   :py:class:`MgmtStaticAddr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MgmtStaticAddr>`
                        
                        .. attribute:: ipv4_prefix
                        
                        	IPv4 context
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: ipv6_prefix
                        
                        	IPv6 context
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        

                        """

                        _prefix = 'mpls-static-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(MplsStatic.LocalLabels.LocalLabel.PathInfo.Nexthop.Address, self).__init__()

                            self.yang_name = "address"
                            self.yang_parent_name = "nexthop"

                            self.af_name = YLeaf(YType.enumeration, "af-name")

                            self.ipv4_prefix = YLeaf(YType.str, "ipv4-prefix")

                            self.ipv6_prefix = YLeaf(YType.str, "ipv6-prefix")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("af_name",
                                            "ipv4_prefix",
                                            "ipv6_prefix") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(MplsStatic.LocalLabels.LocalLabel.PathInfo.Nexthop.Address, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(MplsStatic.LocalLabels.LocalLabel.PathInfo.Nexthop.Address, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.af_name.is_set or
                                self.ipv4_prefix.is_set or
                                self.ipv6_prefix.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.af_name.yfilter != YFilter.not_set or
                                self.ipv4_prefix.yfilter != YFilter.not_set or
                                self.ipv6_prefix.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "address" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.af_name.is_set or self.af_name.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.af_name.get_name_leafdata())
                            if (self.ipv4_prefix.is_set or self.ipv4_prefix.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.ipv4_prefix.get_name_leafdata())
                            if (self.ipv6_prefix.is_set or self.ipv6_prefix.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.ipv6_prefix.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "af-name" or name == "ipv4-prefix" or name == "ipv6-prefix"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "af-name"):
                                self.af_name = value
                                self.af_name.value_namespace = name_space
                                self.af_name.value_namespace_prefix = name_space_prefix
                            if(value_path == "ipv4-prefix"):
                                self.ipv4_prefix = value
                                self.ipv4_prefix.value_namespace = name_space
                                self.ipv4_prefix.value_namespace_prefix = name_space_prefix
                            if(value_path == "ipv6-prefix"):
                                self.ipv6_prefix = value
                                self.ipv6_prefix.value_namespace = name_space
                                self.ipv6_prefix.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        return (
                            self.afi.is_set or
                            self.interface_name.is_set or
                            self.label.is_set or
                            (self.address is not None and self.address.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.afi.yfilter != YFilter.not_set or
                            self.interface_name.yfilter != YFilter.not_set or
                            self.label.yfilter != YFilter.not_set or
                            (self.address is not None and self.address.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "nexthop" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.afi.is_set or self.afi.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.afi.get_name_leafdata())
                        if (self.interface_name.is_set or self.interface_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.interface_name.get_name_leafdata())
                        if (self.label.is_set or self.label.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.label.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "address"):
                            if (self.address is None):
                                self.address = MplsStatic.LocalLabels.LocalLabel.PathInfo.Nexthop.Address()
                                self.address.parent = self
                                self._children_name_map["address"] = "address"
                            return self.address

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "address" or name == "afi" or name == "interface-name" or name == "label"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "afi"):
                            self.afi = value
                            self.afi.value_namespace = name_space
                            self.afi.value_namespace_prefix = name_space_prefix
                        if(value_path == "interface-name"):
                            self.interface_name = value
                            self.interface_name.value_namespace = name_space
                            self.interface_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "label"):
                            self.label = value
                            self.label.value_namespace = name_space
                            self.label.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    return (
                        self.backup_id.is_set or
                        self.path_id.is_set or
                        self.path_number.is_set or
                        self.path_role.is_set or
                        self.status.is_set or
                        self.type.is_set or
                        (self.nexthop is not None and self.nexthop.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.backup_id.yfilter != YFilter.not_set or
                        self.path_id.yfilter != YFilter.not_set or
                        self.path_number.yfilter != YFilter.not_set or
                        self.path_role.yfilter != YFilter.not_set or
                        self.status.yfilter != YFilter.not_set or
                        self.type.yfilter != YFilter.not_set or
                        (self.nexthop is not None and self.nexthop.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "path-info" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.backup_id.is_set or self.backup_id.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.backup_id.get_name_leafdata())
                    if (self.path_id.is_set or self.path_id.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.path_id.get_name_leafdata())
                    if (self.path_number.is_set or self.path_number.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.path_number.get_name_leafdata())
                    if (self.path_role.is_set or self.path_role.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.path_role.get_name_leafdata())
                    if (self.status.is_set or self.status.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.status.get_name_leafdata())
                    if (self.type.is_set or self.type.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.type.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "nexthop"):
                        if (self.nexthop is None):
                            self.nexthop = MplsStatic.LocalLabels.LocalLabel.PathInfo.Nexthop()
                            self.nexthop.parent = self
                            self._children_name_map["nexthop"] = "nexthop"
                        return self.nexthop

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "nexthop" or name == "backup-id" or name == "path-id" or name == "path-number" or name == "path-role" or name == "status" or name == "type"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "backup-id"):
                        self.backup_id = value
                        self.backup_id.value_namespace = name_space
                        self.backup_id.value_namespace_prefix = name_space_prefix
                    if(value_path == "path-id"):
                        self.path_id = value
                        self.path_id.value_namespace = name_space
                        self.path_id.value_namespace_prefix = name_space_prefix
                    if(value_path == "path-number"):
                        self.path_number = value
                        self.path_number.value_namespace = name_space
                        self.path_number.value_namespace_prefix = name_space_prefix
                    if(value_path == "path-role"):
                        self.path_role = value
                        self.path_role.value_namespace = name_space
                        self.path_role.value_namespace_prefix = name_space_prefix
                    if(value_path == "status"):
                        self.status = value
                        self.status.value_namespace = name_space
                        self.status.value_namespace_prefix = name_space_prefix
                    if(value_path == "type"):
                        self.type = value
                        self.type.value_namespace = name_space
                        self.type.value_namespace_prefix = name_space_prefix


            class BackupPathInfo(Entity):
                """
                Backup Path Information
                
                .. attribute:: backup_id
                
                	Path Backup Id
                	**type**\:  int
                
                	**range:** 0..255
                
                .. attribute:: nexthop
                
                	Nexthop information
                	**type**\:   :py:class:`Nexthop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MplsStatic.LocalLabels.LocalLabel.BackupPathInfo.Nexthop>`
                
                .. attribute:: path_id
                
                	Path Id
                	**type**\:  int
                
                	**range:** 0..255
                
                .. attribute:: path_number
                
                	Path Number
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: path_role
                
                	Path Role
                	**type**\:   :py:class:`MplsStaticPathRole <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MplsStaticPathRole>`
                
                .. attribute:: status
                
                	Path Status
                	**type**\:   :py:class:`MgmtMplsStaticPathStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MgmtMplsStaticPathStatus>`
                
                .. attribute:: type
                
                	Path Type
                	**type**\:   :py:class:`MgmtStaticPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MgmtStaticPath>`
                
                

                """

                _prefix = 'mpls-static-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(MplsStatic.LocalLabels.LocalLabel.BackupPathInfo, self).__init__()

                    self.yang_name = "backup-path-info"
                    self.yang_parent_name = "local-label"

                    self.backup_id = YLeaf(YType.uint8, "backup-id")

                    self.path_id = YLeaf(YType.uint8, "path-id")

                    self.path_number = YLeaf(YType.uint32, "path-number")

                    self.path_role = YLeaf(YType.enumeration, "path-role")

                    self.status = YLeaf(YType.enumeration, "status")

                    self.type = YLeaf(YType.enumeration, "type")

                    self.nexthop = MplsStatic.LocalLabels.LocalLabel.BackupPathInfo.Nexthop()
                    self.nexthop.parent = self
                    self._children_name_map["nexthop"] = "nexthop"
                    self._children_yang_names.add("nexthop")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("backup_id",
                                    "path_id",
                                    "path_number",
                                    "path_role",
                                    "status",
                                    "type") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(MplsStatic.LocalLabels.LocalLabel.BackupPathInfo, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(MplsStatic.LocalLabels.LocalLabel.BackupPathInfo, self).__setattr__(name, value)


                class Nexthop(Entity):
                    """
                    Nexthop information
                    
                    .. attribute:: address
                    
                    	Next\-Hop IP Address
                    	**type**\:   :py:class:`Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MplsStatic.LocalLabels.LocalLabel.BackupPathInfo.Nexthop.Address>`
                    
                    .. attribute:: afi
                    
                    	Next\-Hop AFI
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: interface_name
                    
                    	Next\-Hop Interface Name
                    	**type**\:  str
                    
                    .. attribute:: label
                    
                    	Next\-Hop Label
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'mpls-static-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(MplsStatic.LocalLabels.LocalLabel.BackupPathInfo.Nexthop, self).__init__()

                        self.yang_name = "nexthop"
                        self.yang_parent_name = "backup-path-info"

                        self.afi = YLeaf(YType.uint32, "afi")

                        self.interface_name = YLeaf(YType.str, "interface-name")

                        self.label = YLeaf(YType.uint32, "label")

                        self.address = MplsStatic.LocalLabels.LocalLabel.BackupPathInfo.Nexthop.Address()
                        self.address.parent = self
                        self._children_name_map["address"] = "address"
                        self._children_yang_names.add("address")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("afi",
                                        "interface_name",
                                        "label") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(MplsStatic.LocalLabels.LocalLabel.BackupPathInfo.Nexthop, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(MplsStatic.LocalLabels.LocalLabel.BackupPathInfo.Nexthop, self).__setattr__(name, value)


                    class Address(Entity):
                        """
                        Next\-Hop IP Address
                        
                        .. attribute:: af_name
                        
                        	AFName
                        	**type**\:   :py:class:`MgmtStaticAddr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MgmtStaticAddr>`
                        
                        .. attribute:: ipv4_prefix
                        
                        	IPv4 context
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: ipv6_prefix
                        
                        	IPv6 context
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        

                        """

                        _prefix = 'mpls-static-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(MplsStatic.LocalLabels.LocalLabel.BackupPathInfo.Nexthop.Address, self).__init__()

                            self.yang_name = "address"
                            self.yang_parent_name = "nexthop"

                            self.af_name = YLeaf(YType.enumeration, "af-name")

                            self.ipv4_prefix = YLeaf(YType.str, "ipv4-prefix")

                            self.ipv6_prefix = YLeaf(YType.str, "ipv6-prefix")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("af_name",
                                            "ipv4_prefix",
                                            "ipv6_prefix") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(MplsStatic.LocalLabels.LocalLabel.BackupPathInfo.Nexthop.Address, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(MplsStatic.LocalLabels.LocalLabel.BackupPathInfo.Nexthop.Address, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.af_name.is_set or
                                self.ipv4_prefix.is_set or
                                self.ipv6_prefix.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.af_name.yfilter != YFilter.not_set or
                                self.ipv4_prefix.yfilter != YFilter.not_set or
                                self.ipv6_prefix.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "address" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.af_name.is_set or self.af_name.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.af_name.get_name_leafdata())
                            if (self.ipv4_prefix.is_set or self.ipv4_prefix.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.ipv4_prefix.get_name_leafdata())
                            if (self.ipv6_prefix.is_set or self.ipv6_prefix.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.ipv6_prefix.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "af-name" or name == "ipv4-prefix" or name == "ipv6-prefix"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "af-name"):
                                self.af_name = value
                                self.af_name.value_namespace = name_space
                                self.af_name.value_namespace_prefix = name_space_prefix
                            if(value_path == "ipv4-prefix"):
                                self.ipv4_prefix = value
                                self.ipv4_prefix.value_namespace = name_space
                                self.ipv4_prefix.value_namespace_prefix = name_space_prefix
                            if(value_path == "ipv6-prefix"):
                                self.ipv6_prefix = value
                                self.ipv6_prefix.value_namespace = name_space
                                self.ipv6_prefix.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        return (
                            self.afi.is_set or
                            self.interface_name.is_set or
                            self.label.is_set or
                            (self.address is not None and self.address.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.afi.yfilter != YFilter.not_set or
                            self.interface_name.yfilter != YFilter.not_set or
                            self.label.yfilter != YFilter.not_set or
                            (self.address is not None and self.address.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "nexthop" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.afi.is_set or self.afi.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.afi.get_name_leafdata())
                        if (self.interface_name.is_set or self.interface_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.interface_name.get_name_leafdata())
                        if (self.label.is_set or self.label.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.label.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "address"):
                            if (self.address is None):
                                self.address = MplsStatic.LocalLabels.LocalLabel.BackupPathInfo.Nexthop.Address()
                                self.address.parent = self
                                self._children_name_map["address"] = "address"
                            return self.address

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "address" or name == "afi" or name == "interface-name" or name == "label"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "afi"):
                            self.afi = value
                            self.afi.value_namespace = name_space
                            self.afi.value_namespace_prefix = name_space_prefix
                        if(value_path == "interface-name"):
                            self.interface_name = value
                            self.interface_name.value_namespace = name_space
                            self.interface_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "label"):
                            self.label = value
                            self.label.value_namespace = name_space
                            self.label.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    return (
                        self.backup_id.is_set or
                        self.path_id.is_set or
                        self.path_number.is_set or
                        self.path_role.is_set or
                        self.status.is_set or
                        self.type.is_set or
                        (self.nexthop is not None and self.nexthop.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.backup_id.yfilter != YFilter.not_set or
                        self.path_id.yfilter != YFilter.not_set or
                        self.path_number.yfilter != YFilter.not_set or
                        self.path_role.yfilter != YFilter.not_set or
                        self.status.yfilter != YFilter.not_set or
                        self.type.yfilter != YFilter.not_set or
                        (self.nexthop is not None and self.nexthop.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "backup-path-info" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.backup_id.is_set or self.backup_id.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.backup_id.get_name_leafdata())
                    if (self.path_id.is_set or self.path_id.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.path_id.get_name_leafdata())
                    if (self.path_number.is_set or self.path_number.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.path_number.get_name_leafdata())
                    if (self.path_role.is_set or self.path_role.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.path_role.get_name_leafdata())
                    if (self.status.is_set or self.status.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.status.get_name_leafdata())
                    if (self.type.is_set or self.type.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.type.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "nexthop"):
                        if (self.nexthop is None):
                            self.nexthop = MplsStatic.LocalLabels.LocalLabel.BackupPathInfo.Nexthop()
                            self.nexthop.parent = self
                            self._children_name_map["nexthop"] = "nexthop"
                        return self.nexthop

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "nexthop" or name == "backup-id" or name == "path-id" or name == "path-number" or name == "path-role" or name == "status" or name == "type"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "backup-id"):
                        self.backup_id = value
                        self.backup_id.value_namespace = name_space
                        self.backup_id.value_namespace_prefix = name_space_prefix
                    if(value_path == "path-id"):
                        self.path_id = value
                        self.path_id.value_namespace = name_space
                        self.path_id.value_namespace_prefix = name_space_prefix
                    if(value_path == "path-number"):
                        self.path_number = value
                        self.path_number.value_namespace = name_space
                        self.path_number.value_namespace_prefix = name_space_prefix
                    if(value_path == "path-role"):
                        self.path_role = value
                        self.path_role.value_namespace = name_space
                        self.path_role.value_namespace_prefix = name_space_prefix
                    if(value_path == "status"):
                        self.status = value
                        self.status.value_namespace = name_space
                        self.status.value_namespace_prefix = name_space_prefix
                    if(value_path == "type"):
                        self.type = value
                        self.type.value_namespace = name_space
                        self.type.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.backup_path_info:
                    if (c.has_data()):
                        return True
                for c in self.path_info:
                    if (c.has_data()):
                        return True
                return (
                    self.local_label_id.is_set or
                    self.address_family.is_set or
                    self.backup_pathset_via_resolve.is_set or
                    self.label.is_set or
                    self.label_mode.is_set or
                    self.label_status.is_set or
                    self.pathset_via_resolve.is_set or
                    self.vrf_name.is_set or
                    (self.backup_pathset_resolve_nh is not None and self.backup_pathset_resolve_nh.has_data()) or
                    (self.pathset_resolve_nh is not None and self.pathset_resolve_nh.has_data()) or
                    (self.prefix is not None and self.prefix.has_data()))

            def has_operation(self):
                for c in self.backup_path_info:
                    if (c.has_operation()):
                        return True
                for c in self.path_info:
                    if (c.has_operation()):
                        return True
                return (
                    self.yfilter != YFilter.not_set or
                    self.local_label_id.yfilter != YFilter.not_set or
                    self.address_family.yfilter != YFilter.not_set or
                    self.backup_pathset_via_resolve.yfilter != YFilter.not_set or
                    self.label.yfilter != YFilter.not_set or
                    self.label_mode.yfilter != YFilter.not_set or
                    self.label_status.yfilter != YFilter.not_set or
                    self.pathset_via_resolve.yfilter != YFilter.not_set or
                    self.vrf_name.yfilter != YFilter.not_set or
                    (self.backup_pathset_resolve_nh is not None and self.backup_pathset_resolve_nh.has_operation()) or
                    (self.pathset_resolve_nh is not None and self.pathset_resolve_nh.has_operation()) or
                    (self.prefix is not None and self.prefix.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "local-label" + "[local-label-id='" + self.local_label_id.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-mpls-static-oper:mpls-static/local-labels/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.local_label_id.is_set or self.local_label_id.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.local_label_id.get_name_leafdata())
                if (self.address_family.is_set or self.address_family.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.address_family.get_name_leafdata())
                if (self.backup_pathset_via_resolve.is_set or self.backup_pathset_via_resolve.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.backup_pathset_via_resolve.get_name_leafdata())
                if (self.label.is_set or self.label.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.label.get_name_leafdata())
                if (self.label_mode.is_set or self.label_mode.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.label_mode.get_name_leafdata())
                if (self.label_status.is_set or self.label_status.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.label_status.get_name_leafdata())
                if (self.pathset_via_resolve.is_set or self.pathset_via_resolve.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.pathset_via_resolve.get_name_leafdata())
                if (self.vrf_name.is_set or self.vrf_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vrf_name.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "backup-path-info"):
                    for c in self.backup_path_info:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = MplsStatic.LocalLabels.LocalLabel.BackupPathInfo()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.backup_path_info.append(c)
                    return c

                if (child_yang_name == "backup-pathset-resolve-nh"):
                    if (self.backup_pathset_resolve_nh is None):
                        self.backup_pathset_resolve_nh = MplsStatic.LocalLabels.LocalLabel.BackupPathsetResolveNh()
                        self.backup_pathset_resolve_nh.parent = self
                        self._children_name_map["backup_pathset_resolve_nh"] = "backup-pathset-resolve-nh"
                    return self.backup_pathset_resolve_nh

                if (child_yang_name == "path-info"):
                    for c in self.path_info:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = MplsStatic.LocalLabels.LocalLabel.PathInfo()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.path_info.append(c)
                    return c

                if (child_yang_name == "pathset-resolve-nh"):
                    if (self.pathset_resolve_nh is None):
                        self.pathset_resolve_nh = MplsStatic.LocalLabels.LocalLabel.PathsetResolveNh()
                        self.pathset_resolve_nh.parent = self
                        self._children_name_map["pathset_resolve_nh"] = "pathset-resolve-nh"
                    return self.pathset_resolve_nh

                if (child_yang_name == "prefix"):
                    if (self.prefix is None):
                        self.prefix = MplsStatic.LocalLabels.LocalLabel.Prefix()
                        self.prefix.parent = self
                        self._children_name_map["prefix"] = "prefix"
                    return self.prefix

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "backup-path-info" or name == "backup-pathset-resolve-nh" or name == "path-info" or name == "pathset-resolve-nh" or name == "prefix" or name == "local-label-id" or name == "address-family" or name == "backup-pathset-via-resolve" or name == "label" or name == "label-mode" or name == "label-status" or name == "pathset-via-resolve" or name == "vrf-name"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "local-label-id"):
                    self.local_label_id = value
                    self.local_label_id.value_namespace = name_space
                    self.local_label_id.value_namespace_prefix = name_space_prefix
                if(value_path == "address-family"):
                    self.address_family = value
                    self.address_family.value_namespace = name_space
                    self.address_family.value_namespace_prefix = name_space_prefix
                if(value_path == "backup-pathset-via-resolve"):
                    self.backup_pathset_via_resolve = value
                    self.backup_pathset_via_resolve.value_namespace = name_space
                    self.backup_pathset_via_resolve.value_namespace_prefix = name_space_prefix
                if(value_path == "label"):
                    self.label = value
                    self.label.value_namespace = name_space
                    self.label.value_namespace_prefix = name_space_prefix
                if(value_path == "label-mode"):
                    self.label_mode = value
                    self.label_mode.value_namespace = name_space
                    self.label_mode.value_namespace_prefix = name_space_prefix
                if(value_path == "label-status"):
                    self.label_status = value
                    self.label_status.value_namespace = name_space
                    self.label_status.value_namespace_prefix = name_space_prefix
                if(value_path == "pathset-via-resolve"):
                    self.pathset_via_resolve = value
                    self.pathset_via_resolve.value_namespace = name_space
                    self.pathset_via_resolve.value_namespace_prefix = name_space_prefix
                if(value_path == "vrf-name"):
                    self.vrf_name = value
                    self.vrf_name.value_namespace = name_space
                    self.vrf_name.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.local_label:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.local_label:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "local-labels" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-mpls-static-oper:mpls-static/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "local-label"):
                for c in self.local_label:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = MplsStatic.LocalLabels.LocalLabel()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.local_label.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "local-label"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            (self.local_labels is not None and self.local_labels.has_data()) or
            (self.summary is not None and self.summary.has_data()) or
            (self.vrfs is not None and self.vrfs.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.local_labels is not None and self.local_labels.has_operation()) or
            (self.summary is not None and self.summary.has_operation()) or
            (self.vrfs is not None and self.vrfs.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-mpls-static-oper:mpls-static" + path_buffer

        return path_buffer

    def get_entity_path(self, ancestor):
        path_buffer = ""
        if (not ancestor is None):
            raise YPYModelError("ancestor has to be None for top-level node")

        path_buffer = self.get_segment_path()
        leaf_name_data = LeafDataList()

        entity_path = EntityPath(path_buffer, leaf_name_data)
        return entity_path

    def get_child_by_name(self, child_yang_name, segment_path):
        child = self._get_child_by_seg_name([child_yang_name, segment_path])
        if child is not None:
            return child

        if (child_yang_name == "local-labels"):
            if (self.local_labels is None):
                self.local_labels = MplsStatic.LocalLabels()
                self.local_labels.parent = self
                self._children_name_map["local_labels"] = "local-labels"
            return self.local_labels

        if (child_yang_name == "summary"):
            if (self.summary is None):
                self.summary = MplsStatic.Summary()
                self.summary.parent = self
                self._children_name_map["summary"] = "summary"
            return self.summary

        if (child_yang_name == "vrfs"):
            if (self.vrfs is None):
                self.vrfs = MplsStatic.Vrfs()
                self.vrfs.parent = self
                self._children_name_map["vrfs"] = "vrfs"
            return self.vrfs

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "local-labels" or name == "summary" or name == "vrfs"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = MplsStatic()
        return self._top_entity

