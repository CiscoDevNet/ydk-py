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
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class HistoryEventMedium(Enum):
    """
    HistoryEventMedium (Enum Class)

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



class CISCOCONFIGMANMIB(Entity):
    """
    
    
    .. attribute:: ccmhistory
    
    	
    	**type**\:  :py:class:`Ccmhistory <ydk.models.cisco_ios_xe.CISCO_CONFIG_MAN_MIB.CISCOCONFIGMANMIB.Ccmhistory>`
    
    .. attribute:: ccmclihistory
    
    	
    	**type**\:  :py:class:`Ccmclihistory <ydk.models.cisco_ios_xe.CISCO_CONFIG_MAN_MIB.CISCOCONFIGMANMIB.Ccmclihistory>`
    
    .. attribute:: ccmclicfg
    
    	
    	**type**\:  :py:class:`Ccmclicfg <ydk.models.cisco_ios_xe.CISCO_CONFIG_MAN_MIB.CISCOCONFIGMANMIB.Ccmclicfg>`
    
    .. attribute:: ccmctidobjects
    
    	
    	**type**\:  :py:class:`Ccmctidobjects <ydk.models.cisco_ios_xe.CISCO_CONFIG_MAN_MIB.CISCOCONFIGMANMIB.Ccmctidobjects>`
    
    .. attribute:: ccmhistoryeventtable
    
    	A table of configuration events on this router
    	**type**\:  :py:class:`Ccmhistoryeventtable <ydk.models.cisco_ios_xe.CISCO_CONFIG_MAN_MIB.CISCOCONFIGMANMIB.Ccmhistoryeventtable>`
    
    .. attribute:: ccmclihistorycommandtable
    
    	A table of CLI commands that took effect during configuration events
    	**type**\:  :py:class:`Ccmclihistorycommandtable <ydk.models.cisco_ios_xe.CISCO_CONFIG_MAN_MIB.CISCOCONFIGMANMIB.Ccmclihistorycommandtable>`
    
    

    """

    _prefix = 'CISCO-CONFIG-MAN-MIB'
    _revision = '2007-04-27'

    def __init__(self):
        super(CISCOCONFIGMANMIB, self).__init__()
        self._top_entity = None

        self.yang_name = "CISCO-CONFIG-MAN-MIB"
        self.yang_parent_name = "CISCO-CONFIG-MAN-MIB"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([("ccmHistory", ("ccmhistory", CISCOCONFIGMANMIB.Ccmhistory)), ("ccmCLIHistory", ("ccmclihistory", CISCOCONFIGMANMIB.Ccmclihistory)), ("ccmCLICfg", ("ccmclicfg", CISCOCONFIGMANMIB.Ccmclicfg)), ("ccmCTIDObjects", ("ccmctidobjects", CISCOCONFIGMANMIB.Ccmctidobjects)), ("ccmHistoryEventTable", ("ccmhistoryeventtable", CISCOCONFIGMANMIB.Ccmhistoryeventtable)), ("ccmCLIHistoryCommandTable", ("ccmclihistorycommandtable", CISCOCONFIGMANMIB.Ccmclihistorycommandtable))])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.ccmhistory = CISCOCONFIGMANMIB.Ccmhistory()
        self.ccmhistory.parent = self
        self._children_name_map["ccmhistory"] = "ccmHistory"
        self._children_yang_names.add("ccmHistory")

        self.ccmclihistory = CISCOCONFIGMANMIB.Ccmclihistory()
        self.ccmclihistory.parent = self
        self._children_name_map["ccmclihistory"] = "ccmCLIHistory"
        self._children_yang_names.add("ccmCLIHistory")

        self.ccmclicfg = CISCOCONFIGMANMIB.Ccmclicfg()
        self.ccmclicfg.parent = self
        self._children_name_map["ccmclicfg"] = "ccmCLICfg"
        self._children_yang_names.add("ccmCLICfg")

        self.ccmctidobjects = CISCOCONFIGMANMIB.Ccmctidobjects()
        self.ccmctidobjects.parent = self
        self._children_name_map["ccmctidobjects"] = "ccmCTIDObjects"
        self._children_yang_names.add("ccmCTIDObjects")

        self.ccmhistoryeventtable = CISCOCONFIGMANMIB.Ccmhistoryeventtable()
        self.ccmhistoryeventtable.parent = self
        self._children_name_map["ccmhistoryeventtable"] = "ccmHistoryEventTable"
        self._children_yang_names.add("ccmHistoryEventTable")

        self.ccmclihistorycommandtable = CISCOCONFIGMANMIB.Ccmclihistorycommandtable()
        self.ccmclihistorycommandtable.parent = self
        self._children_name_map["ccmclihistorycommandtable"] = "ccmCLIHistoryCommandTable"
        self._children_yang_names.add("ccmCLIHistoryCommandTable")
        self._segment_path = lambda: "CISCO-CONFIG-MAN-MIB:CISCO-CONFIG-MAN-MIB"


    class Ccmhistory(Entity):
        """
        
        
        .. attribute:: ccmhistoryrunninglastchanged
        
        	The value of sysUpTime when the running configuration was last changed.          If the value of ccmHistoryRunningLastChanged is         greater than ccmHistoryRunningLastSaved, the          configuration has been changed but not saved
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: ccmhistoryrunninglastsaved
        
        	The value of sysUpTime when the running configuration was last saved (written).  If the value of ccmHistoryRunningLastChanged is  greater than ccmHistoryRunningLastSaved, the  configuration has been changed but not saved.  What constitutes a safe saving of the running configuration is a management policy issue beyond the scope of this MIB.  For some installations, writing the running configuration to a terminal may be a way of capturing and saving it.  Others may use local or remote storage.  Thus ANY write is considered saving for the purposes of the MIB
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: ccmhistorystartuplastchanged
        
        	The value of sysUpTime when the startup configuration was last written to.  In general this is the default configuration used when cold starting the system.  It may have been changed by a save of the running configuration or by a copy from elsewhere
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: ccmhistorymaxevententries
        
        	The maximum number of entries that can be held in ccmHistoryEventTable.  The recommended value for implementations is 10
        	**type**\: int
        
        	**range:** 0..2147483647
        
        .. attribute:: ccmhistoryevententriesbumped
        
        	The number of times the oldest entry in ccmHistoryEventTable was deleted to make room  for a new entry
        	**type**\: int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'CISCO-CONFIG-MAN-MIB'
        _revision = '2007-04-27'

        def __init__(self):
            super(CISCOCONFIGMANMIB.Ccmhistory, self).__init__()

            self.yang_name = "ccmHistory"
            self.yang_parent_name = "CISCO-CONFIG-MAN-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('ccmhistoryrunninglastchanged', YLeaf(YType.uint32, 'ccmHistoryRunningLastChanged')),
                ('ccmhistoryrunninglastsaved', YLeaf(YType.uint32, 'ccmHistoryRunningLastSaved')),
                ('ccmhistorystartuplastchanged', YLeaf(YType.uint32, 'ccmHistoryStartupLastChanged')),
                ('ccmhistorymaxevententries', YLeaf(YType.int32, 'ccmHistoryMaxEventEntries')),
                ('ccmhistoryevententriesbumped', YLeaf(YType.uint32, 'ccmHistoryEventEntriesBumped')),
            ])
            self.ccmhistoryrunninglastchanged = None
            self.ccmhistoryrunninglastsaved = None
            self.ccmhistorystartuplastchanged = None
            self.ccmhistorymaxevententries = None
            self.ccmhistoryevententriesbumped = None
            self._segment_path = lambda: "ccmHistory"
            self._absolute_path = lambda: "CISCO-CONFIG-MAN-MIB:CISCO-CONFIG-MAN-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOCONFIGMANMIB.Ccmhistory, ['ccmhistoryrunninglastchanged', 'ccmhistoryrunninglastsaved', 'ccmhistorystartuplastchanged', 'ccmhistorymaxevententries', 'ccmhistoryevententriesbumped'], name, value)


    class Ccmclihistory(Entity):
        """
        
        
        .. attribute:: ccmclihistorymaxcmdentries
        
        	The maximum number of entries that can be held in ccmCLIHistoryCommandTable.  The recommended value for implementations is 100.  If the number of entries in ccmCLIHistoryCommandTable  exceeds the value of this object, old entries will be  bumped to make room for new entries.  The ccmCLIHistoryCommandTable will not be populated if the value of this object is 0
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: ccmclihistorycmdentries
        
        	The current number of entries in ccmCLIHistoryCommandTable
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: ccmclihistorycmdentriesallowed
        
        	This object indicates the upper limit on the number of entries allowed in  ccmCLIHistoryCommandTable by the managed system
        	**type**\: int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'CISCO-CONFIG-MAN-MIB'
        _revision = '2007-04-27'

        def __init__(self):
            super(CISCOCONFIGMANMIB.Ccmclihistory, self).__init__()

            self.yang_name = "ccmCLIHistory"
            self.yang_parent_name = "CISCO-CONFIG-MAN-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('ccmclihistorymaxcmdentries', YLeaf(YType.uint32, 'ccmCLIHistoryMaxCmdEntries')),
                ('ccmclihistorycmdentries', YLeaf(YType.uint32, 'ccmCLIHistoryCmdEntries')),
                ('ccmclihistorycmdentriesallowed', YLeaf(YType.uint32, 'ccmCLIHistoryCmdEntriesAllowed')),
            ])
            self.ccmclihistorymaxcmdentries = None
            self.ccmclihistorycmdentries = None
            self.ccmclihistorycmdentriesallowed = None
            self._segment_path = lambda: "ccmCLIHistory"
            self._absolute_path = lambda: "CISCO-CONFIG-MAN-MIB:CISCO-CONFIG-MAN-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOCONFIGMANMIB.Ccmclihistory, ['ccmclihistorymaxcmdentries', 'ccmclihistorycmdentries', 'ccmclihistorycmdentriesallowed'], name, value)


    class Ccmclicfg(Entity):
        """
        
        
        .. attribute:: ccmclicfgrunconfnotifenable
        
        	This variable indicates whether the system produces the ccmCLIRunningConfigChanged notification. A false  value will prevent notifications from being generated  by this system
        	**type**\: bool
        
        

        """

        _prefix = 'CISCO-CONFIG-MAN-MIB'
        _revision = '2007-04-27'

        def __init__(self):
            super(CISCOCONFIGMANMIB.Ccmclicfg, self).__init__()

            self.yang_name = "ccmCLICfg"
            self.yang_parent_name = "CISCO-CONFIG-MAN-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('ccmclicfgrunconfnotifenable', YLeaf(YType.boolean, 'ccmCLICfgRunConfNotifEnable')),
            ])
            self.ccmclicfgrunconfnotifenable = None
            self._segment_path = lambda: "ccmCLICfg"
            self._absolute_path = lambda: "CISCO-CONFIG-MAN-MIB:CISCO-CONFIG-MAN-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOCONFIGMANMIB.Ccmclicfg, ['ccmclicfgrunconfnotifenable'], name, value)


    class Ccmctidobjects(Entity):
        """
        
        
        .. attribute:: ccmctid
        
        	This object indicates the Config Change Tracking ID which uniquely represents version\-incrementing changes to the IOS  running configuration
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        .. attribute:: ccmctidlastchangetime
        
        	This object indicates the time when the Config Change Tracking ID last changed
        	**type**\: str
        
        .. attribute:: ccmctidwhochanged
        
        	This object indicates the user who last reset the Config Change Tracking ID
        	**type**\: str
        
        .. attribute:: ccmctidrolledovernotifenable
        
        	This variable indicates whether the system produces the ccmCTIDRolledOver notification. A false value will prevent notifications from being generated by this system
        	**type**\: bool
        
        

        """

        _prefix = 'CISCO-CONFIG-MAN-MIB'
        _revision = '2007-04-27'

        def __init__(self):
            super(CISCOCONFIGMANMIB.Ccmctidobjects, self).__init__()

            self.yang_name = "ccmCTIDObjects"
            self.yang_parent_name = "CISCO-CONFIG-MAN-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('ccmctid', YLeaf(YType.uint64, 'ccmCTID')),
                ('ccmctidlastchangetime', YLeaf(YType.str, 'ccmCTIDLastChangeTime')),
                ('ccmctidwhochanged', YLeaf(YType.str, 'ccmCTIDWhoChanged')),
                ('ccmctidrolledovernotifenable', YLeaf(YType.boolean, 'ccmCTIDRolledOverNotifEnable')),
            ])
            self.ccmctid = None
            self.ccmctidlastchangetime = None
            self.ccmctidwhochanged = None
            self.ccmctidrolledovernotifenable = None
            self._segment_path = lambda: "ccmCTIDObjects"
            self._absolute_path = lambda: "CISCO-CONFIG-MAN-MIB:CISCO-CONFIG-MAN-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOCONFIGMANMIB.Ccmctidobjects, ['ccmctid', 'ccmctidlastchangetime', 'ccmctidwhochanged', 'ccmctidrolledovernotifenable'], name, value)


    class Ccmhistoryeventtable(Entity):
        """
        A table of configuration events on this router.
        
        .. attribute:: ccmhistoryevententry
        
        	Information about a configuration event on this router
        	**type**\: list of  		 :py:class:`Ccmhistoryevententry <ydk.models.cisco_ios_xe.CISCO_CONFIG_MAN_MIB.CISCOCONFIGMANMIB.Ccmhistoryeventtable.Ccmhistoryevententry>`
        
        

        """

        _prefix = 'CISCO-CONFIG-MAN-MIB'
        _revision = '2007-04-27'

        def __init__(self):
            super(CISCOCONFIGMANMIB.Ccmhistoryeventtable, self).__init__()

            self.yang_name = "ccmHistoryEventTable"
            self.yang_parent_name = "CISCO-CONFIG-MAN-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("ccmHistoryEventEntry", ("ccmhistoryevententry", CISCOCONFIGMANMIB.Ccmhistoryeventtable.Ccmhistoryevententry))])
            self._leafs = OrderedDict()

            self.ccmhistoryevententry = YList(self)
            self._segment_path = lambda: "ccmHistoryEventTable"
            self._absolute_path = lambda: "CISCO-CONFIG-MAN-MIB:CISCO-CONFIG-MAN-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOCONFIGMANMIB.Ccmhistoryeventtable, [], name, value)


        class Ccmhistoryevententry(Entity):
            """
            Information about a configuration event on this
            router.
            
            .. attribute:: ccmhistoryeventindex  (key)
            
            	A monotonically increasing integer for the sole purpose of indexing events.  When it reaches the  maximum value, an extremely unlikely event, the agent  wraps the value back to 1 and may flush existing  entries
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: ccmhistoryeventtime
            
            	The value of sysUpTime when the event occurred
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ccmhistoryeventcommandsource
            
            	The source of the command that instigated the event
            	**type**\:  :py:class:`Ccmhistoryeventcommandsource <ydk.models.cisco_ios_xe.CISCO_CONFIG_MAN_MIB.CISCOCONFIGMANMIB.Ccmhistoryeventtable.Ccmhistoryevententry.Ccmhistoryeventcommandsource>`
            
            .. attribute:: ccmhistoryeventconfigsource
            
            	The configuration data source for the event
            	**type**\:  :py:class:`HistoryEventMedium <ydk.models.cisco_ios_xe.CISCO_CONFIG_MAN_MIB.HistoryEventMedium>`
            
            .. attribute:: ccmhistoryeventconfigdestination
            
            	The configuration data destination for the event
            	**type**\:  :py:class:`HistoryEventMedium <ydk.models.cisco_ios_xe.CISCO_CONFIG_MAN_MIB.HistoryEventMedium>`
            
            .. attribute:: ccmhistoryeventterminaltype
            
            	If ccmHistoryEventCommandSource is 'commandLine', the terminal type, otherwise 'notApplicable'
            	**type**\:  :py:class:`Ccmhistoryeventterminaltype <ydk.models.cisco_ios_xe.CISCO_CONFIG_MAN_MIB.CISCOCONFIGMANMIB.Ccmhistoryeventtable.Ccmhistoryevententry.Ccmhistoryeventterminaltype>`
            
            .. attribute:: ccmhistoryeventterminalnumber
            
            	If ccmHistoryEventCommandSource is 'commandLine', the terminal number.  The value is \-1 if not available or not applicable
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: ccmhistoryeventterminaluser
            
            	If ccmHistoryEventCommandSource is 'commandLine', the name of the logged in user.  The length is zero if not available or not applicable
            	**type**\: str
            
            	**length:** 0..64
            
            .. attribute:: ccmhistoryeventterminallocation
            
            	If ccmHistoryEventCommandSource is 'commandLine', the hard\-wired location of the terminal or the remote  host for an incoming connection.  The length is zero  if not available or not applicable
            	**type**\: str
            
            	**length:** 0..64
            
            .. attribute:: ccmhistoryeventcommandsourceaddress
            
            	If ccmHistoryEventTerminalType is 'virtual', the internet address of the connected system.  If ccmHistoryEventCommandSource is 'snmp', the internet address of the requester.  The value is 0.0.0.0 if not available or not  applicable.  This object is deprecated by ccmHistoryEventCommandSourceAddrRev1
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**status**\: deprecated
            
            .. attribute:: ccmhistoryeventvirtualhostname
            
            	If ccmHistoryEventTerminalType is 'virtual', the host name of the connected system.  The length is zero if not available or not applicable
            	**type**\: str
            
            	**length:** 0..64
            
            .. attribute:: ccmhistoryeventserveraddress
            
            	If ccmHistoryEventConfigSource or ccmHistoryEventConfigDestination is 'networkTftp' or 'networkRcp', the internet address of the storage file server.  The value is 0.0.0.0 if not applicable or not         available.         This object is deprecated by         ccmHistoryEventServerAddrRev1
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**status**\: deprecated
            
            .. attribute:: ccmhistoryeventfile
            
            	If ccmHistoryEventConfigSource or ccmHistoryEventConfigDestination is 'networkTftp' or 'networkRcp', the configuration file name at the storage file server.  The length is zero if not available or not applicable
            	**type**\: str
            
            	**length:** 0..64
            
            .. attribute:: ccmhistoryeventrcpuser
            
            	If ccmHistoryEventConfigSource or ccmHistoryEventConfigDestination is 'networkRcp', the remote user name.  The length is zero if not applicable or not available
            	**type**\: str
            
            	**length:** 0..64
            
            .. attribute:: ccmhistoryclicmdentriesbumped
            
            	The number of times the oldest entry in ccmCLIHistoryCommandTable with first index as  ccmHistoryEventIndex was deleted to make  room for a new entry.  This object is applicable only if  ccmHistoryEventCommandSource has a value  of 'commandLine'
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ccmhistoryeventcommandsourceaddrtype
            
            	This object indicates the transport type of the address contained in ccmHistoryEventCommandSourceAddrRev1.  The value will be zero if not available or not applicable
            	**type**\:  :py:class:`InetAddressType <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetAddressType>`
            
            .. attribute:: ccmhistoryeventcommandsourceaddrrev1
            
            	If ccmHistoryEventTerminalType is 'virtual', the internet address of the connected system.  If ccmHistoryEventCommandSource is 'snmp', the internet address of the requester.  The value of all bit's is zero  if not available or not applicable.  The Format of this address depends on the value of the ccmHistoryEventCommandSourceAddrType object.  This object deprecates ccmHistoryEventCommandSourceAddress
            	**type**\: str
            
            	**length:** 0..255
            
            .. attribute:: ccmhistoryeventserveraddrtype
            
            	This object indicates the transport type of the address contained in ccmHistoryEventServerAddrRev1.  The value will be zero if not available or not aplicable
            	**type**\:  :py:class:`InetAddressType <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetAddressType>`
            
            .. attribute:: ccmhistoryeventserveraddrrev1
            
            	If ccmHistoryEventConfigSource or ccmHistoryEventConfigDestination is 'networkTftp' or 'networkRcp', the internet address of the storage file server.   The value of all bits is 0s if not applicable or not available.  The Format of this address depends on the value of the ccmHistoryEventServerAddrType object.  This object deprecates ccmHistoryEventServerAddress
            	**type**\: str
            
            	**length:** 0..255
            
            

            """

            _prefix = 'CISCO-CONFIG-MAN-MIB'
            _revision = '2007-04-27'

            def __init__(self):
                super(CISCOCONFIGMANMIB.Ccmhistoryeventtable.Ccmhistoryevententry, self).__init__()

                self.yang_name = "ccmHistoryEventEntry"
                self.yang_parent_name = "ccmHistoryEventTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ccmhistoryeventindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ccmhistoryeventindex', YLeaf(YType.int32, 'ccmHistoryEventIndex')),
                    ('ccmhistoryeventtime', YLeaf(YType.uint32, 'ccmHistoryEventTime')),
                    ('ccmhistoryeventcommandsource', YLeaf(YType.enumeration, 'ccmHistoryEventCommandSource')),
                    ('ccmhistoryeventconfigsource', YLeaf(YType.enumeration, 'ccmHistoryEventConfigSource')),
                    ('ccmhistoryeventconfigdestination', YLeaf(YType.enumeration, 'ccmHistoryEventConfigDestination')),
                    ('ccmhistoryeventterminaltype', YLeaf(YType.enumeration, 'ccmHistoryEventTerminalType')),
                    ('ccmhistoryeventterminalnumber', YLeaf(YType.int32, 'ccmHistoryEventTerminalNumber')),
                    ('ccmhistoryeventterminaluser', YLeaf(YType.str, 'ccmHistoryEventTerminalUser')),
                    ('ccmhistoryeventterminallocation', YLeaf(YType.str, 'ccmHistoryEventTerminalLocation')),
                    ('ccmhistoryeventcommandsourceaddress', YLeaf(YType.str, 'ccmHistoryEventCommandSourceAddress')),
                    ('ccmhistoryeventvirtualhostname', YLeaf(YType.str, 'ccmHistoryEventVirtualHostName')),
                    ('ccmhistoryeventserveraddress', YLeaf(YType.str, 'ccmHistoryEventServerAddress')),
                    ('ccmhistoryeventfile', YLeaf(YType.str, 'ccmHistoryEventFile')),
                    ('ccmhistoryeventrcpuser', YLeaf(YType.str, 'ccmHistoryEventRcpUser')),
                    ('ccmhistoryclicmdentriesbumped', YLeaf(YType.uint32, 'ccmHistoryCLICmdEntriesBumped')),
                    ('ccmhistoryeventcommandsourceaddrtype', YLeaf(YType.enumeration, 'ccmHistoryEventCommandSourceAddrType')),
                    ('ccmhistoryeventcommandsourceaddrrev1', YLeaf(YType.str, 'ccmHistoryEventCommandSourceAddrRev1')),
                    ('ccmhistoryeventserveraddrtype', YLeaf(YType.enumeration, 'ccmHistoryEventServerAddrType')),
                    ('ccmhistoryeventserveraddrrev1', YLeaf(YType.str, 'ccmHistoryEventServerAddrRev1')),
                ])
                self.ccmhistoryeventindex = None
                self.ccmhistoryeventtime = None
                self.ccmhistoryeventcommandsource = None
                self.ccmhistoryeventconfigsource = None
                self.ccmhistoryeventconfigdestination = None
                self.ccmhistoryeventterminaltype = None
                self.ccmhistoryeventterminalnumber = None
                self.ccmhistoryeventterminaluser = None
                self.ccmhistoryeventterminallocation = None
                self.ccmhistoryeventcommandsourceaddress = None
                self.ccmhistoryeventvirtualhostname = None
                self.ccmhistoryeventserveraddress = None
                self.ccmhistoryeventfile = None
                self.ccmhistoryeventrcpuser = None
                self.ccmhistoryclicmdentriesbumped = None
                self.ccmhistoryeventcommandsourceaddrtype = None
                self.ccmhistoryeventcommandsourceaddrrev1 = None
                self.ccmhistoryeventserveraddrtype = None
                self.ccmhistoryeventserveraddrrev1 = None
                self._segment_path = lambda: "ccmHistoryEventEntry" + "[ccmHistoryEventIndex='" + str(self.ccmhistoryeventindex) + "']"
                self._absolute_path = lambda: "CISCO-CONFIG-MAN-MIB:CISCO-CONFIG-MAN-MIB/ccmHistoryEventTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOCONFIGMANMIB.Ccmhistoryeventtable.Ccmhistoryevententry, ['ccmhistoryeventindex', 'ccmhistoryeventtime', 'ccmhistoryeventcommandsource', 'ccmhistoryeventconfigsource', 'ccmhistoryeventconfigdestination', 'ccmhistoryeventterminaltype', 'ccmhistoryeventterminalnumber', 'ccmhistoryeventterminaluser', 'ccmhistoryeventterminallocation', 'ccmhistoryeventcommandsourceaddress', 'ccmhistoryeventvirtualhostname', 'ccmhistoryeventserveraddress', 'ccmhistoryeventfile', 'ccmhistoryeventrcpuser', 'ccmhistoryclicmdentriesbumped', 'ccmhistoryeventcommandsourceaddrtype', 'ccmhistoryeventcommandsourceaddrrev1', 'ccmhistoryeventserveraddrtype', 'ccmhistoryeventserveraddrrev1'], name, value)

            class Ccmhistoryeventcommandsource(Enum):
                """
                Ccmhistoryeventcommandsource (Enum Class)

                The source of the command that instigated the event.

                .. data:: commandLine = 1

                .. data:: snmp = 2

                """

                commandLine = Enum.YLeaf(1, "commandLine")

                snmp = Enum.YLeaf(2, "snmp")


            class Ccmhistoryeventterminaltype(Enum):
                """
                Ccmhistoryeventterminaltype (Enum Class)

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



    class Ccmclihistorycommandtable(Entity):
        """
        A table of CLI commands that took effect during
        configuration events.
        
        .. attribute:: ccmclihistorycommandentry
        
        	Information about the CLI commands that took effect during the configuration event pointed by  ccmCLIHistoryEventIndex.  A set of rows in this table having the first index as ccmHistoryEventIndex will store the CLI commands entered during the corresponding  configuration event in ccmHistoryEventTable.  An entry will be created in this table only if  the corresponding entry in ccmHistoryEventTable has  a value of 'commandLine' for  ccmHistoryEventCommandSource
        	**type**\: list of  		 :py:class:`Ccmclihistorycommandentry <ydk.models.cisco_ios_xe.CISCO_CONFIG_MAN_MIB.CISCOCONFIGMANMIB.Ccmclihistorycommandtable.Ccmclihistorycommandentry>`
        
        

        """

        _prefix = 'CISCO-CONFIG-MAN-MIB'
        _revision = '2007-04-27'

        def __init__(self):
            super(CISCOCONFIGMANMIB.Ccmclihistorycommandtable, self).__init__()

            self.yang_name = "ccmCLIHistoryCommandTable"
            self.yang_parent_name = "CISCO-CONFIG-MAN-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("ccmCLIHistoryCommandEntry", ("ccmclihistorycommandentry", CISCOCONFIGMANMIB.Ccmclihistorycommandtable.Ccmclihistorycommandentry))])
            self._leafs = OrderedDict()

            self.ccmclihistorycommandentry = YList(self)
            self._segment_path = lambda: "ccmCLIHistoryCommandTable"
            self._absolute_path = lambda: "CISCO-CONFIG-MAN-MIB:CISCO-CONFIG-MAN-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOCONFIGMANMIB.Ccmclihistorycommandtable, [], name, value)


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
            
            .. attribute:: ccmhistoryeventindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ccmhistoryeventindex <ydk.models.cisco_ios_xe.CISCO_CONFIG_MAN_MIB.CISCOCONFIGMANMIB.Ccmhistoryeventtable.Ccmhistoryevententry>`
            
            .. attribute:: ccmclihistorycommandindex  (key)
            
            	A monotonically increasing integer for the purpose of indexing CLI commands which took effect during a configuration event
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: ccmclihistorycommand
            
            	The CLI command entered which took effect during the configuration event pointed by  ccmHistoryEventIndex
            	**type**\: str
            
            

            """

            _prefix = 'CISCO-CONFIG-MAN-MIB'
            _revision = '2007-04-27'

            def __init__(self):
                super(CISCOCONFIGMANMIB.Ccmclihistorycommandtable.Ccmclihistorycommandentry, self).__init__()

                self.yang_name = "ccmCLIHistoryCommandEntry"
                self.yang_parent_name = "ccmCLIHistoryCommandTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ccmhistoryeventindex','ccmclihistorycommandindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ccmhistoryeventindex', YLeaf(YType.str, 'ccmHistoryEventIndex')),
                    ('ccmclihistorycommandindex', YLeaf(YType.uint32, 'ccmCLIHistoryCommandIndex')),
                    ('ccmclihistorycommand', YLeaf(YType.str, 'ccmCLIHistoryCommand')),
                ])
                self.ccmhistoryeventindex = None
                self.ccmclihistorycommandindex = None
                self.ccmclihistorycommand = None
                self._segment_path = lambda: "ccmCLIHistoryCommandEntry" + "[ccmHistoryEventIndex='" + str(self.ccmhistoryeventindex) + "']" + "[ccmCLIHistoryCommandIndex='" + str(self.ccmclihistorycommandindex) + "']"
                self._absolute_path = lambda: "CISCO-CONFIG-MAN-MIB:CISCO-CONFIG-MAN-MIB/ccmCLIHistoryCommandTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOCONFIGMANMIB.Ccmclihistorycommandtable.Ccmclihistorycommandentry, ['ccmhistoryeventindex', 'ccmclihistorycommandindex', 'ccmclihistorycommand'], name, value)

    def clone_ptr(self):
        self._top_entity = CISCOCONFIGMANMIB()
        return self._top_entity

