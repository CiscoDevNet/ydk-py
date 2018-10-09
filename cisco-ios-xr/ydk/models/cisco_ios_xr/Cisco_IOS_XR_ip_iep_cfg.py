""" Cisco_IOS_XR_ip_iep_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ip\-iep package configuration.

This module contains definitions
for the following management objects\:
  ip\-explicit\-paths\: IP Explicit Path config data

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class IpIepHop(Enum):
    """
    IpIepHop (Enum Class)

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

    next_strict = Enum.YLeaf(2, "next-strict")

    next_loose = Enum.YLeaf(3, "next-loose")

    exclude = Enum.YLeaf(4, "exclude")

    exclude_srlg = Enum.YLeaf(5, "exclude-srlg")

    next_label = Enum.YLeaf(6, "next-label")


class IpIepNum(Enum):
    """
    IpIepNum (Enum Class)

    Ip iep num

    .. data:: unnumbered = 1

    	Unnumbered

    .. data:: numbered = 2

    	Numbered

    """

    unnumbered = Enum.YLeaf(1, "unnumbered")

    numbered = Enum.YLeaf(2, "numbered")


class IpIepPath(Enum):
    """
    IpIepPath (Enum Class)

    Ip iep path

    .. data:: identifier = 1

    	Identifier

    .. data:: name = 2

    	Name

    """

    identifier = Enum.YLeaf(1, "identifier")

    name = Enum.YLeaf(2, "name")



class IpExplicitPaths(Entity):
    """
    IP Explicit Path config data
    
    .. attribute:: paths
    
    	A list of explicit paths
    	**type**\:  :py:class:`Paths <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iep_cfg.IpExplicitPaths.Paths>`
    
    

    """

    _prefix = 'ip-iep-cfg'
    _revision = '2017-09-07'

    def __init__(self):
        super(IpExplicitPaths, self).__init__()
        self._top_entity = None

        self.yang_name = "ip-explicit-paths"
        self.yang_parent_name = "Cisco-IOS-XR-ip-iep-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("paths", ("paths", IpExplicitPaths.Paths))])
        self._leafs = OrderedDict()

        self.paths = IpExplicitPaths.Paths()
        self.paths.parent = self
        self._children_name_map["paths"] = "paths"
        self._segment_path = lambda: "Cisco-IOS-XR-ip-iep-cfg:ip-explicit-paths"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(IpExplicitPaths, [], name, value)


    class Paths(Entity):
        """
        A list of explicit paths
        
        .. attribute:: path
        
        	Config data for a specific explicit path
        	**type**\: list of  		 :py:class:`Path <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iep_cfg.IpExplicitPaths.Paths.Path>`
        
        

        """

        _prefix = 'ip-iep-cfg'
        _revision = '2017-09-07'

        def __init__(self):
            super(IpExplicitPaths.Paths, self).__init__()

            self.yang_name = "paths"
            self.yang_parent_name = "ip-explicit-paths"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("path", ("path", IpExplicitPaths.Paths.Path))])
            self._leafs = OrderedDict()

            self.path = YList(self)
            self._segment_path = lambda: "paths"
            self._absolute_path = lambda: "Cisco-IOS-XR-ip-iep-cfg:ip-explicit-paths/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(IpExplicitPaths.Paths, [], name, value)


        class Path(Entity):
            """
            Config data for a specific explicit path
            
            .. attribute:: type  (key)
            
            	Path type
            	**type**\:  :py:class:`IpIepPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iep_cfg.IpIepPath>`
            
            .. attribute:: name
            
            	name
            	**type**\: list of  		 :py:class:`Name <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iep_cfg.IpExplicitPaths.Paths.Path.Name>`
            
            .. attribute:: identifier
            
            	identifier
            	**type**\: list of  		 :py:class:`Identifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iep_cfg.IpExplicitPaths.Paths.Path.Identifier>`
            
            

            """

            _prefix = 'ip-iep-cfg'
            _revision = '2017-09-07'

            def __init__(self):
                super(IpExplicitPaths.Paths.Path, self).__init__()

                self.yang_name = "path"
                self.yang_parent_name = "paths"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['type']
                self._child_classes = OrderedDict([("name", ("name", IpExplicitPaths.Paths.Path.Name)), ("identifier", ("identifier", IpExplicitPaths.Paths.Path.Identifier))])
                self._leafs = OrderedDict([
                    ('type', (YLeaf(YType.enumeration, 'type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iep_cfg', 'IpIepPath', '')])),
                ])
                self.type = None

                self.name = YList(self)
                self.identifier = YList(self)
                self._segment_path = lambda: "path" + "[type='" + str(self.type) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-ip-iep-cfg:ip-explicit-paths/paths/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(IpExplicitPaths.Paths.Path, ['type'], name, value)


            class Name(Entity):
                """
                name
                
                .. attribute:: name  (key)
                
                	Path name
                	**type**\: str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: hops
                
                	List of Hops
                	**type**\:  :py:class:`Hops <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iep_cfg.IpExplicitPaths.Paths.Path.Name.Hops>`
                
                .. attribute:: disable
                
                	Disable the explicit path
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                

                """

                _prefix = 'ip-iep-cfg'
                _revision = '2017-09-07'

                def __init__(self):
                    super(IpExplicitPaths.Paths.Path.Name, self).__init__()

                    self.yang_name = "name"
                    self.yang_parent_name = "path"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = ['name']
                    self._child_classes = OrderedDict([("hops", ("hops", IpExplicitPaths.Paths.Path.Name.Hops))])
                    self._leafs = OrderedDict([
                        ('name', (YLeaf(YType.str, 'name'), ['str'])),
                        ('disable', (YLeaf(YType.empty, 'disable'), ['Empty'])),
                    ])
                    self.name = None
                    self.disable = None

                    self.hops = IpExplicitPaths.Paths.Path.Name.Hops()
                    self.hops.parent = self
                    self._children_name_map["hops"] = "hops"
                    self._segment_path = lambda: "name" + "[name='" + str(self.name) + "']"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(IpExplicitPaths.Paths.Path.Name, ['name', 'disable'], name, value)


                class Hops(Entity):
                    """
                    List of Hops
                    
                    .. attribute:: hop
                    
                    	Hop Information
                    	**type**\: list of  		 :py:class:`Hop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iep_cfg.IpExplicitPaths.Paths.Path.Name.Hops.Hop>`
                    
                    

                    """

                    _prefix = 'ip-iep-cfg'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(IpExplicitPaths.Paths.Path.Name.Hops, self).__init__()

                        self.yang_name = "hops"
                        self.yang_parent_name = "name"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("hop", ("hop", IpExplicitPaths.Paths.Path.Name.Hops.Hop))])
                        self._leafs = OrderedDict()

                        self.hop = YList(self)
                        self._segment_path = lambda: "hops"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(IpExplicitPaths.Paths.Path.Name.Hops, [], name, value)


                    class Hop(Entity):
                        """
                        Hop Information
                        
                        .. attribute:: index_number  (key)
                        
                        	Index number
                        	**type**\: int
                        
                        	**range:** 1..65535
                        
                        .. attribute:: ip_address
                        
                        	IP address of the hop
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        	**default value**\: 0.0.0.0
                        
                        .. attribute:: hop_type
                        
                        	Include or exclude this hop in the path
                        	**type**\:  :py:class:`IpIepHop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iep_cfg.IpIepHop>`
                        
                        	**default value**\: next-strict
                        
                        .. attribute:: if_index
                        
                        	Ifindex value
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**default value**\: 0
                        
                        .. attribute:: num_type
                        
                        	Number type Numbered or Unnumbered
                        	**type**\:  :py:class:`IpIepNum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iep_cfg.IpIepNum>`
                        
                        	**default value**\: numbered
                        
                        .. attribute:: mpls_label
                        
                        	MPLS Label
                        	**type**\: int
                        
                        	**range:** 0..1048575
                        
                        

                        """

                        _prefix = 'ip-iep-cfg'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(IpExplicitPaths.Paths.Path.Name.Hops.Hop, self).__init__()

                            self.yang_name = "hop"
                            self.yang_parent_name = "hops"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['index_number']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('index_number', (YLeaf(YType.uint32, 'index-number'), ['int'])),
                                ('ip_address', (YLeaf(YType.str, 'ip-address'), ['str'])),
                                ('hop_type', (YLeaf(YType.enumeration, 'hop-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iep_cfg', 'IpIepHop', '')])),
                                ('if_index', (YLeaf(YType.uint32, 'if-index'), ['int'])),
                                ('num_type', (YLeaf(YType.enumeration, 'num-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iep_cfg', 'IpIepNum', '')])),
                                ('mpls_label', (YLeaf(YType.uint32, 'mpls-label'), ['int'])),
                            ])
                            self.index_number = None
                            self.ip_address = None
                            self.hop_type = None
                            self.if_index = None
                            self.num_type = None
                            self.mpls_label = None
                            self._segment_path = lambda: "hop" + "[index-number='" + str(self.index_number) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(IpExplicitPaths.Paths.Path.Name.Hops.Hop, ['index_number', 'ip_address', 'hop_type', 'if_index', 'num_type', 'mpls_label'], name, value)


            class Identifier(Entity):
                """
                identifier
                
                .. attribute:: id  (key)
                
                	Path identifier
                	**type**\: int
                
                	**range:** 1..65535
                
                .. attribute:: hops
                
                	List of Hops
                	**type**\:  :py:class:`Hops <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iep_cfg.IpExplicitPaths.Paths.Path.Identifier.Hops>`
                
                .. attribute:: disable
                
                	Disable the explicit path
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                

                """

                _prefix = 'ip-iep-cfg'
                _revision = '2017-09-07'

                def __init__(self):
                    super(IpExplicitPaths.Paths.Path.Identifier, self).__init__()

                    self.yang_name = "identifier"
                    self.yang_parent_name = "path"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = ['id']
                    self._child_classes = OrderedDict([("hops", ("hops", IpExplicitPaths.Paths.Path.Identifier.Hops))])
                    self._leafs = OrderedDict([
                        ('id', (YLeaf(YType.uint32, 'id'), ['int'])),
                        ('disable', (YLeaf(YType.empty, 'disable'), ['Empty'])),
                    ])
                    self.id = None
                    self.disable = None

                    self.hops = IpExplicitPaths.Paths.Path.Identifier.Hops()
                    self.hops.parent = self
                    self._children_name_map["hops"] = "hops"
                    self._segment_path = lambda: "identifier" + "[id='" + str(self.id) + "']"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(IpExplicitPaths.Paths.Path.Identifier, ['id', 'disable'], name, value)


                class Hops(Entity):
                    """
                    List of Hops
                    
                    .. attribute:: hop
                    
                    	Hop Information
                    	**type**\: list of  		 :py:class:`Hop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iep_cfg.IpExplicitPaths.Paths.Path.Identifier.Hops.Hop>`
                    
                    

                    """

                    _prefix = 'ip-iep-cfg'
                    _revision = '2017-09-07'

                    def __init__(self):
                        super(IpExplicitPaths.Paths.Path.Identifier.Hops, self).__init__()

                        self.yang_name = "hops"
                        self.yang_parent_name = "identifier"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("hop", ("hop", IpExplicitPaths.Paths.Path.Identifier.Hops.Hop))])
                        self._leafs = OrderedDict()

                        self.hop = YList(self)
                        self._segment_path = lambda: "hops"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(IpExplicitPaths.Paths.Path.Identifier.Hops, [], name, value)


                    class Hop(Entity):
                        """
                        Hop Information
                        
                        .. attribute:: index_number  (key)
                        
                        	Index number
                        	**type**\: int
                        
                        	**range:** 1..65535
                        
                        .. attribute:: ip_address
                        
                        	IP address of the hop
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        	**default value**\: 0.0.0.0
                        
                        .. attribute:: hop_type
                        
                        	Include or exclude this hop in the path
                        	**type**\:  :py:class:`IpIepHop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iep_cfg.IpIepHop>`
                        
                        	**default value**\: next-strict
                        
                        .. attribute:: if_index
                        
                        	Ifindex value
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**default value**\: 0
                        
                        .. attribute:: num_type
                        
                        	Number type Numbered or Unnumbered
                        	**type**\:  :py:class:`IpIepNum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iep_cfg.IpIepNum>`
                        
                        	**default value**\: numbered
                        
                        .. attribute:: mpls_label
                        
                        	MPLS Label
                        	**type**\: int
                        
                        	**range:** 0..1048575
                        
                        

                        """

                        _prefix = 'ip-iep-cfg'
                        _revision = '2017-09-07'

                        def __init__(self):
                            super(IpExplicitPaths.Paths.Path.Identifier.Hops.Hop, self).__init__()

                            self.yang_name = "hop"
                            self.yang_parent_name = "hops"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['index_number']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('index_number', (YLeaf(YType.uint32, 'index-number'), ['int'])),
                                ('ip_address', (YLeaf(YType.str, 'ip-address'), ['str'])),
                                ('hop_type', (YLeaf(YType.enumeration, 'hop-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iep_cfg', 'IpIepHop', '')])),
                                ('if_index', (YLeaf(YType.uint32, 'if-index'), ['int'])),
                                ('num_type', (YLeaf(YType.enumeration, 'num-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iep_cfg', 'IpIepNum', '')])),
                                ('mpls_label', (YLeaf(YType.uint32, 'mpls-label'), ['int'])),
                            ])
                            self.index_number = None
                            self.ip_address = None
                            self.hop_type = None
                            self.if_index = None
                            self.num_type = None
                            self.mpls_label = None
                            self._segment_path = lambda: "hop" + "[index-number='" + str(self.index_number) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(IpExplicitPaths.Paths.Path.Identifier.Hops.Hop, ['index_number', 'ip_address', 'hop_type', 'if_index', 'num_type', 'mpls_label'], name, value)

    def clone_ptr(self):
        self._top_entity = IpExplicitPaths()
        return self._top_entity

