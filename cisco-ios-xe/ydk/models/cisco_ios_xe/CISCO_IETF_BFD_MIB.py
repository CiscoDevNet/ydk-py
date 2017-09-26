""" CISCO_IETF_BFD_MIB 

This document contains the Management information base for
Bidirectional Forwarding Detection(BFD) Protocol as defined
in draft\-ietf\-bfd\-base\-06.txt.

BFD is a protocol intended to detect faults in the
bidirectional path between two forwarding engines, including
interfaces, data link(s), and to the extent possible the forwarding
engines themselves, with potentially very low latency.  It operates
independently of media, data protocols, and routing protocols.

This MIB module is based on the Internet Draft
draft\-ietf\-bfd\-mib\-03.txt and draft\-ietf\-bfd\-mib\-04.txt

"""
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class CiscoBfdDiag(Enum):
    """
    CiscoBfdDiag

    A common BFD diagnostic code.

    .. data:: noDiagnostic = 0

    .. data:: controlDetectionTimeExpired = 1

    .. data:: echoFunctionFailed = 2

    .. data:: neighborSignaledSessionDown = 3

    .. data:: forwardingPlaneReset = 4

    .. data:: pathDown = 5

    .. data:: concatenatedPathDown = 6

    .. data:: administrativelyDown = 7

    .. data:: reverseConcatenatedPathDown = 8

    """

    noDiagnostic = Enum.YLeaf(0, "noDiagnostic")

    controlDetectionTimeExpired = Enum.YLeaf(1, "controlDetectionTimeExpired")

    echoFunctionFailed = Enum.YLeaf(2, "echoFunctionFailed")

    neighborSignaledSessionDown = Enum.YLeaf(3, "neighborSignaledSessionDown")

    forwardingPlaneReset = Enum.YLeaf(4, "forwardingPlaneReset")

    pathDown = Enum.YLeaf(5, "pathDown")

    concatenatedPathDown = Enum.YLeaf(6, "concatenatedPathDown")

    administrativelyDown = Enum.YLeaf(7, "administrativelyDown")

    reverseConcatenatedPathDown = Enum.YLeaf(8, "reverseConcatenatedPathDown")



class CISCOIETFBFDMIB(Entity):
    """
    
    
    .. attribute:: ciscobfdscalarobjects
    
    	
    	**type**\:   :py:class:`Ciscobfdscalarobjects <ydk.models.cisco_ios_xe.CISCO_IETF_BFD_MIB.CISCOIETFBFDMIB.Ciscobfdscalarobjects>`
    
    .. attribute:: ciscobfdsessdiscmaptable
    
    	The BFD Session Discriminator Mapping Table maps a local discriminator value to associated BFD sessions' CiscoBfdSessIndexTC used in the ciscoBfdSessTable
    	**type**\:   :py:class:`Ciscobfdsessdiscmaptable <ydk.models.cisco_ios_xe.CISCO_IETF_BFD_MIB.CISCOIETFBFDMIB.Ciscobfdsessdiscmaptable>`
    
    .. attribute:: ciscobfdsessipmaptable
    
    	The BFD Session IP Mapping Table maps given ciscoBfdSessInterface, ciscoBfdSessAddrType, and ciscoBbfdSessAddr to an associated BFD sessions' CiscoBfdSessIndexTC used in the ciscoBfdSessTable. This table SHOULD contains those BFD sessions are of IP type\: singleHop(1) and multiHop(2)
    	**type**\:   :py:class:`Ciscobfdsessipmaptable <ydk.models.cisco_ios_xe.CISCO_IETF_BFD_MIB.CISCOIETFBFDMIB.Ciscobfdsessipmaptable>`
    
    .. attribute:: ciscobfdsessmaptable
    
    	The BFD Session Mapping Table maps the complex indexing of the BFD sessions to the flat  CiscoBfdSessIndexTC used in the ciscoBfdSessTable
    	**type**\:   :py:class:`Ciscobfdsessmaptable <ydk.models.cisco_ios_xe.CISCO_IETF_BFD_MIB.CISCOIETFBFDMIB.Ciscobfdsessmaptable>`
    
    .. attribute:: ciscobfdsesstable
    
    	The BFD Session Table describes the BFD sessions
    	**type**\:   :py:class:`Ciscobfdsesstable <ydk.models.cisco_ios_xe.CISCO_IETF_BFD_MIB.CISCOIETFBFDMIB.Ciscobfdsesstable>`
    
    

    """

    _prefix = 'CISCO-IETF-BFD-MIB'
    _revision = '2011-04-16'

    def __init__(self):
        super(CISCOIETFBFDMIB, self).__init__()
        self._top_entity = None

        self.yang_name = "CISCO-IETF-BFD-MIB"
        self.yang_parent_name = "CISCO-IETF-BFD-MIB"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {"ciscoBfdScalarObjects" : ("ciscobfdscalarobjects", CISCOIETFBFDMIB.Ciscobfdscalarobjects), "ciscoBfdSessDiscMapTable" : ("ciscobfdsessdiscmaptable", CISCOIETFBFDMIB.Ciscobfdsessdiscmaptable), "ciscoBfdSessIpMapTable" : ("ciscobfdsessipmaptable", CISCOIETFBFDMIB.Ciscobfdsessipmaptable), "ciscoBfdSessMapTable" : ("ciscobfdsessmaptable", CISCOIETFBFDMIB.Ciscobfdsessmaptable), "ciscoBfdSessTable" : ("ciscobfdsesstable", CISCOIETFBFDMIB.Ciscobfdsesstable)}
        self._child_list_classes = {}

        self.ciscobfdscalarobjects = CISCOIETFBFDMIB.Ciscobfdscalarobjects()
        self.ciscobfdscalarobjects.parent = self
        self._children_name_map["ciscobfdscalarobjects"] = "ciscoBfdScalarObjects"
        self._children_yang_names.add("ciscoBfdScalarObjects")

        self.ciscobfdsessdiscmaptable = CISCOIETFBFDMIB.Ciscobfdsessdiscmaptable()
        self.ciscobfdsessdiscmaptable.parent = self
        self._children_name_map["ciscobfdsessdiscmaptable"] = "ciscoBfdSessDiscMapTable"
        self._children_yang_names.add("ciscoBfdSessDiscMapTable")

        self.ciscobfdsessipmaptable = CISCOIETFBFDMIB.Ciscobfdsessipmaptable()
        self.ciscobfdsessipmaptable.parent = self
        self._children_name_map["ciscobfdsessipmaptable"] = "ciscoBfdSessIpMapTable"
        self._children_yang_names.add("ciscoBfdSessIpMapTable")

        self.ciscobfdsessmaptable = CISCOIETFBFDMIB.Ciscobfdsessmaptable()
        self.ciscobfdsessmaptable.parent = self
        self._children_name_map["ciscobfdsessmaptable"] = "ciscoBfdSessMapTable"
        self._children_yang_names.add("ciscoBfdSessMapTable")

        self.ciscobfdsesstable = CISCOIETFBFDMIB.Ciscobfdsesstable()
        self.ciscobfdsesstable.parent = self
        self._children_name_map["ciscobfdsesstable"] = "ciscoBfdSessTable"
        self._children_yang_names.add("ciscoBfdSessTable")
        self._segment_path = lambda: "CISCO-IETF-BFD-MIB:CISCO-IETF-BFD-MIB"


    class Ciscobfdscalarobjects(Entity):
        """
        
        
        .. attribute:: ciscobfdadminstatus
        
        	The global administrative status of BFD in this router. The value 'enabled' denotes that the BFD Process is  active on at least one interface; 'disabled' disables   it on all interfaces
        	**type**\:   :py:class:`Ciscobfdadminstatus <ydk.models.cisco_ios_xe.CISCO_IETF_BFD_MIB.CISCOIETFBFDMIB.Ciscobfdscalarobjects.Ciscobfdadminstatus>`
        
        .. attribute:: ciscobfdsessnotificationsenable
        
        	If this object is set to true(1), then it enables the emission of ciscoBfdSessUp and ciscoBfdSessDown  notifications; otherwise these notifications are not  emitted
        	**type**\:  bool
        
        .. attribute:: ciscobfdversionnumber
        
        	The current version number of the BFD protocol
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'CISCO-IETF-BFD-MIB'
        _revision = '2011-04-16'

        def __init__(self):
            super(CISCOIETFBFDMIB.Ciscobfdscalarobjects, self).__init__()

            self.yang_name = "ciscoBfdScalarObjects"
            self.yang_parent_name = "CISCO-IETF-BFD-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {}

            self.ciscobfdadminstatus = YLeaf(YType.enumeration, "ciscoBfdAdminStatus")

            self.ciscobfdsessnotificationsenable = YLeaf(YType.boolean, "ciscoBfdSessNotificationsEnable")

            self.ciscobfdversionnumber = YLeaf(YType.uint32, "ciscoBfdVersionNumber")
            self._segment_path = lambda: "ciscoBfdScalarObjects"
            self._absolute_path = lambda: "CISCO-IETF-BFD-MIB:CISCO-IETF-BFD-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOIETFBFDMIB.Ciscobfdscalarobjects, ['ciscobfdadminstatus', 'ciscobfdsessnotificationsenable', 'ciscobfdversionnumber'], name, value)

        class Ciscobfdadminstatus(Enum):
            """
            Ciscobfdadminstatus

            The global administrative status of BFD in this router.

            The value 'enabled' denotes that the BFD Process is 

            active on at least one interface; 'disabled' disables  

            it on all interfaces.

            .. data:: enabled = 1

            .. data:: disabled = 2

            """

            enabled = Enum.YLeaf(1, "enabled")

            disabled = Enum.YLeaf(2, "disabled")



    class Ciscobfdsessdiscmaptable(Entity):
        """
        The BFD Session Discriminator Mapping Table maps a
        local discriminator value to associated BFD sessions'
        CiscoBfdSessIndexTC used in the ciscoBfdSessTable.
        
        .. attribute:: ciscobfdsessdiscmapentry
        
        	Each row contains a mapping between a local discriminator value to an entry in ciscoBfdSessTable
        	**type**\: list of    :py:class:`Ciscobfdsessdiscmapentry <ydk.models.cisco_ios_xe.CISCO_IETF_BFD_MIB.CISCOIETFBFDMIB.Ciscobfdsessdiscmaptable.Ciscobfdsessdiscmapentry>`
        
        

        """

        _prefix = 'CISCO-IETF-BFD-MIB'
        _revision = '2011-04-16'

        def __init__(self):
            super(CISCOIETFBFDMIB.Ciscobfdsessdiscmaptable, self).__init__()

            self.yang_name = "ciscoBfdSessDiscMapTable"
            self.yang_parent_name = "CISCO-IETF-BFD-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"ciscoBfdSessDiscMapEntry" : ("ciscobfdsessdiscmapentry", CISCOIETFBFDMIB.Ciscobfdsessdiscmaptable.Ciscobfdsessdiscmapentry)}

            self.ciscobfdsessdiscmapentry = YList(self)
            self._segment_path = lambda: "ciscoBfdSessDiscMapTable"
            self._absolute_path = lambda: "CISCO-IETF-BFD-MIB:CISCO-IETF-BFD-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOIETFBFDMIB.Ciscobfdsessdiscmaptable, [], name, value)


        class Ciscobfdsessdiscmapentry(Entity):
            """
            Each row contains a mapping between a local discriminator
            value to an entry in ciscoBfdSessTable.
            
            .. attribute:: ciscobfdsessdiscriminator  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            	**refers to**\:  :py:class:`ciscobfdsessdiscriminator <ydk.models.cisco_ios_xe.CISCO_IETF_BFD_MIB.CISCOIETFBFDMIB.Ciscobfdsesstable.Ciscobfdsessentry>`
            
            .. attribute:: ciscobfdsessdiscmapindex
            
            	This object indicates the CiscoBfdSessIndexTC referred to by the index of this row. In essence, a mapping is  provided between this index and the ciscoBfdSessTable
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            

            """

            _prefix = 'CISCO-IETF-BFD-MIB'
            _revision = '2011-04-16'

            def __init__(self):
                super(CISCOIETFBFDMIB.Ciscobfdsessdiscmaptable.Ciscobfdsessdiscmapentry, self).__init__()

                self.yang_name = "ciscoBfdSessDiscMapEntry"
                self.yang_parent_name = "ciscoBfdSessDiscMapTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.ciscobfdsessdiscriminator = YLeaf(YType.str, "ciscoBfdSessDiscriminator")

                self.ciscobfdsessdiscmapindex = YLeaf(YType.uint32, "ciscoBfdSessDiscMapIndex")
                self._segment_path = lambda: "ciscoBfdSessDiscMapEntry" + "[ciscoBfdSessDiscriminator='" + self.ciscobfdsessdiscriminator.get() + "']"
                self._absolute_path = lambda: "CISCO-IETF-BFD-MIB:CISCO-IETF-BFD-MIB/ciscoBfdSessDiscMapTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOIETFBFDMIB.Ciscobfdsessdiscmaptable.Ciscobfdsessdiscmapentry, ['ciscobfdsessdiscriminator', 'ciscobfdsessdiscmapindex'], name, value)


    class Ciscobfdsessipmaptable(Entity):
        """
        The BFD Session IP Mapping Table maps given
        ciscoBfdSessInterface, ciscoBfdSessAddrType, and
        ciscoBbfdSessAddr to an associated BFD sessions'
        CiscoBfdSessIndexTC used in the ciscoBfdSessTable.
        This table SHOULD contains those BFD sessions are
        of IP type\: singleHop(1) and multiHop(2).
        
        .. attribute:: ciscobfdsessipmapentry
        
        	Each row contains a mapping between ciscoBfdSessInterface, ciscoBfdSessAddrType and ciscoBfdSessAddr values to an  entry in ciscoBfdSessTable
        	**type**\: list of    :py:class:`Ciscobfdsessipmapentry <ydk.models.cisco_ios_xe.CISCO_IETF_BFD_MIB.CISCOIETFBFDMIB.Ciscobfdsessipmaptable.Ciscobfdsessipmapentry>`
        
        

        """

        _prefix = 'CISCO-IETF-BFD-MIB'
        _revision = '2011-04-16'

        def __init__(self):
            super(CISCOIETFBFDMIB.Ciscobfdsessipmaptable, self).__init__()

            self.yang_name = "ciscoBfdSessIpMapTable"
            self.yang_parent_name = "CISCO-IETF-BFD-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"ciscoBfdSessIpMapEntry" : ("ciscobfdsessipmapentry", CISCOIETFBFDMIB.Ciscobfdsessipmaptable.Ciscobfdsessipmapentry)}

            self.ciscobfdsessipmapentry = YList(self)
            self._segment_path = lambda: "ciscoBfdSessIpMapTable"
            self._absolute_path = lambda: "CISCO-IETF-BFD-MIB:CISCO-IETF-BFD-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOIETFBFDMIB.Ciscobfdsessipmaptable, [], name, value)


        class Ciscobfdsessipmapentry(Entity):
            """
            Each row contains a mapping between ciscoBfdSessInterface,
            ciscoBfdSessAddrType and ciscoBfdSessAddr values to an 
            entry in ciscoBfdSessTable.
            
            .. attribute:: ciscobfdsessinterface  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ciscobfdsessinterface <ydk.models.cisco_ios_xe.CISCO_IETF_BFD_MIB.CISCOIETFBFDMIB.Ciscobfdsesstable.Ciscobfdsessentry>`
            
            .. attribute:: ciscobfdsessaddrtype  <key>
            
            	
            	**type**\:   :py:class:`InetAddressType <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetAddressType>`
            
            .. attribute:: ciscobfdsessaddr  <key>
            
            	
            	**type**\:  str
            
            	**length:** 0..255
            
            	**refers to**\:  :py:class:`ciscobfdsessaddr <ydk.models.cisco_ios_xe.CISCO_IETF_BFD_MIB.CISCOIETFBFDMIB.Ciscobfdsesstable.Ciscobfdsessentry>`
            
            .. attribute:: ciscobfdsessipmapindex
            
            	This object indicates the CiscoBfdSessIndexTC referred to by the indices of this row. In essence, a mapping is  provided between these indices and an entry in ciscoBfdSessTable
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            

            """

            _prefix = 'CISCO-IETF-BFD-MIB'
            _revision = '2011-04-16'

            def __init__(self):
                super(CISCOIETFBFDMIB.Ciscobfdsessipmaptable.Ciscobfdsessipmapentry, self).__init__()

                self.yang_name = "ciscoBfdSessIpMapEntry"
                self.yang_parent_name = "ciscoBfdSessIpMapTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.ciscobfdsessinterface = YLeaf(YType.str, "ciscoBfdSessInterface")

                self.ciscobfdsessaddrtype = YLeaf(YType.enumeration, "ciscoBfdSessAddrType")

                self.ciscobfdsessaddr = YLeaf(YType.str, "ciscoBfdSessAddr")

                self.ciscobfdsessipmapindex = YLeaf(YType.uint32, "ciscoBfdSessIpMapIndex")
                self._segment_path = lambda: "ciscoBfdSessIpMapEntry" + "[ciscoBfdSessInterface='" + self.ciscobfdsessinterface.get() + "']" + "[ciscoBfdSessAddrType='" + self.ciscobfdsessaddrtype.get() + "']" + "[ciscoBfdSessAddr='" + self.ciscobfdsessaddr.get() + "']"
                self._absolute_path = lambda: "CISCO-IETF-BFD-MIB:CISCO-IETF-BFD-MIB/ciscoBfdSessIpMapTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOIETFBFDMIB.Ciscobfdsessipmaptable.Ciscobfdsessipmapentry, ['ciscobfdsessinterface', 'ciscobfdsessaddrtype', 'ciscobfdsessaddr', 'ciscobfdsessipmapindex'], name, value)


    class Ciscobfdsessmaptable(Entity):
        """
        The BFD Session Mapping Table maps the complex
        indexing of the BFD sessions to the flat 
        CiscoBfdSessIndexTC used in the ciscoBfdSessTable.
        
        .. attribute:: ciscobfdsessmapentry
        
        	The BFD Session Entry describes BFD session that is mapped to this index
        	**type**\: list of    :py:class:`Ciscobfdsessmapentry <ydk.models.cisco_ios_xe.CISCO_IETF_BFD_MIB.CISCOIETFBFDMIB.Ciscobfdsessmaptable.Ciscobfdsessmapentry>`
        
        

        """

        _prefix = 'CISCO-IETF-BFD-MIB'
        _revision = '2011-04-16'

        def __init__(self):
            super(CISCOIETFBFDMIB.Ciscobfdsessmaptable, self).__init__()

            self.yang_name = "ciscoBfdSessMapTable"
            self.yang_parent_name = "CISCO-IETF-BFD-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"ciscoBfdSessMapEntry" : ("ciscobfdsessmapentry", CISCOIETFBFDMIB.Ciscobfdsessmaptable.Ciscobfdsessmapentry)}

            self.ciscobfdsessmapentry = YList(self)
            self._segment_path = lambda: "ciscoBfdSessMapTable"
            self._absolute_path = lambda: "CISCO-IETF-BFD-MIB:CISCO-IETF-BFD-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOIETFBFDMIB.Ciscobfdsessmaptable, [], name, value)


        class Ciscobfdsessmapentry(Entity):
            """
            The BFD Session Entry describes BFD session
            that is mapped to this index.
            
            .. attribute:: ciscobfdsessapplicationid  <key>
            
            	
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**refers to**\:  :py:class:`ciscobfdsessapplicationid <ydk.models.cisco_ios_xe.CISCO_IETF_BFD_MIB.CISCOIETFBFDMIB.Ciscobfdsesstable.Ciscobfdsessentry>`
            
            .. attribute:: ciscobfdsessdiscriminator  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            	**refers to**\:  :py:class:`ciscobfdsessdiscriminator <ydk.models.cisco_ios_xe.CISCO_IETF_BFD_MIB.CISCOIETFBFDMIB.Ciscobfdsesstable.Ciscobfdsessentry>`
            
            .. attribute:: ciscobfdsessaddrtype  <key>
            
            	
            	**type**\:   :py:class:`InetAddressType <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetAddressType>`
            
            .. attribute:: ciscobfdsessaddr  <key>
            
            	
            	**type**\:  str
            
            	**length:** 0..255
            
            	**refers to**\:  :py:class:`ciscobfdsessaddr <ydk.models.cisco_ios_xe.CISCO_IETF_BFD_MIB.CISCOIETFBFDMIB.Ciscobfdsesstable.Ciscobfdsessentry>`
            
            .. attribute:: ciscobfdsessmapbfdindex
            
            	This object indicates the CiscoBfdSessIndexTC referred to by the indices of this row. In essence, a mapping is  provided between these indices and the ciscoBfdSessTable
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            

            """

            _prefix = 'CISCO-IETF-BFD-MIB'
            _revision = '2011-04-16'

            def __init__(self):
                super(CISCOIETFBFDMIB.Ciscobfdsessmaptable.Ciscobfdsessmapentry, self).__init__()

                self.yang_name = "ciscoBfdSessMapEntry"
                self.yang_parent_name = "ciscoBfdSessMapTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.ciscobfdsessapplicationid = YLeaf(YType.str, "ciscoBfdSessApplicationId")

                self.ciscobfdsessdiscriminator = YLeaf(YType.str, "ciscoBfdSessDiscriminator")

                self.ciscobfdsessaddrtype = YLeaf(YType.enumeration, "ciscoBfdSessAddrType")

                self.ciscobfdsessaddr = YLeaf(YType.str, "ciscoBfdSessAddr")

                self.ciscobfdsessmapbfdindex = YLeaf(YType.uint32, "ciscoBfdSessMapBfdIndex")
                self._segment_path = lambda: "ciscoBfdSessMapEntry" + "[ciscoBfdSessApplicationId='" + self.ciscobfdsessapplicationid.get() + "']" + "[ciscoBfdSessDiscriminator='" + self.ciscobfdsessdiscriminator.get() + "']" + "[ciscoBfdSessAddrType='" + self.ciscobfdsessaddrtype.get() + "']" + "[ciscoBfdSessAddr='" + self.ciscobfdsessaddr.get() + "']"
                self._absolute_path = lambda: "CISCO-IETF-BFD-MIB:CISCO-IETF-BFD-MIB/ciscoBfdSessMapTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOIETFBFDMIB.Ciscobfdsessmaptable.Ciscobfdsessmapentry, ['ciscobfdsessapplicationid', 'ciscobfdsessdiscriminator', 'ciscobfdsessaddrtype', 'ciscobfdsessaddr', 'ciscobfdsessmapbfdindex'], name, value)


    class Ciscobfdsesstable(Entity):
        """
        The BFD Session Table describes the BFD sessions.
        
        .. attribute:: ciscobfdsessentry
        
        	The BFD Session Entry describes BFD session
        	**type**\: list of    :py:class:`Ciscobfdsessentry <ydk.models.cisco_ios_xe.CISCO_IETF_BFD_MIB.CISCOIETFBFDMIB.Ciscobfdsesstable.Ciscobfdsessentry>`
        
        

        """

        _prefix = 'CISCO-IETF-BFD-MIB'
        _revision = '2011-04-16'

        def __init__(self):
            super(CISCOIETFBFDMIB.Ciscobfdsesstable, self).__init__()

            self.yang_name = "ciscoBfdSessTable"
            self.yang_parent_name = "CISCO-IETF-BFD-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"ciscoBfdSessEntry" : ("ciscobfdsessentry", CISCOIETFBFDMIB.Ciscobfdsesstable.Ciscobfdsessentry)}

            self.ciscobfdsessentry = YList(self)
            self._segment_path = lambda: "ciscoBfdSessTable"
            self._absolute_path = lambda: "CISCO-IETF-BFD-MIB:CISCO-IETF-BFD-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOIETFBFDMIB.Ciscobfdsesstable, [], name, value)


        class Ciscobfdsessentry(Entity):
            """
            The BFD Session Entry describes BFD session.
            
            .. attribute:: ciscobfdsessindex  <key>
            
            	This object contains an index used to represent a unique BFD session on this device
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            .. attribute:: ciscobfdsessaddr
            
            	This object specifies the neighboring IP address which is being monitored with this BFD session. It can also be used to enabled BFD on a specific   interface. The value is set to zero when BFD session is not   associated with a specific interface
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: ciscobfdsessaddrtype
            
            	This object specifies IP address type of the neighboring IP address which is being monitored with this BFD session.  Only values unknown(0), ipv4(1) or ipv6(2)  have to be supported.    A value of unknown(0) is allowed only when   the outgoing interface is of type point\-to\-point, or  when the BFD session is not associated with a specific   interface.   If any other unsupported values are attempted in a set  operation, the agent MUST return an inconsistentValue   error
            	**type**\:   :py:class:`InetAddressType <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetAddressType>`
            
            .. attribute:: ciscobfdsessapplicationid
            
            	This object contains an index used to indicate a local application which owns or maintains this  BFD session. For instance, the MPLS VPN process may  maintain a subset of the total number of BFD  sessions.  This application ID provides a convenient  way to segregate sessions by the applications which  maintain them
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ciscobfdsessauthenticationtype
            
            	The Authentication Type used for this BFD session. This field is valid only when the Authentication Present bit is set
            	**type**\:   :py:class:`Ciscobfdsessauthenticationtype <ydk.models.cisco_ios_xe.CISCO_IETF_BFD_MIB.CISCOIETFBFDMIB.Ciscobfdsesstable.Ciscobfdsessentry.Ciscobfdsessauthenticationtype>`
            
            .. attribute:: ciscobfdsessauthpresflag
            
            	This object indicates that the local system's desire to use Authentication. Specifically, it is set   to true(1) if the local system wishes the session   to be authenticated or false(0) if not
            	**type**\:  bool
            
            .. attribute:: ciscobfdsesscontrolplanindepflag
            
            	This object indicates that the local system's ability to continue to function through a disruption of   the control plane. Specifically, it is set   to true(1) if the local system BFD implementation is  independent of the control plane. Otherwise, the   value is set to false(0)
            	**type**\:  bool
            
            .. attribute:: ciscobfdsessdemandmodedesiredflag
            
            	This object indicates that the local system's desire to use Demand mode. Specifically, it is set   to true(1) if the local system wishes to use   Demand mode or false(0) if not
            	**type**\:  bool
            
            .. attribute:: ciscobfdsessdesiredmintxinterval
            
            	This object specifies the minimum interval, in microseconds, that the local system would like to use when       transmitting BFD Control packets
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ciscobfdsessdetectmult
            
            	This object specifies the Detect time multiplier
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ciscobfdsessdiag
            
            	A diagnostic code specifying the local system's reason for the last transition of the session from up(1)   to some other state
            	**type**\:   :py:class:`CiscoBfdDiag <ydk.models.cisco_ios_xe.CISCO_IETF_BFD_MIB.CiscoBfdDiag>`
            
            .. attribute:: ciscobfdsessdiscriminator
            
            	This object specifies the local discriminator for this BFD session, used to uniquely identify it
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            .. attribute:: ciscobfdsessechofuncmodedesiredflag
            
            	This object indicates that the local system's desire to use Echo mode. Specifically, it is set   to true(1) if the local system wishes to use   Echo mode or false(0) if not
            	**type**\:  bool
            
            .. attribute:: ciscobfdsessinterface
            
            	This object contains an interface index used to indicate the interface which this BFD session is running on
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            .. attribute:: ciscobfdsessopermode
            
            	This object specifies current operating mode that BFD session is operating in
            	**type**\:   :py:class:`Ciscobfdsessopermode <ydk.models.cisco_ios_xe.CISCO_IETF_BFD_MIB.CISCOIETFBFDMIB.Ciscobfdsesstable.Ciscobfdsessentry.Ciscobfdsessopermode>`
            
            .. attribute:: ciscobfdsessperfdisctime
            
            	The value of sysUpTime on the most recent occasion at which any one or more of the session counters suffered  a discontinuity.    The relevant counters are the specific instances associated   with this BFD session of any Counter32 object contained in  the ciscoBfdSessPerfTable. If no such discontinuities have occurred   since the last re\-initialization of the local management  subsystem, then this object contains a zero value
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ciscobfdsessperflastcommlostdiag
            
            	The BFD diag code for the last time communication was lost with the neighbor. If no such down event exists this object   contains a zero value
            	**type**\:   :py:class:`CiscoBfdDiag <ydk.models.cisco_ios_xe.CISCO_IETF_BFD_MIB.CiscoBfdDiag>`
            
            .. attribute:: ciscobfdsessperflastsessdowntime
            
            	The value of sysUpTime on the most recent occasion at which the last time communication was lost with the neighbor. If   no such down event exist this object contains a zero value
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ciscobfdsessperfpktin
            
            	The total number of BFD messages received for this BFD session
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ciscobfdsessperfpktinhc
            
            	This value represents the total number of BFD messages received for this BFD session. It MUST be equal to the  least significant 32 bits of ciscoBfdSessPerfPktIn  if ciscoBfdSessPerfPktInHC is supported according to  the rules spelled out in RFC2863
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: ciscobfdsessperfpktout
            
            	The total number of BFD messages sent for this BFD session
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ciscobfdsessperfpktouthc
            
            	This value represents the total number of total number of BFD messages transmitted for this   BFD session. It MUST be equal to the  least significant 32 bits of ciscoBfdSessPerfPktIn  if ciscoBfdSessPerfPktOutHC is supported according to  the rules spelled out in RFC2863
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: ciscobfdsessperfsessupcount
            
            	The number of times this session has gone into the Up state since the router last rebooted
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ciscobfdsessremotediscr
            
            	This object specifies the session discriminator chosen by the remote system for this BFD session
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ciscobfdsessremoteheardflag
            
            	This object specifies status of BFD packet reception from the remote system. Specifically, it is set to true(1) if  the local system is actively receiving BFD packets from the   remote system, and is set to false(0) if the local system   has not received BFD packets recently (within the detection   time) or if the local system is attempting to tear down  the BFD session
            	**type**\:  bool
            
            .. attribute:: ciscobfdsessreqminechorxinterval
            
            	This object specifies the minimum interval, in microseconds, between received BFD Echo packets that this  system is capable of supporting
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ciscobfdsessreqminrxinterval
            
            	This object specifies the minimum interval, in microseconds, between received  BFD Control packets the   local system is capable of supporting
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ciscobfdsessrowstatus
            
            	This variable is used to create, modify, and/or delete a row in this table. When a row in this  table has a row in the active(1) state, no   objects in this row can be modified except the  ciscoBfdSessRowStatus and ciscoBfdSessStorageType
            	**type**\:   :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            .. attribute:: ciscobfdsessstate
            
            	The perceived state of the BFD session
            	**type**\:   :py:class:`Ciscobfdsessstate <ydk.models.cisco_ios_xe.CISCO_IETF_BFD_MIB.CISCOIETFBFDMIB.Ciscobfdsesstable.Ciscobfdsessentry.Ciscobfdsessstate>`
            
            .. attribute:: ciscobfdsessstortype
            
            	This variable indicates the storage type for this object. Conceptual rows having the value   'permanent' need not allow write\-access to any   columnar objects in the row
            	**type**\:   :py:class:`StorageType <ydk.models.cisco_ios_xe.SNMPv2_TC.StorageType>`
            
            .. attribute:: ciscobfdsesstype
            
            	The type of this BFD session
            	**type**\:   :py:class:`Ciscobfdsesstype <ydk.models.cisco_ios_xe.CISCO_IETF_BFD_MIB.CISCOIETFBFDMIB.Ciscobfdsesstable.Ciscobfdsessentry.Ciscobfdsesstype>`
            
            .. attribute:: ciscobfdsessudpport
            
            	The destination UDP Port for BFD. The default value is the well\-known value for this port. BFD State failing(5) is only applicable if this BFD session is running version 0
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: ciscobfdsessuptime
            
            	The value of sysUpTime on the most recent occasion at which the session came up. If no such up event exists this object  contains a zero value
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ciscobfdsessversionnumber
            
            	The version number of the BFD protocol that this session is running in
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'CISCO-IETF-BFD-MIB'
            _revision = '2011-04-16'

            def __init__(self):
                super(CISCOIETFBFDMIB.Ciscobfdsesstable.Ciscobfdsessentry, self).__init__()

                self.yang_name = "ciscoBfdSessEntry"
                self.yang_parent_name = "ciscoBfdSessTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.ciscobfdsessindex = YLeaf(YType.uint32, "ciscoBfdSessIndex")

                self.ciscobfdsessaddr = YLeaf(YType.str, "ciscoBfdSessAddr")

                self.ciscobfdsessaddrtype = YLeaf(YType.enumeration, "ciscoBfdSessAddrType")

                self.ciscobfdsessapplicationid = YLeaf(YType.uint32, "ciscoBfdSessApplicationId")

                self.ciscobfdsessauthenticationtype = YLeaf(YType.enumeration, "ciscoBfdSessAuthenticationType")

                self.ciscobfdsessauthpresflag = YLeaf(YType.boolean, "ciscoBfdSessAuthPresFlag")

                self.ciscobfdsesscontrolplanindepflag = YLeaf(YType.boolean, "ciscoBfdSessControlPlanIndepFlag")

                self.ciscobfdsessdemandmodedesiredflag = YLeaf(YType.boolean, "ciscoBfdSessDemandModeDesiredFlag")

                self.ciscobfdsessdesiredmintxinterval = YLeaf(YType.uint32, "ciscoBfdSessDesiredMinTxInterval")

                self.ciscobfdsessdetectmult = YLeaf(YType.uint32, "ciscoBfdSessDetectMult")

                self.ciscobfdsessdiag = YLeaf(YType.enumeration, "ciscoBfdSessDiag")

                self.ciscobfdsessdiscriminator = YLeaf(YType.uint32, "ciscoBfdSessDiscriminator")

                self.ciscobfdsessechofuncmodedesiredflag = YLeaf(YType.boolean, "ciscoBfdSessEchoFuncModeDesiredFlag")

                self.ciscobfdsessinterface = YLeaf(YType.int32, "ciscoBfdSessInterface")

                self.ciscobfdsessopermode = YLeaf(YType.enumeration, "ciscoBfdSessOperMode")

                self.ciscobfdsessperfdisctime = YLeaf(YType.uint32, "ciscoBfdSessPerfDiscTime")

                self.ciscobfdsessperflastcommlostdiag = YLeaf(YType.enumeration, "ciscoBfdSessPerfLastCommLostDiag")

                self.ciscobfdsessperflastsessdowntime = YLeaf(YType.uint32, "ciscoBfdSessPerfLastSessDownTime")

                self.ciscobfdsessperfpktin = YLeaf(YType.uint32, "ciscoBfdSessPerfPktIn")

                self.ciscobfdsessperfpktinhc = YLeaf(YType.uint64, "ciscoBfdSessPerfPktInHC")

                self.ciscobfdsessperfpktout = YLeaf(YType.uint32, "ciscoBfdSessPerfPktOut")

                self.ciscobfdsessperfpktouthc = YLeaf(YType.uint64, "ciscoBfdSessPerfPktOutHC")

                self.ciscobfdsessperfsessupcount = YLeaf(YType.uint32, "ciscoBfdSessPerfSessUpCount")

                self.ciscobfdsessremotediscr = YLeaf(YType.uint32, "ciscoBfdSessRemoteDiscr")

                self.ciscobfdsessremoteheardflag = YLeaf(YType.boolean, "ciscoBfdSessRemoteHeardFlag")

                self.ciscobfdsessreqminechorxinterval = YLeaf(YType.uint32, "ciscoBfdSessReqMinEchoRxInterval")

                self.ciscobfdsessreqminrxinterval = YLeaf(YType.uint32, "ciscoBfdSessReqMinRxInterval")

                self.ciscobfdsessrowstatus = YLeaf(YType.enumeration, "ciscoBfdSessRowStatus")

                self.ciscobfdsessstate = YLeaf(YType.enumeration, "ciscoBfdSessState")

                self.ciscobfdsessstortype = YLeaf(YType.enumeration, "ciscoBfdSessStorType")

                self.ciscobfdsesstype = YLeaf(YType.enumeration, "ciscoBfdSessType")

                self.ciscobfdsessudpport = YLeaf(YType.uint16, "ciscoBfdSessUdpPort")

                self.ciscobfdsessuptime = YLeaf(YType.uint32, "ciscoBfdSessUpTime")

                self.ciscobfdsessversionnumber = YLeaf(YType.uint32, "ciscoBfdSessVersionNumber")
                self._segment_path = lambda: "ciscoBfdSessEntry" + "[ciscoBfdSessIndex='" + self.ciscobfdsessindex.get() + "']"
                self._absolute_path = lambda: "CISCO-IETF-BFD-MIB:CISCO-IETF-BFD-MIB/ciscoBfdSessTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOIETFBFDMIB.Ciscobfdsesstable.Ciscobfdsessentry, ['ciscobfdsessindex', 'ciscobfdsessaddr', 'ciscobfdsessaddrtype', 'ciscobfdsessapplicationid', 'ciscobfdsessauthenticationtype', 'ciscobfdsessauthpresflag', 'ciscobfdsesscontrolplanindepflag', 'ciscobfdsessdemandmodedesiredflag', 'ciscobfdsessdesiredmintxinterval', 'ciscobfdsessdetectmult', 'ciscobfdsessdiag', 'ciscobfdsessdiscriminator', 'ciscobfdsessechofuncmodedesiredflag', 'ciscobfdsessinterface', 'ciscobfdsessopermode', 'ciscobfdsessperfdisctime', 'ciscobfdsessperflastcommlostdiag', 'ciscobfdsessperflastsessdowntime', 'ciscobfdsessperfpktin', 'ciscobfdsessperfpktinhc', 'ciscobfdsessperfpktout', 'ciscobfdsessperfpktouthc', 'ciscobfdsessperfsessupcount', 'ciscobfdsessremotediscr', 'ciscobfdsessremoteheardflag', 'ciscobfdsessreqminechorxinterval', 'ciscobfdsessreqminrxinterval', 'ciscobfdsessrowstatus', 'ciscobfdsessstate', 'ciscobfdsessstortype', 'ciscobfdsesstype', 'ciscobfdsessudpport', 'ciscobfdsessuptime', 'ciscobfdsessversionnumber'], name, value)

            class Ciscobfdsessauthenticationtype(Enum):
                """
                Ciscobfdsessauthenticationtype

                The Authentication Type used for this BFD session. This

                field is valid only when the Authentication Present bit is set

                .. data:: simplePassword = 1

                .. data:: keyedMD5 = 2

                .. data:: meticulousKeyedMD5 = 3

                .. data:: keyedSHA1 = 4

                .. data:: meticulousKeyedSHA1 = 5

                """

                simplePassword = Enum.YLeaf(1, "simplePassword")

                keyedMD5 = Enum.YLeaf(2, "keyedMD5")

                meticulousKeyedMD5 = Enum.YLeaf(3, "meticulousKeyedMD5")

                keyedSHA1 = Enum.YLeaf(4, "keyedSHA1")

                meticulousKeyedSHA1 = Enum.YLeaf(5, "meticulousKeyedSHA1")


            class Ciscobfdsessopermode(Enum):
                """
                Ciscobfdsessopermode

                This object specifies current operating mode that BFD

                session is operating in.

                .. data:: asyncModeWEchoFun = 1

                .. data:: asynchModeWOEchoFun = 2

                .. data:: demandModeWEchoFunction = 3

                .. data:: demandModeWOEchoFunction = 4

                """

                asyncModeWEchoFun = Enum.YLeaf(1, "asyncModeWEchoFun")

                asynchModeWOEchoFun = Enum.YLeaf(2, "asynchModeWOEchoFun")

                demandModeWEchoFunction = Enum.YLeaf(3, "demandModeWEchoFunction")

                demandModeWOEchoFunction = Enum.YLeaf(4, "demandModeWOEchoFunction")


            class Ciscobfdsessstate(Enum):
                """
                Ciscobfdsessstate

                The perceived state of the BFD session.

                .. data:: adminDown = 1

                .. data:: down = 2

                .. data:: init = 3

                .. data:: up = 4

                .. data:: failing = 5

                """

                adminDown = Enum.YLeaf(1, "adminDown")

                down = Enum.YLeaf(2, "down")

                init = Enum.YLeaf(3, "init")

                up = Enum.YLeaf(4, "up")

                failing = Enum.YLeaf(5, "failing")


            class Ciscobfdsesstype(Enum):
                """
                Ciscobfdsesstype

                The type of this BFD session.

                .. data:: singleHop = 1

                .. data:: multiHop = 2

                """

                singleHop = Enum.YLeaf(1, "singleHop")

                multiHop = Enum.YLeaf(2, "multiHop")


    def clone_ptr(self):
        self._top_entity = CISCOIETFBFDMIB()
        return self._top_entity

