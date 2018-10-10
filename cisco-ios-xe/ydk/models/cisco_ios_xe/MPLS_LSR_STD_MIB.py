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
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class MPLSLSRSTDMIB(Entity):
    """
    
    
    .. attribute:: mplslsrobjects
    
    	
    	**type**\:  :py:class:`MplsLsrObjects <ydk.models.cisco_ios_xe.MPLS_LSR_STD_MIB.MPLSLSRSTDMIB.MplsLsrObjects>`
    
    .. attribute:: mplsinterfacetable
    
    	This table specifies per\-interface MPLS capability and associated information
    	**type**\:  :py:class:`MplsInterfaceTable <ydk.models.cisco_ios_xe.MPLS_LSR_STD_MIB.MPLSLSRSTDMIB.MplsInterfaceTable>`
    
    .. attribute:: mplsinsegmenttable
    
    	This table contains a description of the incoming MPLS segments (labels) to an LSR and their associated parameters. The index for this table is mplsInSegmentIndex. The index structure of this table is specifically designed to handle many different MPLS implementations that manage their labels both in a distributed and centralized manner. The table is also designed to handle existing MPLS labels as defined in RFC3031 as well as longer ones that may be necessary in the future.  In cases where the label cannot fit into the mplsInSegmentLabel object, the mplsInSegmentLabelPtr will indicate this by being set to the first accessible column in the appropriate extension table's row. In this case an additional table MUST be provided and MUST be indexed by at least the indexes used by this table. In all other cases when the label is represented within the mplsInSegmentLabel object, the mplsInSegmentLabelPtr MUST be set to 0.0. Due to the fact that MPLS labels may not exceed 24 bits, the mplsInSegmentLabelPtr object is only a provision for future\-proofing the MIB module. Thus, the definition of any extension tables is beyond the scope of this MIB module
    	**type**\:  :py:class:`MplsInSegmentTable <ydk.models.cisco_ios_xe.MPLS_LSR_STD_MIB.MPLSLSRSTDMIB.MplsInSegmentTable>`
    
    .. attribute:: mplsoutsegmenttable
    
    	This table contains a representation of the outgoing segments from an LSR
    	**type**\:  :py:class:`MplsOutSegmentTable <ydk.models.cisco_ios_xe.MPLS_LSR_STD_MIB.MPLSLSRSTDMIB.MplsOutSegmentTable>`
    
    .. attribute:: mplsxctable
    
    	This table specifies information for switching between LSP segments.  It supports point\-to\-point, point\-to\-multipoint and multipoint\-to\-point connections.  mplsLabelStackTable specifies the label stack information for a cross\-connect LSR and is referred to from mplsXCTable
    	**type**\:  :py:class:`MplsXCTable <ydk.models.cisco_ios_xe.MPLS_LSR_STD_MIB.MPLSLSRSTDMIB.MplsXCTable>`
    
    .. attribute:: mplslabelstacktable
    
    	This table specifies the label stack to be pushed onto a packet, beneath the top label.  Entries into this table are referred to from mplsXCTable
    	**type**\:  :py:class:`MplsLabelStackTable <ydk.models.cisco_ios_xe.MPLS_LSR_STD_MIB.MPLSLSRSTDMIB.MplsLabelStackTable>`
    
    .. attribute:: mplsinsegmentmaptable
    
    	This table specifies the mapping from the mplsInSegmentIndex to the corresponding mplsInSegmentInterface and mplsInSegmentLabel objects. The purpose of this table is to provide the manager with an alternative means by which to locate in\-segments
    	**type**\:  :py:class:`MplsInSegmentMapTable <ydk.models.cisco_ios_xe.MPLS_LSR_STD_MIB.MPLSLSRSTDMIB.MplsInSegmentMapTable>`
    
    

    """

    _prefix = 'MPLS-LSR-STD-MIB'
    _revision = '2004-06-03'

    def __init__(self):
        super(MPLSLSRSTDMIB, self).__init__()
        self._top_entity = None

        self.yang_name = "MPLS-LSR-STD-MIB"
        self.yang_parent_name = "MPLS-LSR-STD-MIB"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("mplsLsrObjects", ("mplslsrobjects", MPLSLSRSTDMIB.MplsLsrObjects)), ("mplsInterfaceTable", ("mplsinterfacetable", MPLSLSRSTDMIB.MplsInterfaceTable)), ("mplsInSegmentTable", ("mplsinsegmenttable", MPLSLSRSTDMIB.MplsInSegmentTable)), ("mplsOutSegmentTable", ("mplsoutsegmenttable", MPLSLSRSTDMIB.MplsOutSegmentTable)), ("mplsXCTable", ("mplsxctable", MPLSLSRSTDMIB.MplsXCTable)), ("mplsLabelStackTable", ("mplslabelstacktable", MPLSLSRSTDMIB.MplsLabelStackTable)), ("mplsInSegmentMapTable", ("mplsinsegmentmaptable", MPLSLSRSTDMIB.MplsInSegmentMapTable))])
        self._leafs = OrderedDict()

        self.mplslsrobjects = MPLSLSRSTDMIB.MplsLsrObjects()
        self.mplslsrobjects.parent = self
        self._children_name_map["mplslsrobjects"] = "mplsLsrObjects"

        self.mplsinterfacetable = MPLSLSRSTDMIB.MplsInterfaceTable()
        self.mplsinterfacetable.parent = self
        self._children_name_map["mplsinterfacetable"] = "mplsInterfaceTable"

        self.mplsinsegmenttable = MPLSLSRSTDMIB.MplsInSegmentTable()
        self.mplsinsegmenttable.parent = self
        self._children_name_map["mplsinsegmenttable"] = "mplsInSegmentTable"

        self.mplsoutsegmenttable = MPLSLSRSTDMIB.MplsOutSegmentTable()
        self.mplsoutsegmenttable.parent = self
        self._children_name_map["mplsoutsegmenttable"] = "mplsOutSegmentTable"

        self.mplsxctable = MPLSLSRSTDMIB.MplsXCTable()
        self.mplsxctable.parent = self
        self._children_name_map["mplsxctable"] = "mplsXCTable"

        self.mplslabelstacktable = MPLSLSRSTDMIB.MplsLabelStackTable()
        self.mplslabelstacktable.parent = self
        self._children_name_map["mplslabelstacktable"] = "mplsLabelStackTable"

        self.mplsinsegmentmaptable = MPLSLSRSTDMIB.MplsInSegmentMapTable()
        self.mplsinsegmentmaptable.parent = self
        self._children_name_map["mplsinsegmentmaptable"] = "mplsInSegmentMapTable"
        self._segment_path = lambda: "MPLS-LSR-STD-MIB:MPLS-LSR-STD-MIB"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(MPLSLSRSTDMIB, [], name, value)


    class MplsLsrObjects(Entity):
        """
        
        
        .. attribute:: mplsinsegmentindexnext
        
        	This object contains the next available value to be used for mplsInSegmentIndex when creating entries in the mplsInSegmentTable. The special value of a string containing the single octet 0x00 indicates that no new entries can be created in this table. Agents not allowing managers to create entries in this table MUST set this object to this special value
        	**type**\: str
        
        	**length:** 1..24
        
        .. attribute:: mplsoutsegmentindexnext
        
        	This object contains the next available value to be used for mplsOutSegmentIndex when creating entries in the mplsOutSegmentTable. The special value of a string containing the single octet 0x00 indicates that no new entries can be created in this table. Agents not allowing managers to create entries in this table MUST set this object to this special value
        	**type**\: str
        
        	**length:** 1..24
        
        .. attribute:: mplsxcindexnext
        
        	This object contains the next available value to be used for mplsXCIndex when creating entries in the mplsXCTable. A special value of the zero length string indicates that no more new entries can be created in the relevant table.  Agents not allowing managers to create entries in this table MUST set this value to the zero length string
        	**type**\: str
        
        	**length:** 1..24
        
        .. attribute:: mplsmaxlabelstackdepth
        
        	The maximum stack depth supported by this LSR
        	**type**\: int
        
        	**range:** 1..2147483647
        
        .. attribute:: mplslabelstackindexnext
        
        	This object contains the next available value to be used for mplsLabelStackIndex when creating entries in the mplsLabelStackTable. The special string containing the single octet 0x00 indicates that no more new entries can be created in the relevant table.  Agents not allowing managers to create entries in this table MUST set this value to the string containing the single octet 0x00
        	**type**\: str
        
        	**length:** 1..24
        
        .. attribute:: mplsxcnotificationsenable
        
        	If this object is set to true(1), then it enables the emission of mplsXCUp and mplsXCDown notifications; otherwise these notifications are not emitted
        	**type**\: bool
        
        

        """

        _prefix = 'MPLS-LSR-STD-MIB'
        _revision = '2004-06-03'

        def __init__(self):
            super(MPLSLSRSTDMIB.MplsLsrObjects, self).__init__()

            self.yang_name = "mplsLsrObjects"
            self.yang_parent_name = "MPLS-LSR-STD-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('mplsinsegmentindexnext', (YLeaf(YType.str, 'mplsInSegmentIndexNext'), ['str'])),
                ('mplsoutsegmentindexnext', (YLeaf(YType.str, 'mplsOutSegmentIndexNext'), ['str'])),
                ('mplsxcindexnext', (YLeaf(YType.str, 'mplsXCIndexNext'), ['str'])),
                ('mplsmaxlabelstackdepth', (YLeaf(YType.uint32, 'mplsMaxLabelStackDepth'), ['int'])),
                ('mplslabelstackindexnext', (YLeaf(YType.str, 'mplsLabelStackIndexNext'), ['str'])),
                ('mplsxcnotificationsenable', (YLeaf(YType.boolean, 'mplsXCNotificationsEnable'), ['bool'])),
            ])
            self.mplsinsegmentindexnext = None
            self.mplsoutsegmentindexnext = None
            self.mplsxcindexnext = None
            self.mplsmaxlabelstackdepth = None
            self.mplslabelstackindexnext = None
            self.mplsxcnotificationsenable = None
            self._segment_path = lambda: "mplsLsrObjects"
            self._absolute_path = lambda: "MPLS-LSR-STD-MIB:MPLS-LSR-STD-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(MPLSLSRSTDMIB.MplsLsrObjects, [u'mplsinsegmentindexnext', u'mplsoutsegmentindexnext', u'mplsxcindexnext', u'mplsmaxlabelstackdepth', u'mplslabelstackindexnext', u'mplsxcnotificationsenable'], name, value)


    class MplsInterfaceTable(Entity):
        """
        This table specifies per\-interface MPLS capability
        and associated information.
        
        .. attribute:: mplsinterfaceentry
        
        	A conceptual row in this table is created automatically by an LSR for every interface capable of supporting MPLS and which is configured to do so. A conceptual row in this table will exist if and only if a corresponding entry in ifTable exists with ifType = mpls(166). If this associated entry in ifTable is operationally disabled (thus removing MPLS capabilities on that interface), the corresponding entry in this table MUST be deleted shortly thereafter. An conceptual row with index 0 is created if the LSR supports per\-platform labels. This conceptual row represents the per\-platform label space and contains parameters that apply to all interfaces that participate in the per\-platform label space. Other conceptual rows in this table represent MPLS interfaces that may participate in either the per\-platform or per\- interface label spaces, or both.  Implementations that either only support per\-platform labels, or have only them configured, may choose to return just the mplsInterfaceEntry of 0 and not return the other rows. This will greatly reduce the number of objects returned. Further information about label space participation of an interface is provided in the DESCRIPTION clause of mplsInterfaceLabelParticipationType
        	**type**\: list of  		 :py:class:`MplsInterfaceEntry <ydk.models.cisco_ios_xe.MPLS_LSR_STD_MIB.MPLSLSRSTDMIB.MplsInterfaceTable.MplsInterfaceEntry>`
        
        

        """

        _prefix = 'MPLS-LSR-STD-MIB'
        _revision = '2004-06-03'

        def __init__(self):
            super(MPLSLSRSTDMIB.MplsInterfaceTable, self).__init__()

            self.yang_name = "mplsInterfaceTable"
            self.yang_parent_name = "MPLS-LSR-STD-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("mplsInterfaceEntry", ("mplsinterfaceentry", MPLSLSRSTDMIB.MplsInterfaceTable.MplsInterfaceEntry))])
            self._leafs = OrderedDict()

            self.mplsinterfaceentry = YList(self)
            self._segment_path = lambda: "mplsInterfaceTable"
            self._absolute_path = lambda: "MPLS-LSR-STD-MIB:MPLS-LSR-STD-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(MPLSLSRSTDMIB.MplsInterfaceTable, [], name, value)


        class MplsInterfaceEntry(Entity):
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
            
            .. attribute:: mplsinterfaceindex  (key)
            
            	This is a unique index for an entry in the MplsInterfaceTable.  A non\-zero index for an entry indicates the ifIndex for the corresponding interface entry of the MPLS\-layer in the ifTable. The entry with index 0 represents the per\-platform label space and contains parameters that apply to all interfaces that participate in the per\-platform label space. Other entries defined in this table represent additional MPLS interfaces that may participate in either the per\-platform or per\-interface label spaces, or both
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: mplsinterfacelabelminin
            
            	This is the minimum value of an MPLS label that this LSR is willing to receive on this interface
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplsinterfacelabelmaxin
            
            	This is the maximum value of an MPLS label that this LSR is willing to receive on this interface
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplsinterfacelabelminout
            
            	This is the minimum value of an MPLS label that this LSR is willing to send on this interface
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplsinterfacelabelmaxout
            
            	This is the maximum value of an MPLS label that this LSR is willing to send on this interface
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplsinterfacetotalbandwidth
            
            	This value indicates the total amount of usable bandwidth on this interface and is specified in kilobits per second (Kbps).  This variable is not applicable when applied to the interface with index 0. When this value cannot be measured, this value should contain the nominal bandwidth
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: kilobits per second
            
            .. attribute:: mplsinterfaceavailablebandwidth
            
            	This value indicates the total amount of available bandwidth available on this interface and is specified in kilobits per second (Kbps).  This value is calculated as the difference between the amount of bandwidth currently in use and that specified in mplsInterfaceTotalBandwidth.  This variable is not applicable when applied to the interface with index 0. When this value cannot be measured, this value should contain the nominal bandwidth
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplsinterfacelabelparticipationtype
            
            	If the value of the mplsInterfaceIndex for this entry is zero, then this entry corresponds to the per\-platform label space for all interfaces configured to use that label space. In this case the perPlatform(0) bit MUST be set; the perInterface(1) bit is meaningless and MUST be ignored.  The remainder of this description applies to entries with a non\-zero value of mplsInterfaceIndex.  If the perInterface(1) bit is set then the value of mplsInterfaceLabelMinIn, mplsInterfaceLabelMaxIn, mplsInterfaceLabelMinOut, and mplsInterfaceLabelMaxOut for this entry reflect the label ranges for this interface.  If only the perPlatform(0) bit is set, then the value of mplsInterfaceLabelMinIn, mplsInterfaceLabelMaxIn, mplsInterfaceLabelMinOut, and mplsInterfaceLabelMaxOut for this entry MUST be identical to the instance of these objects with index 0.  These objects may only vary from the entry with index 0 if both the perPlatform(0) and perInterface(1) bits are set.  In all cases, at a minimum one of the perPlatform(0) or perInterface(1) bits MUST be set to indicate that at least one label space is in use by this interface. In all cases, agents MUST ensure that label ranges are specified consistently and MUST return an inconsistentValue error when they do not
            	**type**\:  :py:class:`MplsInterfaceLabelParticipationType <ydk.models.cisco_ios_xe.MPLS_LSR_STD_MIB.MPLSLSRSTDMIB.MplsInterfaceTable.MplsInterfaceEntry.MplsInterfaceLabelParticipationType>`
            
            .. attribute:: mplsinterfaceperfinlabelsinuse
            
            	This object counts the number of labels that are in use at this point in time on this interface in the incoming direction. If the interface participates in only the per\-platform label space, then the value of the instance of this object MUST be identical to the value of the instance with index 0. If the interface participates in the per\-interface label space, then the instance of this object MUST represent the number of per\-interface labels that are in use on this interface
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplsinterfaceperfinlabellookupfailures
            
            	This object counts the number of labeled packets that have been received on this interface and which were discarded because there was no matching cross\- connect entry. This object MUST count on a per\- interface basis regardless of which label space the interface participates in
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplsinterfaceperfoutlabelsinuse
            
            	This object counts the number of top\-most labels in the outgoing label stacks that are in use at this point in time on this interface. This object MUST count on a per\-interface basis regardless of which label space the interface participates in
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplsinterfaceperfoutfragmentedpkts
            
            	This object counts the number of outgoing MPLS packets that required fragmentation before transmission on this interface. This object MUST count on a per\-interface basis regardless of which label space the interface participates in
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'MPLS-LSR-STD-MIB'
            _revision = '2004-06-03'

            def __init__(self):
                super(MPLSLSRSTDMIB.MplsInterfaceTable.MplsInterfaceEntry, self).__init__()

                self.yang_name = "mplsInterfaceEntry"
                self.yang_parent_name = "mplsInterfaceTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['mplsinterfaceindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('mplsinterfaceindex', (YLeaf(YType.int32, 'mplsInterfaceIndex'), ['int'])),
                    ('mplsinterfacelabelminin', (YLeaf(YType.uint32, 'mplsInterfaceLabelMinIn'), ['int'])),
                    ('mplsinterfacelabelmaxin', (YLeaf(YType.uint32, 'mplsInterfaceLabelMaxIn'), ['int'])),
                    ('mplsinterfacelabelminout', (YLeaf(YType.uint32, 'mplsInterfaceLabelMinOut'), ['int'])),
                    ('mplsinterfacelabelmaxout', (YLeaf(YType.uint32, 'mplsInterfaceLabelMaxOut'), ['int'])),
                    ('mplsinterfacetotalbandwidth', (YLeaf(YType.uint32, 'mplsInterfaceTotalBandwidth'), ['int'])),
                    ('mplsinterfaceavailablebandwidth', (YLeaf(YType.uint32, 'mplsInterfaceAvailableBandwidth'), ['int'])),
                    ('mplsinterfacelabelparticipationtype', (YLeaf(YType.bits, 'mplsInterfaceLabelParticipationType'), ['Bits'])),
                    ('mplsinterfaceperfinlabelsinuse', (YLeaf(YType.uint32, 'mplsInterfacePerfInLabelsInUse'), ['int'])),
                    ('mplsinterfaceperfinlabellookupfailures', (YLeaf(YType.uint32, 'mplsInterfacePerfInLabelLookupFailures'), ['int'])),
                    ('mplsinterfaceperfoutlabelsinuse', (YLeaf(YType.uint32, 'mplsInterfacePerfOutLabelsInUse'), ['int'])),
                    ('mplsinterfaceperfoutfragmentedpkts', (YLeaf(YType.uint32, 'mplsInterfacePerfOutFragmentedPkts'), ['int'])),
                ])
                self.mplsinterfaceindex = None
                self.mplsinterfacelabelminin = None
                self.mplsinterfacelabelmaxin = None
                self.mplsinterfacelabelminout = None
                self.mplsinterfacelabelmaxout = None
                self.mplsinterfacetotalbandwidth = None
                self.mplsinterfaceavailablebandwidth = None
                self.mplsinterfacelabelparticipationtype = Bits()
                self.mplsinterfaceperfinlabelsinuse = None
                self.mplsinterfaceperfinlabellookupfailures = None
                self.mplsinterfaceperfoutlabelsinuse = None
                self.mplsinterfaceperfoutfragmentedpkts = None
                self._segment_path = lambda: "mplsInterfaceEntry" + "[mplsInterfaceIndex='" + str(self.mplsinterfaceindex) + "']"
                self._absolute_path = lambda: "MPLS-LSR-STD-MIB:MPLS-LSR-STD-MIB/mplsInterfaceTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(MPLSLSRSTDMIB.MplsInterfaceTable.MplsInterfaceEntry, [u'mplsinterfaceindex', u'mplsinterfacelabelminin', u'mplsinterfacelabelmaxin', u'mplsinterfacelabelminout', u'mplsinterfacelabelmaxout', u'mplsinterfacetotalbandwidth', u'mplsinterfaceavailablebandwidth', u'mplsinterfacelabelparticipationtype', u'mplsinterfaceperfinlabelsinuse', u'mplsinterfaceperfinlabellookupfailures', u'mplsinterfaceperfoutlabelsinuse', u'mplsinterfaceperfoutfragmentedpkts'], name, value)


    class MplsInSegmentTable(Entity):
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
        	**type**\: list of  		 :py:class:`MplsInSegmentEntry <ydk.models.cisco_ios_xe.MPLS_LSR_STD_MIB.MPLSLSRSTDMIB.MplsInSegmentTable.MplsInSegmentEntry>`
        
        

        """

        _prefix = 'MPLS-LSR-STD-MIB'
        _revision = '2004-06-03'

        def __init__(self):
            super(MPLSLSRSTDMIB.MplsInSegmentTable, self).__init__()

            self.yang_name = "mplsInSegmentTable"
            self.yang_parent_name = "MPLS-LSR-STD-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("mplsInSegmentEntry", ("mplsinsegmententry", MPLSLSRSTDMIB.MplsInSegmentTable.MplsInSegmentEntry))])
            self._leafs = OrderedDict()

            self.mplsinsegmententry = YList(self)
            self._segment_path = lambda: "mplsInSegmentTable"
            self._absolute_path = lambda: "MPLS-LSR-STD-MIB:MPLS-LSR-STD-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(MPLSLSRSTDMIB.MplsInSegmentTable, [], name, value)


        class MplsInSegmentEntry(Entity):
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
            
            .. attribute:: mplsinsegmentindex  (key)
            
            	The index for this in\-segment. The string containing the single octet 0x00 MUST not be used as an index
            	**type**\: str
            
            	**length:** 1..24
            
            .. attribute:: mplsinsegmentinterface
            
            	This object represents the interface index for the incoming MPLS interface.  A value of zero represents all interfaces participating in the per\-platform label space.  This may only be used in cases where the incoming interface and label are associated with the same mplsXCEntry. Specifically, given a label and any incoming interface pair from the per\-platform label space, the outgoing label/interface mapping remains the same. If this is not the case, then individual entries MUST exist that can then be mapped to unique mplsXCEntries
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: mplsinsegmentlabel
            
            	If the corresponding instance of mplsInSegmentLabelPtr is zeroDotZero then this object MUST contain the incoming label associated with this in\-segment. If not this object SHOULD be zero and MUST be ignored
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplsinsegmentlabelptr
            
            	If the label for this segment cannot be represented fully within the mplsInSegmentLabel object, this object MUST point to the first accessible column of a conceptual row in an external table containing the label.  In this case, the mplsInSegmentTopLabel object SHOULD be set to 0 and ignored. This object MUST be set to zeroDotZero otherwise
            	**type**\: str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: mplsinsegmentnpop
            
            	The number of labels to pop from the incoming packet.  Normally only the top label is popped from the packet and used for all switching decisions for that packet.  This is indicated by setting this object to the default value of 1. If an LSR supports popping of more than one label, this object MUST be set to that number. This object cannot be modified if mplsInSegmentRowStatus is active(1)
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: mplsinsegmentaddrfamily
            
            	The IANA address family [IANAFamily] of packets received on this segment, which is used at an egress LSR to deliver them to the appropriate layer 3 entity. A value of other(0) indicates that the family type is either unknown or undefined; this SHOULD NOT be used at an egress LSR. This object cannot be modified if mplsInSegmentRowStatus is active(1)
            	**type**\:  :py:class:`AddressFamilyNumbers <ydk.models.cisco_ios_xe.IANA_ADDRESS_FAMILY_NUMBERS_MIB.AddressFamilyNumbers>`
            
            .. attribute:: mplsinsegmentxcindex
            
            	Index into mplsXCTable which identifies which cross\- connect entry this segment is part of.  The string containing the single octet 0x00 indicates that this entry is not referred to by any cross\-connect entry. When a cross\-connect entry is created which this in\-segment is a part of, this object is automatically updated to reflect the value of mplsXCIndex of that cross\-connect entry
            	**type**\: str
            
            	**length:** 1..24
            
            .. attribute:: mplsinsegmentowner
            
            	Denotes the entity that created and is responsible for managing this segment
            	**type**\:  :py:class:`MplsOwner <ydk.models.cisco_ios_xe.MPLS_TC_STD_MIB.MplsOwner>`
            
            .. attribute:: mplsinsegmenttrafficparamptr
            
            	This variable represents a pointer to the traffic parameter specification for this in\-segment.  This value may point at an entry in the mplsTunnelResourceTable in the MPLS\-TE\-STD\-MIB (RFC3812) to indicate which traffic parameter settings for this segment if it represents an LSP used for a TE tunnel.  This value may optionally point at an externally defined traffic parameter specification table.  A value of zeroDotZero indicates best\-effort treatment.  By having the same value of this object, two or more segments can indicate resource sharing of such things as LSP queue space, etc.  This object cannot be modified if mplsInSegmentRowStatus is active(1).  For entries in this table that are preserved after a re\-boot, the agent MUST ensure that their integrity be preserved, or this object should be set to 0.0 if it cannot
            	**type**\: str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: mplsinsegmentrowstatus
            
            	This variable is used to create, modify, and/or delete a row in this table. When a row in this table has a row in the active(1) state, no objects in this row can be modified except the mplsInSegmentRowStatus and mplsInSegmentStorageType
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            .. attribute:: mplsinsegmentstoragetype
            
            	This variable indicates the storage type for this object. The agent MUST ensure that this object's value remains consistent with the associated mplsXCEntry. Conceptual rows having the value 'permanent' need not allow write\-access to any columnar objects in the row
            	**type**\:  :py:class:`StorageType <ydk.models.cisco_ios_xe.SNMPv2_TC.StorageType>`
            
            .. attribute:: mplsinsegmentperfoctets
            
            	This value represents the total number of octets received by this segment. It MUST be equal to the least significant 32 bits of mplsInSegmentPerfHCOctets if mplsInSegmentPerfHCOctets is supported according to the rules spelled out in RFC2863
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplsinsegmentperfpackets
            
            	Total number of packets received by this segment
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplsinsegmentperferrors
            
            	The number of errored packets received on this segment
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplsinsegmentperfdiscards
            
            	The number of labeled packets received on this in\- segment, which were chosen to be discarded even though no errors had been detected to prevent their being transmitted.  One possible reason for discarding such a labeled packet could be to free up buffer space
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplsinsegmentperfhcoctets
            
            	The total number of octets received.  This is the 64 bit version of mplsInSegmentPerfOctets, if mplsInSegmentPerfHCOctets is supported according to the rules spelled out in RFC2863
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: mplsinsegmentperfdiscontinuitytime
            
            	The value of sysUpTime on the most recent occasion at which any one or more of this segment's Counter32 or Counter64 suffered a discontinuity. If no such discontinuities have occurred since the last re\- initialization of the local management subsystem, then this object contains a zero value
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'MPLS-LSR-STD-MIB'
            _revision = '2004-06-03'

            def __init__(self):
                super(MPLSLSRSTDMIB.MplsInSegmentTable.MplsInSegmentEntry, self).__init__()

                self.yang_name = "mplsInSegmentEntry"
                self.yang_parent_name = "mplsInSegmentTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['mplsinsegmentindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('mplsinsegmentindex', (YLeaf(YType.str, 'mplsInSegmentIndex'), ['str'])),
                    ('mplsinsegmentinterface', (YLeaf(YType.int32, 'mplsInSegmentInterface'), ['int'])),
                    ('mplsinsegmentlabel', (YLeaf(YType.uint32, 'mplsInSegmentLabel'), ['int'])),
                    ('mplsinsegmentlabelptr', (YLeaf(YType.str, 'mplsInSegmentLabelPtr'), ['str'])),
                    ('mplsinsegmentnpop', (YLeaf(YType.int32, 'mplsInSegmentNPop'), ['int'])),
                    ('mplsinsegmentaddrfamily', (YLeaf(YType.enumeration, 'mplsInSegmentAddrFamily'), [('ydk.models.cisco_ios_xe.IANA_ADDRESS_FAMILY_NUMBERS_MIB', 'AddressFamilyNumbers', '')])),
                    ('mplsinsegmentxcindex', (YLeaf(YType.str, 'mplsInSegmentXCIndex'), ['str'])),
                    ('mplsinsegmentowner', (YLeaf(YType.enumeration, 'mplsInSegmentOwner'), [('ydk.models.cisco_ios_xe.MPLS_TC_STD_MIB', 'MplsOwner', '')])),
                    ('mplsinsegmenttrafficparamptr', (YLeaf(YType.str, 'mplsInSegmentTrafficParamPtr'), ['str'])),
                    ('mplsinsegmentrowstatus', (YLeaf(YType.enumeration, 'mplsInSegmentRowStatus'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowStatus', '')])),
                    ('mplsinsegmentstoragetype', (YLeaf(YType.enumeration, 'mplsInSegmentStorageType'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'StorageType', '')])),
                    ('mplsinsegmentperfoctets', (YLeaf(YType.uint32, 'mplsInSegmentPerfOctets'), ['int'])),
                    ('mplsinsegmentperfpackets', (YLeaf(YType.uint32, 'mplsInSegmentPerfPackets'), ['int'])),
                    ('mplsinsegmentperferrors', (YLeaf(YType.uint32, 'mplsInSegmentPerfErrors'), ['int'])),
                    ('mplsinsegmentperfdiscards', (YLeaf(YType.uint32, 'mplsInSegmentPerfDiscards'), ['int'])),
                    ('mplsinsegmentperfhcoctets', (YLeaf(YType.uint64, 'mplsInSegmentPerfHCOctets'), ['int'])),
                    ('mplsinsegmentperfdiscontinuitytime', (YLeaf(YType.uint32, 'mplsInSegmentPerfDiscontinuityTime'), ['int'])),
                ])
                self.mplsinsegmentindex = None
                self.mplsinsegmentinterface = None
                self.mplsinsegmentlabel = None
                self.mplsinsegmentlabelptr = None
                self.mplsinsegmentnpop = None
                self.mplsinsegmentaddrfamily = None
                self.mplsinsegmentxcindex = None
                self.mplsinsegmentowner = None
                self.mplsinsegmenttrafficparamptr = None
                self.mplsinsegmentrowstatus = None
                self.mplsinsegmentstoragetype = None
                self.mplsinsegmentperfoctets = None
                self.mplsinsegmentperfpackets = None
                self.mplsinsegmentperferrors = None
                self.mplsinsegmentperfdiscards = None
                self.mplsinsegmentperfhcoctets = None
                self.mplsinsegmentperfdiscontinuitytime = None
                self._segment_path = lambda: "mplsInSegmentEntry" + "[mplsInSegmentIndex='" + str(self.mplsinsegmentindex) + "']"
                self._absolute_path = lambda: "MPLS-LSR-STD-MIB:MPLS-LSR-STD-MIB/mplsInSegmentTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(MPLSLSRSTDMIB.MplsInSegmentTable.MplsInSegmentEntry, [u'mplsinsegmentindex', u'mplsinsegmentinterface', u'mplsinsegmentlabel', u'mplsinsegmentlabelptr', u'mplsinsegmentnpop', u'mplsinsegmentaddrfamily', u'mplsinsegmentxcindex', u'mplsinsegmentowner', u'mplsinsegmenttrafficparamptr', u'mplsinsegmentrowstatus', u'mplsinsegmentstoragetype', u'mplsinsegmentperfoctets', u'mplsinsegmentperfpackets', u'mplsinsegmentperferrors', u'mplsinsegmentperfdiscards', u'mplsinsegmentperfhcoctets', u'mplsinsegmentperfdiscontinuitytime'], name, value)


    class MplsOutSegmentTable(Entity):
        """
        This table contains a representation of the outgoing
        segments from an LSR.
        
        .. attribute:: mplsoutsegmententry
        
        	An entry in this table represents one outgoing segment.  An entry can be created by a network administrator, an SNMP agent, or an MPLS signaling protocol.  The object mplsOutSegmentOwner indicates the creator of this entry. The value of mplsOutSegmentRowStatus cannot be active(1) unless the ifTable entry corresponding to mplsOutSegmentInterface exists.  Note that the indexing of this table uses a single, arbitrary index (mplsOutSegmentIndex) to indicate which out\-segment (i.e.\: label) is being switched to from which in\-segment (i.e\: label) or in\-segments. This is necessary because it is possible to have an equal\-cost multi\-path situation where two identical out\-going labels are assigned to the same cross\-connect (i.e.\: they go to two different neighboring LSRs); thus, requiring two out\-segments. In order to preserve the uniqueness of the references by the mplsXCEntry, an arbitrary integer must be used as the index for this table
        	**type**\: list of  		 :py:class:`MplsOutSegmentEntry <ydk.models.cisco_ios_xe.MPLS_LSR_STD_MIB.MPLSLSRSTDMIB.MplsOutSegmentTable.MplsOutSegmentEntry>`
        
        

        """

        _prefix = 'MPLS-LSR-STD-MIB'
        _revision = '2004-06-03'

        def __init__(self):
            super(MPLSLSRSTDMIB.MplsOutSegmentTable, self).__init__()

            self.yang_name = "mplsOutSegmentTable"
            self.yang_parent_name = "MPLS-LSR-STD-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("mplsOutSegmentEntry", ("mplsoutsegmententry", MPLSLSRSTDMIB.MplsOutSegmentTable.MplsOutSegmentEntry))])
            self._leafs = OrderedDict()

            self.mplsoutsegmententry = YList(self)
            self._segment_path = lambda: "mplsOutSegmentTable"
            self._absolute_path = lambda: "MPLS-LSR-STD-MIB:MPLS-LSR-STD-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(MPLSLSRSTDMIB.MplsOutSegmentTable, [], name, value)


        class MplsOutSegmentEntry(Entity):
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
            
            .. attribute:: mplsoutsegmentindex  (key)
            
            	This value contains a unique index for this row. While a value of a string containing the single octet 0x00 is not valid as an index for entries in this table, it can be supplied as a valid value to index the mplsXCTable to represent entries for which no out\-segment has been configured or exists
            	**type**\: str
            
            	**length:** 1..24
            
            .. attribute:: mplsoutsegmentinterface
            
            	This value must contain the interface index of the outgoing interface. This object cannot be modified if mplsOutSegmentRowStatus is active(1). The mplsOutSegmentRowStatus cannot be set to active(1) until this object is set to a value corresponding to a valid ifEntry
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: mplsoutsegmentpushtoplabel
            
            	This value indicates whether or not a top label should be pushed onto the outgoing packet's label stack.  The value of this variable MUST be set to true(1) if the outgoing interface does not support pop\-and\-go (and no label stack remains). For example, on ATM interface, or if the segment represents a tunnel origination.  Note that it is considered an error in the case that mplsOutSegmentPushTopLabel is set to false, but the cross\-connect entry which refers to this out\-segment has a non\-zero mplsLabelStackIndex.  The LSR MUST ensure that this situation does not happen. This object cannot be modified if mplsOutSegmentRowStatus is active(1)
            	**type**\: bool
            
            .. attribute:: mplsoutsegmenttoplabel
            
            	If mplsOutSegmentPushTopLabel is true then this represents the label that should be pushed onto the top of the outgoing packet's label stack. Otherwise this value SHOULD be set to 0 by the management station and MUST be ignored by the agent. This object cannot be modified if mplsOutSegmentRowStatus is active(1)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplsoutsegmenttoplabelptr
            
            	If the label for this segment cannot be represented fully within the mplsOutSegmentLabel object, this object MUST point to the first accessible column of a conceptual row in an external table containing the label.  In this case, the mplsOutSegmentTopLabel object SHOULD be set to 0 and ignored. This object MUST be set to zeroDotZero otherwise
            	**type**\: str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: mplsoutsegmentnexthopaddrtype
            
            	Indicates the next hop Internet address type. Only values unknown(0), ipv4(1) or ipv6(2) have to be supported.  A value of unknown(0) is allowed only when the outgoing interface is of type point\-to\-point. If any other unsupported values are attempted in a set operation, the agent MUST return an inconsistentValue error
            	**type**\:  :py:class:`InetAddressType <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetAddressType>`
            
            .. attribute:: mplsoutsegmentnexthopaddr
            
            	The internet address of the next hop. The type of this address is determined by the value of the mplslOutSegmentNextHopAddrType object.  This object cannot be modified if mplsOutSegmentRowStatus is active(1)
            	**type**\: str
            
            	**length:** 0..255
            
            .. attribute:: mplsoutsegmentxcindex
            
            	Index into mplsXCTable which identifies which cross\- connect entry this segment is part of.  A value of the string containing the single octet 0x00 indicates that this entry is not referred to by any cross\-connect entry.  When a cross\-connect entry is created which this out\-segment is a part of, this object MUST be updated by the agent to reflect the value of mplsXCIndex of that cross\-connect entry
            	**type**\: str
            
            	**length:** 1..24
            
            .. attribute:: mplsoutsegmentowner
            
            	Denotes the entity which created and is responsible for managing this segment
            	**type**\:  :py:class:`MplsOwner <ydk.models.cisco_ios_xe.MPLS_TC_STD_MIB.MplsOwner>`
            
            .. attribute:: mplsoutsegmenttrafficparamptr
            
            	This variable represents a pointer to the traffic parameter specification for this out\-segment.  This value may point at an entry in the MplsTunnelResourceEntry in the MPLS\-TE\-STD\-MIB (RFC3812)  RFC Editor\: Please fill in RFC number.  to indicate which traffic parameter settings for this segment if it represents an LSP used for a TE tunnel.  This value may optionally point at an externally defined traffic parameter specification table.  A value of zeroDotZero indicates best\-effort treatment.  By having the same value of this object, two or more segments can indicate resource sharing of such things as LSP queue space, etc.  This object cannot be modified if mplsOutSegmentRowStatus is active(1). For entries in this table that are preserved after a re\-boot, the agent MUST ensure that their integrity be preserved, or this object should be set to 0.0 if it cannot
            	**type**\: str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: mplsoutsegmentrowstatus
            
            	For creating, modifying, and deleting this row. When a row in this table has a row in the active(1) state, no objects in this row can be modified except the mplsOutSegmentRowStatus or mplsOutSegmentStorageType
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            .. attribute:: mplsoutsegmentstoragetype
            
            	This variable indicates the storage type for this object. The agent MUST ensure that this object's value remains consistent with the associated mplsXCEntry. Conceptual rows having the value 'permanent' need not allow write\-access to any columnar objects in the row
            	**type**\:  :py:class:`StorageType <ydk.models.cisco_ios_xe.SNMPv2_TC.StorageType>`
            
            .. attribute:: mplsoutsegmentperfoctets
            
            	This value contains the total number of octets sent on this segment. It MUST be equal to the least significant 32 bits of mplsOutSegmentPerfHCOctets if mplsOutSegmentPerfHCOctets is supported according to the rules spelled out in RFC2863
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplsoutsegmentperfpackets
            
            	This value contains the total number of packets sent on this segment
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplsoutsegmentperferrors
            
            	Number of packets that could not be sent due to errors on this segment
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplsoutsegmentperfdiscards
            
            	The number of labeled packets attempted to be transmitted on this out\-segment, which were chosen to be discarded even though no errors had been detected to prevent their being transmitted. One possible reason for discarding such a labeled packet could be to free up buffer space
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplsoutsegmentperfhcoctets
            
            	Total number of octets sent.  This is the 64 bit version of mplsOutSegmentPerfOctets, if mplsOutSegmentPerfHCOctets is supported according to the rules spelled out in RFC2863
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: mplsoutsegmentperfdiscontinuitytime
            
            	The value of sysUpTime on the most recent occasion at which any one or more of this segment's Counter32 or Counter64 suffered a discontinuity. If no such discontinuities have occurred since the last re\- initialization of the local management subsystem, then this object contains a zero value
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'MPLS-LSR-STD-MIB'
            _revision = '2004-06-03'

            def __init__(self):
                super(MPLSLSRSTDMIB.MplsOutSegmentTable.MplsOutSegmentEntry, self).__init__()

                self.yang_name = "mplsOutSegmentEntry"
                self.yang_parent_name = "mplsOutSegmentTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['mplsoutsegmentindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('mplsoutsegmentindex', (YLeaf(YType.str, 'mplsOutSegmentIndex'), ['str'])),
                    ('mplsoutsegmentinterface', (YLeaf(YType.int32, 'mplsOutSegmentInterface'), ['int'])),
                    ('mplsoutsegmentpushtoplabel', (YLeaf(YType.boolean, 'mplsOutSegmentPushTopLabel'), ['bool'])),
                    ('mplsoutsegmenttoplabel', (YLeaf(YType.uint32, 'mplsOutSegmentTopLabel'), ['int'])),
                    ('mplsoutsegmenttoplabelptr', (YLeaf(YType.str, 'mplsOutSegmentTopLabelPtr'), ['str'])),
                    ('mplsoutsegmentnexthopaddrtype', (YLeaf(YType.enumeration, 'mplsOutSegmentNextHopAddrType'), [('ydk.models.cisco_ios_xe.INET_ADDRESS_MIB', 'InetAddressType', '')])),
                    ('mplsoutsegmentnexthopaddr', (YLeaf(YType.str, 'mplsOutSegmentNextHopAddr'), ['str'])),
                    ('mplsoutsegmentxcindex', (YLeaf(YType.str, 'mplsOutSegmentXCIndex'), ['str'])),
                    ('mplsoutsegmentowner', (YLeaf(YType.enumeration, 'mplsOutSegmentOwner'), [('ydk.models.cisco_ios_xe.MPLS_TC_STD_MIB', 'MplsOwner', '')])),
                    ('mplsoutsegmenttrafficparamptr', (YLeaf(YType.str, 'mplsOutSegmentTrafficParamPtr'), ['str'])),
                    ('mplsoutsegmentrowstatus', (YLeaf(YType.enumeration, 'mplsOutSegmentRowStatus'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowStatus', '')])),
                    ('mplsoutsegmentstoragetype', (YLeaf(YType.enumeration, 'mplsOutSegmentStorageType'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'StorageType', '')])),
                    ('mplsoutsegmentperfoctets', (YLeaf(YType.uint32, 'mplsOutSegmentPerfOctets'), ['int'])),
                    ('mplsoutsegmentperfpackets', (YLeaf(YType.uint32, 'mplsOutSegmentPerfPackets'), ['int'])),
                    ('mplsoutsegmentperferrors', (YLeaf(YType.uint32, 'mplsOutSegmentPerfErrors'), ['int'])),
                    ('mplsoutsegmentperfdiscards', (YLeaf(YType.uint32, 'mplsOutSegmentPerfDiscards'), ['int'])),
                    ('mplsoutsegmentperfhcoctets', (YLeaf(YType.uint64, 'mplsOutSegmentPerfHCOctets'), ['int'])),
                    ('mplsoutsegmentperfdiscontinuitytime', (YLeaf(YType.uint32, 'mplsOutSegmentPerfDiscontinuityTime'), ['int'])),
                ])
                self.mplsoutsegmentindex = None
                self.mplsoutsegmentinterface = None
                self.mplsoutsegmentpushtoplabel = None
                self.mplsoutsegmenttoplabel = None
                self.mplsoutsegmenttoplabelptr = None
                self.mplsoutsegmentnexthopaddrtype = None
                self.mplsoutsegmentnexthopaddr = None
                self.mplsoutsegmentxcindex = None
                self.mplsoutsegmentowner = None
                self.mplsoutsegmenttrafficparamptr = None
                self.mplsoutsegmentrowstatus = None
                self.mplsoutsegmentstoragetype = None
                self.mplsoutsegmentperfoctets = None
                self.mplsoutsegmentperfpackets = None
                self.mplsoutsegmentperferrors = None
                self.mplsoutsegmentperfdiscards = None
                self.mplsoutsegmentperfhcoctets = None
                self.mplsoutsegmentperfdiscontinuitytime = None
                self._segment_path = lambda: "mplsOutSegmentEntry" + "[mplsOutSegmentIndex='" + str(self.mplsoutsegmentindex) + "']"
                self._absolute_path = lambda: "MPLS-LSR-STD-MIB:MPLS-LSR-STD-MIB/mplsOutSegmentTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(MPLSLSRSTDMIB.MplsOutSegmentTable.MplsOutSegmentEntry, [u'mplsoutsegmentindex', u'mplsoutsegmentinterface', u'mplsoutsegmentpushtoplabel', u'mplsoutsegmenttoplabel', u'mplsoutsegmenttoplabelptr', u'mplsoutsegmentnexthopaddrtype', u'mplsoutsegmentnexthopaddr', u'mplsoutsegmentxcindex', u'mplsoutsegmentowner', u'mplsoutsegmenttrafficparamptr', u'mplsoutsegmentrowstatus', u'mplsoutsegmentstoragetype', u'mplsoutsegmentperfoctets', u'mplsoutsegmentperfpackets', u'mplsoutsegmentperferrors', u'mplsoutsegmentperfdiscards', u'mplsoutsegmentperfhcoctets', u'mplsoutsegmentperfdiscontinuitytime'], name, value)


    class MplsXCTable(Entity):
        """
        This table specifies information for switching
        between LSP segments.  It supports point\-to\-point,
        point\-to\-multipoint and multipoint\-to\-point
        connections.  mplsLabelStackTable specifies the
        label stack information for a cross\-connect LSR and
        is referred to from mplsXCTable.
        
        .. attribute:: mplsxcentry
        
        	A row in this table represents one cross\-connect entry.  It is indexed by the following objects\:  \- cross\-connect index mplsXCIndex that uniquely   identifies a group of cross\-connect entries  \- in\-segment index, mplsXCInSegmentIndex  \- out\-segment index, mplsXCOutSegmentIndex  LSPs originating at this LSR\: These are represented by using the special of value of mplsXCInSegmentIndex set to the string containing a single octet 0x00. In this case the mplsXCOutSegmentIndex MUST not be the string containing a single octet 0x00.  LSPs terminating at this LSR\: These are represented by using the special value mplsXCOutSegmentIndex set to the string containing a single octet 0x00.  Special labels\: Entries indexed by the strings containing the reserved MPLS label values as a single octet 0x00 through 0x0f (inclusive) imply LSPs terminating at this LSR.  Note that situations where LSPs are terminated with incoming label equal to the string containing a single octet 0x00 can be distinguished from LSPs originating at this LSR because the mplsXCOutSegmentIndex equals the string containing the single octet 0x00.  An entry can be created by a network administrator or by an SNMP agent as instructed by an MPLS signaling protocol
        	**type**\: list of  		 :py:class:`MplsXCEntry <ydk.models.cisco_ios_xe.MPLS_LSR_STD_MIB.MPLSLSRSTDMIB.MplsXCTable.MplsXCEntry>`
        
        

        """

        _prefix = 'MPLS-LSR-STD-MIB'
        _revision = '2004-06-03'

        def __init__(self):
            super(MPLSLSRSTDMIB.MplsXCTable, self).__init__()

            self.yang_name = "mplsXCTable"
            self.yang_parent_name = "MPLS-LSR-STD-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("mplsXCEntry", ("mplsxcentry", MPLSLSRSTDMIB.MplsXCTable.MplsXCEntry))])
            self._leafs = OrderedDict()

            self.mplsxcentry = YList(self)
            self._segment_path = lambda: "mplsXCTable"
            self._absolute_path = lambda: "MPLS-LSR-STD-MIB:MPLS-LSR-STD-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(MPLSLSRSTDMIB.MplsXCTable, [], name, value)


        class MplsXCEntry(Entity):
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
            
            .. attribute:: mplsxcindex  (key)
            
            	Primary index for the conceptual row identifying a group of cross\-connect segments. The string containing a single octet 0x00 is an invalid index
            	**type**\: str
            
            	**length:** 1..24
            
            .. attribute:: mplsxcinsegmentindex  (key)
            
            	Incoming label index. If this object is set to the string containing a single octet 0x00, this indicates a special case outlined in the table's description above. In this case no corresponding mplsInSegmentEntry shall exist
            	**type**\: str
            
            	**length:** 1..24
            
            .. attribute:: mplsxcoutsegmentindex  (key)
            
            	Index of out\-segment for LSPs not terminating on this LSR if not set to the string containing the single octet 0x00. If the segment identified by this entry is terminating, then this object MUST be set to the string containing a single octet 0x00 to indicate that no corresponding mplsOutSegmentEntry shall exist
            	**type**\: str
            
            	**length:** 1..24
            
            .. attribute:: mplsxclspid
            
            	This value identifies the label switched path that this cross\-connect entry belongs to. This object cannot be modified if mplsXCRowStatus is active(1) except for this object
            	**type**\: str
            
            	**length:** 2 \| 6
            
            .. attribute:: mplsxclabelstackindex
            
            	Primary index into mplsLabelStackTable identifying a stack of labels to be pushed beneath the top label. Note that the top label identified by the out\- segment ensures that all the components of a multipoint\-to\-point connection have the same outgoing label. A value of the string containing the single octet 0x00 indicates that no labels are to be stacked beneath the top label. This object cannot be modified if mplsXCRowStatus is active(1)
            	**type**\: str
            
            	**length:** 1..24
            
            .. attribute:: mplsxcowner
            
            	Denotes the entity that created and is responsible for managing this cross\-connect
            	**type**\:  :py:class:`MplsOwner <ydk.models.cisco_ios_xe.MPLS_TC_STD_MIB.MplsOwner>`
            
            .. attribute:: mplsxcrowstatus
            
            	For creating, modifying, and deleting this row. When a row in this table has a row in the active(1) state, no objects in this row except this object and the mplsXCStorageType can be modified. 
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            .. attribute:: mplsxcstoragetype
            
            	This variable indicates the storage type for this object. The agent MUST ensure that the associated in and out segments also have the same StorageType value and are restored consistently upon system restart. This value SHOULD be set to permanent(4) if created as a result of a static LSP configuration.  Conceptual rows having the value 'permanent' need not allow write\-access to any columnar objects in the row
            	**type**\:  :py:class:`StorageType <ydk.models.cisco_ios_xe.SNMPv2_TC.StorageType>`
            
            .. attribute:: mplsxcadminstatus
            
            	The desired operational status of this segment
            	**type**\:  :py:class:`MplsXCAdminStatus <ydk.models.cisco_ios_xe.MPLS_LSR_STD_MIB.MPLSLSRSTDMIB.MplsXCTable.MplsXCEntry.MplsXCAdminStatus>`
            
            .. attribute:: mplsxcoperstatus
            
            	The actual operational status of this cross\- connect
            	**type**\:  :py:class:`MplsXCOperStatus <ydk.models.cisco_ios_xe.MPLS_LSR_STD_MIB.MPLSLSRSTDMIB.MplsXCTable.MplsXCEntry.MplsXCOperStatus>`
            
            

            """

            _prefix = 'MPLS-LSR-STD-MIB'
            _revision = '2004-06-03'

            def __init__(self):
                super(MPLSLSRSTDMIB.MplsXCTable.MplsXCEntry, self).__init__()

                self.yang_name = "mplsXCEntry"
                self.yang_parent_name = "mplsXCTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['mplsxcindex','mplsxcinsegmentindex','mplsxcoutsegmentindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('mplsxcindex', (YLeaf(YType.str, 'mplsXCIndex'), ['str'])),
                    ('mplsxcinsegmentindex', (YLeaf(YType.str, 'mplsXCInSegmentIndex'), ['str'])),
                    ('mplsxcoutsegmentindex', (YLeaf(YType.str, 'mplsXCOutSegmentIndex'), ['str'])),
                    ('mplsxclspid', (YLeaf(YType.str, 'mplsXCLspId'), ['str'])),
                    ('mplsxclabelstackindex', (YLeaf(YType.str, 'mplsXCLabelStackIndex'), ['str'])),
                    ('mplsxcowner', (YLeaf(YType.enumeration, 'mplsXCOwner'), [('ydk.models.cisco_ios_xe.MPLS_TC_STD_MIB', 'MplsOwner', '')])),
                    ('mplsxcrowstatus', (YLeaf(YType.enumeration, 'mplsXCRowStatus'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowStatus', '')])),
                    ('mplsxcstoragetype', (YLeaf(YType.enumeration, 'mplsXCStorageType'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'StorageType', '')])),
                    ('mplsxcadminstatus', (YLeaf(YType.enumeration, 'mplsXCAdminStatus'), [('ydk.models.cisco_ios_xe.MPLS_LSR_STD_MIB', 'MPLSLSRSTDMIB', 'MplsXCTable.MplsXCEntry.MplsXCAdminStatus')])),
                    ('mplsxcoperstatus', (YLeaf(YType.enumeration, 'mplsXCOperStatus'), [('ydk.models.cisco_ios_xe.MPLS_LSR_STD_MIB', 'MPLSLSRSTDMIB', 'MplsXCTable.MplsXCEntry.MplsXCOperStatus')])),
                ])
                self.mplsxcindex = None
                self.mplsxcinsegmentindex = None
                self.mplsxcoutsegmentindex = None
                self.mplsxclspid = None
                self.mplsxclabelstackindex = None
                self.mplsxcowner = None
                self.mplsxcrowstatus = None
                self.mplsxcstoragetype = None
                self.mplsxcadminstatus = None
                self.mplsxcoperstatus = None
                self._segment_path = lambda: "mplsXCEntry" + "[mplsXCIndex='" + str(self.mplsxcindex) + "']" + "[mplsXCInSegmentIndex='" + str(self.mplsxcinsegmentindex) + "']" + "[mplsXCOutSegmentIndex='" + str(self.mplsxcoutsegmentindex) + "']"
                self._absolute_path = lambda: "MPLS-LSR-STD-MIB:MPLS-LSR-STD-MIB/mplsXCTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(MPLSLSRSTDMIB.MplsXCTable.MplsXCEntry, [u'mplsxcindex', u'mplsxcinsegmentindex', u'mplsxcoutsegmentindex', u'mplsxclspid', u'mplsxclabelstackindex', u'mplsxcowner', u'mplsxcrowstatus', u'mplsxcstoragetype', u'mplsxcadminstatus', u'mplsxcoperstatus'], name, value)

            class MplsXCAdminStatus(Enum):
                """
                MplsXCAdminStatus (Enum Class)

                The desired operational status of this segment.

                .. data:: up = 1

                .. data:: down = 2

                .. data:: testing = 3

                """

                up = Enum.YLeaf(1, "up")

                down = Enum.YLeaf(2, "down")

                testing = Enum.YLeaf(3, "testing")


            class MplsXCOperStatus(Enum):
                """
                MplsXCOperStatus (Enum Class)

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



    class MplsLabelStackTable(Entity):
        """
        This table specifies the label stack to be pushed
        onto a packet, beneath the top label.  Entries into
        this table are referred to from mplsXCTable.
        
        .. attribute:: mplslabelstackentry
        
        	An entry in this table represents one label which is to be pushed onto an outgoing packet, beneath the top label.  An entry can be created by a network administrator or by an SNMP agent as instructed by an MPLS signaling protocol
        	**type**\: list of  		 :py:class:`MplsLabelStackEntry <ydk.models.cisco_ios_xe.MPLS_LSR_STD_MIB.MPLSLSRSTDMIB.MplsLabelStackTable.MplsLabelStackEntry>`
        
        

        """

        _prefix = 'MPLS-LSR-STD-MIB'
        _revision = '2004-06-03'

        def __init__(self):
            super(MPLSLSRSTDMIB.MplsLabelStackTable, self).__init__()

            self.yang_name = "mplsLabelStackTable"
            self.yang_parent_name = "MPLS-LSR-STD-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("mplsLabelStackEntry", ("mplslabelstackentry", MPLSLSRSTDMIB.MplsLabelStackTable.MplsLabelStackEntry))])
            self._leafs = OrderedDict()

            self.mplslabelstackentry = YList(self)
            self._segment_path = lambda: "mplsLabelStackTable"
            self._absolute_path = lambda: "MPLS-LSR-STD-MIB:MPLS-LSR-STD-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(MPLSLSRSTDMIB.MplsLabelStackTable, [], name, value)


        class MplsLabelStackEntry(Entity):
            """
            An entry in this table represents one label which is
            to be pushed onto an outgoing packet, beneath the
            top label.  An entry can be created by a network
            administrator or by an SNMP agent as instructed by
            an MPLS signaling protocol.
            
            .. attribute:: mplslabelstackindex  (key)
            
            	Primary index for this row identifying a stack of labels to be pushed on an outgoing packet, beneath the top label. An index containing the string with a single octet 0x00 MUST not be used
            	**type**\: str
            
            	**length:** 1..24
            
            .. attribute:: mplslabelstacklabelindex  (key)
            
            	Secondary index for this row identifying one label of the stack.  Note that an entry with a smaller mplsLabelStackLabelIndex would refer to a label higher up the label stack and would be popped at a downstream LSR before a label represented by a higher mplsLabelStackLabelIndex at a downstream LSR
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: mplslabelstacklabel
            
            	The label to pushed
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplslabelstacklabelptr
            
            	If the label for this segment cannot be represented fully within the mplsLabelStackLabel object, this object MUST point to the first accessible column of a conceptual row in an external table containing the label.  In this case, the mplsLabelStackLabel object SHOULD be set to 0 and ignored. This object MUST be set to zeroDotZero otherwise
            	**type**\: str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: mplslabelstackrowstatus
            
            	For creating, modifying, and deleting this row. When a row in this table has a row in the active(1) state, no objects in this row except this object and the mplsLabelStackStorageType can be modified
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            .. attribute:: mplslabelstackstoragetype
            
            	This variable indicates the storage type for this object. This object cannot be modified if mplsLabelStackRowStatus is active(1). No objects are required to be writable for rows in this table with this object set to permanent(4).  The agent MUST ensure that all related entries in this table retain the same value for this object.  Agents MUST ensure that the storage type for all entries related to a particular mplsXCEntry retain the same value for this object as the mplsXCEntry's StorageType
            	**type**\:  :py:class:`StorageType <ydk.models.cisco_ios_xe.SNMPv2_TC.StorageType>`
            
            

            """

            _prefix = 'MPLS-LSR-STD-MIB'
            _revision = '2004-06-03'

            def __init__(self):
                super(MPLSLSRSTDMIB.MplsLabelStackTable.MplsLabelStackEntry, self).__init__()

                self.yang_name = "mplsLabelStackEntry"
                self.yang_parent_name = "mplsLabelStackTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['mplslabelstackindex','mplslabelstacklabelindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('mplslabelstackindex', (YLeaf(YType.str, 'mplsLabelStackIndex'), ['str'])),
                    ('mplslabelstacklabelindex', (YLeaf(YType.uint32, 'mplsLabelStackLabelIndex'), ['int'])),
                    ('mplslabelstacklabel', (YLeaf(YType.uint32, 'mplsLabelStackLabel'), ['int'])),
                    ('mplslabelstacklabelptr', (YLeaf(YType.str, 'mplsLabelStackLabelPtr'), ['str'])),
                    ('mplslabelstackrowstatus', (YLeaf(YType.enumeration, 'mplsLabelStackRowStatus'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowStatus', '')])),
                    ('mplslabelstackstoragetype', (YLeaf(YType.enumeration, 'mplsLabelStackStorageType'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'StorageType', '')])),
                ])
                self.mplslabelstackindex = None
                self.mplslabelstacklabelindex = None
                self.mplslabelstacklabel = None
                self.mplslabelstacklabelptr = None
                self.mplslabelstackrowstatus = None
                self.mplslabelstackstoragetype = None
                self._segment_path = lambda: "mplsLabelStackEntry" + "[mplsLabelStackIndex='" + str(self.mplslabelstackindex) + "']" + "[mplsLabelStackLabelIndex='" + str(self.mplslabelstacklabelindex) + "']"
                self._absolute_path = lambda: "MPLS-LSR-STD-MIB:MPLS-LSR-STD-MIB/mplsLabelStackTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(MPLSLSRSTDMIB.MplsLabelStackTable.MplsLabelStackEntry, [u'mplslabelstackindex', u'mplslabelstacklabelindex', u'mplslabelstacklabel', u'mplslabelstacklabelptr', u'mplslabelstackrowstatus', u'mplslabelstackstoragetype'], name, value)


    class MplsInSegmentMapTable(Entity):
        """
        This table specifies the mapping from the
        mplsInSegmentIndex to the corresponding
        mplsInSegmentInterface and mplsInSegmentLabel
        objects. The purpose of this table is to
        provide the manager with an alternative
        means by which to locate in\-segments.
        
        .. attribute:: mplsinsegmentmapentry
        
        	An entry in this table represents one interface and incoming label pair.  In cases where the label cannot fit into the mplsInSegmentLabel object, the mplsInSegmentLabelPtr will indicate this by being set to the first accessible column in the appropriate extension table's row, and the mplsInSegmentLabel SHOULD be set to 0. In all other cases when the label is represented within the mplsInSegmentLabel object, the mplsInSegmentLabelPtr MUST be 0.0.  Implementors need to be aware that if the value of the mplsInSegmentMapLabelPtrIndex (an OID) has more that 111 sub\-identifiers, then OIDs of column instances in this table will have more than 128 sub\-identifiers and cannot be accessed using SNMPv1, SNMPv2c, or SNMPv3
        	**type**\: list of  		 :py:class:`MplsInSegmentMapEntry <ydk.models.cisco_ios_xe.MPLS_LSR_STD_MIB.MPLSLSRSTDMIB.MplsInSegmentMapTable.MplsInSegmentMapEntry>`
        
        

        """

        _prefix = 'MPLS-LSR-STD-MIB'
        _revision = '2004-06-03'

        def __init__(self):
            super(MPLSLSRSTDMIB.MplsInSegmentMapTable, self).__init__()

            self.yang_name = "mplsInSegmentMapTable"
            self.yang_parent_name = "MPLS-LSR-STD-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("mplsInSegmentMapEntry", ("mplsinsegmentmapentry", MPLSLSRSTDMIB.MplsInSegmentMapTable.MplsInSegmentMapEntry))])
            self._leafs = OrderedDict()

            self.mplsinsegmentmapentry = YList(self)
            self._segment_path = lambda: "mplsInSegmentMapTable"
            self._absolute_path = lambda: "MPLS-LSR-STD-MIB:MPLS-LSR-STD-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(MPLSLSRSTDMIB.MplsInSegmentMapTable, [], name, value)


        class MplsInSegmentMapEntry(Entity):
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
            
            .. attribute:: mplsinsegmentmapinterface  (key)
            
            	This index contains the same value as the mplsInSegmentIndex in the mplsInSegmentTable
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: mplsinsegmentmaplabel  (key)
            
            	This index contains the same value as the mplsInSegmentLabel in the mplsInSegmentTable
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: mplsinsegmentmaplabelptrindex  (key)
            
            	This index contains the same value as the mplsInSegmentLabelPtr.  If the label for the InSegment cannot be represented fully within the mplsInSegmentLabel object, this index MUST point to the first accessible column of a conceptual row in an external table containing the label.  In this case, the mplsInSegmentTopLabel object SHOULD be set to 0 and ignored. This object MUST be set to zeroDotZero otherwise
            	**type**\: str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: mplsinsegmentmapindex
            
            	The mplsInSegmentIndex that corresponds to the mplsInSegmentInterface and mplsInSegmentLabel, or the mplsInSegmentInterface and mplsInSegmentLabelPtr, if applicable. The string containing the single octet 0x00 MUST not be returned
            	**type**\: str
            
            	**length:** 1..24
            
            

            """

            _prefix = 'MPLS-LSR-STD-MIB'
            _revision = '2004-06-03'

            def __init__(self):
                super(MPLSLSRSTDMIB.MplsInSegmentMapTable.MplsInSegmentMapEntry, self).__init__()

                self.yang_name = "mplsInSegmentMapEntry"
                self.yang_parent_name = "mplsInSegmentMapTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['mplsinsegmentmapinterface','mplsinsegmentmaplabel','mplsinsegmentmaplabelptrindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('mplsinsegmentmapinterface', (YLeaf(YType.int32, 'mplsInSegmentMapInterface'), ['int'])),
                    ('mplsinsegmentmaplabel', (YLeaf(YType.uint32, 'mplsInSegmentMapLabel'), ['int'])),
                    ('mplsinsegmentmaplabelptrindex', (YLeaf(YType.str, 'mplsInSegmentMapLabelPtrIndex'), ['str'])),
                    ('mplsinsegmentmapindex', (YLeaf(YType.str, 'mplsInSegmentMapIndex'), ['str'])),
                ])
                self.mplsinsegmentmapinterface = None
                self.mplsinsegmentmaplabel = None
                self.mplsinsegmentmaplabelptrindex = None
                self.mplsinsegmentmapindex = None
                self._segment_path = lambda: "mplsInSegmentMapEntry" + "[mplsInSegmentMapInterface='" + str(self.mplsinsegmentmapinterface) + "']" + "[mplsInSegmentMapLabel='" + str(self.mplsinsegmentmaplabel) + "']" + "[mplsInSegmentMapLabelPtrIndex='" + str(self.mplsinsegmentmaplabelptrindex) + "']"
                self._absolute_path = lambda: "MPLS-LSR-STD-MIB:MPLS-LSR-STD-MIB/mplsInSegmentMapTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(MPLSLSRSTDMIB.MplsInSegmentMapTable.MplsInSegmentMapEntry, [u'mplsinsegmentmapinterface', u'mplsinsegmentmaplabel', u'mplsinsegmentmaplabelptrindex', u'mplsinsegmentmapindex'], name, value)

    def clone_ptr(self):
        self._top_entity = MPLSLSRSTDMIB()
        return self._top_entity

