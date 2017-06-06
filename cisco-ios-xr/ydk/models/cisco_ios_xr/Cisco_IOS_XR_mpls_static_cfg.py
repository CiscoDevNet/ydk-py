""" Cisco_IOS_XR_mpls_static_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR mpls\-static package configuration.

This module contains definitions
for the following management objects\:
  mpls\-static\: MPLS Static Configuration Data

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class MplsStaticAddressFamilyEnum(Enum):
    """
    MplsStaticAddressFamilyEnum

    Mpls static address family

    .. data:: ipv4_unicast = 1

    	IPv4 Unicast

    """

    ipv4_unicast = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_static_cfg as meta
        return meta._meta_table['MplsStaticAddressFamilyEnum']


class MplsStaticLabelModeEnum(Enum):
    """
    MplsStaticLabelModeEnum

    Mpls static label mode

    .. data:: per_vrf = 1

    	Per VRF

    .. data:: per_prefix = 2

    	Per Prefix

    .. data:: lsp = 3

    	Cross connect

    """

    per_vrf = 1

    per_prefix = 2

    lsp = 3


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_static_cfg as meta
        return meta._meta_table['MplsStaticLabelModeEnum']


class MplsStaticNhAddressFamilyEnum(Enum):
    """
    MplsStaticNhAddressFamilyEnum

    Mpls static nh address family

    .. data:: ipv4 = 1

    	IPv4 Next Hop

    .. data:: ipv6 = 2

    	IPv6 Next Hop

    """

    ipv4 = 1

    ipv6 = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_static_cfg as meta
        return meta._meta_table['MplsStaticNhAddressFamilyEnum']


class MplsStaticNhModeEnum(Enum):
    """
    MplsStaticNhModeEnum

    Mpls static nh mode

    .. data:: configured = 0

    	Explicitly configured next hop path

    .. data:: resolve = 1

    	Resolvable next hop which will result in a path

    	set

    """

    configured = 0

    resolve = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_static_cfg as meta
        return meta._meta_table['MplsStaticNhModeEnum']


class MplsStaticOutLabelTypesEnum(Enum):
    """
    MplsStaticOutLabelTypesEnum

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

    none = 0

    out_label = 1

    pop = 2

    exp_null = 3

    ipv6_explicit_null = 4


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_static_cfg as meta
        return meta._meta_table['MplsStaticOutLabelTypesEnum']


class MplsStaticPathEnum(Enum):
    """
    MplsStaticPathEnum

    Mpls static path

    .. data:: pop_and_lookup = 1

    	Pop and Lookup

    .. data:: cross_connect = 2

    	Crossconnect

    """

    pop_and_lookup = 1

    cross_connect = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_static_cfg as meta
        return meta._meta_table['MplsStaticPathEnum']


class MplsStaticPathRoleEnum(Enum):
    """
    MplsStaticPathRoleEnum

    Mpls static path role

    .. data:: primary = 0

    	Path is only for primary traffic

    .. data:: backup = 1

    	Path is only for backup traffic

    .. data:: primary_backup = 2

    	Path is for primary and backup traffic

    """

    primary = 0

    backup = 1

    primary_backup = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_static_cfg as meta
        return meta._meta_table['MplsStaticPathRoleEnum']



class MplsStatic(object):
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
        self.default_vrf = MplsStatic.DefaultVrf()
        self.default_vrf.parent = self
        self.enable = None
        self.interfaces = MplsStatic.Interfaces()
        self.interfaces.parent = self
        self.vrfs = MplsStatic.Vrfs()
        self.vrfs.parent = self


    class Vrfs(object):
        """
        VRF table
        
        .. attribute:: vrf
        
        	VRF Name
        	**type**\: list of    :py:class:`Vrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStatic.Vrfs.Vrf>`
        
        

        """

        _prefix = 'mpls-static-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.vrf = YList()
            self.vrf.parent = self
            self.vrf.name = 'vrf'


        class Vrf(object):
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
                self.parent = None
                self.vrf_name = None
                self.afs = MplsStatic.Vrfs.Vrf.Afs()
                self.afs.parent = self
                self.enable = None
                self.label_switched_paths = MplsStatic.Vrfs.Vrf.LabelSwitchedPaths()
                self.label_switched_paths.parent = self


            class LabelSwitchedPaths(object):
                """
                Table of the Label Switched Paths
                
                .. attribute:: label_switched_path
                
                	Label Switched Path
                	**type**\: list of    :py:class:`LabelSwitchedPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStatic.Vrfs.Vrf.LabelSwitchedPaths.LabelSwitchedPath>`
                
                

                """

                _prefix = 'mpls-static-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.label_switched_path = YList()
                    self.label_switched_path.parent = self
                    self.label_switched_path.name = 'label_switched_path'


                class LabelSwitchedPath(object):
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
                        self.parent = None
                        self.lsp_name = None
                        self.backup_paths = MplsStatic.Vrfs.Vrf.LabelSwitchedPaths.LabelSwitchedPath.BackupPaths()
                        self.backup_paths.parent = self
                        self.enable = None
                        self.in_label = MplsStatic.Vrfs.Vrf.LabelSwitchedPaths.LabelSwitchedPath.InLabel()
                        self.in_label.parent = self
                        self.paths = MplsStatic.Vrfs.Vrf.LabelSwitchedPaths.LabelSwitchedPath.Paths()
                        self.paths.parent = self


                    class BackupPaths(object):
                        """
                        Backup Path Parameters
                        
                        .. attribute:: path
                        
                        	Path Information
                        	**type**\: list of    :py:class:`Path <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStatic.Vrfs.Vrf.LabelSwitchedPaths.LabelSwitchedPath.BackupPaths.Path>`
                        
                        

                        """

                        _prefix = 'mpls-static-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.path = YList()
                            self.path.parent = self
                            self.path.name = 'path'


                        class Path(object):
                            """
                            Path Information
                            
                            .. attribute:: path_id  <key>
                            
                            	Number of paths
                            	**type**\:  int
                            
                            	**range:** 1..16
                            
                            .. attribute:: afi
                            
                            	Next hop Address Family
                            	**type**\:   :py:class:`MplsStaticNhAddressFamilyEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStaticNhAddressFamilyEnum>`
                            
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
                            	**type**\:   :py:class:`MplsStaticOutLabelTypesEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStaticOutLabelTypesEnum>`
                            
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
                            	**type**\:   :py:class:`MplsStaticNhModeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStaticNhModeEnum>`
                            
                            	**default value**\: configured
                            
                            .. attribute:: path_role
                            
                            	Path Role
                            	**type**\:   :py:class:`MplsStaticPathRoleEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStaticPathRoleEnum>`
                            
                            	**default value**\: primary
                            
                            .. attribute:: path_type
                            
                            	Type of Path (PopAndLookup, CrossConnect)
                            	**type**\:   :py:class:`MplsStaticPathEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStaticPathEnum>`
                            
                            	**default value**\: cross-connect
                            
                            

                            """

                            _prefix = 'mpls-static-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.path_id = None
                                self.afi = None
                                self.backup_id = None
                                self.interface_name = None
                                self.label_type = None
                                self.metric = None
                                self.next_hop_address = None
                                self.next_hop_label = None
                                self.nh_mode = None
                                self.path_role = None
                                self.path_type = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                if self.path_id is None:
                                    raise YPYModelError('Key property path_id is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-mpls-static-cfg:path[Cisco-IOS-XR-mpls-static-cfg:path-id = ' + str(self.path_id) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.path_id is not None:
                                    return True

                                if self.afi is not None:
                                    return True

                                if self.backup_id is not None:
                                    return True

                                if self.interface_name is not None:
                                    return True

                                if self.label_type is not None:
                                    return True

                                if self.metric is not None:
                                    return True

                                if self.next_hop_address is not None:
                                    return True

                                if self.next_hop_label is not None:
                                    return True

                                if self.nh_mode is not None:
                                    return True

                                if self.path_role is not None:
                                    return True

                                if self.path_type is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_static_cfg as meta
                                return meta._meta_table['MplsStatic.Vrfs.Vrf.LabelSwitchedPaths.LabelSwitchedPath.BackupPaths.Path']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-mpls-static-cfg:backup-paths'

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
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_static_cfg as meta
                            return meta._meta_table['MplsStatic.Vrfs.Vrf.LabelSwitchedPaths.LabelSwitchedPath.BackupPaths']['meta_info']


                    class InLabel(object):
                        """
                        MPLS Static Local Label Value
                        
                        .. attribute:: in_label_value
                        
                        	Local Label
                        	**type**\:  int
                        
                        	**range:** 16..1048575
                        
                        .. attribute:: label_mode
                        
                        	Label Mode (PerVRF, PerPrefix or LSP)
                        	**type**\:   :py:class:`MplsStaticLabelModeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStaticLabelModeEnum>`
                        
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
                            self.parent = None
                            self.in_label_value = None
                            self.label_mode = None
                            self.prefix = None
                            self.prefix_length = None
                            self.tlh_mode = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-mpls-static-cfg:in-label'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.in_label_value is not None:
                                return True

                            if self.label_mode is not None:
                                return True

                            if self.prefix is not None:
                                return True

                            if self.prefix_length is not None:
                                return True

                            if self.tlh_mode is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_static_cfg as meta
                            return meta._meta_table['MplsStatic.Vrfs.Vrf.LabelSwitchedPaths.LabelSwitchedPath.InLabel']['meta_info']


                    class Paths(object):
                        """
                        Forward Path Parameters
                        
                        .. attribute:: path
                        
                        	Path Information
                        	**type**\: list of    :py:class:`Path <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStatic.Vrfs.Vrf.LabelSwitchedPaths.LabelSwitchedPath.Paths.Path>`
                        
                        

                        """

                        _prefix = 'mpls-static-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.path = YList()
                            self.path.parent = self
                            self.path.name = 'path'


                        class Path(object):
                            """
                            Path Information
                            
                            .. attribute:: path_id  <key>
                            
                            	Number of paths
                            	**type**\:  int
                            
                            	**range:** 1..16
                            
                            .. attribute:: afi
                            
                            	Next hop Address Family
                            	**type**\:   :py:class:`MplsStaticNhAddressFamilyEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStaticNhAddressFamilyEnum>`
                            
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
                            	**type**\:   :py:class:`MplsStaticOutLabelTypesEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStaticOutLabelTypesEnum>`
                            
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
                            	**type**\:   :py:class:`MplsStaticNhModeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStaticNhModeEnum>`
                            
                            	**default value**\: configured
                            
                            .. attribute:: path_role
                            
                            	Path Role
                            	**type**\:   :py:class:`MplsStaticPathRoleEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStaticPathRoleEnum>`
                            
                            	**default value**\: primary
                            
                            .. attribute:: path_type
                            
                            	Type of Path (PopAndLookup, CrossConnect)
                            	**type**\:   :py:class:`MplsStaticPathEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStaticPathEnum>`
                            
                            	**default value**\: cross-connect
                            
                            

                            """

                            _prefix = 'mpls-static-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.path_id = None
                                self.afi = None
                                self.backup_id = None
                                self.interface_name = None
                                self.label_type = None
                                self.metric = None
                                self.next_hop_address = None
                                self.next_hop_label = None
                                self.nh_mode = None
                                self.path_role = None
                                self.path_type = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                if self.path_id is None:
                                    raise YPYModelError('Key property path_id is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-mpls-static-cfg:path[Cisco-IOS-XR-mpls-static-cfg:path-id = ' + str(self.path_id) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.path_id is not None:
                                    return True

                                if self.afi is not None:
                                    return True

                                if self.backup_id is not None:
                                    return True

                                if self.interface_name is not None:
                                    return True

                                if self.label_type is not None:
                                    return True

                                if self.metric is not None:
                                    return True

                                if self.next_hop_address is not None:
                                    return True

                                if self.next_hop_label is not None:
                                    return True

                                if self.nh_mode is not None:
                                    return True

                                if self.path_role is not None:
                                    return True

                                if self.path_type is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_static_cfg as meta
                                return meta._meta_table['MplsStatic.Vrfs.Vrf.LabelSwitchedPaths.LabelSwitchedPath.Paths.Path']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-mpls-static-cfg:paths'

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
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_static_cfg as meta
                            return meta._meta_table['MplsStatic.Vrfs.Vrf.LabelSwitchedPaths.LabelSwitchedPath.Paths']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.lsp_name is None:
                            raise YPYModelError('Key property lsp_name is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-mpls-static-cfg:label-switched-path[Cisco-IOS-XR-mpls-static-cfg:lsp-name = ' + str(self.lsp_name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.lsp_name is not None:
                            return True

                        if self.backup_paths is not None and self.backup_paths._has_data():
                            return True

                        if self.enable is not None:
                            return True

                        if self.in_label is not None and self.in_label._has_data():
                            return True

                        if self.paths is not None and self.paths._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_static_cfg as meta
                        return meta._meta_table['MplsStatic.Vrfs.Vrf.LabelSwitchedPaths.LabelSwitchedPath']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-mpls-static-cfg:label-switched-paths'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.label_switched_path is not None:
                        for child_ref in self.label_switched_path:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_static_cfg as meta
                    return meta._meta_table['MplsStatic.Vrfs.Vrf.LabelSwitchedPaths']['meta_info']


            class Afs(object):
                """
                Address Family Table
                
                .. attribute:: af
                
                	Address Family
                	**type**\: list of    :py:class:`Af <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStatic.Vrfs.Vrf.Afs.Af>`
                
                

                """

                _prefix = 'mpls-static-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.af = YList()
                    self.af.parent = self
                    self.af.name = 'af'


                class Af(object):
                    """
                    Address Family
                    
                    .. attribute:: afi  <key>
                    
                    	Address Family
                    	**type**\:   :py:class:`MplsStaticAddressFamilyEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStaticAddressFamilyEnum>`
                    
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
                        self.parent = None
                        self.afi = None
                        self.enable = None
                        self.local_labels = MplsStatic.Vrfs.Vrf.Afs.Af.LocalLabels()
                        self.local_labels.parent = self
                        self.top_label_hash = MplsStatic.Vrfs.Vrf.Afs.Af.TopLabelHash()
                        self.top_label_hash.parent = self


                    class TopLabelHash(object):
                        """
                        Top Label Hash
                        
                        .. attribute:: local_labels
                        
                        	Local Label
                        	**type**\:   :py:class:`LocalLabels <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStatic.Vrfs.Vrf.Afs.Af.TopLabelHash.LocalLabels>`
                        
                        

                        """

                        _prefix = 'mpls-static-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.local_labels = MplsStatic.Vrfs.Vrf.Afs.Af.TopLabelHash.LocalLabels()
                            self.local_labels.parent = self


                        class LocalLabels(object):
                            """
                            Local Label
                            
                            .. attribute:: local_label
                            
                            	Specify Local Label
                            	**type**\: list of    :py:class:`LocalLabel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStatic.Vrfs.Vrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel>`
                            
                            

                            """

                            _prefix = 'mpls-static-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.local_label = YList()
                                self.local_label.parent = self
                                self.local_label.name = 'local_label'


                            class LocalLabel(object):
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
                                    self.parent = None
                                    self.local_label_id = None
                                    self.label_type = MplsStatic.Vrfs.Vrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel.LabelType()
                                    self.label_type.parent = self
                                    self.paths = MplsStatic.Vrfs.Vrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel.Paths()
                                    self.paths.parent = self


                                class LabelType(object):
                                    """
                                    MPLS Static Local Label Value
                                    
                                    .. attribute:: label_mode
                                    
                                    	Label Mode (PerVRF, PerPrefix or LSP)
                                    	**type**\:   :py:class:`MplsStaticLabelModeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStaticLabelModeEnum>`
                                    
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
                                        self.parent = None
                                        self.label_mode = None
                                        self.prefix = None
                                        self.prefix_length = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-mpls-static-cfg:label-type'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if self.label_mode is not None:
                                            return True

                                        if self.prefix is not None:
                                            return True

                                        if self.prefix_length is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_static_cfg as meta
                                        return meta._meta_table['MplsStatic.Vrfs.Vrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel.LabelType']['meta_info']


                                class Paths(object):
                                    """
                                    Forward Path Parameters
                                    
                                    .. attribute:: path
                                    
                                    	Path Information
                                    	**type**\: list of    :py:class:`Path <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStatic.Vrfs.Vrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel.Paths.Path>`
                                    
                                    

                                    """

                                    _prefix = 'mpls-static-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.path = YList()
                                        self.path.parent = self
                                        self.path.name = 'path'


                                    class Path(object):
                                        """
                                        Path Information
                                        
                                        .. attribute:: path_id  <key>
                                        
                                        	Number of paths
                                        	**type**\:  int
                                        
                                        	**range:** 1..16
                                        
                                        .. attribute:: afi
                                        
                                        	Next hop Address Family
                                        	**type**\:   :py:class:`MplsStaticNhAddressFamilyEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStaticNhAddressFamilyEnum>`
                                        
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
                                        	**type**\:   :py:class:`MplsStaticOutLabelTypesEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStaticOutLabelTypesEnum>`
                                        
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
                                        	**type**\:   :py:class:`MplsStaticNhModeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStaticNhModeEnum>`
                                        
                                        	**default value**\: configured
                                        
                                        .. attribute:: path_role
                                        
                                        	Path Role
                                        	**type**\:   :py:class:`MplsStaticPathRoleEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStaticPathRoleEnum>`
                                        
                                        	**default value**\: primary
                                        
                                        .. attribute:: path_type
                                        
                                        	Type of Path (PopAndLookup, CrossConnect)
                                        	**type**\:   :py:class:`MplsStaticPathEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStaticPathEnum>`
                                        
                                        	**default value**\: cross-connect
                                        
                                        

                                        """

                                        _prefix = 'mpls-static-cfg'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.path_id = None
                                            self.afi = None
                                            self.backup_id = None
                                            self.interface_name = None
                                            self.label_type = None
                                            self.metric = None
                                            self.next_hop_address = None
                                            self.next_hop_label = None
                                            self.nh_mode = None
                                            self.path_role = None
                                            self.path_type = None

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')
                                            if self.path_id is None:
                                                raise YPYModelError('Key property path_id is None')

                                            return self.parent._common_path +'/Cisco-IOS-XR-mpls-static-cfg:path[Cisco-IOS-XR-mpls-static-cfg:path-id = ' + str(self.path_id) + ']'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return True

                                        def _has_data(self):
                                            if self.path_id is not None:
                                                return True

                                            if self.afi is not None:
                                                return True

                                            if self.backup_id is not None:
                                                return True

                                            if self.interface_name is not None:
                                                return True

                                            if self.label_type is not None:
                                                return True

                                            if self.metric is not None:
                                                return True

                                            if self.next_hop_address is not None:
                                                return True

                                            if self.next_hop_label is not None:
                                                return True

                                            if self.nh_mode is not None:
                                                return True

                                            if self.path_role is not None:
                                                return True

                                            if self.path_type is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_static_cfg as meta
                                            return meta._meta_table['MplsStatic.Vrfs.Vrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel.Paths.Path']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-mpls-static-cfg:paths'

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
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_static_cfg as meta
                                        return meta._meta_table['MplsStatic.Vrfs.Vrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel.Paths']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')
                                    if self.local_label_id is None:
                                        raise YPYModelError('Key property local_label_id is None')

                                    return self.parent._common_path +'/Cisco-IOS-XR-mpls-static-cfg:local-label[Cisco-IOS-XR-mpls-static-cfg:local-label-id = ' + str(self.local_label_id) + ']'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.local_label_id is not None:
                                        return True

                                    if self.label_type is not None and self.label_type._has_data():
                                        return True

                                    if self.paths is not None and self.paths._has_data():
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_static_cfg as meta
                                    return meta._meta_table['MplsStatic.Vrfs.Vrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-mpls-static-cfg:local-labels'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.local_label is not None:
                                    for child_ref in self.local_label:
                                        if child_ref._has_data():
                                            return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_static_cfg as meta
                                return meta._meta_table['MplsStatic.Vrfs.Vrf.Afs.Af.TopLabelHash.LocalLabels']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-mpls-static-cfg:top-label-hash'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.local_labels is not None and self.local_labels._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_static_cfg as meta
                            return meta._meta_table['MplsStatic.Vrfs.Vrf.Afs.Af.TopLabelHash']['meta_info']


                    class LocalLabels(object):
                        """
                        Local Label
                        
                        .. attribute:: local_label
                        
                        	Specify Local Label
                        	**type**\: list of    :py:class:`LocalLabel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStatic.Vrfs.Vrf.Afs.Af.LocalLabels.LocalLabel>`
                        
                        

                        """

                        _prefix = 'mpls-static-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.local_label = YList()
                            self.local_label.parent = self
                            self.local_label.name = 'local_label'


                        class LocalLabel(object):
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
                                self.parent = None
                                self.local_label_id = None
                                self.label_type = MplsStatic.Vrfs.Vrf.Afs.Af.LocalLabels.LocalLabel.LabelType()
                                self.label_type.parent = self
                                self.paths = MplsStatic.Vrfs.Vrf.Afs.Af.LocalLabels.LocalLabel.Paths()
                                self.paths.parent = self


                            class LabelType(object):
                                """
                                MPLS Static Local Label Value
                                
                                .. attribute:: label_mode
                                
                                	Label Mode (PerVRF, PerPrefix or LSP)
                                	**type**\:   :py:class:`MplsStaticLabelModeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStaticLabelModeEnum>`
                                
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
                                    self.parent = None
                                    self.label_mode = None
                                    self.prefix = None
                                    self.prefix_length = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-mpls-static-cfg:label-type'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.label_mode is not None:
                                        return True

                                    if self.prefix is not None:
                                        return True

                                    if self.prefix_length is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_static_cfg as meta
                                    return meta._meta_table['MplsStatic.Vrfs.Vrf.Afs.Af.LocalLabels.LocalLabel.LabelType']['meta_info']


                            class Paths(object):
                                """
                                Forward Path Parameters
                                
                                .. attribute:: path
                                
                                	Path Information
                                	**type**\: list of    :py:class:`Path <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStatic.Vrfs.Vrf.Afs.Af.LocalLabels.LocalLabel.Paths.Path>`
                                
                                

                                """

                                _prefix = 'mpls-static-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.path = YList()
                                    self.path.parent = self
                                    self.path.name = 'path'


                                class Path(object):
                                    """
                                    Path Information
                                    
                                    .. attribute:: path_id  <key>
                                    
                                    	Number of paths
                                    	**type**\:  int
                                    
                                    	**range:** 1..16
                                    
                                    .. attribute:: afi
                                    
                                    	Next hop Address Family
                                    	**type**\:   :py:class:`MplsStaticNhAddressFamilyEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStaticNhAddressFamilyEnum>`
                                    
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
                                    	**type**\:   :py:class:`MplsStaticOutLabelTypesEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStaticOutLabelTypesEnum>`
                                    
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
                                    	**type**\:   :py:class:`MplsStaticNhModeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStaticNhModeEnum>`
                                    
                                    	**default value**\: configured
                                    
                                    .. attribute:: path_role
                                    
                                    	Path Role
                                    	**type**\:   :py:class:`MplsStaticPathRoleEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStaticPathRoleEnum>`
                                    
                                    	**default value**\: primary
                                    
                                    .. attribute:: path_type
                                    
                                    	Type of Path (PopAndLookup, CrossConnect)
                                    	**type**\:   :py:class:`MplsStaticPathEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStaticPathEnum>`
                                    
                                    	**default value**\: cross-connect
                                    
                                    

                                    """

                                    _prefix = 'mpls-static-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.path_id = None
                                        self.afi = None
                                        self.backup_id = None
                                        self.interface_name = None
                                        self.label_type = None
                                        self.metric = None
                                        self.next_hop_address = None
                                        self.next_hop_label = None
                                        self.nh_mode = None
                                        self.path_role = None
                                        self.path_type = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')
                                        if self.path_id is None:
                                            raise YPYModelError('Key property path_id is None')

                                        return self.parent._common_path +'/Cisco-IOS-XR-mpls-static-cfg:path[Cisco-IOS-XR-mpls-static-cfg:path-id = ' + str(self.path_id) + ']'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if self.path_id is not None:
                                            return True

                                        if self.afi is not None:
                                            return True

                                        if self.backup_id is not None:
                                            return True

                                        if self.interface_name is not None:
                                            return True

                                        if self.label_type is not None:
                                            return True

                                        if self.metric is not None:
                                            return True

                                        if self.next_hop_address is not None:
                                            return True

                                        if self.next_hop_label is not None:
                                            return True

                                        if self.nh_mode is not None:
                                            return True

                                        if self.path_role is not None:
                                            return True

                                        if self.path_type is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_static_cfg as meta
                                        return meta._meta_table['MplsStatic.Vrfs.Vrf.Afs.Af.LocalLabels.LocalLabel.Paths.Path']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-mpls-static-cfg:paths'

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
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_static_cfg as meta
                                    return meta._meta_table['MplsStatic.Vrfs.Vrf.Afs.Af.LocalLabels.LocalLabel.Paths']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                if self.local_label_id is None:
                                    raise YPYModelError('Key property local_label_id is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-mpls-static-cfg:local-label[Cisco-IOS-XR-mpls-static-cfg:local-label-id = ' + str(self.local_label_id) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.local_label_id is not None:
                                    return True

                                if self.label_type is not None and self.label_type._has_data():
                                    return True

                                if self.paths is not None and self.paths._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_static_cfg as meta
                                return meta._meta_table['MplsStatic.Vrfs.Vrf.Afs.Af.LocalLabels.LocalLabel']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-mpls-static-cfg:local-labels'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.local_label is not None:
                                for child_ref in self.local_label:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_static_cfg as meta
                            return meta._meta_table['MplsStatic.Vrfs.Vrf.Afs.Af.LocalLabels']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.afi is None:
                            raise YPYModelError('Key property afi is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-mpls-static-cfg:af[Cisco-IOS-XR-mpls-static-cfg:afi = ' + str(self.afi) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.afi is not None:
                            return True

                        if self.enable is not None:
                            return True

                        if self.local_labels is not None and self.local_labels._has_data():
                            return True

                        if self.top_label_hash is not None and self.top_label_hash._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_static_cfg as meta
                        return meta._meta_table['MplsStatic.Vrfs.Vrf.Afs.Af']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-mpls-static-cfg:afs'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.af is not None:
                        for child_ref in self.af:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_static_cfg as meta
                    return meta._meta_table['MplsStatic.Vrfs.Vrf.Afs']['meta_info']

            @property
            def _common_path(self):
                if self.vrf_name is None:
                    raise YPYModelError('Key property vrf_name is None')

                return '/Cisco-IOS-XR-mpls-static-cfg:mpls-static/Cisco-IOS-XR-mpls-static-cfg:vrfs/Cisco-IOS-XR-mpls-static-cfg:vrf[Cisco-IOS-XR-mpls-static-cfg:vrf-name = ' + str(self.vrf_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.vrf_name is not None:
                    return True

                if self.afs is not None and self.afs._has_data():
                    return True

                if self.enable is not None:
                    return True

                if self.label_switched_paths is not None and self.label_switched_paths._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_static_cfg as meta
                return meta._meta_table['MplsStatic.Vrfs.Vrf']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-mpls-static-cfg:mpls-static/Cisco-IOS-XR-mpls-static-cfg:vrfs'

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
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_static_cfg as meta
            return meta._meta_table['MplsStatic.Vrfs']['meta_info']


    class Interfaces(object):
        """
        MPLS Static Interface Table
        
        .. attribute:: interface
        
        	MPLS Static Interface Enable
        	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStatic.Interfaces.Interface>`
        
        

        """

        _prefix = 'mpls-static-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.interface = YList()
            self.interface.parent = self
            self.interface.name = 'interface'


        class Interface(object):
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
                self.parent = None
                self.interface_name = None

            @property
            def _common_path(self):
                if self.interface_name is None:
                    raise YPYModelError('Key property interface_name is None')

                return '/Cisco-IOS-XR-mpls-static-cfg:mpls-static/Cisco-IOS-XR-mpls-static-cfg:interfaces/Cisco-IOS-XR-mpls-static-cfg:interface[Cisco-IOS-XR-mpls-static-cfg:interface-name = ' + str(self.interface_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.interface_name is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_static_cfg as meta
                return meta._meta_table['MplsStatic.Interfaces.Interface']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-mpls-static-cfg:mpls-static/Cisco-IOS-XR-mpls-static-cfg:interfaces'

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
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_static_cfg as meta
            return meta._meta_table['MplsStatic.Interfaces']['meta_info']


    class DefaultVrf(object):
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
            self.parent = None
            self.afs = MplsStatic.DefaultVrf.Afs()
            self.afs.parent = self
            self.enable = None
            self.label_switched_paths = MplsStatic.DefaultVrf.LabelSwitchedPaths()
            self.label_switched_paths.parent = self


        class LabelSwitchedPaths(object):
            """
            Table of the Label Switched Paths
            
            .. attribute:: label_switched_path
            
            	Label Switched Path
            	**type**\: list of    :py:class:`LabelSwitchedPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStatic.DefaultVrf.LabelSwitchedPaths.LabelSwitchedPath>`
            
            

            """

            _prefix = 'mpls-static-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.label_switched_path = YList()
                self.label_switched_path.parent = self
                self.label_switched_path.name = 'label_switched_path'


            class LabelSwitchedPath(object):
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
                    self.parent = None
                    self.lsp_name = None
                    self.backup_paths = MplsStatic.DefaultVrf.LabelSwitchedPaths.LabelSwitchedPath.BackupPaths()
                    self.backup_paths.parent = self
                    self.enable = None
                    self.in_label = MplsStatic.DefaultVrf.LabelSwitchedPaths.LabelSwitchedPath.InLabel()
                    self.in_label.parent = self
                    self.paths = MplsStatic.DefaultVrf.LabelSwitchedPaths.LabelSwitchedPath.Paths()
                    self.paths.parent = self


                class BackupPaths(object):
                    """
                    Backup Path Parameters
                    
                    .. attribute:: path
                    
                    	Path Information
                    	**type**\: list of    :py:class:`Path <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStatic.DefaultVrf.LabelSwitchedPaths.LabelSwitchedPath.BackupPaths.Path>`
                    
                    

                    """

                    _prefix = 'mpls-static-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.path = YList()
                        self.path.parent = self
                        self.path.name = 'path'


                    class Path(object):
                        """
                        Path Information
                        
                        .. attribute:: path_id  <key>
                        
                        	Number of paths
                        	**type**\:  int
                        
                        	**range:** 1..16
                        
                        .. attribute:: afi
                        
                        	Next hop Address Family
                        	**type**\:   :py:class:`MplsStaticNhAddressFamilyEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStaticNhAddressFamilyEnum>`
                        
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
                        	**type**\:   :py:class:`MplsStaticOutLabelTypesEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStaticOutLabelTypesEnum>`
                        
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
                        	**type**\:   :py:class:`MplsStaticNhModeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStaticNhModeEnum>`
                        
                        	**default value**\: configured
                        
                        .. attribute:: path_role
                        
                        	Path Role
                        	**type**\:   :py:class:`MplsStaticPathRoleEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStaticPathRoleEnum>`
                        
                        	**default value**\: primary
                        
                        .. attribute:: path_type
                        
                        	Type of Path (PopAndLookup, CrossConnect)
                        	**type**\:   :py:class:`MplsStaticPathEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStaticPathEnum>`
                        
                        	**default value**\: cross-connect
                        
                        

                        """

                        _prefix = 'mpls-static-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.path_id = None
                            self.afi = None
                            self.backup_id = None
                            self.interface_name = None
                            self.label_type = None
                            self.metric = None
                            self.next_hop_address = None
                            self.next_hop_label = None
                            self.nh_mode = None
                            self.path_role = None
                            self.path_type = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.path_id is None:
                                raise YPYModelError('Key property path_id is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-mpls-static-cfg:path[Cisco-IOS-XR-mpls-static-cfg:path-id = ' + str(self.path_id) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.path_id is not None:
                                return True

                            if self.afi is not None:
                                return True

                            if self.backup_id is not None:
                                return True

                            if self.interface_name is not None:
                                return True

                            if self.label_type is not None:
                                return True

                            if self.metric is not None:
                                return True

                            if self.next_hop_address is not None:
                                return True

                            if self.next_hop_label is not None:
                                return True

                            if self.nh_mode is not None:
                                return True

                            if self.path_role is not None:
                                return True

                            if self.path_type is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_static_cfg as meta
                            return meta._meta_table['MplsStatic.DefaultVrf.LabelSwitchedPaths.LabelSwitchedPath.BackupPaths.Path']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-mpls-static-cfg:backup-paths'

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
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_static_cfg as meta
                        return meta._meta_table['MplsStatic.DefaultVrf.LabelSwitchedPaths.LabelSwitchedPath.BackupPaths']['meta_info']


                class InLabel(object):
                    """
                    MPLS Static Local Label Value
                    
                    .. attribute:: in_label_value
                    
                    	Local Label
                    	**type**\:  int
                    
                    	**range:** 16..1048575
                    
                    .. attribute:: label_mode
                    
                    	Label Mode (PerVRF, PerPrefix or LSP)
                    	**type**\:   :py:class:`MplsStaticLabelModeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStaticLabelModeEnum>`
                    
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
                        self.parent = None
                        self.in_label_value = None
                        self.label_mode = None
                        self.prefix = None
                        self.prefix_length = None
                        self.tlh_mode = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-mpls-static-cfg:in-label'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.in_label_value is not None:
                            return True

                        if self.label_mode is not None:
                            return True

                        if self.prefix is not None:
                            return True

                        if self.prefix_length is not None:
                            return True

                        if self.tlh_mode is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_static_cfg as meta
                        return meta._meta_table['MplsStatic.DefaultVrf.LabelSwitchedPaths.LabelSwitchedPath.InLabel']['meta_info']


                class Paths(object):
                    """
                    Forward Path Parameters
                    
                    .. attribute:: path
                    
                    	Path Information
                    	**type**\: list of    :py:class:`Path <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStatic.DefaultVrf.LabelSwitchedPaths.LabelSwitchedPath.Paths.Path>`
                    
                    

                    """

                    _prefix = 'mpls-static-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.path = YList()
                        self.path.parent = self
                        self.path.name = 'path'


                    class Path(object):
                        """
                        Path Information
                        
                        .. attribute:: path_id  <key>
                        
                        	Number of paths
                        	**type**\:  int
                        
                        	**range:** 1..16
                        
                        .. attribute:: afi
                        
                        	Next hop Address Family
                        	**type**\:   :py:class:`MplsStaticNhAddressFamilyEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStaticNhAddressFamilyEnum>`
                        
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
                        	**type**\:   :py:class:`MplsStaticOutLabelTypesEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStaticOutLabelTypesEnum>`
                        
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
                        	**type**\:   :py:class:`MplsStaticNhModeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStaticNhModeEnum>`
                        
                        	**default value**\: configured
                        
                        .. attribute:: path_role
                        
                        	Path Role
                        	**type**\:   :py:class:`MplsStaticPathRoleEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStaticPathRoleEnum>`
                        
                        	**default value**\: primary
                        
                        .. attribute:: path_type
                        
                        	Type of Path (PopAndLookup, CrossConnect)
                        	**type**\:   :py:class:`MplsStaticPathEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStaticPathEnum>`
                        
                        	**default value**\: cross-connect
                        
                        

                        """

                        _prefix = 'mpls-static-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.path_id = None
                            self.afi = None
                            self.backup_id = None
                            self.interface_name = None
                            self.label_type = None
                            self.metric = None
                            self.next_hop_address = None
                            self.next_hop_label = None
                            self.nh_mode = None
                            self.path_role = None
                            self.path_type = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.path_id is None:
                                raise YPYModelError('Key property path_id is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-mpls-static-cfg:path[Cisco-IOS-XR-mpls-static-cfg:path-id = ' + str(self.path_id) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.path_id is not None:
                                return True

                            if self.afi is not None:
                                return True

                            if self.backup_id is not None:
                                return True

                            if self.interface_name is not None:
                                return True

                            if self.label_type is not None:
                                return True

                            if self.metric is not None:
                                return True

                            if self.next_hop_address is not None:
                                return True

                            if self.next_hop_label is not None:
                                return True

                            if self.nh_mode is not None:
                                return True

                            if self.path_role is not None:
                                return True

                            if self.path_type is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_static_cfg as meta
                            return meta._meta_table['MplsStatic.DefaultVrf.LabelSwitchedPaths.LabelSwitchedPath.Paths.Path']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-mpls-static-cfg:paths'

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
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_static_cfg as meta
                        return meta._meta_table['MplsStatic.DefaultVrf.LabelSwitchedPaths.LabelSwitchedPath.Paths']['meta_info']

                @property
                def _common_path(self):
                    if self.lsp_name is None:
                        raise YPYModelError('Key property lsp_name is None')

                    return '/Cisco-IOS-XR-mpls-static-cfg:mpls-static/Cisco-IOS-XR-mpls-static-cfg:default-vrf/Cisco-IOS-XR-mpls-static-cfg:label-switched-paths/Cisco-IOS-XR-mpls-static-cfg:label-switched-path[Cisco-IOS-XR-mpls-static-cfg:lsp-name = ' + str(self.lsp_name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.lsp_name is not None:
                        return True

                    if self.backup_paths is not None and self.backup_paths._has_data():
                        return True

                    if self.enable is not None:
                        return True

                    if self.in_label is not None and self.in_label._has_data():
                        return True

                    if self.paths is not None and self.paths._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_static_cfg as meta
                    return meta._meta_table['MplsStatic.DefaultVrf.LabelSwitchedPaths.LabelSwitchedPath']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-mpls-static-cfg:mpls-static/Cisco-IOS-XR-mpls-static-cfg:default-vrf/Cisco-IOS-XR-mpls-static-cfg:label-switched-paths'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.label_switched_path is not None:
                    for child_ref in self.label_switched_path:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_static_cfg as meta
                return meta._meta_table['MplsStatic.DefaultVrf.LabelSwitchedPaths']['meta_info']


        class Afs(object):
            """
            Address Family Table
            
            .. attribute:: af
            
            	Address Family
            	**type**\: list of    :py:class:`Af <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStatic.DefaultVrf.Afs.Af>`
            
            

            """

            _prefix = 'mpls-static-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.af = YList()
                self.af.parent = self
                self.af.name = 'af'


            class Af(object):
                """
                Address Family
                
                .. attribute:: afi  <key>
                
                	Address Family
                	**type**\:   :py:class:`MplsStaticAddressFamilyEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStaticAddressFamilyEnum>`
                
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
                    self.parent = None
                    self.afi = None
                    self.enable = None
                    self.local_labels = MplsStatic.DefaultVrf.Afs.Af.LocalLabels()
                    self.local_labels.parent = self
                    self.top_label_hash = MplsStatic.DefaultVrf.Afs.Af.TopLabelHash()
                    self.top_label_hash.parent = self


                class TopLabelHash(object):
                    """
                    Top Label Hash
                    
                    .. attribute:: local_labels
                    
                    	Local Label
                    	**type**\:   :py:class:`LocalLabels <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStatic.DefaultVrf.Afs.Af.TopLabelHash.LocalLabels>`
                    
                    

                    """

                    _prefix = 'mpls-static-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.local_labels = MplsStatic.DefaultVrf.Afs.Af.TopLabelHash.LocalLabels()
                        self.local_labels.parent = self


                    class LocalLabels(object):
                        """
                        Local Label
                        
                        .. attribute:: local_label
                        
                        	Specify Local Label
                        	**type**\: list of    :py:class:`LocalLabel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStatic.DefaultVrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel>`
                        
                        

                        """

                        _prefix = 'mpls-static-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.local_label = YList()
                            self.local_label.parent = self
                            self.local_label.name = 'local_label'


                        class LocalLabel(object):
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
                                self.parent = None
                                self.local_label_id = None
                                self.label_type = MplsStatic.DefaultVrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel.LabelType()
                                self.label_type.parent = self
                                self.paths = MplsStatic.DefaultVrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel.Paths()
                                self.paths.parent = self


                            class LabelType(object):
                                """
                                MPLS Static Local Label Value
                                
                                .. attribute:: label_mode
                                
                                	Label Mode (PerVRF, PerPrefix or LSP)
                                	**type**\:   :py:class:`MplsStaticLabelModeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStaticLabelModeEnum>`
                                
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
                                    self.parent = None
                                    self.label_mode = None
                                    self.prefix = None
                                    self.prefix_length = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-mpls-static-cfg:label-type'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.label_mode is not None:
                                        return True

                                    if self.prefix is not None:
                                        return True

                                    if self.prefix_length is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_static_cfg as meta
                                    return meta._meta_table['MplsStatic.DefaultVrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel.LabelType']['meta_info']


                            class Paths(object):
                                """
                                Forward Path Parameters
                                
                                .. attribute:: path
                                
                                	Path Information
                                	**type**\: list of    :py:class:`Path <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStatic.DefaultVrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel.Paths.Path>`
                                
                                

                                """

                                _prefix = 'mpls-static-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.path = YList()
                                    self.path.parent = self
                                    self.path.name = 'path'


                                class Path(object):
                                    """
                                    Path Information
                                    
                                    .. attribute:: path_id  <key>
                                    
                                    	Number of paths
                                    	**type**\:  int
                                    
                                    	**range:** 1..16
                                    
                                    .. attribute:: afi
                                    
                                    	Next hop Address Family
                                    	**type**\:   :py:class:`MplsStaticNhAddressFamilyEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStaticNhAddressFamilyEnum>`
                                    
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
                                    	**type**\:   :py:class:`MplsStaticOutLabelTypesEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStaticOutLabelTypesEnum>`
                                    
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
                                    	**type**\:   :py:class:`MplsStaticNhModeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStaticNhModeEnum>`
                                    
                                    	**default value**\: configured
                                    
                                    .. attribute:: path_role
                                    
                                    	Path Role
                                    	**type**\:   :py:class:`MplsStaticPathRoleEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStaticPathRoleEnum>`
                                    
                                    	**default value**\: primary
                                    
                                    .. attribute:: path_type
                                    
                                    	Type of Path (PopAndLookup, CrossConnect)
                                    	**type**\:   :py:class:`MplsStaticPathEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStaticPathEnum>`
                                    
                                    	**default value**\: cross-connect
                                    
                                    

                                    """

                                    _prefix = 'mpls-static-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.path_id = None
                                        self.afi = None
                                        self.backup_id = None
                                        self.interface_name = None
                                        self.label_type = None
                                        self.metric = None
                                        self.next_hop_address = None
                                        self.next_hop_label = None
                                        self.nh_mode = None
                                        self.path_role = None
                                        self.path_type = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')
                                        if self.path_id is None:
                                            raise YPYModelError('Key property path_id is None')

                                        return self.parent._common_path +'/Cisco-IOS-XR-mpls-static-cfg:path[Cisco-IOS-XR-mpls-static-cfg:path-id = ' + str(self.path_id) + ']'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if self.path_id is not None:
                                            return True

                                        if self.afi is not None:
                                            return True

                                        if self.backup_id is not None:
                                            return True

                                        if self.interface_name is not None:
                                            return True

                                        if self.label_type is not None:
                                            return True

                                        if self.metric is not None:
                                            return True

                                        if self.next_hop_address is not None:
                                            return True

                                        if self.next_hop_label is not None:
                                            return True

                                        if self.nh_mode is not None:
                                            return True

                                        if self.path_role is not None:
                                            return True

                                        if self.path_type is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_static_cfg as meta
                                        return meta._meta_table['MplsStatic.DefaultVrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel.Paths.Path']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-mpls-static-cfg:paths'

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
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_static_cfg as meta
                                    return meta._meta_table['MplsStatic.DefaultVrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel.Paths']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                if self.local_label_id is None:
                                    raise YPYModelError('Key property local_label_id is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-mpls-static-cfg:local-label[Cisco-IOS-XR-mpls-static-cfg:local-label-id = ' + str(self.local_label_id) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.local_label_id is not None:
                                    return True

                                if self.label_type is not None and self.label_type._has_data():
                                    return True

                                if self.paths is not None and self.paths._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_static_cfg as meta
                                return meta._meta_table['MplsStatic.DefaultVrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-mpls-static-cfg:local-labels'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.local_label is not None:
                                for child_ref in self.local_label:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_static_cfg as meta
                            return meta._meta_table['MplsStatic.DefaultVrf.Afs.Af.TopLabelHash.LocalLabels']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-mpls-static-cfg:top-label-hash'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.local_labels is not None and self.local_labels._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_static_cfg as meta
                        return meta._meta_table['MplsStatic.DefaultVrf.Afs.Af.TopLabelHash']['meta_info']


                class LocalLabels(object):
                    """
                    Local Label
                    
                    .. attribute:: local_label
                    
                    	Specify Local Label
                    	**type**\: list of    :py:class:`LocalLabel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStatic.DefaultVrf.Afs.Af.LocalLabels.LocalLabel>`
                    
                    

                    """

                    _prefix = 'mpls-static-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.local_label = YList()
                        self.local_label.parent = self
                        self.local_label.name = 'local_label'


                    class LocalLabel(object):
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
                            self.parent = None
                            self.local_label_id = None
                            self.label_type = MplsStatic.DefaultVrf.Afs.Af.LocalLabels.LocalLabel.LabelType()
                            self.label_type.parent = self
                            self.paths = MplsStatic.DefaultVrf.Afs.Af.LocalLabels.LocalLabel.Paths()
                            self.paths.parent = self


                        class LabelType(object):
                            """
                            MPLS Static Local Label Value
                            
                            .. attribute:: label_mode
                            
                            	Label Mode (PerVRF, PerPrefix or LSP)
                            	**type**\:   :py:class:`MplsStaticLabelModeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStaticLabelModeEnum>`
                            
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
                                self.parent = None
                                self.label_mode = None
                                self.prefix = None
                                self.prefix_length = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-mpls-static-cfg:label-type'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.label_mode is not None:
                                    return True

                                if self.prefix is not None:
                                    return True

                                if self.prefix_length is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_static_cfg as meta
                                return meta._meta_table['MplsStatic.DefaultVrf.Afs.Af.LocalLabels.LocalLabel.LabelType']['meta_info']


                        class Paths(object):
                            """
                            Forward Path Parameters
                            
                            .. attribute:: path
                            
                            	Path Information
                            	**type**\: list of    :py:class:`Path <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStatic.DefaultVrf.Afs.Af.LocalLabels.LocalLabel.Paths.Path>`
                            
                            

                            """

                            _prefix = 'mpls-static-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.path = YList()
                                self.path.parent = self
                                self.path.name = 'path'


                            class Path(object):
                                """
                                Path Information
                                
                                .. attribute:: path_id  <key>
                                
                                	Number of paths
                                	**type**\:  int
                                
                                	**range:** 1..16
                                
                                .. attribute:: afi
                                
                                	Next hop Address Family
                                	**type**\:   :py:class:`MplsStaticNhAddressFamilyEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStaticNhAddressFamilyEnum>`
                                
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
                                	**type**\:   :py:class:`MplsStaticOutLabelTypesEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStaticOutLabelTypesEnum>`
                                
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
                                	**type**\:   :py:class:`MplsStaticNhModeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStaticNhModeEnum>`
                                
                                	**default value**\: configured
                                
                                .. attribute:: path_role
                                
                                	Path Role
                                	**type**\:   :py:class:`MplsStaticPathRoleEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStaticPathRoleEnum>`
                                
                                	**default value**\: primary
                                
                                .. attribute:: path_type
                                
                                	Type of Path (PopAndLookup, CrossConnect)
                                	**type**\:   :py:class:`MplsStaticPathEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg.MplsStaticPathEnum>`
                                
                                	**default value**\: cross-connect
                                
                                

                                """

                                _prefix = 'mpls-static-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.path_id = None
                                    self.afi = None
                                    self.backup_id = None
                                    self.interface_name = None
                                    self.label_type = None
                                    self.metric = None
                                    self.next_hop_address = None
                                    self.next_hop_label = None
                                    self.nh_mode = None
                                    self.path_role = None
                                    self.path_type = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')
                                    if self.path_id is None:
                                        raise YPYModelError('Key property path_id is None')

                                    return self.parent._common_path +'/Cisco-IOS-XR-mpls-static-cfg:path[Cisco-IOS-XR-mpls-static-cfg:path-id = ' + str(self.path_id) + ']'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.path_id is not None:
                                        return True

                                    if self.afi is not None:
                                        return True

                                    if self.backup_id is not None:
                                        return True

                                    if self.interface_name is not None:
                                        return True

                                    if self.label_type is not None:
                                        return True

                                    if self.metric is not None:
                                        return True

                                    if self.next_hop_address is not None:
                                        return True

                                    if self.next_hop_label is not None:
                                        return True

                                    if self.nh_mode is not None:
                                        return True

                                    if self.path_role is not None:
                                        return True

                                    if self.path_type is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_static_cfg as meta
                                    return meta._meta_table['MplsStatic.DefaultVrf.Afs.Af.LocalLabels.LocalLabel.Paths.Path']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-mpls-static-cfg:paths'

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
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_static_cfg as meta
                                return meta._meta_table['MplsStatic.DefaultVrf.Afs.Af.LocalLabels.LocalLabel.Paths']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.local_label_id is None:
                                raise YPYModelError('Key property local_label_id is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-mpls-static-cfg:local-label[Cisco-IOS-XR-mpls-static-cfg:local-label-id = ' + str(self.local_label_id) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.local_label_id is not None:
                                return True

                            if self.label_type is not None and self.label_type._has_data():
                                return True

                            if self.paths is not None and self.paths._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_static_cfg as meta
                            return meta._meta_table['MplsStatic.DefaultVrf.Afs.Af.LocalLabels.LocalLabel']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-mpls-static-cfg:local-labels'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.local_label is not None:
                            for child_ref in self.local_label:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_static_cfg as meta
                        return meta._meta_table['MplsStatic.DefaultVrf.Afs.Af.LocalLabels']['meta_info']

                @property
                def _common_path(self):
                    if self.afi is None:
                        raise YPYModelError('Key property afi is None')

                    return '/Cisco-IOS-XR-mpls-static-cfg:mpls-static/Cisco-IOS-XR-mpls-static-cfg:default-vrf/Cisco-IOS-XR-mpls-static-cfg:afs/Cisco-IOS-XR-mpls-static-cfg:af[Cisco-IOS-XR-mpls-static-cfg:afi = ' + str(self.afi) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.afi is not None:
                        return True

                    if self.enable is not None:
                        return True

                    if self.local_labels is not None and self.local_labels._has_data():
                        return True

                    if self.top_label_hash is not None and self.top_label_hash._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_static_cfg as meta
                    return meta._meta_table['MplsStatic.DefaultVrf.Afs.Af']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-mpls-static-cfg:mpls-static/Cisco-IOS-XR-mpls-static-cfg:default-vrf/Cisco-IOS-XR-mpls-static-cfg:afs'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.af is not None:
                    for child_ref in self.af:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_static_cfg as meta
                return meta._meta_table['MplsStatic.DefaultVrf.Afs']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-mpls-static-cfg:mpls-static/Cisco-IOS-XR-mpls-static-cfg:default-vrf'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.afs is not None and self.afs._has_data():
                return True

            if self.enable is not None:
                return True

            if self.label_switched_paths is not None and self.label_switched_paths._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_static_cfg as meta
            return meta._meta_table['MplsStatic.DefaultVrf']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-mpls-static-cfg:mpls-static'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.default_vrf is not None and self.default_vrf._has_data():
            return True

        if self.enable is not None:
            return True

        if self.interfaces is not None and self.interfaces._has_data():
            return True

        if self.vrfs is not None and self.vrfs._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_static_cfg as meta
        return meta._meta_table['MplsStatic']['meta_info']


