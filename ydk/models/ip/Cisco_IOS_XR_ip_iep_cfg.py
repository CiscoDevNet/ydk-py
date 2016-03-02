""" Cisco_IOS_XR_ip_iep_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ip\-iep package configuration.

This module contains definitions
for the following management objects\:
  ip\-explicit\-paths\: IP Explicit Path config data

Copyright (c) 2013\-2015 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError



class IpIepHop_Enum(Enum):
    """
    IpIepHop_Enum

    Ip iep hop

    """

    """

    NextStrict

    """
    NEXT_STRICT = 2

    """

    NextLoose

    """
    NEXT_LOOSE = 3

    """

    Exclude

    """
    EXCLUDE = 4

    """

    Exclude Shared Risk Link Group

    """
    EXCLUDE_SRLG = 5

    """

    NextLabel

    """
    NEXT_LABEL = 6


    @staticmethod
    def _meta_info():
        from ydk.models.ip._meta import _Cisco_IOS_XR_ip_iep_cfg as meta
        return meta._meta_table['IpIepHop_Enum']


class IpIepNum_Enum(Enum):
    """
    IpIepNum_Enum

    Ip iep num

    """

    """

    Unnumbered

    """
    UNNUMBERED = 1

    """

    Numbered

    """
    NUMBERED = 2


    @staticmethod
    def _meta_info():
        from ydk.models.ip._meta import _Cisco_IOS_XR_ip_iep_cfg as meta
        return meta._meta_table['IpIepNum_Enum']


class IpIepPath_Enum(Enum):
    """
    IpIepPath_Enum

    Ip iep path

    """

    """

    Identifier

    """
    IDENTIFIER = 1

    """

    Name

    """
    NAME = 2


    @staticmethod
    def _meta_info():
        from ydk.models.ip._meta import _Cisco_IOS_XR_ip_iep_cfg as meta
        return meta._meta_table['IpIepPath_Enum']



class IpExplicitPaths(object):
    """
    IP Explicit Path config data
    
    .. attribute:: paths
    
    	A list of explicit paths
    	**type**\: :py:class:`Paths <ydk.models.ip.Cisco_IOS_XR_ip_iep_cfg.IpExplicitPaths.Paths>`
    
    

    """

    _prefix = 'ip-iep-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        self.paths = IpExplicitPaths.Paths()
        self.paths.parent = self


    class Paths(object):
        """
        A list of explicit paths
        
        .. attribute:: path
        
        	Config data for a specific explicit path
        	**type**\: list of :py:class:`Path <ydk.models.ip.Cisco_IOS_XR_ip_iep_cfg.IpExplicitPaths.Paths.Path>`
        
        

        """

        _prefix = 'ip-iep-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.path = YList()
            self.path.parent = self
            self.path.name = 'path'


        class Path(object):
            """
            Config data for a specific explicit path
            
            .. attribute:: type
            
            	Path type
            	**type**\: :py:class:`IpIepPath_Enum <ydk.models.ip.Cisco_IOS_XR_ip_iep_cfg.IpIepPath_Enum>`
            
            .. attribute:: identifier
            
            	identifier
            	**type**\: list of :py:class:`Identifier <ydk.models.ip.Cisco_IOS_XR_ip_iep_cfg.IpExplicitPaths.Paths.Path.Identifier>`
            
            .. attribute:: name
            
            	name
            	**type**\: list of :py:class:`Name <ydk.models.ip.Cisco_IOS_XR_ip_iep_cfg.IpExplicitPaths.Paths.Path.Name>`
            
            

            """

            _prefix = 'ip-iep-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.type = None
                self.identifier = YList()
                self.identifier.parent = self
                self.identifier.name = 'identifier'
                self.name = YList()
                self.name.parent = self
                self.name.name = 'name'


            class Identifier(object):
                """
                identifier
                
                .. attribute:: id
                
                	Path identifier
                	**type**\: int
                
                	**range:** 1..65535
                
                .. attribute:: disable
                
                	Disable the explicit path
                	**type**\: :py:class:`Empty <ydk.types.Empty>`
                
                .. attribute:: hops
                
                	List of Hops
                	**type**\: :py:class:`Hops <ydk.models.ip.Cisco_IOS_XR_ip_iep_cfg.IpExplicitPaths.Paths.Path.Identifier.Hops>`
                
                

                """

                _prefix = 'ip-iep-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.id = None
                    self.disable = None
                    self.hops = IpExplicitPaths.Paths.Path.Identifier.Hops()
                    self.hops.parent = self


                class Hops(object):
                    """
                    List of Hops
                    
                    .. attribute:: hop
                    
                    	Hop Information
                    	**type**\: list of :py:class:`Hop <ydk.models.ip.Cisco_IOS_XR_ip_iep_cfg.IpExplicitPaths.Paths.Path.Identifier.Hops.Hop>`
                    
                    

                    """

                    _prefix = 'ip-iep-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.hop = YList()
                        self.hop.parent = self
                        self.hop.name = 'hop'


                    class Hop(object):
                        """
                        Hop Information
                        
                        .. attribute:: index_number
                        
                        	Index number
                        	**type**\: int
                        
                        	**range:** 1..65535
                        
                        .. attribute:: hop_type
                        
                        	Include or exclude this hop in the path
                        	**type**\: :py:class:`IpIepHop_Enum <ydk.models.ip.Cisco_IOS_XR_ip_iep_cfg.IpIepHop_Enum>`
                        
                        .. attribute:: if_index
                        
                        	Ifindex value
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: ip_address
                        
                        	IP address of the hop
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: mpls_label
                        
                        	MPLS Label
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: num_type
                        
                        	Number type Numbered or Unnumbered
                        	**type**\: :py:class:`IpIepNum_Enum <ydk.models.ip.Cisco_IOS_XR_ip_iep_cfg.IpIepNum_Enum>`
                        
                        

                        """

                        _prefix = 'ip-iep-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.index_number = None
                            self.hop_type = None
                            self.if_index = None
                            self.ip_address = None
                            self.mpls_label = None
                            self.num_type = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')
                            if self.index_number is None:
                                raise YPYDataValidationError('Key property index_number is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-ip-iep-cfg:hop[Cisco-IOS-XR-ip-iep-cfg:index-number = ' + str(self.index_number) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.is_presence():
                                return True
                            if self.index_number is not None:
                                return True

                            if self.hop_type is not None:
                                return True

                            if self.if_index is not None:
                                return True

                            if self.ip_address is not None:
                                return True

                            if self.mpls_label is not None:
                                return True

                            if self.num_type is not None:
                                return True

                            return False

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.ip._meta import _Cisco_IOS_XR_ip_iep_cfg as meta
                            return meta._meta_table['IpExplicitPaths.Paths.Path.Identifier.Hops.Hop']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ip-iep-cfg:hops'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.is_presence():
                            return True
                        if self.hop is not None:
                            for child_ref in self.hop:
                                if child_ref._has_data():
                                    return True

                        return False

                    def is_presence(self):
                        ''' Returns True if this instance represents presence container else returns False '''
                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.ip._meta import _Cisco_IOS_XR_ip_iep_cfg as meta
                        return meta._meta_table['IpExplicitPaths.Paths.Path.Identifier.Hops']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')
                    if self.id is None:
                        raise YPYDataValidationError('Key property id is None')

                    return self.parent._common_path +'/Cisco-IOS-XR-ip-iep-cfg:identifier[Cisco-IOS-XR-ip-iep-cfg:id = ' + str(self.id) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.is_presence():
                        return True
                    if self.id is not None:
                        return True

                    if self.disable is not None:
                        return True

                    if self.hops is not None and self.hops._has_data():
                        return True

                    if self.hops is not None and self.hops.is_presence():
                        return True

                    return False

                def is_presence(self):
                    ''' Returns True if this instance represents presence container else returns False '''
                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ip._meta import _Cisco_IOS_XR_ip_iep_cfg as meta
                    return meta._meta_table['IpExplicitPaths.Paths.Path.Identifier']['meta_info']


            class Name(object):
                """
                name
                
                .. attribute:: name
                
                	Path name
                	**type**\: str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: disable
                
                	Disable the explicit path
                	**type**\: :py:class:`Empty <ydk.types.Empty>`
                
                .. attribute:: hops
                
                	List of Hops
                	**type**\: :py:class:`Hops <ydk.models.ip.Cisco_IOS_XR_ip_iep_cfg.IpExplicitPaths.Paths.Path.Name.Hops>`
                
                

                """

                _prefix = 'ip-iep-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.name = None
                    self.disable = None
                    self.hops = IpExplicitPaths.Paths.Path.Name.Hops()
                    self.hops.parent = self


                class Hops(object):
                    """
                    List of Hops
                    
                    .. attribute:: hop
                    
                    	Hop Information
                    	**type**\: list of :py:class:`Hop <ydk.models.ip.Cisco_IOS_XR_ip_iep_cfg.IpExplicitPaths.Paths.Path.Name.Hops.Hop>`
                    
                    

                    """

                    _prefix = 'ip-iep-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.hop = YList()
                        self.hop.parent = self
                        self.hop.name = 'hop'


                    class Hop(object):
                        """
                        Hop Information
                        
                        .. attribute:: index_number
                        
                        	Index number
                        	**type**\: int
                        
                        	**range:** 1..65535
                        
                        .. attribute:: hop_type
                        
                        	Include or exclude this hop in the path
                        	**type**\: :py:class:`IpIepHop_Enum <ydk.models.ip.Cisco_IOS_XR_ip_iep_cfg.IpIepHop_Enum>`
                        
                        .. attribute:: if_index
                        
                        	Ifindex value
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: ip_address
                        
                        	IP address of the hop
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: mpls_label
                        
                        	MPLS Label
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: num_type
                        
                        	Number type Numbered or Unnumbered
                        	**type**\: :py:class:`IpIepNum_Enum <ydk.models.ip.Cisco_IOS_XR_ip_iep_cfg.IpIepNum_Enum>`
                        
                        

                        """

                        _prefix = 'ip-iep-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.index_number = None
                            self.hop_type = None
                            self.if_index = None
                            self.ip_address = None
                            self.mpls_label = None
                            self.num_type = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')
                            if self.index_number is None:
                                raise YPYDataValidationError('Key property index_number is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-ip-iep-cfg:hop[Cisco-IOS-XR-ip-iep-cfg:index-number = ' + str(self.index_number) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.is_presence():
                                return True
                            if self.index_number is not None:
                                return True

                            if self.hop_type is not None:
                                return True

                            if self.if_index is not None:
                                return True

                            if self.ip_address is not None:
                                return True

                            if self.mpls_label is not None:
                                return True

                            if self.num_type is not None:
                                return True

                            return False

                        def is_presence(self):
                            ''' Returns True if this instance represents presence container else returns False '''
                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.ip._meta import _Cisco_IOS_XR_ip_iep_cfg as meta
                            return meta._meta_table['IpExplicitPaths.Paths.Path.Name.Hops.Hop']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ip-iep-cfg:hops'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.is_presence():
                            return True
                        if self.hop is not None:
                            for child_ref in self.hop:
                                if child_ref._has_data():
                                    return True

                        return False

                    def is_presence(self):
                        ''' Returns True if this instance represents presence container else returns False '''
                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.ip._meta import _Cisco_IOS_XR_ip_iep_cfg as meta
                        return meta._meta_table['IpExplicitPaths.Paths.Path.Name.Hops']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')
                    if self.name is None:
                        raise YPYDataValidationError('Key property name is None')

                    return self.parent._common_path +'/Cisco-IOS-XR-ip-iep-cfg:name[Cisco-IOS-XR-ip-iep-cfg:name = ' + str(self.name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.is_presence():
                        return True
                    if self.name is not None:
                        return True

                    if self.disable is not None:
                        return True

                    if self.hops is not None and self.hops._has_data():
                        return True

                    if self.hops is not None and self.hops.is_presence():
                        return True

                    return False

                def is_presence(self):
                    ''' Returns True if this instance represents presence container else returns False '''
                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ip._meta import _Cisco_IOS_XR_ip_iep_cfg as meta
                    return meta._meta_table['IpExplicitPaths.Paths.Path.Name']['meta_info']

            @property
            def _common_path(self):
                if self.type is None:
                    raise YPYDataValidationError('Key property type is None')

                return '/Cisco-IOS-XR-ip-iep-cfg:ip-explicit-paths/Cisco-IOS-XR-ip-iep-cfg:paths/Cisco-IOS-XR-ip-iep-cfg:path[Cisco-IOS-XR-ip-iep-cfg:type = ' + str(self.type) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.type is not None:
                    return True

                if self.identifier is not None:
                    for child_ref in self.identifier:
                        if child_ref._has_data():
                            return True

                if self.name is not None:
                    for child_ref in self.name:
                        if child_ref._has_data():
                            return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ip._meta import _Cisco_IOS_XR_ip_iep_cfg as meta
                return meta._meta_table['IpExplicitPaths.Paths.Path']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ip-iep-cfg:ip-explicit-paths/Cisco-IOS-XR-ip-iep-cfg:paths'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.path is not None:
                for child_ref in self.path:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ip._meta import _Cisco_IOS_XR_ip_iep_cfg as meta
            return meta._meta_table['IpExplicitPaths.Paths']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-ip-iep-cfg:ip-explicit-paths'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if not self.is_config():
            return False
        if self.is_presence():
            return True
        if self.paths is not None and self.paths._has_data():
            return True

        if self.paths is not None and self.paths.is_presence():
            return True

        return False

    def is_presence(self):
        ''' Returns True if this instance represents presence container else returns False '''
        return False

    @staticmethod
    def _meta_info():
        from ydk.models.ip._meta import _Cisco_IOS_XR_ip_iep_cfg as meta
        return meta._meta_table['IpExplicitPaths']['meta_info']


