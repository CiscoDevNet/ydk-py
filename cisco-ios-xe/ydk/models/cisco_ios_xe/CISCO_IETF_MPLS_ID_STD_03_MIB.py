""" CISCO_IETF_MPLS_ID_STD_03_MIB 

Copyright (c) 2012 IETF Trust and the persons identified
as the document authors.  All rights reserved.

This MIB module contains generic object definitions for
MPLS Traffic Engineering in transport networks. This module is a
cisco\-ized version of the IETF draft\:
draft\-ietf\-mpls\-tp\-te\-mib\-03.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class CiscoIetfMplsIdStd03Mib(Entity):
    """
    
    
    .. attribute:: cmplsidobjects
    
    	
    	**type**\:   :py:class:`Cmplsidobjects <ydk.models.cisco_ios_xe.CISCO_IETF_MPLS_ID_STD_03_MIB.CiscoIetfMplsIdStd03Mib.Cmplsidobjects>`
    
    

    """

    _prefix = 'CISCO-IETF-MPLS-ID-STD-03-MIB'
    _revision = '2012-06-07'

    def __init__(self):
        super(CiscoIetfMplsIdStd03Mib, self).__init__()
        self._top_entity = None

        self.yang_name = "CISCO-IETF-MPLS-ID-STD-03-MIB"
        self.yang_parent_name = "CISCO-IETF-MPLS-ID-STD-03-MIB"

        self.cmplsidobjects = CiscoIetfMplsIdStd03Mib.Cmplsidobjects()
        self.cmplsidobjects.parent = self
        self._children_name_map["cmplsidobjects"] = "cmplsIdObjects"
        self._children_yang_names.add("cmplsIdObjects")


    class Cmplsidobjects(Entity):
        """
        
        
        .. attribute:: cmplsglobalid
        
        	This object allows the administrator to assign a unique operator identifier also called MPLS\-TP Global\_ID
        	**type**\:  str
        
        	**length:** 4
        
        .. attribute:: cmplsicc
        
        	This object allows the operator or service provider to assign a unique MPLS\-TP ITU\-T Carrier Code (ICC) to a network
        	**type**\:  str
        
        	**length:** 1..6
        
        .. attribute:: cmplsnodeid
        
        	This object allows the operator or service provider to assign a unique MPLS\-TP Node\_ID.  The Node\_ID is assigned within the scope of the Global\_ID
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'CISCO-IETF-MPLS-ID-STD-03-MIB'
        _revision = '2012-06-07'

        def __init__(self):
            super(CiscoIetfMplsIdStd03Mib.Cmplsidobjects, self).__init__()

            self.yang_name = "cmplsIdObjects"
            self.yang_parent_name = "CISCO-IETF-MPLS-ID-STD-03-MIB"

            self.cmplsglobalid = YLeaf(YType.str, "cmplsGlobalId")

            self.cmplsicc = YLeaf(YType.str, "cmplsIcc")

            self.cmplsnodeid = YLeaf(YType.uint32, "cmplsNodeId")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("cmplsglobalid",
                            "cmplsicc",
                            "cmplsnodeid") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoIetfMplsIdStd03Mib.Cmplsidobjects, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoIetfMplsIdStd03Mib.Cmplsidobjects, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.cmplsglobalid.is_set or
                self.cmplsicc.is_set or
                self.cmplsnodeid.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.cmplsglobalid.yfilter != YFilter.not_set or
                self.cmplsicc.yfilter != YFilter.not_set or
                self.cmplsnodeid.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cmplsIdObjects" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-IETF-MPLS-ID-STD-03-MIB:CISCO-IETF-MPLS-ID-STD-03-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.cmplsglobalid.is_set or self.cmplsglobalid.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cmplsglobalid.get_name_leafdata())
            if (self.cmplsicc.is_set or self.cmplsicc.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cmplsicc.get_name_leafdata())
            if (self.cmplsnodeid.is_set or self.cmplsnodeid.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cmplsnodeid.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cmplsGlobalId" or name == "cmplsIcc" or name == "cmplsNodeId"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "cmplsGlobalId"):
                self.cmplsglobalid = value
                self.cmplsglobalid.value_namespace = name_space
                self.cmplsglobalid.value_namespace_prefix = name_space_prefix
            if(value_path == "cmplsIcc"):
                self.cmplsicc = value
                self.cmplsicc.value_namespace = name_space
                self.cmplsicc.value_namespace_prefix = name_space_prefix
            if(value_path == "cmplsNodeId"):
                self.cmplsnodeid = value
                self.cmplsnodeid.value_namespace = name_space
                self.cmplsnodeid.value_namespace_prefix = name_space_prefix

    def has_data(self):
        return (self.cmplsidobjects is not None and self.cmplsidobjects.has_data())

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.cmplsidobjects is not None and self.cmplsidobjects.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "CISCO-IETF-MPLS-ID-STD-03-MIB:CISCO-IETF-MPLS-ID-STD-03-MIB" + path_buffer

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

        if (child_yang_name == "cmplsIdObjects"):
            if (self.cmplsidobjects is None):
                self.cmplsidobjects = CiscoIetfMplsIdStd03Mib.Cmplsidobjects()
                self.cmplsidobjects.parent = self
                self._children_name_map["cmplsidobjects"] = "cmplsIdObjects"
            return self.cmplsidobjects

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "cmplsIdObjects"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = CiscoIetfMplsIdStd03Mib()
        return self._top_entity

