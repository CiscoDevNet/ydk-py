""" Cisco_IOS_XR_ip_iep_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ip\-iep package operational data.

This module contains definitions
for the following management objects\:
  explicit\-paths\: Configured IP explicit paths

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class IepAddress(Enum):
    """
    IepAddress

    Address types

    .. data:: next = 0

    	Address type is next

    .. data:: exclude = 1

    	Address type is exclude

    .. data:: exclude_srlg = 2

    	Address type is exclude SRLG

    """

    next = Enum.YLeaf(0, "next")

    exclude = Enum.YLeaf(1, "exclude")

    exclude_srlg = Enum.YLeaf(2, "exclude-srlg")


class IepHop(Enum):
    """
    IepHop

    Hop types of the next\-address configured

    .. data:: strict = 0

    	Hop type is strict

    .. data:: loose = 1

    	Hop type is loose

    """

    strict = Enum.YLeaf(0, "strict")

    loose = Enum.YLeaf(1, "loose")


class IepStatus(Enum):
    """
    IepStatus

    Status of the path

    .. data:: enabled = 0

    	Status is enabled

    .. data:: disabled = 1

    	Status is disabled

    """

    enabled = Enum.YLeaf(0, "enabled")

    disabled = Enum.YLeaf(1, "disabled")



class ExplicitPaths(Entity):
    """
    Configured IP explicit paths
    
    .. attribute:: identifiers
    
    	List of configured IP explicit path identifiers, this corresponds to mplsTunnelHopTable in TE MIB
    	**type**\:   :py:class:`Identifiers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iep_oper.ExplicitPaths.Identifiers>`
    
    .. attribute:: names
    
    	List of configured IP explicit path names, this corresponds to mplsTunnelHopTable in TE MIB
    	**type**\:   :py:class:`Names <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iep_oper.ExplicitPaths.Names>`
    
    

    """

    _prefix = 'ip-iep-oper'
    _revision = '2015-11-09'

    def __init__(self):
        super(ExplicitPaths, self).__init__()
        self._top_entity = None

        self.yang_name = "explicit-paths"
        self.yang_parent_name = "Cisco-IOS-XR-ip-iep-oper"

        self.identifiers = ExplicitPaths.Identifiers()
        self.identifiers.parent = self
        self._children_name_map["identifiers"] = "identifiers"
        self._children_yang_names.add("identifiers")

        self.names = ExplicitPaths.Names()
        self.names.parent = self
        self._children_name_map["names"] = "names"
        self._children_yang_names.add("names")


    class Identifiers(Entity):
        """
        List of configured IP explicit path identifiers,
        this corresponds to mplsTunnelHopTable in TE MIB
        
        .. attribute:: identifier
        
        	IP explicit path configured for a particular identifier
        	**type**\: list of    :py:class:`Identifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iep_oper.ExplicitPaths.Identifiers.Identifier>`
        
        

        """

        _prefix = 'ip-iep-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(ExplicitPaths.Identifiers, self).__init__()

            self.yang_name = "identifiers"
            self.yang_parent_name = "explicit-paths"

            self.identifier = YList(self)

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
                        super(ExplicitPaths.Identifiers, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(ExplicitPaths.Identifiers, self).__setattr__(name, value)


        class Identifier(Entity):
            """
            IP explicit path configured for a particular
            identifier
            
            .. attribute:: identifier_id  <key>
            
            	Identifier ID
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: address
            
            	List of IP addresses configured in the explicit path
            	**type**\: list of    :py:class:`Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iep_oper.ExplicitPaths.Identifiers.Identifier.Address>`
            
            .. attribute:: status
            
            	Status of the path
            	**type**\:   :py:class:`IepStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iep_oper.IepStatus>`
            
            

            """

            _prefix = 'ip-iep-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(ExplicitPaths.Identifiers.Identifier, self).__init__()

                self.yang_name = "identifier"
                self.yang_parent_name = "identifiers"

                self.identifier_id = YLeaf(YType.int32, "identifier-id")

                self.status = YLeaf(YType.enumeration, "status")

                self.address = YList(self)

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("identifier_id",
                                "status") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(ExplicitPaths.Identifiers.Identifier, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(ExplicitPaths.Identifiers.Identifier, self).__setattr__(name, value)


            class Address(Entity):
                """
                List of IP addresses configured in the explicit
                path
                
                .. attribute:: address
                
                	IPv4 unicast address
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: address_type
                
                	Specifies the address type
                	**type**\:   :py:class:`IepAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iep_oper.IepAddress>`
                
                .. attribute:: hop_type
                
                	Specifies the next unicast address in the path as a strict or loose hop
                	**type**\:   :py:class:`IepHop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iep_oper.IepHop>`
                
                .. attribute:: if_index
                
                	Interface Index of the path
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: index
                
                	Index number at which the path entry is inserted or modified
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: mpls_label
                
                	MPLS label
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'ip-iep-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(ExplicitPaths.Identifiers.Identifier.Address, self).__init__()

                    self.yang_name = "address"
                    self.yang_parent_name = "identifier"

                    self.address = YLeaf(YType.str, "address")

                    self.address_type = YLeaf(YType.enumeration, "address-type")

                    self.hop_type = YLeaf(YType.enumeration, "hop-type")

                    self.if_index = YLeaf(YType.uint32, "if-index")

                    self.index = YLeaf(YType.uint32, "index")

                    self.mpls_label = YLeaf(YType.uint32, "mpls-label")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("address",
                                    "address_type",
                                    "hop_type",
                                    "if_index",
                                    "index",
                                    "mpls_label") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(ExplicitPaths.Identifiers.Identifier.Address, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(ExplicitPaths.Identifiers.Identifier.Address, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.address.is_set or
                        self.address_type.is_set or
                        self.hop_type.is_set or
                        self.if_index.is_set or
                        self.index.is_set or
                        self.mpls_label.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.address.yfilter != YFilter.not_set or
                        self.address_type.yfilter != YFilter.not_set or
                        self.hop_type.yfilter != YFilter.not_set or
                        self.if_index.yfilter != YFilter.not_set or
                        self.index.yfilter != YFilter.not_set or
                        self.mpls_label.yfilter != YFilter.not_set)

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
                    if (self.address.is_set or self.address.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.address.get_name_leafdata())
                    if (self.address_type.is_set or self.address_type.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.address_type.get_name_leafdata())
                    if (self.hop_type.is_set or self.hop_type.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.hop_type.get_name_leafdata())
                    if (self.if_index.is_set or self.if_index.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.if_index.get_name_leafdata())
                    if (self.index.is_set or self.index.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.index.get_name_leafdata())
                    if (self.mpls_label.is_set or self.mpls_label.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.mpls_label.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "address" or name == "address-type" or name == "hop-type" or name == "if-index" or name == "index" or name == "mpls-label"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "address"):
                        self.address = value
                        self.address.value_namespace = name_space
                        self.address.value_namespace_prefix = name_space_prefix
                    if(value_path == "address-type"):
                        self.address_type = value
                        self.address_type.value_namespace = name_space
                        self.address_type.value_namespace_prefix = name_space_prefix
                    if(value_path == "hop-type"):
                        self.hop_type = value
                        self.hop_type.value_namespace = name_space
                        self.hop_type.value_namespace_prefix = name_space_prefix
                    if(value_path == "if-index"):
                        self.if_index = value
                        self.if_index.value_namespace = name_space
                        self.if_index.value_namespace_prefix = name_space_prefix
                    if(value_path == "index"):
                        self.index = value
                        self.index.value_namespace = name_space
                        self.index.value_namespace_prefix = name_space_prefix
                    if(value_path == "mpls-label"):
                        self.mpls_label = value
                        self.mpls_label.value_namespace = name_space
                        self.mpls_label.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.address:
                    if (c.has_data()):
                        return True
                return (
                    self.identifier_id.is_set or
                    self.status.is_set)

            def has_operation(self):
                for c in self.address:
                    if (c.has_operation()):
                        return True
                return (
                    self.yfilter != YFilter.not_set or
                    self.identifier_id.yfilter != YFilter.not_set or
                    self.status.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "identifier" + "[identifier-id='" + self.identifier_id.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-ip-iep-oper:explicit-paths/identifiers/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.identifier_id.is_set or self.identifier_id.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.identifier_id.get_name_leafdata())
                if (self.status.is_set or self.status.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.status.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "address"):
                    for c in self.address:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = ExplicitPaths.Identifiers.Identifier.Address()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.address.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "address" or name == "identifier-id" or name == "status"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "identifier-id"):
                    self.identifier_id = value
                    self.identifier_id.value_namespace = name_space
                    self.identifier_id.value_namespace_prefix = name_space_prefix
                if(value_path == "status"):
                    self.status = value
                    self.status.value_namespace = name_space
                    self.status.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.identifier:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.identifier:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "identifiers" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-ip-iep-oper:explicit-paths/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

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
                c = ExplicitPaths.Identifiers.Identifier()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.identifier.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "identifier"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Names(Entity):
        """
        List of configured IP explicit path names, this
        corresponds to mplsTunnelHopTable in TE MIB
        
        .. attribute:: name
        
        	IP explicit path configured for a particular path name
        	**type**\: list of    :py:class:`Name <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iep_oper.ExplicitPaths.Names.Name>`
        
        

        """

        _prefix = 'ip-iep-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(ExplicitPaths.Names, self).__init__()

            self.yang_name = "names"
            self.yang_parent_name = "explicit-paths"

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
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(ExplicitPaths.Names, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(ExplicitPaths.Names, self).__setattr__(name, value)


        class Name(Entity):
            """
            IP explicit path configured for a particular
            path name
            
            .. attribute:: path_name  <key>
            
            	Path name
            	**type**\:  str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: address
            
            	List of IP addresses configured in the explicit path
            	**type**\: list of    :py:class:`Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iep_oper.ExplicitPaths.Names.Name.Address>`
            
            .. attribute:: status
            
            	Status of the path
            	**type**\:   :py:class:`IepStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iep_oper.IepStatus>`
            
            

            """

            _prefix = 'ip-iep-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(ExplicitPaths.Names.Name, self).__init__()

                self.yang_name = "name"
                self.yang_parent_name = "names"

                self.path_name = YLeaf(YType.str, "path-name")

                self.status = YLeaf(YType.enumeration, "status")

                self.address = YList(self)

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("path_name",
                                "status") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(ExplicitPaths.Names.Name, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(ExplicitPaths.Names.Name, self).__setattr__(name, value)


            class Address(Entity):
                """
                List of IP addresses configured in the explicit
                path
                
                .. attribute:: address
                
                	IPv4 unicast address
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: address_type
                
                	Specifies the address type
                	**type**\:   :py:class:`IepAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iep_oper.IepAddress>`
                
                .. attribute:: hop_type
                
                	Specifies the next unicast address in the path as a strict or loose hop
                	**type**\:   :py:class:`IepHop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iep_oper.IepHop>`
                
                .. attribute:: if_index
                
                	Interface Index of the path
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: index
                
                	Index number at which the path entry is inserted or modified
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: mpls_label
                
                	MPLS label
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'ip-iep-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(ExplicitPaths.Names.Name.Address, self).__init__()

                    self.yang_name = "address"
                    self.yang_parent_name = "name"

                    self.address = YLeaf(YType.str, "address")

                    self.address_type = YLeaf(YType.enumeration, "address-type")

                    self.hop_type = YLeaf(YType.enumeration, "hop-type")

                    self.if_index = YLeaf(YType.uint32, "if-index")

                    self.index = YLeaf(YType.uint32, "index")

                    self.mpls_label = YLeaf(YType.uint32, "mpls-label")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("address",
                                    "address_type",
                                    "hop_type",
                                    "if_index",
                                    "index",
                                    "mpls_label") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(ExplicitPaths.Names.Name.Address, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(ExplicitPaths.Names.Name.Address, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.address.is_set or
                        self.address_type.is_set or
                        self.hop_type.is_set or
                        self.if_index.is_set or
                        self.index.is_set or
                        self.mpls_label.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.address.yfilter != YFilter.not_set or
                        self.address_type.yfilter != YFilter.not_set or
                        self.hop_type.yfilter != YFilter.not_set or
                        self.if_index.yfilter != YFilter.not_set or
                        self.index.yfilter != YFilter.not_set or
                        self.mpls_label.yfilter != YFilter.not_set)

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
                    if (self.address.is_set or self.address.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.address.get_name_leafdata())
                    if (self.address_type.is_set or self.address_type.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.address_type.get_name_leafdata())
                    if (self.hop_type.is_set or self.hop_type.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.hop_type.get_name_leafdata())
                    if (self.if_index.is_set or self.if_index.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.if_index.get_name_leafdata())
                    if (self.index.is_set or self.index.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.index.get_name_leafdata())
                    if (self.mpls_label.is_set or self.mpls_label.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.mpls_label.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "address" or name == "address-type" or name == "hop-type" or name == "if-index" or name == "index" or name == "mpls-label"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "address"):
                        self.address = value
                        self.address.value_namespace = name_space
                        self.address.value_namespace_prefix = name_space_prefix
                    if(value_path == "address-type"):
                        self.address_type = value
                        self.address_type.value_namespace = name_space
                        self.address_type.value_namespace_prefix = name_space_prefix
                    if(value_path == "hop-type"):
                        self.hop_type = value
                        self.hop_type.value_namespace = name_space
                        self.hop_type.value_namespace_prefix = name_space_prefix
                    if(value_path == "if-index"):
                        self.if_index = value
                        self.if_index.value_namespace = name_space
                        self.if_index.value_namespace_prefix = name_space_prefix
                    if(value_path == "index"):
                        self.index = value
                        self.index.value_namespace = name_space
                        self.index.value_namespace_prefix = name_space_prefix
                    if(value_path == "mpls-label"):
                        self.mpls_label = value
                        self.mpls_label.value_namespace = name_space
                        self.mpls_label.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.address:
                    if (c.has_data()):
                        return True
                return (
                    self.path_name.is_set or
                    self.status.is_set)

            def has_operation(self):
                for c in self.address:
                    if (c.has_operation()):
                        return True
                return (
                    self.yfilter != YFilter.not_set or
                    self.path_name.yfilter != YFilter.not_set or
                    self.status.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "name" + "[path-name='" + self.path_name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-ip-iep-oper:explicit-paths/names/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.path_name.is_set or self.path_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.path_name.get_name_leafdata())
                if (self.status.is_set or self.status.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.status.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "address"):
                    for c in self.address:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = ExplicitPaths.Names.Name.Address()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.address.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "address" or name == "path-name" or name == "status"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "path-name"):
                    self.path_name = value
                    self.path_name.value_namespace = name_space
                    self.path_name.value_namespace_prefix = name_space_prefix
                if(value_path == "status"):
                    self.status = value
                    self.status.value_namespace = name_space
                    self.status.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.name:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.name:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "names" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-ip-iep-oper:explicit-paths/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "name"):
                for c in self.name:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = ExplicitPaths.Names.Name()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.name.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "name"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            (self.identifiers is not None and self.identifiers.has_data()) or
            (self.names is not None and self.names.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.identifiers is not None and self.identifiers.has_operation()) or
            (self.names is not None and self.names.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-ip-iep-oper:explicit-paths" + path_buffer

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

        if (child_yang_name == "identifiers"):
            if (self.identifiers is None):
                self.identifiers = ExplicitPaths.Identifiers()
                self.identifiers.parent = self
                self._children_name_map["identifiers"] = "identifiers"
            return self.identifiers

        if (child_yang_name == "names"):
            if (self.names is None):
                self.names = ExplicitPaths.Names()
                self.names.parent = self
                self._children_name_map["names"] = "names"
            return self.names

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "identifiers" or name == "names"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = ExplicitPaths()
        return self._top_entity

