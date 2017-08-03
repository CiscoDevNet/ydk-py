""" CISCO_IMAGE_MIB 

Router image MIB which identify the capabilities
and characteristics of the image

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class CiscoImageMib(Entity):
    """
    
    
    .. attribute:: ciscoimagetable
    
    	A table provides content information describing the executing IOS image
    	**type**\:   :py:class:`Ciscoimagetable <ydk.models.cisco_ios_xe.CISCO_IMAGE_MIB.CiscoImageMib.Ciscoimagetable>`
    
    

    """

    _prefix = 'CISCO-IMAGE-MIB'
    _revision = '1995-08-15'

    def __init__(self):
        super(CiscoImageMib, self).__init__()
        self._top_entity = None

        self.yang_name = "CISCO-IMAGE-MIB"
        self.yang_parent_name = "CISCO-IMAGE-MIB"

        self.ciscoimagetable = CiscoImageMib.Ciscoimagetable()
        self.ciscoimagetable.parent = self
        self._children_name_map["ciscoimagetable"] = "ciscoImageTable"
        self._children_yang_names.add("ciscoImageTable")


    class Ciscoimagetable(Entity):
        """
        A table provides content information describing the
        executing IOS image.
        
        .. attribute:: ciscoimageentry
        
        	A image characteristic string entry
        	**type**\: list of    :py:class:`Ciscoimageentry <ydk.models.cisco_ios_xe.CISCO_IMAGE_MIB.CiscoImageMib.Ciscoimagetable.Ciscoimageentry>`
        
        

        """

        _prefix = 'CISCO-IMAGE-MIB'
        _revision = '1995-08-15'

        def __init__(self):
            super(CiscoImageMib.Ciscoimagetable, self).__init__()

            self.yang_name = "ciscoImageTable"
            self.yang_parent_name = "CISCO-IMAGE-MIB"

            self.ciscoimageentry = YList(self)

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
                        super(CiscoImageMib.Ciscoimagetable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoImageMib.Ciscoimagetable, self).__setattr__(name, value)


        class Ciscoimageentry(Entity):
            """
            A image characteristic string entry.
            
            .. attribute:: ciscoimageindex  <key>
            
            	A sequence number for each string stored in the IOS image
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: ciscoimagestring
            
            	The string of this entry
            	**type**\:  str
            
            

            """

            _prefix = 'CISCO-IMAGE-MIB'
            _revision = '1995-08-15'

            def __init__(self):
                super(CiscoImageMib.Ciscoimagetable.Ciscoimageentry, self).__init__()

                self.yang_name = "ciscoImageEntry"
                self.yang_parent_name = "ciscoImageTable"

                self.ciscoimageindex = YLeaf(YType.int32, "ciscoImageIndex")

                self.ciscoimagestring = YLeaf(YType.str, "ciscoImageString")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("ciscoimageindex",
                                "ciscoimagestring") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoImageMib.Ciscoimagetable.Ciscoimageentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoImageMib.Ciscoimagetable.Ciscoimageentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.ciscoimageindex.is_set or
                    self.ciscoimagestring.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ciscoimageindex.yfilter != YFilter.not_set or
                    self.ciscoimagestring.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "ciscoImageEntry" + "[ciscoImageIndex='" + self.ciscoimageindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-IMAGE-MIB:CISCO-IMAGE-MIB/ciscoImageTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ciscoimageindex.is_set or self.ciscoimageindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscoimageindex.get_name_leafdata())
                if (self.ciscoimagestring.is_set or self.ciscoimagestring.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscoimagestring.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ciscoImageIndex" or name == "ciscoImageString"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "ciscoImageIndex"):
                    self.ciscoimageindex = value
                    self.ciscoimageindex.value_namespace = name_space
                    self.ciscoimageindex.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoImageString"):
                    self.ciscoimagestring = value
                    self.ciscoimagestring.value_namespace = name_space
                    self.ciscoimagestring.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.ciscoimageentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.ciscoimageentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "ciscoImageTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-IMAGE-MIB:CISCO-IMAGE-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "ciscoImageEntry"):
                for c in self.ciscoimageentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoImageMib.Ciscoimagetable.Ciscoimageentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.ciscoimageentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "ciscoImageEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (self.ciscoimagetable is not None and self.ciscoimagetable.has_data())

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.ciscoimagetable is not None and self.ciscoimagetable.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "CISCO-IMAGE-MIB:CISCO-IMAGE-MIB" + path_buffer

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

        if (child_yang_name == "ciscoImageTable"):
            if (self.ciscoimagetable is None):
                self.ciscoimagetable = CiscoImageMib.Ciscoimagetable()
                self.ciscoimagetable.parent = self
                self._children_name_map["ciscoimagetable"] = "ciscoImageTable"
            return self.ciscoimagetable

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "ciscoImageTable"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = CiscoImageMib()
        return self._top_entity

