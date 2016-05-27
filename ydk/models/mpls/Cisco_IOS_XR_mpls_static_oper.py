""" Cisco_IOS_XR_mpls_static_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR mpls\-static package operational data.

This module contains definitions
for the following management objects\:
  mpls\-static\: MPLS STATIC operational data

Copyright (c) 2013\-2015 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError



class MgmtMplsStaticLabelModeEnum(Enum):
    """
    MgmtMplsStaticLabelModeEnum

    Mgmt mpls static label mode

    .. data:: NONE = 0

    	No Label Mode

    .. data:: PER_PREFIX = 1

    	Per-prefix Label

    .. data:: PER_VRF = 2

    	Per-VRF label

    .. data:: CROSS_CONNECT = 3

    	Label with crossconnect

    """

    NONE = 0

    PER_PREFIX = 1

    PER_VRF = 2

    CROSS_CONNECT = 3


    @staticmethod
    def _meta_info():
        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_static_oper as meta
        return meta._meta_table['MgmtMplsStaticLabelModeEnum']


class MgmtMplsStaticLabelStatusEnum(Enum):
    """
    MgmtMplsStaticLabelStatusEnum

    Mgmt mpls static label status

    .. data:: NOT_CREATED = 0

    	Label Not Created

    .. data:: VRF_DOWN = 1

    	Label without active VRF

    .. data:: REWRITE_VRF_DOWN = 2

    	Rewrite without active VRF

    .. data:: LSD_DISCONNECTED = 3

    	LSD is disconnected

    .. data:: LSD_FAILED = 4

    	LSD operation failed

    .. data:: WAIT_FOR_LSD_REPLY = 5

    	Waiting for LSD operation

    .. data:: LABEL_CREATED = 6

    	Label Created

    .. data:: LABEL_CREATE_FAILED = 7

    	Label Creation Failed

    .. data:: LABEL_REWRITE_FAILED = 8

    	Rewrite Creation Failed

    .. data:: REWRITE_NEXT_HOP_INTERFACE_MISSING = 9

    	Rewrite NextHop Missing 

    .. data:: LABEL_DISCREPANCY = 10

    	Label Discrepancy 

    .. data:: REWRITE_DISCREPANCY = 11

    	Rewrite Discrepancy 

    .. data:: LABEL_STATUS_UNKNOWN = 12

    	Label Status Unknown

    """

    NOT_CREATED = 0

    VRF_DOWN = 1

    REWRITE_VRF_DOWN = 2

    LSD_DISCONNECTED = 3

    LSD_FAILED = 4

    WAIT_FOR_LSD_REPLY = 5

    LABEL_CREATED = 6

    LABEL_CREATE_FAILED = 7

    LABEL_REWRITE_FAILED = 8

    REWRITE_NEXT_HOP_INTERFACE_MISSING = 9

    LABEL_DISCREPANCY = 10

    REWRITE_DISCREPANCY = 11

    LABEL_STATUS_UNKNOWN = 12


    @staticmethod
    def _meta_info():
        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_static_oper as meta
        return meta._meta_table['MgmtMplsStaticLabelStatusEnum']


class MgmtStaticAddrEnum(Enum):
    """
    MgmtStaticAddrEnum

    Mgmt static addr

    .. data:: IPV4 = 0

    	IPv4

    .. data:: IPV6 = 1

    	IPv6

    """

    IPV4 = 0

    IPV6 = 1


    @staticmethod
    def _meta_info():
        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_static_oper as meta
        return meta._meta_table['MgmtStaticAddrEnum']


class MgmtStaticNhLblEnum(Enum):
    """
    MgmtStaticNhLblEnum

    Mgmt static nh lbl

    .. data:: OUT_LABEL = 0

    	Next-Hop Label

    .. data:: OUT_POP = 1

    	Next-Hop Pop

    .. data:: OUT_EXPLICIT_NULL = 2

    	Next-Hop Explicit-Null

    """

    OUT_LABEL = 0

    OUT_POP = 1

    OUT_EXPLICIT_NULL = 2


    @staticmethod
    def _meta_info():
        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_static_oper as meta
        return meta._meta_table['MgmtStaticNhLblEnum']


class MgmtStaticPathEnum(Enum):
    """
    MgmtStaticPathEnum

    Mgmt static path

    .. data:: CROSS_CONNECT_PATH = 0

    	Crossconnect Path

    .. data:: POP_LOOKUP_PATH = 1

    	Pop and Lookup Path

    """

    CROSS_CONNECT_PATH = 0

    POP_LOOKUP_PATH = 1


    @staticmethod
    def _meta_info():
        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_static_oper as meta
        return meta._meta_table['MgmtStaticPathEnum']



class MplsStatic(object):
    """
    MPLS STATIC operational data
    
    .. attribute:: vrfs
    
    	VRF table
    	**type**\: :py:class:`Vrfs <ydk.models.mpls.Cisco_IOS_XR_mpls_static_oper.MplsStatic.Vrfs>`
    
    .. attribute:: summary
    
    	MPLS STATIC summary data
    	**type**\: :py:class:`Summary <ydk.models.mpls.Cisco_IOS_XR_mpls_static_oper.MplsStatic.Summary>`
    
    .. attribute:: local_labels
    
    	data for static local\-label table
    	**type**\: :py:class:`LocalLabels <ydk.models.mpls.Cisco_IOS_XR_mpls_static_oper.MplsStatic.LocalLabels>`
    
    

    """

    _prefix = 'mpls-static-oper'
    _revision = '2015-11-09'

    def __init__(self):
        self.vrfs = MplsStatic.Vrfs()
        self.vrfs.parent = self
        self.summary = MplsStatic.Summary()
        self.summary.parent = self
        self.local_labels = MplsStatic.LocalLabels()
        self.local_labels.parent = self


    class Vrfs(object):
        """
        VRF table
        
        .. attribute:: vrf
        
        	VRF Name
        	**type**\: list of :py:class:`Vrf <ydk.models.mpls.Cisco_IOS_XR_mpls_static_oper.MplsStatic.Vrfs.Vrf>`
        
        

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
            	**type**\: str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: local_labels
            
            	data for static local\-label table
            	**type**\: :py:class:`LocalLabels <ydk.models.mpls.Cisco_IOS_XR_mpls_static_oper.MplsStatic.Vrfs.Vrf.LocalLabels>`
            
            

            """

            _prefix = 'mpls-static-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.vrf_name = None
                self.local_labels = MplsStatic.Vrfs.Vrf.LocalLabels()
                self.local_labels.parent = self


            class LocalLabels(object):
                """
                data for static local\-label table
                
                .. attribute:: local_label
                
                	Data for static label
                	**type**\: list of :py:class:`LocalLabel <ydk.models.mpls.Cisco_IOS_XR_mpls_static_oper.MplsStatic.Vrfs.Vrf.LocalLabels.LocalLabel>`
                
                

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
                    	**type**\: int
                    
                    	**range:** 16..1048575
                    
                    .. attribute:: prefix
                    
                    	Prefix Information
                    	**type**\: :py:class:`Prefix <ydk.models.mpls.Cisco_IOS_XR_mpls_static_oper.MplsStatic.Vrfs.Vrf.LocalLabels.LocalLabel.Prefix>`
                    
                    .. attribute:: label
                    
                    	Label value
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: label_mode
                    
                    	Label Mode
                    	**type**\: :py:class:`MgmtMplsStaticLabelModeEnum <ydk.models.mpls.Cisco_IOS_XR_mpls_static_oper.MgmtMplsStaticLabelModeEnum>`
                    
                    .. attribute:: label_status
                    
                    	Label Status
                    	**type**\: :py:class:`MgmtMplsStaticLabelStatusEnum <ydk.models.mpls.Cisco_IOS_XR_mpls_static_oper.MgmtMplsStaticLabelStatusEnum>`
                    
                    .. attribute:: vrf_name
                    
                    	VRF name
                    	**type**\: str
                    
                    .. attribute:: path_info
                    
                    	Path Information
                    	**type**\: list of :py:class:`PathInfo <ydk.models.mpls.Cisco_IOS_XR_mpls_static_oper.MplsStatic.Vrfs.Vrf.LocalLabels.LocalLabel.PathInfo>`
                    
                    

                    """

                    _prefix = 'mpls-static-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.local_label_id = None
                        self.prefix = MplsStatic.Vrfs.Vrf.LocalLabels.LocalLabel.Prefix()
                        self.prefix.parent = self
                        self.label = None
                        self.label_mode = None
                        self.label_status = None
                        self.vrf_name = None
                        self.path_info = YList()
                        self.path_info.parent = self
                        self.path_info.name = 'path_info'


                    class Prefix(object):
                        """
                        Prefix Information
                        
                        .. attribute:: prefix
                        
                        	Prefix
                        	**type**\: :py:class:`Prefix <ydk.models.mpls.Cisco_IOS_XR_mpls_static_oper.MplsStatic.Vrfs.Vrf.LocalLabels.LocalLabel.Prefix.Prefix>`
                        
                        .. attribute:: prefix_length
                        
                        	Prefix length
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        

                        """

                        _prefix = 'mpls-static-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.prefix = MplsStatic.Vrfs.Vrf.LocalLabels.LocalLabel.Prefix.Prefix()
                            self.prefix.parent = self
                            self.prefix_length = None


                        class Prefix(object):
                            """
                            Prefix
                            
                            .. attribute:: af_name
                            
                            	AFName
                            	**type**\: :py:class:`MgmtStaticAddrEnum <ydk.models.mpls.Cisco_IOS_XR_mpls_static_oper.MgmtStaticAddrEnum>`
                            
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
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.af_name = None
                                self.ipv4_prefix = None
                                self.ipv6_prefix = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-mpls-static-oper:prefix'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.af_name is not None:
                                    return True

                                if self.ipv4_prefix is not None:
                                    return True

                                if self.ipv6_prefix is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_static_oper as meta
                                return meta._meta_table['MplsStatic.Vrfs.Vrf.LocalLabels.LocalLabel.Prefix.Prefix']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-mpls-static-oper:prefix'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.prefix is not None and self.prefix._has_data():
                                return True

                            if self.prefix_length is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_static_oper as meta
                            return meta._meta_table['MplsStatic.Vrfs.Vrf.LocalLabels.LocalLabel.Prefix']['meta_info']


                    class PathInfo(object):
                        """
                        Path Information
                        
                        .. attribute:: path
                        
                        	Path Number
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: type
                        
                        	Path Type
                        	**type**\: :py:class:`MgmtStaticPathEnum <ydk.models.mpls.Cisco_IOS_XR_mpls_static_oper.MgmtStaticPathEnum>`
                        
                        .. attribute:: next_hop_label_type
                        
                        	Next\-Hop Label Type
                        	**type**\: :py:class:`MgmtStaticNhLblEnum <ydk.models.mpls.Cisco_IOS_XR_mpls_static_oper.MgmtStaticNhLblEnum>`
                        
                        .. attribute:: next_hop_label
                        
                        	Next\-Hop Label
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: next_hop_interface_name
                        
                        	Next\-Hop Interface Name
                        	**type**\: str
                        
                        .. attribute:: next_hop_ipv4_address_set
                        
                        	Next\-Hop Ipv4 Set
                        	**type**\: bool
                        
                        .. attribute:: next_hop_ipv4_address
                        
                        	Next\-Hop Ipv4 Address
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        

                        """

                        _prefix = 'mpls-static-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.path = None
                            self.type = None
                            self.next_hop_label_type = None
                            self.next_hop_label = None
                            self.next_hop_interface_name = None
                            self.next_hop_ipv4_address_set = None
                            self.next_hop_ipv4_address = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-mpls-static-oper:path-info'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.path is not None:
                                return True

                            if self.type is not None:
                                return True

                            if self.next_hop_label_type is not None:
                                return True

                            if self.next_hop_label is not None:
                                return True

                            if self.next_hop_interface_name is not None:
                                return True

                            if self.next_hop_ipv4_address_set is not None:
                                return True

                            if self.next_hop_ipv4_address is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_static_oper as meta
                            return meta._meta_table['MplsStatic.Vrfs.Vrf.LocalLabels.LocalLabel.PathInfo']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')
                        if self.local_label_id is None:
                            raise YPYDataValidationError('Key property local_label_id is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-mpls-static-oper:local-label[Cisco-IOS-XR-mpls-static-oper:local-label-id = ' + str(self.local_label_id) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.local_label_id is not None:
                            return True

                        if self.prefix is not None and self.prefix._has_data():
                            return True

                        if self.label is not None:
                            return True

                        if self.label_mode is not None:
                            return True

                        if self.label_status is not None:
                            return True

                        if self.vrf_name is not None:
                            return True

                        if self.path_info is not None:
                            for child_ref in self.path_info:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_static_oper as meta
                        return meta._meta_table['MplsStatic.Vrfs.Vrf.LocalLabels.LocalLabel']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-mpls-static-oper:local-labels'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.local_label is not None:
                        for child_ref in self.local_label:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_static_oper as meta
                    return meta._meta_table['MplsStatic.Vrfs.Vrf.LocalLabels']['meta_info']

            @property
            def _common_path(self):
                if self.vrf_name is None:
                    raise YPYDataValidationError('Key property vrf_name is None')

                return '/Cisco-IOS-XR-mpls-static-oper:mpls-static/Cisco-IOS-XR-mpls-static-oper:vrfs/Cisco-IOS-XR-mpls-static-oper:vrf[Cisco-IOS-XR-mpls-static-oper:vrf-name = ' + str(self.vrf_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.vrf_name is not None:
                    return True

                if self.local_labels is not None and self.local_labels._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_static_oper as meta
                return meta._meta_table['MplsStatic.Vrfs.Vrf']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-mpls-static-oper:mpls-static/Cisco-IOS-XR-mpls-static-oper:vrfs'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.vrf is not None:
                for child_ref in self.vrf:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_static_oper as meta
            return meta._meta_table['MplsStatic.Vrfs']['meta_info']


    class Summary(object):
        """
        MPLS STATIC summary data
        
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
        
        .. attribute:: lsd_connected
        
        	LSD connection is up
        	**type**\: bool
        
        .. attribute:: im_connected
        
        	IM is connected
        	**type**\: bool
        
        .. attribute:: rsi_connected
        
        	RSI is connected
        	**type**\: bool
        
        

        """

        _prefix = 'mpls-static-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.label_count = None
            self.label_error_count = None
            self.label_discrepancy_count = None
            self.vrf_count = None
            self.active_vrf_count = None
            self.interface_count = None
            self.interface_foward_reference_count = None
            self.mpls_enabled_interface_count = None
            self.lsd_connected = None
            self.im_connected = None
            self.rsi_connected = None

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-mpls-static-oper:mpls-static/Cisco-IOS-XR-mpls-static-oper:summary'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.label_count is not None:
                return True

            if self.label_error_count is not None:
                return True

            if self.label_discrepancy_count is not None:
                return True

            if self.vrf_count is not None:
                return True

            if self.active_vrf_count is not None:
                return True

            if self.interface_count is not None:
                return True

            if self.interface_foward_reference_count is not None:
                return True

            if self.mpls_enabled_interface_count is not None:
                return True

            if self.lsd_connected is not None:
                return True

            if self.im_connected is not None:
                return True

            if self.rsi_connected is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_static_oper as meta
            return meta._meta_table['MplsStatic.Summary']['meta_info']


    class LocalLabels(object):
        """
        data for static local\-label table
        
        .. attribute:: local_label
        
        	Data for static label
        	**type**\: list of :py:class:`LocalLabel <ydk.models.mpls.Cisco_IOS_XR_mpls_static_oper.MplsStatic.LocalLabels.LocalLabel>`
        
        

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
            	**type**\: int
            
            	**range:** 16..1048575
            
            .. attribute:: prefix
            
            	Prefix Information
            	**type**\: :py:class:`Prefix <ydk.models.mpls.Cisco_IOS_XR_mpls_static_oper.MplsStatic.LocalLabels.LocalLabel.Prefix>`
            
            .. attribute:: label
            
            	Label value
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: label_mode
            
            	Label Mode
            	**type**\: :py:class:`MgmtMplsStaticLabelModeEnum <ydk.models.mpls.Cisco_IOS_XR_mpls_static_oper.MgmtMplsStaticLabelModeEnum>`
            
            .. attribute:: label_status
            
            	Label Status
            	**type**\: :py:class:`MgmtMplsStaticLabelStatusEnum <ydk.models.mpls.Cisco_IOS_XR_mpls_static_oper.MgmtMplsStaticLabelStatusEnum>`
            
            .. attribute:: vrf_name
            
            	VRF name
            	**type**\: str
            
            .. attribute:: path_info
            
            	Path Information
            	**type**\: list of :py:class:`PathInfo <ydk.models.mpls.Cisco_IOS_XR_mpls_static_oper.MplsStatic.LocalLabels.LocalLabel.PathInfo>`
            
            

            """

            _prefix = 'mpls-static-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.local_label_id = None
                self.prefix = MplsStatic.LocalLabels.LocalLabel.Prefix()
                self.prefix.parent = self
                self.label = None
                self.label_mode = None
                self.label_status = None
                self.vrf_name = None
                self.path_info = YList()
                self.path_info.parent = self
                self.path_info.name = 'path_info'


            class Prefix(object):
                """
                Prefix Information
                
                .. attribute:: prefix
                
                	Prefix
                	**type**\: :py:class:`Prefix <ydk.models.mpls.Cisco_IOS_XR_mpls_static_oper.MplsStatic.LocalLabels.LocalLabel.Prefix.Prefix>`
                
                .. attribute:: prefix_length
                
                	Prefix length
                	**type**\: int
                
                	**range:** 0..255
                
                

                """

                _prefix = 'mpls-static-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.prefix = MplsStatic.LocalLabels.LocalLabel.Prefix.Prefix()
                    self.prefix.parent = self
                    self.prefix_length = None


                class Prefix(object):
                    """
                    Prefix
                    
                    .. attribute:: af_name
                    
                    	AFName
                    	**type**\: :py:class:`MgmtStaticAddrEnum <ydk.models.mpls.Cisco_IOS_XR_mpls_static_oper.MgmtStaticAddrEnum>`
                    
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
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.af_name = None
                        self.ipv4_prefix = None
                        self.ipv6_prefix = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-mpls-static-oper:prefix'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.af_name is not None:
                            return True

                        if self.ipv4_prefix is not None:
                            return True

                        if self.ipv6_prefix is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_static_oper as meta
                        return meta._meta_table['MplsStatic.LocalLabels.LocalLabel.Prefix.Prefix']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-mpls-static-oper:prefix'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.prefix is not None and self.prefix._has_data():
                        return True

                    if self.prefix_length is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_static_oper as meta
                    return meta._meta_table['MplsStatic.LocalLabels.LocalLabel.Prefix']['meta_info']


            class PathInfo(object):
                """
                Path Information
                
                .. attribute:: path
                
                	Path Number
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: type
                
                	Path Type
                	**type**\: :py:class:`MgmtStaticPathEnum <ydk.models.mpls.Cisco_IOS_XR_mpls_static_oper.MgmtStaticPathEnum>`
                
                .. attribute:: next_hop_label_type
                
                	Next\-Hop Label Type
                	**type**\: :py:class:`MgmtStaticNhLblEnum <ydk.models.mpls.Cisco_IOS_XR_mpls_static_oper.MgmtStaticNhLblEnum>`
                
                .. attribute:: next_hop_label
                
                	Next\-Hop Label
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: next_hop_interface_name
                
                	Next\-Hop Interface Name
                	**type**\: str
                
                .. attribute:: next_hop_ipv4_address_set
                
                	Next\-Hop Ipv4 Set
                	**type**\: bool
                
                .. attribute:: next_hop_ipv4_address
                
                	Next\-Hop Ipv4 Address
                	**type**\: str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                

                """

                _prefix = 'mpls-static-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.path = None
                    self.type = None
                    self.next_hop_label_type = None
                    self.next_hop_label = None
                    self.next_hop_interface_name = None
                    self.next_hop_ipv4_address_set = None
                    self.next_hop_ipv4_address = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-mpls-static-oper:path-info'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.path is not None:
                        return True

                    if self.type is not None:
                        return True

                    if self.next_hop_label_type is not None:
                        return True

                    if self.next_hop_label is not None:
                        return True

                    if self.next_hop_interface_name is not None:
                        return True

                    if self.next_hop_ipv4_address_set is not None:
                        return True

                    if self.next_hop_ipv4_address is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_static_oper as meta
                    return meta._meta_table['MplsStatic.LocalLabels.LocalLabel.PathInfo']['meta_info']

            @property
            def _common_path(self):
                if self.local_label_id is None:
                    raise YPYDataValidationError('Key property local_label_id is None')

                return '/Cisco-IOS-XR-mpls-static-oper:mpls-static/Cisco-IOS-XR-mpls-static-oper:local-labels/Cisco-IOS-XR-mpls-static-oper:local-label[Cisco-IOS-XR-mpls-static-oper:local-label-id = ' + str(self.local_label_id) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.local_label_id is not None:
                    return True

                if self.prefix is not None and self.prefix._has_data():
                    return True

                if self.label is not None:
                    return True

                if self.label_mode is not None:
                    return True

                if self.label_status is not None:
                    return True

                if self.vrf_name is not None:
                    return True

                if self.path_info is not None:
                    for child_ref in self.path_info:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_static_oper as meta
                return meta._meta_table['MplsStatic.LocalLabels.LocalLabel']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-mpls-static-oper:mpls-static/Cisco-IOS-XR-mpls-static-oper:local-labels'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.local_label is not None:
                for child_ref in self.local_label:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_static_oper as meta
            return meta._meta_table['MplsStatic.LocalLabels']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-mpls-static-oper:mpls-static'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if not self.is_config():
            return False
        if self.vrfs is not None and self.vrfs._has_data():
            return True

        if self.summary is not None and self.summary._has_data():
            return True

        if self.local_labels is not None and self.local_labels._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_static_oper as meta
        return meta._meta_table['MplsStatic']['meta_info']


