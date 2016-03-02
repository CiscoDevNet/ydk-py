""" CISCO_CBP_TARGET_MIB 

This MIB module defines the managed objects for
representing targets which have class\-based policy  
mappings.  A target can be any logical interface 
to which a class\-based policy is able to be associated.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError


from ydk.models.cbp.CISCO_CBP_TARGET_TC_MIB import CcbptPolicySourceType_Enum
from ydk.models.cbp.CISCO_CBP_TARGET_TC_MIB import CcbptTargetDirection_Enum
from ydk.models.cbp.CISCO_CBP_TARGET_TC_MIB import CcbptTargetType_Enum
from ydk.models.snmpv2.SNMPv2_TC import RowStatus_Enum
from ydk.models.snmpv2.SNMPv2_TC import StorageType_Enum


class CISCOCBPTARGETMIB(object):
    """
    
    
    .. attribute:: ccbpttargetattachcfg
    
    	
    	**type**\: :py:class:`CcbptTargetAttachCfg <ydk.models.cbp.CISCO_CBP_TARGET_MIB.CISCOCBPTARGETMIB.CcbptTargetAttachCfg>`
    
    .. attribute:: ccbpttargettable
    
    	This table describes the class\-based policy attachments to to specific targets
    	**type**\: :py:class:`CcbptTargetTable <ydk.models.cbp.CISCO_CBP_TARGET_MIB.CISCOCBPTARGETMIB.CcbptTargetTable>`
    
    

    """

    _prefix = 'cisco-cbp-target'
    _revision = '2006-05-24'

    def __init__(self):
        self.ccbpttargetattachcfg = CISCOCBPTARGETMIB.CcbptTargetAttachCfg()
        self.ccbpttargetattachcfg.parent = self
        self.ccbpttargettable = CISCOCBPTARGETMIB.CcbptTargetTable()
        self.ccbpttargettable.parent = self


    class CcbptTargetAttachCfg(object):
        """
        
        
        .. attribute:: ccbptpolicyidnext
        
        	This object indicates the next available value of  ccbptPolicyId that can be used to create a new conceptual row in the ccbptTargetTable.  If no available identifier exists, then this object will have the value '0'
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: ccbpttargettablelastchange
        
        	The value of sysUpTime at the time of the last change to an entry in the ccbptTargetTable
        	**type**\: int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'cisco-cbp-target'
        _revision = '2006-05-24'

        def __init__(self):
            self.parent = None
            self.ccbptpolicyidnext = None
            self.ccbpttargettablelastchange = None

        @property
        def _common_path(self):

            return '/CISCO-CBP-TARGET-MIB:CISCO-CBP-TARGET-MIB/CISCO-CBP-TARGET-MIB:ccbptTargetAttachCfg'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.ccbptpolicyidnext is not None:
                return True

            if self.ccbpttargettablelastchange is not None:
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cbp._meta import _CISCO_CBP_TARGET_MIB as meta
            return meta._meta_table['CISCOCBPTARGETMIB.CcbptTargetAttachCfg']['meta_info']


    class CcbptTargetTable(object):
        """
        This table describes the class\-based policy attachments to
        to specific targets.
        
        .. attribute:: ccbpttargetentry
        
        	Each entry describes a class\-based policy attachment to a  particular target.    The ccbptTargetType uniquely identifies the type of target in the attachment.  Additionally, the ccbptTargetId uniquely identifies the target in attachment and is of the format indicated by the ccbptTargetType.  The ccbptTargetDir  identifies the direction, relative to the ccbptTargetId,  to which the policy is attached.  The ccbptPolicySourceType identifies the source\-type of the policy attached.  The  ccbptPolicyId uniquely identifies the policy within the scope of ccbptTargetType, ccbptTargetId, ccbptTargetDir, and  ccbptPolicySourceType.  A class\-based policy attachment to a target can be created  through other network management interfaces (e.g., the local console), in which case the SNMP entity will automatically  create an entry in this table.  A class\-based policy attachment to a target can be destroyed through other network management interfaces, in which case the SNMP entity will automatically destroy the corresponding entry in this table.  A class\-based policy attachment to a target can be created, destroyed, and modified through the SNMP using  ccbptTargetStatus using the semantics described by the  RowStatus Textual Convention.  However, when creating a new class\-based policy attachment to a target, the value of ccbptPolicyIdNext should be used to identify the new policy within the scope of the target type, identifier, direction, and policy\-source type
        	**type**\: list of :py:class:`CcbptTargetEntry <ydk.models.cbp.CISCO_CBP_TARGET_MIB.CISCOCBPTARGETMIB.CcbptTargetTable.CcbptTargetEntry>`
        
        

        """

        _prefix = 'cisco-cbp-target'
        _revision = '2006-05-24'

        def __init__(self):
            self.parent = None
            self.ccbpttargetentry = YList()
            self.ccbpttargetentry.parent = self
            self.ccbpttargetentry.name = 'ccbpttargetentry'


        class CcbptTargetEntry(object):
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
            
            .. attribute:: ccbptpolicyid
            
            	Unique identifier of this class\-based policy instance
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: ccbptpolicysourcetype
            
            	The source\-type of the class\-based policy for this target. The source\-type refers to the source of the class\-based policy definition.  The intent of this object is to allow implementations to distinguish between different MIBs defining policy\-maps. 
            	**type**\: :py:class:`CcbptPolicySourceType_Enum <ydk.models.cbp.CISCO_CBP_TARGET_TC_MIB.CcbptPolicySourceType_Enum>`
            
            .. attribute:: ccbpttargetdir
            
            	The direction relative to the ccbptTargetId for this class based policy attachment.  
            	**type**\: :py:class:`CcbptTargetDirection_Enum <ydk.models.cbp.CISCO_CBP_TARGET_TC_MIB.CcbptTargetDirection_Enum>`
            
            .. attribute:: ccbpttargetid
            
            	The target identifier for this class\-based policy attachment. For decoding the ccbptTargetId refer to the ccbptTargetType object and the CcbptTargetType description
            	**type**\: str
            
            	**range:** 0..64
            
            .. attribute:: ccbpttargettype
            
            	The type of target for this class\-based policy attachment. This object identifies the format of the ccbptTargetId for this entry
            	**type**\: :py:class:`CcbptTargetType_Enum <ydk.models.cbp.CISCO_CBP_TARGET_TC_MIB.CcbptTargetType_Enum>`
            
            .. attribute:: ccbptpolicyattachtime
            
            	The value of sysUpTime for the last time that the corresponding ccbptTargetStatus instance transitioned to the 'active' state.  
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ccbptpolicyinstance
            
            	Refers to the first accessible object in the policy  instance table used to manage policy instance information  for policy\-maps of this ccbptPolicySourceType.  Specific MIB tables are not mentioned here as the intent of this mapping is to allow for different implementations to  refer to their supported class\-based policy definition table without requiring support of a specific MIB module
            	**type**\: str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: ccbptpolicymap
            
            	Refers to the first accessible object in the policy\-map definition table used to manage policy\-map information for policy\-maps for the corresponding ccbptPolicySourceType.  Specific MIB tables are not mentioned here as the intent of this mapping is to allow for different implementations to  refer to their supported class\-based policy definition table without requiring support of a specific MIB module
            	**type**\: str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: ccbpttargetstatus
            
            	The status of the policy attachment to this target.  The value for the corresponding instance of each of the  following objects must be valid before the attachment  can be activated\:     \-ccbptTargetStorageType     \-ccbptPolicyMap  Observe that no corresponding instance of any object in  this table can be modified when the value of this object is 'active'
            	**type**\: :py:class:`RowStatus_Enum <ydk.models.snmpv2.SNMPv2_TC.RowStatus_Enum>`
            
            .. attribute:: ccbpttargetstoragetype
            
            	This object indicates how the device stores the data  contained by the conceptual row.  If an instance of this object has the value 'permanent', then this MIB definition does not require the SNMP entity to allow the instance of any object in the corresponding conceptual row to be writable through the SNMP
            	**type**\: :py:class:`StorageType_Enum <ydk.models.snmpv2.SNMPv2_TC.StorageType_Enum>`
            
            

            """

            _prefix = 'cisco-cbp-target'
            _revision = '2006-05-24'

            def __init__(self):
                self.parent = None
                self.ccbptpolicyid = None
                self.ccbptpolicysourcetype = None
                self.ccbpttargetdir = None
                self.ccbpttargetid = None
                self.ccbpttargettype = None
                self.ccbptpolicyattachtime = None
                self.ccbptpolicyinstance = None
                self.ccbptpolicymap = None
                self.ccbpttargetstatus = None
                self.ccbpttargetstoragetype = None

            @property
            def _common_path(self):
                if self.ccbptpolicyid is None:
                    raise YPYDataValidationError('Key property ccbptpolicyid is None')
                if self.ccbptpolicysourcetype is None:
                    raise YPYDataValidationError('Key property ccbptpolicysourcetype is None')
                if self.ccbpttargetdir is None:
                    raise YPYDataValidationError('Key property ccbpttargetdir is None')
                if self.ccbpttargetid is None:
                    raise YPYDataValidationError('Key property ccbpttargetid is None')
                if self.ccbpttargettype is None:
                    raise YPYDataValidationError('Key property ccbpttargettype is None')

                return '/CISCO-CBP-TARGET-MIB:CISCO-CBP-TARGET-MIB/CISCO-CBP-TARGET-MIB:ccbptTargetTable/CISCO-CBP-TARGET-MIB:ccbptTargetEntry[CISCO-CBP-TARGET-MIB:ccbptPolicyId = ' + str(self.ccbptpolicyid) + '][CISCO-CBP-TARGET-MIB:ccbptPolicySourceType = ' + str(self.ccbptpolicysourcetype) + '][CISCO-CBP-TARGET-MIB:ccbptTargetDir = ' + str(self.ccbpttargetdir) + '][CISCO-CBP-TARGET-MIB:ccbptTargetId = ' + str(self.ccbpttargetid) + '][CISCO-CBP-TARGET-MIB:ccbptTargetType = ' + str(self.ccbpttargettype) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.ccbptpolicyid is not None:
                    return True

                if self.ccbptpolicysourcetype is not None:
                    return True

                if self.ccbpttargetdir is not None:
                    return True

                if self.ccbpttargetid is not None:
                    return True

                if self.ccbpttargettype is not None:
                    return True

                if self.ccbptpolicyattachtime is not None:
                    return True

                if self.ccbptpolicyinstance is not None:
                    return True

                if self.ccbptpolicymap is not None:
                    return True

                if self.ccbpttargetstatus is not None:
                    return True

                if self.ccbpttargetstoragetype is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cbp._meta import _CISCO_CBP_TARGET_MIB as meta
                return meta._meta_table['CISCOCBPTARGETMIB.CcbptTargetTable.CcbptTargetEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-CBP-TARGET-MIB:CISCO-CBP-TARGET-MIB/CISCO-CBP-TARGET-MIB:ccbptTargetTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.ccbpttargetentry is not None:
                for child_ref in self.ccbpttargetentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cbp._meta import _CISCO_CBP_TARGET_MIB as meta
            return meta._meta_table['CISCOCBPTARGETMIB.CcbptTargetTable']['meta_info']

    @property
    def _common_path(self):

        return '/CISCO-CBP-TARGET-MIB:CISCO-CBP-TARGET-MIB'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if not self.is_config():
            return False
        if self.is_presence():
            return True
        if self.ccbpttargetattachcfg is not None and self.ccbpttargetattachcfg._has_data():
            return True

        if self.ccbpttargetattachcfg is not None and self.ccbpttargetattachcfg.is_presence():
            return True

        if self.ccbpttargettable is not None and self.ccbpttargettable._has_data():
            return True

        if self.ccbpttargettable is not None and self.ccbpttargettable.is_presence():
            return True

        return False

    def is_presence(self):
        ''' Returns True if this instance represents presence container else returns False '''
        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cbp._meta import _CISCO_CBP_TARGET_MIB as meta
        return meta._meta_table['CISCOCBPTARGETMIB']['meta_info']


