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
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class MPLSLDPGENERICSTDMIB(Entity):
    """
    
    
    .. attribute:: mplsldpentitygenericlrtable
    
    	The MPLS LDP Entity Generic Label Range (LR) Table.  The purpose of this table is to provide a mechanism for configurating a contiguous range of generic labels, or a 'label range' for LDP Entities.  LDP Entities which use Generic Labels must have at least one entry in this table.  In other words, this table 'extends' the mpldLdpEntityTable for Generic Labels
    	**type**\:  :py:class:`Mplsldpentitygenericlrtable <ydk.models.cisco_ios_xe.MPLS_LDP_GENERIC_STD_MIB.MPLSLDPGENERICSTDMIB.Mplsldpentitygenericlrtable>`
    
    

    """

    _prefix = 'MPLS-LDP-GENERIC-STD-MIB'
    _revision = '2004-06-03'

    def __init__(self):
        super(MPLSLDPGENERICSTDMIB, self).__init__()
        self._top_entity = None

        self.yang_name = "MPLS-LDP-GENERIC-STD-MIB"
        self.yang_parent_name = "MPLS-LDP-GENERIC-STD-MIB"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([("mplsLdpEntityGenericLRTable", ("mplsldpentitygenericlrtable", MPLSLDPGENERICSTDMIB.Mplsldpentitygenericlrtable))])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.mplsldpentitygenericlrtable = MPLSLDPGENERICSTDMIB.Mplsldpentitygenericlrtable()
        self.mplsldpentitygenericlrtable.parent = self
        self._children_name_map["mplsldpentitygenericlrtable"] = "mplsLdpEntityGenericLRTable"
        self._children_yang_names.add("mplsLdpEntityGenericLRTable")
        self._segment_path = lambda: "MPLS-LDP-GENERIC-STD-MIB:MPLS-LDP-GENERIC-STD-MIB"


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
        	**type**\: list of  		 :py:class:`Mplsldpentitygenericlrentry <ydk.models.cisco_ios_xe.MPLS_LDP_GENERIC_STD_MIB.MPLSLDPGENERICSTDMIB.Mplsldpentitygenericlrtable.Mplsldpentitygenericlrentry>`
        
        

        """

        _prefix = 'MPLS-LDP-GENERIC-STD-MIB'
        _revision = '2004-06-03'

        def __init__(self):
            super(MPLSLDPGENERICSTDMIB.Mplsldpentitygenericlrtable, self).__init__()

            self.yang_name = "mplsLdpEntityGenericLRTable"
            self.yang_parent_name = "MPLS-LDP-GENERIC-STD-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("mplsLdpEntityGenericLREntry", ("mplsldpentitygenericlrentry", MPLSLDPGENERICSTDMIB.Mplsldpentitygenericlrtable.Mplsldpentitygenericlrentry))])
            self._leafs = OrderedDict()

            self.mplsldpentitygenericlrentry = YList(self)
            self._segment_path = lambda: "mplsLdpEntityGenericLRTable"
            self._absolute_path = lambda: "MPLS-LDP-GENERIC-STD-MIB:MPLS-LDP-GENERIC-STD-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(MPLSLDPGENERICSTDMIB.Mplsldpentitygenericlrtable, [], name, value)


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
            
            .. attribute:: mplsldpentityldpid  (key)
            
            	
            	**type**\: str
            
            	**refers to**\:  :py:class:`mplsldpentityldpid <ydk.models.cisco_ios_xe.MPLS_LDP_STD_MIB.MPLSLDPSTDMIB.Mplsldpentitytable.Mplsldpentityentry>`
            
            .. attribute:: mplsldpentityindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..4294967295
            
            	**refers to**\:  :py:class:`mplsldpentityindex <ydk.models.cisco_ios_xe.MPLS_LDP_STD_MIB.MPLSLDPSTDMIB.Mplsldpentitytable.Mplsldpentityentry>`
            
            .. attribute:: mplsldpentitygenericlrmin  (key)
            
            	The minimum label configured for this range
            	**type**\: int
            
            	**range:** 0..1048575
            
            .. attribute:: mplsldpentitygenericlrmax  (key)
            
            	The maximum label configured for this range
            	**type**\: int
            
            	**range:** 0..1048575
            
            .. attribute:: mplsldpentitygenericlabelspace
            
            	This value of this object is perPlatform(1), then this means that the label space type is per platform.  If this object is perInterface(2), then this means that the label space type is per Interface
            	**type**\:  :py:class:`Mplsldpentitygenericlabelspace <ydk.models.cisco_ios_xe.MPLS_LDP_GENERIC_STD_MIB.MPLSLDPGENERICSTDMIB.Mplsldpentitygenericlrtable.Mplsldpentitygenericlrentry.Mplsldpentitygenericlabelspace>`
            
            .. attribute:: mplsldpentitygenericifindexorzero
            
            	This value represents either the InterfaceIndex of the 'ifLayer' where these Generic Label would be created,   or 0 (zero).  The value of zero means that the InterfaceIndex is not known.  However, if the InterfaceIndex is known, then it must be represented by this value.  If an InterfaceIndex becomes known, then the network management entity (e.g., SNMP agent) responsible for this object MUST change the value from 0 (zero) to the value of the InterfaceIndex
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: mplsldpentitygenericlrstoragetype
            
            	The storage type for this conceptual row. Conceptual rows having the value 'permanent(4)' need not allow write\-access to any columnar objects in the row
            	**type**\:  :py:class:`StorageType <ydk.models.cisco_ios_xe.SNMPv2_TC.StorageType>`
            
            .. attribute:: mplsldpentitygenericlrrowstatus
            
            	The status of this conceptual row.  All writable objects in this row may be modified at any time, however, as described in  detail in the section entitled, 'Changing Values After Session Establishment', and again described in the DESCRIPTION clause of the mplsLdpEntityAdminStatus object, if a session has been initiated with a Peer, changing objects in this table will wreak havoc with the session and interrupt traffic. To repeat again\:  the recommended procedure is to set the mplsLdpEntityAdminStatus to down, thereby explicitly causing a session to be torn down. Then, change objects in this entry, then set the mplsLdpEntityAdminStatus to enable which enables a new session to be initiated.  There must exist at least one entry in this table for every LDP Entity that has a generic label configured
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            

            """

            _prefix = 'MPLS-LDP-GENERIC-STD-MIB'
            _revision = '2004-06-03'

            def __init__(self):
                super(MPLSLDPGENERICSTDMIB.Mplsldpentitygenericlrtable.Mplsldpentitygenericlrentry, self).__init__()

                self.yang_name = "mplsLdpEntityGenericLREntry"
                self.yang_parent_name = "mplsLdpEntityGenericLRTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['mplsldpentityldpid','mplsldpentityindex','mplsldpentitygenericlrmin','mplsldpentitygenericlrmax']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('mplsldpentityldpid', YLeaf(YType.str, 'mplsLdpEntityLdpId')),
                    ('mplsldpentityindex', YLeaf(YType.str, 'mplsLdpEntityIndex')),
                    ('mplsldpentitygenericlrmin', YLeaf(YType.uint32, 'mplsLdpEntityGenericLRMin')),
                    ('mplsldpentitygenericlrmax', YLeaf(YType.uint32, 'mplsLdpEntityGenericLRMax')),
                    ('mplsldpentitygenericlabelspace', YLeaf(YType.enumeration, 'mplsLdpEntityGenericLabelSpace')),
                    ('mplsldpentitygenericifindexorzero', YLeaf(YType.int32, 'mplsLdpEntityGenericIfIndexOrZero')),
                    ('mplsldpentitygenericlrstoragetype', YLeaf(YType.enumeration, 'mplsLdpEntityGenericLRStorageType')),
                    ('mplsldpentitygenericlrrowstatus', YLeaf(YType.enumeration, 'mplsLdpEntityGenericLRRowStatus')),
                ])
                self.mplsldpentityldpid = None
                self.mplsldpentityindex = None
                self.mplsldpentitygenericlrmin = None
                self.mplsldpentitygenericlrmax = None
                self.mplsldpentitygenericlabelspace = None
                self.mplsldpentitygenericifindexorzero = None
                self.mplsldpentitygenericlrstoragetype = None
                self.mplsldpentitygenericlrrowstatus = None
                self._segment_path = lambda: "mplsLdpEntityGenericLREntry" + "[mplsLdpEntityLdpId='" + str(self.mplsldpentityldpid) + "']" + "[mplsLdpEntityIndex='" + str(self.mplsldpentityindex) + "']" + "[mplsLdpEntityGenericLRMin='" + str(self.mplsldpentitygenericlrmin) + "']" + "[mplsLdpEntityGenericLRMax='" + str(self.mplsldpentitygenericlrmax) + "']"
                self._absolute_path = lambda: "MPLS-LDP-GENERIC-STD-MIB:MPLS-LDP-GENERIC-STD-MIB/mplsLdpEntityGenericLRTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(MPLSLDPGENERICSTDMIB.Mplsldpentitygenericlrtable.Mplsldpentitygenericlrentry, ['mplsldpentityldpid', 'mplsldpentityindex', 'mplsldpentitygenericlrmin', 'mplsldpentitygenericlrmax', 'mplsldpentitygenericlabelspace', 'mplsldpentitygenericifindexorzero', 'mplsldpentitygenericlrstoragetype', 'mplsldpentitygenericlrrowstatus'], name, value)

            class Mplsldpentitygenericlabelspace(Enum):
                """
                Mplsldpentitygenericlabelspace (Enum Class)

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


    def clone_ptr(self):
        self._top_entity = MPLSLDPGENERICSTDMIB()
        return self._top_entity

