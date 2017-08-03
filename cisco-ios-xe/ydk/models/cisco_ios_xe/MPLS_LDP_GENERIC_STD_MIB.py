""" MPLS_LDP_GENERIC_STD_MIB 

Copyright (C) The Internet Society (year). The
initial version of this MIB module was published
in RFC 3815. For full legal notices see the RFC
itself or see\:
http\://www.ietf.org/copyrights/ianamib.html

This MIB contains managed object definitions for
configuring and monitoring the Multiprotocol Label
Switching (MPLS), Label Distribution Protocol (LDP),
utilizing ethernet as the Layer 2 media.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class MplsLdpGenericStdMib(Entity):
    """
    
    
    .. attribute:: mplsldpentitygenericlrtable
    
    	The MPLS LDP Entity Generic Label Range (LR) Table.  The purpose of this table is to provide a mechanism for configurating a contiguous range of generic labels, or a 'label range' for LDP Entities.  LDP Entities which use Generic Labels must have at least one entry in this table.  In other words, this table 'extends' the mpldLdpEntityTable for Generic Labels
    	**type**\:   :py:class:`Mplsldpentitygenericlrtable <ydk.models.cisco_ios_xe.MPLS_LDP_GENERIC_STD_MIB.MplsLdpGenericStdMib.Mplsldpentitygenericlrtable>`
    
    

    """

    _prefix = 'MPLS-LDP-GENERIC-STD-MIB'
    _revision = '2004-06-03'

    def __init__(self):
        super(MplsLdpGenericStdMib, self).__init__()
        self._top_entity = None

        self.yang_name = "MPLS-LDP-GENERIC-STD-MIB"
        self.yang_parent_name = "MPLS-LDP-GENERIC-STD-MIB"

        self.mplsldpentitygenericlrtable = MplsLdpGenericStdMib.Mplsldpentitygenericlrtable()
        self.mplsldpentitygenericlrtable.parent = self
        self._children_name_map["mplsldpentitygenericlrtable"] = "mplsLdpEntityGenericLRTable"
        self._children_yang_names.add("mplsLdpEntityGenericLRTable")


    class Mplsldpentitygenericlrtable(Entity):
        """
        The MPLS LDP Entity Generic Label Range (LR)
        Table.
        
        The purpose of this table is to provide a mechanism
        for configurating a contiguous range of generic labels,
        or a 'label range' for LDP Entities.
        
        LDP Entities which use Generic Labels must have at least
        one entry in this table.  In other words, this table
        'extends' the mpldLdpEntityTable for Generic Labels.
        
        .. attribute:: mplsldpentitygenericlrentry
        
        	A row in the LDP Entity Generic Label Range (LR) Table.  One entry in this table contains information on a single range of labels represented by the configured Upper and Lower Bounds pairs.  NOTE\: there is NO corresponding LDP message which relates to the information in this table, however, this table does provide a way for a user to 'reserve' a generic label range.  NOTE\:  The ranges for a specific LDP Entity are UNIQUE and non\-overlapping.  A row will not be created unless a unique and non\-overlapping range is specified
        	**type**\: list of    :py:class:`Mplsldpentitygenericlrentry <ydk.models.cisco_ios_xe.MPLS_LDP_GENERIC_STD_MIB.MplsLdpGenericStdMib.Mplsldpentitygenericlrtable.Mplsldpentitygenericlrentry>`
        
        

        """

        _prefix = 'MPLS-LDP-GENERIC-STD-MIB'
        _revision = '2004-06-03'

        def __init__(self):
            super(MplsLdpGenericStdMib.Mplsldpentitygenericlrtable, self).__init__()

            self.yang_name = "mplsLdpEntityGenericLRTable"
            self.yang_parent_name = "MPLS-LDP-GENERIC-STD-MIB"

            self.mplsldpentitygenericlrentry = YList(self)

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
                        super(MplsLdpGenericStdMib.Mplsldpentitygenericlrtable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(MplsLdpGenericStdMib.Mplsldpentitygenericlrtable, self).__setattr__(name, value)


        class Mplsldpentitygenericlrentry(Entity):
            """
            A row in the LDP Entity Generic Label
            Range (LR) Table.  One entry in this table contains
            information on a single range of labels
            represented by the configured Upper and Lower
            Bounds pairs.  NOTE\: there is NO corresponding
            LDP message which relates to the information
            in this table, however, this table does provide
            a way for a user to 'reserve' a generic label
            range.
            
            NOTE\:  The ranges for a specific LDP Entity
            are UNIQUE and non\-overlapping.
            
            A row will not be created unless a unique and
            non\-overlapping range is specified.
            
            .. attribute:: mplsldpentityldpid  <key>
            
            	
            	**type**\:  str
            
            	**refers to**\:  :py:class:`mplsldpentityldpid <ydk.models.cisco_ios_xe.MPLS_LDP_STD_MIB.MplsLdpStdMib.Mplsldpentitytable.Mplsldpentityentry>`
            
            .. attribute:: mplsldpentityindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            	**refers to**\:  :py:class:`mplsldpentityindex <ydk.models.cisco_ios_xe.MPLS_LDP_STD_MIB.MplsLdpStdMib.Mplsldpentitytable.Mplsldpentityentry>`
            
            .. attribute:: mplsldpentitygenericlrmin  <key>
            
            	The minimum label configured for this range
            	**type**\:  int
            
            	**range:** 0..1048575
            
            .. attribute:: mplsldpentitygenericlrmax  <key>
            
            	The maximum label configured for this range
            	**type**\:  int
            
            	**range:** 0..1048575
            
            .. attribute:: mplsldpentitygenericifindexorzero
            
            	This value represents either the InterfaceIndex of the 'ifLayer' where these Generic Label would be created,   or 0 (zero).  The value of zero means that the InterfaceIndex is not known.  However, if the InterfaceIndex is known, then it must be represented by this value.  If an InterfaceIndex becomes known, then the network management entity (e.g., SNMP agent) responsible for this object MUST change the value from 0 (zero) to the value of the InterfaceIndex
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: mplsldpentitygenericlabelspace
            
            	This value of this object is perPlatform(1), then this means that the label space type is per platform.  If this object is perInterface(2), then this means that the label space type is per Interface
            	**type**\:   :py:class:`Mplsldpentitygenericlabelspace <ydk.models.cisco_ios_xe.MPLS_LDP_GENERIC_STD_MIB.MplsLdpGenericStdMib.Mplsldpentitygenericlrtable.Mplsldpentitygenericlrentry.Mplsldpentitygenericlabelspace>`
            
            .. attribute:: mplsldpentitygenericlrrowstatus
            
            	The status of this conceptual row.  All writable objects in this row may be modified at any time, however, as described in  detail in the section entitled, 'Changing Values After Session Establishment', and again described in the DESCRIPTION clause of the mplsLdpEntityAdminStatus object, if a session has been initiated with a Peer, changing objects in this table will wreak havoc with the session and interrupt traffic. To repeat again\:  the recommended procedure is to set the mplsLdpEntityAdminStatus to down, thereby explicitly causing a session to be torn down. Then, change objects in this entry, then set the mplsLdpEntityAdminStatus to enable which enables a new session to be initiated.  There must exist at least one entry in this table for every LDP Entity that has a generic label configured
            	**type**\:   :py:class:`Rowstatus <ydk.models.cisco_ios_xe.SNMPv2_TC.Rowstatus>`
            
            .. attribute:: mplsldpentitygenericlrstoragetype
            
            	The storage type for this conceptual row. Conceptual rows having the value 'permanent(4)' need not allow write\-access to any columnar objects in the row
            	**type**\:   :py:class:`Storagetype <ydk.models.cisco_ios_xe.SNMPv2_TC.Storagetype>`
            
            

            """

            _prefix = 'MPLS-LDP-GENERIC-STD-MIB'
            _revision = '2004-06-03'

            def __init__(self):
                super(MplsLdpGenericStdMib.Mplsldpentitygenericlrtable.Mplsldpentitygenericlrentry, self).__init__()

                self.yang_name = "mplsLdpEntityGenericLREntry"
                self.yang_parent_name = "mplsLdpEntityGenericLRTable"

                self.mplsldpentityldpid = YLeaf(YType.str, "mplsLdpEntityLdpId")

                self.mplsldpentityindex = YLeaf(YType.str, "mplsLdpEntityIndex")

                self.mplsldpentitygenericlrmin = YLeaf(YType.uint32, "mplsLdpEntityGenericLRMin")

                self.mplsldpentitygenericlrmax = YLeaf(YType.uint32, "mplsLdpEntityGenericLRMax")

                self.mplsldpentitygenericifindexorzero = YLeaf(YType.int32, "mplsLdpEntityGenericIfIndexOrZero")

                self.mplsldpentitygenericlabelspace = YLeaf(YType.enumeration, "mplsLdpEntityGenericLabelSpace")

                self.mplsldpentitygenericlrrowstatus = YLeaf(YType.enumeration, "mplsLdpEntityGenericLRRowStatus")

                self.mplsldpentitygenericlrstoragetype = YLeaf(YType.enumeration, "mplsLdpEntityGenericLRStorageType")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("mplsldpentityldpid",
                                "mplsldpentityindex",
                                "mplsldpentitygenericlrmin",
                                "mplsldpentitygenericlrmax",
                                "mplsldpentitygenericifindexorzero",
                                "mplsldpentitygenericlabelspace",
                                "mplsldpentitygenericlrrowstatus",
                                "mplsldpentitygenericlrstoragetype") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(MplsLdpGenericStdMib.Mplsldpentitygenericlrtable.Mplsldpentitygenericlrentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(MplsLdpGenericStdMib.Mplsldpentitygenericlrtable.Mplsldpentitygenericlrentry, self).__setattr__(name, value)

            class Mplsldpentitygenericlabelspace(Enum):
                """
                Mplsldpentitygenericlabelspace

                This value of this object is perPlatform(1), then

                this means that the label space type is

                per platform.

                If this object is perInterface(2), then this

                means that the label space type is per Interface.

                .. data:: perPlatform = 1

                .. data:: perInterface = 2

                """

                perPlatform = Enum.YLeaf(1, "perPlatform")

                perInterface = Enum.YLeaf(2, "perInterface")


            def has_data(self):
                return (
                    self.mplsldpentityldpid.is_set or
                    self.mplsldpentityindex.is_set or
                    self.mplsldpentitygenericlrmin.is_set or
                    self.mplsldpentitygenericlrmax.is_set or
                    self.mplsldpentitygenericifindexorzero.is_set or
                    self.mplsldpentitygenericlabelspace.is_set or
                    self.mplsldpentitygenericlrrowstatus.is_set or
                    self.mplsldpentitygenericlrstoragetype.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.mplsldpentityldpid.yfilter != YFilter.not_set or
                    self.mplsldpentityindex.yfilter != YFilter.not_set or
                    self.mplsldpentitygenericlrmin.yfilter != YFilter.not_set or
                    self.mplsldpentitygenericlrmax.yfilter != YFilter.not_set or
                    self.mplsldpentitygenericifindexorzero.yfilter != YFilter.not_set or
                    self.mplsldpentitygenericlabelspace.yfilter != YFilter.not_set or
                    self.mplsldpentitygenericlrrowstatus.yfilter != YFilter.not_set or
                    self.mplsldpentitygenericlrstoragetype.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "mplsLdpEntityGenericLREntry" + "[mplsLdpEntityLdpId='" + self.mplsldpentityldpid.get() + "']" + "[mplsLdpEntityIndex='" + self.mplsldpentityindex.get() + "']" + "[mplsLdpEntityGenericLRMin='" + self.mplsldpentitygenericlrmin.get() + "']" + "[mplsLdpEntityGenericLRMax='" + self.mplsldpentitygenericlrmax.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "MPLS-LDP-GENERIC-STD-MIB:MPLS-LDP-GENERIC-STD-MIB/mplsLdpEntityGenericLRTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.mplsldpentityldpid.is_set or self.mplsldpentityldpid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsldpentityldpid.get_name_leafdata())
                if (self.mplsldpentityindex.is_set or self.mplsldpentityindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsldpentityindex.get_name_leafdata())
                if (self.mplsldpentitygenericlrmin.is_set or self.mplsldpentitygenericlrmin.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsldpentitygenericlrmin.get_name_leafdata())
                if (self.mplsldpentitygenericlrmax.is_set or self.mplsldpentitygenericlrmax.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsldpentitygenericlrmax.get_name_leafdata())
                if (self.mplsldpentitygenericifindexorzero.is_set or self.mplsldpentitygenericifindexorzero.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsldpentitygenericifindexorzero.get_name_leafdata())
                if (self.mplsldpentitygenericlabelspace.is_set or self.mplsldpentitygenericlabelspace.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsldpentitygenericlabelspace.get_name_leafdata())
                if (self.mplsldpentitygenericlrrowstatus.is_set or self.mplsldpentitygenericlrrowstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsldpentitygenericlrrowstatus.get_name_leafdata())
                if (self.mplsldpentitygenericlrstoragetype.is_set or self.mplsldpentitygenericlrstoragetype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsldpentitygenericlrstoragetype.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "mplsLdpEntityLdpId" or name == "mplsLdpEntityIndex" or name == "mplsLdpEntityGenericLRMin" or name == "mplsLdpEntityGenericLRMax" or name == "mplsLdpEntityGenericIfIndexOrZero" or name == "mplsLdpEntityGenericLabelSpace" or name == "mplsLdpEntityGenericLRRowStatus" or name == "mplsLdpEntityGenericLRStorageType"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "mplsLdpEntityLdpId"):
                    self.mplsldpentityldpid = value
                    self.mplsldpentityldpid.value_namespace = name_space
                    self.mplsldpentityldpid.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsLdpEntityIndex"):
                    self.mplsldpentityindex = value
                    self.mplsldpentityindex.value_namespace = name_space
                    self.mplsldpentityindex.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsLdpEntityGenericLRMin"):
                    self.mplsldpentitygenericlrmin = value
                    self.mplsldpentitygenericlrmin.value_namespace = name_space
                    self.mplsldpentitygenericlrmin.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsLdpEntityGenericLRMax"):
                    self.mplsldpentitygenericlrmax = value
                    self.mplsldpentitygenericlrmax.value_namespace = name_space
                    self.mplsldpentitygenericlrmax.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsLdpEntityGenericIfIndexOrZero"):
                    self.mplsldpentitygenericifindexorzero = value
                    self.mplsldpentitygenericifindexorzero.value_namespace = name_space
                    self.mplsldpentitygenericifindexorzero.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsLdpEntityGenericLabelSpace"):
                    self.mplsldpentitygenericlabelspace = value
                    self.mplsldpentitygenericlabelspace.value_namespace = name_space
                    self.mplsldpentitygenericlabelspace.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsLdpEntityGenericLRRowStatus"):
                    self.mplsldpentitygenericlrrowstatus = value
                    self.mplsldpentitygenericlrrowstatus.value_namespace = name_space
                    self.mplsldpentitygenericlrrowstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsLdpEntityGenericLRStorageType"):
                    self.mplsldpentitygenericlrstoragetype = value
                    self.mplsldpentitygenericlrstoragetype.value_namespace = name_space
                    self.mplsldpentitygenericlrstoragetype.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.mplsldpentitygenericlrentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.mplsldpentitygenericlrentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "mplsLdpEntityGenericLRTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "MPLS-LDP-GENERIC-STD-MIB:MPLS-LDP-GENERIC-STD-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "mplsLdpEntityGenericLREntry"):
                for c in self.mplsldpentitygenericlrentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = MplsLdpGenericStdMib.Mplsldpentitygenericlrtable.Mplsldpentitygenericlrentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.mplsldpentitygenericlrentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "mplsLdpEntityGenericLREntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (self.mplsldpentitygenericlrtable is not None and self.mplsldpentitygenericlrtable.has_data())

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.mplsldpentitygenericlrtable is not None and self.mplsldpentitygenericlrtable.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "MPLS-LDP-GENERIC-STD-MIB:MPLS-LDP-GENERIC-STD-MIB" + path_buffer

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

        if (child_yang_name == "mplsLdpEntityGenericLRTable"):
            if (self.mplsldpentitygenericlrtable is None):
                self.mplsldpentitygenericlrtable = MplsLdpGenericStdMib.Mplsldpentitygenericlrtable()
                self.mplsldpentitygenericlrtable.parent = self
                self._children_name_map["mplsldpentitygenericlrtable"] = "mplsLdpEntityGenericLRTable"
            return self.mplsldpentitygenericlrtable

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "mplsLdpEntityGenericLRTable"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = MplsLdpGenericStdMib()
        return self._top_entity

