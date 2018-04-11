""" CISCO_FLASH_MIB 

This MIB provides for the management of Cisco
Flash Devices.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class FlashFileType(Enum):
    """
    FlashFileType (Enum Class)

    File types for files in a flash.

    unknown        \- file type is not one of the following.

    config         \- configuration file like

                     startup configuration or

                     running configuration.

    image          \- image file.

    directory      \- directory entry.

    crashinfo      \- file containing crashinfo.

    .. data:: unknown = 1

    .. data:: config = 2

    .. data:: image = 3

    .. data:: directory = 4

    .. data:: crashinfo = 5

    """

    unknown = Enum.YLeaf(1, "unknown")

    config = Enum.YLeaf(2, "config")

    image = Enum.YLeaf(3, "image")

    directory = Enum.YLeaf(4, "directory")

    crashinfo = Enum.YLeaf(5, "crashinfo")



class CISCOFLASHMIB(Entity):
    """
    
    
    .. attribute:: ciscoflashdevice
    
    	
    	**type**\:  :py:class:`Ciscoflashdevice <ydk.models.cisco_ios_xe.CISCO_FLASH_MIB.CISCOFLASHMIB.Ciscoflashdevice>`
    
    .. attribute:: ciscoflashcfg
    
    	
    	**type**\:  :py:class:`Ciscoflashcfg <ydk.models.cisco_ios_xe.CISCO_FLASH_MIB.CISCOFLASHMIB.Ciscoflashcfg>`
    
    .. attribute:: ciscoflashdevicetable
    
    	Table of Flash device properties for each initialized Flash device. Each Flash device installed in a system is detected, sized, and initialized when the system image boots up. For removable Flash devices, the device properties will be dynamically deleted and recreated as the device is removed and inserted. Note that in this case, the newly inserted device may not be the same as the earlier removed one. The ciscoFlashDeviceInitTime object is available for a management station to determine the time at which a device was initialized, and thereby detect the change of a removable device. A removable device that has not been installed will also have an entry in this table. This is to let a management station know about a removable device that has been removed. Since a removed device obviously cannot be sized and initialized, the table entry for such a device will have ciscoFlashDeviceSize equal to zero, and the following objects will have an indeterminate value\:         ciscoFlashDeviceMinPartitionSize,         ciscoFlashDeviceMaxPartitions,         ciscoFlashDevicePartitions, and         ciscoFlashDeviceChipCount. ciscoFlashDeviceRemovable will be true to indicate it is removable
    	**type**\:  :py:class:`Ciscoflashdevicetable <ydk.models.cisco_ios_xe.CISCO_FLASH_MIB.CISCOFLASHMIB.Ciscoflashdevicetable>`
    
    .. attribute:: ciscoflashchiptable
    
    	Table of Flash device chip properties for each initialized Flash device. This table is meant primarily for aiding error diagnosis
    	**type**\:  :py:class:`Ciscoflashchiptable <ydk.models.cisco_ios_xe.CISCO_FLASH_MIB.CISCOFLASHMIB.Ciscoflashchiptable>`
    
    .. attribute:: ciscoflashpartitiontable
    
    	Table of flash device partition properties for each initialized flash partition. Whenever there is no explicit partitioning done, a single partition spanning the entire device will be assumed to exist. There will therefore always be atleast one partition on a device
    	**type**\:  :py:class:`Ciscoflashpartitiontable <ydk.models.cisco_ios_xe.CISCO_FLASH_MIB.CISCOFLASHMIB.Ciscoflashpartitiontable>`
    
    .. attribute:: ciscoflashfiletable
    
    	Table of information for files in a Flash partition
    	**type**\:  :py:class:`Ciscoflashfiletable <ydk.models.cisco_ios_xe.CISCO_FLASH_MIB.CISCOFLASHMIB.Ciscoflashfiletable>`
    
    .. attribute:: ciscoflashfilebytypetable
    
    	Table of information for files on the manageable flash devices sorted by File Types
    	**type**\:  :py:class:`Ciscoflashfilebytypetable <ydk.models.cisco_ios_xe.CISCO_FLASH_MIB.CISCOFLASHMIB.Ciscoflashfilebytypetable>`
    
    .. attribute:: ciscoflashcopytable
    
    	A table of Flash copy operation entries. Each entry represents a Flash copy operation (to or from Flash) that has been initiated
    	**type**\:  :py:class:`Ciscoflashcopytable <ydk.models.cisco_ios_xe.CISCO_FLASH_MIB.CISCOFLASHMIB.Ciscoflashcopytable>`
    
    .. attribute:: ciscoflashpartitioningtable
    
    	A table of Flash partitioning operation entries. Each entry represents a Flash partitioning operation that has been initiated
    	**type**\:  :py:class:`Ciscoflashpartitioningtable <ydk.models.cisco_ios_xe.CISCO_FLASH_MIB.CISCOFLASHMIB.Ciscoflashpartitioningtable>`
    
    .. attribute:: ciscoflashmiscoptable
    
    	A table of misc Flash operation entries. Each entry represents a Flash operation that has been initiated
    	**type**\:  :py:class:`Ciscoflashmiscoptable <ydk.models.cisco_ios_xe.CISCO_FLASH_MIB.CISCOFLASHMIB.Ciscoflashmiscoptable>`
    
    

    """

    _prefix = 'CISCO-FLASH-MIB'
    _revision = '2013-08-06'

    def __init__(self):
        super(CISCOFLASHMIB, self).__init__()
        self._top_entity = None

        self.yang_name = "CISCO-FLASH-MIB"
        self.yang_parent_name = "CISCO-FLASH-MIB"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([("ciscoFlashDevice", ("ciscoflashdevice", CISCOFLASHMIB.Ciscoflashdevice)), ("ciscoFlashCfg", ("ciscoflashcfg", CISCOFLASHMIB.Ciscoflashcfg)), ("ciscoFlashDeviceTable", ("ciscoflashdevicetable", CISCOFLASHMIB.Ciscoflashdevicetable)), ("ciscoFlashChipTable", ("ciscoflashchiptable", CISCOFLASHMIB.Ciscoflashchiptable)), ("ciscoFlashPartitionTable", ("ciscoflashpartitiontable", CISCOFLASHMIB.Ciscoflashpartitiontable)), ("ciscoFlashFileTable", ("ciscoflashfiletable", CISCOFLASHMIB.Ciscoflashfiletable)), ("ciscoFlashFileByTypeTable", ("ciscoflashfilebytypetable", CISCOFLASHMIB.Ciscoflashfilebytypetable)), ("ciscoFlashCopyTable", ("ciscoflashcopytable", CISCOFLASHMIB.Ciscoflashcopytable)), ("ciscoFlashPartitioningTable", ("ciscoflashpartitioningtable", CISCOFLASHMIB.Ciscoflashpartitioningtable)), ("ciscoFlashMiscOpTable", ("ciscoflashmiscoptable", CISCOFLASHMIB.Ciscoflashmiscoptable))])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.ciscoflashdevice = CISCOFLASHMIB.Ciscoflashdevice()
        self.ciscoflashdevice.parent = self
        self._children_name_map["ciscoflashdevice"] = "ciscoFlashDevice"
        self._children_yang_names.add("ciscoFlashDevice")

        self.ciscoflashcfg = CISCOFLASHMIB.Ciscoflashcfg()
        self.ciscoflashcfg.parent = self
        self._children_name_map["ciscoflashcfg"] = "ciscoFlashCfg"
        self._children_yang_names.add("ciscoFlashCfg")

        self.ciscoflashdevicetable = CISCOFLASHMIB.Ciscoflashdevicetable()
        self.ciscoflashdevicetable.parent = self
        self._children_name_map["ciscoflashdevicetable"] = "ciscoFlashDeviceTable"
        self._children_yang_names.add("ciscoFlashDeviceTable")

        self.ciscoflashchiptable = CISCOFLASHMIB.Ciscoflashchiptable()
        self.ciscoflashchiptable.parent = self
        self._children_name_map["ciscoflashchiptable"] = "ciscoFlashChipTable"
        self._children_yang_names.add("ciscoFlashChipTable")

        self.ciscoflashpartitiontable = CISCOFLASHMIB.Ciscoflashpartitiontable()
        self.ciscoflashpartitiontable.parent = self
        self._children_name_map["ciscoflashpartitiontable"] = "ciscoFlashPartitionTable"
        self._children_yang_names.add("ciscoFlashPartitionTable")

        self.ciscoflashfiletable = CISCOFLASHMIB.Ciscoflashfiletable()
        self.ciscoflashfiletable.parent = self
        self._children_name_map["ciscoflashfiletable"] = "ciscoFlashFileTable"
        self._children_yang_names.add("ciscoFlashFileTable")

        self.ciscoflashfilebytypetable = CISCOFLASHMIB.Ciscoflashfilebytypetable()
        self.ciscoflashfilebytypetable.parent = self
        self._children_name_map["ciscoflashfilebytypetable"] = "ciscoFlashFileByTypeTable"
        self._children_yang_names.add("ciscoFlashFileByTypeTable")

        self.ciscoflashcopytable = CISCOFLASHMIB.Ciscoflashcopytable()
        self.ciscoflashcopytable.parent = self
        self._children_name_map["ciscoflashcopytable"] = "ciscoFlashCopyTable"
        self._children_yang_names.add("ciscoFlashCopyTable")

        self.ciscoflashpartitioningtable = CISCOFLASHMIB.Ciscoflashpartitioningtable()
        self.ciscoflashpartitioningtable.parent = self
        self._children_name_map["ciscoflashpartitioningtable"] = "ciscoFlashPartitioningTable"
        self._children_yang_names.add("ciscoFlashPartitioningTable")

        self.ciscoflashmiscoptable = CISCOFLASHMIB.Ciscoflashmiscoptable()
        self.ciscoflashmiscoptable.parent = self
        self._children_name_map["ciscoflashmiscoptable"] = "ciscoFlashMiscOpTable"
        self._children_yang_names.add("ciscoFlashMiscOpTable")
        self._segment_path = lambda: "CISCO-FLASH-MIB:CISCO-FLASH-MIB"


    class Ciscoflashdevice(Entity):
        """
        
        
        .. attribute:: ciscoflashdevicessupported
        
        	Number of Flash devices supported by the system. If the system does not support any Flash devices, this MIB will not be loaded on that system. The value of this object will therefore be atleast 1
        	**type**\: int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'CISCO-FLASH-MIB'
        _revision = '2013-08-06'

        def __init__(self):
            super(CISCOFLASHMIB.Ciscoflashdevice, self).__init__()

            self.yang_name = "ciscoFlashDevice"
            self.yang_parent_name = "CISCO-FLASH-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('ciscoflashdevicessupported', YLeaf(YType.uint32, 'ciscoFlashDevicesSupported')),
            ])
            self.ciscoflashdevicessupported = None
            self._segment_path = lambda: "ciscoFlashDevice"
            self._absolute_path = lambda: "CISCO-FLASH-MIB:CISCO-FLASH-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOFLASHMIB.Ciscoflashdevice, ['ciscoflashdevicessupported'], name, value)


    class Ciscoflashcfg(Entity):
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

        _prefix = 'CISCO-FLASH-MIB'
        _revision = '2013-08-06'

        def __init__(self):
            super(CISCOFLASHMIB.Ciscoflashcfg, self).__init__()

            self.yang_name = "ciscoFlashCfg"
            self.yang_parent_name = "CISCO-FLASH-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('ciscoflashcfgdevinsnotifenable', YLeaf(YType.boolean, 'ciscoFlashCfgDevInsNotifEnable')),
                ('ciscoflashcfgdevremnotifenable', YLeaf(YType.boolean, 'ciscoFlashCfgDevRemNotifEnable')),
                ('ciscoflashpartitionlowspacenotifenable', YLeaf(YType.boolean, 'ciscoFlashPartitionLowSpaceNotifEnable')),
            ])
            self.ciscoflashcfgdevinsnotifenable = None
            self.ciscoflashcfgdevremnotifenable = None
            self.ciscoflashpartitionlowspacenotifenable = None
            self._segment_path = lambda: "ciscoFlashCfg"
            self._absolute_path = lambda: "CISCO-FLASH-MIB:CISCO-FLASH-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOFLASHMIB.Ciscoflashcfg, ['ciscoflashcfgdevinsnotifenable', 'ciscoflashcfgdevremnotifenable', 'ciscoflashpartitionlowspacenotifenable'], name, value)


    class Ciscoflashdevicetable(Entity):
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
        	**type**\: list of  		 :py:class:`Ciscoflashdeviceentry <ydk.models.cisco_ios_xe.CISCO_FLASH_MIB.CISCOFLASHMIB.Ciscoflashdevicetable.Ciscoflashdeviceentry>`
        
        

        """

        _prefix = 'CISCO-FLASH-MIB'
        _revision = '2013-08-06'

        def __init__(self):
            super(CISCOFLASHMIB.Ciscoflashdevicetable, self).__init__()

            self.yang_name = "ciscoFlashDeviceTable"
            self.yang_parent_name = "CISCO-FLASH-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("ciscoFlashDeviceEntry", ("ciscoflashdeviceentry", CISCOFLASHMIB.Ciscoflashdevicetable.Ciscoflashdeviceentry))])
            self._leafs = OrderedDict()

            self.ciscoflashdeviceentry = YList(self)
            self._segment_path = lambda: "ciscoFlashDeviceTable"
            self._absolute_path = lambda: "CISCO-FLASH-MIB:CISCO-FLASH-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOFLASHMIB.Ciscoflashdevicetable, [], name, value)


        class Ciscoflashdeviceentry(Entity):
            """
            An entry in the table of flash device properties for
            each initialized flash device.
            Each entry can be randomly accessed by using
            ciscoFlashDeviceIndex as an index into the table.
            Note that removable devices will have an entry in
            the table even when they have been removed. However,
            a non\-removable device that has not been installed
            will not have an entry in the table.
            
            .. attribute:: ciscoflashdeviceindex  (key)
            
            	Flash device sequence number to index within the table of initialized flash devices. The lowest value should be 1. The highest should be less than or equal to the value of the ciscoFlashDevicesSupported object
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: ciscoflashdevicesize
            
            	Total size of the Flash device. For a removable device, the size will be zero if the device has been removed.  If the total size of the flash device is greater than the maximum value reportable by this object then this object should report its maximum value(4,294,967,295) and ciscoFlashDeviceSizeExtended must be used to report the flash device's size
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: bytes
            
            .. attribute:: ciscoflashdeviceminpartitionsize
            
            	This object will give the minimum partition size supported for this device. For systems that execute code directly out of Flash, the minimum partition size needs to be the bank size. (Bank size is equal to the size of a chip multiplied by the width of the device. In most cases, the device width is 4 bytes, and so the bank size would be four times the size of a chip). This has to be so because all programming commands affect the operation of an entire chip (in our case, an entire bank because all operations are done on the entire width of the device) even though the actual command may be localized to a small portion of each chip. So when executing code out of Flash, one needs to be able to write and erase some portion of Flash without affecting the code execution. For systems that execute code out of DRAM or ROM, it is possible to partition Flash with a finer granularity (for eg., at erase sector boundaries) if the system code supports such granularity.  This object will let a management entity know the minimum partition size as defined by the system. If the system does not support partitioning, the value will be equal to the device size in ciscoFlashDeviceSize. The maximum number of partitions that could be configured will be equal to the minimum of ciscoFlashDeviceMaxPartitions and (ciscoFlashDeviceSize / ciscoFlashDeviceMinPartitionSize).  If the total size of the flash device is greater than the maximum value reportable by this object then this object should report its maximum value(4,294,967,295) and ciscoFlashDeviceMinPartitionSizeExtended must be used to report the flash device's minimum partition size
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: bytes
            
            .. attribute:: ciscoflashdevicemaxpartitions
            
            	Max number of partitions supported by the system for this Flash device. Default will be 1, which actually means that partitioning is not supported. Note that this value will be defined by system limitations, not by the flash device itself (for eg., the system may impose a limit of 2 partitions even though the device may be large enough to be partitioned into 4 based on the smallest partition unit supported). On systems that execute code out of Flash, partitioning is a way of creating multiple file systems in the Flash device so that writing into or erasing of one file system can be done while executing code residing in another file system. For systems executing code out of DRAM, partitioning gives a way of sub\-dividing a large Flash device for easier management of files
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ciscoflashdevicepartitions
            
            	Flash device partitions actually present. Number of partitions cannot exceed the minimum of ciscoFlashDeviceMaxPartitions and (ciscoFlashDeviceSize / ciscoFlashDeviceMinPartitionSize). Will be equal to at least 1, the case where the partition spans the entire device (actually no partitioning). A partition will contain one or more minimum partition units (where a minimum partition unit is defined by ciscoFlashDeviceMinPartitionSize)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ciscoflashdevicechipcount
            
            	Total number of chips within the Flash device. The purpose of this object is to provide information upfront to a management station on how much chip info to expect and possibly help double check the chip index against an upper limit when randomly retrieving chip info for a partition
            	**type**\: int
            
            	**range:** 0..64
            
            .. attribute:: ciscoflashdevicename
            
            	Flash device name. This name is used to refer to the device within the system. Flash operations get directed to a device based on this name. The system has a concept of a default device. This would be the primary or most used device in case of multiple devices. The system directs an operation to the default device whenever a device name is not specified. The device name is therefore mandatory except when the operation is being done on the default device, or, the system supports only a single Flash device. The device name will always be available for a removable device, even when the device has been removed
            	**type**\: str
            
            	**length:** 0..16
            
            	**status**\: deprecated
            
            .. attribute:: ciscoflashdevicedescr
            
            	Description of a Flash device. The description is meant to explain what the Flash device and its purpose is. Current values are\:   System flash \- for the primary Flash used to store full                  system images.   Boot flash   \- for the secondary Flash used to store                  bootstrap images. The ciscoFlashDeviceDescr, ciscoFlashDeviceController (if applicable), and ciscoFlashPhyEntIndex objects are expected to collectively give all information about a Flash device. The device description will always be available for a removable device, even when the device has been removed
            	**type**\: str
            
            	**length:** 0..64
            
            .. attribute:: ciscoflashdevicecontroller
            
            	Flash device controller. The h/w card that actually controls Flash read/write/erase. Relevant for the AGS+ systems where Flash may be controlled by the MC+, STR or the ENVM cards, cards that may not actually contain the Flash chips. For systems that have removable PCMCIA flash cards that are controlled by a PCMCIA controller chip, this object may contain a description of that controller chip. Where irrelevant (Flash is a direct memory mapped device accessed directly by the main processor), this object will have an empty (NULL) string
            	**type**\: str
            
            	**length:** 0..64
            
            .. attribute:: ciscoflashdevicecard
            
            	This object will point to an instance of a card entry in the cardTable. The card entry will give details about the card on which the Flash device is actually located. For most systems, this is usually the main processor board. On the AGS+ systems, Flash is located on a separate multibus card such as the MC. This object will therefore be used to essentially index into cardTable to retrieve details about the card such as cardDescr, cardSlotNumber, etc
            	**type**\: str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            	**status**\: deprecated
            
            .. attribute:: ciscoflashdeviceprogrammingjumper
            
            	This object gives the state of a jumper (if present and can be determined) that controls the programming voltage called Vpp to the Flash device. Vpp is required for programming (erasing and writing) Flash. For certain older technology chips it is also required for identifying the chips (which in turn is required to identify which programming algorithms to use; different chips require different algorithms and commands). The purpose of the jumper, on systems where it is available, is to write protect a Flash device. On most of the newer remote access routers, this jumper is unavailable since users are not expected to visit remote sites just to install and remove the jumpers when upgrading software in the Flash device. The unknown(3) value will be returned for such systems and can be interpreted to mean that a programming jumper is not present or not required on those systems. On systems where the programming jumper state can be read back via a hardware register, the installed(1) or notInstalled(2) value will be returned. This object is expected to be used in conjunction with the ciscoFlashPartitionStatus object whenever that object has the readOnly(1) value. In such a case, this object will indicate whether the programming jumper is a possible reason for the readOnly state
            	**type**\:  :py:class:`Ciscoflashdeviceprogrammingjumper <ydk.models.cisco_ios_xe.CISCO_FLASH_MIB.CISCOFLASHMIB.Ciscoflashdevicetable.Ciscoflashdeviceentry.Ciscoflashdeviceprogrammingjumper>`
            
            .. attribute:: ciscoflashdeviceinittime
            
            	System time at which device was initialized. For fixed devices, this will be the system time at boot up. For removable devices, it will be the time at which the device was inserted, which may be boot up time, or a later time (if device was inserted later). If a device (fixed or removable) was repartitioned, it will be the time of repartitioning. The purpose of this object is to help a management station determine if a removable device has been changed. The application should retrieve this object prior to any operation and compare with the previously retrieved value. Note that this time will not be real time but a running time maintained by the system. This running time starts from zero when the system boots up. For a removable device that has been removed, this value will be zero
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ciscoflashdeviceremovable
            
            	Whether Flash device is removable. Generally, only PCMCIA Flash cards will be treated as removable. Socketed Flash chips and Flash SIMM modules will not be treated as removable. Simply put, only those Flash devices that can be inserted or removed without opening the hardware casing will be considered removable. Further, removable Flash devices are expected to have the necessary hardware support \-   1. on\-line removal and insertion   2. interrupt generation on removal or insertion
            	**type**\: bool
            
            .. attribute:: ciscoflashphyentindex
            
            	This object indicates the physical entity index of a physical entity in entPhysicalTable which the flash device actually located
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: ciscoflashdevicenameextended
            
            	Extended Flash device name whose size can be upto 255 characters. This name is used to refer to the device within the system. Flash operations get directed to a device based on this name. The system has a concept of a default device. This would be the primary or most used device in case of multiple devices. The system directs an operation to the default device whenever a device name is not specified. The device name is therefore mandatory except when the operation is being done on the default device, or, the system supports only a single Flash device. The device name will always be available for a removable device, even when the device has been removed
            	**type**\: str
            
            	**length:** 0..255
            
            .. attribute:: ciscoflashdevicesizeextended
            
            	Total size of the Flash device. For a removable device, the size will be zero if the device has been removed.  This object is a 64\-bit version of ciscoFlashDeviceSize
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: bytes
            
            .. attribute:: ciscoflashdeviceminpartitionsizeextended
            
            	This object provides the minimum partition size supported for this device. This object is a 64\-bit version of  ciscoFlashDeviceMinPatitionSize
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            

            """

            _prefix = 'CISCO-FLASH-MIB'
            _revision = '2013-08-06'

            def __init__(self):
                super(CISCOFLASHMIB.Ciscoflashdevicetable.Ciscoflashdeviceentry, self).__init__()

                self.yang_name = "ciscoFlashDeviceEntry"
                self.yang_parent_name = "ciscoFlashDeviceTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ciscoflashdeviceindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ciscoflashdeviceindex', YLeaf(YType.uint32, 'ciscoFlashDeviceIndex')),
                    ('ciscoflashdevicesize', YLeaf(YType.uint32, 'ciscoFlashDeviceSize')),
                    ('ciscoflashdeviceminpartitionsize', YLeaf(YType.uint32, 'ciscoFlashDeviceMinPartitionSize')),
                    ('ciscoflashdevicemaxpartitions', YLeaf(YType.uint32, 'ciscoFlashDeviceMaxPartitions')),
                    ('ciscoflashdevicepartitions', YLeaf(YType.uint32, 'ciscoFlashDevicePartitions')),
                    ('ciscoflashdevicechipcount', YLeaf(YType.int32, 'ciscoFlashDeviceChipCount')),
                    ('ciscoflashdevicename', YLeaf(YType.str, 'ciscoFlashDeviceName')),
                    ('ciscoflashdevicedescr', YLeaf(YType.str, 'ciscoFlashDeviceDescr')),
                    ('ciscoflashdevicecontroller', YLeaf(YType.str, 'ciscoFlashDeviceController')),
                    ('ciscoflashdevicecard', YLeaf(YType.str, 'ciscoFlashDeviceCard')),
                    ('ciscoflashdeviceprogrammingjumper', YLeaf(YType.enumeration, 'ciscoFlashDeviceProgrammingJumper')),
                    ('ciscoflashdeviceinittime', YLeaf(YType.uint32, 'ciscoFlashDeviceInitTime')),
                    ('ciscoflashdeviceremovable', YLeaf(YType.boolean, 'ciscoFlashDeviceRemovable')),
                    ('ciscoflashphyentindex', YLeaf(YType.int32, 'ciscoFlashPhyEntIndex')),
                    ('ciscoflashdevicenameextended', YLeaf(YType.str, 'ciscoFlashDeviceNameExtended')),
                    ('ciscoflashdevicesizeextended', YLeaf(YType.uint64, 'ciscoFlashDeviceSizeExtended')),
                    ('ciscoflashdeviceminpartitionsizeextended', YLeaf(YType.uint64, 'ciscoFlashDeviceMinPartitionSizeExtended')),
                ])
                self.ciscoflashdeviceindex = None
                self.ciscoflashdevicesize = None
                self.ciscoflashdeviceminpartitionsize = None
                self.ciscoflashdevicemaxpartitions = None
                self.ciscoflashdevicepartitions = None
                self.ciscoflashdevicechipcount = None
                self.ciscoflashdevicename = None
                self.ciscoflashdevicedescr = None
                self.ciscoflashdevicecontroller = None
                self.ciscoflashdevicecard = None
                self.ciscoflashdeviceprogrammingjumper = None
                self.ciscoflashdeviceinittime = None
                self.ciscoflashdeviceremovable = None
                self.ciscoflashphyentindex = None
                self.ciscoflashdevicenameextended = None
                self.ciscoflashdevicesizeextended = None
                self.ciscoflashdeviceminpartitionsizeextended = None
                self._segment_path = lambda: "ciscoFlashDeviceEntry" + "[ciscoFlashDeviceIndex='" + str(self.ciscoflashdeviceindex) + "']"
                self._absolute_path = lambda: "CISCO-FLASH-MIB:CISCO-FLASH-MIB/ciscoFlashDeviceTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOFLASHMIB.Ciscoflashdevicetable.Ciscoflashdeviceentry, ['ciscoflashdeviceindex', 'ciscoflashdevicesize', 'ciscoflashdeviceminpartitionsize', 'ciscoflashdevicemaxpartitions', 'ciscoflashdevicepartitions', 'ciscoflashdevicechipcount', 'ciscoflashdevicename', 'ciscoflashdevicedescr', 'ciscoflashdevicecontroller', 'ciscoflashdevicecard', 'ciscoflashdeviceprogrammingjumper', 'ciscoflashdeviceinittime', 'ciscoflashdeviceremovable', 'ciscoflashphyentindex', 'ciscoflashdevicenameextended', 'ciscoflashdevicesizeextended', 'ciscoflashdeviceminpartitionsizeextended'], name, value)

            class Ciscoflashdeviceprogrammingjumper(Enum):
                """
                Ciscoflashdeviceprogrammingjumper (Enum Class)

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

                .. data:: installed = 1

                .. data:: notInstalled = 2

                .. data:: unknown = 3

                """

                installed = Enum.YLeaf(1, "installed")

                notInstalled = Enum.YLeaf(2, "notInstalled")

                unknown = Enum.YLeaf(3, "unknown")



    class Ciscoflashchiptable(Entity):
        """
        Table of Flash device chip properties for each
        initialized Flash device.
        This table is meant primarily for aiding error
        diagnosis.
        
        .. attribute:: ciscoflashchipentry
        
        	An entry in the table of chip info for each flash device initialized in the system. An entry is indexed by two objects \- the device index and the chip index within that device
        	**type**\: list of  		 :py:class:`Ciscoflashchipentry <ydk.models.cisco_ios_xe.CISCO_FLASH_MIB.CISCOFLASHMIB.Ciscoflashchiptable.Ciscoflashchipentry>`
        
        

        """

        _prefix = 'CISCO-FLASH-MIB'
        _revision = '2013-08-06'

        def __init__(self):
            super(CISCOFLASHMIB.Ciscoflashchiptable, self).__init__()

            self.yang_name = "ciscoFlashChipTable"
            self.yang_parent_name = "CISCO-FLASH-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("ciscoFlashChipEntry", ("ciscoflashchipentry", CISCOFLASHMIB.Ciscoflashchiptable.Ciscoflashchipentry))])
            self._leafs = OrderedDict()

            self.ciscoflashchipentry = YList(self)
            self._segment_path = lambda: "ciscoFlashChipTable"
            self._absolute_path = lambda: "CISCO-FLASH-MIB:CISCO-FLASH-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOFLASHMIB.Ciscoflashchiptable, [], name, value)


        class Ciscoflashchipentry(Entity):
            """
            An entry in the table of chip info for each
            flash device initialized in the system.
            An entry is indexed by two objects \- the
            device index and the chip index within that
            device.
            
            .. attribute:: ciscoflashdeviceindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..4294967295
            
            	**refers to**\:  :py:class:`ciscoflashdeviceindex <ydk.models.cisco_ios_xe.CISCO_FLASH_MIB.CISCOFLASHMIB.Ciscoflashdevicetable.Ciscoflashdeviceentry>`
            
            .. attribute:: ciscoflashchipindex  (key)
            
            	Chip sequence number within selected flash device. Used to index within chip info table. Value starts from 1 and should not be greater than ciscoFlashDeviceChipCount for that device. When retrieving chip information for chips within a partition, the sequence number should lie between ciscoFlashPartitionStartChip & ciscoFlashPartitionEndChip (both inclusive)
            	**type**\: int
            
            	**range:** 1..64
            
            .. attribute:: ciscoflashchipcode
            
            	Manufacturer and device code for a chip. Lower byte will contain the device code. Upper byte will contain the manufacturer code. If a chip code is unknown because it could not be queried out of the chip, the value of this object will be 00\:00. Since programming algorithms differ from chip type to chip type, this chip code should be used to determine which algorithms to use (and thereby whether the chip is supported in the first place)
            	**type**\: str
            
            	**length:** 0..5
            
            .. attribute:: ciscoflashchipdescr
            
            	Flash chip name corresponding to the chip code. The name will contain the manufacturer and the chip type. It will be of the form \:   Intel 27F008SA. In the case where a chip code is unknown, this object will be an empty (NULL) string. In the case where the chip code is known but the chip is not supported by the system, this object will be an empty (NULL) string. A management station is therefore expected to use the chip code and the chip description in conjunction to provide additional information whenever the ciscoFlashPartitionStatus object has the readOnly(1) value
            	**type**\: str
            
            	**length:** 0..32
            
            .. attribute:: ciscoflashchipwriteretries
            
            	This object will provide a cumulative count (since last system boot up or initialization) of the number of write retries that were done in the chip. If no writes have been done to Flash, the count will be zero. Typically, a maximum of 25 retries are done on a single location before flagging a write error. A management station is expected to get this object for each chip in a partition after a write failure in that partition. To keep a track of retries for a given write operation, the management station would have to retrieve the values for the concerned chips before and after any write operation
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ciscoflashchiperaseretries
            
            	This object will provide a cumulative count (since last system boot up or initialization) of the number of erase retries that were done in the chip. Typically, a maximum of 2000 retries are done in a single erase zone (which may be a full chip or a portion, depending on the chip technology) before flagging an erase error. A management station is expected to get this object for each chip in a partition after an erase failure in that partition. To keep a track of retries for a given erase operation, the management station would have to retrieve the values for the concerned chips before and after any erase operation. Note that erase may be done through an independent command, or through a copy\-to\-flash command
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ciscoflashchipmaxwriteretries
            
            	The maximum number of write retries done at any single location before declaring a write failure
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ciscoflashchipmaxeraseretries
            
            	The maximum number of erase retries done within an erase sector before declaring an erase failure
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'CISCO-FLASH-MIB'
            _revision = '2013-08-06'

            def __init__(self):
                super(CISCOFLASHMIB.Ciscoflashchiptable.Ciscoflashchipentry, self).__init__()

                self.yang_name = "ciscoFlashChipEntry"
                self.yang_parent_name = "ciscoFlashChipTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ciscoflashdeviceindex','ciscoflashchipindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ciscoflashdeviceindex', YLeaf(YType.str, 'ciscoFlashDeviceIndex')),
                    ('ciscoflashchipindex', YLeaf(YType.int32, 'ciscoFlashChipIndex')),
                    ('ciscoflashchipcode', YLeaf(YType.str, 'ciscoFlashChipCode')),
                    ('ciscoflashchipdescr', YLeaf(YType.str, 'ciscoFlashChipDescr')),
                    ('ciscoflashchipwriteretries', YLeaf(YType.uint32, 'ciscoFlashChipWriteRetries')),
                    ('ciscoflashchiperaseretries', YLeaf(YType.uint32, 'ciscoFlashChipEraseRetries')),
                    ('ciscoflashchipmaxwriteretries', YLeaf(YType.uint32, 'ciscoFlashChipMaxWriteRetries')),
                    ('ciscoflashchipmaxeraseretries', YLeaf(YType.uint32, 'ciscoFlashChipMaxEraseRetries')),
                ])
                self.ciscoflashdeviceindex = None
                self.ciscoflashchipindex = None
                self.ciscoflashchipcode = None
                self.ciscoflashchipdescr = None
                self.ciscoflashchipwriteretries = None
                self.ciscoflashchiperaseretries = None
                self.ciscoflashchipmaxwriteretries = None
                self.ciscoflashchipmaxeraseretries = None
                self._segment_path = lambda: "ciscoFlashChipEntry" + "[ciscoFlashDeviceIndex='" + str(self.ciscoflashdeviceindex) + "']" + "[ciscoFlashChipIndex='" + str(self.ciscoflashchipindex) + "']"
                self._absolute_path = lambda: "CISCO-FLASH-MIB:CISCO-FLASH-MIB/ciscoFlashChipTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOFLASHMIB.Ciscoflashchiptable.Ciscoflashchipentry, ['ciscoflashdeviceindex', 'ciscoflashchipindex', 'ciscoflashchipcode', 'ciscoflashchipdescr', 'ciscoflashchipwriteretries', 'ciscoflashchiperaseretries', 'ciscoflashchipmaxwriteretries', 'ciscoflashchipmaxeraseretries'], name, value)


    class Ciscoflashpartitiontable(Entity):
        """
        Table of flash device partition properties for each
        initialized flash partition. Whenever there is no
        explicit partitioning done, a single partition spanning
        the entire device will be assumed to exist. There will
        therefore always be atleast one partition on a device.
        
        .. attribute:: ciscoflashpartitionentry
        
        	An entry in the table of flash partition properties for each initialized flash partition. Each entry will be indexed by a device number and a partition number within the device
        	**type**\: list of  		 :py:class:`Ciscoflashpartitionentry <ydk.models.cisco_ios_xe.CISCO_FLASH_MIB.CISCOFLASHMIB.Ciscoflashpartitiontable.Ciscoflashpartitionentry>`
        
        

        """

        _prefix = 'CISCO-FLASH-MIB'
        _revision = '2013-08-06'

        def __init__(self):
            super(CISCOFLASHMIB.Ciscoflashpartitiontable, self).__init__()

            self.yang_name = "ciscoFlashPartitionTable"
            self.yang_parent_name = "CISCO-FLASH-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("ciscoFlashPartitionEntry", ("ciscoflashpartitionentry", CISCOFLASHMIB.Ciscoflashpartitiontable.Ciscoflashpartitionentry))])
            self._leafs = OrderedDict()

            self.ciscoflashpartitionentry = YList(self)
            self._segment_path = lambda: "ciscoFlashPartitionTable"
            self._absolute_path = lambda: "CISCO-FLASH-MIB:CISCO-FLASH-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOFLASHMIB.Ciscoflashpartitiontable, [], name, value)


        class Ciscoflashpartitionentry(Entity):
            """
            An entry in the table of flash partition properties
            for each initialized flash partition. Each entry
            will be indexed by a device number and a partition
            number within the device.
            
            .. attribute:: ciscoflashdeviceindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..4294967295
            
            	**refers to**\:  :py:class:`ciscoflashdeviceindex <ydk.models.cisco_ios_xe.CISCO_FLASH_MIB.CISCOFLASHMIB.Ciscoflashdevicetable.Ciscoflashdeviceentry>`
            
            .. attribute:: ciscoflashpartitionindex  (key)
            
            	Flash partition sequence number used to index within table of initialized flash partitions
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: ciscoflashpartitionstartchip
            
            	Chip sequence number of first chip in partition. Used as an index into the chip table
            	**type**\: int
            
            	**range:** 1..64
            
            .. attribute:: ciscoflashpartitionendchip
            
            	Chip sequence number of last chip in partition. Used as an index into the chip table
            	**type**\: int
            
            	**range:** 1..64
            
            .. attribute:: ciscoflashpartitionsize
            
            	Flash partition size. It should be an integral multiple of ciscoFlashDeviceMinPartitionSize. If there is a single partition, this size will be equal to ciscoFlashDeviceSize.  If the size of the flash partition is greater than the maximum value reportable by this object then this object should report its maximum value(4,294,967,295) and ciscoFlashPartitionSizeExtended must be used to report the flash partition's size
            	**type**\: int
            
            	**range:** 1..4294967295
            
            	**units**\: bytes
            
            .. attribute:: ciscoflashpartitionfreespace
            
            	Free space within a Flash partition. Note that the actual size of a file in Flash includes a small overhead that represents the file system's file header. Certain file systems may also have a partition or device header overhead to be considered when computing the free space. Free space will be computed as total partition size less size of all existing files (valid/invalid/deleted files and including file header of each file), less size of any partition header, less size of header of next file to be copied in. In short, this object will give the size of the largest file that can be copied in. The management entity will not be expected to know or use any overheads such as file and partition header lengths, since such overheads may vary from file system to file system. Deleted files in Flash do not free up space. A partition may have to be erased in order to reclaim the space occupied by files.  If the free space within a flash partition is greater than the maximum value reportable by this object then this object should report its maximum value(4,294,967,295) and ciscoFlashPartitionFreeSpaceExtended must be used to report the flash partition's free space
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: bytes
            
            .. attribute:: ciscoflashpartitionfilecount
            
            	Count of all files in a flash partition. Both good and bad (deleted or invalid checksum) files will be included in this count
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ciscoflashpartitionchecksumalgorithm
            
            	Checksum algorithm identifier for checksum method used by the file system. Normally, this would be fixed for a particular file system. When a file system writes a file to Flash, it checksums the data written. The checksum then serves as a way to validate the data read back whenever the file is opened for reading. Since there is no way, when using TFTP, to guarantee that a network download has been error free (since UDP checksums may not have been enabled), this object together with the ciscoFlashFileChecksum object provides a method for any management station to regenerate the checksum of the original file on the server and compare checksums to ensure that the file download to Flash was error free. simpleChecksum represents a simple 1s complement addition of short word values. Other algorithm values will be added as necessary
            	**type**\:  :py:class:`Ciscoflashpartitionchecksumalgorithm <ydk.models.cisco_ios_xe.CISCO_FLASH_MIB.CISCOFLASHMIB.Ciscoflashpartitiontable.Ciscoflashpartitionentry.Ciscoflashpartitionchecksumalgorithm>`
            
            .. attribute:: ciscoflashpartitionstatus
            
            	Flash partition status can be \:  \* readOnly if device is not programmable either because chips could not be recognized or an erroneous mismatch of chips was detected. Chip recognition may fail either because the chips are not supported by the system, or because the Vpp voltage required to identify chips has been disabled via the programming jumper. The ciscoFlashDeviceProgrammingJumper, ciscoFlashChipCode, and ciscoFlashChipDescr objects can be examined to get more details on the cause of this status \* runFromFlash (RFF) if current image is running from this partition. The ciscoFlashPartitionUpgradeMethod object will then indicate whether the Flash Load Helper can be used to write a file to this partition or not.  \* readWrite if partition is programmable
            	**type**\:  :py:class:`Ciscoflashpartitionstatus <ydk.models.cisco_ios_xe.CISCO_FLASH_MIB.CISCOFLASHMIB.Ciscoflashpartitiontable.Ciscoflashpartitionentry.Ciscoflashpartitionstatus>`
            
            .. attribute:: ciscoflashpartitionupgrademethod
            
            	Flash partition upgrade method, ie., method by which new files can be downloaded into the partition. FLH stands for Flash Load Helper, a feature provided on run\-from\-Flash systems for upgrading Flash. This feature uses the bootstrap code in ROMs to help in automatic download. This object should be retrieved if the partition status is runFromFlash(2). If the partition status is readOnly(1), the upgrade method would depend on the reason for the readOnly status. For eg., it may simply be a matter of installing the programming jumper, or it may require execution of a later version of software that supports the Flash chips.  unknown      \-  the current system image does not know                 how Flash can be programmed. A possible                 method would be to reload the ROM image                 and perform the upgrade manually. rxbootFLH    \-  the Flash Load Helper is available to                 download files to Flash. A copy\-to\-flash                 command can be used and this system image                 will automatically reload the Rxboot image                 in ROM and direct it to carry out the                 download request. direct       \-  will be done directly by this image
            	**type**\:  :py:class:`Ciscoflashpartitionupgrademethod <ydk.models.cisco_ios_xe.CISCO_FLASH_MIB.CISCOFLASHMIB.Ciscoflashpartitiontable.Ciscoflashpartitionentry.Ciscoflashpartitionupgrademethod>`
            
            .. attribute:: ciscoflashpartitionname
            
            	Flash partition name used to refer to a partition by the system. This can be any alpha\-numeric character string of the form AAAAAAAAnn, where A represents an optional alpha character and n a numeric character. Any numeric characters must always form the trailing part of the string. The system will strip off the alpha characters and use the numeric portion to map to a partition index. Flash operations get directed to a device partition based on this name. The system has a concept of a default partition. This would be the first partition in the device. The system directs an operation to the default partition whenever a partition name is not specified. The partition name is therefore mandatory except when the operation is being done on the default partition, or the device has just one partition (is not partitioned)
            	**type**\: str
            
            	**length:** 0..16
            
            .. attribute:: ciscoflashpartitionneederasure
            
            	This object indicates whether a partition requires erasure before any write operations can be done in it. A management station should therefore retrieve this object prior to attempting any write operation. A partition requires erasure after it becomes full free space left is less than or equal to the (filesystem file header size). A partition also requires erasure if the system does not find the existence of any file system when it boots up. The partition may be erased explicitly through the erase(5) command, or by using the copyToFlashWithErase(1) command. If a copyToFlashWithoutErase(2) command is issued when this object has the TRUE value, the command will fail
            	**type**\: bool
            
            .. attribute:: ciscoflashpartitionfilenamelength
            
            	Maximum file name length supported by the file system. Max file name length will depend on the file system implemented. Today, all file systems support a max length of at least 48 bytes. A management entity must use this object when prompting a user for, or deriving the Flash file name length
            	**type**\: int
            
            	**range:** 1..256
            
            .. attribute:: ciscoflashpartitionsizeextended
            
            	Flash partition size. It should be an integral multiple of ciscoFlashDeviceMinPartitionSize. If there is a single partition, this size will be equal to ciscoFlashDeviceSize.  This object is a 64\-bit version of ciscoFlashPartitionSize
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: bytes
            
            .. attribute:: ciscoflashpartitionfreespaceextended
            
            	Free space within a Flash partition. Note that the actual size of a file in Flash includes a small overhead that represents the file system's file header. Certain file systems may also have a partition or device header overhead to be considered when computing the free space. Free space will be computed as total partition size less size of all existing files (valid/invalid/deleted files and including file header of each file), less size of any partition header, less size of header of next file to be copied in. In short, this object will give the size of the largest file that can be copied in. The management entity will not be expected to know or use any overheads such as file and partition header lengths, since such overheads may vary from file system to file system. Deleted files in Flash do not free up space. A partition may have to be erased in order to reclaim the space occupied by files.  This object is a 64\-bit version of ciscoFlashPartitionFreeSpace
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: bytes
            
            .. attribute:: ciscoflashpartitionlowspacenotifthreshold
            
            	This object specifies the minimum threshold value in percentage of free space for each partition. If the free space available goes below this threshold value and if ciscoFlashPartionLowSpaceNotifEnable is set to true, ciscoFlashPartitionLowSpaceNotif will be generated. When the available free space comes back to the threshold value ciscoFlashPartionLowSpaceRecoveryNotif will be generated
            	**type**\: int
            
            	**range:** 0..100
            
            

            """

            _prefix = 'CISCO-FLASH-MIB'
            _revision = '2013-08-06'

            def __init__(self):
                super(CISCOFLASHMIB.Ciscoflashpartitiontable.Ciscoflashpartitionentry, self).__init__()

                self.yang_name = "ciscoFlashPartitionEntry"
                self.yang_parent_name = "ciscoFlashPartitionTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ciscoflashdeviceindex','ciscoflashpartitionindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ciscoflashdeviceindex', YLeaf(YType.str, 'ciscoFlashDeviceIndex')),
                    ('ciscoflashpartitionindex', YLeaf(YType.uint32, 'ciscoFlashPartitionIndex')),
                    ('ciscoflashpartitionstartchip', YLeaf(YType.int32, 'ciscoFlashPartitionStartChip')),
                    ('ciscoflashpartitionendchip', YLeaf(YType.int32, 'ciscoFlashPartitionEndChip')),
                    ('ciscoflashpartitionsize', YLeaf(YType.uint32, 'ciscoFlashPartitionSize')),
                    ('ciscoflashpartitionfreespace', YLeaf(YType.uint32, 'ciscoFlashPartitionFreeSpace')),
                    ('ciscoflashpartitionfilecount', YLeaf(YType.uint32, 'ciscoFlashPartitionFileCount')),
                    ('ciscoflashpartitionchecksumalgorithm', YLeaf(YType.enumeration, 'ciscoFlashPartitionChecksumAlgorithm')),
                    ('ciscoflashpartitionstatus', YLeaf(YType.enumeration, 'ciscoFlashPartitionStatus')),
                    ('ciscoflashpartitionupgrademethod', YLeaf(YType.enumeration, 'ciscoFlashPartitionUpgradeMethod')),
                    ('ciscoflashpartitionname', YLeaf(YType.str, 'ciscoFlashPartitionName')),
                    ('ciscoflashpartitionneederasure', YLeaf(YType.boolean, 'ciscoFlashPartitionNeedErasure')),
                    ('ciscoflashpartitionfilenamelength', YLeaf(YType.int32, 'ciscoFlashPartitionFileNameLength')),
                    ('ciscoflashpartitionsizeextended', YLeaf(YType.uint64, 'ciscoFlashPartitionSizeExtended')),
                    ('ciscoflashpartitionfreespaceextended', YLeaf(YType.uint64, 'ciscoFlashPartitionFreeSpaceExtended')),
                    ('ciscoflashpartitionlowspacenotifthreshold', YLeaf(YType.int32, 'ciscoFlashPartitionLowSpaceNotifThreshold')),
                ])
                self.ciscoflashdeviceindex = None
                self.ciscoflashpartitionindex = None
                self.ciscoflashpartitionstartchip = None
                self.ciscoflashpartitionendchip = None
                self.ciscoflashpartitionsize = None
                self.ciscoflashpartitionfreespace = None
                self.ciscoflashpartitionfilecount = None
                self.ciscoflashpartitionchecksumalgorithm = None
                self.ciscoflashpartitionstatus = None
                self.ciscoflashpartitionupgrademethod = None
                self.ciscoflashpartitionname = None
                self.ciscoflashpartitionneederasure = None
                self.ciscoflashpartitionfilenamelength = None
                self.ciscoflashpartitionsizeextended = None
                self.ciscoflashpartitionfreespaceextended = None
                self.ciscoflashpartitionlowspacenotifthreshold = None
                self._segment_path = lambda: "ciscoFlashPartitionEntry" + "[ciscoFlashDeviceIndex='" + str(self.ciscoflashdeviceindex) + "']" + "[ciscoFlashPartitionIndex='" + str(self.ciscoflashpartitionindex) + "']"
                self._absolute_path = lambda: "CISCO-FLASH-MIB:CISCO-FLASH-MIB/ciscoFlashPartitionTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOFLASHMIB.Ciscoflashpartitiontable.Ciscoflashpartitionentry, ['ciscoflashdeviceindex', 'ciscoflashpartitionindex', 'ciscoflashpartitionstartchip', 'ciscoflashpartitionendchip', 'ciscoflashpartitionsize', 'ciscoflashpartitionfreespace', 'ciscoflashpartitionfilecount', 'ciscoflashpartitionchecksumalgorithm', 'ciscoflashpartitionstatus', 'ciscoflashpartitionupgrademethod', 'ciscoflashpartitionname', 'ciscoflashpartitionneederasure', 'ciscoflashpartitionfilenamelength', 'ciscoflashpartitionsizeextended', 'ciscoflashpartitionfreespaceextended', 'ciscoflashpartitionlowspacenotifthreshold'], name, value)

            class Ciscoflashpartitionchecksumalgorithm(Enum):
                """
                Ciscoflashpartitionchecksumalgorithm (Enum Class)

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

                .. data:: simpleChecksum = 1

                .. data:: undefined = 2

                .. data:: simpleCRC = 3

                """

                simpleChecksum = Enum.YLeaf(1, "simpleChecksum")

                undefined = Enum.YLeaf(2, "undefined")

                simpleCRC = Enum.YLeaf(3, "simpleCRC")


            class Ciscoflashpartitionstatus(Enum):
                """
                Ciscoflashpartitionstatus (Enum Class)

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

                .. data:: readOnly = 1

                .. data:: runFromFlash = 2

                .. data:: readWrite = 3

                """

                readOnly = Enum.YLeaf(1, "readOnly")

                runFromFlash = Enum.YLeaf(2, "runFromFlash")

                readWrite = Enum.YLeaf(3, "readWrite")


            class Ciscoflashpartitionupgrademethod(Enum):
                """
                Ciscoflashpartitionupgrademethod (Enum Class)

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

                .. data:: unknown = 1

                .. data:: rxbootFLH = 2

                .. data:: direct = 3

                """

                unknown = Enum.YLeaf(1, "unknown")

                rxbootFLH = Enum.YLeaf(2, "rxbootFLH")

                direct = Enum.YLeaf(3, "direct")



    class Ciscoflashfiletable(Entity):
        """
        Table of information for files in a Flash partition.
        
        .. attribute:: ciscoflashfileentry
        
        	An entry in the table of Flash file properties for each initialized Flash partition. Each entry represents a file and gives details about the file. An entry is indexed using the device number, partition number within the device, and file number within the partition
        	**type**\: list of  		 :py:class:`Ciscoflashfileentry <ydk.models.cisco_ios_xe.CISCO_FLASH_MIB.CISCOFLASHMIB.Ciscoflashfiletable.Ciscoflashfileentry>`
        
        

        """

        _prefix = 'CISCO-FLASH-MIB'
        _revision = '2013-08-06'

        def __init__(self):
            super(CISCOFLASHMIB.Ciscoflashfiletable, self).__init__()

            self.yang_name = "ciscoFlashFileTable"
            self.yang_parent_name = "CISCO-FLASH-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("ciscoFlashFileEntry", ("ciscoflashfileentry", CISCOFLASHMIB.Ciscoflashfiletable.Ciscoflashfileentry))])
            self._leafs = OrderedDict()

            self.ciscoflashfileentry = YList(self)
            self._segment_path = lambda: "ciscoFlashFileTable"
            self._absolute_path = lambda: "CISCO-FLASH-MIB:CISCO-FLASH-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOFLASHMIB.Ciscoflashfiletable, [], name, value)


        class Ciscoflashfileentry(Entity):
            """
            An entry in the table of Flash file properties
            for each initialized Flash partition. Each entry
            represents a file and gives details about the file.
            An entry is indexed using the device number,
            partition number within the device, and file
            number within the partition.
            
            .. attribute:: ciscoflashdeviceindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..4294967295
            
            	**refers to**\:  :py:class:`ciscoflashdeviceindex <ydk.models.cisco_ios_xe.CISCO_FLASH_MIB.CISCOFLASHMIB.Ciscoflashdevicetable.Ciscoflashdeviceentry>`
            
            .. attribute:: ciscoflashpartitionindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..4294967295
            
            	**refers to**\:  :py:class:`ciscoflashpartitionindex <ydk.models.cisco_ios_xe.CISCO_FLASH_MIB.CISCOFLASHMIB.Ciscoflashpartitiontable.Ciscoflashpartitionentry>`
            
            .. attribute:: ciscoflashfileindex  (key)
            
            	Flash file sequence number used to index within a Flash partition directory table
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: ciscoflashfilesize
            
            	Size of the file in bytes. Note that this size does not include the size of the filesystem file header. File size will always be non\-zero
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: bytes
            
            .. attribute:: ciscoflashfilechecksum
            
            	File checksum stored in the file header. This checksum is computed and stored when the file is written into Flash. It serves to validate the data written into Flash. Whereas the system will generate and store the checksum internally in hexadecimal form, this object will provide the checksum in a string form. The checksum will be available for all valid and invalid\-checksum files
            	**type**\: str
            
            .. attribute:: ciscoflashfilestatus
            
            	Status of a file. A file could be explicitly deleted if the file system supports such a user command facility. Alternately, an existing good file would be automatically deleted if another good file with the same name were copied in. Note that deleted files continue to occupy prime Flash real estate.  A file is marked as having an invalid checksum if any checksum mismatch was detected while writing or reading the file. Incomplete files (files truncated either because of lack of free space, or a network download failure) are also written with a bad checksum and marked as invalid
            	**type**\:  :py:class:`Ciscoflashfilestatus <ydk.models.cisco_ios_xe.CISCO_FLASH_MIB.CISCOFLASHMIB.Ciscoflashfiletable.Ciscoflashfileentry.Ciscoflashfilestatus>`
            
            .. attribute:: ciscoflashfilename
            
            	Flash file name as specified by the user copying in the file. The name should not include the colon (\:) character as it is a special separator character used to delineate the device name, partition name, and the file name
            	**type**\: str
            
            	**length:** 1..255
            
            .. attribute:: ciscoflashfiletype
            
            	Type of the file
            	**type**\:  :py:class:`FlashFileType <ydk.models.cisco_ios_xe.CISCO_FLASH_MIB.FlashFileType>`
            
            .. attribute:: ciscoflashfiledate
            
            	The time at which this file was created
            	**type**\: str
            
            

            """

            _prefix = 'CISCO-FLASH-MIB'
            _revision = '2013-08-06'

            def __init__(self):
                super(CISCOFLASHMIB.Ciscoflashfiletable.Ciscoflashfileentry, self).__init__()

                self.yang_name = "ciscoFlashFileEntry"
                self.yang_parent_name = "ciscoFlashFileTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ciscoflashdeviceindex','ciscoflashpartitionindex','ciscoflashfileindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ciscoflashdeviceindex', YLeaf(YType.str, 'ciscoFlashDeviceIndex')),
                    ('ciscoflashpartitionindex', YLeaf(YType.str, 'ciscoFlashPartitionIndex')),
                    ('ciscoflashfileindex', YLeaf(YType.uint32, 'ciscoFlashFileIndex')),
                    ('ciscoflashfilesize', YLeaf(YType.uint32, 'ciscoFlashFileSize')),
                    ('ciscoflashfilechecksum', YLeaf(YType.str, 'ciscoFlashFileChecksum')),
                    ('ciscoflashfilestatus', YLeaf(YType.enumeration, 'ciscoFlashFileStatus')),
                    ('ciscoflashfilename', YLeaf(YType.str, 'ciscoFlashFileName')),
                    ('ciscoflashfiletype', YLeaf(YType.enumeration, 'ciscoFlashFileType')),
                    ('ciscoflashfiledate', YLeaf(YType.str, 'ciscoFlashFileDate')),
                ])
                self.ciscoflashdeviceindex = None
                self.ciscoflashpartitionindex = None
                self.ciscoflashfileindex = None
                self.ciscoflashfilesize = None
                self.ciscoflashfilechecksum = None
                self.ciscoflashfilestatus = None
                self.ciscoflashfilename = None
                self.ciscoflashfiletype = None
                self.ciscoflashfiledate = None
                self._segment_path = lambda: "ciscoFlashFileEntry" + "[ciscoFlashDeviceIndex='" + str(self.ciscoflashdeviceindex) + "']" + "[ciscoFlashPartitionIndex='" + str(self.ciscoflashpartitionindex) + "']" + "[ciscoFlashFileIndex='" + str(self.ciscoflashfileindex) + "']"
                self._absolute_path = lambda: "CISCO-FLASH-MIB:CISCO-FLASH-MIB/ciscoFlashFileTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOFLASHMIB.Ciscoflashfiletable.Ciscoflashfileentry, ['ciscoflashdeviceindex', 'ciscoflashpartitionindex', 'ciscoflashfileindex', 'ciscoflashfilesize', 'ciscoflashfilechecksum', 'ciscoflashfilestatus', 'ciscoflashfilename', 'ciscoflashfiletype', 'ciscoflashfiledate'], name, value)

            class Ciscoflashfilestatus(Enum):
                """
                Ciscoflashfilestatus (Enum Class)

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

                .. data:: deleted = 1

                .. data:: invalidChecksum = 2

                .. data:: valid = 3

                """

                deleted = Enum.YLeaf(1, "deleted")

                invalidChecksum = Enum.YLeaf(2, "invalidChecksum")

                valid = Enum.YLeaf(3, "valid")



    class Ciscoflashfilebytypetable(Entity):
        """
        Table of information for files on the manageable
        flash devices sorted by File Types.
        
        .. attribute:: ciscoflashfilebytypeentry
        
        	An entry in the table of Flash file properties for each initialized Flash partition. Each entry represents a file sorted by file type.  This table contains exactly the same set of rows as are contained in the ciscoFlashFileTable but in a different order, i.e., ordered by  the type of file, given by  ciscoFlashFileType; the device number, given by ciscoFlashDeviceIndex; the partition number within the device, given by ciscoFlashPartitionIndex; the file number within the partition, given by ciscoFlashFileIndex
        	**type**\: list of  		 :py:class:`Ciscoflashfilebytypeentry <ydk.models.cisco_ios_xe.CISCO_FLASH_MIB.CISCOFLASHMIB.Ciscoflashfilebytypetable.Ciscoflashfilebytypeentry>`
        
        

        """

        _prefix = 'CISCO-FLASH-MIB'
        _revision = '2013-08-06'

        def __init__(self):
            super(CISCOFLASHMIB.Ciscoflashfilebytypetable, self).__init__()

            self.yang_name = "ciscoFlashFileByTypeTable"
            self.yang_parent_name = "CISCO-FLASH-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("ciscoFlashFileByTypeEntry", ("ciscoflashfilebytypeentry", CISCOFLASHMIB.Ciscoflashfilebytypetable.Ciscoflashfilebytypeentry))])
            self._leafs = OrderedDict()

            self.ciscoflashfilebytypeentry = YList(self)
            self._segment_path = lambda: "ciscoFlashFileByTypeTable"
            self._absolute_path = lambda: "CISCO-FLASH-MIB:CISCO-FLASH-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOFLASHMIB.Ciscoflashfilebytypetable, [], name, value)


        class Ciscoflashfilebytypeentry(Entity):
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
            
            .. attribute:: ciscoflashfiletype  (key)
            
            	
            	**type**\:  :py:class:`FlashFileType <ydk.models.cisco_ios_xe.CISCO_FLASH_MIB.FlashFileType>`
            
            .. attribute:: ciscoflashdeviceindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..4294967295
            
            	**refers to**\:  :py:class:`ciscoflashdeviceindex <ydk.models.cisco_ios_xe.CISCO_FLASH_MIB.CISCOFLASHMIB.Ciscoflashdevicetable.Ciscoflashdeviceentry>`
            
            .. attribute:: ciscoflashpartitionindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..4294967295
            
            	**refers to**\:  :py:class:`ciscoflashpartitionindex <ydk.models.cisco_ios_xe.CISCO_FLASH_MIB.CISCOFLASHMIB.Ciscoflashpartitiontable.Ciscoflashpartitionentry>`
            
            .. attribute:: ciscoflashfileindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..4294967295
            
            	**refers to**\:  :py:class:`ciscoflashfileindex <ydk.models.cisco_ios_xe.CISCO_FLASH_MIB.CISCOFLASHMIB.Ciscoflashfiletable.Ciscoflashfileentry>`
            
            .. attribute:: ciscoflashfilebytypesize
            
            	This object represents exactly the same info as ciscoFlashFileSize object in ciscoFlashFileTable
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: bytes
            
            .. attribute:: ciscoflashfilebytypechecksum
            
            	This object represents exactly the same info as ciscoFlashFileChecksum object in ciscoFlashFileTable
            	**type**\: str
            
            .. attribute:: ciscoflashfilebytypestatus
            
            	This object represents exactly the same info as ciscoFlashFileStatus object in ciscoFlashFileTable
            	**type**\:  :py:class:`Ciscoflashfilebytypestatus <ydk.models.cisco_ios_xe.CISCO_FLASH_MIB.CISCOFLASHMIB.Ciscoflashfilebytypetable.Ciscoflashfilebytypeentry.Ciscoflashfilebytypestatus>`
            
            .. attribute:: ciscoflashfilebytypename
            
            	This object represents exactly the same info as ciscoFlashFileName object in ciscoFlashFileTable
            	**type**\: str
            
            	**length:** 1..255
            
            .. attribute:: ciscoflashfilebytypedate
            
            	This object represents exactly the same info as ciscoFlashFileDate object in ciscoFlashFileTable
            	**type**\: str
            
            

            """

            _prefix = 'CISCO-FLASH-MIB'
            _revision = '2013-08-06'

            def __init__(self):
                super(CISCOFLASHMIB.Ciscoflashfilebytypetable.Ciscoflashfilebytypeentry, self).__init__()

                self.yang_name = "ciscoFlashFileByTypeEntry"
                self.yang_parent_name = "ciscoFlashFileByTypeTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ciscoflashfiletype','ciscoflashdeviceindex','ciscoflashpartitionindex','ciscoflashfileindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ciscoflashfiletype', YLeaf(YType.enumeration, 'ciscoFlashFileType')),
                    ('ciscoflashdeviceindex', YLeaf(YType.str, 'ciscoFlashDeviceIndex')),
                    ('ciscoflashpartitionindex', YLeaf(YType.str, 'ciscoFlashPartitionIndex')),
                    ('ciscoflashfileindex', YLeaf(YType.str, 'ciscoFlashFileIndex')),
                    ('ciscoflashfilebytypesize', YLeaf(YType.uint32, 'ciscoFlashFileByTypeSize')),
                    ('ciscoflashfilebytypechecksum', YLeaf(YType.str, 'ciscoFlashFileByTypeChecksum')),
                    ('ciscoflashfilebytypestatus', YLeaf(YType.enumeration, 'ciscoFlashFileByTypeStatus')),
                    ('ciscoflashfilebytypename', YLeaf(YType.str, 'ciscoFlashFileByTypeName')),
                    ('ciscoflashfilebytypedate', YLeaf(YType.str, 'ciscoFlashFileByTypeDate')),
                ])
                self.ciscoflashfiletype = None
                self.ciscoflashdeviceindex = None
                self.ciscoflashpartitionindex = None
                self.ciscoflashfileindex = None
                self.ciscoflashfilebytypesize = None
                self.ciscoflashfilebytypechecksum = None
                self.ciscoflashfilebytypestatus = None
                self.ciscoflashfilebytypename = None
                self.ciscoflashfilebytypedate = None
                self._segment_path = lambda: "ciscoFlashFileByTypeEntry" + "[ciscoFlashFileType='" + str(self.ciscoflashfiletype) + "']" + "[ciscoFlashDeviceIndex='" + str(self.ciscoflashdeviceindex) + "']" + "[ciscoFlashPartitionIndex='" + str(self.ciscoflashpartitionindex) + "']" + "[ciscoFlashFileIndex='" + str(self.ciscoflashfileindex) + "']"
                self._absolute_path = lambda: "CISCO-FLASH-MIB:CISCO-FLASH-MIB/ciscoFlashFileByTypeTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOFLASHMIB.Ciscoflashfilebytypetable.Ciscoflashfilebytypeentry, ['ciscoflashfiletype', 'ciscoflashdeviceindex', 'ciscoflashpartitionindex', 'ciscoflashfileindex', 'ciscoflashfilebytypesize', 'ciscoflashfilebytypechecksum', 'ciscoflashfilebytypestatus', 'ciscoflashfilebytypename', 'ciscoflashfilebytypedate'], name, value)

            class Ciscoflashfilebytypestatus(Enum):
                """
                Ciscoflashfilebytypestatus (Enum Class)

                This object represents exactly the

                same info as ciscoFlashFileStatus

                object in ciscoFlashFileTable.

                .. data:: deleted = 1

                .. data:: invalidChecksum = 2

                .. data:: valid = 3

                """

                deleted = Enum.YLeaf(1, "deleted")

                invalidChecksum = Enum.YLeaf(2, "invalidChecksum")

                valid = Enum.YLeaf(3, "valid")



    class Ciscoflashcopytable(Entity):
        """
        A table of Flash copy operation entries. Each
        entry represents a Flash copy operation (to or
        from Flash) that has been initiated.
        
        .. attribute:: ciscoflashcopyentry
        
        	A Flash copy operation entry. Each entry consists of a command, a source, and optional parameters such as protocol to be used, a destination, a server address, etc.  A management station wishing to create an entry should first generate a pseudo\-random serial number to be used as the index to this sparse table.  The station should then create the associated instance of the row status object. It must also, either in the same or in successive PDUs, create the associated instance of the command and parameter objects. It should also modify the default values for any of the parameter objects if the defaults are not appropriate.  Once the appropriate instances of all the command objects have been created, either by an explicit SNMP set request or by default, the row status should be set to active to initiate the operation. Note that this entire procedure may be initiated via a single set request which specifies a row status  of createAndGo as well as specifies valid values for the non\-defaulted parameter objects.  Once an operation has been activated, it cannot be stopped.  Once the operation completes, the management station should retrieve the value of the status object (and time if desired), and delete the entry.  In order to prevent old entries from clogging the table, entries will be aged out, but an entry will never be deleted within 5 minutes of completing
        	**type**\: list of  		 :py:class:`Ciscoflashcopyentry <ydk.models.cisco_ios_xe.CISCO_FLASH_MIB.CISCOFLASHMIB.Ciscoflashcopytable.Ciscoflashcopyentry>`
        
        

        """

        _prefix = 'CISCO-FLASH-MIB'
        _revision = '2013-08-06'

        def __init__(self):
            super(CISCOFLASHMIB.Ciscoflashcopytable, self).__init__()

            self.yang_name = "ciscoFlashCopyTable"
            self.yang_parent_name = "CISCO-FLASH-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("ciscoFlashCopyEntry", ("ciscoflashcopyentry", CISCOFLASHMIB.Ciscoflashcopytable.Ciscoflashcopyentry))])
            self._leafs = OrderedDict()

            self.ciscoflashcopyentry = YList(self)
            self._segment_path = lambda: "ciscoFlashCopyTable"
            self._absolute_path = lambda: "CISCO-FLASH-MIB:CISCO-FLASH-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOFLASHMIB.Ciscoflashcopytable, [], name, value)


        class Ciscoflashcopyentry(Entity):
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
            
            .. attribute:: ciscoflashcopyserialnumber  (key)
            
            	Object which specifies a unique entry in the table. A management station wishing to initiate a copy operation should use a pseudo\-random value for this object when creating or modifying an instance of a ciscoFlashCopyEntry
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: ciscoflashcopycommand
            
            	The copy command to be executed. Mandatory. Note that it is possible for a system to support multiple file systems (different file systems on different Flash devices, or different file systems on different partitions within a device). Each such file system may support only a subset of these commands. If a command is unsupported, the invalidOperation(3) error will be reported in the operation status.  Command                 Remarks copyToFlashWithErase    Copy a file to flash; erase                         flash before copy.                         Use the TFTP or rcp protocol. copyToFlashWithoutErase Copy a file to flash; do not                         erase.                         Note that this command will fail                         if the PartitionNeedErasure                         object specifies that the                         partition being copied to needs                         erasure.                         Use the TFTP or rcp protocol. copyFromFlash           Copy a file from flash using                         the TFTP, rcp or lex protocol.                         Note that the lex protocol                         can only be used to copy to a                         lex device. copyFromFlhLog          Copy contents of FLH log to                         server using TFTP protocol.   Command table           Parameters copyToFlashWithErase    CopyProtocol                         CopyServerAddress                         CopySourceName                         CopyDestinationName (opt)                         CopyRemoteUserName (opt)                         CopyNotifyOnCompletion (opt) copyToFlashWithoutErase CopyProtocol                         CopyServerAddress                         CopySourceName                         CopyDestinationName (opt)                         CopyRemoteUserName (opt)                         CopyNotifyOnCompletion (opt) copyFromFlash           CopyProtocol                         CopyServerAddress                         CopySourceName                         CopyDestinationName (opt)                         CopyRemoteUserName (opt)                         CopyNotifyOnCompletion (opt) copyFromFlhLog          CopyProtocol                         CopyServerAddress                         CopyDestinationName                         CopyNotifyOnCompletion (opt)
            	**type**\:  :py:class:`Ciscoflashcopycommand <ydk.models.cisco_ios_xe.CISCO_FLASH_MIB.CISCOFLASHMIB.Ciscoflashcopytable.Ciscoflashcopyentry.Ciscoflashcopycommand>`
            
            .. attribute:: ciscoflashcopyprotocol
            
            	The protocol to be used for any copy. Optional. Will default to tftp if not specified.  Since feature support depends on a software release, version number within the release, platform, and maybe the image type (subset type), a management station would be expected to somehow determine the protocol support for a command
            	**type**\:  :py:class:`Ciscoflashcopyprotocol <ydk.models.cisco_ios_xe.CISCO_FLASH_MIB.CISCOFLASHMIB.Ciscoflashcopytable.Ciscoflashcopyentry.Ciscoflashcopyprotocol>`
            
            .. attribute:: ciscoflashcopyserveraddress
            
            	The server address to be used for any copy. Optional. Will default to 'FFFFFFFF'H  (or 255.255.255.255).  Since this object can just hold only IPv4 Transport type, it is deprecated and replaced by ciscoFlashCopyServerAddrRev1
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**status**\: deprecated
            
            .. attribute:: ciscoflashcopysourcename
            
            	Source file name, either in Flash or on a server, depending on the type of copy command. Mandatory.  For a copy from Flash\: File name must be of the form         [device>\:][\:] where  is a value obtained from FlashDeviceName,          is obtained from FlashPartitionName     and  is the name of a file in Flash. A management station could derive its own partition name as per the description for the ciscoFlashPartitionName object. If <device> is not specified, the default Flash device will be assumed. If <partition> is not specified, the default partition will be assumed. If a device is not partitioned into 2 or more partitions, this value may be left out.  For a copy to Flash, the file name will be as per the file naming conventions and path to the file on the server
            	**type**\: str
            
            	**length:** 1..255
            
            .. attribute:: ciscoflashcopydestinationname
            
            	Destination file name.  For a copy to Flash\: File name must be of the form         {device>\:][<partition>\:]<file> where <device> is a value obtained from FlashDeviceName,       <partition> is obtained from FlashPartitionName   and <file> is any character string that does not have embedded colon characters. A management station could derive its own partition name as per the description for the ciscoFlashPartitionName object. If <device> is not specified, the default Flash device will be assumed. If <partition> is not specified, the default partition will be assumed. If a device is not partitioned into 2 or more partitions, this value may be left out. If <file> is not specified, it will default to <file> specified in ciscoFlashCopySourceName.  For a copy from Flash via tftp or rcp, the file name will be as per the file naming conventions and destination sub\-directory on the server. If not specified, <file> from the source file name will be used. For a copy from Flash via lex, this string will consist of numeric characters specifying the interface on the lex box that will receive the source flash image
            	**type**\: str
            
            	**length:** 0..255
            
            .. attribute:: ciscoflashcopyremoteusername
            
            	Remote user name for copy via rcp protocol. Optional. This object will be ignored for protocols other than rcp. If specified, it will override the remote user\-name configured through the         rcmd remote\-username configuration command. The remote user\-name is sent as the server user\-name in an rcp command request sent by the system to a remote rcp server
            	**type**\: str
            
            	**length:** 1..255
            
            .. attribute:: ciscoflashcopystatus
            
            	The status of the specified copy operation.  copyOperationPending \:         operation request is received and         pending for validation and process  copyInProgress \:         specified operation is active  copyOperationSuccess \:         specified operation is supported and         completed successfully  copyInvalidOperation \:         command invalid or command\-protocol\-device         combination unsupported  copyInvalidProtocol \:         invalid protocol specified  copyInvalidSourceName \:         invalid source file name specified         For the  copy from flash to lex operation, this         error code will be returned when the source file         is not a valid lex image.  copyInvalidDestName \:         invalid target name (file or partition or         device name) specified         For the  copy from flash to lex operation, this         error code will be returned when no lex devices         are connected to the router or when an invalid         lex interface number has been specified in         the destination string.  copyInvalidServerAddress \:         invalid server address specified  copyDeviceBusy \:         specified device is in use and locked by         another process  copyDeviceOpenError \:         invalid device name  copyDeviceError \:         device read, write or erase error  copyDeviceNotProgrammable \:         device is read\-only but a write or erase         operation was specified  copyDeviceFull \:         device is filled to capacity  copyFileOpenError \:         invalid file name; file not found in partition  copyFileTransferError \:         file transfer was unsuccessfull; network failure  copyFileChecksumError \:         file checksum in Flash failed  copyNoMemory \:         system running low on memory  copyUnknownFailure \:         failure unknown  copyProhibited\:       stop user from overwriting current boot image file
            	**type**\:  :py:class:`Ciscoflashcopystatus <ydk.models.cisco_ios_xe.CISCO_FLASH_MIB.CISCOFLASHMIB.Ciscoflashcopytable.Ciscoflashcopyentry.Ciscoflashcopystatus>`
            
            .. attribute:: ciscoflashcopynotifyoncompletion
            
            	Specifies whether or not a notification should be generated on the completion of the copy operation. If specified, ciscoFlashCopyCompletionTrap will be generated. It is the responsibility of the management entity to ensure that the SNMP administrative model is configured in such a way as to allow the notification to be delivered
            	**type**\: bool
            
            .. attribute:: ciscoflashcopytime
            
            	Time taken for the copy operation. This object will be like a stopwatch, starting when the operation starts, stopping when the operation completes. If a management entity keeps a database of completion times for various operations, it can then use the stopwatch capability to display percentage completion time
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ciscoflashcopyentrystatus
            
            	The status of this table entry
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            .. attribute:: ciscoflashcopyverify
            
            	Specifies whether the file that is copied need to be verified for integrity / authenticity, after copy succeeds. If it is set to true, and if the file that is copied doesn't have integrity /authenticity attachement, or the integrity / authenticity check fails, then the command will be aborted, and the file that is copied will be deleted from the destination file system
            	**type**\: bool
            
            .. attribute:: ciscoflashcopyserveraddrtype
            
            	This object indicates the transport type of the address contained in ciscoFlashCopyServerAddrRev1. Optional. Will default to '1' (IPv4 address type)
            	**type**\:  :py:class:`InetAddressType <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetAddressType>`
            
            .. attribute:: ciscoflashcopyserveraddrrev1
            
            	The server address to be used for any copy. Optional. Will default to 'FFFFFFFF'H  (or 255.255.255.255).  The Format of this address depends on the value of the ciscoFlashCopyServerAddrType.  This object deprecates the old ciscoFlashCopyServerAddress object
            	**type**\: str
            
            	**length:** 0..255
            
            .. attribute:: ciscoflashcopyremotepassword
            
            	Password used by ftp, sftp or scp for copying a file to/from an ftp/sftp/scp server. This object must be created when the ciscoFlashCopyProtocol is ftp, sftp or scp. Reading it returns a zero\-length string for security reasons
            	**type**\: str
            
            	**length:** 1..40
            
            

            """

            _prefix = 'CISCO-FLASH-MIB'
            _revision = '2013-08-06'

            def __init__(self):
                super(CISCOFLASHMIB.Ciscoflashcopytable.Ciscoflashcopyentry, self).__init__()

                self.yang_name = "ciscoFlashCopyEntry"
                self.yang_parent_name = "ciscoFlashCopyTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ciscoflashcopyserialnumber']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ciscoflashcopyserialnumber', YLeaf(YType.int32, 'ciscoFlashCopySerialNumber')),
                    ('ciscoflashcopycommand', YLeaf(YType.enumeration, 'ciscoFlashCopyCommand')),
                    ('ciscoflashcopyprotocol', YLeaf(YType.enumeration, 'ciscoFlashCopyProtocol')),
                    ('ciscoflashcopyserveraddress', YLeaf(YType.str, 'ciscoFlashCopyServerAddress')),
                    ('ciscoflashcopysourcename', YLeaf(YType.str, 'ciscoFlashCopySourceName')),
                    ('ciscoflashcopydestinationname', YLeaf(YType.str, 'ciscoFlashCopyDestinationName')),
                    ('ciscoflashcopyremoteusername', YLeaf(YType.str, 'ciscoFlashCopyRemoteUserName')),
                    ('ciscoflashcopystatus', YLeaf(YType.enumeration, 'ciscoFlashCopyStatus')),
                    ('ciscoflashcopynotifyoncompletion', YLeaf(YType.boolean, 'ciscoFlashCopyNotifyOnCompletion')),
                    ('ciscoflashcopytime', YLeaf(YType.uint32, 'ciscoFlashCopyTime')),
                    ('ciscoflashcopyentrystatus', YLeaf(YType.enumeration, 'ciscoFlashCopyEntryStatus')),
                    ('ciscoflashcopyverify', YLeaf(YType.boolean, 'ciscoFlashCopyVerify')),
                    ('ciscoflashcopyserveraddrtype', YLeaf(YType.enumeration, 'ciscoFlashCopyServerAddrType')),
                    ('ciscoflashcopyserveraddrrev1', YLeaf(YType.str, 'ciscoFlashCopyServerAddrRev1')),
                    ('ciscoflashcopyremotepassword', YLeaf(YType.str, 'ciscoFlashCopyRemotePassword')),
                ])
                self.ciscoflashcopyserialnumber = None
                self.ciscoflashcopycommand = None
                self.ciscoflashcopyprotocol = None
                self.ciscoflashcopyserveraddress = None
                self.ciscoflashcopysourcename = None
                self.ciscoflashcopydestinationname = None
                self.ciscoflashcopyremoteusername = None
                self.ciscoflashcopystatus = None
                self.ciscoflashcopynotifyoncompletion = None
                self.ciscoflashcopytime = None
                self.ciscoflashcopyentrystatus = None
                self.ciscoflashcopyverify = None
                self.ciscoflashcopyserveraddrtype = None
                self.ciscoflashcopyserveraddrrev1 = None
                self.ciscoflashcopyremotepassword = None
                self._segment_path = lambda: "ciscoFlashCopyEntry" + "[ciscoFlashCopySerialNumber='" + str(self.ciscoflashcopyserialnumber) + "']"
                self._absolute_path = lambda: "CISCO-FLASH-MIB:CISCO-FLASH-MIB/ciscoFlashCopyTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOFLASHMIB.Ciscoflashcopytable.Ciscoflashcopyentry, ['ciscoflashcopyserialnumber', 'ciscoflashcopycommand', 'ciscoflashcopyprotocol', 'ciscoflashcopyserveraddress', 'ciscoflashcopysourcename', 'ciscoflashcopydestinationname', 'ciscoflashcopyremoteusername', 'ciscoflashcopystatus', 'ciscoflashcopynotifyoncompletion', 'ciscoflashcopytime', 'ciscoflashcopyentrystatus', 'ciscoflashcopyverify', 'ciscoflashcopyserveraddrtype', 'ciscoflashcopyserveraddrrev1', 'ciscoflashcopyremotepassword'], name, value)

            class Ciscoflashcopycommand(Enum):
                """
                Ciscoflashcopycommand (Enum Class)

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

                .. data:: copyToFlashWithErase = 1

                .. data:: copyToFlashWithoutErase = 2

                .. data:: copyFromFlash = 3

                .. data:: copyFromFlhLog = 4

                """

                copyToFlashWithErase = Enum.YLeaf(1, "copyToFlashWithErase")

                copyToFlashWithoutErase = Enum.YLeaf(2, "copyToFlashWithoutErase")

                copyFromFlash = Enum.YLeaf(3, "copyFromFlash")

                copyFromFlhLog = Enum.YLeaf(4, "copyFromFlhLog")


            class Ciscoflashcopyprotocol(Enum):
                """
                Ciscoflashcopyprotocol (Enum Class)

                The protocol to be used for any copy. Optional.

                Will default to tftp if not specified.

                Since feature support depends on a software release,

                version number within the release, platform, and

                maybe the image type (subset type), a management

                station would be expected to somehow determine

                the protocol support for a command.

                .. data:: tftp = 1

                .. data:: rcp = 2

                .. data:: lex = 3

                .. data:: ftp = 4

                .. data:: scp = 5

                .. data:: sftp = 6

                """

                tftp = Enum.YLeaf(1, "tftp")

                rcp = Enum.YLeaf(2, "rcp")

                lex = Enum.YLeaf(3, "lex")

                ftp = Enum.YLeaf(4, "ftp")

                scp = Enum.YLeaf(5, "scp")

                sftp = Enum.YLeaf(6, "sftp")


            class Ciscoflashcopystatus(Enum):
                """
                Ciscoflashcopystatus (Enum Class)

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

                .. data:: copyOperationPending = 0

                .. data:: copyInProgress = 1

                .. data:: copyOperationSuccess = 2

                .. data:: copyInvalidOperation = 3

                .. data:: copyInvalidProtocol = 4

                .. data:: copyInvalidSourceName = 5

                .. data:: copyInvalidDestName = 6

                .. data:: copyInvalidServerAddress = 7

                .. data:: copyDeviceBusy = 8

                .. data:: copyDeviceOpenError = 9

                .. data:: copyDeviceError = 10

                .. data:: copyDeviceNotProgrammable = 11

                .. data:: copyDeviceFull = 12

                .. data:: copyFileOpenError = 13

                .. data:: copyFileTransferError = 14

                .. data:: copyFileChecksumError = 15

                .. data:: copyNoMemory = 16

                .. data:: copyUnknownFailure = 17

                .. data:: copyInvalidSignature = 18

                .. data:: copyProhibited = 19

                """

                copyOperationPending = Enum.YLeaf(0, "copyOperationPending")

                copyInProgress = Enum.YLeaf(1, "copyInProgress")

                copyOperationSuccess = Enum.YLeaf(2, "copyOperationSuccess")

                copyInvalidOperation = Enum.YLeaf(3, "copyInvalidOperation")

                copyInvalidProtocol = Enum.YLeaf(4, "copyInvalidProtocol")

                copyInvalidSourceName = Enum.YLeaf(5, "copyInvalidSourceName")

                copyInvalidDestName = Enum.YLeaf(6, "copyInvalidDestName")

                copyInvalidServerAddress = Enum.YLeaf(7, "copyInvalidServerAddress")

                copyDeviceBusy = Enum.YLeaf(8, "copyDeviceBusy")

                copyDeviceOpenError = Enum.YLeaf(9, "copyDeviceOpenError")

                copyDeviceError = Enum.YLeaf(10, "copyDeviceError")

                copyDeviceNotProgrammable = Enum.YLeaf(11, "copyDeviceNotProgrammable")

                copyDeviceFull = Enum.YLeaf(12, "copyDeviceFull")

                copyFileOpenError = Enum.YLeaf(13, "copyFileOpenError")

                copyFileTransferError = Enum.YLeaf(14, "copyFileTransferError")

                copyFileChecksumError = Enum.YLeaf(15, "copyFileChecksumError")

                copyNoMemory = Enum.YLeaf(16, "copyNoMemory")

                copyUnknownFailure = Enum.YLeaf(17, "copyUnknownFailure")

                copyInvalidSignature = Enum.YLeaf(18, "copyInvalidSignature")

                copyProhibited = Enum.YLeaf(19, "copyProhibited")



    class Ciscoflashpartitioningtable(Entity):
        """
        A table of Flash partitioning operation entries. Each
        entry represents a Flash partitioning operation that
        has been initiated.
        
        .. attribute:: ciscoflashpartitioningentry
        
        	A Flash partitioning operation entry. Each entry consists of the command, the target device, the partition count, and optionally the partition sizes.  A management station wishing to create an entry should first generate a pseudo\-random serial number to be used as the index to this sparse table.  The station should then create the associated instance of the row status object. It must also, either in the same or in successive PDUs, create the associated instance of the command and parameter objects. It should also modify the default values for any of the parameter objects if the defaults are not appropriate.  Once the appropriate instances of all the command objects have been created, either by an explicit SNMP set request or by default, the row status should be set to active to initiate the operation. Note that this entire procedure may be initiated via a single set request which specifies a row status of createAndGo as well as specifies valid values for the non\-defaulted parameter objects.  Once an operation has been activated, it cannot be stopped.  Once the operation completes, the management station should retrieve the value of the status object (and time if desired), and delete the entry.  In order to prevent old entries from clogging the table, entries will be aged out, but an entry will never be deleted within 5 minutes of completing
        	**type**\: list of  		 :py:class:`Ciscoflashpartitioningentry <ydk.models.cisco_ios_xe.CISCO_FLASH_MIB.CISCOFLASHMIB.Ciscoflashpartitioningtable.Ciscoflashpartitioningentry>`
        
        

        """

        _prefix = 'CISCO-FLASH-MIB'
        _revision = '2013-08-06'

        def __init__(self):
            super(CISCOFLASHMIB.Ciscoflashpartitioningtable, self).__init__()

            self.yang_name = "ciscoFlashPartitioningTable"
            self.yang_parent_name = "CISCO-FLASH-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("ciscoFlashPartitioningEntry", ("ciscoflashpartitioningentry", CISCOFLASHMIB.Ciscoflashpartitioningtable.Ciscoflashpartitioningentry))])
            self._leafs = OrderedDict()

            self.ciscoflashpartitioningentry = YList(self)
            self._segment_path = lambda: "ciscoFlashPartitioningTable"
            self._absolute_path = lambda: "CISCO-FLASH-MIB:CISCO-FLASH-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOFLASHMIB.Ciscoflashpartitioningtable, [], name, value)


        class Ciscoflashpartitioningentry(Entity):
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
            
            .. attribute:: ciscoflashpartitioningserialnumber  (key)
            
            	Object which specifies a unique entry in the partitioning operations table. A management station wishing to initiate a partitioning operation should use a pseudo\-random value for this object when creating or modifying an instance of a ciscoFlashPartitioningEntry
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: ciscoflashpartitioningcommand
            
            	The partitioning command to be executed. Mandatory. If the command is unsupported, the partitioningInvalidOperation error will be reported in the operation status.  Command                 Remarks partition               Partition a Flash device.                         All the prerequisites for                         partitioning must be met for                         this command to succeed.  Command table           Parameters 1) partition            PartitioningDestinationName                         PartitioningPartitionCount                         PartitioningPartitionSizes (opt)                         PartitioningNotifyOnCompletion (opt)
            	**type**\:  :py:class:`Ciscoflashpartitioningcommand <ydk.models.cisco_ios_xe.CISCO_FLASH_MIB.CISCOFLASHMIB.Ciscoflashpartitioningtable.Ciscoflashpartitioningentry.Ciscoflashpartitioningcommand>`
            
            .. attribute:: ciscoflashpartitioningdestinationname
            
            	Destination device name. This name will be the value obtained from FlashDeviceName. If the name is not specified, the default Flash device will be assumed
            	**type**\: str
            
            	**length:** 0..255
            
            .. attribute:: ciscoflashpartitioningpartitioncount
            
            	This object is used to specify the number of partitions to be created. Its value cannot exceed the value of ciscoFlashDeviceMaxPartitions.  To undo partitioning (revert to a single partition), this object must have the value 1
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: ciscoflashpartitioningpartitionsizes
            
            	This object is used to explicitly specify the size of each partition to be created. The size of each partition will be in units of ciscoFlashDeviceMinPartitionSize. The value of this object will be in the form\:         <part1>\:<part2>...\:<partn>  If partition sizes are not specified, the system will calculate default sizes based on the partition count, the minimum partition size, and the device size. Partition size need not be specified when undoing partitioning (partition count is 1). If partition sizes are specified, the number of sizes specified must exactly match the partition count. If not, the partitioning command will be rejected with the invalidPartitionSizes error 
            	**type**\: str
            
            .. attribute:: ciscoflashpartitioningstatus
            
            	The status of the specified partitioning operation. partitioningInProgress \:         specified operation is active  partitioningOperationSuccess \:         specified operation is supported and completed         successfully  partitioningInvalidOperation \:         command invalid or command\-protocol\-device         combination unsupported  partitioningInvalidDestName \:         invalid target name (file or partition or         device name) specified  partitioningInvalidPartitionCount \:         invalid partition count specified for the         partitioning command  partitioningInvalidPartitionSizes \:         invalid partition size, or invalid count of         partition sizes  partitioningDeviceBusy \:         specified device is in use and locked by         another process  partitioningDeviceOpenError \:         invalid device name  partitioningDeviceError \:         device read, write or erase error  partitioningNoMemory \:         system running low on memory  partitioningUnknownFailure \:         failure unknown
            	**type**\:  :py:class:`Ciscoflashpartitioningstatus <ydk.models.cisco_ios_xe.CISCO_FLASH_MIB.CISCOFLASHMIB.Ciscoflashpartitioningtable.Ciscoflashpartitioningentry.Ciscoflashpartitioningstatus>`
            
            .. attribute:: ciscoflashpartitioningnotifyoncompletion
            
            	Specifies whether or not a notification should be generated on the completion of the partitioning operation. If specified, ciscoFlashPartitioningCompletionTrap will be generated. It is the responsibility of the management entity to ensure that the SNMP administrative model is configured in such a way as to allow the notification to be delivered
            	**type**\: bool
            
            .. attribute:: ciscoflashpartitioningtime
            
            	Time taken for the operation. This object will be like a stopwatch, starting when the operation starts, stopping when the operation completes. If a management entity keeps a database of completion times for various operations, it can then use the stopwatch capability to display percentage completion time
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ciscoflashpartitioningentrystatus
            
            	The status of this table entry
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            

            """

            _prefix = 'CISCO-FLASH-MIB'
            _revision = '2013-08-06'

            def __init__(self):
                super(CISCOFLASHMIB.Ciscoflashpartitioningtable.Ciscoflashpartitioningentry, self).__init__()

                self.yang_name = "ciscoFlashPartitioningEntry"
                self.yang_parent_name = "ciscoFlashPartitioningTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ciscoflashpartitioningserialnumber']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ciscoflashpartitioningserialnumber', YLeaf(YType.int32, 'ciscoFlashPartitioningSerialNumber')),
                    ('ciscoflashpartitioningcommand', YLeaf(YType.enumeration, 'ciscoFlashPartitioningCommand')),
                    ('ciscoflashpartitioningdestinationname', YLeaf(YType.str, 'ciscoFlashPartitioningDestinationName')),
                    ('ciscoflashpartitioningpartitioncount', YLeaf(YType.uint32, 'ciscoFlashPartitioningPartitionCount')),
                    ('ciscoflashpartitioningpartitionsizes', YLeaf(YType.str, 'ciscoFlashPartitioningPartitionSizes')),
                    ('ciscoflashpartitioningstatus', YLeaf(YType.enumeration, 'ciscoFlashPartitioningStatus')),
                    ('ciscoflashpartitioningnotifyoncompletion', YLeaf(YType.boolean, 'ciscoFlashPartitioningNotifyOnCompletion')),
                    ('ciscoflashpartitioningtime', YLeaf(YType.uint32, 'ciscoFlashPartitioningTime')),
                    ('ciscoflashpartitioningentrystatus', YLeaf(YType.enumeration, 'ciscoFlashPartitioningEntryStatus')),
                ])
                self.ciscoflashpartitioningserialnumber = None
                self.ciscoflashpartitioningcommand = None
                self.ciscoflashpartitioningdestinationname = None
                self.ciscoflashpartitioningpartitioncount = None
                self.ciscoflashpartitioningpartitionsizes = None
                self.ciscoflashpartitioningstatus = None
                self.ciscoflashpartitioningnotifyoncompletion = None
                self.ciscoflashpartitioningtime = None
                self.ciscoflashpartitioningentrystatus = None
                self._segment_path = lambda: "ciscoFlashPartitioningEntry" + "[ciscoFlashPartitioningSerialNumber='" + str(self.ciscoflashpartitioningserialnumber) + "']"
                self._absolute_path = lambda: "CISCO-FLASH-MIB:CISCO-FLASH-MIB/ciscoFlashPartitioningTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOFLASHMIB.Ciscoflashpartitioningtable.Ciscoflashpartitioningentry, ['ciscoflashpartitioningserialnumber', 'ciscoflashpartitioningcommand', 'ciscoflashpartitioningdestinationname', 'ciscoflashpartitioningpartitioncount', 'ciscoflashpartitioningpartitionsizes', 'ciscoflashpartitioningstatus', 'ciscoflashpartitioningnotifyoncompletion', 'ciscoflashpartitioningtime', 'ciscoflashpartitioningentrystatus'], name, value)

            class Ciscoflashpartitioningcommand(Enum):
                """
                Ciscoflashpartitioningcommand (Enum Class)

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

                .. data:: partition = 1

                """

                partition = Enum.YLeaf(1, "partition")


            class Ciscoflashpartitioningstatus(Enum):
                """
                Ciscoflashpartitioningstatus (Enum Class)

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

                .. data:: partitioningInProgress = 1

                .. data:: partitioningOperationSuccess = 2

                .. data:: partitioningInvalidOperation = 3

                .. data:: partitioningInvalidDestName = 4

                .. data:: partitioningInvalidPartitionCount = 5

                .. data:: partitioningInvalidPartitionSizes = 6

                .. data:: partitioningDeviceBusy = 7

                .. data:: partitioningDeviceOpenError = 8

                .. data:: partitioningDeviceError = 9

                .. data:: partitioningNoMemory = 10

                .. data:: partitioningUnknownFailure = 11

                """

                partitioningInProgress = Enum.YLeaf(1, "partitioningInProgress")

                partitioningOperationSuccess = Enum.YLeaf(2, "partitioningOperationSuccess")

                partitioningInvalidOperation = Enum.YLeaf(3, "partitioningInvalidOperation")

                partitioningInvalidDestName = Enum.YLeaf(4, "partitioningInvalidDestName")

                partitioningInvalidPartitionCount = Enum.YLeaf(5, "partitioningInvalidPartitionCount")

                partitioningInvalidPartitionSizes = Enum.YLeaf(6, "partitioningInvalidPartitionSizes")

                partitioningDeviceBusy = Enum.YLeaf(7, "partitioningDeviceBusy")

                partitioningDeviceOpenError = Enum.YLeaf(8, "partitioningDeviceOpenError")

                partitioningDeviceError = Enum.YLeaf(9, "partitioningDeviceError")

                partitioningNoMemory = Enum.YLeaf(10, "partitioningNoMemory")

                partitioningUnknownFailure = Enum.YLeaf(11, "partitioningUnknownFailure")



    class Ciscoflashmiscoptable(Entity):
        """
        A table of misc Flash operation entries. Each
        entry represents a Flash operation that
        has been initiated.
        
        .. attribute:: ciscoflashmiscopentry
        
        	A Flash operation entry. Each entry consists of a command, a target, and any optional parameters.  A management station wishing to create an entry should first generate a pseudo\-random serial number to be used as the index to this sparse table.  The station should then create the associated instance of the row status object. It must also, either in the same or in successive PDUs, create the associated instance of the command and parameter objects. It should also modify the default values for any of the parameter objects if the defaults are not appropriate.  Once the appropriate instances of all the command objects have been created, either by an explicit SNMP set request or by default, the row status should be set to active to initiate the operation. Note that this entire procedure may be initiated via a single set request which specifies a row status of createAndGo as well as specifies valid values for the non\-defaulted parameter objects.  Once an operation has been activated, it cannot be stopped.  Once the operation completes, the management station should retrieve the value of the status object (and time if desired), and delete the entry.  In order to prevent old entries from clogging the table, entries will be aged out, but an entry will never be deleted within 5 minutes of completing
        	**type**\: list of  		 :py:class:`Ciscoflashmiscopentry <ydk.models.cisco_ios_xe.CISCO_FLASH_MIB.CISCOFLASHMIB.Ciscoflashmiscoptable.Ciscoflashmiscopentry>`
        
        

        """

        _prefix = 'CISCO-FLASH-MIB'
        _revision = '2013-08-06'

        def __init__(self):
            super(CISCOFLASHMIB.Ciscoflashmiscoptable, self).__init__()

            self.yang_name = "ciscoFlashMiscOpTable"
            self.yang_parent_name = "CISCO-FLASH-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("ciscoFlashMiscOpEntry", ("ciscoflashmiscopentry", CISCOFLASHMIB.Ciscoflashmiscoptable.Ciscoflashmiscopentry))])
            self._leafs = OrderedDict()

            self.ciscoflashmiscopentry = YList(self)
            self._segment_path = lambda: "ciscoFlashMiscOpTable"
            self._absolute_path = lambda: "CISCO-FLASH-MIB:CISCO-FLASH-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOFLASHMIB.Ciscoflashmiscoptable, [], name, value)


        class Ciscoflashmiscopentry(Entity):
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
            
            .. attribute:: ciscoflashmiscopserialnumber  (key)
            
            	Object which specifies a unique entry in the table. A management station wishing to initiate a flash operation should use a pseudo\-random value for this object when creating or modifying an instance of a ciscoFlashMiscOpEntry
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: ciscoflashmiscopcommand
            
            	The command to be executed. Mandatory. Note that it is possible for a system to support multiple file systems (different file systems on different Flash devices, or different file systems on different partitions within a device). Each such file system may support only a subset of these commands. If a command is unsupported, the miscOpInvalidOperation(3) error will be reported in the operation status.  Command         Remarks erase           Erase flash. verify          Verify flash file checksum. delete          Delete a file. undelete        Revive a deleted file .                 Note that there are limits on                 the number of times a file can                 be deleted and undeleted. When                 this limit is exceeded, the                 system will return the appropriate                 error. squeeze         Recover space occupied by                 deleted files. This command                 preserves the good files, erases                 out the file system, then restores                 the preserved good files. format          Format a flash device.  Command table   Parameters erase           MiscOpDestinationName                 MiscOpNotifyOnCompletion (opt) verify          MiscOpDestinationName                 MiscOpNotifyOnCompletion (opt) delete          MiscOpDestinationName                 MiscOpNotifyOnCompletion (opt) undelete        MiscOpDestinationName                 MiscOpNotifyOnCompletion (opt) squeeze         MiscOpDestinationName                 MiscOpNotifyOnCompletion (opt) format          MiscOpDestinationName                 MiscOpNotifyOnCompletion (opt)
            	**type**\:  :py:class:`Ciscoflashmiscopcommand <ydk.models.cisco_ios_xe.CISCO_FLASH_MIB.CISCOFLASHMIB.Ciscoflashmiscoptable.Ciscoflashmiscopentry.Ciscoflashmiscopcommand>`
            
            .. attribute:: ciscoflashmiscopdestinationname
            
            	Destination file, or partition name. File name must be of the form         [device>\:][<partition>\:]<file> where <device> is a value obtained from FlashDeviceName,       <partition> is obtained from FlashPartitionName   and <file> is the name of a file in Flash. While leading and/or trailing whitespaces are acceptable, no whitespaces are allowed within the path itself.  A management station could derive its own partition name as per the description for the ciscoFlashPartitionName object. If <device> is not specified, the default Flash device will be assumed. If <partition> is not specified, the default partition will be assumed. If a device is not partitioned into 2 or more partitions, this value may be left out.  For an operation on a partition, eg., the erase command, this object would specify the partition name in the form\:         [device>\:][<partition>\:]
            	**type**\: str
            
            	**length:** 0..255
            
            .. attribute:: ciscoflashmiscopstatus
            
            	The status of the specified operation. miscOpInProgress \:         specified operation is active  miscOpOperationSuccess \:         specified operation is supported and completed         successfully  miscOpInvalidOperation \:         command invalid or command\-protocol\-device         combination unsupported  miscOpInvalidDestName \:         invalid target name (file or partition or         device name) specified  miscOpDeviceBusy \:         specified device is in use and locked by another         process  miscOpDeviceOpenError \:         invalid device name  miscOpDeviceError \:         device read, write or erase error  miscOpDeviceNotProgrammable \:         device is read\-only but a write or erase         operation was specified  miscOpFileOpenError \:         invalid file name; file not found in partition  miscOpFileDeleteFailure \:         file could not be deleted; delete count exceeded  miscOpFileUndeleteFailure \:         file could not be undeleted; undelete count         exceeded  miscOpFileChecksumError \:         file has a bad checksum  miscOpNoMemory \:         system running low on memory  miscOpUnknownFailure \:         failure unknown  miscOpSqueezeFailure \:         the squeeze operation failed  miscOpNoSuchFile \:         a valid but nonexistent file name was specified  miscOpFormatFailure \:         the format operation failed
            	**type**\:  :py:class:`Ciscoflashmiscopstatus <ydk.models.cisco_ios_xe.CISCO_FLASH_MIB.CISCOFLASHMIB.Ciscoflashmiscoptable.Ciscoflashmiscopentry.Ciscoflashmiscopstatus>`
            
            .. attribute:: ciscoflashmiscopnotifyoncompletion
            
            	Specifies whether or not a notification should be generated on the completion of an operation. If specified, ciscoFlashMiscOpCompletionTrap will be generated. It is the responsibility of the management entity to ensure that the SNMP administrative model is configured in such a way as to allow the notification to be delivered
            	**type**\: bool
            
            .. attribute:: ciscoflashmiscoptime
            
            	Time taken for the operation. This object will be like a stopwatch, starting when the operation starts, stopping when the operation completes. If a management entity keeps a database of completion times for various operations, it can then use the stopwatch capability to display percentage completion time
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ciscoflashmiscopentrystatus
            
            	The status of this table entry
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            

            """

            _prefix = 'CISCO-FLASH-MIB'
            _revision = '2013-08-06'

            def __init__(self):
                super(CISCOFLASHMIB.Ciscoflashmiscoptable.Ciscoflashmiscopentry, self).__init__()

                self.yang_name = "ciscoFlashMiscOpEntry"
                self.yang_parent_name = "ciscoFlashMiscOpTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ciscoflashmiscopserialnumber']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ciscoflashmiscopserialnumber', YLeaf(YType.int32, 'ciscoFlashMiscOpSerialNumber')),
                    ('ciscoflashmiscopcommand', YLeaf(YType.enumeration, 'ciscoFlashMiscOpCommand')),
                    ('ciscoflashmiscopdestinationname', YLeaf(YType.str, 'ciscoFlashMiscOpDestinationName')),
                    ('ciscoflashmiscopstatus', YLeaf(YType.enumeration, 'ciscoFlashMiscOpStatus')),
                    ('ciscoflashmiscopnotifyoncompletion', YLeaf(YType.boolean, 'ciscoFlashMiscOpNotifyOnCompletion')),
                    ('ciscoflashmiscoptime', YLeaf(YType.uint32, 'ciscoFlashMiscOpTime')),
                    ('ciscoflashmiscopentrystatus', YLeaf(YType.enumeration, 'ciscoFlashMiscOpEntryStatus')),
                ])
                self.ciscoflashmiscopserialnumber = None
                self.ciscoflashmiscopcommand = None
                self.ciscoflashmiscopdestinationname = None
                self.ciscoflashmiscopstatus = None
                self.ciscoflashmiscopnotifyoncompletion = None
                self.ciscoflashmiscoptime = None
                self.ciscoflashmiscopentrystatus = None
                self._segment_path = lambda: "ciscoFlashMiscOpEntry" + "[ciscoFlashMiscOpSerialNumber='" + str(self.ciscoflashmiscopserialnumber) + "']"
                self._absolute_path = lambda: "CISCO-FLASH-MIB:CISCO-FLASH-MIB/ciscoFlashMiscOpTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOFLASHMIB.Ciscoflashmiscoptable.Ciscoflashmiscopentry, ['ciscoflashmiscopserialnumber', 'ciscoflashmiscopcommand', 'ciscoflashmiscopdestinationname', 'ciscoflashmiscopstatus', 'ciscoflashmiscopnotifyoncompletion', 'ciscoflashmiscoptime', 'ciscoflashmiscopentrystatus'], name, value)

            class Ciscoflashmiscopcommand(Enum):
                """
                Ciscoflashmiscopcommand (Enum Class)

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

                .. data:: erase = 1

                .. data:: verify = 2

                .. data:: delete = 3

                .. data:: undelete = 4

                .. data:: squeeze = 5

                .. data:: format = 6

                """

                erase = Enum.YLeaf(1, "erase")

                verify = Enum.YLeaf(2, "verify")

                delete = Enum.YLeaf(3, "delete")

                undelete = Enum.YLeaf(4, "undelete")

                squeeze = Enum.YLeaf(5, "squeeze")

                format = Enum.YLeaf(6, "format")


            class Ciscoflashmiscopstatus(Enum):
                """
                Ciscoflashmiscopstatus (Enum Class)

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

                .. data:: miscOpInProgress = 1

                .. data:: miscOpOperationSuccess = 2

                .. data:: miscOpInvalidOperation = 3

                .. data:: miscOpInvalidDestName = 4

                .. data:: miscOpDeviceBusy = 5

                .. data:: miscOpDeviceOpenError = 6

                .. data:: miscOpDeviceError = 7

                .. data:: miscOpDeviceNotProgrammable = 8

                .. data:: miscOpFileOpenError = 9

                .. data:: miscOpFileDeleteFailure = 10

                .. data:: miscOpFileUndeleteFailure = 11

                .. data:: miscOpFileChecksumError = 12

                .. data:: miscOpNoMemory = 13

                .. data:: miscOpUnknownFailure = 14

                .. data:: miscOpSqueezeFailure = 18

                .. data:: miscOpNoSuchFile = 19

                .. data:: miscOpFormatFailure = 20

                """

                miscOpInProgress = Enum.YLeaf(1, "miscOpInProgress")

                miscOpOperationSuccess = Enum.YLeaf(2, "miscOpOperationSuccess")

                miscOpInvalidOperation = Enum.YLeaf(3, "miscOpInvalidOperation")

                miscOpInvalidDestName = Enum.YLeaf(4, "miscOpInvalidDestName")

                miscOpDeviceBusy = Enum.YLeaf(5, "miscOpDeviceBusy")

                miscOpDeviceOpenError = Enum.YLeaf(6, "miscOpDeviceOpenError")

                miscOpDeviceError = Enum.YLeaf(7, "miscOpDeviceError")

                miscOpDeviceNotProgrammable = Enum.YLeaf(8, "miscOpDeviceNotProgrammable")

                miscOpFileOpenError = Enum.YLeaf(9, "miscOpFileOpenError")

                miscOpFileDeleteFailure = Enum.YLeaf(10, "miscOpFileDeleteFailure")

                miscOpFileUndeleteFailure = Enum.YLeaf(11, "miscOpFileUndeleteFailure")

                miscOpFileChecksumError = Enum.YLeaf(12, "miscOpFileChecksumError")

                miscOpNoMemory = Enum.YLeaf(13, "miscOpNoMemory")

                miscOpUnknownFailure = Enum.YLeaf(14, "miscOpUnknownFailure")

                miscOpSqueezeFailure = Enum.YLeaf(18, "miscOpSqueezeFailure")

                miscOpNoSuchFile = Enum.YLeaf(19, "miscOpNoSuchFile")

                miscOpFormatFailure = Enum.YLeaf(20, "miscOpFormatFailure")


    def clone_ptr(self):
        self._top_entity = CISCOFLASHMIB()
        return self._top_entity

