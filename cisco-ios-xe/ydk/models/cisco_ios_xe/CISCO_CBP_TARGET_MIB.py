""" CISCO_CBP_TARGET_MIB 

This MIB module defines the managed objects for
representing targets which have class\-based policy  
mappings.  A target can be any logical interface 
to which a class\-based policy is able to be associated.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class CiscoCbpTargetMib(Entity):
    """
    
    
    .. attribute:: ccbpttargetattachcfg
    
    	
    	**type**\:   :py:class:`Ccbpttargetattachcfg <ydk.models.cisco_ios_xe.CISCO_CBP_TARGET_MIB.CiscoCbpTargetMib.Ccbpttargetattachcfg>`
    
    .. attribute:: ccbpttargettable
    
    	This table describes the class\-based policy attachments to to specific targets
    	**type**\:   :py:class:`Ccbpttargettable <ydk.models.cisco_ios_xe.CISCO_CBP_TARGET_MIB.CiscoCbpTargetMib.Ccbpttargettable>`
    
    

    """

    _prefix = 'CISCO-CBP-TARGET-MIB'
    _revision = '2006-05-24'

    def __init__(self):
        super(CiscoCbpTargetMib, self).__init__()
        self._top_entity = None

        self.yang_name = "CISCO-CBP-TARGET-MIB"
        self.yang_parent_name = "CISCO-CBP-TARGET-MIB"

        self.ccbpttargetattachcfg = CiscoCbpTargetMib.Ccbpttargetattachcfg()
        self.ccbpttargetattachcfg.parent = self
        self._children_name_map["ccbpttargetattachcfg"] = "ccbptTargetAttachCfg"
        self._children_yang_names.add("ccbptTargetAttachCfg")

        self.ccbpttargettable = CiscoCbpTargetMib.Ccbpttargettable()
        self.ccbpttargettable.parent = self
        self._children_name_map["ccbpttargettable"] = "ccbptTargetTable"
        self._children_yang_names.add("ccbptTargetTable")


    class Ccbpttargetattachcfg(Entity):
        """
        
        
        .. attribute:: ccbptpolicyidnext
        
        	This object indicates the next available value of  ccbptPolicyId that can be used to create a new conceptual row in the ccbptTargetTable.  If no available identifier exists, then this object will have the value '0'
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: ccbpttargettablelastchange
        
        	The value of sysUpTime at the time of the last change to an entry in the ccbptTargetTable
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'CISCO-CBP-TARGET-MIB'
        _revision = '2006-05-24'

        def __init__(self):
            super(CiscoCbpTargetMib.Ccbpttargetattachcfg, self).__init__()

            self.yang_name = "ccbptTargetAttachCfg"
            self.yang_parent_name = "CISCO-CBP-TARGET-MIB"

            self.ccbptpolicyidnext = YLeaf(YType.uint32, "ccbptPolicyIdNext")

            self.ccbpttargettablelastchange = YLeaf(YType.uint32, "ccbptTargetTableLastChange")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("ccbptpolicyidnext",
                            "ccbpttargettablelastchange") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoCbpTargetMib.Ccbpttargetattachcfg, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoCbpTargetMib.Ccbpttargetattachcfg, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.ccbptpolicyidnext.is_set or
                self.ccbpttargettablelastchange.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.ccbptpolicyidnext.yfilter != YFilter.not_set or
                self.ccbpttargettablelastchange.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "ccbptTargetAttachCfg" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-CBP-TARGET-MIB:CISCO-CBP-TARGET-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.ccbptpolicyidnext.is_set or self.ccbptpolicyidnext.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ccbptpolicyidnext.get_name_leafdata())
            if (self.ccbpttargettablelastchange.is_set or self.ccbpttargettablelastchange.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ccbpttargettablelastchange.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "ccbptPolicyIdNext" or name == "ccbptTargetTableLastChange"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "ccbptPolicyIdNext"):
                self.ccbptpolicyidnext = value
                self.ccbptpolicyidnext.value_namespace = name_space
                self.ccbptpolicyidnext.value_namespace_prefix = name_space_prefix
            if(value_path == "ccbptTargetTableLastChange"):
                self.ccbpttargettablelastchange = value
                self.ccbpttargettablelastchange.value_namespace = name_space
                self.ccbpttargettablelastchange.value_namespace_prefix = name_space_prefix


    class Ccbpttargettable(Entity):
        """
        This table describes the class\-based policy attachments to
        to specific targets.
        
        .. attribute:: ccbpttargetentry
        
        	Each entry describes a class\-based policy attachment to a  particular target.    The ccbptTargetType uniquely identifies the type of target in the attachment.  Additionally, the ccbptTargetId uniquely identifies the target in attachment and is of the format indicated by the ccbptTargetType.  The ccbptTargetDir  identifies the direction, relative to the ccbptTargetId,  to which the policy is attached.  The ccbptPolicySourceType identifies the source\-type of the policy attached.  The  ccbptPolicyId uniquely identifies the policy within the scope of ccbptTargetType, ccbptTargetId, ccbptTargetDir, and  ccbptPolicySourceType.  A class\-based policy attachment to a target can be created  through other network management interfaces (e.g., the local console), in which case the SNMP entity will automatically  create an entry in this table.  A class\-based policy attachment to a target can be destroyed through other network management interfaces, in which case the SNMP entity will automatically destroy the corresponding entry in this table.  A class\-based policy attachment to a target can be created, destroyed, and modified through the SNMP using  ccbptTargetStatus using the semantics described by the  RowStatus Textual Convention.  However, when creating a new class\-based policy attachment to a target, the value of ccbptPolicyIdNext should be used to identify the new policy within the scope of the target type, identifier, direction, and policy\-source type
        	**type**\: list of    :py:class:`Ccbpttargetentry <ydk.models.cisco_ios_xe.CISCO_CBP_TARGET_MIB.CiscoCbpTargetMib.Ccbpttargettable.Ccbpttargetentry>`
        
        

        """

        _prefix = 'CISCO-CBP-TARGET-MIB'
        _revision = '2006-05-24'

        def __init__(self):
            super(CiscoCbpTargetMib.Ccbpttargettable, self).__init__()

            self.yang_name = "ccbptTargetTable"
            self.yang_parent_name = "CISCO-CBP-TARGET-MIB"

            self.ccbpttargetentry = YList(self)

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
                        super(CiscoCbpTargetMib.Ccbpttargettable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoCbpTargetMib.Ccbpttargettable, self).__setattr__(name, value)


        class Ccbpttargetentry(Entity):
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
            
            .. attribute:: ccbpttargettype  <key>
            
            	The type of target for this class\-based policy attachment. This object identifies the format of the ccbptTargetId for this entry
            	**type**\:   :py:class:`Ccbpttargettype <ydk.models.cisco_ios_xe.CISCO_CBP_TARGET_TC_MIB.Ccbpttargettype>`
            
            .. attribute:: ccbpttargetid  <key>
            
            	The target identifier for this class\-based policy attachment. For decoding the ccbptTargetId refer to the ccbptTargetType object and the CcbptTargetType description
            	**type**\:  str
            
            	**length:** 0..64
            
            .. attribute:: ccbpttargetdir  <key>
            
            	The direction relative to the ccbptTargetId for this class based policy attachment.  
            	**type**\:   :py:class:`Ccbpttargetdirection <ydk.models.cisco_ios_xe.CISCO_CBP_TARGET_TC_MIB.Ccbpttargetdirection>`
            
            .. attribute:: ccbptpolicysourcetype  <key>
            
            	The source\-type of the class\-based policy for this target. The source\-type refers to the source of the class\-based policy definition.  The intent of this object is to allow implementations to distinguish between different MIBs defining policy\-maps. 
            	**type**\:   :py:class:`Ccbptpolicysourcetype <ydk.models.cisco_ios_xe.CISCO_CBP_TARGET_TC_MIB.Ccbptpolicysourcetype>`
            
            .. attribute:: ccbptpolicyid  <key>
            
            	Unique identifier of this class\-based policy instance
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            .. attribute:: ccbptpolicyattachtime
            
            	The value of sysUpTime for the last time that the corresponding ccbptTargetStatus instance transitioned to the 'active' state.  
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ccbptpolicyinstance
            
            	Refers to the first accessible object in the policy  instance table used to manage policy instance information  for policy\-maps of this ccbptPolicySourceType.  Specific MIB tables are not mentioned here as the intent of this mapping is to allow for different implementations to  refer to their supported class\-based policy definition table without requiring support of a specific MIB module
            	**type**\:  str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: ccbptpolicymap
            
            	Refers to the first accessible object in the policy\-map definition table used to manage policy\-map information for policy\-maps for the corresponding ccbptPolicySourceType.  Specific MIB tables are not mentioned here as the intent of this mapping is to allow for different implementations to  refer to their supported class\-based policy definition table without requiring support of a specific MIB module
            	**type**\:  str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: ccbpttargetstatus
            
            	The status of the policy attachment to this target.  The value for the corresponding instance of each of the  following objects must be valid before the attachment  can be activated\:     \-ccbptTargetStorageType     \-ccbptPolicyMap  Observe that no corresponding instance of any object in  this table can be modified when the value of this object is 'active'
            	**type**\:   :py:class:`Rowstatus <ydk.models.cisco_ios_xe.SNMPv2_TC.Rowstatus>`
            
            .. attribute:: ccbpttargetstoragetype
            
            	This object indicates how the device stores the data  contained by the conceptual row.  If an instance of this object has the value 'permanent', then this MIB definition does not require the SNMP entity to allow the instance of any object in the corresponding conceptual row to be writable through the SNMP
            	**type**\:   :py:class:`Storagetype <ydk.models.cisco_ios_xe.SNMPv2_TC.Storagetype>`
            
            

            """

            _prefix = 'CISCO-CBP-TARGET-MIB'
            _revision = '2006-05-24'

            def __init__(self):
                super(CiscoCbpTargetMib.Ccbpttargettable.Ccbpttargetentry, self).__init__()

                self.yang_name = "ccbptTargetEntry"
                self.yang_parent_name = "ccbptTargetTable"

                self.ccbpttargettype = YLeaf(YType.enumeration, "ccbptTargetType")

                self.ccbpttargetid = YLeaf(YType.str, "ccbptTargetId")

                self.ccbpttargetdir = YLeaf(YType.enumeration, "ccbptTargetDir")

                self.ccbptpolicysourcetype = YLeaf(YType.enumeration, "ccbptPolicySourceType")

                self.ccbptpolicyid = YLeaf(YType.uint32, "ccbptPolicyId")

                self.ccbptpolicyattachtime = YLeaf(YType.uint32, "ccbptPolicyAttachTime")

                self.ccbptpolicyinstance = YLeaf(YType.str, "ccbptPolicyInstance")

                self.ccbptpolicymap = YLeaf(YType.str, "ccbptPolicyMap")

                self.ccbpttargetstatus = YLeaf(YType.enumeration, "ccbptTargetStatus")

                self.ccbpttargetstoragetype = YLeaf(YType.enumeration, "ccbptTargetStorageType")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("ccbpttargettype",
                                "ccbpttargetid",
                                "ccbpttargetdir",
                                "ccbptpolicysourcetype",
                                "ccbptpolicyid",
                                "ccbptpolicyattachtime",
                                "ccbptpolicyinstance",
                                "ccbptpolicymap",
                                "ccbpttargetstatus",
                                "ccbpttargetstoragetype") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoCbpTargetMib.Ccbpttargettable.Ccbpttargetentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoCbpTargetMib.Ccbpttargettable.Ccbpttargetentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.ccbpttargettype.is_set or
                    self.ccbpttargetid.is_set or
                    self.ccbpttargetdir.is_set or
                    self.ccbptpolicysourcetype.is_set or
                    self.ccbptpolicyid.is_set or
                    self.ccbptpolicyattachtime.is_set or
                    self.ccbptpolicyinstance.is_set or
                    self.ccbptpolicymap.is_set or
                    self.ccbpttargetstatus.is_set or
                    self.ccbpttargetstoragetype.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ccbpttargettype.yfilter != YFilter.not_set or
                    self.ccbpttargetid.yfilter != YFilter.not_set or
                    self.ccbpttargetdir.yfilter != YFilter.not_set or
                    self.ccbptpolicysourcetype.yfilter != YFilter.not_set or
                    self.ccbptpolicyid.yfilter != YFilter.not_set or
                    self.ccbptpolicyattachtime.yfilter != YFilter.not_set or
                    self.ccbptpolicyinstance.yfilter != YFilter.not_set or
                    self.ccbptpolicymap.yfilter != YFilter.not_set or
                    self.ccbpttargetstatus.yfilter != YFilter.not_set or
                    self.ccbpttargetstoragetype.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "ccbptTargetEntry" + "[ccbptTargetType='" + self.ccbpttargettype.get() + "']" + "[ccbptTargetId='" + self.ccbpttargetid.get() + "']" + "[ccbptTargetDir='" + self.ccbpttargetdir.get() + "']" + "[ccbptPolicySourceType='" + self.ccbptpolicysourcetype.get() + "']" + "[ccbptPolicyId='" + self.ccbptpolicyid.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-CBP-TARGET-MIB:CISCO-CBP-TARGET-MIB/ccbptTargetTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ccbpttargettype.is_set or self.ccbpttargettype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ccbpttargettype.get_name_leafdata())
                if (self.ccbpttargetid.is_set or self.ccbpttargetid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ccbpttargetid.get_name_leafdata())
                if (self.ccbpttargetdir.is_set or self.ccbpttargetdir.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ccbpttargetdir.get_name_leafdata())
                if (self.ccbptpolicysourcetype.is_set or self.ccbptpolicysourcetype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ccbptpolicysourcetype.get_name_leafdata())
                if (self.ccbptpolicyid.is_set or self.ccbptpolicyid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ccbptpolicyid.get_name_leafdata())
                if (self.ccbptpolicyattachtime.is_set or self.ccbptpolicyattachtime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ccbptpolicyattachtime.get_name_leafdata())
                if (self.ccbptpolicyinstance.is_set or self.ccbptpolicyinstance.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ccbptpolicyinstance.get_name_leafdata())
                if (self.ccbptpolicymap.is_set or self.ccbptpolicymap.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ccbptpolicymap.get_name_leafdata())
                if (self.ccbpttargetstatus.is_set or self.ccbpttargetstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ccbpttargetstatus.get_name_leafdata())
                if (self.ccbpttargetstoragetype.is_set or self.ccbpttargetstoragetype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ccbpttargetstoragetype.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ccbptTargetType" or name == "ccbptTargetId" or name == "ccbptTargetDir" or name == "ccbptPolicySourceType" or name == "ccbptPolicyId" or name == "ccbptPolicyAttachTime" or name == "ccbptPolicyInstance" or name == "ccbptPolicyMap" or name == "ccbptTargetStatus" or name == "ccbptTargetStorageType"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "ccbptTargetType"):
                    self.ccbpttargettype = value
                    self.ccbpttargettype.value_namespace = name_space
                    self.ccbpttargettype.value_namespace_prefix = name_space_prefix
                if(value_path == "ccbptTargetId"):
                    self.ccbpttargetid = value
                    self.ccbpttargetid.value_namespace = name_space
                    self.ccbpttargetid.value_namespace_prefix = name_space_prefix
                if(value_path == "ccbptTargetDir"):
                    self.ccbpttargetdir = value
                    self.ccbpttargetdir.value_namespace = name_space
                    self.ccbpttargetdir.value_namespace_prefix = name_space_prefix
                if(value_path == "ccbptPolicySourceType"):
                    self.ccbptpolicysourcetype = value
                    self.ccbptpolicysourcetype.value_namespace = name_space
                    self.ccbptpolicysourcetype.value_namespace_prefix = name_space_prefix
                if(value_path == "ccbptPolicyId"):
                    self.ccbptpolicyid = value
                    self.ccbptpolicyid.value_namespace = name_space
                    self.ccbptpolicyid.value_namespace_prefix = name_space_prefix
                if(value_path == "ccbptPolicyAttachTime"):
                    self.ccbptpolicyattachtime = value
                    self.ccbptpolicyattachtime.value_namespace = name_space
                    self.ccbptpolicyattachtime.value_namespace_prefix = name_space_prefix
                if(value_path == "ccbptPolicyInstance"):
                    self.ccbptpolicyinstance = value
                    self.ccbptpolicyinstance.value_namespace = name_space
                    self.ccbptpolicyinstance.value_namespace_prefix = name_space_prefix
                if(value_path == "ccbptPolicyMap"):
                    self.ccbptpolicymap = value
                    self.ccbptpolicymap.value_namespace = name_space
                    self.ccbptpolicymap.value_namespace_prefix = name_space_prefix
                if(value_path == "ccbptTargetStatus"):
                    self.ccbpttargetstatus = value
                    self.ccbpttargetstatus.value_namespace = name_space
                    self.ccbpttargetstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "ccbptTargetStorageType"):
                    self.ccbpttargetstoragetype = value
                    self.ccbpttargetstoragetype.value_namespace = name_space
                    self.ccbpttargetstoragetype.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.ccbpttargetentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.ccbpttargetentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "ccbptTargetTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-CBP-TARGET-MIB:CISCO-CBP-TARGET-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "ccbptTargetEntry"):
                for c in self.ccbpttargetentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoCbpTargetMib.Ccbpttargettable.Ccbpttargetentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.ccbpttargetentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "ccbptTargetEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            (self.ccbpttargetattachcfg is not None and self.ccbpttargetattachcfg.has_data()) or
            (self.ccbpttargettable is not None and self.ccbpttargettable.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.ccbpttargetattachcfg is not None and self.ccbpttargetattachcfg.has_operation()) or
            (self.ccbpttargettable is not None and self.ccbpttargettable.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "CISCO-CBP-TARGET-MIB:CISCO-CBP-TARGET-MIB" + path_buffer

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

        if (child_yang_name == "ccbptTargetAttachCfg"):
            if (self.ccbpttargetattachcfg is None):
                self.ccbpttargetattachcfg = CiscoCbpTargetMib.Ccbpttargetattachcfg()
                self.ccbpttargetattachcfg.parent = self
                self._children_name_map["ccbpttargetattachcfg"] = "ccbptTargetAttachCfg"
            return self.ccbpttargetattachcfg

        if (child_yang_name == "ccbptTargetTable"):
            if (self.ccbpttargettable is None):
                self.ccbpttargettable = CiscoCbpTargetMib.Ccbpttargettable()
                self.ccbpttargettable.parent = self
                self._children_name_map["ccbpttargettable"] = "ccbptTargetTable"
            return self.ccbpttargettable

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "ccbptTargetAttachCfg" or name == "ccbptTargetTable"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = CiscoCbpTargetMib()
        return self._top_entity

