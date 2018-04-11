""" Cisco_IOS_XE_device_hardware_oper 

This module contains a collection of YANG definitions
for Device Hardware operational data.
Copyright (c) 2017 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class AlarmSeverity(Enum):
    """
    AlarmSeverity (Enum Class)

    Alarm severity

    .. data:: alarm_severity_critical = 0

    	Critical Alarms

    .. data:: alarm_severity_major = 1

    	Major Alarms

    .. data:: alarm_severity_minor = 2

    	Minor Alarms

    """

    alarm_severity_critical = Enum.YLeaf(0, "alarm-severity-critical")

    alarm_severity_major = Enum.YLeaf(1, "alarm-severity-major")

    alarm_severity_minor = Enum.YLeaf(2, "alarm-severity-minor")


class HwType(Enum):
    """
    HwType (Enum Class)

    The broad type of hardware device

    .. data:: hw_type_unknown = 0

    	Unknown Hardware Type

    .. data:: hw_type_chassis = 1

    	Chassis

    .. data:: hw_type_cpu = 2

    	Central Processing Unit

    .. data:: hw_type_dram = 3

    	Dynamic Random Access Memory

    .. data:: hw_type_flash = 4

    	Flash

    .. data:: hw_type_emmc = 5

    	embedded Memory Controller

    .. data:: hw_type_sdcard = 6

    	SD-Card

    .. data:: hw_type_usb = 7

    	Universal Serial Bus

    .. data:: hw_type_pim = 8

    	Pluggable interface model

    .. data:: hw_type_transceiver = 9

    	Transceiver

    .. data:: hw_type_fantray = 10

    	Fan tray

    .. data:: hw_type_pem = 11

    	Power Entry Module

    """

    hw_type_unknown = Enum.YLeaf(0, "hw-type-unknown")

    hw_type_chassis = Enum.YLeaf(1, "hw-type-chassis")

    hw_type_cpu = Enum.YLeaf(2, "hw-type-cpu")

    hw_type_dram = Enum.YLeaf(3, "hw-type-dram")

    hw_type_flash = Enum.YLeaf(4, "hw-type-flash")

    hw_type_emmc = Enum.YLeaf(5, "hw-type-emmc")

    hw_type_sdcard = Enum.YLeaf(6, "hw-type-sdcard")

    hw_type_usb = Enum.YLeaf(7, "hw-type-usb")

    hw_type_pim = Enum.YLeaf(8, "hw-type-pim")

    hw_type_transceiver = Enum.YLeaf(9, "hw-type-transceiver")

    hw_type_fantray = Enum.YLeaf(10, "hw-type-fantray")

    hw_type_pem = Enum.YLeaf(11, "hw-type-pem")



class DeviceHardwareData(Entity):
    """
    Device Hardware
    
    .. attribute:: device_hardware
    
    	The device hardware model
    	**type**\:  :py:class:`DeviceHardware <ydk.models.cisco_ios_xe.Cisco_IOS_XE_device_hardware_oper.DeviceHardwareData.DeviceHardware>`
    
    	**presence node**\: True
    
    

    """

    _prefix = 'device-hardware-xe-oper'
    _revision = '2017-11-01'

    def __init__(self):
        super(DeviceHardwareData, self).__init__()
        self._top_entity = None

        self.yang_name = "device-hardware-data"
        self.yang_parent_name = "Cisco-IOS-XE-device-hardware-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([("device-hardware", ("device_hardware", DeviceHardwareData.DeviceHardware))])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.device_hardware = None
        self._children_name_map["device_hardware"] = "device-hardware"
        self._children_yang_names.add("device-hardware")
        self._segment_path = lambda: "Cisco-IOS-XE-device-hardware-oper:device-hardware-data"


    class DeviceHardware(Entity):
        """
        The device hardware model
        
        .. attribute:: device_inventory
        
        	All the inventory in the hardware
        	**type**\: list of  		 :py:class:`DeviceInventory <ydk.models.cisco_ios_xe.Cisco_IOS_XE_device_hardware_oper.DeviceHardwareData.DeviceHardware.DeviceInventory>`
        
        .. attribute:: device_alarm
        
        	The current alarms
        	**type**\: list of  		 :py:class:`DeviceAlarm <ydk.models.cisco_ios_xe.Cisco_IOS_XE_device_hardware_oper.DeviceHardwareData.DeviceHardware.DeviceAlarm>`
        
        .. attribute:: device_system_data
        
        	The current device system data
        	**type**\:  :py:class:`DeviceSystemData <ydk.models.cisco_ios_xe.Cisco_IOS_XE_device_hardware_oper.DeviceHardwareData.DeviceHardware.DeviceSystemData>`
        
        	**presence node**\: True
        
        

        This class is a :ref:`presence class<presence-class>`

        """

        _prefix = 'device-hardware-xe-oper'
        _revision = '2017-11-01'

        def __init__(self):
            super(DeviceHardwareData.DeviceHardware, self).__init__()

            self.yang_name = "device-hardware"
            self.yang_parent_name = "device-hardware-data"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([("device-system-data", ("device_system_data", DeviceHardwareData.DeviceHardware.DeviceSystemData))])
            self._child_list_classes = OrderedDict([("device-inventory", ("device_inventory", DeviceHardwareData.DeviceHardware.DeviceInventory)), ("device-alarm", ("device_alarm", DeviceHardwareData.DeviceHardware.DeviceAlarm))])
            self.is_presence_container = True
            self._leafs = OrderedDict()

            self.device_system_data = None
            self._children_name_map["device_system_data"] = "device-system-data"
            self._children_yang_names.add("device-system-data")

            self.device_inventory = YList(self)
            self.device_alarm = YList(self)
            self._segment_path = lambda: "device-hardware"
            self._absolute_path = lambda: "Cisco-IOS-XE-device-hardware-oper:device-hardware-data/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(DeviceHardwareData.DeviceHardware, [], name, value)


        class DeviceInventory(Entity):
            """
            All the inventory in the hardware
            
            .. attribute:: hw_type  (key)
            
            	Type of the hardware being represented
            	**type**\:  :py:class:`HwType <ydk.models.cisco_ios_xe.Cisco_IOS_XE_device_hardware_oper.HwType>`
            
            .. attribute:: hw_dev_index  (key)
            
            	The physical index of the inventory item
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: version
            
            	Version of this device
            	**type**\: str
            
            .. attribute:: part_number
            
            	The part number of this device. This  is only valid if the device is a field replaceable unit
            	**type**\: str
            
            .. attribute:: serial_number
            
            	The serial number of the device. This is only valid if the device is individually trackable
            	**type**\: str
            
            .. attribute:: hw_description
            
            	Description of the device
            	**type**\: str
            
            

            """

            _prefix = 'device-hardware-xe-oper'
            _revision = '2017-11-01'

            def __init__(self):
                super(DeviceHardwareData.DeviceHardware.DeviceInventory, self).__init__()

                self.yang_name = "device-inventory"
                self.yang_parent_name = "device-hardware"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['hw_type','hw_dev_index']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('hw_type', YLeaf(YType.enumeration, 'hw-type')),
                    ('hw_dev_index', YLeaf(YType.uint32, 'hw-dev-index')),
                    ('version', YLeaf(YType.str, 'version')),
                    ('part_number', YLeaf(YType.str, 'part-number')),
                    ('serial_number', YLeaf(YType.str, 'serial-number')),
                    ('hw_description', YLeaf(YType.str, 'hw-description')),
                ])
                self.hw_type = None
                self.hw_dev_index = None
                self.version = None
                self.part_number = None
                self.serial_number = None
                self.hw_description = None
                self._segment_path = lambda: "device-inventory" + "[hw-type='" + str(self.hw_type) + "']" + "[hw-dev-index='" + str(self.hw_dev_index) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XE-device-hardware-oper:device-hardware-data/device-hardware/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(DeviceHardwareData.DeviceHardware.DeviceInventory, ['hw_type', 'hw_dev_index', 'version', 'part_number', 'serial_number', 'hw_description'], name, value)


        class DeviceAlarm(Entity):
            """
            The current alarms
            
            .. attribute:: alarm_id  (key)
            
            	The Alarm Identifier
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: alarm_instance  (key)
            
            	The instance of this alarm. This corresponds to the  entity index
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: alarm_name
            
            	The name of the alarm
            	**type**\: str
            
            .. attribute:: alarm_category
            
            	The catagory (or severity) of the alarm that is being asserted
            	**type**\:  :py:class:`AlarmSeverity <ydk.models.cisco_ios_xe.Cisco_IOS_XE_device_hardware_oper.AlarmSeverity>`
            
            .. attribute:: alarm_time
            
            	Time the alarm was raised
            	**type**\: str
            
            	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
            
            .. attribute:: alarm_description
            
            	Description of the alarm
            	**type**\: str
            
            

            """

            _prefix = 'device-hardware-xe-oper'
            _revision = '2017-11-01'

            def __init__(self):
                super(DeviceHardwareData.DeviceHardware.DeviceAlarm, self).__init__()

                self.yang_name = "device-alarm"
                self.yang_parent_name = "device-hardware"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['alarm_id','alarm_instance']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('alarm_id', YLeaf(YType.uint32, 'alarm-id')),
                    ('alarm_instance', YLeaf(YType.uint32, 'alarm-instance')),
                    ('alarm_name', YLeaf(YType.str, 'alarm-name')),
                    ('alarm_category', YLeaf(YType.enumeration, 'alarm-category')),
                    ('alarm_time', YLeaf(YType.str, 'alarm-time')),
                    ('alarm_description', YLeaf(YType.str, 'alarm-description')),
                ])
                self.alarm_id = None
                self.alarm_instance = None
                self.alarm_name = None
                self.alarm_category = None
                self.alarm_time = None
                self.alarm_description = None
                self._segment_path = lambda: "device-alarm" + "[alarm-id='" + str(self.alarm_id) + "']" + "[alarm-instance='" + str(self.alarm_instance) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XE-device-hardware-oper:device-hardware-data/device-hardware/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(DeviceHardwareData.DeviceHardware.DeviceAlarm, ['alarm_id', 'alarm_instance', 'alarm_name', 'alarm_category', 'alarm_time', 'alarm_description'], name, value)


        class DeviceSystemData(Entity):
            """
            The current device system data
            
            .. attribute:: current_time
            
            	Current time on device in UTC
            	**type**\: str
            
            	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
            
            .. attribute:: boot_time
            
            	This timestamp indicates the time that the system was last restarted.  The value is the timestamp in seconds relative to the Unix Epoch (Jan 1, 1970 00\:00\:00 UTC)
            	**type**\: str
            
            	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
            
            .. attribute:: software_version
            
            	Software version
            	**type**\: str
            
            .. attribute:: rommon_version
            
            	Rommon version
            	**type**\: str
            
            .. attribute:: last_reboot_reason
            
            	Last reboot reason
            	**type**\: str
            
            

            This class is a :ref:`presence class<presence-class>`

            """

            _prefix = 'device-hardware-xe-oper'
            _revision = '2017-11-01'

            def __init__(self):
                super(DeviceHardwareData.DeviceHardware.DeviceSystemData, self).__init__()

                self.yang_name = "device-system-data"
                self.yang_parent_name = "device-hardware"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self.is_presence_container = True
                self._leafs = OrderedDict([
                    ('current_time', YLeaf(YType.str, 'current-time')),
                    ('boot_time', YLeaf(YType.str, 'boot-time')),
                    ('software_version', YLeaf(YType.str, 'software-version')),
                    ('rommon_version', YLeaf(YType.str, 'rommon-version')),
                    ('last_reboot_reason', YLeaf(YType.str, 'last-reboot-reason')),
                ])
                self.current_time = None
                self.boot_time = None
                self.software_version = None
                self.rommon_version = None
                self.last_reboot_reason = None
                self._segment_path = lambda: "device-system-data"
                self._absolute_path = lambda: "Cisco-IOS-XE-device-hardware-oper:device-hardware-data/device-hardware/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(DeviceHardwareData.DeviceHardware.DeviceSystemData, ['current_time', 'boot_time', 'software_version', 'rommon_version', 'last_reboot_reason'], name, value)

    def clone_ptr(self):
        self._top_entity = DeviceHardwareData()
        return self._top_entity

