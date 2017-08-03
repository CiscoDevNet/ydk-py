""" CISCO_IGMP_FILTER_MIB 

IGMP Filter configuration MIB. This MIB provides a
mechanism for users to configure the system to intercept 
IGMP joins for IP Multicast groups identified in this 
MIB and only allow certain ports to join certain 
multicast groups.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class CiscoIgmpFilterMib(Entity):
    """
    
    
    .. attribute:: cigmpfiltereditor
    
    	
    	**type**\:   :py:class:`Cigmpfiltereditor <ydk.models.cisco_ios_xe.CISCO_IGMP_FILTER_MIB.CiscoIgmpFilterMib.Cigmpfiltereditor>`
    
    .. attribute:: cigmpfiltergeneral
    
    	
    	**type**\:   :py:class:`Cigmpfiltergeneral <ydk.models.cisco_ios_xe.CISCO_IGMP_FILTER_MIB.CiscoIgmpFilterMib.Cigmpfiltergeneral>`
    
    .. attribute:: cigmpfilterinterfacetable
    
    	This table contains the list of interfaces that can support IGMP filter feature
    	**type**\:   :py:class:`Cigmpfilterinterfacetable <ydk.models.cisco_ios_xe.CISCO_IGMP_FILTER_MIB.CiscoIgmpFilterMib.Cigmpfilterinterfacetable>`
    
    .. attribute:: cigmpfiltertable
    
    	This table contains entries that identify lists of IP Multicast groups for each profile configured on the device.   Each entry contains a range of contiguous IP Multicast groups associated to a profile index. Multiple cIgmpFilterEntry may be associated with the same cIgmpFilterProfileIndex.  All the cIgmpFilterEntry with  the same profile index  are subjected to the same IGMP filtering action as  defined in cIgmpFilterProfileAction.  Each profile index may be associated with zero or more  interfaces through cIgmpFilterInterfaceIfIndex object in cIgmpFilterInterfaceTable. The maximum number of entries is determined by cIgmpFilterMaxProfiles
    	**type**\:   :py:class:`Cigmpfiltertable <ydk.models.cisco_ios_xe.CISCO_IGMP_FILTER_MIB.CiscoIgmpFilterMib.Cigmpfiltertable>`
    
    

    """

    _prefix = 'CISCO-IGMP-FILTER-MIB'
    _revision = '2005-11-29'

    def __init__(self):
        super(CiscoIgmpFilterMib, self).__init__()
        self._top_entity = None

        self.yang_name = "CISCO-IGMP-FILTER-MIB"
        self.yang_parent_name = "CISCO-IGMP-FILTER-MIB"

        self.cigmpfiltereditor = CiscoIgmpFilterMib.Cigmpfiltereditor()
        self.cigmpfiltereditor.parent = self
        self._children_name_map["cigmpfiltereditor"] = "cIgmpFilterEditor"
        self._children_yang_names.add("cIgmpFilterEditor")

        self.cigmpfiltergeneral = CiscoIgmpFilterMib.Cigmpfiltergeneral()
        self.cigmpfiltergeneral.parent = self
        self._children_name_map["cigmpfiltergeneral"] = "cIgmpFilterGeneral"
        self._children_yang_names.add("cIgmpFilterGeneral")

        self.cigmpfilterinterfacetable = CiscoIgmpFilterMib.Cigmpfilterinterfacetable()
        self.cigmpfilterinterfacetable.parent = self
        self._children_name_map["cigmpfilterinterfacetable"] = "cIgmpFilterInterfaceTable"
        self._children_yang_names.add("cIgmpFilterInterfaceTable")

        self.cigmpfiltertable = CiscoIgmpFilterMib.Cigmpfiltertable()
        self.cigmpfiltertable.parent = self
        self._children_name_map["cigmpfiltertable"] = "cIgmpFilterTable"
        self._children_yang_names.add("cIgmpFilterTable")


    class Cigmpfiltergeneral(Entity):
        """
        
        
        .. attribute:: cigmpfilterenable
        
        	This object controls whether the IGMP filtering is enabled on the device. A false(2) value will  prevent the IGMP filtering action on the device
        	**type**\:  bool
        
        .. attribute:: cigmpfiltermaxprofiles
        
        	Indicates the maximum number of profiles supported by this device.  A value of zero indicates no limitation on the number of profiles
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**units**\: profiles
        
        

        """

        _prefix = 'CISCO-IGMP-FILTER-MIB'
        _revision = '2005-11-29'

        def __init__(self):
            super(CiscoIgmpFilterMib.Cigmpfiltergeneral, self).__init__()

            self.yang_name = "cIgmpFilterGeneral"
            self.yang_parent_name = "CISCO-IGMP-FILTER-MIB"

            self.cigmpfilterenable = YLeaf(YType.boolean, "cIgmpFilterEnable")

            self.cigmpfiltermaxprofiles = YLeaf(YType.uint32, "cIgmpFilterMaxProfiles")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("cigmpfilterenable",
                            "cigmpfiltermaxprofiles") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoIgmpFilterMib.Cigmpfiltergeneral, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoIgmpFilterMib.Cigmpfiltergeneral, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.cigmpfilterenable.is_set or
                self.cigmpfiltermaxprofiles.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.cigmpfilterenable.yfilter != YFilter.not_set or
                self.cigmpfiltermaxprofiles.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cIgmpFilterGeneral" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-IGMP-FILTER-MIB:CISCO-IGMP-FILTER-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.cigmpfilterenable.is_set or self.cigmpfilterenable.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cigmpfilterenable.get_name_leafdata())
            if (self.cigmpfiltermaxprofiles.is_set or self.cigmpfiltermaxprofiles.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cigmpfiltermaxprofiles.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cIgmpFilterEnable" or name == "cIgmpFilterMaxProfiles"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "cIgmpFilterEnable"):
                self.cigmpfilterenable = value
                self.cigmpfilterenable.value_namespace = name_space
                self.cigmpfilterenable.value_namespace_prefix = name_space_prefix
            if(value_path == "cIgmpFilterMaxProfiles"):
                self.cigmpfiltermaxprofiles = value
                self.cigmpfiltermaxprofiles.value_namespace = name_space
                self.cigmpfiltermaxprofiles.value_namespace_prefix = name_space_prefix


    class Cigmpfiltereditor(Entity):
        """
        
        
        .. attribute:: cigmpfilterapplystatus
        
        	The current status of an 'add', 'delete' or 'modify' operation. If no apply is currently active, the status  represented is that of the most recently completed 'add',  'delete' or 'modify' operation.  The value of this objects indicates succeeded(2) state  initially when no 'add', 'delete', 'modify' operation has been carried out.  The possible values are\:    someOtherError \- the 'add', 'delete' or 'modify' failed     due to undefined error(s) in apply operation.    (e.g., insufficient memory).      succeeded \- the 'add', 'delete' or 'modify' operation    was successful. (This value is also used when no    apply has been invoked since the last time the local     system restarted.)     inconsistentEdit \- the 'add', 'delete' or 'modify' failed    due to inconsistency of the data.     entryPresentError \- the 'add' operation failed  as the     corresponding entry already exists in cIgmpFilterTable.     entryNotPresentError \- the 'modify' operation failed     as no corresponding entry exists in cIgmpFilterTable
        	**type**\:   :py:class:`Cigmpfilterapplystatus <ydk.models.cisco_ios_xe.CISCO_IGMP_FILTER_MIB.CiscoIgmpFilterMib.Cigmpfiltereditor.Cigmpfilterapplystatus>`
        
        .. attribute:: cigmpfiltereditendaddress
        
        	Buffer object to edit corresponding object cIgmpFilterEndAddress in cIgmpFilterTable  to establish end address of filtering  range for a profile
        	**type**\:  str
        
        	**length:** 0..255
        
        .. attribute:: cigmpfiltereditendaddresstype
        
        	Buffer object to edit corresponding object cIgmpFilterEndAddressType in cIgmpFilterTable.  This object describes the type of Internet      address used to determine the start address  of IP multicast group for a profile
        	**type**\:   :py:class:`Inetaddresstype <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.Inetaddresstype>`
        
        .. attribute:: cigmpfiltereditoperation
        
        	The function of this object is to allow user to apply the changes in cIgmpFilterEditor objects to  cIgmpFilterTable.   This object always has the value 'none' when read. When written each value causes the appropriate action\:  'add' \- tries to insert the information contained  in cIgmpFilterEditor objects into  cIgmpFilterTable. If the entry already exists in the table the 'add'  fails.          'delete' \- tries to delete corresponding entry from cIgmpFilterTable. If a user completely deletes a profile that has corresponding entries in the cIgmpFilterInterfaceTable, then all the interfaces mapped to corresponding profile will be cleared and set to zero.  'modify' \- Mode of operation used to edit an entry in  cIgmpFilterTable. If the corresponding entry does not   exist, modify operation fails. This mode allows user to  extend/truncate a contiguous filtered range, type of  Internet addressing and filtering action for a profile.   'none' \- no operation is performed
        	**type**\:   :py:class:`Cigmpfiltereditoperation <ydk.models.cisco_ios_xe.CISCO_IGMP_FILTER_MIB.CiscoIgmpFilterMib.Cigmpfiltereditor.Cigmpfiltereditoperation>`
        
        .. attribute:: cigmpfiltereditprofileaction
        
        	Buffer object to edit corresponding object in cIgmpFilterTable to determine filtering action of each profile
        	**type**\:   :py:class:`Cigmpfiltereditprofileaction <ydk.models.cisco_ios_xe.CISCO_IGMP_FILTER_MIB.CiscoIgmpFilterMib.Cigmpfiltereditor.Cigmpfiltereditprofileaction>`
        
        .. attribute:: cigmpfiltereditprofileindex
        
        	Buffer object to edit corresponding object cIgmpFilterProfileIndex in cIgmpFilterTable.  Maximum value this object can be set to is  determined by cIgmpFilterMaxProfiles object
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: cigmpfiltereditspinlock
        
        	This object is used to facilitate modification of IGMP Filter Editor Group in the CISCO\-IGMP\-FILTER\-MIB  module by multiple managers.  In particular, it is  useful when modifying the value of the cIgmpFilterEditor  object.   The procedure for modifying the cIgmpFilterEditor  object is as follows\:       1.  Retrieve the value of cIgmpFilterEditSpinLock and          of object within cIgmpFilterEditor group.       2.  Generate new values for 'writeable' objects         in the cIgmpFilterEditor group except for          cIgmpFilterEditSpinLock object.      3.  Set the value of cIgmpFilterEditSpinLock to the          retrieved value, and the value of objects in          cIgmpFilterEditor to the new value. If the set         fails for the cIgmpFilterEditSpinLock object,         go back to step 1.   The cIgmpFilterApplyStatus and cIgmpFilterEditSpinLock  should be read together by NMS to make sure that the  result is associated with its configuration request.  To add/delete or modify a profile ( through cIgmpFilterEditor objects ) following procedure may be followed as an example.\:      1.  GET(cIgmpFilterEditSpinLock.0) and save in sValue.     2.  SET(cIgmpFilterEditSpinLock.0 = sValue,             cIgmpFilterEditProfileIndex.0 = validProfileNumber,             cIgmpFilterEditStartAddress.0 = validStartAddress,             cIgmpFilterEditEndAddress.0 = validEndAddress,             cIgmpFilterEditOperation.0 =  validOperation)     3.  If the SET in step 2 is not successful go back         to step 1.     4.  If the SET in step 2 is successful, user should          GET(cIgmpFilterEditSpinLock.0) and          GET(cIgmpFilterApplyStatus.0) simultaneously.      5.  The cIgmpFilterApplyStatus.0 reflects the outcome of         step 2 only if         cIgmpFilterEditSpinLock.0 = sValue + 1 or         cIgmpFilterEditSpinLock.0 = 0 if sValue reaches         value at which cIgmpFilterEditSpinLock wraps          around
        	**type**\:  int
        
        	**range:** 0..2147483647
        
        .. attribute:: cigmpfiltereditstartaddress
        
        	Buffer object to edit corresponding object cIgmpFilterStartAddress in cIgmpFilterTable   to establish start address of filtering range for a profile
        	**type**\:  str
        
        	**length:** 1..64
        
        .. attribute:: cigmpfiltereditstartaddresstype
        
        	Buffer object to edit corresponding object cIgmpFilterStartAddressType in cIgmpFilterTable.  This object describes the type of Internet   address used to determine the start address  of IP multicast group for a profile
        	**type**\:   :py:class:`Inetaddresstype <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.Inetaddresstype>`
        
        

        """

        _prefix = 'CISCO-IGMP-FILTER-MIB'
        _revision = '2005-11-29'

        def __init__(self):
            super(CiscoIgmpFilterMib.Cigmpfiltereditor, self).__init__()

            self.yang_name = "cIgmpFilterEditor"
            self.yang_parent_name = "CISCO-IGMP-FILTER-MIB"

            self.cigmpfilterapplystatus = YLeaf(YType.enumeration, "cIgmpFilterApplyStatus")

            self.cigmpfiltereditendaddress = YLeaf(YType.str, "cIgmpFilterEditEndAddress")

            self.cigmpfiltereditendaddresstype = YLeaf(YType.enumeration, "cIgmpFilterEditEndAddressType")

            self.cigmpfiltereditoperation = YLeaf(YType.enumeration, "cIgmpFilterEditOperation")

            self.cigmpfiltereditprofileaction = YLeaf(YType.enumeration, "cIgmpFilterEditProfileAction")

            self.cigmpfiltereditprofileindex = YLeaf(YType.uint32, "cIgmpFilterEditProfileIndex")

            self.cigmpfiltereditspinlock = YLeaf(YType.int32, "cIgmpFilterEditSpinLock")

            self.cigmpfiltereditstartaddress = YLeaf(YType.str, "cIgmpFilterEditStartAddress")

            self.cigmpfiltereditstartaddresstype = YLeaf(YType.enumeration, "cIgmpFilterEditStartAddressType")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("cigmpfilterapplystatus",
                            "cigmpfiltereditendaddress",
                            "cigmpfiltereditendaddresstype",
                            "cigmpfiltereditoperation",
                            "cigmpfiltereditprofileaction",
                            "cigmpfiltereditprofileindex",
                            "cigmpfiltereditspinlock",
                            "cigmpfiltereditstartaddress",
                            "cigmpfiltereditstartaddresstype") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoIgmpFilterMib.Cigmpfiltereditor, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoIgmpFilterMib.Cigmpfiltereditor, self).__setattr__(name, value)

        class Cigmpfilterapplystatus(Enum):
            """
            Cigmpfilterapplystatus

            The current status of an 'add', 'delete' or 'modify'

            operation. If no apply is currently active, the status 

            represented is that of the most recently completed 'add', 

            'delete' or 'modify' operation.

            The value of this objects indicates succeeded(2) state 

            initially when no 'add', 'delete', 'modify' operation

            has been carried out.

            The possible values are\:

               someOtherError \- the 'add', 'delete' or 'modify' failed 

               due to undefined error(s) in apply operation.

               (e.g., insufficient memory). 

               succeeded \- the 'add', 'delete' or 'modify' operation

               was successful. (This value is also used when no

               apply has been invoked since the last time the local 

               system restarted.)

               inconsistentEdit \- the 'add', 'delete' or 'modify' failed

               due to inconsistency of the data.

               entryPresentError \- the 'add' operation failed  as the 

               corresponding entry already exists in cIgmpFilterTable.

               entryNotPresentError \- the 'modify' operation failed 

               as no corresponding entry exists in cIgmpFilterTable.

            .. data:: someOtherError = 1

            .. data:: succeeded = 2

            .. data:: inconsistentEdit = 3

            .. data:: entryPresentError = 4

            .. data:: entryNotPresentError = 5

            """

            someOtherError = Enum.YLeaf(1, "someOtherError")

            succeeded = Enum.YLeaf(2, "succeeded")

            inconsistentEdit = Enum.YLeaf(3, "inconsistentEdit")

            entryPresentError = Enum.YLeaf(4, "entryPresentError")

            entryNotPresentError = Enum.YLeaf(5, "entryNotPresentError")


        class Cigmpfiltereditoperation(Enum):
            """
            Cigmpfiltereditoperation

            The function of this object is to allow user to

            apply the changes in cIgmpFilterEditor objects to 

            cIgmpFilterTable. 

            This object always has the value 'none' when read.

            When written each value causes the appropriate action\:

            'add' \- tries to insert the information contained 

            in cIgmpFilterEditor objects into  cIgmpFilterTable.

            If the entry already exists in the table the 'add' 

            fails.        

            'delete' \- tries to delete corresponding entry from

            cIgmpFilterTable. If a user completely deletes a profile

            that has corresponding entries in the

            cIgmpFilterInterfaceTable, then all the interfaces mapped

            to corresponding profile will be cleared and set to zero.

            'modify' \- Mode of operation used to edit an entry in

             cIgmpFilterTable. If the corresponding entry does not 

             exist, modify operation fails. This mode allows user to

             extend/truncate a contiguous filtered range, type of

             Internet addressing and filtering action for a profile. 

            'none' \- no operation is performed.

            .. data:: none = 1

            .. data:: add = 2

            .. data:: delete = 3

            .. data:: modify = 4

            """

            none = Enum.YLeaf(1, "none")

            add = Enum.YLeaf(2, "add")

            delete = Enum.YLeaf(3, "delete")

            modify = Enum.YLeaf(4, "modify")


        class Cigmpfiltereditprofileaction(Enum):
            """
            Cigmpfiltereditprofileaction

            Buffer object to edit corresponding object in

            cIgmpFilterTable to determine filtering action

            of each profile.

            .. data:: unSpecified = 0

            .. data:: permit = 1

            .. data:: deny = 2

            """

            unSpecified = Enum.YLeaf(0, "unSpecified")

            permit = Enum.YLeaf(1, "permit")

            deny = Enum.YLeaf(2, "deny")


        def has_data(self):
            return (
                self.cigmpfilterapplystatus.is_set or
                self.cigmpfiltereditendaddress.is_set or
                self.cigmpfiltereditendaddresstype.is_set or
                self.cigmpfiltereditoperation.is_set or
                self.cigmpfiltereditprofileaction.is_set or
                self.cigmpfiltereditprofileindex.is_set or
                self.cigmpfiltereditspinlock.is_set or
                self.cigmpfiltereditstartaddress.is_set or
                self.cigmpfiltereditstartaddresstype.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.cigmpfilterapplystatus.yfilter != YFilter.not_set or
                self.cigmpfiltereditendaddress.yfilter != YFilter.not_set or
                self.cigmpfiltereditendaddresstype.yfilter != YFilter.not_set or
                self.cigmpfiltereditoperation.yfilter != YFilter.not_set or
                self.cigmpfiltereditprofileaction.yfilter != YFilter.not_set or
                self.cigmpfiltereditprofileindex.yfilter != YFilter.not_set or
                self.cigmpfiltereditspinlock.yfilter != YFilter.not_set or
                self.cigmpfiltereditstartaddress.yfilter != YFilter.not_set or
                self.cigmpfiltereditstartaddresstype.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cIgmpFilterEditor" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-IGMP-FILTER-MIB:CISCO-IGMP-FILTER-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.cigmpfilterapplystatus.is_set or self.cigmpfilterapplystatus.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cigmpfilterapplystatus.get_name_leafdata())
            if (self.cigmpfiltereditendaddress.is_set or self.cigmpfiltereditendaddress.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cigmpfiltereditendaddress.get_name_leafdata())
            if (self.cigmpfiltereditendaddresstype.is_set or self.cigmpfiltereditendaddresstype.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cigmpfiltereditendaddresstype.get_name_leafdata())
            if (self.cigmpfiltereditoperation.is_set or self.cigmpfiltereditoperation.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cigmpfiltereditoperation.get_name_leafdata())
            if (self.cigmpfiltereditprofileaction.is_set or self.cigmpfiltereditprofileaction.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cigmpfiltereditprofileaction.get_name_leafdata())
            if (self.cigmpfiltereditprofileindex.is_set or self.cigmpfiltereditprofileindex.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cigmpfiltereditprofileindex.get_name_leafdata())
            if (self.cigmpfiltereditspinlock.is_set or self.cigmpfiltereditspinlock.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cigmpfiltereditspinlock.get_name_leafdata())
            if (self.cigmpfiltereditstartaddress.is_set or self.cigmpfiltereditstartaddress.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cigmpfiltereditstartaddress.get_name_leafdata())
            if (self.cigmpfiltereditstartaddresstype.is_set or self.cigmpfiltereditstartaddresstype.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cigmpfiltereditstartaddresstype.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cIgmpFilterApplyStatus" or name == "cIgmpFilterEditEndAddress" or name == "cIgmpFilterEditEndAddressType" or name == "cIgmpFilterEditOperation" or name == "cIgmpFilterEditProfileAction" or name == "cIgmpFilterEditProfileIndex" or name == "cIgmpFilterEditSpinLock" or name == "cIgmpFilterEditStartAddress" or name == "cIgmpFilterEditStartAddressType"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "cIgmpFilterApplyStatus"):
                self.cigmpfilterapplystatus = value
                self.cigmpfilterapplystatus.value_namespace = name_space
                self.cigmpfilterapplystatus.value_namespace_prefix = name_space_prefix
            if(value_path == "cIgmpFilterEditEndAddress"):
                self.cigmpfiltereditendaddress = value
                self.cigmpfiltereditendaddress.value_namespace = name_space
                self.cigmpfiltereditendaddress.value_namespace_prefix = name_space_prefix
            if(value_path == "cIgmpFilterEditEndAddressType"):
                self.cigmpfiltereditendaddresstype = value
                self.cigmpfiltereditendaddresstype.value_namespace = name_space
                self.cigmpfiltereditendaddresstype.value_namespace_prefix = name_space_prefix
            if(value_path == "cIgmpFilterEditOperation"):
                self.cigmpfiltereditoperation = value
                self.cigmpfiltereditoperation.value_namespace = name_space
                self.cigmpfiltereditoperation.value_namespace_prefix = name_space_prefix
            if(value_path == "cIgmpFilterEditProfileAction"):
                self.cigmpfiltereditprofileaction = value
                self.cigmpfiltereditprofileaction.value_namespace = name_space
                self.cigmpfiltereditprofileaction.value_namespace_prefix = name_space_prefix
            if(value_path == "cIgmpFilterEditProfileIndex"):
                self.cigmpfiltereditprofileindex = value
                self.cigmpfiltereditprofileindex.value_namespace = name_space
                self.cigmpfiltereditprofileindex.value_namespace_prefix = name_space_prefix
            if(value_path == "cIgmpFilterEditSpinLock"):
                self.cigmpfiltereditspinlock = value
                self.cigmpfiltereditspinlock.value_namespace = name_space
                self.cigmpfiltereditspinlock.value_namespace_prefix = name_space_prefix
            if(value_path == "cIgmpFilterEditStartAddress"):
                self.cigmpfiltereditstartaddress = value
                self.cigmpfiltereditstartaddress.value_namespace = name_space
                self.cigmpfiltereditstartaddress.value_namespace_prefix = name_space_prefix
            if(value_path == "cIgmpFilterEditStartAddressType"):
                self.cigmpfiltereditstartaddresstype = value
                self.cigmpfiltereditstartaddresstype.value_namespace = name_space
                self.cigmpfiltereditstartaddresstype.value_namespace_prefix = name_space_prefix


    class Cigmpfiltertable(Entity):
        """
        This table contains entries that identify lists of
        IP Multicast groups for each profile configured on
        the device. 
        
        Each entry contains a range of contiguous IP
        Multicast groups associated to a profile index.
        Multiple cIgmpFilterEntry may be associated
        with the same cIgmpFilterProfileIndex.
        
        All the cIgmpFilterEntry with  the same profile index 
        are subjected to the same IGMP filtering action as 
        defined in cIgmpFilterProfileAction.
        
        Each profile index may be associated with zero or more 
        interfaces through cIgmpFilterInterfaceIfIndex
        object in cIgmpFilterInterfaceTable.
        The maximum number of entries is determined by
        cIgmpFilterMaxProfiles.
        
        .. attribute:: cigmpfilterentry
        
        	An entry (conceptual row) in the cIgmpFilterTable.  The creation, deletion or modification of an entry is controlled through the MIB objects defined under cIgmpFilterEditor group
        	**type**\: list of    :py:class:`Cigmpfilterentry <ydk.models.cisco_ios_xe.CISCO_IGMP_FILTER_MIB.CiscoIgmpFilterMib.Cigmpfiltertable.Cigmpfilterentry>`
        
        

        """

        _prefix = 'CISCO-IGMP-FILTER-MIB'
        _revision = '2005-11-29'

        def __init__(self):
            super(CiscoIgmpFilterMib.Cigmpfiltertable, self).__init__()

            self.yang_name = "cIgmpFilterTable"
            self.yang_parent_name = "CISCO-IGMP-FILTER-MIB"

            self.cigmpfilterentry = YList(self)

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
                        super(CiscoIgmpFilterMib.Cigmpfiltertable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoIgmpFilterMib.Cigmpfiltertable, self).__setattr__(name, value)


        class Cigmpfilterentry(Entity):
            """
            An entry (conceptual row) in the cIgmpFilterTable.
            
            The creation, deletion or modification of an entry
            is controlled through the MIB objects defined under
            cIgmpFilterEditor group.
            
            .. attribute:: cigmpfilterprofileindex  <key>
            
            	Index identifying this entry
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cigmpfilterstartaddresstype  <key>
            
            	This object describes the type of Internet address used to determine the start address  of IP multicast group for a profile
            	**type**\:   :py:class:`Inetaddresstype <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.Inetaddresstype>`
            
            .. attribute:: cigmpfilterstartaddress  <key>
            
            	This object describes the start of the IP multicast group address of a contiguous range which will be subjected to filtering operation
            	**type**\:  str
            
            	**length:** 1..64
            
            .. attribute:: cigmpfilterendaddress
            
            	This object indicates the end of the IP multicast group address of a contiguous range which will be  subjected to filtering operation
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: cigmpfilterendaddresstype
            
            	This object indicates the type of Internet address used to determine the end address  of IP multicast group for a profile
            	**type**\:   :py:class:`Inetaddresstype <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.Inetaddresstype>`
            
            .. attribute:: cigmpfilterprofileaction
            
            	This object defines the action for filtering IGMP reports for this profile.  If the object is set to deny(2)\: then all IGMP reports associated to IP multicast groups included in the profile identified by cIgmpFilterInterfaceProfileIndex will be dropped.  If the object is set to permit(1)\: then all IGMP reports associated to IP multicast groups not included in the profile identified by cIgmpFilterInterfaceProfileIndex will be dropped
            	**type**\:   :py:class:`Cigmpfilterprofileaction <ydk.models.cisco_ios_xe.CISCO_IGMP_FILTER_MIB.CiscoIgmpFilterMib.Cigmpfiltertable.Cigmpfilterentry.Cigmpfilterprofileaction>`
            
            

            """

            _prefix = 'CISCO-IGMP-FILTER-MIB'
            _revision = '2005-11-29'

            def __init__(self):
                super(CiscoIgmpFilterMib.Cigmpfiltertable.Cigmpfilterentry, self).__init__()

                self.yang_name = "cIgmpFilterEntry"
                self.yang_parent_name = "cIgmpFilterTable"

                self.cigmpfilterprofileindex = YLeaf(YType.uint32, "cIgmpFilterProfileIndex")

                self.cigmpfilterstartaddresstype = YLeaf(YType.enumeration, "cIgmpFilterStartAddressType")

                self.cigmpfilterstartaddress = YLeaf(YType.str, "cIgmpFilterStartAddress")

                self.cigmpfilterendaddress = YLeaf(YType.str, "cIgmpFilterEndAddress")

                self.cigmpfilterendaddresstype = YLeaf(YType.enumeration, "cIgmpFilterEndAddressType")

                self.cigmpfilterprofileaction = YLeaf(YType.enumeration, "cIgmpFilterProfileAction")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("cigmpfilterprofileindex",
                                "cigmpfilterstartaddresstype",
                                "cigmpfilterstartaddress",
                                "cigmpfilterendaddress",
                                "cigmpfilterendaddresstype",
                                "cigmpfilterprofileaction") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoIgmpFilterMib.Cigmpfiltertable.Cigmpfilterentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoIgmpFilterMib.Cigmpfiltertable.Cigmpfilterentry, self).__setattr__(name, value)

            class Cigmpfilterprofileaction(Enum):
                """
                Cigmpfilterprofileaction

                This object defines the action for

                filtering IGMP reports for this profile.

                If the object is set to deny(2)\:

                then all IGMP reports associated to IP multicast

                groups included in the profile identified by

                cIgmpFilterInterfaceProfileIndex will be dropped.

                If the object is set to permit(1)\:

                then all IGMP reports associated to IP multicast

                groups not included in the profile identified by

                cIgmpFilterInterfaceProfileIndex will be dropped.

                .. data:: permit = 1

                .. data:: deny = 2

                """

                permit = Enum.YLeaf(1, "permit")

                deny = Enum.YLeaf(2, "deny")


            def has_data(self):
                return (
                    self.cigmpfilterprofileindex.is_set or
                    self.cigmpfilterstartaddresstype.is_set or
                    self.cigmpfilterstartaddress.is_set or
                    self.cigmpfilterendaddress.is_set or
                    self.cigmpfilterendaddresstype.is_set or
                    self.cigmpfilterprofileaction.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.cigmpfilterprofileindex.yfilter != YFilter.not_set or
                    self.cigmpfilterstartaddresstype.yfilter != YFilter.not_set or
                    self.cigmpfilterstartaddress.yfilter != YFilter.not_set or
                    self.cigmpfilterendaddress.yfilter != YFilter.not_set or
                    self.cigmpfilterendaddresstype.yfilter != YFilter.not_set or
                    self.cigmpfilterprofileaction.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cIgmpFilterEntry" + "[cIgmpFilterProfileIndex='" + self.cigmpfilterprofileindex.get() + "']" + "[cIgmpFilterStartAddressType='" + self.cigmpfilterstartaddresstype.get() + "']" + "[cIgmpFilterStartAddress='" + self.cigmpfilterstartaddress.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-IGMP-FILTER-MIB:CISCO-IGMP-FILTER-MIB/cIgmpFilterTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.cigmpfilterprofileindex.is_set or self.cigmpfilterprofileindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cigmpfilterprofileindex.get_name_leafdata())
                if (self.cigmpfilterstartaddresstype.is_set or self.cigmpfilterstartaddresstype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cigmpfilterstartaddresstype.get_name_leafdata())
                if (self.cigmpfilterstartaddress.is_set or self.cigmpfilterstartaddress.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cigmpfilterstartaddress.get_name_leafdata())
                if (self.cigmpfilterendaddress.is_set or self.cigmpfilterendaddress.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cigmpfilterendaddress.get_name_leafdata())
                if (self.cigmpfilterendaddresstype.is_set or self.cigmpfilterendaddresstype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cigmpfilterendaddresstype.get_name_leafdata())
                if (self.cigmpfilterprofileaction.is_set or self.cigmpfilterprofileaction.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cigmpfilterprofileaction.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cIgmpFilterProfileIndex" or name == "cIgmpFilterStartAddressType" or name == "cIgmpFilterStartAddress" or name == "cIgmpFilterEndAddress" or name == "cIgmpFilterEndAddressType" or name == "cIgmpFilterProfileAction"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "cIgmpFilterProfileIndex"):
                    self.cigmpfilterprofileindex = value
                    self.cigmpfilterprofileindex.value_namespace = name_space
                    self.cigmpfilterprofileindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cIgmpFilterStartAddressType"):
                    self.cigmpfilterstartaddresstype = value
                    self.cigmpfilterstartaddresstype.value_namespace = name_space
                    self.cigmpfilterstartaddresstype.value_namespace_prefix = name_space_prefix
                if(value_path == "cIgmpFilterStartAddress"):
                    self.cigmpfilterstartaddress = value
                    self.cigmpfilterstartaddress.value_namespace = name_space
                    self.cigmpfilterstartaddress.value_namespace_prefix = name_space_prefix
                if(value_path == "cIgmpFilterEndAddress"):
                    self.cigmpfilterendaddress = value
                    self.cigmpfilterendaddress.value_namespace = name_space
                    self.cigmpfilterendaddress.value_namespace_prefix = name_space_prefix
                if(value_path == "cIgmpFilterEndAddressType"):
                    self.cigmpfilterendaddresstype = value
                    self.cigmpfilterendaddresstype.value_namespace = name_space
                    self.cigmpfilterendaddresstype.value_namespace_prefix = name_space_prefix
                if(value_path == "cIgmpFilterProfileAction"):
                    self.cigmpfilterprofileaction = value
                    self.cigmpfilterprofileaction.value_namespace = name_space
                    self.cigmpfilterprofileaction.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cigmpfilterentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cigmpfilterentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cIgmpFilterTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-IGMP-FILTER-MIB:CISCO-IGMP-FILTER-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cIgmpFilterEntry"):
                for c in self.cigmpfilterentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoIgmpFilterMib.Cigmpfiltertable.Cigmpfilterentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cigmpfilterentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cIgmpFilterEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Cigmpfilterinterfacetable(Entity):
        """
        This table contains the list of interfaces that can
        support IGMP filter feature.
        
        .. attribute:: cigmpfilterinterfaceentry
        
        	Each entry contains the configuration for associating the IGMP filter profile index with the interface.  An entry is created for each of the IGMP filter capable  interface on the system.  The entry is removed on removal of corresponding  interface from system
        	**type**\: list of    :py:class:`Cigmpfilterinterfaceentry <ydk.models.cisco_ios_xe.CISCO_IGMP_FILTER_MIB.CiscoIgmpFilterMib.Cigmpfilterinterfacetable.Cigmpfilterinterfaceentry>`
        
        

        """

        _prefix = 'CISCO-IGMP-FILTER-MIB'
        _revision = '2005-11-29'

        def __init__(self):
            super(CiscoIgmpFilterMib.Cigmpfilterinterfacetable, self).__init__()

            self.yang_name = "cIgmpFilterInterfaceTable"
            self.yang_parent_name = "CISCO-IGMP-FILTER-MIB"

            self.cigmpfilterinterfaceentry = YList(self)

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
                        super(CiscoIgmpFilterMib.Cigmpfilterinterfacetable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoIgmpFilterMib.Cigmpfilterinterfacetable, self).__setattr__(name, value)


        class Cigmpfilterinterfaceentry(Entity):
            """
            Each entry contains the configuration for associating
            the IGMP filter profile index with the interface.
            
            An entry is created for each of the IGMP filter capable 
            interface on the system.
            
            The entry is removed on removal of corresponding 
            interface from system.
            
            .. attribute:: ifindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IfMib.Iftable.Ifentry>`
            
            .. attribute:: cigmpfilterinterfaceprofileindex
            
            	Specifies which IGMP filter profile applies to this interface. If the value of this MIB object matches the  value of cIgmpFilterProfileIndex in cIgmpFilterTable,  the corresponding profile configuration will apply to this interface.   Agent returns inconsistentValue if this profile  does not exist in cIgmpFilterTable.  A value of zero indicates no profile is associated with corresponding interface.  The filtering action on each interface is also defined by the associated profile
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'CISCO-IGMP-FILTER-MIB'
            _revision = '2005-11-29'

            def __init__(self):
                super(CiscoIgmpFilterMib.Cigmpfilterinterfacetable.Cigmpfilterinterfaceentry, self).__init__()

                self.yang_name = "cIgmpFilterInterfaceEntry"
                self.yang_parent_name = "cIgmpFilterInterfaceTable"

                self.ifindex = YLeaf(YType.str, "ifIndex")

                self.cigmpfilterinterfaceprofileindex = YLeaf(YType.uint32, "cIgmpFilterInterfaceProfileIndex")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("ifindex",
                                "cigmpfilterinterfaceprofileindex") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoIgmpFilterMib.Cigmpfilterinterfacetable.Cigmpfilterinterfaceentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoIgmpFilterMib.Cigmpfilterinterfacetable.Cigmpfilterinterfaceentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.ifindex.is_set or
                    self.cigmpfilterinterfaceprofileindex.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ifindex.yfilter != YFilter.not_set or
                    self.cigmpfilterinterfaceprofileindex.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cIgmpFilterInterfaceEntry" + "[ifIndex='" + self.ifindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-IGMP-FILTER-MIB:CISCO-IGMP-FILTER-MIB/cIgmpFilterInterfaceTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ifindex.is_set or self.ifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ifindex.get_name_leafdata())
                if (self.cigmpfilterinterfaceprofileindex.is_set or self.cigmpfilterinterfaceprofileindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cigmpfilterinterfaceprofileindex.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ifIndex" or name == "cIgmpFilterInterfaceProfileIndex"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "ifIndex"):
                    self.ifindex = value
                    self.ifindex.value_namespace = name_space
                    self.ifindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cIgmpFilterInterfaceProfileIndex"):
                    self.cigmpfilterinterfaceprofileindex = value
                    self.cigmpfilterinterfaceprofileindex.value_namespace = name_space
                    self.cigmpfilterinterfaceprofileindex.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cigmpfilterinterfaceentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cigmpfilterinterfaceentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cIgmpFilterInterfaceTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-IGMP-FILTER-MIB:CISCO-IGMP-FILTER-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cIgmpFilterInterfaceEntry"):
                for c in self.cigmpfilterinterfaceentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoIgmpFilterMib.Cigmpfilterinterfacetable.Cigmpfilterinterfaceentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cigmpfilterinterfaceentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cIgmpFilterInterfaceEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            (self.cigmpfiltereditor is not None and self.cigmpfiltereditor.has_data()) or
            (self.cigmpfiltergeneral is not None and self.cigmpfiltergeneral.has_data()) or
            (self.cigmpfilterinterfacetable is not None and self.cigmpfilterinterfacetable.has_data()) or
            (self.cigmpfiltertable is not None and self.cigmpfiltertable.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.cigmpfiltereditor is not None and self.cigmpfiltereditor.has_operation()) or
            (self.cigmpfiltergeneral is not None and self.cigmpfiltergeneral.has_operation()) or
            (self.cigmpfilterinterfacetable is not None and self.cigmpfilterinterfacetable.has_operation()) or
            (self.cigmpfiltertable is not None and self.cigmpfiltertable.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "CISCO-IGMP-FILTER-MIB:CISCO-IGMP-FILTER-MIB" + path_buffer

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

        if (child_yang_name == "cIgmpFilterEditor"):
            if (self.cigmpfiltereditor is None):
                self.cigmpfiltereditor = CiscoIgmpFilterMib.Cigmpfiltereditor()
                self.cigmpfiltereditor.parent = self
                self._children_name_map["cigmpfiltereditor"] = "cIgmpFilterEditor"
            return self.cigmpfiltereditor

        if (child_yang_name == "cIgmpFilterGeneral"):
            if (self.cigmpfiltergeneral is None):
                self.cigmpfiltergeneral = CiscoIgmpFilterMib.Cigmpfiltergeneral()
                self.cigmpfiltergeneral.parent = self
                self._children_name_map["cigmpfiltergeneral"] = "cIgmpFilterGeneral"
            return self.cigmpfiltergeneral

        if (child_yang_name == "cIgmpFilterInterfaceTable"):
            if (self.cigmpfilterinterfacetable is None):
                self.cigmpfilterinterfacetable = CiscoIgmpFilterMib.Cigmpfilterinterfacetable()
                self.cigmpfilterinterfacetable.parent = self
                self._children_name_map["cigmpfilterinterfacetable"] = "cIgmpFilterInterfaceTable"
            return self.cigmpfilterinterfacetable

        if (child_yang_name == "cIgmpFilterTable"):
            if (self.cigmpfiltertable is None):
                self.cigmpfiltertable = CiscoIgmpFilterMib.Cigmpfiltertable()
                self.cigmpfiltertable.parent = self
                self._children_name_map["cigmpfiltertable"] = "cIgmpFilterTable"
            return self.cigmpfiltertable

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "cIgmpFilterEditor" or name == "cIgmpFilterGeneral" or name == "cIgmpFilterInterfaceTable" or name == "cIgmpFilterTable"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = CiscoIgmpFilterMib()
        return self._top_entity

