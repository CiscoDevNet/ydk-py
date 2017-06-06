""" Cisco_IOS_XR_ip_iep_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ip\-iep package configuration.

This module contains definitions
for the following management objects\:
  ip\-explicit\-paths\: IP Explicit Path config data

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class IpIepHopEnum(Enum):
    """
    IpIepHopEnum

    Ip iep hop

    .. data:: next_strict = 2

    	NextStrict

    .. data:: next_loose = 3

    	NextLoose

    .. data:: exclude = 4

    	Exclude

    .. data:: exclude_srlg = 5

    	Exclude Shared Risk Link Group

    .. data:: next_label = 6

    	NextLabel

    """

    next_strict = 2

    next_loose = 3

    exclude = 4

    exclude_srlg = 5

    next_label = 6


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_iep_cfg as meta
        return meta._meta_table['IpIepHopEnum']


class IpIepNumEnum(Enum):
    """
    IpIepNumEnum

    Ip iep num

    .. data:: unnumbered = 1

    	Unnumbered

    .. data:: numbered = 2

    	Numbered

    """

    unnumbered = 1

    numbered = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_iep_cfg as meta
        return meta._meta_table['IpIepNumEnum']


class IpIepPathEnum(Enum):
    """
    IpIepPathEnum

    Ip iep path

    .. data:: identifier = 1

    	Identifier

    .. data:: name = 2

    	Name

    """

    identifier = 1

    name = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_iep_cfg as meta
        return meta._meta_table['IpIepPathEnum']



class IpExplicitPaths(object):
    """
    IP Explicit Path config data
    
    .. attribute:: paths
    
    	A list of explicit paths
    	**type**\:   :py:class:`Paths <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iep_cfg.IpExplicitPaths.Paths>`
    
    

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
        	**type**\: list of    :py:class:`Path <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iep_cfg.IpExplicitPaths.Paths.Path>`
        
        

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
            
            .. attribute:: type  <key>
            
            	Path type
            	**type**\:   :py:class:`IpIepPathEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iep_cfg.IpIepPathEnum>`
            
            .. attribute:: identifier
            
            	identifier
            	**type**\: list of    :py:class:`Identifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iep_cfg.IpExplicitPaths.Paths.Path.Identifier>`
            
            .. attribute:: name
            
            	name
            	**type**\: list of    :py:class:`Name <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iep_cfg.IpExplicitPaths.Paths.Path.Name>`
            
            

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


            class Name(object):
                """
                name
                
                .. attribute:: name  <key>
                
                	Path name
                	**type**\:  str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: disable
                
                	Disable the explicit path
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: hops
                
                	List of Hops
                	**type**\:   :py:class:`Hops <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iep_cfg.IpExplicitPaths.Paths.Path.Name.Hops>`
                
                

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
                    	**type**\: list of    :py:class:`Hop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iep_cfg.IpExplicitPaths.Paths.Path.Name.Hops.Hop>`
                    
                    

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
                        
                        .. attribute:: index_number  <key>
                        
                        	Index number
                        	**type**\:  int
                        
                        	**range:** 1..65535
                        
                        .. attribute:: hop_type
                        
                        	Include or exclude this hop in the path
                        	**type**\:   :py:class:`IpIepHopEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iep_cfg.IpIepHopEnum>`
                        
                        	**default value**\: next-strict
                        
                        .. attribute:: if_index
                        
                        	Ifindex value
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        	**default value**\: 0
                        
                        .. attribute:: ip_address
                        
                        	IP address of the hop
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        	**default value**\: 0.0.0.0
                        
                        .. attribute:: mpls_label
                        
                        	MPLS Label
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: num_type
                        
                        	Number type Numbered or Unnumbered
                        	**type**\:   :py:class:`IpIepNumEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iep_cfg.IpIepNumEnum>`
                        
                        	**default value**\: numbered
                        
                        

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
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.index_number is None:
                                raise YPYModelError('Key property index_number is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-ip-iep-cfg:hop[Cisco-IOS-XR-ip-iep-cfg:index-number = ' + str(self.index_number) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
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

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_iep_cfg as meta
                            return meta._meta_table['IpExplicitPaths.Paths.Path.Name.Hops.Hop']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ip-iep-cfg:hops'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.hop is not None:
                            for child_ref in self.hop:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_iep_cfg as meta
                        return meta._meta_table['IpExplicitPaths.Paths.Path.Name.Hops']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')
                    if self.name is None:
                        raise YPYModelError('Key property name is None')

                    return self.parent._common_path +'/Cisco-IOS-XR-ip-iep-cfg:name[Cisco-IOS-XR-ip-iep-cfg:name = ' + str(self.name) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.name is not None:
                        return True

                    if self.disable is not None:
                        return True

                    if self.hops is not None and self.hops._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_iep_cfg as meta
                    return meta._meta_table['IpExplicitPaths.Paths.Path.Name']['meta_info']


            class Identifier(object):
                """
                identifier
                
                .. attribute:: id  <key>
                
                	Path identifier
                	**type**\:  int
                
                	**range:** 1..65535
                
                .. attribute:: disable
                
                	Disable the explicit path
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: hops
                
                	List of Hops
                	**type**\:   :py:class:`Hops <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iep_cfg.IpExplicitPaths.Paths.Path.Identifier.Hops>`
                
                

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
                    	**type**\: list of    :py:class:`Hop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iep_cfg.IpExplicitPaths.Paths.Path.Identifier.Hops.Hop>`
                    
                    

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
                        
                        .. attribute:: index_number  <key>
                        
                        	Index number
                        	**type**\:  int
                        
                        	**range:** 1..65535
                        
                        .. attribute:: hop_type
                        
                        	Include or exclude this hop in the path
                        	**type**\:   :py:class:`IpIepHopEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iep_cfg.IpIepHopEnum>`
                        
                        	**default value**\: next-strict
                        
                        .. attribute:: if_index
                        
                        	Ifindex value
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        	**default value**\: 0
                        
                        .. attribute:: ip_address
                        
                        	IP address of the hop
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        	**default value**\: 0.0.0.0
                        
                        .. attribute:: mpls_label
                        
                        	MPLS Label
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: num_type
                        
                        	Number type Numbered or Unnumbered
                        	**type**\:   :py:class:`IpIepNumEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iep_cfg.IpIepNumEnum>`
                        
                        	**default value**\: numbered
                        
                        

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
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.index_number is None:
                                raise YPYModelError('Key property index_number is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-ip-iep-cfg:hop[Cisco-IOS-XR-ip-iep-cfg:index-number = ' + str(self.index_number) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
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

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_iep_cfg as meta
                            return meta._meta_table['IpExplicitPaths.Paths.Path.Identifier.Hops.Hop']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ip-iep-cfg:hops'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.hop is not None:
                            for child_ref in self.hop:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_iep_cfg as meta
                        return meta._meta_table['IpExplicitPaths.Paths.Path.Identifier.Hops']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')
                    if self.id is None:
                        raise YPYModelError('Key property id is None')

                    return self.parent._common_path +'/Cisco-IOS-XR-ip-iep-cfg:identifier[Cisco-IOS-XR-ip-iep-cfg:id = ' + str(self.id) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.id is not None:
                        return True

                    if self.disable is not None:
                        return True

                    if self.hops is not None and self.hops._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_iep_cfg as meta
                    return meta._meta_table['IpExplicitPaths.Paths.Path.Identifier']['meta_info']

            @property
            def _common_path(self):
                if self.type is None:
                    raise YPYModelError('Key property type is None')

                return '/Cisco-IOS-XR-ip-iep-cfg:ip-explicit-paths/Cisco-IOS-XR-ip-iep-cfg:paths/Cisco-IOS-XR-ip-iep-cfg:path[Cisco-IOS-XR-ip-iep-cfg:type = ' + str(self.type) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
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

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_iep_cfg as meta
                return meta._meta_table['IpExplicitPaths.Paths.Path']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ip-iep-cfg:ip-explicit-paths/Cisco-IOS-XR-ip-iep-cfg:paths'

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
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_iep_cfg as meta
            return meta._meta_table['IpExplicitPaths.Paths']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-ip-iep-cfg:ip-explicit-paths'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.paths is not None and self.paths._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_iep_cfg as meta
        return meta._meta_table['IpExplicitPaths']['meta_info']


