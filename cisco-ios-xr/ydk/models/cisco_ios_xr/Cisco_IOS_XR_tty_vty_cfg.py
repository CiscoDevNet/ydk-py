""" Cisco_IOS_XR_tty_vty_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR tty\-vty package configuration.

This module contains definitions
for the following management objects\:
  vty\: VTY Pools configuration

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class Vty(Entity):
    """
    VTY Pools configuration
    
    .. attribute:: vty_pools
    
    	List of VTY Pools
    	**type**\:   :py:class:`VtyPools <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_vty_cfg.Vty.VtyPools>`
    
    

    """

    _prefix = 'tty-vty-cfg'
    _revision = '2015-09-16'

    def __init__(self):
        super(Vty, self).__init__()
        self._top_entity = None

        self.yang_name = "vty"
        self.yang_parent_name = "Cisco-IOS-XR-tty-vty-cfg"

        self.vty_pools = Vty.VtyPools()
        self.vty_pools.parent = self
        self._children_name_map["vty_pools"] = "vty-pools"
        self._children_yang_names.add("vty-pools")


    class VtyPools(Entity):
        """
        List of VTY Pools
        
        .. attribute:: vty_pool
        
        	VTY Pool
        	**type**\: list of    :py:class:`VtyPool <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tty_vty_cfg.Vty.VtyPools.VtyPool>`
        
        

        """

        _prefix = 'tty-vty-cfg'
        _revision = '2015-09-16'

        def __init__(self):
            super(Vty.VtyPools, self).__init__()

            self.yang_name = "vty-pools"
            self.yang_parent_name = "vty"

            self.vty_pool = YList(self)

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
                        super(Vty.VtyPools, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Vty.VtyPools, self).__setattr__(name, value)


        class VtyPool(Entity):
            """
            VTY Pool
            
            .. attribute:: pool_name  <key>
            
            	For configuring range for default pool use 'default',For configuring range for fault\-manager pool use 'fm',For configuring range for any user defined pool use any other string
            	**type**\:  str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: first_vty
            
            	First VTY number,For default VTY use 0,For user\-defined use 5,For fault\-manager use 100
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            	**mandatory**\: True
            
            .. attribute:: last_vty
            
            	Last VTY number,For default configure between 0\-99,For user\-defined configure between 5\-99 ,For fault\-manager configure between 100\-199
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            	**mandatory**\: True
            
            .. attribute:: line_template
            
            	Name of line template
            	**type**\:  str
            
            .. attribute:: none
            
            	Empty Option
            	**type**\:  str
            
            

            """

            _prefix = 'tty-vty-cfg'
            _revision = '2015-09-16'

            def __init__(self):
                super(Vty.VtyPools.VtyPool, self).__init__()

                self.yang_name = "vty-pool"
                self.yang_parent_name = "vty-pools"

                self.pool_name = YLeaf(YType.str, "pool-name")

                self.first_vty = YLeaf(YType.int32, "first-vty")

                self.last_vty = YLeaf(YType.int32, "last-vty")

                self.line_template = YLeaf(YType.str, "line-template")

                self.none = YLeaf(YType.str, "none")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("pool_name",
                                "first_vty",
                                "last_vty",
                                "line_template",
                                "none") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Vty.VtyPools.VtyPool, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Vty.VtyPools.VtyPool, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.pool_name.is_set or
                    self.first_vty.is_set or
                    self.last_vty.is_set or
                    self.line_template.is_set or
                    self.none.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.pool_name.yfilter != YFilter.not_set or
                    self.first_vty.yfilter != YFilter.not_set or
                    self.last_vty.yfilter != YFilter.not_set or
                    self.line_template.yfilter != YFilter.not_set or
                    self.none.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "vty-pool" + "[pool-name='" + self.pool_name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-tty-vty-cfg:vty/vty-pools/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.pool_name.is_set or self.pool_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.pool_name.get_name_leafdata())
                if (self.first_vty.is_set or self.first_vty.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.first_vty.get_name_leafdata())
                if (self.last_vty.is_set or self.last_vty.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.last_vty.get_name_leafdata())
                if (self.line_template.is_set or self.line_template.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.line_template.get_name_leafdata())
                if (self.none.is_set or self.none.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.none.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "pool-name" or name == "first-vty" or name == "last-vty" or name == "line-template" or name == "none"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "pool-name"):
                    self.pool_name = value
                    self.pool_name.value_namespace = name_space
                    self.pool_name.value_namespace_prefix = name_space_prefix
                if(value_path == "first-vty"):
                    self.first_vty = value
                    self.first_vty.value_namespace = name_space
                    self.first_vty.value_namespace_prefix = name_space_prefix
                if(value_path == "last-vty"):
                    self.last_vty = value
                    self.last_vty.value_namespace = name_space
                    self.last_vty.value_namespace_prefix = name_space_prefix
                if(value_path == "line-template"):
                    self.line_template = value
                    self.line_template.value_namespace = name_space
                    self.line_template.value_namespace_prefix = name_space_prefix
                if(value_path == "none"):
                    self.none = value
                    self.none.value_namespace = name_space
                    self.none.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.vty_pool:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.vty_pool:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "vty-pools" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-tty-vty-cfg:vty/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "vty-pool"):
                for c in self.vty_pool:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = Vty.VtyPools.VtyPool()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.vty_pool.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "vty-pool"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (self.vty_pools is not None and self.vty_pools.has_data())

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.vty_pools is not None and self.vty_pools.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-tty-vty-cfg:vty" + path_buffer

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

        if (child_yang_name == "vty-pools"):
            if (self.vty_pools is None):
                self.vty_pools = Vty.VtyPools()
                self.vty_pools.parent = self
                self._children_name_map["vty_pools"] = "vty-pools"
            return self.vty_pools

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "vty-pools"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = Vty()
        return self._top_entity

