""" CISCO_MPLS_LSR_EXT_STD_MIB 

Copyright (c) 2012 IETF Trust and the persons identified
as the document authors.  All rights reserved.

This MIB module contains generic object definitions for


MPLS LSR in transport networks.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class CiscoMplsLsrExtStdMib(Entity):
    """
    
    
    .. attribute:: cmplsxcexttable
    
    	This table sparse augments the mplsXCTable of MPLS\-LSR\-STD\-MIB [RFC3813] to provide MPLS\-TP specific information about associated tunnel information
    	**type**\:   :py:class:`Cmplsxcexttable <ydk.models.cisco_ios_xe.CISCO_MPLS_LSR_EXT_STD_MIB.CiscoMplsLsrExtStdMib.Cmplsxcexttable>`
    
    

    """

    _prefix = 'CISCO-MPLS-LSR-EXT-STD-MIB'
    _revision = '2012-04-30'

    def __init__(self):
        super(CiscoMplsLsrExtStdMib, self).__init__()
        self._top_entity = None

        self.yang_name = "CISCO-MPLS-LSR-EXT-STD-MIB"
        self.yang_parent_name = "CISCO-MPLS-LSR-EXT-STD-MIB"

        self.cmplsxcexttable = CiscoMplsLsrExtStdMib.Cmplsxcexttable()
        self.cmplsxcexttable.parent = self
        self._children_name_map["cmplsxcexttable"] = "cmplsXCExtTable"
        self._children_yang_names.add("cmplsXCExtTable")


    class Cmplsxcexttable(Entity):
        """
        This table sparse augments the mplsXCTable of
        MPLS\-LSR\-STD\-MIB [RFC3813] to provide MPLS\-TP specific
        information about associated tunnel information
        
        .. attribute:: cmplsxcextentry
        
        	An entry in this table extends the cross connect information represented by an entry in the mplsXCTable in MPLS\-LSR\-STD\-MIB [RFC3813] through a sparse augmentation.  An entry can be created by a network administrator via SNMP SET commands, or in response to signaling protocol events
        	**type**\: list of    :py:class:`Cmplsxcextentry <ydk.models.cisco_ios_xe.CISCO_MPLS_LSR_EXT_STD_MIB.CiscoMplsLsrExtStdMib.Cmplsxcexttable.Cmplsxcextentry>`
        
        

        """

        _prefix = 'CISCO-MPLS-LSR-EXT-STD-MIB'
        _revision = '2012-04-30'

        def __init__(self):
            super(CiscoMplsLsrExtStdMib.Cmplsxcexttable, self).__init__()

            self.yang_name = "cmplsXCExtTable"
            self.yang_parent_name = "CISCO-MPLS-LSR-EXT-STD-MIB"

            self.cmplsxcextentry = YList(self)

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
                        super(CiscoMplsLsrExtStdMib.Cmplsxcexttable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoMplsLsrExtStdMib.Cmplsxcexttable, self).__setattr__(name, value)


        class Cmplsxcextentry(Entity):
            """
            An entry in this table extends the cross connect
            information represented by an entry in
            the mplsXCTable in MPLS\-LSR\-STD\-MIB [RFC3813] through
            a sparse augmentation.  An entry can be created by
            a network administrator via SNMP SET commands, or in
            response to signaling protocol events.
            
            .. attribute:: mplsxcindex  <key>
            
            	
            	**type**\:  str
            
            	**length:** 1..24
            
            	**refers to**\:  :py:class:`mplsxcindex <ydk.models.cisco_ios_xe.MPLS_LSR_STD_MIB.MplsLsrStdMib.Mplsxctable.Mplsxcentry>`
            
            .. attribute:: mplsxcinsegmentindex  <key>
            
            	
            	**type**\:  str
            
            	**length:** 1..24
            
            	**refers to**\:  :py:class:`mplsxcinsegmentindex <ydk.models.cisco_ios_xe.MPLS_LSR_STD_MIB.MplsLsrStdMib.Mplsxctable.Mplsxcentry>`
            
            .. attribute:: mplsxcoutsegmentindex  <key>
            
            	
            	**type**\:  str
            
            	**length:** 1..24
            
            	**refers to**\:  :py:class:`mplsxcoutsegmentindex <ydk.models.cisco_ios_xe.MPLS_LSR_STD_MIB.MplsLsrStdMib.Mplsxctable.Mplsxcentry>`
            
            .. attribute:: cmplsxcexttunnelpointer
            
            	This object indicates the back pointer to the tunnel entry segment.  This object cannot be modified if mplsXCRowStatus for the corresponding entry in the mplsXCTable is active(1)
            	**type**\:  str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: cmplsxcoppositedirxcptr
            
            	This object indicates the pointer to the opposite direction XC entry.  This object cannot be modified if mplsXCRowStatus for the corresponding entry in the mplsXCTable is active(1)
            	**type**\:  str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            

            """

            _prefix = 'CISCO-MPLS-LSR-EXT-STD-MIB'
            _revision = '2012-04-30'

            def __init__(self):
                super(CiscoMplsLsrExtStdMib.Cmplsxcexttable.Cmplsxcextentry, self).__init__()

                self.yang_name = "cmplsXCExtEntry"
                self.yang_parent_name = "cmplsXCExtTable"

                self.mplsxcindex = YLeaf(YType.str, "mplsXCIndex")

                self.mplsxcinsegmentindex = YLeaf(YType.str, "mplsXCInSegmentIndex")

                self.mplsxcoutsegmentindex = YLeaf(YType.str, "mplsXCOutSegmentIndex")

                self.cmplsxcexttunnelpointer = YLeaf(YType.str, "cmplsXCExtTunnelPointer")

                self.cmplsxcoppositedirxcptr = YLeaf(YType.str, "cmplsXCOppositeDirXCPtr")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("mplsxcindex",
                                "mplsxcinsegmentindex",
                                "mplsxcoutsegmentindex",
                                "cmplsxcexttunnelpointer",
                                "cmplsxcoppositedirxcptr") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoMplsLsrExtStdMib.Cmplsxcexttable.Cmplsxcextentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoMplsLsrExtStdMib.Cmplsxcexttable.Cmplsxcextentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.mplsxcindex.is_set or
                    self.mplsxcinsegmentindex.is_set or
                    self.mplsxcoutsegmentindex.is_set or
                    self.cmplsxcexttunnelpointer.is_set or
                    self.cmplsxcoppositedirxcptr.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.mplsxcindex.yfilter != YFilter.not_set or
                    self.mplsxcinsegmentindex.yfilter != YFilter.not_set or
                    self.mplsxcoutsegmentindex.yfilter != YFilter.not_set or
                    self.cmplsxcexttunnelpointer.yfilter != YFilter.not_set or
                    self.cmplsxcoppositedirxcptr.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cmplsXCExtEntry" + "[mplsXCIndex='" + self.mplsxcindex.get() + "']" + "[mplsXCInSegmentIndex='" + self.mplsxcinsegmentindex.get() + "']" + "[mplsXCOutSegmentIndex='" + self.mplsxcoutsegmentindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-MPLS-LSR-EXT-STD-MIB:CISCO-MPLS-LSR-EXT-STD-MIB/cmplsXCExtTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.mplsxcindex.is_set or self.mplsxcindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsxcindex.get_name_leafdata())
                if (self.mplsxcinsegmentindex.is_set or self.mplsxcinsegmentindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsxcinsegmentindex.get_name_leafdata())
                if (self.mplsxcoutsegmentindex.is_set or self.mplsxcoutsegmentindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsxcoutsegmentindex.get_name_leafdata())
                if (self.cmplsxcexttunnelpointer.is_set or self.cmplsxcexttunnelpointer.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cmplsxcexttunnelpointer.get_name_leafdata())
                if (self.cmplsxcoppositedirxcptr.is_set or self.cmplsxcoppositedirxcptr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cmplsxcoppositedirxcptr.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "mplsXCIndex" or name == "mplsXCInSegmentIndex" or name == "mplsXCOutSegmentIndex" or name == "cmplsXCExtTunnelPointer" or name == "cmplsXCOppositeDirXCPtr"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "mplsXCIndex"):
                    self.mplsxcindex = value
                    self.mplsxcindex.value_namespace = name_space
                    self.mplsxcindex.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsXCInSegmentIndex"):
                    self.mplsxcinsegmentindex = value
                    self.mplsxcinsegmentindex.value_namespace = name_space
                    self.mplsxcinsegmentindex.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsXCOutSegmentIndex"):
                    self.mplsxcoutsegmentindex = value
                    self.mplsxcoutsegmentindex.value_namespace = name_space
                    self.mplsxcoutsegmentindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cmplsXCExtTunnelPointer"):
                    self.cmplsxcexttunnelpointer = value
                    self.cmplsxcexttunnelpointer.value_namespace = name_space
                    self.cmplsxcexttunnelpointer.value_namespace_prefix = name_space_prefix
                if(value_path == "cmplsXCOppositeDirXCPtr"):
                    self.cmplsxcoppositedirxcptr = value
                    self.cmplsxcoppositedirxcptr.value_namespace = name_space
                    self.cmplsxcoppositedirxcptr.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cmplsxcextentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cmplsxcextentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cmplsXCExtTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-MPLS-LSR-EXT-STD-MIB:CISCO-MPLS-LSR-EXT-STD-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cmplsXCExtEntry"):
                for c in self.cmplsxcextentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoMplsLsrExtStdMib.Cmplsxcexttable.Cmplsxcextentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cmplsxcextentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cmplsXCExtEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (self.cmplsxcexttable is not None and self.cmplsxcexttable.has_data())

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.cmplsxcexttable is not None and self.cmplsxcexttable.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "CISCO-MPLS-LSR-EXT-STD-MIB:CISCO-MPLS-LSR-EXT-STD-MIB" + path_buffer

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

        if (child_yang_name == "cmplsXCExtTable"):
            if (self.cmplsxcexttable is None):
                self.cmplsxcexttable = CiscoMplsLsrExtStdMib.Cmplsxcexttable()
                self.cmplsxcexttable.parent = self
                self._children_name_map["cmplsxcexttable"] = "cmplsXCExtTable"
            return self.cmplsxcexttable

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "cmplsXCExtTable"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = CiscoMplsLsrExtStdMib()
        return self._top_entity

