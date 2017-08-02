""" Cisco_IOS_XR_ip_iep_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ip\-iep package configuration.

This module contains definitions
for the following management objects\:
  ip\-explicit\-paths\: IP Explicit Path config data

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class IpIepHop(Enum):
    """
    IpIepHop

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
    IpIepNum

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
    IpIepPath

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
    	**type**\:   :py:class:`Paths <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iep_cfg.IpExplicitPaths.Paths>`
    
    

    """

    _prefix = 'ip-iep-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        super(IpExplicitPaths, self).__init__()
        self._top_entity = None

        self.yang_name = "ip-explicit-paths"
        self.yang_parent_name = "Cisco-IOS-XR-ip-iep-cfg"

        self.paths = IpExplicitPaths.Paths()
        self.paths.parent = self
        self._children_name_map["paths"] = "paths"
        self._children_yang_names.add("paths")


    class Paths(Entity):
        """
        A list of explicit paths
        
        .. attribute:: path
        
        	Config data for a specific explicit path
        	**type**\: list of    :py:class:`Path <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iep_cfg.IpExplicitPaths.Paths.Path>`
        
        

        """

        _prefix = 'ip-iep-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(IpExplicitPaths.Paths, self).__init__()

            self.yang_name = "paths"
            self.yang_parent_name = "ip-explicit-paths"

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
                        super(IpExplicitPaths.Paths, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(IpExplicitPaths.Paths, self).__setattr__(name, value)


        class Path(Entity):
            """
            Config data for a specific explicit path
            
            .. attribute:: type  <key>
            
            	Path type
            	**type**\:   :py:class:`IpIepPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iep_cfg.IpIepPath>`
            
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
                super(IpExplicitPaths.Paths.Path, self).__init__()

                self.yang_name = "path"
                self.yang_parent_name = "paths"

                self.type = YLeaf(YType.enumeration, "type")

                self.identifier = YList(self)
                self.name = YList(self)

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("type") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(IpExplicitPaths.Paths.Path, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(IpExplicitPaths.Paths.Path, self).__setattr__(name, value)


            class Name(Entity):
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
                    super(IpExplicitPaths.Paths.Path.Name, self).__init__()

                    self.yang_name = "name"
                    self.yang_parent_name = "path"

                    self.name = YLeaf(YType.str, "name")

                    self.disable = YLeaf(YType.empty, "disable")

                    self.hops = IpExplicitPaths.Paths.Path.Name.Hops()
                    self.hops.parent = self
                    self._children_name_map["hops"] = "hops"
                    self._children_yang_names.add("hops")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("name",
                                    "disable") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(IpExplicitPaths.Paths.Path.Name, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(IpExplicitPaths.Paths.Path.Name, self).__setattr__(name, value)


                class Hops(Entity):
                    """
                    List of Hops
                    
                    .. attribute:: hop
                    
                    	Hop Information
                    	**type**\: list of    :py:class:`Hop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iep_cfg.IpExplicitPaths.Paths.Path.Name.Hops.Hop>`
                    
                    

                    """

                    _prefix = 'ip-iep-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(IpExplicitPaths.Paths.Path.Name.Hops, self).__init__()

                        self.yang_name = "hops"
                        self.yang_parent_name = "name"

                        self.hop = YList(self)

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
                                    super(IpExplicitPaths.Paths.Path.Name.Hops, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(IpExplicitPaths.Paths.Path.Name.Hops, self).__setattr__(name, value)


                    class Hop(Entity):
                        """
                        Hop Information
                        
                        .. attribute:: index_number  <key>
                        
                        	Index number
                        	**type**\:  int
                        
                        	**range:** 1..65535
                        
                        .. attribute:: hop_type
                        
                        	Include or exclude this hop in the path
                        	**type**\:   :py:class:`IpIepHop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iep_cfg.IpIepHop>`
                        
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
                        	**type**\:   :py:class:`IpIepNum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iep_cfg.IpIepNum>`
                        
                        	**default value**\: numbered
                        
                        

                        """

                        _prefix = 'ip-iep-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(IpExplicitPaths.Paths.Path.Name.Hops.Hop, self).__init__()

                            self.yang_name = "hop"
                            self.yang_parent_name = "hops"

                            self.index_number = YLeaf(YType.uint32, "index-number")

                            self.hop_type = YLeaf(YType.enumeration, "hop-type")

                            self.if_index = YLeaf(YType.int32, "if-index")

                            self.ip_address = YLeaf(YType.str, "ip-address")

                            self.mpls_label = YLeaf(YType.int32, "mpls-label")

                            self.num_type = YLeaf(YType.enumeration, "num-type")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("index_number",
                                            "hop_type",
                                            "if_index",
                                            "ip_address",
                                            "mpls_label",
                                            "num_type") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(IpExplicitPaths.Paths.Path.Name.Hops.Hop, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(IpExplicitPaths.Paths.Path.Name.Hops.Hop, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.index_number.is_set or
                                self.hop_type.is_set or
                                self.if_index.is_set or
                                self.ip_address.is_set or
                                self.mpls_label.is_set or
                                self.num_type.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.index_number.yfilter != YFilter.not_set or
                                self.hop_type.yfilter != YFilter.not_set or
                                self.if_index.yfilter != YFilter.not_set or
                                self.ip_address.yfilter != YFilter.not_set or
                                self.mpls_label.yfilter != YFilter.not_set or
                                self.num_type.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "hop" + "[index-number='" + self.index_number.get() + "']" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.index_number.is_set or self.index_number.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.index_number.get_name_leafdata())
                            if (self.hop_type.is_set or self.hop_type.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.hop_type.get_name_leafdata())
                            if (self.if_index.is_set or self.if_index.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.if_index.get_name_leafdata())
                            if (self.ip_address.is_set or self.ip_address.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.ip_address.get_name_leafdata())
                            if (self.mpls_label.is_set or self.mpls_label.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.mpls_label.get_name_leafdata())
                            if (self.num_type.is_set or self.num_type.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.num_type.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "index-number" or name == "hop-type" or name == "if-index" or name == "ip-address" or name == "mpls-label" or name == "num-type"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "index-number"):
                                self.index_number = value
                                self.index_number.value_namespace = name_space
                                self.index_number.value_namespace_prefix = name_space_prefix
                            if(value_path == "hop-type"):
                                self.hop_type = value
                                self.hop_type.value_namespace = name_space
                                self.hop_type.value_namespace_prefix = name_space_prefix
                            if(value_path == "if-index"):
                                self.if_index = value
                                self.if_index.value_namespace = name_space
                                self.if_index.value_namespace_prefix = name_space_prefix
                            if(value_path == "ip-address"):
                                self.ip_address = value
                                self.ip_address.value_namespace = name_space
                                self.ip_address.value_namespace_prefix = name_space_prefix
                            if(value_path == "mpls-label"):
                                self.mpls_label = value
                                self.mpls_label.value_namespace = name_space
                                self.mpls_label.value_namespace_prefix = name_space_prefix
                            if(value_path == "num-type"):
                                self.num_type = value
                                self.num_type.value_namespace = name_space
                                self.num_type.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.hop:
                            if (c.has_data()):
                                return True
                        return False

                    def has_operation(self):
                        for c in self.hop:
                            if (c.has_operation()):
                                return True
                        return self.yfilter != YFilter.not_set

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "hops" + path_buffer

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

                        if (child_yang_name == "hop"):
                            for c in self.hop:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = IpExplicitPaths.Paths.Path.Name.Hops.Hop()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.hop.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "hop"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass

                def has_data(self):
                    return (
                        self.name.is_set or
                        self.disable.is_set or
                        (self.hops is not None and self.hops.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.name.yfilter != YFilter.not_set or
                        self.disable.yfilter != YFilter.not_set or
                        (self.hops is not None and self.hops.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "name" + "[name='" + self.name.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.name.is_set or self.name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.name.get_name_leafdata())
                    if (self.disable.is_set or self.disable.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.disable.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "hops"):
                        if (self.hops is None):
                            self.hops = IpExplicitPaths.Paths.Path.Name.Hops()
                            self.hops.parent = self
                            self._children_name_map["hops"] = "hops"
                        return self.hops

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "hops" or name == "name" or name == "disable"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "name"):
                        self.name = value
                        self.name.value_namespace = name_space
                        self.name.value_namespace_prefix = name_space_prefix
                    if(value_path == "disable"):
                        self.disable = value
                        self.disable.value_namespace = name_space
                        self.disable.value_namespace_prefix = name_space_prefix


            class Identifier(Entity):
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
                    super(IpExplicitPaths.Paths.Path.Identifier, self).__init__()

                    self.yang_name = "identifier"
                    self.yang_parent_name = "path"

                    self.id = YLeaf(YType.uint32, "id")

                    self.disable = YLeaf(YType.empty, "disable")

                    self.hops = IpExplicitPaths.Paths.Path.Identifier.Hops()
                    self.hops.parent = self
                    self._children_name_map["hops"] = "hops"
                    self._children_yang_names.add("hops")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("id",
                                    "disable") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(IpExplicitPaths.Paths.Path.Identifier, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(IpExplicitPaths.Paths.Path.Identifier, self).__setattr__(name, value)


                class Hops(Entity):
                    """
                    List of Hops
                    
                    .. attribute:: hop
                    
                    	Hop Information
                    	**type**\: list of    :py:class:`Hop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iep_cfg.IpExplicitPaths.Paths.Path.Identifier.Hops.Hop>`
                    
                    

                    """

                    _prefix = 'ip-iep-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(IpExplicitPaths.Paths.Path.Identifier.Hops, self).__init__()

                        self.yang_name = "hops"
                        self.yang_parent_name = "identifier"

                        self.hop = YList(self)

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
                                    super(IpExplicitPaths.Paths.Path.Identifier.Hops, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(IpExplicitPaths.Paths.Path.Identifier.Hops, self).__setattr__(name, value)


                    class Hop(Entity):
                        """
                        Hop Information
                        
                        .. attribute:: index_number  <key>
                        
                        	Index number
                        	**type**\:  int
                        
                        	**range:** 1..65535
                        
                        .. attribute:: hop_type
                        
                        	Include or exclude this hop in the path
                        	**type**\:   :py:class:`IpIepHop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iep_cfg.IpIepHop>`
                        
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
                        	**type**\:   :py:class:`IpIepNum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iep_cfg.IpIepNum>`
                        
                        	**default value**\: numbered
                        
                        

                        """

                        _prefix = 'ip-iep-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(IpExplicitPaths.Paths.Path.Identifier.Hops.Hop, self).__init__()

                            self.yang_name = "hop"
                            self.yang_parent_name = "hops"

                            self.index_number = YLeaf(YType.uint32, "index-number")

                            self.hop_type = YLeaf(YType.enumeration, "hop-type")

                            self.if_index = YLeaf(YType.int32, "if-index")

                            self.ip_address = YLeaf(YType.str, "ip-address")

                            self.mpls_label = YLeaf(YType.int32, "mpls-label")

                            self.num_type = YLeaf(YType.enumeration, "num-type")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("index_number",
                                            "hop_type",
                                            "if_index",
                                            "ip_address",
                                            "mpls_label",
                                            "num_type") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(IpExplicitPaths.Paths.Path.Identifier.Hops.Hop, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(IpExplicitPaths.Paths.Path.Identifier.Hops.Hop, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.index_number.is_set or
                                self.hop_type.is_set or
                                self.if_index.is_set or
                                self.ip_address.is_set or
                                self.mpls_label.is_set or
                                self.num_type.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.index_number.yfilter != YFilter.not_set or
                                self.hop_type.yfilter != YFilter.not_set or
                                self.if_index.yfilter != YFilter.not_set or
                                self.ip_address.yfilter != YFilter.not_set or
                                self.mpls_label.yfilter != YFilter.not_set or
                                self.num_type.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "hop" + "[index-number='" + self.index_number.get() + "']" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.index_number.is_set or self.index_number.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.index_number.get_name_leafdata())
                            if (self.hop_type.is_set or self.hop_type.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.hop_type.get_name_leafdata())
                            if (self.if_index.is_set or self.if_index.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.if_index.get_name_leafdata())
                            if (self.ip_address.is_set or self.ip_address.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.ip_address.get_name_leafdata())
                            if (self.mpls_label.is_set or self.mpls_label.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.mpls_label.get_name_leafdata())
                            if (self.num_type.is_set or self.num_type.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.num_type.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "index-number" or name == "hop-type" or name == "if-index" or name == "ip-address" or name == "mpls-label" or name == "num-type"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "index-number"):
                                self.index_number = value
                                self.index_number.value_namespace = name_space
                                self.index_number.value_namespace_prefix = name_space_prefix
                            if(value_path == "hop-type"):
                                self.hop_type = value
                                self.hop_type.value_namespace = name_space
                                self.hop_type.value_namespace_prefix = name_space_prefix
                            if(value_path == "if-index"):
                                self.if_index = value
                                self.if_index.value_namespace = name_space
                                self.if_index.value_namespace_prefix = name_space_prefix
                            if(value_path == "ip-address"):
                                self.ip_address = value
                                self.ip_address.value_namespace = name_space
                                self.ip_address.value_namespace_prefix = name_space_prefix
                            if(value_path == "mpls-label"):
                                self.mpls_label = value
                                self.mpls_label.value_namespace = name_space
                                self.mpls_label.value_namespace_prefix = name_space_prefix
                            if(value_path == "num-type"):
                                self.num_type = value
                                self.num_type.value_namespace = name_space
                                self.num_type.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.hop:
                            if (c.has_data()):
                                return True
                        return False

                    def has_operation(self):
                        for c in self.hop:
                            if (c.has_operation()):
                                return True
                        return self.yfilter != YFilter.not_set

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "hops" + path_buffer

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

                        if (child_yang_name == "hop"):
                            for c in self.hop:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = IpExplicitPaths.Paths.Path.Identifier.Hops.Hop()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.hop.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "hop"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass

                def has_data(self):
                    return (
                        self.id.is_set or
                        self.disable.is_set or
                        (self.hops is not None and self.hops.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.id.yfilter != YFilter.not_set or
                        self.disable.yfilter != YFilter.not_set or
                        (self.hops is not None and self.hops.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "identifier" + "[id='" + self.id.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.id.is_set or self.id.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.id.get_name_leafdata())
                    if (self.disable.is_set or self.disable.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.disable.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "hops"):
                        if (self.hops is None):
                            self.hops = IpExplicitPaths.Paths.Path.Identifier.Hops()
                            self.hops.parent = self
                            self._children_name_map["hops"] = "hops"
                        return self.hops

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "hops" or name == "id" or name == "disable"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "id"):
                        self.id = value
                        self.id.value_namespace = name_space
                        self.id.value_namespace_prefix = name_space_prefix
                    if(value_path == "disable"):
                        self.disable = value
                        self.disable.value_namespace = name_space
                        self.disable.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.identifier:
                    if (c.has_data()):
                        return True
                for c in self.name:
                    if (c.has_data()):
                        return True
                return self.type.is_set

            def has_operation(self):
                for c in self.identifier:
                    if (c.has_operation()):
                        return True
                for c in self.name:
                    if (c.has_operation()):
                        return True
                return (
                    self.yfilter != YFilter.not_set or
                    self.type.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "path" + "[type='" + self.type.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-ip-iep-cfg:ip-explicit-paths/paths/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.type.is_set or self.type.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.type.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "identifier"):
                    for c in self.identifier:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = IpExplicitPaths.Paths.Path.Identifier()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.identifier.append(c)
                    return c

                if (child_yang_name == "name"):
                    for c in self.name:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = IpExplicitPaths.Paths.Path.Name()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.name.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "identifier" or name == "name" or name == "type"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "type"):
                    self.type = value
                    self.type.value_namespace = name_space
                    self.type.value_namespace_prefix = name_space_prefix

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
                path_buffer = "Cisco-IOS-XR-ip-iep-cfg:ip-explicit-paths/%s" % self.get_segment_path()
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
                c = IpExplicitPaths.Paths.Path()
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
        return (self.paths is not None and self.paths.has_data())

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.paths is not None and self.paths.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-ip-iep-cfg:ip-explicit-paths" + path_buffer

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

        if (child_yang_name == "paths"):
            if (self.paths is None):
                self.paths = IpExplicitPaths.Paths()
                self.paths.parent = self
                self._children_name_map["paths"] = "paths"
            return self.paths

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "paths"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = IpExplicitPaths()
        return self._top_entity

