""" CISCO_IETF_MPLS_TE_EXT_STD_03_MIB 

Copyright (c) 2012 IETF Trust and the persons identified
as the document authors.  All rights reserved.
This MIB module contains generic object definitions for
MPLS Traffic Engineering in transport networks.This module is a
cisco\-ized version of the IETF draft\:
draft\-ietf\-mpls\-tp\-te\-mib\-03

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class CISCOIETFMPLSTEEXTSTD03MIB(Entity):
    """
    
    
    .. attribute:: cmplsnodeconfigtable
    
    	This table allows the administrator to map a node or LSR Identifier (IP compatible [Global\_Node\_ID] or ICC) with a local identifier.   This table is created to reuse the existing mplsTunnelTable for MPLS based transport network tunnels also. Since the MPLS tunnel's Ingress/Egress LSR identifiers' size (Unsigned32) value is not compatible for MPLS\-TP tunnel i.e. Global\_Node\_Id of size 8 bytes and ICC of size 6 bytes, there exists a need to map the Global\_Node\_ID or ICC with the local identifier of size 4 bytes (Unsigned32) value in order to index (Ingress/Egress LSR identifier) the existing mplsTunnelTable
    	**type**\:  :py:class:`Cmplsnodeconfigtable <ydk.models.cisco_ios_xe.CISCO_IETF_MPLS_TE_EXT_STD_03_MIB.CISCOIETFMPLSTEEXTSTD03MIB.Cmplsnodeconfigtable>`
    
    .. attribute:: cmplsnodeipmaptable
    
    	This read\-only table allows the administrator to retrieve the local identifier for a given Global\_Node\_ID in an IP compatible operator environment.  This table MAY be used in on\-demand and/or proactive OAM operations to get the Ingress/Egress LSR identifier (Local Identifier) from Src\-Global\_Node\_ID or Dst\-Global\_Node\_ID and the Ingress and Egress LSR identifiers are used to retrieve the tunnel entry.  This table returns nothing when the associated entry is not defined in mplsNodeConfigTable
    	**type**\:  :py:class:`Cmplsnodeipmaptable <ydk.models.cisco_ios_xe.CISCO_IETF_MPLS_TE_EXT_STD_03_MIB.CISCOIETFMPLSTEEXTSTD03MIB.Cmplsnodeipmaptable>`
    
    .. attribute:: cmplsnodeiccmaptable
    
    	This read\-only table allows the administrator to retrieve the local identifier for a given ICC operator in an ICC operator environment.  This table MAY be used in on\-demand and/or proactive OAM operations to get the Ingress/Egress LSR identifier (Local Identifier) from Src\-ICC or Dst\-ICC and the Ingress and Egress LSR identifiers are used to retrieve the tunnel entry. This table returns nothing when the associated entry is not defined in mplsNodeConfigTable
    	**type**\:  :py:class:`Cmplsnodeiccmaptable <ydk.models.cisco_ios_xe.CISCO_IETF_MPLS_TE_EXT_STD_03_MIB.CISCOIETFMPLSTEEXTSTD03MIB.Cmplsnodeiccmaptable>`
    
    .. attribute:: cmplstunnelexttable
    
    	This table represents MPLS\-TP specific extensions to mplsTunnelTable.  As per MPLS\-TP Identifiers [RFC6370], LSP\_ID for IP based co\-routed bidirectional tunnel,  A1\-{Global\_ID\:\:Node\_ID\:\:Tunnel\_Num}\:\:Z9\-{Global\_ID\:\: Node\_ID\:\:Tunnel\_Num}\:\:LSP\_Num  LSP\_ID for IP based associated bidirectional tunnel, A1\-{Global\_ID\:\:Node\_ID\:\:Tunnel\_Num\:\:LSP\_Num}\:\: Z9\-{Global\_ID\:\:Node\_ID\:\:Tunnel\_Num\:\:LSP\_Num}  mplsTunnelTable is reused for forming the LSP\_ID as follows,  Source Tunnel\_Num is mapped with mplsTunnelIndex, Source Node\_ID is mapped with mplsTunnelIngressLSRId, Destination Node\_ID is mapped with mplsTunnelEgressLSRId LSP\_Num is mapped with mplsTunnelInstance.  Source Global\_Node\_ID and/or ICC and Destination Global\_Node\_ID and/or ICC are maintained in the mplsNodeConfigTable and mplsNodeConfigLocalId is used to create an entry in mplsTunnelTable
    	**type**\:  :py:class:`Cmplstunnelexttable <ydk.models.cisco_ios_xe.CISCO_IETF_MPLS_TE_EXT_STD_03_MIB.CISCOIETFMPLSTEEXTSTD03MIB.Cmplstunnelexttable>`
    
    .. attribute:: cmplstunnelreverseperftable
    
    	This table extends the mplsTunnelTable to provide per\-tunnel packet performance information for the reverse direction of a bidirectional tunnel.  It can be seen as supplementing the mplsTunnelPerfTable, which augments the mplsTunnelTable.  For links that do not transport packets, these packet counters cannot be maintained.  For such links, attempts to read the objects in this table will return noSuchInstance
    	**type**\:  :py:class:`Cmplstunnelreverseperftable <ydk.models.cisco_ios_xe.CISCO_IETF_MPLS_TE_EXT_STD_03_MIB.CISCOIETFMPLSTEEXTSTD03MIB.Cmplstunnelreverseperftable>`
    
    

    """

    _prefix = 'CISCO-IETF-MPLS-TE-EXT-STD-03-MIB'
    _revision = '2012-06-06'

    def __init__(self):
        super(CISCOIETFMPLSTEEXTSTD03MIB, self).__init__()
        self._top_entity = None

        self.yang_name = "CISCO-IETF-MPLS-TE-EXT-STD-03-MIB"
        self.yang_parent_name = "CISCO-IETF-MPLS-TE-EXT-STD-03-MIB"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([("cmplsNodeConfigTable", ("cmplsnodeconfigtable", CISCOIETFMPLSTEEXTSTD03MIB.Cmplsnodeconfigtable)), ("cmplsNodeIpMapTable", ("cmplsnodeipmaptable", CISCOIETFMPLSTEEXTSTD03MIB.Cmplsnodeipmaptable)), ("cmplsNodeIccMapTable", ("cmplsnodeiccmaptable", CISCOIETFMPLSTEEXTSTD03MIB.Cmplsnodeiccmaptable)), ("cmplsTunnelExtTable", ("cmplstunnelexttable", CISCOIETFMPLSTEEXTSTD03MIB.Cmplstunnelexttable)), ("cmplsTunnelReversePerfTable", ("cmplstunnelreverseperftable", CISCOIETFMPLSTEEXTSTD03MIB.Cmplstunnelreverseperftable))])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.cmplsnodeconfigtable = CISCOIETFMPLSTEEXTSTD03MIB.Cmplsnodeconfigtable()
        self.cmplsnodeconfigtable.parent = self
        self._children_name_map["cmplsnodeconfigtable"] = "cmplsNodeConfigTable"
        self._children_yang_names.add("cmplsNodeConfigTable")

        self.cmplsnodeipmaptable = CISCOIETFMPLSTEEXTSTD03MIB.Cmplsnodeipmaptable()
        self.cmplsnodeipmaptable.parent = self
        self._children_name_map["cmplsnodeipmaptable"] = "cmplsNodeIpMapTable"
        self._children_yang_names.add("cmplsNodeIpMapTable")

        self.cmplsnodeiccmaptable = CISCOIETFMPLSTEEXTSTD03MIB.Cmplsnodeiccmaptable()
        self.cmplsnodeiccmaptable.parent = self
        self._children_name_map["cmplsnodeiccmaptable"] = "cmplsNodeIccMapTable"
        self._children_yang_names.add("cmplsNodeIccMapTable")

        self.cmplstunnelexttable = CISCOIETFMPLSTEEXTSTD03MIB.Cmplstunnelexttable()
        self.cmplstunnelexttable.parent = self
        self._children_name_map["cmplstunnelexttable"] = "cmplsTunnelExtTable"
        self._children_yang_names.add("cmplsTunnelExtTable")

        self.cmplstunnelreverseperftable = CISCOIETFMPLSTEEXTSTD03MIB.Cmplstunnelreverseperftable()
        self.cmplstunnelreverseperftable.parent = self
        self._children_name_map["cmplstunnelreverseperftable"] = "cmplsTunnelReversePerfTable"
        self._children_yang_names.add("cmplsTunnelReversePerfTable")
        self._segment_path = lambda: "CISCO-IETF-MPLS-TE-EXT-STD-03-MIB:CISCO-IETF-MPLS-TE-EXT-STD-03-MIB"


    class Cmplsnodeconfigtable(Entity):
        """
        This table allows the administrator to map a node or
        LSR Identifier (IP compatible [Global\_Node\_ID] or ICC)
        with a local identifier.
        
        
        This table is created to reuse the existing
        mplsTunnelTable for MPLS based transport network
        tunnels also.
        Since the MPLS tunnel's Ingress/Egress LSR identifiers'
        size (Unsigned32) value is not compatible for
        MPLS\-TP tunnel i.e. Global\_Node\_Id of size 8 bytes and
        ICC of size 6 bytes, there exists a need to map the
        Global\_Node\_ID or ICC with the local identifier of size
        4 bytes (Unsigned32) value in order
        to index (Ingress/Egress LSR identifier)
        the existing mplsTunnelTable.
        
        .. attribute:: cmplsnodeconfigentry
        
        	An entry in this table represents a mapping identification for the operator or service provider with node or LSR.  As per [RFC6370], this mapping is  represented as Global\_Node\_ID or ICC.  Note\: Each entry in this table should have a unique Global\_ID and Node\_ID combination
        	**type**\: list of  		 :py:class:`Cmplsnodeconfigentry <ydk.models.cisco_ios_xe.CISCO_IETF_MPLS_TE_EXT_STD_03_MIB.CISCOIETFMPLSTEEXTSTD03MIB.Cmplsnodeconfigtable.Cmplsnodeconfigentry>`
        
        

        """

        _prefix = 'CISCO-IETF-MPLS-TE-EXT-STD-03-MIB'
        _revision = '2012-06-06'

        def __init__(self):
            super(CISCOIETFMPLSTEEXTSTD03MIB.Cmplsnodeconfigtable, self).__init__()

            self.yang_name = "cmplsNodeConfigTable"
            self.yang_parent_name = "CISCO-IETF-MPLS-TE-EXT-STD-03-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("cmplsNodeConfigEntry", ("cmplsnodeconfigentry", CISCOIETFMPLSTEEXTSTD03MIB.Cmplsnodeconfigtable.Cmplsnodeconfigentry))])
            self._leafs = OrderedDict()

            self.cmplsnodeconfigentry = YList(self)
            self._segment_path = lambda: "cmplsNodeConfigTable"
            self._absolute_path = lambda: "CISCO-IETF-MPLS-TE-EXT-STD-03-MIB:CISCO-IETF-MPLS-TE-EXT-STD-03-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOIETFMPLSTEEXTSTD03MIB.Cmplsnodeconfigtable, [], name, value)


        class Cmplsnodeconfigentry(Entity):
            """
            An entry in this table represents a mapping
            identification for the operator or service provider
            with node or LSR.
            
            As per [RFC6370], this mapping is
            
            represented as Global\_Node\_ID or ICC.
            
            Note\: Each entry in this table should have a unique
            Global\_ID and Node\_ID combination.
            
            .. attribute:: cmplsnodeconfiglocalid  (key)
            
            	This object allows the administrator to assign a unique local identifier to map Global\_Node\_ID or ICC
            	**type**\: int
            
            	**range:** 1..16777215
            
            .. attribute:: cmplsnodeconfigglobalid
            
            	This object indicates the Global Operator Identifier. This object value should be zero when mplsNodeConfigIccId is configured with non\-null value
            	**type**\: str
            
            	**length:** 4
            
            .. attribute:: cmplsnodeconfignodeid
            
            	This object indicates the Node\_ID within the operator. This object value should be zero when mplsNodeConfigIccId is configured with non\-null value
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cmplsnodeconfigiccid
            
            	This object allows the operator or service provider to configure a unique MPLS\-TP ITU\-T Carrier Code (ICC) either for Ingress ID or Egress ID.  This object value should be zero when mplsNodeConfigGlobalId and mplsNodeConfigNodeId are assigned with non\-zero value
            	**type**\: str
            
            	**length:** 1..6
            
            .. attribute:: cmplsnodeconfigrowstatus
            
            	This object allows the administrator to create, modify, and/or delete a row in this table
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            .. attribute:: cmplsnodeconfigstoragetype
            
            	This variable indicates the storage type for this object. Conceptual rows having the value 'permanent' need not allow write\-access to any columnar objects in the row
            	**type**\:  :py:class:`StorageType <ydk.models.cisco_ios_xe.SNMPv2_TC.StorageType>`
            
            

            """

            _prefix = 'CISCO-IETF-MPLS-TE-EXT-STD-03-MIB'
            _revision = '2012-06-06'

            def __init__(self):
                super(CISCOIETFMPLSTEEXTSTD03MIB.Cmplsnodeconfigtable.Cmplsnodeconfigentry, self).__init__()

                self.yang_name = "cmplsNodeConfigEntry"
                self.yang_parent_name = "cmplsNodeConfigTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['cmplsnodeconfiglocalid']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cmplsnodeconfiglocalid', YLeaf(YType.uint32, 'cmplsNodeConfigLocalId')),
                    ('cmplsnodeconfigglobalid', YLeaf(YType.str, 'cmplsNodeConfigGlobalId')),
                    ('cmplsnodeconfignodeid', YLeaf(YType.uint32, 'cmplsNodeConfigNodeId')),
                    ('cmplsnodeconfigiccid', YLeaf(YType.str, 'cmplsNodeConfigIccId')),
                    ('cmplsnodeconfigrowstatus', YLeaf(YType.enumeration, 'cmplsNodeConfigRowStatus')),
                    ('cmplsnodeconfigstoragetype', YLeaf(YType.enumeration, 'cmplsNodeConfigStorageType')),
                ])
                self.cmplsnodeconfiglocalid = None
                self.cmplsnodeconfigglobalid = None
                self.cmplsnodeconfignodeid = None
                self.cmplsnodeconfigiccid = None
                self.cmplsnodeconfigrowstatus = None
                self.cmplsnodeconfigstoragetype = None
                self._segment_path = lambda: "cmplsNodeConfigEntry" + "[cmplsNodeConfigLocalId='" + str(self.cmplsnodeconfiglocalid) + "']"
                self._absolute_path = lambda: "CISCO-IETF-MPLS-TE-EXT-STD-03-MIB:CISCO-IETF-MPLS-TE-EXT-STD-03-MIB/cmplsNodeConfigTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOIETFMPLSTEEXTSTD03MIB.Cmplsnodeconfigtable.Cmplsnodeconfigentry, ['cmplsnodeconfiglocalid', 'cmplsnodeconfigglobalid', 'cmplsnodeconfignodeid', 'cmplsnodeconfigiccid', 'cmplsnodeconfigrowstatus', 'cmplsnodeconfigstoragetype'], name, value)


    class Cmplsnodeipmaptable(Entity):
        """
        This read\-only table allows the administrator to retrieve
        the local identifier for a given Global\_Node\_ID in an IP
        compatible operator environment.
        
        This table MAY be used in on\-demand and/or proactive
        OAM operations to get the Ingress/Egress LSR identifier
        (Local Identifier) from Src\-Global\_Node\_ID
        or Dst\-Global\_Node\_ID and the Ingress and Egress LSR
        identifiers are used to retrieve the tunnel entry.
        
        This table returns nothing when the associated entry
        is not defined in mplsNodeConfigTable.
        
        .. attribute:: cmplsnodeipmapentry
        
        	An entry in this table represents a mapping of Global\_Node\_ID with the local identifier.  An entry in this table is created automatically when the Local identifier is associated with Global\_ID and Node\_Id in the mplsNodeConfigTable. Note\: Each entry in this table should have a unique Global\_ID and Node\_ID combination
        	**type**\: list of  		 :py:class:`Cmplsnodeipmapentry <ydk.models.cisco_ios_xe.CISCO_IETF_MPLS_TE_EXT_STD_03_MIB.CISCOIETFMPLSTEEXTSTD03MIB.Cmplsnodeipmaptable.Cmplsnodeipmapentry>`
        
        

        """

        _prefix = 'CISCO-IETF-MPLS-TE-EXT-STD-03-MIB'
        _revision = '2012-06-06'

        def __init__(self):
            super(CISCOIETFMPLSTEEXTSTD03MIB.Cmplsnodeipmaptable, self).__init__()

            self.yang_name = "cmplsNodeIpMapTable"
            self.yang_parent_name = "CISCO-IETF-MPLS-TE-EXT-STD-03-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("cmplsNodeIpMapEntry", ("cmplsnodeipmapentry", CISCOIETFMPLSTEEXTSTD03MIB.Cmplsnodeipmaptable.Cmplsnodeipmapentry))])
            self._leafs = OrderedDict()

            self.cmplsnodeipmapentry = YList(self)
            self._segment_path = lambda: "cmplsNodeIpMapTable"
            self._absolute_path = lambda: "CISCO-IETF-MPLS-TE-EXT-STD-03-MIB:CISCO-IETF-MPLS-TE-EXT-STD-03-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOIETFMPLSTEEXTSTD03MIB.Cmplsnodeipmaptable, [], name, value)


        class Cmplsnodeipmapentry(Entity):
            """
            An entry in this table represents a mapping of
            Global\_Node\_ID with the local identifier.
            
            An entry in this table is created automatically when
            the Local identifier is associated with Global\_ID and
            Node\_Id in the mplsNodeConfigTable.
            Note\: Each entry in this table should have a unique
            Global\_ID and Node\_ID combination.
            
            .. attribute:: cmplsnodeipmapglobalid  (key)
            
            	This object indicates the Global\_ID
            	**type**\: str
            
            	**length:** 4
            
            .. attribute:: cmplsnodeipmapnodeid  (key)
            
            	This object indicates the Node\_ID within the operator
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cmplsnodeipmaplocalid
            
            	This object contains an IP compatible local identifier which is defined in mplsNodeConfigTable
            	**type**\: int
            
            	**range:** 1..16777215
            
            

            """

            _prefix = 'CISCO-IETF-MPLS-TE-EXT-STD-03-MIB'
            _revision = '2012-06-06'

            def __init__(self):
                super(CISCOIETFMPLSTEEXTSTD03MIB.Cmplsnodeipmaptable.Cmplsnodeipmapentry, self).__init__()

                self.yang_name = "cmplsNodeIpMapEntry"
                self.yang_parent_name = "cmplsNodeIpMapTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['cmplsnodeipmapglobalid','cmplsnodeipmapnodeid']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cmplsnodeipmapglobalid', YLeaf(YType.str, 'cmplsNodeIpMapGlobalId')),
                    ('cmplsnodeipmapnodeid', YLeaf(YType.uint32, 'cmplsNodeIpMapNodeId')),
                    ('cmplsnodeipmaplocalid', YLeaf(YType.uint32, 'cmplsNodeIpMapLocalId')),
                ])
                self.cmplsnodeipmapglobalid = None
                self.cmplsnodeipmapnodeid = None
                self.cmplsnodeipmaplocalid = None
                self._segment_path = lambda: "cmplsNodeIpMapEntry" + "[cmplsNodeIpMapGlobalId='" + str(self.cmplsnodeipmapglobalid) + "']" + "[cmplsNodeIpMapNodeId='" + str(self.cmplsnodeipmapnodeid) + "']"
                self._absolute_path = lambda: "CISCO-IETF-MPLS-TE-EXT-STD-03-MIB:CISCO-IETF-MPLS-TE-EXT-STD-03-MIB/cmplsNodeIpMapTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOIETFMPLSTEEXTSTD03MIB.Cmplsnodeipmaptable.Cmplsnodeipmapentry, ['cmplsnodeipmapglobalid', 'cmplsnodeipmapnodeid', 'cmplsnodeipmaplocalid'], name, value)


    class Cmplsnodeiccmaptable(Entity):
        """
        This read\-only table allows the administrator to retrieve
        the local identifier for a given ICC operator in an ICC
        operator environment.
        
        This table MAY be used in on\-demand and/or proactive
        OAM operations to get the Ingress/Egress LSR
        identifier (Local Identifier) from Src\-ICC
        or Dst\-ICC and the Ingress and Egress LSR
        identifiers are used to retrieve the tunnel entry.
        This table returns nothing when the associated entry
        is not defined in mplsNodeConfigTable.
        
        .. attribute:: cmplsnodeiccmapentry
        
        	An entry in this table represents a mapping of ICC with the local identifier.  An entry in this table is created automatically when the Local identifier is associated with ICC in the mplsNodeConfigTable
        	**type**\: list of  		 :py:class:`Cmplsnodeiccmapentry <ydk.models.cisco_ios_xe.CISCO_IETF_MPLS_TE_EXT_STD_03_MIB.CISCOIETFMPLSTEEXTSTD03MIB.Cmplsnodeiccmaptable.Cmplsnodeiccmapentry>`
        
        

        """

        _prefix = 'CISCO-IETF-MPLS-TE-EXT-STD-03-MIB'
        _revision = '2012-06-06'

        def __init__(self):
            super(CISCOIETFMPLSTEEXTSTD03MIB.Cmplsnodeiccmaptable, self).__init__()

            self.yang_name = "cmplsNodeIccMapTable"
            self.yang_parent_name = "CISCO-IETF-MPLS-TE-EXT-STD-03-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("cmplsNodeIccMapEntry", ("cmplsnodeiccmapentry", CISCOIETFMPLSTEEXTSTD03MIB.Cmplsnodeiccmaptable.Cmplsnodeiccmapentry))])
            self._leafs = OrderedDict()

            self.cmplsnodeiccmapentry = YList(self)
            self._segment_path = lambda: "cmplsNodeIccMapTable"
            self._absolute_path = lambda: "CISCO-IETF-MPLS-TE-EXT-STD-03-MIB:CISCO-IETF-MPLS-TE-EXT-STD-03-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOIETFMPLSTEEXTSTD03MIB.Cmplsnodeiccmaptable, [], name, value)


        class Cmplsnodeiccmapentry(Entity):
            """
            An entry in this table represents a mapping of ICC with
            the local identifier.
            
            An entry in this table is created automatically when
            the Local identifier is associated with ICC in
            the mplsNodeConfigTable.
            
            .. attribute:: cmplsnodeiccmapiccid  (key)
            
            	This object allows the operator or service provider to configure a unique MPLS\-TP ITU\-T Carrier Code (ICC) either for Ingress or Egress LSR ID.  The ICC is a string of one to six characters, each character being either alphabetic (i.e.  A\-Z) or numeric (i.e. 0\-9) characters. Alphabetic characters in the ICC should be represented with upper case letters
            	**type**\: str
            
            	**length:** 1..6
            
            .. attribute:: cmplsnodeiccmaplocalid
            
            	This object contains an ICC based local identifier which is defined in mplsNodeConfigTable
            	**type**\: int
            
            	**range:** 1..16777215
            
            

            """

            _prefix = 'CISCO-IETF-MPLS-TE-EXT-STD-03-MIB'
            _revision = '2012-06-06'

            def __init__(self):
                super(CISCOIETFMPLSTEEXTSTD03MIB.Cmplsnodeiccmaptable.Cmplsnodeiccmapentry, self).__init__()

                self.yang_name = "cmplsNodeIccMapEntry"
                self.yang_parent_name = "cmplsNodeIccMapTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['cmplsnodeiccmapiccid']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cmplsnodeiccmapiccid', YLeaf(YType.str, 'cmplsNodeIccMapIccId')),
                    ('cmplsnodeiccmaplocalid', YLeaf(YType.uint32, 'cmplsNodeIccMapLocalId')),
                ])
                self.cmplsnodeiccmapiccid = None
                self.cmplsnodeiccmaplocalid = None
                self._segment_path = lambda: "cmplsNodeIccMapEntry" + "[cmplsNodeIccMapIccId='" + str(self.cmplsnodeiccmapiccid) + "']"
                self._absolute_path = lambda: "CISCO-IETF-MPLS-TE-EXT-STD-03-MIB:CISCO-IETF-MPLS-TE-EXT-STD-03-MIB/cmplsNodeIccMapTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOIETFMPLSTEEXTSTD03MIB.Cmplsnodeiccmaptable.Cmplsnodeiccmapentry, ['cmplsnodeiccmapiccid', 'cmplsnodeiccmaplocalid'], name, value)


    class Cmplstunnelexttable(Entity):
        """
        This table represents MPLS\-TP specific extensions to
        mplsTunnelTable.
        
        As per MPLS\-TP Identifiers [RFC6370], LSP\_ID for IP based
        co\-routed bidirectional tunnel,
        
        A1\-{Global\_ID\:\:Node\_ID\:\:Tunnel\_Num}\:\:Z9\-{Global\_ID\:\:
        Node\_ID\:\:Tunnel\_Num}\:\:LSP\_Num
        
        LSP\_ID for IP based associated bidirectional tunnel,
        A1\-{Global\_ID\:\:Node\_ID\:\:Tunnel\_Num\:\:LSP\_Num}\:\:
        Z9\-{Global\_ID\:\:Node\_ID\:\:Tunnel\_Num\:\:LSP\_Num}
        
        mplsTunnelTable is reused for forming the LSP\_ID
        as follows,
        
        Source Tunnel\_Num is mapped with mplsTunnelIndex,
        Source Node\_ID is mapped with
        mplsTunnelIngressLSRId, Destination Node\_ID is
        mapped with mplsTunnelEgressLSRId LSP\_Num is mapped with
        mplsTunnelInstance.
        
        Source Global\_Node\_ID and/or ICC and Destination
        Global\_Node\_ID and/or ICC are maintained in the
        mplsNodeConfigTable and mplsNodeConfigLocalId is
        used to create an entry in mplsTunnelTable.
        
        .. attribute:: cmplstunnelextentry
        
        	An entry in this table represents MPLS\-TP specific additional tunnel configurations
        	**type**\: list of  		 :py:class:`Cmplstunnelextentry <ydk.models.cisco_ios_xe.CISCO_IETF_MPLS_TE_EXT_STD_03_MIB.CISCOIETFMPLSTEEXTSTD03MIB.Cmplstunnelexttable.Cmplstunnelextentry>`
        
        

        """

        _prefix = 'CISCO-IETF-MPLS-TE-EXT-STD-03-MIB'
        _revision = '2012-06-06'

        def __init__(self):
            super(CISCOIETFMPLSTEEXTSTD03MIB.Cmplstunnelexttable, self).__init__()

            self.yang_name = "cmplsTunnelExtTable"
            self.yang_parent_name = "CISCO-IETF-MPLS-TE-EXT-STD-03-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("cmplsTunnelExtEntry", ("cmplstunnelextentry", CISCOIETFMPLSTEEXTSTD03MIB.Cmplstunnelexttable.Cmplstunnelextentry))])
            self._leafs = OrderedDict()

            self.cmplstunnelextentry = YList(self)
            self._segment_path = lambda: "cmplsTunnelExtTable"
            self._absolute_path = lambda: "CISCO-IETF-MPLS-TE-EXT-STD-03-MIB:CISCO-IETF-MPLS-TE-EXT-STD-03-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOIETFMPLSTEEXTSTD03MIB.Cmplstunnelexttable, [], name, value)


        class Cmplstunnelextentry(Entity):
            """
            An entry in this table represents MPLS\-TP
            specific additional tunnel configurations.
            
            .. attribute:: mplstunnelindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 0..65535
            
            	**refers to**\:  :py:class:`mplstunnelindex <ydk.models.cisco_ios_xe.MPLS_TE_STD_MIB.MPLSTESTDMIB.Mplstunneltable.Mplstunnelentry>`
            
            .. attribute:: mplstunnelinstance  (key)
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**refers to**\:  :py:class:`mplstunnelinstance <ydk.models.cisco_ios_xe.MPLS_TE_STD_MIB.MPLSTESTDMIB.Mplstunneltable.Mplstunnelentry>`
            
            .. attribute:: mplstunnelingresslsrid  (key)
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**refers to**\:  :py:class:`mplstunnelingresslsrid <ydk.models.cisco_ios_xe.MPLS_TE_STD_MIB.MPLSTESTDMIB.Mplstunneltable.Mplstunnelentry>`
            
            .. attribute:: mplstunnelegresslsrid  (key)
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**refers to**\:  :py:class:`mplstunnelegresslsrid <ydk.models.cisco_ios_xe.MPLS_TE_STD_MIB.MPLSTESTDMIB.Mplstunneltable.Mplstunnelentry>`
            
            .. attribute:: cmplstunneloppositedirptr
            
            	This object is applicable only for the bidirectional tunnel that has the forward and reverse LSPs in the same tunnel or in the different tunnels.  This object holds the opposite direction tunnel entry if the bidirectional tunnel is setup by configuring two tunnel entries in mplsTunnelTable.  The value of zeroDotZero indicates single tunnel entry is used for bidirectional tunnel setup
            	**type**\: str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: cmplstunnelextoppositedirtnlvalid
            
            	Denotes whether or not this tunnel uses mplsTunnelOppositeDirPtr for identifying the opposite direction tunnel information. Note that if this variable is set to true then the mplsTunnelOppositeDirPtr should point to the first accessible row of the opposite direction tunnel
            	**type**\: bool
            
            .. attribute:: cmplstunnelextdesttnlindex
            
            	This object is applicable only for the bidirectional tunnel that has the forward and reverse LSPs in the same tunnel or in the different tunnels.  This object holds the same value as that of the mplsTunnelIndex of mplsTunnelEntry if the forward and reverse LSPs are in the same tunnel. Otherwise, this object holds the value of the other direction associated LSP's mplsTunnelIndex from a different tunnel.  The values of this object and the mplsTunnelExtDestTnlLspIndex object together can be used to identify an opposite direction LSP i.e. if the mplsTunnelIndex and mplsTunnelInstance hold the value for forward LSP, this object and mplsTunnelExtDestTnlLspIndex can be used to retrieve the reverse direction LSP and vice versa.  This object and mplsTunnelExtDestTnlLspIndex values provide the first two indices of tunnel entry and the remaining indices can be derived as follows, if both the forward and reverse LSPs are present in the same tunnel, the opposite direction LSP's Ingress and Egress Identifier will be same for both the LSPs, else the Ingress and Egress Identifiers should be swapped in order to index the other direction tunnel
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: cmplstunnelextdesttnllspindex
            
            	This object is applicable only for the bidirectional tunnel that has the forward and reverse LSPs in the same tunnel or in the different tunnels.  This object should contain different value if both the forward and reverse LSPs present in the same tunnel.  This object can contain same value or different values if the forward and reverse LSPs present in the different tunnels
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cmplstunnelextdesttnlvalid
            
            	Denotes whether or not this tunnel uses mplsTunnelExtDestTnlIndex and mplsTunnelExtDestTnlLspIndex for identifying the opposite direction tunnel information. Note that if this variable is set to true then the mplsTunnelExtDestTnlIndex and mplsTunnelExtDestTnlLspIndex objects should have the valid opposite direction tunnel indices
            	**type**\: bool
            
            

            """

            _prefix = 'CISCO-IETF-MPLS-TE-EXT-STD-03-MIB'
            _revision = '2012-06-06'

            def __init__(self):
                super(CISCOIETFMPLSTEEXTSTD03MIB.Cmplstunnelexttable.Cmplstunnelextentry, self).__init__()

                self.yang_name = "cmplsTunnelExtEntry"
                self.yang_parent_name = "cmplsTunnelExtTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['mplstunnelindex','mplstunnelinstance','mplstunnelingresslsrid','mplstunnelegresslsrid']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('mplstunnelindex', YLeaf(YType.str, 'mplsTunnelIndex')),
                    ('mplstunnelinstance', YLeaf(YType.str, 'mplsTunnelInstance')),
                    ('mplstunnelingresslsrid', YLeaf(YType.str, 'mplsTunnelIngressLSRId')),
                    ('mplstunnelegresslsrid', YLeaf(YType.str, 'mplsTunnelEgressLSRId')),
                    ('cmplstunneloppositedirptr', YLeaf(YType.str, 'cmplsTunnelOppositeDirPtr')),
                    ('cmplstunnelextoppositedirtnlvalid', YLeaf(YType.boolean, 'cmplsTunnelExtOppositeDirTnlValid')),
                    ('cmplstunnelextdesttnlindex', YLeaf(YType.uint32, 'cmplsTunnelExtDestTnlIndex')),
                    ('cmplstunnelextdesttnllspindex', YLeaf(YType.uint32, 'cmplsTunnelExtDestTnlLspIndex')),
                    ('cmplstunnelextdesttnlvalid', YLeaf(YType.boolean, 'cmplsTunnelExtDestTnlValid')),
                ])
                self.mplstunnelindex = None
                self.mplstunnelinstance = None
                self.mplstunnelingresslsrid = None
                self.mplstunnelegresslsrid = None
                self.cmplstunneloppositedirptr = None
                self.cmplstunnelextoppositedirtnlvalid = None
                self.cmplstunnelextdesttnlindex = None
                self.cmplstunnelextdesttnllspindex = None
                self.cmplstunnelextdesttnlvalid = None
                self._segment_path = lambda: "cmplsTunnelExtEntry" + "[mplsTunnelIndex='" + str(self.mplstunnelindex) + "']" + "[mplsTunnelInstance='" + str(self.mplstunnelinstance) + "']" + "[mplsTunnelIngressLSRId='" + str(self.mplstunnelingresslsrid) + "']" + "[mplsTunnelEgressLSRId='" + str(self.mplstunnelegresslsrid) + "']"
                self._absolute_path = lambda: "CISCO-IETF-MPLS-TE-EXT-STD-03-MIB:CISCO-IETF-MPLS-TE-EXT-STD-03-MIB/cmplsTunnelExtTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOIETFMPLSTEEXTSTD03MIB.Cmplstunnelexttable.Cmplstunnelextentry, ['mplstunnelindex', 'mplstunnelinstance', 'mplstunnelingresslsrid', 'mplstunnelegresslsrid', 'cmplstunneloppositedirptr', 'cmplstunnelextoppositedirtnlvalid', 'cmplstunnelextdesttnlindex', 'cmplstunnelextdesttnllspindex', 'cmplstunnelextdesttnlvalid'], name, value)


    class Cmplstunnelreverseperftable(Entity):
        """
        This table extends the mplsTunnelTable to provide
        per\-tunnel packet performance information for the reverse
        direction of a bidirectional tunnel.  It can be seen as
        supplementing the mplsTunnelPerfTable, which augments the
        mplsTunnelTable.
        
        For links that do not transport packets, these packet
        counters cannot be maintained.  For such links, attempts
        to read the objects in this table will return
        noSuchInstance.
        
        .. attribute:: cmplstunnelreverseperfentry
        
        	An entry in this table is created by the LSR for every bidirectional MPLS tunnel where packets are visible to the LSR
        	**type**\: list of  		 :py:class:`Cmplstunnelreverseperfentry <ydk.models.cisco_ios_xe.CISCO_IETF_MPLS_TE_EXT_STD_03_MIB.CISCOIETFMPLSTEEXTSTD03MIB.Cmplstunnelreverseperftable.Cmplstunnelreverseperfentry>`
        
        

        """

        _prefix = 'CISCO-IETF-MPLS-TE-EXT-STD-03-MIB'
        _revision = '2012-06-06'

        def __init__(self):
            super(CISCOIETFMPLSTEEXTSTD03MIB.Cmplstunnelreverseperftable, self).__init__()

            self.yang_name = "cmplsTunnelReversePerfTable"
            self.yang_parent_name = "CISCO-IETF-MPLS-TE-EXT-STD-03-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("cmplsTunnelReversePerfEntry", ("cmplstunnelreverseperfentry", CISCOIETFMPLSTEEXTSTD03MIB.Cmplstunnelreverseperftable.Cmplstunnelreverseperfentry))])
            self._leafs = OrderedDict()

            self.cmplstunnelreverseperfentry = YList(self)
            self._segment_path = lambda: "cmplsTunnelReversePerfTable"
            self._absolute_path = lambda: "CISCO-IETF-MPLS-TE-EXT-STD-03-MIB:CISCO-IETF-MPLS-TE-EXT-STD-03-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOIETFMPLSTEEXTSTD03MIB.Cmplstunnelreverseperftable, [], name, value)


        class Cmplstunnelreverseperfentry(Entity):
            """
            An entry in this table is created by the LSR for every
            bidirectional MPLS tunnel where packets are visible to the
            LSR.
            
            .. attribute:: mplstunnelindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 0..65535
            
            	**refers to**\:  :py:class:`mplstunnelindex <ydk.models.cisco_ios_xe.MPLS_TE_STD_MIB.MPLSTESTDMIB.Mplstunneltable.Mplstunnelentry>`
            
            .. attribute:: mplstunnelinstance  (key)
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**refers to**\:  :py:class:`mplstunnelinstance <ydk.models.cisco_ios_xe.MPLS_TE_STD_MIB.MPLSTESTDMIB.Mplstunneltable.Mplstunnelentry>`
            
            .. attribute:: mplstunnelingresslsrid  (key)
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**refers to**\:  :py:class:`mplstunnelingresslsrid <ydk.models.cisco_ios_xe.MPLS_TE_STD_MIB.MPLSTESTDMIB.Mplstunneltable.Mplstunnelentry>`
            
            .. attribute:: mplstunnelegresslsrid  (key)
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**refers to**\:  :py:class:`mplstunnelegresslsrid <ydk.models.cisco_ios_xe.MPLS_TE_STD_MIB.MPLSTESTDMIB.Mplstunneltable.Mplstunnelentry>`
            
            .. attribute:: cmplstunnelreverseperfpackets
            
            	Number of packets forwarded on the tunnel in the reverse direction if it is bidirectional.  This object represents the 32\-bit value of the least significant part of the 64\-bit value if both mplsTunnelReversePerfHCPackets and this object are returned.  For links that do not transport packets, this packet counter cannot be maintained.  For such links, this value will return noSuchInstance
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cmplstunnelreverseperfhcpackets
            
            	High\-capacity counter for number of packets forwarded on the tunnel in the reverse direction if it is bidirectional.  For links that do not transport packets, this packet counter cannot be maintained.  For such links, this value will return noSuchInstance
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cmplstunnelreverseperferrors
            
            	Number of errored packets received on the tunnel in the reverse direction if it is bidirectional.  For links that do not transport packets, this packet counter cannot be maintained.  For such links, this value will return noSuchInstance
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cmplstunnelreverseperfbytes
            
            	Number of bytes forwarded on the tunnel in the reverse direction if it is bidirectional.  This object represents the 32\-bit value of the least significant part of the 64\-bit value if both mplsTunnelReversePerfHCBytes and this object are returned.  For links that do not transport packets, this packet counter cannot be maintained.  For such links, this value will return noSuchInstance
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cmplstunnelreverseperfhcbytes
            
            	High\-capacity counter for number of bytes forwarded on the tunnel in the reverse direction if it is bidirectional.  For links that do not transport packets, this packet counter cannot be maintained.  For such links, this value will return noSuchInstance
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            

            """

            _prefix = 'CISCO-IETF-MPLS-TE-EXT-STD-03-MIB'
            _revision = '2012-06-06'

            def __init__(self):
                super(CISCOIETFMPLSTEEXTSTD03MIB.Cmplstunnelreverseperftable.Cmplstunnelreverseperfentry, self).__init__()

                self.yang_name = "cmplsTunnelReversePerfEntry"
                self.yang_parent_name = "cmplsTunnelReversePerfTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['mplstunnelindex','mplstunnelinstance','mplstunnelingresslsrid','mplstunnelegresslsrid']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('mplstunnelindex', YLeaf(YType.str, 'mplsTunnelIndex')),
                    ('mplstunnelinstance', YLeaf(YType.str, 'mplsTunnelInstance')),
                    ('mplstunnelingresslsrid', YLeaf(YType.str, 'mplsTunnelIngressLSRId')),
                    ('mplstunnelegresslsrid', YLeaf(YType.str, 'mplsTunnelEgressLSRId')),
                    ('cmplstunnelreverseperfpackets', YLeaf(YType.uint32, 'cmplsTunnelReversePerfPackets')),
                    ('cmplstunnelreverseperfhcpackets', YLeaf(YType.uint64, 'cmplsTunnelReversePerfHCPackets')),
                    ('cmplstunnelreverseperferrors', YLeaf(YType.uint32, 'cmplsTunnelReversePerfErrors')),
                    ('cmplstunnelreverseperfbytes', YLeaf(YType.uint32, 'cmplsTunnelReversePerfBytes')),
                    ('cmplstunnelreverseperfhcbytes', YLeaf(YType.uint64, 'cmplsTunnelReversePerfHCBytes')),
                ])
                self.mplstunnelindex = None
                self.mplstunnelinstance = None
                self.mplstunnelingresslsrid = None
                self.mplstunnelegresslsrid = None
                self.cmplstunnelreverseperfpackets = None
                self.cmplstunnelreverseperfhcpackets = None
                self.cmplstunnelreverseperferrors = None
                self.cmplstunnelreverseperfbytes = None
                self.cmplstunnelreverseperfhcbytes = None
                self._segment_path = lambda: "cmplsTunnelReversePerfEntry" + "[mplsTunnelIndex='" + str(self.mplstunnelindex) + "']" + "[mplsTunnelInstance='" + str(self.mplstunnelinstance) + "']" + "[mplsTunnelIngressLSRId='" + str(self.mplstunnelingresslsrid) + "']" + "[mplsTunnelEgressLSRId='" + str(self.mplstunnelegresslsrid) + "']"
                self._absolute_path = lambda: "CISCO-IETF-MPLS-TE-EXT-STD-03-MIB:CISCO-IETF-MPLS-TE-EXT-STD-03-MIB/cmplsTunnelReversePerfTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOIETFMPLSTEEXTSTD03MIB.Cmplstunnelreverseperftable.Cmplstunnelreverseperfentry, ['mplstunnelindex', 'mplstunnelinstance', 'mplstunnelingresslsrid', 'mplstunnelegresslsrid', 'cmplstunnelreverseperfpackets', 'cmplstunnelreverseperfhcpackets', 'cmplstunnelreverseperferrors', 'cmplstunnelreverseperfbytes', 'cmplstunnelreverseperfhcbytes'], name, value)

    def clone_ptr(self):
        self._top_entity = CISCOIETFMPLSTEEXTSTD03MIB()
        return self._top_entity

