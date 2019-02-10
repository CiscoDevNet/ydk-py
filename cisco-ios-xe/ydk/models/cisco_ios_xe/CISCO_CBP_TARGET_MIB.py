""" CISCO_CBP_TARGET_MIB 

This MIB module defines the managed objects for
representing targets which have class\-based policy  
mappings.  A target can be any logical interface 
to which a class\-based policy is able to be associated.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class CISCOCBPTARGETMIB(Entity):
    """
    
    
    .. attribute:: ccbpttargetattachcfg
    
    	
    	**type**\:  :py:class:`CcbptTargetAttachCfg <ydk.models.cisco_ios_xe.CISCO_CBP_TARGET_MIB.CISCOCBPTARGETMIB.CcbptTargetAttachCfg>`
    
    	**config**\: False
    
    .. attribute:: ccbpttargettable
    
    	This table describes the class\-based policy attachments to to specific targets
    	**type**\:  :py:class:`CcbptTargetTable <ydk.models.cisco_ios_xe.CISCO_CBP_TARGET_MIB.CISCOCBPTARGETMIB.CcbptTargetTable>`
    
    	**config**\: False
    
    

    """

    _prefix = 'CISCO-CBP-TARGET-MIB'
    _revision = '2006-05-24'

    def __init__(self):
        super(CISCOCBPTARGETMIB, self).__init__()
        self._top_entity = None

        self.yang_name = "CISCO-CBP-TARGET-MIB"
        self.yang_parent_name = "CISCO-CBP-TARGET-MIB"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("ccbptTargetAttachCfg", ("ccbpttargetattachcfg", CISCOCBPTARGETMIB.CcbptTargetAttachCfg)), ("ccbptTargetTable", ("ccbpttargettable", CISCOCBPTARGETMIB.CcbptTargetTable))])
        self._leafs = OrderedDict()

        self.ccbpttargetattachcfg = CISCOCBPTARGETMIB.CcbptTargetAttachCfg()
        self.ccbpttargetattachcfg.parent = self
        self._children_name_map["ccbpttargetattachcfg"] = "ccbptTargetAttachCfg"

        self.ccbpttargettable = CISCOCBPTARGETMIB.CcbptTargetTable()
        self.ccbpttargettable.parent = self
        self._children_name_map["ccbpttargettable"] = "ccbptTargetTable"
        self._segment_path = lambda: "CISCO-CBP-TARGET-MIB:CISCO-CBP-TARGET-MIB"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(CISCOCBPTARGETMIB, [], name, value)


    class CcbptTargetAttachCfg(Entity):
        """
        
        
        .. attribute:: ccbptpolicyidnext
        
        	This object indicates the next available value of  ccbptPolicyId that can be used to create a new conceptual row in the ccbptTargetTable.  If no available identifier exists, then this object will have the value '0'
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**config**\: False
        
        .. attribute:: ccbpttargettablelastchange
        
        	The value of sysUpTime at the time of the last change to an entry in the ccbptTargetTable
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-CBP-TARGET-MIB'
        _revision = '2006-05-24'

        def __init__(self):
            super(CISCOCBPTARGETMIB.CcbptTargetAttachCfg, self).__init__()

            self.yang_name = "ccbptTargetAttachCfg"
            self.yang_parent_name = "CISCO-CBP-TARGET-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('ccbptpolicyidnext', (YLeaf(YType.uint32, 'ccbptPolicyIdNext'), ['int'])),
                ('ccbpttargettablelastchange', (YLeaf(YType.uint32, 'ccbptTargetTableLastChange'), ['int'])),
            ])
            self.ccbptpolicyidnext = None
            self.ccbpttargettablelastchange = None
            self._segment_path = lambda: "ccbptTargetAttachCfg"
            self._absolute_path = lambda: "CISCO-CBP-TARGET-MIB:CISCO-CBP-TARGET-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOCBPTARGETMIB.CcbptTargetAttachCfg, ['ccbptpolicyidnext', 'ccbpttargettablelastchange'], name, value)



    class CcbptTargetTable(Entity):
        """
        This table describes the class\-based policy attachments to
        to specific targets.
        
        .. attribute:: ccbpttargetentry
        
        	Each entry describes a class\-based policy attachment to a  particular target.    The ccbptTargetType uniquely identifies the type of target in the attachment.  Additionally, the ccbptTargetId uniquely identifies the target in attachment and is of the format indicated by the ccbptTargetType.  The ccbptTargetDir  identifies the direction, relative to the ccbptTargetId,  to which the policy is attached.  The ccbptPolicySourceType identifies the source\-type of the policy attached.  The  ccbptPolicyId uniquely identifies the policy within the scope of ccbptTargetType, ccbptTargetId, ccbptTargetDir, and  ccbptPolicySourceType.  A class\-based policy attachment to a target can be created  through other network management interfaces (e.g., the local console), in which case the SNMP entity will automatically  create an entry in this table.  A class\-based policy attachment to a target can be destroyed through other network management interfaces, in which case the SNMP entity will automatically destroy the corresponding entry in this table.  A class\-based policy attachment to a target can be created, destroyed, and modified through the SNMP using  ccbptTargetStatus using the semantics described by the  RowStatus Textual Convention.  However, when creating a new class\-based policy attachment to a target, the value of ccbptPolicyIdNext should be used to identify the new policy within the scope of the target type, identifier, direction, and policy\-source type
        	**type**\: list of  		 :py:class:`CcbptTargetEntry <ydk.models.cisco_ios_xe.CISCO_CBP_TARGET_MIB.CISCOCBPTARGETMIB.CcbptTargetTable.CcbptTargetEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-CBP-TARGET-MIB'
        _revision = '2006-05-24'

        def __init__(self):
            super(CISCOCBPTARGETMIB.CcbptTargetTable, self).__init__()

            self.yang_name = "ccbptTargetTable"
            self.yang_parent_name = "CISCO-CBP-TARGET-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("ccbptTargetEntry", ("ccbpttargetentry", CISCOCBPTARGETMIB.CcbptTargetTable.CcbptTargetEntry))])
            self._leafs = OrderedDict()

            self.ccbpttargetentry = YList(self)
            self._segment_path = lambda: "ccbptTargetTable"
            self._absolute_path = lambda: "CISCO-CBP-TARGET-MIB:CISCO-CBP-TARGET-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOCBPTARGETMIB.CcbptTargetTable, [], name, value)


        class CcbptTargetEntry(Entity):
            """
            Each entry describes a class\-based policy attachment to a 
            particular target. 
             
            The ccbptTargetType uniquely identifies the type of target
            in the attachment.  Additionally, the ccbptTargetId uniquely
            identifies the target in attachment and is of the format
            indicated by the ccbptTargetType.  The ccbptTargetDir 
            identifies the direction, relative to the ccbptTargetId, 
            to which the policy is attached.  The ccbptPolicySourceType
            identifies the source\-type of the policy attached.  The 
            ccbptPolicyId uniquely identifies the policy within the scope
            of ccbptTargetType, ccbptTargetId, ccbptTargetDir, and 
            ccbptPolicySourceType.
            
            A class\-based policy attachment to a target can be created 
            through other network management interfaces (e.g., the local
            console), in which case the SNMP entity will automatically 
            create an entry in this table.
            
            A class\-based policy attachment to a target can be destroyed
            through other network management interfaces, in which case
            the SNMP entity will automatically destroy the corresponding
            entry in this table.
            
            A class\-based policy attachment to a target can be created,
            destroyed, and modified through the SNMP using 
            ccbptTargetStatus using the semantics described by the 
            RowStatus Textual Convention.  However, when creating a new
            class\-based policy attachment to a target, the value of
            ccbptPolicyIdNext should be used to identify the new policy
            within the scope of the target type, identifier, direction,
            and policy\-source type.
            
            .. attribute:: ccbpttargettype  (key)
            
            	The type of target for this class\-based policy attachment. This object identifies the format of the ccbptTargetId for this entry
            	**type**\:  :py:class:`CcbptTargetType <ydk.models.cisco_ios_xe.CISCO_CBP_TARGET_TC_MIB.CcbptTargetType>`
            
            	**config**\: False
            
            .. attribute:: ccbpttargetid  (key)
            
            	The target identifier for this class\-based policy attachment. For decoding the ccbptTargetId refer to the ccbptTargetType object and the CcbptTargetType description
            	**type**\: str
            
            	**length:** 0..64
            
            	**config**\: False
            
            .. attribute:: ccbpttargetdir  (key)
            
            	The direction relative to the ccbptTargetId for this class based policy attachment.  
            	**type**\:  :py:class:`CcbptTargetDirection <ydk.models.cisco_ios_xe.CISCO_CBP_TARGET_TC_MIB.CcbptTargetDirection>`
            
            	**config**\: False
            
            .. attribute:: ccbptpolicysourcetype  (key)
            
            	The source\-type of the class\-based policy for this target. The source\-type refers to the source of the class\-based policy definition.  The intent of this object is to allow implementations to distinguish between different MIBs defining policy\-maps. 
            	**type**\:  :py:class:`CcbptPolicySourceType <ydk.models.cisco_ios_xe.CISCO_CBP_TARGET_TC_MIB.CcbptPolicySourceType>`
            
            	**config**\: False
            
            .. attribute:: ccbptpolicyid  (key)
            
            	Unique identifier of this class\-based policy instance
            	**type**\: int
            
            	**range:** 1..4294967295
            
            	**config**\: False
            
            .. attribute:: ccbpttargetstatus
            
            	The status of the policy attachment to this target.  The value for the corresponding instance of each of the  following objects must be valid before the attachment  can be activated\:     \-ccbptTargetStorageType     \-ccbptPolicyMap  Observe that no corresponding instance of any object in  this table can be modified when the value of this object is 'active'
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            	**config**\: False
            
            .. attribute:: ccbpttargetstoragetype
            
            	This object indicates how the device stores the data  contained by the conceptual row.  If an instance of this object has the value 'permanent', then this MIB definition does not require the SNMP entity to allow the instance of any object in the corresponding conceptual row to be writable through the SNMP
            	**type**\:  :py:class:`StorageType <ydk.models.cisco_ios_xe.SNMPv2_TC.StorageType>`
            
            	**config**\: False
            
            .. attribute:: ccbptpolicymap
            
            	Refers to the first accessible object in the policy\-map definition table used to manage policy\-map information for policy\-maps for the corresponding ccbptPolicySourceType.  Specific MIB tables are not mentioned here as the intent of this mapping is to allow for different implementations to  refer to their supported class\-based policy definition table without requiring support of a specific MIB module
            	**type**\: str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            	**config**\: False
            
            .. attribute:: ccbptpolicyinstance
            
            	Refers to the first accessible object in the policy  instance table used to manage policy instance information  for policy\-maps of this ccbptPolicySourceType.  Specific MIB tables are not mentioned here as the intent of this mapping is to allow for different implementations to  refer to their supported class\-based policy definition table without requiring support of a specific MIB module
            	**type**\: str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            	**config**\: False
            
            .. attribute:: ccbptpolicyattachtime
            
            	The value of sysUpTime for the last time that the corresponding ccbptTargetStatus instance transitioned to the 'active' state.  
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            

            """

            _prefix = 'CISCO-CBP-TARGET-MIB'
            _revision = '2006-05-24'

            def __init__(self):
                super(CISCOCBPTARGETMIB.CcbptTargetTable.CcbptTargetEntry, self).__init__()

                self.yang_name = "ccbptTargetEntry"
                self.yang_parent_name = "ccbptTargetTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ccbpttargettype','ccbpttargetid','ccbpttargetdir','ccbptpolicysourcetype','ccbptpolicyid']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ccbpttargettype', (YLeaf(YType.enumeration, 'ccbptTargetType'), [('ydk.models.cisco_ios_xe.CISCO_CBP_TARGET_TC_MIB', 'CcbptTargetType', '')])),
                    ('ccbpttargetid', (YLeaf(YType.str, 'ccbptTargetId'), ['str'])),
                    ('ccbpttargetdir', (YLeaf(YType.enumeration, 'ccbptTargetDir'), [('ydk.models.cisco_ios_xe.CISCO_CBP_TARGET_TC_MIB', 'CcbptTargetDirection', '')])),
                    ('ccbptpolicysourcetype', (YLeaf(YType.enumeration, 'ccbptPolicySourceType'), [('ydk.models.cisco_ios_xe.CISCO_CBP_TARGET_TC_MIB', 'CcbptPolicySourceType', '')])),
                    ('ccbptpolicyid', (YLeaf(YType.uint32, 'ccbptPolicyId'), ['int'])),
                    ('ccbpttargetstatus', (YLeaf(YType.enumeration, 'ccbptTargetStatus'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowStatus', '')])),
                    ('ccbpttargetstoragetype', (YLeaf(YType.enumeration, 'ccbptTargetStorageType'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'StorageType', '')])),
                    ('ccbptpolicymap', (YLeaf(YType.str, 'ccbptPolicyMap'), ['str'])),
                    ('ccbptpolicyinstance', (YLeaf(YType.str, 'ccbptPolicyInstance'), ['str'])),
                    ('ccbptpolicyattachtime', (YLeaf(YType.uint32, 'ccbptPolicyAttachTime'), ['int'])),
                ])
                self.ccbpttargettype = None
                self.ccbpttargetid = None
                self.ccbpttargetdir = None
                self.ccbptpolicysourcetype = None
                self.ccbptpolicyid = None
                self.ccbpttargetstatus = None
                self.ccbpttargetstoragetype = None
                self.ccbptpolicymap = None
                self.ccbptpolicyinstance = None
                self.ccbptpolicyattachtime = None
                self._segment_path = lambda: "ccbptTargetEntry" + "[ccbptTargetType='" + str(self.ccbpttargettype) + "']" + "[ccbptTargetId='" + str(self.ccbpttargetid) + "']" + "[ccbptTargetDir='" + str(self.ccbpttargetdir) + "']" + "[ccbptPolicySourceType='" + str(self.ccbptpolicysourcetype) + "']" + "[ccbptPolicyId='" + str(self.ccbptpolicyid) + "']"
                self._absolute_path = lambda: "CISCO-CBP-TARGET-MIB:CISCO-CBP-TARGET-MIB/ccbptTargetTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOCBPTARGETMIB.CcbptTargetTable.CcbptTargetEntry, ['ccbpttargettype', 'ccbpttargetid', 'ccbpttargetdir', 'ccbptpolicysourcetype', 'ccbptpolicyid', 'ccbpttargetstatus', 'ccbpttargetstoragetype', 'ccbptpolicymap', 'ccbptpolicyinstance', 'ccbptpolicyattachtime'], name, value)



    def clone_ptr(self):
        self._top_entity = CISCOCBPTARGETMIB()
        return self._top_entity



