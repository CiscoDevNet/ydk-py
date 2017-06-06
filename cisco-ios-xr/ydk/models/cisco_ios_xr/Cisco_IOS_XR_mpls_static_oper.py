""" Cisco_IOS_XR_mpls_static_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR mpls\-static package operational data.

This module contains definitions
for the following management objects\:
  mpls\-static\: MPLS STATIC operational data

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class MgmtMplsStaticLabelModeEnum(Enum):
    """
    MgmtMplsStaticLabelModeEnum

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

    none = 0

    per_prefix = 1

    per_vrf = 2

    cross_connect = 3


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_static_oper as meta
        return meta._meta_table['MgmtMplsStaticLabelModeEnum']


class MgmtMplsStaticLabelStatusEnum(Enum):
    """
    MgmtMplsStaticLabelStatusEnum

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

    not_created = 0

    vrf_down = 1

    rewrite_vrf_down = 2

    lsd_disconnected = 3

    lsd_failed = 4

    wait_for_lsd_reply = 5

    label_created = 6

    label_create_failed = 7

    label_rewrite_failed = 8

    rewrite_next_hop_interface_down = 9

    label_discrepancy = 10

    rewrite_discrepancy = 11

    label_status_unknown = 12


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_static_oper as meta
        return meta._meta_table['MgmtMplsStaticLabelStatusEnum']


class MgmtMplsStaticPathStatusEnum(Enum):
    """
    MgmtMplsStaticPathStatusEnum

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

    path_next_hop_none = 0

    path_next_hop_interface_down = 1

    path_next_hop_valid = 2

    resolve_failed = 3

    frr_backup = 4

    backup = 5


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_static_oper as meta
        return meta._meta_table['MgmtMplsStaticPathStatusEnum']


class MgmtStaticAddrEnum(Enum):
    """
    MgmtStaticAddrEnum

    Mgmt static addr

    .. data:: not_applicable = 0

    	Not Applicable

    .. data:: ipv4 = 1

    	IPv4

    .. data:: ipv6 = 2

    	IPv6

    """

    not_applicable = 0

    ipv4 = 1

    ipv6 = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_static_oper as meta
        return meta._meta_table['MgmtStaticAddrEnum']


class MgmtStaticPathEnum(Enum):
    """
    MgmtStaticPathEnum

    Mgmt static path

    .. data:: cross_connect_path = 0

    	Crossconnect Path

    .. data:: pop_lookup_path = 1

    	Pop and Lookup Path

    """

    cross_connect_path = 0

    pop_lookup_path = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_static_oper as meta
        return meta._meta_table['MgmtStaticPathEnum']


class MplsStaticPathRoleEnum(Enum):
    """
    MplsStaticPathRoleEnum

    Mpls static path role

    .. data:: primary = 0

    	Path is only for primary traffic

    .. data:: backup = 1

    	Path is only for backup traffic

    .. data:: primary_and_backup = 2

    	Path is for primary and backup traffic

    """

    primary = 0

    backup = 1

    primary_and_backup = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_static_oper as meta
        return meta._meta_table['MplsStaticPathRoleEnum']



class MplsStatic(object):
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
        self.local_labels = MplsStatic.LocalLabels()
        self.local_labels.parent = self
        self.summary = MplsStatic.Summary()
        self.summary.parent = self
        self.vrfs = MplsStatic.Vrfs()
        self.vrfs.parent = self


    class Vrfs(object):
        """
        VRF table
        
        .. attribute:: vrf
        
        	VRF Name
        	**type**\: list of    :py:class:`Vrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MplsStatic.Vrfs.Vrf>`
        
        

        """

        _prefix = 'mpls-static-oper'
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
                self.parent = None
                self.vrf_name = None
                self.local_labels = MplsStatic.Vrfs.Vrf.LocalLabels()
                self.local_labels.parent = self
                self.lsps = MplsStatic.Vrfs.Vrf.Lsps()
                self.lsps.parent = self


            class Lsps(object):
                """
                data for static lsp table
                
                .. attribute:: lsp
                
                	Data for static lsp
                	**type**\: list of    :py:class:`Lsp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MplsStatic.Vrfs.Vrf.Lsps.Lsp>`
                
                

                """

                _prefix = 'mpls-static-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.lsp = YList()
                    self.lsp.parent = self
                    self.lsp.name = 'lsp'


                class Lsp(object):
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
                        self.parent = None
                        self.lsp_name = None
                        self.label = MplsStatic.Vrfs.Vrf.Lsps.Lsp.Label()
                        self.label.parent = self
                        self.lsp_name_xr = None


                    class Label(object):
                        """
                        Label Information
                        
                        .. attribute:: address_family
                        
                        	Address Family
                        	**type**\:   :py:class:`MgmtStaticAddrEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MgmtStaticAddrEnum>`
                        
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
                        	**type**\:   :py:class:`MgmtMplsStaticLabelModeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MgmtMplsStaticLabelModeEnum>`
                        
                        .. attribute:: label_status
                        
                        	Label Status
                        	**type**\:   :py:class:`MgmtMplsStaticLabelStatusEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MgmtMplsStaticLabelStatusEnum>`
                        
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
                            self.parent = None
                            self.address_family = None
                            self.backup_path_info = YList()
                            self.backup_path_info.parent = self
                            self.backup_path_info.name = 'backup_path_info'
                            self.backup_pathset_resolve_nh = MplsStatic.Vrfs.Vrf.Lsps.Lsp.Label.BackupPathsetResolveNh()
                            self.backup_pathset_resolve_nh.parent = self
                            self.backup_pathset_via_resolve = None
                            self.label = None
                            self.label_mode = None
                            self.label_status = None
                            self.path_info = YList()
                            self.path_info.parent = self
                            self.path_info.name = 'path_info'
                            self.pathset_resolve_nh = MplsStatic.Vrfs.Vrf.Lsps.Lsp.Label.PathsetResolveNh()
                            self.pathset_resolve_nh.parent = self
                            self.pathset_via_resolve = None
                            self.prefix = MplsStatic.Vrfs.Vrf.Lsps.Lsp.Label.Prefix()
                            self.prefix.parent = self
                            self.vrf_name = None


                        class Prefix(object):
                            """
                            Prefix Information
                            
                            .. attribute:: prefix
                            
                            	Prefix
                            	**type**\:   :py:class:`Prefix_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MplsStatic.Vrfs.Vrf.Lsps.Lsp.Label.Prefix.Prefix_>`
                            
                            .. attribute:: prefix_length
                            
                            	Prefix length
                            	**type**\:  int
                            
                            	**range:** 0..255
                            
                            

                            """

                            _prefix = 'mpls-static-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.prefix = MplsStatic.Vrfs.Vrf.Lsps.Lsp.Label.Prefix.Prefix_()
                                self.prefix.parent = self
                                self.prefix_length = None


                            class Prefix_(object):
                                """
                                Prefix
                                
                                .. attribute:: af_name
                                
                                	AFName
                                	**type**\:   :py:class:`MgmtStaticAddrEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MgmtStaticAddrEnum>`
                                
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
                                    self.parent = None
                                    self.af_name = None
                                    self.ipv4_prefix = None
                                    self.ipv6_prefix = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-mpls-static-oper:prefix'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.af_name is not None:
                                        return True

                                    if self.ipv4_prefix is not None:
                                        return True

                                    if self.ipv6_prefix is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_static_oper as meta
                                    return meta._meta_table['MplsStatic.Vrfs.Vrf.Lsps.Lsp.Label.Prefix.Prefix_']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-mpls-static-oper:prefix'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.prefix is not None and self.prefix._has_data():
                                    return True

                                if self.prefix_length is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_static_oper as meta
                                return meta._meta_table['MplsStatic.Vrfs.Vrf.Lsps.Lsp.Label.Prefix']['meta_info']


                        class PathsetResolveNh(object):
                            """
                            Primary pathset resolve\-nexthop IP Address
                            
                            .. attribute:: af_name
                            
                            	AFName
                            	**type**\:   :py:class:`MgmtStaticAddrEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MgmtStaticAddrEnum>`
                            
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
                                self.parent = None
                                self.af_name = None
                                self.ipv4_prefix = None
                                self.ipv6_prefix = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-mpls-static-oper:pathset-resolve-nh'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.af_name is not None:
                                    return True

                                if self.ipv4_prefix is not None:
                                    return True

                                if self.ipv6_prefix is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_static_oper as meta
                                return meta._meta_table['MplsStatic.Vrfs.Vrf.Lsps.Lsp.Label.PathsetResolveNh']['meta_info']


                        class BackupPathsetResolveNh(object):
                            """
                            Backup pathset resolve\-nexthop IP Address
                            
                            .. attribute:: af_name
                            
                            	AFName
                            	**type**\:   :py:class:`MgmtStaticAddrEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MgmtStaticAddrEnum>`
                            
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
                                self.parent = None
                                self.af_name = None
                                self.ipv4_prefix = None
                                self.ipv6_prefix = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-mpls-static-oper:backup-pathset-resolve-nh'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.af_name is not None:
                                    return True

                                if self.ipv4_prefix is not None:
                                    return True

                                if self.ipv6_prefix is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_static_oper as meta
                                return meta._meta_table['MplsStatic.Vrfs.Vrf.Lsps.Lsp.Label.BackupPathsetResolveNh']['meta_info']


                        class PathInfo(object):
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
                            	**type**\:   :py:class:`MplsStaticPathRoleEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MplsStaticPathRoleEnum>`
                            
                            .. attribute:: status
                            
                            	Path Status
                            	**type**\:   :py:class:`MgmtMplsStaticPathStatusEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MgmtMplsStaticPathStatusEnum>`
                            
                            .. attribute:: type
                            
                            	Path Type
                            	**type**\:   :py:class:`MgmtStaticPathEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MgmtStaticPathEnum>`
                            
                            

                            """

                            _prefix = 'mpls-static-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.backup_id = None
                                self.nexthop = MplsStatic.Vrfs.Vrf.Lsps.Lsp.Label.PathInfo.Nexthop()
                                self.nexthop.parent = self
                                self.path_id = None
                                self.path_number = None
                                self.path_role = None
                                self.status = None
                                self.type = None


                            class Nexthop(object):
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
                                    self.parent = None
                                    self.address = MplsStatic.Vrfs.Vrf.Lsps.Lsp.Label.PathInfo.Nexthop.Address()
                                    self.address.parent = self
                                    self.afi = None
                                    self.interface_name = None
                                    self.label = None


                                class Address(object):
                                    """
                                    Next\-Hop IP Address
                                    
                                    .. attribute:: af_name
                                    
                                    	AFName
                                    	**type**\:   :py:class:`MgmtStaticAddrEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MgmtStaticAddrEnum>`
                                    
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
                                        self.parent = None
                                        self.af_name = None
                                        self.ipv4_prefix = None
                                        self.ipv6_prefix = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-mpls-static-oper:address'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.af_name is not None:
                                            return True

                                        if self.ipv4_prefix is not None:
                                            return True

                                        if self.ipv6_prefix is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_static_oper as meta
                                        return meta._meta_table['MplsStatic.Vrfs.Vrf.Lsps.Lsp.Label.PathInfo.Nexthop.Address']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-mpls-static-oper:nexthop'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.address is not None and self.address._has_data():
                                        return True

                                    if self.afi is not None:
                                        return True

                                    if self.interface_name is not None:
                                        return True

                                    if self.label is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_static_oper as meta
                                    return meta._meta_table['MplsStatic.Vrfs.Vrf.Lsps.Lsp.Label.PathInfo.Nexthop']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-mpls-static-oper:path-info'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.backup_id is not None:
                                    return True

                                if self.nexthop is not None and self.nexthop._has_data():
                                    return True

                                if self.path_id is not None:
                                    return True

                                if self.path_number is not None:
                                    return True

                                if self.path_role is not None:
                                    return True

                                if self.status is not None:
                                    return True

                                if self.type is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_static_oper as meta
                                return meta._meta_table['MplsStatic.Vrfs.Vrf.Lsps.Lsp.Label.PathInfo']['meta_info']


                        class BackupPathInfo(object):
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
                            	**type**\:   :py:class:`MplsStaticPathRoleEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MplsStaticPathRoleEnum>`
                            
                            .. attribute:: status
                            
                            	Path Status
                            	**type**\:   :py:class:`MgmtMplsStaticPathStatusEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MgmtMplsStaticPathStatusEnum>`
                            
                            .. attribute:: type
                            
                            	Path Type
                            	**type**\:   :py:class:`MgmtStaticPathEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MgmtStaticPathEnum>`
                            
                            

                            """

                            _prefix = 'mpls-static-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.backup_id = None
                                self.nexthop = MplsStatic.Vrfs.Vrf.Lsps.Lsp.Label.BackupPathInfo.Nexthop()
                                self.nexthop.parent = self
                                self.path_id = None
                                self.path_number = None
                                self.path_role = None
                                self.status = None
                                self.type = None


                            class Nexthop(object):
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
                                    self.parent = None
                                    self.address = MplsStatic.Vrfs.Vrf.Lsps.Lsp.Label.BackupPathInfo.Nexthop.Address()
                                    self.address.parent = self
                                    self.afi = None
                                    self.interface_name = None
                                    self.label = None


                                class Address(object):
                                    """
                                    Next\-Hop IP Address
                                    
                                    .. attribute:: af_name
                                    
                                    	AFName
                                    	**type**\:   :py:class:`MgmtStaticAddrEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MgmtStaticAddrEnum>`
                                    
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
                                        self.parent = None
                                        self.af_name = None
                                        self.ipv4_prefix = None
                                        self.ipv6_prefix = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-mpls-static-oper:address'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.af_name is not None:
                                            return True

                                        if self.ipv4_prefix is not None:
                                            return True

                                        if self.ipv6_prefix is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_static_oper as meta
                                        return meta._meta_table['MplsStatic.Vrfs.Vrf.Lsps.Lsp.Label.BackupPathInfo.Nexthop.Address']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-mpls-static-oper:nexthop'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.address is not None and self.address._has_data():
                                        return True

                                    if self.afi is not None:
                                        return True

                                    if self.interface_name is not None:
                                        return True

                                    if self.label is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_static_oper as meta
                                    return meta._meta_table['MplsStatic.Vrfs.Vrf.Lsps.Lsp.Label.BackupPathInfo.Nexthop']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-mpls-static-oper:backup-path-info'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.backup_id is not None:
                                    return True

                                if self.nexthop is not None and self.nexthop._has_data():
                                    return True

                                if self.path_id is not None:
                                    return True

                                if self.path_number is not None:
                                    return True

                                if self.path_role is not None:
                                    return True

                                if self.status is not None:
                                    return True

                                if self.type is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_static_oper as meta
                                return meta._meta_table['MplsStatic.Vrfs.Vrf.Lsps.Lsp.Label.BackupPathInfo']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-mpls-static-oper:label'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.address_family is not None:
                                return True

                            if self.backup_path_info is not None:
                                for child_ref in self.backup_path_info:
                                    if child_ref._has_data():
                                        return True

                            if self.backup_pathset_resolve_nh is not None and self.backup_pathset_resolve_nh._has_data():
                                return True

                            if self.backup_pathset_via_resolve is not None:
                                return True

                            if self.label is not None:
                                return True

                            if self.label_mode is not None:
                                return True

                            if self.label_status is not None:
                                return True

                            if self.path_info is not None:
                                for child_ref in self.path_info:
                                    if child_ref._has_data():
                                        return True

                            if self.pathset_resolve_nh is not None and self.pathset_resolve_nh._has_data():
                                return True

                            if self.pathset_via_resolve is not None:
                                return True

                            if self.prefix is not None and self.prefix._has_data():
                                return True

                            if self.vrf_name is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_static_oper as meta
                            return meta._meta_table['MplsStatic.Vrfs.Vrf.Lsps.Lsp.Label']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.lsp_name is None:
                            raise YPYModelError('Key property lsp_name is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-mpls-static-oper:lsp[Cisco-IOS-XR-mpls-static-oper:lsp-name = ' + str(self.lsp_name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.lsp_name is not None:
                            return True

                        if self.label is not None and self.label._has_data():
                            return True

                        if self.lsp_name_xr is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_static_oper as meta
                        return meta._meta_table['MplsStatic.Vrfs.Vrf.Lsps.Lsp']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-mpls-static-oper:lsps'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.lsp is not None:
                        for child_ref in self.lsp:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_static_oper as meta
                    return meta._meta_table['MplsStatic.Vrfs.Vrf.Lsps']['meta_info']


            class LocalLabels(object):
                """
                data for static local\-label table
                
                .. attribute:: local_label
                
                	Data for static label
                	**type**\: list of    :py:class:`LocalLabel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MplsStatic.Vrfs.Vrf.LocalLabels.LocalLabel>`
                
                

                """

                _prefix = 'mpls-static-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.local_label = YList()
                    self.local_label.parent = self
                    self.local_label.name = 'local_label'


                class LocalLabel(object):
                    """
                    Data for static label
                    
                    .. attribute:: local_label_id  <key>
                    
                    	Local Label
                    	**type**\:  int
                    
                    	**range:** 16..1048575
                    
                    .. attribute:: address_family
                    
                    	Address Family
                    	**type**\:   :py:class:`MgmtStaticAddrEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MgmtStaticAddrEnum>`
                    
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
                    	**type**\:   :py:class:`MgmtMplsStaticLabelModeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MgmtMplsStaticLabelModeEnum>`
                    
                    .. attribute:: label_status
                    
                    	Label Status
                    	**type**\:   :py:class:`MgmtMplsStaticLabelStatusEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MgmtMplsStaticLabelStatusEnum>`
                    
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
                        self.parent = None
                        self.local_label_id = None
                        self.address_family = None
                        self.backup_path_info = YList()
                        self.backup_path_info.parent = self
                        self.backup_path_info.name = 'backup_path_info'
                        self.backup_pathset_resolve_nh = MplsStatic.Vrfs.Vrf.LocalLabels.LocalLabel.BackupPathsetResolveNh()
                        self.backup_pathset_resolve_nh.parent = self
                        self.backup_pathset_via_resolve = None
                        self.label = None
                        self.label_mode = None
                        self.label_status = None
                        self.path_info = YList()
                        self.path_info.parent = self
                        self.path_info.name = 'path_info'
                        self.pathset_resolve_nh = MplsStatic.Vrfs.Vrf.LocalLabels.LocalLabel.PathsetResolveNh()
                        self.pathset_resolve_nh.parent = self
                        self.pathset_via_resolve = None
                        self.prefix = MplsStatic.Vrfs.Vrf.LocalLabels.LocalLabel.Prefix()
                        self.prefix.parent = self
                        self.vrf_name = None


                    class Prefix(object):
                        """
                        Prefix Information
                        
                        .. attribute:: prefix
                        
                        	Prefix
                        	**type**\:   :py:class:`Prefix_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MplsStatic.Vrfs.Vrf.LocalLabels.LocalLabel.Prefix.Prefix_>`
                        
                        .. attribute:: prefix_length
                        
                        	Prefix length
                        	**type**\:  int
                        
                        	**range:** 0..255
                        
                        

                        """

                        _prefix = 'mpls-static-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.prefix = MplsStatic.Vrfs.Vrf.LocalLabels.LocalLabel.Prefix.Prefix_()
                            self.prefix.parent = self
                            self.prefix_length = None


                        class Prefix_(object):
                            """
                            Prefix
                            
                            .. attribute:: af_name
                            
                            	AFName
                            	**type**\:   :py:class:`MgmtStaticAddrEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MgmtStaticAddrEnum>`
                            
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
                                self.parent = None
                                self.af_name = None
                                self.ipv4_prefix = None
                                self.ipv6_prefix = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-mpls-static-oper:prefix'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.af_name is not None:
                                    return True

                                if self.ipv4_prefix is not None:
                                    return True

                                if self.ipv6_prefix is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_static_oper as meta
                                return meta._meta_table['MplsStatic.Vrfs.Vrf.LocalLabels.LocalLabel.Prefix.Prefix_']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-mpls-static-oper:prefix'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.prefix is not None and self.prefix._has_data():
                                return True

                            if self.prefix_length is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_static_oper as meta
                            return meta._meta_table['MplsStatic.Vrfs.Vrf.LocalLabels.LocalLabel.Prefix']['meta_info']


                    class PathsetResolveNh(object):
                        """
                        Primary pathset resolve\-nexthop IP Address
                        
                        .. attribute:: af_name
                        
                        	AFName
                        	**type**\:   :py:class:`MgmtStaticAddrEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MgmtStaticAddrEnum>`
                        
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
                            self.parent = None
                            self.af_name = None
                            self.ipv4_prefix = None
                            self.ipv6_prefix = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-mpls-static-oper:pathset-resolve-nh'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.af_name is not None:
                                return True

                            if self.ipv4_prefix is not None:
                                return True

                            if self.ipv6_prefix is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_static_oper as meta
                            return meta._meta_table['MplsStatic.Vrfs.Vrf.LocalLabels.LocalLabel.PathsetResolveNh']['meta_info']


                    class BackupPathsetResolveNh(object):
                        """
                        Backup pathset resolve\-nexthop IP Address
                        
                        .. attribute:: af_name
                        
                        	AFName
                        	**type**\:   :py:class:`MgmtStaticAddrEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MgmtStaticAddrEnum>`
                        
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
                            self.parent = None
                            self.af_name = None
                            self.ipv4_prefix = None
                            self.ipv6_prefix = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-mpls-static-oper:backup-pathset-resolve-nh'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.af_name is not None:
                                return True

                            if self.ipv4_prefix is not None:
                                return True

                            if self.ipv6_prefix is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_static_oper as meta
                            return meta._meta_table['MplsStatic.Vrfs.Vrf.LocalLabels.LocalLabel.BackupPathsetResolveNh']['meta_info']


                    class PathInfo(object):
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
                        	**type**\:   :py:class:`MplsStaticPathRoleEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MplsStaticPathRoleEnum>`
                        
                        .. attribute:: status
                        
                        	Path Status
                        	**type**\:   :py:class:`MgmtMplsStaticPathStatusEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MgmtMplsStaticPathStatusEnum>`
                        
                        .. attribute:: type
                        
                        	Path Type
                        	**type**\:   :py:class:`MgmtStaticPathEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MgmtStaticPathEnum>`
                        
                        

                        """

                        _prefix = 'mpls-static-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.backup_id = None
                            self.nexthop = MplsStatic.Vrfs.Vrf.LocalLabels.LocalLabel.PathInfo.Nexthop()
                            self.nexthop.parent = self
                            self.path_id = None
                            self.path_number = None
                            self.path_role = None
                            self.status = None
                            self.type = None


                        class Nexthop(object):
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
                                self.parent = None
                                self.address = MplsStatic.Vrfs.Vrf.LocalLabels.LocalLabel.PathInfo.Nexthop.Address()
                                self.address.parent = self
                                self.afi = None
                                self.interface_name = None
                                self.label = None


                            class Address(object):
                                """
                                Next\-Hop IP Address
                                
                                .. attribute:: af_name
                                
                                	AFName
                                	**type**\:   :py:class:`MgmtStaticAddrEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MgmtStaticAddrEnum>`
                                
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
                                    self.parent = None
                                    self.af_name = None
                                    self.ipv4_prefix = None
                                    self.ipv6_prefix = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-mpls-static-oper:address'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.af_name is not None:
                                        return True

                                    if self.ipv4_prefix is not None:
                                        return True

                                    if self.ipv6_prefix is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_static_oper as meta
                                    return meta._meta_table['MplsStatic.Vrfs.Vrf.LocalLabels.LocalLabel.PathInfo.Nexthop.Address']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-mpls-static-oper:nexthop'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.address is not None and self.address._has_data():
                                    return True

                                if self.afi is not None:
                                    return True

                                if self.interface_name is not None:
                                    return True

                                if self.label is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_static_oper as meta
                                return meta._meta_table['MplsStatic.Vrfs.Vrf.LocalLabels.LocalLabel.PathInfo.Nexthop']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-mpls-static-oper:path-info'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.backup_id is not None:
                                return True

                            if self.nexthop is not None and self.nexthop._has_data():
                                return True

                            if self.path_id is not None:
                                return True

                            if self.path_number is not None:
                                return True

                            if self.path_role is not None:
                                return True

                            if self.status is not None:
                                return True

                            if self.type is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_static_oper as meta
                            return meta._meta_table['MplsStatic.Vrfs.Vrf.LocalLabels.LocalLabel.PathInfo']['meta_info']


                    class BackupPathInfo(object):
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
                        	**type**\:   :py:class:`MplsStaticPathRoleEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MplsStaticPathRoleEnum>`
                        
                        .. attribute:: status
                        
                        	Path Status
                        	**type**\:   :py:class:`MgmtMplsStaticPathStatusEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MgmtMplsStaticPathStatusEnum>`
                        
                        .. attribute:: type
                        
                        	Path Type
                        	**type**\:   :py:class:`MgmtStaticPathEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MgmtStaticPathEnum>`
                        
                        

                        """

                        _prefix = 'mpls-static-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.backup_id = None
                            self.nexthop = MplsStatic.Vrfs.Vrf.LocalLabels.LocalLabel.BackupPathInfo.Nexthop()
                            self.nexthop.parent = self
                            self.path_id = None
                            self.path_number = None
                            self.path_role = None
                            self.status = None
                            self.type = None


                        class Nexthop(object):
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
                                self.parent = None
                                self.address = MplsStatic.Vrfs.Vrf.LocalLabels.LocalLabel.BackupPathInfo.Nexthop.Address()
                                self.address.parent = self
                                self.afi = None
                                self.interface_name = None
                                self.label = None


                            class Address(object):
                                """
                                Next\-Hop IP Address
                                
                                .. attribute:: af_name
                                
                                	AFName
                                	**type**\:   :py:class:`MgmtStaticAddrEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MgmtStaticAddrEnum>`
                                
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
                                    self.parent = None
                                    self.af_name = None
                                    self.ipv4_prefix = None
                                    self.ipv6_prefix = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-mpls-static-oper:address'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.af_name is not None:
                                        return True

                                    if self.ipv4_prefix is not None:
                                        return True

                                    if self.ipv6_prefix is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_static_oper as meta
                                    return meta._meta_table['MplsStatic.Vrfs.Vrf.LocalLabels.LocalLabel.BackupPathInfo.Nexthop.Address']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-mpls-static-oper:nexthop'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.address is not None and self.address._has_data():
                                    return True

                                if self.afi is not None:
                                    return True

                                if self.interface_name is not None:
                                    return True

                                if self.label is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_static_oper as meta
                                return meta._meta_table['MplsStatic.Vrfs.Vrf.LocalLabels.LocalLabel.BackupPathInfo.Nexthop']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-mpls-static-oper:backup-path-info'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.backup_id is not None:
                                return True

                            if self.nexthop is not None and self.nexthop._has_data():
                                return True

                            if self.path_id is not None:
                                return True

                            if self.path_number is not None:
                                return True

                            if self.path_role is not None:
                                return True

                            if self.status is not None:
                                return True

                            if self.type is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_static_oper as meta
                            return meta._meta_table['MplsStatic.Vrfs.Vrf.LocalLabels.LocalLabel.BackupPathInfo']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.local_label_id is None:
                            raise YPYModelError('Key property local_label_id is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-mpls-static-oper:local-label[Cisco-IOS-XR-mpls-static-oper:local-label-id = ' + str(self.local_label_id) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.local_label_id is not None:
                            return True

                        if self.address_family is not None:
                            return True

                        if self.backup_path_info is not None:
                            for child_ref in self.backup_path_info:
                                if child_ref._has_data():
                                    return True

                        if self.backup_pathset_resolve_nh is not None and self.backup_pathset_resolve_nh._has_data():
                            return True

                        if self.backup_pathset_via_resolve is not None:
                            return True

                        if self.label is not None:
                            return True

                        if self.label_mode is not None:
                            return True

                        if self.label_status is not None:
                            return True

                        if self.path_info is not None:
                            for child_ref in self.path_info:
                                if child_ref._has_data():
                                    return True

                        if self.pathset_resolve_nh is not None and self.pathset_resolve_nh._has_data():
                            return True

                        if self.pathset_via_resolve is not None:
                            return True

                        if self.prefix is not None and self.prefix._has_data():
                            return True

                        if self.vrf_name is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_static_oper as meta
                        return meta._meta_table['MplsStatic.Vrfs.Vrf.LocalLabels.LocalLabel']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-mpls-static-oper:local-labels'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.local_label is not None:
                        for child_ref in self.local_label:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_static_oper as meta
                    return meta._meta_table['MplsStatic.Vrfs.Vrf.LocalLabels']['meta_info']

            @property
            def _common_path(self):
                if self.vrf_name is None:
                    raise YPYModelError('Key property vrf_name is None')

                return '/Cisco-IOS-XR-mpls-static-oper:mpls-static/Cisco-IOS-XR-mpls-static-oper:vrfs/Cisco-IOS-XR-mpls-static-oper:vrf[Cisco-IOS-XR-mpls-static-oper:vrf-name = ' + str(self.vrf_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.vrf_name is not None:
                    return True

                if self.local_labels is not None and self.local_labels._has_data():
                    return True

                if self.lsps is not None and self.lsps._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_static_oper as meta
                return meta._meta_table['MplsStatic.Vrfs.Vrf']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-mpls-static-oper:mpls-static/Cisco-IOS-XR-mpls-static-oper:vrfs'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.vrf is not None:
                for child_ref in self.vrf:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_static_oper as meta
            return meta._meta_table['MplsStatic.Vrfs']['meta_info']


    class Summary(object):
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
            self.parent = None
            self.active_vrf_count = None
            self.im_connected = None
            self.interface_count = None
            self.interface_foward_reference_count = None
            self.ipv4_route_count = None
            self.ipv6_route_count = None
            self.label_count = None
            self.label_discrepancy_count = None
            self.label_error_count = None
            self.lsd_connected = None
            self.mpls_enabled_interface_count = None
            self.ribv4_connected = None
            self.ribv6_connected = None
            self.rsi_connected = None
            self.vrf_count = None

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-mpls-static-oper:mpls-static/Cisco-IOS-XR-mpls-static-oper:summary'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.active_vrf_count is not None:
                return True

            if self.im_connected is not None:
                return True

            if self.interface_count is not None:
                return True

            if self.interface_foward_reference_count is not None:
                return True

            if self.ipv4_route_count is not None:
                return True

            if self.ipv6_route_count is not None:
                return True

            if self.label_count is not None:
                return True

            if self.label_discrepancy_count is not None:
                return True

            if self.label_error_count is not None:
                return True

            if self.lsd_connected is not None:
                return True

            if self.mpls_enabled_interface_count is not None:
                return True

            if self.ribv4_connected is not None:
                return True

            if self.ribv6_connected is not None:
                return True

            if self.rsi_connected is not None:
                return True

            if self.vrf_count is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_static_oper as meta
            return meta._meta_table['MplsStatic.Summary']['meta_info']


    class LocalLabels(object):
        """
        data for static local\-label table
        
        .. attribute:: local_label
        
        	Data for static label
        	**type**\: list of    :py:class:`LocalLabel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MplsStatic.LocalLabels.LocalLabel>`
        
        

        """

        _prefix = 'mpls-static-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.local_label = YList()
            self.local_label.parent = self
            self.local_label.name = 'local_label'


        class LocalLabel(object):
            """
            Data for static label
            
            .. attribute:: local_label_id  <key>
            
            	Local Label
            	**type**\:  int
            
            	**range:** 16..1048575
            
            .. attribute:: address_family
            
            	Address Family
            	**type**\:   :py:class:`MgmtStaticAddrEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MgmtStaticAddrEnum>`
            
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
            	**type**\:   :py:class:`MgmtMplsStaticLabelModeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MgmtMplsStaticLabelModeEnum>`
            
            .. attribute:: label_status
            
            	Label Status
            	**type**\:   :py:class:`MgmtMplsStaticLabelStatusEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MgmtMplsStaticLabelStatusEnum>`
            
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
                self.parent = None
                self.local_label_id = None
                self.address_family = None
                self.backup_path_info = YList()
                self.backup_path_info.parent = self
                self.backup_path_info.name = 'backup_path_info'
                self.backup_pathset_resolve_nh = MplsStatic.LocalLabels.LocalLabel.BackupPathsetResolveNh()
                self.backup_pathset_resolve_nh.parent = self
                self.backup_pathset_via_resolve = None
                self.label = None
                self.label_mode = None
                self.label_status = None
                self.path_info = YList()
                self.path_info.parent = self
                self.path_info.name = 'path_info'
                self.pathset_resolve_nh = MplsStatic.LocalLabels.LocalLabel.PathsetResolveNh()
                self.pathset_resolve_nh.parent = self
                self.pathset_via_resolve = None
                self.prefix = MplsStatic.LocalLabels.LocalLabel.Prefix()
                self.prefix.parent = self
                self.vrf_name = None


            class Prefix(object):
                """
                Prefix Information
                
                .. attribute:: prefix
                
                	Prefix
                	**type**\:   :py:class:`Prefix_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MplsStatic.LocalLabels.LocalLabel.Prefix.Prefix_>`
                
                .. attribute:: prefix_length
                
                	Prefix length
                	**type**\:  int
                
                	**range:** 0..255
                
                

                """

                _prefix = 'mpls-static-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.prefix = MplsStatic.LocalLabels.LocalLabel.Prefix.Prefix_()
                    self.prefix.parent = self
                    self.prefix_length = None


                class Prefix_(object):
                    """
                    Prefix
                    
                    .. attribute:: af_name
                    
                    	AFName
                    	**type**\:   :py:class:`MgmtStaticAddrEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MgmtStaticAddrEnum>`
                    
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
                        self.parent = None
                        self.af_name = None
                        self.ipv4_prefix = None
                        self.ipv6_prefix = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-mpls-static-oper:prefix'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.af_name is not None:
                            return True

                        if self.ipv4_prefix is not None:
                            return True

                        if self.ipv6_prefix is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_static_oper as meta
                        return meta._meta_table['MplsStatic.LocalLabels.LocalLabel.Prefix.Prefix_']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-mpls-static-oper:prefix'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.prefix is not None and self.prefix._has_data():
                        return True

                    if self.prefix_length is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_static_oper as meta
                    return meta._meta_table['MplsStatic.LocalLabels.LocalLabel.Prefix']['meta_info']


            class PathsetResolveNh(object):
                """
                Primary pathset resolve\-nexthop IP Address
                
                .. attribute:: af_name
                
                	AFName
                	**type**\:   :py:class:`MgmtStaticAddrEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MgmtStaticAddrEnum>`
                
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
                    self.parent = None
                    self.af_name = None
                    self.ipv4_prefix = None
                    self.ipv6_prefix = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-mpls-static-oper:pathset-resolve-nh'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.af_name is not None:
                        return True

                    if self.ipv4_prefix is not None:
                        return True

                    if self.ipv6_prefix is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_static_oper as meta
                    return meta._meta_table['MplsStatic.LocalLabels.LocalLabel.PathsetResolveNh']['meta_info']


            class BackupPathsetResolveNh(object):
                """
                Backup pathset resolve\-nexthop IP Address
                
                .. attribute:: af_name
                
                	AFName
                	**type**\:   :py:class:`MgmtStaticAddrEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MgmtStaticAddrEnum>`
                
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
                    self.parent = None
                    self.af_name = None
                    self.ipv4_prefix = None
                    self.ipv6_prefix = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-mpls-static-oper:backup-pathset-resolve-nh'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.af_name is not None:
                        return True

                    if self.ipv4_prefix is not None:
                        return True

                    if self.ipv6_prefix is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_static_oper as meta
                    return meta._meta_table['MplsStatic.LocalLabels.LocalLabel.BackupPathsetResolveNh']['meta_info']


            class PathInfo(object):
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
                	**type**\:   :py:class:`MplsStaticPathRoleEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MplsStaticPathRoleEnum>`
                
                .. attribute:: status
                
                	Path Status
                	**type**\:   :py:class:`MgmtMplsStaticPathStatusEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MgmtMplsStaticPathStatusEnum>`
                
                .. attribute:: type
                
                	Path Type
                	**type**\:   :py:class:`MgmtStaticPathEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MgmtStaticPathEnum>`
                
                

                """

                _prefix = 'mpls-static-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.backup_id = None
                    self.nexthop = MplsStatic.LocalLabels.LocalLabel.PathInfo.Nexthop()
                    self.nexthop.parent = self
                    self.path_id = None
                    self.path_number = None
                    self.path_role = None
                    self.status = None
                    self.type = None


                class Nexthop(object):
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
                        self.parent = None
                        self.address = MplsStatic.LocalLabels.LocalLabel.PathInfo.Nexthop.Address()
                        self.address.parent = self
                        self.afi = None
                        self.interface_name = None
                        self.label = None


                    class Address(object):
                        """
                        Next\-Hop IP Address
                        
                        .. attribute:: af_name
                        
                        	AFName
                        	**type**\:   :py:class:`MgmtStaticAddrEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MgmtStaticAddrEnum>`
                        
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
                            self.parent = None
                            self.af_name = None
                            self.ipv4_prefix = None
                            self.ipv6_prefix = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-mpls-static-oper:address'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.af_name is not None:
                                return True

                            if self.ipv4_prefix is not None:
                                return True

                            if self.ipv6_prefix is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_static_oper as meta
                            return meta._meta_table['MplsStatic.LocalLabels.LocalLabel.PathInfo.Nexthop.Address']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-mpls-static-oper:nexthop'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.address is not None and self.address._has_data():
                            return True

                        if self.afi is not None:
                            return True

                        if self.interface_name is not None:
                            return True

                        if self.label is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_static_oper as meta
                        return meta._meta_table['MplsStatic.LocalLabels.LocalLabel.PathInfo.Nexthop']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-mpls-static-oper:path-info'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.backup_id is not None:
                        return True

                    if self.nexthop is not None and self.nexthop._has_data():
                        return True

                    if self.path_id is not None:
                        return True

                    if self.path_number is not None:
                        return True

                    if self.path_role is not None:
                        return True

                    if self.status is not None:
                        return True

                    if self.type is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_static_oper as meta
                    return meta._meta_table['MplsStatic.LocalLabels.LocalLabel.PathInfo']['meta_info']


            class BackupPathInfo(object):
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
                	**type**\:   :py:class:`MplsStaticPathRoleEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MplsStaticPathRoleEnum>`
                
                .. attribute:: status
                
                	Path Status
                	**type**\:   :py:class:`MgmtMplsStaticPathStatusEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MgmtMplsStaticPathStatusEnum>`
                
                .. attribute:: type
                
                	Path Type
                	**type**\:   :py:class:`MgmtStaticPathEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MgmtStaticPathEnum>`
                
                

                """

                _prefix = 'mpls-static-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.backup_id = None
                    self.nexthop = MplsStatic.LocalLabels.LocalLabel.BackupPathInfo.Nexthop()
                    self.nexthop.parent = self
                    self.path_id = None
                    self.path_number = None
                    self.path_role = None
                    self.status = None
                    self.type = None


                class Nexthop(object):
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
                        self.parent = None
                        self.address = MplsStatic.LocalLabels.LocalLabel.BackupPathInfo.Nexthop.Address()
                        self.address.parent = self
                        self.afi = None
                        self.interface_name = None
                        self.label = None


                    class Address(object):
                        """
                        Next\-Hop IP Address
                        
                        .. attribute:: af_name
                        
                        	AFName
                        	**type**\:   :py:class:`MgmtStaticAddrEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_oper.MgmtStaticAddrEnum>`
                        
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
                            self.parent = None
                            self.af_name = None
                            self.ipv4_prefix = None
                            self.ipv6_prefix = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-mpls-static-oper:address'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.af_name is not None:
                                return True

                            if self.ipv4_prefix is not None:
                                return True

                            if self.ipv6_prefix is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_static_oper as meta
                            return meta._meta_table['MplsStatic.LocalLabels.LocalLabel.BackupPathInfo.Nexthop.Address']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-mpls-static-oper:nexthop'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.address is not None and self.address._has_data():
                            return True

                        if self.afi is not None:
                            return True

                        if self.interface_name is not None:
                            return True

                        if self.label is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_static_oper as meta
                        return meta._meta_table['MplsStatic.LocalLabels.LocalLabel.BackupPathInfo.Nexthop']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-mpls-static-oper:backup-path-info'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.backup_id is not None:
                        return True

                    if self.nexthop is not None and self.nexthop._has_data():
                        return True

                    if self.path_id is not None:
                        return True

                    if self.path_number is not None:
                        return True

                    if self.path_role is not None:
                        return True

                    if self.status is not None:
                        return True

                    if self.type is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_static_oper as meta
                    return meta._meta_table['MplsStatic.LocalLabels.LocalLabel.BackupPathInfo']['meta_info']

            @property
            def _common_path(self):
                if self.local_label_id is None:
                    raise YPYModelError('Key property local_label_id is None')

                return '/Cisco-IOS-XR-mpls-static-oper:mpls-static/Cisco-IOS-XR-mpls-static-oper:local-labels/Cisco-IOS-XR-mpls-static-oper:local-label[Cisco-IOS-XR-mpls-static-oper:local-label-id = ' + str(self.local_label_id) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.local_label_id is not None:
                    return True

                if self.address_family is not None:
                    return True

                if self.backup_path_info is not None:
                    for child_ref in self.backup_path_info:
                        if child_ref._has_data():
                            return True

                if self.backup_pathset_resolve_nh is not None and self.backup_pathset_resolve_nh._has_data():
                    return True

                if self.backup_pathset_via_resolve is not None:
                    return True

                if self.label is not None:
                    return True

                if self.label_mode is not None:
                    return True

                if self.label_status is not None:
                    return True

                if self.path_info is not None:
                    for child_ref in self.path_info:
                        if child_ref._has_data():
                            return True

                if self.pathset_resolve_nh is not None and self.pathset_resolve_nh._has_data():
                    return True

                if self.pathset_via_resolve is not None:
                    return True

                if self.prefix is not None and self.prefix._has_data():
                    return True

                if self.vrf_name is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_static_oper as meta
                return meta._meta_table['MplsStatic.LocalLabels.LocalLabel']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-mpls-static-oper:mpls-static/Cisco-IOS-XR-mpls-static-oper:local-labels'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.local_label is not None:
                for child_ref in self.local_label:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_static_oper as meta
            return meta._meta_table['MplsStatic.LocalLabels']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-mpls-static-oper:mpls-static'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.local_labels is not None and self.local_labels._has_data():
            return True

        if self.summary is not None and self.summary._has_data():
            return True

        if self.vrfs is not None and self.vrfs._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_mpls_static_oper as meta
        return meta._meta_table['MplsStatic']['meta_info']


