""" Cisco_IOS_XR_mpls_static_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR mpls\-static package configuration.

This module contains definitions
for the following management objects\:
  mpls\-static\: MPLS Static Configuration Data

Copyright (c) 2013\-2015 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError



class MplsStaticAddressFamilyEnum(Enum):
    """
    MplsStaticAddressFamilyEnum

    Mpls static address family

    .. data:: IPV4_UNICAST = 1

    	IPv4 Unicast

    """

    IPV4_UNICAST = 1


    @staticmethod
    def _meta_info():
        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_static_cfg as meta
        return meta._meta_table['MplsStaticAddressFamilyEnum']


class MplsStaticLabelModeEnum(Enum):
    """
    MplsStaticLabelModeEnum

    Mpls static label mode

    .. data:: PER_VRF = 1

    	Per VRF

    .. data:: PER_PREFIX = 2

    	Per Prefix

    .. data:: LSP = 3

    	Cross connect

    """

    PER_VRF = 1

    PER_PREFIX = 2

    LSP = 3


    @staticmethod
    def _meta_info():
        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_static_cfg as meta
        return meta._meta_table['MplsStaticLabelModeEnum']


class MplsStaticOutLabelTypesEnum(Enum):
    """
    MplsStaticOutLabelTypesEnum

    Mpls static out label types

    .. data:: NONE = 0

    	None

    .. data:: OUT_LABEL = 1

    	OutLabel

    .. data:: POP = 2

    	Pop

    .. data:: EXP_NULL = 3

    	Exp Null

    """

    NONE = 0

    OUT_LABEL = 1

    POP = 2

    EXP_NULL = 3


    @staticmethod
    def _meta_info():
        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_static_cfg as meta
        return meta._meta_table['MplsStaticOutLabelTypesEnum']


class MplsStaticPathEnum(Enum):
    """
    MplsStaticPathEnum

    Mpls static path

    .. data:: POP_AND_LOOKUP = 1

    	Pop and Lookup

    .. data:: CROSS_CONNECT = 2

    	Crossconnect

    """

    POP_AND_LOOKUP = 1

    CROSS_CONNECT = 2


    @staticmethod
    def _meta_info():
        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_static_cfg as meta
        return meta._meta_table['MplsStaticPathEnum']



class MplsStatic(object):
    """
    MPLS Static Configuration Data
    
    .. attribute:: default_vrf
    
    	Default VRF
    	**type**\: :py:class:`DefaultVrf <ydk.models.mpls.Cisco_IOS_XR_mpls_static_cfg.MplsStatic.DefaultVrf>`
    
    .. attribute:: enable
    
    	MPLS Static Apply Enable
    	**type**\: :py:class:`Empty <ydk.types.Empty>`
    
    .. attribute:: interfaces
    
    	MPLS Static Interface Table
    	**type**\: :py:class:`Interfaces <ydk.models.mpls.Cisco_IOS_XR_mpls_static_cfg.MplsStatic.Interfaces>`
    
    .. attribute:: vrfs
    
    	VRF table
    	**type**\: :py:class:`Vrfs <ydk.models.mpls.Cisco_IOS_XR_mpls_static_cfg.MplsStatic.Vrfs>`
    
    

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


    class DefaultVrf(object):
        """
        Default VRF
        
        .. attribute:: afs
        
        	Address Family Table
        	**type**\: :py:class:`Afs <ydk.models.mpls.Cisco_IOS_XR_mpls_static_cfg.MplsStatic.DefaultVrf.Afs>`
        
        .. attribute:: enable
        
        	MPLS Static Apply Enable
        	**type**\: :py:class:`Empty <ydk.types.Empty>`
        
        

        """

        _prefix = 'mpls-static-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.afs = MplsStatic.DefaultVrf.Afs()
            self.afs.parent = self
            self.enable = None


        class Afs(object):
            """
            Address Family Table
            
            .. attribute:: af
            
            	Address Family
            	**type**\: list of :py:class:`Af <ydk.models.mpls.Cisco_IOS_XR_mpls_static_cfg.MplsStatic.DefaultVrf.Afs.Af>`
            
            

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
                
                .. attribute:: afi
                
                	Address Family
                	**type**\: :py:class:`MplsStaticAddressFamilyEnum <ydk.models.mpls.Cisco_IOS_XR_mpls_static_cfg.MplsStaticAddressFamilyEnum>`
                
                .. attribute:: enable
                
                	MPLS Static Apply Enable
                	**type**\: :py:class:`Empty <ydk.types.Empty>`
                
                .. attribute:: local_labels
                
                	Local Label
                	**type**\: :py:class:`LocalLabels <ydk.models.mpls.Cisco_IOS_XR_mpls_static_cfg.MplsStatic.DefaultVrf.Afs.Af.LocalLabels>`
                
                .. attribute:: top_label_hash
                
                	Top Label Hash
                	**type**\: :py:class:`TopLabelHash <ydk.models.mpls.Cisco_IOS_XR_mpls_static_cfg.MplsStatic.DefaultVrf.Afs.Af.TopLabelHash>`
                
                

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


                class LocalLabels(object):
                    """
                    Local Label
                    
                    .. attribute:: local_label
                    
                    	Specify Local Label
                    	**type**\: list of :py:class:`LocalLabel <ydk.models.mpls.Cisco_IOS_XR_mpls_static_cfg.MplsStatic.DefaultVrf.Afs.Af.LocalLabels.LocalLabel>`
                    
                    

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
                        
                        .. attribute:: local_label_id
                        
                        	Local Label
                        	**type**\: int
                        
                        	**range:** 16..1048575
                        
                        .. attribute:: label_type
                        
                        	MPLS Static Local Label Value
                        	**type**\: :py:class:`LabelType <ydk.models.mpls.Cisco_IOS_XR_mpls_static_cfg.MplsStatic.DefaultVrf.Afs.Af.LocalLabels.LocalLabel.LabelType>`
                        
                        .. attribute:: paths
                        
                        	Forward Path Parameters
                        	**type**\: :py:class:`Paths <ydk.models.mpls.Cisco_IOS_XR_mpls_static_cfg.MplsStatic.DefaultVrf.Afs.Af.LocalLabels.LocalLabel.Paths>`
                        
                        

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
                            	**type**\: :py:class:`MplsStaticLabelModeEnum <ydk.models.mpls.Cisco_IOS_XR_mpls_static_cfg.MplsStaticLabelModeEnum>`
                            
                            .. attribute:: prefix
                            
                            	Address (IPv4/6 depending on AFI)
                            	**type**\: one of { str | str }
                            
                            .. attribute:: prefix_length
                            
                            	Prefix length
                            	**type**\: int
                            
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
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-mpls-static-cfg:label-type'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.label_mode is not None:
                                    return True

                                if self.prefix is not None:
                                    return True

                                if self.prefix_length is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_static_cfg as meta
                                return meta._meta_table['MplsStatic.DefaultVrf.Afs.Af.LocalLabels.LocalLabel.LabelType']['meta_info']


                        class Paths(object):
                            """
                            Forward Path Parameters
                            
                            .. attribute:: path
                            
                            	Path Information
                            	**type**\: list of :py:class:`Path <ydk.models.mpls.Cisco_IOS_XR_mpls_static_cfg.MplsStatic.DefaultVrf.Afs.Af.LocalLabels.LocalLabel.Paths.Path>`
                            
                            

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
                                
                                .. attribute:: path_id
                                
                                	Number of paths
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: interface_name
                                
                                	Next hop Interface with form <Interface>R/S/I/P
                                	**type**\: str
                                
                                	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                                
                                .. attribute:: label_type
                                
                                	Type of label (Outlabel, ExpNull or Pop)
                                	**type**\: :py:class:`MplsStaticOutLabelTypesEnum <ydk.models.mpls.Cisco_IOS_XR_mpls_static_cfg.MplsStaticOutLabelTypesEnum>`
                                
                                .. attribute:: next_hop_address
                                
                                	Next Hop IPv4 Address
                                	**type**\: one of { str | str }
                                
                                .. attribute:: next_hop_label
                                
                                	NH Label
                                	**type**\: int
                                
                                	**range:** 16..1048575
                                
                                .. attribute:: path_type
                                
                                	Type of Path (PopAndLookup, CrossConnect)
                                	**type**\: :py:class:`MplsStaticPathEnum <ydk.models.mpls.Cisco_IOS_XR_mpls_static_cfg.MplsStaticPathEnum>`
                                
                                

                                """

                                _prefix = 'mpls-static-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.path_id = None
                                    self.interface_name = None
                                    self.label_type = None
                                    self.next_hop_address = None
                                    self.next_hop_label = None
                                    self.path_type = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')
                                    if self.path_id is None:
                                        raise YPYDataValidationError('Key property path_id is None')

                                    return self.parent._common_path +'/Cisco-IOS-XR-mpls-static-cfg:path[Cisco-IOS-XR-mpls-static-cfg:path-id = ' + str(self.path_id) + ']'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.path_id is not None:
                                        return True

                                    if self.interface_name is not None:
                                        return True

                                    if self.label_type is not None:
                                        return True

                                    if self.next_hop_address is not None:
                                        return True

                                    if self.next_hop_label is not None:
                                        return True

                                    if self.path_type is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_static_cfg as meta
                                    return meta._meta_table['MplsStatic.DefaultVrf.Afs.Af.LocalLabels.LocalLabel.Paths.Path']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-mpls-static-cfg:paths'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.path is not None:
                                    for child_ref in self.path:
                                        if child_ref._has_data():
                                            return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_static_cfg as meta
                                return meta._meta_table['MplsStatic.DefaultVrf.Afs.Af.LocalLabels.LocalLabel.Paths']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')
                            if self.local_label_id is None:
                                raise YPYDataValidationError('Key property local_label_id is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-mpls-static-cfg:local-label[Cisco-IOS-XR-mpls-static-cfg:local-label-id = ' + str(self.local_label_id) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.local_label_id is not None:
                                return True

                            if self.label_type is not None and self.label_type._has_data():
                                return True

                            if self.paths is not None and self.paths._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_static_cfg as meta
                            return meta._meta_table['MplsStatic.DefaultVrf.Afs.Af.LocalLabels.LocalLabel']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-mpls-static-cfg:local-labels'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

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
                        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_static_cfg as meta
                        return meta._meta_table['MplsStatic.DefaultVrf.Afs.Af.LocalLabels']['meta_info']


                class TopLabelHash(object):
                    """
                    Top Label Hash
                    
                    .. attribute:: local_labels
                    
                    	Local Label
                    	**type**\: :py:class:`LocalLabels <ydk.models.mpls.Cisco_IOS_XR_mpls_static_cfg.MplsStatic.DefaultVrf.Afs.Af.TopLabelHash.LocalLabels>`
                    
                    

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
                        	**type**\: list of :py:class:`LocalLabel <ydk.models.mpls.Cisco_IOS_XR_mpls_static_cfg.MplsStatic.DefaultVrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel>`
                        
                        

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
                            
                            .. attribute:: local_label_id
                            
                            	Local Label
                            	**type**\: int
                            
                            	**range:** 16..1048575
                            
                            .. attribute:: label_type
                            
                            	MPLS Static Local Label Value
                            	**type**\: :py:class:`LabelType <ydk.models.mpls.Cisco_IOS_XR_mpls_static_cfg.MplsStatic.DefaultVrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel.LabelType>`
                            
                            .. attribute:: paths
                            
                            	Forward Path Parameters
                            	**type**\: :py:class:`Paths <ydk.models.mpls.Cisco_IOS_XR_mpls_static_cfg.MplsStatic.DefaultVrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel.Paths>`
                            
                            

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
                                	**type**\: :py:class:`MplsStaticLabelModeEnum <ydk.models.mpls.Cisco_IOS_XR_mpls_static_cfg.MplsStaticLabelModeEnum>`
                                
                                .. attribute:: prefix
                                
                                	Address (IPv4/6 depending on AFI)
                                	**type**\: one of { str | str }
                                
                                .. attribute:: prefix_length
                                
                                	Prefix length
                                	**type**\: int
                                
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
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-mpls-static-cfg:label-type'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.label_mode is not None:
                                        return True

                                    if self.prefix is not None:
                                        return True

                                    if self.prefix_length is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_static_cfg as meta
                                    return meta._meta_table['MplsStatic.DefaultVrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel.LabelType']['meta_info']


                            class Paths(object):
                                """
                                Forward Path Parameters
                                
                                .. attribute:: path
                                
                                	Path Information
                                	**type**\: list of :py:class:`Path <ydk.models.mpls.Cisco_IOS_XR_mpls_static_cfg.MplsStatic.DefaultVrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel.Paths.Path>`
                                
                                

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
                                    
                                    .. attribute:: path_id
                                    
                                    	Number of paths
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: interface_name
                                    
                                    	Next hop Interface with form <Interface>R/S/I/P
                                    	**type**\: str
                                    
                                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                                    
                                    .. attribute:: label_type
                                    
                                    	Type of label (Outlabel, ExpNull or Pop)
                                    	**type**\: :py:class:`MplsStaticOutLabelTypesEnum <ydk.models.mpls.Cisco_IOS_XR_mpls_static_cfg.MplsStaticOutLabelTypesEnum>`
                                    
                                    .. attribute:: next_hop_address
                                    
                                    	Next Hop IPv4 Address
                                    	**type**\: one of { str | str }
                                    
                                    .. attribute:: next_hop_label
                                    
                                    	NH Label
                                    	**type**\: int
                                    
                                    	**range:** 16..1048575
                                    
                                    .. attribute:: path_type
                                    
                                    	Type of Path (PopAndLookup, CrossConnect)
                                    	**type**\: :py:class:`MplsStaticPathEnum <ydk.models.mpls.Cisco_IOS_XR_mpls_static_cfg.MplsStaticPathEnum>`
                                    
                                    

                                    """

                                    _prefix = 'mpls-static-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.path_id = None
                                        self.interface_name = None
                                        self.label_type = None
                                        self.next_hop_address = None
                                        self.next_hop_label = None
                                        self.path_type = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYDataValidationError('parent is not set . Cannot derive path.')
                                        if self.path_id is None:
                                            raise YPYDataValidationError('Key property path_id is None')

                                        return self.parent._common_path +'/Cisco-IOS-XR-mpls-static-cfg:path[Cisco-IOS-XR-mpls-static-cfg:path-id = ' + str(self.path_id) + ']'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if not self.is_config():
                                            return False
                                        if self.path_id is not None:
                                            return True

                                        if self.interface_name is not None:
                                            return True

                                        if self.label_type is not None:
                                            return True

                                        if self.next_hop_address is not None:
                                            return True

                                        if self.next_hop_label is not None:
                                            return True

                                        if self.path_type is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_static_cfg as meta
                                        return meta._meta_table['MplsStatic.DefaultVrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel.Paths.Path']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-mpls-static-cfg:paths'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.path is not None:
                                        for child_ref in self.path:
                                            if child_ref._has_data():
                                                return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_static_cfg as meta
                                    return meta._meta_table['MplsStatic.DefaultVrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel.Paths']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')
                                if self.local_label_id is None:
                                    raise YPYDataValidationError('Key property local_label_id is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-mpls-static-cfg:local-label[Cisco-IOS-XR-mpls-static-cfg:local-label-id = ' + str(self.local_label_id) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.local_label_id is not None:
                                    return True

                                if self.label_type is not None and self.label_type._has_data():
                                    return True

                                if self.paths is not None and self.paths._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_static_cfg as meta
                                return meta._meta_table['MplsStatic.DefaultVrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-mpls-static-cfg:local-labels'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

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
                            from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_static_cfg as meta
                            return meta._meta_table['MplsStatic.DefaultVrf.Afs.Af.TopLabelHash.LocalLabels']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-mpls-static-cfg:top-label-hash'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.local_labels is not None and self.local_labels._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_static_cfg as meta
                        return meta._meta_table['MplsStatic.DefaultVrf.Afs.Af.TopLabelHash']['meta_info']

                @property
                def _common_path(self):
                    if self.afi is None:
                        raise YPYDataValidationError('Key property afi is None')

                    return '/Cisco-IOS-XR-mpls-static-cfg:mpls-static/Cisco-IOS-XR-mpls-static-cfg:default-vrf/Cisco-IOS-XR-mpls-static-cfg:afs/Cisco-IOS-XR-mpls-static-cfg:af[Cisco-IOS-XR-mpls-static-cfg:afi = ' + str(self.afi) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
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
                    from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_static_cfg as meta
                    return meta._meta_table['MplsStatic.DefaultVrf.Afs.Af']['meta_info']

            @property
            def _common_path(self):

                return '/Cisco-IOS-XR-mpls-static-cfg:mpls-static/Cisco-IOS-XR-mpls-static-cfg:default-vrf/Cisco-IOS-XR-mpls-static-cfg:afs'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.af is not None:
                    for child_ref in self.af:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_static_cfg as meta
                return meta._meta_table['MplsStatic.DefaultVrf.Afs']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-mpls-static-cfg:mpls-static/Cisco-IOS-XR-mpls-static-cfg:default-vrf'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.afs is not None and self.afs._has_data():
                return True

            if self.enable is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_static_cfg as meta
            return meta._meta_table['MplsStatic.DefaultVrf']['meta_info']


    class Interfaces(object):
        """
        MPLS Static Interface Table
        
        .. attribute:: interface
        
        	MPLS Static Interface Enable
        	**type**\: list of :py:class:`Interface <ydk.models.mpls.Cisco_IOS_XR_mpls_static_cfg.MplsStatic.Interfaces.Interface>`
        
        

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
            
            .. attribute:: interface_name
            
            	Name of Interface
            	**type**\: str
            
            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
            
            

            """

            _prefix = 'mpls-static-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.interface_name = None

            @property
            def _common_path(self):
                if self.interface_name is None:
                    raise YPYDataValidationError('Key property interface_name is None')

                return '/Cisco-IOS-XR-mpls-static-cfg:mpls-static/Cisco-IOS-XR-mpls-static-cfg:interfaces/Cisco-IOS-XR-mpls-static-cfg:interface[Cisco-IOS-XR-mpls-static-cfg:interface-name = ' + str(self.interface_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.interface_name is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_static_cfg as meta
                return meta._meta_table['MplsStatic.Interfaces.Interface']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-mpls-static-cfg:mpls-static/Cisco-IOS-XR-mpls-static-cfg:interfaces'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.interface is not None:
                for child_ref in self.interface:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_static_cfg as meta
            return meta._meta_table['MplsStatic.Interfaces']['meta_info']


    class Vrfs(object):
        """
        VRF table
        
        .. attribute:: vrf
        
        	VRF Name
        	**type**\: list of :py:class:`Vrf <ydk.models.mpls.Cisco_IOS_XR_mpls_static_cfg.MplsStatic.Vrfs.Vrf>`
        
        

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
            
            .. attribute:: vrf_name
            
            	VRF Name
            	**type**\: str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: afs
            
            	Address Family Table
            	**type**\: :py:class:`Afs <ydk.models.mpls.Cisco_IOS_XR_mpls_static_cfg.MplsStatic.Vrfs.Vrf.Afs>`
            
            .. attribute:: enable
            
            	MPLS Static Apply Enable
            	**type**\: :py:class:`Empty <ydk.types.Empty>`
            
            

            """

            _prefix = 'mpls-static-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.vrf_name = None
                self.afs = MplsStatic.Vrfs.Vrf.Afs()
                self.afs.parent = self
                self.enable = None


            class Afs(object):
                """
                Address Family Table
                
                .. attribute:: af
                
                	Address Family
                	**type**\: list of :py:class:`Af <ydk.models.mpls.Cisco_IOS_XR_mpls_static_cfg.MplsStatic.Vrfs.Vrf.Afs.Af>`
                
                

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
                    
                    .. attribute:: afi
                    
                    	Address Family
                    	**type**\: :py:class:`MplsStaticAddressFamilyEnum <ydk.models.mpls.Cisco_IOS_XR_mpls_static_cfg.MplsStaticAddressFamilyEnum>`
                    
                    .. attribute:: enable
                    
                    	MPLS Static Apply Enable
                    	**type**\: :py:class:`Empty <ydk.types.Empty>`
                    
                    .. attribute:: local_labels
                    
                    	Local Label
                    	**type**\: :py:class:`LocalLabels <ydk.models.mpls.Cisco_IOS_XR_mpls_static_cfg.MplsStatic.Vrfs.Vrf.Afs.Af.LocalLabels>`
                    
                    .. attribute:: top_label_hash
                    
                    	Top Label Hash
                    	**type**\: :py:class:`TopLabelHash <ydk.models.mpls.Cisco_IOS_XR_mpls_static_cfg.MplsStatic.Vrfs.Vrf.Afs.Af.TopLabelHash>`
                    
                    

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


                    class LocalLabels(object):
                        """
                        Local Label
                        
                        .. attribute:: local_label
                        
                        	Specify Local Label
                        	**type**\: list of :py:class:`LocalLabel <ydk.models.mpls.Cisco_IOS_XR_mpls_static_cfg.MplsStatic.Vrfs.Vrf.Afs.Af.LocalLabels.LocalLabel>`
                        
                        

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
                            
                            .. attribute:: local_label_id
                            
                            	Local Label
                            	**type**\: int
                            
                            	**range:** 16..1048575
                            
                            .. attribute:: label_type
                            
                            	MPLS Static Local Label Value
                            	**type**\: :py:class:`LabelType <ydk.models.mpls.Cisco_IOS_XR_mpls_static_cfg.MplsStatic.Vrfs.Vrf.Afs.Af.LocalLabels.LocalLabel.LabelType>`
                            
                            .. attribute:: paths
                            
                            	Forward Path Parameters
                            	**type**\: :py:class:`Paths <ydk.models.mpls.Cisco_IOS_XR_mpls_static_cfg.MplsStatic.Vrfs.Vrf.Afs.Af.LocalLabels.LocalLabel.Paths>`
                            
                            

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
                                	**type**\: :py:class:`MplsStaticLabelModeEnum <ydk.models.mpls.Cisco_IOS_XR_mpls_static_cfg.MplsStaticLabelModeEnum>`
                                
                                .. attribute:: prefix
                                
                                	Address (IPv4/6 depending on AFI)
                                	**type**\: one of { str | str }
                                
                                .. attribute:: prefix_length
                                
                                	Prefix length
                                	**type**\: int
                                
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
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-mpls-static-cfg:label-type'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.label_mode is not None:
                                        return True

                                    if self.prefix is not None:
                                        return True

                                    if self.prefix_length is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_static_cfg as meta
                                    return meta._meta_table['MplsStatic.Vrfs.Vrf.Afs.Af.LocalLabels.LocalLabel.LabelType']['meta_info']


                            class Paths(object):
                                """
                                Forward Path Parameters
                                
                                .. attribute:: path
                                
                                	Path Information
                                	**type**\: list of :py:class:`Path <ydk.models.mpls.Cisco_IOS_XR_mpls_static_cfg.MplsStatic.Vrfs.Vrf.Afs.Af.LocalLabels.LocalLabel.Paths.Path>`
                                
                                

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
                                    
                                    .. attribute:: path_id
                                    
                                    	Number of paths
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: interface_name
                                    
                                    	Next hop Interface with form <Interface>R/S/I/P
                                    	**type**\: str
                                    
                                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                                    
                                    .. attribute:: label_type
                                    
                                    	Type of label (Outlabel, ExpNull or Pop)
                                    	**type**\: :py:class:`MplsStaticOutLabelTypesEnum <ydk.models.mpls.Cisco_IOS_XR_mpls_static_cfg.MplsStaticOutLabelTypesEnum>`
                                    
                                    .. attribute:: next_hop_address
                                    
                                    	Next Hop IPv4 Address
                                    	**type**\: one of { str | str }
                                    
                                    .. attribute:: next_hop_label
                                    
                                    	NH Label
                                    	**type**\: int
                                    
                                    	**range:** 16..1048575
                                    
                                    .. attribute:: path_type
                                    
                                    	Type of Path (PopAndLookup, CrossConnect)
                                    	**type**\: :py:class:`MplsStaticPathEnum <ydk.models.mpls.Cisco_IOS_XR_mpls_static_cfg.MplsStaticPathEnum>`
                                    
                                    

                                    """

                                    _prefix = 'mpls-static-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.path_id = None
                                        self.interface_name = None
                                        self.label_type = None
                                        self.next_hop_address = None
                                        self.next_hop_label = None
                                        self.path_type = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYDataValidationError('parent is not set . Cannot derive path.')
                                        if self.path_id is None:
                                            raise YPYDataValidationError('Key property path_id is None')

                                        return self.parent._common_path +'/Cisco-IOS-XR-mpls-static-cfg:path[Cisco-IOS-XR-mpls-static-cfg:path-id = ' + str(self.path_id) + ']'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if not self.is_config():
                                            return False
                                        if self.path_id is not None:
                                            return True

                                        if self.interface_name is not None:
                                            return True

                                        if self.label_type is not None:
                                            return True

                                        if self.next_hop_address is not None:
                                            return True

                                        if self.next_hop_label is not None:
                                            return True

                                        if self.path_type is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_static_cfg as meta
                                        return meta._meta_table['MplsStatic.Vrfs.Vrf.Afs.Af.LocalLabels.LocalLabel.Paths.Path']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-mpls-static-cfg:paths'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.path is not None:
                                        for child_ref in self.path:
                                            if child_ref._has_data():
                                                return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_static_cfg as meta
                                    return meta._meta_table['MplsStatic.Vrfs.Vrf.Afs.Af.LocalLabels.LocalLabel.Paths']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')
                                if self.local_label_id is None:
                                    raise YPYDataValidationError('Key property local_label_id is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-mpls-static-cfg:local-label[Cisco-IOS-XR-mpls-static-cfg:local-label-id = ' + str(self.local_label_id) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.local_label_id is not None:
                                    return True

                                if self.label_type is not None and self.label_type._has_data():
                                    return True

                                if self.paths is not None and self.paths._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_static_cfg as meta
                                return meta._meta_table['MplsStatic.Vrfs.Vrf.Afs.Af.LocalLabels.LocalLabel']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-mpls-static-cfg:local-labels'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

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
                            from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_static_cfg as meta
                            return meta._meta_table['MplsStatic.Vrfs.Vrf.Afs.Af.LocalLabels']['meta_info']


                    class TopLabelHash(object):
                        """
                        Top Label Hash
                        
                        .. attribute:: local_labels
                        
                        	Local Label
                        	**type**\: :py:class:`LocalLabels <ydk.models.mpls.Cisco_IOS_XR_mpls_static_cfg.MplsStatic.Vrfs.Vrf.Afs.Af.TopLabelHash.LocalLabels>`
                        
                        

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
                            	**type**\: list of :py:class:`LocalLabel <ydk.models.mpls.Cisco_IOS_XR_mpls_static_cfg.MplsStatic.Vrfs.Vrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel>`
                            
                            

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
                                
                                .. attribute:: local_label_id
                                
                                	Local Label
                                	**type**\: int
                                
                                	**range:** 16..1048575
                                
                                .. attribute:: label_type
                                
                                	MPLS Static Local Label Value
                                	**type**\: :py:class:`LabelType <ydk.models.mpls.Cisco_IOS_XR_mpls_static_cfg.MplsStatic.Vrfs.Vrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel.LabelType>`
                                
                                .. attribute:: paths
                                
                                	Forward Path Parameters
                                	**type**\: :py:class:`Paths <ydk.models.mpls.Cisco_IOS_XR_mpls_static_cfg.MplsStatic.Vrfs.Vrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel.Paths>`
                                
                                

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
                                    	**type**\: :py:class:`MplsStaticLabelModeEnum <ydk.models.mpls.Cisco_IOS_XR_mpls_static_cfg.MplsStaticLabelModeEnum>`
                                    
                                    .. attribute:: prefix
                                    
                                    	Address (IPv4/6 depending on AFI)
                                    	**type**\: one of { str | str }
                                    
                                    .. attribute:: prefix_length
                                    
                                    	Prefix length
                                    	**type**\: int
                                    
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
                                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-mpls-static-cfg:label-type'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if not self.is_config():
                                            return False
                                        if self.label_mode is not None:
                                            return True

                                        if self.prefix is not None:
                                            return True

                                        if self.prefix_length is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_static_cfg as meta
                                        return meta._meta_table['MplsStatic.Vrfs.Vrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel.LabelType']['meta_info']


                                class Paths(object):
                                    """
                                    Forward Path Parameters
                                    
                                    .. attribute:: path
                                    
                                    	Path Information
                                    	**type**\: list of :py:class:`Path <ydk.models.mpls.Cisco_IOS_XR_mpls_static_cfg.MplsStatic.Vrfs.Vrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel.Paths.Path>`
                                    
                                    

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
                                        
                                        .. attribute:: path_id
                                        
                                        	Number of paths
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: interface_name
                                        
                                        	Next hop Interface with form <Interface>R/S/I/P
                                        	**type**\: str
                                        
                                        	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                                        
                                        .. attribute:: label_type
                                        
                                        	Type of label (Outlabel, ExpNull or Pop)
                                        	**type**\: :py:class:`MplsStaticOutLabelTypesEnum <ydk.models.mpls.Cisco_IOS_XR_mpls_static_cfg.MplsStaticOutLabelTypesEnum>`
                                        
                                        .. attribute:: next_hop_address
                                        
                                        	Next Hop IPv4 Address
                                        	**type**\: one of { str | str }
                                        
                                        .. attribute:: next_hop_label
                                        
                                        	NH Label
                                        	**type**\: int
                                        
                                        	**range:** 16..1048575
                                        
                                        .. attribute:: path_type
                                        
                                        	Type of Path (PopAndLookup, CrossConnect)
                                        	**type**\: :py:class:`MplsStaticPathEnum <ydk.models.mpls.Cisco_IOS_XR_mpls_static_cfg.MplsStaticPathEnum>`
                                        
                                        

                                        """

                                        _prefix = 'mpls-static-cfg'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.path_id = None
                                            self.interface_name = None
                                            self.label_type = None
                                            self.next_hop_address = None
                                            self.next_hop_label = None
                                            self.path_type = None

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYDataValidationError('parent is not set . Cannot derive path.')
                                            if self.path_id is None:
                                                raise YPYDataValidationError('Key property path_id is None')

                                            return self.parent._common_path +'/Cisco-IOS-XR-mpls-static-cfg:path[Cisco-IOS-XR-mpls-static-cfg:path-id = ' + str(self.path_id) + ']'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return True

                                        def _has_data(self):
                                            if not self.is_config():
                                                return False
                                            if self.path_id is not None:
                                                return True

                                            if self.interface_name is not None:
                                                return True

                                            if self.label_type is not None:
                                                return True

                                            if self.next_hop_address is not None:
                                                return True

                                            if self.next_hop_label is not None:
                                                return True

                                            if self.path_type is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_static_cfg as meta
                                            return meta._meta_table['MplsStatic.Vrfs.Vrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel.Paths.Path']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-mpls-static-cfg:paths'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return True

                                    def _has_data(self):
                                        if not self.is_config():
                                            return False
                                        if self.path is not None:
                                            for child_ref in self.path:
                                                if child_ref._has_data():
                                                    return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_static_cfg as meta
                                        return meta._meta_table['MplsStatic.Vrfs.Vrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel.Paths']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')
                                    if self.local_label_id is None:
                                        raise YPYDataValidationError('Key property local_label_id is None')

                                    return self.parent._common_path +'/Cisco-IOS-XR-mpls-static-cfg:local-label[Cisco-IOS-XR-mpls-static-cfg:local-label-id = ' + str(self.local_label_id) + ']'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.local_label_id is not None:
                                        return True

                                    if self.label_type is not None and self.label_type._has_data():
                                        return True

                                    if self.paths is not None and self.paths._has_data():
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_static_cfg as meta
                                    return meta._meta_table['MplsStatic.Vrfs.Vrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-mpls-static-cfg:local-labels'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

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
                                from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_static_cfg as meta
                                return meta._meta_table['MplsStatic.Vrfs.Vrf.Afs.Af.TopLabelHash.LocalLabels']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-mpls-static-cfg:top-label-hash'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.local_labels is not None and self.local_labels._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_static_cfg as meta
                            return meta._meta_table['MplsStatic.Vrfs.Vrf.Afs.Af.TopLabelHash']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')
                        if self.afi is None:
                            raise YPYDataValidationError('Key property afi is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-mpls-static-cfg:af[Cisco-IOS-XR-mpls-static-cfg:afi = ' + str(self.afi) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
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
                        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_static_cfg as meta
                        return meta._meta_table['MplsStatic.Vrfs.Vrf.Afs.Af']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-mpls-static-cfg:afs'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.af is not None:
                        for child_ref in self.af:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_static_cfg as meta
                    return meta._meta_table['MplsStatic.Vrfs.Vrf.Afs']['meta_info']

            @property
            def _common_path(self):
                if self.vrf_name is None:
                    raise YPYDataValidationError('Key property vrf_name is None')

                return '/Cisco-IOS-XR-mpls-static-cfg:mpls-static/Cisco-IOS-XR-mpls-static-cfg:vrfs/Cisco-IOS-XR-mpls-static-cfg:vrf[Cisco-IOS-XR-mpls-static-cfg:vrf-name = ' + str(self.vrf_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.vrf_name is not None:
                    return True

                if self.afs is not None and self.afs._has_data():
                    return True

                if self.enable is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_static_cfg as meta
                return meta._meta_table['MplsStatic.Vrfs.Vrf']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-mpls-static-cfg:mpls-static/Cisco-IOS-XR-mpls-static-cfg:vrfs'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

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
            from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_static_cfg as meta
            return meta._meta_table['MplsStatic.Vrfs']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-mpls-static-cfg:mpls-static'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if not self.is_config():
            return False
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
        from ydk.models.mpls._meta import _Cisco_IOS_XR_mpls_static_cfg as meta
        return meta._meta_table['MplsStatic']['meta_info']


