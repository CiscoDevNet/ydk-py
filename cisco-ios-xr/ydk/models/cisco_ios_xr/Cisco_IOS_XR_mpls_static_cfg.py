""" Cisco_IOS_XR_mpls_static_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR mpls\-static package configuration.

This module contains definitions
for the following management objects\:
  mpls\-static\: MPLS Static Configuration Data

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
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
    _revision = '2015-11-09'

    def __init__(self):
        super(MplsStatic, self).__init__()
        self._top_entity = None

        self.yang_name = "mpls-static"
        self.yang_parent_name = "Cisco-IOS-XR-mpls-static-cfg"

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

    def __setattr__(self, name, value):
        self._check_monkey_patching_error(name, value)
        with _handle_type_error():
            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                    "Please use list append or extend method."
                                    .format(value))
            if isinstance(value, Enum.YLeaf):
                value = value.name
            if name in ("enable") and name in self.__dict__:
                if isinstance(value, YLeaf):
                    self.__dict__[name].set(value.get())
                elif isinstance(value, YLeafList):
                    super(MplsStatic, self).__setattr__(name, value)
                else:
                    self.__dict__[name].set(value)
            else:
                if hasattr(value, "parent") and name != "parent":
                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                        value.parent = self
                    elif value.parent is None and value.yang_name in self._children_yang_names:
                        value.parent = self
                super(MplsStatic, self).__setattr__(name, value)


    class Vrfs(Entity):
        """
        VRF table
        
        .. attribute:: vrf
        
        	VRF Name
        	**type**\: list of    :py:class:`Vrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStatic.Vrfs.Vrf>`
        
        

        """

        _prefix = 'mpls-static-cfg'
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
            _revision = '2015-11-09'

            def __init__(self):
                super(MplsStatic.Vrfs.Vrf, self).__init__()

                self.yang_name = "vrf"
                self.yang_parent_name = "vrfs"

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

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("vrf_name",
                                "enable") and name in self.__dict__:
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


            class LabelSwitchedPaths(Entity):
                """
                Table of the Label Switched Paths
                
                .. attribute:: label_switched_path
                
                	Label Switched Path
                	**type**\: list of    :py:class:`LabelSwitchedPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStatic.Vrfs.Vrf.LabelSwitchedPaths.LabelSwitchedPath>`
                
                

                """

                _prefix = 'mpls-static-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(MplsStatic.Vrfs.Vrf.LabelSwitchedPaths, self).__init__()

                    self.yang_name = "label-switched-paths"
                    self.yang_parent_name = "vrf"

                    self.label_switched_path = YList(self)

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
                                super(MplsStatic.Vrfs.Vrf.LabelSwitchedPaths, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(MplsStatic.Vrfs.Vrf.LabelSwitchedPaths, self).__setattr__(name, value)


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
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(MplsStatic.Vrfs.Vrf.LabelSwitchedPaths.LabelSwitchedPath, self).__init__()

                        self.yang_name = "label-switched-path"
                        self.yang_parent_name = "label-switched-paths"

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
                                        "enable") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(MplsStatic.Vrfs.Vrf.LabelSwitchedPaths.LabelSwitchedPath, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(MplsStatic.Vrfs.Vrf.LabelSwitchedPaths.LabelSwitchedPath, self).__setattr__(name, value)


                    class BackupPaths(Entity):
                        """
                        Backup Path Parameters
                        
                        .. attribute:: path
                        
                        	Path Information
                        	**type**\: list of    :py:class:`Path <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStatic.Vrfs.Vrf.LabelSwitchedPaths.LabelSwitchedPath.BackupPaths.Path>`
                        
                        

                        """

                        _prefix = 'mpls-static-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(MplsStatic.Vrfs.Vrf.LabelSwitchedPaths.LabelSwitchedPath.BackupPaths, self).__init__()

                            self.yang_name = "backup-paths"
                            self.yang_parent_name = "label-switched-path"

                            self.path = YList(self)

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
                                        super(MplsStatic.Vrfs.Vrf.LabelSwitchedPaths.LabelSwitchedPath.BackupPaths, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(MplsStatic.Vrfs.Vrf.LabelSwitchedPaths.LabelSwitchedPath.BackupPaths, self).__setattr__(name, value)


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
                            
                            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                            
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
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(MplsStatic.Vrfs.Vrf.LabelSwitchedPaths.LabelSwitchedPath.BackupPaths.Path, self).__init__()

                                self.yang_name = "path"
                                self.yang_parent_name = "backup-paths"

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

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("path_id",
                                                "afi",
                                                "backup_id",
                                                "interface_name",
                                                "label_type",
                                                "metric",
                                                "next_hop_address",
                                                "next_hop_label",
                                                "nh_mode",
                                                "path_role",
                                                "path_type") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(MplsStatic.Vrfs.Vrf.LabelSwitchedPaths.LabelSwitchedPath.BackupPaths.Path, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(MplsStatic.Vrfs.Vrf.LabelSwitchedPaths.LabelSwitchedPath.BackupPaths.Path, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.path_id.is_set or
                                    self.afi.is_set or
                                    self.backup_id.is_set or
                                    self.interface_name.is_set or
                                    self.label_type.is_set or
                                    self.metric.is_set or
                                    self.next_hop_address.is_set or
                                    self.next_hop_label.is_set or
                                    self.nh_mode.is_set or
                                    self.path_role.is_set or
                                    self.path_type.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.path_id.yfilter != YFilter.not_set or
                                    self.afi.yfilter != YFilter.not_set or
                                    self.backup_id.yfilter != YFilter.not_set or
                                    self.interface_name.yfilter != YFilter.not_set or
                                    self.label_type.yfilter != YFilter.not_set or
                                    self.metric.yfilter != YFilter.not_set or
                                    self.next_hop_address.yfilter != YFilter.not_set or
                                    self.next_hop_label.yfilter != YFilter.not_set or
                                    self.nh_mode.yfilter != YFilter.not_set or
                                    self.path_role.yfilter != YFilter.not_set or
                                    self.path_type.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "path" + "[path-id='" + self.path_id.get() + "']" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.path_id.is_set or self.path_id.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.path_id.get_name_leafdata())
                                if (self.afi.is_set or self.afi.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.afi.get_name_leafdata())
                                if (self.backup_id.is_set or self.backup_id.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.backup_id.get_name_leafdata())
                                if (self.interface_name.is_set or self.interface_name.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.interface_name.get_name_leafdata())
                                if (self.label_type.is_set or self.label_type.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.label_type.get_name_leafdata())
                                if (self.metric.is_set or self.metric.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.metric.get_name_leafdata())
                                if (self.next_hop_address.is_set or self.next_hop_address.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.next_hop_address.get_name_leafdata())
                                if (self.next_hop_label.is_set or self.next_hop_label.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.next_hop_label.get_name_leafdata())
                                if (self.nh_mode.is_set or self.nh_mode.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.nh_mode.get_name_leafdata())
                                if (self.path_role.is_set or self.path_role.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.path_role.get_name_leafdata())
                                if (self.path_type.is_set or self.path_type.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.path_type.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "path-id" or name == "afi" or name == "backup-id" or name == "interface-name" or name == "label-type" or name == "metric" or name == "next-hop-address" or name == "next-hop-label" or name == "nh-mode" or name == "path-role" or name == "path-type"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "path-id"):
                                    self.path_id = value
                                    self.path_id.value_namespace = name_space
                                    self.path_id.value_namespace_prefix = name_space_prefix
                                if(value_path == "afi"):
                                    self.afi = value
                                    self.afi.value_namespace = name_space
                                    self.afi.value_namespace_prefix = name_space_prefix
                                if(value_path == "backup-id"):
                                    self.backup_id = value
                                    self.backup_id.value_namespace = name_space
                                    self.backup_id.value_namespace_prefix = name_space_prefix
                                if(value_path == "interface-name"):
                                    self.interface_name = value
                                    self.interface_name.value_namespace = name_space
                                    self.interface_name.value_namespace_prefix = name_space_prefix
                                if(value_path == "label-type"):
                                    self.label_type = value
                                    self.label_type.value_namespace = name_space
                                    self.label_type.value_namespace_prefix = name_space_prefix
                                if(value_path == "metric"):
                                    self.metric = value
                                    self.metric.value_namespace = name_space
                                    self.metric.value_namespace_prefix = name_space_prefix
                                if(value_path == "next-hop-address"):
                                    self.next_hop_address = value
                                    self.next_hop_address.value_namespace = name_space
                                    self.next_hop_address.value_namespace_prefix = name_space_prefix
                                if(value_path == "next-hop-label"):
                                    self.next_hop_label = value
                                    self.next_hop_label.value_namespace = name_space
                                    self.next_hop_label.value_namespace_prefix = name_space_prefix
                                if(value_path == "nh-mode"):
                                    self.nh_mode = value
                                    self.nh_mode.value_namespace = name_space
                                    self.nh_mode.value_namespace_prefix = name_space_prefix
                                if(value_path == "path-role"):
                                    self.path_role = value
                                    self.path_role.value_namespace = name_space
                                    self.path_role.value_namespace_prefix = name_space_prefix
                                if(value_path == "path-type"):
                                    self.path_type = value
                                    self.path_type.value_namespace = name_space
                                    self.path_type.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            for c in self.path:
                                if (c.has_data()):
                                    return True
                            return False

                        def has_operation(self):
                            for c in self.path:
                                if (c.has_operation()):
                                    return True
                            return self.yfilter != YFilter.not_set

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "backup-paths" + path_buffer

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

                            if (child_yang_name == "path"):
                                for c in self.path:
                                    segment = c.get_segment_path()
                                    if (segment_path == segment):
                                        return c
                                c = MplsStatic.Vrfs.Vrf.LabelSwitchedPaths.LabelSwitchedPath.BackupPaths.Path()
                                c.parent = self
                                local_reference_key = "ydk::seg::%s" % segment_path
                                self._local_refs[local_reference_key] = c
                                self.path.append(c)
                                return c

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "path"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            pass


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
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(MplsStatic.Vrfs.Vrf.LabelSwitchedPaths.LabelSwitchedPath.InLabel, self).__init__()

                            self.yang_name = "in-label"
                            self.yang_parent_name = "label-switched-path"

                            self.in_label_value = YLeaf(YType.uint32, "in-label-value")

                            self.label_mode = YLeaf(YType.enumeration, "label-mode")

                            self.prefix = YLeaf(YType.str, "prefix")

                            self.prefix_length = YLeaf(YType.int32, "prefix-length")

                            self.tlh_mode = YLeaf(YType.boolean, "tlh-mode")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("in_label_value",
                                            "label_mode",
                                            "prefix",
                                            "prefix_length",
                                            "tlh_mode") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(MplsStatic.Vrfs.Vrf.LabelSwitchedPaths.LabelSwitchedPath.InLabel, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(MplsStatic.Vrfs.Vrf.LabelSwitchedPaths.LabelSwitchedPath.InLabel, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.in_label_value.is_set or
                                self.label_mode.is_set or
                                self.prefix.is_set or
                                self.prefix_length.is_set or
                                self.tlh_mode.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.in_label_value.yfilter != YFilter.not_set or
                                self.label_mode.yfilter != YFilter.not_set or
                                self.prefix.yfilter != YFilter.not_set or
                                self.prefix_length.yfilter != YFilter.not_set or
                                self.tlh_mode.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "in-label" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.in_label_value.is_set or self.in_label_value.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.in_label_value.get_name_leafdata())
                            if (self.label_mode.is_set or self.label_mode.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.label_mode.get_name_leafdata())
                            if (self.prefix.is_set or self.prefix.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.prefix.get_name_leafdata())
                            if (self.prefix_length.is_set or self.prefix_length.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.prefix_length.get_name_leafdata())
                            if (self.tlh_mode.is_set or self.tlh_mode.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.tlh_mode.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "in-label-value" or name == "label-mode" or name == "prefix" or name == "prefix-length" or name == "tlh-mode"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "in-label-value"):
                                self.in_label_value = value
                                self.in_label_value.value_namespace = name_space
                                self.in_label_value.value_namespace_prefix = name_space_prefix
                            if(value_path == "label-mode"):
                                self.label_mode = value
                                self.label_mode.value_namespace = name_space
                                self.label_mode.value_namespace_prefix = name_space_prefix
                            if(value_path == "prefix"):
                                self.prefix = value
                                self.prefix.value_namespace = name_space
                                self.prefix.value_namespace_prefix = name_space_prefix
                            if(value_path == "prefix-length"):
                                self.prefix_length = value
                                self.prefix_length.value_namespace = name_space
                                self.prefix_length.value_namespace_prefix = name_space_prefix
                            if(value_path == "tlh-mode"):
                                self.tlh_mode = value
                                self.tlh_mode.value_namespace = name_space
                                self.tlh_mode.value_namespace_prefix = name_space_prefix


                    class Paths(Entity):
                        """
                        Forward Path Parameters
                        
                        .. attribute:: path
                        
                        	Path Information
                        	**type**\: list of    :py:class:`Path <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStatic.Vrfs.Vrf.LabelSwitchedPaths.LabelSwitchedPath.Paths.Path>`
                        
                        

                        """

                        _prefix = 'mpls-static-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(MplsStatic.Vrfs.Vrf.LabelSwitchedPaths.LabelSwitchedPath.Paths, self).__init__()

                            self.yang_name = "paths"
                            self.yang_parent_name = "label-switched-path"

                            self.path = YList(self)

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
                                        super(MplsStatic.Vrfs.Vrf.LabelSwitchedPaths.LabelSwitchedPath.Paths, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(MplsStatic.Vrfs.Vrf.LabelSwitchedPaths.LabelSwitchedPath.Paths, self).__setattr__(name, value)


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
                            
                            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                            
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
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(MplsStatic.Vrfs.Vrf.LabelSwitchedPaths.LabelSwitchedPath.Paths.Path, self).__init__()

                                self.yang_name = "path"
                                self.yang_parent_name = "paths"

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

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("path_id",
                                                "afi",
                                                "backup_id",
                                                "interface_name",
                                                "label_type",
                                                "metric",
                                                "next_hop_address",
                                                "next_hop_label",
                                                "nh_mode",
                                                "path_role",
                                                "path_type") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(MplsStatic.Vrfs.Vrf.LabelSwitchedPaths.LabelSwitchedPath.Paths.Path, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(MplsStatic.Vrfs.Vrf.LabelSwitchedPaths.LabelSwitchedPath.Paths.Path, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.path_id.is_set or
                                    self.afi.is_set or
                                    self.backup_id.is_set or
                                    self.interface_name.is_set or
                                    self.label_type.is_set or
                                    self.metric.is_set or
                                    self.next_hop_address.is_set or
                                    self.next_hop_label.is_set or
                                    self.nh_mode.is_set or
                                    self.path_role.is_set or
                                    self.path_type.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.path_id.yfilter != YFilter.not_set or
                                    self.afi.yfilter != YFilter.not_set or
                                    self.backup_id.yfilter != YFilter.not_set or
                                    self.interface_name.yfilter != YFilter.not_set or
                                    self.label_type.yfilter != YFilter.not_set or
                                    self.metric.yfilter != YFilter.not_set or
                                    self.next_hop_address.yfilter != YFilter.not_set or
                                    self.next_hop_label.yfilter != YFilter.not_set or
                                    self.nh_mode.yfilter != YFilter.not_set or
                                    self.path_role.yfilter != YFilter.not_set or
                                    self.path_type.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "path" + "[path-id='" + self.path_id.get() + "']" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.path_id.is_set or self.path_id.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.path_id.get_name_leafdata())
                                if (self.afi.is_set or self.afi.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.afi.get_name_leafdata())
                                if (self.backup_id.is_set or self.backup_id.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.backup_id.get_name_leafdata())
                                if (self.interface_name.is_set or self.interface_name.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.interface_name.get_name_leafdata())
                                if (self.label_type.is_set or self.label_type.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.label_type.get_name_leafdata())
                                if (self.metric.is_set or self.metric.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.metric.get_name_leafdata())
                                if (self.next_hop_address.is_set or self.next_hop_address.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.next_hop_address.get_name_leafdata())
                                if (self.next_hop_label.is_set or self.next_hop_label.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.next_hop_label.get_name_leafdata())
                                if (self.nh_mode.is_set or self.nh_mode.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.nh_mode.get_name_leafdata())
                                if (self.path_role.is_set or self.path_role.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.path_role.get_name_leafdata())
                                if (self.path_type.is_set or self.path_type.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.path_type.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "path-id" or name == "afi" or name == "backup-id" or name == "interface-name" or name == "label-type" or name == "metric" or name == "next-hop-address" or name == "next-hop-label" or name == "nh-mode" or name == "path-role" or name == "path-type"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "path-id"):
                                    self.path_id = value
                                    self.path_id.value_namespace = name_space
                                    self.path_id.value_namespace_prefix = name_space_prefix
                                if(value_path == "afi"):
                                    self.afi = value
                                    self.afi.value_namespace = name_space
                                    self.afi.value_namespace_prefix = name_space_prefix
                                if(value_path == "backup-id"):
                                    self.backup_id = value
                                    self.backup_id.value_namespace = name_space
                                    self.backup_id.value_namespace_prefix = name_space_prefix
                                if(value_path == "interface-name"):
                                    self.interface_name = value
                                    self.interface_name.value_namespace = name_space
                                    self.interface_name.value_namespace_prefix = name_space_prefix
                                if(value_path == "label-type"):
                                    self.label_type = value
                                    self.label_type.value_namespace = name_space
                                    self.label_type.value_namespace_prefix = name_space_prefix
                                if(value_path == "metric"):
                                    self.metric = value
                                    self.metric.value_namespace = name_space
                                    self.metric.value_namespace_prefix = name_space_prefix
                                if(value_path == "next-hop-address"):
                                    self.next_hop_address = value
                                    self.next_hop_address.value_namespace = name_space
                                    self.next_hop_address.value_namespace_prefix = name_space_prefix
                                if(value_path == "next-hop-label"):
                                    self.next_hop_label = value
                                    self.next_hop_label.value_namespace = name_space
                                    self.next_hop_label.value_namespace_prefix = name_space_prefix
                                if(value_path == "nh-mode"):
                                    self.nh_mode = value
                                    self.nh_mode.value_namespace = name_space
                                    self.nh_mode.value_namespace_prefix = name_space_prefix
                                if(value_path == "path-role"):
                                    self.path_role = value
                                    self.path_role.value_namespace = name_space
                                    self.path_role.value_namespace_prefix = name_space_prefix
                                if(value_path == "path-type"):
                                    self.path_type = value
                                    self.path_type.value_namespace = name_space
                                    self.path_type.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            for c in self.path:
                                if (c.has_data()):
                                    return True
                            return False

                        def has_operation(self):
                            for c in self.path:
                                if (c.has_operation()):
                                    return True
                            return self.yfilter != YFilter.not_set

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "paths" + path_buffer

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

                            if (child_yang_name == "path"):
                                for c in self.path:
                                    segment = c.get_segment_path()
                                    if (segment_path == segment):
                                        return c
                                c = MplsStatic.Vrfs.Vrf.LabelSwitchedPaths.LabelSwitchedPath.Paths.Path()
                                c.parent = self
                                local_reference_key = "ydk::seg::%s" % segment_path
                                self._local_refs[local_reference_key] = c
                                self.path.append(c)
                                return c

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "path"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            pass

                    def has_data(self):
                        return (
                            self.lsp_name.is_set or
                            self.enable.is_set or
                            (self.backup_paths is not None and self.backup_paths.has_data()) or
                            (self.in_label is not None and self.in_label.has_data()) or
                            (self.paths is not None and self.paths.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.lsp_name.yfilter != YFilter.not_set or
                            self.enable.yfilter != YFilter.not_set or
                            (self.backup_paths is not None and self.backup_paths.has_operation()) or
                            (self.in_label is not None and self.in_label.has_operation()) or
                            (self.paths is not None and self.paths.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "label-switched-path" + "[lsp-name='" + self.lsp_name.get() + "']" + path_buffer

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
                        if (self.enable.is_set or self.enable.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.enable.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "backup-paths"):
                            if (self.backup_paths is None):
                                self.backup_paths = MplsStatic.Vrfs.Vrf.LabelSwitchedPaths.LabelSwitchedPath.BackupPaths()
                                self.backup_paths.parent = self
                                self._children_name_map["backup_paths"] = "backup-paths"
                            return self.backup_paths

                        if (child_yang_name == "in-label"):
                            if (self.in_label is None):
                                self.in_label = MplsStatic.Vrfs.Vrf.LabelSwitchedPaths.LabelSwitchedPath.InLabel()
                                self.in_label.parent = self
                                self._children_name_map["in_label"] = "in-label"
                            return self.in_label

                        if (child_yang_name == "paths"):
                            if (self.paths is None):
                                self.paths = MplsStatic.Vrfs.Vrf.LabelSwitchedPaths.LabelSwitchedPath.Paths()
                                self.paths.parent = self
                                self._children_name_map["paths"] = "paths"
                            return self.paths

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "backup-paths" or name == "in-label" or name == "paths" or name == "lsp-name" or name == "enable"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "lsp-name"):
                            self.lsp_name = value
                            self.lsp_name.value_namespace = name_space
                            self.lsp_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "enable"):
                            self.enable = value
                            self.enable.value_namespace = name_space
                            self.enable.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.label_switched_path:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.label_switched_path:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "label-switched-paths" + path_buffer

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

                    if (child_yang_name == "label-switched-path"):
                        for c in self.label_switched_path:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = MplsStatic.Vrfs.Vrf.LabelSwitchedPaths.LabelSwitchedPath()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.label_switched_path.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "label-switched-path"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class Afs(Entity):
                """
                Address Family Table
                
                .. attribute:: af
                
                	Address Family
                	**type**\: list of    :py:class:`Af <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStatic.Vrfs.Vrf.Afs.Af>`
                
                

                """

                _prefix = 'mpls-static-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(MplsStatic.Vrfs.Vrf.Afs, self).__init__()

                    self.yang_name = "afs"
                    self.yang_parent_name = "vrf"

                    self.af = YList(self)

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
                                super(MplsStatic.Vrfs.Vrf.Afs, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(MplsStatic.Vrfs.Vrf.Afs, self).__setattr__(name, value)


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
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(MplsStatic.Vrfs.Vrf.Afs.Af, self).__init__()

                        self.yang_name = "af"
                        self.yang_parent_name = "afs"

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
                                        "enable") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(MplsStatic.Vrfs.Vrf.Afs.Af, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(MplsStatic.Vrfs.Vrf.Afs.Af, self).__setattr__(name, value)


                    class TopLabelHash(Entity):
                        """
                        Top Label Hash
                        
                        .. attribute:: local_labels
                        
                        	Local Label
                        	**type**\:   :py:class:`LocalLabels <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStatic.Vrfs.Vrf.Afs.Af.TopLabelHash.LocalLabels>`
                        
                        

                        """

                        _prefix = 'mpls-static-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(MplsStatic.Vrfs.Vrf.Afs.Af.TopLabelHash, self).__init__()

                            self.yang_name = "top-label-hash"
                            self.yang_parent_name = "af"

                            self.local_labels = MplsStatic.Vrfs.Vrf.Afs.Af.TopLabelHash.LocalLabels()
                            self.local_labels.parent = self
                            self._children_name_map["local_labels"] = "local-labels"
                            self._children_yang_names.add("local-labels")


                        class LocalLabels(Entity):
                            """
                            Local Label
                            
                            .. attribute:: local_label
                            
                            	Specify Local Label
                            	**type**\: list of    :py:class:`LocalLabel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStatic.Vrfs.Vrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel>`
                            
                            

                            """

                            _prefix = 'mpls-static-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(MplsStatic.Vrfs.Vrf.Afs.Af.TopLabelHash.LocalLabels, self).__init__()

                                self.yang_name = "local-labels"
                                self.yang_parent_name = "top-label-hash"

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
                                            super(MplsStatic.Vrfs.Vrf.Afs.Af.TopLabelHash.LocalLabels, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(MplsStatic.Vrfs.Vrf.Afs.Af.TopLabelHash.LocalLabels, self).__setattr__(name, value)


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
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(MplsStatic.Vrfs.Vrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel, self).__init__()

                                    self.yang_name = "local-label"
                                    self.yang_parent_name = "local-labels"

                                    self.local_label_id = YLeaf(YType.uint32, "local-label-id")

                                    self.label_type = MplsStatic.Vrfs.Vrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel.LabelType()
                                    self.label_type.parent = self
                                    self._children_name_map["label_type"] = "label-type"
                                    self._children_yang_names.add("label-type")

                                    self.paths = MplsStatic.Vrfs.Vrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel.Paths()
                                    self.paths.parent = self
                                    self._children_name_map["paths"] = "paths"
                                    self._children_yang_names.add("paths")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("local_label_id") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(MplsStatic.Vrfs.Vrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(MplsStatic.Vrfs.Vrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel, self).__setattr__(name, value)


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
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(MplsStatic.Vrfs.Vrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel.LabelType, self).__init__()

                                        self.yang_name = "label-type"
                                        self.yang_parent_name = "local-label"

                                        self.label_mode = YLeaf(YType.enumeration, "label-mode")

                                        self.prefix = YLeaf(YType.str, "prefix")

                                        self.prefix_length = YLeaf(YType.int32, "prefix-length")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("label_mode",
                                                        "prefix",
                                                        "prefix_length") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(MplsStatic.Vrfs.Vrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel.LabelType, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(MplsStatic.Vrfs.Vrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel.LabelType, self).__setattr__(name, value)

                                    def has_data(self):
                                        return (
                                            self.label_mode.is_set or
                                            self.prefix.is_set or
                                            self.prefix_length.is_set)

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.label_mode.yfilter != YFilter.not_set or
                                            self.prefix.yfilter != YFilter.not_set or
                                            self.prefix_length.yfilter != YFilter.not_set)

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "label-type" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()
                                        if (self.label_mode.is_set or self.label_mode.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.label_mode.get_name_leafdata())
                                        if (self.prefix.is_set or self.prefix.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.prefix.get_name_leafdata())
                                        if (self.prefix_length.is_set or self.prefix_length.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.prefix_length.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "label-mode" or name == "prefix" or name == "prefix-length"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "label-mode"):
                                            self.label_mode = value
                                            self.label_mode.value_namespace = name_space
                                            self.label_mode.value_namespace_prefix = name_space_prefix
                                        if(value_path == "prefix"):
                                            self.prefix = value
                                            self.prefix.value_namespace = name_space
                                            self.prefix.value_namespace_prefix = name_space_prefix
                                        if(value_path == "prefix-length"):
                                            self.prefix_length = value
                                            self.prefix_length.value_namespace = name_space
                                            self.prefix_length.value_namespace_prefix = name_space_prefix


                                class Paths(Entity):
                                    """
                                    Forward Path Parameters
                                    
                                    .. attribute:: path
                                    
                                    	Path Information
                                    	**type**\: list of    :py:class:`Path <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStatic.Vrfs.Vrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel.Paths.Path>`
                                    
                                    

                                    """

                                    _prefix = 'mpls-static-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(MplsStatic.Vrfs.Vrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel.Paths, self).__init__()

                                        self.yang_name = "paths"
                                        self.yang_parent_name = "local-label"

                                        self.path = YList(self)

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
                                                    super(MplsStatic.Vrfs.Vrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel.Paths, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(MplsStatic.Vrfs.Vrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel.Paths, self).__setattr__(name, value)


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
                                        
                                        	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                                        
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
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(MplsStatic.Vrfs.Vrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel.Paths.Path, self).__init__()

                                            self.yang_name = "path"
                                            self.yang_parent_name = "paths"

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

                                        def __setattr__(self, name, value):
                                            self._check_monkey_patching_error(name, value)
                                            with _handle_type_error():
                                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                        "Please use list append or extend method."
                                                                        .format(value))
                                                if isinstance(value, Enum.YLeaf):
                                                    value = value.name
                                                if name in ("path_id",
                                                            "afi",
                                                            "backup_id",
                                                            "interface_name",
                                                            "label_type",
                                                            "metric",
                                                            "next_hop_address",
                                                            "next_hop_label",
                                                            "nh_mode",
                                                            "path_role",
                                                            "path_type") and name in self.__dict__:
                                                    if isinstance(value, YLeaf):
                                                        self.__dict__[name].set(value.get())
                                                    elif isinstance(value, YLeafList):
                                                        super(MplsStatic.Vrfs.Vrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel.Paths.Path, self).__setattr__(name, value)
                                                    else:
                                                        self.__dict__[name].set(value)
                                                else:
                                                    if hasattr(value, "parent") and name != "parent":
                                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                            value.parent = self
                                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                                            value.parent = self
                                                    super(MplsStatic.Vrfs.Vrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel.Paths.Path, self).__setattr__(name, value)

                                        def has_data(self):
                                            return (
                                                self.path_id.is_set or
                                                self.afi.is_set or
                                                self.backup_id.is_set or
                                                self.interface_name.is_set or
                                                self.label_type.is_set or
                                                self.metric.is_set or
                                                self.next_hop_address.is_set or
                                                self.next_hop_label.is_set or
                                                self.nh_mode.is_set or
                                                self.path_role.is_set or
                                                self.path_type.is_set)

                                        def has_operation(self):
                                            return (
                                                self.yfilter != YFilter.not_set or
                                                self.path_id.yfilter != YFilter.not_set or
                                                self.afi.yfilter != YFilter.not_set or
                                                self.backup_id.yfilter != YFilter.not_set or
                                                self.interface_name.yfilter != YFilter.not_set or
                                                self.label_type.yfilter != YFilter.not_set or
                                                self.metric.yfilter != YFilter.not_set or
                                                self.next_hop_address.yfilter != YFilter.not_set or
                                                self.next_hop_label.yfilter != YFilter.not_set or
                                                self.nh_mode.yfilter != YFilter.not_set or
                                                self.path_role.yfilter != YFilter.not_set or
                                                self.path_type.yfilter != YFilter.not_set)

                                        def get_segment_path(self):
                                            path_buffer = ""
                                            path_buffer = "path" + "[path-id='" + self.path_id.get() + "']" + path_buffer

                                            return path_buffer

                                        def get_entity_path(self, ancestor):
                                            path_buffer = ""
                                            if (ancestor is None):
                                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                            else:
                                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                            leaf_name_data = LeafDataList()
                                            if (self.path_id.is_set or self.path_id.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.path_id.get_name_leafdata())
                                            if (self.afi.is_set or self.afi.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.afi.get_name_leafdata())
                                            if (self.backup_id.is_set or self.backup_id.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.backup_id.get_name_leafdata())
                                            if (self.interface_name.is_set or self.interface_name.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.interface_name.get_name_leafdata())
                                            if (self.label_type.is_set or self.label_type.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.label_type.get_name_leafdata())
                                            if (self.metric.is_set or self.metric.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.metric.get_name_leafdata())
                                            if (self.next_hop_address.is_set or self.next_hop_address.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.next_hop_address.get_name_leafdata())
                                            if (self.next_hop_label.is_set or self.next_hop_label.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.next_hop_label.get_name_leafdata())
                                            if (self.nh_mode.is_set or self.nh_mode.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.nh_mode.get_name_leafdata())
                                            if (self.path_role.is_set or self.path_role.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.path_role.get_name_leafdata())
                                            if (self.path_type.is_set or self.path_type.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.path_type.get_name_leafdata())

                                            entity_path = EntityPath(path_buffer, leaf_name_data)
                                            return entity_path

                                        def get_child_by_name(self, child_yang_name, segment_path):
                                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                            if child is not None:
                                                return child

                                            return None

                                        def has_leaf_or_child_of_name(self, name):
                                            if(name == "path-id" or name == "afi" or name == "backup-id" or name == "interface-name" or name == "label-type" or name == "metric" or name == "next-hop-address" or name == "next-hop-label" or name == "nh-mode" or name == "path-role" or name == "path-type"):
                                                return True
                                            return False

                                        def set_value(self, value_path, value, name_space, name_space_prefix):
                                            if(value_path == "path-id"):
                                                self.path_id = value
                                                self.path_id.value_namespace = name_space
                                                self.path_id.value_namespace_prefix = name_space_prefix
                                            if(value_path == "afi"):
                                                self.afi = value
                                                self.afi.value_namespace = name_space
                                                self.afi.value_namespace_prefix = name_space_prefix
                                            if(value_path == "backup-id"):
                                                self.backup_id = value
                                                self.backup_id.value_namespace = name_space
                                                self.backup_id.value_namespace_prefix = name_space_prefix
                                            if(value_path == "interface-name"):
                                                self.interface_name = value
                                                self.interface_name.value_namespace = name_space
                                                self.interface_name.value_namespace_prefix = name_space_prefix
                                            if(value_path == "label-type"):
                                                self.label_type = value
                                                self.label_type.value_namespace = name_space
                                                self.label_type.value_namespace_prefix = name_space_prefix
                                            if(value_path == "metric"):
                                                self.metric = value
                                                self.metric.value_namespace = name_space
                                                self.metric.value_namespace_prefix = name_space_prefix
                                            if(value_path == "next-hop-address"):
                                                self.next_hop_address = value
                                                self.next_hop_address.value_namespace = name_space
                                                self.next_hop_address.value_namespace_prefix = name_space_prefix
                                            if(value_path == "next-hop-label"):
                                                self.next_hop_label = value
                                                self.next_hop_label.value_namespace = name_space
                                                self.next_hop_label.value_namespace_prefix = name_space_prefix
                                            if(value_path == "nh-mode"):
                                                self.nh_mode = value
                                                self.nh_mode.value_namespace = name_space
                                                self.nh_mode.value_namespace_prefix = name_space_prefix
                                            if(value_path == "path-role"):
                                                self.path_role = value
                                                self.path_role.value_namespace = name_space
                                                self.path_role.value_namespace_prefix = name_space_prefix
                                            if(value_path == "path-type"):
                                                self.path_type = value
                                                self.path_type.value_namespace = name_space
                                                self.path_type.value_namespace_prefix = name_space_prefix

                                    def has_data(self):
                                        for c in self.path:
                                            if (c.has_data()):
                                                return True
                                        return False

                                    def has_operation(self):
                                        for c in self.path:
                                            if (c.has_operation()):
                                                return True
                                        return self.yfilter != YFilter.not_set

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "paths" + path_buffer

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

                                        if (child_yang_name == "path"):
                                            for c in self.path:
                                                segment = c.get_segment_path()
                                                if (segment_path == segment):
                                                    return c
                                            c = MplsStatic.Vrfs.Vrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel.Paths.Path()
                                            c.parent = self
                                            local_reference_key = "ydk::seg::%s" % segment_path
                                            self._local_refs[local_reference_key] = c
                                            self.path.append(c)
                                            return c

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "path"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        pass

                                def has_data(self):
                                    return (
                                        self.local_label_id.is_set or
                                        (self.label_type is not None and self.label_type.has_data()) or
                                        (self.paths is not None and self.paths.has_data()))

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.local_label_id.yfilter != YFilter.not_set or
                                        (self.label_type is not None and self.label_type.has_operation()) or
                                        (self.paths is not None and self.paths.has_operation()))

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

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    if (child_yang_name == "label-type"):
                                        if (self.label_type is None):
                                            self.label_type = MplsStatic.Vrfs.Vrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel.LabelType()
                                            self.label_type.parent = self
                                            self._children_name_map["label_type"] = "label-type"
                                        return self.label_type

                                    if (child_yang_name == "paths"):
                                        if (self.paths is None):
                                            self.paths = MplsStatic.Vrfs.Vrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel.Paths()
                                            self.paths.parent = self
                                            self._children_name_map["paths"] = "paths"
                                        return self.paths

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "label-type" or name == "paths" or name == "local-label-id"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "local-label-id"):
                                        self.local_label_id = value
                                        self.local_label_id.value_namespace = name_space
                                        self.local_label_id.value_namespace_prefix = name_space_prefix

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
                                    c = MplsStatic.Vrfs.Vrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel()
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
                            return (self.local_labels is not None and self.local_labels.has_data())

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                (self.local_labels is not None and self.local_labels.has_operation()))

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "top-label-hash" + path_buffer

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

                            if (child_yang_name == "local-labels"):
                                if (self.local_labels is None):
                                    self.local_labels = MplsStatic.Vrfs.Vrf.Afs.Af.TopLabelHash.LocalLabels()
                                    self.local_labels.parent = self
                                    self._children_name_map["local_labels"] = "local-labels"
                                return self.local_labels

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "local-labels"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            pass


                    class LocalLabels(Entity):
                        """
                        Local Label
                        
                        .. attribute:: local_label
                        
                        	Specify Local Label
                        	**type**\: list of    :py:class:`LocalLabel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStatic.Vrfs.Vrf.Afs.Af.LocalLabels.LocalLabel>`
                        
                        

                        """

                        _prefix = 'mpls-static-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(MplsStatic.Vrfs.Vrf.Afs.Af.LocalLabels, self).__init__()

                            self.yang_name = "local-labels"
                            self.yang_parent_name = "af"

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
                                        super(MplsStatic.Vrfs.Vrf.Afs.Af.LocalLabels, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(MplsStatic.Vrfs.Vrf.Afs.Af.LocalLabels, self).__setattr__(name, value)


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
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(MplsStatic.Vrfs.Vrf.Afs.Af.LocalLabels.LocalLabel, self).__init__()

                                self.yang_name = "local-label"
                                self.yang_parent_name = "local-labels"

                                self.local_label_id = YLeaf(YType.uint32, "local-label-id")

                                self.label_type = MplsStatic.Vrfs.Vrf.Afs.Af.LocalLabels.LocalLabel.LabelType()
                                self.label_type.parent = self
                                self._children_name_map["label_type"] = "label-type"
                                self._children_yang_names.add("label-type")

                                self.paths = MplsStatic.Vrfs.Vrf.Afs.Af.LocalLabels.LocalLabel.Paths()
                                self.paths.parent = self
                                self._children_name_map["paths"] = "paths"
                                self._children_yang_names.add("paths")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("local_label_id") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(MplsStatic.Vrfs.Vrf.Afs.Af.LocalLabels.LocalLabel, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(MplsStatic.Vrfs.Vrf.Afs.Af.LocalLabels.LocalLabel, self).__setattr__(name, value)


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
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(MplsStatic.Vrfs.Vrf.Afs.Af.LocalLabels.LocalLabel.LabelType, self).__init__()

                                    self.yang_name = "label-type"
                                    self.yang_parent_name = "local-label"

                                    self.label_mode = YLeaf(YType.enumeration, "label-mode")

                                    self.prefix = YLeaf(YType.str, "prefix")

                                    self.prefix_length = YLeaf(YType.int32, "prefix-length")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("label_mode",
                                                    "prefix",
                                                    "prefix_length") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(MplsStatic.Vrfs.Vrf.Afs.Af.LocalLabels.LocalLabel.LabelType, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(MplsStatic.Vrfs.Vrf.Afs.Af.LocalLabels.LocalLabel.LabelType, self).__setattr__(name, value)

                                def has_data(self):
                                    return (
                                        self.label_mode.is_set or
                                        self.prefix.is_set or
                                        self.prefix_length.is_set)

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.label_mode.yfilter != YFilter.not_set or
                                        self.prefix.yfilter != YFilter.not_set or
                                        self.prefix_length.yfilter != YFilter.not_set)

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "label-type" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.label_mode.is_set or self.label_mode.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.label_mode.get_name_leafdata())
                                    if (self.prefix.is_set or self.prefix.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.prefix.get_name_leafdata())
                                    if (self.prefix_length.is_set or self.prefix_length.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.prefix_length.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "label-mode" or name == "prefix" or name == "prefix-length"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "label-mode"):
                                        self.label_mode = value
                                        self.label_mode.value_namespace = name_space
                                        self.label_mode.value_namespace_prefix = name_space_prefix
                                    if(value_path == "prefix"):
                                        self.prefix = value
                                        self.prefix.value_namespace = name_space
                                        self.prefix.value_namespace_prefix = name_space_prefix
                                    if(value_path == "prefix-length"):
                                        self.prefix_length = value
                                        self.prefix_length.value_namespace = name_space
                                        self.prefix_length.value_namespace_prefix = name_space_prefix


                            class Paths(Entity):
                                """
                                Forward Path Parameters
                                
                                .. attribute:: path
                                
                                	Path Information
                                	**type**\: list of    :py:class:`Path <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStatic.Vrfs.Vrf.Afs.Af.LocalLabels.LocalLabel.Paths.Path>`
                                
                                

                                """

                                _prefix = 'mpls-static-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(MplsStatic.Vrfs.Vrf.Afs.Af.LocalLabels.LocalLabel.Paths, self).__init__()

                                    self.yang_name = "paths"
                                    self.yang_parent_name = "local-label"

                                    self.path = YList(self)

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
                                                super(MplsStatic.Vrfs.Vrf.Afs.Af.LocalLabels.LocalLabel.Paths, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(MplsStatic.Vrfs.Vrf.Afs.Af.LocalLabels.LocalLabel.Paths, self).__setattr__(name, value)


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
                                    
                                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                                    
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
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(MplsStatic.Vrfs.Vrf.Afs.Af.LocalLabels.LocalLabel.Paths.Path, self).__init__()

                                        self.yang_name = "path"
                                        self.yang_parent_name = "paths"

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

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("path_id",
                                                        "afi",
                                                        "backup_id",
                                                        "interface_name",
                                                        "label_type",
                                                        "metric",
                                                        "next_hop_address",
                                                        "next_hop_label",
                                                        "nh_mode",
                                                        "path_role",
                                                        "path_type") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(MplsStatic.Vrfs.Vrf.Afs.Af.LocalLabels.LocalLabel.Paths.Path, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(MplsStatic.Vrfs.Vrf.Afs.Af.LocalLabels.LocalLabel.Paths.Path, self).__setattr__(name, value)

                                    def has_data(self):
                                        return (
                                            self.path_id.is_set or
                                            self.afi.is_set or
                                            self.backup_id.is_set or
                                            self.interface_name.is_set or
                                            self.label_type.is_set or
                                            self.metric.is_set or
                                            self.next_hop_address.is_set or
                                            self.next_hop_label.is_set or
                                            self.nh_mode.is_set or
                                            self.path_role.is_set or
                                            self.path_type.is_set)

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.path_id.yfilter != YFilter.not_set or
                                            self.afi.yfilter != YFilter.not_set or
                                            self.backup_id.yfilter != YFilter.not_set or
                                            self.interface_name.yfilter != YFilter.not_set or
                                            self.label_type.yfilter != YFilter.not_set or
                                            self.metric.yfilter != YFilter.not_set or
                                            self.next_hop_address.yfilter != YFilter.not_set or
                                            self.next_hop_label.yfilter != YFilter.not_set or
                                            self.nh_mode.yfilter != YFilter.not_set or
                                            self.path_role.yfilter != YFilter.not_set or
                                            self.path_type.yfilter != YFilter.not_set)

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "path" + "[path-id='" + self.path_id.get() + "']" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()
                                        if (self.path_id.is_set or self.path_id.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.path_id.get_name_leafdata())
                                        if (self.afi.is_set or self.afi.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.afi.get_name_leafdata())
                                        if (self.backup_id.is_set or self.backup_id.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.backup_id.get_name_leafdata())
                                        if (self.interface_name.is_set or self.interface_name.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.interface_name.get_name_leafdata())
                                        if (self.label_type.is_set or self.label_type.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.label_type.get_name_leafdata())
                                        if (self.metric.is_set or self.metric.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.metric.get_name_leafdata())
                                        if (self.next_hop_address.is_set or self.next_hop_address.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.next_hop_address.get_name_leafdata())
                                        if (self.next_hop_label.is_set or self.next_hop_label.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.next_hop_label.get_name_leafdata())
                                        if (self.nh_mode.is_set or self.nh_mode.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.nh_mode.get_name_leafdata())
                                        if (self.path_role.is_set or self.path_role.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.path_role.get_name_leafdata())
                                        if (self.path_type.is_set or self.path_type.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.path_type.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "path-id" or name == "afi" or name == "backup-id" or name == "interface-name" or name == "label-type" or name == "metric" or name == "next-hop-address" or name == "next-hop-label" or name == "nh-mode" or name == "path-role" or name == "path-type"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "path-id"):
                                            self.path_id = value
                                            self.path_id.value_namespace = name_space
                                            self.path_id.value_namespace_prefix = name_space_prefix
                                        if(value_path == "afi"):
                                            self.afi = value
                                            self.afi.value_namespace = name_space
                                            self.afi.value_namespace_prefix = name_space_prefix
                                        if(value_path == "backup-id"):
                                            self.backup_id = value
                                            self.backup_id.value_namespace = name_space
                                            self.backup_id.value_namespace_prefix = name_space_prefix
                                        if(value_path == "interface-name"):
                                            self.interface_name = value
                                            self.interface_name.value_namespace = name_space
                                            self.interface_name.value_namespace_prefix = name_space_prefix
                                        if(value_path == "label-type"):
                                            self.label_type = value
                                            self.label_type.value_namespace = name_space
                                            self.label_type.value_namespace_prefix = name_space_prefix
                                        if(value_path == "metric"):
                                            self.metric = value
                                            self.metric.value_namespace = name_space
                                            self.metric.value_namespace_prefix = name_space_prefix
                                        if(value_path == "next-hop-address"):
                                            self.next_hop_address = value
                                            self.next_hop_address.value_namespace = name_space
                                            self.next_hop_address.value_namespace_prefix = name_space_prefix
                                        if(value_path == "next-hop-label"):
                                            self.next_hop_label = value
                                            self.next_hop_label.value_namespace = name_space
                                            self.next_hop_label.value_namespace_prefix = name_space_prefix
                                        if(value_path == "nh-mode"):
                                            self.nh_mode = value
                                            self.nh_mode.value_namespace = name_space
                                            self.nh_mode.value_namespace_prefix = name_space_prefix
                                        if(value_path == "path-role"):
                                            self.path_role = value
                                            self.path_role.value_namespace = name_space
                                            self.path_role.value_namespace_prefix = name_space_prefix
                                        if(value_path == "path-type"):
                                            self.path_type = value
                                            self.path_type.value_namespace = name_space
                                            self.path_type.value_namespace_prefix = name_space_prefix

                                def has_data(self):
                                    for c in self.path:
                                        if (c.has_data()):
                                            return True
                                    return False

                                def has_operation(self):
                                    for c in self.path:
                                        if (c.has_operation()):
                                            return True
                                    return self.yfilter != YFilter.not_set

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "paths" + path_buffer

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

                                    if (child_yang_name == "path"):
                                        for c in self.path:
                                            segment = c.get_segment_path()
                                            if (segment_path == segment):
                                                return c
                                        c = MplsStatic.Vrfs.Vrf.Afs.Af.LocalLabels.LocalLabel.Paths.Path()
                                        c.parent = self
                                        local_reference_key = "ydk::seg::%s" % segment_path
                                        self._local_refs[local_reference_key] = c
                                        self.path.append(c)
                                        return c

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "path"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    pass

                            def has_data(self):
                                return (
                                    self.local_label_id.is_set or
                                    (self.label_type is not None and self.label_type.has_data()) or
                                    (self.paths is not None and self.paths.has_data()))

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.local_label_id.yfilter != YFilter.not_set or
                                    (self.label_type is not None and self.label_type.has_operation()) or
                                    (self.paths is not None and self.paths.has_operation()))

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

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                if (child_yang_name == "label-type"):
                                    if (self.label_type is None):
                                        self.label_type = MplsStatic.Vrfs.Vrf.Afs.Af.LocalLabels.LocalLabel.LabelType()
                                        self.label_type.parent = self
                                        self._children_name_map["label_type"] = "label-type"
                                    return self.label_type

                                if (child_yang_name == "paths"):
                                    if (self.paths is None):
                                        self.paths = MplsStatic.Vrfs.Vrf.Afs.Af.LocalLabels.LocalLabel.Paths()
                                        self.paths.parent = self
                                        self._children_name_map["paths"] = "paths"
                                    return self.paths

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "label-type" or name == "paths" or name == "local-label-id"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "local-label-id"):
                                    self.local_label_id = value
                                    self.local_label_id.value_namespace = name_space
                                    self.local_label_id.value_namespace_prefix = name_space_prefix

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
                                c = MplsStatic.Vrfs.Vrf.Afs.Af.LocalLabels.LocalLabel()
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
                            self.afi.is_set or
                            self.enable.is_set or
                            (self.local_labels is not None and self.local_labels.has_data()) or
                            (self.top_label_hash is not None and self.top_label_hash.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.afi.yfilter != YFilter.not_set or
                            self.enable.yfilter != YFilter.not_set or
                            (self.local_labels is not None and self.local_labels.has_operation()) or
                            (self.top_label_hash is not None and self.top_label_hash.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "af" + "[afi='" + self.afi.get() + "']" + path_buffer

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
                        if (self.enable.is_set or self.enable.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.enable.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "local-labels"):
                            if (self.local_labels is None):
                                self.local_labels = MplsStatic.Vrfs.Vrf.Afs.Af.LocalLabels()
                                self.local_labels.parent = self
                                self._children_name_map["local_labels"] = "local-labels"
                            return self.local_labels

                        if (child_yang_name == "top-label-hash"):
                            if (self.top_label_hash is None):
                                self.top_label_hash = MplsStatic.Vrfs.Vrf.Afs.Af.TopLabelHash()
                                self.top_label_hash.parent = self
                                self._children_name_map["top_label_hash"] = "top-label-hash"
                            return self.top_label_hash

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "local-labels" or name == "top-label-hash" or name == "afi" or name == "enable"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "afi"):
                            self.afi = value
                            self.afi.value_namespace = name_space
                            self.afi.value_namespace_prefix = name_space_prefix
                        if(value_path == "enable"):
                            self.enable = value
                            self.enable.value_namespace = name_space
                            self.enable.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.af:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.af:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "afs" + path_buffer

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

                    if (child_yang_name == "af"):
                        for c in self.af:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = MplsStatic.Vrfs.Vrf.Afs.Af()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.af.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "af"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass

            def has_data(self):
                return (
                    self.vrf_name.is_set or
                    self.enable.is_set or
                    (self.afs is not None and self.afs.has_data()) or
                    (self.label_switched_paths is not None and self.label_switched_paths.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.vrf_name.yfilter != YFilter.not_set or
                    self.enable.yfilter != YFilter.not_set or
                    (self.afs is not None and self.afs.has_operation()) or
                    (self.label_switched_paths is not None and self.label_switched_paths.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "vrf" + "[vrf-name='" + self.vrf_name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-mpls-static-cfg:mpls-static/vrfs/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.vrf_name.is_set or self.vrf_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vrf_name.get_name_leafdata())
                if (self.enable.is_set or self.enable.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.enable.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "afs"):
                    if (self.afs is None):
                        self.afs = MplsStatic.Vrfs.Vrf.Afs()
                        self.afs.parent = self
                        self._children_name_map["afs"] = "afs"
                    return self.afs

                if (child_yang_name == "label-switched-paths"):
                    if (self.label_switched_paths is None):
                        self.label_switched_paths = MplsStatic.Vrfs.Vrf.LabelSwitchedPaths()
                        self.label_switched_paths.parent = self
                        self._children_name_map["label_switched_paths"] = "label-switched-paths"
                    return self.label_switched_paths

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "afs" or name == "label-switched-paths" or name == "vrf-name" or name == "enable"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "vrf-name"):
                    self.vrf_name = value
                    self.vrf_name.value_namespace = name_space
                    self.vrf_name.value_namespace_prefix = name_space_prefix
                if(value_path == "enable"):
                    self.enable = value
                    self.enable.value_namespace = name_space
                    self.enable.value_namespace_prefix = name_space_prefix

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
                path_buffer = "Cisco-IOS-XR-mpls-static-cfg:mpls-static/%s" % self.get_segment_path()
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


    class Interfaces(Entity):
        """
        MPLS Static Interface Table
        
        .. attribute:: interface
        
        	MPLS Static Interface Enable
        	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStatic.Interfaces.Interface>`
        
        

        """

        _prefix = 'mpls-static-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(MplsStatic.Interfaces, self).__init__()

            self.yang_name = "interfaces"
            self.yang_parent_name = "mpls-static"

            self.interface = YList(self)

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
                        super(MplsStatic.Interfaces, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(MplsStatic.Interfaces, self).__setattr__(name, value)


        class Interface(Entity):
            """
            MPLS Static Interface Enable
            
            .. attribute:: interface_name  <key>
            
            	Name of Interface
            	**type**\:  str
            
            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
            
            

            """

            _prefix = 'mpls-static-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(MplsStatic.Interfaces.Interface, self).__init__()

                self.yang_name = "interface"
                self.yang_parent_name = "interfaces"

                self.interface_name = YLeaf(YType.str, "interface-name")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("interface_name") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(MplsStatic.Interfaces.Interface, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(MplsStatic.Interfaces.Interface, self).__setattr__(name, value)

            def has_data(self):
                return self.interface_name.is_set

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.interface_name.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "interface" + "[interface-name='" + self.interface_name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-mpls-static-cfg:mpls-static/interfaces/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.interface_name.is_set or self.interface_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.interface_name.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "interface-name"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "interface-name"):
                    self.interface_name = value
                    self.interface_name.value_namespace = name_space
                    self.interface_name.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.interface:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.interface:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "interfaces" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-mpls-static-cfg:mpls-static/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "interface"):
                for c in self.interface:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = MplsStatic.Interfaces.Interface()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.interface.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "interface"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


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
        _revision = '2015-11-09'

        def __init__(self):
            super(MplsStatic.DefaultVrf, self).__init__()

            self.yang_name = "default-vrf"
            self.yang_parent_name = "mpls-static"

            self.enable = YLeaf(YType.empty, "enable")

            self.afs = MplsStatic.DefaultVrf.Afs()
            self.afs.parent = self
            self._children_name_map["afs"] = "afs"
            self._children_yang_names.add("afs")

            self.label_switched_paths = MplsStatic.DefaultVrf.LabelSwitchedPaths()
            self.label_switched_paths.parent = self
            self._children_name_map["label_switched_paths"] = "label-switched-paths"
            self._children_yang_names.add("label-switched-paths")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("enable") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(MplsStatic.DefaultVrf, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(MplsStatic.DefaultVrf, self).__setattr__(name, value)


        class LabelSwitchedPaths(Entity):
            """
            Table of the Label Switched Paths
            
            .. attribute:: label_switched_path
            
            	Label Switched Path
            	**type**\: list of    :py:class:`LabelSwitchedPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStatic.DefaultVrf.LabelSwitchedPaths.LabelSwitchedPath>`
            
            

            """

            _prefix = 'mpls-static-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(MplsStatic.DefaultVrf.LabelSwitchedPaths, self).__init__()

                self.yang_name = "label-switched-paths"
                self.yang_parent_name = "default-vrf"

                self.label_switched_path = YList(self)

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
                            super(MplsStatic.DefaultVrf.LabelSwitchedPaths, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(MplsStatic.DefaultVrf.LabelSwitchedPaths, self).__setattr__(name, value)


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
                _revision = '2015-11-09'

                def __init__(self):
                    super(MplsStatic.DefaultVrf.LabelSwitchedPaths.LabelSwitchedPath, self).__init__()

                    self.yang_name = "label-switched-path"
                    self.yang_parent_name = "label-switched-paths"

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
                                    "enable") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(MplsStatic.DefaultVrf.LabelSwitchedPaths.LabelSwitchedPath, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(MplsStatic.DefaultVrf.LabelSwitchedPaths.LabelSwitchedPath, self).__setattr__(name, value)


                class BackupPaths(Entity):
                    """
                    Backup Path Parameters
                    
                    .. attribute:: path
                    
                    	Path Information
                    	**type**\: list of    :py:class:`Path <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStatic.DefaultVrf.LabelSwitchedPaths.LabelSwitchedPath.BackupPaths.Path>`
                    
                    

                    """

                    _prefix = 'mpls-static-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(MplsStatic.DefaultVrf.LabelSwitchedPaths.LabelSwitchedPath.BackupPaths, self).__init__()

                        self.yang_name = "backup-paths"
                        self.yang_parent_name = "label-switched-path"

                        self.path = YList(self)

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
                                    super(MplsStatic.DefaultVrf.LabelSwitchedPaths.LabelSwitchedPath.BackupPaths, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(MplsStatic.DefaultVrf.LabelSwitchedPaths.LabelSwitchedPath.BackupPaths, self).__setattr__(name, value)


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
                        
                        	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                        
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
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(MplsStatic.DefaultVrf.LabelSwitchedPaths.LabelSwitchedPath.BackupPaths.Path, self).__init__()

                            self.yang_name = "path"
                            self.yang_parent_name = "backup-paths"

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

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("path_id",
                                            "afi",
                                            "backup_id",
                                            "interface_name",
                                            "label_type",
                                            "metric",
                                            "next_hop_address",
                                            "next_hop_label",
                                            "nh_mode",
                                            "path_role",
                                            "path_type") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(MplsStatic.DefaultVrf.LabelSwitchedPaths.LabelSwitchedPath.BackupPaths.Path, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(MplsStatic.DefaultVrf.LabelSwitchedPaths.LabelSwitchedPath.BackupPaths.Path, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.path_id.is_set or
                                self.afi.is_set or
                                self.backup_id.is_set or
                                self.interface_name.is_set or
                                self.label_type.is_set or
                                self.metric.is_set or
                                self.next_hop_address.is_set or
                                self.next_hop_label.is_set or
                                self.nh_mode.is_set or
                                self.path_role.is_set or
                                self.path_type.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.path_id.yfilter != YFilter.not_set or
                                self.afi.yfilter != YFilter.not_set or
                                self.backup_id.yfilter != YFilter.not_set or
                                self.interface_name.yfilter != YFilter.not_set or
                                self.label_type.yfilter != YFilter.not_set or
                                self.metric.yfilter != YFilter.not_set or
                                self.next_hop_address.yfilter != YFilter.not_set or
                                self.next_hop_label.yfilter != YFilter.not_set or
                                self.nh_mode.yfilter != YFilter.not_set or
                                self.path_role.yfilter != YFilter.not_set or
                                self.path_type.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "path" + "[path-id='" + self.path_id.get() + "']" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.path_id.is_set or self.path_id.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.path_id.get_name_leafdata())
                            if (self.afi.is_set or self.afi.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.afi.get_name_leafdata())
                            if (self.backup_id.is_set or self.backup_id.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.backup_id.get_name_leafdata())
                            if (self.interface_name.is_set or self.interface_name.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.interface_name.get_name_leafdata())
                            if (self.label_type.is_set or self.label_type.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.label_type.get_name_leafdata())
                            if (self.metric.is_set or self.metric.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.metric.get_name_leafdata())
                            if (self.next_hop_address.is_set or self.next_hop_address.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.next_hop_address.get_name_leafdata())
                            if (self.next_hop_label.is_set or self.next_hop_label.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.next_hop_label.get_name_leafdata())
                            if (self.nh_mode.is_set or self.nh_mode.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.nh_mode.get_name_leafdata())
                            if (self.path_role.is_set or self.path_role.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.path_role.get_name_leafdata())
                            if (self.path_type.is_set or self.path_type.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.path_type.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "path-id" or name == "afi" or name == "backup-id" or name == "interface-name" or name == "label-type" or name == "metric" or name == "next-hop-address" or name == "next-hop-label" or name == "nh-mode" or name == "path-role" or name == "path-type"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "path-id"):
                                self.path_id = value
                                self.path_id.value_namespace = name_space
                                self.path_id.value_namespace_prefix = name_space_prefix
                            if(value_path == "afi"):
                                self.afi = value
                                self.afi.value_namespace = name_space
                                self.afi.value_namespace_prefix = name_space_prefix
                            if(value_path == "backup-id"):
                                self.backup_id = value
                                self.backup_id.value_namespace = name_space
                                self.backup_id.value_namespace_prefix = name_space_prefix
                            if(value_path == "interface-name"):
                                self.interface_name = value
                                self.interface_name.value_namespace = name_space
                                self.interface_name.value_namespace_prefix = name_space_prefix
                            if(value_path == "label-type"):
                                self.label_type = value
                                self.label_type.value_namespace = name_space
                                self.label_type.value_namespace_prefix = name_space_prefix
                            if(value_path == "metric"):
                                self.metric = value
                                self.metric.value_namespace = name_space
                                self.metric.value_namespace_prefix = name_space_prefix
                            if(value_path == "next-hop-address"):
                                self.next_hop_address = value
                                self.next_hop_address.value_namespace = name_space
                                self.next_hop_address.value_namespace_prefix = name_space_prefix
                            if(value_path == "next-hop-label"):
                                self.next_hop_label = value
                                self.next_hop_label.value_namespace = name_space
                                self.next_hop_label.value_namespace_prefix = name_space_prefix
                            if(value_path == "nh-mode"):
                                self.nh_mode = value
                                self.nh_mode.value_namespace = name_space
                                self.nh_mode.value_namespace_prefix = name_space_prefix
                            if(value_path == "path-role"):
                                self.path_role = value
                                self.path_role.value_namespace = name_space
                                self.path_role.value_namespace_prefix = name_space_prefix
                            if(value_path == "path-type"):
                                self.path_type = value
                                self.path_type.value_namespace = name_space
                                self.path_type.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.path:
                            if (c.has_data()):
                                return True
                        return False

                    def has_operation(self):
                        for c in self.path:
                            if (c.has_operation()):
                                return True
                        return self.yfilter != YFilter.not_set

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "backup-paths" + path_buffer

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

                        if (child_yang_name == "path"):
                            for c in self.path:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = MplsStatic.DefaultVrf.LabelSwitchedPaths.LabelSwitchedPath.BackupPaths.Path()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.path.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "path"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass


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
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(MplsStatic.DefaultVrf.LabelSwitchedPaths.LabelSwitchedPath.InLabel, self).__init__()

                        self.yang_name = "in-label"
                        self.yang_parent_name = "label-switched-path"

                        self.in_label_value = YLeaf(YType.uint32, "in-label-value")

                        self.label_mode = YLeaf(YType.enumeration, "label-mode")

                        self.prefix = YLeaf(YType.str, "prefix")

                        self.prefix_length = YLeaf(YType.int32, "prefix-length")

                        self.tlh_mode = YLeaf(YType.boolean, "tlh-mode")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("in_label_value",
                                        "label_mode",
                                        "prefix",
                                        "prefix_length",
                                        "tlh_mode") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(MplsStatic.DefaultVrf.LabelSwitchedPaths.LabelSwitchedPath.InLabel, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(MplsStatic.DefaultVrf.LabelSwitchedPaths.LabelSwitchedPath.InLabel, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.in_label_value.is_set or
                            self.label_mode.is_set or
                            self.prefix.is_set or
                            self.prefix_length.is_set or
                            self.tlh_mode.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.in_label_value.yfilter != YFilter.not_set or
                            self.label_mode.yfilter != YFilter.not_set or
                            self.prefix.yfilter != YFilter.not_set or
                            self.prefix_length.yfilter != YFilter.not_set or
                            self.tlh_mode.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "in-label" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.in_label_value.is_set or self.in_label_value.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.in_label_value.get_name_leafdata())
                        if (self.label_mode.is_set or self.label_mode.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.label_mode.get_name_leafdata())
                        if (self.prefix.is_set or self.prefix.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.prefix.get_name_leafdata())
                        if (self.prefix_length.is_set or self.prefix_length.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.prefix_length.get_name_leafdata())
                        if (self.tlh_mode.is_set or self.tlh_mode.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.tlh_mode.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "in-label-value" or name == "label-mode" or name == "prefix" or name == "prefix-length" or name == "tlh-mode"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "in-label-value"):
                            self.in_label_value = value
                            self.in_label_value.value_namespace = name_space
                            self.in_label_value.value_namespace_prefix = name_space_prefix
                        if(value_path == "label-mode"):
                            self.label_mode = value
                            self.label_mode.value_namespace = name_space
                            self.label_mode.value_namespace_prefix = name_space_prefix
                        if(value_path == "prefix"):
                            self.prefix = value
                            self.prefix.value_namespace = name_space
                            self.prefix.value_namespace_prefix = name_space_prefix
                        if(value_path == "prefix-length"):
                            self.prefix_length = value
                            self.prefix_length.value_namespace = name_space
                            self.prefix_length.value_namespace_prefix = name_space_prefix
                        if(value_path == "tlh-mode"):
                            self.tlh_mode = value
                            self.tlh_mode.value_namespace = name_space
                            self.tlh_mode.value_namespace_prefix = name_space_prefix


                class Paths(Entity):
                    """
                    Forward Path Parameters
                    
                    .. attribute:: path
                    
                    	Path Information
                    	**type**\: list of    :py:class:`Path <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStatic.DefaultVrf.LabelSwitchedPaths.LabelSwitchedPath.Paths.Path>`
                    
                    

                    """

                    _prefix = 'mpls-static-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(MplsStatic.DefaultVrf.LabelSwitchedPaths.LabelSwitchedPath.Paths, self).__init__()

                        self.yang_name = "paths"
                        self.yang_parent_name = "label-switched-path"

                        self.path = YList(self)

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
                                    super(MplsStatic.DefaultVrf.LabelSwitchedPaths.LabelSwitchedPath.Paths, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(MplsStatic.DefaultVrf.LabelSwitchedPaths.LabelSwitchedPath.Paths, self).__setattr__(name, value)


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
                        
                        	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                        
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
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(MplsStatic.DefaultVrf.LabelSwitchedPaths.LabelSwitchedPath.Paths.Path, self).__init__()

                            self.yang_name = "path"
                            self.yang_parent_name = "paths"

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

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("path_id",
                                            "afi",
                                            "backup_id",
                                            "interface_name",
                                            "label_type",
                                            "metric",
                                            "next_hop_address",
                                            "next_hop_label",
                                            "nh_mode",
                                            "path_role",
                                            "path_type") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(MplsStatic.DefaultVrf.LabelSwitchedPaths.LabelSwitchedPath.Paths.Path, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(MplsStatic.DefaultVrf.LabelSwitchedPaths.LabelSwitchedPath.Paths.Path, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.path_id.is_set or
                                self.afi.is_set or
                                self.backup_id.is_set or
                                self.interface_name.is_set or
                                self.label_type.is_set or
                                self.metric.is_set or
                                self.next_hop_address.is_set or
                                self.next_hop_label.is_set or
                                self.nh_mode.is_set or
                                self.path_role.is_set or
                                self.path_type.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.path_id.yfilter != YFilter.not_set or
                                self.afi.yfilter != YFilter.not_set or
                                self.backup_id.yfilter != YFilter.not_set or
                                self.interface_name.yfilter != YFilter.not_set or
                                self.label_type.yfilter != YFilter.not_set or
                                self.metric.yfilter != YFilter.not_set or
                                self.next_hop_address.yfilter != YFilter.not_set or
                                self.next_hop_label.yfilter != YFilter.not_set or
                                self.nh_mode.yfilter != YFilter.not_set or
                                self.path_role.yfilter != YFilter.not_set or
                                self.path_type.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "path" + "[path-id='" + self.path_id.get() + "']" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.path_id.is_set or self.path_id.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.path_id.get_name_leafdata())
                            if (self.afi.is_set or self.afi.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.afi.get_name_leafdata())
                            if (self.backup_id.is_set or self.backup_id.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.backup_id.get_name_leafdata())
                            if (self.interface_name.is_set or self.interface_name.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.interface_name.get_name_leafdata())
                            if (self.label_type.is_set or self.label_type.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.label_type.get_name_leafdata())
                            if (self.metric.is_set or self.metric.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.metric.get_name_leafdata())
                            if (self.next_hop_address.is_set or self.next_hop_address.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.next_hop_address.get_name_leafdata())
                            if (self.next_hop_label.is_set or self.next_hop_label.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.next_hop_label.get_name_leafdata())
                            if (self.nh_mode.is_set or self.nh_mode.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.nh_mode.get_name_leafdata())
                            if (self.path_role.is_set or self.path_role.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.path_role.get_name_leafdata())
                            if (self.path_type.is_set or self.path_type.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.path_type.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "path-id" or name == "afi" or name == "backup-id" or name == "interface-name" or name == "label-type" or name == "metric" or name == "next-hop-address" or name == "next-hop-label" or name == "nh-mode" or name == "path-role" or name == "path-type"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "path-id"):
                                self.path_id = value
                                self.path_id.value_namespace = name_space
                                self.path_id.value_namespace_prefix = name_space_prefix
                            if(value_path == "afi"):
                                self.afi = value
                                self.afi.value_namespace = name_space
                                self.afi.value_namespace_prefix = name_space_prefix
                            if(value_path == "backup-id"):
                                self.backup_id = value
                                self.backup_id.value_namespace = name_space
                                self.backup_id.value_namespace_prefix = name_space_prefix
                            if(value_path == "interface-name"):
                                self.interface_name = value
                                self.interface_name.value_namespace = name_space
                                self.interface_name.value_namespace_prefix = name_space_prefix
                            if(value_path == "label-type"):
                                self.label_type = value
                                self.label_type.value_namespace = name_space
                                self.label_type.value_namespace_prefix = name_space_prefix
                            if(value_path == "metric"):
                                self.metric = value
                                self.metric.value_namespace = name_space
                                self.metric.value_namespace_prefix = name_space_prefix
                            if(value_path == "next-hop-address"):
                                self.next_hop_address = value
                                self.next_hop_address.value_namespace = name_space
                                self.next_hop_address.value_namespace_prefix = name_space_prefix
                            if(value_path == "next-hop-label"):
                                self.next_hop_label = value
                                self.next_hop_label.value_namespace = name_space
                                self.next_hop_label.value_namespace_prefix = name_space_prefix
                            if(value_path == "nh-mode"):
                                self.nh_mode = value
                                self.nh_mode.value_namespace = name_space
                                self.nh_mode.value_namespace_prefix = name_space_prefix
                            if(value_path == "path-role"):
                                self.path_role = value
                                self.path_role.value_namespace = name_space
                                self.path_role.value_namespace_prefix = name_space_prefix
                            if(value_path == "path-type"):
                                self.path_type = value
                                self.path_type.value_namespace = name_space
                                self.path_type.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.path:
                            if (c.has_data()):
                                return True
                        return False

                    def has_operation(self):
                        for c in self.path:
                            if (c.has_operation()):
                                return True
                        return self.yfilter != YFilter.not_set

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "paths" + path_buffer

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

                        if (child_yang_name == "path"):
                            for c in self.path:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = MplsStatic.DefaultVrf.LabelSwitchedPaths.LabelSwitchedPath.Paths.Path()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.path.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "path"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass

                def has_data(self):
                    return (
                        self.lsp_name.is_set or
                        self.enable.is_set or
                        (self.backup_paths is not None and self.backup_paths.has_data()) or
                        (self.in_label is not None and self.in_label.has_data()) or
                        (self.paths is not None and self.paths.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.lsp_name.yfilter != YFilter.not_set or
                        self.enable.yfilter != YFilter.not_set or
                        (self.backup_paths is not None and self.backup_paths.has_operation()) or
                        (self.in_label is not None and self.in_label.has_operation()) or
                        (self.paths is not None and self.paths.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "label-switched-path" + "[lsp-name='" + self.lsp_name.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-mpls-static-cfg:mpls-static/default-vrf/label-switched-paths/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.lsp_name.is_set or self.lsp_name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.lsp_name.get_name_leafdata())
                    if (self.enable.is_set or self.enable.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.enable.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "backup-paths"):
                        if (self.backup_paths is None):
                            self.backup_paths = MplsStatic.DefaultVrf.LabelSwitchedPaths.LabelSwitchedPath.BackupPaths()
                            self.backup_paths.parent = self
                            self._children_name_map["backup_paths"] = "backup-paths"
                        return self.backup_paths

                    if (child_yang_name == "in-label"):
                        if (self.in_label is None):
                            self.in_label = MplsStatic.DefaultVrf.LabelSwitchedPaths.LabelSwitchedPath.InLabel()
                            self.in_label.parent = self
                            self._children_name_map["in_label"] = "in-label"
                        return self.in_label

                    if (child_yang_name == "paths"):
                        if (self.paths is None):
                            self.paths = MplsStatic.DefaultVrf.LabelSwitchedPaths.LabelSwitchedPath.Paths()
                            self.paths.parent = self
                            self._children_name_map["paths"] = "paths"
                        return self.paths

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "backup-paths" or name == "in-label" or name == "paths" or name == "lsp-name" or name == "enable"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "lsp-name"):
                        self.lsp_name = value
                        self.lsp_name.value_namespace = name_space
                        self.lsp_name.value_namespace_prefix = name_space_prefix
                    if(value_path == "enable"):
                        self.enable = value
                        self.enable.value_namespace = name_space
                        self.enable.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.label_switched_path:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.label_switched_path:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "label-switched-paths" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-mpls-static-cfg:mpls-static/default-vrf/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "label-switched-path"):
                    for c in self.label_switched_path:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = MplsStatic.DefaultVrf.LabelSwitchedPaths.LabelSwitchedPath()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.label_switched_path.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "label-switched-path"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass


        class Afs(Entity):
            """
            Address Family Table
            
            .. attribute:: af
            
            	Address Family
            	**type**\: list of    :py:class:`Af <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStatic.DefaultVrf.Afs.Af>`
            
            

            """

            _prefix = 'mpls-static-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(MplsStatic.DefaultVrf.Afs, self).__init__()

                self.yang_name = "afs"
                self.yang_parent_name = "default-vrf"

                self.af = YList(self)

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
                            super(MplsStatic.DefaultVrf.Afs, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(MplsStatic.DefaultVrf.Afs, self).__setattr__(name, value)


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
                _revision = '2015-11-09'

                def __init__(self):
                    super(MplsStatic.DefaultVrf.Afs.Af, self).__init__()

                    self.yang_name = "af"
                    self.yang_parent_name = "afs"

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
                                    "enable") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(MplsStatic.DefaultVrf.Afs.Af, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(MplsStatic.DefaultVrf.Afs.Af, self).__setattr__(name, value)


                class TopLabelHash(Entity):
                    """
                    Top Label Hash
                    
                    .. attribute:: local_labels
                    
                    	Local Label
                    	**type**\:   :py:class:`LocalLabels <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStatic.DefaultVrf.Afs.Af.TopLabelHash.LocalLabels>`
                    
                    

                    """

                    _prefix = 'mpls-static-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(MplsStatic.DefaultVrf.Afs.Af.TopLabelHash, self).__init__()

                        self.yang_name = "top-label-hash"
                        self.yang_parent_name = "af"

                        self.local_labels = MplsStatic.DefaultVrf.Afs.Af.TopLabelHash.LocalLabels()
                        self.local_labels.parent = self
                        self._children_name_map["local_labels"] = "local-labels"
                        self._children_yang_names.add("local-labels")


                    class LocalLabels(Entity):
                        """
                        Local Label
                        
                        .. attribute:: local_label
                        
                        	Specify Local Label
                        	**type**\: list of    :py:class:`LocalLabel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStatic.DefaultVrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel>`
                        
                        

                        """

                        _prefix = 'mpls-static-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(MplsStatic.DefaultVrf.Afs.Af.TopLabelHash.LocalLabels, self).__init__()

                            self.yang_name = "local-labels"
                            self.yang_parent_name = "top-label-hash"

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
                                        super(MplsStatic.DefaultVrf.Afs.Af.TopLabelHash.LocalLabels, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(MplsStatic.DefaultVrf.Afs.Af.TopLabelHash.LocalLabels, self).__setattr__(name, value)


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
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(MplsStatic.DefaultVrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel, self).__init__()

                                self.yang_name = "local-label"
                                self.yang_parent_name = "local-labels"

                                self.local_label_id = YLeaf(YType.uint32, "local-label-id")

                                self.label_type = MplsStatic.DefaultVrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel.LabelType()
                                self.label_type.parent = self
                                self._children_name_map["label_type"] = "label-type"
                                self._children_yang_names.add("label-type")

                                self.paths = MplsStatic.DefaultVrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel.Paths()
                                self.paths.parent = self
                                self._children_name_map["paths"] = "paths"
                                self._children_yang_names.add("paths")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("local_label_id") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(MplsStatic.DefaultVrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(MplsStatic.DefaultVrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel, self).__setattr__(name, value)


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
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(MplsStatic.DefaultVrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel.LabelType, self).__init__()

                                    self.yang_name = "label-type"
                                    self.yang_parent_name = "local-label"

                                    self.label_mode = YLeaf(YType.enumeration, "label-mode")

                                    self.prefix = YLeaf(YType.str, "prefix")

                                    self.prefix_length = YLeaf(YType.int32, "prefix-length")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("label_mode",
                                                    "prefix",
                                                    "prefix_length") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(MplsStatic.DefaultVrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel.LabelType, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(MplsStatic.DefaultVrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel.LabelType, self).__setattr__(name, value)

                                def has_data(self):
                                    return (
                                        self.label_mode.is_set or
                                        self.prefix.is_set or
                                        self.prefix_length.is_set)

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.label_mode.yfilter != YFilter.not_set or
                                        self.prefix.yfilter != YFilter.not_set or
                                        self.prefix_length.yfilter != YFilter.not_set)

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "label-type" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.label_mode.is_set or self.label_mode.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.label_mode.get_name_leafdata())
                                    if (self.prefix.is_set or self.prefix.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.prefix.get_name_leafdata())
                                    if (self.prefix_length.is_set or self.prefix_length.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.prefix_length.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "label-mode" or name == "prefix" or name == "prefix-length"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "label-mode"):
                                        self.label_mode = value
                                        self.label_mode.value_namespace = name_space
                                        self.label_mode.value_namespace_prefix = name_space_prefix
                                    if(value_path == "prefix"):
                                        self.prefix = value
                                        self.prefix.value_namespace = name_space
                                        self.prefix.value_namespace_prefix = name_space_prefix
                                    if(value_path == "prefix-length"):
                                        self.prefix_length = value
                                        self.prefix_length.value_namespace = name_space
                                        self.prefix_length.value_namespace_prefix = name_space_prefix


                            class Paths(Entity):
                                """
                                Forward Path Parameters
                                
                                .. attribute:: path
                                
                                	Path Information
                                	**type**\: list of    :py:class:`Path <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStatic.DefaultVrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel.Paths.Path>`
                                
                                

                                """

                                _prefix = 'mpls-static-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(MplsStatic.DefaultVrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel.Paths, self).__init__()

                                    self.yang_name = "paths"
                                    self.yang_parent_name = "local-label"

                                    self.path = YList(self)

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
                                                super(MplsStatic.DefaultVrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel.Paths, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(MplsStatic.DefaultVrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel.Paths, self).__setattr__(name, value)


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
                                    
                                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                                    
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
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(MplsStatic.DefaultVrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel.Paths.Path, self).__init__()

                                        self.yang_name = "path"
                                        self.yang_parent_name = "paths"

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

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("path_id",
                                                        "afi",
                                                        "backup_id",
                                                        "interface_name",
                                                        "label_type",
                                                        "metric",
                                                        "next_hop_address",
                                                        "next_hop_label",
                                                        "nh_mode",
                                                        "path_role",
                                                        "path_type") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(MplsStatic.DefaultVrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel.Paths.Path, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(MplsStatic.DefaultVrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel.Paths.Path, self).__setattr__(name, value)

                                    def has_data(self):
                                        return (
                                            self.path_id.is_set or
                                            self.afi.is_set or
                                            self.backup_id.is_set or
                                            self.interface_name.is_set or
                                            self.label_type.is_set or
                                            self.metric.is_set or
                                            self.next_hop_address.is_set or
                                            self.next_hop_label.is_set or
                                            self.nh_mode.is_set or
                                            self.path_role.is_set or
                                            self.path_type.is_set)

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.path_id.yfilter != YFilter.not_set or
                                            self.afi.yfilter != YFilter.not_set or
                                            self.backup_id.yfilter != YFilter.not_set or
                                            self.interface_name.yfilter != YFilter.not_set or
                                            self.label_type.yfilter != YFilter.not_set or
                                            self.metric.yfilter != YFilter.not_set or
                                            self.next_hop_address.yfilter != YFilter.not_set or
                                            self.next_hop_label.yfilter != YFilter.not_set or
                                            self.nh_mode.yfilter != YFilter.not_set or
                                            self.path_role.yfilter != YFilter.not_set or
                                            self.path_type.yfilter != YFilter.not_set)

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "path" + "[path-id='" + self.path_id.get() + "']" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()
                                        if (self.path_id.is_set or self.path_id.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.path_id.get_name_leafdata())
                                        if (self.afi.is_set or self.afi.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.afi.get_name_leafdata())
                                        if (self.backup_id.is_set or self.backup_id.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.backup_id.get_name_leafdata())
                                        if (self.interface_name.is_set or self.interface_name.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.interface_name.get_name_leafdata())
                                        if (self.label_type.is_set or self.label_type.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.label_type.get_name_leafdata())
                                        if (self.metric.is_set or self.metric.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.metric.get_name_leafdata())
                                        if (self.next_hop_address.is_set or self.next_hop_address.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.next_hop_address.get_name_leafdata())
                                        if (self.next_hop_label.is_set or self.next_hop_label.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.next_hop_label.get_name_leafdata())
                                        if (self.nh_mode.is_set or self.nh_mode.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.nh_mode.get_name_leafdata())
                                        if (self.path_role.is_set or self.path_role.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.path_role.get_name_leafdata())
                                        if (self.path_type.is_set or self.path_type.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.path_type.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "path-id" or name == "afi" or name == "backup-id" or name == "interface-name" or name == "label-type" or name == "metric" or name == "next-hop-address" or name == "next-hop-label" or name == "nh-mode" or name == "path-role" or name == "path-type"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "path-id"):
                                            self.path_id = value
                                            self.path_id.value_namespace = name_space
                                            self.path_id.value_namespace_prefix = name_space_prefix
                                        if(value_path == "afi"):
                                            self.afi = value
                                            self.afi.value_namespace = name_space
                                            self.afi.value_namespace_prefix = name_space_prefix
                                        if(value_path == "backup-id"):
                                            self.backup_id = value
                                            self.backup_id.value_namespace = name_space
                                            self.backup_id.value_namespace_prefix = name_space_prefix
                                        if(value_path == "interface-name"):
                                            self.interface_name = value
                                            self.interface_name.value_namespace = name_space
                                            self.interface_name.value_namespace_prefix = name_space_prefix
                                        if(value_path == "label-type"):
                                            self.label_type = value
                                            self.label_type.value_namespace = name_space
                                            self.label_type.value_namespace_prefix = name_space_prefix
                                        if(value_path == "metric"):
                                            self.metric = value
                                            self.metric.value_namespace = name_space
                                            self.metric.value_namespace_prefix = name_space_prefix
                                        if(value_path == "next-hop-address"):
                                            self.next_hop_address = value
                                            self.next_hop_address.value_namespace = name_space
                                            self.next_hop_address.value_namespace_prefix = name_space_prefix
                                        if(value_path == "next-hop-label"):
                                            self.next_hop_label = value
                                            self.next_hop_label.value_namespace = name_space
                                            self.next_hop_label.value_namespace_prefix = name_space_prefix
                                        if(value_path == "nh-mode"):
                                            self.nh_mode = value
                                            self.nh_mode.value_namespace = name_space
                                            self.nh_mode.value_namespace_prefix = name_space_prefix
                                        if(value_path == "path-role"):
                                            self.path_role = value
                                            self.path_role.value_namespace = name_space
                                            self.path_role.value_namespace_prefix = name_space_prefix
                                        if(value_path == "path-type"):
                                            self.path_type = value
                                            self.path_type.value_namespace = name_space
                                            self.path_type.value_namespace_prefix = name_space_prefix

                                def has_data(self):
                                    for c in self.path:
                                        if (c.has_data()):
                                            return True
                                    return False

                                def has_operation(self):
                                    for c in self.path:
                                        if (c.has_operation()):
                                            return True
                                    return self.yfilter != YFilter.not_set

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "paths" + path_buffer

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

                                    if (child_yang_name == "path"):
                                        for c in self.path:
                                            segment = c.get_segment_path()
                                            if (segment_path == segment):
                                                return c
                                        c = MplsStatic.DefaultVrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel.Paths.Path()
                                        c.parent = self
                                        local_reference_key = "ydk::seg::%s" % segment_path
                                        self._local_refs[local_reference_key] = c
                                        self.path.append(c)
                                        return c

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "path"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    pass

                            def has_data(self):
                                return (
                                    self.local_label_id.is_set or
                                    (self.label_type is not None and self.label_type.has_data()) or
                                    (self.paths is not None and self.paths.has_data()))

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.local_label_id.yfilter != YFilter.not_set or
                                    (self.label_type is not None and self.label_type.has_operation()) or
                                    (self.paths is not None and self.paths.has_operation()))

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

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                if (child_yang_name == "label-type"):
                                    if (self.label_type is None):
                                        self.label_type = MplsStatic.DefaultVrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel.LabelType()
                                        self.label_type.parent = self
                                        self._children_name_map["label_type"] = "label-type"
                                    return self.label_type

                                if (child_yang_name == "paths"):
                                    if (self.paths is None):
                                        self.paths = MplsStatic.DefaultVrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel.Paths()
                                        self.paths.parent = self
                                        self._children_name_map["paths"] = "paths"
                                    return self.paths

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "label-type" or name == "paths" or name == "local-label-id"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "local-label-id"):
                                    self.local_label_id = value
                                    self.local_label_id.value_namespace = name_space
                                    self.local_label_id.value_namespace_prefix = name_space_prefix

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
                                c = MplsStatic.DefaultVrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel()
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
                        return (self.local_labels is not None and self.local_labels.has_data())

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            (self.local_labels is not None and self.local_labels.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "top-label-hash" + path_buffer

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

                        if (child_yang_name == "local-labels"):
                            if (self.local_labels is None):
                                self.local_labels = MplsStatic.DefaultVrf.Afs.Af.TopLabelHash.LocalLabels()
                                self.local_labels.parent = self
                                self._children_name_map["local_labels"] = "local-labels"
                            return self.local_labels

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "local-labels"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass


                class LocalLabels(Entity):
                    """
                    Local Label
                    
                    .. attribute:: local_label
                    
                    	Specify Local Label
                    	**type**\: list of    :py:class:`LocalLabel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStatic.DefaultVrf.Afs.Af.LocalLabels.LocalLabel>`
                    
                    

                    """

                    _prefix = 'mpls-static-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(MplsStatic.DefaultVrf.Afs.Af.LocalLabels, self).__init__()

                        self.yang_name = "local-labels"
                        self.yang_parent_name = "af"

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
                                    super(MplsStatic.DefaultVrf.Afs.Af.LocalLabels, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(MplsStatic.DefaultVrf.Afs.Af.LocalLabels, self).__setattr__(name, value)


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
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(MplsStatic.DefaultVrf.Afs.Af.LocalLabels.LocalLabel, self).__init__()

                            self.yang_name = "local-label"
                            self.yang_parent_name = "local-labels"

                            self.local_label_id = YLeaf(YType.uint32, "local-label-id")

                            self.label_type = MplsStatic.DefaultVrf.Afs.Af.LocalLabels.LocalLabel.LabelType()
                            self.label_type.parent = self
                            self._children_name_map["label_type"] = "label-type"
                            self._children_yang_names.add("label-type")

                            self.paths = MplsStatic.DefaultVrf.Afs.Af.LocalLabels.LocalLabel.Paths()
                            self.paths.parent = self
                            self._children_name_map["paths"] = "paths"
                            self._children_yang_names.add("paths")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("local_label_id") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(MplsStatic.DefaultVrf.Afs.Af.LocalLabels.LocalLabel, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(MplsStatic.DefaultVrf.Afs.Af.LocalLabels.LocalLabel, self).__setattr__(name, value)


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
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(MplsStatic.DefaultVrf.Afs.Af.LocalLabels.LocalLabel.LabelType, self).__init__()

                                self.yang_name = "label-type"
                                self.yang_parent_name = "local-label"

                                self.label_mode = YLeaf(YType.enumeration, "label-mode")

                                self.prefix = YLeaf(YType.str, "prefix")

                                self.prefix_length = YLeaf(YType.int32, "prefix-length")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("label_mode",
                                                "prefix",
                                                "prefix_length") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(MplsStatic.DefaultVrf.Afs.Af.LocalLabels.LocalLabel.LabelType, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(MplsStatic.DefaultVrf.Afs.Af.LocalLabels.LocalLabel.LabelType, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.label_mode.is_set or
                                    self.prefix.is_set or
                                    self.prefix_length.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.label_mode.yfilter != YFilter.not_set or
                                    self.prefix.yfilter != YFilter.not_set or
                                    self.prefix_length.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "label-type" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.label_mode.is_set or self.label_mode.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.label_mode.get_name_leafdata())
                                if (self.prefix.is_set or self.prefix.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.prefix.get_name_leafdata())
                                if (self.prefix_length.is_set or self.prefix_length.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.prefix_length.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "label-mode" or name == "prefix" or name == "prefix-length"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "label-mode"):
                                    self.label_mode = value
                                    self.label_mode.value_namespace = name_space
                                    self.label_mode.value_namespace_prefix = name_space_prefix
                                if(value_path == "prefix"):
                                    self.prefix = value
                                    self.prefix.value_namespace = name_space
                                    self.prefix.value_namespace_prefix = name_space_prefix
                                if(value_path == "prefix-length"):
                                    self.prefix_length = value
                                    self.prefix_length.value_namespace = name_space
                                    self.prefix_length.value_namespace_prefix = name_space_prefix


                        class Paths(Entity):
                            """
                            Forward Path Parameters
                            
                            .. attribute:: path
                            
                            	Path Information
                            	**type**\: list of    :py:class:`Path <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStatic.DefaultVrf.Afs.Af.LocalLabels.LocalLabel.Paths.Path>`
                            
                            

                            """

                            _prefix = 'mpls-static-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(MplsStatic.DefaultVrf.Afs.Af.LocalLabels.LocalLabel.Paths, self).__init__()

                                self.yang_name = "paths"
                                self.yang_parent_name = "local-label"

                                self.path = YList(self)

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
                                            super(MplsStatic.DefaultVrf.Afs.Af.LocalLabels.LocalLabel.Paths, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(MplsStatic.DefaultVrf.Afs.Af.LocalLabels.LocalLabel.Paths, self).__setattr__(name, value)


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
                                
                                	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                                
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
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(MplsStatic.DefaultVrf.Afs.Af.LocalLabels.LocalLabel.Paths.Path, self).__init__()

                                    self.yang_name = "path"
                                    self.yang_parent_name = "paths"

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

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("path_id",
                                                    "afi",
                                                    "backup_id",
                                                    "interface_name",
                                                    "label_type",
                                                    "metric",
                                                    "next_hop_address",
                                                    "next_hop_label",
                                                    "nh_mode",
                                                    "path_role",
                                                    "path_type") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(MplsStatic.DefaultVrf.Afs.Af.LocalLabels.LocalLabel.Paths.Path, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(MplsStatic.DefaultVrf.Afs.Af.LocalLabels.LocalLabel.Paths.Path, self).__setattr__(name, value)

                                def has_data(self):
                                    return (
                                        self.path_id.is_set or
                                        self.afi.is_set or
                                        self.backup_id.is_set or
                                        self.interface_name.is_set or
                                        self.label_type.is_set or
                                        self.metric.is_set or
                                        self.next_hop_address.is_set or
                                        self.next_hop_label.is_set or
                                        self.nh_mode.is_set or
                                        self.path_role.is_set or
                                        self.path_type.is_set)

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.path_id.yfilter != YFilter.not_set or
                                        self.afi.yfilter != YFilter.not_set or
                                        self.backup_id.yfilter != YFilter.not_set or
                                        self.interface_name.yfilter != YFilter.not_set or
                                        self.label_type.yfilter != YFilter.not_set or
                                        self.metric.yfilter != YFilter.not_set or
                                        self.next_hop_address.yfilter != YFilter.not_set or
                                        self.next_hop_label.yfilter != YFilter.not_set or
                                        self.nh_mode.yfilter != YFilter.not_set or
                                        self.path_role.yfilter != YFilter.not_set or
                                        self.path_type.yfilter != YFilter.not_set)

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "path" + "[path-id='" + self.path_id.get() + "']" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.path_id.is_set or self.path_id.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.path_id.get_name_leafdata())
                                    if (self.afi.is_set or self.afi.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.afi.get_name_leafdata())
                                    if (self.backup_id.is_set or self.backup_id.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.backup_id.get_name_leafdata())
                                    if (self.interface_name.is_set or self.interface_name.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.interface_name.get_name_leafdata())
                                    if (self.label_type.is_set or self.label_type.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.label_type.get_name_leafdata())
                                    if (self.metric.is_set or self.metric.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.metric.get_name_leafdata())
                                    if (self.next_hop_address.is_set or self.next_hop_address.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.next_hop_address.get_name_leafdata())
                                    if (self.next_hop_label.is_set or self.next_hop_label.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.next_hop_label.get_name_leafdata())
                                    if (self.nh_mode.is_set or self.nh_mode.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.nh_mode.get_name_leafdata())
                                    if (self.path_role.is_set or self.path_role.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.path_role.get_name_leafdata())
                                    if (self.path_type.is_set or self.path_type.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.path_type.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "path-id" or name == "afi" or name == "backup-id" or name == "interface-name" or name == "label-type" or name == "metric" or name == "next-hop-address" or name == "next-hop-label" or name == "nh-mode" or name == "path-role" or name == "path-type"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "path-id"):
                                        self.path_id = value
                                        self.path_id.value_namespace = name_space
                                        self.path_id.value_namespace_prefix = name_space_prefix
                                    if(value_path == "afi"):
                                        self.afi = value
                                        self.afi.value_namespace = name_space
                                        self.afi.value_namespace_prefix = name_space_prefix
                                    if(value_path == "backup-id"):
                                        self.backup_id = value
                                        self.backup_id.value_namespace = name_space
                                        self.backup_id.value_namespace_prefix = name_space_prefix
                                    if(value_path == "interface-name"):
                                        self.interface_name = value
                                        self.interface_name.value_namespace = name_space
                                        self.interface_name.value_namespace_prefix = name_space_prefix
                                    if(value_path == "label-type"):
                                        self.label_type = value
                                        self.label_type.value_namespace = name_space
                                        self.label_type.value_namespace_prefix = name_space_prefix
                                    if(value_path == "metric"):
                                        self.metric = value
                                        self.metric.value_namespace = name_space
                                        self.metric.value_namespace_prefix = name_space_prefix
                                    if(value_path == "next-hop-address"):
                                        self.next_hop_address = value
                                        self.next_hop_address.value_namespace = name_space
                                        self.next_hop_address.value_namespace_prefix = name_space_prefix
                                    if(value_path == "next-hop-label"):
                                        self.next_hop_label = value
                                        self.next_hop_label.value_namespace = name_space
                                        self.next_hop_label.value_namespace_prefix = name_space_prefix
                                    if(value_path == "nh-mode"):
                                        self.nh_mode = value
                                        self.nh_mode.value_namespace = name_space
                                        self.nh_mode.value_namespace_prefix = name_space_prefix
                                    if(value_path == "path-role"):
                                        self.path_role = value
                                        self.path_role.value_namespace = name_space
                                        self.path_role.value_namespace_prefix = name_space_prefix
                                    if(value_path == "path-type"):
                                        self.path_type = value
                                        self.path_type.value_namespace = name_space
                                        self.path_type.value_namespace_prefix = name_space_prefix

                            def has_data(self):
                                for c in self.path:
                                    if (c.has_data()):
                                        return True
                                return False

                            def has_operation(self):
                                for c in self.path:
                                    if (c.has_operation()):
                                        return True
                                return self.yfilter != YFilter.not_set

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "paths" + path_buffer

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

                                if (child_yang_name == "path"):
                                    for c in self.path:
                                        segment = c.get_segment_path()
                                        if (segment_path == segment):
                                            return c
                                    c = MplsStatic.DefaultVrf.Afs.Af.LocalLabels.LocalLabel.Paths.Path()
                                    c.parent = self
                                    local_reference_key = "ydk::seg::%s" % segment_path
                                    self._local_refs[local_reference_key] = c
                                    self.path.append(c)
                                    return c

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "path"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                pass

                        def has_data(self):
                            return (
                                self.local_label_id.is_set or
                                (self.label_type is not None and self.label_type.has_data()) or
                                (self.paths is not None and self.paths.has_data()))

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.local_label_id.yfilter != YFilter.not_set or
                                (self.label_type is not None and self.label_type.has_operation()) or
                                (self.paths is not None and self.paths.has_operation()))

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

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "label-type"):
                                if (self.label_type is None):
                                    self.label_type = MplsStatic.DefaultVrf.Afs.Af.LocalLabels.LocalLabel.LabelType()
                                    self.label_type.parent = self
                                    self._children_name_map["label_type"] = "label-type"
                                return self.label_type

                            if (child_yang_name == "paths"):
                                if (self.paths is None):
                                    self.paths = MplsStatic.DefaultVrf.Afs.Af.LocalLabels.LocalLabel.Paths()
                                    self.paths.parent = self
                                    self._children_name_map["paths"] = "paths"
                                return self.paths

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "label-type" or name == "paths" or name == "local-label-id"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "local-label-id"):
                                self.local_label_id = value
                                self.local_label_id.value_namespace = name_space
                                self.local_label_id.value_namespace_prefix = name_space_prefix

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
                            c = MplsStatic.DefaultVrf.Afs.Af.LocalLabels.LocalLabel()
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
                        self.afi.is_set or
                        self.enable.is_set or
                        (self.local_labels is not None and self.local_labels.has_data()) or
                        (self.top_label_hash is not None and self.top_label_hash.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.afi.yfilter != YFilter.not_set or
                        self.enable.yfilter != YFilter.not_set or
                        (self.local_labels is not None and self.local_labels.has_operation()) or
                        (self.top_label_hash is not None and self.top_label_hash.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "af" + "[afi='" + self.afi.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-mpls-static-cfg:mpls-static/default-vrf/afs/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.afi.is_set or self.afi.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.afi.get_name_leafdata())
                    if (self.enable.is_set or self.enable.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.enable.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "local-labels"):
                        if (self.local_labels is None):
                            self.local_labels = MplsStatic.DefaultVrf.Afs.Af.LocalLabels()
                            self.local_labels.parent = self
                            self._children_name_map["local_labels"] = "local-labels"
                        return self.local_labels

                    if (child_yang_name == "top-label-hash"):
                        if (self.top_label_hash is None):
                            self.top_label_hash = MplsStatic.DefaultVrf.Afs.Af.TopLabelHash()
                            self.top_label_hash.parent = self
                            self._children_name_map["top_label_hash"] = "top-label-hash"
                        return self.top_label_hash

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "local-labels" or name == "top-label-hash" or name == "afi" or name == "enable"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "afi"):
                        self.afi = value
                        self.afi.value_namespace = name_space
                        self.afi.value_namespace_prefix = name_space_prefix
                    if(value_path == "enable"):
                        self.enable = value
                        self.enable.value_namespace = name_space
                        self.enable.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.af:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.af:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "afs" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-mpls-static-cfg:mpls-static/default-vrf/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "af"):
                    for c in self.af:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = MplsStatic.DefaultVrf.Afs.Af()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.af.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "af"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass

        def has_data(self):
            return (
                self.enable.is_set or
                (self.afs is not None and self.afs.has_data()) or
                (self.label_switched_paths is not None and self.label_switched_paths.has_data()))

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.enable.yfilter != YFilter.not_set or
                (self.afs is not None and self.afs.has_operation()) or
                (self.label_switched_paths is not None and self.label_switched_paths.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "default-vrf" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-mpls-static-cfg:mpls-static/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.enable.is_set or self.enable.yfilter != YFilter.not_set):
                leaf_name_data.append(self.enable.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "afs"):
                if (self.afs is None):
                    self.afs = MplsStatic.DefaultVrf.Afs()
                    self.afs.parent = self
                    self._children_name_map["afs"] = "afs"
                return self.afs

            if (child_yang_name == "label-switched-paths"):
                if (self.label_switched_paths is None):
                    self.label_switched_paths = MplsStatic.DefaultVrf.LabelSwitchedPaths()
                    self.label_switched_paths.parent = self
                    self._children_name_map["label_switched_paths"] = "label-switched-paths"
                return self.label_switched_paths

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "afs" or name == "label-switched-paths" or name == "enable"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "enable"):
                self.enable = value
                self.enable.value_namespace = name_space
                self.enable.value_namespace_prefix = name_space_prefix

    def has_data(self):
        return (
            self.enable.is_set or
            (self.default_vrf is not None and self.default_vrf.has_data()) or
            (self.interfaces is not None and self.interfaces.has_data()) or
            (self.vrfs is not None and self.vrfs.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            self.enable.yfilter != YFilter.not_set or
            (self.default_vrf is not None and self.default_vrf.has_operation()) or
            (self.interfaces is not None and self.interfaces.has_operation()) or
            (self.vrfs is not None and self.vrfs.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-mpls-static-cfg:mpls-static" + path_buffer

        return path_buffer

    def get_entity_path(self, ancestor):
        path_buffer = ""
        if (not ancestor is None):
            raise YPYModelError("ancestor has to be None for top-level node")

        path_buffer = self.get_segment_path()
        leaf_name_data = LeafDataList()
        if (self.enable.is_set or self.enable.yfilter != YFilter.not_set):
            leaf_name_data.append(self.enable.get_name_leafdata())

        entity_path = EntityPath(path_buffer, leaf_name_data)
        return entity_path

    def get_child_by_name(self, child_yang_name, segment_path):
        child = self._get_child_by_seg_name([child_yang_name, segment_path])
        if child is not None:
            return child

        if (child_yang_name == "default-vrf"):
            if (self.default_vrf is None):
                self.default_vrf = MplsStatic.DefaultVrf()
                self.default_vrf.parent = self
                self._children_name_map["default_vrf"] = "default-vrf"
            return self.default_vrf

        if (child_yang_name == "interfaces"):
            if (self.interfaces is None):
                self.interfaces = MplsStatic.Interfaces()
                self.interfaces.parent = self
                self._children_name_map["interfaces"] = "interfaces"
            return self.interfaces

        if (child_yang_name == "vrfs"):
            if (self.vrfs is None):
                self.vrfs = MplsStatic.Vrfs()
                self.vrfs.parent = self
                self._children_name_map["vrfs"] = "vrfs"
            return self.vrfs

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "default-vrf" or name == "interfaces" or name == "vrfs" or name == "enable"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        if(value_path == "enable"):
            self.enable = value
            self.enable.value_namespace = name_space
            self.enable.value_namespace_prefix = name_space_prefix

    def clone_ptr(self):
        self._top_entity = MplsStatic()
        return self._top_entity

