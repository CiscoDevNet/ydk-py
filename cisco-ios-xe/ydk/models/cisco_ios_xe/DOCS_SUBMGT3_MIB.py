""" DOCS_SUBMGT3_MIB 

This MIB module contains the management objects for the 
CMTS control of the IP4 and IPv6 traffic with origin and 
destination to CMs and/or CPEs behind the CM.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class DOCSSUBMGT3MIB(Entity):
    """
    
    
    .. attribute:: docssubmgt3base
    
    	
    	**type**\:  :py:class:`DocsSubmgt3Base <ydk.models.cisco_ios_xe.DOCS_SUBMGT3_MIB.DOCSSUBMGT3MIB.DocsSubmgt3Base>`
    
    .. attribute:: docssubmgt3cpectrltable
    
    	This object maintains per\-CM traffic policies enforced  by the CMTS. The CMTS acquires the CM traffic policies  through the CM registration process, or in the  absence of some or all of those parameters, from the  Base object. The CM information and controls are meaningful  and used by the CMTS, but only after the CM is  operational
    	**type**\:  :py:class:`DocsSubmgt3CpeCtrlTable <ydk.models.cisco_ios_xe.DOCS_SUBMGT3_MIB.DOCSSUBMGT3MIB.DocsSubmgt3CpeCtrlTable>`
    
    .. attribute:: docssubmgt3cpeiptable
    
    	This object defines the list of IP Addresses behind  the CM known by the CMTS.   If the Active attribute of the CpeCtrl object associated  with a CM is set to 'true' and the CMTS receives an  IP packet from a CM that contains a source IP address that  does not match one of the CPE IP addresses associated  with this CM, one of two things occurs. If the number  of CPE IPs is less than the MaxCpeIp of the CpeCtrl object  for that CM, the source IP address is added to this  object and the packet is forwarded; otherwise, the  packet is dropped
    	**type**\:  :py:class:`DocsSubmgt3CpeIpTable <ydk.models.cisco_ios_xe.DOCS_SUBMGT3_MIB.DOCSSUBMGT3MIB.DocsSubmgt3CpeIpTable>`
    
    .. attribute:: docssubmgt3grptable
    
    	This object defines the set of downstream and upstream  filter groups that the CMTS applies to traffic associated  with that CM
    	**type**\:  :py:class:`DocsSubmgt3GrpTable <ydk.models.cisco_ios_xe.DOCS_SUBMGT3_MIB.DOCSSUBMGT3MIB.DocsSubmgt3GrpTable>`
    
    .. attribute:: docssubmgt3filtergrptable
    
    	This object describes a set of filter or classifier  criteria. Classifiers are assigned by group to the  individual CMs. That assignment is made via the 'Subscriber  Management TLVs' encodings sent upstream from  the CM to the CMTS during registration or in their  absence, default values configured in the CMTS.  A Filter Group ID (GrpId) is a set of rules that correspond  to the expansion of a UDC Group ID into UDC individual   classification rules.  The Filter Group Ids are generated   whenever the CMTS is configured to send UDCs during the CM   registration process. Implementation of L2 classification   criteria is optional for the CMTS; LLC/MAC upstream and   downstream filter criteria can be ignored during the packet  matching process
    	**type**\:  :py:class:`DocsSubmgt3FilterGrpTable <ydk.models.cisco_ios_xe.DOCS_SUBMGT3_MIB.DOCSSUBMGT3MIB.DocsSubmgt3FilterGrpTable>`
    
    

    """

    _prefix = 'DOCS-SUBMGT3-MIB'
    _revision = '2007-05-18'

    def __init__(self):
        super(DOCSSUBMGT3MIB, self).__init__()
        self._top_entity = None

        self.yang_name = "DOCS-SUBMGT3-MIB"
        self.yang_parent_name = "DOCS-SUBMGT3-MIB"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("docsSubmgt3Base", ("docssubmgt3base", DOCSSUBMGT3MIB.DocsSubmgt3Base)), ("docsSubmgt3CpeCtrlTable", ("docssubmgt3cpectrltable", DOCSSUBMGT3MIB.DocsSubmgt3CpeCtrlTable)), ("docsSubmgt3CpeIpTable", ("docssubmgt3cpeiptable", DOCSSUBMGT3MIB.DocsSubmgt3CpeIpTable)), ("docsSubmgt3GrpTable", ("docssubmgt3grptable", DOCSSUBMGT3MIB.DocsSubmgt3GrpTable)), ("docsSubmgt3FilterGrpTable", ("docssubmgt3filtergrptable", DOCSSUBMGT3MIB.DocsSubmgt3FilterGrpTable))])
        self._leafs = OrderedDict()

        self.docssubmgt3base = DOCSSUBMGT3MIB.DocsSubmgt3Base()
        self.docssubmgt3base.parent = self
        self._children_name_map["docssubmgt3base"] = "docsSubmgt3Base"

        self.docssubmgt3cpectrltable = DOCSSUBMGT3MIB.DocsSubmgt3CpeCtrlTable()
        self.docssubmgt3cpectrltable.parent = self
        self._children_name_map["docssubmgt3cpectrltable"] = "docsSubmgt3CpeCtrlTable"

        self.docssubmgt3cpeiptable = DOCSSUBMGT3MIB.DocsSubmgt3CpeIpTable()
        self.docssubmgt3cpeiptable.parent = self
        self._children_name_map["docssubmgt3cpeiptable"] = "docsSubmgt3CpeIpTable"

        self.docssubmgt3grptable = DOCSSUBMGT3MIB.DocsSubmgt3GrpTable()
        self.docssubmgt3grptable.parent = self
        self._children_name_map["docssubmgt3grptable"] = "docsSubmgt3GrpTable"

        self.docssubmgt3filtergrptable = DOCSSUBMGT3MIB.DocsSubmgt3FilterGrpTable()
        self.docssubmgt3filtergrptable.parent = self
        self._children_name_map["docssubmgt3filtergrptable"] = "docsSubmgt3FilterGrpTable"
        self._segment_path = lambda: "DOCS-SUBMGT3-MIB:DOCS-SUBMGT3-MIB"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(DOCSSUBMGT3MIB, [], name, value)


    class DocsSubmgt3Base(Entity):
        """
        
        
        .. attribute:: docssubmgt3basecpemaxipv4def
        
        	This attribute represents the maximum number of IPv4   Addresses allowed for the CM's CPEs if not signaled in the   registration process
        	**type**\: int
        
        	**range:** 0..1023
        
        .. attribute:: docssubmgt3basecpemaxipv6prefixdef
        
        	This attribute represents the maximum number of IPv6   prefixes allowed for the CM's CPEs if not signaled in  the registration process
        	**type**\: int
        
        	**range:** 0..1023
        
        .. attribute:: docssubmgt3basecpeactivedef
        
        	This attribute represents the default value for enabling  Subscriber Management filters and controls  in the CM if the parameter is not signaled in the DOCSIS  Registration process
        	**type**\: bool
        
        .. attribute:: docssubmgt3basecpelearnabledef
        
        	This attribute represents the default value for enabling  the CPE learning process for the CM if the parameter  is not signaled in the DOCSIS Registration process
        	**type**\: bool
        
        .. attribute:: docssubmgt3basesubfilterdowndef
        
        	This attribute represents the default value for the  subscriber (CPE) downstream filter group for the  CM if the parameter is not signaled in the DOCSIS Registration  process
        	**type**\: int
        
        	**range:** 0..1024
        
        .. attribute:: docssubmgt3basesubfilterupdef
        
        	This attribute represents the default value for the  subscriber (CPE) upstream filter group for the CM  if the parameter is not signaled in the DOCSIS Registration  process
        	**type**\: int
        
        	**range:** 0..1024
        
        .. attribute:: docssubmgt3basecmfilterdowndef
        
        	This attribute represents the default value for the  CM stack downstream filter group applying to the CM  if the parameter is not signaled in the DOCSIS Registration  process
        	**type**\: int
        
        	**range:** 0..1024
        
        .. attribute:: docssubmgt3basecmfilterupdef
        
        	This attribute represents the default value for the  CM stack upstream filter group applying to the CM if  the parameter is not signaled in the DOCSIS Registration  process
        	**type**\: int
        
        	**range:** 0..1024
        
        .. attribute:: docssubmgt3basepsfilterdowndef
        
        	This attribute represents the default value for the  PS or eRouter downstream filter group for the CM if  the parameter is not signaled in the DOCSIS Registration  process
        	**type**\: int
        
        	**range:** 0..1024
        
        .. attribute:: docssubmgt3basepsfilterupdef
        
        	This attribute represents the default value for the  PS or eRouter upstream filter group for the CM if the  parameter is not signaled in the DOCSIS Registration  process
        	**type**\: int
        
        	**range:** 0..1024
        
        .. attribute:: docssubmgt3basemtafilterdowndef
        
        	This attribute represents the default value for the  MTA downstream filter group for the CM if the parameter  is not signaled in the DOCSIS Registration process
        	**type**\: int
        
        	**range:** 0..1024
        
        .. attribute:: docssubmgt3basemtafilterupdef
        
        	This attribute represents the default value for the  MTA upstream filter group for the CM if the parameter  is not signaled in the DOCSIS Registration process
        	**type**\: int
        
        	**range:** 0..1024
        
        .. attribute:: docssubmgt3basestbfilterdowndef
        
        	This attribute represents the default value for the  STB downstream filter group for the CM if the parameter  is not signaled in the DOCSIS Registration process
        	**type**\: int
        
        	**range:** 0..1024
        
        .. attribute:: docssubmgt3basestbfilterupdef
        
        	This attribute represents the default value for the  STB upstream filter group for the CM if the parameter  is not signaled in the DOCSIS Registration process
        	**type**\: int
        
        	**range:** 0..1024
        
        

        """

        _prefix = 'DOCS-SUBMGT3-MIB'
        _revision = '2007-05-18'

        def __init__(self):
            super(DOCSSUBMGT3MIB.DocsSubmgt3Base, self).__init__()

            self.yang_name = "docsSubmgt3Base"
            self.yang_parent_name = "DOCS-SUBMGT3-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('docssubmgt3basecpemaxipv4def', (YLeaf(YType.uint32, 'docsSubmgt3BaseCpeMaxIpv4Def'), ['int'])),
                ('docssubmgt3basecpemaxipv6prefixdef', (YLeaf(YType.uint32, 'docsSubmgt3BaseCpeMaxIpv6PrefixDef'), ['int'])),
                ('docssubmgt3basecpeactivedef', (YLeaf(YType.boolean, 'docsSubmgt3BaseCpeActiveDef'), ['bool'])),
                ('docssubmgt3basecpelearnabledef', (YLeaf(YType.boolean, 'docsSubmgt3BaseCpeLearnableDef'), ['bool'])),
                ('docssubmgt3basesubfilterdowndef', (YLeaf(YType.uint32, 'docsSubmgt3BaseSubFilterDownDef'), ['int'])),
                ('docssubmgt3basesubfilterupdef', (YLeaf(YType.uint32, 'docsSubmgt3BaseSubFilterUpDef'), ['int'])),
                ('docssubmgt3basecmfilterdowndef', (YLeaf(YType.uint32, 'docsSubmgt3BaseCmFilterDownDef'), ['int'])),
                ('docssubmgt3basecmfilterupdef', (YLeaf(YType.uint32, 'docsSubmgt3BaseCmFilterUpDef'), ['int'])),
                ('docssubmgt3basepsfilterdowndef', (YLeaf(YType.uint32, 'docsSubmgt3BasePsFilterDownDef'), ['int'])),
                ('docssubmgt3basepsfilterupdef', (YLeaf(YType.uint32, 'docsSubmgt3BasePsFilterUpDef'), ['int'])),
                ('docssubmgt3basemtafilterdowndef', (YLeaf(YType.uint32, 'docsSubmgt3BaseMtaFilterDownDef'), ['int'])),
                ('docssubmgt3basemtafilterupdef', (YLeaf(YType.uint32, 'docsSubmgt3BaseMtaFilterUpDef'), ['int'])),
                ('docssubmgt3basestbfilterdowndef', (YLeaf(YType.uint32, 'docsSubmgt3BaseStbFilterDownDef'), ['int'])),
                ('docssubmgt3basestbfilterupdef', (YLeaf(YType.uint32, 'docsSubmgt3BaseStbFilterUpDef'), ['int'])),
            ])
            self.docssubmgt3basecpemaxipv4def = None
            self.docssubmgt3basecpemaxipv6prefixdef = None
            self.docssubmgt3basecpeactivedef = None
            self.docssubmgt3basecpelearnabledef = None
            self.docssubmgt3basesubfilterdowndef = None
            self.docssubmgt3basesubfilterupdef = None
            self.docssubmgt3basecmfilterdowndef = None
            self.docssubmgt3basecmfilterupdef = None
            self.docssubmgt3basepsfilterdowndef = None
            self.docssubmgt3basepsfilterupdef = None
            self.docssubmgt3basemtafilterdowndef = None
            self.docssubmgt3basemtafilterupdef = None
            self.docssubmgt3basestbfilterdowndef = None
            self.docssubmgt3basestbfilterupdef = None
            self._segment_path = lambda: "docsSubmgt3Base"
            self._absolute_path = lambda: "DOCS-SUBMGT3-MIB:DOCS-SUBMGT3-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(DOCSSUBMGT3MIB.DocsSubmgt3Base, ['docssubmgt3basecpemaxipv4def', 'docssubmgt3basecpemaxipv6prefixdef', 'docssubmgt3basecpeactivedef', 'docssubmgt3basecpelearnabledef', 'docssubmgt3basesubfilterdowndef', 'docssubmgt3basesubfilterupdef', 'docssubmgt3basecmfilterdowndef', 'docssubmgt3basecmfilterupdef', 'docssubmgt3basepsfilterdowndef', 'docssubmgt3basepsfilterupdef', 'docssubmgt3basemtafilterdowndef', 'docssubmgt3basemtafilterupdef', 'docssubmgt3basestbfilterdowndef', 'docssubmgt3basestbfilterupdef'], name, value)


    class DocsSubmgt3CpeCtrlTable(Entity):
        """
        This object maintains per\-CM traffic policies enforced 
        by the CMTS. The CMTS acquires the CM traffic policies 
        through the CM registration process, or in the 
        absence of some or all of those parameters, from the 
        Base object. The CM information and controls are meaningful 
        and used by the CMTS, but only after the CM is 
        operational.
        
        .. attribute:: docssubmgt3cpectrlentry
        
        	The conceptual row of docsSubmgt3CpeCtrlTable.  The CMTS does not persist the instances of the CpeCtrl  object across reinitializations
        	**type**\: list of  		 :py:class:`DocsSubmgt3CpeCtrlEntry <ydk.models.cisco_ios_xe.DOCS_SUBMGT3_MIB.DOCSSUBMGT3MIB.DocsSubmgt3CpeCtrlTable.DocsSubmgt3CpeCtrlEntry>`
        
        

        """

        _prefix = 'DOCS-SUBMGT3-MIB'
        _revision = '2007-05-18'

        def __init__(self):
            super(DOCSSUBMGT3MIB.DocsSubmgt3CpeCtrlTable, self).__init__()

            self.yang_name = "docsSubmgt3CpeCtrlTable"
            self.yang_parent_name = "DOCS-SUBMGT3-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("docsSubmgt3CpeCtrlEntry", ("docssubmgt3cpectrlentry", DOCSSUBMGT3MIB.DocsSubmgt3CpeCtrlTable.DocsSubmgt3CpeCtrlEntry))])
            self._leafs = OrderedDict()

            self.docssubmgt3cpectrlentry = YList(self)
            self._segment_path = lambda: "docsSubmgt3CpeCtrlTable"
            self._absolute_path = lambda: "DOCS-SUBMGT3-MIB:DOCS-SUBMGT3-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(DOCSSUBMGT3MIB.DocsSubmgt3CpeCtrlTable, [], name, value)


        class DocsSubmgt3CpeCtrlEntry(Entity):
            """
            The conceptual row of docsSubmgt3CpeCtrlTable. 
            The CMTS does not persist the instances of the CpeCtrl 
            object across reinitializations.
            
            .. attribute:: docsif3cmtscmregstatusid  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..4294967295
            
            	**refers to**\:  :py:class:`docsif3cmtscmregstatusid <ydk.models.cisco_ios_xe.DOCS_IF3_MIB.DOCSIF3MIB.DocsIf3CmtsCmRegStatusTable.DocsIf3CmtsCmRegStatusEntry>`
            
            .. attribute:: docssubmgt3cpectrlmaxcpeipv4
            
            	This attribute represents the number of simultaneous  IP v4 addresses permitted for CPE connected to the CM.  When the MaxCpeIpv4 attribute is set to zero (0), all Ipv4 CPE  traffic from the CM is dropped. The CMTS configures this  attribute with whichever of the 'Subscriber Management CPE IPv4  List' or 'Subscriber Management Control\-Max\_CpeIPv4' signaled  encodings is greater, or in the absence of all of those  provisioning parameters, with the CpeMaxIp v4Def  from the Base object. This limit applies to learned  and DOCSIS\-provisioned entries but not to entries added  through some administrative process at the CMTS.  Note that this attribute is only meaningful when the  Active attribute of the CM is set to 'true'
            	**type**\: int
            
            	**range:** 0..1023
            
            .. attribute:: docssubmgt3cpectrlmaxcpeipv6prefix
            
            	This attribute represents the number of simultaneous  IPv6 prefixes permitted for CPE connected to the  CM.   When the MaxCpeIpv6Prefix is set to zero (0), all IPv6 CPE   traffic from the CM is dropped. The CMTS configures this   attribute with whichever of the 'Subscriber Management CPE IPv6 List'   or'Subscriber Management Control Max Cpe IPv6 Prefix'   signaled encodings is greater, or in the absence of all of those  provisioning parameters, with the CpeMaxIpv6PrefixDef  from the Base object. This limit applies to learned  and DOCSIS\-provisioned entries but not to entries added  through some administrative process at the CMTS.  Note that this attribute is only meaningful when the  Active attribute of the CM is set to 'true'
            	**type**\: int
            
            	**range:** 0..1023
            
            .. attribute:: docssubmgt3cpectrlactive
            
            	This attribute controls the application of subscriber  management to this CM. If this is set to 'true',  CMTS\-based CPE control is active, and all the actions  required by the various filter policies and controls  apply at the CMTS. If this is set to false, no subscriber  management filtering is done at the CMTS (but other  filters may apply). If not set through DOCSIS provisioning,  this object defaults to the value of the Active  attribute of the Base object
            	**type**\: bool
            
            .. attribute:: docssubmgt3cpectrllearnable
            
            	This attribute controls whether the CMTS may learn  (and pass traffic for) CPE IP addresses associated  with a CM. If this is set to 'true', the CMTS may learn up  to the CM MaxCpeIp value less any DOCSIS\-provisioned  entries related to this CM. The nature of the learning  mechanism is not specified here. If not set through  DOCSIS provisioning, this object defaults to the  value of the CpeLearnableDef attribute from the Base  object. Note that this attribute is only meaningful  if docsSubMgtCpeControlActive is 'true' to enforce  a limit in the number of CPEs learned. CPE learning  is always performed for the CMTS for security reasons
            	**type**\: bool
            
            .. attribute:: docssubmgt3cpectrlreset
            
            	If set to 'true', this attribute commands the CMTS  to delete the instances denoted as 'learned' addresses  in the CpeIp object. This attribute always returns  false on read
            	**type**\: bool
            
            .. attribute:: docssubmgt3cpectrllastreset
            
            	This attribute represents the system Up Time of the  last set to 'true' of the Reset attribute of this instance.  Zero if never reset
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'DOCS-SUBMGT3-MIB'
            _revision = '2007-05-18'

            def __init__(self):
                super(DOCSSUBMGT3MIB.DocsSubmgt3CpeCtrlTable.DocsSubmgt3CpeCtrlEntry, self).__init__()

                self.yang_name = "docsSubmgt3CpeCtrlEntry"
                self.yang_parent_name = "docsSubmgt3CpeCtrlTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['docsif3cmtscmregstatusid']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('docsif3cmtscmregstatusid', (YLeaf(YType.str, 'docsIf3CmtsCmRegStatusId'), ['int'])),
                    ('docssubmgt3cpectrlmaxcpeipv4', (YLeaf(YType.uint32, 'docsSubmgt3CpeCtrlMaxCpeIpv4'), ['int'])),
                    ('docssubmgt3cpectrlmaxcpeipv6prefix', (YLeaf(YType.uint32, 'docsSubmgt3CpeCtrlMaxCpeIpv6Prefix'), ['int'])),
                    ('docssubmgt3cpectrlactive', (YLeaf(YType.boolean, 'docsSubmgt3CpeCtrlActive'), ['bool'])),
                    ('docssubmgt3cpectrllearnable', (YLeaf(YType.boolean, 'docsSubmgt3CpeCtrlLearnable'), ['bool'])),
                    ('docssubmgt3cpectrlreset', (YLeaf(YType.boolean, 'docsSubmgt3CpeCtrlReset'), ['bool'])),
                    ('docssubmgt3cpectrllastreset', (YLeaf(YType.uint32, 'docsSubmgt3CpeCtrlLastReset'), ['int'])),
                ])
                self.docsif3cmtscmregstatusid = None
                self.docssubmgt3cpectrlmaxcpeipv4 = None
                self.docssubmgt3cpectrlmaxcpeipv6prefix = None
                self.docssubmgt3cpectrlactive = None
                self.docssubmgt3cpectrllearnable = None
                self.docssubmgt3cpectrlreset = None
                self.docssubmgt3cpectrllastreset = None
                self._segment_path = lambda: "docsSubmgt3CpeCtrlEntry" + "[docsIf3CmtsCmRegStatusId='" + str(self.docsif3cmtscmregstatusid) + "']"
                self._absolute_path = lambda: "DOCS-SUBMGT3-MIB:DOCS-SUBMGT3-MIB/docsSubmgt3CpeCtrlTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(DOCSSUBMGT3MIB.DocsSubmgt3CpeCtrlTable.DocsSubmgt3CpeCtrlEntry, ['docsif3cmtscmregstatusid', 'docssubmgt3cpectrlmaxcpeipv4', 'docssubmgt3cpectrlmaxcpeipv6prefix', 'docssubmgt3cpectrlactive', 'docssubmgt3cpectrllearnable', 'docssubmgt3cpectrlreset', 'docssubmgt3cpectrllastreset'], name, value)


    class DocsSubmgt3CpeIpTable(Entity):
        """
        This object defines the list of IP Addresses behind 
        the CM known by the CMTS. 
        
        If the Active attribute of the CpeCtrl object associated 
        with a CM is set to 'true' and the CMTS receives an 
        IP packet from a CM that contains a source IP address that 
        does not match one of the CPE IP addresses associated 
        with this CM, one of two things occurs. If the number 
        of CPE IPs is less than the MaxCpeIp of the CpeCtrl object 
        for that CM, the source IP address is added to this 
        object and the packet is forwarded; otherwise, the 
        packet is dropped.
        
        .. attribute:: docssubmgt3cpeipentry
        
        	The conceptual row of docsSubmgt3CpeIpTable
        	**type**\: list of  		 :py:class:`DocsSubmgt3CpeIpEntry <ydk.models.cisco_ios_xe.DOCS_SUBMGT3_MIB.DOCSSUBMGT3MIB.DocsSubmgt3CpeIpTable.DocsSubmgt3CpeIpEntry>`
        
        

        """

        _prefix = 'DOCS-SUBMGT3-MIB'
        _revision = '2007-05-18'

        def __init__(self):
            super(DOCSSUBMGT3MIB.DocsSubmgt3CpeIpTable, self).__init__()

            self.yang_name = "docsSubmgt3CpeIpTable"
            self.yang_parent_name = "DOCS-SUBMGT3-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("docsSubmgt3CpeIpEntry", ("docssubmgt3cpeipentry", DOCSSUBMGT3MIB.DocsSubmgt3CpeIpTable.DocsSubmgt3CpeIpEntry))])
            self._leafs = OrderedDict()

            self.docssubmgt3cpeipentry = YList(self)
            self._segment_path = lambda: "docsSubmgt3CpeIpTable"
            self._absolute_path = lambda: "DOCS-SUBMGT3-MIB:DOCS-SUBMGT3-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(DOCSSUBMGT3MIB.DocsSubmgt3CpeIpTable, [], name, value)


        class DocsSubmgt3CpeIpEntry(Entity):
            """
            The conceptual row of docsSubmgt3CpeIpTable.
            
            .. attribute:: docsif3cmtscmregstatusid  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..4294967295
            
            	**refers to**\:  :py:class:`docsif3cmtscmregstatusid <ydk.models.cisco_ios_xe.DOCS_IF3_MIB.DOCSIF3MIB.DocsIf3CmtsCmRegStatusTable.DocsIf3CmtsCmRegStatusEntry>`
            
            .. attribute:: docssubmgt3cpeipid  (key)
            
            	This attribute represents a unique identifier for  a CPE IP of the CM. An instance of this attribute exists  for each CPE provisioned in the 'Subscriber Management  CPE IPv4 Table' or 'Subscriber Management CPE  IPv6 Table' encodings. An entry is created either through  the included CPE IP addresses in the provisioning  object, or CPEs learned from traffic sourced from the  CM
            	**type**\: int
            
            	**range:** 1..1023
            
            .. attribute:: docssubmgt3cpeipaddrtype
            
            	The type of Internet address of the Addr attribute
            	**type**\:  :py:class:`InetAddressType <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetAddressType>`
            
            .. attribute:: docssubmgt3cpeipaddr
            
            	This attribute represents the IP address either set  from provisioning or learned via address gleaning  or other forwarding means
            	**type**\: str
            
            	**length:** 0..255
            
            .. attribute:: docssubmgt3cpeipaddrprefixlen
            
            	This attribute represents the prefix length associated with  the IP subnet prefix either set from provisioning or learned  via address gleaning or other forwarding means. For IPv4 CPE  addresses this attribute generally reports the value 32   (32 bits) to indicate a unicast IPv4 address. For IPv6, this  attribute represents either an IPv6 unicast address  (128 bits, equal to /128 prefix length) or a subnet prefix   length (for example 56 bits, equal to /56 prefix length)
            	**type**\: int
            
            	**range:** 0..2040
            
            .. attribute:: docssubmgt3cpeiplearned
            
            	This attribute is set to 'true' when the IP address  was learned from IP packets sent upstream rather than  via the CM provisioning process
            	**type**\: bool
            
            .. attribute:: docssubmgt3cpeiptype
            
            	This attribute represents the type of CPE based on  the following classification below\:               'cpe' Regular CPE clients.               'ps'  CableHome Portal Server (PS)               'mta' PacketCable Multimedia Terminal Adapter (MTA)               'stb' Digital Set\-top Box (STB).               'tea' T1 Emulation adapter (TEA)               'erouter' Embedded Router (eRouter)
            	**type**\:  :py:class:`DocsSubmgt3CpeIpType <ydk.models.cisco_ios_xe.DOCS_SUBMGT3_MIB.DOCSSUBMGT3MIB.DocsSubmgt3CpeIpTable.DocsSubmgt3CpeIpEntry.DocsSubmgt3CpeIpType>`
            
            

            """

            _prefix = 'DOCS-SUBMGT3-MIB'
            _revision = '2007-05-18'

            def __init__(self):
                super(DOCSSUBMGT3MIB.DocsSubmgt3CpeIpTable.DocsSubmgt3CpeIpEntry, self).__init__()

                self.yang_name = "docsSubmgt3CpeIpEntry"
                self.yang_parent_name = "docsSubmgt3CpeIpTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['docsif3cmtscmregstatusid','docssubmgt3cpeipid']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('docsif3cmtscmregstatusid', (YLeaf(YType.str, 'docsIf3CmtsCmRegStatusId'), ['int'])),
                    ('docssubmgt3cpeipid', (YLeaf(YType.uint32, 'docsSubmgt3CpeIpId'), ['int'])),
                    ('docssubmgt3cpeipaddrtype', (YLeaf(YType.enumeration, 'docsSubmgt3CpeIpAddrType'), [('ydk.models.cisco_ios_xe.INET_ADDRESS_MIB', 'InetAddressType', '')])),
                    ('docssubmgt3cpeipaddr', (YLeaf(YType.str, 'docsSubmgt3CpeIpAddr'), ['str'])),
                    ('docssubmgt3cpeipaddrprefixlen', (YLeaf(YType.uint32, 'docsSubmgt3CpeIpAddrPrefixLen'), ['int'])),
                    ('docssubmgt3cpeiplearned', (YLeaf(YType.boolean, 'docsSubmgt3CpeIpLearned'), ['bool'])),
                    ('docssubmgt3cpeiptype', (YLeaf(YType.enumeration, 'docsSubmgt3CpeIpType'), [('ydk.models.cisco_ios_xe.DOCS_SUBMGT3_MIB', 'DOCSSUBMGT3MIB', 'DocsSubmgt3CpeIpTable.DocsSubmgt3CpeIpEntry.DocsSubmgt3CpeIpType')])),
                ])
                self.docsif3cmtscmregstatusid = None
                self.docssubmgt3cpeipid = None
                self.docssubmgt3cpeipaddrtype = None
                self.docssubmgt3cpeipaddr = None
                self.docssubmgt3cpeipaddrprefixlen = None
                self.docssubmgt3cpeiplearned = None
                self.docssubmgt3cpeiptype = None
                self._segment_path = lambda: "docsSubmgt3CpeIpEntry" + "[docsIf3CmtsCmRegStatusId='" + str(self.docsif3cmtscmregstatusid) + "']" + "[docsSubmgt3CpeIpId='" + str(self.docssubmgt3cpeipid) + "']"
                self._absolute_path = lambda: "DOCS-SUBMGT3-MIB:DOCS-SUBMGT3-MIB/docsSubmgt3CpeIpTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(DOCSSUBMGT3MIB.DocsSubmgt3CpeIpTable.DocsSubmgt3CpeIpEntry, ['docsif3cmtscmregstatusid', 'docssubmgt3cpeipid', 'docssubmgt3cpeipaddrtype', 'docssubmgt3cpeipaddr', 'docssubmgt3cpeipaddrprefixlen', 'docssubmgt3cpeiplearned', 'docssubmgt3cpeiptype'], name, value)

            class DocsSubmgt3CpeIpType(Enum):
                """
                DocsSubmgt3CpeIpType (Enum Class)

                This attribute represents the type of CPE based on 

                the following classification below\: 

                             'cpe' Regular CPE clients. 

                             'ps'  CableHome Portal Server (PS) 

                             'mta' PacketCable Multimedia Terminal Adapter (MTA) 

                             'stb' Digital Set\-top Box (STB). 

                             'tea' T1 Emulation adapter (TEA) 

                             'erouter' Embedded Router (eRouter)

                .. data:: cpe = 1

                .. data:: ps = 2

                .. data:: mta = 3

                .. data:: stb = 4

                .. data:: tea = 5

                .. data:: erouter = 6

                """

                cpe = Enum.YLeaf(1, "cpe")

                ps = Enum.YLeaf(2, "ps")

                mta = Enum.YLeaf(3, "mta")

                stb = Enum.YLeaf(4, "stb")

                tea = Enum.YLeaf(5, "tea")

                erouter = Enum.YLeaf(6, "erouter")



    class DocsSubmgt3GrpTable(Entity):
        """
        This object defines the set of downstream and upstream 
        filter groups that the CMTS applies to traffic associated 
        with that CM.
        
        .. attribute:: docssubmgt3grpentry
        
        	The conceptual row of docsSubmgt3GrpTable.  The CMTS does not persist the instances of the Grp  object across reinitializations
        	**type**\: list of  		 :py:class:`DocsSubmgt3GrpEntry <ydk.models.cisco_ios_xe.DOCS_SUBMGT3_MIB.DOCSSUBMGT3MIB.DocsSubmgt3GrpTable.DocsSubmgt3GrpEntry>`
        
        

        """

        _prefix = 'DOCS-SUBMGT3-MIB'
        _revision = '2007-05-18'

        def __init__(self):
            super(DOCSSUBMGT3MIB.DocsSubmgt3GrpTable, self).__init__()

            self.yang_name = "docsSubmgt3GrpTable"
            self.yang_parent_name = "DOCS-SUBMGT3-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("docsSubmgt3GrpEntry", ("docssubmgt3grpentry", DOCSSUBMGT3MIB.DocsSubmgt3GrpTable.DocsSubmgt3GrpEntry))])
            self._leafs = OrderedDict()

            self.docssubmgt3grpentry = YList(self)
            self._segment_path = lambda: "docsSubmgt3GrpTable"
            self._absolute_path = lambda: "DOCS-SUBMGT3-MIB:DOCS-SUBMGT3-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(DOCSSUBMGT3MIB.DocsSubmgt3GrpTable, [], name, value)


        class DocsSubmgt3GrpEntry(Entity):
            """
            The conceptual row of docsSubmgt3GrpTable. 
            The CMTS does not persist the instances of the Grp 
            object across reinitializations.
            
            .. attribute:: docsif3cmtscmregstatusid  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..4294967295
            
            	**refers to**\:  :py:class:`docsif3cmtscmregstatusid <ydk.models.cisco_ios_xe.DOCS_IF3_MIB.DOCSIF3MIB.DocsIf3CmtsCmRegStatusTable.DocsIf3CmtsCmRegStatusEntry>`
            
            .. attribute:: docssubmgt3grpudcgroupids
            
            	This attribute represents the filter group(s) associated  with the CM signaled 'Upstream Drop Classifier Group ID'   encodings during the registration process. UDC Group IDs are  integer values and this attribute reports them as decimal   numbers that are space\-separated. The zero\-length string indicates   that the CM didn't signal UDC Group IDs.   This attribute provides two functions\:   \- Communicate the CM the configured UDC Group ID(s), irrespective   of the CM being provisioned to filter upstream traffic based   on IP Filters or UDCs.   \- Optionally, and with regards to the CMTS, if the value of the  attribute UdcSentInReqRsp is 'true', indicates that the filtering   rules associated with the Subscriber Management Group ID(s) will  be sent during registration to the CM. It is vendor specific   whether the CMTS updates individual CM UDCs after registration  when rules are changed in the Grp object
            	**type**\: str
            
            .. attribute:: docssubmgt3grpudcsentinregrsp
            
            	This attribute represents the CMTS upstream filtering   status for this CM. The value 'true' indicates that the   CMTS has sent UDCs to the CM during registration process.     In order for a CMTS to send UDCs to a CM, the CMTS MAC Domain  needed to be enabled via the MAC Domain attribute   SendUdcRulesEnabled and the CM had indicated the UDC capability   support during the registration process. The value 'false'   indicates that the CMTS was not enabled to sent UDCs to the   CMs in the MAC Domain, or the CM does not advertised UDC   support in its capabilities encodings, or both. Since the   CMTS capability to sent UDCs to CMs during the registration  process is optional, the CMTS is not required to implement   the value 'true'
            	**type**\: bool
            
            .. attribute:: docssubmgt3grpsubfilterds
            
            	This attribute represents the filter group applied  to traffic destined for subscriber's CPE attached to the  referenced CM (attached to CM CPE interfaces). This  value corresponds to the 'Subscriber Downstream  Group' value of the 'Subscriber Management Filter Groups'  encoding signaled during the CM registration  or in its absence, to the SubFilterDownDef attribute  of the Base object. The value zero or a filter group  ID not configured in the CMTS means no filtering is applied  to traffic destined to hosts attached to this CM
            	**type**\: int
            
            	**range:** 0..1024
            
            .. attribute:: docssubmgt3grpsubfilterus
            
            	This attribute represents the filter group applied  to traffic originating from subscriber's CPE attached  to the referenced CM (attached to CM CPE interfaces).  This value corresponds to the 'Subscriber Upstream  Group' value of the 'Subscriber Management Filter  Groups' encoding signaled during the CM registration  or in its absence, to the SubFilterUpDef attribute  of the Base object. The value zero or a filter group  ID not configured in the CMTS means no filtering  is applied to traffic originating from hosts attached  to this CM
            	**type**\: int
            
            	**range:** 0..1024
            
            .. attribute:: docssubmgt3grpcmfilterds
            
            	This attribute represents the filter group applied  to traffic destined for the CM itself. This value corresponds  to the 'CM Downstream Group' value of the  'Subscriber Management Filter Groups' encoding signaled  during the CM registration or in its absence,  to the CmFilterDownDef attribute of the Base object.  The value zero or a filter group ID not configured in  the CMTS means no filtering is applied to traffic destined  to the CM
            	**type**\: int
            
            	**range:** 0..1024
            
            .. attribute:: docssubmgt3grpcmfilterus
            
            	This attribute represents the filter group applied  to traffic originating from the CM itself. This value  corresponds to the 'Subscriber Upstream Group'  value of the 'Subscriber Management Filter Groups'  encoding signaled during the CM registration or in its  absence, to the SubFilterUpDef attribute of the Base  object. The value zero or a filter group ID not configured  in the CMTS means no filtering is applied to traffic  originating from this CM
            	**type**\: int
            
            	**range:** 0..1024
            
            .. attribute:: docssubmgt3grppsfilterds
            
            	This attribute represents the filter group applied  to traffic destined to the Embedded CableHome Portal  Services Element or the Embedded Router on the referenced  CM. This value corresponds to the 'PS Downstream  Group' value of the 'Subscriber Management Filter  Groups' encoding signaled during the CM registration  or in its absence, to the SubFilterDownDef attribute  of the Base object. The value zero or a filter  group ID not configured in the CMTS means no filtering  is applied to traffic destined to the Embedded CableHome  Portal Services Element or Embedded Router on  this CM
            	**type**\: int
            
            	**range:** 0..1024
            
            .. attribute:: docssubmgt3grppsfilterus
            
            	This attribute represents the filter group applied  to traffic originating from the Embedded CableHome  Portal Services Element or Embedded Router on the  referenced CM. This value corresponds to the 'PS Upstream  Group' value of the 'Subscriber Management Filter  Groups' encoding signaled during the CM registration  or in its absence, to the SubFilterUpDef attribute  of the Base object. The value zero or a filter group  ID not configured in the CMTS means no filtering is  applied to traffic originating from the Embedded CableHome  Portal Services Element or Embedded Router  on this CM
            	**type**\: int
            
            	**range:** 0..1024
            
            .. attribute:: docssubmgt3grpmtafilterds
            
            	This attribute represents the filter group applied  to traffic destined to the Embedded Multimedia Terminal  Adapter on the referenced CM. This value corresponds  to the 'MTA Downstream Group' value of the 'Subscriber  Management Filter Groups' encoding signaled  during the CM registration or in its absence, to  the SubFilterDownDef attribute of the Base object.  The value zero or a filter group ID not configured in the  CMTS means no filtering is applied to traffic destined  to the Embedded Multimedia Terminal Adapter on  this CM
            	**type**\: int
            
            	**range:** 0..1024
            
            .. attribute:: docssubmgt3grpmtafilterus
            
            	This attribute represents the filter group applied  to traffic originating from the Embedded Multimedia  Terminal Adapter on the referenced CM. This value  corresponds to the 'MTA Upstream Group' value of the  'Subscriber Management Filter Groups' encoding signaled  during the CM registration or in its absence,  to the SubFilterUpDef attribute of the Base object.  The value zero or a filter group ID not configured in  the CMTS means no filtering is applied to traffic originating  from the Embedded Multimedia Terminal Adapter  on this CM
            	**type**\: int
            
            	**range:** 0..1024
            
            .. attribute:: docssubmgt3grpstbfilterds
            
            	This attribute represents the filter group applied  to traffic destined for the Embedded Set\-Top Box on  the referenced CM. This value corresponds to the 'STB  Downstream Group' value of the 'Subscriber Management  Filter Groups' encoding signaled during the CM  registration or in its absence, to the SubFilterDownDef  attribute of the Base object. The value zero or  a filter group ID not configured in the CMTS means no filtering  is applied to traffic destined to the Embedded  Set\-Top Box on this CM
            	**type**\: int
            
            	**range:** 0..1024
            
            .. attribute:: docssubmgt3grpstbfilterus
            
            	This attribute represents the filter group applied  to traffic originating from the Embedded Set\-Top  Box on the referenced CM. This value corresponds to the  'STB Upstream Group' value of the 'Subscriber Management  Filter Groups' encoding signaled during the  CM registration or in its absence, to the SubFilterUpDef  attribute of the Base object. The value zero or  a filter group ID not configured in the CMTS means no filtering  is applied to traffic originating from the  Embedded Set\-Top Box on this CM
            	**type**\: int
            
            	**range:** 0..1024
            
            

            """

            _prefix = 'DOCS-SUBMGT3-MIB'
            _revision = '2007-05-18'

            def __init__(self):
                super(DOCSSUBMGT3MIB.DocsSubmgt3GrpTable.DocsSubmgt3GrpEntry, self).__init__()

                self.yang_name = "docsSubmgt3GrpEntry"
                self.yang_parent_name = "docsSubmgt3GrpTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['docsif3cmtscmregstatusid']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('docsif3cmtscmregstatusid', (YLeaf(YType.str, 'docsIf3CmtsCmRegStatusId'), ['int'])),
                    ('docssubmgt3grpudcgroupids', (YLeaf(YType.str, 'docsSubMgt3GrpUdcGroupIds'), ['str'])),
                    ('docssubmgt3grpudcsentinregrsp', (YLeaf(YType.boolean, 'docsSubMgt3GrpUdcSentInRegRsp'), ['bool'])),
                    ('docssubmgt3grpsubfilterds', (YLeaf(YType.uint32, 'docsSubmgt3GrpSubFilterDs'), ['int'])),
                    ('docssubmgt3grpsubfilterus', (YLeaf(YType.uint32, 'docsSubmgt3GrpSubFilterUs'), ['int'])),
                    ('docssubmgt3grpcmfilterds', (YLeaf(YType.uint32, 'docsSubmgt3GrpCmFilterDs'), ['int'])),
                    ('docssubmgt3grpcmfilterus', (YLeaf(YType.uint32, 'docsSubmgt3GrpCmFilterUs'), ['int'])),
                    ('docssubmgt3grppsfilterds', (YLeaf(YType.uint32, 'docsSubmgt3GrpPsFilterDs'), ['int'])),
                    ('docssubmgt3grppsfilterus', (YLeaf(YType.uint32, 'docsSubmgt3GrpPsFilterUs'), ['int'])),
                    ('docssubmgt3grpmtafilterds', (YLeaf(YType.uint32, 'docsSubmgt3GrpMtaFilterDs'), ['int'])),
                    ('docssubmgt3grpmtafilterus', (YLeaf(YType.uint32, 'docsSubmgt3GrpMtaFilterUs'), ['int'])),
                    ('docssubmgt3grpstbfilterds', (YLeaf(YType.uint32, 'docsSubmgt3GrpStbFilterDs'), ['int'])),
                    ('docssubmgt3grpstbfilterus', (YLeaf(YType.uint32, 'docsSubmgt3GrpStbFilterUs'), ['int'])),
                ])
                self.docsif3cmtscmregstatusid = None
                self.docssubmgt3grpudcgroupids = None
                self.docssubmgt3grpudcsentinregrsp = None
                self.docssubmgt3grpsubfilterds = None
                self.docssubmgt3grpsubfilterus = None
                self.docssubmgt3grpcmfilterds = None
                self.docssubmgt3grpcmfilterus = None
                self.docssubmgt3grppsfilterds = None
                self.docssubmgt3grppsfilterus = None
                self.docssubmgt3grpmtafilterds = None
                self.docssubmgt3grpmtafilterus = None
                self.docssubmgt3grpstbfilterds = None
                self.docssubmgt3grpstbfilterus = None
                self._segment_path = lambda: "docsSubmgt3GrpEntry" + "[docsIf3CmtsCmRegStatusId='" + str(self.docsif3cmtscmregstatusid) + "']"
                self._absolute_path = lambda: "DOCS-SUBMGT3-MIB:DOCS-SUBMGT3-MIB/docsSubmgt3GrpTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(DOCSSUBMGT3MIB.DocsSubmgt3GrpTable.DocsSubmgt3GrpEntry, ['docsif3cmtscmregstatusid', 'docssubmgt3grpudcgroupids', 'docssubmgt3grpudcsentinregrsp', 'docssubmgt3grpsubfilterds', 'docssubmgt3grpsubfilterus', 'docssubmgt3grpcmfilterds', 'docssubmgt3grpcmfilterus', 'docssubmgt3grppsfilterds', 'docssubmgt3grppsfilterus', 'docssubmgt3grpmtafilterds', 'docssubmgt3grpmtafilterus', 'docssubmgt3grpstbfilterds', 'docssubmgt3grpstbfilterus'], name, value)


    class DocsSubmgt3FilterGrpTable(Entity):
        """
        This object describes a set of filter or classifier 
        criteria. Classifiers are assigned by group to the 
        individual CMs. That assignment is made via the 'Subscriber 
        Management TLVs' encodings sent upstream from 
        the CM to the CMTS during registration or in their 
        absence, default values configured in the CMTS. 
        A Filter Group ID (GrpId) is a set of rules that correspond 
        to the expansion of a UDC Group ID into UDC individual  
        classification rules.  The Filter Group Ids are generated  
        whenever the CMTS is configured to send UDCs during the CM  
        registration process. Implementation of L2 classification  
        criteria is optional for the CMTS; LLC/MAC upstream and  
        downstream filter criteria can be ignored during the packet 
        matching process.
        
        .. attribute:: docssubmgt3filtergrpentry
        
        	The conceptual row of docsSubmgt3FilterGrpTable.  The CMTS persists all instances of the FilterGrp object  across reinitializations
        	**type**\: list of  		 :py:class:`DocsSubmgt3FilterGrpEntry <ydk.models.cisco_ios_xe.DOCS_SUBMGT3_MIB.DOCSSUBMGT3MIB.DocsSubmgt3FilterGrpTable.DocsSubmgt3FilterGrpEntry>`
        
        

        """

        _prefix = 'DOCS-SUBMGT3-MIB'
        _revision = '2007-05-18'

        def __init__(self):
            super(DOCSSUBMGT3MIB.DocsSubmgt3FilterGrpTable, self).__init__()

            self.yang_name = "docsSubmgt3FilterGrpTable"
            self.yang_parent_name = "DOCS-SUBMGT3-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("docsSubmgt3FilterGrpEntry", ("docssubmgt3filtergrpentry", DOCSSUBMGT3MIB.DocsSubmgt3FilterGrpTable.DocsSubmgt3FilterGrpEntry))])
            self._leafs = OrderedDict()

            self.docssubmgt3filtergrpentry = YList(self)
            self._segment_path = lambda: "docsSubmgt3FilterGrpTable"
            self._absolute_path = lambda: "DOCS-SUBMGT3-MIB:DOCS-SUBMGT3-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(DOCSSUBMGT3MIB.DocsSubmgt3FilterGrpTable, [], name, value)


        class DocsSubmgt3FilterGrpEntry(Entity):
            """
            The conceptual row of docsSubmgt3FilterGrpTable. 
            The CMTS persists all instances of the FilterGrp object 
            across reinitializations.
            
            .. attribute:: docssubmgt3filtergrpgrpid  (key)
            
            	This key is an identifier for a set of classifiers known  as a filter group. Each CM may be associated with  several filter groups for its upstream and downstream  traffic, one group per target end point on the CM as  defined in the Grp object. Typically, many CMs share  a common set of filter groups
            	**type**\: int
            
            	**range:** 1..65535
            
            .. attribute:: docssubmgt3filtergrpruleid  (key)
            
            	This key represents an ordered classifier identifier  within the group.  Filters are applied in order if  the Priority attribute is not supported
            	**type**\: int
            
            	**range:** 1..65535
            
            .. attribute:: docssubmgt3filtergrpaction
            
            	This attribute represents the action to take upon  this filter matching.  'permit' means to stop the classification  matching and accept the packet for further  processing.  'deny' means to drop the packet
            	**type**\:  :py:class:`DocsSubmgt3FilterGrpAction <ydk.models.cisco_ios_xe.DOCS_SUBMGT3_MIB.DOCSSUBMGT3MIB.DocsSubmgt3FilterGrpTable.DocsSubmgt3FilterGrpEntry.DocsSubmgt3FilterGrpAction>`
            
            .. attribute:: docssubmgt3filtergrppriority
            
            	This attribute defines the order in which classifiers  are compared against packets. The higher the value,  the higher the priority
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: docssubmgt3filtergrpiptoslow
            
            	This attribute represents the low value of a range  of ToS (Type of Service) octet values. This object is  defined as an 8\-bit octet as per the DOCSIS Specification  for packet classification.  The IP ToS octet, as originally defined in RFC 791, has  been superseded by the 6\-bit Differentiated Services  Field (DSField, RFC 3260) and the 2\-bit Explicit  Congestion Notification Field (ECN field, RFC 3168)
            	**type**\: str
            
            	**length:** 1
            
            .. attribute:: docssubmgt3filtergrpiptoshigh
            
            	This attribute represents the high value of a range  of ToS octet values. This object is defined as an 8\-bit  octet as per the DOCSIS Specification for packet classification.  The IP ToS octet, as originally defined in RFC 791, has  been superseded by the 6\-bit Differentiated Services  Field (DSField, RFC 3260) and the 2\-bit Explicit  Congestion Notification Field (ECN field, RFC 3168)
            	**type**\: str
            
            	**length:** 1
            
            .. attribute:: docssubmgt3filtergrpiptosmask
            
            	This attribute represents the mask value that is bitwise  ANDed with ToS octet in an IP packet, and the resulting value  is used for range checking of IpTosLow and IpTosHigh
            	**type**\: str
            
            	**length:** 1
            
            .. attribute:: docssubmgt3filtergrpipprotocol
            
            	This attribute represents the value of the IP Protocol  field required for IP packets to match this rule.  The value 256 matches traffic with any IP Protocol value.  The value 257 by convention matches both TCP and  UDP
            	**type**\: int
            
            	**range:** 0..257
            
            .. attribute:: docssubmgt3filtergrpinetaddrtype
            
            	The type of the Internet address for InetSrcAddr,  InetSrcMask, InetDestAddr, and InetDestMask
            	**type**\:  :py:class:`InetAddressType <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetAddressType>`
            
            .. attribute:: docssubmgt3filtergrpinetsrcaddr
            
            	This attribute specifies the value of the IP Source Address  required for packets to match this rule. An IP packet  matches the rule when the packet's IP Source Address  bitwise ANDed with the InetSrcMask value equals  the InetSrcAddr value. The address type of this object  is specified by the InetAddressType attribute
            	**type**\: str
            
            	**length:** 0..255
            
            .. attribute:: docssubmgt3filtergrpinetsrcmask
            
            	This attribute represents which bits of a packet's  IP Source Address are compared to match this rule. An  IP packet matches the rule when the packet's IP Source  Address bitwise ANDed with the InetSrcMask value equals  the InetSrcAddr value. The address type of this  object is specified by InetAddrType
            	**type**\: str
            
            	**length:** 0..255
            
            .. attribute:: docssubmgt3filtergrpinetdestaddr
            
            	This attribute specifies the value of the IP Destination  Address required for packets to match this rule.  An IP packet matches the rule when the packet's IP Destination  Address bitwise ANDed with the InetSrcMask  value equals the InetDestAddr value. The address type  of this object is specified by the InetAddrType attribute
            	**type**\: str
            
            	**length:** 0..255
            
            .. attribute:: docssubmgt3filtergrpinetdestmask
            
            	This attribute represents which bits of a packet's  IP Destination Address are compared to match this rule.  An IP packet matches the rule when the packet's IP Destination  Address bitwise ANDed with the InetDestMask value  equals the InetDestAddr value. The address type  of this object is specified by InetAddrType
            	**type**\: str
            
            	**length:** 0..255
            
            .. attribute:: docssubmgt3filtergrpsrcportstart
            
            	This attribute represents the low\-end inclusive  range of TCP/UDP source port numbers to which a packet  is compared. This attribute is irrelevant for non\-TCP/UDP  IP packets
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: docssubmgt3filtergrpsrcportend
            
            	This attribute represents the high\-end inclusive  range of TCP/UDP source port numbers to which a packet  is compared. This attribute is irrelevant for non\-TCP/UDP  IP packets
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: docssubmgt3filtergrpdestportstart
            
            	This attribute represents the low\-end inclusive  range of TCP/UDP destination port numbers to which a  packet is compared. This attribute is irrelevant for  non\-TCP/UDP IP packets
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: docssubmgt3filtergrpdestportend
            
            	This attribute represents the high\-end inclusive  range of TCP/UDP destination port numbers to which a packet  is compared. This attribute is irrelevant for non\-TCP/UDP  IP packets
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: docssubmgt3filtergrpdestmacaddr
            
            	This attribute represents the criteria to match against  an Ethernet packet MAC address bitwise ANDed  with DestMacMask
            	**type**\: str
            
            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
            
            .. attribute:: docssubmgt3filtergrpdestmacmask
            
            	An Ethernet packet matches an entry when its  destination MAC address bitwise ANDed with  the DestMacMask attribute equals the value of  the DestMacAddr attribute
            	**type**\: str
            
            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
            
            .. attribute:: docssubmgt3filtergrpsrcmacaddr
            
            	This attribute represents the value to match against  an Ethernet packet source MAC address
            	**type**\: str
            
            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
            
            .. attribute:: docssubmgt3filtergrpenetprotocoltype
            
            	This attribute indicates the format of the layer 3  protocol ID in the Ethernet packet. A value of 'none'  means that the rule does not use the layer 3 protocol  type as a matching criteria. A value of 'ethertype'  means that the rule applies only to frames that contain  an EtherType value. EtherType values are contained  in packets using the DEC\-Intel\-Xerox (DIX) encapsulation  or the RFC 1042 Sub\-Network Access Protocol  (SNAP) encapsulation formats. A value of 'dsap' means  that the rule applies only to frames using the IEEE802.3  encapsulation format with a Destination Service  Access Point (DSAP) other than 0xAA (which is reserved  for SNAP). A value of 'mac' means that the rule  applies only to MAC management messages for MAC management  messages. A value of 'all' means that the rule  matches all Ethernet packets. If the Ethernet frame  contains an 802.1P/Q Tag header (i.e., EtherType  0x8100), this attribute applies to the embedded EtherType  field within the 802.1p/Q header.  The value 'mac' is only used for passing UDCs to CMs during   Registration. The CMTS ignores filter rules that include   the value of this attribute set to 'mac' for CMTS enforced   upstream and downstream subscriber management filter group  rules
            	**type**\:  :py:class:`DocsSubmgt3FilterGrpEnetProtocolType <ydk.models.cisco_ios_xe.DOCS_SUBMGT3_MIB.DOCSSUBMGT3MIB.DocsSubmgt3FilterGrpTable.DocsSubmgt3FilterGrpEntry.DocsSubmgt3FilterGrpEnetProtocolType>`
            
            .. attribute:: docssubmgt3filtergrpenetprotocol
            
            	This attribute represents the Ethernet protocol  type to be matched against the packets. For EnetProtocolType  set to 'none', this attribute is ignored when considering  whether a packet matches the current rule.  If the attribute EnetProtocolType is 'ethertype',  this attribute gives the 16\-bit value of the EtherType  that the packet must match in order to match the rule.  If the attribute EnetProtocolType is 'dsap', the lower  8 bits of this attribute's value must match the DSAP  octet of the packet in order to match the rule. If the Ethernet  frame contains an 802.1p/Q Tag header (i.e.,  EtherType 0x8100), this attribute applies to the embedded  EtherType field within the 802.1p/Q header
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: docssubmgt3filtergrpuserprilow
            
            	This attribute applies only to Ethernet frames using  the 802.1p/Q tag header (indicated with EtherType  0x8100). Such frames include a 16\-bit Tag that contains  a 3\-bit Priority field and a 12\-bit VLAN number.  Tagged Ethernet packets must have a 3\-bit Priority  field within the range of PriLow to PriHigh in order to  match this rule
            	**type**\: int
            
            	**range:** 0..7
            
            .. attribute:: docssubmgt3filtergrpuserprihigh
            
            	This attribute applies only to Ethernet frames using  the 802.1p/Q tag header (indicated with EtherType  0x8100). Such frames include a 16\-bit Tag that contains  a 3\-bit Priority field and a 12\-bit VLAN number.  Tagged Ethernet packets must have a 3\-bit Priority  field within the range of PriLow to PriHigh in order to  match this rule
            	**type**\: int
            
            	**range:** 0..7
            
            .. attribute:: docssubmgt3filtergrpvlanid
            
            	This attribute applies only to Ethernet frames using  the 802.1p/Q tag header. Tagged packets must have  a VLAN Identifier that matches the value in order to  match the rule
            	**type**\: int
            
            	**range:** 0..4094
            
            .. attribute:: docssubmgt3filtergrpclasspkts
            
            	This attribute counts the number of packets  that have been classified (matched) using this rule  entry. This includes all packets delivered to a Service  Flow maximum rate policing function, whether  or not that function drops the packets. Discontinuities  in the value of this counter can occur at re\-initialization  of the managed system, and at other times  as indicated by the value of ifCounterDiscontinuityTime  for the CM MAC Domain interface
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: docssubmgt3filtergrpflowlabel
            
            	This attribute represents the Flow Label field in  the IPv6 header to be matched by the classifier.  The value zero indicates that the Flow Label is not specified  as part of the classifier and is not matched against packets
            	**type**\: int
            
            	**range:** 0..1048575
            
            .. attribute:: docssubmgt3filtergrpcminterfacemask
            
            	This attribute represents a bit\-mask of the CM in\-bound  interfaces to which this classifier applies.  This attribute only applies to upstream Drop Classifiers   being sent to CMs during the registration process
            	**type**\:  :py:class:`DocsL2vpnIfList <ydk.models.cisco_ios_xe.DOCS_L2VPN_MIB.DocsL2vpnIfList>`
            
            .. attribute:: docssubmgt3filtergrprowstatus
            
            	The conceptual row status of this object
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            

            """

            _prefix = 'DOCS-SUBMGT3-MIB'
            _revision = '2007-05-18'

            def __init__(self):
                super(DOCSSUBMGT3MIB.DocsSubmgt3FilterGrpTable.DocsSubmgt3FilterGrpEntry, self).__init__()

                self.yang_name = "docsSubmgt3FilterGrpEntry"
                self.yang_parent_name = "docsSubmgt3FilterGrpTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['docssubmgt3filtergrpgrpid','docssubmgt3filtergrpruleid']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('docssubmgt3filtergrpgrpid', (YLeaf(YType.uint32, 'docsSubmgt3FilterGrpGrpId'), ['int'])),
                    ('docssubmgt3filtergrpruleid', (YLeaf(YType.uint32, 'docsSubmgt3FilterGrpRuleId'), ['int'])),
                    ('docssubmgt3filtergrpaction', (YLeaf(YType.enumeration, 'docsSubmgt3FilterGrpAction'), [('ydk.models.cisco_ios_xe.DOCS_SUBMGT3_MIB', 'DOCSSUBMGT3MIB', 'DocsSubmgt3FilterGrpTable.DocsSubmgt3FilterGrpEntry.DocsSubmgt3FilterGrpAction')])),
                    ('docssubmgt3filtergrppriority', (YLeaf(YType.uint32, 'docsSubmgt3FilterGrpPriority'), ['int'])),
                    ('docssubmgt3filtergrpiptoslow', (YLeaf(YType.str, 'docsSubmgt3FilterGrpIpTosLow'), ['str'])),
                    ('docssubmgt3filtergrpiptoshigh', (YLeaf(YType.str, 'docsSubmgt3FilterGrpIpTosHigh'), ['str'])),
                    ('docssubmgt3filtergrpiptosmask', (YLeaf(YType.str, 'docsSubmgt3FilterGrpIpTosMask'), ['str'])),
                    ('docssubmgt3filtergrpipprotocol', (YLeaf(YType.uint32, 'docsSubmgt3FilterGrpIpProtocol'), ['int'])),
                    ('docssubmgt3filtergrpinetaddrtype', (YLeaf(YType.enumeration, 'docsSubmgt3FilterGrpInetAddrType'), [('ydk.models.cisco_ios_xe.INET_ADDRESS_MIB', 'InetAddressType', '')])),
                    ('docssubmgt3filtergrpinetsrcaddr', (YLeaf(YType.str, 'docsSubmgt3FilterGrpInetSrcAddr'), ['str'])),
                    ('docssubmgt3filtergrpinetsrcmask', (YLeaf(YType.str, 'docsSubmgt3FilterGrpInetSrcMask'), ['str'])),
                    ('docssubmgt3filtergrpinetdestaddr', (YLeaf(YType.str, 'docsSubmgt3FilterGrpInetDestAddr'), ['str'])),
                    ('docssubmgt3filtergrpinetdestmask', (YLeaf(YType.str, 'docsSubmgt3FilterGrpInetDestMask'), ['str'])),
                    ('docssubmgt3filtergrpsrcportstart', (YLeaf(YType.uint16, 'docsSubmgt3FilterGrpSrcPortStart'), ['int'])),
                    ('docssubmgt3filtergrpsrcportend', (YLeaf(YType.uint16, 'docsSubmgt3FilterGrpSrcPortEnd'), ['int'])),
                    ('docssubmgt3filtergrpdestportstart', (YLeaf(YType.uint16, 'docsSubmgt3FilterGrpDestPortStart'), ['int'])),
                    ('docssubmgt3filtergrpdestportend', (YLeaf(YType.uint16, 'docsSubmgt3FilterGrpDestPortEnd'), ['int'])),
                    ('docssubmgt3filtergrpdestmacaddr', (YLeaf(YType.str, 'docsSubmgt3FilterGrpDestMacAddr'), ['str'])),
                    ('docssubmgt3filtergrpdestmacmask', (YLeaf(YType.str, 'docsSubmgt3FilterGrpDestMacMask'), ['str'])),
                    ('docssubmgt3filtergrpsrcmacaddr', (YLeaf(YType.str, 'docsSubmgt3FilterGrpSrcMacAddr'), ['str'])),
                    ('docssubmgt3filtergrpenetprotocoltype', (YLeaf(YType.enumeration, 'docsSubmgt3FilterGrpEnetProtocolType'), [('ydk.models.cisco_ios_xe.DOCS_SUBMGT3_MIB', 'DOCSSUBMGT3MIB', 'DocsSubmgt3FilterGrpTable.DocsSubmgt3FilterGrpEntry.DocsSubmgt3FilterGrpEnetProtocolType')])),
                    ('docssubmgt3filtergrpenetprotocol', (YLeaf(YType.uint32, 'docsSubmgt3FilterGrpEnetProtocol'), ['int'])),
                    ('docssubmgt3filtergrpuserprilow', (YLeaf(YType.uint32, 'docsSubmgt3FilterGrpUserPriLow'), ['int'])),
                    ('docssubmgt3filtergrpuserprihigh', (YLeaf(YType.uint32, 'docsSubmgt3FilterGrpUserPriHigh'), ['int'])),
                    ('docssubmgt3filtergrpvlanid', (YLeaf(YType.uint32, 'docsSubmgt3FilterGrpVlanId'), ['int'])),
                    ('docssubmgt3filtergrpclasspkts', (YLeaf(YType.uint64, 'docsSubmgt3FilterGrpClassPkts'), ['int'])),
                    ('docssubmgt3filtergrpflowlabel', (YLeaf(YType.uint32, 'docsSubmgt3FilterGrpFlowLabel'), ['int'])),
                    ('docssubmgt3filtergrpcminterfacemask', (YLeaf(YType.bits, 'docsSubmgt3FilterGrpCmInterfaceMask'), ['Bits'])),
                    ('docssubmgt3filtergrprowstatus', (YLeaf(YType.enumeration, 'docsSubmgt3FilterGrpRowStatus'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowStatus', '')])),
                ])
                self.docssubmgt3filtergrpgrpid = None
                self.docssubmgt3filtergrpruleid = None
                self.docssubmgt3filtergrpaction = None
                self.docssubmgt3filtergrppriority = None
                self.docssubmgt3filtergrpiptoslow = None
                self.docssubmgt3filtergrpiptoshigh = None
                self.docssubmgt3filtergrpiptosmask = None
                self.docssubmgt3filtergrpipprotocol = None
                self.docssubmgt3filtergrpinetaddrtype = None
                self.docssubmgt3filtergrpinetsrcaddr = None
                self.docssubmgt3filtergrpinetsrcmask = None
                self.docssubmgt3filtergrpinetdestaddr = None
                self.docssubmgt3filtergrpinetdestmask = None
                self.docssubmgt3filtergrpsrcportstart = None
                self.docssubmgt3filtergrpsrcportend = None
                self.docssubmgt3filtergrpdestportstart = None
                self.docssubmgt3filtergrpdestportend = None
                self.docssubmgt3filtergrpdestmacaddr = None
                self.docssubmgt3filtergrpdestmacmask = None
                self.docssubmgt3filtergrpsrcmacaddr = None
                self.docssubmgt3filtergrpenetprotocoltype = None
                self.docssubmgt3filtergrpenetprotocol = None
                self.docssubmgt3filtergrpuserprilow = None
                self.docssubmgt3filtergrpuserprihigh = None
                self.docssubmgt3filtergrpvlanid = None
                self.docssubmgt3filtergrpclasspkts = None
                self.docssubmgt3filtergrpflowlabel = None
                self.docssubmgt3filtergrpcminterfacemask = Bits()
                self.docssubmgt3filtergrprowstatus = None
                self._segment_path = lambda: "docsSubmgt3FilterGrpEntry" + "[docsSubmgt3FilterGrpGrpId='" + str(self.docssubmgt3filtergrpgrpid) + "']" + "[docsSubmgt3FilterGrpRuleId='" + str(self.docssubmgt3filtergrpruleid) + "']"
                self._absolute_path = lambda: "DOCS-SUBMGT3-MIB:DOCS-SUBMGT3-MIB/docsSubmgt3FilterGrpTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(DOCSSUBMGT3MIB.DocsSubmgt3FilterGrpTable.DocsSubmgt3FilterGrpEntry, ['docssubmgt3filtergrpgrpid', 'docssubmgt3filtergrpruleid', 'docssubmgt3filtergrpaction', 'docssubmgt3filtergrppriority', 'docssubmgt3filtergrpiptoslow', 'docssubmgt3filtergrpiptoshigh', 'docssubmgt3filtergrpiptosmask', 'docssubmgt3filtergrpipprotocol', 'docssubmgt3filtergrpinetaddrtype', 'docssubmgt3filtergrpinetsrcaddr', 'docssubmgt3filtergrpinetsrcmask', 'docssubmgt3filtergrpinetdestaddr', 'docssubmgt3filtergrpinetdestmask', 'docssubmgt3filtergrpsrcportstart', 'docssubmgt3filtergrpsrcportend', 'docssubmgt3filtergrpdestportstart', 'docssubmgt3filtergrpdestportend', 'docssubmgt3filtergrpdestmacaddr', 'docssubmgt3filtergrpdestmacmask', 'docssubmgt3filtergrpsrcmacaddr', 'docssubmgt3filtergrpenetprotocoltype', 'docssubmgt3filtergrpenetprotocol', 'docssubmgt3filtergrpuserprilow', 'docssubmgt3filtergrpuserprihigh', 'docssubmgt3filtergrpvlanid', 'docssubmgt3filtergrpclasspkts', 'docssubmgt3filtergrpflowlabel', 'docssubmgt3filtergrpcminterfacemask', 'docssubmgt3filtergrprowstatus'], name, value)

            class DocsSubmgt3FilterGrpAction(Enum):
                """
                DocsSubmgt3FilterGrpAction (Enum Class)

                This attribute represents the action to take upon 

                this filter matching.  'permit' means to stop the classification 

                matching and accept the packet for further 

                processing.  'deny' means to drop the packet.

                .. data:: permit = 1

                .. data:: deny = 2

                """

                permit = Enum.YLeaf(1, "permit")

                deny = Enum.YLeaf(2, "deny")


            class DocsSubmgt3FilterGrpEnetProtocolType(Enum):
                """
                DocsSubmgt3FilterGrpEnetProtocolType (Enum Class)

                This attribute indicates the format of the layer 3 

                protocol ID in the Ethernet packet. A value of 'none' 

                means that the rule does not use the layer 3 protocol 

                type as a matching criteria. A value of 'ethertype' 

                means that the rule applies only to frames that contain 

                an EtherType value. EtherType values are contained 

                in packets using the DEC\-Intel\-Xerox (DIX) encapsulation 

                or the RFC 1042 Sub\-Network Access Protocol 

                (SNAP) encapsulation formats. A value of 'dsap' means 

                that the rule applies only to frames using the IEEE802.3 

                encapsulation format with a Destination Service 

                Access Point (DSAP) other than 0xAA (which is reserved 

                for SNAP). A value of 'mac' means that the rule 

                applies only to MAC management messages for MAC management 

                messages. A value of 'all' means that the rule 

                matches all Ethernet packets. If the Ethernet frame 

                contains an 802.1P/Q Tag header (i.e., EtherType 

                0x8100), this attribute applies to the embedded EtherType 

                field within the 802.1p/Q header. 

                The value 'mac' is only used for passing UDCs to CMs during  

                Registration. The CMTS ignores filter rules that include  

                the value of this attribute set to 'mac' for CMTS enforced  

                upstream and downstream subscriber management filter group 

                rules.

                .. data:: none = 0

                .. data:: ethertype = 1

                .. data:: dsap = 2

                .. data:: mac = 3

                .. data:: all = 4

                """

                none = Enum.YLeaf(0, "none")

                ethertype = Enum.YLeaf(1, "ethertype")

                dsap = Enum.YLeaf(2, "dsap")

                mac = Enum.YLeaf(3, "mac")

                all = Enum.YLeaf(4, "all")


    def clone_ptr(self):
        self._top_entity = DOCSSUBMGT3MIB()
        return self._top_entity

