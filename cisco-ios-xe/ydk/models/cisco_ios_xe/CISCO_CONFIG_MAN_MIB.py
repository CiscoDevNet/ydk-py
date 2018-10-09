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
    
    	
    	**type**\:  :py:class:`CcmHistory <ydk.models.cisco_ios_xe.CISCO_CONFIG_MAN_MIB.CISCOCONFIGMANMIB.CcmHistory>`
    
    .. attribute:: ccmclihistory
    
    	
    	**type**\:  :py:class:`CcmCLIHistory <ydk.models.cisco_ios_xe.CISCO_CONFIG_MAN_MIB.CISCOCONFIGMANMIB.CcmCLIHistory>`
    
    .. attribute:: ccmclicfg
    
    	
    	**type**\:  :py:class:`CcmCLICfg <ydk.models.cisco_ios_xe.CISCO_CONFIG_MAN_MIB.CISCOCONFIGMANMIB.CcmCLICfg>`
    
    .. attribute:: ccmctidobjects
    
    	
    	**type**\:  :py:class:`CcmCTIDObjects <ydk.models.cisco_ios_xe.CISCO_CONFIG_MAN_MIB.CISCOCONFIGMANMIB.CcmCTIDObjects>`
    
    .. attribute:: ccmhistoryeventtable
    
    	A table of configuration events on this router
    	**type**\:  :py:class:`CcmHistoryEventTable <ydk.models.cisco_ios_xe.CISCO_CONFIG_MAN_MIB.CISCOCONFIGMANMIB.CcmHistoryEventTable>`
    
    .. attribute:: ccmclihistorycommandtable
    
    	A table of CLI commands that took effect during configuration events
    	**type**\:  :py:class:`CcmCLIHistoryCommandTable <ydk.models.cisco_ios_xe.CISCO_CONFIG_MAN_MIB.CISCOCONFIGMANMIB.CcmCLIHistoryCommandTable>`
    
    

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
        self._child_classes = OrderedDict([("ccmHistory", ("ccmhistory", CISCOCONFIGMANMIB.CcmHistory)), ("ccmCLIHistory", ("ccmclihistory", CISCOCONFIGMANMIB.CcmCLIHistory)), ("ccmCLICfg", ("ccmclicfg", CISCOCONFIGMANMIB.CcmCLICfg)), ("ccmCTIDObjects", ("ccmctidobjects", CISCOCONFIGMANMIB.CcmCTIDObjects)), ("ccmHistoryEventTable", ("ccmhistoryeventtable", CISCOCONFIGMANMIB.CcmHistoryEventTable)), ("ccmCLIHistoryCommandTable", ("ccmclihistorycommandtable", CISCOCONFIGMANMIB.CcmCLIHistoryCommandTable))])
        self._leafs = OrderedDict()

        self.ccmhistory = CISCOCONFIGMANMIB.CcmHistory()
        self.ccmhistory.parent = self
        self._children_name_map["ccmhistory"] = "ccmHistory"

        self.ccmclihistory = CISCOCONFIGMANMIB.CcmCLIHistory()
        self.ccmclihistory.parent = self
        self._children_name_map["ccmclihistory"] = "ccmCLIHistory"

        self.ccmclicfg = CISCOCONFIGMANMIB.CcmCLICfg()
        self.ccmclicfg.parent = self
        self._children_name_map["ccmclicfg"] = "ccmCLICfg"

        self.ccmctidobjects = CISCOCONFIGMANMIB.CcmCTIDObjects()
        self.ccmctidobjects.parent = self
        self._children_name_map["ccmctidobjects"] = "ccmCTIDObjects"

        self.ccmhistoryeventtable = CISCOCONFIGMANMIB.CcmHistoryEventTable()
        self.ccmhistoryeventtable.parent = self
        self._children_name_map["ccmhistoryeventtable"] = "ccmHistoryEventTable"

        self.ccmclihistorycommandtable = CISCOCONFIGMANMIB.CcmCLIHistoryCommandTable()
        self.ccmclihistorycommandtable.parent = self
        self._children_name_map["ccmclihistorycommandtable"] = "ccmCLIHistoryCommandTable"
        self._segment_path = lambda: "CISCO-CONFIG-MAN-MIB:CISCO-CONFIG-MAN-MIB"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(CISCOCONFIGMANMIB, [], name, value)


    class CcmHistory(Entity):
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
            super(CISCOCONFIGMANMIB.CcmHistory, self).__init__()

            self.yang_name = "ccmHistory"
            self.yang_parent_name = "CISCO-CONFIG-MAN-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('ccmhistoryrunninglastchanged', (YLeaf(YType.uint32, 'ccmHistoryRunningLastChanged'), ['int'])),
                ('ccmhistoryrunninglastsaved', (YLeaf(YType.uint32, 'ccmHistoryRunningLastSaved'), ['int'])),
                ('ccmhistorystartuplastchanged', (YLeaf(YType.uint32, 'ccmHistoryStartupLastChanged'), ['int'])),
                ('ccmhistorymaxevententries', (YLeaf(YType.int32, 'ccmHistoryMaxEventEntries'), ['int'])),
                ('ccmhistoryevententriesbumped', (YLeaf(YType.uint32, 'ccmHistoryEventEntriesBumped'), ['int'])),
            ])
            self.ccmhistoryrunninglastchanged = None
            self.ccmhistoryrunninglastsaved = None
            self.ccmhistorystartuplastchanged = None
            self.ccmhistorymaxevententries = None
            self.ccmhistoryevententriesbumped = None
            self._segment_path = lambda: "ccmHistory"
            self._absolute_path = lambda: "CISCO-CONFIG-MAN-MIB:CISCO-CONFIG-MAN-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOCONFIGMANMIB.CcmHistory, ['ccmhistoryrunninglastchanged', 'ccmhistoryrunninglastsaved', 'ccmhistorystartuplastchanged', 'ccmhistorymaxevententries', 'ccmhistoryevententriesbumped'], name, value)


    class CcmCLIHistory(Entity):
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
            super(CISCOCONFIGMANMIB.CcmCLIHistory, self).__init__()

            self.yang_name = "ccmCLIHistory"
            self.yang_parent_name = "CISCO-CONFIG-MAN-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('ccmclihistorymaxcmdentries', (YLeaf(YType.uint32, 'ccmCLIHistoryMaxCmdEntries'), ['int'])),
                ('ccmclihistorycmdentries', (YLeaf(YType.uint32, 'ccmCLIHistoryCmdEntries'), ['int'])),
                ('ccmclihistorycmdentriesallowed', (YLeaf(YType.uint32, 'ccmCLIHistoryCmdEntriesAllowed'), ['int'])),
            ])
            self.ccmclihistorymaxcmdentries = None
            self.ccmclihistorycmdentries = None
            self.ccmclihistorycmdentriesallowed = None
            self._segment_path = lambda: "ccmCLIHistory"
            self._absolute_path = lambda: "CISCO-CONFIG-MAN-MIB:CISCO-CONFIG-MAN-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOCONFIGMANMIB.CcmCLIHistory, ['ccmclihistorymaxcmdentries', 'ccmclihistorycmdentries', 'ccmclihistorycmdentriesallowed'], name, value)


    class CcmCLICfg(Entity):
        """
        
        
        .. attribute:: ccmclicfgrunconfnotifenable
        
        	This variable indicates whether the system produces the ccmCLIRunningConfigChanged notification. A false  value will prevent notifications from being generated  by this system
        	**type**\: bool
        
        

        """

        _prefix = 'CISCO-CONFIG-MAN-MIB'
        _revision = '2007-04-27'

        def __init__(self):
            super(CISCOCONFIGMANMIB.CcmCLICfg, self).__init__()

            self.yang_name = "ccmCLICfg"
            self.yang_parent_name = "CISCO-CONFIG-MAN-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('ccmclicfgrunconfnotifenable', (YLeaf(YType.boolean, 'ccmCLICfgRunConfNotifEnable'), ['bool'])),
            ])
            self.ccmclicfgrunconfnotifenable = None
            self._segment_path = lambda: "ccmCLICfg"
            self._absolute_path = lambda: "CISCO-CONFIG-MAN-MIB:CISCO-CONFIG-MAN-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOCONFIGMANMIB.CcmCLICfg, ['ccmclicfgrunconfnotifenable'], name, value)


    class CcmCTIDObjects(Entity):
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
            super(CISCOCONFIGMANMIB.CcmCTIDObjects, self).__init__()

            self.yang_name = "ccmCTIDObjects"
            self.yang_parent_name = "CISCO-CONFIG-MAN-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('ccmctid', (YLeaf(YType.uint64, 'ccmCTID'), ['int'])),
                ('ccmctidlastchangetime', (YLeaf(YType.str, 'ccmCTIDLastChangeTime'), ['str'])),
                ('ccmctidwhochanged', (YLeaf(YType.str, 'ccmCTIDWhoChanged'), ['str'])),
                ('ccmctidrolledovernotifenable', (YLeaf(YType.boolean, 'ccmCTIDRolledOverNotifEnable'), ['bool'])),
            ])
            self.ccmctid = None
            self.ccmctidlastchangetime = None
            self.ccmctidwhochanged = None
            self.ccmctidrolledovernotifenable = None
            self._segment_path = lambda: "ccmCTIDObjects"
            self._absolute_path = lambda: "CISCO-CONFIG-MAN-MIB:CISCO-CONFIG-MAN-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOCONFIGMANMIB.CcmCTIDObjects, ['ccmctid', 'ccmctidlastchangetime', 'ccmctidwhochanged', 'ccmctidrolledovernotifenable'], name, value)


    class CcmHistoryEventTable(Entity):
        """
        A table of configuration events on this router.
        
        .. attribute:: ccmhistoryevententry
        
        	Information about a configuration event on this router
        	**type**\: list of  		 :py:class:`CcmHistoryEventEntry <ydk.models.cisco_ios_xe.CISCO_CONFIG_MAN_MIB.CISCOCONFIGMANMIB.CcmHistoryEventTable.CcmHistoryEventEntry>`
        
        

        """

        _prefix = 'CISCO-CONFIG-MAN-MIB'
        _revision = '2007-04-27'

        def __init__(self):
            super(CISCOCONFIGMANMIB.CcmHistoryEventTable, self).__init__()

            self.yang_name = "ccmHistoryEventTable"
            self.yang_parent_name = "CISCO-CONFIG-MAN-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("ccmHistoryEventEntry", ("ccmhistoryevententry", CISCOCONFIGMANMIB.CcmHistoryEventTable.CcmHistoryEventEntry))])
            self._leafs = OrderedDict()

            self.ccmhistoryevententry = YList(self)
            self._segment_path = lambda: "ccmHistoryEventTable"
            self._absolute_path = lambda: "CISCO-CONFIG-MAN-MIB:CISCO-CONFIG-MAN-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOCONFIGMANMIB.CcmHistoryEventTable, [], name, value)


        class CcmHistoryEventEntry(Entity):
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
            	**type**\:  :py:class:`CcmHistoryEventCommandSource <ydk.models.cisco_ios_xe.CISCO_CONFIG_MAN_MIB.CISCOCONFIGMANMIB.CcmHistoryEventTable.CcmHistoryEventEntry.CcmHistoryEventCommandSource>`
            
            .. attribute:: ccmhistoryeventconfigsource
            
            	The configuration data source for the event
            	**type**\:  :py:class:`HistoryEventMedium <ydk.models.cisco_ios_xe.CISCO_CONFIG_MAN_MIB.HistoryEventMedium>`
            
            .. attribute:: ccmhistoryeventconfigdestination
            
            	The configuration data destination for the event
            	**type**\:  :py:class:`HistoryEventMedium <ydk.models.cisco_ios_xe.CISCO_CONFIG_MAN_MIB.HistoryEventMedium>`
            
            .. attribute:: ccmhistoryeventterminaltype
            
            	If ccmHistoryEventCommandSource is 'commandLine', the terminal type, otherwise 'notApplicable'
            	**type**\:  :py:class:`CcmHistoryEventTerminalType <ydk.models.cisco_ios_xe.CISCO_CONFIG_MAN_MIB.CISCOCONFIGMANMIB.CcmHistoryEventTable.CcmHistoryEventEntry.CcmHistoryEventTerminalType>`
            
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
                super(CISCOCONFIGMANMIB.CcmHistoryEventTable.CcmHistoryEventEntry, self).__init__()

                self.yang_name = "ccmHistoryEventEntry"
                self.yang_parent_name = "ccmHistoryEventTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ccmhistoryeventindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ccmhistoryeventindex', (YLeaf(YType.int32, 'ccmHistoryEventIndex'), ['int'])),
                    ('ccmhistoryeventtime', (YLeaf(YType.uint32, 'ccmHistoryEventTime'), ['int'])),
                    ('ccmhistoryeventcommandsource', (YLeaf(YType.enumeration, 'ccmHistoryEventCommandSource'), [('ydk.models.cisco_ios_xe.CISCO_CONFIG_MAN_MIB', 'CISCOCONFIGMANMIB', 'CcmHistoryEventTable.CcmHistoryEventEntry.CcmHistoryEventCommandSource')])),
                    ('ccmhistoryeventconfigsource', (YLeaf(YType.enumeration, 'ccmHistoryEventConfigSource'), [('ydk.models.cisco_ios_xe.CISCO_CONFIG_MAN_MIB', 'HistoryEventMedium', '')])),
                    ('ccmhistoryeventconfigdestination', (YLeaf(YType.enumeration, 'ccmHistoryEventConfigDestination'), [('ydk.models.cisco_ios_xe.CISCO_CONFIG_MAN_MIB', 'HistoryEventMedium', '')])),
                    ('ccmhistoryeventterminaltype', (YLeaf(YType.enumeration, 'ccmHistoryEventTerminalType'), [('ydk.models.cisco_ios_xe.CISCO_CONFIG_MAN_MIB', 'CISCOCONFIGMANMIB', 'CcmHistoryEventTable.CcmHistoryEventEntry.CcmHistoryEventTerminalType')])),
                    ('ccmhistoryeventterminalnumber', (YLeaf(YType.int32, 'ccmHistoryEventTerminalNumber'), ['int'])),
                    ('ccmhistoryeventterminaluser', (YLeaf(YType.str, 'ccmHistoryEventTerminalUser'), ['str'])),
                    ('ccmhistoryeventterminallocation', (YLeaf(YType.str, 'ccmHistoryEventTerminalLocation'), ['str'])),
                    ('ccmhistoryeventcommandsourceaddress', (YLeaf(YType.str, 'ccmHistoryEventCommandSourceAddress'), ['str'])),
                    ('ccmhistoryeventvirtualhostname', (YLeaf(YType.str, 'ccmHistoryEventVirtualHostName'), ['str'])),
                    ('ccmhistoryeventserveraddress', (YLeaf(YType.str, 'ccmHistoryEventServerAddress'), ['str'])),
                    ('ccmhistoryeventfile', (YLeaf(YType.str, 'ccmHistoryEventFile'), ['str'])),
                    ('ccmhistoryeventrcpuser', (YLeaf(YType.str, 'ccmHistoryEventRcpUser'), ['str'])),
                    ('ccmhistoryclicmdentriesbumped', (YLeaf(YType.uint32, 'ccmHistoryCLICmdEntriesBumped'), ['int'])),
                    ('ccmhistoryeventcommandsourceaddrtype', (YLeaf(YType.enumeration, 'ccmHistoryEventCommandSourceAddrType'), [('ydk.models.cisco_ios_xe.INET_ADDRESS_MIB', 'InetAddressType', '')])),
                    ('ccmhistoryeventcommandsourceaddrrev1', (YLeaf(YType.str, 'ccmHistoryEventCommandSourceAddrRev1'), ['str'])),
                    ('ccmhistoryeventserveraddrtype', (YLeaf(YType.enumeration, 'ccmHistoryEventServerAddrType'), [('ydk.models.cisco_ios_xe.INET_ADDRESS_MIB', 'InetAddressType', '')])),
                    ('ccmhistoryeventserveraddrrev1', (YLeaf(YType.str, 'ccmHistoryEventServerAddrRev1'), ['str'])),
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
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOCONFIGMANMIB.CcmHistoryEventTable.CcmHistoryEventEntry, ['ccmhistoryeventindex', 'ccmhistoryeventtime', 'ccmhistoryeventcommandsource', 'ccmhistoryeventconfigsource', 'ccmhistoryeventconfigdestination', 'ccmhistoryeventterminaltype', 'ccmhistoryeventterminalnumber', 'ccmhistoryeventterminaluser', 'ccmhistoryeventterminallocation', 'ccmhistoryeventcommandsourceaddress', 'ccmhistoryeventvirtualhostname', 'ccmhistoryeventserveraddress', 'ccmhistoryeventfile', 'ccmhistoryeventrcpuser', 'ccmhistoryclicmdentriesbumped', 'ccmhistoryeventcommandsourceaddrtype', 'ccmhistoryeventcommandsourceaddrrev1', 'ccmhistoryeventserveraddrtype', 'ccmhistoryeventserveraddrrev1'], name, value)

            class CcmHistoryEventCommandSource(Enum):
                """
                CcmHistoryEventCommandSource (Enum Class)

                The source of the command that instigated the event.

                .. data:: commandLine = 1

                .. data:: snmp = 2

                """

                commandLine = Enum.YLeaf(1, "commandLine")

                snmp = Enum.YLeaf(2, "snmp")


            class CcmHistoryEventTerminalType(Enum):
                """
                CcmHistoryEventTerminalType (Enum Class)

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



    class CcmCLIHistoryCommandTable(Entity):
        """
        A table of CLI commands that took effect during
        configuration events.
        
        .. attribute:: ccmclihistorycommandentry
        
        	Information about the CLI commands that took effect during the configuration event pointed by  ccmCLIHistoryEventIndex.  A set of rows in this table having the first index as ccmHistoryEventIndex will store the CLI commands entered during the corresponding  configuration event in ccmHistoryEventTable.  An entry will be created in this table only if  the corresponding entry in ccmHistoryEventTable has  a value of 'commandLine' for  ccmHistoryEventCommandSource
        	**type**\: list of  		 :py:class:`CcmCLIHistoryCommandEntry <ydk.models.cisco_ios_xe.CISCO_CONFIG_MAN_MIB.CISCOCONFIGMANMIB.CcmCLIHistoryCommandTable.CcmCLIHistoryCommandEntry>`
        
        

        """

        _prefix = 'CISCO-CONFIG-MAN-MIB'
        _revision = '2007-04-27'

        def __init__(self):
            super(CISCOCONFIGMANMIB.CcmCLIHistoryCommandTable, self).__init__()

            self.yang_name = "ccmCLIHistoryCommandTable"
            self.yang_parent_name = "CISCO-CONFIG-MAN-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("ccmCLIHistoryCommandEntry", ("ccmclihistorycommandentry", CISCOCONFIGMANMIB.CcmCLIHistoryCommandTable.CcmCLIHistoryCommandEntry))])
            self._leafs = OrderedDict()

            self.ccmclihistorycommandentry = YList(self)
            self._segment_path = lambda: "ccmCLIHistoryCommandTable"
            self._absolute_path = lambda: "CISCO-CONFIG-MAN-MIB:CISCO-CONFIG-MAN-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOCONFIGMANMIB.CcmCLIHistoryCommandTable, [], name, value)


        class CcmCLIHistoryCommandEntry(Entity):
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
            
            	**refers to**\:  :py:class:`ccmhistoryeventindex <ydk.models.cisco_ios_xe.CISCO_CONFIG_MAN_MIB.CISCOCONFIGMANMIB.CcmHistoryEventTable.CcmHistoryEventEntry>`
            
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
                super(CISCOCONFIGMANMIB.CcmCLIHistoryCommandTable.CcmCLIHistoryCommandEntry, self).__init__()

                self.yang_name = "ccmCLIHistoryCommandEntry"
                self.yang_parent_name = "ccmCLIHistoryCommandTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ccmhistoryeventindex','ccmclihistorycommandindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ccmhistoryeventindex', (YLeaf(YType.str, 'ccmHistoryEventIndex'), ['int'])),
                    ('ccmclihistorycommandindex', (YLeaf(YType.uint32, 'ccmCLIHistoryCommandIndex'), ['int'])),
                    ('ccmclihistorycommand', (YLeaf(YType.str, 'ccmCLIHistoryCommand'), ['str'])),
                ])
                self.ccmhistoryeventindex = None
                self.ccmclihistorycommandindex = None
                self.ccmclihistorycommand = None
                self._segment_path = lambda: "ccmCLIHistoryCommandEntry" + "[ccmHistoryEventIndex='" + str(self.ccmhistoryeventindex) + "']" + "[ccmCLIHistoryCommandIndex='" + str(self.ccmclihistorycommandindex) + "']"
                self._absolute_path = lambda: "CISCO-CONFIG-MAN-MIB:CISCO-CONFIG-MAN-MIB/ccmCLIHistoryCommandTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOCONFIGMANMIB.CcmCLIHistoryCommandTable.CcmCLIHistoryCommandEntry, ['ccmhistoryeventindex', 'ccmclihistorycommandindex', 'ccmclihistorycommand'], name, value)

    def clone_ptr(self):
        self._top_entity = CISCOCONFIGMANMIB()
        return self._top_entity

