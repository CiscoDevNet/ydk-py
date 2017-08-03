""" MPLS_LSR_STD_MIB 

This MIB module contains managed object definitions for
the Multiprotocol Label Switching (MPLS) Router as
defined in\: Rosen, E., Viswanathan, A., and R.
Callon, Multiprotocol Label Switching Architecture,
RFC 3031, January 2001.

Copyright (C) The Internet Society (2004). The
initial version of this MIB module was published
in RFC 3812. For full legal notices see the RFC
itself or see\:
http\://www.ietf.org/copyrights/ianamib.html

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class MplsLsrStdMib(Entity):
    """
    
    
    .. attribute:: mplsinsegmentmaptable
    
    	This table specifies the mapping from the mplsInSegmentIndex to the corresponding mplsInSegmentInterface and mplsInSegmentLabel objects. The purpose of this table is to provide the manager with an alternative means by which to locate in\-segments
    	**type**\:   :py:class:`Mplsinsegmentmaptable <ydk.models.cisco_ios_xe.MPLS_LSR_STD_MIB.MplsLsrStdMib.Mplsinsegmentmaptable>`
    
    .. attribute:: mplsinsegmenttable
    
    	This table contains a description of the incoming MPLS segments (labels) to an LSR and their associated parameters. The index for this table is mplsInSegmentIndex. The index structure of this table is specifically designed to handle many different MPLS implementations that manage their labels both in a distributed and centralized manner. The table is also designed to handle existing MPLS labels as defined in RFC3031 as well as longer ones that may be necessary in the future.  In cases where the label cannot fit into the mplsInSegmentLabel object, the mplsInSegmentLabelPtr will indicate this by being set to the first accessible column in the appropriate extension table's row. In this case an additional table MUST be provided and MUST be indexed by at least the indexes used by this table. In all other cases when the label is represented within the mplsInSegmentLabel object, the mplsInSegmentLabelPtr MUST be set to 0.0. Due to the fact that MPLS labels may not exceed 24 bits, the mplsInSegmentLabelPtr object is only a provision for future\-proofing the MIB module. Thus, the definition of any extension tables is beyond the scope of this MIB module
    	**type**\:   :py:class:`Mplsinsegmenttable <ydk.models.cisco_ios_xe.MPLS_LSR_STD_MIB.MplsLsrStdMib.Mplsinsegmenttable>`
    
    .. attribute:: mplsinterfacetable
    
    	This table specifies per\-interface MPLS capability and associated information
    	**type**\:   :py:class:`Mplsinterfacetable <ydk.models.cisco_ios_xe.MPLS_LSR_STD_MIB.MplsLsrStdMib.Mplsinterfacetable>`
    
    .. attribute:: mplslabelstacktable
    
    	This table specifies the label stack to be pushed onto a packet, beneath the top label.  Entries into this table are referred to from mplsXCTable
    	**type**\:   :py:class:`Mplslabelstacktable <ydk.models.cisco_ios_xe.MPLS_LSR_STD_MIB.MplsLsrStdMib.Mplslabelstacktable>`
    
    .. attribute:: mplslsrobjects
    
    	
    	**type**\:   :py:class:`Mplslsrobjects <ydk.models.cisco_ios_xe.MPLS_LSR_STD_MIB.MplsLsrStdMib.Mplslsrobjects>`
    
    .. attribute:: mplsoutsegmenttable
    
    	This table contains a representation of the outgoing segments from an LSR
    	**type**\:   :py:class:`Mplsoutsegmenttable <ydk.models.cisco_ios_xe.MPLS_LSR_STD_MIB.MplsLsrStdMib.Mplsoutsegmenttable>`
    
    .. attribute:: mplsxctable
    
    	This table specifies information for switching between LSP segments.  It supports point\-to\-point, point\-to\-multipoint and multipoint\-to\-point connections.  mplsLabelStackTable specifies the label stack information for a cross\-connect LSR and is referred to from mplsXCTable
    	**type**\:   :py:class:`Mplsxctable <ydk.models.cisco_ios_xe.MPLS_LSR_STD_MIB.MplsLsrStdMib.Mplsxctable>`
    
    

    """

    _prefix = 'MPLS-LSR-STD-MIB'
    _revision = '2004-06-03'

    def __init__(self):
        super(MplsLsrStdMib, self).__init__()
        self._top_entity = None

        self.yang_name = "MPLS-LSR-STD-MIB"
        self.yang_parent_name = "MPLS-LSR-STD-MIB"

        self.mplsinsegmentmaptable = MplsLsrStdMib.Mplsinsegmentmaptable()
        self.mplsinsegmentmaptable.parent = self
        self._children_name_map["mplsinsegmentmaptable"] = "mplsInSegmentMapTable"
        self._children_yang_names.add("mplsInSegmentMapTable")

        self.mplsinsegmenttable = MplsLsrStdMib.Mplsinsegmenttable()
        self.mplsinsegmenttable.parent = self
        self._children_name_map["mplsinsegmenttable"] = "mplsInSegmentTable"
        self._children_yang_names.add("mplsInSegmentTable")

        self.mplsinterfacetable = MplsLsrStdMib.Mplsinterfacetable()
        self.mplsinterfacetable.parent = self
        self._children_name_map["mplsinterfacetable"] = "mplsInterfaceTable"
        self._children_yang_names.add("mplsInterfaceTable")

        self.mplslabelstacktable = MplsLsrStdMib.Mplslabelstacktable()
        self.mplslabelstacktable.parent = self
        self._children_name_map["mplslabelstacktable"] = "mplsLabelStackTable"
        self._children_yang_names.add("mplsLabelStackTable")

        self.mplslsrobjects = MplsLsrStdMib.Mplslsrobjects()
        self.mplslsrobjects.parent = self
        self._children_name_map["mplslsrobjects"] = "mplsLsrObjects"
        self._children_yang_names.add("mplsLsrObjects")

        self.mplsoutsegmenttable = MplsLsrStdMib.Mplsoutsegmenttable()
        self.mplsoutsegmenttable.parent = self
        self._children_name_map["mplsoutsegmenttable"] = "mplsOutSegmentTable"
        self._children_yang_names.add("mplsOutSegmentTable")

        self.mplsxctable = MplsLsrStdMib.Mplsxctable()
        self.mplsxctable.parent = self
        self._children_name_map["mplsxctable"] = "mplsXCTable"
        self._children_yang_names.add("mplsXCTable")


    class Mplslsrobjects(Entity):
        """
        
        
        .. attribute:: mplsinsegmentindexnext
        
        	This object contains the next available value to be used for mplsInSegmentIndex when creating entries in the mplsInSegmentTable. The special value of a string containing the single octet 0x00 indicates that no new entries can be created in this table. Agents not allowing managers to create entries in this table MUST set this object to this special value
        	**type**\:  str
        
        	**length:** 1..24
        
        .. attribute:: mplslabelstackindexnext
        
        	This object contains the next available value to be used for mplsLabelStackIndex when creating entries in the mplsLabelStackTable. The special string containing the single octet 0x00 indicates that no more new entries can be created in the relevant table.  Agents not allowing managers to create entries in this table MUST set this value to the string containing the single octet 0x00
        	**type**\:  str
        
        	**length:** 1..24
        
        .. attribute:: mplsmaxlabelstackdepth
        
        	The maximum stack depth supported by this LSR
        	**type**\:  int
        
        	**range:** 1..2147483647
        
        .. attribute:: mplsoutsegmentindexnext
        
        	This object contains the next available value to be used for mplsOutSegmentIndex when creating entries in the mplsOutSegmentTable. The special value of a string containing the single octet 0x00 indicates that no new entries can be created in this table. Agents not allowing managers to create entries in this table MUST set this object to this special value
        	**type**\:  str
        
        	**length:** 1..24
        
        .. attribute:: mplsxcindexnext
        
        	This object contains the next available value to be used for mplsXCIndex when creating entries in the mplsXCTable. A special value of the zero length string indicates that no more new entries can be created in the relevant table.  Agents not allowing managers to create entries in this table MUST set this value to the zero length string
        	**type**\:  str
        
        	**length:** 1..24
        
        .. attribute:: mplsxcnotificationsenable
        
        	If this object is set to true(1), then it enables the emission of mplsXCUp and mplsXCDown notifications; otherwise these notifications are not emitted
        	**type**\:  bool
        
        

        """

        _prefix = 'MPLS-LSR-STD-MIB'
        _revision = '2004-06-03'

        def __init__(self):
            super(MplsLsrStdMib.Mplslsrobjects, self).__init__()

            self.yang_name = "mplsLsrObjects"
            self.yang_parent_name = "MPLS-LSR-STD-MIB"

            self.mplsinsegmentindexnext = YLeaf(YType.str, "mplsInSegmentIndexNext")

            self.mplslabelstackindexnext = YLeaf(YType.str, "mplsLabelStackIndexNext")

            self.mplsmaxlabelstackdepth = YLeaf(YType.uint32, "mplsMaxLabelStackDepth")

            self.mplsoutsegmentindexnext = YLeaf(YType.str, "mplsOutSegmentIndexNext")

            self.mplsxcindexnext = YLeaf(YType.str, "mplsXCIndexNext")

            self.mplsxcnotificationsenable = YLeaf(YType.boolean, "mplsXCNotificationsEnable")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("mplsinsegmentindexnext",
                            "mplslabelstackindexnext",
                            "mplsmaxlabelstackdepth",
                            "mplsoutsegmentindexnext",
                            "mplsxcindexnext",
                            "mplsxcnotificationsenable") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(MplsLsrStdMib.Mplslsrobjects, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(MplsLsrStdMib.Mplslsrobjects, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.mplsinsegmentindexnext.is_set or
                self.mplslabelstackindexnext.is_set or
                self.mplsmaxlabelstackdepth.is_set or
                self.mplsoutsegmentindexnext.is_set or
                self.mplsxcindexnext.is_set or
                self.mplsxcnotificationsenable.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.mplsinsegmentindexnext.yfilter != YFilter.not_set or
                self.mplslabelstackindexnext.yfilter != YFilter.not_set or
                self.mplsmaxlabelstackdepth.yfilter != YFilter.not_set or
                self.mplsoutsegmentindexnext.yfilter != YFilter.not_set or
                self.mplsxcindexnext.yfilter != YFilter.not_set or
                self.mplsxcnotificationsenable.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "mplsLsrObjects" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "MPLS-LSR-STD-MIB:MPLS-LSR-STD-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.mplsinsegmentindexnext.is_set or self.mplsinsegmentindexnext.yfilter != YFilter.not_set):
                leaf_name_data.append(self.mplsinsegmentindexnext.get_name_leafdata())
            if (self.mplslabelstackindexnext.is_set or self.mplslabelstackindexnext.yfilter != YFilter.not_set):
                leaf_name_data.append(self.mplslabelstackindexnext.get_name_leafdata())
            if (self.mplsmaxlabelstackdepth.is_set or self.mplsmaxlabelstackdepth.yfilter != YFilter.not_set):
                leaf_name_data.append(self.mplsmaxlabelstackdepth.get_name_leafdata())
            if (self.mplsoutsegmentindexnext.is_set or self.mplsoutsegmentindexnext.yfilter != YFilter.not_set):
                leaf_name_data.append(self.mplsoutsegmentindexnext.get_name_leafdata())
            if (self.mplsxcindexnext.is_set or self.mplsxcindexnext.yfilter != YFilter.not_set):
                leaf_name_data.append(self.mplsxcindexnext.get_name_leafdata())
            if (self.mplsxcnotificationsenable.is_set or self.mplsxcnotificationsenable.yfilter != YFilter.not_set):
                leaf_name_data.append(self.mplsxcnotificationsenable.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "mplsInSegmentIndexNext" or name == "mplsLabelStackIndexNext" or name == "mplsMaxLabelStackDepth" or name == "mplsOutSegmentIndexNext" or name == "mplsXCIndexNext" or name == "mplsXCNotificationsEnable"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "mplsInSegmentIndexNext"):
                self.mplsinsegmentindexnext = value
                self.mplsinsegmentindexnext.value_namespace = name_space
                self.mplsinsegmentindexnext.value_namespace_prefix = name_space_prefix
            if(value_path == "mplsLabelStackIndexNext"):
                self.mplslabelstackindexnext = value
                self.mplslabelstackindexnext.value_namespace = name_space
                self.mplslabelstackindexnext.value_namespace_prefix = name_space_prefix
            if(value_path == "mplsMaxLabelStackDepth"):
                self.mplsmaxlabelstackdepth = value
                self.mplsmaxlabelstackdepth.value_namespace = name_space
                self.mplsmaxlabelstackdepth.value_namespace_prefix = name_space_prefix
            if(value_path == "mplsOutSegmentIndexNext"):
                self.mplsoutsegmentindexnext = value
                self.mplsoutsegmentindexnext.value_namespace = name_space
                self.mplsoutsegmentindexnext.value_namespace_prefix = name_space_prefix
            if(value_path == "mplsXCIndexNext"):
                self.mplsxcindexnext = value
                self.mplsxcindexnext.value_namespace = name_space
                self.mplsxcindexnext.value_namespace_prefix = name_space_prefix
            if(value_path == "mplsXCNotificationsEnable"):
                self.mplsxcnotificationsenable = value
                self.mplsxcnotificationsenable.value_namespace = name_space
                self.mplsxcnotificationsenable.value_namespace_prefix = name_space_prefix


    class Mplsinterfacetable(Entity):
        """
        This table specifies per\-interface MPLS capability
        and associated information.
        
        .. attribute:: mplsinterfaceentry
        
        	A conceptual row in this table is created automatically by an LSR for every interface capable of supporting MPLS and which is configured to do so. A conceptual row in this table will exist if and only if a corresponding entry in ifTable exists with ifType = mpls(166). If this associated entry in ifTable is operationally disabled (thus removing MPLS capabilities on that interface), the corresponding entry in this table MUST be deleted shortly thereafter. An conceptual row with index 0 is created if the LSR supports per\-platform labels. This conceptual row represents the per\-platform label space and contains parameters that apply to all interfaces that participate in the per\-platform label space. Other conceptual rows in this table represent MPLS interfaces that may participate in either the per\-platform or per\- interface label spaces, or both.  Implementations that either only support per\-platform labels, or have only them configured, may choose to return just the mplsInterfaceEntry of 0 and not return the other rows. This will greatly reduce the number of objects returned. Further information about label space participation of an interface is provided in the DESCRIPTION clause of mplsInterfaceLabelParticipationType
        	**type**\: list of    :py:class:`Mplsinterfaceentry <ydk.models.cisco_ios_xe.MPLS_LSR_STD_MIB.MplsLsrStdMib.Mplsinterfacetable.Mplsinterfaceentry>`
        
        

        """

        _prefix = 'MPLS-LSR-STD-MIB'
        _revision = '2004-06-03'

        def __init__(self):
            super(MplsLsrStdMib.Mplsinterfacetable, self).__init__()

            self.yang_name = "mplsInterfaceTable"
            self.yang_parent_name = "MPLS-LSR-STD-MIB"

            self.mplsinterfaceentry = YList(self)

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
                        super(MplsLsrStdMib.Mplsinterfacetable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(MplsLsrStdMib.Mplsinterfacetable, self).__setattr__(name, value)


        class Mplsinterfaceentry(Entity):
            """
            A conceptual row in this table is created
            automatically by an LSR for every interface capable
            of supporting MPLS and which is configured to do so.
            A conceptual row in this table will exist if and only if
            a corresponding entry in ifTable exists with ifType =
            mpls(166). If this associated entry in ifTable is
            operationally disabled (thus removing MPLS
            capabilities on that interface), the corresponding
            entry in this table MUST be deleted shortly thereafter.
            An conceptual row with index 0 is created if the LSR
            supports per\-platform labels. This conceptual row
            represents the per\-platform label space and contains
            parameters that apply to all interfaces that participate
            in the per\-platform label space. Other conceptual rows
            in this table represent MPLS interfaces that may
            participate in either the per\-platform or per\-
            interface label spaces, or both.  Implementations
            that either only support per\-platform labels,
            or have only them configured, may choose to return
            just the mplsInterfaceEntry of 0 and not return
            the other rows. This will greatly reduce the number
            of objects returned. Further information about label
            space participation of an interface is provided in
            the DESCRIPTION clause of
            mplsInterfaceLabelParticipationType.
            
            .. attribute:: mplsinterfaceindex  <key>
            
            	This is a unique index for an entry in the MplsInterfaceTable.  A non\-zero index for an entry indicates the ifIndex for the corresponding interface entry of the MPLS\-layer in the ifTable. The entry with index 0 represents the per\-platform label space and contains parameters that apply to all interfaces that participate in the per\-platform label space. Other entries defined in this table represent additional MPLS interfaces that may participate in either the per\-platform or per\-interface label spaces, or both
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: mplsinterfaceavailablebandwidth
            
            	This value indicates the total amount of available bandwidth available on this interface and is specified in kilobits per second (Kbps).  This value is calculated as the difference between the amount of bandwidth currently in use and that specified in mplsInterfaceTotalBandwidth.  This variable is not applicable when applied to the interface with index 0. When this value cannot be measured, this value should contain the nominal bandwidth
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplsinterfacelabelmaxin
            
            	This is the maximum value of an MPLS label that this LSR is willing to receive on this interface
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplsinterfacelabelmaxout
            
            	This is the maximum value of an MPLS label that this LSR is willing to send on this interface
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplsinterfacelabelminin
            
            	This is the minimum value of an MPLS label that this LSR is willing to receive on this interface
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplsinterfacelabelminout
            
            	This is the minimum value of an MPLS label that this LSR is willing to send on this interface
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplsinterfacelabelparticipationtype
            
            	If the value of the mplsInterfaceIndex for this entry is zero, then this entry corresponds to the per\-platform label space for all interfaces configured to use that label space. In this case the perPlatform(0) bit MUST be set; the perInterface(1) bit is meaningless and MUST be ignored.  The remainder of this description applies to entries with a non\-zero value of mplsInterfaceIndex.  If the perInterface(1) bit is set then the value of mplsInterfaceLabelMinIn, mplsInterfaceLabelMaxIn, mplsInterfaceLabelMinOut, and mplsInterfaceLabelMaxOut for this entry reflect the label ranges for this interface.  If only the perPlatform(0) bit is set, then the value of mplsInterfaceLabelMinIn, mplsInterfaceLabelMaxIn, mplsInterfaceLabelMinOut, and mplsInterfaceLabelMaxOut for this entry MUST be identical to the instance of these objects with index 0.  These objects may only vary from the entry with index 0 if both the perPlatform(0) and perInterface(1) bits are set.  In all cases, at a minimum one of the perPlatform(0) or perInterface(1) bits MUST be set to indicate that at least one label space is in use by this interface. In all cases, agents MUST ensure that label ranges are specified consistently and MUST return an inconsistentValue error when they do not
            	**type**\:   :py:class:`Mplsinterfacelabelparticipationtype <ydk.models.cisco_ios_xe.MPLS_LSR_STD_MIB.MplsLsrStdMib.Mplsinterfacetable.Mplsinterfaceentry.Mplsinterfacelabelparticipationtype>`
            
            .. attribute:: mplsinterfaceperfinlabellookupfailures
            
            	This object counts the number of labeled packets that have been received on this interface and which were discarded because there was no matching cross\- connect entry. This object MUST count on a per\- interface basis regardless of which label space the interface participates in
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplsinterfaceperfinlabelsinuse
            
            	This object counts the number of labels that are in use at this point in time on this interface in the incoming direction. If the interface participates in only the per\-platform label space, then the value of the instance of this object MUST be identical to the value of the instance with index 0. If the interface participates in the per\-interface label space, then the instance of this object MUST represent the number of per\-interface labels that are in use on this interface
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplsinterfaceperfoutfragmentedpkts
            
            	This object counts the number of outgoing MPLS packets that required fragmentation before transmission on this interface. This object MUST count on a per\-interface basis regardless of which label space the interface participates in
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplsinterfaceperfoutlabelsinuse
            
            	This object counts the number of top\-most labels in the outgoing label stacks that are in use at this point in time on this interface. This object MUST count on a per\-interface basis regardless of which label space the interface participates in
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplsinterfacetotalbandwidth
            
            	This value indicates the total amount of usable bandwidth on this interface and is specified in kilobits per second (Kbps).  This variable is not applicable when applied to the interface with index 0. When this value cannot be measured, this value should contain the nominal bandwidth
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: kilobits per second
            
            

            """

            _prefix = 'MPLS-LSR-STD-MIB'
            _revision = '2004-06-03'

            def __init__(self):
                super(MplsLsrStdMib.Mplsinterfacetable.Mplsinterfaceentry, self).__init__()

                self.yang_name = "mplsInterfaceEntry"
                self.yang_parent_name = "mplsInterfaceTable"

                self.mplsinterfaceindex = YLeaf(YType.int32, "mplsInterfaceIndex")

                self.mplsinterfaceavailablebandwidth = YLeaf(YType.uint32, "mplsInterfaceAvailableBandwidth")

                self.mplsinterfacelabelmaxin = YLeaf(YType.uint32, "mplsInterfaceLabelMaxIn")

                self.mplsinterfacelabelmaxout = YLeaf(YType.uint32, "mplsInterfaceLabelMaxOut")

                self.mplsinterfacelabelminin = YLeaf(YType.uint32, "mplsInterfaceLabelMinIn")

                self.mplsinterfacelabelminout = YLeaf(YType.uint32, "mplsInterfaceLabelMinOut")

                self.mplsinterfacelabelparticipationtype = YLeaf(YType.bits, "mplsInterfaceLabelParticipationType")

                self.mplsinterfaceperfinlabellookupfailures = YLeaf(YType.uint32, "mplsInterfacePerfInLabelLookupFailures")

                self.mplsinterfaceperfinlabelsinuse = YLeaf(YType.uint32, "mplsInterfacePerfInLabelsInUse")

                self.mplsinterfaceperfoutfragmentedpkts = YLeaf(YType.uint32, "mplsInterfacePerfOutFragmentedPkts")

                self.mplsinterfaceperfoutlabelsinuse = YLeaf(YType.uint32, "mplsInterfacePerfOutLabelsInUse")

                self.mplsinterfacetotalbandwidth = YLeaf(YType.uint32, "mplsInterfaceTotalBandwidth")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("mplsinterfaceindex",
                                "mplsinterfaceavailablebandwidth",
                                "mplsinterfacelabelmaxin",
                                "mplsinterfacelabelmaxout",
                                "mplsinterfacelabelminin",
                                "mplsinterfacelabelminout",
                                "mplsinterfacelabelparticipationtype",
                                "mplsinterfaceperfinlabellookupfailures",
                                "mplsinterfaceperfinlabelsinuse",
                                "mplsinterfaceperfoutfragmentedpkts",
                                "mplsinterfaceperfoutlabelsinuse",
                                "mplsinterfacetotalbandwidth") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(MplsLsrStdMib.Mplsinterfacetable.Mplsinterfaceentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(MplsLsrStdMib.Mplsinterfacetable.Mplsinterfaceentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.mplsinterfaceindex.is_set or
                    self.mplsinterfaceavailablebandwidth.is_set or
                    self.mplsinterfacelabelmaxin.is_set or
                    self.mplsinterfacelabelmaxout.is_set or
                    self.mplsinterfacelabelminin.is_set or
                    self.mplsinterfacelabelminout.is_set or
                    self.mplsinterfacelabelparticipationtype.is_set or
                    self.mplsinterfaceperfinlabellookupfailures.is_set or
                    self.mplsinterfaceperfinlabelsinuse.is_set or
                    self.mplsinterfaceperfoutfragmentedpkts.is_set or
                    self.mplsinterfaceperfoutlabelsinuse.is_set or
                    self.mplsinterfacetotalbandwidth.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.mplsinterfaceindex.yfilter != YFilter.not_set or
                    self.mplsinterfaceavailablebandwidth.yfilter != YFilter.not_set or
                    self.mplsinterfacelabelmaxin.yfilter != YFilter.not_set or
                    self.mplsinterfacelabelmaxout.yfilter != YFilter.not_set or
                    self.mplsinterfacelabelminin.yfilter != YFilter.not_set or
                    self.mplsinterfacelabelminout.yfilter != YFilter.not_set or
                    self.mplsinterfacelabelparticipationtype.yfilter != YFilter.not_set or
                    self.mplsinterfaceperfinlabellookupfailures.yfilter != YFilter.not_set or
                    self.mplsinterfaceperfinlabelsinuse.yfilter != YFilter.not_set or
                    self.mplsinterfaceperfoutfragmentedpkts.yfilter != YFilter.not_set or
                    self.mplsinterfaceperfoutlabelsinuse.yfilter != YFilter.not_set or
                    self.mplsinterfacetotalbandwidth.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "mplsInterfaceEntry" + "[mplsInterfaceIndex='" + self.mplsinterfaceindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "MPLS-LSR-STD-MIB:MPLS-LSR-STD-MIB/mplsInterfaceTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.mplsinterfaceindex.is_set or self.mplsinterfaceindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsinterfaceindex.get_name_leafdata())
                if (self.mplsinterfaceavailablebandwidth.is_set or self.mplsinterfaceavailablebandwidth.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsinterfaceavailablebandwidth.get_name_leafdata())
                if (self.mplsinterfacelabelmaxin.is_set or self.mplsinterfacelabelmaxin.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsinterfacelabelmaxin.get_name_leafdata())
                if (self.mplsinterfacelabelmaxout.is_set or self.mplsinterfacelabelmaxout.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsinterfacelabelmaxout.get_name_leafdata())
                if (self.mplsinterfacelabelminin.is_set or self.mplsinterfacelabelminin.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsinterfacelabelminin.get_name_leafdata())
                if (self.mplsinterfacelabelminout.is_set or self.mplsinterfacelabelminout.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsinterfacelabelminout.get_name_leafdata())
                if (self.mplsinterfacelabelparticipationtype.is_set or self.mplsinterfacelabelparticipationtype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsinterfacelabelparticipationtype.get_name_leafdata())
                if (self.mplsinterfaceperfinlabellookupfailures.is_set or self.mplsinterfaceperfinlabellookupfailures.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsinterfaceperfinlabellookupfailures.get_name_leafdata())
                if (self.mplsinterfaceperfinlabelsinuse.is_set or self.mplsinterfaceperfinlabelsinuse.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsinterfaceperfinlabelsinuse.get_name_leafdata())
                if (self.mplsinterfaceperfoutfragmentedpkts.is_set or self.mplsinterfaceperfoutfragmentedpkts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsinterfaceperfoutfragmentedpkts.get_name_leafdata())
                if (self.mplsinterfaceperfoutlabelsinuse.is_set or self.mplsinterfaceperfoutlabelsinuse.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsinterfaceperfoutlabelsinuse.get_name_leafdata())
                if (self.mplsinterfacetotalbandwidth.is_set or self.mplsinterfacetotalbandwidth.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsinterfacetotalbandwidth.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "mplsInterfaceIndex" or name == "mplsInterfaceAvailableBandwidth" or name == "mplsInterfaceLabelMaxIn" or name == "mplsInterfaceLabelMaxOut" or name == "mplsInterfaceLabelMinIn" or name == "mplsInterfaceLabelMinOut" or name == "mplsInterfaceLabelParticipationType" or name == "mplsInterfacePerfInLabelLookupFailures" or name == "mplsInterfacePerfInLabelsInUse" or name == "mplsInterfacePerfOutFragmentedPkts" or name == "mplsInterfacePerfOutLabelsInUse" or name == "mplsInterfaceTotalBandwidth"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "mplsInterfaceIndex"):
                    self.mplsinterfaceindex = value
                    self.mplsinterfaceindex.value_namespace = name_space
                    self.mplsinterfaceindex.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsInterfaceAvailableBandwidth"):
                    self.mplsinterfaceavailablebandwidth = value
                    self.mplsinterfaceavailablebandwidth.value_namespace = name_space
                    self.mplsinterfaceavailablebandwidth.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsInterfaceLabelMaxIn"):
                    self.mplsinterfacelabelmaxin = value
                    self.mplsinterfacelabelmaxin.value_namespace = name_space
                    self.mplsinterfacelabelmaxin.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsInterfaceLabelMaxOut"):
                    self.mplsinterfacelabelmaxout = value
                    self.mplsinterfacelabelmaxout.value_namespace = name_space
                    self.mplsinterfacelabelmaxout.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsInterfaceLabelMinIn"):
                    self.mplsinterfacelabelminin = value
                    self.mplsinterfacelabelminin.value_namespace = name_space
                    self.mplsinterfacelabelminin.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsInterfaceLabelMinOut"):
                    self.mplsinterfacelabelminout = value
                    self.mplsinterfacelabelminout.value_namespace = name_space
                    self.mplsinterfacelabelminout.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsInterfaceLabelParticipationType"):
                    self.mplsinterfacelabelparticipationtype[value] = True
                if(value_path == "mplsInterfacePerfInLabelLookupFailures"):
                    self.mplsinterfaceperfinlabellookupfailures = value
                    self.mplsinterfaceperfinlabellookupfailures.value_namespace = name_space
                    self.mplsinterfaceperfinlabellookupfailures.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsInterfacePerfInLabelsInUse"):
                    self.mplsinterfaceperfinlabelsinuse = value
                    self.mplsinterfaceperfinlabelsinuse.value_namespace = name_space
                    self.mplsinterfaceperfinlabelsinuse.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsInterfacePerfOutFragmentedPkts"):
                    self.mplsinterfaceperfoutfragmentedpkts = value
                    self.mplsinterfaceperfoutfragmentedpkts.value_namespace = name_space
                    self.mplsinterfaceperfoutfragmentedpkts.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsInterfacePerfOutLabelsInUse"):
                    self.mplsinterfaceperfoutlabelsinuse = value
                    self.mplsinterfaceperfoutlabelsinuse.value_namespace = name_space
                    self.mplsinterfaceperfoutlabelsinuse.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsInterfaceTotalBandwidth"):
                    self.mplsinterfacetotalbandwidth = value
                    self.mplsinterfacetotalbandwidth.value_namespace = name_space
                    self.mplsinterfacetotalbandwidth.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.mplsinterfaceentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.mplsinterfaceentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "mplsInterfaceTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "MPLS-LSR-STD-MIB:MPLS-LSR-STD-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "mplsInterfaceEntry"):
                for c in self.mplsinterfaceentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = MplsLsrStdMib.Mplsinterfacetable.Mplsinterfaceentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.mplsinterfaceentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "mplsInterfaceEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Mplsinsegmenttable(Entity):
        """
        This table contains a description of the incoming MPLS
        segments (labels) to an LSR and their associated parameters.
        The index for this table is mplsInSegmentIndex.
        The index structure of this table is specifically designed
        to handle many different MPLS implementations that manage
        their labels both in a distributed and centralized manner.
        The table is also designed to handle existing MPLS labels
        as defined in RFC3031 as well as longer ones that may
        be necessary in the future.
        
        In cases where the label cannot fit into the
        mplsInSegmentLabel object, the mplsInSegmentLabelPtr
        will indicate this by being set to the first accessible
        column in the appropriate extension table's row.
        In this case an additional table MUST
        be provided and MUST be indexed by at least the indexes
        used by this table. In all other cases when the label is
        represented within the mplsInSegmentLabel object, the
        mplsInSegmentLabelPtr MUST be set to 0.0. Due to the
        fact that MPLS labels may not exceed 24 bits, the
        mplsInSegmentLabelPtr object is only a provision for
        future\-proofing the MIB module. Thus, the definition
        of any extension tables is beyond the scope of this
        MIB module.
        
        .. attribute:: mplsinsegmententry
        
        	An entry in this table represents one incoming segment as is represented in an LSR's LFIB. An entry can be created by a network administrator or an SNMP agent, or an MPLS signaling protocol.  The creator of the entry is denoted by mplsInSegmentOwner. The value of mplsInSegmentRowStatus cannot be active(1) unless the ifTable entry corresponding to mplsInSegmentInterface exists.  An entry in this table must match any incoming packets, and indicates an instance of mplsXCEntry based on which forwarding and/or switching actions are taken
        	**type**\: list of    :py:class:`Mplsinsegmententry <ydk.models.cisco_ios_xe.MPLS_LSR_STD_MIB.MplsLsrStdMib.Mplsinsegmenttable.Mplsinsegmententry>`
        
        

        """

        _prefix = 'MPLS-LSR-STD-MIB'
        _revision = '2004-06-03'

        def __init__(self):
            super(MplsLsrStdMib.Mplsinsegmenttable, self).__init__()

            self.yang_name = "mplsInSegmentTable"
            self.yang_parent_name = "MPLS-LSR-STD-MIB"

            self.mplsinsegmententry = YList(self)

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
                        super(MplsLsrStdMib.Mplsinsegmenttable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(MplsLsrStdMib.Mplsinsegmenttable, self).__setattr__(name, value)


        class Mplsinsegmententry(Entity):
            """
            An entry in this table represents one incoming
            segment as is represented in an LSR's LFIB.
            An entry can be created by a network
            administrator or an SNMP agent, or an MPLS signaling
            protocol.  The creator of the entry is denoted by
            mplsInSegmentOwner.
            The value of mplsInSegmentRowStatus cannot be active(1)
            unless the ifTable entry corresponding to
            mplsInSegmentInterface exists.  An entry in this table
            must match any incoming packets, and indicates an
            instance of mplsXCEntry based on which forwarding
            and/or switching actions are taken.
            
            .. attribute:: mplsinsegmentindex  <key>
            
            	The index for this in\-segment. The string containing the single octet 0x00 MUST not be used as an index
            	**type**\:  str
            
            	**length:** 1..24
            
            .. attribute:: mplsinsegmentaddrfamily
            
            	The IANA address family [IANAFamily] of packets received on this segment, which is used at an egress LSR to deliver them to the appropriate layer 3 entity. A value of other(0) indicates that the family type is either unknown or undefined; this SHOULD NOT be used at an egress LSR. This object cannot be modified if mplsInSegmentRowStatus is active(1)
            	**type**\:   :py:class:`Addressfamilynumbers <ydk.models.cisco_ios_xe.IANA_ADDRESS_FAMILY_NUMBERS_MIB.Addressfamilynumbers>`
            
            .. attribute:: mplsinsegmentinterface
            
            	This object represents the interface index for the incoming MPLS interface.  A value of zero represents all interfaces participating in the per\-platform label space.  This may only be used in cases where the incoming interface and label are associated with the same mplsXCEntry. Specifically, given a label and any incoming interface pair from the per\-platform label space, the outgoing label/interface mapping remains the same. If this is not the case, then individual entries MUST exist that can then be mapped to unique mplsXCEntries
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: mplsinsegmentlabel
            
            	If the corresponding instance of mplsInSegmentLabelPtr is zeroDotZero then this object MUST contain the incoming label associated with this in\-segment. If not this object SHOULD be zero and MUST be ignored
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplsinsegmentlabelptr
            
            	If the label for this segment cannot be represented fully within the mplsInSegmentLabel object, this object MUST point to the first accessible column of a conceptual row in an external table containing the label.  In this case, the mplsInSegmentTopLabel object SHOULD be set to 0 and ignored. This object MUST be set to zeroDotZero otherwise
            	**type**\:  str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: mplsinsegmentnpop
            
            	The number of labels to pop from the incoming packet.  Normally only the top label is popped from the packet and used for all switching decisions for that packet.  This is indicated by setting this object to the default value of 1. If an LSR supports popping of more than one label, this object MUST be set to that number. This object cannot be modified if mplsInSegmentRowStatus is active(1)
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            .. attribute:: mplsinsegmentowner
            
            	Denotes the entity that created and is responsible for managing this segment
            	**type**\:   :py:class:`Mplsowner <ydk.models.cisco_ios_xe.MPLS_TC_STD_MIB.Mplsowner>`
            
            .. attribute:: mplsinsegmentperfdiscards
            
            	The number of labeled packets received on this in\- segment, which were chosen to be discarded even though no errors had been detected to prevent their being transmitted.  One possible reason for discarding such a labeled packet could be to free up buffer space
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplsinsegmentperfdiscontinuitytime
            
            	The value of sysUpTime on the most recent occasion at which any one or more of this segment's Counter32 or Counter64 suffered a discontinuity. If no such discontinuities have occurred since the last re\- initialization of the local management subsystem, then this object contains a zero value
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplsinsegmentperferrors
            
            	The number of errored packets received on this segment
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplsinsegmentperfhcoctets
            
            	The total number of octets received.  This is the 64 bit version of mplsInSegmentPerfOctets, if mplsInSegmentPerfHCOctets is supported according to the rules spelled out in RFC2863
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: mplsinsegmentperfoctets
            
            	This value represents the total number of octets received by this segment. It MUST be equal to the least significant 32 bits of mplsInSegmentPerfHCOctets if mplsInSegmentPerfHCOctets is supported according to the rules spelled out in RFC2863
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplsinsegmentperfpackets
            
            	Total number of packets received by this segment
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplsinsegmentrowstatus
            
            	This variable is used to create, modify, and/or delete a row in this table. When a row in this table has a row in the active(1) state, no objects in this row can be modified except the mplsInSegmentRowStatus and mplsInSegmentStorageType
            	**type**\:   :py:class:`Rowstatus <ydk.models.cisco_ios_xe.SNMPv2_TC.Rowstatus>`
            
            .. attribute:: mplsinsegmentstoragetype
            
            	This variable indicates the storage type for this object. The agent MUST ensure that this object's value remains consistent with the associated mplsXCEntry. Conceptual rows having the value 'permanent' need not allow write\-access to any columnar objects in the row
            	**type**\:   :py:class:`Storagetype <ydk.models.cisco_ios_xe.SNMPv2_TC.Storagetype>`
            
            .. attribute:: mplsinsegmenttrafficparamptr
            
            	This variable represents a pointer to the traffic parameter specification for this in\-segment.  This value may point at an entry in the mplsTunnelResourceTable in the MPLS\-TE\-STD\-MIB (RFC3812) to indicate which traffic parameter settings for this segment if it represents an LSP used for a TE tunnel.  This value may optionally point at an externally defined traffic parameter specification table.  A value of zeroDotZero indicates best\-effort treatment.  By having the same value of this object, two or more segments can indicate resource sharing of such things as LSP queue space, etc.  This object cannot be modified if mplsInSegmentRowStatus is active(1).  For entries in this table that are preserved after a re\-boot, the agent MUST ensure that their integrity be preserved, or this object should be set to 0.0 if it cannot
            	**type**\:  str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: mplsinsegmentxcindex
            
            	Index into mplsXCTable which identifies which cross\- connect entry this segment is part of.  The string containing the single octet 0x00 indicates that this entry is not referred to by any cross\-connect entry. When a cross\-connect entry is created which this in\-segment is a part of, this object is automatically updated to reflect the value of mplsXCIndex of that cross\-connect entry
            	**type**\:  str
            
            	**length:** 1..24
            
            

            """

            _prefix = 'MPLS-LSR-STD-MIB'
            _revision = '2004-06-03'

            def __init__(self):
                super(MplsLsrStdMib.Mplsinsegmenttable.Mplsinsegmententry, self).__init__()

                self.yang_name = "mplsInSegmentEntry"
                self.yang_parent_name = "mplsInSegmentTable"

                self.mplsinsegmentindex = YLeaf(YType.str, "mplsInSegmentIndex")

                self.mplsinsegmentaddrfamily = YLeaf(YType.enumeration, "mplsInSegmentAddrFamily")

                self.mplsinsegmentinterface = YLeaf(YType.int32, "mplsInSegmentInterface")

                self.mplsinsegmentlabel = YLeaf(YType.uint32, "mplsInSegmentLabel")

                self.mplsinsegmentlabelptr = YLeaf(YType.str, "mplsInSegmentLabelPtr")

                self.mplsinsegmentnpop = YLeaf(YType.int32, "mplsInSegmentNPop")

                self.mplsinsegmentowner = YLeaf(YType.enumeration, "mplsInSegmentOwner")

                self.mplsinsegmentperfdiscards = YLeaf(YType.uint32, "mplsInSegmentPerfDiscards")

                self.mplsinsegmentperfdiscontinuitytime = YLeaf(YType.uint32, "mplsInSegmentPerfDiscontinuityTime")

                self.mplsinsegmentperferrors = YLeaf(YType.uint32, "mplsInSegmentPerfErrors")

                self.mplsinsegmentperfhcoctets = YLeaf(YType.uint64, "mplsInSegmentPerfHCOctets")

                self.mplsinsegmentperfoctets = YLeaf(YType.uint32, "mplsInSegmentPerfOctets")

                self.mplsinsegmentperfpackets = YLeaf(YType.uint32, "mplsInSegmentPerfPackets")

                self.mplsinsegmentrowstatus = YLeaf(YType.enumeration, "mplsInSegmentRowStatus")

                self.mplsinsegmentstoragetype = YLeaf(YType.enumeration, "mplsInSegmentStorageType")

                self.mplsinsegmenttrafficparamptr = YLeaf(YType.str, "mplsInSegmentTrafficParamPtr")

                self.mplsinsegmentxcindex = YLeaf(YType.str, "mplsInSegmentXCIndex")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("mplsinsegmentindex",
                                "mplsinsegmentaddrfamily",
                                "mplsinsegmentinterface",
                                "mplsinsegmentlabel",
                                "mplsinsegmentlabelptr",
                                "mplsinsegmentnpop",
                                "mplsinsegmentowner",
                                "mplsinsegmentperfdiscards",
                                "mplsinsegmentperfdiscontinuitytime",
                                "mplsinsegmentperferrors",
                                "mplsinsegmentperfhcoctets",
                                "mplsinsegmentperfoctets",
                                "mplsinsegmentperfpackets",
                                "mplsinsegmentrowstatus",
                                "mplsinsegmentstoragetype",
                                "mplsinsegmenttrafficparamptr",
                                "mplsinsegmentxcindex") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(MplsLsrStdMib.Mplsinsegmenttable.Mplsinsegmententry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(MplsLsrStdMib.Mplsinsegmenttable.Mplsinsegmententry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.mplsinsegmentindex.is_set or
                    self.mplsinsegmentaddrfamily.is_set or
                    self.mplsinsegmentinterface.is_set or
                    self.mplsinsegmentlabel.is_set or
                    self.mplsinsegmentlabelptr.is_set or
                    self.mplsinsegmentnpop.is_set or
                    self.mplsinsegmentowner.is_set or
                    self.mplsinsegmentperfdiscards.is_set or
                    self.mplsinsegmentperfdiscontinuitytime.is_set or
                    self.mplsinsegmentperferrors.is_set or
                    self.mplsinsegmentperfhcoctets.is_set or
                    self.mplsinsegmentperfoctets.is_set or
                    self.mplsinsegmentperfpackets.is_set or
                    self.mplsinsegmentrowstatus.is_set or
                    self.mplsinsegmentstoragetype.is_set or
                    self.mplsinsegmenttrafficparamptr.is_set or
                    self.mplsinsegmentxcindex.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.mplsinsegmentindex.yfilter != YFilter.not_set or
                    self.mplsinsegmentaddrfamily.yfilter != YFilter.not_set or
                    self.mplsinsegmentinterface.yfilter != YFilter.not_set or
                    self.mplsinsegmentlabel.yfilter != YFilter.not_set or
                    self.mplsinsegmentlabelptr.yfilter != YFilter.not_set or
                    self.mplsinsegmentnpop.yfilter != YFilter.not_set or
                    self.mplsinsegmentowner.yfilter != YFilter.not_set or
                    self.mplsinsegmentperfdiscards.yfilter != YFilter.not_set or
                    self.mplsinsegmentperfdiscontinuitytime.yfilter != YFilter.not_set or
                    self.mplsinsegmentperferrors.yfilter != YFilter.not_set or
                    self.mplsinsegmentperfhcoctets.yfilter != YFilter.not_set or
                    self.mplsinsegmentperfoctets.yfilter != YFilter.not_set or
                    self.mplsinsegmentperfpackets.yfilter != YFilter.not_set or
                    self.mplsinsegmentrowstatus.yfilter != YFilter.not_set or
                    self.mplsinsegmentstoragetype.yfilter != YFilter.not_set or
                    self.mplsinsegmenttrafficparamptr.yfilter != YFilter.not_set or
                    self.mplsinsegmentxcindex.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "mplsInSegmentEntry" + "[mplsInSegmentIndex='" + self.mplsinsegmentindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "MPLS-LSR-STD-MIB:MPLS-LSR-STD-MIB/mplsInSegmentTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.mplsinsegmentindex.is_set or self.mplsinsegmentindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsinsegmentindex.get_name_leafdata())
                if (self.mplsinsegmentaddrfamily.is_set or self.mplsinsegmentaddrfamily.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsinsegmentaddrfamily.get_name_leafdata())
                if (self.mplsinsegmentinterface.is_set or self.mplsinsegmentinterface.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsinsegmentinterface.get_name_leafdata())
                if (self.mplsinsegmentlabel.is_set or self.mplsinsegmentlabel.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsinsegmentlabel.get_name_leafdata())
                if (self.mplsinsegmentlabelptr.is_set or self.mplsinsegmentlabelptr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsinsegmentlabelptr.get_name_leafdata())
                if (self.mplsinsegmentnpop.is_set or self.mplsinsegmentnpop.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsinsegmentnpop.get_name_leafdata())
                if (self.mplsinsegmentowner.is_set or self.mplsinsegmentowner.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsinsegmentowner.get_name_leafdata())
                if (self.mplsinsegmentperfdiscards.is_set or self.mplsinsegmentperfdiscards.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsinsegmentperfdiscards.get_name_leafdata())
                if (self.mplsinsegmentperfdiscontinuitytime.is_set or self.mplsinsegmentperfdiscontinuitytime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsinsegmentperfdiscontinuitytime.get_name_leafdata())
                if (self.mplsinsegmentperferrors.is_set or self.mplsinsegmentperferrors.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsinsegmentperferrors.get_name_leafdata())
                if (self.mplsinsegmentperfhcoctets.is_set or self.mplsinsegmentperfhcoctets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsinsegmentperfhcoctets.get_name_leafdata())
                if (self.mplsinsegmentperfoctets.is_set or self.mplsinsegmentperfoctets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsinsegmentperfoctets.get_name_leafdata())
                if (self.mplsinsegmentperfpackets.is_set or self.mplsinsegmentperfpackets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsinsegmentperfpackets.get_name_leafdata())
                if (self.mplsinsegmentrowstatus.is_set or self.mplsinsegmentrowstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsinsegmentrowstatus.get_name_leafdata())
                if (self.mplsinsegmentstoragetype.is_set or self.mplsinsegmentstoragetype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsinsegmentstoragetype.get_name_leafdata())
                if (self.mplsinsegmenttrafficparamptr.is_set or self.mplsinsegmenttrafficparamptr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsinsegmenttrafficparamptr.get_name_leafdata())
                if (self.mplsinsegmentxcindex.is_set or self.mplsinsegmentxcindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsinsegmentxcindex.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "mplsInSegmentIndex" or name == "mplsInSegmentAddrFamily" or name == "mplsInSegmentInterface" or name == "mplsInSegmentLabel" or name == "mplsInSegmentLabelPtr" or name == "mplsInSegmentNPop" or name == "mplsInSegmentOwner" or name == "mplsInSegmentPerfDiscards" or name == "mplsInSegmentPerfDiscontinuityTime" or name == "mplsInSegmentPerfErrors" or name == "mplsInSegmentPerfHCOctets" or name == "mplsInSegmentPerfOctets" or name == "mplsInSegmentPerfPackets" or name == "mplsInSegmentRowStatus" or name == "mplsInSegmentStorageType" or name == "mplsInSegmentTrafficParamPtr" or name == "mplsInSegmentXCIndex"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "mplsInSegmentIndex"):
                    self.mplsinsegmentindex = value
                    self.mplsinsegmentindex.value_namespace = name_space
                    self.mplsinsegmentindex.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsInSegmentAddrFamily"):
                    self.mplsinsegmentaddrfamily = value
                    self.mplsinsegmentaddrfamily.value_namespace = name_space
                    self.mplsinsegmentaddrfamily.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsInSegmentInterface"):
                    self.mplsinsegmentinterface = value
                    self.mplsinsegmentinterface.value_namespace = name_space
                    self.mplsinsegmentinterface.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsInSegmentLabel"):
                    self.mplsinsegmentlabel = value
                    self.mplsinsegmentlabel.value_namespace = name_space
                    self.mplsinsegmentlabel.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsInSegmentLabelPtr"):
                    self.mplsinsegmentlabelptr = value
                    self.mplsinsegmentlabelptr.value_namespace = name_space
                    self.mplsinsegmentlabelptr.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsInSegmentNPop"):
                    self.mplsinsegmentnpop = value
                    self.mplsinsegmentnpop.value_namespace = name_space
                    self.mplsinsegmentnpop.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsInSegmentOwner"):
                    self.mplsinsegmentowner = value
                    self.mplsinsegmentowner.value_namespace = name_space
                    self.mplsinsegmentowner.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsInSegmentPerfDiscards"):
                    self.mplsinsegmentperfdiscards = value
                    self.mplsinsegmentperfdiscards.value_namespace = name_space
                    self.mplsinsegmentperfdiscards.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsInSegmentPerfDiscontinuityTime"):
                    self.mplsinsegmentperfdiscontinuitytime = value
                    self.mplsinsegmentperfdiscontinuitytime.value_namespace = name_space
                    self.mplsinsegmentperfdiscontinuitytime.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsInSegmentPerfErrors"):
                    self.mplsinsegmentperferrors = value
                    self.mplsinsegmentperferrors.value_namespace = name_space
                    self.mplsinsegmentperferrors.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsInSegmentPerfHCOctets"):
                    self.mplsinsegmentperfhcoctets = value
                    self.mplsinsegmentperfhcoctets.value_namespace = name_space
                    self.mplsinsegmentperfhcoctets.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsInSegmentPerfOctets"):
                    self.mplsinsegmentperfoctets = value
                    self.mplsinsegmentperfoctets.value_namespace = name_space
                    self.mplsinsegmentperfoctets.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsInSegmentPerfPackets"):
                    self.mplsinsegmentperfpackets = value
                    self.mplsinsegmentperfpackets.value_namespace = name_space
                    self.mplsinsegmentperfpackets.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsInSegmentRowStatus"):
                    self.mplsinsegmentrowstatus = value
                    self.mplsinsegmentrowstatus.value_namespace = name_space
                    self.mplsinsegmentrowstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsInSegmentStorageType"):
                    self.mplsinsegmentstoragetype = value
                    self.mplsinsegmentstoragetype.value_namespace = name_space
                    self.mplsinsegmentstoragetype.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsInSegmentTrafficParamPtr"):
                    self.mplsinsegmenttrafficparamptr = value
                    self.mplsinsegmenttrafficparamptr.value_namespace = name_space
                    self.mplsinsegmenttrafficparamptr.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsInSegmentXCIndex"):
                    self.mplsinsegmentxcindex = value
                    self.mplsinsegmentxcindex.value_namespace = name_space
                    self.mplsinsegmentxcindex.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.mplsinsegmententry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.mplsinsegmententry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "mplsInSegmentTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "MPLS-LSR-STD-MIB:MPLS-LSR-STD-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "mplsInSegmentEntry"):
                for c in self.mplsinsegmententry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = MplsLsrStdMib.Mplsinsegmenttable.Mplsinsegmententry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.mplsinsegmententry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "mplsInSegmentEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Mplsoutsegmenttable(Entity):
        """
        This table contains a representation of the outgoing
        segments from an LSR.
        
        .. attribute:: mplsoutsegmententry
        
        	An entry in this table represents one outgoing segment.  An entry can be created by a network administrator, an SNMP agent, or an MPLS signaling protocol.  The object mplsOutSegmentOwner indicates the creator of this entry. The value of mplsOutSegmentRowStatus cannot be active(1) unless the ifTable entry corresponding to mplsOutSegmentInterface exists.  Note that the indexing of this table uses a single, arbitrary index (mplsOutSegmentIndex) to indicate which out\-segment (i.e.\: label) is being switched to from which in\-segment (i.e\: label) or in\-segments. This is necessary because it is possible to have an equal\-cost multi\-path situation where two identical out\-going labels are assigned to the same cross\-connect (i.e.\: they go to two different neighboring LSRs); thus, requiring two out\-segments. In order to preserve the uniqueness of the references by the mplsXCEntry, an arbitrary integer must be used as the index for this table
        	**type**\: list of    :py:class:`Mplsoutsegmententry <ydk.models.cisco_ios_xe.MPLS_LSR_STD_MIB.MplsLsrStdMib.Mplsoutsegmenttable.Mplsoutsegmententry>`
        
        

        """

        _prefix = 'MPLS-LSR-STD-MIB'
        _revision = '2004-06-03'

        def __init__(self):
            super(MplsLsrStdMib.Mplsoutsegmenttable, self).__init__()

            self.yang_name = "mplsOutSegmentTable"
            self.yang_parent_name = "MPLS-LSR-STD-MIB"

            self.mplsoutsegmententry = YList(self)

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
                        super(MplsLsrStdMib.Mplsoutsegmenttable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(MplsLsrStdMib.Mplsoutsegmenttable, self).__setattr__(name, value)


        class Mplsoutsegmententry(Entity):
            """
            An entry in this table represents one outgoing
            segment.  An entry can be created by a network
            administrator, an SNMP agent, or an MPLS signaling
            protocol.  The object mplsOutSegmentOwner indicates
            the creator of this entry. The value of
            mplsOutSegmentRowStatus cannot be active(1) unless
            the ifTable entry corresponding to
            mplsOutSegmentInterface exists.
            
            Note that the indexing of this table uses a single,
            arbitrary index (mplsOutSegmentIndex) to indicate
            which out\-segment (i.e.\: label) is being switched to
            from which in\-segment (i.e\: label) or in\-segments.
            This is necessary because it is possible to have an
            equal\-cost multi\-path situation where two identical
            out\-going labels are assigned to the same
            cross\-connect (i.e.\: they go to two different neighboring
            LSRs); thus, requiring two out\-segments. In order to
            preserve the uniqueness of the references
            by the mplsXCEntry, an arbitrary integer must be used as
            the index for this table.
            
            .. attribute:: mplsoutsegmentindex  <key>
            
            	This value contains a unique index for this row. While a value of a string containing the single octet 0x00 is not valid as an index for entries in this table, it can be supplied as a valid value to index the mplsXCTable to represent entries for which no out\-segment has been configured or exists
            	**type**\:  str
            
            	**length:** 1..24
            
            .. attribute:: mplsoutsegmentinterface
            
            	This value must contain the interface index of the outgoing interface. This object cannot be modified if mplsOutSegmentRowStatus is active(1). The mplsOutSegmentRowStatus cannot be set to active(1) until this object is set to a value corresponding to a valid ifEntry
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: mplsoutsegmentnexthopaddr
            
            	The internet address of the next hop. The type of this address is determined by the value of the mplslOutSegmentNextHopAddrType object.  This object cannot be modified if mplsOutSegmentRowStatus is active(1)
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: mplsoutsegmentnexthopaddrtype
            
            	Indicates the next hop Internet address type. Only values unknown(0), ipv4(1) or ipv6(2) have to be supported.  A value of unknown(0) is allowed only when the outgoing interface is of type point\-to\-point. If any other unsupported values are attempted in a set operation, the agent MUST return an inconsistentValue error
            	**type**\:   :py:class:`Inetaddresstype <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.Inetaddresstype>`
            
            .. attribute:: mplsoutsegmentowner
            
            	Denotes the entity which created and is responsible for managing this segment
            	**type**\:   :py:class:`Mplsowner <ydk.models.cisco_ios_xe.MPLS_TC_STD_MIB.Mplsowner>`
            
            .. attribute:: mplsoutsegmentperfdiscards
            
            	The number of labeled packets attempted to be transmitted on this out\-segment, which were chosen to be discarded even though no errors had been detected to prevent their being transmitted. One possible reason for discarding such a labeled packet could be to free up buffer space
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplsoutsegmentperfdiscontinuitytime
            
            	The value of sysUpTime on the most recent occasion at which any one or more of this segment's Counter32 or Counter64 suffered a discontinuity. If no such discontinuities have occurred since the last re\- initialization of the local management subsystem, then this object contains a zero value
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplsoutsegmentperferrors
            
            	Number of packets that could not be sent due to errors on this segment
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplsoutsegmentperfhcoctets
            
            	Total number of octets sent.  This is the 64 bit version of mplsOutSegmentPerfOctets, if mplsOutSegmentPerfHCOctets is supported according to the rules spelled out in RFC2863
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: mplsoutsegmentperfoctets
            
            	This value contains the total number of octets sent on this segment. It MUST be equal to the least significant 32 bits of mplsOutSegmentPerfHCOctets if mplsOutSegmentPerfHCOctets is supported according to the rules spelled out in RFC2863
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplsoutsegmentperfpackets
            
            	This value contains the total number of packets sent on this segment
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplsoutsegmentpushtoplabel
            
            	This value indicates whether or not a top label should be pushed onto the outgoing packet's label stack.  The value of this variable MUST be set to true(1) if the outgoing interface does not support pop\-and\-go (and no label stack remains). For example, on ATM interface, or if the segment represents a tunnel origination.  Note that it is considered an error in the case that mplsOutSegmentPushTopLabel is set to false, but the cross\-connect entry which refers to this out\-segment has a non\-zero mplsLabelStackIndex.  The LSR MUST ensure that this situation does not happen. This object cannot be modified if mplsOutSegmentRowStatus is active(1)
            	**type**\:  bool
            
            .. attribute:: mplsoutsegmentrowstatus
            
            	For creating, modifying, and deleting this row. When a row in this table has a row in the active(1) state, no objects in this row can be modified except the mplsOutSegmentRowStatus or mplsOutSegmentStorageType
            	**type**\:   :py:class:`Rowstatus <ydk.models.cisco_ios_xe.SNMPv2_TC.Rowstatus>`
            
            .. attribute:: mplsoutsegmentstoragetype
            
            	This variable indicates the storage type for this object. The agent MUST ensure that this object's value remains consistent with the associated mplsXCEntry. Conceptual rows having the value 'permanent' need not allow write\-access to any columnar objects in the row
            	**type**\:   :py:class:`Storagetype <ydk.models.cisco_ios_xe.SNMPv2_TC.Storagetype>`
            
            .. attribute:: mplsoutsegmenttoplabel
            
            	If mplsOutSegmentPushTopLabel is true then this represents the label that should be pushed onto the top of the outgoing packet's label stack. Otherwise this value SHOULD be set to 0 by the management station and MUST be ignored by the agent. This object cannot be modified if mplsOutSegmentRowStatus is active(1)
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplsoutsegmenttoplabelptr
            
            	If the label for this segment cannot be represented fully within the mplsOutSegmentLabel object, this object MUST point to the first accessible column of a conceptual row in an external table containing the label.  In this case, the mplsOutSegmentTopLabel object SHOULD be set to 0 and ignored. This object MUST be set to zeroDotZero otherwise
            	**type**\:  str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: mplsoutsegmenttrafficparamptr
            
            	This variable represents a pointer to the traffic parameter specification for this out\-segment.  This value may point at an entry in the MplsTunnelResourceEntry in the MPLS\-TE\-STD\-MIB (RFC3812)  RFC Editor\: Please fill in RFC number.  to indicate which traffic parameter settings for this segment if it represents an LSP used for a TE tunnel.  This value may optionally point at an externally defined traffic parameter specification table.  A value of zeroDotZero indicates best\-effort treatment.  By having the same value of this object, two or more segments can indicate resource sharing of such things as LSP queue space, etc.  This object cannot be modified if mplsOutSegmentRowStatus is active(1). For entries in this table that are preserved after a re\-boot, the agent MUST ensure that their integrity be preserved, or this object should be set to 0.0 if it cannot
            	**type**\:  str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: mplsoutsegmentxcindex
            
            	Index into mplsXCTable which identifies which cross\- connect entry this segment is part of.  A value of the string containing the single octet 0x00 indicates that this entry is not referred to by any cross\-connect entry.  When a cross\-connect entry is created which this out\-segment is a part of, this object MUST be updated by the agent to reflect the value of mplsXCIndex of that cross\-connect entry
            	**type**\:  str
            
            	**length:** 1..24
            
            

            """

            _prefix = 'MPLS-LSR-STD-MIB'
            _revision = '2004-06-03'

            def __init__(self):
                super(MplsLsrStdMib.Mplsoutsegmenttable.Mplsoutsegmententry, self).__init__()

                self.yang_name = "mplsOutSegmentEntry"
                self.yang_parent_name = "mplsOutSegmentTable"

                self.mplsoutsegmentindex = YLeaf(YType.str, "mplsOutSegmentIndex")

                self.mplsoutsegmentinterface = YLeaf(YType.int32, "mplsOutSegmentInterface")

                self.mplsoutsegmentnexthopaddr = YLeaf(YType.str, "mplsOutSegmentNextHopAddr")

                self.mplsoutsegmentnexthopaddrtype = YLeaf(YType.enumeration, "mplsOutSegmentNextHopAddrType")

                self.mplsoutsegmentowner = YLeaf(YType.enumeration, "mplsOutSegmentOwner")

                self.mplsoutsegmentperfdiscards = YLeaf(YType.uint32, "mplsOutSegmentPerfDiscards")

                self.mplsoutsegmentperfdiscontinuitytime = YLeaf(YType.uint32, "mplsOutSegmentPerfDiscontinuityTime")

                self.mplsoutsegmentperferrors = YLeaf(YType.uint32, "mplsOutSegmentPerfErrors")

                self.mplsoutsegmentperfhcoctets = YLeaf(YType.uint64, "mplsOutSegmentPerfHCOctets")

                self.mplsoutsegmentperfoctets = YLeaf(YType.uint32, "mplsOutSegmentPerfOctets")

                self.mplsoutsegmentperfpackets = YLeaf(YType.uint32, "mplsOutSegmentPerfPackets")

                self.mplsoutsegmentpushtoplabel = YLeaf(YType.boolean, "mplsOutSegmentPushTopLabel")

                self.mplsoutsegmentrowstatus = YLeaf(YType.enumeration, "mplsOutSegmentRowStatus")

                self.mplsoutsegmentstoragetype = YLeaf(YType.enumeration, "mplsOutSegmentStorageType")

                self.mplsoutsegmenttoplabel = YLeaf(YType.uint32, "mplsOutSegmentTopLabel")

                self.mplsoutsegmenttoplabelptr = YLeaf(YType.str, "mplsOutSegmentTopLabelPtr")

                self.mplsoutsegmenttrafficparamptr = YLeaf(YType.str, "mplsOutSegmentTrafficParamPtr")

                self.mplsoutsegmentxcindex = YLeaf(YType.str, "mplsOutSegmentXCIndex")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("mplsoutsegmentindex",
                                "mplsoutsegmentinterface",
                                "mplsoutsegmentnexthopaddr",
                                "mplsoutsegmentnexthopaddrtype",
                                "mplsoutsegmentowner",
                                "mplsoutsegmentperfdiscards",
                                "mplsoutsegmentperfdiscontinuitytime",
                                "mplsoutsegmentperferrors",
                                "mplsoutsegmentperfhcoctets",
                                "mplsoutsegmentperfoctets",
                                "mplsoutsegmentperfpackets",
                                "mplsoutsegmentpushtoplabel",
                                "mplsoutsegmentrowstatus",
                                "mplsoutsegmentstoragetype",
                                "mplsoutsegmenttoplabel",
                                "mplsoutsegmenttoplabelptr",
                                "mplsoutsegmenttrafficparamptr",
                                "mplsoutsegmentxcindex") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(MplsLsrStdMib.Mplsoutsegmenttable.Mplsoutsegmententry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(MplsLsrStdMib.Mplsoutsegmenttable.Mplsoutsegmententry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.mplsoutsegmentindex.is_set or
                    self.mplsoutsegmentinterface.is_set or
                    self.mplsoutsegmentnexthopaddr.is_set or
                    self.mplsoutsegmentnexthopaddrtype.is_set or
                    self.mplsoutsegmentowner.is_set or
                    self.mplsoutsegmentperfdiscards.is_set or
                    self.mplsoutsegmentperfdiscontinuitytime.is_set or
                    self.mplsoutsegmentperferrors.is_set or
                    self.mplsoutsegmentperfhcoctets.is_set or
                    self.mplsoutsegmentperfoctets.is_set or
                    self.mplsoutsegmentperfpackets.is_set or
                    self.mplsoutsegmentpushtoplabel.is_set or
                    self.mplsoutsegmentrowstatus.is_set or
                    self.mplsoutsegmentstoragetype.is_set or
                    self.mplsoutsegmenttoplabel.is_set or
                    self.mplsoutsegmenttoplabelptr.is_set or
                    self.mplsoutsegmenttrafficparamptr.is_set or
                    self.mplsoutsegmentxcindex.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.mplsoutsegmentindex.yfilter != YFilter.not_set or
                    self.mplsoutsegmentinterface.yfilter != YFilter.not_set or
                    self.mplsoutsegmentnexthopaddr.yfilter != YFilter.not_set or
                    self.mplsoutsegmentnexthopaddrtype.yfilter != YFilter.not_set or
                    self.mplsoutsegmentowner.yfilter != YFilter.not_set or
                    self.mplsoutsegmentperfdiscards.yfilter != YFilter.not_set or
                    self.mplsoutsegmentperfdiscontinuitytime.yfilter != YFilter.not_set or
                    self.mplsoutsegmentperferrors.yfilter != YFilter.not_set or
                    self.mplsoutsegmentperfhcoctets.yfilter != YFilter.not_set or
                    self.mplsoutsegmentperfoctets.yfilter != YFilter.not_set or
                    self.mplsoutsegmentperfpackets.yfilter != YFilter.not_set or
                    self.mplsoutsegmentpushtoplabel.yfilter != YFilter.not_set or
                    self.mplsoutsegmentrowstatus.yfilter != YFilter.not_set or
                    self.mplsoutsegmentstoragetype.yfilter != YFilter.not_set or
                    self.mplsoutsegmenttoplabel.yfilter != YFilter.not_set or
                    self.mplsoutsegmenttoplabelptr.yfilter != YFilter.not_set or
                    self.mplsoutsegmenttrafficparamptr.yfilter != YFilter.not_set or
                    self.mplsoutsegmentxcindex.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "mplsOutSegmentEntry" + "[mplsOutSegmentIndex='" + self.mplsoutsegmentindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "MPLS-LSR-STD-MIB:MPLS-LSR-STD-MIB/mplsOutSegmentTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.mplsoutsegmentindex.is_set or self.mplsoutsegmentindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsoutsegmentindex.get_name_leafdata())
                if (self.mplsoutsegmentinterface.is_set or self.mplsoutsegmentinterface.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsoutsegmentinterface.get_name_leafdata())
                if (self.mplsoutsegmentnexthopaddr.is_set or self.mplsoutsegmentnexthopaddr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsoutsegmentnexthopaddr.get_name_leafdata())
                if (self.mplsoutsegmentnexthopaddrtype.is_set or self.mplsoutsegmentnexthopaddrtype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsoutsegmentnexthopaddrtype.get_name_leafdata())
                if (self.mplsoutsegmentowner.is_set or self.mplsoutsegmentowner.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsoutsegmentowner.get_name_leafdata())
                if (self.mplsoutsegmentperfdiscards.is_set or self.mplsoutsegmentperfdiscards.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsoutsegmentperfdiscards.get_name_leafdata())
                if (self.mplsoutsegmentperfdiscontinuitytime.is_set or self.mplsoutsegmentperfdiscontinuitytime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsoutsegmentperfdiscontinuitytime.get_name_leafdata())
                if (self.mplsoutsegmentperferrors.is_set or self.mplsoutsegmentperferrors.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsoutsegmentperferrors.get_name_leafdata())
                if (self.mplsoutsegmentperfhcoctets.is_set or self.mplsoutsegmentperfhcoctets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsoutsegmentperfhcoctets.get_name_leafdata())
                if (self.mplsoutsegmentperfoctets.is_set or self.mplsoutsegmentperfoctets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsoutsegmentperfoctets.get_name_leafdata())
                if (self.mplsoutsegmentperfpackets.is_set or self.mplsoutsegmentperfpackets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsoutsegmentperfpackets.get_name_leafdata())
                if (self.mplsoutsegmentpushtoplabel.is_set or self.mplsoutsegmentpushtoplabel.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsoutsegmentpushtoplabel.get_name_leafdata())
                if (self.mplsoutsegmentrowstatus.is_set or self.mplsoutsegmentrowstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsoutsegmentrowstatus.get_name_leafdata())
                if (self.mplsoutsegmentstoragetype.is_set or self.mplsoutsegmentstoragetype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsoutsegmentstoragetype.get_name_leafdata())
                if (self.mplsoutsegmenttoplabel.is_set or self.mplsoutsegmenttoplabel.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsoutsegmenttoplabel.get_name_leafdata())
                if (self.mplsoutsegmenttoplabelptr.is_set or self.mplsoutsegmenttoplabelptr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsoutsegmenttoplabelptr.get_name_leafdata())
                if (self.mplsoutsegmenttrafficparamptr.is_set or self.mplsoutsegmenttrafficparamptr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsoutsegmenttrafficparamptr.get_name_leafdata())
                if (self.mplsoutsegmentxcindex.is_set or self.mplsoutsegmentxcindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsoutsegmentxcindex.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "mplsOutSegmentIndex" or name == "mplsOutSegmentInterface" or name == "mplsOutSegmentNextHopAddr" or name == "mplsOutSegmentNextHopAddrType" or name == "mplsOutSegmentOwner" or name == "mplsOutSegmentPerfDiscards" or name == "mplsOutSegmentPerfDiscontinuityTime" or name == "mplsOutSegmentPerfErrors" or name == "mplsOutSegmentPerfHCOctets" or name == "mplsOutSegmentPerfOctets" or name == "mplsOutSegmentPerfPackets" or name == "mplsOutSegmentPushTopLabel" or name == "mplsOutSegmentRowStatus" or name == "mplsOutSegmentStorageType" or name == "mplsOutSegmentTopLabel" or name == "mplsOutSegmentTopLabelPtr" or name == "mplsOutSegmentTrafficParamPtr" or name == "mplsOutSegmentXCIndex"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "mplsOutSegmentIndex"):
                    self.mplsoutsegmentindex = value
                    self.mplsoutsegmentindex.value_namespace = name_space
                    self.mplsoutsegmentindex.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsOutSegmentInterface"):
                    self.mplsoutsegmentinterface = value
                    self.mplsoutsegmentinterface.value_namespace = name_space
                    self.mplsoutsegmentinterface.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsOutSegmentNextHopAddr"):
                    self.mplsoutsegmentnexthopaddr = value
                    self.mplsoutsegmentnexthopaddr.value_namespace = name_space
                    self.mplsoutsegmentnexthopaddr.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsOutSegmentNextHopAddrType"):
                    self.mplsoutsegmentnexthopaddrtype = value
                    self.mplsoutsegmentnexthopaddrtype.value_namespace = name_space
                    self.mplsoutsegmentnexthopaddrtype.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsOutSegmentOwner"):
                    self.mplsoutsegmentowner = value
                    self.mplsoutsegmentowner.value_namespace = name_space
                    self.mplsoutsegmentowner.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsOutSegmentPerfDiscards"):
                    self.mplsoutsegmentperfdiscards = value
                    self.mplsoutsegmentperfdiscards.value_namespace = name_space
                    self.mplsoutsegmentperfdiscards.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsOutSegmentPerfDiscontinuityTime"):
                    self.mplsoutsegmentperfdiscontinuitytime = value
                    self.mplsoutsegmentperfdiscontinuitytime.value_namespace = name_space
                    self.mplsoutsegmentperfdiscontinuitytime.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsOutSegmentPerfErrors"):
                    self.mplsoutsegmentperferrors = value
                    self.mplsoutsegmentperferrors.value_namespace = name_space
                    self.mplsoutsegmentperferrors.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsOutSegmentPerfHCOctets"):
                    self.mplsoutsegmentperfhcoctets = value
                    self.mplsoutsegmentperfhcoctets.value_namespace = name_space
                    self.mplsoutsegmentperfhcoctets.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsOutSegmentPerfOctets"):
                    self.mplsoutsegmentperfoctets = value
                    self.mplsoutsegmentperfoctets.value_namespace = name_space
                    self.mplsoutsegmentperfoctets.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsOutSegmentPerfPackets"):
                    self.mplsoutsegmentperfpackets = value
                    self.mplsoutsegmentperfpackets.value_namespace = name_space
                    self.mplsoutsegmentperfpackets.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsOutSegmentPushTopLabel"):
                    self.mplsoutsegmentpushtoplabel = value
                    self.mplsoutsegmentpushtoplabel.value_namespace = name_space
                    self.mplsoutsegmentpushtoplabel.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsOutSegmentRowStatus"):
                    self.mplsoutsegmentrowstatus = value
                    self.mplsoutsegmentrowstatus.value_namespace = name_space
                    self.mplsoutsegmentrowstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsOutSegmentStorageType"):
                    self.mplsoutsegmentstoragetype = value
                    self.mplsoutsegmentstoragetype.value_namespace = name_space
                    self.mplsoutsegmentstoragetype.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsOutSegmentTopLabel"):
                    self.mplsoutsegmenttoplabel = value
                    self.mplsoutsegmenttoplabel.value_namespace = name_space
                    self.mplsoutsegmenttoplabel.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsOutSegmentTopLabelPtr"):
                    self.mplsoutsegmenttoplabelptr = value
                    self.mplsoutsegmenttoplabelptr.value_namespace = name_space
                    self.mplsoutsegmenttoplabelptr.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsOutSegmentTrafficParamPtr"):
                    self.mplsoutsegmenttrafficparamptr = value
                    self.mplsoutsegmenttrafficparamptr.value_namespace = name_space
                    self.mplsoutsegmenttrafficparamptr.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsOutSegmentXCIndex"):
                    self.mplsoutsegmentxcindex = value
                    self.mplsoutsegmentxcindex.value_namespace = name_space
                    self.mplsoutsegmentxcindex.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.mplsoutsegmententry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.mplsoutsegmententry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "mplsOutSegmentTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "MPLS-LSR-STD-MIB:MPLS-LSR-STD-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "mplsOutSegmentEntry"):
                for c in self.mplsoutsegmententry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = MplsLsrStdMib.Mplsoutsegmenttable.Mplsoutsegmententry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.mplsoutsegmententry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "mplsOutSegmentEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Mplsxctable(Entity):
        """
        This table specifies information for switching
        between LSP segments.  It supports point\-to\-point,
        point\-to\-multipoint and multipoint\-to\-point
        connections.  mplsLabelStackTable specifies the
        label stack information for a cross\-connect LSR and
        is referred to from mplsXCTable.
        
        .. attribute:: mplsxcentry
        
        	A row in this table represents one cross\-connect entry.  It is indexed by the following objects\:  \- cross\-connect index mplsXCIndex that uniquely   identifies a group of cross\-connect entries  \- in\-segment index, mplsXCInSegmentIndex  \- out\-segment index, mplsXCOutSegmentIndex  LSPs originating at this LSR\: These are represented by using the special of value of mplsXCInSegmentIndex set to the string containing a single octet 0x00. In this case the mplsXCOutSegmentIndex MUST not be the string containing a single octet 0x00.  LSPs terminating at this LSR\: These are represented by using the special value mplsXCOutSegmentIndex set to the string containing a single octet 0x00.  Special labels\: Entries indexed by the strings containing the reserved MPLS label values as a single octet 0x00 through 0x0f (inclusive) imply LSPs terminating at this LSR.  Note that situations where LSPs are terminated with incoming label equal to the string containing a single octet 0x00 can be distinguished from LSPs originating at this LSR because the mplsXCOutSegmentIndex equals the string containing the single octet 0x00.  An entry can be created by a network administrator or by an SNMP agent as instructed by an MPLS signaling protocol
        	**type**\: list of    :py:class:`Mplsxcentry <ydk.models.cisco_ios_xe.MPLS_LSR_STD_MIB.MplsLsrStdMib.Mplsxctable.Mplsxcentry>`
        
        

        """

        _prefix = 'MPLS-LSR-STD-MIB'
        _revision = '2004-06-03'

        def __init__(self):
            super(MplsLsrStdMib.Mplsxctable, self).__init__()

            self.yang_name = "mplsXCTable"
            self.yang_parent_name = "MPLS-LSR-STD-MIB"

            self.mplsxcentry = YList(self)

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
                        super(MplsLsrStdMib.Mplsxctable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(MplsLsrStdMib.Mplsxctable, self).__setattr__(name, value)


        class Mplsxcentry(Entity):
            """
            A row in this table represents one cross\-connect
            entry.  It is indexed by the following objects\:
            
            \- cross\-connect index mplsXCIndex that uniquely
              identifies a group of cross\-connect entries
            
            \- in\-segment index, mplsXCInSegmentIndex
            
            \- out\-segment index, mplsXCOutSegmentIndex
            
            LSPs originating at this LSR\:
            These are represented by using the special
            of value of mplsXCInSegmentIndex set to the
            string containing a single octet 0x00. In
            this case the mplsXCOutSegmentIndex
            MUST not be the string containing a single
            octet 0x00.
            
            LSPs terminating at this LSR\:
            These are represented by using the special value
            mplsXCOutSegmentIndex set to the string containing
            a single octet 0x00.
            
            Special labels\:
            Entries indexed by the strings containing the
            reserved MPLS label values as a single octet 0x00
            through 0x0f (inclusive) imply LSPs terminating at
            this LSR.  Note that situations where LSPs are
            terminated with incoming label equal to the string
            containing a single octet 0x00 can be distinguished
            from LSPs originating at this LSR because the
            mplsXCOutSegmentIndex equals the string containing the
            single octet 0x00.
            
            An entry can be created by a network administrator
            or by an SNMP agent as instructed by an MPLS
            signaling protocol.
            
            .. attribute:: mplsxcindex  <key>
            
            	Primary index for the conceptual row identifying a group of cross\-connect segments. The string containing a single octet 0x00 is an invalid index
            	**type**\:  str
            
            	**length:** 1..24
            
            .. attribute:: mplsxcinsegmentindex  <key>
            
            	Incoming label index. If this object is set to the string containing a single octet 0x00, this indicates a special case outlined in the table's description above. In this case no corresponding mplsInSegmentEntry shall exist
            	**type**\:  str
            
            	**length:** 1..24
            
            .. attribute:: mplsxcoutsegmentindex  <key>
            
            	Index of out\-segment for LSPs not terminating on this LSR if not set to the string containing the single octet 0x00. If the segment identified by this entry is terminating, then this object MUST be set to the string containing a single octet 0x00 to indicate that no corresponding mplsOutSegmentEntry shall exist
            	**type**\:  str
            
            	**length:** 1..24
            
            .. attribute:: mplsxcadminstatus
            
            	The desired operational status of this segment
            	**type**\:   :py:class:`Mplsxcadminstatus <ydk.models.cisco_ios_xe.MPLS_LSR_STD_MIB.MplsLsrStdMib.Mplsxctable.Mplsxcentry.Mplsxcadminstatus>`
            
            .. attribute:: mplsxclabelstackindex
            
            	Primary index into mplsLabelStackTable identifying a stack of labels to be pushed beneath the top label. Note that the top label identified by the out\- segment ensures that all the components of a multipoint\-to\-point connection have the same outgoing label. A value of the string containing the single octet 0x00 indicates that no labels are to be stacked beneath the top label. This object cannot be modified if mplsXCRowStatus is active(1)
            	**type**\:  str
            
            	**length:** 1..24
            
            .. attribute:: mplsxclspid
            
            	This value identifies the label switched path that this cross\-connect entry belongs to. This object cannot be modified if mplsXCRowStatus is active(1) except for this object
            	**type**\:  str
            
            	**length:** 2 \| 6
            
            .. attribute:: mplsxcoperstatus
            
            	The actual operational status of this cross\- connect
            	**type**\:   :py:class:`Mplsxcoperstatus <ydk.models.cisco_ios_xe.MPLS_LSR_STD_MIB.MplsLsrStdMib.Mplsxctable.Mplsxcentry.Mplsxcoperstatus>`
            
            .. attribute:: mplsxcowner
            
            	Denotes the entity that created and is responsible for managing this cross\-connect
            	**type**\:   :py:class:`Mplsowner <ydk.models.cisco_ios_xe.MPLS_TC_STD_MIB.Mplsowner>`
            
            .. attribute:: mplsxcrowstatus
            
            	For creating, modifying, and deleting this row. When a row in this table has a row in the active(1) state, no objects in this row except this object and the mplsXCStorageType can be modified. 
            	**type**\:   :py:class:`Rowstatus <ydk.models.cisco_ios_xe.SNMPv2_TC.Rowstatus>`
            
            .. attribute:: mplsxcstoragetype
            
            	This variable indicates the storage type for this object. The agent MUST ensure that the associated in and out segments also have the same StorageType value and are restored consistently upon system restart. This value SHOULD be set to permanent(4) if created as a result of a static LSP configuration.  Conceptual rows having the value 'permanent' need not allow write\-access to any columnar objects in the row
            	**type**\:   :py:class:`Storagetype <ydk.models.cisco_ios_xe.SNMPv2_TC.Storagetype>`
            
            

            """

            _prefix = 'MPLS-LSR-STD-MIB'
            _revision = '2004-06-03'

            def __init__(self):
                super(MplsLsrStdMib.Mplsxctable.Mplsxcentry, self).__init__()

                self.yang_name = "mplsXCEntry"
                self.yang_parent_name = "mplsXCTable"

                self.mplsxcindex = YLeaf(YType.str, "mplsXCIndex")

                self.mplsxcinsegmentindex = YLeaf(YType.str, "mplsXCInSegmentIndex")

                self.mplsxcoutsegmentindex = YLeaf(YType.str, "mplsXCOutSegmentIndex")

                self.mplsxcadminstatus = YLeaf(YType.enumeration, "mplsXCAdminStatus")

                self.mplsxclabelstackindex = YLeaf(YType.str, "mplsXCLabelStackIndex")

                self.mplsxclspid = YLeaf(YType.str, "mplsXCLspId")

                self.mplsxcoperstatus = YLeaf(YType.enumeration, "mplsXCOperStatus")

                self.mplsxcowner = YLeaf(YType.enumeration, "mplsXCOwner")

                self.mplsxcrowstatus = YLeaf(YType.enumeration, "mplsXCRowStatus")

                self.mplsxcstoragetype = YLeaf(YType.enumeration, "mplsXCStorageType")

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
                                "mplsxcadminstatus",
                                "mplsxclabelstackindex",
                                "mplsxclspid",
                                "mplsxcoperstatus",
                                "mplsxcowner",
                                "mplsxcrowstatus",
                                "mplsxcstoragetype") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(MplsLsrStdMib.Mplsxctable.Mplsxcentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(MplsLsrStdMib.Mplsxctable.Mplsxcentry, self).__setattr__(name, value)

            class Mplsxcadminstatus(Enum):
                """
                Mplsxcadminstatus

                The desired operational status of this segment.

                .. data:: up = 1

                .. data:: down = 2

                .. data:: testing = 3

                """

                up = Enum.YLeaf(1, "up")

                down = Enum.YLeaf(2, "down")

                testing = Enum.YLeaf(3, "testing")


            class Mplsxcoperstatus(Enum):
                """
                Mplsxcoperstatus

                The actual operational status of this cross\-

                connect.

                .. data:: up = 1

                .. data:: down = 2

                .. data:: testing = 3

                .. data:: unknown = 4

                .. data:: dormant = 5

                .. data:: notPresent = 6

                .. data:: lowerLayerDown = 7

                """

                up = Enum.YLeaf(1, "up")

                down = Enum.YLeaf(2, "down")

                testing = Enum.YLeaf(3, "testing")

                unknown = Enum.YLeaf(4, "unknown")

                dormant = Enum.YLeaf(5, "dormant")

                notPresent = Enum.YLeaf(6, "notPresent")

                lowerLayerDown = Enum.YLeaf(7, "lowerLayerDown")


            def has_data(self):
                return (
                    self.mplsxcindex.is_set or
                    self.mplsxcinsegmentindex.is_set or
                    self.mplsxcoutsegmentindex.is_set or
                    self.mplsxcadminstatus.is_set or
                    self.mplsxclabelstackindex.is_set or
                    self.mplsxclspid.is_set or
                    self.mplsxcoperstatus.is_set or
                    self.mplsxcowner.is_set or
                    self.mplsxcrowstatus.is_set or
                    self.mplsxcstoragetype.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.mplsxcindex.yfilter != YFilter.not_set or
                    self.mplsxcinsegmentindex.yfilter != YFilter.not_set or
                    self.mplsxcoutsegmentindex.yfilter != YFilter.not_set or
                    self.mplsxcadminstatus.yfilter != YFilter.not_set or
                    self.mplsxclabelstackindex.yfilter != YFilter.not_set or
                    self.mplsxclspid.yfilter != YFilter.not_set or
                    self.mplsxcoperstatus.yfilter != YFilter.not_set or
                    self.mplsxcowner.yfilter != YFilter.not_set or
                    self.mplsxcrowstatus.yfilter != YFilter.not_set or
                    self.mplsxcstoragetype.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "mplsXCEntry" + "[mplsXCIndex='" + self.mplsxcindex.get() + "']" + "[mplsXCInSegmentIndex='" + self.mplsxcinsegmentindex.get() + "']" + "[mplsXCOutSegmentIndex='" + self.mplsxcoutsegmentindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "MPLS-LSR-STD-MIB:MPLS-LSR-STD-MIB/mplsXCTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.mplsxcindex.is_set or self.mplsxcindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsxcindex.get_name_leafdata())
                if (self.mplsxcinsegmentindex.is_set or self.mplsxcinsegmentindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsxcinsegmentindex.get_name_leafdata())
                if (self.mplsxcoutsegmentindex.is_set or self.mplsxcoutsegmentindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsxcoutsegmentindex.get_name_leafdata())
                if (self.mplsxcadminstatus.is_set or self.mplsxcadminstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsxcadminstatus.get_name_leafdata())
                if (self.mplsxclabelstackindex.is_set or self.mplsxclabelstackindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsxclabelstackindex.get_name_leafdata())
                if (self.mplsxclspid.is_set or self.mplsxclspid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsxclspid.get_name_leafdata())
                if (self.mplsxcoperstatus.is_set or self.mplsxcoperstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsxcoperstatus.get_name_leafdata())
                if (self.mplsxcowner.is_set or self.mplsxcowner.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsxcowner.get_name_leafdata())
                if (self.mplsxcrowstatus.is_set or self.mplsxcrowstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsxcrowstatus.get_name_leafdata())
                if (self.mplsxcstoragetype.is_set or self.mplsxcstoragetype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsxcstoragetype.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "mplsXCIndex" or name == "mplsXCInSegmentIndex" or name == "mplsXCOutSegmentIndex" or name == "mplsXCAdminStatus" or name == "mplsXCLabelStackIndex" or name == "mplsXCLspId" or name == "mplsXCOperStatus" or name == "mplsXCOwner" or name == "mplsXCRowStatus" or name == "mplsXCStorageType"):
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
                if(value_path == "mplsXCAdminStatus"):
                    self.mplsxcadminstatus = value
                    self.mplsxcadminstatus.value_namespace = name_space
                    self.mplsxcadminstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsXCLabelStackIndex"):
                    self.mplsxclabelstackindex = value
                    self.mplsxclabelstackindex.value_namespace = name_space
                    self.mplsxclabelstackindex.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsXCLspId"):
                    self.mplsxclspid = value
                    self.mplsxclspid.value_namespace = name_space
                    self.mplsxclspid.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsXCOperStatus"):
                    self.mplsxcoperstatus = value
                    self.mplsxcoperstatus.value_namespace = name_space
                    self.mplsxcoperstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsXCOwner"):
                    self.mplsxcowner = value
                    self.mplsxcowner.value_namespace = name_space
                    self.mplsxcowner.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsXCRowStatus"):
                    self.mplsxcrowstatus = value
                    self.mplsxcrowstatus.value_namespace = name_space
                    self.mplsxcrowstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsXCStorageType"):
                    self.mplsxcstoragetype = value
                    self.mplsxcstoragetype.value_namespace = name_space
                    self.mplsxcstoragetype.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.mplsxcentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.mplsxcentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "mplsXCTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "MPLS-LSR-STD-MIB:MPLS-LSR-STD-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "mplsXCEntry"):
                for c in self.mplsxcentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = MplsLsrStdMib.Mplsxctable.Mplsxcentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.mplsxcentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "mplsXCEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Mplslabelstacktable(Entity):
        """
        This table specifies the label stack to be pushed
        onto a packet, beneath the top label.  Entries into
        this table are referred to from mplsXCTable.
        
        .. attribute:: mplslabelstackentry
        
        	An entry in this table represents one label which is to be pushed onto an outgoing packet, beneath the top label.  An entry can be created by a network administrator or by an SNMP agent as instructed by an MPLS signaling protocol
        	**type**\: list of    :py:class:`Mplslabelstackentry <ydk.models.cisco_ios_xe.MPLS_LSR_STD_MIB.MplsLsrStdMib.Mplslabelstacktable.Mplslabelstackentry>`
        
        

        """

        _prefix = 'MPLS-LSR-STD-MIB'
        _revision = '2004-06-03'

        def __init__(self):
            super(MplsLsrStdMib.Mplslabelstacktable, self).__init__()

            self.yang_name = "mplsLabelStackTable"
            self.yang_parent_name = "MPLS-LSR-STD-MIB"

            self.mplslabelstackentry = YList(self)

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
                        super(MplsLsrStdMib.Mplslabelstacktable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(MplsLsrStdMib.Mplslabelstacktable, self).__setattr__(name, value)


        class Mplslabelstackentry(Entity):
            """
            An entry in this table represents one label which is
            to be pushed onto an outgoing packet, beneath the
            top label.  An entry can be created by a network
            administrator or by an SNMP agent as instructed by
            an MPLS signaling protocol.
            
            .. attribute:: mplslabelstackindex  <key>
            
            	Primary index for this row identifying a stack of labels to be pushed on an outgoing packet, beneath the top label. An index containing the string with a single octet 0x00 MUST not be used
            	**type**\:  str
            
            	**length:** 1..24
            
            .. attribute:: mplslabelstacklabelindex  <key>
            
            	Secondary index for this row identifying one label of the stack.  Note that an entry with a smaller mplsLabelStackLabelIndex would refer to a label higher up the label stack and would be popped at a downstream LSR before a label represented by a higher mplsLabelStackLabelIndex at a downstream LSR
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            .. attribute:: mplslabelstacklabel
            
            	The label to pushed
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplslabelstacklabelptr
            
            	If the label for this segment cannot be represented fully within the mplsLabelStackLabel object, this object MUST point to the first accessible column of a conceptual row in an external table containing the label.  In this case, the mplsLabelStackLabel object SHOULD be set to 0 and ignored. This object MUST be set to zeroDotZero otherwise
            	**type**\:  str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: mplslabelstackrowstatus
            
            	For creating, modifying, and deleting this row. When a row in this table has a row in the active(1) state, no objects in this row except this object and the mplsLabelStackStorageType can be modified
            	**type**\:   :py:class:`Rowstatus <ydk.models.cisco_ios_xe.SNMPv2_TC.Rowstatus>`
            
            .. attribute:: mplslabelstackstoragetype
            
            	This variable indicates the storage type for this object. This object cannot be modified if mplsLabelStackRowStatus is active(1). No objects are required to be writable for rows in this table with this object set to permanent(4).  The agent MUST ensure that all related entries in this table retain the same value for this object.  Agents MUST ensure that the storage type for all entries related to a particular mplsXCEntry retain the same value for this object as the mplsXCEntry's StorageType
            	**type**\:   :py:class:`Storagetype <ydk.models.cisco_ios_xe.SNMPv2_TC.Storagetype>`
            
            

            """

            _prefix = 'MPLS-LSR-STD-MIB'
            _revision = '2004-06-03'

            def __init__(self):
                super(MplsLsrStdMib.Mplslabelstacktable.Mplslabelstackentry, self).__init__()

                self.yang_name = "mplsLabelStackEntry"
                self.yang_parent_name = "mplsLabelStackTable"

                self.mplslabelstackindex = YLeaf(YType.str, "mplsLabelStackIndex")

                self.mplslabelstacklabelindex = YLeaf(YType.uint32, "mplsLabelStackLabelIndex")

                self.mplslabelstacklabel = YLeaf(YType.uint32, "mplsLabelStackLabel")

                self.mplslabelstacklabelptr = YLeaf(YType.str, "mplsLabelStackLabelPtr")

                self.mplslabelstackrowstatus = YLeaf(YType.enumeration, "mplsLabelStackRowStatus")

                self.mplslabelstackstoragetype = YLeaf(YType.enumeration, "mplsLabelStackStorageType")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("mplslabelstackindex",
                                "mplslabelstacklabelindex",
                                "mplslabelstacklabel",
                                "mplslabelstacklabelptr",
                                "mplslabelstackrowstatus",
                                "mplslabelstackstoragetype") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(MplsLsrStdMib.Mplslabelstacktable.Mplslabelstackentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(MplsLsrStdMib.Mplslabelstacktable.Mplslabelstackentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.mplslabelstackindex.is_set or
                    self.mplslabelstacklabelindex.is_set or
                    self.mplslabelstacklabel.is_set or
                    self.mplslabelstacklabelptr.is_set or
                    self.mplslabelstackrowstatus.is_set or
                    self.mplslabelstackstoragetype.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.mplslabelstackindex.yfilter != YFilter.not_set or
                    self.mplslabelstacklabelindex.yfilter != YFilter.not_set or
                    self.mplslabelstacklabel.yfilter != YFilter.not_set or
                    self.mplslabelstacklabelptr.yfilter != YFilter.not_set or
                    self.mplslabelstackrowstatus.yfilter != YFilter.not_set or
                    self.mplslabelstackstoragetype.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "mplsLabelStackEntry" + "[mplsLabelStackIndex='" + self.mplslabelstackindex.get() + "']" + "[mplsLabelStackLabelIndex='" + self.mplslabelstacklabelindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "MPLS-LSR-STD-MIB:MPLS-LSR-STD-MIB/mplsLabelStackTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.mplslabelstackindex.is_set or self.mplslabelstackindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplslabelstackindex.get_name_leafdata())
                if (self.mplslabelstacklabelindex.is_set or self.mplslabelstacklabelindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplslabelstacklabelindex.get_name_leafdata())
                if (self.mplslabelstacklabel.is_set or self.mplslabelstacklabel.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplslabelstacklabel.get_name_leafdata())
                if (self.mplslabelstacklabelptr.is_set or self.mplslabelstacklabelptr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplslabelstacklabelptr.get_name_leafdata())
                if (self.mplslabelstackrowstatus.is_set or self.mplslabelstackrowstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplslabelstackrowstatus.get_name_leafdata())
                if (self.mplslabelstackstoragetype.is_set or self.mplslabelstackstoragetype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplslabelstackstoragetype.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "mplsLabelStackIndex" or name == "mplsLabelStackLabelIndex" or name == "mplsLabelStackLabel" or name == "mplsLabelStackLabelPtr" or name == "mplsLabelStackRowStatus" or name == "mplsLabelStackStorageType"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "mplsLabelStackIndex"):
                    self.mplslabelstackindex = value
                    self.mplslabelstackindex.value_namespace = name_space
                    self.mplslabelstackindex.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsLabelStackLabelIndex"):
                    self.mplslabelstacklabelindex = value
                    self.mplslabelstacklabelindex.value_namespace = name_space
                    self.mplslabelstacklabelindex.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsLabelStackLabel"):
                    self.mplslabelstacklabel = value
                    self.mplslabelstacklabel.value_namespace = name_space
                    self.mplslabelstacklabel.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsLabelStackLabelPtr"):
                    self.mplslabelstacklabelptr = value
                    self.mplslabelstacklabelptr.value_namespace = name_space
                    self.mplslabelstacklabelptr.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsLabelStackRowStatus"):
                    self.mplslabelstackrowstatus = value
                    self.mplslabelstackrowstatus.value_namespace = name_space
                    self.mplslabelstackrowstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsLabelStackStorageType"):
                    self.mplslabelstackstoragetype = value
                    self.mplslabelstackstoragetype.value_namespace = name_space
                    self.mplslabelstackstoragetype.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.mplslabelstackentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.mplslabelstackentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "mplsLabelStackTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "MPLS-LSR-STD-MIB:MPLS-LSR-STD-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "mplsLabelStackEntry"):
                for c in self.mplslabelstackentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = MplsLsrStdMib.Mplslabelstacktable.Mplslabelstackentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.mplslabelstackentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "mplsLabelStackEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Mplsinsegmentmaptable(Entity):
        """
        This table specifies the mapping from the
        mplsInSegmentIndex to the corresponding
        mplsInSegmentInterface and mplsInSegmentLabel
        objects. The purpose of this table is to
        provide the manager with an alternative
        means by which to locate in\-segments.
        
        .. attribute:: mplsinsegmentmapentry
        
        	An entry in this table represents one interface and incoming label pair.  In cases where the label cannot fit into the mplsInSegmentLabel object, the mplsInSegmentLabelPtr will indicate this by being set to the first accessible column in the appropriate extension table's row, and the mplsInSegmentLabel SHOULD be set to 0. In all other cases when the label is represented within the mplsInSegmentLabel object, the mplsInSegmentLabelPtr MUST be 0.0.  Implementors need to be aware that if the value of the mplsInSegmentMapLabelPtrIndex (an OID) has more that 111 sub\-identifiers, then OIDs of column instances in this table will have more than 128 sub\-identifiers and cannot be accessed using SNMPv1, SNMPv2c, or SNMPv3
        	**type**\: list of    :py:class:`Mplsinsegmentmapentry <ydk.models.cisco_ios_xe.MPLS_LSR_STD_MIB.MplsLsrStdMib.Mplsinsegmentmaptable.Mplsinsegmentmapentry>`
        
        

        """

        _prefix = 'MPLS-LSR-STD-MIB'
        _revision = '2004-06-03'

        def __init__(self):
            super(MplsLsrStdMib.Mplsinsegmentmaptable, self).__init__()

            self.yang_name = "mplsInSegmentMapTable"
            self.yang_parent_name = "MPLS-LSR-STD-MIB"

            self.mplsinsegmentmapentry = YList(self)

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
                        super(MplsLsrStdMib.Mplsinsegmentmaptable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(MplsLsrStdMib.Mplsinsegmentmaptable, self).__setattr__(name, value)


        class Mplsinsegmentmapentry(Entity):
            """
            An entry in this table represents one interface
            and incoming label pair.
            
            In cases where the label cannot fit into the
            mplsInSegmentLabel object, the mplsInSegmentLabelPtr
            will indicate this by being set to the first accessible
            column in the appropriate extension table's row,
            and the mplsInSegmentLabel SHOULD be set to 0.
            In all other cases when the label is
            represented within the mplsInSegmentLabel object, the
            mplsInSegmentLabelPtr MUST be 0.0.
            
            Implementors need to be aware that if the value of
            the mplsInSegmentMapLabelPtrIndex (an OID) has more
            that 111 sub\-identifiers, then OIDs of column
            instances in this table will have more than 128
            sub\-identifiers and cannot be accessed using SNMPv1,
            SNMPv2c, or SNMPv3.
            
            .. attribute:: mplsinsegmentmapinterface  <key>
            
            	This index contains the same value as the mplsInSegmentIndex in the mplsInSegmentTable
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: mplsinsegmentmaplabel  <key>
            
            	This index contains the same value as the mplsInSegmentLabel in the mplsInSegmentTable
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplsinsegmentmaplabelptrindex  <key>
            
            	This index contains the same value as the mplsInSegmentLabelPtr.  If the label for the InSegment cannot be represented fully within the mplsInSegmentLabel object, this index MUST point to the first accessible column of a conceptual row in an external table containing the label.  In this case, the mplsInSegmentTopLabel object SHOULD be set to 0 and ignored. This object MUST be set to zeroDotZero otherwise
            	**type**\:  str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: mplsinsegmentmapindex
            
            	The mplsInSegmentIndex that corresponds to the mplsInSegmentInterface and mplsInSegmentLabel, or the mplsInSegmentInterface and mplsInSegmentLabelPtr, if applicable. The string containing the single octet 0x00 MUST not be returned
            	**type**\:  str
            
            	**length:** 1..24
            
            

            """

            _prefix = 'MPLS-LSR-STD-MIB'
            _revision = '2004-06-03'

            def __init__(self):
                super(MplsLsrStdMib.Mplsinsegmentmaptable.Mplsinsegmentmapentry, self).__init__()

                self.yang_name = "mplsInSegmentMapEntry"
                self.yang_parent_name = "mplsInSegmentMapTable"

                self.mplsinsegmentmapinterface = YLeaf(YType.int32, "mplsInSegmentMapInterface")

                self.mplsinsegmentmaplabel = YLeaf(YType.uint32, "mplsInSegmentMapLabel")

                self.mplsinsegmentmaplabelptrindex = YLeaf(YType.str, "mplsInSegmentMapLabelPtrIndex")

                self.mplsinsegmentmapindex = YLeaf(YType.str, "mplsInSegmentMapIndex")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("mplsinsegmentmapinterface",
                                "mplsinsegmentmaplabel",
                                "mplsinsegmentmaplabelptrindex",
                                "mplsinsegmentmapindex") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(MplsLsrStdMib.Mplsinsegmentmaptable.Mplsinsegmentmapentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(MplsLsrStdMib.Mplsinsegmentmaptable.Mplsinsegmentmapentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.mplsinsegmentmapinterface.is_set or
                    self.mplsinsegmentmaplabel.is_set or
                    self.mplsinsegmentmaplabelptrindex.is_set or
                    self.mplsinsegmentmapindex.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.mplsinsegmentmapinterface.yfilter != YFilter.not_set or
                    self.mplsinsegmentmaplabel.yfilter != YFilter.not_set or
                    self.mplsinsegmentmaplabelptrindex.yfilter != YFilter.not_set or
                    self.mplsinsegmentmapindex.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "mplsInSegmentMapEntry" + "[mplsInSegmentMapInterface='" + self.mplsinsegmentmapinterface.get() + "']" + "[mplsInSegmentMapLabel='" + self.mplsinsegmentmaplabel.get() + "']" + "[mplsInSegmentMapLabelPtrIndex='" + self.mplsinsegmentmaplabelptrindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "MPLS-LSR-STD-MIB:MPLS-LSR-STD-MIB/mplsInSegmentMapTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.mplsinsegmentmapinterface.is_set or self.mplsinsegmentmapinterface.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsinsegmentmapinterface.get_name_leafdata())
                if (self.mplsinsegmentmaplabel.is_set or self.mplsinsegmentmaplabel.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsinsegmentmaplabel.get_name_leafdata())
                if (self.mplsinsegmentmaplabelptrindex.is_set or self.mplsinsegmentmaplabelptrindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsinsegmentmaplabelptrindex.get_name_leafdata())
                if (self.mplsinsegmentmapindex.is_set or self.mplsinsegmentmapindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mplsinsegmentmapindex.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "mplsInSegmentMapInterface" or name == "mplsInSegmentMapLabel" or name == "mplsInSegmentMapLabelPtrIndex" or name == "mplsInSegmentMapIndex"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "mplsInSegmentMapInterface"):
                    self.mplsinsegmentmapinterface = value
                    self.mplsinsegmentmapinterface.value_namespace = name_space
                    self.mplsinsegmentmapinterface.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsInSegmentMapLabel"):
                    self.mplsinsegmentmaplabel = value
                    self.mplsinsegmentmaplabel.value_namespace = name_space
                    self.mplsinsegmentmaplabel.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsInSegmentMapLabelPtrIndex"):
                    self.mplsinsegmentmaplabelptrindex = value
                    self.mplsinsegmentmaplabelptrindex.value_namespace = name_space
                    self.mplsinsegmentmaplabelptrindex.value_namespace_prefix = name_space_prefix
                if(value_path == "mplsInSegmentMapIndex"):
                    self.mplsinsegmentmapindex = value
                    self.mplsinsegmentmapindex.value_namespace = name_space
                    self.mplsinsegmentmapindex.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.mplsinsegmentmapentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.mplsinsegmentmapentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "mplsInSegmentMapTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "MPLS-LSR-STD-MIB:MPLS-LSR-STD-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "mplsInSegmentMapEntry"):
                for c in self.mplsinsegmentmapentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = MplsLsrStdMib.Mplsinsegmentmaptable.Mplsinsegmentmapentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.mplsinsegmentmapentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "mplsInSegmentMapEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            (self.mplsinsegmentmaptable is not None and self.mplsinsegmentmaptable.has_data()) or
            (self.mplsinsegmenttable is not None and self.mplsinsegmenttable.has_data()) or
            (self.mplsinterfacetable is not None and self.mplsinterfacetable.has_data()) or
            (self.mplslabelstacktable is not None and self.mplslabelstacktable.has_data()) or
            (self.mplslsrobjects is not None and self.mplslsrobjects.has_data()) or
            (self.mplsoutsegmenttable is not None and self.mplsoutsegmenttable.has_data()) or
            (self.mplsxctable is not None and self.mplsxctable.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.mplsinsegmentmaptable is not None and self.mplsinsegmentmaptable.has_operation()) or
            (self.mplsinsegmenttable is not None and self.mplsinsegmenttable.has_operation()) or
            (self.mplsinterfacetable is not None and self.mplsinterfacetable.has_operation()) or
            (self.mplslabelstacktable is not None and self.mplslabelstacktable.has_operation()) or
            (self.mplslsrobjects is not None and self.mplslsrobjects.has_operation()) or
            (self.mplsoutsegmenttable is not None and self.mplsoutsegmenttable.has_operation()) or
            (self.mplsxctable is not None and self.mplsxctable.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "MPLS-LSR-STD-MIB:MPLS-LSR-STD-MIB" + path_buffer

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

        if (child_yang_name == "mplsInSegmentMapTable"):
            if (self.mplsinsegmentmaptable is None):
                self.mplsinsegmentmaptable = MplsLsrStdMib.Mplsinsegmentmaptable()
                self.mplsinsegmentmaptable.parent = self
                self._children_name_map["mplsinsegmentmaptable"] = "mplsInSegmentMapTable"
            return self.mplsinsegmentmaptable

        if (child_yang_name == "mplsInSegmentTable"):
            if (self.mplsinsegmenttable is None):
                self.mplsinsegmenttable = MplsLsrStdMib.Mplsinsegmenttable()
                self.mplsinsegmenttable.parent = self
                self._children_name_map["mplsinsegmenttable"] = "mplsInSegmentTable"
            return self.mplsinsegmenttable

        if (child_yang_name == "mplsInterfaceTable"):
            if (self.mplsinterfacetable is None):
                self.mplsinterfacetable = MplsLsrStdMib.Mplsinterfacetable()
                self.mplsinterfacetable.parent = self
                self._children_name_map["mplsinterfacetable"] = "mplsInterfaceTable"
            return self.mplsinterfacetable

        if (child_yang_name == "mplsLabelStackTable"):
            if (self.mplslabelstacktable is None):
                self.mplslabelstacktable = MplsLsrStdMib.Mplslabelstacktable()
                self.mplslabelstacktable.parent = self
                self._children_name_map["mplslabelstacktable"] = "mplsLabelStackTable"
            return self.mplslabelstacktable

        if (child_yang_name == "mplsLsrObjects"):
            if (self.mplslsrobjects is None):
                self.mplslsrobjects = MplsLsrStdMib.Mplslsrobjects()
                self.mplslsrobjects.parent = self
                self._children_name_map["mplslsrobjects"] = "mplsLsrObjects"
            return self.mplslsrobjects

        if (child_yang_name == "mplsOutSegmentTable"):
            if (self.mplsoutsegmenttable is None):
                self.mplsoutsegmenttable = MplsLsrStdMib.Mplsoutsegmenttable()
                self.mplsoutsegmenttable.parent = self
                self._children_name_map["mplsoutsegmenttable"] = "mplsOutSegmentTable"
            return self.mplsoutsegmenttable

        if (child_yang_name == "mplsXCTable"):
            if (self.mplsxctable is None):
                self.mplsxctable = MplsLsrStdMib.Mplsxctable()
                self.mplsxctable.parent = self
                self._children_name_map["mplsxctable"] = "mplsXCTable"
            return self.mplsxctable

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "mplsInSegmentMapTable" or name == "mplsInSegmentTable" or name == "mplsInterfaceTable" or name == "mplsLabelStackTable" or name == "mplsLsrObjects" or name == "mplsOutSegmentTable" or name == "mplsXCTable"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = MplsLsrStdMib()
        return self._top_entity

