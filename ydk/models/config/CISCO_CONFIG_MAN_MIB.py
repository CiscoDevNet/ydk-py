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


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError


from ydk.models.inet.INET_ADDRESS_MIB import InetAddressType_Enum

class HistoryEventMedium_Enum(Enum):
    """
    HistoryEventMedium_Enum

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

    """

    ERASE = 1

    COMMANDSOURCE = 2

    RUNNING = 3

    STARTUP = 4

    LOCAL = 5

    NETWORKTFTP = 6

    NETWORKRCP = 7

    NETWORKFTP = 8

    NETWORKSCP = 9


    @staticmethod
    def _meta_info():
        from ydk.models.config._meta import _CISCO_CONFIG_MAN_MIB as meta
        return meta._meta_table['HistoryEventMedium_Enum']



class CISCOCONFIGMANMIB(object):
    """
    
    
    .. attribute:: ccmclicfg
    
    	
    	**type**\: :py:class:`CcmCLICfg <ydk.models.config.CISCO_CONFIG_MAN_MIB.CISCOCONFIGMANMIB.CcmCLICfg>`
    
    .. attribute:: ccmclihistory
    
    	
    	**type**\: :py:class:`CcmCLIHistory <ydk.models.config.CISCO_CONFIG_MAN_MIB.CISCOCONFIGMANMIB.CcmCLIHistory>`
    
    .. attribute:: ccmclihistorycommandtable
    
    	A table of CLI commands that took effect during configuration events
    	**type**\: :py:class:`CcmCLIHistoryCommandTable <ydk.models.config.CISCO_CONFIG_MAN_MIB.CISCOCONFIGMANMIB.CcmCLIHistoryCommandTable>`
    
    .. attribute:: ccmctidobjects
    
    	
    	**type**\: :py:class:`CcmCTIDObjects <ydk.models.config.CISCO_CONFIG_MAN_MIB.CISCOCONFIGMANMIB.CcmCTIDObjects>`
    
    .. attribute:: ccmhistory
    
    	
    	**type**\: :py:class:`CcmHistory <ydk.models.config.CISCO_CONFIG_MAN_MIB.CISCOCONFIGMANMIB.CcmHistory>`
    
    .. attribute:: ccmhistoryeventtable
    
    	A table of configuration events on this router
    	**type**\: :py:class:`CcmHistoryEventTable <ydk.models.config.CISCO_CONFIG_MAN_MIB.CISCOCONFIGMANMIB.CcmHistoryEventTable>`
    
    

    """

    _prefix = 'cisco-config'
    _revision = '2007-04-27'

    def __init__(self):
        self.ccmclicfg = CISCOCONFIGMANMIB.CcmCLICfg()
        self.ccmclicfg.parent = self
        self.ccmclihistory = CISCOCONFIGMANMIB.CcmCLIHistory()
        self.ccmclihistory.parent = self
        self.ccmclihistorycommandtable = CISCOCONFIGMANMIB.CcmCLIHistoryCommandTable()
        self.ccmclihistorycommandtable.parent = self
        self.ccmctidobjects = CISCOCONFIGMANMIB.CcmCTIDObjects()
        self.ccmctidobjects.parent = self
        self.ccmhistory = CISCOCONFIGMANMIB.CcmHistory()
        self.ccmhistory.parent = self
        self.ccmhistoryeventtable = CISCOCONFIGMANMIB.CcmHistoryEventTable()
        self.ccmhistoryeventtable.parent = self


    class CcmCLICfg(object):
        """
        
        
        .. attribute:: ccmclicfgrunconfnotifenable
        
        	This variable indicates whether the system produces the ccmCLIRunningConfigChanged notification. A false  value will prevent notifications from being generated  by this system
        	**type**\: bool
        
        

        """

        _prefix = 'cisco-config'
        _revision = '2007-04-27'

        def __init__(self):
            self.parent = None
            self.ccmclicfgrunconfnotifenable = None

        @property
        def _common_path(self):

            return '/CISCO-CONFIG-MAN-MIB:CISCO-CONFIG-MAN-MIB/CISCO-CONFIG-MAN-MIB:ccmCLICfg'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.ccmclicfgrunconfnotifenable is not None:
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.config._meta import _CISCO_CONFIG_MAN_MIB as meta
            return meta._meta_table['CISCOCONFIGMANMIB.CcmCLICfg']['meta_info']


    class CcmCLIHistory(object):
        """
        
        
        .. attribute:: ccmclihistorycmdentries
        
        	The current number of entries in ccmCLIHistoryCommandTable
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: ccmclihistorycmdentriesallowed
        
        	This object indicates the upper limit on the number of entries allowed in  ccmCLIHistoryCommandTable by the managed system
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: ccmclihistorymaxcmdentries
        
        	The maximum number of entries that can be held in ccmCLIHistoryCommandTable.  The recommended value for implementations is 100.  If the number of entries in ccmCLIHistoryCommandTable  exceeds the value of this object, old entries will be  bumped to make room for new entries.  The ccmCLIHistoryCommandTable will not be populated if the value of this object is 0
        	**type**\: int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'cisco-config'
        _revision = '2007-04-27'

        def __init__(self):
            self.parent = None
            self.ccmclihistorycmdentries = None
            self.ccmclihistorycmdentriesallowed = None
            self.ccmclihistorymaxcmdentries = None

        @property
        def _common_path(self):

            return '/CISCO-CONFIG-MAN-MIB:CISCO-CONFIG-MAN-MIB/CISCO-CONFIG-MAN-MIB:ccmCLIHistory'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.ccmclihistorycmdentries is not None:
                return True

            if self.ccmclihistorycmdentriesallowed is not None:
                return True

            if self.ccmclihistorymaxcmdentries is not None:
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.config._meta import _CISCO_CONFIG_MAN_MIB as meta
            return meta._meta_table['CISCOCONFIGMANMIB.CcmCLIHistory']['meta_info']


    class CcmCLIHistoryCommandTable(object):
        """
        A table of CLI commands that took effect during
        configuration events.
        
        .. attribute:: ccmclihistorycommandentry
        
        	Information about the CLI commands that took effect during the configuration event pointed by  ccmCLIHistoryEventIndex.  A set of rows in this table having the first index as ccmHistoryEventIndex will store the CLI commands entered during the corresponding  configuration event in ccmHistoryEventTable.  An entry will be created in this table only if  the corresponding entry in ccmHistoryEventTable has  a value of 'commandLine' for  ccmHistoryEventCommandSource
        	**type**\: list of :py:class:`CcmCLIHistoryCommandEntry <ydk.models.config.CISCO_CONFIG_MAN_MIB.CISCOCONFIGMANMIB.CcmCLIHistoryCommandTable.CcmCLIHistoryCommandEntry>`
        
        

        """

        _prefix = 'cisco-config'
        _revision = '2007-04-27'

        def __init__(self):
            self.parent = None
            self.ccmclihistorycommandentry = YList()
            self.ccmclihistorycommandentry.parent = self
            self.ccmclihistorycommandentry.name = 'ccmclihistorycommandentry'


        class CcmCLIHistoryCommandEntry(object):
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
            
            .. attribute:: ccmclihistorycommandindex
            
            	A monotonically increasing integer for the purpose of indexing CLI commands which took effect during a configuration event
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: ccmhistoryeventindex
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: ccmclihistorycommand
            
            	The CLI command entered which took effect during the configuration event pointed by  ccmHistoryEventIndex
            	**type**\: str
            
            	**pattern:** \\p{IsBasicLatin}{0,255}
            
            

            """

            _prefix = 'cisco-config'
            _revision = '2007-04-27'

            def __init__(self):
                self.parent = None
                self.ccmclihistorycommandindex = None
                self.ccmhistoryeventindex = None
                self.ccmclihistorycommand = None

            @property
            def _common_path(self):
                if self.ccmclihistorycommandindex is None:
                    raise YPYDataValidationError('Key property ccmclihistorycommandindex is None')
                if self.ccmhistoryeventindex is None:
                    raise YPYDataValidationError('Key property ccmhistoryeventindex is None')

                return '/CISCO-CONFIG-MAN-MIB:CISCO-CONFIG-MAN-MIB/CISCO-CONFIG-MAN-MIB:ccmCLIHistoryCommandTable/CISCO-CONFIG-MAN-MIB:ccmCLIHistoryCommandEntry[CISCO-CONFIG-MAN-MIB:ccmCLIHistoryCommandIndex = ' + str(self.ccmclihistorycommandindex) + '][CISCO-CONFIG-MAN-MIB:ccmHistoryEventIndex = ' + str(self.ccmhistoryeventindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.ccmclihistorycommandindex is not None:
                    return True

                if self.ccmhistoryeventindex is not None:
                    return True

                if self.ccmclihistorycommand is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.config._meta import _CISCO_CONFIG_MAN_MIB as meta
                return meta._meta_table['CISCOCONFIGMANMIB.CcmCLIHistoryCommandTable.CcmCLIHistoryCommandEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-CONFIG-MAN-MIB:CISCO-CONFIG-MAN-MIB/CISCO-CONFIG-MAN-MIB:ccmCLIHistoryCommandTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.ccmclihistorycommandentry is not None:
                for child_ref in self.ccmclihistorycommandentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.config._meta import _CISCO_CONFIG_MAN_MIB as meta
            return meta._meta_table['CISCOCONFIGMANMIB.CcmCLIHistoryCommandTable']['meta_info']


    class CcmCTIDObjects(object):
        """
        
        
        .. attribute:: ccmctid
        
        	This object indicates the Config Change Tracking ID which uniquely represents version\-incrementing changes to the IOS  running configuration
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        .. attribute:: ccmctidlastchangetime
        
        	This object indicates the time when the Config Change Tracking ID last changed
        	**type**\: str
        
        .. attribute:: ccmctidrolledovernotifenable
        
        	This variable indicates whether the system produces the ccmCTIDRolledOver notification. A false value will prevent notifications from being generated by this system
        	**type**\: bool
        
        .. attribute:: ccmctidwhochanged
        
        	This object indicates the user who last reset the Config Change Tracking ID
        	**type**\: str
        
        	**range:** 0..255
        
        

        """

        _prefix = 'cisco-config'
        _revision = '2007-04-27'

        def __init__(self):
            self.parent = None
            self.ccmctid = None
            self.ccmctidlastchangetime = None
            self.ccmctidrolledovernotifenable = None
            self.ccmctidwhochanged = None

        @property
        def _common_path(self):

            return '/CISCO-CONFIG-MAN-MIB:CISCO-CONFIG-MAN-MIB/CISCO-CONFIG-MAN-MIB:ccmCTIDObjects'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.ccmctid is not None:
                return True

            if self.ccmctidlastchangetime is not None:
                return True

            if self.ccmctidrolledovernotifenable is not None:
                return True

            if self.ccmctidwhochanged is not None:
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.config._meta import _CISCO_CONFIG_MAN_MIB as meta
            return meta._meta_table['CISCOCONFIGMANMIB.CcmCTIDObjects']['meta_info']


    class CcmHistory(object):
        """
        
        
        .. attribute:: ccmhistoryevententriesbumped
        
        	The number of times the oldest entry in ccmHistoryEventTable was deleted to make room  for a new entry
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: ccmhistorymaxevententries
        
        	The maximum number of entries that can be held in ccmHistoryEventTable.  The recommended value for implementations is 10
        	**type**\: int
        
        	**range:** 0..2147483647
        
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
        
        

        """

        _prefix = 'cisco-config'
        _revision = '2007-04-27'

        def __init__(self):
            self.parent = None
            self.ccmhistoryevententriesbumped = None
            self.ccmhistorymaxevententries = None
            self.ccmhistoryrunninglastchanged = None
            self.ccmhistoryrunninglastsaved = None
            self.ccmhistorystartuplastchanged = None

        @property
        def _common_path(self):

            return '/CISCO-CONFIG-MAN-MIB:CISCO-CONFIG-MAN-MIB/CISCO-CONFIG-MAN-MIB:ccmHistory'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.ccmhistoryevententriesbumped is not None:
                return True

            if self.ccmhistorymaxevententries is not None:
                return True

            if self.ccmhistoryrunninglastchanged is not None:
                return True

            if self.ccmhistoryrunninglastsaved is not None:
                return True

            if self.ccmhistorystartuplastchanged is not None:
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.config._meta import _CISCO_CONFIG_MAN_MIB as meta
            return meta._meta_table['CISCOCONFIGMANMIB.CcmHistory']['meta_info']


    class CcmHistoryEventTable(object):
        """
        A table of configuration events on this router.
        
        .. attribute:: ccmhistoryevententry
        
        	Information about a configuration event on this router
        	**type**\: list of :py:class:`CcmHistoryEventEntry <ydk.models.config.CISCO_CONFIG_MAN_MIB.CISCOCONFIGMANMIB.CcmHistoryEventTable.CcmHistoryEventEntry>`
        
        

        """

        _prefix = 'cisco-config'
        _revision = '2007-04-27'

        def __init__(self):
            self.parent = None
            self.ccmhistoryevententry = YList()
            self.ccmhistoryevententry.parent = self
            self.ccmhistoryevententry.name = 'ccmhistoryevententry'


        class CcmHistoryEventEntry(object):
            """
            Information about a configuration event on this
            router.
            
            .. attribute:: ccmhistoryeventindex
            
            	A monotonically increasing integer for the sole purpose of indexing events.  When it reaches the  maximum value, an extremely unlikely event, the agent  wraps the value back to 1 and may flush existing  entries
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: ccmhistoryclicmdentriesbumped
            
            	The number of times the oldest entry in ccmCLIHistoryCommandTable with first index as  ccmHistoryEventIndex was deleted to make  room for a new entry.  This object is applicable only if  ccmHistoryEventCommandSource has a value  of 'commandLine'
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ccmhistoryeventcommandsource
            
            	The source of the command that instigated the event
            	**type**\: :py:class:`CcmHistoryEventCommandSource_Enum <ydk.models.config.CISCO_CONFIG_MAN_MIB.CISCOCONFIGMANMIB.CcmHistoryEventTable.CcmHistoryEventEntry.CcmHistoryEventCommandSource_Enum>`
            
            .. attribute:: ccmhistoryeventcommandsourceaddress
            
            	If ccmHistoryEventTerminalType is 'virtual', the internet address of the connected system.  If ccmHistoryEventCommandSource is 'snmp', the internet address of the requester.  The value is 0.0.0.0 if not available or not  applicable.  This object is deprecated by ccmHistoryEventCommandSourceAddrRev1
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: ccmhistoryeventcommandsourceaddrrev1
            
            	If ccmHistoryEventTerminalType is 'virtual', the internet address of the connected system.  If ccmHistoryEventCommandSource is 'snmp', the internet address of the requester.  The value of all bit's is zero  if not available or not applicable.  The Format of this address depends on the value of the ccmHistoryEventCommandSourceAddrType object.  This object deprecates ccmHistoryEventCommandSourceAddress
            	**type**\: str
            
            	**range:** 0..255
            
            .. attribute:: ccmhistoryeventcommandsourceaddrtype
            
            	This object indicates the transport type of the address contained in ccmHistoryEventCommandSourceAddrRev1.  The value will be zero if not available or not applicable
            	**type**\: :py:class:`InetAddressType_Enum <ydk.models.inet.INET_ADDRESS_MIB.InetAddressType_Enum>`
            
            .. attribute:: ccmhistoryeventconfigdestination
            
            	The configuration data destination for the event
            	**type**\: :py:class:`HistoryEventMedium_Enum <ydk.models.config.CISCO_CONFIG_MAN_MIB.HistoryEventMedium_Enum>`
            
            .. attribute:: ccmhistoryeventconfigsource
            
            	The configuration data source for the event
            	**type**\: :py:class:`HistoryEventMedium_Enum <ydk.models.config.CISCO_CONFIG_MAN_MIB.HistoryEventMedium_Enum>`
            
            .. attribute:: ccmhistoryeventfile
            
            	If ccmHistoryEventConfigSource or ccmHistoryEventConfigDestination is 'networkTftp' or 'networkRcp', the configuration file name at the storage file server.  The length is zero if not available or not applicable
            	**type**\: str
            
            	**range:** 0..64
            
            .. attribute:: ccmhistoryeventrcpuser
            
            	If ccmHistoryEventConfigSource or ccmHistoryEventConfigDestination is 'networkRcp', the remote user name.  The length is zero if not applicable or not available
            	**type**\: str
            
            	**range:** 0..64
            
            .. attribute:: ccmhistoryeventserveraddress
            
            	If ccmHistoryEventConfigSource or ccmHistoryEventConfigDestination is 'networkTftp' or 'networkRcp', the internet address of the storage file server.  The value is 0.0.0.0 if not applicable or not         available.         This object is deprecated by         ccmHistoryEventServerAddrRev1
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: ccmhistoryeventserveraddrrev1
            
            	If ccmHistoryEventConfigSource or ccmHistoryEventConfigDestination is 'networkTftp' or 'networkRcp', the internet address of the storage file server.   The value of all bits is 0s if not applicable or not available.  The Format of this address depends on the value of the ccmHistoryEventServerAddrType object.  This object deprecates ccmHistoryEventServerAddress
            	**type**\: str
            
            	**range:** 0..255
            
            .. attribute:: ccmhistoryeventserveraddrtype
            
            	This object indicates the transport type of the address contained in ccmHistoryEventServerAddrRev1.  The value will be zero if not available or not aplicable
            	**type**\: :py:class:`InetAddressType_Enum <ydk.models.inet.INET_ADDRESS_MIB.InetAddressType_Enum>`
            
            .. attribute:: ccmhistoryeventterminallocation
            
            	If ccmHistoryEventCommandSource is 'commandLine', the hard\-wired location of the terminal or the remote  host for an incoming connection.  The length is zero  if not available or not applicable
            	**type**\: str
            
            	**range:** 0..64
            
            .. attribute:: ccmhistoryeventterminalnumber
            
            	If ccmHistoryEventCommandSource is 'commandLine', the terminal number.  The value is \-1 if not available or not applicable
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: ccmhistoryeventterminaltype
            
            	If ccmHistoryEventCommandSource is 'commandLine', the terminal type, otherwise 'notApplicable'
            	**type**\: :py:class:`CcmHistoryEventTerminalType_Enum <ydk.models.config.CISCO_CONFIG_MAN_MIB.CISCOCONFIGMANMIB.CcmHistoryEventTable.CcmHistoryEventEntry.CcmHistoryEventTerminalType_Enum>`
            
            .. attribute:: ccmhistoryeventterminaluser
            
            	If ccmHistoryEventCommandSource is 'commandLine', the name of the logged in user.  The length is zero if not available or not applicable
            	**type**\: str
            
            	**range:** 0..64
            
            .. attribute:: ccmhistoryeventtime
            
            	The value of sysUpTime when the event occurred
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ccmhistoryeventvirtualhostname
            
            	If ccmHistoryEventTerminalType is 'virtual', the host name of the connected system.  The length is zero if not available or not applicable
            	**type**\: str
            
            	**range:** 0..64
            
            

            """

            _prefix = 'cisco-config'
            _revision = '2007-04-27'

            def __init__(self):
                self.parent = None
                self.ccmhistoryeventindex = None
                self.ccmhistoryclicmdentriesbumped = None
                self.ccmhistoryeventcommandsource = None
                self.ccmhistoryeventcommandsourceaddress = None
                self.ccmhistoryeventcommandsourceaddrrev1 = None
                self.ccmhistoryeventcommandsourceaddrtype = None
                self.ccmhistoryeventconfigdestination = None
                self.ccmhistoryeventconfigsource = None
                self.ccmhistoryeventfile = None
                self.ccmhistoryeventrcpuser = None
                self.ccmhistoryeventserveraddress = None
                self.ccmhistoryeventserveraddrrev1 = None
                self.ccmhistoryeventserveraddrtype = None
                self.ccmhistoryeventterminallocation = None
                self.ccmhistoryeventterminalnumber = None
                self.ccmhistoryeventterminaltype = None
                self.ccmhistoryeventterminaluser = None
                self.ccmhistoryeventtime = None
                self.ccmhistoryeventvirtualhostname = None

            class CcmHistoryEventCommandSource_Enum(Enum):
                """
                CcmHistoryEventCommandSource_Enum

                The source of the command that instigated the event.

                """

                COMMANDLINE = 1

                SNMP = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.config._meta import _CISCO_CONFIG_MAN_MIB as meta
                    return meta._meta_table['CISCOCONFIGMANMIB.CcmHistoryEventTable.CcmHistoryEventEntry.CcmHistoryEventCommandSource_Enum']


            class CcmHistoryEventTerminalType_Enum(Enum):
                """
                CcmHistoryEventTerminalType_Enum

                If ccmHistoryEventCommandSource is 'commandLine',
                the terminal type, otherwise 'notApplicable'.

                """

                NOTAPPLICABLE = 1

                UNKNOWN = 2

                CONSOLE = 3

                TERMINAL = 4

                VIRTUAL = 5

                AUXILIARY = 6


                @staticmethod
                def _meta_info():
                    from ydk.models.config._meta import _CISCO_CONFIG_MAN_MIB as meta
                    return meta._meta_table['CISCOCONFIGMANMIB.CcmHistoryEventTable.CcmHistoryEventEntry.CcmHistoryEventTerminalType_Enum']


            @property
            def _common_path(self):
                if self.ccmhistoryeventindex is None:
                    raise YPYDataValidationError('Key property ccmhistoryeventindex is None')

                return '/CISCO-CONFIG-MAN-MIB:CISCO-CONFIG-MAN-MIB/CISCO-CONFIG-MAN-MIB:ccmHistoryEventTable/CISCO-CONFIG-MAN-MIB:ccmHistoryEventEntry[CISCO-CONFIG-MAN-MIB:ccmHistoryEventIndex = ' + str(self.ccmhistoryeventindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.ccmhistoryeventindex is not None:
                    return True

                if self.ccmhistoryclicmdentriesbumped is not None:
                    return True

                if self.ccmhistoryeventcommandsource is not None:
                    return True

                if self.ccmhistoryeventcommandsourceaddress is not None:
                    return True

                if self.ccmhistoryeventcommandsourceaddrrev1 is not None:
                    return True

                if self.ccmhistoryeventcommandsourceaddrtype is not None:
                    return True

                if self.ccmhistoryeventconfigdestination is not None:
                    return True

                if self.ccmhistoryeventconfigsource is not None:
                    return True

                if self.ccmhistoryeventfile is not None:
                    return True

                if self.ccmhistoryeventrcpuser is not None:
                    return True

                if self.ccmhistoryeventserveraddress is not None:
                    return True

                if self.ccmhistoryeventserveraddrrev1 is not None:
                    return True

                if self.ccmhistoryeventserveraddrtype is not None:
                    return True

                if self.ccmhistoryeventterminallocation is not None:
                    return True

                if self.ccmhistoryeventterminalnumber is not None:
                    return True

                if self.ccmhistoryeventterminaltype is not None:
                    return True

                if self.ccmhistoryeventterminaluser is not None:
                    return True

                if self.ccmhistoryeventtime is not None:
                    return True

                if self.ccmhistoryeventvirtualhostname is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.config._meta import _CISCO_CONFIG_MAN_MIB as meta
                return meta._meta_table['CISCOCONFIGMANMIB.CcmHistoryEventTable.CcmHistoryEventEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-CONFIG-MAN-MIB:CISCO-CONFIG-MAN-MIB/CISCO-CONFIG-MAN-MIB:ccmHistoryEventTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.ccmhistoryevententry is not None:
                for child_ref in self.ccmhistoryevententry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.config._meta import _CISCO_CONFIG_MAN_MIB as meta
            return meta._meta_table['CISCOCONFIGMANMIB.CcmHistoryEventTable']['meta_info']

    @property
    def _common_path(self):

        return '/CISCO-CONFIG-MAN-MIB:CISCO-CONFIG-MAN-MIB'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if not self.is_config():
            return False
        if self.is_presence():
            return True
        if self.ccmclicfg is not None and self.ccmclicfg._has_data():
            return True

        if self.ccmclicfg is not None and self.ccmclicfg.is_presence():
            return True

        if self.ccmclihistory is not None and self.ccmclihistory._has_data():
            return True

        if self.ccmclihistory is not None and self.ccmclihistory.is_presence():
            return True

        if self.ccmclihistorycommandtable is not None and self.ccmclihistorycommandtable._has_data():
            return True

        if self.ccmclihistorycommandtable is not None and self.ccmclihistorycommandtable.is_presence():
            return True

        if self.ccmctidobjects is not None and self.ccmctidobjects._has_data():
            return True

        if self.ccmctidobjects is not None and self.ccmctidobjects.is_presence():
            return True

        if self.ccmhistory is not None and self.ccmhistory._has_data():
            return True

        if self.ccmhistory is not None and self.ccmhistory.is_presence():
            return True

        if self.ccmhistoryeventtable is not None and self.ccmhistoryeventtable._has_data():
            return True

        if self.ccmhistoryeventtable is not None and self.ccmhistoryeventtable.is_presence():
            return True

        return False

    def is_presence(self):
        ''' Returns True if this instance represents presence container else returns False '''
        return False

    @staticmethod
    def _meta_info():
        from ydk.models.config._meta import _CISCO_CONFIG_MAN_MIB as meta
        return meta._meta_table['CISCOCONFIGMANMIB']['meta_info']


