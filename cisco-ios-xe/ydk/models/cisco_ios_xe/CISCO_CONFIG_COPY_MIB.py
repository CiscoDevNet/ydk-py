""" CISCO_CONFIG_COPY_MIB 

This MIB facilitates writing of configuration files
of an SNMP Agent running Cisco's IOS in the 
following ways\: to and from the net, copying running 
configurations to startup configurations and 
vice\-versa, and copying a configuration
(running or startup) to and from the local 
IOS file system.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class ConfigCopyFailCause(Enum):
    """
    ConfigCopyFailCause (Enum Class)

    The reason a config\-copy request failed.

    unknown\:        very descriptive.

    badFileName\:    check your file 

                    name/path/permissions.

    timeout\:        the network may be overloaded, 

                    or the remote file server may not

                    be responding.

    noMem\:          the Agent wasn't able to allocate 

                    memory for the config\-copy 

                    operation.

    noConfig\:       the agent\-config selected as the 

                    source was non\-existent.

    unsupportedProtocol\:    the protocol is not 

                            supported by the agent.

    someConfigApplyFailed\:  applying of some of the 

                            configuration commands 

                            failed.

    systemNotReady\: system is not ready to copy.

    requestAborted\: config copy operation aborted.

    .. data:: unknown = 1

    .. data:: badFileName = 2

    .. data:: timeout = 3

    .. data:: noMem = 4

    .. data:: noConfig = 5

    .. data:: unsupportedProtocol = 6

    .. data:: someConfigApplyFailed = 7

    .. data:: systemNotReady = 8

    .. data:: requestAborted = 9

    """

    unknown = Enum.YLeaf(1, "unknown")

    badFileName = Enum.YLeaf(2, "badFileName")

    timeout = Enum.YLeaf(3, "timeout")

    noMem = Enum.YLeaf(4, "noMem")

    noConfig = Enum.YLeaf(5, "noConfig")

    unsupportedProtocol = Enum.YLeaf(6, "unsupportedProtocol")

    someConfigApplyFailed = Enum.YLeaf(7, "someConfigApplyFailed")

    systemNotReady = Enum.YLeaf(8, "systemNotReady")

    requestAborted = Enum.YLeaf(9, "requestAborted")


class ConfigCopyProtocol(Enum):
    """
    ConfigCopyProtocol (Enum Class)

    The protocol file transfer protocol that should be

    used to copy the configuration file over the 

    network. If the config file transfer is to occur 

    locally on the SNMP agent, the method of transfer 

    is left up to the implementation, and is not 

    restricted to the protocols below.

    tftp\:   Transfer File Transfer Protocol 

    ftp\:    File Transfer protocol

    rcp\:    Remote Copy Protocol

    scp\:    Secure Copy Protocol

    sftp\:   Secure File Transfer Protocol

    .. data:: tftp = 1

    .. data:: ftp = 2

    .. data:: rcp = 3

    .. data:: scp = 4

    .. data:: sftp = 5

    """

    tftp = Enum.YLeaf(1, "tftp")

    ftp = Enum.YLeaf(2, "ftp")

    rcp = Enum.YLeaf(3, "rcp")

    scp = Enum.YLeaf(4, "scp")

    sftp = Enum.YLeaf(5, "sftp")


class ConfigCopyState(Enum):
    """
    ConfigCopyState (Enum Class)

    The state of a TFTP config\-copy operation.

    The description of each state is given below\:

    waiting\:     only one config\-copy request can run 

                 at any time. A newly activated 

                 config\-copy request is placed in this 

                 state if another request has already 

                 been activated.

    running\:     this state signifies that the 

                 config\-copy request is running.

    successful\:  the state when a config\-copy request 

                 is successfully completed.

    failed\:      the config\-copy request was 

                 unsuccessful.

    .. data:: waiting = 1

    .. data:: running = 2

    .. data:: successful = 3

    .. data:: failed = 4

    """

    waiting = Enum.YLeaf(1, "waiting")

    running = Enum.YLeaf(2, "running")

    successful = Enum.YLeaf(3, "successful")

    failed = Enum.YLeaf(4, "failed")


class ConfigFileType(Enum):
    """
    ConfigFileType (Enum Class)

    The various types of files on which a config\-copy

    operation can be performed.

    networkFile\:       file on another network device, 

                       e.g. a file\-server on the 

                       network.

    iosFile\:           a file on the local agent, other

                       than startup or running config.

    startupConfig\:     a startup config file.

    runningConfig\:     a running config file.

    terminal\:          a terminal (e.g. the console 

                       window) on which the config is 

                       to be displayed.

    fabricStartupConfig\:   a file type which can be

                           used for a destination file;

                           when a running\-config is to

                           copied to a destination of

                           this type, the file is copied

                           to the startup config on all

                           devices in the fabric. Such

                           a fabric could, for example,

                           be a Fibre Channel fabric,

                           or even a MAC\-based fabric.

    .. data:: networkFile = 1

    .. data:: iosFile = 2

    .. data:: startupConfig = 3

    .. data:: runningConfig = 4

    .. data:: terminal = 5

    .. data:: fabricStartupConfig = 6

    """

    networkFile = Enum.YLeaf(1, "networkFile")

    iosFile = Enum.YLeaf(2, "iosFile")

    startupConfig = Enum.YLeaf(3, "startupConfig")

    runningConfig = Enum.YLeaf(4, "runningConfig")

    terminal = Enum.YLeaf(5, "terminal")

    fabricStartupConfig = Enum.YLeaf(6, "fabricStartupConfig")



class CISCOCONFIGCOPYMIB(Entity):
    """
    
    
    .. attribute:: cccopytable
    
    	A table of config\-copy requests
    	**type**\:  :py:class:`Cccopytable <ydk.models.cisco_ios_xe.CISCO_CONFIG_COPY_MIB.CISCOCONFIGCOPYMIB.Cccopytable>`
    
    .. attribute:: cccopyerrortable
    
    	A table containing information about the failure cause of the config copy operation. An entry is created only when the value of ccCopyState changes to 'failed' for a config copy operation.  Not all combinations of ccCopySourceFileType and ccCopyDestFileType need to be supported.  For example, an implementation may choose to support only the following combination\: ccCopySourceFileType = 'runningConfig' ccCopyDestFileType = 'fabricStartupConfig'.   In the case where a fabric wide config copy  operation is being performed, for example by selecting ccCopyDestFileType value to be 'fabricStartupConfig', it is possible that the fabric could have more than one device. In such cases this table would have one entry for each device in the fabric. In this case even if the  operation succeeded in one device and failed in  another, the operation as such has failed, so the global state  represented by ccCopyState 'failed', but for the device on which it was success,  ccCopyErrorDescription would have the  distinguished value, 'success'.   Once the config copy operation completes and if an entry gets instantiated, the management station  should retrieve the values of the status objects of  interest. Once an entry in ccCopyTable is deleted by management station, all the corresponding entries with the same ccCopyIndex in this table are also  deleted.   In order to prevent old entries from clogging the  table, entries age out at the same time as the  corresponding entry with same ccCopyIndex in  ccCopyTable ages out
    	**type**\:  :py:class:`Cccopyerrortable <ydk.models.cisco_ios_xe.CISCO_CONFIG_COPY_MIB.CISCOCONFIGCOPYMIB.Cccopyerrortable>`
    
    

    """

    _prefix = 'CISCO-CONFIG-COPY-MIB'
    _revision = '2005-04-06'

    def __init__(self):
        super(CISCOCONFIGCOPYMIB, self).__init__()
        self._top_entity = None

        self.yang_name = "CISCO-CONFIG-COPY-MIB"
        self.yang_parent_name = "CISCO-CONFIG-COPY-MIB"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([("ccCopyTable", ("cccopytable", CISCOCONFIGCOPYMIB.Cccopytable)), ("ccCopyErrorTable", ("cccopyerrortable", CISCOCONFIGCOPYMIB.Cccopyerrortable))])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.cccopytable = CISCOCONFIGCOPYMIB.Cccopytable()
        self.cccopytable.parent = self
        self._children_name_map["cccopytable"] = "ccCopyTable"
        self._children_yang_names.add("ccCopyTable")

        self.cccopyerrortable = CISCOCONFIGCOPYMIB.Cccopyerrortable()
        self.cccopyerrortable.parent = self
        self._children_name_map["cccopyerrortable"] = "ccCopyErrorTable"
        self._children_yang_names.add("ccCopyErrorTable")
        self._segment_path = lambda: "CISCO-CONFIG-COPY-MIB:CISCO-CONFIG-COPY-MIB"


    class Cccopytable(Entity):
        """
        A table of config\-copy requests.
        
        .. attribute:: cccopyentry
        
        	A config\-copy request.  A management station wishing to create an entry  should first generate a random serial number to be used as the index to this sparse table. The station  should then create the associated instance of the row status and row index objects.  It must also,  either in the same or in successive PDUs, create an instance of ccCopySourceFileType and  ccCopyDestFileType.  At least one of the file types defined in  ConfigFileType TC must be an agent\-config file type (i.e. 'startupConfig' or 'runningConfig'). If one of the file types is a 'networkFile', a valid ccCopyFileName and ccCopyServerAddressType and  ccCopyServerAddressRev1 or just ccCopyServerAddress must be created as well. If ccCopyServerAddress is created then ccCopyServerAddressRev1 will store the same IP address and ccCopyServerAddressType will  take the value 'ipv4'.  For a file type of 'iosFile', only a valid ccCopyFileName needs to be created as an  extra parameter.  It should also modify the default values for the  other configuration objects if the defaults are not appropriate.  Once the appropriate instance of all the  configuration objects have been created, either by an explicit SNMP set request or by default, the row  status should be set to active to initiate the  request. Note that this entire procedure may be  initiated via a single set request which specifies a row status of createAndGo as well as specifies valid values for the non\-defaulted  configuration objects.  Once the config\-copy request has been created  (i.e. the ccCopyEntryRowStatus has been made  active), the entry cannot be modified \- the only  operation possible after this is to delete the row.  Once the request completes, the management station  should retrieve the values of the status objects of  interest, and should then delete the entry.  In order to prevent old entries from clogging the  table, entries will be aged out, but an entry will  ever be deleted within 5 minutes of completing
        	**type**\: list of  		 :py:class:`Cccopyentry <ydk.models.cisco_ios_xe.CISCO_CONFIG_COPY_MIB.CISCOCONFIGCOPYMIB.Cccopytable.Cccopyentry>`
        
        

        """

        _prefix = 'CISCO-CONFIG-COPY-MIB'
        _revision = '2005-04-06'

        def __init__(self):
            super(CISCOCONFIGCOPYMIB.Cccopytable, self).__init__()

            self.yang_name = "ccCopyTable"
            self.yang_parent_name = "CISCO-CONFIG-COPY-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("ccCopyEntry", ("cccopyentry", CISCOCONFIGCOPYMIB.Cccopytable.Cccopyentry))])
            self._leafs = OrderedDict()

            self.cccopyentry = YList(self)
            self._segment_path = lambda: "ccCopyTable"
            self._absolute_path = lambda: "CISCO-CONFIG-COPY-MIB:CISCO-CONFIG-COPY-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOCONFIGCOPYMIB.Cccopytable, [], name, value)


        class Cccopyentry(Entity):
            """
            A config\-copy request.
            
            A management station wishing to create an entry 
            should first generate a random serial number to be
            used as the index to this sparse table. The station 
            should then create the associated instance of the
            row status and row index objects.  It must also, 
            either in the same or in successive PDUs, create an
            instance of ccCopySourceFileType and 
            ccCopyDestFileType.
            
            At least one of the file types defined in 
            ConfigFileType TC must be an agent\-config file type
            (i.e. 'startupConfig' or 'runningConfig').
            If one of the file types is a 'networkFile', a valid
            ccCopyFileName and ccCopyServerAddressType and 
            ccCopyServerAddressRev1 or just ccCopyServerAddress
            must be created as well. If ccCopyServerAddress is
            created then ccCopyServerAddressRev1 will store the
            same IP address and ccCopyServerAddressType will 
            take the value 'ipv4'.
            
            For a file type of 'iosFile', only
            a valid ccCopyFileName needs to be created as an 
            extra parameter.
            
            It should also modify the default values for the 
            other configuration objects if the defaults are not
            appropriate.
            
            Once the appropriate instance of all the 
            configuration objects have been created, either by
            an explicit SNMP set request or by default, the row 
            status should be set to active to initiate the 
            request. Note that this entire procedure may be 
            initiated via a single set request which specifies
            a row status of createAndGo as well as
            specifies valid values for the non\-defaulted 
            configuration objects.
            
            Once the config\-copy request has been created 
            (i.e. the ccCopyEntryRowStatus has been made 
            active), the entry cannot be modified \- the only 
            operation possible after this is to delete the row.
            
            Once the request completes, the management station 
            should retrieve the values of the status objects of 
            interest, and should then delete the entry.  In
            order to prevent old entries from clogging the 
            table, entries will be aged out, but an entry will 
            ever be deleted within 5 minutes of completing.
            
            .. attribute:: cccopyindex  (key)
            
            	Object which specifies a unique entry in the ccCopyTable.  A management station wishing to initiate a config\-copy operation should use a random value for this object when creating or modifying an instance of a ccCopyEntry. The RowStatus semantics of the ccCopyEntryRowStatus object will prevent access conflicts
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: cccopyprotocol
            
            	The protocol to be used for any copy.  If the copy operation occurs locally on the SNMP  agent (e.g. 'runningConfig' to 'startupConfig'), this object may be ignored by the implementation
            	**type**\:  :py:class:`ConfigCopyProtocol <ydk.models.cisco_ios_xe.CISCO_CONFIG_COPY_MIB.ConfigCopyProtocol>`
            
            .. attribute:: cccopysourcefiletype
            
            	Specifies the type of file to copy from. Either the ccCopySourceFileType or the ccCopyDestFileType  (or both) must be of type 'runningConfig' or  'startupConfig'. Also, the ccCopySourceFileType must be different from the ccCopyDestFileType.  If the ccCopySourceFileType has the value of  'networkFile', the ccCopyServerAddress/ ccCopyServerAddressRev1 and ccCopyServerAddressType and ccCopyFileName must also be created, and 3  objects together (ccCopySourceFileType, ccCopyServerAddressRev1, ccCopyFileName) will  uniquely identify the source file. If  ccCopyServerAddress is created then  ccCopyServerAddressRev1 will store the same IP address and ccCopyServerAddressType will  take the value 'ipv4'.   If the ccCopySourceFileType is 'iosFile', the  ccCopyFileName must also be created, and the  2 objects together (ccCopySourceFileType, ccCopyFileName) will uniquely identify the source  file
            	**type**\:  :py:class:`ConfigFileType <ydk.models.cisco_ios_xe.CISCO_CONFIG_COPY_MIB.ConfigFileType>`
            
            .. attribute:: cccopydestfiletype
            
            	specifies the type of file to copy to. Either the ccCopySourceFileType or the ccCopyDestFileType  (or both) must be of type 'runningConfig' or  'startupConfig'. Also, the ccCopySourceFileType  must be different from the ccCopyDestFileType.  If the ccCopyDestFileType has the value of  'networkFile', the  ccCopyServerAddress/ccCopyServerAddressType and ccCopyServerAddressRev1 and ccCopyFileName must also be created, and 3 objects together (ccCopyDestFileType, ccCopyServerAddressRev1,   ccCopyFileName) will uniquely identify the  destination file. If ccCopyServerAddress is created then ccCopyServerAddressRev1 will store the same IP address and ccCopyServerAddressType will take the  value 'ipv4'.   If the ccCopyDestFileType is 'iosFile', the  ccCopyFileName must also be created, and the 2 objects together (ccCopyDestFileType,  ccCopyFileName) will uniquely identify the  destination file
            	**type**\:  :py:class:`ConfigFileType <ydk.models.cisco_ios_xe.CISCO_CONFIG_COPY_MIB.ConfigFileType>`
            
            .. attribute:: cccopyserveraddress
            
            	The IP address of the TFTP server from (or to) which to copy the configuration file. This object  must be created when either the  ccCopySourceFileType or ccCopyDestFileType has the value 'networkFile'.  Values of 0.0.0.0 or FF.FF.FF.FF for ccCopyServerAddress are not allowed.  Since this object can just hold only IPv4 Transport type, it is deprecated and replaced by  ccCopyServerAddressRev1
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**status**\: deprecated
            
            .. attribute:: cccopyfilename
            
            	The file name (including the path, if applicable) of the file. This object must be created when either the ccCopySourceFileType or ccCopyDestFileType has the value 'networkFile' or 'iosFile'
            	**type**\: str
            
            .. attribute:: cccopyusername
            
            	Remote username for copy via FTP, RCP, SFTP or SCP protocol. This object must be created when the ccCopyProtocol is 'rcp', 'scp', 'ftp', or 'sftp'. If the protocol is RCP, it will override the remote  username configured through the          rcmd remote\-username <username> configuration command.  The remote username is sent as the server username  in an RCP command request sent by the system to a remote RCP server
            	**type**\: str
            
            	**length:** 1..40
            
            .. attribute:: cccopyuserpassword
            
            	Password used by FTP, SFTP or SCP for copying a file to/from an FTP/SFTP/SCP server. This object  must be created when the ccCopyProtocol is FTP or SCP.  Reading it returns a zero\-length string for security  reasons
            	**type**\: str
            
            	**length:** 1..40
            
            .. attribute:: cccopynotificationoncompletion
            
            	Specifies whether or not a ccCopyCompletion notification should be issued on completion of the TFTP transfer. If such a notification is desired,  it is the responsibility of the management entity to ensure that the SNMP administrative model is  configured in such a way as to allow the  notification to be delivered
            	**type**\: bool
            
            .. attribute:: cccopystate
            
            	Specifies the state of this config\-copy request. This value of this object is instantiated only after  the row has been instantiated, i.e. after the  ccCopyEntryRowStatus has been made active
            	**type**\:  :py:class:`ConfigCopyState <ydk.models.cisco_ios_xe.CISCO_CONFIG_COPY_MIB.ConfigCopyState>`
            
            .. attribute:: cccopytimestarted
            
            	Specifies the time the ccCopyState last transitioned to 'running', or 0 if the state has  never transitioned to 'running'(e.g., stuck in 'waiting' state).  This object is instantiated only after the row has  been instantiated
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cccopytimecompleted
            
            	Specifies the time the ccCopyState last transitioned from 'running' to 'successful' or  'failed' states. This object is instantiated only  after the row has been instantiated. Its value will remain 0 until the request has  completed
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cccopyfailcause
            
            	The reason why the config\-copy operation failed. This object is instantiated only when the  ccCopyState for this entry is in the  'failed' state
            	**type**\:  :py:class:`ConfigCopyFailCause <ydk.models.cisco_ios_xe.CISCO_CONFIG_COPY_MIB.ConfigCopyFailCause>`
            
            .. attribute:: cccopyentryrowstatus
            
            	The status of this table entry. Once the entry status is set to active, the associated entry cannot  be modified until the request completes  (ccCopyState transitions to 'successful' or 'failed' state)
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            .. attribute:: cccopyserveraddresstype
            
            	This object indicates the transport type of the address contained in ccCopyServerAddressRev1 object.  This must be created when either the ccCopySourceFileType or ccCopyDestFileType has the value 'networkFile'
            	**type**\:  :py:class:`InetAddressType <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetAddressType>`
            
            .. attribute:: cccopyserveraddressrev1
            
            	The IP address of the TFTP server from (or to) which to copy the configuration file. This object must be created when either the  ccCopySourceFileType or ccCopyDestFileType has the value 'networkFile'.    All bits as 0s or 1s for ccCopyServerAddressRev1 are not allowed.  The format of this address depends on the value of  the ccCopyServerAddressType object
            	**type**\: str
            
            	**length:** 0..255
            
            

            """

            _prefix = 'CISCO-CONFIG-COPY-MIB'
            _revision = '2005-04-06'

            def __init__(self):
                super(CISCOCONFIGCOPYMIB.Cccopytable.Cccopyentry, self).__init__()

                self.yang_name = "ccCopyEntry"
                self.yang_parent_name = "ccCopyTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['cccopyindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cccopyindex', YLeaf(YType.uint32, 'ccCopyIndex')),
                    ('cccopyprotocol', YLeaf(YType.enumeration, 'ccCopyProtocol')),
                    ('cccopysourcefiletype', YLeaf(YType.enumeration, 'ccCopySourceFileType')),
                    ('cccopydestfiletype', YLeaf(YType.enumeration, 'ccCopyDestFileType')),
                    ('cccopyserveraddress', YLeaf(YType.str, 'ccCopyServerAddress')),
                    ('cccopyfilename', YLeaf(YType.str, 'ccCopyFileName')),
                    ('cccopyusername', YLeaf(YType.str, 'ccCopyUserName')),
                    ('cccopyuserpassword', YLeaf(YType.str, 'ccCopyUserPassword')),
                    ('cccopynotificationoncompletion', YLeaf(YType.boolean, 'ccCopyNotificationOnCompletion')),
                    ('cccopystate', YLeaf(YType.enumeration, 'ccCopyState')),
                    ('cccopytimestarted', YLeaf(YType.uint32, 'ccCopyTimeStarted')),
                    ('cccopytimecompleted', YLeaf(YType.uint32, 'ccCopyTimeCompleted')),
                    ('cccopyfailcause', YLeaf(YType.enumeration, 'ccCopyFailCause')),
                    ('cccopyentryrowstatus', YLeaf(YType.enumeration, 'ccCopyEntryRowStatus')),
                    ('cccopyserveraddresstype', YLeaf(YType.enumeration, 'ccCopyServerAddressType')),
                    ('cccopyserveraddressrev1', YLeaf(YType.str, 'ccCopyServerAddressRev1')),
                ])
                self.cccopyindex = None
                self.cccopyprotocol = None
                self.cccopysourcefiletype = None
                self.cccopydestfiletype = None
                self.cccopyserveraddress = None
                self.cccopyfilename = None
                self.cccopyusername = None
                self.cccopyuserpassword = None
                self.cccopynotificationoncompletion = None
                self.cccopystate = None
                self.cccopytimestarted = None
                self.cccopytimecompleted = None
                self.cccopyfailcause = None
                self.cccopyentryrowstatus = None
                self.cccopyserveraddresstype = None
                self.cccopyserveraddressrev1 = None
                self._segment_path = lambda: "ccCopyEntry" + "[ccCopyIndex='" + str(self.cccopyindex) + "']"
                self._absolute_path = lambda: "CISCO-CONFIG-COPY-MIB:CISCO-CONFIG-COPY-MIB/ccCopyTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOCONFIGCOPYMIB.Cccopytable.Cccopyentry, ['cccopyindex', 'cccopyprotocol', 'cccopysourcefiletype', 'cccopydestfiletype', 'cccopyserveraddress', 'cccopyfilename', 'cccopyusername', 'cccopyuserpassword', 'cccopynotificationoncompletion', 'cccopystate', 'cccopytimestarted', 'cccopytimecompleted', 'cccopyfailcause', 'cccopyentryrowstatus', 'cccopyserveraddresstype', 'cccopyserveraddressrev1'], name, value)


    class Cccopyerrortable(Entity):
        """
        A table containing information about the failure
        cause of the config copy operation. An entry is
        created only when the value of ccCopyState changes
        to 'failed' for a config copy operation.
        
        Not all combinations of ccCopySourceFileType and
        ccCopyDestFileType need to be supported.  For
        example, an implementation may choose to support
        only the following combination\:
        ccCopySourceFileType = 'runningConfig'
        ccCopyDestFileType = 'fabricStartupConfig'. 
        
        In the case where a fabric wide config copy 
        operation is being performed, for example by
        selecting ccCopyDestFileType value to be
        'fabricStartupConfig', it is possible that the
        fabric could have more than one device. In such
        cases this table would have one entry for each
        device in the fabric. In this case even if the 
        operation succeeded in one device and failed in 
        another, the operation as such has failed, so the
        global state  represented by ccCopyState 'failed',
        but for the device on which it was success, 
        ccCopyErrorDescription would have the 
        distinguished value, 'success'. 
        
        Once the config copy operation completes and if an
        entry gets instantiated, the management station 
        should retrieve the values of the status objects of 
        interest. Once an entry in ccCopyTable is deleted
        by management station, all the corresponding entries
        with the same ccCopyIndex in this table are also 
        deleted. 
        
        In order to prevent old entries from clogging the 
        table, entries age out at the same time as the 
        corresponding entry with same ccCopyIndex in 
        ccCopyTable ages out.
        
        .. attribute:: cccopyerrorentry
        
        	An entry containing information about the outcome at one destination of a failed config copy operation
        	**type**\: list of  		 :py:class:`Cccopyerrorentry <ydk.models.cisco_ios_xe.CISCO_CONFIG_COPY_MIB.CISCOCONFIGCOPYMIB.Cccopyerrortable.Cccopyerrorentry>`
        
        

        """

        _prefix = 'CISCO-CONFIG-COPY-MIB'
        _revision = '2005-04-06'

        def __init__(self):
            super(CISCOCONFIGCOPYMIB.Cccopyerrortable, self).__init__()

            self.yang_name = "ccCopyErrorTable"
            self.yang_parent_name = "CISCO-CONFIG-COPY-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("ccCopyErrorEntry", ("cccopyerrorentry", CISCOCONFIGCOPYMIB.Cccopyerrortable.Cccopyerrorentry))])
            self._leafs = OrderedDict()

            self.cccopyerrorentry = YList(self)
            self._segment_path = lambda: "ccCopyErrorTable"
            self._absolute_path = lambda: "CISCO-CONFIG-COPY-MIB:CISCO-CONFIG-COPY-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOCONFIGCOPYMIB.Cccopyerrortable, [], name, value)


        class Cccopyerrorentry(Entity):
            """
            An entry containing information about the
            outcome at one destination of a failed config
            copy operation.
            
            .. attribute:: cccopyindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`cccopyindex <ydk.models.cisco_ios_xe.CISCO_CONFIG_COPY_MIB.CISCOCONFIGCOPYMIB.Cccopytable.Cccopyentry>`
            
            .. attribute:: cccopyerrorindex  (key)
            
            	A monotonically increasing integer for the sole purpose of indexing entries in this table. When a config copy operation has multiple  destinations, then this index value is used to  distinguish between those multiple destinations
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cccopyerrordeviceipaddresstype
            
            	The type of Internet address for this destination device on which config copy operation is performed
            	**type**\:  :py:class:`InetAddressType <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetAddressType>`
            
            .. attribute:: cccopyerrordeviceipaddress
            
            	The IP address of this destination device on which config copy operation is performed. The object value has to be consistent with the type specified in ccCopyErrorDeviceIpAddressType
            	**type**\: str
            
            	**length:** 0..255
            
            .. attribute:: cccopyerrordevicewwn
            
            	The World Wide Name (WWN) of this destination device on which config copy operation is performed. The value of this object is zero\-length string if  WWN is unassigned or unknown. For example, devices  which do not support fibre channel would not have WWN
            	**type**\: str
            
            	**length:** 0 \| 8 \| 16
            
            .. attribute:: cccopyerrordescription
            
            	The error description for the error happened for this destination of this config copy  operation
            	**type**\: str
            
            

            """

            _prefix = 'CISCO-CONFIG-COPY-MIB'
            _revision = '2005-04-06'

            def __init__(self):
                super(CISCOCONFIGCOPYMIB.Cccopyerrortable.Cccopyerrorentry, self).__init__()

                self.yang_name = "ccCopyErrorEntry"
                self.yang_parent_name = "ccCopyErrorTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['cccopyindex','cccopyerrorindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cccopyindex', YLeaf(YType.str, 'ccCopyIndex')),
                    ('cccopyerrorindex', YLeaf(YType.uint32, 'ccCopyErrorIndex')),
                    ('cccopyerrordeviceipaddresstype', YLeaf(YType.enumeration, 'ccCopyErrorDeviceIpAddressType')),
                    ('cccopyerrordeviceipaddress', YLeaf(YType.str, 'ccCopyErrorDeviceIpAddress')),
                    ('cccopyerrordevicewwn', YLeaf(YType.str, 'ccCopyErrorDeviceWWN')),
                    ('cccopyerrordescription', YLeaf(YType.str, 'ccCopyErrorDescription')),
                ])
                self.cccopyindex = None
                self.cccopyerrorindex = None
                self.cccopyerrordeviceipaddresstype = None
                self.cccopyerrordeviceipaddress = None
                self.cccopyerrordevicewwn = None
                self.cccopyerrordescription = None
                self._segment_path = lambda: "ccCopyErrorEntry" + "[ccCopyIndex='" + str(self.cccopyindex) + "']" + "[ccCopyErrorIndex='" + str(self.cccopyerrorindex) + "']"
                self._absolute_path = lambda: "CISCO-CONFIG-COPY-MIB:CISCO-CONFIG-COPY-MIB/ccCopyErrorTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOCONFIGCOPYMIB.Cccopyerrortable.Cccopyerrorentry, ['cccopyindex', 'cccopyerrorindex', 'cccopyerrordeviceipaddresstype', 'cccopyerrordeviceipaddress', 'cccopyerrordevicewwn', 'cccopyerrordescription'], name, value)

    def clone_ptr(self):
        self._top_entity = CISCOCONFIGCOPYMIB()
        return self._top_entity

