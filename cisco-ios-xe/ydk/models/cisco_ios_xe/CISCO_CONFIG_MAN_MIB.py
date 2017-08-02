""" CISCO_CONFIG_MAN_MIB 

Configuration management MIB.

The MIB represents a model of configuration data that
exists in various locations\:

running       in use by the running system
terminal      saved to whatever is attached as the terminal        
local         saved locally in NVRAM or flash
remote        saved to some server on the network

Although some of the system functions that relate here
can be used for general file storage and transfer, this
MIB intends to include only such operations as clearly
relate to configuration.  Its primary emphasis is to
track changes and saves of the running configuration.

As saved data moves further from startup use, such as
into different local flash files or onto the network,
tracking becomes difficult to impossible, so the MIB's
interest and functions are confined in that area.

Information from ccmCLIHistoryCommandTable can be used
to track the exact configuration changes that took
place within a particular Configuration History
event. NMS' can use this information to update 
the related components. 
For example\:
    If commands related only to MPLS are entered
    then the NMS need to update only the MPLS related
    management information rather than updating
    all of its management information.
    Acronyms and terms\:

    CLI   Command Line Interface.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class Historyeventmedium(Enum):
    """
    Historyeventmedium

    The source or destination of a configuration change,

    save, or copy.

    erase        erasing destination (source only)

    running        live operational data

    commandSource    the command source itself

    startup        what the system will use next reboot

    local        local NVRAM or flash

    networkTftp    network host via Trivial File Transfer

    networkRcp    network host via Remote Copy

    networkFtp       network host via File transfer

    networkScp       network host via Secure Copy

    .. data:: erase = 1

    .. data:: commandSource = 2

    .. data:: running = 3

    .. data:: startup = 4

    .. data:: local = 5

    .. data:: networkTftp = 6

    .. data:: networkRcp = 7

    .. data:: networkFtp = 8

    .. data:: networkScp = 9

    """

    erase = Enum.YLeaf(1, "erase")

    commandSource = Enum.YLeaf(2, "commandSource")

    running = Enum.YLeaf(3, "running")

    startup = Enum.YLeaf(4, "startup")

    local = Enum.YLeaf(5, "local")

    networkTftp = Enum.YLeaf(6, "networkTftp")

    networkRcp = Enum.YLeaf(7, "networkRcp")

    networkFtp = Enum.YLeaf(8, "networkFtp")

    networkScp = Enum.YLeaf(9, "networkScp")



class CiscoConfigManMib(Entity):
    """
    
    
    .. attribute:: ccmclicfg
    
    	
    	**type**\:   :py:class:`Ccmclicfg <ydk.models.cisco_ios_xe.CISCO_CONFIG_MAN_MIB.CiscoConfigManMib.Ccmclicfg>`
    
    .. attribute:: ccmclihistory
    
    	
    	**type**\:   :py:class:`Ccmclihistory <ydk.models.cisco_ios_xe.CISCO_CONFIG_MAN_MIB.CiscoConfigManMib.Ccmclihistory>`
    
    .. attribute:: ccmclihistorycommandtable
    
    	A table of CLI commands that took effect during configuration events
    	**type**\:   :py:class:`Ccmclihistorycommandtable <ydk.models.cisco_ios_xe.CISCO_CONFIG_MAN_MIB.CiscoConfigManMib.Ccmclihistorycommandtable>`
    
    .. attribute:: ccmctidobjects
    
    	
    	**type**\:   :py:class:`Ccmctidobjects <ydk.models.cisco_ios_xe.CISCO_CONFIG_MAN_MIB.CiscoConfigManMib.Ccmctidobjects>`
    
    .. attribute:: ccmhistory
    
    	
    	**type**\:   :py:class:`Ccmhistory <ydk.models.cisco_ios_xe.CISCO_CONFIG_MAN_MIB.CiscoConfigManMib.Ccmhistory>`
    
    .. attribute:: ccmhistoryeventtable
    
    	A table of configuration events on this router
    	**type**\:   :py:class:`Ccmhistoryeventtable <ydk.models.cisco_ios_xe.CISCO_CONFIG_MAN_MIB.CiscoConfigManMib.Ccmhistoryeventtable>`
    
    

    """

    _prefix = 'CISCO-CONFIG-MAN-MIB'
    _revision = '2007-04-27'

    def __init__(self):
        super(CiscoConfigManMib, self).__init__()
        self._top_entity = None

        self.yang_name = "CISCO-CONFIG-MAN-MIB"
        self.yang_parent_name = "CISCO-CONFIG-MAN-MIB"

        self.ccmclicfg = CiscoConfigManMib.Ccmclicfg()
        self.ccmclicfg.parent = self
        self._children_name_map["ccmclicfg"] = "ccmCLICfg"
        self._children_yang_names.add("ccmCLICfg")

        self.ccmclihistory = CiscoConfigManMib.Ccmclihistory()
        self.ccmclihistory.parent = self
        self._children_name_map["ccmclihistory"] = "ccmCLIHistory"
        self._children_yang_names.add("ccmCLIHistory")

        self.ccmclihistorycommandtable = CiscoConfigManMib.Ccmclihistorycommandtable()
        self.ccmclihistorycommandtable.parent = self
        self._children_name_map["ccmclihistorycommandtable"] = "ccmCLIHistoryCommandTable"
        self._children_yang_names.add("ccmCLIHistoryCommandTable")

        self.ccmctidobjects = CiscoConfigManMib.Ccmctidobjects()
        self.ccmctidobjects.parent = self
        self._children_name_map["ccmctidobjects"] = "ccmCTIDObjects"
        self._children_yang_names.add("ccmCTIDObjects")

        self.ccmhistory = CiscoConfigManMib.Ccmhistory()
        self.ccmhistory.parent = self
        self._children_name_map["ccmhistory"] = "ccmHistory"
        self._children_yang_names.add("ccmHistory")

        self.ccmhistoryeventtable = CiscoConfigManMib.Ccmhistoryeventtable()
        self.ccmhistoryeventtable.parent = self
        self._children_name_map["ccmhistoryeventtable"] = "ccmHistoryEventTable"
        self._children_yang_names.add("ccmHistoryEventTable")


    class Ccmhistory(Entity):
        """
        
        
        .. attribute:: ccmhistoryevententriesbumped
        
        	The number of times the oldest entry in ccmHistoryEventTable was deleted to make room  for a new entry
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: ccmhistorymaxevententries
        
        	The maximum number of entries that can be held in ccmHistoryEventTable.  The recommended value for implementations is 10
        	**type**\:  int
        
        	**range:** 0..2147483647
        
        .. attribute:: ccmhistoryrunninglastchanged
        
        	The value of sysUpTime when the running configuration was last changed.          If the value of ccmHistoryRunningLastChanged is         greater than ccmHistoryRunningLastSaved, the          configuration has been changed but not saved
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: ccmhistoryrunninglastsaved
        
        	The value of sysUpTime when the running configuration was last saved (written).  If the value of ccmHistoryRunningLastChanged is  greater than ccmHistoryRunningLastSaved, the  configuration has been changed but not saved.  What constitutes a safe saving of the running configuration is a management policy issue beyond the scope of this MIB.  For some installations, writing the running configuration to a terminal may be a way of capturing and saving it.  Others may use local or remote storage.  Thus ANY write is considered saving for the purposes of the MIB
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: ccmhistorystartuplastchanged
        
        	The value of sysUpTime when the startup configuration was last written to.  In general this is the default configuration used when cold starting the system.  It may have been changed by a save of the running configuration or by a copy from elsewhere
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'CISCO-CONFIG-MAN-MIB'
        _revision = '2007-04-27'

        def __init__(self):
            super(CiscoConfigManMib.Ccmhistory, self).__init__()

            self.yang_name = "ccmHistory"
            self.yang_parent_name = "CISCO-CONFIG-MAN-MIB"

            self.ccmhistoryevententriesbumped = YLeaf(YType.uint32, "ccmHistoryEventEntriesBumped")

            self.ccmhistorymaxevententries = YLeaf(YType.int32, "ccmHistoryMaxEventEntries")

            self.ccmhistoryrunninglastchanged = YLeaf(YType.uint32, "ccmHistoryRunningLastChanged")

            self.ccmhistoryrunninglastsaved = YLeaf(YType.uint32, "ccmHistoryRunningLastSaved")

            self.ccmhistorystartuplastchanged = YLeaf(YType.uint32, "ccmHistoryStartupLastChanged")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("ccmhistoryevententriesbumped",
                            "ccmhistorymaxevententries",
                            "ccmhistoryrunninglastchanged",
                            "ccmhistoryrunninglastsaved",
                            "ccmhistorystartuplastchanged") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoConfigManMib.Ccmhistory, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoConfigManMib.Ccmhistory, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.ccmhistoryevententriesbumped.is_set or
                self.ccmhistorymaxevententries.is_set or
                self.ccmhistoryrunninglastchanged.is_set or
                self.ccmhistoryrunninglastsaved.is_set or
                self.ccmhistorystartuplastchanged.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.ccmhistoryevententriesbumped.yfilter != YFilter.not_set or
                self.ccmhistorymaxevententries.yfilter != YFilter.not_set or
                self.ccmhistoryrunninglastchanged.yfilter != YFilter.not_set or
                self.ccmhistoryrunninglastsaved.yfilter != YFilter.not_set or
                self.ccmhistorystartuplastchanged.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "ccmHistory" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-CONFIG-MAN-MIB:CISCO-CONFIG-MAN-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.ccmhistoryevententriesbumped.is_set or self.ccmhistoryevententriesbumped.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ccmhistoryevententriesbumped.get_name_leafdata())
            if (self.ccmhistorymaxevententries.is_set or self.ccmhistorymaxevententries.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ccmhistorymaxevententries.get_name_leafdata())
            if (self.ccmhistoryrunninglastchanged.is_set or self.ccmhistoryrunninglastchanged.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ccmhistoryrunninglastchanged.get_name_leafdata())
            if (self.ccmhistoryrunninglastsaved.is_set or self.ccmhistoryrunninglastsaved.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ccmhistoryrunninglastsaved.get_name_leafdata())
            if (self.ccmhistorystartuplastchanged.is_set or self.ccmhistorystartuplastchanged.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ccmhistorystartuplastchanged.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "ccmHistoryEventEntriesBumped" or name == "ccmHistoryMaxEventEntries" or name == "ccmHistoryRunningLastChanged" or name == "ccmHistoryRunningLastSaved" or name == "ccmHistoryStartupLastChanged"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "ccmHistoryEventEntriesBumped"):
                self.ccmhistoryevententriesbumped = value
                self.ccmhistoryevententriesbumped.value_namespace = name_space
                self.ccmhistoryevententriesbumped.value_namespace_prefix = name_space_prefix
            if(value_path == "ccmHistoryMaxEventEntries"):
                self.ccmhistorymaxevententries = value
                self.ccmhistorymaxevententries.value_namespace = name_space
                self.ccmhistorymaxevententries.value_namespace_prefix = name_space_prefix
            if(value_path == "ccmHistoryRunningLastChanged"):
                self.ccmhistoryrunninglastchanged = value
                self.ccmhistoryrunninglastchanged.value_namespace = name_space
                self.ccmhistoryrunninglastchanged.value_namespace_prefix = name_space_prefix
            if(value_path == "ccmHistoryRunningLastSaved"):
                self.ccmhistoryrunninglastsaved = value
                self.ccmhistoryrunninglastsaved.value_namespace = name_space
                self.ccmhistoryrunninglastsaved.value_namespace_prefix = name_space_prefix
            if(value_path == "ccmHistoryStartupLastChanged"):
                self.ccmhistorystartuplastchanged = value
                self.ccmhistorystartuplastchanged.value_namespace = name_space
                self.ccmhistorystartuplastchanged.value_namespace_prefix = name_space_prefix


    class Ccmclihistory(Entity):
        """
        
        
        .. attribute:: ccmclihistorycmdentries
        
        	The current number of entries in ccmCLIHistoryCommandTable
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: ccmclihistorycmdentriesallowed
        
        	This object indicates the upper limit on the number of entries allowed in  ccmCLIHistoryCommandTable by the managed system
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: ccmclihistorymaxcmdentries
        
        	The maximum number of entries that can be held in ccmCLIHistoryCommandTable.  The recommended value for implementations is 100.  If the number of entries in ccmCLIHistoryCommandTable  exceeds the value of this object, old entries will be  bumped to make room for new entries.  The ccmCLIHistoryCommandTable will not be populated if the value of this object is 0
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'CISCO-CONFIG-MAN-MIB'
        _revision = '2007-04-27'

        def __init__(self):
            super(CiscoConfigManMib.Ccmclihistory, self).__init__()

            self.yang_name = "ccmCLIHistory"
            self.yang_parent_name = "CISCO-CONFIG-MAN-MIB"

            self.ccmclihistorycmdentries = YLeaf(YType.uint32, "ccmCLIHistoryCmdEntries")

            self.ccmclihistorycmdentriesallowed = YLeaf(YType.uint32, "ccmCLIHistoryCmdEntriesAllowed")

            self.ccmclihistorymaxcmdentries = YLeaf(YType.uint32, "ccmCLIHistoryMaxCmdEntries")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("ccmclihistorycmdentries",
                            "ccmclihistorycmdentriesallowed",
                            "ccmclihistorymaxcmdentries") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoConfigManMib.Ccmclihistory, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoConfigManMib.Ccmclihistory, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.ccmclihistorycmdentries.is_set or
                self.ccmclihistorycmdentriesallowed.is_set or
                self.ccmclihistorymaxcmdentries.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.ccmclihistorycmdentries.yfilter != YFilter.not_set or
                self.ccmclihistorycmdentriesallowed.yfilter != YFilter.not_set or
                self.ccmclihistorymaxcmdentries.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "ccmCLIHistory" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-CONFIG-MAN-MIB:CISCO-CONFIG-MAN-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.ccmclihistorycmdentries.is_set or self.ccmclihistorycmdentries.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ccmclihistorycmdentries.get_name_leafdata())
            if (self.ccmclihistorycmdentriesallowed.is_set or self.ccmclihistorycmdentriesallowed.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ccmclihistorycmdentriesallowed.get_name_leafdata())
            if (self.ccmclihistorymaxcmdentries.is_set or self.ccmclihistorymaxcmdentries.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ccmclihistorymaxcmdentries.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "ccmCLIHistoryCmdEntries" or name == "ccmCLIHistoryCmdEntriesAllowed" or name == "ccmCLIHistoryMaxCmdEntries"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "ccmCLIHistoryCmdEntries"):
                self.ccmclihistorycmdentries = value
                self.ccmclihistorycmdentries.value_namespace = name_space
                self.ccmclihistorycmdentries.value_namespace_prefix = name_space_prefix
            if(value_path == "ccmCLIHistoryCmdEntriesAllowed"):
                self.ccmclihistorycmdentriesallowed = value
                self.ccmclihistorycmdentriesallowed.value_namespace = name_space
                self.ccmclihistorycmdentriesallowed.value_namespace_prefix = name_space_prefix
            if(value_path == "ccmCLIHistoryMaxCmdEntries"):
                self.ccmclihistorymaxcmdentries = value
                self.ccmclihistorymaxcmdentries.value_namespace = name_space
                self.ccmclihistorymaxcmdentries.value_namespace_prefix = name_space_prefix


    class Ccmclicfg(Entity):
        """
        
        
        .. attribute:: ccmclicfgrunconfnotifenable
        
        	This variable indicates whether the system produces the ccmCLIRunningConfigChanged notification. A false  value will prevent notifications from being generated  by this system
        	**type**\:  bool
        
        

        """

        _prefix = 'CISCO-CONFIG-MAN-MIB'
        _revision = '2007-04-27'

        def __init__(self):
            super(CiscoConfigManMib.Ccmclicfg, self).__init__()

            self.yang_name = "ccmCLICfg"
            self.yang_parent_name = "CISCO-CONFIG-MAN-MIB"

            self.ccmclicfgrunconfnotifenable = YLeaf(YType.boolean, "ccmCLICfgRunConfNotifEnable")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("ccmclicfgrunconfnotifenable") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoConfigManMib.Ccmclicfg, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoConfigManMib.Ccmclicfg, self).__setattr__(name, value)

        def has_data(self):
            return self.ccmclicfgrunconfnotifenable.is_set

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.ccmclicfgrunconfnotifenable.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "ccmCLICfg" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-CONFIG-MAN-MIB:CISCO-CONFIG-MAN-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.ccmclicfgrunconfnotifenable.is_set or self.ccmclicfgrunconfnotifenable.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ccmclicfgrunconfnotifenable.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "ccmCLICfgRunConfNotifEnable"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "ccmCLICfgRunConfNotifEnable"):
                self.ccmclicfgrunconfnotifenable = value
                self.ccmclicfgrunconfnotifenable.value_namespace = name_space
                self.ccmclicfgrunconfnotifenable.value_namespace_prefix = name_space_prefix


    class Ccmctidobjects(Entity):
        """
        
        
        .. attribute:: ccmctid
        
        	This object indicates the Config Change Tracking ID which uniquely represents version\-incrementing changes to the IOS  running configuration
        	**type**\:  int
        
        	**range:** 0..18446744073709551615
        
        .. attribute:: ccmctidlastchangetime
        
        	This object indicates the time when the Config Change Tracking ID last changed
        	**type**\:  str
        
        .. attribute:: ccmctidrolledovernotifenable
        
        	This variable indicates whether the system produces the ccmCTIDRolledOver notification. A false value will prevent notifications from being generated by this system
        	**type**\:  bool
        
        .. attribute:: ccmctidwhochanged
        
        	This object indicates the user who last reset the Config Change Tracking ID
        	**type**\:  str
        
        

        """

        _prefix = 'CISCO-CONFIG-MAN-MIB'
        _revision = '2007-04-27'

        def __init__(self):
            super(CiscoConfigManMib.Ccmctidobjects, self).__init__()

            self.yang_name = "ccmCTIDObjects"
            self.yang_parent_name = "CISCO-CONFIG-MAN-MIB"

            self.ccmctid = YLeaf(YType.uint64, "ccmCTID")

            self.ccmctidlastchangetime = YLeaf(YType.str, "ccmCTIDLastChangeTime")

            self.ccmctidrolledovernotifenable = YLeaf(YType.boolean, "ccmCTIDRolledOverNotifEnable")

            self.ccmctidwhochanged = YLeaf(YType.str, "ccmCTIDWhoChanged")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("ccmctid",
                            "ccmctidlastchangetime",
                            "ccmctidrolledovernotifenable",
                            "ccmctidwhochanged") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoConfigManMib.Ccmctidobjects, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoConfigManMib.Ccmctidobjects, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.ccmctid.is_set or
                self.ccmctidlastchangetime.is_set or
                self.ccmctidrolledovernotifenable.is_set or
                self.ccmctidwhochanged.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.ccmctid.yfilter != YFilter.not_set or
                self.ccmctidlastchangetime.yfilter != YFilter.not_set or
                self.ccmctidrolledovernotifenable.yfilter != YFilter.not_set or
                self.ccmctidwhochanged.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "ccmCTIDObjects" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-CONFIG-MAN-MIB:CISCO-CONFIG-MAN-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.ccmctid.is_set or self.ccmctid.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ccmctid.get_name_leafdata())
            if (self.ccmctidlastchangetime.is_set or self.ccmctidlastchangetime.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ccmctidlastchangetime.get_name_leafdata())
            if (self.ccmctidrolledovernotifenable.is_set or self.ccmctidrolledovernotifenable.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ccmctidrolledovernotifenable.get_name_leafdata())
            if (self.ccmctidwhochanged.is_set or self.ccmctidwhochanged.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ccmctidwhochanged.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "ccmCTID" or name == "ccmCTIDLastChangeTime" or name == "ccmCTIDRolledOverNotifEnable" or name == "ccmCTIDWhoChanged"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "ccmCTID"):
                self.ccmctid = value
                self.ccmctid.value_namespace = name_space
                self.ccmctid.value_namespace_prefix = name_space_prefix
            if(value_path == "ccmCTIDLastChangeTime"):
                self.ccmctidlastchangetime = value
                self.ccmctidlastchangetime.value_namespace = name_space
                self.ccmctidlastchangetime.value_namespace_prefix = name_space_prefix
            if(value_path == "ccmCTIDRolledOverNotifEnable"):
                self.ccmctidrolledovernotifenable = value
                self.ccmctidrolledovernotifenable.value_namespace = name_space
                self.ccmctidrolledovernotifenable.value_namespace_prefix = name_space_prefix
            if(value_path == "ccmCTIDWhoChanged"):
                self.ccmctidwhochanged = value
                self.ccmctidwhochanged.value_namespace = name_space
                self.ccmctidwhochanged.value_namespace_prefix = name_space_prefix


    class Ccmhistoryeventtable(Entity):
        """
        A table of configuration events on this router.
        
        .. attribute:: ccmhistoryevententry
        
        	Information about a configuration event on this router
        	**type**\: list of    :py:class:`Ccmhistoryevententry <ydk.models.cisco_ios_xe.CISCO_CONFIG_MAN_MIB.CiscoConfigManMib.Ccmhistoryeventtable.Ccmhistoryevententry>`
        
        

        """

        _prefix = 'CISCO-CONFIG-MAN-MIB'
        _revision = '2007-04-27'

        def __init__(self):
            super(CiscoConfigManMib.Ccmhistoryeventtable, self).__init__()

            self.yang_name = "ccmHistoryEventTable"
            self.yang_parent_name = "CISCO-CONFIG-MAN-MIB"

            self.ccmhistoryevententry = YList(self)

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
                        super(CiscoConfigManMib.Ccmhistoryeventtable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoConfigManMib.Ccmhistoryeventtable, self).__setattr__(name, value)


        class Ccmhistoryevententry(Entity):
            """
            Information about a configuration event on this
            router.
            
            .. attribute:: ccmhistoryeventindex  <key>
            
            	A monotonically increasing integer for the sole purpose of indexing events.  When it reaches the  maximum value, an extremely unlikely event, the agent  wraps the value back to 1 and may flush existing  entries
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            .. attribute:: ccmhistoryclicmdentriesbumped
            
            	The number of times the oldest entry in ccmCLIHistoryCommandTable with first index as  ccmHistoryEventIndex was deleted to make  room for a new entry.  This object is applicable only if  ccmHistoryEventCommandSource has a value  of 'commandLine'
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ccmhistoryeventcommandsource
            
            	The source of the command that instigated the event
            	**type**\:   :py:class:`Ccmhistoryeventcommandsource <ydk.models.cisco_ios_xe.CISCO_CONFIG_MAN_MIB.CiscoConfigManMib.Ccmhistoryeventtable.Ccmhistoryevententry.Ccmhistoryeventcommandsource>`
            
            .. attribute:: ccmhistoryeventcommandsourceaddress
            
            	If ccmHistoryEventTerminalType is 'virtual', the internet address of the connected system.  If ccmHistoryEventCommandSource is 'snmp', the internet address of the requester.  The value is 0.0.0.0 if not available or not  applicable.  This object is deprecated by ccmHistoryEventCommandSourceAddrRev1
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**status**\: deprecated
            
            .. attribute:: ccmhistoryeventcommandsourceaddrrev1
            
            	If ccmHistoryEventTerminalType is 'virtual', the internet address of the connected system.  If ccmHistoryEventCommandSource is 'snmp', the internet address of the requester.  The value of all bit's is zero  if not available or not applicable.  The Format of this address depends on the value of the ccmHistoryEventCommandSourceAddrType object.  This object deprecates ccmHistoryEventCommandSourceAddress
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: ccmhistoryeventcommandsourceaddrtype
            
            	This object indicates the transport type of the address contained in ccmHistoryEventCommandSourceAddrRev1.  The value will be zero if not available or not applicable
            	**type**\:   :py:class:`Inetaddresstype <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.Inetaddresstype>`
            
            .. attribute:: ccmhistoryeventconfigdestination
            
            	The configuration data destination for the event
            	**type**\:   :py:class:`Historyeventmedium <ydk.models.cisco_ios_xe.CISCO_CONFIG_MAN_MIB.Historyeventmedium>`
            
            .. attribute:: ccmhistoryeventconfigsource
            
            	The configuration data source for the event
            	**type**\:   :py:class:`Historyeventmedium <ydk.models.cisco_ios_xe.CISCO_CONFIG_MAN_MIB.Historyeventmedium>`
            
            .. attribute:: ccmhistoryeventfile
            
            	If ccmHistoryEventConfigSource or ccmHistoryEventConfigDestination is 'networkTftp' or 'networkRcp', the configuration file name at the storage file server.  The length is zero if not available or not applicable
            	**type**\:  str
            
            	**length:** 0..64
            
            .. attribute:: ccmhistoryeventrcpuser
            
            	If ccmHistoryEventConfigSource or ccmHistoryEventConfigDestination is 'networkRcp', the remote user name.  The length is zero if not applicable or not available
            	**type**\:  str
            
            	**length:** 0..64
            
            .. attribute:: ccmhistoryeventserveraddress
            
            	If ccmHistoryEventConfigSource or ccmHistoryEventConfigDestination is 'networkTftp' or 'networkRcp', the internet address of the storage file server.  The value is 0.0.0.0 if not applicable or not         available.         This object is deprecated by         ccmHistoryEventServerAddrRev1
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**status**\: deprecated
            
            .. attribute:: ccmhistoryeventserveraddrrev1
            
            	If ccmHistoryEventConfigSource or ccmHistoryEventConfigDestination is 'networkTftp' or 'networkRcp', the internet address of the storage file server.   The value of all bits is 0s if not applicable or not available.  The Format of this address depends on the value of the ccmHistoryEventServerAddrType object.  This object deprecates ccmHistoryEventServerAddress
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: ccmhistoryeventserveraddrtype
            
            	This object indicates the transport type of the address contained in ccmHistoryEventServerAddrRev1.  The value will be zero if not available or not aplicable
            	**type**\:   :py:class:`Inetaddresstype <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.Inetaddresstype>`
            
            .. attribute:: ccmhistoryeventterminallocation
            
            	If ccmHistoryEventCommandSource is 'commandLine', the hard\-wired location of the terminal or the remote  host for an incoming connection.  The length is zero  if not available or not applicable
            	**type**\:  str
            
            	**length:** 0..64
            
            .. attribute:: ccmhistoryeventterminalnumber
            
            	If ccmHistoryEventCommandSource is 'commandLine', the terminal number.  The value is \-1 if not available or not applicable
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: ccmhistoryeventterminaltype
            
            	If ccmHistoryEventCommandSource is 'commandLine', the terminal type, otherwise 'notApplicable'
            	**type**\:   :py:class:`Ccmhistoryeventterminaltype <ydk.models.cisco_ios_xe.CISCO_CONFIG_MAN_MIB.CiscoConfigManMib.Ccmhistoryeventtable.Ccmhistoryevententry.Ccmhistoryeventterminaltype>`
            
            .. attribute:: ccmhistoryeventterminaluser
            
            	If ccmHistoryEventCommandSource is 'commandLine', the name of the logged in user.  The length is zero if not available or not applicable
            	**type**\:  str
            
            	**length:** 0..64
            
            .. attribute:: ccmhistoryeventtime
            
            	The value of sysUpTime when the event occurred
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ccmhistoryeventvirtualhostname
            
            	If ccmHistoryEventTerminalType is 'virtual', the host name of the connected system.  The length is zero if not available or not applicable
            	**type**\:  str
            
            	**length:** 0..64
            
            

            """

            _prefix = 'CISCO-CONFIG-MAN-MIB'
            _revision = '2007-04-27'

            def __init__(self):
                super(CiscoConfigManMib.Ccmhistoryeventtable.Ccmhistoryevententry, self).__init__()

                self.yang_name = "ccmHistoryEventEntry"
                self.yang_parent_name = "ccmHistoryEventTable"

                self.ccmhistoryeventindex = YLeaf(YType.int32, "ccmHistoryEventIndex")

                self.ccmhistoryclicmdentriesbumped = YLeaf(YType.uint32, "ccmHistoryCLICmdEntriesBumped")

                self.ccmhistoryeventcommandsource = YLeaf(YType.enumeration, "ccmHistoryEventCommandSource")

                self.ccmhistoryeventcommandsourceaddress = YLeaf(YType.str, "ccmHistoryEventCommandSourceAddress")

                self.ccmhistoryeventcommandsourceaddrrev1 = YLeaf(YType.str, "ccmHistoryEventCommandSourceAddrRev1")

                self.ccmhistoryeventcommandsourceaddrtype = YLeaf(YType.enumeration, "ccmHistoryEventCommandSourceAddrType")

                self.ccmhistoryeventconfigdestination = YLeaf(YType.enumeration, "ccmHistoryEventConfigDestination")

                self.ccmhistoryeventconfigsource = YLeaf(YType.enumeration, "ccmHistoryEventConfigSource")

                self.ccmhistoryeventfile = YLeaf(YType.str, "ccmHistoryEventFile")

                self.ccmhistoryeventrcpuser = YLeaf(YType.str, "ccmHistoryEventRcpUser")

                self.ccmhistoryeventserveraddress = YLeaf(YType.str, "ccmHistoryEventServerAddress")

                self.ccmhistoryeventserveraddrrev1 = YLeaf(YType.str, "ccmHistoryEventServerAddrRev1")

                self.ccmhistoryeventserveraddrtype = YLeaf(YType.enumeration, "ccmHistoryEventServerAddrType")

                self.ccmhistoryeventterminallocation = YLeaf(YType.str, "ccmHistoryEventTerminalLocation")

                self.ccmhistoryeventterminalnumber = YLeaf(YType.int32, "ccmHistoryEventTerminalNumber")

                self.ccmhistoryeventterminaltype = YLeaf(YType.enumeration, "ccmHistoryEventTerminalType")

                self.ccmhistoryeventterminaluser = YLeaf(YType.str, "ccmHistoryEventTerminalUser")

                self.ccmhistoryeventtime = YLeaf(YType.uint32, "ccmHistoryEventTime")

                self.ccmhistoryeventvirtualhostname = YLeaf(YType.str, "ccmHistoryEventVirtualHostName")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("ccmhistoryeventindex",
                                "ccmhistoryclicmdentriesbumped",
                                "ccmhistoryeventcommandsource",
                                "ccmhistoryeventcommandsourceaddress",
                                "ccmhistoryeventcommandsourceaddrrev1",
                                "ccmhistoryeventcommandsourceaddrtype",
                                "ccmhistoryeventconfigdestination",
                                "ccmhistoryeventconfigsource",
                                "ccmhistoryeventfile",
                                "ccmhistoryeventrcpuser",
                                "ccmhistoryeventserveraddress",
                                "ccmhistoryeventserveraddrrev1",
                                "ccmhistoryeventserveraddrtype",
                                "ccmhistoryeventterminallocation",
                                "ccmhistoryeventterminalnumber",
                                "ccmhistoryeventterminaltype",
                                "ccmhistoryeventterminaluser",
                                "ccmhistoryeventtime",
                                "ccmhistoryeventvirtualhostname") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoConfigManMib.Ccmhistoryeventtable.Ccmhistoryevententry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoConfigManMib.Ccmhistoryeventtable.Ccmhistoryevententry, self).__setattr__(name, value)

            class Ccmhistoryeventcommandsource(Enum):
                """
                Ccmhistoryeventcommandsource

                The source of the command that instigated the event.

                .. data:: commandLine = 1

                .. data:: snmp = 2

                """

                commandLine = Enum.YLeaf(1, "commandLine")

                snmp = Enum.YLeaf(2, "snmp")


            class Ccmhistoryeventterminaltype(Enum):
                """
                Ccmhistoryeventterminaltype

                If ccmHistoryEventCommandSource is 'commandLine',

                the terminal type, otherwise 'notApplicable'.

                .. data:: notApplicable = 1

                .. data:: unknown = 2

                .. data:: console = 3

                .. data:: terminal = 4

                .. data:: virtual = 5

                .. data:: auxiliary = 6

                """

                notApplicable = Enum.YLeaf(1, "notApplicable")

                unknown = Enum.YLeaf(2, "unknown")

                console = Enum.YLeaf(3, "console")

                terminal = Enum.YLeaf(4, "terminal")

                virtual = Enum.YLeaf(5, "virtual")

                auxiliary = Enum.YLeaf(6, "auxiliary")


            def has_data(self):
                return (
                    self.ccmhistoryeventindex.is_set or
                    self.ccmhistoryclicmdentriesbumped.is_set or
                    self.ccmhistoryeventcommandsource.is_set or
                    self.ccmhistoryeventcommandsourceaddress.is_set or
                    self.ccmhistoryeventcommandsourceaddrrev1.is_set or
                    self.ccmhistoryeventcommandsourceaddrtype.is_set or
                    self.ccmhistoryeventconfigdestination.is_set or
                    self.ccmhistoryeventconfigsource.is_set or
                    self.ccmhistoryeventfile.is_set or
                    self.ccmhistoryeventrcpuser.is_set or
                    self.ccmhistoryeventserveraddress.is_set or
                    self.ccmhistoryeventserveraddrrev1.is_set or
                    self.ccmhistoryeventserveraddrtype.is_set or
                    self.ccmhistoryeventterminallocation.is_set or
                    self.ccmhistoryeventterminalnumber.is_set or
                    self.ccmhistoryeventterminaltype.is_set or
                    self.ccmhistoryeventterminaluser.is_set or
                    self.ccmhistoryeventtime.is_set or
                    self.ccmhistoryeventvirtualhostname.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ccmhistoryeventindex.yfilter != YFilter.not_set or
                    self.ccmhistoryclicmdentriesbumped.yfilter != YFilter.not_set or
                    self.ccmhistoryeventcommandsource.yfilter != YFilter.not_set or
                    self.ccmhistoryeventcommandsourceaddress.yfilter != YFilter.not_set or
                    self.ccmhistoryeventcommandsourceaddrrev1.yfilter != YFilter.not_set or
                    self.ccmhistoryeventcommandsourceaddrtype.yfilter != YFilter.not_set or
                    self.ccmhistoryeventconfigdestination.yfilter != YFilter.not_set or
                    self.ccmhistoryeventconfigsource.yfilter != YFilter.not_set or
                    self.ccmhistoryeventfile.yfilter != YFilter.not_set or
                    self.ccmhistoryeventrcpuser.yfilter != YFilter.not_set or
                    self.ccmhistoryeventserveraddress.yfilter != YFilter.not_set or
                    self.ccmhistoryeventserveraddrrev1.yfilter != YFilter.not_set or
                    self.ccmhistoryeventserveraddrtype.yfilter != YFilter.not_set or
                    self.ccmhistoryeventterminallocation.yfilter != YFilter.not_set or
                    self.ccmhistoryeventterminalnumber.yfilter != YFilter.not_set or
                    self.ccmhistoryeventterminaltype.yfilter != YFilter.not_set or
                    self.ccmhistoryeventterminaluser.yfilter != YFilter.not_set or
                    self.ccmhistoryeventtime.yfilter != YFilter.not_set or
                    self.ccmhistoryeventvirtualhostname.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "ccmHistoryEventEntry" + "[ccmHistoryEventIndex='" + self.ccmhistoryeventindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-CONFIG-MAN-MIB:CISCO-CONFIG-MAN-MIB/ccmHistoryEventTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ccmhistoryeventindex.is_set or self.ccmhistoryeventindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ccmhistoryeventindex.get_name_leafdata())
                if (self.ccmhistoryclicmdentriesbumped.is_set or self.ccmhistoryclicmdentriesbumped.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ccmhistoryclicmdentriesbumped.get_name_leafdata())
                if (self.ccmhistoryeventcommandsource.is_set or self.ccmhistoryeventcommandsource.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ccmhistoryeventcommandsource.get_name_leafdata())
                if (self.ccmhistoryeventcommandsourceaddress.is_set or self.ccmhistoryeventcommandsourceaddress.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ccmhistoryeventcommandsourceaddress.get_name_leafdata())
                if (self.ccmhistoryeventcommandsourceaddrrev1.is_set or self.ccmhistoryeventcommandsourceaddrrev1.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ccmhistoryeventcommandsourceaddrrev1.get_name_leafdata())
                if (self.ccmhistoryeventcommandsourceaddrtype.is_set or self.ccmhistoryeventcommandsourceaddrtype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ccmhistoryeventcommandsourceaddrtype.get_name_leafdata())
                if (self.ccmhistoryeventconfigdestination.is_set or self.ccmhistoryeventconfigdestination.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ccmhistoryeventconfigdestination.get_name_leafdata())
                if (self.ccmhistoryeventconfigsource.is_set or self.ccmhistoryeventconfigsource.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ccmhistoryeventconfigsource.get_name_leafdata())
                if (self.ccmhistoryeventfile.is_set or self.ccmhistoryeventfile.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ccmhistoryeventfile.get_name_leafdata())
                if (self.ccmhistoryeventrcpuser.is_set or self.ccmhistoryeventrcpuser.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ccmhistoryeventrcpuser.get_name_leafdata())
                if (self.ccmhistoryeventserveraddress.is_set or self.ccmhistoryeventserveraddress.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ccmhistoryeventserveraddress.get_name_leafdata())
                if (self.ccmhistoryeventserveraddrrev1.is_set or self.ccmhistoryeventserveraddrrev1.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ccmhistoryeventserveraddrrev1.get_name_leafdata())
                if (self.ccmhistoryeventserveraddrtype.is_set or self.ccmhistoryeventserveraddrtype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ccmhistoryeventserveraddrtype.get_name_leafdata())
                if (self.ccmhistoryeventterminallocation.is_set or self.ccmhistoryeventterminallocation.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ccmhistoryeventterminallocation.get_name_leafdata())
                if (self.ccmhistoryeventterminalnumber.is_set or self.ccmhistoryeventterminalnumber.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ccmhistoryeventterminalnumber.get_name_leafdata())
                if (self.ccmhistoryeventterminaltype.is_set or self.ccmhistoryeventterminaltype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ccmhistoryeventterminaltype.get_name_leafdata())
                if (self.ccmhistoryeventterminaluser.is_set or self.ccmhistoryeventterminaluser.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ccmhistoryeventterminaluser.get_name_leafdata())
                if (self.ccmhistoryeventtime.is_set or self.ccmhistoryeventtime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ccmhistoryeventtime.get_name_leafdata())
                if (self.ccmhistoryeventvirtualhostname.is_set or self.ccmhistoryeventvirtualhostname.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ccmhistoryeventvirtualhostname.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ccmHistoryEventIndex" or name == "ccmHistoryCLICmdEntriesBumped" or name == "ccmHistoryEventCommandSource" or name == "ccmHistoryEventCommandSourceAddress" or name == "ccmHistoryEventCommandSourceAddrRev1" or name == "ccmHistoryEventCommandSourceAddrType" or name == "ccmHistoryEventConfigDestination" or name == "ccmHistoryEventConfigSource" or name == "ccmHistoryEventFile" or name == "ccmHistoryEventRcpUser" or name == "ccmHistoryEventServerAddress" or name == "ccmHistoryEventServerAddrRev1" or name == "ccmHistoryEventServerAddrType" or name == "ccmHistoryEventTerminalLocation" or name == "ccmHistoryEventTerminalNumber" or name == "ccmHistoryEventTerminalType" or name == "ccmHistoryEventTerminalUser" or name == "ccmHistoryEventTime" or name == "ccmHistoryEventVirtualHostName"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "ccmHistoryEventIndex"):
                    self.ccmhistoryeventindex = value
                    self.ccmhistoryeventindex.value_namespace = name_space
                    self.ccmhistoryeventindex.value_namespace_prefix = name_space_prefix
                if(value_path == "ccmHistoryCLICmdEntriesBumped"):
                    self.ccmhistoryclicmdentriesbumped = value
                    self.ccmhistoryclicmdentriesbumped.value_namespace = name_space
                    self.ccmhistoryclicmdentriesbumped.value_namespace_prefix = name_space_prefix
                if(value_path == "ccmHistoryEventCommandSource"):
                    self.ccmhistoryeventcommandsource = value
                    self.ccmhistoryeventcommandsource.value_namespace = name_space
                    self.ccmhistoryeventcommandsource.value_namespace_prefix = name_space_prefix
                if(value_path == "ccmHistoryEventCommandSourceAddress"):
                    self.ccmhistoryeventcommandsourceaddress = value
                    self.ccmhistoryeventcommandsourceaddress.value_namespace = name_space
                    self.ccmhistoryeventcommandsourceaddress.value_namespace_prefix = name_space_prefix
                if(value_path == "ccmHistoryEventCommandSourceAddrRev1"):
                    self.ccmhistoryeventcommandsourceaddrrev1 = value
                    self.ccmhistoryeventcommandsourceaddrrev1.value_namespace = name_space
                    self.ccmhistoryeventcommandsourceaddrrev1.value_namespace_prefix = name_space_prefix
                if(value_path == "ccmHistoryEventCommandSourceAddrType"):
                    self.ccmhistoryeventcommandsourceaddrtype = value
                    self.ccmhistoryeventcommandsourceaddrtype.value_namespace = name_space
                    self.ccmhistoryeventcommandsourceaddrtype.value_namespace_prefix = name_space_prefix
                if(value_path == "ccmHistoryEventConfigDestination"):
                    self.ccmhistoryeventconfigdestination = value
                    self.ccmhistoryeventconfigdestination.value_namespace = name_space
                    self.ccmhistoryeventconfigdestination.value_namespace_prefix = name_space_prefix
                if(value_path == "ccmHistoryEventConfigSource"):
                    self.ccmhistoryeventconfigsource = value
                    self.ccmhistoryeventconfigsource.value_namespace = name_space
                    self.ccmhistoryeventconfigsource.value_namespace_prefix = name_space_prefix
                if(value_path == "ccmHistoryEventFile"):
                    self.ccmhistoryeventfile = value
                    self.ccmhistoryeventfile.value_namespace = name_space
                    self.ccmhistoryeventfile.value_namespace_prefix = name_space_prefix
                if(value_path == "ccmHistoryEventRcpUser"):
                    self.ccmhistoryeventrcpuser = value
                    self.ccmhistoryeventrcpuser.value_namespace = name_space
                    self.ccmhistoryeventrcpuser.value_namespace_prefix = name_space_prefix
                if(value_path == "ccmHistoryEventServerAddress"):
                    self.ccmhistoryeventserveraddress = value
                    self.ccmhistoryeventserveraddress.value_namespace = name_space
                    self.ccmhistoryeventserveraddress.value_namespace_prefix = name_space_prefix
                if(value_path == "ccmHistoryEventServerAddrRev1"):
                    self.ccmhistoryeventserveraddrrev1 = value
                    self.ccmhistoryeventserveraddrrev1.value_namespace = name_space
                    self.ccmhistoryeventserveraddrrev1.value_namespace_prefix = name_space_prefix
                if(value_path == "ccmHistoryEventServerAddrType"):
                    self.ccmhistoryeventserveraddrtype = value
                    self.ccmhistoryeventserveraddrtype.value_namespace = name_space
                    self.ccmhistoryeventserveraddrtype.value_namespace_prefix = name_space_prefix
                if(value_path == "ccmHistoryEventTerminalLocation"):
                    self.ccmhistoryeventterminallocation = value
                    self.ccmhistoryeventterminallocation.value_namespace = name_space
                    self.ccmhistoryeventterminallocation.value_namespace_prefix = name_space_prefix
                if(value_path == "ccmHistoryEventTerminalNumber"):
                    self.ccmhistoryeventterminalnumber = value
                    self.ccmhistoryeventterminalnumber.value_namespace = name_space
                    self.ccmhistoryeventterminalnumber.value_namespace_prefix = name_space_prefix
                if(value_path == "ccmHistoryEventTerminalType"):
                    self.ccmhistoryeventterminaltype = value
                    self.ccmhistoryeventterminaltype.value_namespace = name_space
                    self.ccmhistoryeventterminaltype.value_namespace_prefix = name_space_prefix
                if(value_path == "ccmHistoryEventTerminalUser"):
                    self.ccmhistoryeventterminaluser = value
                    self.ccmhistoryeventterminaluser.value_namespace = name_space
                    self.ccmhistoryeventterminaluser.value_namespace_prefix = name_space_prefix
                if(value_path == "ccmHistoryEventTime"):
                    self.ccmhistoryeventtime = value
                    self.ccmhistoryeventtime.value_namespace = name_space
                    self.ccmhistoryeventtime.value_namespace_prefix = name_space_prefix
                if(value_path == "ccmHistoryEventVirtualHostName"):
                    self.ccmhistoryeventvirtualhostname = value
                    self.ccmhistoryeventvirtualhostname.value_namespace = name_space
                    self.ccmhistoryeventvirtualhostname.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.ccmhistoryevententry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.ccmhistoryevententry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "ccmHistoryEventTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-CONFIG-MAN-MIB:CISCO-CONFIG-MAN-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "ccmHistoryEventEntry"):
                for c in self.ccmhistoryevententry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoConfigManMib.Ccmhistoryeventtable.Ccmhistoryevententry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.ccmhistoryevententry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "ccmHistoryEventEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Ccmclihistorycommandtable(Entity):
        """
        A table of CLI commands that took effect during
        configuration events.
        
        .. attribute:: ccmclihistorycommandentry
        
        	Information about the CLI commands that took effect during the configuration event pointed by  ccmCLIHistoryEventIndex.  A set of rows in this table having the first index as ccmHistoryEventIndex will store the CLI commands entered during the corresponding  configuration event in ccmHistoryEventTable.  An entry will be created in this table only if  the corresponding entry in ccmHistoryEventTable has  a value of 'commandLine' for  ccmHistoryEventCommandSource
        	**type**\: list of    :py:class:`Ccmclihistorycommandentry <ydk.models.cisco_ios_xe.CISCO_CONFIG_MAN_MIB.CiscoConfigManMib.Ccmclihistorycommandtable.Ccmclihistorycommandentry>`
        
        

        """

        _prefix = 'CISCO-CONFIG-MAN-MIB'
        _revision = '2007-04-27'

        def __init__(self):
            super(CiscoConfigManMib.Ccmclihistorycommandtable, self).__init__()

            self.yang_name = "ccmCLIHistoryCommandTable"
            self.yang_parent_name = "CISCO-CONFIG-MAN-MIB"

            self.ccmclihistorycommandentry = YList(self)

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
                        super(CiscoConfigManMib.Ccmclihistorycommandtable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoConfigManMib.Ccmclihistorycommandtable, self).__setattr__(name, value)


        class Ccmclihistorycommandentry(Entity):
            """
            Information about the CLI commands that took effect
            during the configuration event pointed by 
            ccmCLIHistoryEventIndex.
            
            A set of rows in this table having the first
            index as ccmHistoryEventIndex will store the
            CLI commands entered during the corresponding 
            configuration event in ccmHistoryEventTable.
            
            An entry will be created in this table only if 
            the corresponding entry in ccmHistoryEventTable has 
            a value of 'commandLine' for 
            ccmHistoryEventCommandSource.
            
            .. attribute:: ccmhistoryeventindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ccmhistoryeventindex <ydk.models.cisco_ios_xe.CISCO_CONFIG_MAN_MIB.CiscoConfigManMib.Ccmhistoryeventtable.Ccmhistoryevententry>`
            
            .. attribute:: ccmclihistorycommandindex  <key>
            
            	A monotonically increasing integer for the purpose of indexing CLI commands which took effect during a configuration event
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            .. attribute:: ccmclihistorycommand
            
            	The CLI command entered which took effect during the configuration event pointed by  ccmHistoryEventIndex
            	**type**\:  str
            
            

            """

            _prefix = 'CISCO-CONFIG-MAN-MIB'
            _revision = '2007-04-27'

            def __init__(self):
                super(CiscoConfigManMib.Ccmclihistorycommandtable.Ccmclihistorycommandentry, self).__init__()

                self.yang_name = "ccmCLIHistoryCommandEntry"
                self.yang_parent_name = "ccmCLIHistoryCommandTable"

                self.ccmhistoryeventindex = YLeaf(YType.str, "ccmHistoryEventIndex")

                self.ccmclihistorycommandindex = YLeaf(YType.uint32, "ccmCLIHistoryCommandIndex")

                self.ccmclihistorycommand = YLeaf(YType.str, "ccmCLIHistoryCommand")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("ccmhistoryeventindex",
                                "ccmclihistorycommandindex",
                                "ccmclihistorycommand") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoConfigManMib.Ccmclihistorycommandtable.Ccmclihistorycommandentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoConfigManMib.Ccmclihistorycommandtable.Ccmclihistorycommandentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.ccmhistoryeventindex.is_set or
                    self.ccmclihistorycommandindex.is_set or
                    self.ccmclihistorycommand.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ccmhistoryeventindex.yfilter != YFilter.not_set or
                    self.ccmclihistorycommandindex.yfilter != YFilter.not_set or
                    self.ccmclihistorycommand.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "ccmCLIHistoryCommandEntry" + "[ccmHistoryEventIndex='" + self.ccmhistoryeventindex.get() + "']" + "[ccmCLIHistoryCommandIndex='" + self.ccmclihistorycommandindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-CONFIG-MAN-MIB:CISCO-CONFIG-MAN-MIB/ccmCLIHistoryCommandTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ccmhistoryeventindex.is_set or self.ccmhistoryeventindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ccmhistoryeventindex.get_name_leafdata())
                if (self.ccmclihistorycommandindex.is_set or self.ccmclihistorycommandindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ccmclihistorycommandindex.get_name_leafdata())
                if (self.ccmclihistorycommand.is_set or self.ccmclihistorycommand.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ccmclihistorycommand.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ccmHistoryEventIndex" or name == "ccmCLIHistoryCommandIndex" or name == "ccmCLIHistoryCommand"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "ccmHistoryEventIndex"):
                    self.ccmhistoryeventindex = value
                    self.ccmhistoryeventindex.value_namespace = name_space
                    self.ccmhistoryeventindex.value_namespace_prefix = name_space_prefix
                if(value_path == "ccmCLIHistoryCommandIndex"):
                    self.ccmclihistorycommandindex = value
                    self.ccmclihistorycommandindex.value_namespace = name_space
                    self.ccmclihistorycommandindex.value_namespace_prefix = name_space_prefix
                if(value_path == "ccmCLIHistoryCommand"):
                    self.ccmclihistorycommand = value
                    self.ccmclihistorycommand.value_namespace = name_space
                    self.ccmclihistorycommand.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.ccmclihistorycommandentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.ccmclihistorycommandentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "ccmCLIHistoryCommandTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-CONFIG-MAN-MIB:CISCO-CONFIG-MAN-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "ccmCLIHistoryCommandEntry"):
                for c in self.ccmclihistorycommandentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoConfigManMib.Ccmclihistorycommandtable.Ccmclihistorycommandentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.ccmclihistorycommandentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "ccmCLIHistoryCommandEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            (self.ccmclicfg is not None and self.ccmclicfg.has_data()) or
            (self.ccmclihistory is not None and self.ccmclihistory.has_data()) or
            (self.ccmclihistorycommandtable is not None and self.ccmclihistorycommandtable.has_data()) or
            (self.ccmctidobjects is not None and self.ccmctidobjects.has_data()) or
            (self.ccmhistory is not None and self.ccmhistory.has_data()) or
            (self.ccmhistoryeventtable is not None and self.ccmhistoryeventtable.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.ccmclicfg is not None and self.ccmclicfg.has_operation()) or
            (self.ccmclihistory is not None and self.ccmclihistory.has_operation()) or
            (self.ccmclihistorycommandtable is not None and self.ccmclihistorycommandtable.has_operation()) or
            (self.ccmctidobjects is not None and self.ccmctidobjects.has_operation()) or
            (self.ccmhistory is not None and self.ccmhistory.has_operation()) or
            (self.ccmhistoryeventtable is not None and self.ccmhistoryeventtable.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "CISCO-CONFIG-MAN-MIB:CISCO-CONFIG-MAN-MIB" + path_buffer

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

        if (child_yang_name == "ccmCLICfg"):
            if (self.ccmclicfg is None):
                self.ccmclicfg = CiscoConfigManMib.Ccmclicfg()
                self.ccmclicfg.parent = self
                self._children_name_map["ccmclicfg"] = "ccmCLICfg"
            return self.ccmclicfg

        if (child_yang_name == "ccmCLIHistory"):
            if (self.ccmclihistory is None):
                self.ccmclihistory = CiscoConfigManMib.Ccmclihistory()
                self.ccmclihistory.parent = self
                self._children_name_map["ccmclihistory"] = "ccmCLIHistory"
            return self.ccmclihistory

        if (child_yang_name == "ccmCLIHistoryCommandTable"):
            if (self.ccmclihistorycommandtable is None):
                self.ccmclihistorycommandtable = CiscoConfigManMib.Ccmclihistorycommandtable()
                self.ccmclihistorycommandtable.parent = self
                self._children_name_map["ccmclihistorycommandtable"] = "ccmCLIHistoryCommandTable"
            return self.ccmclihistorycommandtable

        if (child_yang_name == "ccmCTIDObjects"):
            if (self.ccmctidobjects is None):
                self.ccmctidobjects = CiscoConfigManMib.Ccmctidobjects()
                self.ccmctidobjects.parent = self
                self._children_name_map["ccmctidobjects"] = "ccmCTIDObjects"
            return self.ccmctidobjects

        if (child_yang_name == "ccmHistory"):
            if (self.ccmhistory is None):
                self.ccmhistory = CiscoConfigManMib.Ccmhistory()
                self.ccmhistory.parent = self
                self._children_name_map["ccmhistory"] = "ccmHistory"
            return self.ccmhistory

        if (child_yang_name == "ccmHistoryEventTable"):
            if (self.ccmhistoryeventtable is None):
                self.ccmhistoryeventtable = CiscoConfigManMib.Ccmhistoryeventtable()
                self.ccmhistoryeventtable.parent = self
                self._children_name_map["ccmhistoryeventtable"] = "ccmHistoryEventTable"
            return self.ccmhistoryeventtable

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "ccmCLICfg" or name == "ccmCLIHistory" or name == "ccmCLIHistoryCommandTable" or name == "ccmCTIDObjects" or name == "ccmHistory" or name == "ccmHistoryEventTable"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = CiscoConfigManMib()
        return self._top_entity

