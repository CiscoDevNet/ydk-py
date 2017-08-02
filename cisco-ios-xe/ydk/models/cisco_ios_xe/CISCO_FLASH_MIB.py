""" CISCO_FLASH_MIB 

This MIB provides for the management of Cisco
Flash Devices.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class Flashfiletype(Enum):
    """
    Flashfiletype

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



class CiscoFlashMib(Entity):
    """
    
    
    .. attribute:: ciscoflashcfg
    
    	
    	**type**\:   :py:class:`Ciscoflashcfg <ydk.models.cisco_ios_xe.CISCO_FLASH_MIB.CiscoFlashMib.Ciscoflashcfg>`
    
    .. attribute:: ciscoflashchiptable
    
    	Table of Flash device chip properties for each initialized Flash device. This table is meant primarily for aiding error diagnosis
    	**type**\:   :py:class:`Ciscoflashchiptable <ydk.models.cisco_ios_xe.CISCO_FLASH_MIB.CiscoFlashMib.Ciscoflashchiptable>`
    
    .. attribute:: ciscoflashcopytable
    
    	A table of Flash copy operation entries. Each entry represents a Flash copy operation (to or from Flash) that has been initiated
    	**type**\:   :py:class:`Ciscoflashcopytable <ydk.models.cisco_ios_xe.CISCO_FLASH_MIB.CiscoFlashMib.Ciscoflashcopytable>`
    
    .. attribute:: ciscoflashdevice
    
    	
    	**type**\:   :py:class:`Ciscoflashdevice <ydk.models.cisco_ios_xe.CISCO_FLASH_MIB.CiscoFlashMib.Ciscoflashdevice>`
    
    .. attribute:: ciscoflashdevicetable
    
    	Table of Flash device properties for each initialized Flash device. Each Flash device installed in a system is detected, sized, and initialized when the system image boots up. For removable Flash devices, the device properties will be dynamically deleted and recreated as the device is removed and inserted. Note that in this case, the newly inserted device may not be the same as the earlier removed one. The ciscoFlashDeviceInitTime object is available for a management station to determine the time at which a device was initialized, and thereby detect the change of a removable device. A removable device that has not been installed will also have an entry in this table. This is to let a management station know about a removable device that has been removed. Since a removed device obviously cannot be sized and initialized, the table entry for such a device will have ciscoFlashDeviceSize equal to zero, and the following objects will have an indeterminate value\:         ciscoFlashDeviceMinPartitionSize,         ciscoFlashDeviceMaxPartitions,         ciscoFlashDevicePartitions, and         ciscoFlashDeviceChipCount. ciscoFlashDeviceRemovable will be true to indicate it is removable
    	**type**\:   :py:class:`Ciscoflashdevicetable <ydk.models.cisco_ios_xe.CISCO_FLASH_MIB.CiscoFlashMib.Ciscoflashdevicetable>`
    
    .. attribute:: ciscoflashfilebytypetable
    
    	Table of information for files on the manageable flash devices sorted by File Types
    	**type**\:   :py:class:`Ciscoflashfilebytypetable <ydk.models.cisco_ios_xe.CISCO_FLASH_MIB.CiscoFlashMib.Ciscoflashfilebytypetable>`
    
    .. attribute:: ciscoflashfiletable
    
    	Table of information for files in a Flash partition
    	**type**\:   :py:class:`Ciscoflashfiletable <ydk.models.cisco_ios_xe.CISCO_FLASH_MIB.CiscoFlashMib.Ciscoflashfiletable>`
    
    .. attribute:: ciscoflashmiscoptable
    
    	A table of misc Flash operation entries. Each entry represents a Flash operation that has been initiated
    	**type**\:   :py:class:`Ciscoflashmiscoptable <ydk.models.cisco_ios_xe.CISCO_FLASH_MIB.CiscoFlashMib.Ciscoflashmiscoptable>`
    
    .. attribute:: ciscoflashpartitioningtable
    
    	A table of Flash partitioning operation entries. Each entry represents a Flash partitioning operation that has been initiated
    	**type**\:   :py:class:`Ciscoflashpartitioningtable <ydk.models.cisco_ios_xe.CISCO_FLASH_MIB.CiscoFlashMib.Ciscoflashpartitioningtable>`
    
    .. attribute:: ciscoflashpartitiontable
    
    	Table of flash device partition properties for each initialized flash partition. Whenever there is no explicit partitioning done, a single partition spanning the entire device will be assumed to exist. There will therefore always be atleast one partition on a device
    	**type**\:   :py:class:`Ciscoflashpartitiontable <ydk.models.cisco_ios_xe.CISCO_FLASH_MIB.CiscoFlashMib.Ciscoflashpartitiontable>`
    
    

    """

    _prefix = 'CISCO-FLASH-MIB'
    _revision = '2013-08-06'

    def __init__(self):
        super(CiscoFlashMib, self).__init__()
        self._top_entity = None

        self.yang_name = "CISCO-FLASH-MIB"
        self.yang_parent_name = "CISCO-FLASH-MIB"

        self.ciscoflashcfg = CiscoFlashMib.Ciscoflashcfg()
        self.ciscoflashcfg.parent = self
        self._children_name_map["ciscoflashcfg"] = "ciscoFlashCfg"
        self._children_yang_names.add("ciscoFlashCfg")

        self.ciscoflashchiptable = CiscoFlashMib.Ciscoflashchiptable()
        self.ciscoflashchiptable.parent = self
        self._children_name_map["ciscoflashchiptable"] = "ciscoFlashChipTable"
        self._children_yang_names.add("ciscoFlashChipTable")

        self.ciscoflashcopytable = CiscoFlashMib.Ciscoflashcopytable()
        self.ciscoflashcopytable.parent = self
        self._children_name_map["ciscoflashcopytable"] = "ciscoFlashCopyTable"
        self._children_yang_names.add("ciscoFlashCopyTable")

        self.ciscoflashdevice = CiscoFlashMib.Ciscoflashdevice()
        self.ciscoflashdevice.parent = self
        self._children_name_map["ciscoflashdevice"] = "ciscoFlashDevice"
        self._children_yang_names.add("ciscoFlashDevice")

        self.ciscoflashdevicetable = CiscoFlashMib.Ciscoflashdevicetable()
        self.ciscoflashdevicetable.parent = self
        self._children_name_map["ciscoflashdevicetable"] = "ciscoFlashDeviceTable"
        self._children_yang_names.add("ciscoFlashDeviceTable")

        self.ciscoflashfilebytypetable = CiscoFlashMib.Ciscoflashfilebytypetable()
        self.ciscoflashfilebytypetable.parent = self
        self._children_name_map["ciscoflashfilebytypetable"] = "ciscoFlashFileByTypeTable"
        self._children_yang_names.add("ciscoFlashFileByTypeTable")

        self.ciscoflashfiletable = CiscoFlashMib.Ciscoflashfiletable()
        self.ciscoflashfiletable.parent = self
        self._children_name_map["ciscoflashfiletable"] = "ciscoFlashFileTable"
        self._children_yang_names.add("ciscoFlashFileTable")

        self.ciscoflashmiscoptable = CiscoFlashMib.Ciscoflashmiscoptable()
        self.ciscoflashmiscoptable.parent = self
        self._children_name_map["ciscoflashmiscoptable"] = "ciscoFlashMiscOpTable"
        self._children_yang_names.add("ciscoFlashMiscOpTable")

        self.ciscoflashpartitioningtable = CiscoFlashMib.Ciscoflashpartitioningtable()
        self.ciscoflashpartitioningtable.parent = self
        self._children_name_map["ciscoflashpartitioningtable"] = "ciscoFlashPartitioningTable"
        self._children_yang_names.add("ciscoFlashPartitioningTable")

        self.ciscoflashpartitiontable = CiscoFlashMib.Ciscoflashpartitiontable()
        self.ciscoflashpartitiontable.parent = self
        self._children_name_map["ciscoflashpartitiontable"] = "ciscoFlashPartitionTable"
        self._children_yang_names.add("ciscoFlashPartitionTable")


    class Ciscoflashdevice(Entity):
        """
        
        
        .. attribute:: ciscoflashdevicessupported
        
        	Number of Flash devices supported by the system. If the system does not support any Flash devices, this MIB will not be loaded on that system. The value of this object will therefore be atleast 1
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'CISCO-FLASH-MIB'
        _revision = '2013-08-06'

        def __init__(self):
            super(CiscoFlashMib.Ciscoflashdevice, self).__init__()

            self.yang_name = "ciscoFlashDevice"
            self.yang_parent_name = "CISCO-FLASH-MIB"

            self.ciscoflashdevicessupported = YLeaf(YType.uint32, "ciscoFlashDevicesSupported")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("ciscoflashdevicessupported") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoFlashMib.Ciscoflashdevice, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoFlashMib.Ciscoflashdevice, self).__setattr__(name, value)

        def has_data(self):
            return self.ciscoflashdevicessupported.is_set

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.ciscoflashdevicessupported.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "ciscoFlashDevice" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-FLASH-MIB:CISCO-FLASH-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.ciscoflashdevicessupported.is_set or self.ciscoflashdevicessupported.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ciscoflashdevicessupported.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "ciscoFlashDevicesSupported"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "ciscoFlashDevicesSupported"):
                self.ciscoflashdevicessupported = value
                self.ciscoflashdevicessupported.value_namespace = name_space
                self.ciscoflashdevicessupported.value_namespace_prefix = name_space_prefix


    class Ciscoflashcfg(Entity):
        """
        
        
        .. attribute:: ciscoflashcfgdevinsnotifenable
        
        	Specifies whether or not a notification should be generated on the insertion of a Flash device.  If the value of this object is 'true' then the ciscoFlashDeviceInsertedNotif notification will be generated.  If the value of this object is 'false' then the ciscoFlashDeviceInsertedNotif notification will not be generated.  It is the responsibility of the management entity to ensure that the SNMP administrative model is configured in such a way as to allow the notification to be delivered
        	**type**\:  bool
        
        .. attribute:: ciscoflashcfgdevremnotifenable
        
        	Specifies whether or not a notification should be generated on the removal of a Flash device.  If the value of this object is 'true' then the ciscoFlashDeviceRemovedNotif notification will be generated.  If the value of this object is 'false' then the ciscoFlashDeviceRemovedNotif notification will not be generated.  It is the responsibility of the management entity to ensure that the SNMP administrative model is configured in such a way as to allow the notification to be delivered
        	**type**\:  bool
        
        .. attribute:: ciscoflashpartitionlowspacenotifenable
        
        	This object specifies whether or not a notification should be generated when the free space falls below the threshold value on a flash partition and on recovery from low space.  If the value of this object is 'true' then ciscoFlashPartitionLowSpaceNotif and ciscoFlashPartitionLowSpaceRecoveryNotif notifications will be generated.  If the value of this object is 'false' then the ciscoFlashPartitionLowSpaceNotif  and ciscoFlashPartitionLowSpaceRecoveryNotif notifications will not be generated.  It is the responsibility of the management entity to ensure that the SNMP administrative model is configured in such a way as to allow the notifications to be delivered
        	**type**\:  bool
        
        

        """

        _prefix = 'CISCO-FLASH-MIB'
        _revision = '2013-08-06'

        def __init__(self):
            super(CiscoFlashMib.Ciscoflashcfg, self).__init__()

            self.yang_name = "ciscoFlashCfg"
            self.yang_parent_name = "CISCO-FLASH-MIB"

            self.ciscoflashcfgdevinsnotifenable = YLeaf(YType.boolean, "ciscoFlashCfgDevInsNotifEnable")

            self.ciscoflashcfgdevremnotifenable = YLeaf(YType.boolean, "ciscoFlashCfgDevRemNotifEnable")

            self.ciscoflashpartitionlowspacenotifenable = YLeaf(YType.boolean, "ciscoFlashPartitionLowSpaceNotifEnable")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("ciscoflashcfgdevinsnotifenable",
                            "ciscoflashcfgdevremnotifenable",
                            "ciscoflashpartitionlowspacenotifenable") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoFlashMib.Ciscoflashcfg, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoFlashMib.Ciscoflashcfg, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.ciscoflashcfgdevinsnotifenable.is_set or
                self.ciscoflashcfgdevremnotifenable.is_set or
                self.ciscoflashpartitionlowspacenotifenable.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.ciscoflashcfgdevinsnotifenable.yfilter != YFilter.not_set or
                self.ciscoflashcfgdevremnotifenable.yfilter != YFilter.not_set or
                self.ciscoflashpartitionlowspacenotifenable.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "ciscoFlashCfg" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-FLASH-MIB:CISCO-FLASH-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.ciscoflashcfgdevinsnotifenable.is_set or self.ciscoflashcfgdevinsnotifenable.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ciscoflashcfgdevinsnotifenable.get_name_leafdata())
            if (self.ciscoflashcfgdevremnotifenable.is_set or self.ciscoflashcfgdevremnotifenable.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ciscoflashcfgdevremnotifenable.get_name_leafdata())
            if (self.ciscoflashpartitionlowspacenotifenable.is_set or self.ciscoflashpartitionlowspacenotifenable.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ciscoflashpartitionlowspacenotifenable.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "ciscoFlashCfgDevInsNotifEnable" or name == "ciscoFlashCfgDevRemNotifEnable" or name == "ciscoFlashPartitionLowSpaceNotifEnable"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "ciscoFlashCfgDevInsNotifEnable"):
                self.ciscoflashcfgdevinsnotifenable = value
                self.ciscoflashcfgdevinsnotifenable.value_namespace = name_space
                self.ciscoflashcfgdevinsnotifenable.value_namespace_prefix = name_space_prefix
            if(value_path == "ciscoFlashCfgDevRemNotifEnable"):
                self.ciscoflashcfgdevremnotifenable = value
                self.ciscoflashcfgdevremnotifenable.value_namespace = name_space
                self.ciscoflashcfgdevremnotifenable.value_namespace_prefix = name_space_prefix
            if(value_path == "ciscoFlashPartitionLowSpaceNotifEnable"):
                self.ciscoflashpartitionlowspacenotifenable = value
                self.ciscoflashpartitionlowspacenotifenable.value_namespace = name_space
                self.ciscoflashpartitionlowspacenotifenable.value_namespace_prefix = name_space_prefix


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
        	**type**\: list of    :py:class:`Ciscoflashdeviceentry <ydk.models.cisco_ios_xe.CISCO_FLASH_MIB.CiscoFlashMib.Ciscoflashdevicetable.Ciscoflashdeviceentry>`
        
        

        """

        _prefix = 'CISCO-FLASH-MIB'
        _revision = '2013-08-06'

        def __init__(self):
            super(CiscoFlashMib.Ciscoflashdevicetable, self).__init__()

            self.yang_name = "ciscoFlashDeviceTable"
            self.yang_parent_name = "CISCO-FLASH-MIB"

            self.ciscoflashdeviceentry = YList(self)

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
                        super(CiscoFlashMib.Ciscoflashdevicetable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoFlashMib.Ciscoflashdevicetable, self).__setattr__(name, value)


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
            
            .. attribute:: ciscoflashdeviceindex  <key>
            
            	Flash device sequence number to index within the table of initialized flash devices. The lowest value should be 1. The highest should be less than or equal to the value of the ciscoFlashDevicesSupported object
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            .. attribute:: ciscoflashdevicecard
            
            	This object will point to an instance of a card entry in the cardTable. The card entry will give details about the card on which the Flash device is actually located. For most systems, this is usually the main processor board. On the AGS+ systems, Flash is located on a separate multibus card such as the MC. This object will therefore be used to essentially index into cardTable to retrieve details about the card such as cardDescr, cardSlotNumber, etc
            	**type**\:  str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            	**status**\: deprecated
            
            .. attribute:: ciscoflashdevicechipcount
            
            	Total number of chips within the Flash device. The purpose of this object is to provide information upfront to a management station on how much chip info to expect and possibly help double check the chip index against an upper limit when randomly retrieving chip info for a partition
            	**type**\:  int
            
            	**range:** 0..64
            
            .. attribute:: ciscoflashdevicecontroller
            
            	Flash device controller. The h/w card that actually controls Flash read/write/erase. Relevant for the AGS+ systems where Flash may be controlled by the MC+, STR or the ENVM cards, cards that may not actually contain the Flash chips. For systems that have removable PCMCIA flash cards that are controlled by a PCMCIA controller chip, this object may contain a description of that controller chip. Where irrelevant (Flash is a direct memory mapped device accessed directly by the main processor), this object will have an empty (NULL) string
            	**type**\:  str
            
            	**length:** 0..64
            
            .. attribute:: ciscoflashdevicedescr
            
            	Description of a Flash device. The description is meant to explain what the Flash device and its purpose is. Current values are\:   System flash \- for the primary Flash used to store full                  system images.   Boot flash   \- for the secondary Flash used to store                  bootstrap images. The ciscoFlashDeviceDescr, ciscoFlashDeviceController (if applicable), and ciscoFlashPhyEntIndex objects are expected to collectively give all information about a Flash device. The device description will always be available for a removable device, even when the device has been removed
            	**type**\:  str
            
            	**length:** 0..64
            
            .. attribute:: ciscoflashdeviceinittime
            
            	System time at which device was initialized. For fixed devices, this will be the system time at boot up. For removable devices, it will be the time at which the device was inserted, which may be boot up time, or a later time (if device was inserted later). If a device (fixed or removable) was repartitioned, it will be the time of repartitioning. The purpose of this object is to help a management station determine if a removable device has been changed. The application should retrieve this object prior to any operation and compare with the previously retrieved value. Note that this time will not be real time but a running time maintained by the system. This running time starts from zero when the system boots up. For a removable device that has been removed, this value will be zero
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ciscoflashdevicemaxpartitions
            
            	Max number of partitions supported by the system for this Flash device. Default will be 1, which actually means that partitioning is not supported. Note that this value will be defined by system limitations, not by the flash device itself (for eg., the system may impose a limit of 2 partitions even though the device may be large enough to be partitioned into 4 based on the smallest partition unit supported). On systems that execute code out of Flash, partitioning is a way of creating multiple file systems in the Flash device so that writing into or erasing of one file system can be done while executing code residing in another file system. For systems executing code out of DRAM, partitioning gives a way of sub\-dividing a large Flash device for easier management of files
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ciscoflashdeviceminpartitionsize
            
            	This object will give the minimum partition size supported for this device. For systems that execute code directly out of Flash, the minimum partition size needs to be the bank size. (Bank size is equal to the size of a chip multiplied by the width of the device. In most cases, the device width is 4 bytes, and so the bank size would be four times the size of a chip). This has to be so because all programming commands affect the operation of an entire chip (in our case, an entire bank because all operations are done on the entire width of the device) even though the actual command may be localized to a small portion of each chip. So when executing code out of Flash, one needs to be able to write and erase some portion of Flash without affecting the code execution. For systems that execute code out of DRAM or ROM, it is possible to partition Flash with a finer granularity (for eg., at erase sector boundaries) if the system code supports such granularity.  This object will let a management entity know the minimum partition size as defined by the system. If the system does not support partitioning, the value will be equal to the device size in ciscoFlashDeviceSize. The maximum number of partitions that could be configured will be equal to the minimum of ciscoFlashDeviceMaxPartitions and (ciscoFlashDeviceSize / ciscoFlashDeviceMinPartitionSize).  If the total size of the flash device is greater than the maximum value reportable by this object then this object should report its maximum value(4,294,967,295) and ciscoFlashDeviceMinPartitionSizeExtended must be used to report the flash device's minimum partition size
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: bytes
            
            .. attribute:: ciscoflashdeviceminpartitionsizeextended
            
            	This object provides the minimum partition size supported for this device. This object is a 64\-bit version of  ciscoFlashDeviceMinPatitionSize
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: ciscoflashdevicename
            
            	Flash device name. This name is used to refer to the device within the system. Flash operations get directed to a device based on this name. The system has a concept of a default device. This would be the primary or most used device in case of multiple devices. The system directs an operation to the default device whenever a device name is not specified. The device name is therefore mandatory except when the operation is being done on the default device, or, the system supports only a single Flash device. The device name will always be available for a removable device, even when the device has been removed
            	**type**\:  str
            
            	**length:** 0..16
            
            	**status**\: deprecated
            
            .. attribute:: ciscoflashdevicenameextended
            
            	Extended Flash device name whose size can be upto 255 characters. This name is used to refer to the device within the system. Flash operations get directed to a device based on this name. The system has a concept of a default device. This would be the primary or most used device in case of multiple devices. The system directs an operation to the default device whenever a device name is not specified. The device name is therefore mandatory except when the operation is being done on the default device, or, the system supports only a single Flash device. The device name will always be available for a removable device, even when the device has been removed
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: ciscoflashdevicepartitions
            
            	Flash device partitions actually present. Number of partitions cannot exceed the minimum of ciscoFlashDeviceMaxPartitions and (ciscoFlashDeviceSize / ciscoFlashDeviceMinPartitionSize). Will be equal to at least 1, the case where the partition spans the entire device (actually no partitioning). A partition will contain one or more minimum partition units (where a minimum partition unit is defined by ciscoFlashDeviceMinPartitionSize)
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ciscoflashdeviceprogrammingjumper
            
            	This object gives the state of a jumper (if present and can be determined) that controls the programming voltage called Vpp to the Flash device. Vpp is required for programming (erasing and writing) Flash. For certain older technology chips it is also required for identifying the chips (which in turn is required to identify which programming algorithms to use; different chips require different algorithms and commands). The purpose of the jumper, on systems where it is available, is to write protect a Flash device. On most of the newer remote access routers, this jumper is unavailable since users are not expected to visit remote sites just to install and remove the jumpers when upgrading software in the Flash device. The unknown(3) value will be returned for such systems and can be interpreted to mean that a programming jumper is not present or not required on those systems. On systems where the programming jumper state can be read back via a hardware register, the installed(1) or notInstalled(2) value will be returned. This object is expected to be used in conjunction with the ciscoFlashPartitionStatus object whenever that object has the readOnly(1) value. In such a case, this object will indicate whether the programming jumper is a possible reason for the readOnly state
            	**type**\:   :py:class:`Ciscoflashdeviceprogrammingjumper <ydk.models.cisco_ios_xe.CISCO_FLASH_MIB.CiscoFlashMib.Ciscoflashdevicetable.Ciscoflashdeviceentry.Ciscoflashdeviceprogrammingjumper>`
            
            .. attribute:: ciscoflashdeviceremovable
            
            	Whether Flash device is removable. Generally, only PCMCIA Flash cards will be treated as removable. Socketed Flash chips and Flash SIMM modules will not be treated as removable. Simply put, only those Flash devices that can be inserted or removed without opening the hardware casing will be considered removable. Further, removable Flash devices are expected to have the necessary hardware support \-   1. on\-line removal and insertion   2. interrupt generation on removal or insertion
            	**type**\:  bool
            
            .. attribute:: ciscoflashdevicesize
            
            	Total size of the Flash device. For a removable device, the size will be zero if the device has been removed.  If the total size of the flash device is greater than the maximum value reportable by this object then this object should report its maximum value(4,294,967,295) and ciscoFlashDeviceSizeExtended must be used to report the flash device's size
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: bytes
            
            .. attribute:: ciscoflashdevicesizeextended
            
            	Total size of the Flash device. For a removable device, the size will be zero if the device has been removed.  This object is a 64\-bit version of ciscoFlashDeviceSize
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: bytes
            
            .. attribute:: ciscoflashphyentindex
            
            	This object indicates the physical entity index of a physical entity in entPhysicalTable which the flash device actually located
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            

            """

            _prefix = 'CISCO-FLASH-MIB'
            _revision = '2013-08-06'

            def __init__(self):
                super(CiscoFlashMib.Ciscoflashdevicetable.Ciscoflashdeviceentry, self).__init__()

                self.yang_name = "ciscoFlashDeviceEntry"
                self.yang_parent_name = "ciscoFlashDeviceTable"

                self.ciscoflashdeviceindex = YLeaf(YType.uint32, "ciscoFlashDeviceIndex")

                self.ciscoflashdevicecard = YLeaf(YType.str, "ciscoFlashDeviceCard")

                self.ciscoflashdevicechipcount = YLeaf(YType.int32, "ciscoFlashDeviceChipCount")

                self.ciscoflashdevicecontroller = YLeaf(YType.str, "ciscoFlashDeviceController")

                self.ciscoflashdevicedescr = YLeaf(YType.str, "ciscoFlashDeviceDescr")

                self.ciscoflashdeviceinittime = YLeaf(YType.uint32, "ciscoFlashDeviceInitTime")

                self.ciscoflashdevicemaxpartitions = YLeaf(YType.uint32, "ciscoFlashDeviceMaxPartitions")

                self.ciscoflashdeviceminpartitionsize = YLeaf(YType.uint32, "ciscoFlashDeviceMinPartitionSize")

                self.ciscoflashdeviceminpartitionsizeextended = YLeaf(YType.uint64, "ciscoFlashDeviceMinPartitionSizeExtended")

                self.ciscoflashdevicename = YLeaf(YType.str, "ciscoFlashDeviceName")

                self.ciscoflashdevicenameextended = YLeaf(YType.str, "ciscoFlashDeviceNameExtended")

                self.ciscoflashdevicepartitions = YLeaf(YType.uint32, "ciscoFlashDevicePartitions")

                self.ciscoflashdeviceprogrammingjumper = YLeaf(YType.enumeration, "ciscoFlashDeviceProgrammingJumper")

                self.ciscoflashdeviceremovable = YLeaf(YType.boolean, "ciscoFlashDeviceRemovable")

                self.ciscoflashdevicesize = YLeaf(YType.uint32, "ciscoFlashDeviceSize")

                self.ciscoflashdevicesizeextended = YLeaf(YType.uint64, "ciscoFlashDeviceSizeExtended")

                self.ciscoflashphyentindex = YLeaf(YType.int32, "ciscoFlashPhyEntIndex")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("ciscoflashdeviceindex",
                                "ciscoflashdevicecard",
                                "ciscoflashdevicechipcount",
                                "ciscoflashdevicecontroller",
                                "ciscoflashdevicedescr",
                                "ciscoflashdeviceinittime",
                                "ciscoflashdevicemaxpartitions",
                                "ciscoflashdeviceminpartitionsize",
                                "ciscoflashdeviceminpartitionsizeextended",
                                "ciscoflashdevicename",
                                "ciscoflashdevicenameextended",
                                "ciscoflashdevicepartitions",
                                "ciscoflashdeviceprogrammingjumper",
                                "ciscoflashdeviceremovable",
                                "ciscoflashdevicesize",
                                "ciscoflashdevicesizeextended",
                                "ciscoflashphyentindex") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoFlashMib.Ciscoflashdevicetable.Ciscoflashdeviceentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoFlashMib.Ciscoflashdevicetable.Ciscoflashdeviceentry, self).__setattr__(name, value)

            class Ciscoflashdeviceprogrammingjumper(Enum):
                """
                Ciscoflashdeviceprogrammingjumper

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


            def has_data(self):
                return (
                    self.ciscoflashdeviceindex.is_set or
                    self.ciscoflashdevicecard.is_set or
                    self.ciscoflashdevicechipcount.is_set or
                    self.ciscoflashdevicecontroller.is_set or
                    self.ciscoflashdevicedescr.is_set or
                    self.ciscoflashdeviceinittime.is_set or
                    self.ciscoflashdevicemaxpartitions.is_set or
                    self.ciscoflashdeviceminpartitionsize.is_set or
                    self.ciscoflashdeviceminpartitionsizeextended.is_set or
                    self.ciscoflashdevicename.is_set or
                    self.ciscoflashdevicenameextended.is_set or
                    self.ciscoflashdevicepartitions.is_set or
                    self.ciscoflashdeviceprogrammingjumper.is_set or
                    self.ciscoflashdeviceremovable.is_set or
                    self.ciscoflashdevicesize.is_set or
                    self.ciscoflashdevicesizeextended.is_set or
                    self.ciscoflashphyentindex.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ciscoflashdeviceindex.yfilter != YFilter.not_set or
                    self.ciscoflashdevicecard.yfilter != YFilter.not_set or
                    self.ciscoflashdevicechipcount.yfilter != YFilter.not_set or
                    self.ciscoflashdevicecontroller.yfilter != YFilter.not_set or
                    self.ciscoflashdevicedescr.yfilter != YFilter.not_set or
                    self.ciscoflashdeviceinittime.yfilter != YFilter.not_set or
                    self.ciscoflashdevicemaxpartitions.yfilter != YFilter.not_set or
                    self.ciscoflashdeviceminpartitionsize.yfilter != YFilter.not_set or
                    self.ciscoflashdeviceminpartitionsizeextended.yfilter != YFilter.not_set or
                    self.ciscoflashdevicename.yfilter != YFilter.not_set or
                    self.ciscoflashdevicenameextended.yfilter != YFilter.not_set or
                    self.ciscoflashdevicepartitions.yfilter != YFilter.not_set or
                    self.ciscoflashdeviceprogrammingjumper.yfilter != YFilter.not_set or
                    self.ciscoflashdeviceremovable.yfilter != YFilter.not_set or
                    self.ciscoflashdevicesize.yfilter != YFilter.not_set or
                    self.ciscoflashdevicesizeextended.yfilter != YFilter.not_set or
                    self.ciscoflashphyentindex.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "ciscoFlashDeviceEntry" + "[ciscoFlashDeviceIndex='" + self.ciscoflashdeviceindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-FLASH-MIB:CISCO-FLASH-MIB/ciscoFlashDeviceTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ciscoflashdeviceindex.is_set or self.ciscoflashdeviceindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscoflashdeviceindex.get_name_leafdata())
                if (self.ciscoflashdevicecard.is_set or self.ciscoflashdevicecard.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscoflashdevicecard.get_name_leafdata())
                if (self.ciscoflashdevicechipcount.is_set or self.ciscoflashdevicechipcount.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscoflashdevicechipcount.get_name_leafdata())
                if (self.ciscoflashdevicecontroller.is_set or self.ciscoflashdevicecontroller.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscoflashdevicecontroller.get_name_leafdata())
                if (self.ciscoflashdevicedescr.is_set or self.ciscoflashdevicedescr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscoflashdevicedescr.get_name_leafdata())
                if (self.ciscoflashdeviceinittime.is_set or self.ciscoflashdeviceinittime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscoflashdeviceinittime.get_name_leafdata())
                if (self.ciscoflashdevicemaxpartitions.is_set or self.ciscoflashdevicemaxpartitions.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscoflashdevicemaxpartitions.get_name_leafdata())
                if (self.ciscoflashdeviceminpartitionsize.is_set or self.ciscoflashdeviceminpartitionsize.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscoflashdeviceminpartitionsize.get_name_leafdata())
                if (self.ciscoflashdeviceminpartitionsizeextended.is_set or self.ciscoflashdeviceminpartitionsizeextended.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscoflashdeviceminpartitionsizeextended.get_name_leafdata())
                if (self.ciscoflashdevicename.is_set or self.ciscoflashdevicename.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscoflashdevicename.get_name_leafdata())
                if (self.ciscoflashdevicenameextended.is_set or self.ciscoflashdevicenameextended.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscoflashdevicenameextended.get_name_leafdata())
                if (self.ciscoflashdevicepartitions.is_set or self.ciscoflashdevicepartitions.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscoflashdevicepartitions.get_name_leafdata())
                if (self.ciscoflashdeviceprogrammingjumper.is_set or self.ciscoflashdeviceprogrammingjumper.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscoflashdeviceprogrammingjumper.get_name_leafdata())
                if (self.ciscoflashdeviceremovable.is_set or self.ciscoflashdeviceremovable.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscoflashdeviceremovable.get_name_leafdata())
                if (self.ciscoflashdevicesize.is_set or self.ciscoflashdevicesize.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscoflashdevicesize.get_name_leafdata())
                if (self.ciscoflashdevicesizeextended.is_set or self.ciscoflashdevicesizeextended.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscoflashdevicesizeextended.get_name_leafdata())
                if (self.ciscoflashphyentindex.is_set or self.ciscoflashphyentindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscoflashphyentindex.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ciscoFlashDeviceIndex" or name == "ciscoFlashDeviceCard" or name == "ciscoFlashDeviceChipCount" or name == "ciscoFlashDeviceController" or name == "ciscoFlashDeviceDescr" or name == "ciscoFlashDeviceInitTime" or name == "ciscoFlashDeviceMaxPartitions" or name == "ciscoFlashDeviceMinPartitionSize" or name == "ciscoFlashDeviceMinPartitionSizeExtended" or name == "ciscoFlashDeviceName" or name == "ciscoFlashDeviceNameExtended" or name == "ciscoFlashDevicePartitions" or name == "ciscoFlashDeviceProgrammingJumper" or name == "ciscoFlashDeviceRemovable" or name == "ciscoFlashDeviceSize" or name == "ciscoFlashDeviceSizeExtended" or name == "ciscoFlashPhyEntIndex"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "ciscoFlashDeviceIndex"):
                    self.ciscoflashdeviceindex = value
                    self.ciscoflashdeviceindex.value_namespace = name_space
                    self.ciscoflashdeviceindex.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoFlashDeviceCard"):
                    self.ciscoflashdevicecard = value
                    self.ciscoflashdevicecard.value_namespace = name_space
                    self.ciscoflashdevicecard.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoFlashDeviceChipCount"):
                    self.ciscoflashdevicechipcount = value
                    self.ciscoflashdevicechipcount.value_namespace = name_space
                    self.ciscoflashdevicechipcount.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoFlashDeviceController"):
                    self.ciscoflashdevicecontroller = value
                    self.ciscoflashdevicecontroller.value_namespace = name_space
                    self.ciscoflashdevicecontroller.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoFlashDeviceDescr"):
                    self.ciscoflashdevicedescr = value
                    self.ciscoflashdevicedescr.value_namespace = name_space
                    self.ciscoflashdevicedescr.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoFlashDeviceInitTime"):
                    self.ciscoflashdeviceinittime = value
                    self.ciscoflashdeviceinittime.value_namespace = name_space
                    self.ciscoflashdeviceinittime.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoFlashDeviceMaxPartitions"):
                    self.ciscoflashdevicemaxpartitions = value
                    self.ciscoflashdevicemaxpartitions.value_namespace = name_space
                    self.ciscoflashdevicemaxpartitions.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoFlashDeviceMinPartitionSize"):
                    self.ciscoflashdeviceminpartitionsize = value
                    self.ciscoflashdeviceminpartitionsize.value_namespace = name_space
                    self.ciscoflashdeviceminpartitionsize.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoFlashDeviceMinPartitionSizeExtended"):
                    self.ciscoflashdeviceminpartitionsizeextended = value
                    self.ciscoflashdeviceminpartitionsizeextended.value_namespace = name_space
                    self.ciscoflashdeviceminpartitionsizeextended.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoFlashDeviceName"):
                    self.ciscoflashdevicename = value
                    self.ciscoflashdevicename.value_namespace = name_space
                    self.ciscoflashdevicename.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoFlashDeviceNameExtended"):
                    self.ciscoflashdevicenameextended = value
                    self.ciscoflashdevicenameextended.value_namespace = name_space
                    self.ciscoflashdevicenameextended.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoFlashDevicePartitions"):
                    self.ciscoflashdevicepartitions = value
                    self.ciscoflashdevicepartitions.value_namespace = name_space
                    self.ciscoflashdevicepartitions.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoFlashDeviceProgrammingJumper"):
                    self.ciscoflashdeviceprogrammingjumper = value
                    self.ciscoflashdeviceprogrammingjumper.value_namespace = name_space
                    self.ciscoflashdeviceprogrammingjumper.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoFlashDeviceRemovable"):
                    self.ciscoflashdeviceremovable = value
                    self.ciscoflashdeviceremovable.value_namespace = name_space
                    self.ciscoflashdeviceremovable.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoFlashDeviceSize"):
                    self.ciscoflashdevicesize = value
                    self.ciscoflashdevicesize.value_namespace = name_space
                    self.ciscoflashdevicesize.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoFlashDeviceSizeExtended"):
                    self.ciscoflashdevicesizeextended = value
                    self.ciscoflashdevicesizeextended.value_namespace = name_space
                    self.ciscoflashdevicesizeextended.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoFlashPhyEntIndex"):
                    self.ciscoflashphyentindex = value
                    self.ciscoflashphyentindex.value_namespace = name_space
                    self.ciscoflashphyentindex.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.ciscoflashdeviceentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.ciscoflashdeviceentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "ciscoFlashDeviceTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-FLASH-MIB:CISCO-FLASH-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "ciscoFlashDeviceEntry"):
                for c in self.ciscoflashdeviceentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoFlashMib.Ciscoflashdevicetable.Ciscoflashdeviceentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.ciscoflashdeviceentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "ciscoFlashDeviceEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Ciscoflashchiptable(Entity):
        """
        Table of Flash device chip properties for each
        initialized Flash device.
        This table is meant primarily for aiding error
        diagnosis.
        
        .. attribute:: ciscoflashchipentry
        
        	An entry in the table of chip info for each flash device initialized in the system. An entry is indexed by two objects \- the device index and the chip index within that device
        	**type**\: list of    :py:class:`Ciscoflashchipentry <ydk.models.cisco_ios_xe.CISCO_FLASH_MIB.CiscoFlashMib.Ciscoflashchiptable.Ciscoflashchipentry>`
        
        

        """

        _prefix = 'CISCO-FLASH-MIB'
        _revision = '2013-08-06'

        def __init__(self):
            super(CiscoFlashMib.Ciscoflashchiptable, self).__init__()

            self.yang_name = "ciscoFlashChipTable"
            self.yang_parent_name = "CISCO-FLASH-MIB"

            self.ciscoflashchipentry = YList(self)

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
                        super(CiscoFlashMib.Ciscoflashchiptable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoFlashMib.Ciscoflashchiptable, self).__setattr__(name, value)


        class Ciscoflashchipentry(Entity):
            """
            An entry in the table of chip info for each
            flash device initialized in the system.
            An entry is indexed by two objects \- the
            device index and the chip index within that
            device.
            
            .. attribute:: ciscoflashdeviceindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            	**refers to**\:  :py:class:`ciscoflashdeviceindex <ydk.models.cisco_ios_xe.CISCO_FLASH_MIB.CiscoFlashMib.Ciscoflashdevicetable.Ciscoflashdeviceentry>`
            
            .. attribute:: ciscoflashchipindex  <key>
            
            	Chip sequence number within selected flash device. Used to index within chip info table. Value starts from 1 and should not be greater than ciscoFlashDeviceChipCount for that device. When retrieving chip information for chips within a partition, the sequence number should lie between ciscoFlashPartitionStartChip & ciscoFlashPartitionEndChip (both inclusive)
            	**type**\:  int
            
            	**range:** 1..64
            
            .. attribute:: ciscoflashchipcode
            
            	Manufacturer and device code for a chip. Lower byte will contain the device code. Upper byte will contain the manufacturer code. If a chip code is unknown because it could not be queried out of the chip, the value of this object will be 00\:00. Since programming algorithms differ from chip type to chip type, this chip code should be used to determine which algorithms to use (and thereby whether the chip is supported in the first place)
            	**type**\:  str
            
            	**length:** 0..5
            
            .. attribute:: ciscoflashchipdescr
            
            	Flash chip name corresponding to the chip code. The name will contain the manufacturer and the chip type. It will be of the form \:   Intel 27F008SA. In the case where a chip code is unknown, this object will be an empty (NULL) string. In the case where the chip code is known but the chip is not supported by the system, this object will be an empty (NULL) string. A management station is therefore expected to use the chip code and the chip description in conjunction to provide additional information whenever the ciscoFlashPartitionStatus object has the readOnly(1) value
            	**type**\:  str
            
            	**length:** 0..32
            
            .. attribute:: ciscoflashchiperaseretries
            
            	This object will provide a cumulative count (since last system boot up or initialization) of the number of erase retries that were done in the chip. Typically, a maximum of 2000 retries are done in a single erase zone (which may be a full chip or a portion, depending on the chip technology) before flagging an erase error. A management station is expected to get this object for each chip in a partition after an erase failure in that partition. To keep a track of retries for a given erase operation, the management station would have to retrieve the values for the concerned chips before and after any erase operation. Note that erase may be done through an independent command, or through a copy\-to\-flash command
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ciscoflashchipmaxeraseretries
            
            	The maximum number of erase retries done within an erase sector before declaring an erase failure
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ciscoflashchipmaxwriteretries
            
            	The maximum number of write retries done at any single location before declaring a write failure
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ciscoflashchipwriteretries
            
            	This object will provide a cumulative count (since last system boot up or initialization) of the number of write retries that were done in the chip. If no writes have been done to Flash, the count will be zero. Typically, a maximum of 25 retries are done on a single location before flagging a write error. A management station is expected to get this object for each chip in a partition after a write failure in that partition. To keep a track of retries for a given write operation, the management station would have to retrieve the values for the concerned chips before and after any write operation
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'CISCO-FLASH-MIB'
            _revision = '2013-08-06'

            def __init__(self):
                super(CiscoFlashMib.Ciscoflashchiptable.Ciscoflashchipentry, self).__init__()

                self.yang_name = "ciscoFlashChipEntry"
                self.yang_parent_name = "ciscoFlashChipTable"

                self.ciscoflashdeviceindex = YLeaf(YType.str, "ciscoFlashDeviceIndex")

                self.ciscoflashchipindex = YLeaf(YType.int32, "ciscoFlashChipIndex")

                self.ciscoflashchipcode = YLeaf(YType.str, "ciscoFlashChipCode")

                self.ciscoflashchipdescr = YLeaf(YType.str, "ciscoFlashChipDescr")

                self.ciscoflashchiperaseretries = YLeaf(YType.uint32, "ciscoFlashChipEraseRetries")

                self.ciscoflashchipmaxeraseretries = YLeaf(YType.uint32, "ciscoFlashChipMaxEraseRetries")

                self.ciscoflashchipmaxwriteretries = YLeaf(YType.uint32, "ciscoFlashChipMaxWriteRetries")

                self.ciscoflashchipwriteretries = YLeaf(YType.uint32, "ciscoFlashChipWriteRetries")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("ciscoflashdeviceindex",
                                "ciscoflashchipindex",
                                "ciscoflashchipcode",
                                "ciscoflashchipdescr",
                                "ciscoflashchiperaseretries",
                                "ciscoflashchipmaxeraseretries",
                                "ciscoflashchipmaxwriteretries",
                                "ciscoflashchipwriteretries") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoFlashMib.Ciscoflashchiptable.Ciscoflashchipentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoFlashMib.Ciscoflashchiptable.Ciscoflashchipentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.ciscoflashdeviceindex.is_set or
                    self.ciscoflashchipindex.is_set or
                    self.ciscoflashchipcode.is_set or
                    self.ciscoflashchipdescr.is_set or
                    self.ciscoflashchiperaseretries.is_set or
                    self.ciscoflashchipmaxeraseretries.is_set or
                    self.ciscoflashchipmaxwriteretries.is_set or
                    self.ciscoflashchipwriteretries.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ciscoflashdeviceindex.yfilter != YFilter.not_set or
                    self.ciscoflashchipindex.yfilter != YFilter.not_set or
                    self.ciscoflashchipcode.yfilter != YFilter.not_set or
                    self.ciscoflashchipdescr.yfilter != YFilter.not_set or
                    self.ciscoflashchiperaseretries.yfilter != YFilter.not_set or
                    self.ciscoflashchipmaxeraseretries.yfilter != YFilter.not_set or
                    self.ciscoflashchipmaxwriteretries.yfilter != YFilter.not_set or
                    self.ciscoflashchipwriteretries.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "ciscoFlashChipEntry" + "[ciscoFlashDeviceIndex='" + self.ciscoflashdeviceindex.get() + "']" + "[ciscoFlashChipIndex='" + self.ciscoflashchipindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-FLASH-MIB:CISCO-FLASH-MIB/ciscoFlashChipTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ciscoflashdeviceindex.is_set or self.ciscoflashdeviceindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscoflashdeviceindex.get_name_leafdata())
                if (self.ciscoflashchipindex.is_set or self.ciscoflashchipindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscoflashchipindex.get_name_leafdata())
                if (self.ciscoflashchipcode.is_set or self.ciscoflashchipcode.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscoflashchipcode.get_name_leafdata())
                if (self.ciscoflashchipdescr.is_set or self.ciscoflashchipdescr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscoflashchipdescr.get_name_leafdata())
                if (self.ciscoflashchiperaseretries.is_set or self.ciscoflashchiperaseretries.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscoflashchiperaseretries.get_name_leafdata())
                if (self.ciscoflashchipmaxeraseretries.is_set or self.ciscoflashchipmaxeraseretries.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscoflashchipmaxeraseretries.get_name_leafdata())
                if (self.ciscoflashchipmaxwriteretries.is_set or self.ciscoflashchipmaxwriteretries.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscoflashchipmaxwriteretries.get_name_leafdata())
                if (self.ciscoflashchipwriteretries.is_set or self.ciscoflashchipwriteretries.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscoflashchipwriteretries.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ciscoFlashDeviceIndex" or name == "ciscoFlashChipIndex" or name == "ciscoFlashChipCode" or name == "ciscoFlashChipDescr" or name == "ciscoFlashChipEraseRetries" or name == "ciscoFlashChipMaxEraseRetries" or name == "ciscoFlashChipMaxWriteRetries" or name == "ciscoFlashChipWriteRetries"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "ciscoFlashDeviceIndex"):
                    self.ciscoflashdeviceindex = value
                    self.ciscoflashdeviceindex.value_namespace = name_space
                    self.ciscoflashdeviceindex.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoFlashChipIndex"):
                    self.ciscoflashchipindex = value
                    self.ciscoflashchipindex.value_namespace = name_space
                    self.ciscoflashchipindex.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoFlashChipCode"):
                    self.ciscoflashchipcode = value
                    self.ciscoflashchipcode.value_namespace = name_space
                    self.ciscoflashchipcode.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoFlashChipDescr"):
                    self.ciscoflashchipdescr = value
                    self.ciscoflashchipdescr.value_namespace = name_space
                    self.ciscoflashchipdescr.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoFlashChipEraseRetries"):
                    self.ciscoflashchiperaseretries = value
                    self.ciscoflashchiperaseretries.value_namespace = name_space
                    self.ciscoflashchiperaseretries.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoFlashChipMaxEraseRetries"):
                    self.ciscoflashchipmaxeraseretries = value
                    self.ciscoflashchipmaxeraseretries.value_namespace = name_space
                    self.ciscoflashchipmaxeraseretries.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoFlashChipMaxWriteRetries"):
                    self.ciscoflashchipmaxwriteretries = value
                    self.ciscoflashchipmaxwriteretries.value_namespace = name_space
                    self.ciscoflashchipmaxwriteretries.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoFlashChipWriteRetries"):
                    self.ciscoflashchipwriteretries = value
                    self.ciscoflashchipwriteretries.value_namespace = name_space
                    self.ciscoflashchipwriteretries.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.ciscoflashchipentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.ciscoflashchipentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "ciscoFlashChipTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-FLASH-MIB:CISCO-FLASH-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "ciscoFlashChipEntry"):
                for c in self.ciscoflashchipentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoFlashMib.Ciscoflashchiptable.Ciscoflashchipentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.ciscoflashchipentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "ciscoFlashChipEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Ciscoflashpartitiontable(Entity):
        """
        Table of flash device partition properties for each
        initialized flash partition. Whenever there is no
        explicit partitioning done, a single partition spanning
        the entire device will be assumed to exist. There will
        therefore always be atleast one partition on a device.
        
        .. attribute:: ciscoflashpartitionentry
        
        	An entry in the table of flash partition properties for each initialized flash partition. Each entry will be indexed by a device number and a partition number within the device
        	**type**\: list of    :py:class:`Ciscoflashpartitionentry <ydk.models.cisco_ios_xe.CISCO_FLASH_MIB.CiscoFlashMib.Ciscoflashpartitiontable.Ciscoflashpartitionentry>`
        
        

        """

        _prefix = 'CISCO-FLASH-MIB'
        _revision = '2013-08-06'

        def __init__(self):
            super(CiscoFlashMib.Ciscoflashpartitiontable, self).__init__()

            self.yang_name = "ciscoFlashPartitionTable"
            self.yang_parent_name = "CISCO-FLASH-MIB"

            self.ciscoflashpartitionentry = YList(self)

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
                        super(CiscoFlashMib.Ciscoflashpartitiontable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoFlashMib.Ciscoflashpartitiontable, self).__setattr__(name, value)


        class Ciscoflashpartitionentry(Entity):
            """
            An entry in the table of flash partition properties
            for each initialized flash partition. Each entry
            will be indexed by a device number and a partition
            number within the device.
            
            .. attribute:: ciscoflashdeviceindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            	**refers to**\:  :py:class:`ciscoflashdeviceindex <ydk.models.cisco_ios_xe.CISCO_FLASH_MIB.CiscoFlashMib.Ciscoflashdevicetable.Ciscoflashdeviceentry>`
            
            .. attribute:: ciscoflashpartitionindex  <key>
            
            	Flash partition sequence number used to index within table of initialized flash partitions
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            .. attribute:: ciscoflashpartitionchecksumalgorithm
            
            	Checksum algorithm identifier for checksum method used by the file system. Normally, this would be fixed for a particular file system. When a file system writes a file to Flash, it checksums the data written. The checksum then serves as a way to validate the data read back whenever the file is opened for reading. Since there is no way, when using TFTP, to guarantee that a network download has been error free (since UDP checksums may not have been enabled), this object together with the ciscoFlashFileChecksum object provides a method for any management station to regenerate the checksum of the original file on the server and compare checksums to ensure that the file download to Flash was error free. simpleChecksum represents a simple 1s complement addition of short word values. Other algorithm values will be added as necessary
            	**type**\:   :py:class:`Ciscoflashpartitionchecksumalgorithm <ydk.models.cisco_ios_xe.CISCO_FLASH_MIB.CiscoFlashMib.Ciscoflashpartitiontable.Ciscoflashpartitionentry.Ciscoflashpartitionchecksumalgorithm>`
            
            .. attribute:: ciscoflashpartitionendchip
            
            	Chip sequence number of last chip in partition. Used as an index into the chip table
            	**type**\:  int
            
            	**range:** 1..64
            
            .. attribute:: ciscoflashpartitionfilecount
            
            	Count of all files in a flash partition. Both good and bad (deleted or invalid checksum) files will be included in this count
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ciscoflashpartitionfilenamelength
            
            	Maximum file name length supported by the file system. Max file name length will depend on the file system implemented. Today, all file systems support a max length of at least 48 bytes. A management entity must use this object when prompting a user for, or deriving the Flash file name length
            	**type**\:  int
            
            	**range:** 1..256
            
            .. attribute:: ciscoflashpartitionfreespace
            
            	Free space within a Flash partition. Note that the actual size of a file in Flash includes a small overhead that represents the file system's file header. Certain file systems may also have a partition or device header overhead to be considered when computing the free space. Free space will be computed as total partition size less size of all existing files (valid/invalid/deleted files and including file header of each file), less size of any partition header, less size of header of next file to be copied in. In short, this object will give the size of the largest file that can be copied in. The management entity will not be expected to know or use any overheads such as file and partition header lengths, since such overheads may vary from file system to file system. Deleted files in Flash do not free up space. A partition may have to be erased in order to reclaim the space occupied by files.  If the free space within a flash partition is greater than the maximum value reportable by this object then this object should report its maximum value(4,294,967,295) and ciscoFlashPartitionFreeSpaceExtended must be used to report the flash partition's free space
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: bytes
            
            .. attribute:: ciscoflashpartitionfreespaceextended
            
            	Free space within a Flash partition. Note that the actual size of a file in Flash includes a small overhead that represents the file system's file header. Certain file systems may also have a partition or device header overhead to be considered when computing the free space. Free space will be computed as total partition size less size of all existing files (valid/invalid/deleted files and including file header of each file), less size of any partition header, less size of header of next file to be copied in. In short, this object will give the size of the largest file that can be copied in. The management entity will not be expected to know or use any overheads such as file and partition header lengths, since such overheads may vary from file system to file system. Deleted files in Flash do not free up space. A partition may have to be erased in order to reclaim the space occupied by files.  This object is a 64\-bit version of ciscoFlashPartitionFreeSpace
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: bytes
            
            .. attribute:: ciscoflashpartitionlowspacenotifthreshold
            
            	This object specifies the minimum threshold value in percentage of free space for each partition. If the free space available goes below this threshold value and if ciscoFlashPartionLowSpaceNotifEnable is set to true, ciscoFlashPartitionLowSpaceNotif will be generated. When the available free space comes back to the threshold value ciscoFlashPartionLowSpaceRecoveryNotif will be generated
            	**type**\:  int
            
            	**range:** 0..100
            
            .. attribute:: ciscoflashpartitionname
            
            	Flash partition name used to refer to a partition by the system. This can be any alpha\-numeric character string of the form AAAAAAAAnn, where A represents an optional alpha character and n a numeric character. Any numeric characters must always form the trailing part of the string. The system will strip off the alpha characters and use the numeric portion to map to a partition index. Flash operations get directed to a device partition based on this name. The system has a concept of a default partition. This would be the first partition in the device. The system directs an operation to the default partition whenever a partition name is not specified. The partition name is therefore mandatory except when the operation is being done on the default partition, or the device has just one partition (is not partitioned)
            	**type**\:  str
            
            	**length:** 0..16
            
            .. attribute:: ciscoflashpartitionneederasure
            
            	This object indicates whether a partition requires erasure before any write operations can be done in it. A management station should therefore retrieve this object prior to attempting any write operation. A partition requires erasure after it becomes full free space left is less than or equal to the (filesystem file header size). A partition also requires erasure if the system does not find the existence of any file system when it boots up. The partition may be erased explicitly through the erase(5) command, or by using the copyToFlashWithErase(1) command. If a copyToFlashWithoutErase(2) command is issued when this object has the TRUE value, the command will fail
            	**type**\:  bool
            
            .. attribute:: ciscoflashpartitionsize
            
            	Flash partition size. It should be an integral multiple of ciscoFlashDeviceMinPartitionSize. If there is a single partition, this size will be equal to ciscoFlashDeviceSize.  If the size of the flash partition is greater than the maximum value reportable by this object then this object should report its maximum value(4,294,967,295) and ciscoFlashPartitionSizeExtended must be used to report the flash partition's size
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            	**units**\: bytes
            
            .. attribute:: ciscoflashpartitionsizeextended
            
            	Flash partition size. It should be an integral multiple of ciscoFlashDeviceMinPartitionSize. If there is a single partition, this size will be equal to ciscoFlashDeviceSize.  This object is a 64\-bit version of ciscoFlashPartitionSize
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: bytes
            
            .. attribute:: ciscoflashpartitionstartchip
            
            	Chip sequence number of first chip in partition. Used as an index into the chip table
            	**type**\:  int
            
            	**range:** 1..64
            
            .. attribute:: ciscoflashpartitionstatus
            
            	Flash partition status can be \:  \* readOnly if device is not programmable either because chips could not be recognized or an erroneous mismatch of chips was detected. Chip recognition may fail either because the chips are not supported by the system, or because the Vpp voltage required to identify chips has been disabled via the programming jumper. The ciscoFlashDeviceProgrammingJumper, ciscoFlashChipCode, and ciscoFlashChipDescr objects can be examined to get more details on the cause of this status \* runFromFlash (RFF) if current image is running from this partition. The ciscoFlashPartitionUpgradeMethod object will then indicate whether the Flash Load Helper can be used to write a file to this partition or not.  \* readWrite if partition is programmable
            	**type**\:   :py:class:`Ciscoflashpartitionstatus <ydk.models.cisco_ios_xe.CISCO_FLASH_MIB.CiscoFlashMib.Ciscoflashpartitiontable.Ciscoflashpartitionentry.Ciscoflashpartitionstatus>`
            
            .. attribute:: ciscoflashpartitionupgrademethod
            
            	Flash partition upgrade method, ie., method by which new files can be downloaded into the partition. FLH stands for Flash Load Helper, a feature provided on run\-from\-Flash systems for upgrading Flash. This feature uses the bootstrap code in ROMs to help in automatic download. This object should be retrieved if the partition status is runFromFlash(2). If the partition status is readOnly(1), the upgrade method would depend on the reason for the readOnly status. For eg., it may simply be a matter of installing the programming jumper, or it may require execution of a later version of software that supports the Flash chips.  unknown      \-  the current system image does not know                 how Flash can be programmed. A possible                 method would be to reload the ROM image                 and perform the upgrade manually. rxbootFLH    \-  the Flash Load Helper is available to                 download files to Flash. A copy\-to\-flash                 command can be used and this system image                 will automatically reload the Rxboot image                 in ROM and direct it to carry out the                 download request. direct       \-  will be done directly by this image
            	**type**\:   :py:class:`Ciscoflashpartitionupgrademethod <ydk.models.cisco_ios_xe.CISCO_FLASH_MIB.CiscoFlashMib.Ciscoflashpartitiontable.Ciscoflashpartitionentry.Ciscoflashpartitionupgrademethod>`
            
            

            """

            _prefix = 'CISCO-FLASH-MIB'
            _revision = '2013-08-06'

            def __init__(self):
                super(CiscoFlashMib.Ciscoflashpartitiontable.Ciscoflashpartitionentry, self).__init__()

                self.yang_name = "ciscoFlashPartitionEntry"
                self.yang_parent_name = "ciscoFlashPartitionTable"

                self.ciscoflashdeviceindex = YLeaf(YType.str, "ciscoFlashDeviceIndex")

                self.ciscoflashpartitionindex = YLeaf(YType.uint32, "ciscoFlashPartitionIndex")

                self.ciscoflashpartitionchecksumalgorithm = YLeaf(YType.enumeration, "ciscoFlashPartitionChecksumAlgorithm")

                self.ciscoflashpartitionendchip = YLeaf(YType.int32, "ciscoFlashPartitionEndChip")

                self.ciscoflashpartitionfilecount = YLeaf(YType.uint32, "ciscoFlashPartitionFileCount")

                self.ciscoflashpartitionfilenamelength = YLeaf(YType.int32, "ciscoFlashPartitionFileNameLength")

                self.ciscoflashpartitionfreespace = YLeaf(YType.uint32, "ciscoFlashPartitionFreeSpace")

                self.ciscoflashpartitionfreespaceextended = YLeaf(YType.uint64, "ciscoFlashPartitionFreeSpaceExtended")

                self.ciscoflashpartitionlowspacenotifthreshold = YLeaf(YType.int32, "ciscoFlashPartitionLowSpaceNotifThreshold")

                self.ciscoflashpartitionname = YLeaf(YType.str, "ciscoFlashPartitionName")

                self.ciscoflashpartitionneederasure = YLeaf(YType.boolean, "ciscoFlashPartitionNeedErasure")

                self.ciscoflashpartitionsize = YLeaf(YType.uint32, "ciscoFlashPartitionSize")

                self.ciscoflashpartitionsizeextended = YLeaf(YType.uint64, "ciscoFlashPartitionSizeExtended")

                self.ciscoflashpartitionstartchip = YLeaf(YType.int32, "ciscoFlashPartitionStartChip")

                self.ciscoflashpartitionstatus = YLeaf(YType.enumeration, "ciscoFlashPartitionStatus")

                self.ciscoflashpartitionupgrademethod = YLeaf(YType.enumeration, "ciscoFlashPartitionUpgradeMethod")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("ciscoflashdeviceindex",
                                "ciscoflashpartitionindex",
                                "ciscoflashpartitionchecksumalgorithm",
                                "ciscoflashpartitionendchip",
                                "ciscoflashpartitionfilecount",
                                "ciscoflashpartitionfilenamelength",
                                "ciscoflashpartitionfreespace",
                                "ciscoflashpartitionfreespaceextended",
                                "ciscoflashpartitionlowspacenotifthreshold",
                                "ciscoflashpartitionname",
                                "ciscoflashpartitionneederasure",
                                "ciscoflashpartitionsize",
                                "ciscoflashpartitionsizeextended",
                                "ciscoflashpartitionstartchip",
                                "ciscoflashpartitionstatus",
                                "ciscoflashpartitionupgrademethod") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoFlashMib.Ciscoflashpartitiontable.Ciscoflashpartitionentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoFlashMib.Ciscoflashpartitiontable.Ciscoflashpartitionentry, self).__setattr__(name, value)

            class Ciscoflashpartitionchecksumalgorithm(Enum):
                """
                Ciscoflashpartitionchecksumalgorithm

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
                Ciscoflashpartitionstatus

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
                Ciscoflashpartitionupgrademethod

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


            def has_data(self):
                return (
                    self.ciscoflashdeviceindex.is_set or
                    self.ciscoflashpartitionindex.is_set or
                    self.ciscoflashpartitionchecksumalgorithm.is_set or
                    self.ciscoflashpartitionendchip.is_set or
                    self.ciscoflashpartitionfilecount.is_set or
                    self.ciscoflashpartitionfilenamelength.is_set or
                    self.ciscoflashpartitionfreespace.is_set or
                    self.ciscoflashpartitionfreespaceextended.is_set or
                    self.ciscoflashpartitionlowspacenotifthreshold.is_set or
                    self.ciscoflashpartitionname.is_set or
                    self.ciscoflashpartitionneederasure.is_set or
                    self.ciscoflashpartitionsize.is_set or
                    self.ciscoflashpartitionsizeextended.is_set or
                    self.ciscoflashpartitionstartchip.is_set or
                    self.ciscoflashpartitionstatus.is_set or
                    self.ciscoflashpartitionupgrademethod.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ciscoflashdeviceindex.yfilter != YFilter.not_set or
                    self.ciscoflashpartitionindex.yfilter != YFilter.not_set or
                    self.ciscoflashpartitionchecksumalgorithm.yfilter != YFilter.not_set or
                    self.ciscoflashpartitionendchip.yfilter != YFilter.not_set or
                    self.ciscoflashpartitionfilecount.yfilter != YFilter.not_set or
                    self.ciscoflashpartitionfilenamelength.yfilter != YFilter.not_set or
                    self.ciscoflashpartitionfreespace.yfilter != YFilter.not_set or
                    self.ciscoflashpartitionfreespaceextended.yfilter != YFilter.not_set or
                    self.ciscoflashpartitionlowspacenotifthreshold.yfilter != YFilter.not_set or
                    self.ciscoflashpartitionname.yfilter != YFilter.not_set or
                    self.ciscoflashpartitionneederasure.yfilter != YFilter.not_set or
                    self.ciscoflashpartitionsize.yfilter != YFilter.not_set or
                    self.ciscoflashpartitionsizeextended.yfilter != YFilter.not_set or
                    self.ciscoflashpartitionstartchip.yfilter != YFilter.not_set or
                    self.ciscoflashpartitionstatus.yfilter != YFilter.not_set or
                    self.ciscoflashpartitionupgrademethod.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "ciscoFlashPartitionEntry" + "[ciscoFlashDeviceIndex='" + self.ciscoflashdeviceindex.get() + "']" + "[ciscoFlashPartitionIndex='" + self.ciscoflashpartitionindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-FLASH-MIB:CISCO-FLASH-MIB/ciscoFlashPartitionTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ciscoflashdeviceindex.is_set or self.ciscoflashdeviceindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscoflashdeviceindex.get_name_leafdata())
                if (self.ciscoflashpartitionindex.is_set or self.ciscoflashpartitionindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscoflashpartitionindex.get_name_leafdata())
                if (self.ciscoflashpartitionchecksumalgorithm.is_set or self.ciscoflashpartitionchecksumalgorithm.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscoflashpartitionchecksumalgorithm.get_name_leafdata())
                if (self.ciscoflashpartitionendchip.is_set or self.ciscoflashpartitionendchip.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscoflashpartitionendchip.get_name_leafdata())
                if (self.ciscoflashpartitionfilecount.is_set or self.ciscoflashpartitionfilecount.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscoflashpartitionfilecount.get_name_leafdata())
                if (self.ciscoflashpartitionfilenamelength.is_set or self.ciscoflashpartitionfilenamelength.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscoflashpartitionfilenamelength.get_name_leafdata())
                if (self.ciscoflashpartitionfreespace.is_set or self.ciscoflashpartitionfreespace.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscoflashpartitionfreespace.get_name_leafdata())
                if (self.ciscoflashpartitionfreespaceextended.is_set or self.ciscoflashpartitionfreespaceextended.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscoflashpartitionfreespaceextended.get_name_leafdata())
                if (self.ciscoflashpartitionlowspacenotifthreshold.is_set or self.ciscoflashpartitionlowspacenotifthreshold.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscoflashpartitionlowspacenotifthreshold.get_name_leafdata())
                if (self.ciscoflashpartitionname.is_set or self.ciscoflashpartitionname.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscoflashpartitionname.get_name_leafdata())
                if (self.ciscoflashpartitionneederasure.is_set or self.ciscoflashpartitionneederasure.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscoflashpartitionneederasure.get_name_leafdata())
                if (self.ciscoflashpartitionsize.is_set or self.ciscoflashpartitionsize.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscoflashpartitionsize.get_name_leafdata())
                if (self.ciscoflashpartitionsizeextended.is_set or self.ciscoflashpartitionsizeextended.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscoflashpartitionsizeextended.get_name_leafdata())
                if (self.ciscoflashpartitionstartchip.is_set or self.ciscoflashpartitionstartchip.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscoflashpartitionstartchip.get_name_leafdata())
                if (self.ciscoflashpartitionstatus.is_set or self.ciscoflashpartitionstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscoflashpartitionstatus.get_name_leafdata())
                if (self.ciscoflashpartitionupgrademethod.is_set or self.ciscoflashpartitionupgrademethod.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscoflashpartitionupgrademethod.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ciscoFlashDeviceIndex" or name == "ciscoFlashPartitionIndex" or name == "ciscoFlashPartitionChecksumAlgorithm" or name == "ciscoFlashPartitionEndChip" or name == "ciscoFlashPartitionFileCount" or name == "ciscoFlashPartitionFileNameLength" or name == "ciscoFlashPartitionFreeSpace" or name == "ciscoFlashPartitionFreeSpaceExtended" or name == "ciscoFlashPartitionLowSpaceNotifThreshold" or name == "ciscoFlashPartitionName" or name == "ciscoFlashPartitionNeedErasure" or name == "ciscoFlashPartitionSize" or name == "ciscoFlashPartitionSizeExtended" or name == "ciscoFlashPartitionStartChip" or name == "ciscoFlashPartitionStatus" or name == "ciscoFlashPartitionUpgradeMethod"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "ciscoFlashDeviceIndex"):
                    self.ciscoflashdeviceindex = value
                    self.ciscoflashdeviceindex.value_namespace = name_space
                    self.ciscoflashdeviceindex.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoFlashPartitionIndex"):
                    self.ciscoflashpartitionindex = value
                    self.ciscoflashpartitionindex.value_namespace = name_space
                    self.ciscoflashpartitionindex.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoFlashPartitionChecksumAlgorithm"):
                    self.ciscoflashpartitionchecksumalgorithm = value
                    self.ciscoflashpartitionchecksumalgorithm.value_namespace = name_space
                    self.ciscoflashpartitionchecksumalgorithm.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoFlashPartitionEndChip"):
                    self.ciscoflashpartitionendchip = value
                    self.ciscoflashpartitionendchip.value_namespace = name_space
                    self.ciscoflashpartitionendchip.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoFlashPartitionFileCount"):
                    self.ciscoflashpartitionfilecount = value
                    self.ciscoflashpartitionfilecount.value_namespace = name_space
                    self.ciscoflashpartitionfilecount.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoFlashPartitionFileNameLength"):
                    self.ciscoflashpartitionfilenamelength = value
                    self.ciscoflashpartitionfilenamelength.value_namespace = name_space
                    self.ciscoflashpartitionfilenamelength.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoFlashPartitionFreeSpace"):
                    self.ciscoflashpartitionfreespace = value
                    self.ciscoflashpartitionfreespace.value_namespace = name_space
                    self.ciscoflashpartitionfreespace.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoFlashPartitionFreeSpaceExtended"):
                    self.ciscoflashpartitionfreespaceextended = value
                    self.ciscoflashpartitionfreespaceextended.value_namespace = name_space
                    self.ciscoflashpartitionfreespaceextended.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoFlashPartitionLowSpaceNotifThreshold"):
                    self.ciscoflashpartitionlowspacenotifthreshold = value
                    self.ciscoflashpartitionlowspacenotifthreshold.value_namespace = name_space
                    self.ciscoflashpartitionlowspacenotifthreshold.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoFlashPartitionName"):
                    self.ciscoflashpartitionname = value
                    self.ciscoflashpartitionname.value_namespace = name_space
                    self.ciscoflashpartitionname.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoFlashPartitionNeedErasure"):
                    self.ciscoflashpartitionneederasure = value
                    self.ciscoflashpartitionneederasure.value_namespace = name_space
                    self.ciscoflashpartitionneederasure.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoFlashPartitionSize"):
                    self.ciscoflashpartitionsize = value
                    self.ciscoflashpartitionsize.value_namespace = name_space
                    self.ciscoflashpartitionsize.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoFlashPartitionSizeExtended"):
                    self.ciscoflashpartitionsizeextended = value
                    self.ciscoflashpartitionsizeextended.value_namespace = name_space
                    self.ciscoflashpartitionsizeextended.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoFlashPartitionStartChip"):
                    self.ciscoflashpartitionstartchip = value
                    self.ciscoflashpartitionstartchip.value_namespace = name_space
                    self.ciscoflashpartitionstartchip.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoFlashPartitionStatus"):
                    self.ciscoflashpartitionstatus = value
                    self.ciscoflashpartitionstatus.value_namespace = name_space
                    self.ciscoflashpartitionstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoFlashPartitionUpgradeMethod"):
                    self.ciscoflashpartitionupgrademethod = value
                    self.ciscoflashpartitionupgrademethod.value_namespace = name_space
                    self.ciscoflashpartitionupgrademethod.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.ciscoflashpartitionentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.ciscoflashpartitionentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "ciscoFlashPartitionTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-FLASH-MIB:CISCO-FLASH-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "ciscoFlashPartitionEntry"):
                for c in self.ciscoflashpartitionentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoFlashMib.Ciscoflashpartitiontable.Ciscoflashpartitionentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.ciscoflashpartitionentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "ciscoFlashPartitionEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Ciscoflashfiletable(Entity):
        """
        Table of information for files in a Flash partition.
        
        .. attribute:: ciscoflashfileentry
        
        	An entry in the table of Flash file properties for each initialized Flash partition. Each entry represents a file and gives details about the file. An entry is indexed using the device number, partition number within the device, and file number within the partition
        	**type**\: list of    :py:class:`Ciscoflashfileentry <ydk.models.cisco_ios_xe.CISCO_FLASH_MIB.CiscoFlashMib.Ciscoflashfiletable.Ciscoflashfileentry>`
        
        

        """

        _prefix = 'CISCO-FLASH-MIB'
        _revision = '2013-08-06'

        def __init__(self):
            super(CiscoFlashMib.Ciscoflashfiletable, self).__init__()

            self.yang_name = "ciscoFlashFileTable"
            self.yang_parent_name = "CISCO-FLASH-MIB"

            self.ciscoflashfileentry = YList(self)

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
                        super(CiscoFlashMib.Ciscoflashfiletable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoFlashMib.Ciscoflashfiletable, self).__setattr__(name, value)


        class Ciscoflashfileentry(Entity):
            """
            An entry in the table of Flash file properties
            for each initialized Flash partition. Each entry
            represents a file and gives details about the file.
            An entry is indexed using the device number,
            partition number within the device, and file
            number within the partition.
            
            .. attribute:: ciscoflashdeviceindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            	**refers to**\:  :py:class:`ciscoflashdeviceindex <ydk.models.cisco_ios_xe.CISCO_FLASH_MIB.CiscoFlashMib.Ciscoflashdevicetable.Ciscoflashdeviceentry>`
            
            .. attribute:: ciscoflashpartitionindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            	**refers to**\:  :py:class:`ciscoflashpartitionindex <ydk.models.cisco_ios_xe.CISCO_FLASH_MIB.CiscoFlashMib.Ciscoflashpartitiontable.Ciscoflashpartitionentry>`
            
            .. attribute:: ciscoflashfileindex  <key>
            
            	Flash file sequence number used to index within a Flash partition directory table
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            .. attribute:: ciscoflashfilechecksum
            
            	File checksum stored in the file header. This checksum is computed and stored when the file is written into Flash. It serves to validate the data written into Flash. Whereas the system will generate and store the checksum internally in hexadecimal form, this object will provide the checksum in a string form. The checksum will be available for all valid and invalid\-checksum files
            	**type**\:  str
            
            .. attribute:: ciscoflashfiledate
            
            	The time at which this file was created
            	**type**\:  str
            
            .. attribute:: ciscoflashfilename
            
            	Flash file name as specified by the user copying in the file. The name should not include the colon (\:) character as it is a special separator character used to delineate the device name, partition name, and the file name
            	**type**\:  str
            
            	**length:** 1..255
            
            .. attribute:: ciscoflashfilesize
            
            	Size of the file in bytes. Note that this size does not include the size of the filesystem file header. File size will always be non\-zero
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: bytes
            
            .. attribute:: ciscoflashfilestatus
            
            	Status of a file. A file could be explicitly deleted if the file system supports such a user command facility. Alternately, an existing good file would be automatically deleted if another good file with the same name were copied in. Note that deleted files continue to occupy prime Flash real estate.  A file is marked as having an invalid checksum if any checksum mismatch was detected while writing or reading the file. Incomplete files (files truncated either because of lack of free space, or a network download failure) are also written with a bad checksum and marked as invalid
            	**type**\:   :py:class:`Ciscoflashfilestatus <ydk.models.cisco_ios_xe.CISCO_FLASH_MIB.CiscoFlashMib.Ciscoflashfiletable.Ciscoflashfileentry.Ciscoflashfilestatus>`
            
            .. attribute:: ciscoflashfiletype
            
            	Type of the file
            	**type**\:   :py:class:`Flashfiletype <ydk.models.cisco_ios_xe.CISCO_FLASH_MIB.Flashfiletype>`
            
            

            """

            _prefix = 'CISCO-FLASH-MIB'
            _revision = '2013-08-06'

            def __init__(self):
                super(CiscoFlashMib.Ciscoflashfiletable.Ciscoflashfileentry, self).__init__()

                self.yang_name = "ciscoFlashFileEntry"
                self.yang_parent_name = "ciscoFlashFileTable"

                self.ciscoflashdeviceindex = YLeaf(YType.str, "ciscoFlashDeviceIndex")

                self.ciscoflashpartitionindex = YLeaf(YType.str, "ciscoFlashPartitionIndex")

                self.ciscoflashfileindex = YLeaf(YType.uint32, "ciscoFlashFileIndex")

                self.ciscoflashfilechecksum = YLeaf(YType.str, "ciscoFlashFileChecksum")

                self.ciscoflashfiledate = YLeaf(YType.str, "ciscoFlashFileDate")

                self.ciscoflashfilename = YLeaf(YType.str, "ciscoFlashFileName")

                self.ciscoflashfilesize = YLeaf(YType.uint32, "ciscoFlashFileSize")

                self.ciscoflashfilestatus = YLeaf(YType.enumeration, "ciscoFlashFileStatus")

                self.ciscoflashfiletype = YLeaf(YType.enumeration, "ciscoFlashFileType")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("ciscoflashdeviceindex",
                                "ciscoflashpartitionindex",
                                "ciscoflashfileindex",
                                "ciscoflashfilechecksum",
                                "ciscoflashfiledate",
                                "ciscoflashfilename",
                                "ciscoflashfilesize",
                                "ciscoflashfilestatus",
                                "ciscoflashfiletype") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoFlashMib.Ciscoflashfiletable.Ciscoflashfileentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoFlashMib.Ciscoflashfiletable.Ciscoflashfileentry, self).__setattr__(name, value)

            class Ciscoflashfilestatus(Enum):
                """
                Ciscoflashfilestatus

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


            def has_data(self):
                return (
                    self.ciscoflashdeviceindex.is_set or
                    self.ciscoflashpartitionindex.is_set or
                    self.ciscoflashfileindex.is_set or
                    self.ciscoflashfilechecksum.is_set or
                    self.ciscoflashfiledate.is_set or
                    self.ciscoflashfilename.is_set or
                    self.ciscoflashfilesize.is_set or
                    self.ciscoflashfilestatus.is_set or
                    self.ciscoflashfiletype.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ciscoflashdeviceindex.yfilter != YFilter.not_set or
                    self.ciscoflashpartitionindex.yfilter != YFilter.not_set or
                    self.ciscoflashfileindex.yfilter != YFilter.not_set or
                    self.ciscoflashfilechecksum.yfilter != YFilter.not_set or
                    self.ciscoflashfiledate.yfilter != YFilter.not_set or
                    self.ciscoflashfilename.yfilter != YFilter.not_set or
                    self.ciscoflashfilesize.yfilter != YFilter.not_set or
                    self.ciscoflashfilestatus.yfilter != YFilter.not_set or
                    self.ciscoflashfiletype.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "ciscoFlashFileEntry" + "[ciscoFlashDeviceIndex='" + self.ciscoflashdeviceindex.get() + "']" + "[ciscoFlashPartitionIndex='" + self.ciscoflashpartitionindex.get() + "']" + "[ciscoFlashFileIndex='" + self.ciscoflashfileindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-FLASH-MIB:CISCO-FLASH-MIB/ciscoFlashFileTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ciscoflashdeviceindex.is_set or self.ciscoflashdeviceindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscoflashdeviceindex.get_name_leafdata())
                if (self.ciscoflashpartitionindex.is_set or self.ciscoflashpartitionindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscoflashpartitionindex.get_name_leafdata())
                if (self.ciscoflashfileindex.is_set or self.ciscoflashfileindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscoflashfileindex.get_name_leafdata())
                if (self.ciscoflashfilechecksum.is_set or self.ciscoflashfilechecksum.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscoflashfilechecksum.get_name_leafdata())
                if (self.ciscoflashfiledate.is_set or self.ciscoflashfiledate.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscoflashfiledate.get_name_leafdata())
                if (self.ciscoflashfilename.is_set or self.ciscoflashfilename.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscoflashfilename.get_name_leafdata())
                if (self.ciscoflashfilesize.is_set or self.ciscoflashfilesize.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscoflashfilesize.get_name_leafdata())
                if (self.ciscoflashfilestatus.is_set or self.ciscoflashfilestatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscoflashfilestatus.get_name_leafdata())
                if (self.ciscoflashfiletype.is_set or self.ciscoflashfiletype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscoflashfiletype.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ciscoFlashDeviceIndex" or name == "ciscoFlashPartitionIndex" or name == "ciscoFlashFileIndex" or name == "ciscoFlashFileChecksum" or name == "ciscoFlashFileDate" or name == "ciscoFlashFileName" or name == "ciscoFlashFileSize" or name == "ciscoFlashFileStatus" or name == "ciscoFlashFileType"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "ciscoFlashDeviceIndex"):
                    self.ciscoflashdeviceindex = value
                    self.ciscoflashdeviceindex.value_namespace = name_space
                    self.ciscoflashdeviceindex.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoFlashPartitionIndex"):
                    self.ciscoflashpartitionindex = value
                    self.ciscoflashpartitionindex.value_namespace = name_space
                    self.ciscoflashpartitionindex.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoFlashFileIndex"):
                    self.ciscoflashfileindex = value
                    self.ciscoflashfileindex.value_namespace = name_space
                    self.ciscoflashfileindex.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoFlashFileChecksum"):
                    self.ciscoflashfilechecksum = value
                    self.ciscoflashfilechecksum.value_namespace = name_space
                    self.ciscoflashfilechecksum.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoFlashFileDate"):
                    self.ciscoflashfiledate = value
                    self.ciscoflashfiledate.value_namespace = name_space
                    self.ciscoflashfiledate.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoFlashFileName"):
                    self.ciscoflashfilename = value
                    self.ciscoflashfilename.value_namespace = name_space
                    self.ciscoflashfilename.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoFlashFileSize"):
                    self.ciscoflashfilesize = value
                    self.ciscoflashfilesize.value_namespace = name_space
                    self.ciscoflashfilesize.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoFlashFileStatus"):
                    self.ciscoflashfilestatus = value
                    self.ciscoflashfilestatus.value_namespace = name_space
                    self.ciscoflashfilestatus.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoFlashFileType"):
                    self.ciscoflashfiletype = value
                    self.ciscoflashfiletype.value_namespace = name_space
                    self.ciscoflashfiletype.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.ciscoflashfileentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.ciscoflashfileentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "ciscoFlashFileTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-FLASH-MIB:CISCO-FLASH-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "ciscoFlashFileEntry"):
                for c in self.ciscoflashfileentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoFlashMib.Ciscoflashfiletable.Ciscoflashfileentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.ciscoflashfileentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "ciscoFlashFileEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Ciscoflashfilebytypetable(Entity):
        """
        Table of information for files on the manageable
        flash devices sorted by File Types.
        
        .. attribute:: ciscoflashfilebytypeentry
        
        	An entry in the table of Flash file properties for each initialized Flash partition. Each entry represents a file sorted by file type.  This table contains exactly the same set of rows as are contained in the ciscoFlashFileTable but in a different order, i.e., ordered by  the type of file, given by  ciscoFlashFileType; the device number, given by ciscoFlashDeviceIndex; the partition number within the device, given by ciscoFlashPartitionIndex; the file number within the partition, given by ciscoFlashFileIndex
        	**type**\: list of    :py:class:`Ciscoflashfilebytypeentry <ydk.models.cisco_ios_xe.CISCO_FLASH_MIB.CiscoFlashMib.Ciscoflashfilebytypetable.Ciscoflashfilebytypeentry>`
        
        

        """

        _prefix = 'CISCO-FLASH-MIB'
        _revision = '2013-08-06'

        def __init__(self):
            super(CiscoFlashMib.Ciscoflashfilebytypetable, self).__init__()

            self.yang_name = "ciscoFlashFileByTypeTable"
            self.yang_parent_name = "CISCO-FLASH-MIB"

            self.ciscoflashfilebytypeentry = YList(self)

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
                        super(CiscoFlashMib.Ciscoflashfilebytypetable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoFlashMib.Ciscoflashfilebytypetable, self).__setattr__(name, value)


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
            
            .. attribute:: ciscoflashfiletype  <key>
            
            	
            	**type**\:   :py:class:`Flashfiletype <ydk.models.cisco_ios_xe.CISCO_FLASH_MIB.Flashfiletype>`
            
            .. attribute:: ciscoflashdeviceindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            	**refers to**\:  :py:class:`ciscoflashdeviceindex <ydk.models.cisco_ios_xe.CISCO_FLASH_MIB.CiscoFlashMib.Ciscoflashdevicetable.Ciscoflashdeviceentry>`
            
            .. attribute:: ciscoflashpartitionindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            	**refers to**\:  :py:class:`ciscoflashpartitionindex <ydk.models.cisco_ios_xe.CISCO_FLASH_MIB.CiscoFlashMib.Ciscoflashpartitiontable.Ciscoflashpartitionentry>`
            
            .. attribute:: ciscoflashfileindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            	**refers to**\:  :py:class:`ciscoflashfileindex <ydk.models.cisco_ios_xe.CISCO_FLASH_MIB.CiscoFlashMib.Ciscoflashfiletable.Ciscoflashfileentry>`
            
            .. attribute:: ciscoflashfilebytypechecksum
            
            	This object represents exactly the same info as ciscoFlashFileChecksum object in ciscoFlashFileTable
            	**type**\:  str
            
            .. attribute:: ciscoflashfilebytypedate
            
            	This object represents exactly the same info as ciscoFlashFileDate object in ciscoFlashFileTable
            	**type**\:  str
            
            .. attribute:: ciscoflashfilebytypename
            
            	This object represents exactly the same info as ciscoFlashFileName object in ciscoFlashFileTable
            	**type**\:  str
            
            	**length:** 1..255
            
            .. attribute:: ciscoflashfilebytypesize
            
            	This object represents exactly the same info as ciscoFlashFileSize object in ciscoFlashFileTable
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: bytes
            
            .. attribute:: ciscoflashfilebytypestatus
            
            	This object represents exactly the same info as ciscoFlashFileStatus object in ciscoFlashFileTable
            	**type**\:   :py:class:`Ciscoflashfilebytypestatus <ydk.models.cisco_ios_xe.CISCO_FLASH_MIB.CiscoFlashMib.Ciscoflashfilebytypetable.Ciscoflashfilebytypeentry.Ciscoflashfilebytypestatus>`
            
            

            """

            _prefix = 'CISCO-FLASH-MIB'
            _revision = '2013-08-06'

            def __init__(self):
                super(CiscoFlashMib.Ciscoflashfilebytypetable.Ciscoflashfilebytypeentry, self).__init__()

                self.yang_name = "ciscoFlashFileByTypeEntry"
                self.yang_parent_name = "ciscoFlashFileByTypeTable"

                self.ciscoflashfiletype = YLeaf(YType.enumeration, "ciscoFlashFileType")

                self.ciscoflashdeviceindex = YLeaf(YType.str, "ciscoFlashDeviceIndex")

                self.ciscoflashpartitionindex = YLeaf(YType.str, "ciscoFlashPartitionIndex")

                self.ciscoflashfileindex = YLeaf(YType.str, "ciscoFlashFileIndex")

                self.ciscoflashfilebytypechecksum = YLeaf(YType.str, "ciscoFlashFileByTypeChecksum")

                self.ciscoflashfilebytypedate = YLeaf(YType.str, "ciscoFlashFileByTypeDate")

                self.ciscoflashfilebytypename = YLeaf(YType.str, "ciscoFlashFileByTypeName")

                self.ciscoflashfilebytypesize = YLeaf(YType.uint32, "ciscoFlashFileByTypeSize")

                self.ciscoflashfilebytypestatus = YLeaf(YType.enumeration, "ciscoFlashFileByTypeStatus")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("ciscoflashfiletype",
                                "ciscoflashdeviceindex",
                                "ciscoflashpartitionindex",
                                "ciscoflashfileindex",
                                "ciscoflashfilebytypechecksum",
                                "ciscoflashfilebytypedate",
                                "ciscoflashfilebytypename",
                                "ciscoflashfilebytypesize",
                                "ciscoflashfilebytypestatus") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoFlashMib.Ciscoflashfilebytypetable.Ciscoflashfilebytypeentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoFlashMib.Ciscoflashfilebytypetable.Ciscoflashfilebytypeentry, self).__setattr__(name, value)

            class Ciscoflashfilebytypestatus(Enum):
                """
                Ciscoflashfilebytypestatus

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


            def has_data(self):
                return (
                    self.ciscoflashfiletype.is_set or
                    self.ciscoflashdeviceindex.is_set or
                    self.ciscoflashpartitionindex.is_set or
                    self.ciscoflashfileindex.is_set or
                    self.ciscoflashfilebytypechecksum.is_set or
                    self.ciscoflashfilebytypedate.is_set or
                    self.ciscoflashfilebytypename.is_set or
                    self.ciscoflashfilebytypesize.is_set or
                    self.ciscoflashfilebytypestatus.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ciscoflashfiletype.yfilter != YFilter.not_set or
                    self.ciscoflashdeviceindex.yfilter != YFilter.not_set or
                    self.ciscoflashpartitionindex.yfilter != YFilter.not_set or
                    self.ciscoflashfileindex.yfilter != YFilter.not_set or
                    self.ciscoflashfilebytypechecksum.yfilter != YFilter.not_set or
                    self.ciscoflashfilebytypedate.yfilter != YFilter.not_set or
                    self.ciscoflashfilebytypename.yfilter != YFilter.not_set or
                    self.ciscoflashfilebytypesize.yfilter != YFilter.not_set or
                    self.ciscoflashfilebytypestatus.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "ciscoFlashFileByTypeEntry" + "[ciscoFlashFileType='" + self.ciscoflashfiletype.get() + "']" + "[ciscoFlashDeviceIndex='" + self.ciscoflashdeviceindex.get() + "']" + "[ciscoFlashPartitionIndex='" + self.ciscoflashpartitionindex.get() + "']" + "[ciscoFlashFileIndex='" + self.ciscoflashfileindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-FLASH-MIB:CISCO-FLASH-MIB/ciscoFlashFileByTypeTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ciscoflashfiletype.is_set or self.ciscoflashfiletype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscoflashfiletype.get_name_leafdata())
                if (self.ciscoflashdeviceindex.is_set or self.ciscoflashdeviceindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscoflashdeviceindex.get_name_leafdata())
                if (self.ciscoflashpartitionindex.is_set or self.ciscoflashpartitionindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscoflashpartitionindex.get_name_leafdata())
                if (self.ciscoflashfileindex.is_set or self.ciscoflashfileindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscoflashfileindex.get_name_leafdata())
                if (self.ciscoflashfilebytypechecksum.is_set or self.ciscoflashfilebytypechecksum.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscoflashfilebytypechecksum.get_name_leafdata())
                if (self.ciscoflashfilebytypedate.is_set or self.ciscoflashfilebytypedate.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscoflashfilebytypedate.get_name_leafdata())
                if (self.ciscoflashfilebytypename.is_set or self.ciscoflashfilebytypename.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscoflashfilebytypename.get_name_leafdata())
                if (self.ciscoflashfilebytypesize.is_set or self.ciscoflashfilebytypesize.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscoflashfilebytypesize.get_name_leafdata())
                if (self.ciscoflashfilebytypestatus.is_set or self.ciscoflashfilebytypestatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscoflashfilebytypestatus.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ciscoFlashFileType" or name == "ciscoFlashDeviceIndex" or name == "ciscoFlashPartitionIndex" or name == "ciscoFlashFileIndex" or name == "ciscoFlashFileByTypeChecksum" or name == "ciscoFlashFileByTypeDate" or name == "ciscoFlashFileByTypeName" or name == "ciscoFlashFileByTypeSize" or name == "ciscoFlashFileByTypeStatus"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "ciscoFlashFileType"):
                    self.ciscoflashfiletype = value
                    self.ciscoflashfiletype.value_namespace = name_space
                    self.ciscoflashfiletype.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoFlashDeviceIndex"):
                    self.ciscoflashdeviceindex = value
                    self.ciscoflashdeviceindex.value_namespace = name_space
                    self.ciscoflashdeviceindex.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoFlashPartitionIndex"):
                    self.ciscoflashpartitionindex = value
                    self.ciscoflashpartitionindex.value_namespace = name_space
                    self.ciscoflashpartitionindex.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoFlashFileIndex"):
                    self.ciscoflashfileindex = value
                    self.ciscoflashfileindex.value_namespace = name_space
                    self.ciscoflashfileindex.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoFlashFileByTypeChecksum"):
                    self.ciscoflashfilebytypechecksum = value
                    self.ciscoflashfilebytypechecksum.value_namespace = name_space
                    self.ciscoflashfilebytypechecksum.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoFlashFileByTypeDate"):
                    self.ciscoflashfilebytypedate = value
                    self.ciscoflashfilebytypedate.value_namespace = name_space
                    self.ciscoflashfilebytypedate.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoFlashFileByTypeName"):
                    self.ciscoflashfilebytypename = value
                    self.ciscoflashfilebytypename.value_namespace = name_space
                    self.ciscoflashfilebytypename.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoFlashFileByTypeSize"):
                    self.ciscoflashfilebytypesize = value
                    self.ciscoflashfilebytypesize.value_namespace = name_space
                    self.ciscoflashfilebytypesize.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoFlashFileByTypeStatus"):
                    self.ciscoflashfilebytypestatus = value
                    self.ciscoflashfilebytypestatus.value_namespace = name_space
                    self.ciscoflashfilebytypestatus.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.ciscoflashfilebytypeentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.ciscoflashfilebytypeentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "ciscoFlashFileByTypeTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-FLASH-MIB:CISCO-FLASH-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "ciscoFlashFileByTypeEntry"):
                for c in self.ciscoflashfilebytypeentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoFlashMib.Ciscoflashfilebytypetable.Ciscoflashfilebytypeentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.ciscoflashfilebytypeentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "ciscoFlashFileByTypeEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Ciscoflashcopytable(Entity):
        """
        A table of Flash copy operation entries. Each
        entry represents a Flash copy operation (to or
        from Flash) that has been initiated.
        
        .. attribute:: ciscoflashcopyentry
        
        	A Flash copy operation entry. Each entry consists of a command, a source, and optional parameters such as protocol to be used, a destination, a server address, etc.  A management station wishing to create an entry should first generate a pseudo\-random serial number to be used as the index to this sparse table.  The station should then create the associated instance of the row status object. It must also, either in the same or in successive PDUs, create the associated instance of the command and parameter objects. It should also modify the default values for any of the parameter objects if the defaults are not appropriate.  Once the appropriate instances of all the command objects have been created, either by an explicit SNMP set request or by default, the row status should be set to active to initiate the operation. Note that this entire procedure may be initiated via a single set request which specifies a row status  of createAndGo as well as specifies valid values for the non\-defaulted parameter objects.  Once an operation has been activated, it cannot be stopped.  Once the operation completes, the management station should retrieve the value of the status object (and time if desired), and delete the entry.  In order to prevent old entries from clogging the table, entries will be aged out, but an entry will never be deleted within 5 minutes of completing
        	**type**\: list of    :py:class:`Ciscoflashcopyentry <ydk.models.cisco_ios_xe.CISCO_FLASH_MIB.CiscoFlashMib.Ciscoflashcopytable.Ciscoflashcopyentry>`
        
        

        """

        _prefix = 'CISCO-FLASH-MIB'
        _revision = '2013-08-06'

        def __init__(self):
            super(CiscoFlashMib.Ciscoflashcopytable, self).__init__()

            self.yang_name = "ciscoFlashCopyTable"
            self.yang_parent_name = "CISCO-FLASH-MIB"

            self.ciscoflashcopyentry = YList(self)

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
                        super(CiscoFlashMib.Ciscoflashcopytable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoFlashMib.Ciscoflashcopytable, self).__setattr__(name, value)


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
            
            .. attribute:: ciscoflashcopyserialnumber  <key>
            
            	Object which specifies a unique entry in the table. A management station wishing to initiate a copy operation should use a pseudo\-random value for this object when creating or modifying an instance of a ciscoFlashCopyEntry
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: ciscoflashcopycommand
            
            	The copy command to be executed. Mandatory. Note that it is possible for a system to support multiple file systems (different file systems on different Flash devices, or different file systems on different partitions within a device). Each such file system may support only a subset of these commands. If a command is unsupported, the invalidOperation(3) error will be reported in the operation status.  Command                 Remarks copyToFlashWithErase    Copy a file to flash; erase                         flash before copy.                         Use the TFTP or rcp protocol. copyToFlashWithoutErase Copy a file to flash; do not                         erase.                         Note that this command will fail                         if the PartitionNeedErasure                         object specifies that the                         partition being copied to needs                         erasure.                         Use the TFTP or rcp protocol. copyFromFlash           Copy a file from flash using                         the TFTP, rcp or lex protocol.                         Note that the lex protocol                         can only be used to copy to a                         lex device. copyFromFlhLog          Copy contents of FLH log to                         server using TFTP protocol.   Command table           Parameters copyToFlashWithErase    CopyProtocol                         CopyServerAddress                         CopySourceName                         CopyDestinationName (opt)                         CopyRemoteUserName (opt)                         CopyNotifyOnCompletion (opt) copyToFlashWithoutErase CopyProtocol                         CopyServerAddress                         CopySourceName                         CopyDestinationName (opt)                         CopyRemoteUserName (opt)                         CopyNotifyOnCompletion (opt) copyFromFlash           CopyProtocol                         CopyServerAddress                         CopySourceName                         CopyDestinationName (opt)                         CopyRemoteUserName (opt)                         CopyNotifyOnCompletion (opt) copyFromFlhLog          CopyProtocol                         CopyServerAddress                         CopyDestinationName                         CopyNotifyOnCompletion (opt)
            	**type**\:   :py:class:`Ciscoflashcopycommand <ydk.models.cisco_ios_xe.CISCO_FLASH_MIB.CiscoFlashMib.Ciscoflashcopytable.Ciscoflashcopyentry.Ciscoflashcopycommand>`
            
            .. attribute:: ciscoflashcopydestinationname
            
            	Destination file name.  For a copy to Flash\: File name must be of the form         {device>\:][<partition>\:]<file> where <device> is a value obtained from FlashDeviceName,       <partition> is obtained from FlashPartitionName   and <file> is any character string that does not have embedded colon characters. A management station could derive its own partition name as per the description for the ciscoFlashPartitionName object. If <device> is not specified, the default Flash device will be assumed. If <partition> is not specified, the default partition will be assumed. If a device is not partitioned into 2 or more partitions, this value may be left out. If <file> is not specified, it will default to <file> specified in ciscoFlashCopySourceName.  For a copy from Flash via tftp or rcp, the file name will be as per the file naming conventions and destination sub\-directory on the server. If not specified, <file> from the source file name will be used. For a copy from Flash via lex, this string will consist of numeric characters specifying the interface on the lex box that will receive the source flash image
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: ciscoflashcopyentrystatus
            
            	The status of this table entry
            	**type**\:   :py:class:`Rowstatus <ydk.models.cisco_ios_xe.SNMPv2_TC.Rowstatus>`
            
            .. attribute:: ciscoflashcopynotifyoncompletion
            
            	Specifies whether or not a notification should be generated on the completion of the copy operation. If specified, ciscoFlashCopyCompletionTrap will be generated. It is the responsibility of the management entity to ensure that the SNMP administrative model is configured in such a way as to allow the notification to be delivered
            	**type**\:  bool
            
            .. attribute:: ciscoflashcopyprotocol
            
            	The protocol to be used for any copy. Optional. Will default to tftp if not specified.  Since feature support depends on a software release, version number within the release, platform, and maybe the image type (subset type), a management station would be expected to somehow determine the protocol support for a command
            	**type**\:   :py:class:`Ciscoflashcopyprotocol <ydk.models.cisco_ios_xe.CISCO_FLASH_MIB.CiscoFlashMib.Ciscoflashcopytable.Ciscoflashcopyentry.Ciscoflashcopyprotocol>`
            
            .. attribute:: ciscoflashcopyremotepassword
            
            	Password used by ftp, sftp or scp for copying a file to/from an ftp/sftp/scp server. This object must be created when the ciscoFlashCopyProtocol is ftp, sftp or scp. Reading it returns a zero\-length string for security reasons
            	**type**\:  str
            
            	**length:** 1..40
            
            .. attribute:: ciscoflashcopyremoteusername
            
            	Remote user name for copy via rcp protocol. Optional. This object will be ignored for protocols other than rcp. If specified, it will override the remote user\-name configured through the         rcmd remote\-username configuration command. The remote user\-name is sent as the server user\-name in an rcp command request sent by the system to a remote rcp server
            	**type**\:  str
            
            	**length:** 1..255
            
            .. attribute:: ciscoflashcopyserveraddress
            
            	The server address to be used for any copy. Optional. Will default to 'FFFFFFFF'H  (or 255.255.255.255).  Since this object can just hold only IPv4 Transport type, it is deprecated and replaced by ciscoFlashCopyServerAddrRev1
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**status**\: deprecated
            
            .. attribute:: ciscoflashcopyserveraddrrev1
            
            	The server address to be used for any copy. Optional. Will default to 'FFFFFFFF'H  (or 255.255.255.255).  The Format of this address depends on the value of the ciscoFlashCopyServerAddrType.  This object deprecates the old ciscoFlashCopyServerAddress object
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: ciscoflashcopyserveraddrtype
            
            	This object indicates the transport type of the address contained in ciscoFlashCopyServerAddrRev1. Optional. Will default to '1' (IPv4 address type)
            	**type**\:   :py:class:`Inetaddresstype <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.Inetaddresstype>`
            
            .. attribute:: ciscoflashcopysourcename
            
            	Source file name, either in Flash or on a server, depending on the type of copy command. Mandatory.  For a copy from Flash\: File name must be of the form         [device>\:][\:] where  is a value obtained from FlashDeviceName,          is obtained from FlashPartitionName     and  is the name of a file in Flash. A management station could derive its own partition name as per the description for the ciscoFlashPartitionName object. If <device> is not specified, the default Flash device will be assumed. If <partition> is not specified, the default partition will be assumed. If a device is not partitioned into 2 or more partitions, this value may be left out.  For a copy to Flash, the file name will be as per the file naming conventions and path to the file on the server
            	**type**\:  str
            
            	**length:** 1..255
            
            .. attribute:: ciscoflashcopystatus
            
            	The status of the specified copy operation.  copyOperationPending \:         operation request is received and         pending for validation and process  copyInProgress \:         specified operation is active  copyOperationSuccess \:         specified operation is supported and         completed successfully  copyInvalidOperation \:         command invalid or command\-protocol\-device         combination unsupported  copyInvalidProtocol \:         invalid protocol specified  copyInvalidSourceName \:         invalid source file name specified         For the  copy from flash to lex operation, this         error code will be returned when the source file         is not a valid lex image.  copyInvalidDestName \:         invalid target name (file or partition or         device name) specified         For the  copy from flash to lex operation, this         error code will be returned when no lex devices         are connected to the router or when an invalid         lex interface number has been specified in         the destination string.  copyInvalidServerAddress \:         invalid server address specified  copyDeviceBusy \:         specified device is in use and locked by         another process  copyDeviceOpenError \:         invalid device name  copyDeviceError \:         device read, write or erase error  copyDeviceNotProgrammable \:         device is read\-only but a write or erase         operation was specified  copyDeviceFull \:         device is filled to capacity  copyFileOpenError \:         invalid file name; file not found in partition  copyFileTransferError \:         file transfer was unsuccessfull; network failure  copyFileChecksumError \:         file checksum in Flash failed  copyNoMemory \:         system running low on memory  copyUnknownFailure \:         failure unknown  copyProhibited\:       stop user from overwriting current boot image file
            	**type**\:   :py:class:`Ciscoflashcopystatus <ydk.models.cisco_ios_xe.CISCO_FLASH_MIB.CiscoFlashMib.Ciscoflashcopytable.Ciscoflashcopyentry.Ciscoflashcopystatus>`
            
            .. attribute:: ciscoflashcopytime
            
            	Time taken for the copy operation. This object will be like a stopwatch, starting when the operation starts, stopping when the operation completes. If a management entity keeps a database of completion times for various operations, it can then use the stopwatch capability to display percentage completion time
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ciscoflashcopyverify
            
            	Specifies whether the file that is copied need to be verified for integrity / authenticity, after copy succeeds. If it is set to true, and if the file that is copied doesn't have integrity /authenticity attachement, or the integrity / authenticity check fails, then the command will be aborted, and the file that is copied will be deleted from the destination file system
            	**type**\:  bool
            
            

            """

            _prefix = 'CISCO-FLASH-MIB'
            _revision = '2013-08-06'

            def __init__(self):
                super(CiscoFlashMib.Ciscoflashcopytable.Ciscoflashcopyentry, self).__init__()

                self.yang_name = "ciscoFlashCopyEntry"
                self.yang_parent_name = "ciscoFlashCopyTable"

                self.ciscoflashcopyserialnumber = YLeaf(YType.int32, "ciscoFlashCopySerialNumber")

                self.ciscoflashcopycommand = YLeaf(YType.enumeration, "ciscoFlashCopyCommand")

                self.ciscoflashcopydestinationname = YLeaf(YType.str, "ciscoFlashCopyDestinationName")

                self.ciscoflashcopyentrystatus = YLeaf(YType.enumeration, "ciscoFlashCopyEntryStatus")

                self.ciscoflashcopynotifyoncompletion = YLeaf(YType.boolean, "ciscoFlashCopyNotifyOnCompletion")

                self.ciscoflashcopyprotocol = YLeaf(YType.enumeration, "ciscoFlashCopyProtocol")

                self.ciscoflashcopyremotepassword = YLeaf(YType.str, "ciscoFlashCopyRemotePassword")

                self.ciscoflashcopyremoteusername = YLeaf(YType.str, "ciscoFlashCopyRemoteUserName")

                self.ciscoflashcopyserveraddress = YLeaf(YType.str, "ciscoFlashCopyServerAddress")

                self.ciscoflashcopyserveraddrrev1 = YLeaf(YType.str, "ciscoFlashCopyServerAddrRev1")

                self.ciscoflashcopyserveraddrtype = YLeaf(YType.enumeration, "ciscoFlashCopyServerAddrType")

                self.ciscoflashcopysourcename = YLeaf(YType.str, "ciscoFlashCopySourceName")

                self.ciscoflashcopystatus = YLeaf(YType.enumeration, "ciscoFlashCopyStatus")

                self.ciscoflashcopytime = YLeaf(YType.uint32, "ciscoFlashCopyTime")

                self.ciscoflashcopyverify = YLeaf(YType.boolean, "ciscoFlashCopyVerify")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("ciscoflashcopyserialnumber",
                                "ciscoflashcopycommand",
                                "ciscoflashcopydestinationname",
                                "ciscoflashcopyentrystatus",
                                "ciscoflashcopynotifyoncompletion",
                                "ciscoflashcopyprotocol",
                                "ciscoflashcopyremotepassword",
                                "ciscoflashcopyremoteusername",
                                "ciscoflashcopyserveraddress",
                                "ciscoflashcopyserveraddrrev1",
                                "ciscoflashcopyserveraddrtype",
                                "ciscoflashcopysourcename",
                                "ciscoflashcopystatus",
                                "ciscoflashcopytime",
                                "ciscoflashcopyverify") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoFlashMib.Ciscoflashcopytable.Ciscoflashcopyentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoFlashMib.Ciscoflashcopytable.Ciscoflashcopyentry, self).__setattr__(name, value)

            class Ciscoflashcopycommand(Enum):
                """
                Ciscoflashcopycommand

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
                Ciscoflashcopyprotocol

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
                Ciscoflashcopystatus

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


            def has_data(self):
                return (
                    self.ciscoflashcopyserialnumber.is_set or
                    self.ciscoflashcopycommand.is_set or
                    self.ciscoflashcopydestinationname.is_set or
                    self.ciscoflashcopyentrystatus.is_set or
                    self.ciscoflashcopynotifyoncompletion.is_set or
                    self.ciscoflashcopyprotocol.is_set or
                    self.ciscoflashcopyremotepassword.is_set or
                    self.ciscoflashcopyremoteusername.is_set or
                    self.ciscoflashcopyserveraddress.is_set or
                    self.ciscoflashcopyserveraddrrev1.is_set or
                    self.ciscoflashcopyserveraddrtype.is_set or
                    self.ciscoflashcopysourcename.is_set or
                    self.ciscoflashcopystatus.is_set or
                    self.ciscoflashcopytime.is_set or
                    self.ciscoflashcopyverify.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ciscoflashcopyserialnumber.yfilter != YFilter.not_set or
                    self.ciscoflashcopycommand.yfilter != YFilter.not_set or
                    self.ciscoflashcopydestinationname.yfilter != YFilter.not_set or
                    self.ciscoflashcopyentrystatus.yfilter != YFilter.not_set or
                    self.ciscoflashcopynotifyoncompletion.yfilter != YFilter.not_set or
                    self.ciscoflashcopyprotocol.yfilter != YFilter.not_set or
                    self.ciscoflashcopyremotepassword.yfilter != YFilter.not_set or
                    self.ciscoflashcopyremoteusername.yfilter != YFilter.not_set or
                    self.ciscoflashcopyserveraddress.yfilter != YFilter.not_set or
                    self.ciscoflashcopyserveraddrrev1.yfilter != YFilter.not_set or
                    self.ciscoflashcopyserveraddrtype.yfilter != YFilter.not_set or
                    self.ciscoflashcopysourcename.yfilter != YFilter.not_set or
                    self.ciscoflashcopystatus.yfilter != YFilter.not_set or
                    self.ciscoflashcopytime.yfilter != YFilter.not_set or
                    self.ciscoflashcopyverify.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "ciscoFlashCopyEntry" + "[ciscoFlashCopySerialNumber='" + self.ciscoflashcopyserialnumber.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-FLASH-MIB:CISCO-FLASH-MIB/ciscoFlashCopyTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ciscoflashcopyserialnumber.is_set or self.ciscoflashcopyserialnumber.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscoflashcopyserialnumber.get_name_leafdata())
                if (self.ciscoflashcopycommand.is_set or self.ciscoflashcopycommand.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscoflashcopycommand.get_name_leafdata())
                if (self.ciscoflashcopydestinationname.is_set or self.ciscoflashcopydestinationname.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscoflashcopydestinationname.get_name_leafdata())
                if (self.ciscoflashcopyentrystatus.is_set or self.ciscoflashcopyentrystatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscoflashcopyentrystatus.get_name_leafdata())
                if (self.ciscoflashcopynotifyoncompletion.is_set or self.ciscoflashcopynotifyoncompletion.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscoflashcopynotifyoncompletion.get_name_leafdata())
                if (self.ciscoflashcopyprotocol.is_set or self.ciscoflashcopyprotocol.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscoflashcopyprotocol.get_name_leafdata())
                if (self.ciscoflashcopyremotepassword.is_set or self.ciscoflashcopyremotepassword.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscoflashcopyremotepassword.get_name_leafdata())
                if (self.ciscoflashcopyremoteusername.is_set or self.ciscoflashcopyremoteusername.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscoflashcopyremoteusername.get_name_leafdata())
                if (self.ciscoflashcopyserveraddress.is_set or self.ciscoflashcopyserveraddress.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscoflashcopyserveraddress.get_name_leafdata())
                if (self.ciscoflashcopyserveraddrrev1.is_set or self.ciscoflashcopyserveraddrrev1.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscoflashcopyserveraddrrev1.get_name_leafdata())
                if (self.ciscoflashcopyserveraddrtype.is_set or self.ciscoflashcopyserveraddrtype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscoflashcopyserveraddrtype.get_name_leafdata())
                if (self.ciscoflashcopysourcename.is_set or self.ciscoflashcopysourcename.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscoflashcopysourcename.get_name_leafdata())
                if (self.ciscoflashcopystatus.is_set or self.ciscoflashcopystatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscoflashcopystatus.get_name_leafdata())
                if (self.ciscoflashcopytime.is_set or self.ciscoflashcopytime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscoflashcopytime.get_name_leafdata())
                if (self.ciscoflashcopyverify.is_set or self.ciscoflashcopyverify.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscoflashcopyverify.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ciscoFlashCopySerialNumber" or name == "ciscoFlashCopyCommand" or name == "ciscoFlashCopyDestinationName" or name == "ciscoFlashCopyEntryStatus" or name == "ciscoFlashCopyNotifyOnCompletion" or name == "ciscoFlashCopyProtocol" or name == "ciscoFlashCopyRemotePassword" or name == "ciscoFlashCopyRemoteUserName" or name == "ciscoFlashCopyServerAddress" or name == "ciscoFlashCopyServerAddrRev1" or name == "ciscoFlashCopyServerAddrType" or name == "ciscoFlashCopySourceName" or name == "ciscoFlashCopyStatus" or name == "ciscoFlashCopyTime" or name == "ciscoFlashCopyVerify"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "ciscoFlashCopySerialNumber"):
                    self.ciscoflashcopyserialnumber = value
                    self.ciscoflashcopyserialnumber.value_namespace = name_space
                    self.ciscoflashcopyserialnumber.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoFlashCopyCommand"):
                    self.ciscoflashcopycommand = value
                    self.ciscoflashcopycommand.value_namespace = name_space
                    self.ciscoflashcopycommand.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoFlashCopyDestinationName"):
                    self.ciscoflashcopydestinationname = value
                    self.ciscoflashcopydestinationname.value_namespace = name_space
                    self.ciscoflashcopydestinationname.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoFlashCopyEntryStatus"):
                    self.ciscoflashcopyentrystatus = value
                    self.ciscoflashcopyentrystatus.value_namespace = name_space
                    self.ciscoflashcopyentrystatus.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoFlashCopyNotifyOnCompletion"):
                    self.ciscoflashcopynotifyoncompletion = value
                    self.ciscoflashcopynotifyoncompletion.value_namespace = name_space
                    self.ciscoflashcopynotifyoncompletion.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoFlashCopyProtocol"):
                    self.ciscoflashcopyprotocol = value
                    self.ciscoflashcopyprotocol.value_namespace = name_space
                    self.ciscoflashcopyprotocol.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoFlashCopyRemotePassword"):
                    self.ciscoflashcopyremotepassword = value
                    self.ciscoflashcopyremotepassword.value_namespace = name_space
                    self.ciscoflashcopyremotepassword.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoFlashCopyRemoteUserName"):
                    self.ciscoflashcopyremoteusername = value
                    self.ciscoflashcopyremoteusername.value_namespace = name_space
                    self.ciscoflashcopyremoteusername.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoFlashCopyServerAddress"):
                    self.ciscoflashcopyserveraddress = value
                    self.ciscoflashcopyserveraddress.value_namespace = name_space
                    self.ciscoflashcopyserveraddress.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoFlashCopyServerAddrRev1"):
                    self.ciscoflashcopyserveraddrrev1 = value
                    self.ciscoflashcopyserveraddrrev1.value_namespace = name_space
                    self.ciscoflashcopyserveraddrrev1.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoFlashCopyServerAddrType"):
                    self.ciscoflashcopyserveraddrtype = value
                    self.ciscoflashcopyserveraddrtype.value_namespace = name_space
                    self.ciscoflashcopyserveraddrtype.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoFlashCopySourceName"):
                    self.ciscoflashcopysourcename = value
                    self.ciscoflashcopysourcename.value_namespace = name_space
                    self.ciscoflashcopysourcename.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoFlashCopyStatus"):
                    self.ciscoflashcopystatus = value
                    self.ciscoflashcopystatus.value_namespace = name_space
                    self.ciscoflashcopystatus.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoFlashCopyTime"):
                    self.ciscoflashcopytime = value
                    self.ciscoflashcopytime.value_namespace = name_space
                    self.ciscoflashcopytime.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoFlashCopyVerify"):
                    self.ciscoflashcopyverify = value
                    self.ciscoflashcopyverify.value_namespace = name_space
                    self.ciscoflashcopyverify.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.ciscoflashcopyentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.ciscoflashcopyentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "ciscoFlashCopyTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-FLASH-MIB:CISCO-FLASH-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "ciscoFlashCopyEntry"):
                for c in self.ciscoflashcopyentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoFlashMib.Ciscoflashcopytable.Ciscoflashcopyentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.ciscoflashcopyentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "ciscoFlashCopyEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Ciscoflashpartitioningtable(Entity):
        """
        A table of Flash partitioning operation entries. Each
        entry represents a Flash partitioning operation that
        has been initiated.
        
        .. attribute:: ciscoflashpartitioningentry
        
        	A Flash partitioning operation entry. Each entry consists of the command, the target device, the partition count, and optionally the partition sizes.  A management station wishing to create an entry should first generate a pseudo\-random serial number to be used as the index to this sparse table.  The station should then create the associated instance of the row status object. It must also, either in the same or in successive PDUs, create the associated instance of the command and parameter objects. It should also modify the default values for any of the parameter objects if the defaults are not appropriate.  Once the appropriate instances of all the command objects have been created, either by an explicit SNMP set request or by default, the row status should be set to active to initiate the operation. Note that this entire procedure may be initiated via a single set request which specifies a row status of createAndGo as well as specifies valid values for the non\-defaulted parameter objects.  Once an operation has been activated, it cannot be stopped.  Once the operation completes, the management station should retrieve the value of the status object (and time if desired), and delete the entry.  In order to prevent old entries from clogging the table, entries will be aged out, but an entry will never be deleted within 5 minutes of completing
        	**type**\: list of    :py:class:`Ciscoflashpartitioningentry <ydk.models.cisco_ios_xe.CISCO_FLASH_MIB.CiscoFlashMib.Ciscoflashpartitioningtable.Ciscoflashpartitioningentry>`
        
        

        """

        _prefix = 'CISCO-FLASH-MIB'
        _revision = '2013-08-06'

        def __init__(self):
            super(CiscoFlashMib.Ciscoflashpartitioningtable, self).__init__()

            self.yang_name = "ciscoFlashPartitioningTable"
            self.yang_parent_name = "CISCO-FLASH-MIB"

            self.ciscoflashpartitioningentry = YList(self)

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
                        super(CiscoFlashMib.Ciscoflashpartitioningtable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoFlashMib.Ciscoflashpartitioningtable, self).__setattr__(name, value)


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
            
            .. attribute:: ciscoflashpartitioningserialnumber  <key>
            
            	Object which specifies a unique entry in the partitioning operations table. A management station wishing to initiate a partitioning operation should use a pseudo\-random value for this object when creating or modifying an instance of a ciscoFlashPartitioningEntry
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: ciscoflashpartitioningcommand
            
            	The partitioning command to be executed. Mandatory. If the command is unsupported, the partitioningInvalidOperation error will be reported in the operation status.  Command                 Remarks partition               Partition a Flash device.                         All the prerequisites for                         partitioning must be met for                         this command to succeed.  Command table           Parameters 1) partition            PartitioningDestinationName                         PartitioningPartitionCount                         PartitioningPartitionSizes (opt)                         PartitioningNotifyOnCompletion (opt)
            	**type**\:   :py:class:`Ciscoflashpartitioningcommand <ydk.models.cisco_ios_xe.CISCO_FLASH_MIB.CiscoFlashMib.Ciscoflashpartitioningtable.Ciscoflashpartitioningentry.Ciscoflashpartitioningcommand>`
            
            .. attribute:: ciscoflashpartitioningdestinationname
            
            	Destination device name. This name will be the value obtained from FlashDeviceName. If the name is not specified, the default Flash device will be assumed
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: ciscoflashpartitioningentrystatus
            
            	The status of this table entry
            	**type**\:   :py:class:`Rowstatus <ydk.models.cisco_ios_xe.SNMPv2_TC.Rowstatus>`
            
            .. attribute:: ciscoflashpartitioningnotifyoncompletion
            
            	Specifies whether or not a notification should be generated on the completion of the partitioning operation. If specified, ciscoFlashPartitioningCompletionTrap will be generated. It is the responsibility of the management entity to ensure that the SNMP administrative model is configured in such a way as to allow the notification to be delivered
            	**type**\:  bool
            
            .. attribute:: ciscoflashpartitioningpartitioncount
            
            	This object is used to specify the number of partitions to be created. Its value cannot exceed the value of ciscoFlashDeviceMaxPartitions.  To undo partitioning (revert to a single partition), this object must have the value 1
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            .. attribute:: ciscoflashpartitioningpartitionsizes
            
            	This object is used to explicitly specify the size of each partition to be created. The size of each partition will be in units of ciscoFlashDeviceMinPartitionSize. The value of this object will be in the form\:         <part1>\:<part2>...\:<partn>  If partition sizes are not specified, the system will calculate default sizes based on the partition count, the minimum partition size, and the device size. Partition size need not be specified when undoing partitioning (partition count is 1). If partition sizes are specified, the number of sizes specified must exactly match the partition count. If not, the partitioning command will be rejected with the invalidPartitionSizes error 
            	**type**\:  str
            
            .. attribute:: ciscoflashpartitioningstatus
            
            	The status of the specified partitioning operation. partitioningInProgress \:         specified operation is active  partitioningOperationSuccess \:         specified operation is supported and completed         successfully  partitioningInvalidOperation \:         command invalid or command\-protocol\-device         combination unsupported  partitioningInvalidDestName \:         invalid target name (file or partition or         device name) specified  partitioningInvalidPartitionCount \:         invalid partition count specified for the         partitioning command  partitioningInvalidPartitionSizes \:         invalid partition size, or invalid count of         partition sizes  partitioningDeviceBusy \:         specified device is in use and locked by         another process  partitioningDeviceOpenError \:         invalid device name  partitioningDeviceError \:         device read, write or erase error  partitioningNoMemory \:         system running low on memory  partitioningUnknownFailure \:         failure unknown
            	**type**\:   :py:class:`Ciscoflashpartitioningstatus <ydk.models.cisco_ios_xe.CISCO_FLASH_MIB.CiscoFlashMib.Ciscoflashpartitioningtable.Ciscoflashpartitioningentry.Ciscoflashpartitioningstatus>`
            
            .. attribute:: ciscoflashpartitioningtime
            
            	Time taken for the operation. This object will be like a stopwatch, starting when the operation starts, stopping when the operation completes. If a management entity keeps a database of completion times for various operations, it can then use the stopwatch capability to display percentage completion time
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'CISCO-FLASH-MIB'
            _revision = '2013-08-06'

            def __init__(self):
                super(CiscoFlashMib.Ciscoflashpartitioningtable.Ciscoflashpartitioningentry, self).__init__()

                self.yang_name = "ciscoFlashPartitioningEntry"
                self.yang_parent_name = "ciscoFlashPartitioningTable"

                self.ciscoflashpartitioningserialnumber = YLeaf(YType.int32, "ciscoFlashPartitioningSerialNumber")

                self.ciscoflashpartitioningcommand = YLeaf(YType.enumeration, "ciscoFlashPartitioningCommand")

                self.ciscoflashpartitioningdestinationname = YLeaf(YType.str, "ciscoFlashPartitioningDestinationName")

                self.ciscoflashpartitioningentrystatus = YLeaf(YType.enumeration, "ciscoFlashPartitioningEntryStatus")

                self.ciscoflashpartitioningnotifyoncompletion = YLeaf(YType.boolean, "ciscoFlashPartitioningNotifyOnCompletion")

                self.ciscoflashpartitioningpartitioncount = YLeaf(YType.uint32, "ciscoFlashPartitioningPartitionCount")

                self.ciscoflashpartitioningpartitionsizes = YLeaf(YType.str, "ciscoFlashPartitioningPartitionSizes")

                self.ciscoflashpartitioningstatus = YLeaf(YType.enumeration, "ciscoFlashPartitioningStatus")

                self.ciscoflashpartitioningtime = YLeaf(YType.uint32, "ciscoFlashPartitioningTime")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("ciscoflashpartitioningserialnumber",
                                "ciscoflashpartitioningcommand",
                                "ciscoflashpartitioningdestinationname",
                                "ciscoflashpartitioningentrystatus",
                                "ciscoflashpartitioningnotifyoncompletion",
                                "ciscoflashpartitioningpartitioncount",
                                "ciscoflashpartitioningpartitionsizes",
                                "ciscoflashpartitioningstatus",
                                "ciscoflashpartitioningtime") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoFlashMib.Ciscoflashpartitioningtable.Ciscoflashpartitioningentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoFlashMib.Ciscoflashpartitioningtable.Ciscoflashpartitioningentry, self).__setattr__(name, value)

            class Ciscoflashpartitioningcommand(Enum):
                """
                Ciscoflashpartitioningcommand

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
                Ciscoflashpartitioningstatus

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


            def has_data(self):
                return (
                    self.ciscoflashpartitioningserialnumber.is_set or
                    self.ciscoflashpartitioningcommand.is_set or
                    self.ciscoflashpartitioningdestinationname.is_set or
                    self.ciscoflashpartitioningentrystatus.is_set or
                    self.ciscoflashpartitioningnotifyoncompletion.is_set or
                    self.ciscoflashpartitioningpartitioncount.is_set or
                    self.ciscoflashpartitioningpartitionsizes.is_set or
                    self.ciscoflashpartitioningstatus.is_set or
                    self.ciscoflashpartitioningtime.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ciscoflashpartitioningserialnumber.yfilter != YFilter.not_set or
                    self.ciscoflashpartitioningcommand.yfilter != YFilter.not_set or
                    self.ciscoflashpartitioningdestinationname.yfilter != YFilter.not_set or
                    self.ciscoflashpartitioningentrystatus.yfilter != YFilter.not_set or
                    self.ciscoflashpartitioningnotifyoncompletion.yfilter != YFilter.not_set or
                    self.ciscoflashpartitioningpartitioncount.yfilter != YFilter.not_set or
                    self.ciscoflashpartitioningpartitionsizes.yfilter != YFilter.not_set or
                    self.ciscoflashpartitioningstatus.yfilter != YFilter.not_set or
                    self.ciscoflashpartitioningtime.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "ciscoFlashPartitioningEntry" + "[ciscoFlashPartitioningSerialNumber='" + self.ciscoflashpartitioningserialnumber.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-FLASH-MIB:CISCO-FLASH-MIB/ciscoFlashPartitioningTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ciscoflashpartitioningserialnumber.is_set or self.ciscoflashpartitioningserialnumber.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscoflashpartitioningserialnumber.get_name_leafdata())
                if (self.ciscoflashpartitioningcommand.is_set or self.ciscoflashpartitioningcommand.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscoflashpartitioningcommand.get_name_leafdata())
                if (self.ciscoflashpartitioningdestinationname.is_set or self.ciscoflashpartitioningdestinationname.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscoflashpartitioningdestinationname.get_name_leafdata())
                if (self.ciscoflashpartitioningentrystatus.is_set or self.ciscoflashpartitioningentrystatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscoflashpartitioningentrystatus.get_name_leafdata())
                if (self.ciscoflashpartitioningnotifyoncompletion.is_set or self.ciscoflashpartitioningnotifyoncompletion.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscoflashpartitioningnotifyoncompletion.get_name_leafdata())
                if (self.ciscoflashpartitioningpartitioncount.is_set or self.ciscoflashpartitioningpartitioncount.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscoflashpartitioningpartitioncount.get_name_leafdata())
                if (self.ciscoflashpartitioningpartitionsizes.is_set or self.ciscoflashpartitioningpartitionsizes.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscoflashpartitioningpartitionsizes.get_name_leafdata())
                if (self.ciscoflashpartitioningstatus.is_set or self.ciscoflashpartitioningstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscoflashpartitioningstatus.get_name_leafdata())
                if (self.ciscoflashpartitioningtime.is_set or self.ciscoflashpartitioningtime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscoflashpartitioningtime.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ciscoFlashPartitioningSerialNumber" or name == "ciscoFlashPartitioningCommand" or name == "ciscoFlashPartitioningDestinationName" or name == "ciscoFlashPartitioningEntryStatus" or name == "ciscoFlashPartitioningNotifyOnCompletion" or name == "ciscoFlashPartitioningPartitionCount" or name == "ciscoFlashPartitioningPartitionSizes" or name == "ciscoFlashPartitioningStatus" or name == "ciscoFlashPartitioningTime"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "ciscoFlashPartitioningSerialNumber"):
                    self.ciscoflashpartitioningserialnumber = value
                    self.ciscoflashpartitioningserialnumber.value_namespace = name_space
                    self.ciscoflashpartitioningserialnumber.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoFlashPartitioningCommand"):
                    self.ciscoflashpartitioningcommand = value
                    self.ciscoflashpartitioningcommand.value_namespace = name_space
                    self.ciscoflashpartitioningcommand.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoFlashPartitioningDestinationName"):
                    self.ciscoflashpartitioningdestinationname = value
                    self.ciscoflashpartitioningdestinationname.value_namespace = name_space
                    self.ciscoflashpartitioningdestinationname.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoFlashPartitioningEntryStatus"):
                    self.ciscoflashpartitioningentrystatus = value
                    self.ciscoflashpartitioningentrystatus.value_namespace = name_space
                    self.ciscoflashpartitioningentrystatus.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoFlashPartitioningNotifyOnCompletion"):
                    self.ciscoflashpartitioningnotifyoncompletion = value
                    self.ciscoflashpartitioningnotifyoncompletion.value_namespace = name_space
                    self.ciscoflashpartitioningnotifyoncompletion.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoFlashPartitioningPartitionCount"):
                    self.ciscoflashpartitioningpartitioncount = value
                    self.ciscoflashpartitioningpartitioncount.value_namespace = name_space
                    self.ciscoflashpartitioningpartitioncount.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoFlashPartitioningPartitionSizes"):
                    self.ciscoflashpartitioningpartitionsizes = value
                    self.ciscoflashpartitioningpartitionsizes.value_namespace = name_space
                    self.ciscoflashpartitioningpartitionsizes.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoFlashPartitioningStatus"):
                    self.ciscoflashpartitioningstatus = value
                    self.ciscoflashpartitioningstatus.value_namespace = name_space
                    self.ciscoflashpartitioningstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoFlashPartitioningTime"):
                    self.ciscoflashpartitioningtime = value
                    self.ciscoflashpartitioningtime.value_namespace = name_space
                    self.ciscoflashpartitioningtime.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.ciscoflashpartitioningentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.ciscoflashpartitioningentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "ciscoFlashPartitioningTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-FLASH-MIB:CISCO-FLASH-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "ciscoFlashPartitioningEntry"):
                for c in self.ciscoflashpartitioningentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoFlashMib.Ciscoflashpartitioningtable.Ciscoflashpartitioningentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.ciscoflashpartitioningentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "ciscoFlashPartitioningEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Ciscoflashmiscoptable(Entity):
        """
        A table of misc Flash operation entries. Each
        entry represents a Flash operation that
        has been initiated.
        
        .. attribute:: ciscoflashmiscopentry
        
        	A Flash operation entry. Each entry consists of a command, a target, and any optional parameters.  A management station wishing to create an entry should first generate a pseudo\-random serial number to be used as the index to this sparse table.  The station should then create the associated instance of the row status object. It must also, either in the same or in successive PDUs, create the associated instance of the command and parameter objects. It should also modify the default values for any of the parameter objects if the defaults are not appropriate.  Once the appropriate instances of all the command objects have been created, either by an explicit SNMP set request or by default, the row status should be set to active to initiate the operation. Note that this entire procedure may be initiated via a single set request which specifies a row status of createAndGo as well as specifies valid values for the non\-defaulted parameter objects.  Once an operation has been activated, it cannot be stopped.  Once the operation completes, the management station should retrieve the value of the status object (and time if desired), and delete the entry.  In order to prevent old entries from clogging the table, entries will be aged out, but an entry will never be deleted within 5 minutes of completing
        	**type**\: list of    :py:class:`Ciscoflashmiscopentry <ydk.models.cisco_ios_xe.CISCO_FLASH_MIB.CiscoFlashMib.Ciscoflashmiscoptable.Ciscoflashmiscopentry>`
        
        

        """

        _prefix = 'CISCO-FLASH-MIB'
        _revision = '2013-08-06'

        def __init__(self):
            super(CiscoFlashMib.Ciscoflashmiscoptable, self).__init__()

            self.yang_name = "ciscoFlashMiscOpTable"
            self.yang_parent_name = "CISCO-FLASH-MIB"

            self.ciscoflashmiscopentry = YList(self)

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
                        super(CiscoFlashMib.Ciscoflashmiscoptable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoFlashMib.Ciscoflashmiscoptable, self).__setattr__(name, value)


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
            
            .. attribute:: ciscoflashmiscopserialnumber  <key>
            
            	Object which specifies a unique entry in the table. A management station wishing to initiate a flash operation should use a pseudo\-random value for this object when creating or modifying an instance of a ciscoFlashMiscOpEntry
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: ciscoflashmiscopcommand
            
            	The command to be executed. Mandatory. Note that it is possible for a system to support multiple file systems (different file systems on different Flash devices, or different file systems on different partitions within a device). Each such file system may support only a subset of these commands. If a command is unsupported, the miscOpInvalidOperation(3) error will be reported in the operation status.  Command         Remarks erase           Erase flash. verify          Verify flash file checksum. delete          Delete a file. undelete        Revive a deleted file .                 Note that there are limits on                 the number of times a file can                 be deleted and undeleted. When                 this limit is exceeded, the                 system will return the appropriate                 error. squeeze         Recover space occupied by                 deleted files. This command                 preserves the good files, erases                 out the file system, then restores                 the preserved good files. format          Format a flash device.  Command table   Parameters erase           MiscOpDestinationName                 MiscOpNotifyOnCompletion (opt) verify          MiscOpDestinationName                 MiscOpNotifyOnCompletion (opt) delete          MiscOpDestinationName                 MiscOpNotifyOnCompletion (opt) undelete        MiscOpDestinationName                 MiscOpNotifyOnCompletion (opt) squeeze         MiscOpDestinationName                 MiscOpNotifyOnCompletion (opt) format          MiscOpDestinationName                 MiscOpNotifyOnCompletion (opt)
            	**type**\:   :py:class:`Ciscoflashmiscopcommand <ydk.models.cisco_ios_xe.CISCO_FLASH_MIB.CiscoFlashMib.Ciscoflashmiscoptable.Ciscoflashmiscopentry.Ciscoflashmiscopcommand>`
            
            .. attribute:: ciscoflashmiscopdestinationname
            
            	Destination file, or partition name. File name must be of the form         [device>\:][<partition>\:]<file> where <device> is a value obtained from FlashDeviceName,       <partition> is obtained from FlashPartitionName   and <file> is the name of a file in Flash. While leading and/or trailing whitespaces are acceptable, no whitespaces are allowed within the path itself.  A management station could derive its own partition name as per the description for the ciscoFlashPartitionName object. If <device> is not specified, the default Flash device will be assumed. If <partition> is not specified, the default partition will be assumed. If a device is not partitioned into 2 or more partitions, this value may be left out.  For an operation on a partition, eg., the erase command, this object would specify the partition name in the form\:         [device>\:][<partition>\:]
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: ciscoflashmiscopentrystatus
            
            	The status of this table entry
            	**type**\:   :py:class:`Rowstatus <ydk.models.cisco_ios_xe.SNMPv2_TC.Rowstatus>`
            
            .. attribute:: ciscoflashmiscopnotifyoncompletion
            
            	Specifies whether or not a notification should be generated on the completion of an operation. If specified, ciscoFlashMiscOpCompletionTrap will be generated. It is the responsibility of the management entity to ensure that the SNMP administrative model is configured in such a way as to allow the notification to be delivered
            	**type**\:  bool
            
            .. attribute:: ciscoflashmiscopstatus
            
            	The status of the specified operation. miscOpInProgress \:         specified operation is active  miscOpOperationSuccess \:         specified operation is supported and completed         successfully  miscOpInvalidOperation \:         command invalid or command\-protocol\-device         combination unsupported  miscOpInvalidDestName \:         invalid target name (file or partition or         device name) specified  miscOpDeviceBusy \:         specified device is in use and locked by another         process  miscOpDeviceOpenError \:         invalid device name  miscOpDeviceError \:         device read, write or erase error  miscOpDeviceNotProgrammable \:         device is read\-only but a write or erase         operation was specified  miscOpFileOpenError \:         invalid file name; file not found in partition  miscOpFileDeleteFailure \:         file could not be deleted; delete count exceeded  miscOpFileUndeleteFailure \:         file could not be undeleted; undelete count         exceeded  miscOpFileChecksumError \:         file has a bad checksum  miscOpNoMemory \:         system running low on memory  miscOpUnknownFailure \:         failure unknown  miscOpSqueezeFailure \:         the squeeze operation failed  miscOpNoSuchFile \:         a valid but nonexistent file name was specified  miscOpFormatFailure \:         the format operation failed
            	**type**\:   :py:class:`Ciscoflashmiscopstatus <ydk.models.cisco_ios_xe.CISCO_FLASH_MIB.CiscoFlashMib.Ciscoflashmiscoptable.Ciscoflashmiscopentry.Ciscoflashmiscopstatus>`
            
            .. attribute:: ciscoflashmiscoptime
            
            	Time taken for the operation. This object will be like a stopwatch, starting when the operation starts, stopping when the operation completes. If a management entity keeps a database of completion times for various operations, it can then use the stopwatch capability to display percentage completion time
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'CISCO-FLASH-MIB'
            _revision = '2013-08-06'

            def __init__(self):
                super(CiscoFlashMib.Ciscoflashmiscoptable.Ciscoflashmiscopentry, self).__init__()

                self.yang_name = "ciscoFlashMiscOpEntry"
                self.yang_parent_name = "ciscoFlashMiscOpTable"

                self.ciscoflashmiscopserialnumber = YLeaf(YType.int32, "ciscoFlashMiscOpSerialNumber")

                self.ciscoflashmiscopcommand = YLeaf(YType.enumeration, "ciscoFlashMiscOpCommand")

                self.ciscoflashmiscopdestinationname = YLeaf(YType.str, "ciscoFlashMiscOpDestinationName")

                self.ciscoflashmiscopentrystatus = YLeaf(YType.enumeration, "ciscoFlashMiscOpEntryStatus")

                self.ciscoflashmiscopnotifyoncompletion = YLeaf(YType.boolean, "ciscoFlashMiscOpNotifyOnCompletion")

                self.ciscoflashmiscopstatus = YLeaf(YType.enumeration, "ciscoFlashMiscOpStatus")

                self.ciscoflashmiscoptime = YLeaf(YType.uint32, "ciscoFlashMiscOpTime")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("ciscoflashmiscopserialnumber",
                                "ciscoflashmiscopcommand",
                                "ciscoflashmiscopdestinationname",
                                "ciscoflashmiscopentrystatus",
                                "ciscoflashmiscopnotifyoncompletion",
                                "ciscoflashmiscopstatus",
                                "ciscoflashmiscoptime") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoFlashMib.Ciscoflashmiscoptable.Ciscoflashmiscopentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoFlashMib.Ciscoflashmiscoptable.Ciscoflashmiscopentry, self).__setattr__(name, value)

            class Ciscoflashmiscopcommand(Enum):
                """
                Ciscoflashmiscopcommand

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
                Ciscoflashmiscopstatus

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


            def has_data(self):
                return (
                    self.ciscoflashmiscopserialnumber.is_set or
                    self.ciscoflashmiscopcommand.is_set or
                    self.ciscoflashmiscopdestinationname.is_set or
                    self.ciscoflashmiscopentrystatus.is_set or
                    self.ciscoflashmiscopnotifyoncompletion.is_set or
                    self.ciscoflashmiscopstatus.is_set or
                    self.ciscoflashmiscoptime.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ciscoflashmiscopserialnumber.yfilter != YFilter.not_set or
                    self.ciscoflashmiscopcommand.yfilter != YFilter.not_set or
                    self.ciscoflashmiscopdestinationname.yfilter != YFilter.not_set or
                    self.ciscoflashmiscopentrystatus.yfilter != YFilter.not_set or
                    self.ciscoflashmiscopnotifyoncompletion.yfilter != YFilter.not_set or
                    self.ciscoflashmiscopstatus.yfilter != YFilter.not_set or
                    self.ciscoflashmiscoptime.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "ciscoFlashMiscOpEntry" + "[ciscoFlashMiscOpSerialNumber='" + self.ciscoflashmiscopserialnumber.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-FLASH-MIB:CISCO-FLASH-MIB/ciscoFlashMiscOpTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ciscoflashmiscopserialnumber.is_set or self.ciscoflashmiscopserialnumber.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscoflashmiscopserialnumber.get_name_leafdata())
                if (self.ciscoflashmiscopcommand.is_set or self.ciscoflashmiscopcommand.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscoflashmiscopcommand.get_name_leafdata())
                if (self.ciscoflashmiscopdestinationname.is_set or self.ciscoflashmiscopdestinationname.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscoflashmiscopdestinationname.get_name_leafdata())
                if (self.ciscoflashmiscopentrystatus.is_set or self.ciscoflashmiscopentrystatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscoflashmiscopentrystatus.get_name_leafdata())
                if (self.ciscoflashmiscopnotifyoncompletion.is_set or self.ciscoflashmiscopnotifyoncompletion.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscoflashmiscopnotifyoncompletion.get_name_leafdata())
                if (self.ciscoflashmiscopstatus.is_set or self.ciscoflashmiscopstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscoflashmiscopstatus.get_name_leafdata())
                if (self.ciscoflashmiscoptime.is_set or self.ciscoflashmiscoptime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciscoflashmiscoptime.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ciscoFlashMiscOpSerialNumber" or name == "ciscoFlashMiscOpCommand" or name == "ciscoFlashMiscOpDestinationName" or name == "ciscoFlashMiscOpEntryStatus" or name == "ciscoFlashMiscOpNotifyOnCompletion" or name == "ciscoFlashMiscOpStatus" or name == "ciscoFlashMiscOpTime"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "ciscoFlashMiscOpSerialNumber"):
                    self.ciscoflashmiscopserialnumber = value
                    self.ciscoflashmiscopserialnumber.value_namespace = name_space
                    self.ciscoflashmiscopserialnumber.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoFlashMiscOpCommand"):
                    self.ciscoflashmiscopcommand = value
                    self.ciscoflashmiscopcommand.value_namespace = name_space
                    self.ciscoflashmiscopcommand.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoFlashMiscOpDestinationName"):
                    self.ciscoflashmiscopdestinationname = value
                    self.ciscoflashmiscopdestinationname.value_namespace = name_space
                    self.ciscoflashmiscopdestinationname.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoFlashMiscOpEntryStatus"):
                    self.ciscoflashmiscopentrystatus = value
                    self.ciscoflashmiscopentrystatus.value_namespace = name_space
                    self.ciscoflashmiscopentrystatus.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoFlashMiscOpNotifyOnCompletion"):
                    self.ciscoflashmiscopnotifyoncompletion = value
                    self.ciscoflashmiscopnotifyoncompletion.value_namespace = name_space
                    self.ciscoflashmiscopnotifyoncompletion.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoFlashMiscOpStatus"):
                    self.ciscoflashmiscopstatus = value
                    self.ciscoflashmiscopstatus.value_namespace = name_space
                    self.ciscoflashmiscopstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "ciscoFlashMiscOpTime"):
                    self.ciscoflashmiscoptime = value
                    self.ciscoflashmiscoptime.value_namespace = name_space
                    self.ciscoflashmiscoptime.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.ciscoflashmiscopentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.ciscoflashmiscopentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "ciscoFlashMiscOpTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-FLASH-MIB:CISCO-FLASH-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "ciscoFlashMiscOpEntry"):
                for c in self.ciscoflashmiscopentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoFlashMib.Ciscoflashmiscoptable.Ciscoflashmiscopentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.ciscoflashmiscopentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "ciscoFlashMiscOpEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            (self.ciscoflashcfg is not None and self.ciscoflashcfg.has_data()) or
            (self.ciscoflashchiptable is not None and self.ciscoflashchiptable.has_data()) or
            (self.ciscoflashcopytable is not None and self.ciscoflashcopytable.has_data()) or
            (self.ciscoflashdevice is not None and self.ciscoflashdevice.has_data()) or
            (self.ciscoflashdevicetable is not None and self.ciscoflashdevicetable.has_data()) or
            (self.ciscoflashfilebytypetable is not None and self.ciscoflashfilebytypetable.has_data()) or
            (self.ciscoflashfiletable is not None and self.ciscoflashfiletable.has_data()) or
            (self.ciscoflashmiscoptable is not None and self.ciscoflashmiscoptable.has_data()) or
            (self.ciscoflashpartitioningtable is not None and self.ciscoflashpartitioningtable.has_data()) or
            (self.ciscoflashpartitiontable is not None and self.ciscoflashpartitiontable.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.ciscoflashcfg is not None and self.ciscoflashcfg.has_operation()) or
            (self.ciscoflashchiptable is not None and self.ciscoflashchiptable.has_operation()) or
            (self.ciscoflashcopytable is not None and self.ciscoflashcopytable.has_operation()) or
            (self.ciscoflashdevice is not None and self.ciscoflashdevice.has_operation()) or
            (self.ciscoflashdevicetable is not None and self.ciscoflashdevicetable.has_operation()) or
            (self.ciscoflashfilebytypetable is not None and self.ciscoflashfilebytypetable.has_operation()) or
            (self.ciscoflashfiletable is not None and self.ciscoflashfiletable.has_operation()) or
            (self.ciscoflashmiscoptable is not None and self.ciscoflashmiscoptable.has_operation()) or
            (self.ciscoflashpartitioningtable is not None and self.ciscoflashpartitioningtable.has_operation()) or
            (self.ciscoflashpartitiontable is not None and self.ciscoflashpartitiontable.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "CISCO-FLASH-MIB:CISCO-FLASH-MIB" + path_buffer

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

        if (child_yang_name == "ciscoFlashCfg"):
            if (self.ciscoflashcfg is None):
                self.ciscoflashcfg = CiscoFlashMib.Ciscoflashcfg()
                self.ciscoflashcfg.parent = self
                self._children_name_map["ciscoflashcfg"] = "ciscoFlashCfg"
            return self.ciscoflashcfg

        if (child_yang_name == "ciscoFlashChipTable"):
            if (self.ciscoflashchiptable is None):
                self.ciscoflashchiptable = CiscoFlashMib.Ciscoflashchiptable()
                self.ciscoflashchiptable.parent = self
                self._children_name_map["ciscoflashchiptable"] = "ciscoFlashChipTable"
            return self.ciscoflashchiptable

        if (child_yang_name == "ciscoFlashCopyTable"):
            if (self.ciscoflashcopytable is None):
                self.ciscoflashcopytable = CiscoFlashMib.Ciscoflashcopytable()
                self.ciscoflashcopytable.parent = self
                self._children_name_map["ciscoflashcopytable"] = "ciscoFlashCopyTable"
            return self.ciscoflashcopytable

        if (child_yang_name == "ciscoFlashDevice"):
            if (self.ciscoflashdevice is None):
                self.ciscoflashdevice = CiscoFlashMib.Ciscoflashdevice()
                self.ciscoflashdevice.parent = self
                self._children_name_map["ciscoflashdevice"] = "ciscoFlashDevice"
            return self.ciscoflashdevice

        if (child_yang_name == "ciscoFlashDeviceTable"):
            if (self.ciscoflashdevicetable is None):
                self.ciscoflashdevicetable = CiscoFlashMib.Ciscoflashdevicetable()
                self.ciscoflashdevicetable.parent = self
                self._children_name_map["ciscoflashdevicetable"] = "ciscoFlashDeviceTable"
            return self.ciscoflashdevicetable

        if (child_yang_name == "ciscoFlashFileByTypeTable"):
            if (self.ciscoflashfilebytypetable is None):
                self.ciscoflashfilebytypetable = CiscoFlashMib.Ciscoflashfilebytypetable()
                self.ciscoflashfilebytypetable.parent = self
                self._children_name_map["ciscoflashfilebytypetable"] = "ciscoFlashFileByTypeTable"
            return self.ciscoflashfilebytypetable

        if (child_yang_name == "ciscoFlashFileTable"):
            if (self.ciscoflashfiletable is None):
                self.ciscoflashfiletable = CiscoFlashMib.Ciscoflashfiletable()
                self.ciscoflashfiletable.parent = self
                self._children_name_map["ciscoflashfiletable"] = "ciscoFlashFileTable"
            return self.ciscoflashfiletable

        if (child_yang_name == "ciscoFlashMiscOpTable"):
            if (self.ciscoflashmiscoptable is None):
                self.ciscoflashmiscoptable = CiscoFlashMib.Ciscoflashmiscoptable()
                self.ciscoflashmiscoptable.parent = self
                self._children_name_map["ciscoflashmiscoptable"] = "ciscoFlashMiscOpTable"
            return self.ciscoflashmiscoptable

        if (child_yang_name == "ciscoFlashPartitioningTable"):
            if (self.ciscoflashpartitioningtable is None):
                self.ciscoflashpartitioningtable = CiscoFlashMib.Ciscoflashpartitioningtable()
                self.ciscoflashpartitioningtable.parent = self
                self._children_name_map["ciscoflashpartitioningtable"] = "ciscoFlashPartitioningTable"
            return self.ciscoflashpartitioningtable

        if (child_yang_name == "ciscoFlashPartitionTable"):
            if (self.ciscoflashpartitiontable is None):
                self.ciscoflashpartitiontable = CiscoFlashMib.Ciscoflashpartitiontable()
                self.ciscoflashpartitiontable.parent = self
                self._children_name_map["ciscoflashpartitiontable"] = "ciscoFlashPartitionTable"
            return self.ciscoflashpartitiontable

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "ciscoFlashCfg" or name == "ciscoFlashChipTable" or name == "ciscoFlashCopyTable" or name == "ciscoFlashDevice" or name == "ciscoFlashDeviceTable" or name == "ciscoFlashFileByTypeTable" or name == "ciscoFlashFileTable" or name == "ciscoFlashMiscOpTable" or name == "ciscoFlashPartitioningTable" or name == "ciscoFlashPartitionTable"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = CiscoFlashMib()
        return self._top_entity

