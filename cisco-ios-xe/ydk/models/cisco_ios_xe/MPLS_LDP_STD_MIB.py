""" MPLS_LDP_STD_MIB 

Copyright (C) The Internet Society (2004). The
initial version of this MIB module was published


in RFC 3815. For full legal notices see the RFC
itself or see\:
http\://www.ietf.org/copyrights/ianamib.html

This MIB contains managed object definitions for the
'Multiprotocol Label Switching, Label Distribution
Protocol, LDP' document.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class MplsLdpStdMib(Entity):
    """
    
    
    .. attribute:: mplsfecobjects
    
    	
    	**type**\:   :py:class:`Mplsfecobjects <ydk.models.cisco_ios_xe.MPLS_LDP_STD_MIB.MplsLdpStdMib.Mplsfecobjects>`
    
    .. attribute:: mplsfectable
    
    	This table represents the FEC (Forwarding Equivalence Class) Information associated with an LSP
    	**type**\:   :py:class:`Mplsfectable <ydk.models.cisco_ios_xe.MPLS_LDP_STD_MIB.MplsLdpStdMib.Mplsfectable>`
    
    .. attribute:: mplsinsegmentldplsptable
    
    	A table of LDP LSP's which map to the mplsInSegmentTable in the MPLS\-LSR\-STD\-MIB module
    	**type**\:   :py:class:`Mplsinsegmentldplsptable <ydk.models.cisco_ios_xe.MPLS_LDP_STD_MIB.MplsLdpStdMib.Mplsinsegmentldplsptable>`
    
    .. attribute:: mplsldpentityobjects
    
    	
    	**type**\:   :py:class:`Mplsldpentityobjects <ydk.models.cisco_ios_xe.MPLS_LDP_STD_MIB.MplsLdpStdMib.Mplsldpentityobjects>`
    
    .. attribute:: mplsldpentitytable
    
    	This table contains information about the MPLS Label Distribution Protocol Entities which exist on this Label Switching Router (LSR) or Label Edge Router (LER)
    	**type**\:   :py:class:`Mplsldpentitytable <ydk.models.cisco_ios_xe.MPLS_LDP_STD_MIB.MplsLdpStdMib.Mplsldpentitytable>`
    
    .. attribute:: mplsldphelloadjacencytable
    
    	A table of Hello Adjacencies for Sessions
    	**type**\:   :py:class:`Mplsldphelloadjacencytable <ydk.models.cisco_ios_xe.MPLS_LDP_STD_MIB.MplsLdpStdMib.Mplsldphelloadjacencytable>`
    
    .. attribute:: mplsldplspfectable
    
    	A table which shows the relationship between LDP LSPs and FECs.  Each row represents a single LDP LSP to FEC association
    	**type**\:   :py:class:`Mplsldplspfectable <ydk.models.cisco_ios_xe.MPLS_LDP_STD_MIB.MplsLdpStdMib.Mplsldplspfectable>`
    
    .. attribute:: mplsldplsrobjects
    
    	
    	**type**\:   :py:class:`Mplsldplsrobjects <ydk.models.cisco_ios_xe.MPLS_LDP_STD_MIB.MplsLdpStdMib.Mplsldplsrobjects>`
    
    .. attribute:: mplsldppeertable
    
    	Information about LDP peers known by Entities in the mplsLdpEntityTable.  The information in this table is based on information from the Entity\-Peer interaction during session initialization but is not appropriate for the mplsLdpSessionTable, because objects in this table may or may not be used in session establishment
    	**type**\:   :py:class:`Mplsldppeertable <ydk.models.cisco_ios_xe.MPLS_LDP_STD_MIB.MplsLdpStdMib.Mplsldppeertable>`
    
    .. attribute:: mplsldpsessionobjects
    
    	
    	**type**\:   :py:class:`Mplsldpsessionobjects <ydk.models.cisco_ios_xe.MPLS_LDP_STD_MIB.MplsLdpStdMib.Mplsldpsessionobjects>`
    
    .. attribute:: mplsldpsessionpeeraddrtable
    
    	This table 'extends' the mplsLdpSessionTable. This table is used to store Label Address Information from Label Address Messages received by this LSR from Peers.  This table is read\-only and should be updated   when Label Withdraw Address Messages are received, i.e., Rows should be deleted as appropriate.  NOTE\:  since more than one address may be contained in a Label Address Message, this table 'sparse augments', the mplsLdpSessionTable's information
    	**type**\:   :py:class:`Mplsldpsessionpeeraddrtable <ydk.models.cisco_ios_xe.MPLS_LDP_STD_MIB.MplsLdpStdMib.Mplsldpsessionpeeraddrtable>`
    
    .. attribute:: mplsoutsegmentldplsptable
    
    	A table of LDP LSP's which map to the mplsOutSegmentTable in the MPLS\-LSR\-STD\-MIB
    	**type**\:   :py:class:`Mplsoutsegmentldplsptable <ydk.models.cisco_ios_xe.MPLS_LDP_STD_MIB.MplsLdpStdMib.Mplsoutsegmentldplsptable>`
    
    

    """

    _prefix = 'MPLS-LDP-STD-MIB'
    _revision = '2004-06-03'

    def __init__(self):
        super(MplsLdpStdMib, self).__init__()
        self._top_entity = None

        self.yang_name = "MPLS-LDP-STD-MIB"
        self.yang_parent_name = "MPLS-LDP-STD-MIB"

        self.mplsfecobjects = MplsLdpStdMib.Mplsfecobjects()
        self.mplsfecobjects.parent = self
        self._children_name_map["mplsfecobjects"] = "mplsFecObjects"
        self._children_yang_names.add("mplsFecObjects")

        self.mplsfectable = MplsLdpStdMib.Mplsfectable()
        self.mplsfectable.parent = self
        self._children_name_map["mplsfectable"] = "mplsFecTable"
        self._children_yang_names.add("mplsFecTable")

        self.mplsinsegmentldplsptable = MplsLdpStdMib.Mplsinsegmentldplsptable()
        self.mplsinsegmentldplsptable.parent = self
        self._children_name_map["mplsinsegmentldplsptable"] = "mplsInSegmentLdpLspTable"
        self._children_yang_names.add("mplsInSegmentLdpLspTable")

        self.mplsldpentityobjects = MplsLdpStdMib.Mplsldpentityobjects()
        self.mplsldpentityobjects.parent = self
        self._children_name_map["mplsldpentityobjects"] = "mplsLdpEntityObjects"
        self._children_yang_names.add("mplsLdpEntityObjects")

        self.mplsldpentitytable = MplsLdpStdMib.Mplsldpentitytable()
        self.mplsldpentitytable.parent = self
        self._children_name_map["mplsldpentitytable"] = "mplsLdpEntityTable"
        self._children_yang_names.add("mplsLdpEntityTable")

        self.mplsldphelloadjacencytable = MplsLdpStdMib.Mplsldphelloadjacencytable()
        self.mplsldphelloadjacencytable.parent = self
        self._children_name_map["mplsldphelloadjacencytable"] = "mplsLdpHelloAdjacencyTable"
        self._children_yang_names.add("mplsLdpHelloAdjacencyTable")

        self.mplsldplspfectable = MplsLdpStdMib.Mplsldplspfectable()
        self.mplsldplspfectable.parent = self
        self._children_name_map["mplsldplspfectable"] = "mplsLdpLspFecTable"
        self._children_yang_names.add("mplsLdpLspFecTable")

        self.mplsldplsrobjects = MplsLdpStdMib.Mplsldplsrobjects()
        self.mplsldplsrobjects.parent = self
        self._children_name_map["mplsldplsrobjects"] = "mplsLdpLsrObjects"
        self._children_yang_names.add("mplsLdpLsrObjects")

        self.mplsldppeertable = MplsLdpStdMib.Mplsldppeertable()
        self.mplsldppeertable.parent = self
        self._children_name_map["mplsldppeertable"] = "mplsLdpPeerTable"
        self._children_yang_names.add("mplsLdpPeerTable")

        self.mplsldpsessionobjects = MplsLdpStdMib.Mplsldpsessionobjects()
        self.mplsldpsessionobjects.parent = self
        self._children_name_map["mplsldpsessionobjects"] = "mplsLdpSessionObjects"
        self._children_yang_names.add("mplsLdpSessionObjects")

        self.mplsldpsessionpeeraddrtable = MplsLdpStdMib.Mplsldpsessionpeeraddrtable()
        self.mplsldpsessionpeeraddrtable.parent = self
        self._children_name_map["mplsldpsessionpeeraddrtable"] = "mplsLdpSessionPeerAddrTable"
        self._children_yang_names.add("mplsLdpSessionPeerAddrTable")

        self.mplsoutsegmentldplsptable = MplsLdpStdMib.Mplsoutsegmentldplsptable()
        self.mplsoutsegmentldplsptable.parent = self
        self._children_name_map["mplsoutsegmentldplsptable"] = "mplsOutSegmentLdpLspTable"
        self._children_yang_names.add("mplsOutSegmentLdpLspTable")


    class Mplsldplsrobjects(Entity):
        """
        
        
        .. attribute:: mplsldplsrid
        
        	The Label Switching Router's Identifier
        	**type**\:  str
        
        	**length:** 4
        
        .. attribute:: mplsldplsrloopdetectioncapable
        
        	A indication of whether this Label Switching Router supports loop detection.  none(1) \-\- Loop Detection is not supported            on this LSR.  other(2) \-\- Loop Detection is supported but             by a method other than those             listed below.  hopCount(3) \-\- Loop Detection is supported by                Hop Count only.  pathVector(4) \-\- Loop Detection is supported by                  Path Vector only.  hopCountAndPathVector(5) \-\- Loop Detection is                      supported by both Hop Count                      And Path Vector.  Since Loop Detection is determined during Session Initialization, an individual session may not be running with loop detection.  This object simply gives an indication of whether or not the LSR has the ability to support Loop Detection and which types
        	**type**\:   :py:class:`Mplsldplsrloopdetectioncapable <ydk.models.cisco_ios_xe.MPLS_LDP_STD_MIB.MplsLdpStdMib.Mplsldplsrobjects.Mplsldplsrloopdetectioncapable>`
        
        

        """

        _prefix = 'MPLS-LDP-STD-MIB'
        _revision = '2004-06-03'

        def __init__(self):
            super(MplsLdpStdMib.Mplsldplsrobjects, self).__init__()

            self.yang_name = "mplsLdpLsrObjects"
            self.yang_parent_name = "MPLS-LDP-STD-MIB"

            self.mplsldplsrid = YLeaf(YType.str, "mplsLdpLsrId")

            self.mplsldplsrloopdetectioncapable = YLeaf(YType.enumeration, "mplsLdpLsrLoopDetectionCapable")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("mplsldplsrid",
                            "mplsldplsrloopdetectioncapable") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(MplsLdpStdMib.Mplsldplsrobjects, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(MplsLdpStdMib.Mplsldplsrobjects, self).__setattr__(name, value)

        class Mplsldplsrloopdetectioncapable(Enum):
            """
            Mplsldplsrloopdetectioncapable

            A indication of whether this

            Label Switching Router supports

            loop detection.

            none(1) \-\- Loop Detection is not supported

                       on this LSR.

            other(2) \-\- Loop Detection is supported but

                        by a method other than those

                        listed below.

            hopCount(3) \-\- Loop Detection is supported by

                           Hop Count only.

            pathVector(4) \-\- Loop Detection is supported by

                             Path Vector only.

            hopCountAndPathVector(5) \-\- Loop Detection is

                                 supported by both Hop Count

                                 And Path Vector.

            Since Loop Detection is determined during

            Session Initialization, an individual session

            may not be running with loop detection.  This

            object simply gives an indication of whether or not the

            LSR has the ability to support Loop Detection and

            which types.

            .. data:: none = 1

            .. data:: other = 2

            .. data:: hopCount = 3

            .. data:: pathVector = 4

            .. data:: hopCountAndPathVector = 5

            """

            none = Enum.YLeaf(1, "none")

            other = Enum.YLeaf(2, "other")

            hopCount = Enum.YLeaf(3, "hopCount")

            pathVector = Enum.YLeaf(4, "pathVector")

            hopCountAndPathVector = Enum.YLeaf(5, "hopCountAndPathVector")


        def has_data(self):
            return (
                self.mplsldplsrid.is_set or
                self.mplsldplsrloopdetectioncapable.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.mplsldplsrid.yfilter != YFilter.not_set or
                self.mplsldplsrloopdetectioncapable.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "mplsLdpLsrObjects" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "MPLS-LDP-STD-MIB:MPLS-LDP-STD-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.mplsldplsrid.is_set or self.mplsldplsrid.yfilter != YFilter.not_set):
                leaf_name_data.append(self.mplsldplsrid.get_name_leafdata())
            if (self.mplsldplsrloopdetectioncapable.is_set or self.mplsldplsrloopdetectioncapable.yfilter != YFilter.not_set):
                leaf_name_data.append(self.mplsldplsrloopdetectioncapable.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "mplsLdpLsrId" or name == "mplsLdpLsrLoopDetectionCapable"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "mplsLdpLsrId"):
                self.mplsldplsrid = value
                self.mplsldplsrid.value_namespace = name_space
                self.mplsldplsrid.value_namespace_prefix = name_space_prefix
            if(value_path == "mplsLdpLsrLoopDetectionCapable"):
                self.mplsldplsrloopdetectioncapable = value
                self.mplsldplsrloopdetectioncapable.value_namespace = name_space
                self.mplsldplsrloopdetectioncapable.value_namespace_prefix = name_space_prefix


    class Mplsldpentityobjects(Entity):
        """
        
        
        .. attribute:: mplsldpentityindexnext
        
        	This object contains an appropriate value to be used for mplsLdpEntityIndex when creating entries in the mplsLdpEntityTable. The value 0 indicates that no unassigned entries are available
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: mplsldpentitylastchange
        
        	The value of sysUpTime at the time of the most recent addition or deletion of an entry to/from the mplsLdpEntityTable/mplsLdpEntityStatsTable, or the most recent change in value of any objects in the mplsLdpEntityTable.   If no such changes have occurred since the last re\-initialization of the local management subsystem, then this object contains a zero value
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'MPLS-LDP-STD-MIB'
        _revision = '2004-06-03'

        def __init__(self):
            super(MplsLdpStdMib.Mplsldpentityobjects, self).__init__()

            self.yang_name = "mplsLdpEntityObjects"
            self.yang_parent_name = "MPLS-LDP-STD-MIB"

            self.mplsldpentityindexnext = YLeaf(YType.uint32, "mplsLdpEntityIndexNext")

            self.mplsldpentitylastchange = YLeaf(YType.uint32, "mplsLdpEntityLastChange")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("mplsldpentityindexnext",
                            "mplsldpentitylastchange") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(MplsLdpStdMib.Mplsldpentityobjects, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(MplsLdpStdMib.Mplsldpentityobjects, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.mplsldpentityindexnext.is_set or
                self.mplsldpentitylastchange.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.mplsldpentityindexnext.yfilter != YFilter.not_set or
                self.mplsldpentitylastchange.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "mplsLdpEntityObjects" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "MPLS-LDP-STD-MIB:MPLS-LDP-STD-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.mplsldpentityindexnext.is_set or self.mplsldpentityindexnext.yfilter != YFilter.not_set):
                leaf_name_data.append(self.mplsldpentityindexnext.get_name_leafdata())
            if (self.mplsldpentitylastchange.is_set or self.mplsldpentitylastchange.yfilter != YFilter.not_set):
                leaf_name_data.append(self.mplsldpentitylastchange.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "mplsLdpEntityIndexNext" or name == "mplsLdpEntityLastChange"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "mplsLdpEntityIndexNext"):
                self.mplsldpentityindexnext = value
                self.mplsldpentityindexnext.value_namespace = name_space
                self.mplsldpentityindexnext.value_namespace_prefix = name_space_prefix
            if(value_path == "mplsLdpEntityLastChange"):
                self.mplsldpentitylastchange = value
                self.mplsldpentitylastchange.value_namespace = name_space
                self.mplsldpentitylastchange.value_namespace_prefix = name_space_prefix


    class Mplsldpsessionobjects(Entity):
        """
        
        
        .. attribute:: mplsldplspfeclastchange
        
        	The value of sysUpTime at the time of the most recent addition/deletion of an entry to/from the mplsLdpLspFecTable or the most recent change in values to any objects in the mplsLdpLspFecTable.  If no such changes have occurred since the last re\-initialization of the local management subsystem, then this object contains a zero value
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: mplsldppeerlastchange
        
        	The value of sysUpTime at the time of the most recent addition or deletion to/from the mplsLdpPeerTable/mplsLdpSessionTable
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'MPLS-LDP-STD-MIB'
        _revision = '2004-06-03'

        def __init__(self):
            super(MplsLdpStdMib.Mplsldpsessionobjects, self).__init__()

            self.yang_name = "mplsLdpSessionObjects"
            self.yang_parent_name = "MPLS-LDP-STD-MIB"

            self.mplsldplspfeclastchange = YLeaf(YType.uint32, "mplsLdpLspFecLastChange")

            self.mplsldppeerlastchange = YLeaf(YType.uint32, "mplsLdpPeerLastChange")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("mplsldplspfeclastchange",
                            "mplsldppeerlastchange") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(MplsLdpStdMib.Mplsldpsessionobjects, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(MplsLdpStdMib.Mplsldpsessionobjects, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.mplsldplspfeclastchange.is_set or
                self.mplsldppeerlastchange.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.mplsldplspfeclastchange.yfilter != YFilter.not_set or
                self.mplsldppeerlastchange.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "mplsLdpSessionObjects" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "MPLS-LDP-STD-MIB:MPLS-LDP-STD-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.mplsldplspfeclastchange.is_set or self.mplsldplspfeclastchange.yfilter != YFilter.not_set):
                leaf_name_data.append(self.mplsldplspfeclastchange.get_name_leafdata())
            if (self.mplsldppeerlastchange.is_set or self.mplsldppeerlastchange.yfilter != YFilter.not_set):
                leaf_name_data.append(self.mplsldppeerlastchange.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "mplsLdpLspFecLastChange" or name == "mplsLdpPeerLastChange"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "mplsLdpLspFecLastChange"):
                self.mplsldplspfeclastchange = value
                self.mplsldplspfeclastchange.value_namespace = name_space
                self.mplsldplspfeclastchange.value_namespace_prefix = name_space_prefix
            if(value_path == "mplsLdpPeerLastChange"):
                self.mplsldppeerlastchange = value
                self.mplsldppeerlastchange.value_namespace = name_space
                self.mplsldppeerlastchange.value_namespace_prefix = name_space_prefix


    class Mplsfecobjects(Entity):
        """
        
        
        .. attribute:: mplsfecindexnext
        
        	This object contains an appropriate value to be used for mplsFecIndex when creating entries in the mplsFecTable. The value 0 indicates that no unassigned entries are available
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: mplsfeclastchange
        
        	The value of sysUpTime at the time of the most recent addition/deletion of an entry to/from the mplsLdpFectTable or the most recent change in values to any objects in the mplsLdpFecTable.  If no such changes have occurred since the last re\-initialization of the local management subsystem, then this object contains a zero value
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'MPLS-LDP-STD-MIB'
        _revision = '2004-06-03'

        def __init__(self):
            super(MplsLdpStdMib.Mplsfecobjects, self).__init__()

            self.yang_name = "mplsFecObjects"
            self.yang_parent_name = "MPLS-LDP-STD-MIB"

            self.mplsfecindexnext = YLeaf(YType.uint32, "mplsFecIndexNext")

            self.mplsfeclastchange = YLeaf(YType.uint32, "mplsFecLastChange")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("mplsfecindexnext",
                            "mplsfeclastchange") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(MplsLdpStdMib.Mplsfecobjects, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(MplsLdpStdMib.Mplsfecobjects, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.mplsfecindexnext.is_set or
                self.mplsfeclastchange.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.mplsfecindexnext.yfilter != YFilter.not_set or
                self.mplsfeclastchange.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "mplsFecObjects" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "MPLS-LDP-STD-MIB:MPLS-LDP-STD-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.mplsfecindexnext.is_set or self.mplsfecindexnext.yfilter != YFilter.not_set):
                leaf_name_data.append(self.mplsfecindexnext.get_name_leafdata())
            if (self.mplsfeclastchange.is_set or self.mplsfeclastchange.yfilter != YFilter.not_set):
                leaf_name_data.append(self.mplsfeclastchange.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "mplsFecIndexNext" or name == "mplsFecLastChange"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "mplsFecIndexNext"):
                self.mplsfecindexnext = value
                self.mplsfecindexnext.value_namespace = name_space
                self.mplsfecindexnext.value_namespace_prefix = name_space_prefix
            if(value_path == "mplsFecLastChange"):
                self.mplsfeclastchange = value
                self.mplsfeclastchange.value_namespace = name_space
                self.mplsfeclastchange.value_namespace_prefix = name_space_prefix


    class Mplsldpentitytable(Entity):
        """
        This table contains information about the
        MPLS Label Distribution Protocol Entities which
        exist on this Label Switching Router (LSR)
        or Label Edge Router (LER).
        
        .. attribute:: mplsldpentityentry
        
        	An entry in this table represents an LDP entity. An entry can be created by a network administrator or by an SNMP agent as instructed by LDP
        	**type**\: list of    :py:class:`Mplsldpentityentry <ydk.models.cisco_ios_xe.MPLS_LDP_STD_MIB.MplsLdpStdMib.Mplsldpentitytable.Mplsldpentityentry>`
        
        

        """

        _prefix = 'MPLS-LDP-STD-MIB'
        _revision = '2004-06-03'

        def __init__(self):
            super(MplsLdpStdMib.Mplsldpentitytable, self).__init__()

            self.yang_name = "mplsLdpEntityTable"
            self.yang_parent_name = "MPLS-LDP-STD-MIB"

            self.mplsldpentityentry = YList(self)

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
                        super(MplsLdpStdMib.Mplsldpentitytable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(MplsLdpStdMib.Mplsldpentitytable, self).__setattr__(name, value)


        class Mplsldpentityentry(Entity):
            """
            An entry in this table represents an LDP entity.
            An entry can be created by a network administrator
            or by an SNMP agent as instructed by LDP.
            
            .. attribute:: mplsldpentityldpid  <key>
            
            	The LDP identifier
            	**type**\:  str
            
            .. attribute:: mplsldpentityindex  <key>
            
            	This index is used as a secondary index to uniquely identify this row.  Before creating a row in this table, the 'mplsLdpEntityIndexNext' object should be retrieved. That value should be used for the value of this index when creating a row in this table.  NOTE\:  if a value of zero (0) is retrieved, that indicates that no rows can be created in this table at this time.  A secondary index (this object) is meaningful to some but not all, LDP implementations.  For example an LDP implementation which uses PPP would use this index to differentiate PPP sub\-links.  Another way to use this index is to give this the value of ifIndex.  However, this is dependant   on the implementation
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            .. attribute:: mplsldpentityadminstatus
            
            	The administrative status of this LDP Entity. If this object is changed from 'enable' to 'disable' and this entity has already attempted to establish contact with a Peer, then all contact with that Peer is lost and all information from that Peer needs to be removed from the MIB. (This implies that the network management subsystem should clean up any related entry in the mplsLdpPeerTable.  This further implies that a 'tear\-down' for that session is issued and the session and all information related to that session cease to exist).  At this point the operator is able to change values which are related to this entity.  When the admin status is set back to 'enable', then this Entity will attempt to establish a new session with the Peer
            	**type**\:   :py:class:`Mplsldpentityadminstatus <ydk.models.cisco_ios_xe.MPLS_LDP_STD_MIB.MplsLdpStdMib.Mplsldpentitytable.Mplsldpentityentry.Mplsldpentityadminstatus>`
            
            .. attribute:: mplsldpentitydiscontinuitytime
            
            	The value of sysUpTime on the most recent occasion at which any one or more of this entity's counters suffered a discontinuity.  The relevant counters are the specific instances associated with this entity of any Counter32 object contained in the 'mplsLdpEntityStatsTable'.  If no such discontinuities have occurred since the last re\-initialization of the local management subsystem, then this object contains a zero value
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplsldpentityhelloholdtimer
            
            	The 16\-bit integer value which is the proposed Hello hold timer for this LDP Entity. The Hello Hold time in seconds.   An LSR maintains a record of Hellos received from potential peers.  This object represents the Hold Time in the Common Hello Parameters TLV of the Hello Message.  A value of 0 is a default value and should be interpretted in conjunction with the mplsLdpEntityTargetPeer object.  If the value of this object is 0\: if the value of the mplsLdpEntityTargetPeer object is false(2), then this specifies that the Hold Time's actual default value is 15 seconds (i.e., the default Hold time for Link Hellos is 15 seconds).  Otherwise if the value of the mplsLdpEntityTargetPeer object is true(1), then this specifies that the Hold Time's actual default value is 45 seconds (i.e., the default Hold time for Targeted Hellos is 45 seconds).  A value of 65535 means infinite (i.e., wait forever).  All other values represent the amount of time in seconds to wait for a Hello Message.  Setting the hold time to a value smaller than 15 is not recommended, although not forbidden according to RFC3036
            	**type**\:  int
            
            	**range:** 0..65535
            
            	**units**\: seconds
            
            .. attribute:: mplsldpentityhopcountlimit
            
            	If the value of this object is 0 (zero), then Loop Detection using Hop Counters is disabled.  If the value of this object is greater than 0 (zero) then Loop Detection using Hop Counters is enabled, and this object specifies this Entity's maximum allowable value for the Hop Count. Also, the value of the object mplsLdpLsrLoopDetectionCapable must be set to either 'hopCount(3)' or 'hopCountAndPathVector(5)' if this object has a value greater than 0 (zero), otherwise it is ignored
            	**type**\:  int
            
            	**range:** 0..255
            
            .. attribute:: mplsldpentityinitsessionthreshold
            
            	When attempting to establish a session with a given Peer, the given LDP Entity should send out the SNMP notification, 'mplsLdpInitSessionThresholdExceeded', when the number of Session Initialization messages sent exceeds this threshold.  The notification is used to notify an operator when this Entity and its Peer are possibly engaged in an endless sequence of messages as each NAKs the other's   Initialization messages with Error Notification messages.  Setting this threshold which triggers the notification is one way to notify the operator.  The notification should be generated each time this threshold is exceeded and for every subsequent Initialization message which is NAK'd with an Error Notification message after this threshold is exceeded.  A value of 0 (zero) for this object indicates that the threshold is infinity, thus the SNMP notification will never be generated
            	**type**\:  int
            
            	**range:** 0..100
            
            .. attribute:: mplsldpentitykeepaliveholdtimer
            
            	The 16\-bit integer value which is the proposed keep alive hold timer for this LDP Entity
            	**type**\:  int
            
            	**range:** 1..65535
            
            	**units**\: seconds
            
            .. attribute:: mplsldpentitylabeldistmethod
            
            	For any given LDP session, the method of label distribution must be specified
            	**type**\:   :py:class:`Mplslabeldistributionmethod <ydk.models.cisco_ios_xe.MPLS_TC_STD_MIB.Mplslabeldistributionmethod>`
            
            .. attribute:: mplsldpentitylabelretentionmode
            
            	The LDP Entity can be configured to use either conservative or liberal label retention mode.  If the value of this object is conservative(1) then advertized label mappings are retained only if they will be used to forward packets, i.e., if label came from a valid next hop.  If the value of this object is liberal(2) then all advertized label mappings are retained whether they are from a valid next hop or not
            	**type**\:   :py:class:`Mplsretentionmode <ydk.models.cisco_ios_xe.MPLS_TC_STD_MIB.Mplsretentionmode>`
            
            .. attribute:: mplsldpentitylabeltype
            
            	Specifies the optional parameters for the LDP Initialization Message.  If the value is generic(1) then no optional parameters will be sent in the LDP Initialization message associated with this Entity.  If the value is atmParameters(2) then a row must be created in the mplsLdpEntityAtmTable, which corresponds to this entry.  If the value is frameRelayParameters(3) then a row must be created in the mplsLdpEntityFrameRelayTable, which corresponds to this entry
            	**type**\:   :py:class:`Mplsldplabeltype <ydk.models.cisco_ios_xe.MPLS_TC_STD_MIB.Mplsldplabeltype>`
            
            .. attribute:: mplsldpentitymaxpdulength
            
            	The maximum PDU Length that is sent in the Common Session Parameters of an Initialization Message. According to the LDP Specification [RFC3036] a value of 255 or less specifies the default maximum length of 4096 octets, this is why the value of this object starts at 256.  The operator should explicitly choose the default value (i.e., 4096), or some other value.  The receiving LSR MUST calculate the maximum PDU length for the session by using the smaller of its and its peer's proposals for Max PDU Length
            	**type**\:  int
            
            	**range:** 256..65535
            
            	**units**\: octets
            
            .. attribute:: mplsldpentityoperstatus
            
            	The operational status of this LDP Entity.  The value of unknown(1) indicates that the operational status cannot be determined at this time.  The value of unknown should be a transient condition before changing to enabled(2) or disabled(3)
            	**type**\:   :py:class:`Mplsldpentityoperstatus <ydk.models.cisco_ios_xe.MPLS_LDP_STD_MIB.MplsLdpStdMib.Mplsldpentitytable.Mplsldpentityentry.Mplsldpentityoperstatus>`
            
            .. attribute:: mplsldpentitypathvectorlimit
            
            	If the value of this object is 0 (zero) then Loop Detection for Path Vectors is disabled.  Otherwise, if this object has a value greater than zero, then Loop Dection for Path Vectors is enabled, and the Path Vector Limit is this value. Also, the value of the object, 'mplsLdpLsrLoopDetectionCapable', must be set to either 'pathVector(4)' or 'hopCountAndPathVector(5)', if this object has a value greater than 0 (zero), otherwise it is ignored
            	**type**\:  int
            
            	**range:** 0..255
            
            .. attribute:: mplsldpentityprotocolversion
            
            	The version number of the LDP protocol which will be used in the session initialization message.  Section 3.5.3 in the LDP Specification specifies that the version of the LDP protocol is negotiated during session establishment. The value of this object represents the value that is sent in the initialization message
            	**type**\:  int
            
            	**range:** 1..65535
            
            .. attribute:: mplsldpentityrowstatus
            
            	The status of this conceptual row.  All writable objects in this row may be modified at any time, however, as described in detail in the section entitled, 'Changing Values After Session Establishment', and again described in the DESCRIPTION clause of the mplsLdpEntityAdminStatus object, if a session has been initiated with a Peer, changing objects in this table will wreak havoc with the session and interrupt traffic.  To repeat again\: the recommended procedure is to set the mplsLdpEntityAdminStatus to down, thereby explicitly causing a session to be torn down. Then, change objects in this entry, then set the mplsLdpEntityAdminStatus to enable, which enables a new session to be initiated
            	**type**\:   :py:class:`Rowstatus <ydk.models.cisco_ios_xe.SNMPv2_TC.Rowstatus>`
            
            .. attribute:: mplsldpentitystatsbadldpidentifiererrors
            
            	This object counts the number of Bad LDP Identifier Fatal Errors detected by the session(s) (past and present) associated with this LDP Entity.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of mplsLdpEntityDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplsldpentitystatsbadmessagelengtherrors
            
            	This object counts the number of Bad Message Length Fatal Errors detected by the session(s) (past and present) associated with this LDP Entity.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of mplsLdpEntityDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplsldpentitystatsbadpdulengtherrors
            
            	This object counts the number of Bad PDU Length Fatal Errors detected by the session(s) (past and present) associated with this LDP Entity.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of mplsLdpEntityDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplsldpentitystatsbadtlvlengtherrors
            
            	This object counts the number of Bad TLV Length Fatal Errors detected by the session(s) (past and present) associated with this LDP Entity.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of mplsLdpEntityDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplsldpentitystatskeepalivetimerexperrors
            
            	This object counts the number of Session Keep Alive Timer Expired Errors detected by the session(s) (past and present) associated with this LDP Entity.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of mplsLdpEntityDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplsldpentitystatsmalformedtlvvalueerrors
            
            	This object counts the number of Malformed TLV Value Fatal Errors detected by the session(s) (past and present) associated with this LDP Entity.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of mplsLdpEntityDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplsldpentitystatssessionattempts
            
            	A count of the Session Initialization messages which were sent or received by this LDP Entity and were NAK'd.   In other words, this counter counts the number of session initializations that failed.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of mplsLdpEntityDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplsldpentitystatssessionrejectedaderrors
            
            	A count of the Session Rejected/Parameters Advertisement Mode Error Notification Messages sent or received by this LDP Entity.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of mplsLdpEntityDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplsldpentitystatssessionrejectedlrerrors
            
            	A count of the Session Rejected/Parameters Label Range Notification Messages sent or received by this LDP Entity.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of mplsLdpEntityDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplsldpentitystatssessionrejectedmaxpduerrors
            
            	A count of the Session Rejected/Parameters  Max Pdu Length Error Notification Messages sent or received by this LDP Entity.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of mplsLdpEntityDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplsldpentitystatssessionrejectednohelloerrors
            
            	A count of the Session Rejected/No Hello Error Notification Messages sent or received by this LDP Entity.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of mplsLdpEntityDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplsldpentitystatsshutdownreceivednotifications
            
            	This object counts the number of Shutdown Notifications received related to session(s) (past and present) associated with this LDP Entity.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of mplsLdpEntityDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplsldpentitystatsshutdownsentnotifications
            
            	This object counts the number of Shutdown Notfications sent related to session(s) (past and present) associated with this LDP Entity.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of   mplsLdpEntityDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplsldpentitystoragetype
            
            	The storage type for this conceptual row. Conceptual rows having the value 'permanent(4)' need not allow write\-access to any columnar objects in the row
            	**type**\:   :py:class:`Storagetype <ydk.models.cisco_ios_xe.SNMPv2_TC.Storagetype>`
            
            .. attribute:: mplsldpentitytargetpeer
            
            	If this LDP entity uses targeted peer then set this to true
            	**type**\:  bool
            
            .. attribute:: mplsldpentitytargetpeeraddr
            
            	The value of the internetwork layer address used for the Extended Discovery.  The value of mplsLdpEntityTargetPeerAddrType specifies how this address is to be interpreted
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: mplsldpentitytargetpeeraddrtype
            
            	The type of the internetwork layer address used for the Extended Discovery.  This object indicates how the value of mplsLdpEntityTargetPeerAddr is to be interpreted
            	**type**\:   :py:class:`Inetaddresstype <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.Inetaddresstype>`
            
            .. attribute:: mplsldpentitytcpport
            
            	The TCP Port for LDP.  The default value is the well\-known value of this port
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: mplsldpentitytransportaddrkind
            
            	This specifies whether the loopback or interface address is to be used as the transport address in the transport address TLV of the hello message.  If the value is interface(1), then the IP address of the interface from which hello messages are sent is used as the transport address in the hello message.  Otherwise, if the value is loopback(2), then the IP address of the loopback interface is used as the transport address in the hello message
            	**type**\:   :py:class:`Mplsldpentitytransportaddrkind <ydk.models.cisco_ios_xe.MPLS_LDP_STD_MIB.MplsLdpStdMib.Mplsldpentitytable.Mplsldpentityentry.Mplsldpentitytransportaddrkind>`
            
            .. attribute:: mplsldpentityudpdscport
            
            	The UDP Discovery Port for LDP.  The default value is the well\-known value for this port
            	**type**\:  int
            
            	**range:** 0..65535
            
            

            """

            _prefix = 'MPLS-LDP-STD-MIB'
            _revision = '2004-06-03'

            def __init__(self):
                super(MplsLdpStdMib.Mplsldpentitytable.Mplsldpentityentry, self).__init__()

                self.yang_name = "mplsLdpEntityEntry"
                self.yang_parent_name = "mplsLdpEntityTable"

                self.mplsldpentityldpid = YLeaf(YType.str, "mplsLdpEntityLdpId")

                self.mplsldpentityindex = YLeaf(YType.uint32, "mplsLdpEntityIndex")

                self.mplsldpentityadminstatus = YLeaf(YType.enumeration, "mplsLdpEntityAdminStatus")

                self.mplsldpentitydiscontinuitytime = YLeaf(YType.uint32, "mplsLdpEntityDiscontinuityTime")

                self.mplsldpentityhelloholdtimer = YLeaf(YType.uint32, "mplsLdpEntityHelloHoldTimer")

                self.mplsldpentityhopcountlimit = YLeaf(YType.int32, "mplsLdpEntityHopCountLimit")

                self.mplsldpentityinitsessionthreshold = YLeaf(YType.int32, "mplsLdpEntityInitSessionThreshold")

                self.mplsldpentitykeepaliveholdtimer = YLeaf(YType.uint32, "mplsLdpEntityKeepAliveHoldTimer")

                self.mplsldpentitylabeldistmethod = YLeaf(YType.enumeration, "mplsLdpEntityLabelDistMethod")

                self.mplsldpentitylabelretentionmode = YLeaf(YType.enumeration, "mplsLdpEntityLabelRetentionMode")

                self.mplsldpentitylabeltype = YLeaf(YType.enumeration, "mplsLdpEntityLabelType")

                self.mplsldpentitymaxpdulength = YLeaf(YType.uint32, "mplsLdpEntityMaxPduLength")

                self.mplsldpentityoperstatus = YLeaf(YType.enumeration, "mplsLdpEntityOperStatus")

                self.mplsldpentitypathvectorlimit = YLeaf(YType.int32, "mplsLdpEntityPathVectorLimit")

                self.mplsldpentityprotocolversion = YLeaf(YType.uint32, "mplsLdpEntityProtocolVersion")

                self.mplsldpentityrowstatus = YLeaf(YType.enumeration, "mplsLdpEntityRowStatus")

                self.mplsldpentitystatsbadldpidentifiererrors = YLeaf(YType.uint32, "mplsLdpEntityStatsBadLdpIdentifierErrors")

                self.mplsldpentitystatsbadmessagelengtherrors = YLeaf(YType.uint32, "mplsLdpEntityStatsBadMessageLengthErrors")

                self.mplsldpentitystatsbadpdulengtherrors = YLeaf(YType.uint32, "mplsLdpEntityStatsBadPduLengthErrors")

                self.mplsldpentitystatsbadtlvlengtherrors = YLeaf(YType.uint32, "mplsLdpEntityStatsBadTlvLengthErrors")

                self.mplsldpentitystatskeepalivetimerexperrors = YLeaf(YType.uint32, "mplsLdpEntityStatsKeepAliveTimerExpErrors")

                self.mplsldpentitystatsmalformedtlvvalueerrors = YLeaf(YType.uint32, "mplsLdpEntityStatsMalformedTlvValueErrors")

                self.mplsldpentitystatssessionattempts = YLeaf(YType.uint32, "mplsLdpEntityStatsSessionAttempts")

                self.mplsldpentitystatssessionrejectedaderrors = YLeaf(YType.uint32, "mplsLdpEntityStatsSessionRejectedAdErrors")

                self.mplsldpentitystatssessionrejectedlrerrors = YLeaf(YType.uint32, "mplsLdpEntityStatsSessionRejectedLRErrors")

                self.mplsldpentitystatssessionrejectedmaxpduerrors = YLeaf(YType.uint32, "mplsLdpEntityStatsSessionRejectedMaxPduErrors")

                self.mplsldpentitystatssessionrejectednohelloerrors = YLeaf(YType.uint32, "mplsLdpEntityStatsSessionRejectedNoHelloErrors")

                self.mplsldpentitystatsshutdownreceivednotifications = YLeaf(YType.uint32, "mplsLdpEntityStatsShutdownReceivedNotifications")

                self.mplsldpentitystatsshutdownsentnotifications = YLeaf(YType.uint32, "mplsLdpEntityStatsShutdownSentNotifications")

                self.mplsldpentitystoragetype = YLeaf(YType.enumeration, "mplsLdpEntityStorageType")

                self.mplsldpentitytargetpeer = YLeaf(YType.boolean, "mplsLdpEntityTargetPeer")

                self.mplsldpentitytargetpeeraddr = YLeaf(YType.str, "mplsLdpEntityTargetPeerAddr")

                self.mplsldpentitytargetpeeraddrtype = YLeaf(YType.enumeration, "mplsLdpEntityTargetPeerAddrType")

                self.mplsldpentitytcpport = YLeaf(YType.uint16, "mplsLdpEntityTcpPort")

                self.mplsldpentitytransportaddrkind = YLeaf(YType.enumeration, "mplsLdpEntityTransportAddrKind")

                self.mplsldpentityudpdscport = YLeaf(YType.uint16, "mplsLdpEntityUdpDscPort")

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
                                "mplsldpentityadminstatus",
                                "mplsldpentitydiscontinuitytime",
                                "mplsldpentityhelloholdtimer",
                                "mplsldpentityhopcountlimit",
                                "mplsldpentityinitsessionthreshold",
                                "mplsldpentitykeepaliveholdtimer",
                                "mplsldpentitylabeldistmethod",
                                "mplsldpentitylabelretentionmode",
                                "mplsldpentitylabeltype",
                                "mplsldpentitymaxpdulength",
                                "mplsldpentityoperstatus",
                                "mplsldpentitypathvectorlimit",
                                "mplsldpentityprotocolversion",
                                "mplsldpentityrowstatus",
                                "mplsldpentitystatsbadldpidentifiererrors",
                                "mplsldpentitystatsbadmessagelengtherrors",
                                "mplsldpentitystatsbadpdulengtherrors",
                                "mplsldpentitystatsbadtlvlengtherrors",
                                "mplsldpentitystatskeepalivetimerexperrors",
                                "mplsldpentitystatsmalformedtlvvalueerrors",
                                "mplsldpentitystatssessionattempts",
                                "mplsldpentitystatssessionrejectedaderrors",
                                "mplsldpentitystatssessionrejectedlrerrors",
                                "mplsldpentitystatssessionrejectedmaxpduerrors",
                                "mplsldpentitystatssessionrejectednohelloerrors",
                                "mplsldpentitystatsshutdownreceivednotifications",
                                "mplsldpentitystatsshutdownsentnotifications",
                                "mplsldpentitystoragetype",
                                "mplsldpentitytargetpeer",
                                "mplsldpentitytargetpeeraddr",
                                "mplsldpentitytargetpeeraddrtype",
                                "mplsldpentitytcpport",
                                "mplsldpentitytransportaddrkind",
                                "mplsldpentityudpdscport") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(MplsLdpStdMib.Mplsldpentitytable.Mplsldpentityentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(MplsLdpStdMib.Mplsldpentitytable.Mplsldpentityentry, self).__setattr__(name, value)

            class Mplsldpentityadminstatus(Enum):
                """
                Mplsldpentityadminstatus

                The administrative status of this LDP Entity.

                If this object is changed from 'enable' to 'disable'

                and this entity has already attempted to establish

                contact with a Peer, then all contact with that

                Peer is lost and all information from that Peer

                needs to be removed from the MIB. (This implies

                that the network management subsystem should clean

                up any related entry in the mplsLdpPeerTable.  This

                further implies that a 'tear\-down' for that session

                is issued and the session and all information related

                to that session cease to exist).

                At this point the operator is able to change values

                which are related to this entity.

                When the admin status is set back to 'enable', then

                this Entity will attempt to establish a new session

                with the Peer.

                .. data:: enable = 1

                .. data:: disable = 2

                """

                enable = Enum.YLeaf(1, "enable")

                disable = Enum.YLeaf(2, "disable")


            class Mplsldpentityoperstatus(Enum):
                """
                Mplsldpentityoperstatus

                The operational status of this LDP Entity.

                The value of unknown(1) indicates that the

                operational status cannot be determined at

                this time.  The value of unknown should be

                a transient condition before changing

                to enabled(2) or disabled(3).

                .. data:: unknown = 1

                .. data:: enabled = 2

                .. data:: disabled = 3

                """

                unknown = Enum.YLeaf(1, "unknown")

                enabled = Enum.YLeaf(2, "enabled")

                disabled = Enum.YLeaf(3, "disabled")


            class Mplsldpentitytransportaddrkind(Enum):
                """
                Mplsldpentitytransportaddrkind

                This specifies whether the loopback or interface

                address is to be used as the transport address

                in the transport address TLV of the

                hello message.

                If the value is interface(1), then the IP

                address of the interface from which hello

                messages are sent is used as the transport

                address in the hello message.

                Otherwise, if the value is loopback(2), then the IP

                address of the loopback interface is used as the

                transport address in the hello message.

                .. data:: interface = 1

                .. data:: loopback = 2

                """

                interface = Enum.YLeaf(1, "interface")

                loopback = Enum.YLeaf(2, "loopback")


            def has_data(self):
                return (
                    self.mplsldpentityldpid.is_set or
                    self.mplsldpentityindex.is_set or
                    self.mplsldpentityadminstatus.is_set or
                    self.mplsldpentitydiscontinuitytime.is_set or
                    self.mplsldpentityhelloholdtimer.is_set or
                    self.mplsldpentityhopcountlimit.is_set or
                    self.mplsldpentityinitsessionthreshold.is_set or
                    self.mplsldpentitykeepaliveholdtimer.is_set or
                    self.mplsldpentitylabeldistmethod.is_set or
                    self.mplsldpentitylabelretentionmode.is_set or
                    self.mplsldpentitylabeltype.is_set or
                    self.mplsldpentitymaxpdulength.is_set or
                    self.mplsldpentityoperstatus.is_set or
                    self.mplsldpentitypathvectorlimit.is_set or
                    self.mplsldpentityprotocolversion.is_set or
                    self.mplsldpentityrowstatus.is_set or
                    self.mplsldpentitystatsbadldpidentifiererrors.is_set or
                    self.mplsldpentitystatsbadmessagelengtherrors.is_set or
                    self.mplsldpentitystatsbadpdulengtherrors.is_set or
                    self.mplsldpentitystatsbadtlvlengtherrors.is_set or
                    self.mplsldpentitystatskeepalivetimerexperrors.is_set or
                    self.mplsldpentitystatsmalformedtlvvalueerrors.is_set or
                    self.mplsldpentitystatssessionattempts.is_set or
                    self.mplsldpentitystatssessionrejectedaderrors.is_set or
                    self.mplsldpentitystatssessionrejectedlrerrors.is_set or
                    self.mplsldpentitystatssessionrejectedmaxpduerrors.is_set or
                    self.mplsldpentitystatssessionrejectednohelloerrors.is_set or
                    self.mplsldpentitystatsshutdownreceivednotifications.is_set or
                    self.mplsldpentitystatsshutdownsentnotifications.is_set or
                    self.mplsldpentitystoragetype.is_set or
                    self.mplsldpentitytargetpeer.is_set or
                    self.mplsldpentitytargetpeeraddr.is_set or
                    self.mplsldpentitytargetpeeraddrtype.is_set or
                    self.mplsldpentitytcpport.is_set or
                    self.mplsldpentitytransportaddrkind.is_set or
                    self.mplsldpentityudpdscport.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.mplsldpentityldpid.yfilter != YFilter.not_set or
                    self.mplsldpentityindex.yfilter != YFilter.not_set or
                    self.mplsldpentityadminstatus.yfilter != YFilter.not_set or
                    self.mplsldpentitydiscontinuitytime.yfilter != YFilter.not_set or
                    self.mplsldpentityhelloholdtimer.yfilter != YFilter.not_set or
                    self.mplsldpentityhopcountlimit.yfilter != YFilter.not_set or
                    self.mplsldpentityinitsessionthreshold.yfilter != YFilter.not_set or
                    self.mplsldpentitykeepaliveholdtimer.yfilter != YFilter.not_set or
                    self.mplsldpentitylabeldistmethod.yfilter != YFilter.not_set or
                    self.mplsldpentitylabelretentionmode.yfilter != YFilter.not_set or
                    self.mplsldpentitylabeltype.yfilter != YFilter.not_set or
                    self.mplsldpentitymaxpdulength.yfilter != YFilter.not_set or
                    self.mplsldpentityoperstatus.yfilter != YFilter.not_set or
                    self.mplsldpentitypathvectorlimit.yfilter != YFilter.not_set or
                    self.mplsldpentityprotocolversion.yfilter != YFilter.not_set or
                    self.mplsldpentityrowstatus.yfilter != YFilter.not_set or
                    self.mplsldpentitystatsbadldpidentifiererrors.yfilter != YFilter.not_set or
                    self.mplsldpentitystatsbadmessagelengtherrors.yfilter != YFilter.not_set or
                    self.mplsldpentitystatsbadpdulengtherrors.yfilter != YFilter.not_set or
                    self.mplsldpentitystatsbadtlvlengtherrors.yfilter != YFilter.not_set or
                    self.mplsldpentitystatskeepalivetimerexperrors.yfilter != YFilter.not_set or
                    self.mplsldpentitystatsmalformedtlvvalueerrors.yfilter != YFilter.not_set or
                    self.mplsldpentitystatssessionattempts.yfilter != YFilter.not_set or
                    self.mplsldpentitystatssessionrejectedaderrors.yfilter != YFilter.not_set or
                    self.mplsldpentitystatssessionrejectedlrerrors.yfilter != YFilter.not_set or
                    self.mplsldpentitystatssessionrejectedmaxpduerrors.yfilter != YFilter.not_set or
                    self.mplsldpentitystatssessionrejectednohelloerrors.yfilter != YFilter.not_set or
                    self.mplsldpentitystatsshutdownreceivednotifications.yfilter != YFilter.not_set or
                    self.mplsldpentitystatsshutdownsentnotifications.yfilter != YFilter.not_set or
                    self.mplsldpentitystoragetype.yfilter != YFilter.not_set or
                    self.mplsldpentitytargetpeer.yfilter != YFilter.not_set or
                    self.mplsldpentitytargetpeeraddr.yfilter != YFilter.not_set or
                    self.mplsldpentitytargetpeeraddrtype.yfilter != YFilter.not_set or
                    self.mplsldpentitytcpport.yfilter != YFilter.not_set or
                    self.mplsldpentitytransportaddrkind.yfilter != YFilter.not_set or
                    self.mplsldpentityudpdscport.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "mplsLdpEntityEntry" + "[mplsLdpEntityLdpId='" + self.mplsldpentityldpid.get() + "']" + "[mplsLdpEntityIndex='" + self.mplsldpentityindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "MPLS-LDP-STD-MIB:MPLS-LDP-STD-MIB/mplsLdpEntityTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.mplsldpentityldpid.is_set or self.mplsldpentityldpid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsldpentityldpid.get_name_leafdata())
                if (self.mplsldpentityindex.is_set or self.mplsldpentityindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsldpentityindex.get_name_leafdata())
                if (self.mplsldpentityadminstatus.is_set or self.mplsldpentityadminstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsldpentityadminstatus.get_name_leafdata())
                if (self.mplsldpentitydiscontinuitytime.is_set or self.mplsldpentitydiscontinuitytime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsldpentitydiscontinuitytime.get_name_leafdata())
                if (self.mplsldpentityhelloholdtimer.is_set or self.mplsldpentityhelloholdtimer.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsldpentityhelloholdtimer.get_name_leafdata())
                if (self.mplsldpentityhopcountlimit.is_set or self.mplsldpentityhopcountlimit.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsldpentityhopcountlimit.get_name_leafdata())
                if (self.mplsldpentityinitsessionthreshold.is_set or self.mplsldpentityinitsessionthreshold.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsldpentityinitsessionthreshold.get_name_leafdata())
                if (self.mplsldpentitykeepaliveholdtimer.is_set or self.mplsldpentitykeepaliveholdtimer.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsldpentitykeepaliveholdtimer.get_name_leafdata())
                if (self.mplsldpentitylabeldistmethod.is_set or self.mplsldpentitylabeldistmethod.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsldpentitylabeldistmethod.get_name_leafdata())
                if (self.mplsldpentitylabelretentionmode.is_set or self.mplsldpentitylabelretentionmode.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsldpentitylabelretentionmode.get_name_leafdata())
                if (self.mplsldpentitylabeltype.is_set or self.mplsldpentitylabeltype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsldpentitylabeltype.get_name_leafdata())
                if (self.mplsldpentitymaxpdulength.is_set or self.mplsldpentitymaxpdulength.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsldpentitymaxpdulength.get_name_leafdata())
                if (self.mplsldpentityoperstatus.is_set or self.mplsldpentityoperstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsldpentityoperstatus.get_name_leafdata())
                if (self.mplsldpentitypathvectorlimit.is_set or self.mplsldpentitypathvectorlimit.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsldpentitypathvectorlimit.get_name_leafdata())
                if (self.mplsldpentityprotocolversion.is_set or self.mplsldpentityprotocolversion.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsldpentityprotocolversion.get_name_leafdata())
                if (self.mplsldpentityrowstatus.is_set or self.mplsldpentityrowstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsldpentityrowstatus.get_name_leafdata())
                if (self.mplsldpentitystatsbadldpidentifiererrors.is_set or self.mplsldpentitystatsbadldpidentifiererrors.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsldpentitystatsbadldpidentifiererrors.get_name_leafdata())
                if (self.mplsldpentitystatsbadmessagelengtherrors.is_set or self.mplsldpentitystatsbadmessagelengtherrors.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsldpentitystatsbadmessagelengtherrors.get_name_leafdata())
                if (self.mplsldpentitystatsbadpdulengtherrors.is_set or self.mplsldpentitystatsbadpdulengtherrors.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsldpentitystatsbadpdulengtherrors.get_name_leafdata())
                if (self.mplsldpentitystatsbadtlvlengtherrors.is_set or self.mplsldpentitystatsbadtlvlengtherrors.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsldpentitystatsbadtlvlengtherrors.get_name_leafdata())
                if (self.mplsldpentitystatskeepalivetimerexperrors.is_set or self.mplsldpentitystatskeepalivetimerexperrors.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsldpentitystatskeepalivetimerexperrors.get_name_leafdata())
                if (self.mplsldpentitystatsmalformedtlvvalueerrors.is_set or self.mplsldpentitystatsmalformedtlvvalueerrors.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsldpentitystatsmalformedtlvvalueerrors.get_name_leafdata())
                if (self.mplsldpentitystatssessionattempts.is_set or self.mplsldpentitystatssessionattempts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsldpentitystatssessionattempts.get_name_leafdata())
                if (self.mplsldpentitystatssessionrejectedaderrors.is_set or self.mplsldpentitystatssessionrejectedaderrors.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsldpentitystatssessionrejectedaderrors.get_name_leafdata())
                if (self.mplsldpentitystatssessionrejectedlrerrors.is_set or self.mplsldpentitystatssessionrejectedlrerrors.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsldpentitystatssessionrejectedlrerrors.get_name_leafdata())
                if (self.mplsldpentitystatssessionrejectedmaxpduerrors.is_set or self.mplsldpentitystatssessionrejectedmaxpduerrors.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsldpentitystatssessionrejectedmaxpduerrors.get_name_leafdata())
                if (self.mplsldpentitystatssessionrejectednohelloerrors.is_set or self.mplsldpentitystatssessionrejectednohelloerrors.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsldpentitystatssessionrejectednohelloerrors.get_name_leafdata())
                if (self.mplsldpentitystatsshutdownreceivednotifications.is_set or self.mplsldpentitystatsshutdownreceivednotifications.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsldpentitystatsshutdownreceivednotifications.get_name_leafdata())
                if (self.mplsldpentitystatsshutdownsentnotifications.is_set or self.mplsldpentitystatsshutdownsentnotifications.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsldpentitystatsshutdownsentnotifications.get_name_leafdata())
                if (self.mplsldpentitystoragetype.is_set or self.mplsldpentitystoragetype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsldpentitystoragetype.get_name_leafdata())
                if (self.mplsldpentitytargetpeer.is_set or self.mplsldpentitytargetpeer.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsldpentitytargetpeer.get_name_leafdata())
                if (self.mplsldpentitytargetpeeraddr.is_set or self.mplsldpentitytargetpeeraddr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsldpentitytargetpeeraddr.get_name_leafdata())
                if (self.mplsldpentitytargetpeeraddrtype.is_set or self.mplsldpentitytargetpeeraddrtype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsldpentitytargetpeeraddrtype.get_name_leafdata())
                if (self.mplsldpentitytcpport.is_set or self.mplsldpentitytcpport.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsldpentitytcpport.get_name_leafdata())
                if (self.mplsldpentitytransportaddrkind.is_set or self.mplsldpentitytransportaddrkind.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsldpentitytransportaddrkind.get_name_leafdata())
                if (self.mplsldpentityudpdscport.is_set or self.mplsldpentityudpdscport.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsldpentityudpdscport.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "mplsLdpEntityLdpId" or name == "mplsLdpEntityIndex" or name == "mplsLdpEntityAdminStatus" or name == "mplsLdpEntityDiscontinuityTime" or name == "mplsLdpEntityHelloHoldTimer" or name == "mplsLdpEntityHopCountLimit" or name == "mplsLdpEntityInitSessionThreshold" or name == "mplsLdpEntityKeepAliveHoldTimer" or name == "mplsLdpEntityLabelDistMethod" or name == "mplsLdpEntityLabelRetentionMode" or name == "mplsLdpEntityLabelType" or name == "mplsLdpEntityMaxPduLength" or name == "mplsLdpEntityOperStatus" or name == "mplsLdpEntityPathVectorLimit" or name == "mplsLdpEntityProtocolVersion" or name == "mplsLdpEntityRowStatus" or name == "mplsLdpEntityStatsBadLdpIdentifierErrors" or name == "mplsLdpEntityStatsBadMessageLengthErrors" or name == "mplsLdpEntityStatsBadPduLengthErrors" or name == "mplsLdpEntityStatsBadTlvLengthErrors" or name == "mplsLdpEntityStatsKeepAliveTimerExpErrors" or name == "mplsLdpEntityStatsMalformedTlvValueErrors" or name == "mplsLdpEntityStatsSessionAttempts" or name == "mplsLdpEntityStatsSessionRejectedAdErrors" or name == "mplsLdpEntityStatsSessionRejectedLRErrors" or name == "mplsLdpEntityStatsSessionRejectedMaxPduErrors" or name == "mplsLdpEntityStatsSessionRejectedNoHelloErrors" or name == "mplsLdpEntityStatsShutdownReceivedNotifications" or name == "mplsLdpEntityStatsShutdownSentNotifications" or name == "mplsLdpEntityStorageType" or name == "mplsLdpEntityTargetPeer" or name == "mplsLdpEntityTargetPeerAddr" or name == "mplsLdpEntityTargetPeerAddrType" or name == "mplsLdpEntityTcpPort" or name == "mplsLdpEntityTransportAddrKind" or name == "mplsLdpEntityUdpDscPort"):
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
                if(value_path == "mplsLdpEntityAdminStatus"):
                    self.mplsldpentityadminstatus = value
                    self.mplsldpentityadminstatus.value_namespace = name_space
                    self.mplsldpentityadminstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsLdpEntityDiscontinuityTime"):
                    self.mplsldpentitydiscontinuitytime = value
                    self.mplsldpentitydiscontinuitytime.value_namespace = name_space
                    self.mplsldpentitydiscontinuitytime.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsLdpEntityHelloHoldTimer"):
                    self.mplsldpentityhelloholdtimer = value
                    self.mplsldpentityhelloholdtimer.value_namespace = name_space
                    self.mplsldpentityhelloholdtimer.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsLdpEntityHopCountLimit"):
                    self.mplsldpentityhopcountlimit = value
                    self.mplsldpentityhopcountlimit.value_namespace = name_space
                    self.mplsldpentityhopcountlimit.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsLdpEntityInitSessionThreshold"):
                    self.mplsldpentityinitsessionthreshold = value
                    self.mplsldpentityinitsessionthreshold.value_namespace = name_space
                    self.mplsldpentityinitsessionthreshold.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsLdpEntityKeepAliveHoldTimer"):
                    self.mplsldpentitykeepaliveholdtimer = value
                    self.mplsldpentitykeepaliveholdtimer.value_namespace = name_space
                    self.mplsldpentitykeepaliveholdtimer.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsLdpEntityLabelDistMethod"):
                    self.mplsldpentitylabeldistmethod = value
                    self.mplsldpentitylabeldistmethod.value_namespace = name_space
                    self.mplsldpentitylabeldistmethod.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsLdpEntityLabelRetentionMode"):
                    self.mplsldpentitylabelretentionmode = value
                    self.mplsldpentitylabelretentionmode.value_namespace = name_space
                    self.mplsldpentitylabelretentionmode.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsLdpEntityLabelType"):
                    self.mplsldpentitylabeltype = value
                    self.mplsldpentitylabeltype.value_namespace = name_space
                    self.mplsldpentitylabeltype.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsLdpEntityMaxPduLength"):
                    self.mplsldpentitymaxpdulength = value
                    self.mplsldpentitymaxpdulength.value_namespace = name_space
                    self.mplsldpentitymaxpdulength.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsLdpEntityOperStatus"):
                    self.mplsldpentityoperstatus = value
                    self.mplsldpentityoperstatus.value_namespace = name_space
                    self.mplsldpentityoperstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsLdpEntityPathVectorLimit"):
                    self.mplsldpentitypathvectorlimit = value
                    self.mplsldpentitypathvectorlimit.value_namespace = name_space
                    self.mplsldpentitypathvectorlimit.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsLdpEntityProtocolVersion"):
                    self.mplsldpentityprotocolversion = value
                    self.mplsldpentityprotocolversion.value_namespace = name_space
                    self.mplsldpentityprotocolversion.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsLdpEntityRowStatus"):
                    self.mplsldpentityrowstatus = value
                    self.mplsldpentityrowstatus.value_namespace = name_space
                    self.mplsldpentityrowstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsLdpEntityStatsBadLdpIdentifierErrors"):
                    self.mplsldpentitystatsbadldpidentifiererrors = value
                    self.mplsldpentitystatsbadldpidentifiererrors.value_namespace = name_space
                    self.mplsldpentitystatsbadldpidentifiererrors.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsLdpEntityStatsBadMessageLengthErrors"):
                    self.mplsldpentitystatsbadmessagelengtherrors = value
                    self.mplsldpentitystatsbadmessagelengtherrors.value_namespace = name_space
                    self.mplsldpentitystatsbadmessagelengtherrors.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsLdpEntityStatsBadPduLengthErrors"):
                    self.mplsldpentitystatsbadpdulengtherrors = value
                    self.mplsldpentitystatsbadpdulengtherrors.value_namespace = name_space
                    self.mplsldpentitystatsbadpdulengtherrors.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsLdpEntityStatsBadTlvLengthErrors"):
                    self.mplsldpentitystatsbadtlvlengtherrors = value
                    self.mplsldpentitystatsbadtlvlengtherrors.value_namespace = name_space
                    self.mplsldpentitystatsbadtlvlengtherrors.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsLdpEntityStatsKeepAliveTimerExpErrors"):
                    self.mplsldpentitystatskeepalivetimerexperrors = value
                    self.mplsldpentitystatskeepalivetimerexperrors.value_namespace = name_space
                    self.mplsldpentitystatskeepalivetimerexperrors.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsLdpEntityStatsMalformedTlvValueErrors"):
                    self.mplsldpentitystatsmalformedtlvvalueerrors = value
                    self.mplsldpentitystatsmalformedtlvvalueerrors.value_namespace = name_space
                    self.mplsldpentitystatsmalformedtlvvalueerrors.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsLdpEntityStatsSessionAttempts"):
                    self.mplsldpentitystatssessionattempts = value
                    self.mplsldpentitystatssessionattempts.value_namespace = name_space
                    self.mplsldpentitystatssessionattempts.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsLdpEntityStatsSessionRejectedAdErrors"):
                    self.mplsldpentitystatssessionrejectedaderrors = value
                    self.mplsldpentitystatssessionrejectedaderrors.value_namespace = name_space
                    self.mplsldpentitystatssessionrejectedaderrors.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsLdpEntityStatsSessionRejectedLRErrors"):
                    self.mplsldpentitystatssessionrejectedlrerrors = value
                    self.mplsldpentitystatssessionrejectedlrerrors.value_namespace = name_space
                    self.mplsldpentitystatssessionrejectedlrerrors.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsLdpEntityStatsSessionRejectedMaxPduErrors"):
                    self.mplsldpentitystatssessionrejectedmaxpduerrors = value
                    self.mplsldpentitystatssessionrejectedmaxpduerrors.value_namespace = name_space
                    self.mplsldpentitystatssessionrejectedmaxpduerrors.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsLdpEntityStatsSessionRejectedNoHelloErrors"):
                    self.mplsldpentitystatssessionrejectednohelloerrors = value
                    self.mplsldpentitystatssessionrejectednohelloerrors.value_namespace = name_space
                    self.mplsldpentitystatssessionrejectednohelloerrors.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsLdpEntityStatsShutdownReceivedNotifications"):
                    self.mplsldpentitystatsshutdownreceivednotifications = value
                    self.mplsldpentitystatsshutdownreceivednotifications.value_namespace = name_space
                    self.mplsldpentitystatsshutdownreceivednotifications.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsLdpEntityStatsShutdownSentNotifications"):
                    self.mplsldpentitystatsshutdownsentnotifications = value
                    self.mplsldpentitystatsshutdownsentnotifications.value_namespace = name_space
                    self.mplsldpentitystatsshutdownsentnotifications.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsLdpEntityStorageType"):
                    self.mplsldpentitystoragetype = value
                    self.mplsldpentitystoragetype.value_namespace = name_space
                    self.mplsldpentitystoragetype.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsLdpEntityTargetPeer"):
                    self.mplsldpentitytargetpeer = value
                    self.mplsldpentitytargetpeer.value_namespace = name_space
                    self.mplsldpentitytargetpeer.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsLdpEntityTargetPeerAddr"):
                    self.mplsldpentitytargetpeeraddr = value
                    self.mplsldpentitytargetpeeraddr.value_namespace = name_space
                    self.mplsldpentitytargetpeeraddr.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsLdpEntityTargetPeerAddrType"):
                    self.mplsldpentitytargetpeeraddrtype = value
                    self.mplsldpentitytargetpeeraddrtype.value_namespace = name_space
                    self.mplsldpentitytargetpeeraddrtype.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsLdpEntityTcpPort"):
                    self.mplsldpentitytcpport = value
                    self.mplsldpentitytcpport.value_namespace = name_space
                    self.mplsldpentitytcpport.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsLdpEntityTransportAddrKind"):
                    self.mplsldpentitytransportaddrkind = value
                    self.mplsldpentitytransportaddrkind.value_namespace = name_space
                    self.mplsldpentitytransportaddrkind.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsLdpEntityUdpDscPort"):
                    self.mplsldpentityudpdscport = value
                    self.mplsldpentityudpdscport.value_namespace = name_space
                    self.mplsldpentityudpdscport.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.mplsldpentityentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.mplsldpentityentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "mplsLdpEntityTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "MPLS-LDP-STD-MIB:MPLS-LDP-STD-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "mplsLdpEntityEntry"):
                for c in self.mplsldpentityentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = MplsLdpStdMib.Mplsldpentitytable.Mplsldpentityentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.mplsldpentityentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "mplsLdpEntityEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Mplsldppeertable(Entity):
        """
        Information about LDP peers known by Entities in
        the mplsLdpEntityTable.  The information in this table
        is based on information from the Entity\-Peer interaction
        during session initialization but is not appropriate
        for the mplsLdpSessionTable, because objects in this
        table may or may not be used in session establishment.
        
        .. attribute:: mplsldppeerentry
        
        	Information about a single Peer which is related to a Session.  This table is augmented by the mplsLdpSessionTable
        	**type**\: list of    :py:class:`Mplsldppeerentry <ydk.models.cisco_ios_xe.MPLS_LDP_STD_MIB.MplsLdpStdMib.Mplsldppeertable.Mplsldppeerentry>`
        
        

        """

        _prefix = 'MPLS-LDP-STD-MIB'
        _revision = '2004-06-03'

        def __init__(self):
            super(MplsLdpStdMib.Mplsldppeertable, self).__init__()

            self.yang_name = "mplsLdpPeerTable"
            self.yang_parent_name = "MPLS-LDP-STD-MIB"

            self.mplsldppeerentry = YList(self)

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
                        super(MplsLdpStdMib.Mplsldppeertable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(MplsLdpStdMib.Mplsldppeertable, self).__setattr__(name, value)


        class Mplsldppeerentry(Entity):
            """
            Information about a single Peer which is related
            to a Session.  This table is augmented by
            the mplsLdpSessionTable.
            
            .. attribute:: mplsldpentityldpid  <key>
            
            	
            	**type**\:  str
            
            	**refers to**\:  :py:class:`mplsldpentityldpid <ydk.models.cisco_ios_xe.MPLS_LDP_STD_MIB.MplsLdpStdMib.Mplsldpentitytable.Mplsldpentityentry>`
            
            .. attribute:: mplsldpentityindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            	**refers to**\:  :py:class:`mplsldpentityindex <ydk.models.cisco_ios_xe.MPLS_LDP_STD_MIB.MplsLdpStdMib.Mplsldpentitytable.Mplsldpentityentry>`
            
            .. attribute:: mplsldppeerldpid  <key>
            
            	The LDP identifier of this LDP Peer
            	**type**\:  str
            
            .. attribute:: mplsldppeerlabeldistmethod
            
            	For any given LDP session, the method of label distribution must be specified
            	**type**\:   :py:class:`Mplslabeldistributionmethod <ydk.models.cisco_ios_xe.MPLS_TC_STD_MIB.Mplslabeldistributionmethod>`
            
            .. attribute:: mplsldppeerpathvectorlimit
            
            	If the value of this object is 0 (zero) then Loop Dection for Path Vectors for this Peer is disabled.  Otherwise, if this object has a value greater than zero, then Loop Dection for Path  Vectors for this Peer is enabled and the Path Vector Limit is this value
            	**type**\:  int
            
            	**range:** 0..255
            
            .. attribute:: mplsldppeertransportaddr
            
            	The Internet address advertised by the peer in the Hello Message or the Hello source address.  The type of this address is specified by the value of the mplsLdpPeerTransportAddrType object
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: mplsldppeertransportaddrtype
            
            	The type of the Internet address for the mplsLdpPeerTransportAddr object.  The LDP specification describes this as being either an IPv4 Transport Address or IPv6 Transport   Address which is used in opening the LDP session's TCP connection, or if the optional TLV is not present, then this is the IPv4/IPv6 source address for the UPD packet carrying the Hellos.  This object specifies how the value of the mplsLdpPeerTransportAddr object should be interpreted
            	**type**\:   :py:class:`Inetaddresstype <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.Inetaddresstype>`
            
            .. attribute:: mplsldpsessiondiscontinuitytime
            
            	The value of sysUpTime on the most recent occasion at which any one or more of this session's counters suffered a discontinuity.  The relevant counters are the specific instances associated with this session of any Counter32 object contained in the mplsLdpSessionStatsTable.  The initial value of this object is the value of sysUpTime when the entry was created in this table.  Also, a command generator can distinguish when a session between a given Entity and Peer goes away and a new session is established.  This value would change and thus indicate to the command generator that this is a different session
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplsldpsessionkeepaliveholdtimerem
            
            	The keep alive hold time remaining for this session
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: mplsldpsessionkeepalivetime
            
            	The negotiated KeepAlive Time which represents the amount of seconds between keep alive messages.  The mplsLdpEntityKeepAliveHoldTimer related to this Session is the value that was proposed as the KeepAlive Time for this session.  This value is negotiated during session initialization between the entity's proposed value (i.e., the value configured in mplsLdpEntityKeepAliveHoldTimer) and the peer's proposed KeepAlive Hold Timer value. This value is the smaller of the two proposed values
            	**type**\:  int
            
            	**range:** 1..65535
            
            	**units**\: seconds
            
            .. attribute:: mplsldpsessionmaxpdulength
            
            	The value of maximum allowable length for LDP PDUs for this session.  This value may have been negotiated during the Session Initialization.  This object is related to the mplsLdpEntityMaxPduLength object.  The mplsLdpEntityMaxPduLength object specifies the requested LDP PDU length, and this object reflects the negotiated LDP PDU length between the Entity and the Peer
            	**type**\:  int
            
            	**range:** 1..65535
            
            	**units**\: octets
            
            .. attribute:: mplsldpsessionprotocolversion
            
            	The version of the LDP Protocol which this session is using.  This is the version of   the LDP protocol which has been negotiated during session initialization
            	**type**\:  int
            
            	**range:** 1..65535
            
            .. attribute:: mplsldpsessionrole
            
            	During session establishment the LSR/LER takes either the active role or the passive role based on address comparisons.  This object indicates whether this LSR/LER was behaving in an active role or passive role during this session's establishment.  The value of unknown(1), indicates that the role is not able to be determined at the present time
            	**type**\:   :py:class:`Mplsldpsessionrole <ydk.models.cisco_ios_xe.MPLS_LDP_STD_MIB.MplsLdpStdMib.Mplsldppeertable.Mplsldppeerentry.Mplsldpsessionrole>`
            
            .. attribute:: mplsldpsessionstate
            
            	The current state of the session, all of the states 1 to 5 are based on the state machine for session negotiation behavior
            	**type**\:   :py:class:`Mplsldpsessionstate <ydk.models.cisco_ios_xe.MPLS_LDP_STD_MIB.MplsLdpStdMib.Mplsldppeertable.Mplsldppeerentry.Mplsldpsessionstate>`
            
            .. attribute:: mplsldpsessionstatelastchange
            
            	The value of sysUpTime at the time this Session entered its current state as denoted by the mplsLdpSessionState object
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplsldpsessionstatsunknownmestypeerrors
            
            	This object counts the number of Unknown Message Type Errors detected by this LSR/LER during this session.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of mplsLdpSessionDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplsldpsessionstatsunknowntlverrors
            
            	This object counts the number of Unknown TLV Errors detected by this LSR/LER during this session.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of mplsLdpSessionDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'MPLS-LDP-STD-MIB'
            _revision = '2004-06-03'

            def __init__(self):
                super(MplsLdpStdMib.Mplsldppeertable.Mplsldppeerentry, self).__init__()

                self.yang_name = "mplsLdpPeerEntry"
                self.yang_parent_name = "mplsLdpPeerTable"

                self.mplsldpentityldpid = YLeaf(YType.str, "mplsLdpEntityLdpId")

                self.mplsldpentityindex = YLeaf(YType.str, "mplsLdpEntityIndex")

                self.mplsldppeerldpid = YLeaf(YType.str, "mplsLdpPeerLdpId")

                self.mplsldppeerlabeldistmethod = YLeaf(YType.enumeration, "mplsLdpPeerLabelDistMethod")

                self.mplsldppeerpathvectorlimit = YLeaf(YType.int32, "mplsLdpPeerPathVectorLimit")

                self.mplsldppeertransportaddr = YLeaf(YType.str, "mplsLdpPeerTransportAddr")

                self.mplsldppeertransportaddrtype = YLeaf(YType.enumeration, "mplsLdpPeerTransportAddrType")

                self.mplsldpsessiondiscontinuitytime = YLeaf(YType.uint32, "mplsLdpSessionDiscontinuityTime")

                self.mplsldpsessionkeepaliveholdtimerem = YLeaf(YType.int32, "mplsLdpSessionKeepAliveHoldTimeRem")

                self.mplsldpsessionkeepalivetime = YLeaf(YType.uint32, "mplsLdpSessionKeepAliveTime")

                self.mplsldpsessionmaxpdulength = YLeaf(YType.uint32, "mplsLdpSessionMaxPduLength")

                self.mplsldpsessionprotocolversion = YLeaf(YType.uint32, "mplsLdpSessionProtocolVersion")

                self.mplsldpsessionrole = YLeaf(YType.enumeration, "mplsLdpSessionRole")

                self.mplsldpsessionstate = YLeaf(YType.enumeration, "mplsLdpSessionState")

                self.mplsldpsessionstatelastchange = YLeaf(YType.uint32, "mplsLdpSessionStateLastChange")

                self.mplsldpsessionstatsunknownmestypeerrors = YLeaf(YType.uint32, "mplsLdpSessionStatsUnknownMesTypeErrors")

                self.mplsldpsessionstatsunknowntlverrors = YLeaf(YType.uint32, "mplsLdpSessionStatsUnknownTlvErrors")

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
                                "mplsldppeerldpid",
                                "mplsldppeerlabeldistmethod",
                                "mplsldppeerpathvectorlimit",
                                "mplsldppeertransportaddr",
                                "mplsldppeertransportaddrtype",
                                "mplsldpsessiondiscontinuitytime",
                                "mplsldpsessionkeepaliveholdtimerem",
                                "mplsldpsessionkeepalivetime",
                                "mplsldpsessionmaxpdulength",
                                "mplsldpsessionprotocolversion",
                                "mplsldpsessionrole",
                                "mplsldpsessionstate",
                                "mplsldpsessionstatelastchange",
                                "mplsldpsessionstatsunknownmestypeerrors",
                                "mplsldpsessionstatsunknowntlverrors") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(MplsLdpStdMib.Mplsldppeertable.Mplsldppeerentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(MplsLdpStdMib.Mplsldppeertable.Mplsldppeerentry, self).__setattr__(name, value)

            class Mplsldpsessionrole(Enum):
                """
                Mplsldpsessionrole

                During session establishment the LSR/LER takes either

                the active role or the passive role based on address

                comparisons.  This object indicates whether this LSR/LER

                was behaving in an active role or passive role during

                this session's establishment.

                The value of unknown(1), indicates that the role is not

                able to be determined at the present time.

                .. data:: unknown = 1

                .. data:: active = 2

                .. data:: passive = 3

                """

                unknown = Enum.YLeaf(1, "unknown")

                active = Enum.YLeaf(2, "active")

                passive = Enum.YLeaf(3, "passive")


            class Mplsldpsessionstate(Enum):
                """
                Mplsldpsessionstate

                The current state of the session, all of the

                states 1 to 5 are based on the state machine

                for session negotiation behavior.

                .. data:: nonexistent = 1

                .. data:: initialized = 2

                .. data:: openrec = 3

                .. data:: opensent = 4

                .. data:: operational = 5

                """

                nonexistent = Enum.YLeaf(1, "nonexistent")

                initialized = Enum.YLeaf(2, "initialized")

                openrec = Enum.YLeaf(3, "openrec")

                opensent = Enum.YLeaf(4, "opensent")

                operational = Enum.YLeaf(5, "operational")


            def has_data(self):
                return (
                    self.mplsldpentityldpid.is_set or
                    self.mplsldpentityindex.is_set or
                    self.mplsldppeerldpid.is_set or
                    self.mplsldppeerlabeldistmethod.is_set or
                    self.mplsldppeerpathvectorlimit.is_set or
                    self.mplsldppeertransportaddr.is_set or
                    self.mplsldppeertransportaddrtype.is_set or
                    self.mplsldpsessiondiscontinuitytime.is_set or
                    self.mplsldpsessionkeepaliveholdtimerem.is_set or
                    self.mplsldpsessionkeepalivetime.is_set or
                    self.mplsldpsessionmaxpdulength.is_set or
                    self.mplsldpsessionprotocolversion.is_set or
                    self.mplsldpsessionrole.is_set or
                    self.mplsldpsessionstate.is_set or
                    self.mplsldpsessionstatelastchange.is_set or
                    self.mplsldpsessionstatsunknownmestypeerrors.is_set or
                    self.mplsldpsessionstatsunknowntlverrors.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.mplsldpentityldpid.yfilter != YFilter.not_set or
                    self.mplsldpentityindex.yfilter != YFilter.not_set or
                    self.mplsldppeerldpid.yfilter != YFilter.not_set or
                    self.mplsldppeerlabeldistmethod.yfilter != YFilter.not_set or
                    self.mplsldppeerpathvectorlimit.yfilter != YFilter.not_set or
                    self.mplsldppeertransportaddr.yfilter != YFilter.not_set or
                    self.mplsldppeertransportaddrtype.yfilter != YFilter.not_set or
                    self.mplsldpsessiondiscontinuitytime.yfilter != YFilter.not_set or
                    self.mplsldpsessionkeepaliveholdtimerem.yfilter != YFilter.not_set or
                    self.mplsldpsessionkeepalivetime.yfilter != YFilter.not_set or
                    self.mplsldpsessionmaxpdulength.yfilter != YFilter.not_set or
                    self.mplsldpsessionprotocolversion.yfilter != YFilter.not_set or
                    self.mplsldpsessionrole.yfilter != YFilter.not_set or
                    self.mplsldpsessionstate.yfilter != YFilter.not_set or
                    self.mplsldpsessionstatelastchange.yfilter != YFilter.not_set or
                    self.mplsldpsessionstatsunknownmestypeerrors.yfilter != YFilter.not_set or
                    self.mplsldpsessionstatsunknowntlverrors.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "mplsLdpPeerEntry" + "[mplsLdpEntityLdpId='" + self.mplsldpentityldpid.get() + "']" + "[mplsLdpEntityIndex='" + self.mplsldpentityindex.get() + "']" + "[mplsLdpPeerLdpId='" + self.mplsldppeerldpid.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "MPLS-LDP-STD-MIB:MPLS-LDP-STD-MIB/mplsLdpPeerTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.mplsldpentityldpid.is_set or self.mplsldpentityldpid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsldpentityldpid.get_name_leafdata())
                if (self.mplsldpentityindex.is_set or self.mplsldpentityindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsldpentityindex.get_name_leafdata())
                if (self.mplsldppeerldpid.is_set or self.mplsldppeerldpid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsldppeerldpid.get_name_leafdata())
                if (self.mplsldppeerlabeldistmethod.is_set or self.mplsldppeerlabeldistmethod.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsldppeerlabeldistmethod.get_name_leafdata())
                if (self.mplsldppeerpathvectorlimit.is_set or self.mplsldppeerpathvectorlimit.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsldppeerpathvectorlimit.get_name_leafdata())
                if (self.mplsldppeertransportaddr.is_set or self.mplsldppeertransportaddr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsldppeertransportaddr.get_name_leafdata())
                if (self.mplsldppeertransportaddrtype.is_set or self.mplsldppeertransportaddrtype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsldppeertransportaddrtype.get_name_leafdata())
                if (self.mplsldpsessiondiscontinuitytime.is_set or self.mplsldpsessiondiscontinuitytime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsldpsessiondiscontinuitytime.get_name_leafdata())
                if (self.mplsldpsessionkeepaliveholdtimerem.is_set or self.mplsldpsessionkeepaliveholdtimerem.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsldpsessionkeepaliveholdtimerem.get_name_leafdata())
                if (self.mplsldpsessionkeepalivetime.is_set or self.mplsldpsessionkeepalivetime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsldpsessionkeepalivetime.get_name_leafdata())
                if (self.mplsldpsessionmaxpdulength.is_set or self.mplsldpsessionmaxpdulength.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsldpsessionmaxpdulength.get_name_leafdata())
                if (self.mplsldpsessionprotocolversion.is_set or self.mplsldpsessionprotocolversion.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsldpsessionprotocolversion.get_name_leafdata())
                if (self.mplsldpsessionrole.is_set or self.mplsldpsessionrole.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsldpsessionrole.get_name_leafdata())
                if (self.mplsldpsessionstate.is_set or self.mplsldpsessionstate.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsldpsessionstate.get_name_leafdata())
                if (self.mplsldpsessionstatelastchange.is_set or self.mplsldpsessionstatelastchange.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsldpsessionstatelastchange.get_name_leafdata())
                if (self.mplsldpsessionstatsunknownmestypeerrors.is_set or self.mplsldpsessionstatsunknownmestypeerrors.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsldpsessionstatsunknownmestypeerrors.get_name_leafdata())
                if (self.mplsldpsessionstatsunknowntlverrors.is_set or self.mplsldpsessionstatsunknowntlverrors.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsldpsessionstatsunknowntlverrors.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "mplsLdpEntityLdpId" or name == "mplsLdpEntityIndex" or name == "mplsLdpPeerLdpId" or name == "mplsLdpPeerLabelDistMethod" or name == "mplsLdpPeerPathVectorLimit" or name == "mplsLdpPeerTransportAddr" or name == "mplsLdpPeerTransportAddrType" or name == "mplsLdpSessionDiscontinuityTime" or name == "mplsLdpSessionKeepAliveHoldTimeRem" or name == "mplsLdpSessionKeepAliveTime" or name == "mplsLdpSessionMaxPduLength" or name == "mplsLdpSessionProtocolVersion" or name == "mplsLdpSessionRole" or name == "mplsLdpSessionState" or name == "mplsLdpSessionStateLastChange" or name == "mplsLdpSessionStatsUnknownMesTypeErrors" or name == "mplsLdpSessionStatsUnknownTlvErrors"):
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
                if(value_path == "mplsLdpPeerLdpId"):
                    self.mplsldppeerldpid = value
                    self.mplsldppeerldpid.value_namespace = name_space
                    self.mplsldppeerldpid.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsLdpPeerLabelDistMethod"):
                    self.mplsldppeerlabeldistmethod = value
                    self.mplsldppeerlabeldistmethod.value_namespace = name_space
                    self.mplsldppeerlabeldistmethod.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsLdpPeerPathVectorLimit"):
                    self.mplsldppeerpathvectorlimit = value
                    self.mplsldppeerpathvectorlimit.value_namespace = name_space
                    self.mplsldppeerpathvectorlimit.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsLdpPeerTransportAddr"):
                    self.mplsldppeertransportaddr = value
                    self.mplsldppeertransportaddr.value_namespace = name_space
                    self.mplsldppeertransportaddr.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsLdpPeerTransportAddrType"):
                    self.mplsldppeertransportaddrtype = value
                    self.mplsldppeertransportaddrtype.value_namespace = name_space
                    self.mplsldppeertransportaddrtype.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsLdpSessionDiscontinuityTime"):
                    self.mplsldpsessiondiscontinuitytime = value
                    self.mplsldpsessiondiscontinuitytime.value_namespace = name_space
                    self.mplsldpsessiondiscontinuitytime.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsLdpSessionKeepAliveHoldTimeRem"):
                    self.mplsldpsessionkeepaliveholdtimerem = value
                    self.mplsldpsessionkeepaliveholdtimerem.value_namespace = name_space
                    self.mplsldpsessionkeepaliveholdtimerem.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsLdpSessionKeepAliveTime"):
                    self.mplsldpsessionkeepalivetime = value
                    self.mplsldpsessionkeepalivetime.value_namespace = name_space
                    self.mplsldpsessionkeepalivetime.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsLdpSessionMaxPduLength"):
                    self.mplsldpsessionmaxpdulength = value
                    self.mplsldpsessionmaxpdulength.value_namespace = name_space
                    self.mplsldpsessionmaxpdulength.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsLdpSessionProtocolVersion"):
                    self.mplsldpsessionprotocolversion = value
                    self.mplsldpsessionprotocolversion.value_namespace = name_space
                    self.mplsldpsessionprotocolversion.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsLdpSessionRole"):
                    self.mplsldpsessionrole = value
                    self.mplsldpsessionrole.value_namespace = name_space
                    self.mplsldpsessionrole.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsLdpSessionState"):
                    self.mplsldpsessionstate = value
                    self.mplsldpsessionstate.value_namespace = name_space
                    self.mplsldpsessionstate.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsLdpSessionStateLastChange"):
                    self.mplsldpsessionstatelastchange = value
                    self.mplsldpsessionstatelastchange.value_namespace = name_space
                    self.mplsldpsessionstatelastchange.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsLdpSessionStatsUnknownMesTypeErrors"):
                    self.mplsldpsessionstatsunknownmestypeerrors = value
                    self.mplsldpsessionstatsunknownmestypeerrors.value_namespace = name_space
                    self.mplsldpsessionstatsunknownmestypeerrors.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsLdpSessionStatsUnknownTlvErrors"):
                    self.mplsldpsessionstatsunknowntlverrors = value
                    self.mplsldpsessionstatsunknowntlverrors.value_namespace = name_space
                    self.mplsldpsessionstatsunknowntlverrors.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.mplsldppeerentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.mplsldppeerentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "mplsLdpPeerTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "MPLS-LDP-STD-MIB:MPLS-LDP-STD-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "mplsLdpPeerEntry"):
                for c in self.mplsldppeerentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = MplsLdpStdMib.Mplsldppeertable.Mplsldppeerentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.mplsldppeerentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "mplsLdpPeerEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Mplsldphelloadjacencytable(Entity):
        """
        A table of Hello Adjacencies for Sessions.
        
        .. attribute:: mplsldphelloadjacencyentry
        
        	Each row represents a single LDP Hello Adjacency. An LDP Session can have one or more Hello Adjacencies
        	**type**\: list of    :py:class:`Mplsldphelloadjacencyentry <ydk.models.cisco_ios_xe.MPLS_LDP_STD_MIB.MplsLdpStdMib.Mplsldphelloadjacencytable.Mplsldphelloadjacencyentry>`
        
        

        """

        _prefix = 'MPLS-LDP-STD-MIB'
        _revision = '2004-06-03'

        def __init__(self):
            super(MplsLdpStdMib.Mplsldphelloadjacencytable, self).__init__()

            self.yang_name = "mplsLdpHelloAdjacencyTable"
            self.yang_parent_name = "MPLS-LDP-STD-MIB"

            self.mplsldphelloadjacencyentry = YList(self)

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
                        super(MplsLdpStdMib.Mplsldphelloadjacencytable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(MplsLdpStdMib.Mplsldphelloadjacencytable, self).__setattr__(name, value)


        class Mplsldphelloadjacencyentry(Entity):
            """
            Each row represents a single LDP Hello Adjacency.
            An LDP Session can have one or more Hello
            Adjacencies.
            
            .. attribute:: mplsldpentityldpid  <key>
            
            	
            	**type**\:  str
            
            	**refers to**\:  :py:class:`mplsldpentityldpid <ydk.models.cisco_ios_xe.MPLS_LDP_STD_MIB.MplsLdpStdMib.Mplsldpentitytable.Mplsldpentityentry>`
            
            .. attribute:: mplsldpentityindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            	**refers to**\:  :py:class:`mplsldpentityindex <ydk.models.cisco_ios_xe.MPLS_LDP_STD_MIB.MplsLdpStdMib.Mplsldpentitytable.Mplsldpentityentry>`
            
            .. attribute:: mplsldppeerldpid  <key>
            
            	
            	**type**\:  str
            
            	**refers to**\:  :py:class:`mplsldppeerldpid <ydk.models.cisco_ios_xe.MPLS_LDP_STD_MIB.MplsLdpStdMib.Mplsldppeertable.Mplsldppeerentry>`
            
            .. attribute:: mplsldphelloadjacencyindex  <key>
            
            	An identifier for this specific adjacency
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            .. attribute:: mplsldphelloadjacencyholdtime
            
            	The Hello hold time which is negotiated between the Entity and the Peer.  The entity associated with this Hello Adjacency issues a proposed Hello Hold Time value in the mplsLdpEntityHelloHoldTimer object.  The peer also proposes a value and this object represents the negotiated value.  A value of 0 means the default, which is 15 seconds for Link Hellos and 45 seconds for Targeted Hellos. A value of 65535 indicates an infinite hold time
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: mplsldphelloadjacencyholdtimerem
            
            	If the value of this object is 65535, this means that the hold time is infinite (i.e., wait forever).  Otherwise, the time remaining for this Hello Adjacency to receive its next Hello Message.  This interval will change when the 'next' Hello Message which corresponds to this Hello Adjacency is received unless it is infinite
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            	**units**\: seconds
            
            .. attribute:: mplsldphelloadjacencytype
            
            	This adjacency is the result of a 'link' hello if the value of this object is link(1).   Otherwise, it is a result of a 'targeted' hello, targeted(2)
            	**type**\:   :py:class:`Mplsldphelloadjacencytype <ydk.models.cisco_ios_xe.MPLS_LDP_STD_MIB.MplsLdpStdMib.Mplsldphelloadjacencytable.Mplsldphelloadjacencyentry.Mplsldphelloadjacencytype>`
            
            

            """

            _prefix = 'MPLS-LDP-STD-MIB'
            _revision = '2004-06-03'

            def __init__(self):
                super(MplsLdpStdMib.Mplsldphelloadjacencytable.Mplsldphelloadjacencyentry, self).__init__()

                self.yang_name = "mplsLdpHelloAdjacencyEntry"
                self.yang_parent_name = "mplsLdpHelloAdjacencyTable"

                self.mplsldpentityldpid = YLeaf(YType.str, "mplsLdpEntityLdpId")

                self.mplsldpentityindex = YLeaf(YType.str, "mplsLdpEntityIndex")

                self.mplsldppeerldpid = YLeaf(YType.str, "mplsLdpPeerLdpId")

                self.mplsldphelloadjacencyindex = YLeaf(YType.uint32, "mplsLdpHelloAdjacencyIndex")

                self.mplsldphelloadjacencyholdtime = YLeaf(YType.uint32, "mplsLdpHelloAdjacencyHoldTime")

                self.mplsldphelloadjacencyholdtimerem = YLeaf(YType.int32, "mplsLdpHelloAdjacencyHoldTimeRem")

                self.mplsldphelloadjacencytype = YLeaf(YType.enumeration, "mplsLdpHelloAdjacencyType")

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
                                "mplsldppeerldpid",
                                "mplsldphelloadjacencyindex",
                                "mplsldphelloadjacencyholdtime",
                                "mplsldphelloadjacencyholdtimerem",
                                "mplsldphelloadjacencytype") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(MplsLdpStdMib.Mplsldphelloadjacencytable.Mplsldphelloadjacencyentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(MplsLdpStdMib.Mplsldphelloadjacencytable.Mplsldphelloadjacencyentry, self).__setattr__(name, value)

            class Mplsldphelloadjacencytype(Enum):
                """
                Mplsldphelloadjacencytype

                This adjacency is the result of a 'link'

                hello if the value of this object is link(1).

                Otherwise, it is a result of a 'targeted'

                hello, targeted(2).

                .. data:: link = 1

                .. data:: targeted = 2

                """

                link = Enum.YLeaf(1, "link")

                targeted = Enum.YLeaf(2, "targeted")


            def has_data(self):
                return (
                    self.mplsldpentityldpid.is_set or
                    self.mplsldpentityindex.is_set or
                    self.mplsldppeerldpid.is_set or
                    self.mplsldphelloadjacencyindex.is_set or
                    self.mplsldphelloadjacencyholdtime.is_set or
                    self.mplsldphelloadjacencyholdtimerem.is_set or
                    self.mplsldphelloadjacencytype.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.mplsldpentityldpid.yfilter != YFilter.not_set or
                    self.mplsldpentityindex.yfilter != YFilter.not_set or
                    self.mplsldppeerldpid.yfilter != YFilter.not_set or
                    self.mplsldphelloadjacencyindex.yfilter != YFilter.not_set or
                    self.mplsldphelloadjacencyholdtime.yfilter != YFilter.not_set or
                    self.mplsldphelloadjacencyholdtimerem.yfilter != YFilter.not_set or
                    self.mplsldphelloadjacencytype.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "mplsLdpHelloAdjacencyEntry" + "[mplsLdpEntityLdpId='" + self.mplsldpentityldpid.get() + "']" + "[mplsLdpEntityIndex='" + self.mplsldpentityindex.get() + "']" + "[mplsLdpPeerLdpId='" + self.mplsldppeerldpid.get() + "']" + "[mplsLdpHelloAdjacencyIndex='" + self.mplsldphelloadjacencyindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "MPLS-LDP-STD-MIB:MPLS-LDP-STD-MIB/mplsLdpHelloAdjacencyTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.mplsldpentityldpid.is_set or self.mplsldpentityldpid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsldpentityldpid.get_name_leafdata())
                if (self.mplsldpentityindex.is_set or self.mplsldpentityindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsldpentityindex.get_name_leafdata())
                if (self.mplsldppeerldpid.is_set or self.mplsldppeerldpid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsldppeerldpid.get_name_leafdata())
                if (self.mplsldphelloadjacencyindex.is_set or self.mplsldphelloadjacencyindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsldphelloadjacencyindex.get_name_leafdata())
                if (self.mplsldphelloadjacencyholdtime.is_set or self.mplsldphelloadjacencyholdtime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsldphelloadjacencyholdtime.get_name_leafdata())
                if (self.mplsldphelloadjacencyholdtimerem.is_set or self.mplsldphelloadjacencyholdtimerem.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsldphelloadjacencyholdtimerem.get_name_leafdata())
                if (self.mplsldphelloadjacencytype.is_set or self.mplsldphelloadjacencytype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsldphelloadjacencytype.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "mplsLdpEntityLdpId" or name == "mplsLdpEntityIndex" or name == "mplsLdpPeerLdpId" or name == "mplsLdpHelloAdjacencyIndex" or name == "mplsLdpHelloAdjacencyHoldTime" or name == "mplsLdpHelloAdjacencyHoldTimeRem" or name == "mplsLdpHelloAdjacencyType"):
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
                if(value_path == "mplsLdpPeerLdpId"):
                    self.mplsldppeerldpid = value
                    self.mplsldppeerldpid.value_namespace = name_space
                    self.mplsldppeerldpid.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsLdpHelloAdjacencyIndex"):
                    self.mplsldphelloadjacencyindex = value
                    self.mplsldphelloadjacencyindex.value_namespace = name_space
                    self.mplsldphelloadjacencyindex.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsLdpHelloAdjacencyHoldTime"):
                    self.mplsldphelloadjacencyholdtime = value
                    self.mplsldphelloadjacencyholdtime.value_namespace = name_space
                    self.mplsldphelloadjacencyholdtime.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsLdpHelloAdjacencyHoldTimeRem"):
                    self.mplsldphelloadjacencyholdtimerem = value
                    self.mplsldphelloadjacencyholdtimerem.value_namespace = name_space
                    self.mplsldphelloadjacencyholdtimerem.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsLdpHelloAdjacencyType"):
                    self.mplsldphelloadjacencytype = value
                    self.mplsldphelloadjacencytype.value_namespace = name_space
                    self.mplsldphelloadjacencytype.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.mplsldphelloadjacencyentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.mplsldphelloadjacencyentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "mplsLdpHelloAdjacencyTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "MPLS-LDP-STD-MIB:MPLS-LDP-STD-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "mplsLdpHelloAdjacencyEntry"):
                for c in self.mplsldphelloadjacencyentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = MplsLdpStdMib.Mplsldphelloadjacencytable.Mplsldphelloadjacencyentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.mplsldphelloadjacencyentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "mplsLdpHelloAdjacencyEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Mplsinsegmentldplsptable(Entity):
        """
        A table of LDP LSP's which
        map to the mplsInSegmentTable in the
        MPLS\-LSR\-STD\-MIB module.
        
        .. attribute:: mplsinsegmentldplspentry
        
        	An entry in this table represents information on a single LDP LSP which is represented by a session's index triple (mplsLdpEntityLdpId, mplsLdpEntityIndex, mplsLdpPeerLdpId) AND the index for the mplsInSegmentTable (mplsInSegmentLdpLspLabelIndex) from the MPLS\-LSR\-STD\-MIB.  The information contained in a row is read\-only
        	**type**\: list of    :py:class:`Mplsinsegmentldplspentry <ydk.models.cisco_ios_xe.MPLS_LDP_STD_MIB.MplsLdpStdMib.Mplsinsegmentldplsptable.Mplsinsegmentldplspentry>`
        
        

        """

        _prefix = 'MPLS-LDP-STD-MIB'
        _revision = '2004-06-03'

        def __init__(self):
            super(MplsLdpStdMib.Mplsinsegmentldplsptable, self).__init__()

            self.yang_name = "mplsInSegmentLdpLspTable"
            self.yang_parent_name = "MPLS-LDP-STD-MIB"

            self.mplsinsegmentldplspentry = YList(self)

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
                        super(MplsLdpStdMib.Mplsinsegmentldplsptable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(MplsLdpStdMib.Mplsinsegmentldplsptable, self).__setattr__(name, value)


        class Mplsinsegmentldplspentry(Entity):
            """
            An entry in this table represents information
            on a single LDP LSP which is represented by
            a session's index triple (mplsLdpEntityLdpId,
            mplsLdpEntityIndex, mplsLdpPeerLdpId) AND the
            index for the mplsInSegmentTable
            (mplsInSegmentLdpLspLabelIndex) from the
            MPLS\-LSR\-STD\-MIB.
            
            The information contained in a row is read\-only.
            
            .. attribute:: mplsldpentityldpid  <key>
            
            	
            	**type**\:  str
            
            	**refers to**\:  :py:class:`mplsldpentityldpid <ydk.models.cisco_ios_xe.MPLS_LDP_STD_MIB.MplsLdpStdMib.Mplsldpentitytable.Mplsldpentityentry>`
            
            .. attribute:: mplsldpentityindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            	**refers to**\:  :py:class:`mplsldpentityindex <ydk.models.cisco_ios_xe.MPLS_LDP_STD_MIB.MplsLdpStdMib.Mplsldpentitytable.Mplsldpentityentry>`
            
            .. attribute:: mplsldppeerldpid  <key>
            
            	
            	**type**\:  str
            
            	**refers to**\:  :py:class:`mplsldppeerldpid <ydk.models.cisco_ios_xe.MPLS_LDP_STD_MIB.MplsLdpStdMib.Mplsldppeertable.Mplsldppeerentry>`
            
            .. attribute:: mplsinsegmentldplspindex  <key>
            
            	This contains the same value as the mplsInSegmentIndex in the MPLS\-LSR\-STD\-MIB's mplsInSegmentTable
            	**type**\:  str
            
            	**length:** 1..24
            
            .. attribute:: mplsinsegmentldplsplabeltype
            
            	The Layer 2 Label Type
            	**type**\:   :py:class:`Mplsldplabeltype <ydk.models.cisco_ios_xe.MPLS_TC_STD_MIB.Mplsldplabeltype>`
            
            .. attribute:: mplsinsegmentldplsptype
            
            	The type of LSP connection
            	**type**\:   :py:class:`Mplslsptype <ydk.models.cisco_ios_xe.MPLS_TC_STD_MIB.Mplslsptype>`
            
            

            """

            _prefix = 'MPLS-LDP-STD-MIB'
            _revision = '2004-06-03'

            def __init__(self):
                super(MplsLdpStdMib.Mplsinsegmentldplsptable.Mplsinsegmentldplspentry, self).__init__()

                self.yang_name = "mplsInSegmentLdpLspEntry"
                self.yang_parent_name = "mplsInSegmentLdpLspTable"

                self.mplsldpentityldpid = YLeaf(YType.str, "mplsLdpEntityLdpId")

                self.mplsldpentityindex = YLeaf(YType.str, "mplsLdpEntityIndex")

                self.mplsldppeerldpid = YLeaf(YType.str, "mplsLdpPeerLdpId")

                self.mplsinsegmentldplspindex = YLeaf(YType.str, "mplsInSegmentLdpLspIndex")

                self.mplsinsegmentldplsplabeltype = YLeaf(YType.enumeration, "mplsInSegmentLdpLspLabelType")

                self.mplsinsegmentldplsptype = YLeaf(YType.enumeration, "mplsInSegmentLdpLspType")

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
                                "mplsldppeerldpid",
                                "mplsinsegmentldplspindex",
                                "mplsinsegmentldplsplabeltype",
                                "mplsinsegmentldplsptype") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(MplsLdpStdMib.Mplsinsegmentldplsptable.Mplsinsegmentldplspentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(MplsLdpStdMib.Mplsinsegmentldplsptable.Mplsinsegmentldplspentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.mplsldpentityldpid.is_set or
                    self.mplsldpentityindex.is_set or
                    self.mplsldppeerldpid.is_set or
                    self.mplsinsegmentldplspindex.is_set or
                    self.mplsinsegmentldplsplabeltype.is_set or
                    self.mplsinsegmentldplsptype.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.mplsldpentityldpid.yfilter != YFilter.not_set or
                    self.mplsldpentityindex.yfilter != YFilter.not_set or
                    self.mplsldppeerldpid.yfilter != YFilter.not_set or
                    self.mplsinsegmentldplspindex.yfilter != YFilter.not_set or
                    self.mplsinsegmentldplsplabeltype.yfilter != YFilter.not_set or
                    self.mplsinsegmentldplsptype.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "mplsInSegmentLdpLspEntry" + "[mplsLdpEntityLdpId='" + self.mplsldpentityldpid.get() + "']" + "[mplsLdpEntityIndex='" + self.mplsldpentityindex.get() + "']" + "[mplsLdpPeerLdpId='" + self.mplsldppeerldpid.get() + "']" + "[mplsInSegmentLdpLspIndex='" + self.mplsinsegmentldplspindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "MPLS-LDP-STD-MIB:MPLS-LDP-STD-MIB/mplsInSegmentLdpLspTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.mplsldpentityldpid.is_set or self.mplsldpentityldpid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsldpentityldpid.get_name_leafdata())
                if (self.mplsldpentityindex.is_set or self.mplsldpentityindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsldpentityindex.get_name_leafdata())
                if (self.mplsldppeerldpid.is_set or self.mplsldppeerldpid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsldppeerldpid.get_name_leafdata())
                if (self.mplsinsegmentldplspindex.is_set or self.mplsinsegmentldplspindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsinsegmentldplspindex.get_name_leafdata())
                if (self.mplsinsegmentldplsplabeltype.is_set or self.mplsinsegmentldplsplabeltype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsinsegmentldplsplabeltype.get_name_leafdata())
                if (self.mplsinsegmentldplsptype.is_set or self.mplsinsegmentldplsptype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsinsegmentldplsptype.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "mplsLdpEntityLdpId" or name == "mplsLdpEntityIndex" or name == "mplsLdpPeerLdpId" or name == "mplsInSegmentLdpLspIndex" or name == "mplsInSegmentLdpLspLabelType" or name == "mplsInSegmentLdpLspType"):
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
                if(value_path == "mplsLdpPeerLdpId"):
                    self.mplsldppeerldpid = value
                    self.mplsldppeerldpid.value_namespace = name_space
                    self.mplsldppeerldpid.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsInSegmentLdpLspIndex"):
                    self.mplsinsegmentldplspindex = value
                    self.mplsinsegmentldplspindex.value_namespace = name_space
                    self.mplsinsegmentldplspindex.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsInSegmentLdpLspLabelType"):
                    self.mplsinsegmentldplsplabeltype = value
                    self.mplsinsegmentldplsplabeltype.value_namespace = name_space
                    self.mplsinsegmentldplsplabeltype.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsInSegmentLdpLspType"):
                    self.mplsinsegmentldplsptype = value
                    self.mplsinsegmentldplsptype.value_namespace = name_space
                    self.mplsinsegmentldplsptype.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.mplsinsegmentldplspentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.mplsinsegmentldplspentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "mplsInSegmentLdpLspTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "MPLS-LDP-STD-MIB:MPLS-LDP-STD-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "mplsInSegmentLdpLspEntry"):
                for c in self.mplsinsegmentldplspentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = MplsLdpStdMib.Mplsinsegmentldplsptable.Mplsinsegmentldplspentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.mplsinsegmentldplspentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "mplsInSegmentLdpLspEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Mplsoutsegmentldplsptable(Entity):
        """
        A table of LDP LSP's which
        map to the mplsOutSegmentTable in the
        MPLS\-LSR\-STD\-MIB.
        
        .. attribute:: mplsoutsegmentldplspentry
        
        	An entry in this table represents information on a single LDP LSP which is represented by a session's index triple (mplsLdpEntityLdpId, mplsLdpEntityIndex, mplsLdpPeerLdpId) AND the index (mplsOutSegmentLdpLspIndex) for the mplsOutSegmentTable.  The information contained in a row is read\-only
        	**type**\: list of    :py:class:`Mplsoutsegmentldplspentry <ydk.models.cisco_ios_xe.MPLS_LDP_STD_MIB.MplsLdpStdMib.Mplsoutsegmentldplsptable.Mplsoutsegmentldplspentry>`
        
        

        """

        _prefix = 'MPLS-LDP-STD-MIB'
        _revision = '2004-06-03'

        def __init__(self):
            super(MplsLdpStdMib.Mplsoutsegmentldplsptable, self).__init__()

            self.yang_name = "mplsOutSegmentLdpLspTable"
            self.yang_parent_name = "MPLS-LDP-STD-MIB"

            self.mplsoutsegmentldplspentry = YList(self)

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
                        super(MplsLdpStdMib.Mplsoutsegmentldplsptable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(MplsLdpStdMib.Mplsoutsegmentldplsptable, self).__setattr__(name, value)


        class Mplsoutsegmentldplspentry(Entity):
            """
            An entry in this table represents information
            on a single LDP LSP which is represented by
            a session's index triple (mplsLdpEntityLdpId,
            mplsLdpEntityIndex, mplsLdpPeerLdpId) AND the
            index (mplsOutSegmentLdpLspIndex)
            for the mplsOutSegmentTable.
            
            The information contained in a row is read\-only.
            
            .. attribute:: mplsldpentityldpid  <key>
            
            	
            	**type**\:  str
            
            	**refers to**\:  :py:class:`mplsldpentityldpid <ydk.models.cisco_ios_xe.MPLS_LDP_STD_MIB.MplsLdpStdMib.Mplsldpentitytable.Mplsldpentityentry>`
            
            .. attribute:: mplsldpentityindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            	**refers to**\:  :py:class:`mplsldpentityindex <ydk.models.cisco_ios_xe.MPLS_LDP_STD_MIB.MplsLdpStdMib.Mplsldpentitytable.Mplsldpentityentry>`
            
            .. attribute:: mplsldppeerldpid  <key>
            
            	
            	**type**\:  str
            
            	**refers to**\:  :py:class:`mplsldppeerldpid <ydk.models.cisco_ios_xe.MPLS_LDP_STD_MIB.MplsLdpStdMib.Mplsldppeertable.Mplsldppeerentry>`
            
            .. attribute:: mplsoutsegmentldplspindex  <key>
            
            	This contains the same value as the mplsOutSegmentIndex in the MPLS\-LSR\-STD\-MIB's mplsOutSegmentTable
            	**type**\:  str
            
            	**length:** 1..24
            
            .. attribute:: mplsoutsegmentldplsplabeltype
            
            	The Layer 2 Label Type
            	**type**\:   :py:class:`Mplsldplabeltype <ydk.models.cisco_ios_xe.MPLS_TC_STD_MIB.Mplsldplabeltype>`
            
            .. attribute:: mplsoutsegmentldplsptype
            
            	The type of LSP connection
            	**type**\:   :py:class:`Mplslsptype <ydk.models.cisco_ios_xe.MPLS_TC_STD_MIB.Mplslsptype>`
            
            

            """

            _prefix = 'MPLS-LDP-STD-MIB'
            _revision = '2004-06-03'

            def __init__(self):
                super(MplsLdpStdMib.Mplsoutsegmentldplsptable.Mplsoutsegmentldplspentry, self).__init__()

                self.yang_name = "mplsOutSegmentLdpLspEntry"
                self.yang_parent_name = "mplsOutSegmentLdpLspTable"

                self.mplsldpentityldpid = YLeaf(YType.str, "mplsLdpEntityLdpId")

                self.mplsldpentityindex = YLeaf(YType.str, "mplsLdpEntityIndex")

                self.mplsldppeerldpid = YLeaf(YType.str, "mplsLdpPeerLdpId")

                self.mplsoutsegmentldplspindex = YLeaf(YType.str, "mplsOutSegmentLdpLspIndex")

                self.mplsoutsegmentldplsplabeltype = YLeaf(YType.enumeration, "mplsOutSegmentLdpLspLabelType")

                self.mplsoutsegmentldplsptype = YLeaf(YType.enumeration, "mplsOutSegmentLdpLspType")

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
                                "mplsldppeerldpid",
                                "mplsoutsegmentldplspindex",
                                "mplsoutsegmentldplsplabeltype",
                                "mplsoutsegmentldplsptype") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(MplsLdpStdMib.Mplsoutsegmentldplsptable.Mplsoutsegmentldplspentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(MplsLdpStdMib.Mplsoutsegmentldplsptable.Mplsoutsegmentldplspentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.mplsldpentityldpid.is_set or
                    self.mplsldpentityindex.is_set or
                    self.mplsldppeerldpid.is_set or
                    self.mplsoutsegmentldplspindex.is_set or
                    self.mplsoutsegmentldplsplabeltype.is_set or
                    self.mplsoutsegmentldplsptype.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.mplsldpentityldpid.yfilter != YFilter.not_set or
                    self.mplsldpentityindex.yfilter != YFilter.not_set or
                    self.mplsldppeerldpid.yfilter != YFilter.not_set or
                    self.mplsoutsegmentldplspindex.yfilter != YFilter.not_set or
                    self.mplsoutsegmentldplsplabeltype.yfilter != YFilter.not_set or
                    self.mplsoutsegmentldplsptype.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "mplsOutSegmentLdpLspEntry" + "[mplsLdpEntityLdpId='" + self.mplsldpentityldpid.get() + "']" + "[mplsLdpEntityIndex='" + self.mplsldpentityindex.get() + "']" + "[mplsLdpPeerLdpId='" + self.mplsldppeerldpid.get() + "']" + "[mplsOutSegmentLdpLspIndex='" + self.mplsoutsegmentldplspindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "MPLS-LDP-STD-MIB:MPLS-LDP-STD-MIB/mplsOutSegmentLdpLspTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.mplsldpentityldpid.is_set or self.mplsldpentityldpid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsldpentityldpid.get_name_leafdata())
                if (self.mplsldpentityindex.is_set or self.mplsldpentityindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsldpentityindex.get_name_leafdata())
                if (self.mplsldppeerldpid.is_set or self.mplsldppeerldpid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsldppeerldpid.get_name_leafdata())
                if (self.mplsoutsegmentldplspindex.is_set or self.mplsoutsegmentldplspindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsoutsegmentldplspindex.get_name_leafdata())
                if (self.mplsoutsegmentldplsplabeltype.is_set or self.mplsoutsegmentldplsplabeltype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsoutsegmentldplsplabeltype.get_name_leafdata())
                if (self.mplsoutsegmentldplsptype.is_set or self.mplsoutsegmentldplsptype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsoutsegmentldplsptype.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "mplsLdpEntityLdpId" or name == "mplsLdpEntityIndex" or name == "mplsLdpPeerLdpId" or name == "mplsOutSegmentLdpLspIndex" or name == "mplsOutSegmentLdpLspLabelType" or name == "mplsOutSegmentLdpLspType"):
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
                if(value_path == "mplsLdpPeerLdpId"):
                    self.mplsldppeerldpid = value
                    self.mplsldppeerldpid.value_namespace = name_space
                    self.mplsldppeerldpid.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsOutSegmentLdpLspIndex"):
                    self.mplsoutsegmentldplspindex = value
                    self.mplsoutsegmentldplspindex.value_namespace = name_space
                    self.mplsoutsegmentldplspindex.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsOutSegmentLdpLspLabelType"):
                    self.mplsoutsegmentldplsplabeltype = value
                    self.mplsoutsegmentldplsplabeltype.value_namespace = name_space
                    self.mplsoutsegmentldplsplabeltype.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsOutSegmentLdpLspType"):
                    self.mplsoutsegmentldplsptype = value
                    self.mplsoutsegmentldplsptype.value_namespace = name_space
                    self.mplsoutsegmentldplsptype.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.mplsoutsegmentldplspentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.mplsoutsegmentldplspentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "mplsOutSegmentLdpLspTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "MPLS-LDP-STD-MIB:MPLS-LDP-STD-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "mplsOutSegmentLdpLspEntry"):
                for c in self.mplsoutsegmentldplspentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = MplsLdpStdMib.Mplsoutsegmentldplsptable.Mplsoutsegmentldplspentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.mplsoutsegmentldplspentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "mplsOutSegmentLdpLspEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Mplsfectable(Entity):
        """
        This table represents the FEC
        (Forwarding Equivalence Class)
        Information associated with an LSP.
        
        .. attribute:: mplsfecentry
        
        	Each row represents a single FEC Element
        	**type**\: list of    :py:class:`Mplsfecentry <ydk.models.cisco_ios_xe.MPLS_LDP_STD_MIB.MplsLdpStdMib.Mplsfectable.Mplsfecentry>`
        
        

        """

        _prefix = 'MPLS-LDP-STD-MIB'
        _revision = '2004-06-03'

        def __init__(self):
            super(MplsLdpStdMib.Mplsfectable, self).__init__()

            self.yang_name = "mplsFecTable"
            self.yang_parent_name = "MPLS-LDP-STD-MIB"

            self.mplsfecentry = YList(self)

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
                        super(MplsLdpStdMib.Mplsfectable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(MplsLdpStdMib.Mplsfectable, self).__setattr__(name, value)


        class Mplsfecentry(Entity):
            """
            Each row represents a single FEC Element.
            
            .. attribute:: mplsfecindex  <key>
            
            	The index which uniquely identifies this entry
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            .. attribute:: mplsfecaddr
            
            	The value of this object is interpreted based on the value of the 'mplsFecAddrType' object.  This address is then further interpretted as an being used with the address prefix, or as the host address.  This further interpretation is indicated by the 'mplsFecType' object. In other words, the FEC element is populated according to the Prefix FEC Element value encoding, or the Host Address FEC Element encoding
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: mplsfecaddrprefixlength
            
            	If the value of the 'mplsFecType' is 'hostAddress(2)' then this object is undefined.  If the value of 'mplsFecType' is 'prefix(1)' then the value of this object is the length in bits of the address prefix represented by 'mplsFecAddr', or zero.  If the value of this object is zero, this indicates that the prefix matches all addresses.  In this case the address prefix MUST also be zero (i.e., 'mplsFecAddr' should have the value of zero.)
            	**type**\:  int
            
            	**range:** 0..2040
            
            .. attribute:: mplsfecaddrtype
            
            	The value of this object is the type of the Internet address.  The value of this object, decides how the value of the mplsFecAddr object is interpreted
            	**type**\:   :py:class:`Inetaddresstype <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.Inetaddresstype>`
            
            .. attribute:: mplsfecrowstatus
            
            	The status of this conceptual row.  If the value of this object is 'active(1)', then none of the writable objects of this entry can be modified, except to set this object to 'destroy(6)'.  NOTE\: if this row is being referenced by any entry in the mplsLdpLspFecTable, then a request to destroy this row, will result in an inconsistentValue error
            	**type**\:   :py:class:`Rowstatus <ydk.models.cisco_ios_xe.SNMPv2_TC.Rowstatus>`
            
            .. attribute:: mplsfecstoragetype
            
            	The storage type for this conceptual row. Conceptual rows having the value 'permanent(4)' need not allow write\-access to any columnar objects in the row
            	**type**\:   :py:class:`Storagetype <ydk.models.cisco_ios_xe.SNMPv2_TC.Storagetype>`
            
            .. attribute:: mplsfectype
            
            	The type of the FEC.  If the value of this object is 'prefix(1)' then the FEC type described by this row is an address prefix.  If the value of this object is 'hostAddress(2)' then the FEC type described by this row is a host address
            	**type**\:   :py:class:`Mplsfectype <ydk.models.cisco_ios_xe.MPLS_LDP_STD_MIB.MplsLdpStdMib.Mplsfectable.Mplsfecentry.Mplsfectype>`
            
            

            """

            _prefix = 'MPLS-LDP-STD-MIB'
            _revision = '2004-06-03'

            def __init__(self):
                super(MplsLdpStdMib.Mplsfectable.Mplsfecentry, self).__init__()

                self.yang_name = "mplsFecEntry"
                self.yang_parent_name = "mplsFecTable"

                self.mplsfecindex = YLeaf(YType.uint32, "mplsFecIndex")

                self.mplsfecaddr = YLeaf(YType.str, "mplsFecAddr")

                self.mplsfecaddrprefixlength = YLeaf(YType.uint32, "mplsFecAddrPrefixLength")

                self.mplsfecaddrtype = YLeaf(YType.enumeration, "mplsFecAddrType")

                self.mplsfecrowstatus = YLeaf(YType.enumeration, "mplsFecRowStatus")

                self.mplsfecstoragetype = YLeaf(YType.enumeration, "mplsFecStorageType")

                self.mplsfectype = YLeaf(YType.enumeration, "mplsFecType")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("mplsfecindex",
                                "mplsfecaddr",
                                "mplsfecaddrprefixlength",
                                "mplsfecaddrtype",
                                "mplsfecrowstatus",
                                "mplsfecstoragetype",
                                "mplsfectype") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(MplsLdpStdMib.Mplsfectable.Mplsfecentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(MplsLdpStdMib.Mplsfectable.Mplsfecentry, self).__setattr__(name, value)

            class Mplsfectype(Enum):
                """
                Mplsfectype

                The type of the FEC.  If the value of this object

                is 'prefix(1)' then the FEC type described by this

                row is an address prefix.

                If the value of this object is 'hostAddress(2)' then

                the FEC type described by this row is a host address.

                .. data:: prefix = 1

                .. data:: hostAddress = 2

                """

                prefix = Enum.YLeaf(1, "prefix")

                hostAddress = Enum.YLeaf(2, "hostAddress")


            def has_data(self):
                return (
                    self.mplsfecindex.is_set or
                    self.mplsfecaddr.is_set or
                    self.mplsfecaddrprefixlength.is_set or
                    self.mplsfecaddrtype.is_set or
                    self.mplsfecrowstatus.is_set or
                    self.mplsfecstoragetype.is_set or
                    self.mplsfectype.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.mplsfecindex.yfilter != YFilter.not_set or
                    self.mplsfecaddr.yfilter != YFilter.not_set or
                    self.mplsfecaddrprefixlength.yfilter != YFilter.not_set or
                    self.mplsfecaddrtype.yfilter != YFilter.not_set or
                    self.mplsfecrowstatus.yfilter != YFilter.not_set or
                    self.mplsfecstoragetype.yfilter != YFilter.not_set or
                    self.mplsfectype.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "mplsFecEntry" + "[mplsFecIndex='" + self.mplsfecindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "MPLS-LDP-STD-MIB:MPLS-LDP-STD-MIB/mplsFecTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.mplsfecindex.is_set or self.mplsfecindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsfecindex.get_name_leafdata())
                if (self.mplsfecaddr.is_set or self.mplsfecaddr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsfecaddr.get_name_leafdata())
                if (self.mplsfecaddrprefixlength.is_set or self.mplsfecaddrprefixlength.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsfecaddrprefixlength.get_name_leafdata())
                if (self.mplsfecaddrtype.is_set or self.mplsfecaddrtype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsfecaddrtype.get_name_leafdata())
                if (self.mplsfecrowstatus.is_set or self.mplsfecrowstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsfecrowstatus.get_name_leafdata())
                if (self.mplsfecstoragetype.is_set or self.mplsfecstoragetype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsfecstoragetype.get_name_leafdata())
                if (self.mplsfectype.is_set or self.mplsfectype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsfectype.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "mplsFecIndex" or name == "mplsFecAddr" or name == "mplsFecAddrPrefixLength" or name == "mplsFecAddrType" or name == "mplsFecRowStatus" or name == "mplsFecStorageType" or name == "mplsFecType"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "mplsFecIndex"):
                    self.mplsfecindex = value
                    self.mplsfecindex.value_namespace = name_space
                    self.mplsfecindex.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsFecAddr"):
                    self.mplsfecaddr = value
                    self.mplsfecaddr.value_namespace = name_space
                    self.mplsfecaddr.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsFecAddrPrefixLength"):
                    self.mplsfecaddrprefixlength = value
                    self.mplsfecaddrprefixlength.value_namespace = name_space
                    self.mplsfecaddrprefixlength.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsFecAddrType"):
                    self.mplsfecaddrtype = value
                    self.mplsfecaddrtype.value_namespace = name_space
                    self.mplsfecaddrtype.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsFecRowStatus"):
                    self.mplsfecrowstatus = value
                    self.mplsfecrowstatus.value_namespace = name_space
                    self.mplsfecrowstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsFecStorageType"):
                    self.mplsfecstoragetype = value
                    self.mplsfecstoragetype.value_namespace = name_space
                    self.mplsfecstoragetype.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsFecType"):
                    self.mplsfectype = value
                    self.mplsfectype.value_namespace = name_space
                    self.mplsfectype.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.mplsfecentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.mplsfecentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "mplsFecTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "MPLS-LDP-STD-MIB:MPLS-LDP-STD-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "mplsFecEntry"):
                for c in self.mplsfecentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = MplsLdpStdMib.Mplsfectable.Mplsfecentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.mplsfecentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "mplsFecEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Mplsldplspfectable(Entity):
        """
        A table which shows the relationship between
        LDP LSPs and FECs.  Each row represents
        a single LDP LSP to FEC association.
        
        .. attribute:: mplsldplspfecentry
        
        	An entry represents a LDP LSP to FEC association
        	**type**\: list of    :py:class:`Mplsldplspfecentry <ydk.models.cisco_ios_xe.MPLS_LDP_STD_MIB.MplsLdpStdMib.Mplsldplspfectable.Mplsldplspfecentry>`
        
        

        """

        _prefix = 'MPLS-LDP-STD-MIB'
        _revision = '2004-06-03'

        def __init__(self):
            super(MplsLdpStdMib.Mplsldplspfectable, self).__init__()

            self.yang_name = "mplsLdpLspFecTable"
            self.yang_parent_name = "MPLS-LDP-STD-MIB"

            self.mplsldplspfecentry = YList(self)

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
                        super(MplsLdpStdMib.Mplsldplspfectable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(MplsLdpStdMib.Mplsldplspfectable, self).__setattr__(name, value)


        class Mplsldplspfecentry(Entity):
            """
            An entry represents a LDP LSP
            to FEC association.
            
            .. attribute:: mplsldpentityldpid  <key>
            
            	
            	**type**\:  str
            
            	**refers to**\:  :py:class:`mplsldpentityldpid <ydk.models.cisco_ios_xe.MPLS_LDP_STD_MIB.MplsLdpStdMib.Mplsldpentitytable.Mplsldpentityentry>`
            
            .. attribute:: mplsldpentityindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            	**refers to**\:  :py:class:`mplsldpentityindex <ydk.models.cisco_ios_xe.MPLS_LDP_STD_MIB.MplsLdpStdMib.Mplsldpentitytable.Mplsldpentityentry>`
            
            .. attribute:: mplsldppeerldpid  <key>
            
            	
            	**type**\:  str
            
            	**refers to**\:  :py:class:`mplsldppeerldpid <ydk.models.cisco_ios_xe.MPLS_LDP_STD_MIB.MplsLdpStdMib.Mplsldppeertable.Mplsldppeerentry>`
            
            .. attribute:: mplsldplspfecsegment  <key>
            
            	If the value is inSegment(1), then this indicates that the following index, mplsLdpLspFecSegmentIndex, contains the same value as the mplsInSegmentLdpLspIndex.  Otherwise, if the value of this object is   outSegment(2),  then this indicates that following index, mplsLdpLspFecSegmentIndex, contains the same value as the mplsOutSegmentLdpLspIndex
            	**type**\:   :py:class:`Mplsldplspfecsegment <ydk.models.cisco_ios_xe.MPLS_LDP_STD_MIB.MplsLdpStdMib.Mplsldplspfectable.Mplsldplspfecentry.Mplsldplspfecsegment>`
            
            .. attribute:: mplsldplspfecsegmentindex  <key>
            
            	This index is interpretted by using the value of the mplsLdpLspFecSegment.  If the mplsLdpLspFecSegment is inSegment(1), then this index has the same value as mplsInSegmentLdpLspIndex.  If the mplsLdpLspFecSegment is outSegment(2), then this index has the same value as mplsOutSegmentLdpLspIndex
            	**type**\:  str
            
            	**length:** 1..24
            
            .. attribute:: mplsldplspfecindex  <key>
            
            	This index identifies the FEC entry in the mplsFecTable associated with this session. In other words, the value of this index is the same as the value of the mplsFecIndex that denotes the FEC associated with this Session
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            .. attribute:: mplsldplspfecrowstatus
            
            	The status of this conceptual row.  If the value of this object is 'active(1)', then none of the writable objects of this entry can be modified.  The Agent should delete this row when the session ceases to exist.  If an operator wants to associate the session with a different FEC, the recommended procedure is (as described in detail in the section entitled, 'Changing Values After Session Establishment', and again described in the DESCRIPTION clause of the mplsLdpEntityAdminStatus object) is to set the mplsLdpEntityAdminStatus to down, thereby explicitly causing a session to be torn down. This will also cause this entry to be deleted.  Then, set the mplsLdpEntityAdminStatus to enable which enables a new session to be initiated. Once the session is initiated, an entry may be added to this table to associate the new session with a FEC
            	**type**\:   :py:class:`Rowstatus <ydk.models.cisco_ios_xe.SNMPv2_TC.Rowstatus>`
            
            .. attribute:: mplsldplspfecstoragetype
            
            	The storage type for this conceptual row. Conceptual rows having the value 'permanent(4)' need not allow write\-access to any columnar objects in the row
            	**type**\:   :py:class:`Storagetype <ydk.models.cisco_ios_xe.SNMPv2_TC.Storagetype>`
            
            

            """

            _prefix = 'MPLS-LDP-STD-MIB'
            _revision = '2004-06-03'

            def __init__(self):
                super(MplsLdpStdMib.Mplsldplspfectable.Mplsldplspfecentry, self).__init__()

                self.yang_name = "mplsLdpLspFecEntry"
                self.yang_parent_name = "mplsLdpLspFecTable"

                self.mplsldpentityldpid = YLeaf(YType.str, "mplsLdpEntityLdpId")

                self.mplsldpentityindex = YLeaf(YType.str, "mplsLdpEntityIndex")

                self.mplsldppeerldpid = YLeaf(YType.str, "mplsLdpPeerLdpId")

                self.mplsldplspfecsegment = YLeaf(YType.enumeration, "mplsLdpLspFecSegment")

                self.mplsldplspfecsegmentindex = YLeaf(YType.str, "mplsLdpLspFecSegmentIndex")

                self.mplsldplspfecindex = YLeaf(YType.uint32, "mplsLdpLspFecIndex")

                self.mplsldplspfecrowstatus = YLeaf(YType.enumeration, "mplsLdpLspFecRowStatus")

                self.mplsldplspfecstoragetype = YLeaf(YType.enumeration, "mplsLdpLspFecStorageType")

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
                                "mplsldppeerldpid",
                                "mplsldplspfecsegment",
                                "mplsldplspfecsegmentindex",
                                "mplsldplspfecindex",
                                "mplsldplspfecrowstatus",
                                "mplsldplspfecstoragetype") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(MplsLdpStdMib.Mplsldplspfectable.Mplsldplspfecentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(MplsLdpStdMib.Mplsldplspfectable.Mplsldplspfecentry, self).__setattr__(name, value)

            class Mplsldplspfecsegment(Enum):
                """
                Mplsldplspfecsegment

                If the value is inSegment(1), then this

                indicates that the following index,

                mplsLdpLspFecSegmentIndex, contains the same

                value as the mplsInSegmentLdpLspIndex.

                Otherwise, if the value of this object is

                outSegment(2),  then this

                indicates that following index,

                mplsLdpLspFecSegmentIndex, contains the same

                value as the mplsOutSegmentLdpLspIndex.

                .. data:: inSegment = 1

                .. data:: outSegment = 2

                """

                inSegment = Enum.YLeaf(1, "inSegment")

                outSegment = Enum.YLeaf(2, "outSegment")


            def has_data(self):
                return (
                    self.mplsldpentityldpid.is_set or
                    self.mplsldpentityindex.is_set or
                    self.mplsldppeerldpid.is_set or
                    self.mplsldplspfecsegment.is_set or
                    self.mplsldplspfecsegmentindex.is_set or
                    self.mplsldplspfecindex.is_set or
                    self.mplsldplspfecrowstatus.is_set or
                    self.mplsldplspfecstoragetype.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.mplsldpentityldpid.yfilter != YFilter.not_set or
                    self.mplsldpentityindex.yfilter != YFilter.not_set or
                    self.mplsldppeerldpid.yfilter != YFilter.not_set or
                    self.mplsldplspfecsegment.yfilter != YFilter.not_set or
                    self.mplsldplspfecsegmentindex.yfilter != YFilter.not_set or
                    self.mplsldplspfecindex.yfilter != YFilter.not_set or
                    self.mplsldplspfecrowstatus.yfilter != YFilter.not_set or
                    self.mplsldplspfecstoragetype.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "mplsLdpLspFecEntry" + "[mplsLdpEntityLdpId='" + self.mplsldpentityldpid.get() + "']" + "[mplsLdpEntityIndex='" + self.mplsldpentityindex.get() + "']" + "[mplsLdpPeerLdpId='" + self.mplsldppeerldpid.get() + "']" + "[mplsLdpLspFecSegment='" + self.mplsldplspfecsegment.get() + "']" + "[mplsLdpLspFecSegmentIndex='" + self.mplsldplspfecsegmentindex.get() + "']" + "[mplsLdpLspFecIndex='" + self.mplsldplspfecindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "MPLS-LDP-STD-MIB:MPLS-LDP-STD-MIB/mplsLdpLspFecTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.mplsldpentityldpid.is_set or self.mplsldpentityldpid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsldpentityldpid.get_name_leafdata())
                if (self.mplsldpentityindex.is_set or self.mplsldpentityindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsldpentityindex.get_name_leafdata())
                if (self.mplsldppeerldpid.is_set or self.mplsldppeerldpid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsldppeerldpid.get_name_leafdata())
                if (self.mplsldplspfecsegment.is_set or self.mplsldplspfecsegment.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsldplspfecsegment.get_name_leafdata())
                if (self.mplsldplspfecsegmentindex.is_set or self.mplsldplspfecsegmentindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsldplspfecsegmentindex.get_name_leafdata())
                if (self.mplsldplspfecindex.is_set or self.mplsldplspfecindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsldplspfecindex.get_name_leafdata())
                if (self.mplsldplspfecrowstatus.is_set or self.mplsldplspfecrowstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsldplspfecrowstatus.get_name_leafdata())
                if (self.mplsldplspfecstoragetype.is_set or self.mplsldplspfecstoragetype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsldplspfecstoragetype.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "mplsLdpEntityLdpId" or name == "mplsLdpEntityIndex" or name == "mplsLdpPeerLdpId" or name == "mplsLdpLspFecSegment" or name == "mplsLdpLspFecSegmentIndex" or name == "mplsLdpLspFecIndex" or name == "mplsLdpLspFecRowStatus" or name == "mplsLdpLspFecStorageType"):
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
                if(value_path == "mplsLdpPeerLdpId"):
                    self.mplsldppeerldpid = value
                    self.mplsldppeerldpid.value_namespace = name_space
                    self.mplsldppeerldpid.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsLdpLspFecSegment"):
                    self.mplsldplspfecsegment = value
                    self.mplsldplspfecsegment.value_namespace = name_space
                    self.mplsldplspfecsegment.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsLdpLspFecSegmentIndex"):
                    self.mplsldplspfecsegmentindex = value
                    self.mplsldplspfecsegmentindex.value_namespace = name_space
                    self.mplsldplspfecsegmentindex.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsLdpLspFecIndex"):
                    self.mplsldplspfecindex = value
                    self.mplsldplspfecindex.value_namespace = name_space
                    self.mplsldplspfecindex.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsLdpLspFecRowStatus"):
                    self.mplsldplspfecrowstatus = value
                    self.mplsldplspfecrowstatus.value_namespace = name_space
                    self.mplsldplspfecrowstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsLdpLspFecStorageType"):
                    self.mplsldplspfecstoragetype = value
                    self.mplsldplspfecstoragetype.value_namespace = name_space
                    self.mplsldplspfecstoragetype.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.mplsldplspfecentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.mplsldplspfecentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "mplsLdpLspFecTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "MPLS-LDP-STD-MIB:MPLS-LDP-STD-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "mplsLdpLspFecEntry"):
                for c in self.mplsldplspfecentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = MplsLdpStdMib.Mplsldplspfectable.Mplsldplspfecentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.mplsldplspfecentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "mplsLdpLspFecEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Mplsldpsessionpeeraddrtable(Entity):
        """
        This table 'extends' the mplsLdpSessionTable.
        This table is used to store Label Address Information
        from Label Address Messages received by this LSR from
        Peers.  This table is read\-only and should be updated
        
        
        when Label Withdraw Address Messages are received, i.e.,
        Rows should be deleted as appropriate.
        
        NOTE\:  since more than one address may be contained
        in a Label Address Message, this table 'sparse augments',
        the mplsLdpSessionTable's information.
        
        .. attribute:: mplsldpsessionpeeraddrentry
        
        	An entry in this table represents information on a session's single next hop address which was advertised in an Address Message from the LDP peer. The information contained in a row is read\-only
        	**type**\: list of    :py:class:`Mplsldpsessionpeeraddrentry <ydk.models.cisco_ios_xe.MPLS_LDP_STD_MIB.MplsLdpStdMib.Mplsldpsessionpeeraddrtable.Mplsldpsessionpeeraddrentry>`
        
        

        """

        _prefix = 'MPLS-LDP-STD-MIB'
        _revision = '2004-06-03'

        def __init__(self):
            super(MplsLdpStdMib.Mplsldpsessionpeeraddrtable, self).__init__()

            self.yang_name = "mplsLdpSessionPeerAddrTable"
            self.yang_parent_name = "MPLS-LDP-STD-MIB"

            self.mplsldpsessionpeeraddrentry = YList(self)

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
                        super(MplsLdpStdMib.Mplsldpsessionpeeraddrtable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(MplsLdpStdMib.Mplsldpsessionpeeraddrtable, self).__setattr__(name, value)


        class Mplsldpsessionpeeraddrentry(Entity):
            """
            An entry in this table represents information on
            a session's single next hop address which was
            advertised in an Address Message from the LDP peer.
            The information contained in a row is read\-only.
            
            .. attribute:: mplsldpentityldpid  <key>
            
            	
            	**type**\:  str
            
            	**refers to**\:  :py:class:`mplsldpentityldpid <ydk.models.cisco_ios_xe.MPLS_LDP_STD_MIB.MplsLdpStdMib.Mplsldpentitytable.Mplsldpentityentry>`
            
            .. attribute:: mplsldpentityindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            	**refers to**\:  :py:class:`mplsldpentityindex <ydk.models.cisco_ios_xe.MPLS_LDP_STD_MIB.MplsLdpStdMib.Mplsldpentitytable.Mplsldpentityentry>`
            
            .. attribute:: mplsldppeerldpid  <key>
            
            	
            	**type**\:  str
            
            	**refers to**\:  :py:class:`mplsldppeerldpid <ydk.models.cisco_ios_xe.MPLS_LDP_STD_MIB.MplsLdpStdMib.Mplsldppeertable.Mplsldppeerentry>`
            
            .. attribute:: mplsldpsessionpeeraddrindex  <key>
            
            	An index which uniquely identifies this entry within a given session
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            .. attribute:: mplsldpsessionpeernexthopaddr
            
            	The next hop address.  The type of this address is specified by the value of the mplsLdpSessionPeerNextHopAddrType
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: mplsldpsessionpeernexthopaddrtype
            
            	The internetwork layer address type of this Next Hop Address as specified in the Label Address Message associated with this Session. The value of this object indicates how to interpret the value of   mplsLdpSessionPeerNextHopAddr
            	**type**\:   :py:class:`Inetaddresstype <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.Inetaddresstype>`
            
            

            """

            _prefix = 'MPLS-LDP-STD-MIB'
            _revision = '2004-06-03'

            def __init__(self):
                super(MplsLdpStdMib.Mplsldpsessionpeeraddrtable.Mplsldpsessionpeeraddrentry, self).__init__()

                self.yang_name = "mplsLdpSessionPeerAddrEntry"
                self.yang_parent_name = "mplsLdpSessionPeerAddrTable"

                self.mplsldpentityldpid = YLeaf(YType.str, "mplsLdpEntityLdpId")

                self.mplsldpentityindex = YLeaf(YType.str, "mplsLdpEntityIndex")

                self.mplsldppeerldpid = YLeaf(YType.str, "mplsLdpPeerLdpId")

                self.mplsldpsessionpeeraddrindex = YLeaf(YType.uint32, "mplsLdpSessionPeerAddrIndex")

                self.mplsldpsessionpeernexthopaddr = YLeaf(YType.str, "mplsLdpSessionPeerNextHopAddr")

                self.mplsldpsessionpeernexthopaddrtype = YLeaf(YType.enumeration, "mplsLdpSessionPeerNextHopAddrType")

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
                                "mplsldppeerldpid",
                                "mplsldpsessionpeeraddrindex",
                                "mplsldpsessionpeernexthopaddr",
                                "mplsldpsessionpeernexthopaddrtype") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(MplsLdpStdMib.Mplsldpsessionpeeraddrtable.Mplsldpsessionpeeraddrentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(MplsLdpStdMib.Mplsldpsessionpeeraddrtable.Mplsldpsessionpeeraddrentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.mplsldpentityldpid.is_set or
                    self.mplsldpentityindex.is_set or
                    self.mplsldppeerldpid.is_set or
                    self.mplsldpsessionpeeraddrindex.is_set or
                    self.mplsldpsessionpeernexthopaddr.is_set or
                    self.mplsldpsessionpeernexthopaddrtype.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.mplsldpentityldpid.yfilter != YFilter.not_set or
                    self.mplsldpentityindex.yfilter != YFilter.not_set or
                    self.mplsldppeerldpid.yfilter != YFilter.not_set or
                    self.mplsldpsessionpeeraddrindex.yfilter != YFilter.not_set or
                    self.mplsldpsessionpeernexthopaddr.yfilter != YFilter.not_set or
                    self.mplsldpsessionpeernexthopaddrtype.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "mplsLdpSessionPeerAddrEntry" + "[mplsLdpEntityLdpId='" + self.mplsldpentityldpid.get() + "']" + "[mplsLdpEntityIndex='" + self.mplsldpentityindex.get() + "']" + "[mplsLdpPeerLdpId='" + self.mplsldppeerldpid.get() + "']" + "[mplsLdpSessionPeerAddrIndex='" + self.mplsldpsessionpeeraddrindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "MPLS-LDP-STD-MIB:MPLS-LDP-STD-MIB/mplsLdpSessionPeerAddrTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.mplsldpentityldpid.is_set or self.mplsldpentityldpid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsldpentityldpid.get_name_leafdata())
                if (self.mplsldpentityindex.is_set or self.mplsldpentityindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsldpentityindex.get_name_leafdata())
                if (self.mplsldppeerldpid.is_set or self.mplsldppeerldpid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsldppeerldpid.get_name_leafdata())
                if (self.mplsldpsessionpeeraddrindex.is_set or self.mplsldpsessionpeeraddrindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsldpsessionpeeraddrindex.get_name_leafdata())
                if (self.mplsldpsessionpeernexthopaddr.is_set or self.mplsldpsessionpeernexthopaddr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsldpsessionpeernexthopaddr.get_name_leafdata())
                if (self.mplsldpsessionpeernexthopaddrtype.is_set or self.mplsldpsessionpeernexthopaddrtype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsldpsessionpeernexthopaddrtype.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "mplsLdpEntityLdpId" or name == "mplsLdpEntityIndex" or name == "mplsLdpPeerLdpId" or name == "mplsLdpSessionPeerAddrIndex" or name == "mplsLdpSessionPeerNextHopAddr" or name == "mplsLdpSessionPeerNextHopAddrType"):
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
                if(value_path == "mplsLdpPeerLdpId"):
                    self.mplsldppeerldpid = value
                    self.mplsldppeerldpid.value_namespace = name_space
                    self.mplsldppeerldpid.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsLdpSessionPeerAddrIndex"):
                    self.mplsldpsessionpeeraddrindex = value
                    self.mplsldpsessionpeeraddrindex.value_namespace = name_space
                    self.mplsldpsessionpeeraddrindex.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsLdpSessionPeerNextHopAddr"):
                    self.mplsldpsessionpeernexthopaddr = value
                    self.mplsldpsessionpeernexthopaddr.value_namespace = name_space
                    self.mplsldpsessionpeernexthopaddr.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsLdpSessionPeerNextHopAddrType"):
                    self.mplsldpsessionpeernexthopaddrtype = value
                    self.mplsldpsessionpeernexthopaddrtype.value_namespace = name_space
                    self.mplsldpsessionpeernexthopaddrtype.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.mplsldpsessionpeeraddrentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.mplsldpsessionpeeraddrentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "mplsLdpSessionPeerAddrTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "MPLS-LDP-STD-MIB:MPLS-LDP-STD-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "mplsLdpSessionPeerAddrEntry"):
                for c in self.mplsldpsessionpeeraddrentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = MplsLdpStdMib.Mplsldpsessionpeeraddrtable.Mplsldpsessionpeeraddrentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.mplsldpsessionpeeraddrentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "mplsLdpSessionPeerAddrEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            (self.mplsfecobjects is not None and self.mplsfecobjects.has_data()) or
            (self.mplsfectable is not None and self.mplsfectable.has_data()) or
            (self.mplsinsegmentldplsptable is not None and self.mplsinsegmentldplsptable.has_data()) or
            (self.mplsldpentityobjects is not None and self.mplsldpentityobjects.has_data()) or
            (self.mplsldpentitytable is not None and self.mplsldpentitytable.has_data()) or
            (self.mplsldphelloadjacencytable is not None and self.mplsldphelloadjacencytable.has_data()) or
            (self.mplsldplspfectable is not None and self.mplsldplspfectable.has_data()) or
            (self.mplsldplsrobjects is not None and self.mplsldplsrobjects.has_data()) or
            (self.mplsldppeertable is not None and self.mplsldppeertable.has_data()) or
            (self.mplsldpsessionobjects is not None and self.mplsldpsessionobjects.has_data()) or
            (self.mplsldpsessionpeeraddrtable is not None and self.mplsldpsessionpeeraddrtable.has_data()) or
            (self.mplsoutsegmentldplsptable is not None and self.mplsoutsegmentldplsptable.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.mplsfecobjects is not None and self.mplsfecobjects.has_operation()) or
            (self.mplsfectable is not None and self.mplsfectable.has_operation()) or
            (self.mplsinsegmentldplsptable is not None and self.mplsinsegmentldplsptable.has_operation()) or
            (self.mplsldpentityobjects is not None and self.mplsldpentityobjects.has_operation()) or
            (self.mplsldpentitytable is not None and self.mplsldpentitytable.has_operation()) or
            (self.mplsldphelloadjacencytable is not None and self.mplsldphelloadjacencytable.has_operation()) or
            (self.mplsldplspfectable is not None and self.mplsldplspfectable.has_operation()) or
            (self.mplsldplsrobjects is not None and self.mplsldplsrobjects.has_operation()) or
            (self.mplsldppeertable is not None and self.mplsldppeertable.has_operation()) or
            (self.mplsldpsessionobjects is not None and self.mplsldpsessionobjects.has_operation()) or
            (self.mplsldpsessionpeeraddrtable is not None and self.mplsldpsessionpeeraddrtable.has_operation()) or
            (self.mplsoutsegmentldplsptable is not None and self.mplsoutsegmentldplsptable.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "MPLS-LDP-STD-MIB:MPLS-LDP-STD-MIB" + path_buffer

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

        if (child_yang_name == "mplsFecObjects"):
            if (self.mplsfecobjects is None):
                self.mplsfecobjects = MplsLdpStdMib.Mplsfecobjects()
                self.mplsfecobjects.parent = self
                self._children_name_map["mplsfecobjects"] = "mplsFecObjects"
            return self.mplsfecobjects

        if (child_yang_name == "mplsFecTable"):
            if (self.mplsfectable is None):
                self.mplsfectable = MplsLdpStdMib.Mplsfectable()
                self.mplsfectable.parent = self
                self._children_name_map["mplsfectable"] = "mplsFecTable"
            return self.mplsfectable

        if (child_yang_name == "mplsInSegmentLdpLspTable"):
            if (self.mplsinsegmentldplsptable is None):
                self.mplsinsegmentldplsptable = MplsLdpStdMib.Mplsinsegmentldplsptable()
                self.mplsinsegmentldplsptable.parent = self
                self._children_name_map["mplsinsegmentldplsptable"] = "mplsInSegmentLdpLspTable"
            return self.mplsinsegmentldplsptable

        if (child_yang_name == "mplsLdpEntityObjects"):
            if (self.mplsldpentityobjects is None):
                self.mplsldpentityobjects = MplsLdpStdMib.Mplsldpentityobjects()
                self.mplsldpentityobjects.parent = self
                self._children_name_map["mplsldpentityobjects"] = "mplsLdpEntityObjects"
            return self.mplsldpentityobjects

        if (child_yang_name == "mplsLdpEntityTable"):
            if (self.mplsldpentitytable is None):
                self.mplsldpentitytable = MplsLdpStdMib.Mplsldpentitytable()
                self.mplsldpentitytable.parent = self
                self._children_name_map["mplsldpentitytable"] = "mplsLdpEntityTable"
            return self.mplsldpentitytable

        if (child_yang_name == "mplsLdpHelloAdjacencyTable"):
            if (self.mplsldphelloadjacencytable is None):
                self.mplsldphelloadjacencytable = MplsLdpStdMib.Mplsldphelloadjacencytable()
                self.mplsldphelloadjacencytable.parent = self
                self._children_name_map["mplsldphelloadjacencytable"] = "mplsLdpHelloAdjacencyTable"
            return self.mplsldphelloadjacencytable

        if (child_yang_name == "mplsLdpLspFecTable"):
            if (self.mplsldplspfectable is None):
                self.mplsldplspfectable = MplsLdpStdMib.Mplsldplspfectable()
                self.mplsldplspfectable.parent = self
                self._children_name_map["mplsldplspfectable"] = "mplsLdpLspFecTable"
            return self.mplsldplspfectable

        if (child_yang_name == "mplsLdpLsrObjects"):
            if (self.mplsldplsrobjects is None):
                self.mplsldplsrobjects = MplsLdpStdMib.Mplsldplsrobjects()
                self.mplsldplsrobjects.parent = self
                self._children_name_map["mplsldplsrobjects"] = "mplsLdpLsrObjects"
            return self.mplsldplsrobjects

        if (child_yang_name == "mplsLdpPeerTable"):
            if (self.mplsldppeertable is None):
                self.mplsldppeertable = MplsLdpStdMib.Mplsldppeertable()
                self.mplsldppeertable.parent = self
                self._children_name_map["mplsldppeertable"] = "mplsLdpPeerTable"
            return self.mplsldppeertable

        if (child_yang_name == "mplsLdpSessionObjects"):
            if (self.mplsldpsessionobjects is None):
                self.mplsldpsessionobjects = MplsLdpStdMib.Mplsldpsessionobjects()
                self.mplsldpsessionobjects.parent = self
                self._children_name_map["mplsldpsessionobjects"] = "mplsLdpSessionObjects"
            return self.mplsldpsessionobjects

        if (child_yang_name == "mplsLdpSessionPeerAddrTable"):
            if (self.mplsldpsessionpeeraddrtable is None):
                self.mplsldpsessionpeeraddrtable = MplsLdpStdMib.Mplsldpsessionpeeraddrtable()
                self.mplsldpsessionpeeraddrtable.parent = self
                self._children_name_map["mplsldpsessionpeeraddrtable"] = "mplsLdpSessionPeerAddrTable"
            return self.mplsldpsessionpeeraddrtable

        if (child_yang_name == "mplsOutSegmentLdpLspTable"):
            if (self.mplsoutsegmentldplsptable is None):
                self.mplsoutsegmentldplsptable = MplsLdpStdMib.Mplsoutsegmentldplsptable()
                self.mplsoutsegmentldplsptable.parent = self
                self._children_name_map["mplsoutsegmentldplsptable"] = "mplsOutSegmentLdpLspTable"
            return self.mplsoutsegmentldplsptable

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "mplsFecObjects" or name == "mplsFecTable" or name == "mplsInSegmentLdpLspTable" or name == "mplsLdpEntityObjects" or name == "mplsLdpEntityTable" or name == "mplsLdpHelloAdjacencyTable" or name == "mplsLdpLspFecTable" or name == "mplsLdpLsrObjects" or name == "mplsLdpPeerTable" or name == "mplsLdpSessionObjects" or name == "mplsLdpSessionPeerAddrTable" or name == "mplsOutSegmentLdpLspTable"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = MplsLdpStdMib()
        return self._top_entity

