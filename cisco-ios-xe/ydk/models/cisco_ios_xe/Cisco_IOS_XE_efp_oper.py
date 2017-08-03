""" Cisco_IOS_XE_efp_oper 

This module contains a collection of YANG definitions
for service instance (efp) stats.
Copyright (c) 2016\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class EfpStats(Entity):
    """
    Service instance stats
    
    .. attribute:: efp_stat
    
    	List of service instance stats
    	**type**\: list of    :py:class:`EfpStat <ydk.models.cisco_ios_xe.Cisco_IOS_XE_efp_oper.EfpStats.EfpStat>`
    
    

    """

    _prefix = 'efp-stats-ios-xe-oper'
    _revision = '2017-02-07'

    def __init__(self):
        super(EfpStats, self).__init__()
        self._top_entity = None

        self.yang_name = "efp-stats"
        self.yang_parent_name = "Cisco-IOS-XE-efp-oper"

        self.efp_stat = YList(self)

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
                    super(EfpStats, self).__setattr__(name, value)
                else:
                    self.__dict__[name].set(value)
            else:
                if hasattr(value, "parent") and name != "parent":
                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                        value.parent = self
                    elif value.parent is None and value.yang_name in self._children_yang_names:
                        value.parent = self
                super(EfpStats, self).__setattr__(name, value)


    class EfpStat(Entity):
        """
        List of service instance stats
        
        .. attribute:: id  <key>
        
        	EFP id
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: interface  <key>
        
        	Interface name
        	**type**\:  str
        
        .. attribute:: in_bytes
        
        	Incoming bytes
        	**type**\:  int
        
        	**range:** 0..18446744073709551615
        
        .. attribute:: in_pkts
        
        	Incoming packets
        	**type**\:  int
        
        	**range:** 0..18446744073709551615
        
        .. attribute:: out_bytes
        
        	Outgoing bytes
        	**type**\:  int
        
        	**range:** 0..18446744073709551615
        
        .. attribute:: out_pkts
        
        	Outgoing packets
        	**type**\:  int
        
        	**range:** 0..18446744073709551615
        
        

        """

        _prefix = 'efp-stats-ios-xe-oper'
        _revision = '2017-02-07'

        def __init__(self):
            super(EfpStats.EfpStat, self).__init__()

            self.yang_name = "efp-stat"
            self.yang_parent_name = "efp-stats"

            self.id = YLeaf(YType.uint32, "id")

            self.interface = YLeaf(YType.str, "interface")

            self.in_bytes = YLeaf(YType.uint64, "in-bytes")

            self.in_pkts = YLeaf(YType.uint64, "in-pkts")

            self.out_bytes = YLeaf(YType.uint64, "out-bytes")

            self.out_pkts = YLeaf(YType.uint64, "out-pkts")

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
                            "interface",
                            "in_bytes",
                            "in_pkts",
                            "out_bytes",
                            "out_pkts") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(EfpStats.EfpStat, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(EfpStats.EfpStat, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.id.is_set or
                self.interface.is_set or
                self.in_bytes.is_set or
                self.in_pkts.is_set or
                self.out_bytes.is_set or
                self.out_pkts.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.id.yfilter != YFilter.not_set or
                self.interface.yfilter != YFilter.not_set or
                self.in_bytes.yfilter != YFilter.not_set or
                self.in_pkts.yfilter != YFilter.not_set or
                self.out_bytes.yfilter != YFilter.not_set or
                self.out_pkts.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "efp-stat" + "[id='" + self.id.get() + "']" + "[interface='" + self.interface.get() + "']" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XE-efp-oper:efp-stats/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.id.is_set or self.id.yfilter != YFilter.not_set):
                leaf_name_data.append(self.id.get_name_leafdata())
            if (self.interface.is_set or self.interface.yfilter != YFilter.not_set):
                leaf_name_data.append(self.interface.get_name_leafdata())
            if (self.in_bytes.is_set or self.in_bytes.yfilter != YFilter.not_set):
                leaf_name_data.append(self.in_bytes.get_name_leafdata())
            if (self.in_pkts.is_set or self.in_pkts.yfilter != YFilter.not_set):
                leaf_name_data.append(self.in_pkts.get_name_leafdata())
            if (self.out_bytes.is_set or self.out_bytes.yfilter != YFilter.not_set):
                leaf_name_data.append(self.out_bytes.get_name_leafdata())
            if (self.out_pkts.is_set or self.out_pkts.yfilter != YFilter.not_set):
                leaf_name_data.append(self.out_pkts.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "id" or name == "interface" or name == "in-bytes" or name == "in-pkts" or name == "out-bytes" or name == "out-pkts"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "id"):
                self.id = value
                self.id.value_namespace = name_space
                self.id.value_namespace_prefix = name_space_prefix
            if(value_path == "interface"):
                self.interface = value
                self.interface.value_namespace = name_space
                self.interface.value_namespace_prefix = name_space_prefix
            if(value_path == "in-bytes"):
                self.in_bytes = value
                self.in_bytes.value_namespace = name_space
                self.in_bytes.value_namespace_prefix = name_space_prefix
            if(value_path == "in-pkts"):
                self.in_pkts = value
                self.in_pkts.value_namespace = name_space
                self.in_pkts.value_namespace_prefix = name_space_prefix
            if(value_path == "out-bytes"):
                self.out_bytes = value
                self.out_bytes.value_namespace = name_space
                self.out_bytes.value_namespace_prefix = name_space_prefix
            if(value_path == "out-pkts"):
                self.out_pkts = value
                self.out_pkts.value_namespace = name_space
                self.out_pkts.value_namespace_prefix = name_space_prefix

    def has_data(self):
        for c in self.efp_stat:
            if (c.has_data()):
                return True
        return False

    def has_operation(self):
        for c in self.efp_stat:
            if (c.has_operation()):
                return True
        return self.yfilter != YFilter.not_set

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XE-efp-oper:efp-stats" + path_buffer

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

        if (child_yang_name == "efp-stat"):
            for c in self.efp_stat:
                segment = c.get_segment_path()
                if (segment_path == segment):
                    return c
            c = EfpStats.EfpStat()
            c.parent = self
            local_reference_key = "ydk::seg::%s" % segment_path
            self._local_refs[local_reference_key] = c
            self.efp_stat.append(c)
            return c

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "efp-stat"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = EfpStats()
        return self._top_entity

