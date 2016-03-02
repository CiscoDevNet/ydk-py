""" CISCO_CONFIG_COPY_MIB 

This MIB facilitates writing of configuration files
of an SNMP Agent running Cisco's IOS in the 
following ways\: to and from the net, copying running 
configurations to startup configurations and 
vice\-versa, and copying a configuration
(running or startup) to and from the local 
IOS file system.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError


from ydk.models.inet.INET_ADDRESS_MIB import InetAddressType_Enum
from ydk.models.snmpv2.SNMPv2_TC import RowStatus_Enum

class ConfigCopyFailCause_Enum(Enum):
    """
    ConfigCopyFailCause_Enum

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

    """

    UNKNOWN = 1

    BADFILENAME = 2

    TIMEOUT = 3

    NOMEM = 4

    NOCONFIG = 5

    UNSUPPORTEDPROTOCOL = 6

    SOMECONFIGAPPLYFAILED = 7

    SYSTEMNOTREADY = 8

    REQUESTABORTED = 9


    @staticmethod
    def _meta_info():
        from ydk.models.config._meta import _CISCO_CONFIG_COPY_MIB as meta
        return meta._meta_table['ConfigCopyFailCause_Enum']


class ConfigCopyProtocol_Enum(Enum):
    """
    ConfigCopyProtocol_Enum

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

    """

    TFTP = 1

    FTP = 2

    RCP = 3

    SCP = 4

    SFTP = 5


    @staticmethod
    def _meta_info():
        from ydk.models.config._meta import _CISCO_CONFIG_COPY_MIB as meta
        return meta._meta_table['ConfigCopyProtocol_Enum']


class ConfigCopyState_Enum(Enum):
    """
    ConfigCopyState_Enum

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

    """

    WAITING = 1

    RUNNING = 2

    SUCCESSFUL = 3

    FAILED = 4


    @staticmethod
    def _meta_info():
        from ydk.models.config._meta import _CISCO_CONFIG_COPY_MIB as meta
        return meta._meta_table['ConfigCopyState_Enum']


class ConfigFileType_Enum(Enum):
    """
    ConfigFileType_Enum

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

    """

    NETWORKFILE = 1

    IOSFILE = 2

    STARTUPCONFIG = 3

    RUNNINGCONFIG = 4

    TERMINAL = 5

    FABRICSTARTUPCONFIG = 6


    @staticmethod
    def _meta_info():
        from ydk.models.config._meta import _CISCO_CONFIG_COPY_MIB as meta
        return meta._meta_table['ConfigFileType_Enum']



class CISCOCONFIGCOPYMIB(object):
    """
    
    
    .. attribute:: cccopyerrortable
    
    	A table containing information about the failure cause of the config copy operation. An entry is created only when the value of ccCopyState changes to 'failed' for a config copy operation.  Not all combinations of ccCopySourceFileType and ccCopyDestFileType need to be supported.  For example, an implementation may choose to support only the following combination\: ccCopySourceFileType = 'runningConfig' ccCopyDestFileType = 'fabricStartupConfig'.   In the case where a fabric wide config copy  operation is being performed, for example by selecting ccCopyDestFileType value to be 'fabricStartupConfig', it is possible that the fabric could have more than one device. In such cases this table would have one entry for each device in the fabric. In this case even if the  operation succeeded in one device and failed in  another, the operation as such has failed, so the global state  represented by ccCopyState 'failed', but for the device on which it was success,  ccCopyErrorDescription would have the  distinguished value, 'success'.   Once the config copy operation completes and if an entry gets instantiated, the management station  should retrieve the values of the status objects of  interest. Once an entry in ccCopyTable is deleted by management station, all the corresponding entries with the same ccCopyIndex in this table are also  deleted.   In order to prevent old entries from clogging the  table, entries age out at the same time as the  corresponding entry with same ccCopyIndex in  ccCopyTable ages out
    	**type**\: :py:class:`CcCopyErrorTable <ydk.models.config.CISCO_CONFIG_COPY_MIB.CISCOCONFIGCOPYMIB.CcCopyErrorTable>`
    
    .. attribute:: cccopytable
    
    	A table of config\-copy requests
    	**type**\: :py:class:`CcCopyTable <ydk.models.config.CISCO_CONFIG_COPY_MIB.CISCOCONFIGCOPYMIB.CcCopyTable>`
    
    

    """

    _prefix = 'cisco-config'
    _revision = '2005-04-06'

    def __init__(self):
        self.cccopyerrortable = CISCOCONFIGCOPYMIB.CcCopyErrorTable()
        self.cccopyerrortable.parent = self
        self.cccopytable = CISCOCONFIGCOPYMIB.CcCopyTable()
        self.cccopytable.parent = self


    class CcCopyErrorTable(object):
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
        	**type**\: list of :py:class:`CcCopyErrorEntry <ydk.models.config.CISCO_CONFIG_COPY_MIB.CISCOCONFIGCOPYMIB.CcCopyErrorTable.CcCopyErrorEntry>`
        
        

        """

        _prefix = 'cisco-config'
        _revision = '2005-04-06'

        def __init__(self):
            self.parent = None
            self.cccopyerrorentry = YList()
            self.cccopyerrorentry.parent = self
            self.cccopyerrorentry.name = 'cccopyerrorentry'


        class CcCopyErrorEntry(object):
            """
            An entry containing information about the
            outcome at one destination of a failed config
            copy operation.
            
            .. attribute:: cccopyerrorindex
            
            	A monotonically increasing integer for the sole purpose of indexing entries in this table. When a config copy operation has multiple  destinations, then this index value is used to  distinguish between those multiple destinations
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cccopyindex
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: cccopyerrordescription
            
            	The error description for the error happened for this destination of this config copy  operation
            	**type**\: str
            
            	**range:** 0..255
            
            .. attribute:: cccopyerrordeviceipaddress
            
            	The IP address of this destination device on which config copy operation is performed. The object value has to be consistent with the type specified in ccCopyErrorDeviceIpAddressType
            	**type**\: str
            
            	**range:** 0..255
            
            .. attribute:: cccopyerrordeviceipaddresstype
            
            	The type of Internet address for this destination device on which config copy operation is performed
            	**type**\: :py:class:`InetAddressType_Enum <ydk.models.inet.INET_ADDRESS_MIB.InetAddressType_Enum>`
            
            .. attribute:: cccopyerrordevicewwn
            
            	The World Wide Name (WWN) of this destination device on which config copy operation is performed. The value of this object is zero\-length string if  WWN is unassigned or unknown. For example, devices  which do not support fibre channel would not have WWN
            	**type**\: str
            
            	**range:** 0 \| 8 \| 16
            
            

            """

            _prefix = 'cisco-config'
            _revision = '2005-04-06'

            def __init__(self):
                self.parent = None
                self.cccopyerrorindex = None
                self.cccopyindex = None
                self.cccopyerrordescription = None
                self.cccopyerrordeviceipaddress = None
                self.cccopyerrordeviceipaddresstype = None
                self.cccopyerrordevicewwn = None

            @property
            def _common_path(self):
                if self.cccopyerrorindex is None:
                    raise YPYDataValidationError('Key property cccopyerrorindex is None')
                if self.cccopyindex is None:
                    raise YPYDataValidationError('Key property cccopyindex is None')

                return '/CISCO-CONFIG-COPY-MIB:CISCO-CONFIG-COPY-MIB/CISCO-CONFIG-COPY-MIB:ccCopyErrorTable/CISCO-CONFIG-COPY-MIB:ccCopyErrorEntry[CISCO-CONFIG-COPY-MIB:ccCopyErrorIndex = ' + str(self.cccopyerrorindex) + '][CISCO-CONFIG-COPY-MIB:ccCopyIndex = ' + str(self.cccopyindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.cccopyerrorindex is not None:
                    return True

                if self.cccopyindex is not None:
                    return True

                if self.cccopyerrordescription is not None:
                    return True

                if self.cccopyerrordeviceipaddress is not None:
                    return True

                if self.cccopyerrordeviceipaddresstype is not None:
                    return True

                if self.cccopyerrordevicewwn is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.config._meta import _CISCO_CONFIG_COPY_MIB as meta
                return meta._meta_table['CISCOCONFIGCOPYMIB.CcCopyErrorTable.CcCopyErrorEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-CONFIG-COPY-MIB:CISCO-CONFIG-COPY-MIB/CISCO-CONFIG-COPY-MIB:ccCopyErrorTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cccopyerrorentry is not None:
                for child_ref in self.cccopyerrorentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.config._meta import _CISCO_CONFIG_COPY_MIB as meta
            return meta._meta_table['CISCOCONFIGCOPYMIB.CcCopyErrorTable']['meta_info']


    class CcCopyTable(object):
        """
        A table of config\-copy requests.
        
        .. attribute:: cccopyentry
        
        	A config\-copy request.  A management station wishing to create an entry  should first generate a random serial number to be used as the index to this sparse table. The station  should then create the associated instance of the row status and row index objects.  It must also,  either in the same or in successive PDUs, create an instance of ccCopySourceFileType and  ccCopyDestFileType.  At least one of the file types defined in  ConfigFileType TC must be an agent\-config file type (i.e. 'startupConfig' or 'runningConfig'). If one of the file types is a 'networkFile', a valid ccCopyFileName and ccCopyServerAddressType and  ccCopyServerAddressRev1 or just ccCopyServerAddress must be created as well. If ccCopyServerAddress is created then ccCopyServerAddressRev1 will store the same IP address and ccCopyServerAddressType will  take the value 'ipv4'.  For a file type of 'iosFile', only a valid ccCopyFileName needs to be created as an  extra parameter.  It should also modify the default values for the  other configuration objects if the defaults are not appropriate.  Once the appropriate instance of all the  configuration objects have been created, either by an explicit SNMP set request or by default, the row  status should be set to active to initiate the  request. Note that this entire procedure may be  initiated via a single set request which specifies a row status of createAndGo as well as specifies valid values for the non\-defaulted  configuration objects.  Once the config\-copy request has been created  (i.e. the ccCopyEntryRowStatus has been made  active), the entry cannot be modified \- the only  operation possible after this is to delete the row.  Once the request completes, the management station  should retrieve the values of the status objects of  interest, and should then delete the entry.  In order to prevent old entries from clogging the  table, entries will be aged out, but an entry will  ever be deleted within 5 minutes of completing
        	**type**\: list of :py:class:`CcCopyEntry <ydk.models.config.CISCO_CONFIG_COPY_MIB.CISCOCONFIGCOPYMIB.CcCopyTable.CcCopyEntry>`
        
        

        """

        _prefix = 'cisco-config'
        _revision = '2005-04-06'

        def __init__(self):
            self.parent = None
            self.cccopyentry = YList()
            self.cccopyentry.parent = self
            self.cccopyentry.name = 'cccopyentry'


        class CcCopyEntry(object):
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
            
            .. attribute:: cccopyindex
            
            	Object which specifies a unique entry in the ccCopyTable.  A management station wishing to initiate a config\-copy operation should use a random value for this object when creating or modifying an instance of a ccCopyEntry. The RowStatus semantics of the ccCopyEntryRowStatus object will prevent access conflicts
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: cccopydestfiletype
            
            	specifies the type of file to copy to. Either the ccCopySourceFileType or the ccCopyDestFileType  (or both) must be of type 'runningConfig' or  'startupConfig'. Also, the ccCopySourceFileType  must be different from the ccCopyDestFileType.  If the ccCopyDestFileType has the value of  'networkFile', the  ccCopyServerAddress/ccCopyServerAddressType and ccCopyServerAddressRev1 and ccCopyFileName must also be created, and 3 objects together (ccCopyDestFileType, ccCopyServerAddressRev1,   ccCopyFileName) will uniquely identify the  destination file. If ccCopyServerAddress is created then ccCopyServerAddressRev1 will store the same IP address and ccCopyServerAddressType will take the  value 'ipv4'.   If the ccCopyDestFileType is 'iosFile', the  ccCopyFileName must also be created, and the 2 objects together (ccCopyDestFileType,  ccCopyFileName) will uniquely identify the  destination file
            	**type**\: :py:class:`ConfigFileType_Enum <ydk.models.config.CISCO_CONFIG_COPY_MIB.ConfigFileType_Enum>`
            
            .. attribute:: cccopyentryrowstatus
            
            	The status of this table entry. Once the entry status is set to active, the associated entry cannot  be modified until the request completes  (ccCopyState transitions to 'successful' or 'failed' state)
            	**type**\: :py:class:`RowStatus_Enum <ydk.models.snmpv2.SNMPv2_TC.RowStatus_Enum>`
            
            .. attribute:: cccopyfailcause
            
            	The reason why the config\-copy operation failed. This object is instantiated only when the  ccCopyState for this entry is in the  'failed' state
            	**type**\: :py:class:`ConfigCopyFailCause_Enum <ydk.models.config.CISCO_CONFIG_COPY_MIB.ConfigCopyFailCause_Enum>`
            
            .. attribute:: cccopyfilename
            
            	The file name (including the path, if applicable) of the file. This object must be created when either the ccCopySourceFileType or ccCopyDestFileType has the value 'networkFile' or 'iosFile'
            	**type**\: str
            
            	**pattern:** \\p{IsBasicLatin}{0,255}
            
            .. attribute:: cccopynotificationoncompletion
            
            	Specifies whether or not a ccCopyCompletion notification should be issued on completion of the TFTP transfer. If such a notification is desired,  it is the responsibility of the management entity to ensure that the SNMP administrative model is  configured in such a way as to allow the  notification to be delivered
            	**type**\: bool
            
            .. attribute:: cccopyprotocol
            
            	The protocol to be used for any copy.  If the copy operation occurs locally on the SNMP  agent (e.g. 'runningConfig' to 'startupConfig'), this object may be ignored by the implementation
            	**type**\: :py:class:`ConfigCopyProtocol_Enum <ydk.models.config.CISCO_CONFIG_COPY_MIB.ConfigCopyProtocol_Enum>`
            
            .. attribute:: cccopyserveraddress
            
            	The IP address of the TFTP server from (or to) which to copy the configuration file. This object  must be created when either the  ccCopySourceFileType or ccCopyDestFileType has the value 'networkFile'.  Values of 0.0.0.0 or FF.FF.FF.FF for ccCopyServerAddress are not allowed.  Since this object can just hold only IPv4 Transport type, it is deprecated and replaced by  ccCopyServerAddressRev1
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: cccopyserveraddressrev1
            
            	The IP address of the TFTP server from (or to) which to copy the configuration file. This object must be created when either the  ccCopySourceFileType or ccCopyDestFileType has the value 'networkFile'.    All bits as 0s or 1s for ccCopyServerAddressRev1 are not allowed.  The format of this address depends on the value of  the ccCopyServerAddressType object
            	**type**\: str
            
            	**range:** 0..255
            
            .. attribute:: cccopyserveraddresstype
            
            	This object indicates the transport type of the address contained in ccCopyServerAddressRev1 object.  This must be created when either the ccCopySourceFileType or ccCopyDestFileType has the value 'networkFile'
            	**type**\: :py:class:`InetAddressType_Enum <ydk.models.inet.INET_ADDRESS_MIB.InetAddressType_Enum>`
            
            .. attribute:: cccopysourcefiletype
            
            	Specifies the type of file to copy from. Either the ccCopySourceFileType or the ccCopyDestFileType  (or both) must be of type 'runningConfig' or  'startupConfig'. Also, the ccCopySourceFileType must be different from the ccCopyDestFileType.  If the ccCopySourceFileType has the value of  'networkFile', the ccCopyServerAddress/ ccCopyServerAddressRev1 and ccCopyServerAddressType and ccCopyFileName must also be created, and 3  objects together (ccCopySourceFileType, ccCopyServerAddressRev1, ccCopyFileName) will  uniquely identify the source file. If  ccCopyServerAddress is created then  ccCopyServerAddressRev1 will store the same IP address and ccCopyServerAddressType will  take the value 'ipv4'.   If the ccCopySourceFileType is 'iosFile', the  ccCopyFileName must also be created, and the  2 objects together (ccCopySourceFileType, ccCopyFileName) will uniquely identify the source  file
            	**type**\: :py:class:`ConfigFileType_Enum <ydk.models.config.CISCO_CONFIG_COPY_MIB.ConfigFileType_Enum>`
            
            .. attribute:: cccopystate
            
            	Specifies the state of this config\-copy request. This value of this object is instantiated only after  the row has been instantiated, i.e. after the  ccCopyEntryRowStatus has been made active
            	**type**\: :py:class:`ConfigCopyState_Enum <ydk.models.config.CISCO_CONFIG_COPY_MIB.ConfigCopyState_Enum>`
            
            .. attribute:: cccopytimecompleted
            
            	Specifies the time the ccCopyState last transitioned from 'running' to 'successful' or  'failed' states. This object is instantiated only  after the row has been instantiated. Its value will remain 0 until the request has  completed
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cccopytimestarted
            
            	Specifies the time the ccCopyState last transitioned to 'running', or 0 if the state has  never transitioned to 'running'(e.g., stuck in 'waiting' state).  This object is instantiated only after the row has  been instantiated
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cccopyusername
            
            	Remote username for copy via FTP, RCP, SFTP or SCP protocol. This object must be created when the ccCopyProtocol is 'rcp', 'scp', 'ftp', or 'sftp'. If the protocol is RCP, it will override the remote  username configured through the          rcmd remote\-username <username> configuration command.  The remote username is sent as the server username  in an RCP command request sent by the system to a remote RCP server
            	**type**\: str
            
            	**range:** 1..40
            
            .. attribute:: cccopyuserpassword
            
            	Password used by FTP, SFTP or SCP for copying a file to/from an FTP/SFTP/SCP server. This object  must be created when the ccCopyProtocol is FTP or SCP.  Reading it returns a zero\-length string for security  reasons
            	**type**\: str
            
            	**range:** 1..40
            
            

            """

            _prefix = 'cisco-config'
            _revision = '2005-04-06'

            def __init__(self):
                self.parent = None
                self.cccopyindex = None
                self.cccopydestfiletype = None
                self.cccopyentryrowstatus = None
                self.cccopyfailcause = None
                self.cccopyfilename = None
                self.cccopynotificationoncompletion = None
                self.cccopyprotocol = None
                self.cccopyserveraddress = None
                self.cccopyserveraddressrev1 = None
                self.cccopyserveraddresstype = None
                self.cccopysourcefiletype = None
                self.cccopystate = None
                self.cccopytimecompleted = None
                self.cccopytimestarted = None
                self.cccopyusername = None
                self.cccopyuserpassword = None

            @property
            def _common_path(self):
                if self.cccopyindex is None:
                    raise YPYDataValidationError('Key property cccopyindex is None')

                return '/CISCO-CONFIG-COPY-MIB:CISCO-CONFIG-COPY-MIB/CISCO-CONFIG-COPY-MIB:ccCopyTable/CISCO-CONFIG-COPY-MIB:ccCopyEntry[CISCO-CONFIG-COPY-MIB:ccCopyIndex = ' + str(self.cccopyindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.cccopyindex is not None:
                    return True

                if self.cccopydestfiletype is not None:
                    return True

                if self.cccopyentryrowstatus is not None:
                    return True

                if self.cccopyfailcause is not None:
                    return True

                if self.cccopyfilename is not None:
                    return True

                if self.cccopynotificationoncompletion is not None:
                    return True

                if self.cccopyprotocol is not None:
                    return True

                if self.cccopyserveraddress is not None:
                    return True

                if self.cccopyserveraddressrev1 is not None:
                    return True

                if self.cccopyserveraddresstype is not None:
                    return True

                if self.cccopysourcefiletype is not None:
                    return True

                if self.cccopystate is not None:
                    return True

                if self.cccopytimecompleted is not None:
                    return True

                if self.cccopytimestarted is not None:
                    return True

                if self.cccopyusername is not None:
                    return True

                if self.cccopyuserpassword is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.config._meta import _CISCO_CONFIG_COPY_MIB as meta
                return meta._meta_table['CISCOCONFIGCOPYMIB.CcCopyTable.CcCopyEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-CONFIG-COPY-MIB:CISCO-CONFIG-COPY-MIB/CISCO-CONFIG-COPY-MIB:ccCopyTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cccopyentry is not None:
                for child_ref in self.cccopyentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.config._meta import _CISCO_CONFIG_COPY_MIB as meta
            return meta._meta_table['CISCOCONFIGCOPYMIB.CcCopyTable']['meta_info']

    @property
    def _common_path(self):

        return '/CISCO-CONFIG-COPY-MIB:CISCO-CONFIG-COPY-MIB'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if not self.is_config():
            return False
        if self.is_presence():
            return True
        if self.cccopyerrortable is not None and self.cccopyerrortable._has_data():
            return True

        if self.cccopyerrortable is not None and self.cccopyerrortable.is_presence():
            return True

        if self.cccopytable is not None and self.cccopytable._has_data():
            return True

        if self.cccopytable is not None and self.cccopytable.is_presence():
            return True

        return False

    def is_presence(self):
        ''' Returns True if this instance represents presence container else returns False '''
        return False

    @staticmethod
    def _meta_info():
        from ydk.models.config._meta import _CISCO_CONFIG_COPY_MIB as meta
        return meta._meta_table['CISCOCONFIGCOPYMIB']['meta_info']


