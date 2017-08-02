""" CISCO_IPSLA_AUTOMEASURE_MIB 

This module defines the MIB for IP SLA Automation. IP SLA
Automation consists of the following\:
1. Use of grouping \- Group is an aggregation of operations 
   sharing the same type, for example UDP jitter type, with 
   common characteristics like frequency, interval etc.  
   Groups are formed by policies dictated either per customer, 
   or by service level or any other requirements.  So, for 
   example, there could be separate groups for customers named 
   Customer A, Customer B etc, or service levels named 
   Gold\-service, Silver\-service etc.  A single group will contain 
   one and only one IP SLA operation definition or reference a 
   single template.
2. Use of templates \- It has been observed that operations can be 
   configured quickly if the variants such as IP address and 
   ports can be configured separately and then combined with a 
   template  consisting of invariants.  This allows for re\-use of 
   the invariant template with various combinations of destination 
   addresses and ports, the benefits for which are multiplied when 
   considering groupings.
3. Auto operations \- With this feature the software will try to 
   automatically kickstart operations by making intelligent 
   assumptions.  For example, if no specific operation is referenced 
   by the group configuration then an ICMP jitter operation is 
   assumed by default.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class CiscoIpslaAutomeasureMib(Entity):
    """
    
    
    .. attribute:: cipslaautogroupdesttable
    
    	A table contains the list of destination IP addresses and ports associated to the auto measure group destination name
    	**type**\:   :py:class:`Cipslaautogroupdesttable <ydk.models.cisco_ios_xe.CISCO_IPSLA_AUTOMEASURE_MIB.CiscoIpslaAutomeasureMib.Cipslaautogroupdesttable>`
    
    .. attribute:: cipslaautogroupschedtable
    
    	A table of group scheduling definitions
    	**type**\:   :py:class:`Cipslaautogroupschedtable <ydk.models.cisco_ios_xe.CISCO_IPSLA_AUTOMEASURE_MIB.CiscoIpslaAutomeasureMib.Cipslaautogroupschedtable>`
    
    .. attribute:: cipslaautogrouptable
    
    	A table that contains IP SLA auto measure group definitions
    	**type**\:   :py:class:`Cipslaautogrouptable <ydk.models.cisco_ios_xe.CISCO_IPSLA_AUTOMEASURE_MIB.CiscoIpslaAutomeasureMib.Cipslaautogrouptable>`
    
    .. attribute:: cipslareacttable
    
    	A table that contains reaction configurations for templates. Each conceptual row in cipslaReactTable corresponds  to a reaction configured for one template.  Each template can have multiple reactions and hence there can be  multiple rows for a particular template. Different template types can have different reactions. The reaction type is  specified as cipslaReactVar based upon template type as some  reaction types are applicable just for specific template types
    	**type**\:   :py:class:`Cipslareacttable <ydk.models.cisco_ios_xe.CISCO_IPSLA_AUTOMEASURE_MIB.CiscoIpslaAutomeasureMib.Cipslareacttable>`
    
    

    """

    _prefix = 'CISCO-IPSLA-AUTOMEASURE-MIB'
    _revision = '2007-06-13'

    def __init__(self):
        super(CiscoIpslaAutomeasureMib, self).__init__()
        self._top_entity = None

        self.yang_name = "CISCO-IPSLA-AUTOMEASURE-MIB"
        self.yang_parent_name = "CISCO-IPSLA-AUTOMEASURE-MIB"

        self.cipslaautogroupdesttable = CiscoIpslaAutomeasureMib.Cipslaautogroupdesttable()
        self.cipslaautogroupdesttable.parent = self
        self._children_name_map["cipslaautogroupdesttable"] = "cipslaAutoGroupDestTable"
        self._children_yang_names.add("cipslaAutoGroupDestTable")

        self.cipslaautogroupschedtable = CiscoIpslaAutomeasureMib.Cipslaautogroupschedtable()
        self.cipslaautogroupschedtable.parent = self
        self._children_name_map["cipslaautogroupschedtable"] = "cipslaAutoGroupSchedTable"
        self._children_yang_names.add("cipslaAutoGroupSchedTable")

        self.cipslaautogrouptable = CiscoIpslaAutomeasureMib.Cipslaautogrouptable()
        self.cipslaautogrouptable.parent = self
        self._children_name_map["cipslaautogrouptable"] = "cipslaAutoGroupTable"
        self._children_yang_names.add("cipslaAutoGroupTable")

        self.cipslareacttable = CiscoIpslaAutomeasureMib.Cipslareacttable()
        self.cipslareacttable.parent = self
        self._children_name_map["cipslareacttable"] = "cipslaReactTable"
        self._children_yang_names.add("cipslaReactTable")


    class Cipslaautogrouptable(Entity):
        """
        A table that contains IP SLA auto measure group definitions.
        
        .. attribute:: cipslaautogroupentry
        
        	An entry containing the configurations for a particular auto measure group
        	**type**\: list of    :py:class:`Cipslaautogroupentry <ydk.models.cisco_ios_xe.CISCO_IPSLA_AUTOMEASURE_MIB.CiscoIpslaAutomeasureMib.Cipslaautogrouptable.Cipslaautogroupentry>`
        
        

        """

        _prefix = 'CISCO-IPSLA-AUTOMEASURE-MIB'
        _revision = '2007-06-13'

        def __init__(self):
            super(CiscoIpslaAutomeasureMib.Cipslaautogrouptable, self).__init__()

            self.yang_name = "cipslaAutoGroupTable"
            self.yang_parent_name = "CISCO-IPSLA-AUTOMEASURE-MIB"

            self.cipslaautogroupentry = YList(self)

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
                        super(CiscoIpslaAutomeasureMib.Cipslaautogrouptable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoIpslaAutomeasureMib.Cipslaautogrouptable, self).__setattr__(name, value)


        class Cipslaautogroupentry(Entity):
            """
            An entry containing the configurations for a particular
            auto measure group.
            
            .. attribute:: cipslaautogroupname  <key>
            
            	A group name which is used by a management application to identify the group
            	**type**\:  str
            
            	**length:** 1..64
            
            .. attribute:: cipslaautogroupaddestipageout
            
            	This object represents the ageout time for the discovered end point.  If the end point becomes inactive for the period  of ageout time, the end point will be removed from the  discovered end point list.  When the value of cipslaAutoGroupDestIPADEnable is  'false', the value of this object has no effect
            	**type**\:  int
            
            	**range:** 0..65536
            
            	**units**\: seconds
            
            .. attribute:: cipslaautogroupaddestport
            
            	This object represents the destination port number for auto discovery use
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: cipslaautogroupadmeasureretry
            
            	This object specifies number of measurement retries to be attempted for the discovered end point after the  connection to the end point is broken. If there is no  re\-registration message received, the end point will be  in inactive state.  When the value of cipslaAutoGroupDestIPADEnable is  'false', the value of this object has no effect
            	**type**\:  int
            
            	**range:** 1..65536
            
            .. attribute:: cipslaautogroupdescription
            
            	This field is used to provide description for the group
            	**type**\:  str
            
            	**length:** 0..128
            
            .. attribute:: cipslaautogroupdestinationname
            
            	This object refers to the cipslaAutoGroupDestName in cipslaAutoGroupDestTable. If the name entered  is not present in cipslaAutoGroupDestTable, then when  group is scheduled, no ip sla operations will be created
            	**type**\:  str
            
            	**length:** 0..64
            
            .. attribute:: cipslaautogroupdestipadenable
            
            	When this object is set to true, destination IP address is populated through auto\-discovery
            	**type**\:  bool
            
            .. attribute:: cipslaautogroupopertemplatename
            
            	A string which is used by a management application to identify the template which is associated with the group. Depends on cipslaAutoGroupOperType, this object refers to cipslaIcmpEchoTmplName in cipslaIcmpEchoTmplTable, or cipslaUdpEchoTmplName in cipslaUdpEchoTmplTable, or cipslaTcpConnTmplName in cipslaTcpConnTmplTable, or cipslaIcmpJitterTmplName in cipslaIcmpJitterTmplTable, or ciscoIpSlaUdpJitterTmplName in ciscoIpSlaUdpJitterTmplTable
            	**type**\:  str
            
            	**length:** 0..64
            
            .. attribute:: cipslaautogroupopertype
            
            	This object specifies the type of IP SLA operation. When operation type is not ICMP jitter, then  cipslaAutoGroupOperTemplateName must be specified
            	**type**\:   :py:class:`Ipslaopertype <ydk.models.cisco_ios_xe.CISCO_IPSLA_TC_MIB.Ipslaopertype>`
            
            .. attribute:: cipslaautogroupqosenable
            
            	When this object is set to true, QoS is enabled for this group and this group is linked to policy map. The  restriction is that after QoS is enabled, it can not be  disabled for this group
            	**type**\:  bool
            
            .. attribute:: cipslaautogrouprowstatus
            
            	The status of the conceptual group control row.  When the status is active, the other writable objects may be modified unless the scheduler with name  specified by cipslaAutoGroupSchedulerId is scheduled
            	**type**\:   :py:class:`Rowstatus <ydk.models.cisco_ios_xe.SNMPv2_TC.Rowstatus>`
            
            .. attribute:: cipslaautogroupschedulerid
            
            	This object refers to the cipslaAutoGroupSchedId in cipslaAutoGroupSchedTable, and is used to schedule  this group
            	**type**\:  str
            
            	**length:** 0..64
            
            .. attribute:: cipslaautogroupstoragetype
            
            	The storage type of this conceptual row
            	**type**\:   :py:class:`Storagetype <ydk.models.cisco_ios_xe.SNMPv2_TC.Storagetype>`
            
            

            """

            _prefix = 'CISCO-IPSLA-AUTOMEASURE-MIB'
            _revision = '2007-06-13'

            def __init__(self):
                super(CiscoIpslaAutomeasureMib.Cipslaautogrouptable.Cipslaautogroupentry, self).__init__()

                self.yang_name = "cipslaAutoGroupEntry"
                self.yang_parent_name = "cipslaAutoGroupTable"

                self.cipslaautogroupname = YLeaf(YType.str, "cipslaAutoGroupName")

                self.cipslaautogroupaddestipageout = YLeaf(YType.uint32, "cipslaAutoGroupADDestIPAgeout")

                self.cipslaautogroupaddestport = YLeaf(YType.uint16, "cipslaAutoGroupADDestPort")

                self.cipslaautogroupadmeasureretry = YLeaf(YType.uint32, "cipslaAutoGroupADMeasureRetry")

                self.cipslaautogroupdescription = YLeaf(YType.str, "cipslaAutoGroupDescription")

                self.cipslaautogroupdestinationname = YLeaf(YType.str, "cipslaAutoGroupDestinationName")

                self.cipslaautogroupdestipadenable = YLeaf(YType.boolean, "cipslaAutoGroupDestIPADEnable")

                self.cipslaautogroupopertemplatename = YLeaf(YType.str, "cipslaAutoGroupOperTemplateName")

                self.cipslaautogroupopertype = YLeaf(YType.enumeration, "cipslaAutoGroupOperType")

                self.cipslaautogroupqosenable = YLeaf(YType.boolean, "cipslaAutoGroupQoSEnable")

                self.cipslaautogrouprowstatus = YLeaf(YType.enumeration, "cipslaAutoGroupRowStatus")

                self.cipslaautogroupschedulerid = YLeaf(YType.str, "cipslaAutoGroupSchedulerId")

                self.cipslaautogroupstoragetype = YLeaf(YType.enumeration, "cipslaAutoGroupStorageType")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("cipslaautogroupname",
                                "cipslaautogroupaddestipageout",
                                "cipslaautogroupaddestport",
                                "cipslaautogroupadmeasureretry",
                                "cipslaautogroupdescription",
                                "cipslaautogroupdestinationname",
                                "cipslaautogroupdestipadenable",
                                "cipslaautogroupopertemplatename",
                                "cipslaautogroupopertype",
                                "cipslaautogroupqosenable",
                                "cipslaautogrouprowstatus",
                                "cipslaautogroupschedulerid",
                                "cipslaautogroupstoragetype") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoIpslaAutomeasureMib.Cipslaautogrouptable.Cipslaautogroupentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoIpslaAutomeasureMib.Cipslaautogrouptable.Cipslaautogroupentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.cipslaautogroupname.is_set or
                    self.cipslaautogroupaddestipageout.is_set or
                    self.cipslaautogroupaddestport.is_set or
                    self.cipslaautogroupadmeasureretry.is_set or
                    self.cipslaautogroupdescription.is_set or
                    self.cipslaautogroupdestinationname.is_set or
                    self.cipslaautogroupdestipadenable.is_set or
                    self.cipslaautogroupopertemplatename.is_set or
                    self.cipslaautogroupopertype.is_set or
                    self.cipslaautogroupqosenable.is_set or
                    self.cipslaautogrouprowstatus.is_set or
                    self.cipslaautogroupschedulerid.is_set or
                    self.cipslaautogroupstoragetype.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.cipslaautogroupname.yfilter != YFilter.not_set or
                    self.cipslaautogroupaddestipageout.yfilter != YFilter.not_set or
                    self.cipslaautogroupaddestport.yfilter != YFilter.not_set or
                    self.cipslaautogroupadmeasureretry.yfilter != YFilter.not_set or
                    self.cipslaautogroupdescription.yfilter != YFilter.not_set or
                    self.cipslaautogroupdestinationname.yfilter != YFilter.not_set or
                    self.cipslaautogroupdestipadenable.yfilter != YFilter.not_set or
                    self.cipslaautogroupopertemplatename.yfilter != YFilter.not_set or
                    self.cipslaautogroupopertype.yfilter != YFilter.not_set or
                    self.cipslaautogroupqosenable.yfilter != YFilter.not_set or
                    self.cipslaautogrouprowstatus.yfilter != YFilter.not_set or
                    self.cipslaautogroupschedulerid.yfilter != YFilter.not_set or
                    self.cipslaautogroupstoragetype.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cipslaAutoGroupEntry" + "[cipslaAutoGroupName='" + self.cipslaautogroupname.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-IPSLA-AUTOMEASURE-MIB:CISCO-IPSLA-AUTOMEASURE-MIB/cipslaAutoGroupTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.cipslaautogroupname.is_set or self.cipslaautogroupname.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipslaautogroupname.get_name_leafdata())
                if (self.cipslaautogroupaddestipageout.is_set or self.cipslaautogroupaddestipageout.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipslaautogroupaddestipageout.get_name_leafdata())
                if (self.cipslaautogroupaddestport.is_set or self.cipslaautogroupaddestport.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipslaautogroupaddestport.get_name_leafdata())
                if (self.cipslaautogroupadmeasureretry.is_set or self.cipslaautogroupadmeasureretry.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipslaautogroupadmeasureretry.get_name_leafdata())
                if (self.cipslaautogroupdescription.is_set or self.cipslaautogroupdescription.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipslaautogroupdescription.get_name_leafdata())
                if (self.cipslaautogroupdestinationname.is_set or self.cipslaautogroupdestinationname.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipslaautogroupdestinationname.get_name_leafdata())
                if (self.cipslaautogroupdestipadenable.is_set or self.cipslaautogroupdestipadenable.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipslaautogroupdestipadenable.get_name_leafdata())
                if (self.cipslaautogroupopertemplatename.is_set or self.cipslaautogroupopertemplatename.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipslaautogroupopertemplatename.get_name_leafdata())
                if (self.cipslaautogroupopertype.is_set or self.cipslaautogroupopertype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipslaautogroupopertype.get_name_leafdata())
                if (self.cipslaautogroupqosenable.is_set or self.cipslaautogroupqosenable.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipslaautogroupqosenable.get_name_leafdata())
                if (self.cipslaautogrouprowstatus.is_set or self.cipslaautogrouprowstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipslaautogrouprowstatus.get_name_leafdata())
                if (self.cipslaautogroupschedulerid.is_set or self.cipslaautogroupschedulerid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipslaautogroupschedulerid.get_name_leafdata())
                if (self.cipslaautogroupstoragetype.is_set or self.cipslaautogroupstoragetype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipslaautogroupstoragetype.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cipslaAutoGroupName" or name == "cipslaAutoGroupADDestIPAgeout" or name == "cipslaAutoGroupADDestPort" or name == "cipslaAutoGroupADMeasureRetry" or name == "cipslaAutoGroupDescription" or name == "cipslaAutoGroupDestinationName" or name == "cipslaAutoGroupDestIPADEnable" or name == "cipslaAutoGroupOperTemplateName" or name == "cipslaAutoGroupOperType" or name == "cipslaAutoGroupQoSEnable" or name == "cipslaAutoGroupRowStatus" or name == "cipslaAutoGroupSchedulerId" or name == "cipslaAutoGroupStorageType"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "cipslaAutoGroupName"):
                    self.cipslaautogroupname = value
                    self.cipslaautogroupname.value_namespace = name_space
                    self.cipslaautogroupname.value_namespace_prefix = name_space_prefix
                if(value_path == "cipslaAutoGroupADDestIPAgeout"):
                    self.cipslaautogroupaddestipageout = value
                    self.cipslaautogroupaddestipageout.value_namespace = name_space
                    self.cipslaautogroupaddestipageout.value_namespace_prefix = name_space_prefix
                if(value_path == "cipslaAutoGroupADDestPort"):
                    self.cipslaautogroupaddestport = value
                    self.cipslaautogroupaddestport.value_namespace = name_space
                    self.cipslaautogroupaddestport.value_namespace_prefix = name_space_prefix
                if(value_path == "cipslaAutoGroupADMeasureRetry"):
                    self.cipslaautogroupadmeasureretry = value
                    self.cipslaautogroupadmeasureretry.value_namespace = name_space
                    self.cipslaautogroupadmeasureretry.value_namespace_prefix = name_space_prefix
                if(value_path == "cipslaAutoGroupDescription"):
                    self.cipslaautogroupdescription = value
                    self.cipslaautogroupdescription.value_namespace = name_space
                    self.cipslaautogroupdescription.value_namespace_prefix = name_space_prefix
                if(value_path == "cipslaAutoGroupDestinationName"):
                    self.cipslaautogroupdestinationname = value
                    self.cipslaautogroupdestinationname.value_namespace = name_space
                    self.cipslaautogroupdestinationname.value_namespace_prefix = name_space_prefix
                if(value_path == "cipslaAutoGroupDestIPADEnable"):
                    self.cipslaautogroupdestipadenable = value
                    self.cipslaautogroupdestipadenable.value_namespace = name_space
                    self.cipslaautogroupdestipadenable.value_namespace_prefix = name_space_prefix
                if(value_path == "cipslaAutoGroupOperTemplateName"):
                    self.cipslaautogroupopertemplatename = value
                    self.cipslaautogroupopertemplatename.value_namespace = name_space
                    self.cipslaautogroupopertemplatename.value_namespace_prefix = name_space_prefix
                if(value_path == "cipslaAutoGroupOperType"):
                    self.cipslaautogroupopertype = value
                    self.cipslaautogroupopertype.value_namespace = name_space
                    self.cipslaautogroupopertype.value_namespace_prefix = name_space_prefix
                if(value_path == "cipslaAutoGroupQoSEnable"):
                    self.cipslaautogroupqosenable = value
                    self.cipslaautogroupqosenable.value_namespace = name_space
                    self.cipslaautogroupqosenable.value_namespace_prefix = name_space_prefix
                if(value_path == "cipslaAutoGroupRowStatus"):
                    self.cipslaautogrouprowstatus = value
                    self.cipslaautogrouprowstatus.value_namespace = name_space
                    self.cipslaautogrouprowstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "cipslaAutoGroupSchedulerId"):
                    self.cipslaautogroupschedulerid = value
                    self.cipslaautogroupschedulerid.value_namespace = name_space
                    self.cipslaautogroupschedulerid.value_namespace_prefix = name_space_prefix
                if(value_path == "cipslaAutoGroupStorageType"):
                    self.cipslaautogroupstoragetype = value
                    self.cipslaautogroupstoragetype.value_namespace = name_space
                    self.cipslaautogroupstoragetype.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cipslaautogroupentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cipslaautogroupentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cipslaAutoGroupTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-IPSLA-AUTOMEASURE-MIB:CISCO-IPSLA-AUTOMEASURE-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cipslaAutoGroupEntry"):
                for c in self.cipslaautogroupentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoIpslaAutomeasureMib.Cipslaautogrouptable.Cipslaautogroupentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cipslaautogroupentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cipslaAutoGroupEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Cipslaautogroupdesttable(Entity):
        """
        A table contains the list of destination IP
        addresses and ports associated to the auto measure
        group destination name.
        
        .. attribute:: cipslaautogroupdestentry
        
        	An entry containing the destination IP addresses and port configurations associated to auto measure group destination name
        	**type**\: list of    :py:class:`Cipslaautogroupdestentry <ydk.models.cisco_ios_xe.CISCO_IPSLA_AUTOMEASURE_MIB.CiscoIpslaAutomeasureMib.Cipslaautogroupdesttable.Cipslaautogroupdestentry>`
        
        

        """

        _prefix = 'CISCO-IPSLA-AUTOMEASURE-MIB'
        _revision = '2007-06-13'

        def __init__(self):
            super(CiscoIpslaAutomeasureMib.Cipslaautogroupdesttable, self).__init__()

            self.yang_name = "cipslaAutoGroupDestTable"
            self.yang_parent_name = "CISCO-IPSLA-AUTOMEASURE-MIB"

            self.cipslaautogroupdestentry = YList(self)

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
                        super(CiscoIpslaAutomeasureMib.Cipslaautogroupdesttable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoIpslaAutomeasureMib.Cipslaautogroupdesttable, self).__setattr__(name, value)


        class Cipslaautogroupdestentry(Entity):
            """
            An entry containing the destination IP addresses
            and port configurations associated to auto measure
            group destination name.
            
            .. attribute:: cipslaautogroupdestname  <key>
            
            	This is the name for an auto measure group destination
            	**type**\:  str
            
            	**length:** 1..64
            
            .. attribute:: cipslaautogroupdestipaddrtype  <key>
            
            	The type of the internet address of a destination for an auto measure group
            	**type**\:   :py:class:`Inetaddresstype <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.Inetaddresstype>`
            
            .. attribute:: cipslaautogroupdestipaddr  <key>
            
            	The internet address of a destination for an auto measure group. The type of this address is determined by the value of cipslaAutoGroupDestIpAddrType
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: cipslaautogroupdestport  <key>
            
            	This object represents the destination port number. For ICMP echo and ICMP jitter, the suggested value is  '0'
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: cipslaautogroupdestrowstatus
            
            	The status of the conceptual destination table control row. No other objects in this row need to be set before this object can become active.  During 'destroy', when cipslaAutoGroupDestIpAddr is specified  as '0.0.0.0' and cipslaAutoGroupDestPort is specified as '0',  then all the rows with same cipslaAutoGroupDestName will be  deleted
            	**type**\:   :py:class:`Rowstatus <ydk.models.cisco_ios_xe.SNMPv2_TC.Rowstatus>`
            
            .. attribute:: cipslaautogroupdeststoragetype
            
            	The storage type of this conceptual row.  By default the entry will be saved into non\-volatile memory
            	**type**\:   :py:class:`Storagetype <ydk.models.cisco_ios_xe.SNMPv2_TC.Storagetype>`
            
            

            """

            _prefix = 'CISCO-IPSLA-AUTOMEASURE-MIB'
            _revision = '2007-06-13'

            def __init__(self):
                super(CiscoIpslaAutomeasureMib.Cipslaautogroupdesttable.Cipslaautogroupdestentry, self).__init__()

                self.yang_name = "cipslaAutoGroupDestEntry"
                self.yang_parent_name = "cipslaAutoGroupDestTable"

                self.cipslaautogroupdestname = YLeaf(YType.str, "cipslaAutoGroupDestName")

                self.cipslaautogroupdestipaddrtype = YLeaf(YType.enumeration, "cipslaAutoGroupDestIpAddrType")

                self.cipslaautogroupdestipaddr = YLeaf(YType.str, "cipslaAutoGroupDestIpAddr")

                self.cipslaautogroupdestport = YLeaf(YType.uint16, "cipslaAutoGroupDestPort")

                self.cipslaautogroupdestrowstatus = YLeaf(YType.enumeration, "cipslaAutoGroupDestRowStatus")

                self.cipslaautogroupdeststoragetype = YLeaf(YType.enumeration, "cipslaAutoGroupDestStorageType")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("cipslaautogroupdestname",
                                "cipslaautogroupdestipaddrtype",
                                "cipslaautogroupdestipaddr",
                                "cipslaautogroupdestport",
                                "cipslaautogroupdestrowstatus",
                                "cipslaautogroupdeststoragetype") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoIpslaAutomeasureMib.Cipslaautogroupdesttable.Cipslaautogroupdestentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoIpslaAutomeasureMib.Cipslaautogroupdesttable.Cipslaautogroupdestentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.cipslaautogroupdestname.is_set or
                    self.cipslaautogroupdestipaddrtype.is_set or
                    self.cipslaautogroupdestipaddr.is_set or
                    self.cipslaautogroupdestport.is_set or
                    self.cipslaautogroupdestrowstatus.is_set or
                    self.cipslaautogroupdeststoragetype.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.cipslaautogroupdestname.yfilter != YFilter.not_set or
                    self.cipslaautogroupdestipaddrtype.yfilter != YFilter.not_set or
                    self.cipslaautogroupdestipaddr.yfilter != YFilter.not_set or
                    self.cipslaautogroupdestport.yfilter != YFilter.not_set or
                    self.cipslaautogroupdestrowstatus.yfilter != YFilter.not_set or
                    self.cipslaautogroupdeststoragetype.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cipslaAutoGroupDestEntry" + "[cipslaAutoGroupDestName='" + self.cipslaautogroupdestname.get() + "']" + "[cipslaAutoGroupDestIpAddrType='" + self.cipslaautogroupdestipaddrtype.get() + "']" + "[cipslaAutoGroupDestIpAddr='" + self.cipslaautogroupdestipaddr.get() + "']" + "[cipslaAutoGroupDestPort='" + self.cipslaautogroupdestport.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-IPSLA-AUTOMEASURE-MIB:CISCO-IPSLA-AUTOMEASURE-MIB/cipslaAutoGroupDestTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.cipslaautogroupdestname.is_set or self.cipslaautogroupdestname.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipslaautogroupdestname.get_name_leafdata())
                if (self.cipslaautogroupdestipaddrtype.is_set or self.cipslaautogroupdestipaddrtype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipslaautogroupdestipaddrtype.get_name_leafdata())
                if (self.cipslaautogroupdestipaddr.is_set or self.cipslaautogroupdestipaddr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipslaautogroupdestipaddr.get_name_leafdata())
                if (self.cipslaautogroupdestport.is_set or self.cipslaautogroupdestport.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipslaautogroupdestport.get_name_leafdata())
                if (self.cipslaautogroupdestrowstatus.is_set or self.cipslaautogroupdestrowstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipslaautogroupdestrowstatus.get_name_leafdata())
                if (self.cipslaautogroupdeststoragetype.is_set or self.cipslaautogroupdeststoragetype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipslaautogroupdeststoragetype.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cipslaAutoGroupDestName" or name == "cipslaAutoGroupDestIpAddrType" or name == "cipslaAutoGroupDestIpAddr" or name == "cipslaAutoGroupDestPort" or name == "cipslaAutoGroupDestRowStatus" or name == "cipslaAutoGroupDestStorageType"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "cipslaAutoGroupDestName"):
                    self.cipslaautogroupdestname = value
                    self.cipslaautogroupdestname.value_namespace = name_space
                    self.cipslaautogroupdestname.value_namespace_prefix = name_space_prefix
                if(value_path == "cipslaAutoGroupDestIpAddrType"):
                    self.cipslaautogroupdestipaddrtype = value
                    self.cipslaautogroupdestipaddrtype.value_namespace = name_space
                    self.cipslaautogroupdestipaddrtype.value_namespace_prefix = name_space_prefix
                if(value_path == "cipslaAutoGroupDestIpAddr"):
                    self.cipslaautogroupdestipaddr = value
                    self.cipslaautogroupdestipaddr.value_namespace = name_space
                    self.cipslaautogroupdestipaddr.value_namespace_prefix = name_space_prefix
                if(value_path == "cipslaAutoGroupDestPort"):
                    self.cipslaautogroupdestport = value
                    self.cipslaautogroupdestport.value_namespace = name_space
                    self.cipslaautogroupdestport.value_namespace_prefix = name_space_prefix
                if(value_path == "cipslaAutoGroupDestRowStatus"):
                    self.cipslaautogroupdestrowstatus = value
                    self.cipslaautogroupdestrowstatus.value_namespace = name_space
                    self.cipslaautogroupdestrowstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "cipslaAutoGroupDestStorageType"):
                    self.cipslaautogroupdeststoragetype = value
                    self.cipslaautogroupdeststoragetype.value_namespace = name_space
                    self.cipslaautogroupdeststoragetype.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cipslaautogroupdestentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cipslaautogroupdestentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cipslaAutoGroupDestTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-IPSLA-AUTOMEASURE-MIB:CISCO-IPSLA-AUTOMEASURE-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cipslaAutoGroupDestEntry"):
                for c in self.cipslaautogroupdestentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoIpslaAutomeasureMib.Cipslaautogroupdesttable.Cipslaautogroupdestentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cipslaautogroupdestentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cipslaAutoGroupDestEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Cipslareacttable(Entity):
        """
        A table that contains reaction configurations for templates.
        Each conceptual row in cipslaReactTable corresponds 
        to a reaction configured for one template.
        
        Each template can have multiple reactions and hence there can be 
        multiple rows for a particular template. Different template
        types can have different reactions. The reaction type is 
        specified as cipslaReactVar based upon template type as some 
        reaction types are applicable just for specific template types.
        
        .. attribute:: cipslareactentry
        
        	A base list of objects that define a conceptual reaction configuration control row
        	**type**\: list of    :py:class:`Cipslareactentry <ydk.models.cisco_ios_xe.CISCO_IPSLA_AUTOMEASURE_MIB.CiscoIpslaAutomeasureMib.Cipslareacttable.Cipslareactentry>`
        
        

        """

        _prefix = 'CISCO-IPSLA-AUTOMEASURE-MIB'
        _revision = '2007-06-13'

        def __init__(self):
            super(CiscoIpslaAutomeasureMib.Cipslareacttable, self).__init__()

            self.yang_name = "cipslaReactTable"
            self.yang_parent_name = "CISCO-IPSLA-AUTOMEASURE-MIB"

            self.cipslareactentry = YList(self)

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
                        super(CiscoIpslaAutomeasureMib.Cipslareacttable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoIpslaAutomeasureMib.Cipslareacttable, self).__setattr__(name, value)


        class Cipslareactentry(Entity):
            """
            A base list of objects that define a conceptual reaction
            configuration control row.
            
            .. attribute:: cipslaautogroupopertype  <key>
            
            	
            	**type**\:   :py:class:`Ipslaopertype <ydk.models.cisco_ios_xe.CISCO_IPSLA_TC_MIB.Ipslaopertype>`
            
            .. attribute:: cipslareactconfigindex  <key>
            
            	This object along with cipslaAutoGroupOperType and cipslaAutoGroupOperTemplateName identifies a particular reaction\-configuration for one IP SLA  template.  This number is persistent across reboots
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            .. attribute:: cipslaautogroupopertemplatename  <key>
            
            	
            	**type**\:  str
            
            	**length:** 0..64
            
            	**refers to**\:  :py:class:`cipslaautogroupopertemplatename <ydk.models.cisco_ios_xe.CISCO_IPSLA_AUTOMEASURE_MIB.CiscoIpslaAutomeasureMib.Cipslaautogrouptable.Cipslaautogroupentry>`
            
            .. attribute:: cipslareactactiontype
            
            	Specifies what type, if any, of reaction to generate if one of the watched (reaction\-configuration ) conditions is satisfied\:  none(1)                \- no reaction is generated notificationOnly(2)    \- a notification is generated
            	**type**\:   :py:class:`Cipslareactactiontype <ydk.models.cisco_ios_xe.CISCO_IPSLA_AUTOMEASURE_MIB.CiscoIpslaAutomeasureMib.Cipslareacttable.Cipslareactentry.Cipslareactactiontype>`
            
            .. attribute:: cipslareactrowstatus
            
            	This objects indicates the status of the conceptual Reaction Control Row.   When this object moves to active state, the conceptual row  is monitored and notifications are generated when threshold  violation takes place.  In order for this object to become active cipslaReactVar must be defined. All other objects assume default values.  When the  status is active, the following objects in that row can be  modified.  cipslaReactThresholdType,  cipslaReactActionType,  cipslaReactThresholdRising,  cipslaReactThresholdFalling,  cipslaReactThresholdCountX,  cipslaReactThresholdCountY,  cipslaReactStorageType  This object can be set to 'destroy' from any value at any time. When this object is set to 'destroy' no reaction configuration would exist. The reaction configuration for the template is  removed
            	**type**\:   :py:class:`Rowstatus <ydk.models.cisco_ios_xe.SNMPv2_TC.Rowstatus>`
            
            .. attribute:: cipslareactstoragetype
            
            	The storage type of this conceptual row.  By default the entry will be saved into non\-volatile memory
            	**type**\:   :py:class:`Storagetype <ydk.models.cisco_ios_xe.SNMPv2_TC.Storagetype>`
            
            .. attribute:: cipslareactthresholdcountx
            
            	If cipslaReactThresholdType value is 'xOfy', this object defines the 'x' value.  If cipslaReactThresholdType value is 'consecutive' this object defines the number of consecutive occurrences that needs threshold violation before setting  cipslaReactOccurred as true.  If cipslaReactThresholdType value is 'average' this object defines the number of samples that needs be considered for calculating average.  This object has no meaning if cipslaReactThresholdType has value of 'never' and 'immediate'
            	**type**\:  int
            
            	**range:** 1..16
            
            .. attribute:: cipslareactthresholdcounty
            
            	This object defines the 'y' value of the xOfy condition if cipslaReactThresholdType is 'xOfy'. The default for the  'y' value is 5.  For other values of cipslaReactThresholdType, this object is not applicable
            	**type**\:  int
            
            	**range:** 1..16
            
            .. attribute:: cipslareactthresholdfalling
            
            	This object defines a lower threshold limit. If the value ( e.g rtt, jitterAvg, packetLossSD etc ) falls below this limit and if the condition specified in cipslaReactThresholdType is satisfied, a notification  is generated. This object value can not bigger than cipslaReactThresholdRising value.  Default value of cipslaReactThresholdFalling    'rtt' is 3000    'jitterAvg' is 100.    'jitterSDAvg' is 100.    'jitterDSAvg' 100.    'packetLossSD' is 10000.    'packetLossDS' is 10000.    'mos' is 500.    'icpif' is 93.    'packetMIA' is 10000.    'packetLateArrival' is 10000.    'packetOutOfSequence' is 10000.    'maxOfPositiveSD' is 10000.    'maxOfNegativeSD' is 10000.    'maxOfPositiveDS' is 10000.    'maxOfNegativeDS' is 10000.    'successivePacketLoss' is 1000.    'maxOfLatencyDS' is 3000.    'maxOfLatencySD' is 3000.    'latencyDSAvg' is 3000.    'latencySDAvg' is 3000.    'packetLoss' is 10000.  This object is not applicable if the cipslaReactVar is 'timeout', 'connectionLoss' or 'verifyError'. For 'timeout', 'connectionLoss' and 'verifyError', default value of cipslaReactThresholdFalling will be 0
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cipslareactthresholdrising
            
            	This object defines the higher threshold limit. If the value ( e.g rtt, jitterAvg, packetLossSD etc ) rises above this limit and if the condition specified in cipslaReactThresholdType is satisfied, a notification is  generated.  Default value of cipslaReactThresholdRising for    'rtt' is 5000    'jitterAvg' is 100.    'jitterSDAvg' is 100.    'jitterDSAvg' 100.    'packetLossSD' is 10000.    'packetLossDS' is 10000.    'mos' is 500.    'icpif' is 93.    'packetMIA' is 10000.    'packetLateArrival' is 10000.    'packetOutOfSequence' is 10000.    'maxOfPositiveSD' is 10000.    'maxOfNegativeSD' is 10000.    'maxOfPositiveDS' is 10000.    'maxOfNegativeDS' is 10000.    'successivePacketLoss' is 1000.    'maxOfLatencyDS' is 5000.    'maxOfLatencySD' is 5000.    'latencyDSAvg' is 5000.    'latencySDAvg' is 5000.    'packetLoss' is 10000.  This object is not applicable if the cipslaReactVar is 'timeout', 'connectionLoss' or 'verifyError'. For 'timeout', 'connectionLoss' and 'verifyError' default value of  cipslaReactThresholdRising will be 0
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cipslareactthresholdtype
            
            	This object specifies the conditions under which a notification ( trap ) is sent. The rttMonReactOccurred object defined in rttMonReactTable in CISCO\-RTTMON\-MIB will change accordingly\:  never(1)       \- rttMonReactOccurred is never set  immediate(2)   \- rttMonReactOccurred is set to 'true' when the                  value of parameter for which reaction is                  configured ( e.g rtt, jitterAvg, packetLossSD,                  mos etc ) violates the threshold.                  Conversely, rttMonReactOccurred is set to 'false'                  when the parameter ( e.g rtt, jitterAvg,                  packetLossSD, mos etc ) is below the threshold                  limits.  consecutive(3) \- rttMonReactOccurred is set to true when the value                  of parameter for which reaction is configured                  ( e.g rtt, jitterAvg, packetLossSD, mos etc )                  violates the threshold for configured consecutive                  times.                  Conversely, rttMonReactOccurred is set to false                  when the value of parameter ( e.g rtt, jitterAvg                  packetLossSD, mos etc ) is below the threshold                  limits for the same number of consecutive                  operations.  xOfy(4)        \- rttMonReactOccurred is set to true when x                  ( as specified by cipslaReactThresholdCountX )                  out of the last y ( as specified by                  cipslaReacthresholdCountY ) times the value of                  parameter for which the reaction is configured                  ( e.g rtt, jitterAvg, packetLossSD, mos etc )                  violates the threshold.                  Conversely, it is set to false when x, out of the                  last y times the value of parameter                  ( e.g rtt, jitterAvg, packetLossSD, mos ) is                  below the threshold limits.                  NOTE\: If x > y, this will never                       generate a reaction.  average(5)    \- rttMonReactOccurred is set to true when the                 average ( cipslaReactThresholdCountX times )                 value of parameter for which reaction is                  configured ( e.g rtt, jitterAvg, packetLossSD,                 mos etc ) violates the threshold condition.                 Conversely, it is set to false when the                 average value of parameter ( e.g rtt, jitterAvg,                 packetLossSD, mos etc ) is below the threshold                 limits.  If this value is changed by a management station, rttMonReactOccurred is set to false, but no reaction is generated if the prior value of rttMonReactOccurred was true
            	**type**\:   :py:class:`Cipslareactthresholdtype <ydk.models.cisco_ios_xe.CISCO_IPSLA_AUTOMEASURE_MIB.CiscoIpslaAutomeasureMib.Cipslareacttable.Cipslareactentry.Cipslareactthresholdtype>`
            
            .. attribute:: cipslareactvar
            
            	This object specifies the type of reaction configured for an IP SLA template. Default value is 'rtt' for ICMP echo, UDP echo and TCP connect. Default value is 'jitterAvg' for UDP jitter and  ICMP jitter.  The reaction types 'rtt', 'timeout', 'connectionLoss' and 'verifyError' can be configured for all template types.  The reaction types 'jitterSDAvg', 'jitterDSAvg', 'jitterAvg',  'packetLateArrival', 'packetOutOfSequence',  'maxOfPositiveSD', 'maxOfNegativeSD', 'maxOfPositiveDS' 'maxOfNegativeDS', 'mos' and 'icpif' can be configured for  UDP jitter and ICMP jitter types only.  The reaction types 'packetLossDS', 'packetLossSD' and  'packetMIA' can be configured for UDP jitter type only.  The reaction types 'successivePacketLoss', 'maxOfLatencyDS',  'maxOfLatencySD', 'latencyDSAvg', 'latencySDAvg' and  'packetLoss' can be configured for ICMP jitter type only
            	**type**\:   :py:class:`Ipslareactvar <ydk.models.cisco_ios_xe.CISCO_IPSLA_TC_MIB.Ipslareactvar>`
            
            

            """

            _prefix = 'CISCO-IPSLA-AUTOMEASURE-MIB'
            _revision = '2007-06-13'

            def __init__(self):
                super(CiscoIpslaAutomeasureMib.Cipslareacttable.Cipslareactentry, self).__init__()

                self.yang_name = "cipslaReactEntry"
                self.yang_parent_name = "cipslaReactTable"

                self.cipslaautogroupopertype = YLeaf(YType.enumeration, "cipslaAutoGroupOperType")

                self.cipslareactconfigindex = YLeaf(YType.uint32, "cipslaReactConfigIndex")

                self.cipslaautogroupopertemplatename = YLeaf(YType.str, "cipslaAutoGroupOperTemplateName")

                self.cipslareactactiontype = YLeaf(YType.enumeration, "cipslaReactActionType")

                self.cipslareactrowstatus = YLeaf(YType.enumeration, "cipslaReactRowStatus")

                self.cipslareactstoragetype = YLeaf(YType.enumeration, "cipslaReactStorageType")

                self.cipslareactthresholdcountx = YLeaf(YType.uint32, "cipslaReactThresholdCountX")

                self.cipslareactthresholdcounty = YLeaf(YType.uint32, "cipslaReactThresholdCountY")

                self.cipslareactthresholdfalling = YLeaf(YType.uint32, "cipslaReactThresholdFalling")

                self.cipslareactthresholdrising = YLeaf(YType.uint32, "cipslaReactThresholdRising")

                self.cipslareactthresholdtype = YLeaf(YType.enumeration, "cipslaReactThresholdType")

                self.cipslareactvar = YLeaf(YType.enumeration, "cipslaReactVar")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("cipslaautogroupopertype",
                                "cipslareactconfigindex",
                                "cipslaautogroupopertemplatename",
                                "cipslareactactiontype",
                                "cipslareactrowstatus",
                                "cipslareactstoragetype",
                                "cipslareactthresholdcountx",
                                "cipslareactthresholdcounty",
                                "cipslareactthresholdfalling",
                                "cipslareactthresholdrising",
                                "cipslareactthresholdtype",
                                "cipslareactvar") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoIpslaAutomeasureMib.Cipslareacttable.Cipslareactentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoIpslaAutomeasureMib.Cipslareacttable.Cipslareactentry, self).__setattr__(name, value)

            class Cipslareactactiontype(Enum):
                """
                Cipslareactactiontype

                Specifies what type, if any, of reaction to

                generate if one of the watched

                (reaction\-configuration ) conditions is satisfied\:

                none(1)                \- no reaction is generated

                notificationOnly(2)    \- a notification is generated

                .. data:: none = 1

                .. data:: notificationOnly = 2

                """

                none = Enum.YLeaf(1, "none")

                notificationOnly = Enum.YLeaf(2, "notificationOnly")


            class Cipslareactthresholdtype(Enum):
                """
                Cipslareactthresholdtype

                This object specifies the conditions under which

                a notification ( trap ) is sent. The rttMonReactOccurred

                object defined in rttMonReactTable in CISCO\-RTTMON\-MIB will

                change accordingly\:

                never(1)       \- rttMonReactOccurred is never set

                immediate(2)   \- rttMonReactOccurred is set to 'true' when the

                                 value of parameter for which reaction is

                                 configured ( e.g rtt, jitterAvg, packetLossSD,

                                 mos etc ) violates the threshold.

                                 Conversely, rttMonReactOccurred is set to 'false'

                                 when the parameter ( e.g rtt, jitterAvg,

                                 packetLossSD, mos etc ) is below the threshold

                                 limits.

                consecutive(3) \- rttMonReactOccurred is set to true when the value

                                 of parameter for which reaction is configured

                                 ( e.g rtt, jitterAvg, packetLossSD, mos etc )

                                 violates the threshold for configured consecutive

                                 times.

                                 Conversely, rttMonReactOccurred is set to false

                                 when the value of parameter ( e.g rtt, jitterAvg

                                 packetLossSD, mos etc ) is below the threshold

                                 limits for the same number of consecutive

                                 operations.

                xOfy(4)        \- rttMonReactOccurred is set to true when x

                                 ( as specified by cipslaReactThresholdCountX )

                                 out of the last y ( as specified by

                                 cipslaReacthresholdCountY ) times the value of

                                 parameter for which the reaction is configured

                                 ( e.g rtt, jitterAvg, packetLossSD, mos etc )

                                 violates the threshold.

                                 Conversely, it is set to false when x, out of the

                                 last y times the value of parameter

                                 ( e.g rtt, jitterAvg, packetLossSD, mos ) is

                                 below the threshold limits.

                                 NOTE\: If x > y, this will never

                                      generate a reaction.

                average(5)    \- rttMonReactOccurred is set to true when the

                                average ( cipslaReactThresholdCountX times )

                                value of parameter for which reaction is 

                                configured ( e.g rtt, jitterAvg, packetLossSD,

                                mos etc ) violates the threshold condition.

                                Conversely, it is set to false when the

                                average value of parameter ( e.g rtt, jitterAvg,

                                packetLossSD, mos etc ) is below the threshold

                                limits.

                If this value is changed by a management station,

                rttMonReactOccurred is set to false, but

                no reaction is generated if the prior value of

                rttMonReactOccurred was true.

                .. data:: never = 1

                .. data:: immediate = 2

                .. data:: consecutive = 3

                .. data:: xOfy = 4

                .. data:: average = 5

                """

                never = Enum.YLeaf(1, "never")

                immediate = Enum.YLeaf(2, "immediate")

                consecutive = Enum.YLeaf(3, "consecutive")

                xOfy = Enum.YLeaf(4, "xOfy")

                average = Enum.YLeaf(5, "average")


            def has_data(self):
                return (
                    self.cipslaautogroupopertype.is_set or
                    self.cipslareactconfigindex.is_set or
                    self.cipslaautogroupopertemplatename.is_set or
                    self.cipslareactactiontype.is_set or
                    self.cipslareactrowstatus.is_set or
                    self.cipslareactstoragetype.is_set or
                    self.cipslareactthresholdcountx.is_set or
                    self.cipslareactthresholdcounty.is_set or
                    self.cipslareactthresholdfalling.is_set or
                    self.cipslareactthresholdrising.is_set or
                    self.cipslareactthresholdtype.is_set or
                    self.cipslareactvar.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.cipslaautogroupopertype.yfilter != YFilter.not_set or
                    self.cipslareactconfigindex.yfilter != YFilter.not_set or
                    self.cipslaautogroupopertemplatename.yfilter != YFilter.not_set or
                    self.cipslareactactiontype.yfilter != YFilter.not_set or
                    self.cipslareactrowstatus.yfilter != YFilter.not_set or
                    self.cipslareactstoragetype.yfilter != YFilter.not_set or
                    self.cipslareactthresholdcountx.yfilter != YFilter.not_set or
                    self.cipslareactthresholdcounty.yfilter != YFilter.not_set or
                    self.cipslareactthresholdfalling.yfilter != YFilter.not_set or
                    self.cipslareactthresholdrising.yfilter != YFilter.not_set or
                    self.cipslareactthresholdtype.yfilter != YFilter.not_set or
                    self.cipslareactvar.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cipslaReactEntry" + "[cipslaAutoGroupOperType='" + self.cipslaautogroupopertype.get() + "']" + "[cipslaReactConfigIndex='" + self.cipslareactconfigindex.get() + "']" + "[cipslaAutoGroupOperTemplateName='" + self.cipslaautogroupopertemplatename.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-IPSLA-AUTOMEASURE-MIB:CISCO-IPSLA-AUTOMEASURE-MIB/cipslaReactTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.cipslaautogroupopertype.is_set or self.cipslaautogroupopertype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipslaautogroupopertype.get_name_leafdata())
                if (self.cipslareactconfigindex.is_set or self.cipslareactconfigindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipslareactconfigindex.get_name_leafdata())
                if (self.cipslaautogroupopertemplatename.is_set or self.cipslaautogroupopertemplatename.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipslaautogroupopertemplatename.get_name_leafdata())
                if (self.cipslareactactiontype.is_set or self.cipslareactactiontype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipslareactactiontype.get_name_leafdata())
                if (self.cipslareactrowstatus.is_set or self.cipslareactrowstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipslareactrowstatus.get_name_leafdata())
                if (self.cipslareactstoragetype.is_set or self.cipslareactstoragetype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipslareactstoragetype.get_name_leafdata())
                if (self.cipslareactthresholdcountx.is_set or self.cipslareactthresholdcountx.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipslareactthresholdcountx.get_name_leafdata())
                if (self.cipslareactthresholdcounty.is_set or self.cipslareactthresholdcounty.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipslareactthresholdcounty.get_name_leafdata())
                if (self.cipslareactthresholdfalling.is_set or self.cipslareactthresholdfalling.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipslareactthresholdfalling.get_name_leafdata())
                if (self.cipslareactthresholdrising.is_set or self.cipslareactthresholdrising.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipslareactthresholdrising.get_name_leafdata())
                if (self.cipslareactthresholdtype.is_set or self.cipslareactthresholdtype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipslareactthresholdtype.get_name_leafdata())
                if (self.cipslareactvar.is_set or self.cipslareactvar.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipslareactvar.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cipslaAutoGroupOperType" or name == "cipslaReactConfigIndex" or name == "cipslaAutoGroupOperTemplateName" or name == "cipslaReactActionType" or name == "cipslaReactRowStatus" or name == "cipslaReactStorageType" or name == "cipslaReactThresholdCountX" or name == "cipslaReactThresholdCountY" or name == "cipslaReactThresholdFalling" or name == "cipslaReactThresholdRising" or name == "cipslaReactThresholdType" or name == "cipslaReactVar"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "cipslaAutoGroupOperType"):
                    self.cipslaautogroupopertype = value
                    self.cipslaautogroupopertype.value_namespace = name_space
                    self.cipslaautogroupopertype.value_namespace_prefix = name_space_prefix
                if(value_path == "cipslaReactConfigIndex"):
                    self.cipslareactconfigindex = value
                    self.cipslareactconfigindex.value_namespace = name_space
                    self.cipslareactconfigindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cipslaAutoGroupOperTemplateName"):
                    self.cipslaautogroupopertemplatename = value
                    self.cipslaautogroupopertemplatename.value_namespace = name_space
                    self.cipslaautogroupopertemplatename.value_namespace_prefix = name_space_prefix
                if(value_path == "cipslaReactActionType"):
                    self.cipslareactactiontype = value
                    self.cipslareactactiontype.value_namespace = name_space
                    self.cipslareactactiontype.value_namespace_prefix = name_space_prefix
                if(value_path == "cipslaReactRowStatus"):
                    self.cipslareactrowstatus = value
                    self.cipslareactrowstatus.value_namespace = name_space
                    self.cipslareactrowstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "cipslaReactStorageType"):
                    self.cipslareactstoragetype = value
                    self.cipslareactstoragetype.value_namespace = name_space
                    self.cipslareactstoragetype.value_namespace_prefix = name_space_prefix
                if(value_path == "cipslaReactThresholdCountX"):
                    self.cipslareactthresholdcountx = value
                    self.cipslareactthresholdcountx.value_namespace = name_space
                    self.cipslareactthresholdcountx.value_namespace_prefix = name_space_prefix
                if(value_path == "cipslaReactThresholdCountY"):
                    self.cipslareactthresholdcounty = value
                    self.cipslareactthresholdcounty.value_namespace = name_space
                    self.cipslareactthresholdcounty.value_namespace_prefix = name_space_prefix
                if(value_path == "cipslaReactThresholdFalling"):
                    self.cipslareactthresholdfalling = value
                    self.cipslareactthresholdfalling.value_namespace = name_space
                    self.cipslareactthresholdfalling.value_namespace_prefix = name_space_prefix
                if(value_path == "cipslaReactThresholdRising"):
                    self.cipslareactthresholdrising = value
                    self.cipslareactthresholdrising.value_namespace = name_space
                    self.cipslareactthresholdrising.value_namespace_prefix = name_space_prefix
                if(value_path == "cipslaReactThresholdType"):
                    self.cipslareactthresholdtype = value
                    self.cipslareactthresholdtype.value_namespace = name_space
                    self.cipslareactthresholdtype.value_namespace_prefix = name_space_prefix
                if(value_path == "cipslaReactVar"):
                    self.cipslareactvar = value
                    self.cipslareactvar.value_namespace = name_space
                    self.cipslareactvar.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cipslareactentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cipslareactentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cipslaReactTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-IPSLA-AUTOMEASURE-MIB:CISCO-IPSLA-AUTOMEASURE-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cipslaReactEntry"):
                for c in self.cipslareactentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoIpslaAutomeasureMib.Cipslareacttable.Cipslareactentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cipslareactentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cipslaReactEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Cipslaautogroupschedtable(Entity):
        """
        A table of group scheduling definitions.
        
        .. attribute:: cipslaautogroupschedentry
        
        	A list of objects that define specific configuration for group scheduling
        	**type**\: list of    :py:class:`Cipslaautogroupschedentry <ydk.models.cisco_ios_xe.CISCO_IPSLA_AUTOMEASURE_MIB.CiscoIpslaAutomeasureMib.Cipslaautogroupschedtable.Cipslaautogroupschedentry>`
        
        

        """

        _prefix = 'CISCO-IPSLA-AUTOMEASURE-MIB'
        _revision = '2007-06-13'

        def __init__(self):
            super(CiscoIpslaAutomeasureMib.Cipslaautogroupschedtable, self).__init__()

            self.yang_name = "cipslaAutoGroupSchedTable"
            self.yang_parent_name = "CISCO-IPSLA-AUTOMEASURE-MIB"

            self.cipslaautogroupschedentry = YList(self)

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
                        super(CiscoIpslaAutomeasureMib.Cipslaautogroupschedtable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoIpslaAutomeasureMib.Cipslaautogroupschedtable, self).__setattr__(name, value)


        class Cipslaautogroupschedentry(Entity):
            """
            A list of objects that define specific configuration for
            group scheduling.
            
            .. attribute:: cipslaautogroupschedid  <key>
            
            	This string uniquely identifies a row in the cipslaAutoGroupSchedTable
            	**type**\:  str
            
            	**length:** 1..64
            
            .. attribute:: cipslaautogroupschedageout
            
            	This object specifies the ageout value of the operations that are getting group scheduled. This value will be placed into rttMonSchedAdminConceptRowAgeout object for each of the operations in the group when this conceptual control row becomes  'active'.  When this value is set to zero, the operations will never ageout
            	**type**\:  int
            
            	**range:** 0..2073600
            
            	**units**\: seconds
            
            .. attribute:: cipslaautogroupschedinterval
            
            	Specifies the duration between initiating each RTT operation for one IP SLA operation generated via the auto  measure group.  The value of this object is only effective when both cipslaAutoGroupSchedMaxInterval and  cipslaAutoGroupSchedMinInterval have zero values
            	**type**\:  int
            
            	**range:** 1..604800
            
            	**units**\: seconds
            
            .. attribute:: cipslaautogroupschedlife
            
            	This object specifies the life of all the operations that are getting group scheduled. This value will be placed into cipslaAutoGroupSchedRttLife object when this conceptual control row becomes 'active'.  The value 2147483647 has a special meaning. When this object is set to 2147483647, the rttMonCtrlOperRttLife object for all the operations will not decrement, and thus the life time of the  operation will never end
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            	**units**\: seconds
            
            .. attribute:: cipslaautogroupschedmaxinterval
            
            	Specifies the max duration between initiating each RTT operation for one IP SLA operation in the group
            	**type**\:  int
            
            	**range:** 0..604800
            
            	**units**\: seconds
            
            .. attribute:: cipslaautogroupschedmininterval
            
            	Specifies the min duration between initiating each RTT operation for one IP SLA operation in the group.  The value of this object should be lower than the value of cipslaAutoGroupSchedMaxInterval
            	**type**\:  int
            
            	**range:** 0..604800
            
            	**units**\: seconds
            
            .. attribute:: cipslaautogroupschedperiod
            
            	Specifies the time duration between initiating two IP SLA operations generated via the auto measure group
            	**type**\:  int
            
            	**range:** 100..99000
            
            	**units**\: seconds
            
            .. attribute:: cipslaautogroupschedrowstatus
            
            	The status of the conceptual group schedule control row.  When the status is active and the value of  cipslaAutoGroupSchedStartTime is '1', the other writable  objects may be modified.  This object can be set to 'destroy' from any value at any time. When this object is set to 'destroy' it will stop all the  operations which had been group scheduled by it earlier,  before destroying the group schedule control row
            	**type**\:   :py:class:`Rowstatus <ydk.models.cisco_ios_xe.SNMPv2_TC.Rowstatus>`
            
            .. attribute:: cipslaautogroupschedstarttime
            
            	This is the time in seconds after which the operations of the associated groups  will take transition to active state. When set to the value other than '1' (pending), then all  objects in this row cannot be modified
            	**type**\:  int
            
            	**range:** 0..604800
            
            	**units**\: seconds
            
            .. attribute:: cipslaautogroupschedstoragetype
            
            	The storage type of this conceptual row.  By default the entry will be saved into non\-volatile memory
            	**type**\:   :py:class:`Storagetype <ydk.models.cisco_ios_xe.SNMPv2_TC.Storagetype>`
            
            

            """

            _prefix = 'CISCO-IPSLA-AUTOMEASURE-MIB'
            _revision = '2007-06-13'

            def __init__(self):
                super(CiscoIpslaAutomeasureMib.Cipslaautogroupschedtable.Cipslaautogroupschedentry, self).__init__()

                self.yang_name = "cipslaAutoGroupSchedEntry"
                self.yang_parent_name = "cipslaAutoGroupSchedTable"

                self.cipslaautogroupschedid = YLeaf(YType.str, "cipslaAutoGroupSchedId")

                self.cipslaautogroupschedageout = YLeaf(YType.uint32, "cipslaAutoGroupSchedAgeout")

                self.cipslaautogroupschedinterval = YLeaf(YType.uint32, "cipslaAutoGroupSchedInterval")

                self.cipslaautogroupschedlife = YLeaf(YType.uint32, "cipslaAutoGroupSchedLife")

                self.cipslaautogroupschedmaxinterval = YLeaf(YType.uint32, "cipslaAutoGroupSchedMaxInterval")

                self.cipslaautogroupschedmininterval = YLeaf(YType.uint32, "cipslaAutoGroupSchedMinInterval")

                self.cipslaautogroupschedperiod = YLeaf(YType.uint32, "cipslaAutoGroupSchedPeriod")

                self.cipslaautogroupschedrowstatus = YLeaf(YType.enumeration, "cipslaAutoGroupSchedRowStatus")

                self.cipslaautogroupschedstarttime = YLeaf(YType.uint32, "cipslaAutoGroupSchedStartTime")

                self.cipslaautogroupschedstoragetype = YLeaf(YType.enumeration, "cipslaAutoGroupSchedStorageType")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("cipslaautogroupschedid",
                                "cipslaautogroupschedageout",
                                "cipslaautogroupschedinterval",
                                "cipslaautogroupschedlife",
                                "cipslaautogroupschedmaxinterval",
                                "cipslaautogroupschedmininterval",
                                "cipslaautogroupschedperiod",
                                "cipslaautogroupschedrowstatus",
                                "cipslaautogroupschedstarttime",
                                "cipslaautogroupschedstoragetype") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoIpslaAutomeasureMib.Cipslaautogroupschedtable.Cipslaautogroupschedentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoIpslaAutomeasureMib.Cipslaautogroupschedtable.Cipslaautogroupschedentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.cipslaautogroupschedid.is_set or
                    self.cipslaautogroupschedageout.is_set or
                    self.cipslaautogroupschedinterval.is_set or
                    self.cipslaautogroupschedlife.is_set or
                    self.cipslaautogroupschedmaxinterval.is_set or
                    self.cipslaautogroupschedmininterval.is_set or
                    self.cipslaautogroupschedperiod.is_set or
                    self.cipslaautogroupschedrowstatus.is_set or
                    self.cipslaautogroupschedstarttime.is_set or
                    self.cipslaautogroupschedstoragetype.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.cipslaautogroupschedid.yfilter != YFilter.not_set or
                    self.cipslaautogroupschedageout.yfilter != YFilter.not_set or
                    self.cipslaautogroupschedinterval.yfilter != YFilter.not_set or
                    self.cipslaautogroupschedlife.yfilter != YFilter.not_set or
                    self.cipslaautogroupschedmaxinterval.yfilter != YFilter.not_set or
                    self.cipslaautogroupschedmininterval.yfilter != YFilter.not_set or
                    self.cipslaautogroupschedperiod.yfilter != YFilter.not_set or
                    self.cipslaautogroupschedrowstatus.yfilter != YFilter.not_set or
                    self.cipslaautogroupschedstarttime.yfilter != YFilter.not_set or
                    self.cipslaautogroupschedstoragetype.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cipslaAutoGroupSchedEntry" + "[cipslaAutoGroupSchedId='" + self.cipslaautogroupschedid.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-IPSLA-AUTOMEASURE-MIB:CISCO-IPSLA-AUTOMEASURE-MIB/cipslaAutoGroupSchedTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.cipslaautogroupschedid.is_set or self.cipslaautogroupschedid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipslaautogroupschedid.get_name_leafdata())
                if (self.cipslaautogroupschedageout.is_set or self.cipslaautogroupschedageout.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipslaautogroupschedageout.get_name_leafdata())
                if (self.cipslaautogroupschedinterval.is_set or self.cipslaautogroupschedinterval.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipslaautogroupschedinterval.get_name_leafdata())
                if (self.cipslaautogroupschedlife.is_set or self.cipslaautogroupschedlife.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipslaautogroupschedlife.get_name_leafdata())
                if (self.cipslaautogroupschedmaxinterval.is_set or self.cipslaautogroupschedmaxinterval.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipslaautogroupschedmaxinterval.get_name_leafdata())
                if (self.cipslaautogroupschedmininterval.is_set or self.cipslaautogroupschedmininterval.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipslaautogroupschedmininterval.get_name_leafdata())
                if (self.cipslaautogroupschedperiod.is_set or self.cipslaautogroupschedperiod.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipslaautogroupschedperiod.get_name_leafdata())
                if (self.cipslaautogroupschedrowstatus.is_set or self.cipslaautogroupschedrowstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipslaautogroupschedrowstatus.get_name_leafdata())
                if (self.cipslaautogroupschedstarttime.is_set or self.cipslaautogroupschedstarttime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipslaautogroupschedstarttime.get_name_leafdata())
                if (self.cipslaautogroupschedstoragetype.is_set or self.cipslaautogroupschedstoragetype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cipslaautogroupschedstoragetype.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cipslaAutoGroupSchedId" or name == "cipslaAutoGroupSchedAgeout" or name == "cipslaAutoGroupSchedInterval" or name == "cipslaAutoGroupSchedLife" or name == "cipslaAutoGroupSchedMaxInterval" or name == "cipslaAutoGroupSchedMinInterval" or name == "cipslaAutoGroupSchedPeriod" or name == "cipslaAutoGroupSchedRowStatus" or name == "cipslaAutoGroupSchedStartTime" or name == "cipslaAutoGroupSchedStorageType"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "cipslaAutoGroupSchedId"):
                    self.cipslaautogroupschedid = value
                    self.cipslaautogroupschedid.value_namespace = name_space
                    self.cipslaautogroupschedid.value_namespace_prefix = name_space_prefix
                if(value_path == "cipslaAutoGroupSchedAgeout"):
                    self.cipslaautogroupschedageout = value
                    self.cipslaautogroupschedageout.value_namespace = name_space
                    self.cipslaautogroupschedageout.value_namespace_prefix = name_space_prefix
                if(value_path == "cipslaAutoGroupSchedInterval"):
                    self.cipslaautogroupschedinterval = value
                    self.cipslaautogroupschedinterval.value_namespace = name_space
                    self.cipslaautogroupschedinterval.value_namespace_prefix = name_space_prefix
                if(value_path == "cipslaAutoGroupSchedLife"):
                    self.cipslaautogroupschedlife = value
                    self.cipslaautogroupschedlife.value_namespace = name_space
                    self.cipslaautogroupschedlife.value_namespace_prefix = name_space_prefix
                if(value_path == "cipslaAutoGroupSchedMaxInterval"):
                    self.cipslaautogroupschedmaxinterval = value
                    self.cipslaautogroupschedmaxinterval.value_namespace = name_space
                    self.cipslaautogroupschedmaxinterval.value_namespace_prefix = name_space_prefix
                if(value_path == "cipslaAutoGroupSchedMinInterval"):
                    self.cipslaautogroupschedmininterval = value
                    self.cipslaautogroupschedmininterval.value_namespace = name_space
                    self.cipslaautogroupschedmininterval.value_namespace_prefix = name_space_prefix
                if(value_path == "cipslaAutoGroupSchedPeriod"):
                    self.cipslaautogroupschedperiod = value
                    self.cipslaautogroupschedperiod.value_namespace = name_space
                    self.cipslaautogroupschedperiod.value_namespace_prefix = name_space_prefix
                if(value_path == "cipslaAutoGroupSchedRowStatus"):
                    self.cipslaautogroupschedrowstatus = value
                    self.cipslaautogroupschedrowstatus.value_namespace = name_space
                    self.cipslaautogroupschedrowstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "cipslaAutoGroupSchedStartTime"):
                    self.cipslaautogroupschedstarttime = value
                    self.cipslaautogroupschedstarttime.value_namespace = name_space
                    self.cipslaautogroupschedstarttime.value_namespace_prefix = name_space_prefix
                if(value_path == "cipslaAutoGroupSchedStorageType"):
                    self.cipslaautogroupschedstoragetype = value
                    self.cipslaautogroupschedstoragetype.value_namespace = name_space
                    self.cipslaautogroupschedstoragetype.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cipslaautogroupschedentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cipslaautogroupschedentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cipslaAutoGroupSchedTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-IPSLA-AUTOMEASURE-MIB:CISCO-IPSLA-AUTOMEASURE-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cipslaAutoGroupSchedEntry"):
                for c in self.cipslaautogroupschedentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoIpslaAutomeasureMib.Cipslaautogroupschedtable.Cipslaautogroupschedentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cipslaautogroupschedentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cipslaAutoGroupSchedEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            (self.cipslaautogroupdesttable is not None and self.cipslaautogroupdesttable.has_data()) or
            (self.cipslaautogroupschedtable is not None and self.cipslaautogroupschedtable.has_data()) or
            (self.cipslaautogrouptable is not None and self.cipslaautogrouptable.has_data()) or
            (self.cipslareacttable is not None and self.cipslareacttable.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.cipslaautogroupdesttable is not None and self.cipslaautogroupdesttable.has_operation()) or
            (self.cipslaautogroupschedtable is not None and self.cipslaautogroupschedtable.has_operation()) or
            (self.cipslaautogrouptable is not None and self.cipslaautogrouptable.has_operation()) or
            (self.cipslareacttable is not None and self.cipslareacttable.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "CISCO-IPSLA-AUTOMEASURE-MIB:CISCO-IPSLA-AUTOMEASURE-MIB" + path_buffer

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

        if (child_yang_name == "cipslaAutoGroupDestTable"):
            if (self.cipslaautogroupdesttable is None):
                self.cipslaautogroupdesttable = CiscoIpslaAutomeasureMib.Cipslaautogroupdesttable()
                self.cipslaautogroupdesttable.parent = self
                self._children_name_map["cipslaautogroupdesttable"] = "cipslaAutoGroupDestTable"
            return self.cipslaautogroupdesttable

        if (child_yang_name == "cipslaAutoGroupSchedTable"):
            if (self.cipslaautogroupschedtable is None):
                self.cipslaautogroupschedtable = CiscoIpslaAutomeasureMib.Cipslaautogroupschedtable()
                self.cipslaautogroupschedtable.parent = self
                self._children_name_map["cipslaautogroupschedtable"] = "cipslaAutoGroupSchedTable"
            return self.cipslaautogroupschedtable

        if (child_yang_name == "cipslaAutoGroupTable"):
            if (self.cipslaautogrouptable is None):
                self.cipslaautogrouptable = CiscoIpslaAutomeasureMib.Cipslaautogrouptable()
                self.cipslaautogrouptable.parent = self
                self._children_name_map["cipslaautogrouptable"] = "cipslaAutoGroupTable"
            return self.cipslaautogrouptable

        if (child_yang_name == "cipslaReactTable"):
            if (self.cipslareacttable is None):
                self.cipslareacttable = CiscoIpslaAutomeasureMib.Cipslareacttable()
                self.cipslareacttable.parent = self
                self._children_name_map["cipslareacttable"] = "cipslaReactTable"
            return self.cipslareacttable

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "cipslaAutoGroupDestTable" or name == "cipslaAutoGroupSchedTable" or name == "cipslaAutoGroupTable" or name == "cipslaReactTable"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = CiscoIpslaAutomeasureMib()
        return self._top_entity

