""" Cisco_IOS_XR_asr9k_fab_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR asr9k\-fab package configuration.

This module contains definitions
for the following management objects\:
  fab\-vqi\-config\: Configure Fabric

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class FabVqiConfig(Entity):
    """
    Configure Fabric
    
    .. attribute:: operates
    
    	none
    	**type**\:   :py:class:`Operates <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_fab_cfg.FabVqiConfig.Operates>`
    
    

    """

    _prefix = 'asr9k-fab-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        super(FabVqiConfig, self).__init__()
        self._top_entity = None

        self.yang_name = "fab-vqi-config"
        self.yang_parent_name = "Cisco-IOS-XR-asr9k-fab-cfg"

        self.operates = FabVqiConfig.Operates()
        self.operates.parent = self
        self._children_name_map["operates"] = "operates"
        self._children_yang_names.add("operates")


    class Operates(Entity):
        """
        none
        
        .. attribute:: operate
        
        	none
        	**type**\: list of    :py:class:`Operate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_fab_cfg.FabVqiConfig.Operates.Operate>`
        
        

        """

        _prefix = 'asr9k-fab-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(FabVqiConfig.Operates, self).__init__()

            self.yang_name = "operates"
            self.yang_parent_name = "fab-vqi-config"

            self.operate = YList(self)

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
                        super(FabVqiConfig.Operates, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(FabVqiConfig.Operates, self).__setattr__(name, value)


        class Operate(Entity):
            """
            none
            
            .. attribute:: id1  <key>
            
            	none
            	**type**\:  str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: id1_xr
            
            	none
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: id2
            
            	none
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            

            """

            _prefix = 'asr9k-fab-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(FabVqiConfig.Operates.Operate, self).__init__()

                self.yang_name = "operate"
                self.yang_parent_name = "operates"

                self.id1 = YLeaf(YType.str, "id1")

                self.id1_xr = YLeaf(YType.int32, "id1-xr")

                self.id2 = YLeaf(YType.int32, "id2")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("id1",
                                "id1_xr",
                                "id2") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(FabVqiConfig.Operates.Operate, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(FabVqiConfig.Operates.Operate, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.id1.is_set or
                    self.id1_xr.is_set or
                    self.id2.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.id1.yfilter != YFilter.not_set or
                    self.id1_xr.yfilter != YFilter.not_set or
                    self.id2.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "operate" + "[id1='" + self.id1.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-asr9k-fab-cfg:fab-vqi-config/operates/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.id1.is_set or self.id1.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.id1.get_name_leafdata())
                if (self.id1_xr.is_set or self.id1_xr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.id1_xr.get_name_leafdata())
                if (self.id2.is_set or self.id2.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.id2.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "id1" or name == "id1-xr" or name == "id2"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "id1"):
                    self.id1 = value
                    self.id1.value_namespace = name_space
                    self.id1.value_namespace_prefix = name_space_prefix
                if(value_path == "id1-xr"):
                    self.id1_xr = value
                    self.id1_xr.value_namespace = name_space
                    self.id1_xr.value_namespace_prefix = name_space_prefix
                if(value_path == "id2"):
                    self.id2 = value
                    self.id2.value_namespace = name_space
                    self.id2.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.operate:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.operate:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "operates" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-asr9k-fab-cfg:fab-vqi-config/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "operate"):
                for c in self.operate:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = FabVqiConfig.Operates.Operate()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.operate.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "operate"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (self.operates is not None and self.operates.has_data())

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.operates is not None and self.operates.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-asr9k-fab-cfg:fab-vqi-config" + path_buffer

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

        if (child_yang_name == "operates"):
            if (self.operates is None):
                self.operates = FabVqiConfig.Operates()
                self.operates.parent = self
                self._children_name_map["operates"] = "operates"
            return self.operates

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "operates"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = FabVqiConfig()
        return self._top_entity

