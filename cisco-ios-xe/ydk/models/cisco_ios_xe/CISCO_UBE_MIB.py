""" CISCO_UBE_MIB 

This MIB describes objects used for managing Cisco
Unified Border Element (CUBE).

The Cisco Unified Border Element (CUBE) is a Cisco 
IOS Session Border Controller (SBC) that interconnects
independent voice over IP (VoIP) and video over IP 
networks for data, voice, and video transport

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class CiscoUbeMib(Entity):
    """
    
    
    .. attribute:: ciscoubemibobjects
    
    	
    	**type**\:   :py:class:`Ciscoubemibobjects <ydk.models.cisco_ios_xe.CISCO_UBE_MIB.CiscoUbeMib.Ciscoubemibobjects>`
    
    

    """

    _prefix = 'CISCO-UBE-MIB'
    _revision = '2010-11-29'

    def __init__(self):
        super(CiscoUbeMib, self).__init__()
        self._top_entity = None

        self.yang_name = "CISCO-UBE-MIB"
        self.yang_parent_name = "CISCO-UBE-MIB"

        self.ciscoubemibobjects = CiscoUbeMib.Ciscoubemibobjects()
        self.ciscoubemibobjects.parent = self
        self._children_name_map["ciscoubemibobjects"] = "ciscoUbeMIBObjects"
        self._children_yang_names.add("ciscoUbeMIBObjects")


    class Ciscoubemibobjects(Entity):
        """
        
        
        .. attribute:: cubeenabled
        
        	This object represents, whether the Cisco Unified Border Element (CUBE) is enabled  on the device or not.  The value 'true' means that the CUBE feature  is enabled on the device.  The value 'false' means that the CUBE feature  is disabled
        	**type**\:  bool
        
        .. attribute:: cubetotalsessionallowed
        
        	This object provides the total number of CUBE session allowed on the device. The value zero  means no sessions are allowed with CUBE
        	**type**\:  int
        
        	**range:** 0..999999
        
        	**units**\: session
        
        .. attribute:: cubeversion
        
        	This object represents the version of Cisco Unified Border Element on the device
        	**type**\:  str
        
        

        """

        _prefix = 'CISCO-UBE-MIB'
        _revision = '2010-11-29'

        def __init__(self):
            super(CiscoUbeMib.Ciscoubemibobjects, self).__init__()

            self.yang_name = "ciscoUbeMIBObjects"
            self.yang_parent_name = "CISCO-UBE-MIB"

            self.cubeenabled = YLeaf(YType.boolean, "cubeEnabled")

            self.cubetotalsessionallowed = YLeaf(YType.uint32, "cubeTotalSessionAllowed")

            self.cubeversion = YLeaf(YType.str, "cubeVersion")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("cubeenabled",
                            "cubetotalsessionallowed",
                            "cubeversion") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoUbeMib.Ciscoubemibobjects, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoUbeMib.Ciscoubemibobjects, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.cubeenabled.is_set or
                self.cubetotalsessionallowed.is_set or
                self.cubeversion.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.cubeenabled.yfilter != YFilter.not_set or
                self.cubetotalsessionallowed.yfilter != YFilter.not_set or
                self.cubeversion.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "ciscoUbeMIBObjects" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-UBE-MIB:CISCO-UBE-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.cubeenabled.is_set or self.cubeenabled.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cubeenabled.get_name_leafdata())
            if (self.cubetotalsessionallowed.is_set or self.cubetotalsessionallowed.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cubetotalsessionallowed.get_name_leafdata())
            if (self.cubeversion.is_set or self.cubeversion.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cubeversion.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cubeEnabled" or name == "cubeTotalSessionAllowed" or name == "cubeVersion"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "cubeEnabled"):
                self.cubeenabled = value
                self.cubeenabled.value_namespace = name_space
                self.cubeenabled.value_namespace_prefix = name_space_prefix
            if(value_path == "cubeTotalSessionAllowed"):
                self.cubetotalsessionallowed = value
                self.cubetotalsessionallowed.value_namespace = name_space
                self.cubetotalsessionallowed.value_namespace_prefix = name_space_prefix
            if(value_path == "cubeVersion"):
                self.cubeversion = value
                self.cubeversion.value_namespace = name_space
                self.cubeversion.value_namespace_prefix = name_space_prefix

    def has_data(self):
        return (self.ciscoubemibobjects is not None and self.ciscoubemibobjects.has_data())

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.ciscoubemibobjects is not None and self.ciscoubemibobjects.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "CISCO-UBE-MIB:CISCO-UBE-MIB" + path_buffer

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

        if (child_yang_name == "ciscoUbeMIBObjects"):
            if (self.ciscoubemibobjects is None):
                self.ciscoubemibobjects = CiscoUbeMib.Ciscoubemibobjects()
                self.ciscoubemibobjects.parent = self
                self._children_name_map["ciscoubemibobjects"] = "ciscoUbeMIBObjects"
            return self.ciscoubemibobjects

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "ciscoUbeMIBObjects"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = CiscoUbeMib()
        return self._top_entity

