""" CISCO_FLASH_MIB 

This MIB provides for the management of Cisco
Flash Devices.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError


from ydk.models.inet.INET_ADDRESS_MIB import InetAddressType_Enum
from ydk.models.snmpv2.SNMPv2_TC import RowStatus_Enum

class FlashFileType_Enum(Enum):
    """
    FlashFileType_Enum

    File types for files in a flash.
    
    unknown        \- file type is not one of the following.
    config         \- configuration file like
                     startup configuration or
                     running configuration.
    image          \- image file.
    directory      \- directory entry.
    crashinfo      \- file containing crashinfo.

    """

    UNKNOWN = 1

    CONFIG = 2

    IMAGE = 3

    DIRECTORY = 4

    CRASHINFO = 5


    @staticmethod
    def _meta_info():
        from ydk.models.flash._meta import _CISCO_FLASH_MIB as meta
        return meta._meta_table['FlashFileType_Enum']



class CISCOFLASHMIB(object):
    """
    
    
    .. attribute:: ciscoflashcfg
    
    	
    	**type**\: :py:class:`CiscoFlashCfg <ydk.models.flash.CISCO_FLASH_MIB.CISCOFLASHMIB.CiscoFlashCfg>`
    
    .. attribute:: ciscoflashchiptable
    
    	Table of Flash device chip properties for each initialized Flash device. This table is meant primarily for aiding error diagnosis
    	**type**\: :py:class:`CiscoFlashChipTable <ydk.models.flash.CISCO_FLASH_MIB.CISCOFLASHMIB.CiscoFlashChipTable>`
    
    .. attribute:: ciscoflashcopytable
    
    	A table of Flash copy operation entries. Each entry represents a Flash copy operation (to or from Flash) that has been initiated
    	**type**\: :py:class:`CiscoFlashCopyTable <ydk.models.flash.CISCO_FLASH_MIB.CISCOFLASHMIB.CiscoFlashCopyTable>`
    
    .. attribute:: ciscoflashdevice
    
    	
    	**type**\: :py:class:`CiscoFlashDevice <ydk.models.flash.CISCO_FLASH_MIB.CISCOFLASHMIB.CiscoFlashDevice>`
    
    .. attribute:: ciscoflashdevicetable
    
    	Table of Flash device properties for each initialized Flash device. Each Flash device installed in a system is detected, sized, and initialized when the system image boots up. For removable Flash devices, the device properties will be dynamically deleted and recreated as the device is removed and inserted. Note that in this case, the newly inserted device may not be the same as the earlier removed one. The ciscoFlashDeviceInitTime object is available for a management station to determine the time at which a device was initialized, and thereby detect the change of a removable device. A removable device that has not been installed will also have an entry in this table. This is to let a management station know about a removable device that has been removed. Since a removed device obviously cannot be sized and initialized, the table entry for such a device will have ciscoFlashDeviceSize equal to zero, and the following objects will have an indeterminate value\:         ciscoFlashDeviceMinPartitionSize,         ciscoFlashDeviceMaxPartitions,         ciscoFlashDevicePartitions, and         ciscoFlashDeviceChipCount. ciscoFlashDeviceRemovable will be true to indicate it is removable
    	**type**\: :py:class:`CiscoFlashDeviceTable <ydk.models.flash.CISCO_FLASH_MIB.CISCOFLASHMIB.CiscoFlashDeviceTable>`
    
    .. attribute:: ciscoflashfilebytypetable
    
    	Table of information for files on the manageable flash devices sorted by File Types
    	**type**\: :py:class:`CiscoFlashFileByTypeTable <ydk.models.flash.CISCO_FLASH_MIB.CISCOFLASHMIB.CiscoFlashFileByTypeTable>`
    
    .. attribute:: ciscoflashfiletable
    
    	Table of information for files in a Flash partition
    	**type**\: :py:class:`CiscoFlashFileTable <ydk.models.flash.CISCO_FLASH_MIB.CISCOFLASHMIB.CiscoFlashFileTable>`
    
    .. attribute:: ciscoflashmiscoptable
    
    	A table of misc Flash operation entries. Each entry represents a Flash operation that has been initiated
    	**type**\: :py:class:`CiscoFlashMiscOpTable <ydk.models.flash.CISCO_FLASH_MIB.CISCOFLASHMIB.CiscoFlashMiscOpTable>`
    
    .. attribute:: ciscoflashpartitioningtable
    
    	A table of Flash partitioning operation entries. Each entry represents a Flash partitioning operation that has been initiated
    	**type**\: :py:class:`CiscoFlashPartitioningTable <ydk.models.flash.CISCO_FLASH_MIB.CISCOFLASHMIB.CiscoFlashPartitioningTable>`
    
    .. attribute:: ciscoflashpartitiontable
    
    	Table of flash device partition properties for each initialized flash partition. Whenever there is no explicit partitioning done, a single partition spanning the entire device will be assumed to exist. There will therefore always be atleast one partition on a device
    	**type**\: :py:class:`CiscoFlashPartitionTable <ydk.models.flash.CISCO_FLASH_MIB.CISCOFLASHMIB.CiscoFlashPartitionTable>`
    
    

    """

    _prefix = 'cisco-flash'
    _revision = '2013-08-06'

    def __init__(self):
        self.ciscoflashcfg = CISCOFLASHMIB.CiscoFlashCfg()
        self.ciscoflashcfg.parent = self
        self.ciscoflashchiptable = CISCOFLASHMIB.CiscoFlashChipTable()
        self.ciscoflashchiptable.parent = self
        self.ciscoflashcopytable = CISCOFLASHMIB.CiscoFlashCopyTable()
        self.ciscoflashcopytable.parent = self
        self.ciscoflashdevice = CISCOFLASHMIB.CiscoFlashDevice()
        self.ciscoflashdevice.parent = self
        self.ciscoflashdevicetable = CISCOFLASHMIB.CiscoFlashDeviceTable()
        self.ciscoflashdevicetable.parent = self
        self.ciscoflashfilebytypetable = CISCOFLASHMIB.CiscoFlashFileByTypeTable()
        self.ciscoflashfilebytypetable.parent = self
        self.ciscoflashfiletable = CISCOFLASHMIB.CiscoFlashFileTable()
        self.ciscoflashfiletable.parent = self
        self.ciscoflashmiscoptable = CISCOFLASHMIB.CiscoFlashMiscOpTable()
        self.ciscoflashmiscoptable.parent = self
        self.ciscoflashpartitioningtable = CISCOFLASHMIB.CiscoFlashPartitioningTable()
        self.ciscoflashpartitioningtable.parent = self
        self.ciscoflashpartitiontable = CISCOFLASHMIB.CiscoFlashPartitionTable()
        self.ciscoflashpartitiontable.parent = self


    class CiscoFlashCfg(object):
        """
        
        
        .. attribute:: ciscoflashcfgdevinsnotifenable
        
        	Specifies whether or not a notification should be generated on the insertion of a Flash device.  If the value of this object is 'true' then the ciscoFlashDeviceInsertedNotif notification will be generated.  If the value of this object is 'false' then the ciscoFlashDeviceInsertedNotif notification will not be generated.  It is the responsibility of the management entity to ensure that the SNMP administrative model is configured in such a way as to allow the notification to be delivered
        	**type**\: bool
        
        .. attribute:: ciscoflashcfgdevremnotifenable
        
        	Specifies whether or not a notification should be generated on the removal of a Flash device.  If the value of this object is 'true' then the ciscoFlashDeviceRemovedNotif notification will be generated.  If the value of this object is 'false' then the ciscoFlashDeviceRemovedNotif notification will not be generated.  It is the responsibility of the management entity to ensure that the SNMP administrative model is configured in such a way as to allow the notification to be delivered
        	**type**\: bool
        
        .. attribute:: ciscoflashpartitionlowspacenotifenable
        
        	This object specifies whether or not a notification should be generated when the free space falls below the threshold value on a flash partition and on recovery from low space.  If the value of this object is 'true' then ciscoFlashPartitionLowSpaceNotif and ciscoFlashPartitionLowSpaceRecoveryNotif notifications will be generated.  If the value of this object is 'false' then the ciscoFlashPartitionLowSpaceNotif  and ciscoFlashPartitionLowSpaceRecoveryNotif notifications will not be generated.  It is the responsibility of the management entity to ensure that the SNMP administrative model is configured in such a way as to allow the notifications to be delivered
        	**type**\: bool
        
        

        """

        _prefix = 'cisco-flash'
        _revision = '2013-08-06'

        def __init__(self):
            self.parent = None
            self.ciscoflashcfgdevinsnotifenable = None
            self.ciscoflashcfgdevremnotifenable = None
            self.ciscoflashpartitionlowspacenotifenable = None

        @property
        def _common_path(self):

            return '/CISCO-FLASH-MIB:CISCO-FLASH-MIB/CISCO-FLASH-MIB:ciscoFlashCfg'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.ciscoflashcfgdevinsnotifenable is not None:
                return True

            if self.ciscoflashcfgdevremnotifenable is not None:
                return True

            if self.ciscoflashpartitionlowspacenotifenable is not None:
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.flash._meta import _CISCO_FLASH_MIB as meta
            return meta._meta_table['CISCOFLASHMIB.CiscoFlashCfg']['meta_info']


    class CiscoFlashChipTable(object):
        """
        Table of Flash device chip properties for each
        initialized Flash device.
        This table is meant primarily for aiding error
        diagnosis.
        
        .. attribute:: ciscoflashchipentry
        
        	An entry in the table of chip info for each flash device initialized in the system. An entry is indexed by two objects \- the device index and the chip index within that device
        	**type**\: list of :py:class:`CiscoFlashChipEntry <ydk.models.flash.CISCO_FLASH_MIB.CISCOFLASHMIB.CiscoFlashChipTable.CiscoFlashChipEntry>`
        
        

        """

        _prefix = 'cisco-flash'
        _revision = '2013-08-06'

        def __init__(self):
            self.parent = None
            self.ciscoflashchipentry = YList()
            self.ciscoflashchipentry.parent = self
            self.ciscoflashchipentry.name = 'ciscoflashchipentry'


        class CiscoFlashChipEntry(object):
            """
            An entry in the table of chip info for each
            flash device initialized in the system.
            An entry is indexed by two objects \- the
            device index and the chip index within that
            device.
            
            .. attribute:: ciscoflashchipindex
            
            	Chip sequence number within selected flash device. Used to index within chip info table. Value starts from 1 and should not be greater than ciscoFlashDeviceChipCount for that device. When retrieving chip information for chips within a partition, the sequence number should lie between ciscoFlashPartitionStartChip & ciscoFlashPartitionEndChip (both inclusive)
            	**type**\: int
            
            	**range:** 1..64
            
            .. attribute:: ciscoflashdeviceindex
            
            	
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: ciscoflashchipcode
            
            	Manufacturer and device code for a chip. Lower byte will contain the device code. Upper byte will contain the manufacturer code. If a chip code is unknown because it could not be queried out of the chip, the value of this object will be 00\:00. Since programming algorithms differ from chip type to chip type, this chip code should be used to determine which algorithms to use (and thereby whether the chip is supported in the first place)
            	**type**\: str
            
            	**range:** 0..5
            
            .. attribute:: ciscoflashchipdescr
            
            	Flash chip name corresponding to the chip code. The name will contain the manufacturer and the chip type. It will be of the form \:   Intel 27F008SA. In the case where a chip code is unknown, this object will be an empty (NULL) string. In the case where the chip code is known but the chip is not supported by the system, this object will be an empty (NULL) string. A management station is therefore expected to use the chip code and the chip description in conjunction to provide additional information whenever the ciscoFlashPartitionStatus object has the readOnly(1) value
            	**type**\: str
            
            	**range:** 0..32
            
            .. attribute:: ciscoflashchiperaseretries
            
            	This object will provide a cumulative count (since last system boot up or initialization) of the number of erase retries that were done in the chip. Typically, a maximum of 2000 retries are done in a single erase zone (which may be a full chip or a portion, depending on the chip technology) before flagging an erase error. A management station is expected to get this object for each chip in a partition after an erase failure in that partition. To keep a track of retries for a given erase operation, the management station would have to retrieve the values for the concerned chips before and after any erase operation. Note that erase may be done through an independent command, or through a copy\-to\-flash command
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ciscoflashchipmaxeraseretries
            
            	The maximum number of erase retries done within an erase sector before declaring an erase failure
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ciscoflashchipmaxwriteretries
            
            	The maximum number of write retries done at any single location before declaring a write failure
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ciscoflashchipwriteretries
            
            	This object will provide a cumulative count (since last system boot up or initialization) of the number of write retries that were done in the chip. If no writes have been done to Flash, the count will be zero. Typically, a maximum of 25 retries are done on a single location before flagging a write error. A management station is expected to get this object for each chip in a partition after a write failure in that partition. To keep a track of retries for a given write operation, the management station would have to retrieve the values for the concerned chips before and after any write operation
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'cisco-flash'
            _revision = '2013-08-06'

            def __init__(self):
                self.parent = None
                self.ciscoflashchipindex = None
                self.ciscoflashdeviceindex = None
                self.ciscoflashchipcode = None
                self.ciscoflashchipdescr = None
                self.ciscoflashchiperaseretries = None
                self.ciscoflashchipmaxeraseretries = None
                self.ciscoflashchipmaxwriteretries = None
                self.ciscoflashchipwriteretries = None

            @property
            def _common_path(self):
                if self.ciscoflashchipindex is None:
                    raise YPYDataValidationError('Key property ciscoflashchipindex is None')
                if self.ciscoflashdeviceindex is None:
                    raise YPYDataValidationError('Key property ciscoflashdeviceindex is None')

                return '/CISCO-FLASH-MIB:CISCO-FLASH-MIB/CISCO-FLASH-MIB:ciscoFlashChipTable/CISCO-FLASH-MIB:ciscoFlashChipEntry[CISCO-FLASH-MIB:ciscoFlashChipIndex = ' + str(self.ciscoflashchipindex) + '][CISCO-FLASH-MIB:ciscoFlashDeviceIndex = ' + str(self.ciscoflashdeviceindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.ciscoflashchipindex is not None:
                    return True

                if self.ciscoflashdeviceindex is not None:
                    return True

                if self.ciscoflashchipcode is not None:
                    return True

                if self.ciscoflashchipdescr is not None:
                    return True

                if self.ciscoflashchiperaseretries is not None:
                    return True

                if self.ciscoflashchipmaxeraseretries is not None:
                    return True

                if self.ciscoflashchipmaxwriteretries is not None:
                    return True

                if self.ciscoflashchipwriteretries is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.flash._meta import _CISCO_FLASH_MIB as meta
                return meta._meta_table['CISCOFLASHMIB.CiscoFlashChipTable.CiscoFlashChipEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-FLASH-MIB:CISCO-FLASH-MIB/CISCO-FLASH-MIB:ciscoFlashChipTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.ciscoflashchipentry is not None:
                for child_ref in self.ciscoflashchipentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.flash._meta import _CISCO_FLASH_MIB as meta
            return meta._meta_table['CISCOFLASHMIB.CiscoFlashChipTable']['meta_info']


    class CiscoFlashCopyTable(object):
        """
        A table of Flash copy operation entries. Each
        entry represents a Flash copy operation (to or
        from Flash) that has been initiated.
        
        .. attribute:: ciscoflashcopyentry
        
        	A Flash copy operation entry. Each entry consists of a command, a source, and optional parameters such as protocol to be used, a destination, a server address, etc.  A management station wishing to create an entry should first generate a pseudo\-random serial number to be used as the index to this sparse table.  The station should then create the associated instance of the row status object. It must also, either in the same or in successive PDUs, create the associated instance of the command and parameter objects. It should also modify the default values for any of the parameter objects if the defaults are not appropriate.  Once the appropriate instances of all the command objects have been created, either by an explicit SNMP set request or by default, the row status should be set to active to initiate the operation. Note that this entire procedure may be initiated via a single set request which specifies a row status  of createAndGo as well as specifies valid values for the non\-defaulted parameter objects.  Once an operation has been activated, it cannot be stopped.  Once the operation completes, the management station should retrieve the value of the status object (and time if desired), and delete the entry.  In order to prevent old entries from clogging the table, entries will be aged out, but an entry will never be deleted within 5 minutes of completing
        	**type**\: list of :py:class:`CiscoFlashCopyEntry <ydk.models.flash.CISCO_FLASH_MIB.CISCOFLASHMIB.CiscoFlashCopyTable.CiscoFlashCopyEntry>`
        
        

        """

        _prefix = 'cisco-flash'
        _revision = '2013-08-06'

        def __init__(self):
            self.parent = None
            self.ciscoflashcopyentry = YList()
            self.ciscoflashcopyentry.parent = self
            self.ciscoflashcopyentry.name = 'ciscoflashcopyentry'


        class CiscoFlashCopyEntry(object):
            """
            A Flash copy operation entry. Each entry consists
            of a command, a source, and optional parameters such
            as protocol to be used, a destination, a server address,
            etc.
            
            A management station wishing to create an entry should
            first generate a pseudo\-random serial number to be used
            as the index to this sparse table.  The station should
            then create the associated instance of the row status
            object. It must also, either in the same or in successive
            PDUs, create the associated instance of the command and
            parameter objects. It should also modify the default values
            for any of the parameter objects if the defaults are not
            appropriate.
            
            Once the appropriate instances of all the command
            objects have been created, either by an explicit SNMP
            set request or by default, the row status should be set
            to active to initiate the operation. Note that this entire
            procedure may be initiated via a single set request which
            specifies a row status  of createAndGo as well as specifies
            valid values for the non\-defaulted parameter objects.
            
            Once an operation has been activated, it cannot be
            stopped.
            
            Once the operation completes, the management station should
            retrieve the value of the status object (and time if
            desired), and delete the entry.  In order to prevent old
            entries from clogging the table, entries will be aged out,
            but an entry will never be deleted within 5 minutes of
            completing.
            
            .. attribute:: ciscoflashcopyserialnumber
            
            	Object which specifies a unique entry in the table. A management station wishing to initiate a copy operation should use a pseudo\-random value for this object when creating or modifying an instance of a ciscoFlashCopyEntry
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: ciscoflashcopycommand
            
            	The copy command to be executed. Mandatory. Note that it is possible for a system to support multiple file systems (different file systems on different Flash devices, or different file systems on different partitions within a device). Each such file system may support only a subset of these commands. If a command is unsupported, the invalidOperation(3) error will be reported in the operation status.  Command                 Remarks copyToFlashWithErase    Copy a file to flash; erase                         flash before copy.                         Use the TFTP or rcp protocol. copyToFlashWithoutErase Copy a file to flash; do not                         erase.                         Note that this command will fail                         if the PartitionNeedErasure                         object specifies that the                         partition being copied to needs                         erasure.                         Use the TFTP or rcp protocol. copyFromFlash           Copy a file from flash using                         the TFTP, rcp or lex protocol.                         Note that the lex protocol                         can only be used to copy to a                         lex device. copyFromFlhLog          Copy contents of FLH log to                         server using TFTP protocol.   Command table           Parameters copyToFlashWithErase    CopyProtocol                         CopyServerAddress                         CopySourceName                         CopyDestinationName (opt)                         CopyRemoteUserName (opt)                         CopyNotifyOnCompletion (opt) copyToFlashWithoutErase CopyProtocol                         CopyServerAddress                         CopySourceName                         CopyDestinationName (opt)                         CopyRemoteUserName (opt)                         CopyNotifyOnCompletion (opt) copyFromFlash           CopyProtocol                         CopyServerAddress                         CopySourceName                         CopyDestinationName (opt)                         CopyRemoteUserName (opt)                         CopyNotifyOnCompletion (opt) copyFromFlhLog          CopyProtocol                         CopyServerAddress                         CopyDestinationName                         CopyNotifyOnCompletion (opt)
            	**type**\: :py:class:`CiscoFlashCopyCommand_Enum <ydk.models.flash.CISCO_FLASH_MIB.CISCOFLASHMIB.CiscoFlashCopyTable.CiscoFlashCopyEntry.CiscoFlashCopyCommand_Enum>`
            
            .. attribute:: ciscoflashcopydestinationname
            
            	Destination file name.  For a copy to Flash\: File name must be of the form         {device>\:][<partition>\:]<file> where <device> is a value obtained from FlashDeviceName,       <partition> is obtained from FlashPartitionName   and <file> is any character string that does not have embedded colon characters. A management station could derive its own partition name as per the description for the ciscoFlashPartitionName object. If <device> is not specified, the default Flash device will be assumed. If <partition> is not specified, the default partition will be assumed. If a device is not partitioned into 2 or more partitions, this value may be left out. If <file> is not specified, it will default to <file> specified in ciscoFlashCopySourceName.  For a copy from Flash via tftp or rcp, the file name will be as per the file naming conventions and destination sub\-directory on the server. If not specified, <file> from the source file name will be used. For a copy from Flash via lex, this string will consist of numeric characters specifying the interface on the lex box that will receive the source flash image
            	**type**\: str
            
            	**range:** 0..255
            
            .. attribute:: ciscoflashcopyentrystatus
            
            	The status of this table entry
            	**type**\: :py:class:`RowStatus_Enum <ydk.models.snmpv2.SNMPv2_TC.RowStatus_Enum>`
            
            .. attribute:: ciscoflashcopynotifyoncompletion
            
            	Specifies whether or not a notification should be generated on the completion of the copy operation. If specified, ciscoFlashCopyCompletionTrap will be generated. It is the responsibility of the management entity to ensure that the SNMP administrative model is configured in such a way as to allow the notification to be delivered
            	**type**\: bool
            
            .. attribute:: ciscoflashcopyprotocol
            
            	The protocol to be used for any copy. Optional. Will default to tftp if not specified.  Since feature support depends on a software release, version number within the release, platform, and maybe the image type (subset type), a management station would be expected to somehow determine the protocol support for a command
            	**type**\: :py:class:`CiscoFlashCopyProtocol_Enum <ydk.models.flash.CISCO_FLASH_MIB.CISCOFLASHMIB.CiscoFlashCopyTable.CiscoFlashCopyEntry.CiscoFlashCopyProtocol_Enum>`
            
            .. attribute:: ciscoflashcopyremotepassword
            
            	Password used by ftp, sftp or scp for copying a file to/from an ftp/sftp/scp server. This object must be created when the ciscoFlashCopyProtocol is ftp, sftp or scp. Reading it returns a zero\-length string for security reasons
            	**type**\: str
            
            	**range:** 1..40
            
            .. attribute:: ciscoflashcopyremoteusername
            
            	Remote user name for copy via rcp protocol. Optional. This object will be ignored for protocols other than rcp. If specified, it will override the remote user\-name configured through the         rcmd remote\-username configuration command. The remote user\-name is sent as the server user\-name in an rcp command request sent by the system to a remote rcp server
            	**type**\: str
            
            	**range:** 1..255
            
            .. attribute:: ciscoflashcopyserveraddress
            
            	The server address to be used for any copy. Optional. Will default to 'FFFFFFFF'H  (or 255.255.255.255).  Since this object can just hold only IPv4 Transport type, it is deprecated and replaced by ciscoFlashCopyServerAddrRev1
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: ciscoflashcopyserveraddrrev1
            
            	The server address to be used for any copy. Optional. Will default to 'FFFFFFFF'H  (or 255.255.255.255).  The Format of this address depends on the value of the ciscoFlashCopyServerAddrType.  This object deprecates the old ciscoFlashCopyServerAddress object
            	**type**\: str
            
            	**range:** 0..255
            
            .. attribute:: ciscoflashcopyserveraddrtype
            
            	This object indicates the transport type of the address contained in ciscoFlashCopyServerAddrRev1. Optional. Will default to '1' (IPv4 address type)
            	**type**\: :py:class:`InetAddressType_Enum <ydk.models.inet.INET_ADDRESS_MIB.InetAddressType_Enum>`
            
            .. attribute:: ciscoflashcopysourcename
            
            	Source file name, either in Flash or on a server, depending on the type of copy command. Mandatory.  For a copy from Flash\: File name must be of the form         [device>\:][\:] where  is a value obtained from FlashDeviceName,          is obtained from FlashPartitionName     and  is the name of a file in Flash. A management station could derive its own partition name as per the description for the ciscoFlashPartitionName object. If <device> is not specified, the default Flash device will be assumed. If <partition> is not specified, the default partition will be assumed. If a device is not partitioned into 2 or more partitions, this value may be left out.  For a copy to Flash, the file name will be as per the file naming conventions and path to the file on the server
            	**type**\: str
            
            	**range:** 1..255
            
            .. attribute:: ciscoflashcopystatus
            
            	The status of the specified copy operation.  copyOperationPending \:         operation request is received and         pending for validation and process  copyInProgress \:         specified operation is active  copyOperationSuccess \:         specified operation is supported and         completed successfully  copyInvalidOperation \:         command invalid or command\-protocol\-device         combination unsupported  copyInvalidProtocol \:         invalid protocol specified  copyInvalidSourceName \:         invalid source file name specified         For the  copy from flash to lex operation, this         error code will be returned when the source file         is not a valid lex image.  copyInvalidDestName \:         invalid target name (file or partition or         device name) specified         For the  copy from flash to lex operation, this         error code will be returned when no lex devices         are connected to the router or when an invalid         lex interface number has been specified in         the destination string.  copyInvalidServerAddress \:         invalid server address specified  copyDeviceBusy \:         specified device is in use and locked by         another process  copyDeviceOpenError \:         invalid device name  copyDeviceError \:         device read, write or erase error  copyDeviceNotProgrammable \:         device is read\-only but a write or erase         operation was specified  copyDeviceFull \:         device is filled to capacity  copyFileOpenError \:         invalid file name; file not found in partition  copyFileTransferError \:         file transfer was unsuccessfull; network failure  copyFileChecksumError \:         file checksum in Flash failed  copyNoMemory \:         system running low on memory  copyUnknownFailure \:         failure unknown  copyProhibited\:       stop user from overwriting current boot image file
            	**type**\: :py:class:`CiscoFlashCopyStatus_Enum <ydk.models.flash.CISCO_FLASH_MIB.CISCOFLASHMIB.CiscoFlashCopyTable.CiscoFlashCopyEntry.CiscoFlashCopyStatus_Enum>`
            
            .. attribute:: ciscoflashcopytime
            
            	Time taken for the copy operation. This object will be like a stopwatch, starting when the operation starts, stopping when the operation completes. If a management entity keeps a database of completion times for various operations, it can then use the stopwatch capability to display percentage completion time
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ciscoflashcopyverify
            
            	Specifies whether the file that is copied need to be verified for integrity / authenticity, after copy succeeds. If it is set to true, and if the file that is copied doesn't have integrity /authenticity attachement, or the integrity / authenticity check fails, then the command will be aborted, and the file that is copied will be deleted from the destination file system
            	**type**\: bool
            
            

            """

            _prefix = 'cisco-flash'
            _revision = '2013-08-06'

            def __init__(self):
                self.parent = None
                self.ciscoflashcopyserialnumber = None
                self.ciscoflashcopycommand = None
                self.ciscoflashcopydestinationname = None
                self.ciscoflashcopyentrystatus = None
                self.ciscoflashcopynotifyoncompletion = None
                self.ciscoflashcopyprotocol = None
                self.ciscoflashcopyremotepassword = None
                self.ciscoflashcopyremoteusername = None
                self.ciscoflashcopyserveraddress = None
                self.ciscoflashcopyserveraddrrev1 = None
                self.ciscoflashcopyserveraddrtype = None
                self.ciscoflashcopysourcename = None
                self.ciscoflashcopystatus = None
                self.ciscoflashcopytime = None
                self.ciscoflashcopyverify = None

            class CiscoFlashCopyCommand_Enum(Enum):
                """
                CiscoFlashCopyCommand_Enum

                The copy command to be executed. Mandatory.
                Note that it is possible for a system to support
                multiple file systems (different file systems on
                different Flash devices, or different file systems
                on different partitions within a device). Each such
                file system may support only a subset of these commands.
                If a command is unsupported, the invalidOperation(3)
                error will be reported in the operation status.
                
                Command                 Remarks
                copyToFlashWithErase    Copy a file to flash; erase
                                        flash before copy.
                                        Use the TFTP or rcp protocol.
                copyToFlashWithoutErase Copy a file to flash; do not
                                        erase.
                                        Note that this command will fail
                                        if the PartitionNeedErasure
                                        object specifies that the
                                        partition being copied to needs
                                        erasure.
                                        Use the TFTP or rcp protocol.
                copyFromFlash           Copy a file from flash using
                                        the TFTP, rcp or lex protocol.
                                        Note that the lex protocol
                                        can only be used to copy to a
                                        lex device.
                copyFromFlhLog          Copy contents of FLH log to
                                        server using TFTP protocol.
                
                
                Command table           Parameters
                copyToFlashWithErase    CopyProtocol
                                        CopyServerAddress
                                        CopySourceName
                                        CopyDestinationName (opt)
                                        CopyRemoteUserName (opt)
                                        CopyNotifyOnCompletion (opt)
                copyToFlashWithoutErase CopyProtocol
                                        CopyServerAddress
                                        CopySourceName
                                        CopyDestinationName (opt)
                                        CopyRemoteUserName (opt)
                                        CopyNotifyOnCompletion (opt)
                copyFromFlash           CopyProtocol
                                        CopyServerAddress
                                        CopySourceName
                                        CopyDestinationName (opt)
                                        CopyRemoteUserName (opt)
                                        CopyNotifyOnCompletion (opt)
                copyFromFlhLog          CopyProtocol
                                        CopyServerAddress
                                        CopyDestinationName
                                        CopyNotifyOnCompletion (opt)

                """

                COPYTOFLASHWITHERASE = 1

                COPYTOFLASHWITHOUTERASE = 2

                COPYFROMFLASH = 3

                COPYFROMFLHLOG = 4


                @staticmethod
                def _meta_info():
                    from ydk.models.flash._meta import _CISCO_FLASH_MIB as meta
                    return meta._meta_table['CISCOFLASHMIB.CiscoFlashCopyTable.CiscoFlashCopyEntry.CiscoFlashCopyCommand_Enum']


            class CiscoFlashCopyProtocol_Enum(Enum):
                """
                CiscoFlashCopyProtocol_Enum

                The protocol to be used for any copy. Optional.
                Will default to tftp if not specified.
                
                Since feature support depends on a software release,
                version number within the release, platform, and
                maybe the image type (subset type), a management
                station would be expected to somehow determine
                the protocol support for a command.

                """

                TFTP = 1

                RCP = 2

                LEX = 3

                FTP = 4

                SCP = 5

                SFTP = 6


                @staticmethod
                def _meta_info():
                    from ydk.models.flash._meta import _CISCO_FLASH_MIB as meta
                    return meta._meta_table['CISCOFLASHMIB.CiscoFlashCopyTable.CiscoFlashCopyEntry.CiscoFlashCopyProtocol_Enum']


            class CiscoFlashCopyStatus_Enum(Enum):
                """
                CiscoFlashCopyStatus_Enum

                The status of the specified copy operation.
                
                copyOperationPending \:
                        operation request is received and
                        pending for validation and process
                
                copyInProgress \:
                        specified operation is active
                
                copyOperationSuccess \:
                        specified operation is supported and
                        completed successfully
                
                copyInvalidOperation \:
                        command invalid or command\-protocol\-device
                        combination unsupported
                
                copyInvalidProtocol \:
                        invalid protocol specified
                
                copyInvalidSourceName \:
                        invalid source file name specified
                        For the  copy from flash to lex operation, this
                        error code will be returned when the source file
                        is not a valid lex image.
                
                copyInvalidDestName \:
                        invalid target name (file or partition or
                        device name) specified
                        For the  copy from flash to lex operation, this
                        error code will be returned when no lex devices
                        are connected to the router or when an invalid
                        lex interface number has been specified in
                        the destination string.
                
                copyInvalidServerAddress \:
                        invalid server address specified
                
                copyDeviceBusy \:
                        specified device is in use and locked by
                        another process
                
                copyDeviceOpenError \:
                        invalid device name
                
                copyDeviceError \:
                        device read, write or erase error
                
                copyDeviceNotProgrammable \:
                        device is read\-only but a write or erase
                        operation was specified
                
                copyDeviceFull \:
                        device is filled to capacity
                
                copyFileOpenError \:
                        invalid file name; file not found in partition
                
                copyFileTransferError \:
                        file transfer was unsuccessfull; network failure
                
                copyFileChecksumError \:
                        file checksum in Flash failed
                
                copyNoMemory \:
                        system running low on memory
                
                copyUnknownFailure \:
                        failure unknown
                
                copyProhibited\:
                      stop user from overwriting current boot image file.

                """

                COPYOPERATIONPENDING = 0

                COPYINPROGRESS = 1

                COPYOPERATIONSUCCESS = 2

                COPYINVALIDOPERATION = 3

                COPYINVALIDPROTOCOL = 4

                COPYINVALIDSOURCENAME = 5

                COPYINVALIDDESTNAME = 6

                COPYINVALIDSERVERADDRESS = 7

                COPYDEVICEBUSY = 8

                COPYDEVICEOPENERROR = 9

                COPYDEVICEERROR = 10

                COPYDEVICENOTPROGRAMMABLE = 11

                COPYDEVICEFULL = 12

                COPYFILEOPENERROR = 13

                COPYFILETRANSFERERROR = 14

                COPYFILECHECKSUMERROR = 15

                COPYNOMEMORY = 16

                COPYUNKNOWNFAILURE = 17

                COPYINVALIDSIGNATURE = 18

                COPYPROHIBITED = 19


                @staticmethod
                def _meta_info():
                    from ydk.models.flash._meta import _CISCO_FLASH_MIB as meta
                    return meta._meta_table['CISCOFLASHMIB.CiscoFlashCopyTable.CiscoFlashCopyEntry.CiscoFlashCopyStatus_Enum']


            @property
            def _common_path(self):
                if self.ciscoflashcopyserialnumber is None:
                    raise YPYDataValidationError('Key property ciscoflashcopyserialnumber is None')

                return '/CISCO-FLASH-MIB:CISCO-FLASH-MIB/CISCO-FLASH-MIB:ciscoFlashCopyTable/CISCO-FLASH-MIB:ciscoFlashCopyEntry[CISCO-FLASH-MIB:ciscoFlashCopySerialNumber = ' + str(self.ciscoflashcopyserialnumber) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.ciscoflashcopyserialnumber is not None:
                    return True

                if self.ciscoflashcopycommand is not None:
                    return True

                if self.ciscoflashcopydestinationname is not None:
                    return True

                if self.ciscoflashcopyentrystatus is not None:
                    return True

                if self.ciscoflashcopynotifyoncompletion is not None:
                    return True

                if self.ciscoflashcopyprotocol is not None:
                    return True

                if self.ciscoflashcopyremotepassword is not None:
                    return True

                if self.ciscoflashcopyremoteusername is not None:
                    return True

                if self.ciscoflashcopyserveraddress is not None:
                    return True

                if self.ciscoflashcopyserveraddrrev1 is not None:
                    return True

                if self.ciscoflashcopyserveraddrtype is not None:
                    return True

                if self.ciscoflashcopysourcename is not None:
                    return True

                if self.ciscoflashcopystatus is not None:
                    return True

                if self.ciscoflashcopytime is not None:
                    return True

                if self.ciscoflashcopyverify is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.flash._meta import _CISCO_FLASH_MIB as meta
                return meta._meta_table['CISCOFLASHMIB.CiscoFlashCopyTable.CiscoFlashCopyEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-FLASH-MIB:CISCO-FLASH-MIB/CISCO-FLASH-MIB:ciscoFlashCopyTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.ciscoflashcopyentry is not None:
                for child_ref in self.ciscoflashcopyentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.flash._meta import _CISCO_FLASH_MIB as meta
            return meta._meta_table['CISCOFLASHMIB.CiscoFlashCopyTable']['meta_info']


    class CiscoFlashDevice(object):
        """
        
        
        .. attribute:: ciscoflashdevicessupported
        
        	Number of Flash devices supported by the system. If the system does not support any Flash devices, this MIB will not be loaded on that system. The value of this object will therefore be atleast 1
        	**type**\: int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'cisco-flash'
        _revision = '2013-08-06'

        def __init__(self):
            self.parent = None
            self.ciscoflashdevicessupported = None

        @property
        def _common_path(self):

            return '/CISCO-FLASH-MIB:CISCO-FLASH-MIB/CISCO-FLASH-MIB:ciscoFlashDevice'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.ciscoflashdevicessupported is not None:
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.flash._meta import _CISCO_FLASH_MIB as meta
            return meta._meta_table['CISCOFLASHMIB.CiscoFlashDevice']['meta_info']


    class CiscoFlashDeviceTable(object):
        """
        Table of Flash device properties for each initialized
        Flash device. Each Flash device installed in a system
        is detected, sized, and initialized when the system
        image boots up.
        For removable Flash devices, the device properties
        will be dynamically deleted and recreated as the
        device is removed and inserted. Note that in this
        case, the newly inserted device may not be the same as
        the earlier removed one. The ciscoFlashDeviceInitTime
        object is available for a management station to determine
        the time at which a device was initialized, and thereby
        detect the change of a removable device.
        A removable device that has not been installed will
        also have an entry in this table. This is to let a
        management station know about a removable device that
        has been removed. Since a removed device obviously
        cannot be sized and initialized, the table entry for
        such a device will have
        ciscoFlashDeviceSize equal to zero,
        and the following objects will have
        an indeterminate value\:
                ciscoFlashDeviceMinPartitionSize,
                ciscoFlashDeviceMaxPartitions,
                ciscoFlashDevicePartitions, and
                ciscoFlashDeviceChipCount.
        ciscoFlashDeviceRemovable will be
        true to indicate it is removable.
        
        .. attribute:: ciscoflashdeviceentry
        
        	An entry in the table of flash device properties for each initialized flash device. Each entry can be randomly accessed by using ciscoFlashDeviceIndex as an index into the table. Note that removable devices will have an entry in the table even when they have been removed. However, a non\-removable device that has not been installed will not have an entry in the table
        	**type**\: list of :py:class:`CiscoFlashDeviceEntry <ydk.models.flash.CISCO_FLASH_MIB.CISCOFLASHMIB.CiscoFlashDeviceTable.CiscoFlashDeviceEntry>`
        
        

        """

        _prefix = 'cisco-flash'
        _revision = '2013-08-06'

        def __init__(self):
            self.parent = None
            self.ciscoflashdeviceentry = YList()
            self.ciscoflashdeviceentry.parent = self
            self.ciscoflashdeviceentry.name = 'ciscoflashdeviceentry'


        class CiscoFlashDeviceEntry(object):
            """
            An entry in the table of flash device properties for
            each initialized flash device.
            Each entry can be randomly accessed by using
            ciscoFlashDeviceIndex as an index into the table.
            Note that removable devices will have an entry in
            the table even when they have been removed. However,
            a non\-removable device that has not been installed
            will not have an entry in the table.
            
            .. attribute:: ciscoflashdeviceindex
            
            	Flash device sequence number to index within the table of initialized flash devices. The lowest value should be 1. The highest should be less than or equal to the value of the ciscoFlashDevicesSupported object
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: ciscoflashdevicecard
            
            	This object will point to an instance of a card entry in the cardTable. The card entry will give details about the card on which the Flash device is actually located. For most systems, this is usually the main processor board. On the AGS+ systems, Flash is located on a separate multibus card such as the MC. This object will therefore be used to essentially index into cardTable to retrieve details about the card such as cardDescr, cardSlotNumber, etc
            	**type**\: str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: ciscoflashdevicechipcount
            
            	Total number of chips within the Flash device. The purpose of this object is to provide information upfront to a management station on how much chip info to expect and possibly help double check the chip index against an upper limit when randomly retrieving chip info for a partition
            	**type**\: int
            
            	**range:** 1..64
            
            .. attribute:: ciscoflashdevicecontroller
            
            	Flash device controller. The h/w card that actually controls Flash read/write/erase. Relevant for the AGS+ systems where Flash may be controlled by the MC+, STR or the ENVM cards, cards that may not actually contain the Flash chips. For systems that have removable PCMCIA flash cards that are controlled by a PCMCIA controller chip, this object may contain a description of that controller chip. Where irrelevant (Flash is a direct memory mapped device accessed directly by the main processor), this object will have an empty (NULL) string
            	**type**\: str
            
            	**range:** 0..64
            
            .. attribute:: ciscoflashdevicedescr
            
            	Description of a Flash device. The description is meant to explain what the Flash device and its purpose is. Current values are\:   System flash \- for the primary Flash used to store full                  system images.   Boot flash   \- for the secondary Flash used to store                  bootstrap images. The ciscoFlashDeviceDescr, ciscoFlashDeviceController (if applicable), and ciscoFlashPhyEntIndex objects are expected to collectively give all information about a Flash device. The device description will always be available for a removable device, even when the device has been removed
            	**type**\: str
            
            	**range:** 0..64
            
            .. attribute:: ciscoflashdeviceinittime
            
            	System time at which device was initialized. For fixed devices, this will be the system time at boot up. For removable devices, it will be the time at which the device was inserted, which may be boot up time, or a later time (if device was inserted later). If a device (fixed or removable) was repartitioned, it will be the time of repartitioning. The purpose of this object is to help a management station determine if a removable device has been changed. The application should retrieve this object prior to any operation and compare with the previously retrieved value. Note that this time will not be real time but a running time maintained by the system. This running time starts from zero when the system boots up. For a removable device that has been removed, this value will be zero
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ciscoflashdevicemaxpartitions
            
            	Max number of partitions supported by the system for this Flash device. Default will be 1, which actually means that partitioning is not supported. Note that this value will be defined by system limitations, not by the flash device itself (for eg., the system may impose a limit of 2 partitions even though the device may be large enough to be partitioned into 4 based on the smallest partition unit supported). On systems that execute code out of Flash, partitioning is a way of creating multiple file systems in the Flash device so that writing into or erasing of one file system can be done while executing code residing in another file system. For systems executing code out of DRAM, partitioning gives a way of sub\-dividing a large Flash device for easier management of files
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ciscoflashdeviceminpartitionsize
            
            	This object will give the minimum partition size supported for this device. For systems that execute code directly out of Flash, the minimum partition size needs to be the bank size. (Bank size is equal to the size of a chip multiplied by the width of the device. In most cases, the device width is 4 bytes, and so the bank size would be four times the size of a chip). This has to be so because all programming commands affect the operation of an entire chip (in our case, an entire bank because all operations are done on the entire width of the device) even though the actual command may be localized to a small portion of each chip. So when executing code out of Flash, one needs to be able to write and erase some portion of Flash without affecting the code execution. For systems that execute code out of DRAM or ROM, it is possible to partition Flash with a finer granularity (for eg., at erase sector boundaries) if the system code supports such granularity.  This object will let a management entity know the minimum partition size as defined by the system. If the system does not support partitioning, the value will be equal to the device size in ciscoFlashDeviceSize. The maximum number of partitions that could be configured will be equal to the minimum of ciscoFlashDeviceMaxPartitions and (ciscoFlashDeviceSize / ciscoFlashDeviceMinPartitionSize).  If the total size of the flash device is greater than the maximum value reportable by this object then this object should report its maximum value(4,294,967,295) and ciscoFlashDeviceMinPartitionSizeExtended must be used to report the flash device's minimum partition size
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: ciscoflashdeviceminpartitionsizeextended
            
            	This object provides the minimum partition size supported for this device. This object is a 64\-bit version of  ciscoFlashDeviceMinPatitionSize
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: ciscoflashdevicename
            
            	Flash device name. This name is used to refer to the device within the system. Flash operations get directed to a device based on this name. The system has a concept of a default device. This would be the primary or most used device in case of multiple devices. The system directs an operation to the default device whenever a device name is not specified. The device name is therefore mandatory except when the operation is being done on the default device, or, the system supports only a single Flash device. The device name will always be available for a removable device, even when the device has been removed
            	**type**\: str
            
            	**range:** 0..16
            
            .. attribute:: ciscoflashdevicenameextended
            
            	Extended Flash device name whose size can be upto 255 characters. This name is used to refer to the device within the system. Flash operations get directed to a device based on this name. The system has a concept of a default device. This would be the primary or most used device in case of multiple devices. The system directs an operation to the default device whenever a device name is not specified. The device name is therefore mandatory except when the operation is being done on the default device, or, the system supports only a single Flash device. The device name will always be available for a removable device, even when the device has been removed
            	**type**\: str
            
            	**range:** 0..255
            
            .. attribute:: ciscoflashdevicepartitions
            
            	Flash device partitions actually present. Number of partitions cannot exceed the minimum of ciscoFlashDeviceMaxPartitions and (ciscoFlashDeviceSize / ciscoFlashDeviceMinPartitionSize). Will be equal to at least 1, the case where the partition spans the entire device (actually no partitioning). A partition will contain one or more minimum partition units (where a minimum partition unit is defined by ciscoFlashDeviceMinPartitionSize)
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: ciscoflashdeviceprogrammingjumper
            
            	This object gives the state of a jumper (if present and can be determined) that controls the programming voltage called Vpp to the Flash device. Vpp is required for programming (erasing and writing) Flash. For certain older technology chips it is also required for identifying the chips (which in turn is required to identify which programming algorithms to use; different chips require different algorithms and commands). The purpose of the jumper, on systems where it is available, is to write protect a Flash device. On most of the newer remote access routers, this jumper is unavailable since users are not expected to visit remote sites just to install and remove the jumpers when upgrading software in the Flash device. The unknown(3) value will be returned for such systems and can be interpreted to mean that a programming jumper is not present or not required on those systems. On systems where the programming jumper state can be read back via a hardware register, the installed(1) or notInstalled(2) value will be returned. This object is expected to be used in conjunction with the ciscoFlashPartitionStatus object whenever that object has the readOnly(1) value. In such a case, this object will indicate whether the programming jumper is a possible reason for the readOnly state
            	**type**\: :py:class:`CiscoFlashDeviceProgrammingJumper_Enum <ydk.models.flash.CISCO_FLASH_MIB.CISCOFLASHMIB.CiscoFlashDeviceTable.CiscoFlashDeviceEntry.CiscoFlashDeviceProgrammingJumper_Enum>`
            
            .. attribute:: ciscoflashdeviceremovable
            
            	Whether Flash device is removable. Generally, only PCMCIA Flash cards will be treated as removable. Socketed Flash chips and Flash SIMM modules will not be treated as removable. Simply put, only those Flash devices that can be inserted or removed without opening the hardware casing will be considered removable. Further, removable Flash devices are expected to have the necessary hardware support \-   1. on\-line removal and insertion   2. interrupt generation on removal or insertion
            	**type**\: bool
            
            .. attribute:: ciscoflashdevicesize
            
            	Total size of the Flash device. For a removable device, the size will be zero if the device has been removed.  If the total size of the flash device is greater than the maximum value reportable by this object then this object should report its maximum value(4,294,967,295) and ciscoFlashDeviceSizeExtended must be used to report the flash device's size
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: ciscoflashdevicesizeextended
            
            	Total size of the Flash device. For a removable device, the size will be zero if the device has been removed.  This object is a 64\-bit version of ciscoFlashDeviceSize
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: ciscoflashphyentindex
            
            	This object indicates the physical entity index of a physical entity in entPhysicalTable which the flash device actually located
            	**type**\: int
            
            	**range:** 1..2147483647
            
            

            """

            _prefix = 'cisco-flash'
            _revision = '2013-08-06'

            def __init__(self):
                self.parent = None
                self.ciscoflashdeviceindex = None
                self.ciscoflashdevicecard = None
                self.ciscoflashdevicechipcount = None
                self.ciscoflashdevicecontroller = None
                self.ciscoflashdevicedescr = None
                self.ciscoflashdeviceinittime = None
                self.ciscoflashdevicemaxpartitions = None
                self.ciscoflashdeviceminpartitionsize = None
                self.ciscoflashdeviceminpartitionsizeextended = None
                self.ciscoflashdevicename = None
                self.ciscoflashdevicenameextended = None
                self.ciscoflashdevicepartitions = None
                self.ciscoflashdeviceprogrammingjumper = None
                self.ciscoflashdeviceremovable = None
                self.ciscoflashdevicesize = None
                self.ciscoflashdevicesizeextended = None
                self.ciscoflashphyentindex = None

            class CiscoFlashDeviceProgrammingJumper_Enum(Enum):
                """
                CiscoFlashDeviceProgrammingJumper_Enum

                This object gives the state of a jumper (if present and can be
                determined) that controls the programming voltage called Vpp
                to the Flash device. Vpp is required for programming (erasing
                and writing) Flash. For certain older technology chips it is
                also required for identifying the chips (which in turn is
                required to identify which programming algorithms to use;
                different chips require different algorithms and commands).
                The purpose of the jumper, on systems where it is available,
                is to write protect a Flash device.
                On most of the newer remote access routers, this jumper is
                unavailable since users are not expected to visit remote sites
                just to install and remove the jumpers when upgrading software
                in the Flash device. The unknown(3) value will be returned for
                such systems and can be interpreted to mean that a programming
                jumper is not present or not required on those systems.
                On systems where the programming jumper state can be read back
                via a hardware register, the installed(1) or notInstalled(2)
                value will be returned.
                This object is expected to be used in conjunction with the
                ciscoFlashPartitionStatus object whenever that object has
                the readOnly(1) value. In such a case, this object will
                indicate whether the programming jumper is a possible reason
                for the readOnly state.

                """

                INSTALLED = 1

                NOTINSTALLED = 2

                UNKNOWN = 3


                @staticmethod
                def _meta_info():
                    from ydk.models.flash._meta import _CISCO_FLASH_MIB as meta
                    return meta._meta_table['CISCOFLASHMIB.CiscoFlashDeviceTable.CiscoFlashDeviceEntry.CiscoFlashDeviceProgrammingJumper_Enum']


            @property
            def _common_path(self):
                if self.ciscoflashdeviceindex is None:
                    raise YPYDataValidationError('Key property ciscoflashdeviceindex is None')

                return '/CISCO-FLASH-MIB:CISCO-FLASH-MIB/CISCO-FLASH-MIB:ciscoFlashDeviceTable/CISCO-FLASH-MIB:ciscoFlashDeviceEntry[CISCO-FLASH-MIB:ciscoFlashDeviceIndex = ' + str(self.ciscoflashdeviceindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.ciscoflashdeviceindex is not None:
                    return True

                if self.ciscoflashdevicecard is not None:
                    return True

                if self.ciscoflashdevicechipcount is not None:
                    return True

                if self.ciscoflashdevicecontroller is not None:
                    return True

                if self.ciscoflashdevicedescr is not None:
                    return True

                if self.ciscoflashdeviceinittime is not None:
                    return True

                if self.ciscoflashdevicemaxpartitions is not None:
                    return True

                if self.ciscoflashdeviceminpartitionsize is not None:
                    return True

                if self.ciscoflashdeviceminpartitionsizeextended is not None:
                    return True

                if self.ciscoflashdevicename is not None:
                    return True

                if self.ciscoflashdevicenameextended is not None:
                    return True

                if self.ciscoflashdevicepartitions is not None:
                    return True

                if self.ciscoflashdeviceprogrammingjumper is not None:
                    return True

                if self.ciscoflashdeviceremovable is not None:
                    return True

                if self.ciscoflashdevicesize is not None:
                    return True

                if self.ciscoflashdevicesizeextended is not None:
                    return True

                if self.ciscoflashphyentindex is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.flash._meta import _CISCO_FLASH_MIB as meta
                return meta._meta_table['CISCOFLASHMIB.CiscoFlashDeviceTable.CiscoFlashDeviceEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-FLASH-MIB:CISCO-FLASH-MIB/CISCO-FLASH-MIB:ciscoFlashDeviceTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.ciscoflashdeviceentry is not None:
                for child_ref in self.ciscoflashdeviceentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.flash._meta import _CISCO_FLASH_MIB as meta
            return meta._meta_table['CISCOFLASHMIB.CiscoFlashDeviceTable']['meta_info']


    class CiscoFlashFileByTypeTable(object):
        """
        Table of information for files on the manageable
        flash devices sorted by File Types.
        
        .. attribute:: ciscoflashfilebytypeentry
        
        	An entry in the table of Flash file properties for each initialized Flash partition. Each entry represents a file sorted by file type.  This table contains exactly the same set of rows as are contained in the ciscoFlashFileTable but in a different order, i.e., ordered by  the type of file, given by  ciscoFlashFileType; the device number, given by ciscoFlashDeviceIndex; the partition number within the device, given by ciscoFlashPartitionIndex; the file number within the partition, given by ciscoFlashFileIndex
        	**type**\: list of :py:class:`CiscoFlashFileByTypeEntry <ydk.models.flash.CISCO_FLASH_MIB.CISCOFLASHMIB.CiscoFlashFileByTypeTable.CiscoFlashFileByTypeEntry>`
        
        

        """

        _prefix = 'cisco-flash'
        _revision = '2013-08-06'

        def __init__(self):
            self.parent = None
            self.ciscoflashfilebytypeentry = YList()
            self.ciscoflashfilebytypeentry.parent = self
            self.ciscoflashfilebytypeentry.name = 'ciscoflashfilebytypeentry'


        class CiscoFlashFileByTypeEntry(object):
            """
            An entry in the table of Flash file properties
            for each initialized Flash partition. Each entry
            represents a file sorted by file type.
            
            This table contains exactly the same set of rows
            as are contained in the ciscoFlashFileTable but
            in a different order, i.e., ordered by
            
            the type of file, given by  ciscoFlashFileType;
            the device number, given by ciscoFlashDeviceIndex;
            the partition number within the device, given by
            ciscoFlashPartitionIndex;
            the file number within the partition, given by
            ciscoFlashFileIndex.
            
            .. attribute:: ciscoflashdeviceindex
            
            	
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: ciscoflashfileindex
            
            	
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: ciscoflashfiletype
            
            	
            	**type**\: :py:class:`FlashFileType_Enum <ydk.models.flash.CISCO_FLASH_MIB.FlashFileType_Enum>`
            
            .. attribute:: ciscoflashpartitionindex
            
            	
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: ciscoflashfilebytypechecksum
            
            	This object represents exactly the same info as ciscoFlashFileChecksum object in ciscoFlashFileTable
            	**type**\: str
            
            .. attribute:: ciscoflashfilebytypedate
            
            	This object represents exactly the same info as ciscoFlashFileDate object in ciscoFlashFileTable
            	**type**\: str
            
            .. attribute:: ciscoflashfilebytypename
            
            	This object represents exactly the same info as ciscoFlashFileName object in ciscoFlashFileTable
            	**type**\: str
            
            	**range:** 1..255
            
            .. attribute:: ciscoflashfilebytypesize
            
            	This object represents exactly the same info as ciscoFlashFileSize object in ciscoFlashFileTable
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ciscoflashfilebytypestatus
            
            	This object represents exactly the same info as ciscoFlashFileStatus object in ciscoFlashFileTable
            	**type**\: :py:class:`CiscoFlashFileByTypeStatus_Enum <ydk.models.flash.CISCO_FLASH_MIB.CISCOFLASHMIB.CiscoFlashFileByTypeTable.CiscoFlashFileByTypeEntry.CiscoFlashFileByTypeStatus_Enum>`
            
            

            """

            _prefix = 'cisco-flash'
            _revision = '2013-08-06'

            def __init__(self):
                self.parent = None
                self.ciscoflashdeviceindex = None
                self.ciscoflashfileindex = None
                self.ciscoflashfiletype = None
                self.ciscoflashpartitionindex = None
                self.ciscoflashfilebytypechecksum = None
                self.ciscoflashfilebytypedate = None
                self.ciscoflashfilebytypename = None
                self.ciscoflashfilebytypesize = None
                self.ciscoflashfilebytypestatus = None

            class CiscoFlashFileByTypeStatus_Enum(Enum):
                """
                CiscoFlashFileByTypeStatus_Enum

                This object represents exactly the
                same info as ciscoFlashFileStatus
                object in ciscoFlashFileTable.

                """

                DELETED = 1

                INVALIDCHECKSUM = 2

                VALID = 3


                @staticmethod
                def _meta_info():
                    from ydk.models.flash._meta import _CISCO_FLASH_MIB as meta
                    return meta._meta_table['CISCOFLASHMIB.CiscoFlashFileByTypeTable.CiscoFlashFileByTypeEntry.CiscoFlashFileByTypeStatus_Enum']


            @property
            def _common_path(self):
                if self.ciscoflashdeviceindex is None:
                    raise YPYDataValidationError('Key property ciscoflashdeviceindex is None')
                if self.ciscoflashfileindex is None:
                    raise YPYDataValidationError('Key property ciscoflashfileindex is None')
                if self.ciscoflashfiletype is None:
                    raise YPYDataValidationError('Key property ciscoflashfiletype is None')
                if self.ciscoflashpartitionindex is None:
                    raise YPYDataValidationError('Key property ciscoflashpartitionindex is None')

                return '/CISCO-FLASH-MIB:CISCO-FLASH-MIB/CISCO-FLASH-MIB:ciscoFlashFileByTypeTable/CISCO-FLASH-MIB:ciscoFlashFileByTypeEntry[CISCO-FLASH-MIB:ciscoFlashDeviceIndex = ' + str(self.ciscoflashdeviceindex) + '][CISCO-FLASH-MIB:ciscoFlashFileIndex = ' + str(self.ciscoflashfileindex) + '][CISCO-FLASH-MIB:ciscoFlashFileType = ' + str(self.ciscoflashfiletype) + '][CISCO-FLASH-MIB:ciscoFlashPartitionIndex = ' + str(self.ciscoflashpartitionindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.ciscoflashdeviceindex is not None:
                    return True

                if self.ciscoflashfileindex is not None:
                    return True

                if self.ciscoflashfiletype is not None:
                    return True

                if self.ciscoflashpartitionindex is not None:
                    return True

                if self.ciscoflashfilebytypechecksum is not None:
                    return True

                if self.ciscoflashfilebytypedate is not None:
                    return True

                if self.ciscoflashfilebytypename is not None:
                    return True

                if self.ciscoflashfilebytypesize is not None:
                    return True

                if self.ciscoflashfilebytypestatus is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.flash._meta import _CISCO_FLASH_MIB as meta
                return meta._meta_table['CISCOFLASHMIB.CiscoFlashFileByTypeTable.CiscoFlashFileByTypeEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-FLASH-MIB:CISCO-FLASH-MIB/CISCO-FLASH-MIB:ciscoFlashFileByTypeTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.ciscoflashfilebytypeentry is not None:
                for child_ref in self.ciscoflashfilebytypeentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.flash._meta import _CISCO_FLASH_MIB as meta
            return meta._meta_table['CISCOFLASHMIB.CiscoFlashFileByTypeTable']['meta_info']


    class CiscoFlashFileTable(object):
        """
        Table of information for files in a Flash partition.
        
        .. attribute:: ciscoflashfileentry
        
        	An entry in the table of Flash file properties for each initialized Flash partition. Each entry represents a file and gives details about the file. An entry is indexed using the device number, partition number within the device, and file number within the partition
        	**type**\: list of :py:class:`CiscoFlashFileEntry <ydk.models.flash.CISCO_FLASH_MIB.CISCOFLASHMIB.CiscoFlashFileTable.CiscoFlashFileEntry>`
        
        

        """

        _prefix = 'cisco-flash'
        _revision = '2013-08-06'

        def __init__(self):
            self.parent = None
            self.ciscoflashfileentry = YList()
            self.ciscoflashfileentry.parent = self
            self.ciscoflashfileentry.name = 'ciscoflashfileentry'


        class CiscoFlashFileEntry(object):
            """
            An entry in the table of Flash file properties
            for each initialized Flash partition. Each entry
            represents a file and gives details about the file.
            An entry is indexed using the device number,
            partition number within the device, and file
            number within the partition.
            
            .. attribute:: ciscoflashdeviceindex
            
            	
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: ciscoflashfileindex
            
            	Flash file sequence number used to index within a Flash partition directory table
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: ciscoflashpartitionindex
            
            	
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: ciscoflashfilechecksum
            
            	File checksum stored in the file header. This checksum is computed and stored when the file is written into Flash. It serves to validate the data written into Flash. Whereas the system will generate and store the checksum internally in hexadecimal form, this object will provide the checksum in a string form. The checksum will be available for all valid and invalid\-checksum files
            	**type**\: str
            
            .. attribute:: ciscoflashfiledate
            
            	The time at which this file was created
            	**type**\: str
            
            .. attribute:: ciscoflashfilename
            
            	Flash file name as specified by the user copying in the file. The name should not include the colon (\:) character as it is a special separator character used to delineate the device name, partition name, and the file name
            	**type**\: str
            
            	**range:** 1..255
            
            .. attribute:: ciscoflashfilesize
            
            	Size of the file in bytes. Note that this size does not include the size of the filesystem file header. File size will always be non\-zero
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ciscoflashfilestatus
            
            	Status of a file. A file could be explicitly deleted if the file system supports such a user command facility. Alternately, an existing good file would be automatically deleted if another good file with the same name were copied in. Note that deleted files continue to occupy prime Flash real estate.  A file is marked as having an invalid checksum if any checksum mismatch was detected while writing or reading the file. Incomplete files (files truncated either because of lack of free space, or a network download failure) are also written with a bad checksum and marked as invalid
            	**type**\: :py:class:`CiscoFlashFileStatus_Enum <ydk.models.flash.CISCO_FLASH_MIB.CISCOFLASHMIB.CiscoFlashFileTable.CiscoFlashFileEntry.CiscoFlashFileStatus_Enum>`
            
            .. attribute:: ciscoflashfiletype
            
            	Type of the file
            	**type**\: :py:class:`FlashFileType_Enum <ydk.models.flash.CISCO_FLASH_MIB.FlashFileType_Enum>`
            
            

            """

            _prefix = 'cisco-flash'
            _revision = '2013-08-06'

            def __init__(self):
                self.parent = None
                self.ciscoflashdeviceindex = None
                self.ciscoflashfileindex = None
                self.ciscoflashpartitionindex = None
                self.ciscoflashfilechecksum = None
                self.ciscoflashfiledate = None
                self.ciscoflashfilename = None
                self.ciscoflashfilesize = None
                self.ciscoflashfilestatus = None
                self.ciscoflashfiletype = None

            class CiscoFlashFileStatus_Enum(Enum):
                """
                CiscoFlashFileStatus_Enum

                Status of a file.
                A file could be explicitly deleted if the file system
                supports such a user command facility. Alternately,
                an existing good file would be automatically deleted
                if another good file with the same name were copied in.
                Note that deleted files continue to occupy prime
                Flash real estate.
                
                A file is marked as having an invalid checksum if any
                checksum mismatch was detected while writing or reading
                the file. Incomplete files (files truncated either
                because of lack of free space, or a network download
                failure) are also written with a bad checksum and
                marked as invalid.

                """

                DELETED = 1

                INVALIDCHECKSUM = 2

                VALID = 3


                @staticmethod
                def _meta_info():
                    from ydk.models.flash._meta import _CISCO_FLASH_MIB as meta
                    return meta._meta_table['CISCOFLASHMIB.CiscoFlashFileTable.CiscoFlashFileEntry.CiscoFlashFileStatus_Enum']


            @property
            def _common_path(self):
                if self.ciscoflashdeviceindex is None:
                    raise YPYDataValidationError('Key property ciscoflashdeviceindex is None')
                if self.ciscoflashfileindex is None:
                    raise YPYDataValidationError('Key property ciscoflashfileindex is None')
                if self.ciscoflashpartitionindex is None:
                    raise YPYDataValidationError('Key property ciscoflashpartitionindex is None')

                return '/CISCO-FLASH-MIB:CISCO-FLASH-MIB/CISCO-FLASH-MIB:ciscoFlashFileTable/CISCO-FLASH-MIB:ciscoFlashFileEntry[CISCO-FLASH-MIB:ciscoFlashDeviceIndex = ' + str(self.ciscoflashdeviceindex) + '][CISCO-FLASH-MIB:ciscoFlashFileIndex = ' + str(self.ciscoflashfileindex) + '][CISCO-FLASH-MIB:ciscoFlashPartitionIndex = ' + str(self.ciscoflashpartitionindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.ciscoflashdeviceindex is not None:
                    return True

                if self.ciscoflashfileindex is not None:
                    return True

                if self.ciscoflashpartitionindex is not None:
                    return True

                if self.ciscoflashfilechecksum is not None:
                    return True

                if self.ciscoflashfiledate is not None:
                    return True

                if self.ciscoflashfilename is not None:
                    return True

                if self.ciscoflashfilesize is not None:
                    return True

                if self.ciscoflashfilestatus is not None:
                    return True

                if self.ciscoflashfiletype is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.flash._meta import _CISCO_FLASH_MIB as meta
                return meta._meta_table['CISCOFLASHMIB.CiscoFlashFileTable.CiscoFlashFileEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-FLASH-MIB:CISCO-FLASH-MIB/CISCO-FLASH-MIB:ciscoFlashFileTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.ciscoflashfileentry is not None:
                for child_ref in self.ciscoflashfileentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.flash._meta import _CISCO_FLASH_MIB as meta
            return meta._meta_table['CISCOFLASHMIB.CiscoFlashFileTable']['meta_info']


    class CiscoFlashMiscOpTable(object):
        """
        A table of misc Flash operation entries. Each
        entry represents a Flash operation that
        has been initiated.
        
        .. attribute:: ciscoflashmiscopentry
        
        	A Flash operation entry. Each entry consists of a command, a target, and any optional parameters.  A management station wishing to create an entry should first generate a pseudo\-random serial number to be used as the index to this sparse table.  The station should then create the associated instance of the row status object. It must also, either in the same or in successive PDUs, create the associated instance of the command and parameter objects. It should also modify the default values for any of the parameter objects if the defaults are not appropriate.  Once the appropriate instances of all the command objects have been created, either by an explicit SNMP set request or by default, the row status should be set to active to initiate the operation. Note that this entire procedure may be initiated via a single set request which specifies a row status of createAndGo as well as specifies valid values for the non\-defaulted parameter objects.  Once an operation has been activated, it cannot be stopped.  Once the operation completes, the management station should retrieve the value of the status object (and time if desired), and delete the entry.  In order to prevent old entries from clogging the table, entries will be aged out, but an entry will never be deleted within 5 minutes of completing
        	**type**\: list of :py:class:`CiscoFlashMiscOpEntry <ydk.models.flash.CISCO_FLASH_MIB.CISCOFLASHMIB.CiscoFlashMiscOpTable.CiscoFlashMiscOpEntry>`
        
        

        """

        _prefix = 'cisco-flash'
        _revision = '2013-08-06'

        def __init__(self):
            self.parent = None
            self.ciscoflashmiscopentry = YList()
            self.ciscoflashmiscopentry.parent = self
            self.ciscoflashmiscopentry.name = 'ciscoflashmiscopentry'


        class CiscoFlashMiscOpEntry(object):
            """
            A Flash operation entry. Each entry consists of a
            command, a target, and any optional parameters.
            
            A management station wishing to create an entry should
            first generate a pseudo\-random serial number to be used
            as the index to this sparse table.  The station should
            then create the associated instance of the row status
            object. It must also, either in the same or in successive
            PDUs, create the associated instance of the command and
            parameter objects. It should also modify the default values
            for any of the parameter objects if the defaults are not
            appropriate.
            
            Once the appropriate instances of all the command
            objects have been created, either by an explicit SNMP
            set request or by default, the row status should be set
            to active to initiate the operation. Note that this entire
            procedure may be initiated via a single set request which
            specifies a row status of createAndGo as well as specifies
            valid values for the non\-defaulted parameter objects.
            
            Once an operation has been activated, it cannot be
            stopped.
            
            Once the operation completes, the management station should
            retrieve the value of the status object (and time if
            desired), and delete the entry.  In order to prevent old
            entries from clogging the table, entries will be aged out,
            but an entry will never be deleted within 5 minutes of
            completing.
            
            .. attribute:: ciscoflashmiscopserialnumber
            
            	Object which specifies a unique entry in the table. A management station wishing to initiate a flash operation should use a pseudo\-random value for this object when creating or modifying an instance of a ciscoFlashMiscOpEntry
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: ciscoflashmiscopcommand
            
            	The command to be executed. Mandatory. Note that it is possible for a system to support multiple file systems (different file systems on different Flash devices, or different file systems on different partitions within a device). Each such file system may support only a subset of these commands. If a command is unsupported, the miscOpInvalidOperation(3) error will be reported in the operation status.  Command         Remarks erase           Erase flash. verify          Verify flash file checksum. delete          Delete a file. undelete        Revive a deleted file .                 Note that there are limits on                 the number of times a file can                 be deleted and undeleted. When                 this limit is exceeded, the                 system will return the appropriate                 error. squeeze         Recover space occupied by                 deleted files. This command                 preserves the good files, erases                 out the file system, then restores                 the preserved good files. format          Format a flash device.  Command table   Parameters erase           MiscOpDestinationName                 MiscOpNotifyOnCompletion (opt) verify          MiscOpDestinationName                 MiscOpNotifyOnCompletion (opt) delete          MiscOpDestinationName                 MiscOpNotifyOnCompletion (opt) undelete        MiscOpDestinationName                 MiscOpNotifyOnCompletion (opt) squeeze         MiscOpDestinationName                 MiscOpNotifyOnCompletion (opt) format          MiscOpDestinationName                 MiscOpNotifyOnCompletion (opt)
            	**type**\: :py:class:`CiscoFlashMiscOpCommand_Enum <ydk.models.flash.CISCO_FLASH_MIB.CISCOFLASHMIB.CiscoFlashMiscOpTable.CiscoFlashMiscOpEntry.CiscoFlashMiscOpCommand_Enum>`
            
            .. attribute:: ciscoflashmiscopdestinationname
            
            	Destination file, or partition name. File name must be of the form         [device>\:][<partition>\:]<file> where <device> is a value obtained from FlashDeviceName,       <partition> is obtained from FlashPartitionName   and <file> is the name of a file in Flash. While leading and/or trailing whitespaces are acceptable, no whitespaces are allowed within the path itself.  A management station could derive its own partition name as per the description for the ciscoFlashPartitionName object. If <device> is not specified, the default Flash device will be assumed. If <partition> is not specified, the default partition will be assumed. If a device is not partitioned into 2 or more partitions, this value may be left out.  For an operation on a partition, eg., the erase command, this object would specify the partition name in the form\:         [device>\:][<partition>\:]
            	**type**\: str
            
            	**range:** 0..255
            
            .. attribute:: ciscoflashmiscopentrystatus
            
            	The status of this table entry
            	**type**\: :py:class:`RowStatus_Enum <ydk.models.snmpv2.SNMPv2_TC.RowStatus_Enum>`
            
            .. attribute:: ciscoflashmiscopnotifyoncompletion
            
            	Specifies whether or not a notification should be generated on the completion of an operation. If specified, ciscoFlashMiscOpCompletionTrap will be generated. It is the responsibility of the management entity to ensure that the SNMP administrative model is configured in such a way as to allow the notification to be delivered
            	**type**\: bool
            
            .. attribute:: ciscoflashmiscopstatus
            
            	The status of the specified operation. miscOpInProgress \:         specified operation is active  miscOpOperationSuccess \:         specified operation is supported and completed         successfully  miscOpInvalidOperation \:         command invalid or command\-protocol\-device         combination unsupported  miscOpInvalidDestName \:         invalid target name (file or partition or         device name) specified  miscOpDeviceBusy \:         specified device is in use and locked by another         process  miscOpDeviceOpenError \:         invalid device name  miscOpDeviceError \:         device read, write or erase error  miscOpDeviceNotProgrammable \:         device is read\-only but a write or erase         operation was specified  miscOpFileOpenError \:         invalid file name; file not found in partition  miscOpFileDeleteFailure \:         file could not be deleted; delete count exceeded  miscOpFileUndeleteFailure \:         file could not be undeleted; undelete count         exceeded  miscOpFileChecksumError \:         file has a bad checksum  miscOpNoMemory \:         system running low on memory  miscOpUnknownFailure \:         failure unknown  miscOpSqueezeFailure \:         the squeeze operation failed  miscOpNoSuchFile \:         a valid but nonexistent file name was specified  miscOpFormatFailure \:         the format operation failed
            	**type**\: :py:class:`CiscoFlashMiscOpStatus_Enum <ydk.models.flash.CISCO_FLASH_MIB.CISCOFLASHMIB.CiscoFlashMiscOpTable.CiscoFlashMiscOpEntry.CiscoFlashMiscOpStatus_Enum>`
            
            .. attribute:: ciscoflashmiscoptime
            
            	Time taken for the operation. This object will be like a stopwatch, starting when the operation starts, stopping when the operation completes. If a management entity keeps a database of completion times for various operations, it can then use the stopwatch capability to display percentage completion time
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'cisco-flash'
            _revision = '2013-08-06'

            def __init__(self):
                self.parent = None
                self.ciscoflashmiscopserialnumber = None
                self.ciscoflashmiscopcommand = None
                self.ciscoflashmiscopdestinationname = None
                self.ciscoflashmiscopentrystatus = None
                self.ciscoflashmiscopnotifyoncompletion = None
                self.ciscoflashmiscopstatus = None
                self.ciscoflashmiscoptime = None

            class CiscoFlashMiscOpCommand_Enum(Enum):
                """
                CiscoFlashMiscOpCommand_Enum

                The command to be executed. Mandatory.
                Note that it is possible for a system to support
                multiple file systems (different file systems on
                different Flash devices, or different file systems
                on different partitions within a device). Each such
                file system may support only a subset of these commands.
                If a command is unsupported, the miscOpInvalidOperation(3)
                error will be reported in the operation status.
                
                Command         Remarks
                erase           Erase flash.
                verify          Verify flash file checksum.
                delete          Delete a file.
                undelete        Revive a deleted file .
                                Note that there are limits on
                                the number of times a file can
                                be deleted and undeleted. When
                                this limit is exceeded, the
                                system will return the appropriate
                                error.
                squeeze         Recover space occupied by
                                deleted files. This command
                                preserves the good files, erases
                                out the file system, then restores
                                the preserved good files.
                format          Format a flash device.
                
                Command table   Parameters
                erase           MiscOpDestinationName
                                MiscOpNotifyOnCompletion (opt)
                verify          MiscOpDestinationName
                                MiscOpNotifyOnCompletion (opt)
                delete          MiscOpDestinationName
                                MiscOpNotifyOnCompletion (opt)
                undelete        MiscOpDestinationName
                                MiscOpNotifyOnCompletion (opt)
                squeeze         MiscOpDestinationName
                                MiscOpNotifyOnCompletion (opt)
                format          MiscOpDestinationName
                                MiscOpNotifyOnCompletion (opt)

                """

                ERASE = 1

                VERIFY = 2

                DELETE = 3

                UNDELETE = 4

                SQUEEZE = 5

                FORMAT = 6


                @staticmethod
                def _meta_info():
                    from ydk.models.flash._meta import _CISCO_FLASH_MIB as meta
                    return meta._meta_table['CISCOFLASHMIB.CiscoFlashMiscOpTable.CiscoFlashMiscOpEntry.CiscoFlashMiscOpCommand_Enum']


            class CiscoFlashMiscOpStatus_Enum(Enum):
                """
                CiscoFlashMiscOpStatus_Enum

                The status of the specified operation.
                miscOpInProgress \:
                        specified operation is active
                
                miscOpOperationSuccess \:
                        specified operation is supported and completed
                        successfully
                
                miscOpInvalidOperation \:
                        command invalid or command\-protocol\-device
                        combination unsupported
                
                miscOpInvalidDestName \:
                        invalid target name (file or partition or
                        device name) specified
                
                miscOpDeviceBusy \:
                        specified device is in use and locked by another
                        process
                
                miscOpDeviceOpenError \:
                        invalid device name
                
                miscOpDeviceError \:
                        device read, write or erase error
                
                miscOpDeviceNotProgrammable \:
                        device is read\-only but a write or erase
                        operation was specified
                
                miscOpFileOpenError \:
                        invalid file name; file not found in partition
                
                miscOpFileDeleteFailure \:
                        file could not be deleted; delete count exceeded
                
                miscOpFileUndeleteFailure \:
                        file could not be undeleted; undelete count
                        exceeded
                
                miscOpFileChecksumError \:
                        file has a bad checksum
                
                miscOpNoMemory \:
                        system running low on memory
                
                miscOpUnknownFailure \:
                        failure unknown
                
                miscOpSqueezeFailure \:
                        the squeeze operation failed
                
                miscOpNoSuchFile \:
                        a valid but nonexistent file name was specified
                
                miscOpFormatFailure \:
                        the format operation failed

                """

                MISCOPINPROGRESS = 1

                MISCOPOPERATIONSUCCESS = 2

                MISCOPINVALIDOPERATION = 3

                MISCOPINVALIDDESTNAME = 4

                MISCOPDEVICEBUSY = 5

                MISCOPDEVICEOPENERROR = 6

                MISCOPDEVICEERROR = 7

                MISCOPDEVICENOTPROGRAMMABLE = 8

                MISCOPFILEOPENERROR = 9

                MISCOPFILEDELETEFAILURE = 10

                MISCOPFILEUNDELETEFAILURE = 11

                MISCOPFILECHECKSUMERROR = 12

                MISCOPNOMEMORY = 13

                MISCOPUNKNOWNFAILURE = 14

                MISCOPSQUEEZEFAILURE = 18

                MISCOPNOSUCHFILE = 19

                MISCOPFORMATFAILURE = 20


                @staticmethod
                def _meta_info():
                    from ydk.models.flash._meta import _CISCO_FLASH_MIB as meta
                    return meta._meta_table['CISCOFLASHMIB.CiscoFlashMiscOpTable.CiscoFlashMiscOpEntry.CiscoFlashMiscOpStatus_Enum']


            @property
            def _common_path(self):
                if self.ciscoflashmiscopserialnumber is None:
                    raise YPYDataValidationError('Key property ciscoflashmiscopserialnumber is None')

                return '/CISCO-FLASH-MIB:CISCO-FLASH-MIB/CISCO-FLASH-MIB:ciscoFlashMiscOpTable/CISCO-FLASH-MIB:ciscoFlashMiscOpEntry[CISCO-FLASH-MIB:ciscoFlashMiscOpSerialNumber = ' + str(self.ciscoflashmiscopserialnumber) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.ciscoflashmiscopserialnumber is not None:
                    return True

                if self.ciscoflashmiscopcommand is not None:
                    return True

                if self.ciscoflashmiscopdestinationname is not None:
                    return True

                if self.ciscoflashmiscopentrystatus is not None:
                    return True

                if self.ciscoflashmiscopnotifyoncompletion is not None:
                    return True

                if self.ciscoflashmiscopstatus is not None:
                    return True

                if self.ciscoflashmiscoptime is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.flash._meta import _CISCO_FLASH_MIB as meta
                return meta._meta_table['CISCOFLASHMIB.CiscoFlashMiscOpTable.CiscoFlashMiscOpEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-FLASH-MIB:CISCO-FLASH-MIB/CISCO-FLASH-MIB:ciscoFlashMiscOpTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.ciscoflashmiscopentry is not None:
                for child_ref in self.ciscoflashmiscopentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.flash._meta import _CISCO_FLASH_MIB as meta
            return meta._meta_table['CISCOFLASHMIB.CiscoFlashMiscOpTable']['meta_info']


    class CiscoFlashPartitionTable(object):
        """
        Table of flash device partition properties for each
        initialized flash partition. Whenever there is no
        explicit partitioning done, a single partition spanning
        the entire device will be assumed to exist. There will
        therefore always be atleast one partition on a device.
        
        .. attribute:: ciscoflashpartitionentry
        
        	An entry in the table of flash partition properties for each initialized flash partition. Each entry will be indexed by a device number and a partition number within the device
        	**type**\: list of :py:class:`CiscoFlashPartitionEntry <ydk.models.flash.CISCO_FLASH_MIB.CISCOFLASHMIB.CiscoFlashPartitionTable.CiscoFlashPartitionEntry>`
        
        

        """

        _prefix = 'cisco-flash'
        _revision = '2013-08-06'

        def __init__(self):
            self.parent = None
            self.ciscoflashpartitionentry = YList()
            self.ciscoflashpartitionentry.parent = self
            self.ciscoflashpartitionentry.name = 'ciscoflashpartitionentry'


        class CiscoFlashPartitionEntry(object):
            """
            An entry in the table of flash partition properties
            for each initialized flash partition. Each entry
            will be indexed by a device number and a partition
            number within the device.
            
            .. attribute:: ciscoflashdeviceindex
            
            	
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: ciscoflashpartitionindex
            
            	Flash partition sequence number used to index within table of initialized flash partitions
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: ciscoflashpartitionchecksumalgorithm
            
            	Checksum algorithm identifier for checksum method used by the file system. Normally, this would be fixed for a particular file system. When a file system writes a file to Flash, it checksums the data written. The checksum then serves as a way to validate the data read back whenever the file is opened for reading. Since there is no way, when using TFTP, to guarantee that a network download has been error free (since UDP checksums may not have been enabled), this object together with the ciscoFlashFileChecksum object provides a method for any management station to regenerate the checksum of the original file on the server and compare checksums to ensure that the file download to Flash was error free. simpleChecksum represents a simple 1s complement addition of short word values. Other algorithm values will be added as necessary
            	**type**\: :py:class:`CiscoFlashPartitionChecksumAlgorithm_Enum <ydk.models.flash.CISCO_FLASH_MIB.CISCOFLASHMIB.CiscoFlashPartitionTable.CiscoFlashPartitionEntry.CiscoFlashPartitionChecksumAlgorithm_Enum>`
            
            .. attribute:: ciscoflashpartitionendchip
            
            	Chip sequence number of last chip in partition. Used as an index into the chip table
            	**type**\: int
            
            	**range:** 1..64
            
            .. attribute:: ciscoflashpartitionfilecount
            
            	Count of all files in a flash partition. Both good and bad (deleted or invalid checksum) files will be included in this count
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ciscoflashpartitionfilenamelength
            
            	Maximum file name length supported by the file system. Max file name length will depend on the file system implemented. Today, all file systems support a max length of at least 48 bytes. A management entity must use this object when prompting a user for, or deriving the Flash file name length
            	**type**\: int
            
            	**range:** 1..256
            
            .. attribute:: ciscoflashpartitionfreespace
            
            	Free space within a Flash partition. Note that the actual size of a file in Flash includes a small overhead that represents the file system's file header. Certain file systems may also have a partition or device header overhead to be considered when computing the free space. Free space will be computed as total partition size less size of all existing files (valid/invalid/deleted files and including file header of each file), less size of any partition header, less size of header of next file to be copied in. In short, this object will give the size of the largest file that can be copied in. The management entity will not be expected to know or use any overheads such as file and partition header lengths, since such overheads may vary from file system to file system. Deleted files in Flash do not free up space. A partition may have to be erased in order to reclaim the space occupied by files.  If the free space within a flash partition is greater than the maximum value reportable by this object then this object should report its maximum value(4,294,967,295) and ciscoFlashPartitionFreeSpaceExtended must be used to report the flash partition's free space
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ciscoflashpartitionfreespaceextended
            
            	Free space within a Flash partition. Note that the actual size of a file in Flash includes a small overhead that represents the file system's file header. Certain file systems may also have a partition or device header overhead to be considered when computing the free space. Free space will be computed as total partition size less size of all existing files (valid/invalid/deleted files and including file header of each file), less size of any partition header, less size of header of next file to be copied in. In short, this object will give the size of the largest file that can be copied in. The management entity will not be expected to know or use any overheads such as file and partition header lengths, since such overheads may vary from file system to file system. Deleted files in Flash do not free up space. A partition may have to be erased in order to reclaim the space occupied by files.  This object is a 64\-bit version of ciscoFlashPartitionFreeSpace
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: ciscoflashpartitionlowspacenotifthreshold
            
            	This object specifies the minimum threshold value in percentage of free space for each partition. If the free space available goes below this threshold value and if ciscoFlashPartionLowSpaceNotifEnable is set to true, ciscoFlashPartitionLowSpaceNotif will be generated. When the available free space comes back to the threshold value ciscoFlashPartionLowSpaceRecoveryNotif will be generated
            	**type**\: int
            
            	**range:** 0..100
            
            .. attribute:: ciscoflashpartitionname
            
            	Flash partition name used to refer to a partition by the system. This can be any alpha\-numeric character string of the form AAAAAAAAnn, where A represents an optional alpha character and n a numeric character. Any numeric characters must always form the trailing part of the string. The system will strip off the alpha characters and use the numeric portion to map to a partition index. Flash operations get directed to a device partition based on this name. The system has a concept of a default partition. This would be the first partition in the device. The system directs an operation to the default partition whenever a partition name is not specified. The partition name is therefore mandatory except when the operation is being done on the default partition, or the device has just one partition (is not partitioned)
            	**type**\: str
            
            	**range:** 0..16
            
            .. attribute:: ciscoflashpartitionneederasure
            
            	This object indicates whether a partition requires erasure before any write operations can be done in it. A management station should therefore retrieve this object prior to attempting any write operation. A partition requires erasure after it becomes full free space left is less than or equal to the (filesystem file header size). A partition also requires erasure if the system does not find the existence of any file system when it boots up. The partition may be erased explicitly through the erase(5) command, or by using the copyToFlashWithErase(1) command. If a copyToFlashWithoutErase(2) command is issued when this object has the TRUE value, the command will fail
            	**type**\: bool
            
            .. attribute:: ciscoflashpartitionsize
            
            	Flash partition size. It should be an integral multiple of ciscoFlashDeviceMinPartitionSize. If there is a single partition, this size will be equal to ciscoFlashDeviceSize.  If the size of the flash partition is greater than the maximum value reportable by this object then this object should report its maximum value(4,294,967,295) and ciscoFlashPartitionSizeExtended must be used to report the flash partition's size
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: ciscoflashpartitionsizeextended
            
            	Flash partition size. It should be an integral multiple of ciscoFlashDeviceMinPartitionSize. If there is a single partition, this size will be equal to ciscoFlashDeviceSize.  This object is a 64\-bit version of ciscoFlashPartitionSize
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: ciscoflashpartitionstartchip
            
            	Chip sequence number of first chip in partition. Used as an index into the chip table
            	**type**\: int
            
            	**range:** 1..64
            
            .. attribute:: ciscoflashpartitionstatus
            
            	Flash partition status can be \:  \* readOnly if device is not programmable either because chips could not be recognized or an erroneous mismatch of chips was detected. Chip recognition may fail either because the chips are not supported by the system, or because the Vpp voltage required to identify chips has been disabled via the programming jumper. The ciscoFlashDeviceProgrammingJumper, ciscoFlashChipCode, and ciscoFlashChipDescr objects can be examined to get more details on the cause of this status \* runFromFlash (RFF) if current image is running from this partition. The ciscoFlashPartitionUpgradeMethod object will then indicate whether the Flash Load Helper can be used to write a file to this partition or not.  \* readWrite if partition is programmable
            	**type**\: :py:class:`CiscoFlashPartitionStatus_Enum <ydk.models.flash.CISCO_FLASH_MIB.CISCOFLASHMIB.CiscoFlashPartitionTable.CiscoFlashPartitionEntry.CiscoFlashPartitionStatus_Enum>`
            
            .. attribute:: ciscoflashpartitionupgrademethod
            
            	Flash partition upgrade method, ie., method by which new files can be downloaded into the partition. FLH stands for Flash Load Helper, a feature provided on run\-from\-Flash systems for upgrading Flash. This feature uses the bootstrap code in ROMs to help in automatic download. This object should be retrieved if the partition status is runFromFlash(2). If the partition status is readOnly(1), the upgrade method would depend on the reason for the readOnly status. For eg., it may simply be a matter of installing the programming jumper, or it may require execution of a later version of software that supports the Flash chips.  unknown      \-  the current system image does not know                 how Flash can be programmed. A possible                 method would be to reload the ROM image                 and perform the upgrade manually. rxbootFLH    \-  the Flash Load Helper is available to                 download files to Flash. A copy\-to\-flash                 command can be used and this system image                 will automatically reload the Rxboot image                 in ROM and direct it to carry out the                 download request. direct       \-  will be done directly by this image
            	**type**\: :py:class:`CiscoFlashPartitionUpgradeMethod_Enum <ydk.models.flash.CISCO_FLASH_MIB.CISCOFLASHMIB.CiscoFlashPartitionTable.CiscoFlashPartitionEntry.CiscoFlashPartitionUpgradeMethod_Enum>`
            
            

            """

            _prefix = 'cisco-flash'
            _revision = '2013-08-06'

            def __init__(self):
                self.parent = None
                self.ciscoflashdeviceindex = None
                self.ciscoflashpartitionindex = None
                self.ciscoflashpartitionchecksumalgorithm = None
                self.ciscoflashpartitionendchip = None
                self.ciscoflashpartitionfilecount = None
                self.ciscoflashpartitionfilenamelength = None
                self.ciscoflashpartitionfreespace = None
                self.ciscoflashpartitionfreespaceextended = None
                self.ciscoflashpartitionlowspacenotifthreshold = None
                self.ciscoflashpartitionname = None
                self.ciscoflashpartitionneederasure = None
                self.ciscoflashpartitionsize = None
                self.ciscoflashpartitionsizeextended = None
                self.ciscoflashpartitionstartchip = None
                self.ciscoflashpartitionstatus = None
                self.ciscoflashpartitionupgrademethod = None

            class CiscoFlashPartitionChecksumAlgorithm_Enum(Enum):
                """
                CiscoFlashPartitionChecksumAlgorithm_Enum

                Checksum algorithm identifier for checksum method
                used by the file system. Normally, this would be
                fixed for a particular file system. When a file
                system writes a file to Flash, it checksums the
                data written. The checksum then serves as a way
                to validate the data read back whenever the file
                is opened for reading.
                Since there is no way, when using TFTP, to guarantee
                that a network download has been error free (since
                UDP checksums may not have been enabled), this
                object together with the ciscoFlashFileChecksum
                object provides a method for any management station
                to regenerate the checksum of the original file
                on the server and compare checksums to ensure that
                the file download to Flash was error free.
                simpleChecksum represents a simple 1s complement
                addition of short word values. Other algorithm
                values will be added as necessary.

                """

                SIMPLECHECKSUM = 1

                UNDEFINED = 2

                SIMPLECRC = 3


                @staticmethod
                def _meta_info():
                    from ydk.models.flash._meta import _CISCO_FLASH_MIB as meta
                    return meta._meta_table['CISCOFLASHMIB.CiscoFlashPartitionTable.CiscoFlashPartitionEntry.CiscoFlashPartitionChecksumAlgorithm_Enum']


            class CiscoFlashPartitionStatus_Enum(Enum):
                """
                CiscoFlashPartitionStatus_Enum

                Flash partition status can be \:
                
                \* readOnly if device is not programmable either because
                chips could not be recognized or an erroneous mismatch
                of chips was detected. Chip recognition may fail either
                because the chips are not supported by the system,
                or because the Vpp voltage required to identify chips
                has been disabled via the programming jumper.
                The ciscoFlashDeviceProgrammingJumper, ciscoFlashChipCode,
                and ciscoFlashChipDescr objects can be examined to get
                more details on the cause of this status
                \* runFromFlash (RFF) if current image is running from
                this partition.
                The ciscoFlashPartitionUpgradeMethod object will then
                indicate whether the Flash Load Helper can be used
                to write a file to this partition or not.
                
                \* readWrite if partition is programmable.

                """

                READONLY = 1

                RUNFROMFLASH = 2

                READWRITE = 3


                @staticmethod
                def _meta_info():
                    from ydk.models.flash._meta import _CISCO_FLASH_MIB as meta
                    return meta._meta_table['CISCOFLASHMIB.CiscoFlashPartitionTable.CiscoFlashPartitionEntry.CiscoFlashPartitionStatus_Enum']


            class CiscoFlashPartitionUpgradeMethod_Enum(Enum):
                """
                CiscoFlashPartitionUpgradeMethod_Enum

                Flash partition upgrade method, ie., method by which
                new files can be downloaded into the partition.
                FLH stands for Flash Load Helper, a feature provided
                on run\-from\-Flash systems for upgrading Flash. This
                feature uses the bootstrap code in ROMs to help in
                automatic download.
                This object should be retrieved if the partition
                status is runFromFlash(2).
                If the partition status is readOnly(1), the upgrade
                method would depend on the reason for the readOnly
                status. For eg., it may simply be a matter of installing
                the programming jumper, or it may require execution of a
                later version of software that supports the Flash chips.
                
                unknown      \-  the current system image does not know
                                how Flash can be programmed. A possible
                                method would be to reload the ROM image
                                and perform the upgrade manually.
                rxbootFLH    \-  the Flash Load Helper is available to
                                download files to Flash. A copy\-to\-flash
                                command can be used and this system image
                                will automatically reload the Rxboot image
                                in ROM and direct it to carry out the
                                download request.
                direct       \-  will be done directly by this image.

                """

                UNKNOWN = 1

                RXBOOTFLH = 2

                DIRECT = 3


                @staticmethod
                def _meta_info():
                    from ydk.models.flash._meta import _CISCO_FLASH_MIB as meta
                    return meta._meta_table['CISCOFLASHMIB.CiscoFlashPartitionTable.CiscoFlashPartitionEntry.CiscoFlashPartitionUpgradeMethod_Enum']


            @property
            def _common_path(self):
                if self.ciscoflashdeviceindex is None:
                    raise YPYDataValidationError('Key property ciscoflashdeviceindex is None')
                if self.ciscoflashpartitionindex is None:
                    raise YPYDataValidationError('Key property ciscoflashpartitionindex is None')

                return '/CISCO-FLASH-MIB:CISCO-FLASH-MIB/CISCO-FLASH-MIB:ciscoFlashPartitionTable/CISCO-FLASH-MIB:ciscoFlashPartitionEntry[CISCO-FLASH-MIB:ciscoFlashDeviceIndex = ' + str(self.ciscoflashdeviceindex) + '][CISCO-FLASH-MIB:ciscoFlashPartitionIndex = ' + str(self.ciscoflashpartitionindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.ciscoflashdeviceindex is not None:
                    return True

                if self.ciscoflashpartitionindex is not None:
                    return True

                if self.ciscoflashpartitionchecksumalgorithm is not None:
                    return True

                if self.ciscoflashpartitionendchip is not None:
                    return True

                if self.ciscoflashpartitionfilecount is not None:
                    return True

                if self.ciscoflashpartitionfilenamelength is not None:
                    return True

                if self.ciscoflashpartitionfreespace is not None:
                    return True

                if self.ciscoflashpartitionfreespaceextended is not None:
                    return True

                if self.ciscoflashpartitionlowspacenotifthreshold is not None:
                    return True

                if self.ciscoflashpartitionname is not None:
                    return True

                if self.ciscoflashpartitionneederasure is not None:
                    return True

                if self.ciscoflashpartitionsize is not None:
                    return True

                if self.ciscoflashpartitionsizeextended is not None:
                    return True

                if self.ciscoflashpartitionstartchip is not None:
                    return True

                if self.ciscoflashpartitionstatus is not None:
                    return True

                if self.ciscoflashpartitionupgrademethod is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.flash._meta import _CISCO_FLASH_MIB as meta
                return meta._meta_table['CISCOFLASHMIB.CiscoFlashPartitionTable.CiscoFlashPartitionEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-FLASH-MIB:CISCO-FLASH-MIB/CISCO-FLASH-MIB:ciscoFlashPartitionTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.ciscoflashpartitionentry is not None:
                for child_ref in self.ciscoflashpartitionentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.flash._meta import _CISCO_FLASH_MIB as meta
            return meta._meta_table['CISCOFLASHMIB.CiscoFlashPartitionTable']['meta_info']


    class CiscoFlashPartitioningTable(object):
        """
        A table of Flash partitioning operation entries. Each
        entry represents a Flash partitioning operation that
        has been initiated.
        
        .. attribute:: ciscoflashpartitioningentry
        
        	A Flash partitioning operation entry. Each entry consists of the command, the target device, the partition count, and optionally the partition sizes.  A management station wishing to create an entry should first generate a pseudo\-random serial number to be used as the index to this sparse table.  The station should then create the associated instance of the row status object. It must also, either in the same or in successive PDUs, create the associated instance of the command and parameter objects. It should also modify the default values for any of the parameter objects if the defaults are not appropriate.  Once the appropriate instances of all the command objects have been created, either by an explicit SNMP set request or by default, the row status should be set to active to initiate the operation. Note that this entire procedure may be initiated via a single set request which specifies a row status of createAndGo as well as specifies valid values for the non\-defaulted parameter objects.  Once an operation has been activated, it cannot be stopped.  Once the operation completes, the management station should retrieve the value of the status object (and time if desired), and delete the entry.  In order to prevent old entries from clogging the table, entries will be aged out, but an entry will never be deleted within 5 minutes of completing
        	**type**\: list of :py:class:`CiscoFlashPartitioningEntry <ydk.models.flash.CISCO_FLASH_MIB.CISCOFLASHMIB.CiscoFlashPartitioningTable.CiscoFlashPartitioningEntry>`
        
        

        """

        _prefix = 'cisco-flash'
        _revision = '2013-08-06'

        def __init__(self):
            self.parent = None
            self.ciscoflashpartitioningentry = YList()
            self.ciscoflashpartitioningentry.parent = self
            self.ciscoflashpartitioningentry.name = 'ciscoflashpartitioningentry'


        class CiscoFlashPartitioningEntry(object):
            """
            A Flash partitioning operation entry. Each entry
            consists of the command, the target device, the
            partition count, and optionally the partition sizes.
            
            A management station wishing to create an entry should
            first generate a pseudo\-random serial number to be used
            as the index to this sparse table.  The station should
            then create the associated instance of the row status
            object. It must also, either in the same or in successive
            PDUs, create the associated instance of the command and
            parameter objects. It should also modify the default values
            for any of the parameter objects if the defaults are not
            appropriate.
            
            Once the appropriate instances of all the command
            objects have been created, either by an explicit SNMP
            set request or by default, the row status should be set
            to active to initiate the operation. Note that this entire
            procedure may be initiated via a single set request which
            specifies a row status of createAndGo as well as specifies
            valid values for the non\-defaulted parameter objects.
            
            Once an operation has been activated, it cannot be
            stopped.
            
            Once the operation completes, the management station should
            retrieve the value of the status object (and time if
            desired), and delete the entry.  In order to prevent old
            entries from clogging the table, entries will be aged out,
            but an entry will never be deleted within 5 minutes of
            completing.
            
            .. attribute:: ciscoflashpartitioningserialnumber
            
            	Object which specifies a unique entry in the partitioning operations table. A management station wishing to initiate a partitioning operation should use a pseudo\-random value for this object when creating or modifying an instance of a ciscoFlashPartitioningEntry
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: ciscoflashpartitioningcommand
            
            	The partitioning command to be executed. Mandatory. If the command is unsupported, the partitioningInvalidOperation error will be reported in the operation status.  Command                 Remarks partition               Partition a Flash device.                         All the prerequisites for                         partitioning must be met for                         this command to succeed.  Command table           Parameters 1) partition            PartitioningDestinationName                         PartitioningPartitionCount                         PartitioningPartitionSizes (opt)                         PartitioningNotifyOnCompletion (opt)
            	**type**\: :py:class:`CiscoFlashPartitioningCommand_Enum <ydk.models.flash.CISCO_FLASH_MIB.CISCOFLASHMIB.CiscoFlashPartitioningTable.CiscoFlashPartitioningEntry.CiscoFlashPartitioningCommand_Enum>`
            
            .. attribute:: ciscoflashpartitioningdestinationname
            
            	Destination device name. This name will be the value obtained from FlashDeviceName. If the name is not specified, the default Flash device will be assumed
            	**type**\: str
            
            	**range:** 0..255
            
            .. attribute:: ciscoflashpartitioningentrystatus
            
            	The status of this table entry
            	**type**\: :py:class:`RowStatus_Enum <ydk.models.snmpv2.SNMPv2_TC.RowStatus_Enum>`
            
            .. attribute:: ciscoflashpartitioningnotifyoncompletion
            
            	Specifies whether or not a notification should be generated on the completion of the partitioning operation. If specified, ciscoFlashPartitioningCompletionTrap will be generated. It is the responsibility of the management entity to ensure that the SNMP administrative model is configured in such a way as to allow the notification to be delivered
            	**type**\: bool
            
            .. attribute:: ciscoflashpartitioningpartitioncount
            
            	This object is used to specify the number of partitions to be created. Its value cannot exceed the value of ciscoFlashDeviceMaxPartitions.  To undo partitioning (revert to a single partition), this object must have the value 1
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: ciscoflashpartitioningpartitionsizes
            
            	This object is used to explicitly specify the size of each partition to be created. The size of each partition will be in units of ciscoFlashDeviceMinPartitionSize. The value of this object will be in the form\:         <part1>\:<part2>...\:<partn>  If partition sizes are not specified, the system will calculate default sizes based on the partition count, the minimum partition size, and the device size. Partition size need not be specified when undoing partitioning (partition count is 1). If partition sizes are specified, the number of sizes specified must exactly match the partition count. If not, the partitioning command will be rejected with the invalidPartitionSizes error 
            	**type**\: str
            
            	**pattern:** \\p{IsBasicLatin}{0,255}
            
            .. attribute:: ciscoflashpartitioningstatus
            
            	The status of the specified partitioning operation. partitioningInProgress \:         specified operation is active  partitioningOperationSuccess \:         specified operation is supported and completed         successfully  partitioningInvalidOperation \:         command invalid or command\-protocol\-device         combination unsupported  partitioningInvalidDestName \:         invalid target name (file or partition or         device name) specified  partitioningInvalidPartitionCount \:         invalid partition count specified for the         partitioning command  partitioningInvalidPartitionSizes \:         invalid partition size, or invalid count of         partition sizes  partitioningDeviceBusy \:         specified device is in use and locked by         another process  partitioningDeviceOpenError \:         invalid device name  partitioningDeviceError \:         device read, write or erase error  partitioningNoMemory \:         system running low on memory  partitioningUnknownFailure \:         failure unknown
            	**type**\: :py:class:`CiscoFlashPartitioningStatus_Enum <ydk.models.flash.CISCO_FLASH_MIB.CISCOFLASHMIB.CiscoFlashPartitioningTable.CiscoFlashPartitioningEntry.CiscoFlashPartitioningStatus_Enum>`
            
            .. attribute:: ciscoflashpartitioningtime
            
            	Time taken for the operation. This object will be like a stopwatch, starting when the operation starts, stopping when the operation completes. If a management entity keeps a database of completion times for various operations, it can then use the stopwatch capability to display percentage completion time
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'cisco-flash'
            _revision = '2013-08-06'

            def __init__(self):
                self.parent = None
                self.ciscoflashpartitioningserialnumber = None
                self.ciscoflashpartitioningcommand = None
                self.ciscoflashpartitioningdestinationname = None
                self.ciscoflashpartitioningentrystatus = None
                self.ciscoflashpartitioningnotifyoncompletion = None
                self.ciscoflashpartitioningpartitioncount = None
                self.ciscoflashpartitioningpartitionsizes = None
                self.ciscoflashpartitioningstatus = None
                self.ciscoflashpartitioningtime = None

            class CiscoFlashPartitioningCommand_Enum(Enum):
                """
                CiscoFlashPartitioningCommand_Enum

                The partitioning command to be executed. Mandatory.
                If the command is unsupported, the
                partitioningInvalidOperation
                error will be reported in the operation status.
                
                Command                 Remarks
                partition               Partition a Flash device.
                                        All the prerequisites for
                                        partitioning must be met for
                                        this command to succeed.
                
                Command table           Parameters
                1) partition            PartitioningDestinationName
                                        PartitioningPartitionCount
                                        PartitioningPartitionSizes (opt)
                                        PartitioningNotifyOnCompletion (opt)

                """

                PARTITION = 1


                @staticmethod
                def _meta_info():
                    from ydk.models.flash._meta import _CISCO_FLASH_MIB as meta
                    return meta._meta_table['CISCOFLASHMIB.CiscoFlashPartitioningTable.CiscoFlashPartitioningEntry.CiscoFlashPartitioningCommand_Enum']


            class CiscoFlashPartitioningStatus_Enum(Enum):
                """
                CiscoFlashPartitioningStatus_Enum

                The status of the specified partitioning operation.
                partitioningInProgress \:
                        specified operation is active
                
                partitioningOperationSuccess \:
                        specified operation is supported and completed
                        successfully
                
                partitioningInvalidOperation \:
                        command invalid or command\-protocol\-device
                        combination unsupported
                
                partitioningInvalidDestName \:
                        invalid target name (file or partition or
                        device name) specified
                
                partitioningInvalidPartitionCount \:
                        invalid partition count specified for the
                        partitioning command
                
                partitioningInvalidPartitionSizes \:
                        invalid partition size, or invalid count of
                        partition sizes
                
                partitioningDeviceBusy \:
                        specified device is in use and locked by
                        another process
                
                partitioningDeviceOpenError \:
                        invalid device name
                
                partitioningDeviceError \:
                        device read, write or erase error
                
                partitioningNoMemory \:
                        system running low on memory
                
                partitioningUnknownFailure \:
                        failure unknown

                """

                PARTITIONINGINPROGRESS = 1

                PARTITIONINGOPERATIONSUCCESS = 2

                PARTITIONINGINVALIDOPERATION = 3

                PARTITIONINGINVALIDDESTNAME = 4

                PARTITIONINGINVALIDPARTITIONCOUNT = 5

                PARTITIONINGINVALIDPARTITIONSIZES = 6

                PARTITIONINGDEVICEBUSY = 7

                PARTITIONINGDEVICEOPENERROR = 8

                PARTITIONINGDEVICEERROR = 9

                PARTITIONINGNOMEMORY = 10

                PARTITIONINGUNKNOWNFAILURE = 11


                @staticmethod
                def _meta_info():
                    from ydk.models.flash._meta import _CISCO_FLASH_MIB as meta
                    return meta._meta_table['CISCOFLASHMIB.CiscoFlashPartitioningTable.CiscoFlashPartitioningEntry.CiscoFlashPartitioningStatus_Enum']


            @property
            def _common_path(self):
                if self.ciscoflashpartitioningserialnumber is None:
                    raise YPYDataValidationError('Key property ciscoflashpartitioningserialnumber is None')

                return '/CISCO-FLASH-MIB:CISCO-FLASH-MIB/CISCO-FLASH-MIB:ciscoFlashPartitioningTable/CISCO-FLASH-MIB:ciscoFlashPartitioningEntry[CISCO-FLASH-MIB:ciscoFlashPartitioningSerialNumber = ' + str(self.ciscoflashpartitioningserialnumber) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.ciscoflashpartitioningserialnumber is not None:
                    return True

                if self.ciscoflashpartitioningcommand is not None:
                    return True

                if self.ciscoflashpartitioningdestinationname is not None:
                    return True

                if self.ciscoflashpartitioningentrystatus is not None:
                    return True

                if self.ciscoflashpartitioningnotifyoncompletion is not None:
                    return True

                if self.ciscoflashpartitioningpartitioncount is not None:
                    return True

                if self.ciscoflashpartitioningpartitionsizes is not None:
                    return True

                if self.ciscoflashpartitioningstatus is not None:
                    return True

                if self.ciscoflashpartitioningtime is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.flash._meta import _CISCO_FLASH_MIB as meta
                return meta._meta_table['CISCOFLASHMIB.CiscoFlashPartitioningTable.CiscoFlashPartitioningEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-FLASH-MIB:CISCO-FLASH-MIB/CISCO-FLASH-MIB:ciscoFlashPartitioningTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.ciscoflashpartitioningentry is not None:
                for child_ref in self.ciscoflashpartitioningentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.flash._meta import _CISCO_FLASH_MIB as meta
            return meta._meta_table['CISCOFLASHMIB.CiscoFlashPartitioningTable']['meta_info']

    @property
    def _common_path(self):

        return '/CISCO-FLASH-MIB:CISCO-FLASH-MIB'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if not self.is_config():
            return False
        if self.is_presence():
            return True
        if self.ciscoflashcfg is not None and self.ciscoflashcfg._has_data():
            return True

        if self.ciscoflashcfg is not None and self.ciscoflashcfg.is_presence():
            return True

        if self.ciscoflashchiptable is not None and self.ciscoflashchiptable._has_data():
            return True

        if self.ciscoflashchiptable is not None and self.ciscoflashchiptable.is_presence():
            return True

        if self.ciscoflashcopytable is not None and self.ciscoflashcopytable._has_data():
            return True

        if self.ciscoflashcopytable is not None and self.ciscoflashcopytable.is_presence():
            return True

        if self.ciscoflashdevice is not None and self.ciscoflashdevice._has_data():
            return True

        if self.ciscoflashdevice is not None and self.ciscoflashdevice.is_presence():
            return True

        if self.ciscoflashdevicetable is not None and self.ciscoflashdevicetable._has_data():
            return True

        if self.ciscoflashdevicetable is not None and self.ciscoflashdevicetable.is_presence():
            return True

        if self.ciscoflashfilebytypetable is not None and self.ciscoflashfilebytypetable._has_data():
            return True

        if self.ciscoflashfilebytypetable is not None and self.ciscoflashfilebytypetable.is_presence():
            return True

        if self.ciscoflashfiletable is not None and self.ciscoflashfiletable._has_data():
            return True

        if self.ciscoflashfiletable is not None and self.ciscoflashfiletable.is_presence():
            return True

        if self.ciscoflashmiscoptable is not None and self.ciscoflashmiscoptable._has_data():
            return True

        if self.ciscoflashmiscoptable is not None and self.ciscoflashmiscoptable.is_presence():
            return True

        if self.ciscoflashpartitioningtable is not None and self.ciscoflashpartitioningtable._has_data():
            return True

        if self.ciscoflashpartitioningtable is not None and self.ciscoflashpartitioningtable.is_presence():
            return True

        if self.ciscoflashpartitiontable is not None and self.ciscoflashpartitiontable._has_data():
            return True

        if self.ciscoflashpartitiontable is not None and self.ciscoflashpartitiontable.is_presence():
            return True

        return False

    def is_presence(self):
        ''' Returns True if this instance represents presence container else returns False '''
        return False

    @staticmethod
    def _meta_info():
        from ydk.models.flash._meta import _CISCO_FLASH_MIB as meta
        return meta._meta_table['CISCOFLASHMIB']['meta_info']


