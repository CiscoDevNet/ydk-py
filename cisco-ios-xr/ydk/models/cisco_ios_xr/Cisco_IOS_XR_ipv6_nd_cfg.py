""" Cisco_IOS_XR_ipv6_nd_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ipv6\-nd package configuration.

This module contains definitions
for the following management objects\:
  ipv6\-neighbor\: IPv6 neighbor or neighbor discovery
    configuration

This YANG module augments the
  Cisco\-IOS\-XR\-ifmgr\-cfg
module with configuration data.

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class Ipv6NdMonth(Enum):
    """
    Ipv6NdMonth

    Ipv6nd month

    .. data:: january = 0

    	January

    .. data:: february = 1

    	February

    .. data:: march = 2

    	March

    .. data:: april = 3

    	April

    .. data:: may = 4

    	May

    .. data:: june = 5

    	June

    .. data:: july = 6

    	July

    .. data:: august = 7

    	August

    .. data:: september = 8

    	September

    .. data:: october = 9

    	October

    .. data:: november = 10

    	November

    .. data:: december = 11

    	December

    """

    january = Enum.YLeaf(0, "january")

    february = Enum.YLeaf(1, "february")

    march = Enum.YLeaf(2, "march")

    april = Enum.YLeaf(3, "april")

    may = Enum.YLeaf(4, "may")

    june = Enum.YLeaf(5, "june")

    july = Enum.YLeaf(6, "july")

    august = Enum.YLeaf(7, "august")

    september = Enum.YLeaf(8, "september")

    october = Enum.YLeaf(9, "october")

    november = Enum.YLeaf(10, "november")

    december = Enum.YLeaf(11, "december")


class Ipv6NdRouterPref(Enum):
    """
    Ipv6NdRouterPref

    Ipv6 nd router pref

    .. data:: high = 1

    	High preference

    .. data:: medium = 2

    	Medium preference

    .. data:: low = 3

    	Low preference

    """

    high = Enum.YLeaf(1, "high")

    medium = Enum.YLeaf(2, "medium")

    low = Enum.YLeaf(3, "low")


class Ipv6SrpEncapsulation(Enum):
    """
    Ipv6SrpEncapsulation

    Ipv6srp encapsulation

    .. data:: srpa = 5

    	Encapsulation type SRP, prefer side A

    .. data:: srpb = 6

    	Encapsulation type SRP, prefer side B

    """

    srpa = Enum.YLeaf(5, "srpa")

    srpb = Enum.YLeaf(6, "srpb")



class Ipv6Neighbor(Entity):
    """
    IPv6 neighbor or neighbor discovery configuration
    
    .. attribute:: neighbors
    
    	IPv6 neighbors
    	**type**\:   :py:class:`Neighbors <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_cfg.Ipv6Neighbor.Neighbors>`
    
    .. attribute:: scavenge_timeout
    
    	Set lifetime for stale neighbor
    	**type**\:  int
    
    	**range:** 1..43200
    
    	**units**\: second
    
    

    """

    _prefix = 'ipv6-nd-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        super(Ipv6Neighbor, self).__init__()
        self._top_entity = None

        self.yang_name = "ipv6-neighbor"
        self.yang_parent_name = "Cisco-IOS-XR-ipv6-nd-cfg"

        self.scavenge_timeout = YLeaf(YType.uint32, "scavenge-timeout")

        self.neighbors = Ipv6Neighbor.Neighbors()
        self.neighbors.parent = self
        self._children_name_map["neighbors"] = "neighbors"
        self._children_yang_names.add("neighbors")

    def __setattr__(self, name, value):
        self._check_monkey_patching_error(name, value)
        with _handle_type_error():
            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                    "Please use list append or extend method."
                                    .format(value))
            if isinstance(value, Enum.YLeaf):
                value = value.name
            if name in ("scavenge_timeout") and name in self.__dict__:
                if isinstance(value, YLeaf):
                    self.__dict__[name].set(value.get())
                elif isinstance(value, YLeafList):
                    super(Ipv6Neighbor, self).__setattr__(name, value)
                else:
                    self.__dict__[name].set(value)
            else:
                if hasattr(value, "parent") and name != "parent":
                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                        value.parent = self
                    elif value.parent is None and value.yang_name in self._children_yang_names:
                        value.parent = self
                super(Ipv6Neighbor, self).__setattr__(name, value)


    class Neighbors(Entity):
        """
        IPv6 neighbors
        
        .. attribute:: neighbor
        
        	IPv6 neighbor configuration
        	**type**\: list of    :py:class:`Neighbor <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_cfg.Ipv6Neighbor.Neighbors.Neighbor>`
        
        

        """

        _prefix = 'ipv6-nd-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(Ipv6Neighbor.Neighbors, self).__init__()

            self.yang_name = "neighbors"
            self.yang_parent_name = "ipv6-neighbor"

            self.neighbor = YList(self)

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
                        super(Ipv6Neighbor.Neighbors, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Ipv6Neighbor.Neighbors, self).__setattr__(name, value)


        class Neighbor(Entity):
            """
            IPv6 neighbor configuration
            
            .. attribute:: neighbor_address  <key>
            
            	IPv6 address
            	**type**\:  str
            
            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: interface_name  <key>
            
            	Interface name
            	**type**\:  str
            
            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
            
            .. attribute:: encapsulation
            
            	Encapsulation type only if interface type is SRP
            	**type**\:   :py:class:`Ipv6SrpEncapsulation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_nd_cfg.Ipv6SrpEncapsulation>`
            
            .. attribute:: mac_address
            
            	48\-bit hardware address H.H.H
            	**type**\:  str
            
            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
            
            	**mandatory**\: True
            
            .. attribute:: zone
            
            	IPv6 address zone
            	**type**\:  str
            
            	**default value**\: 0
            
            

            """

            _prefix = 'ipv6-nd-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(Ipv6Neighbor.Neighbors.Neighbor, self).__init__()

                self.yang_name = "neighbor"
                self.yang_parent_name = "neighbors"

                self.neighbor_address = YLeaf(YType.str, "neighbor-address")

                self.interface_name = YLeaf(YType.str, "interface-name")

                self.encapsulation = YLeaf(YType.enumeration, "encapsulation")

                self.mac_address = YLeaf(YType.str, "mac-address")

                self.zone = YLeaf(YType.str, "zone")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("neighbor_address",
                                "interface_name",
                                "encapsulation",
                                "mac_address",
                                "zone") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Ipv6Neighbor.Neighbors.Neighbor, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Ipv6Neighbor.Neighbors.Neighbor, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.neighbor_address.is_set or
                    self.interface_name.is_set or
                    self.encapsulation.is_set or
                    self.mac_address.is_set or
                    self.zone.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.neighbor_address.yfilter != YFilter.not_set or
                    self.interface_name.yfilter != YFilter.not_set or
                    self.encapsulation.yfilter != YFilter.not_set or
                    self.mac_address.yfilter != YFilter.not_set or
                    self.zone.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "neighbor" + "[neighbor-address='" + self.neighbor_address.get() + "']" + "[interface-name='" + self.interface_name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-ipv6-nd-cfg:ipv6-neighbor/neighbors/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.neighbor_address.is_set or self.neighbor_address.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.neighbor_address.get_name_leafdata())
                if (self.interface_name.is_set or self.interface_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.interface_name.get_name_leafdata())
                if (self.encapsulation.is_set or self.encapsulation.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.encapsulation.get_name_leafdata())
                if (self.mac_address.is_set or self.mac_address.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mac_address.get_name_leafdata())
                if (self.zone.is_set or self.zone.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.zone.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "neighbor-address" or name == "interface-name" or name == "encapsulation" or name == "mac-address" or name == "zone"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "neighbor-address"):
                    self.neighbor_address = value
                    self.neighbor_address.value_namespace = name_space
                    self.neighbor_address.value_namespace_prefix = name_space_prefix
                if(value_path == "interface-name"):
                    self.interface_name = value
                    self.interface_name.value_namespace = name_space
                    self.interface_name.value_namespace_prefix = name_space_prefix
                if(value_path == "encapsulation"):
                    self.encapsulation = value
                    self.encapsulation.value_namespace = name_space
                    self.encapsulation.value_namespace_prefix = name_space_prefix
                if(value_path == "mac-address"):
                    self.mac_address = value
                    self.mac_address.value_namespace = name_space
                    self.mac_address.value_namespace_prefix = name_space_prefix
                if(value_path == "zone"):
                    self.zone = value
                    self.zone.value_namespace = name_space
                    self.zone.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.neighbor:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.neighbor:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "neighbors" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-ipv6-nd-cfg:ipv6-neighbor/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "neighbor"):
                for c in self.neighbor:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = Ipv6Neighbor.Neighbors.Neighbor()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.neighbor.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "neighbor"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            self.scavenge_timeout.is_set or
            (self.neighbors is not None and self.neighbors.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            self.scavenge_timeout.yfilter != YFilter.not_set or
            (self.neighbors is not None and self.neighbors.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-ipv6-nd-cfg:ipv6-neighbor" + path_buffer

        return path_buffer

    def get_entity_path(self, ancestor):
        path_buffer = ""
        if (not ancestor is None):
            raise YPYModelError("ancestor has to be None for top-level node")

        path_buffer = self.get_segment_path()
        leaf_name_data = LeafDataList()
        if (self.scavenge_timeout.is_set or self.scavenge_timeout.yfilter != YFilter.not_set):
            leaf_name_data.append(self.scavenge_timeout.get_name_leafdata())

        entity_path = EntityPath(path_buffer, leaf_name_data)
        return entity_path

    def get_child_by_name(self, child_yang_name, segment_path):
        child = self._get_child_by_seg_name([child_yang_name, segment_path])
        if child is not None:
            return child

        if (child_yang_name == "neighbors"):
            if (self.neighbors is None):
                self.neighbors = Ipv6Neighbor.Neighbors()
                self.neighbors.parent = self
                self._children_name_map["neighbors"] = "neighbors"
            return self.neighbors

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "neighbors" or name == "scavenge-timeout"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        if(value_path == "scavenge-timeout"):
            self.scavenge_timeout = value
            self.scavenge_timeout.value_namespace = name_space
            self.scavenge_timeout.value_namespace_prefix = name_space_prefix

    def clone_ptr(self):
        self._top_entity = Ipv6Neighbor()
        return self._top_entity

