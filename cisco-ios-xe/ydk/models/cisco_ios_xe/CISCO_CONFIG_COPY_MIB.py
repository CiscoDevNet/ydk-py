""" CISCO_CONFIG_COPY_MIB 

This MIB facilitates writing of configuration files
of an SNMP Agent running Cisco's IOS in the 
following ways\: to and from the net, copying running 
configurations to startup configurations and 
vice\-versa, and copying a configuration
(running or startup) to and from the local 
IOS file system.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class Configcopyfailcause(Enum):
    """
    Configcopyfailcause

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


class Configcopyprotocol(Enum):
    """
    Configcopyprotocol

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


class Configcopystate(Enum):
    """
    Configcopystate

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


class Configfiletype(Enum):
    """
    Configfiletype

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



class CiscoConfigCopyMib(Entity):
    """
    
    
    .. attribute:: cccopyerrortable
    
    	A table containing information about the failure cause of the config copy operation. An entry is created only when the value of ccCopyState changes to 'failed' for a config copy operation.  Not all combinations of ccCopySourceFileType and ccCopyDestFileType need to be supported.  For example, an implementation may choose to support only the following combination\: ccCopySourceFileType = 'runningConfig' ccCopyDestFileType = 'fabricStartupConfig'.   In the case where a fabric wide config copy  operation is being performed, for example by selecting ccCopyDestFileType value to be 'fabricStartupConfig', it is possible that the fabric could have more than one device. In such cases this table would have one entry for each device in the fabric. In this case even if the  operation succeeded in one device and failed in  another, the operation as such has failed, so the global state  represented by ccCopyState 'failed', but for the device on which it was success,  ccCopyErrorDescription would have the  distinguished value, 'success'.   Once the config copy operation completes and if an entry gets instantiated, the management station  should retrieve the values of the status objects of  interest. Once an entry in ccCopyTable is deleted by management station, all the corresponding entries with the same ccCopyIndex in this table are also  deleted.   In order to prevent old entries from clogging the  table, entries age out at the same time as the  corresponding entry with same ccCopyIndex in  ccCopyTable ages out
    	**type**\:   :py:class:`Cccopyerrortable <ydk.models.cisco_ios_xe.CISCO_CONFIG_COPY_MIB.CiscoConfigCopyMib.Cccopyerrortable>`
    
    .. attribute:: cccopytable
    
    	A table of config\-copy requests
    	**type**\:   :py:class:`Cccopytable <ydk.models.cisco_ios_xe.CISCO_CONFIG_COPY_MIB.CiscoConfigCopyMib.Cccopytable>`
    
    

    """

    _prefix = 'CISCO-CONFIG-COPY-MIB'
    _revision = '2005-04-06'

    def __init__(self):
        super(CiscoConfigCopyMib, self).__init__()
        self._top_entity = None

        self.yang_name = "CISCO-CONFIG-COPY-MIB"
        self.yang_parent_name = "CISCO-CONFIG-COPY-MIB"

        self.cccopyerrortable = CiscoConfigCopyMib.Cccopyerrortable()
        self.cccopyerrortable.parent = self
        self._children_name_map["cccopyerrortable"] = "ccCopyErrorTable"
        self._children_yang_names.add("ccCopyErrorTable")

        self.cccopytable = CiscoConfigCopyMib.Cccopytable()
        self.cccopytable.parent = self
        self._children_name_map["cccopytable"] = "ccCopyTable"
        self._children_yang_names.add("ccCopyTable")


    class Cccopytable(Entity):
        """
        A table of config\-copy requests.
        
        .. attribute:: cccopyentry
        
        	A config\-copy request.  A management station wishing to create an entry  should first generate a random serial number to be used as the index to this sparse table. The station  should then create the associated instance of the row status and row index objects.  It must also,  either in the same or in successive PDUs, create an instance of ccCopySourceFileType and  ccCopyDestFileType.  At least one of the file types defined in  ConfigFileType TC must be an agent\-config file type (i.e. 'startupConfig' or 'runningConfig'). If one of the file types is a 'networkFile', a valid ccCopyFileName and ccCopyServerAddressType and  ccCopyServerAddressRev1 or just ccCopyServerAddress must be created as well. If ccCopyServerAddress is created then ccCopyServerAddressRev1 will store the same IP address and ccCopyServerAddressType will  take the value 'ipv4'.  For a file type of 'iosFile', only a valid ccCopyFileName needs to be created as an  extra parameter.  It should also modify the default values for the  other configuration objects if the defaults are not appropriate.  Once the appropriate instance of all the  configuration objects have been created, either by an explicit SNMP set request or by default, the row  status should be set to active to initiate the  request. Note that this entire procedure may be  initiated via a single set request which specifies a row status of createAndGo as well as specifies valid values for the non\-defaulted  configuration objects.  Once the config\-copy request has been created  (i.e. the ccCopyEntryRowStatus has been made  active), the entry cannot be modified \- the only  operation possible after this is to delete the row.  Once the request completes, the management station  should retrieve the values of the status objects of  interest, and should then delete the entry.  In order to prevent old entries from clogging the  table, entries will be aged out, but an entry will  ever be deleted within 5 minutes of completing
        	**type**\: list of    :py:class:`Cccopyentry <ydk.models.cisco_ios_xe.CISCO_CONFIG_COPY_MIB.CiscoConfigCopyMib.Cccopytable.Cccopyentry>`
        
        

        """

        _prefix = 'CISCO-CONFIG-COPY-MIB'
        _revision = '2005-04-06'

        def __init__(self):
            super(CiscoConfigCopyMib.Cccopytable, self).__init__()

            self.yang_name = "ccCopyTable"
            self.yang_parent_name = "CISCO-CONFIG-COPY-MIB"

            self.cccopyentry = YList(self)

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
                        super(CiscoConfigCopyMib.Cccopytable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoConfigCopyMib.Cccopytable, self).__setattr__(name, value)


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
            
            .. attribute:: cccopyindex  <key>
            
            	Object which specifies a unique entry in the ccCopyTable.  A management station wishing to initiate a config\-copy operation should use a random value for this object when creating or modifying an instance of a ccCopyEntry. The RowStatus semantics of the ccCopyEntryRowStatus object will prevent access conflicts
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            .. attribute:: cccopydestfiletype
            
            	specifies the type of file to copy to. Either the ccCopySourceFileType or the ccCopyDestFileType  (or both) must be of type 'runningConfig' or  'startupConfig'. Also, the ccCopySourceFileType  must be different from the ccCopyDestFileType.  If the ccCopyDestFileType has the value of  'networkFile', the  ccCopyServerAddress/ccCopyServerAddressType and ccCopyServerAddressRev1 and ccCopyFileName must also be created, and 3 objects together (ccCopyDestFileType, ccCopyServerAddressRev1,   ccCopyFileName) will uniquely identify the  destination file. If ccCopyServerAddress is created then ccCopyServerAddressRev1 will store the same IP address and ccCopyServerAddressType will take the  value 'ipv4'.   If the ccCopyDestFileType is 'iosFile', the  ccCopyFileName must also be created, and the 2 objects together (ccCopyDestFileType,  ccCopyFileName) will uniquely identify the  destination file
            	**type**\:   :py:class:`Configfiletype <ydk.models.cisco_ios_xe.CISCO_CONFIG_COPY_MIB.Configfiletype>`
            
            .. attribute:: cccopyentryrowstatus
            
            	The status of this table entry. Once the entry status is set to active, the associated entry cannot  be modified until the request completes  (ccCopyState transitions to 'successful' or 'failed' state)
            	**type**\:   :py:class:`Rowstatus <ydk.models.cisco_ios_xe.SNMPv2_TC.Rowstatus>`
            
            .. attribute:: cccopyfailcause
            
            	The reason why the config\-copy operation failed. This object is instantiated only when the  ccCopyState for this entry is in the  'failed' state
            	**type**\:   :py:class:`Configcopyfailcause <ydk.models.cisco_ios_xe.CISCO_CONFIG_COPY_MIB.Configcopyfailcause>`
            
            .. attribute:: cccopyfilename
            
            	The file name (including the path, if applicable) of the file. This object must be created when either the ccCopySourceFileType or ccCopyDestFileType has the value 'networkFile' or 'iosFile'
            	**type**\:  str
            
            .. attribute:: cccopynotificationoncompletion
            
            	Specifies whether or not a ccCopyCompletion notification should be issued on completion of the TFTP transfer. If such a notification is desired,  it is the responsibility of the management entity to ensure that the SNMP administrative model is  configured in such a way as to allow the  notification to be delivered
            	**type**\:  bool
            
            .. attribute:: cccopyprotocol
            
            	The protocol to be used for any copy.  If the copy operation occurs locally on the SNMP  agent (e.g. 'runningConfig' to 'startupConfig'), this object may be ignored by the implementation
            	**type**\:   :py:class:`Configcopyprotocol <ydk.models.cisco_ios_xe.CISCO_CONFIG_COPY_MIB.Configcopyprotocol>`
            
            .. attribute:: cccopyserveraddress
            
            	The IP address of the TFTP server from (or to) which to copy the configuration file. This object  must be created when either the  ccCopySourceFileType or ccCopyDestFileType has the value 'networkFile'.  Values of 0.0.0.0 or FF.FF.FF.FF for ccCopyServerAddress are not allowed.  Since this object can just hold only IPv4 Transport type, it is deprecated and replaced by  ccCopyServerAddressRev1
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**status**\: deprecated
            
            .. attribute:: cccopyserveraddressrev1
            
            	The IP address of the TFTP server from (or to) which to copy the configuration file. This object must be created when either the  ccCopySourceFileType or ccCopyDestFileType has the value 'networkFile'.    All bits as 0s or 1s for ccCopyServerAddressRev1 are not allowed.  The format of this address depends on the value of  the ccCopyServerAddressType object
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: cccopyserveraddresstype
            
            	This object indicates the transport type of the address contained in ccCopyServerAddressRev1 object.  This must be created when either the ccCopySourceFileType or ccCopyDestFileType has the value 'networkFile'
            	**type**\:   :py:class:`Inetaddresstype <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.Inetaddresstype>`
            
            .. attribute:: cccopysourcefiletype
            
            	Specifies the type of file to copy from. Either the ccCopySourceFileType or the ccCopyDestFileType  (or both) must be of type 'runningConfig' or  'startupConfig'. Also, the ccCopySourceFileType must be different from the ccCopyDestFileType.  If the ccCopySourceFileType has the value of  'networkFile', the ccCopyServerAddress/ ccCopyServerAddressRev1 and ccCopyServerAddressType and ccCopyFileName must also be created, and 3  objects together (ccCopySourceFileType, ccCopyServerAddressRev1, ccCopyFileName) will  uniquely identify the source file. If  ccCopyServerAddress is created then  ccCopyServerAddressRev1 will store the same IP address and ccCopyServerAddressType will  take the value 'ipv4'.   If the ccCopySourceFileType is 'iosFile', the  ccCopyFileName must also be created, and the  2 objects together (ccCopySourceFileType, ccCopyFileName) will uniquely identify the source  file
            	**type**\:   :py:class:`Configfiletype <ydk.models.cisco_ios_xe.CISCO_CONFIG_COPY_MIB.Configfiletype>`
            
            .. attribute:: cccopystate
            
            	Specifies the state of this config\-copy request. This value of this object is instantiated only after  the row has been instantiated, i.e. after the  ccCopyEntryRowStatus has been made active
            	**type**\:   :py:class:`Configcopystate <ydk.models.cisco_ios_xe.CISCO_CONFIG_COPY_MIB.Configcopystate>`
            
            .. attribute:: cccopytimecompleted
            
            	Specifies the time the ccCopyState last transitioned from 'running' to 'successful' or  'failed' states. This object is instantiated only  after the row has been instantiated. Its value will remain 0 until the request has  completed
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cccopytimestarted
            
            	Specifies the time the ccCopyState last transitioned to 'running', or 0 if the state has  never transitioned to 'running'(e.g., stuck in 'waiting' state).  This object is instantiated only after the row has  been instantiated
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cccopyusername
            
            	Remote username for copy via FTP, RCP, SFTP or SCP protocol. This object must be created when the ccCopyProtocol is 'rcp', 'scp', 'ftp', or 'sftp'. If the protocol is RCP, it will override the remote  username configured through the          rcmd remote\-username <username> configuration command.  The remote username is sent as the server username  in an RCP command request sent by the system to a remote RCP server
            	**type**\:  str
            
            	**length:** 1..40
            
            .. attribute:: cccopyuserpassword
            
            	Password used by FTP, SFTP or SCP for copying a file to/from an FTP/SFTP/SCP server. This object  must be created when the ccCopyProtocol is FTP or SCP.  Reading it returns a zero\-length string for security  reasons
            	**type**\:  str
            
            	**length:** 1..40
            
            

            """

            _prefix = 'CISCO-CONFIG-COPY-MIB'
            _revision = '2005-04-06'

            def __init__(self):
                super(CiscoConfigCopyMib.Cccopytable.Cccopyentry, self).__init__()

                self.yang_name = "ccCopyEntry"
                self.yang_parent_name = "ccCopyTable"

                self.cccopyindex = YLeaf(YType.uint32, "ccCopyIndex")

                self.cccopydestfiletype = YLeaf(YType.enumeration, "ccCopyDestFileType")

                self.cccopyentryrowstatus = YLeaf(YType.enumeration, "ccCopyEntryRowStatus")

                self.cccopyfailcause = YLeaf(YType.enumeration, "ccCopyFailCause")

                self.cccopyfilename = YLeaf(YType.str, "ccCopyFileName")

                self.cccopynotificationoncompletion = YLeaf(YType.boolean, "ccCopyNotificationOnCompletion")

                self.cccopyprotocol = YLeaf(YType.enumeration, "ccCopyProtocol")

                self.cccopyserveraddress = YLeaf(YType.str, "ccCopyServerAddress")

                self.cccopyserveraddressrev1 = YLeaf(YType.str, "ccCopyServerAddressRev1")

                self.cccopyserveraddresstype = YLeaf(YType.enumeration, "ccCopyServerAddressType")

                self.cccopysourcefiletype = YLeaf(YType.enumeration, "ccCopySourceFileType")

                self.cccopystate = YLeaf(YType.enumeration, "ccCopyState")

                self.cccopytimecompleted = YLeaf(YType.uint32, "ccCopyTimeCompleted")

                self.cccopytimestarted = YLeaf(YType.uint32, "ccCopyTimeStarted")

                self.cccopyusername = YLeaf(YType.str, "ccCopyUserName")

                self.cccopyuserpassword = YLeaf(YType.str, "ccCopyUserPassword")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("cccopyindex",
                                "cccopydestfiletype",
                                "cccopyentryrowstatus",
                                "cccopyfailcause",
                                "cccopyfilename",
                                "cccopynotificationoncompletion",
                                "cccopyprotocol",
                                "cccopyserveraddress",
                                "cccopyserveraddressrev1",
                                "cccopyserveraddresstype",
                                "cccopysourcefiletype",
                                "cccopystate",
                                "cccopytimecompleted",
                                "cccopytimestarted",
                                "cccopyusername",
                                "cccopyuserpassword") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoConfigCopyMib.Cccopytable.Cccopyentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoConfigCopyMib.Cccopytable.Cccopyentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.cccopyindex.is_set or
                    self.cccopydestfiletype.is_set or
                    self.cccopyentryrowstatus.is_set or
                    self.cccopyfailcause.is_set or
                    self.cccopyfilename.is_set or
                    self.cccopynotificationoncompletion.is_set or
                    self.cccopyprotocol.is_set or
                    self.cccopyserveraddress.is_set or
                    self.cccopyserveraddressrev1.is_set or
                    self.cccopyserveraddresstype.is_set or
                    self.cccopysourcefiletype.is_set or
                    self.cccopystate.is_set or
                    self.cccopytimecompleted.is_set or
                    self.cccopytimestarted.is_set or
                    self.cccopyusername.is_set or
                    self.cccopyuserpassword.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.cccopyindex.yfilter != YFilter.not_set or
                    self.cccopydestfiletype.yfilter != YFilter.not_set or
                    self.cccopyentryrowstatus.yfilter != YFilter.not_set or
                    self.cccopyfailcause.yfilter != YFilter.not_set or
                    self.cccopyfilename.yfilter != YFilter.not_set or
                    self.cccopynotificationoncompletion.yfilter != YFilter.not_set or
                    self.cccopyprotocol.yfilter != YFilter.not_set or
                    self.cccopyserveraddress.yfilter != YFilter.not_set or
                    self.cccopyserveraddressrev1.yfilter != YFilter.not_set or
                    self.cccopyserveraddresstype.yfilter != YFilter.not_set or
                    self.cccopysourcefiletype.yfilter != YFilter.not_set or
                    self.cccopystate.yfilter != YFilter.not_set or
                    self.cccopytimecompleted.yfilter != YFilter.not_set or
                    self.cccopytimestarted.yfilter != YFilter.not_set or
                    self.cccopyusername.yfilter != YFilter.not_set or
                    self.cccopyuserpassword.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "ccCopyEntry" + "[ccCopyIndex='" + self.cccopyindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-CONFIG-COPY-MIB:CISCO-CONFIG-COPY-MIB/ccCopyTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.cccopyindex.is_set or self.cccopyindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cccopyindex.get_name_leafdata())
                if (self.cccopydestfiletype.is_set or self.cccopydestfiletype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cccopydestfiletype.get_name_leafdata())
                if (self.cccopyentryrowstatus.is_set or self.cccopyentryrowstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cccopyentryrowstatus.get_name_leafdata())
                if (self.cccopyfailcause.is_set or self.cccopyfailcause.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cccopyfailcause.get_name_leafdata())
                if (self.cccopyfilename.is_set or self.cccopyfilename.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cccopyfilename.get_name_leafdata())
                if (self.cccopynotificationoncompletion.is_set or self.cccopynotificationoncompletion.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cccopynotificationoncompletion.get_name_leafdata())
                if (self.cccopyprotocol.is_set or self.cccopyprotocol.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cccopyprotocol.get_name_leafdata())
                if (self.cccopyserveraddress.is_set or self.cccopyserveraddress.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cccopyserveraddress.get_name_leafdata())
                if (self.cccopyserveraddressrev1.is_set or self.cccopyserveraddressrev1.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cccopyserveraddressrev1.get_name_leafdata())
                if (self.cccopyserveraddresstype.is_set or self.cccopyserveraddresstype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cccopyserveraddresstype.get_name_leafdata())
                if (self.cccopysourcefiletype.is_set or self.cccopysourcefiletype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cccopysourcefiletype.get_name_leafdata())
                if (self.cccopystate.is_set or self.cccopystate.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cccopystate.get_name_leafdata())
                if (self.cccopytimecompleted.is_set or self.cccopytimecompleted.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cccopytimecompleted.get_name_leafdata())
                if (self.cccopytimestarted.is_set or self.cccopytimestarted.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cccopytimestarted.get_name_leafdata())
                if (self.cccopyusername.is_set or self.cccopyusername.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cccopyusername.get_name_leafdata())
                if (self.cccopyuserpassword.is_set or self.cccopyuserpassword.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cccopyuserpassword.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ccCopyIndex" or name == "ccCopyDestFileType" or name == "ccCopyEntryRowStatus" or name == "ccCopyFailCause" or name == "ccCopyFileName" or name == "ccCopyNotificationOnCompletion" or name == "ccCopyProtocol" or name == "ccCopyServerAddress" or name == "ccCopyServerAddressRev1" or name == "ccCopyServerAddressType" or name == "ccCopySourceFileType" or name == "ccCopyState" or name == "ccCopyTimeCompleted" or name == "ccCopyTimeStarted" or name == "ccCopyUserName" or name == "ccCopyUserPassword"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "ccCopyIndex"):
                    self.cccopyindex = value
                    self.cccopyindex.value_namespace = name_space
                    self.cccopyindex.value_namespace_prefix = name_space_prefix
                if(value_path == "ccCopyDestFileType"):
                    self.cccopydestfiletype = value
                    self.cccopydestfiletype.value_namespace = name_space
                    self.cccopydestfiletype.value_namespace_prefix = name_space_prefix
                if(value_path == "ccCopyEntryRowStatus"):
                    self.cccopyentryrowstatus = value
                    self.cccopyentryrowstatus.value_namespace = name_space
                    self.cccopyentryrowstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "ccCopyFailCause"):
                    self.cccopyfailcause = value
                    self.cccopyfailcause.value_namespace = name_space
                    self.cccopyfailcause.value_namespace_prefix = name_space_prefix
                if(value_path == "ccCopyFileName"):
                    self.cccopyfilename = value
                    self.cccopyfilename.value_namespace = name_space
                    self.cccopyfilename.value_namespace_prefix = name_space_prefix
                if(value_path == "ccCopyNotificationOnCompletion"):
                    self.cccopynotificationoncompletion = value
                    self.cccopynotificationoncompletion.value_namespace = name_space
                    self.cccopynotificationoncompletion.value_namespace_prefix = name_space_prefix
                if(value_path == "ccCopyProtocol"):
                    self.cccopyprotocol = value
                    self.cccopyprotocol.value_namespace = name_space
                    self.cccopyprotocol.value_namespace_prefix = name_space_prefix
                if(value_path == "ccCopyServerAddress"):
                    self.cccopyserveraddress = value
                    self.cccopyserveraddress.value_namespace = name_space
                    self.cccopyserveraddress.value_namespace_prefix = name_space_prefix
                if(value_path == "ccCopyServerAddressRev1"):
                    self.cccopyserveraddressrev1 = value
                    self.cccopyserveraddressrev1.value_namespace = name_space
                    self.cccopyserveraddressrev1.value_namespace_prefix = name_space_prefix
                if(value_path == "ccCopyServerAddressType"):
                    self.cccopyserveraddresstype = value
                    self.cccopyserveraddresstype.value_namespace = name_space
                    self.cccopyserveraddresstype.value_namespace_prefix = name_space_prefix
                if(value_path == "ccCopySourceFileType"):
                    self.cccopysourcefiletype = value
                    self.cccopysourcefiletype.value_namespace = name_space
                    self.cccopysourcefiletype.value_namespace_prefix = name_space_prefix
                if(value_path == "ccCopyState"):
                    self.cccopystate = value
                    self.cccopystate.value_namespace = name_space
                    self.cccopystate.value_namespace_prefix = name_space_prefix
                if(value_path == "ccCopyTimeCompleted"):
                    self.cccopytimecompleted = value
                    self.cccopytimecompleted.value_namespace = name_space
                    self.cccopytimecompleted.value_namespace_prefix = name_space_prefix
                if(value_path == "ccCopyTimeStarted"):
                    self.cccopytimestarted = value
                    self.cccopytimestarted.value_namespace = name_space
                    self.cccopytimestarted.value_namespace_prefix = name_space_prefix
                if(value_path == "ccCopyUserName"):
                    self.cccopyusername = value
                    self.cccopyusername.value_namespace = name_space
                    self.cccopyusername.value_namespace_prefix = name_space_prefix
                if(value_path == "ccCopyUserPassword"):
                    self.cccopyuserpassword = value
                    self.cccopyuserpassword.value_namespace = name_space
                    self.cccopyuserpassword.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cccopyentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cccopyentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "ccCopyTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-CONFIG-COPY-MIB:CISCO-CONFIG-COPY-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "ccCopyEntry"):
                for c in self.cccopyentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoConfigCopyMib.Cccopytable.Cccopyentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cccopyentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "ccCopyEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


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
        	**type**\: list of    :py:class:`Cccopyerrorentry <ydk.models.cisco_ios_xe.CISCO_CONFIG_COPY_MIB.CiscoConfigCopyMib.Cccopyerrortable.Cccopyerrorentry>`
        
        

        """

        _prefix = 'CISCO-CONFIG-COPY-MIB'
        _revision = '2005-04-06'

        def __init__(self):
            super(CiscoConfigCopyMib.Cccopyerrortable, self).__init__()

            self.yang_name = "ccCopyErrorTable"
            self.yang_parent_name = "CISCO-CONFIG-COPY-MIB"

            self.cccopyerrorentry = YList(self)

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
                        super(CiscoConfigCopyMib.Cccopyerrortable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoConfigCopyMib.Cccopyerrortable, self).__setattr__(name, value)


        class Cccopyerrorentry(Entity):
            """
            An entry containing information about the
            outcome at one destination of a failed config
            copy operation.
            
            .. attribute:: cccopyindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`cccopyindex <ydk.models.cisco_ios_xe.CISCO_CONFIG_COPY_MIB.CiscoConfigCopyMib.Cccopytable.Cccopyentry>`
            
            .. attribute:: cccopyerrorindex  <key>
            
            	A monotonically increasing integer for the sole purpose of indexing entries in this table. When a config copy operation has multiple  destinations, then this index value is used to  distinguish between those multiple destinations
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cccopyerrordescription
            
            	The error description for the error happened for this destination of this config copy  operation
            	**type**\:  str
            
            .. attribute:: cccopyerrordeviceipaddress
            
            	The IP address of this destination device on which config copy operation is performed. The object value has to be consistent with the type specified in ccCopyErrorDeviceIpAddressType
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: cccopyerrordeviceipaddresstype
            
            	The type of Internet address for this destination device on which config copy operation is performed
            	**type**\:   :py:class:`Inetaddresstype <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.Inetaddresstype>`
            
            .. attribute:: cccopyerrordevicewwn
            
            	The World Wide Name (WWN) of this destination device on which config copy operation is performed. The value of this object is zero\-length string if  WWN is unassigned or unknown. For example, devices  which do not support fibre channel would not have WWN
            	**type**\:  str
            
            	**length:** 0 \| 8 \| 16
            
            

            """

            _prefix = 'CISCO-CONFIG-COPY-MIB'
            _revision = '2005-04-06'

            def __init__(self):
                super(CiscoConfigCopyMib.Cccopyerrortable.Cccopyerrorentry, self).__init__()

                self.yang_name = "ccCopyErrorEntry"
                self.yang_parent_name = "ccCopyErrorTable"

                self.cccopyindex = YLeaf(YType.str, "ccCopyIndex")

                self.cccopyerrorindex = YLeaf(YType.uint32, "ccCopyErrorIndex")

                self.cccopyerrordescription = YLeaf(YType.str, "ccCopyErrorDescription")

                self.cccopyerrordeviceipaddress = YLeaf(YType.str, "ccCopyErrorDeviceIpAddress")

                self.cccopyerrordeviceipaddresstype = YLeaf(YType.enumeration, "ccCopyErrorDeviceIpAddressType")

                self.cccopyerrordevicewwn = YLeaf(YType.str, "ccCopyErrorDeviceWWN")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("cccopyindex",
                                "cccopyerrorindex",
                                "cccopyerrordescription",
                                "cccopyerrordeviceipaddress",
                                "cccopyerrordeviceipaddresstype",
                                "cccopyerrordevicewwn") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoConfigCopyMib.Cccopyerrortable.Cccopyerrorentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoConfigCopyMib.Cccopyerrortable.Cccopyerrorentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.cccopyindex.is_set or
                    self.cccopyerrorindex.is_set or
                    self.cccopyerrordescription.is_set or
                    self.cccopyerrordeviceipaddress.is_set or
                    self.cccopyerrordeviceipaddresstype.is_set or
                    self.cccopyerrordevicewwn.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.cccopyindex.yfilter != YFilter.not_set or
                    self.cccopyerrorindex.yfilter != YFilter.not_set or
                    self.cccopyerrordescription.yfilter != YFilter.not_set or
                    self.cccopyerrordeviceipaddress.yfilter != YFilter.not_set or
                    self.cccopyerrordeviceipaddresstype.yfilter != YFilter.not_set or
                    self.cccopyerrordevicewwn.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "ccCopyErrorEntry" + "[ccCopyIndex='" + self.cccopyindex.get() + "']" + "[ccCopyErrorIndex='" + self.cccopyerrorindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-CONFIG-COPY-MIB:CISCO-CONFIG-COPY-MIB/ccCopyErrorTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.cccopyindex.is_set or self.cccopyindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cccopyindex.get_name_leafdata())
                if (self.cccopyerrorindex.is_set or self.cccopyerrorindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cccopyerrorindex.get_name_leafdata())
                if (self.cccopyerrordescription.is_set or self.cccopyerrordescription.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cccopyerrordescription.get_name_leafdata())
                if (self.cccopyerrordeviceipaddress.is_set or self.cccopyerrordeviceipaddress.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cccopyerrordeviceipaddress.get_name_leafdata())
                if (self.cccopyerrordeviceipaddresstype.is_set or self.cccopyerrordeviceipaddresstype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cccopyerrordeviceipaddresstype.get_name_leafdata())
                if (self.cccopyerrordevicewwn.is_set or self.cccopyerrordevicewwn.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cccopyerrordevicewwn.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ccCopyIndex" or name == "ccCopyErrorIndex" or name == "ccCopyErrorDescription" or name == "ccCopyErrorDeviceIpAddress" or name == "ccCopyErrorDeviceIpAddressType" or name == "ccCopyErrorDeviceWWN"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "ccCopyIndex"):
                    self.cccopyindex = value
                    self.cccopyindex.value_namespace = name_space
                    self.cccopyindex.value_namespace_prefix = name_space_prefix
                if(value_path == "ccCopyErrorIndex"):
                    self.cccopyerrorindex = value
                    self.cccopyerrorindex.value_namespace = name_space
                    self.cccopyerrorindex.value_namespace_prefix = name_space_prefix
                if(value_path == "ccCopyErrorDescription"):
                    self.cccopyerrordescription = value
                    self.cccopyerrordescription.value_namespace = name_space
                    self.cccopyerrordescription.value_namespace_prefix = name_space_prefix
                if(value_path == "ccCopyErrorDeviceIpAddress"):
                    self.cccopyerrordeviceipaddress = value
                    self.cccopyerrordeviceipaddress.value_namespace = name_space
                    self.cccopyerrordeviceipaddress.value_namespace_prefix = name_space_prefix
                if(value_path == "ccCopyErrorDeviceIpAddressType"):
                    self.cccopyerrordeviceipaddresstype = value
                    self.cccopyerrordeviceipaddresstype.value_namespace = name_space
                    self.cccopyerrordeviceipaddresstype.value_namespace_prefix = name_space_prefix
                if(value_path == "ccCopyErrorDeviceWWN"):
                    self.cccopyerrordevicewwn = value
                    self.cccopyerrordevicewwn.value_namespace = name_space
                    self.cccopyerrordevicewwn.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cccopyerrorentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cccopyerrorentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "ccCopyErrorTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-CONFIG-COPY-MIB:CISCO-CONFIG-COPY-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "ccCopyErrorEntry"):
                for c in self.cccopyerrorentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoConfigCopyMib.Cccopyerrortable.Cccopyerrorentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cccopyerrorentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "ccCopyErrorEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            (self.cccopyerrortable is not None and self.cccopyerrortable.has_data()) or
            (self.cccopytable is not None and self.cccopytable.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.cccopyerrortable is not None and self.cccopyerrortable.has_operation()) or
            (self.cccopytable is not None and self.cccopytable.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "CISCO-CONFIG-COPY-MIB:CISCO-CONFIG-COPY-MIB" + path_buffer

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

        if (child_yang_name == "ccCopyErrorTable"):
            if (self.cccopyerrortable is None):
                self.cccopyerrortable = CiscoConfigCopyMib.Cccopyerrortable()
                self.cccopyerrortable.parent = self
                self._children_name_map["cccopyerrortable"] = "ccCopyErrorTable"
            return self.cccopyerrortable

        if (child_yang_name == "ccCopyTable"):
            if (self.cccopytable is None):
                self.cccopytable = CiscoConfigCopyMib.Cccopytable()
                self.cccopytable.parent = self
                self._children_name_map["cccopytable"] = "ccCopyTable"
            return self.cccopytable

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "ccCopyErrorTable" or name == "ccCopyTable"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = CiscoConfigCopyMib()
        return self._top_entity

