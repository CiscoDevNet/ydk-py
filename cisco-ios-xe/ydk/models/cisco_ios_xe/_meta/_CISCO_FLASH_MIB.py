


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'FlashfiletypeEnum' : _MetaInfoEnum('FlashfiletypeEnum', 'ydk.models.cisco_ios_xe.CISCO_FLASH_MIB',
        {
            'unknown':'unknown',
            'config':'config',
            'image':'image',
            'directory':'directory',
            'crashinfo':'crashinfo',
        }, 'CISCO-FLASH-MIB', _yang_ns._namespaces['CISCO-FLASH-MIB']),
    'CiscoFlashMib.Ciscoflashdevice' : {
        'meta_info' : _MetaInfoClass('CiscoFlashMib.Ciscoflashdevice',
            False, 
            [
            _MetaInfoClassMember('ciscoFlashDevicesSupported', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Flash devices supported by the system.
                If the system does not support any Flash devices, this
                MIB will not be loaded on that system. The value of this
                object will therefore be atleast 1.
                ''',
                'ciscoflashdevicessupported',
                'CISCO-FLASH-MIB', False),
            ],
            'CISCO-FLASH-MIB',
            'ciscoFlashDevice',
            _yang_ns._namespaces['CISCO-FLASH-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_FLASH_MIB'
        ),
    },
    'CiscoFlashMib.Ciscoflashcfg' : {
        'meta_info' : _MetaInfoClass('CiscoFlashMib.Ciscoflashcfg',
            False, 
            [
            _MetaInfoClassMember('ciscoFlashCfgDevInsNotifEnable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Specifies whether or not a notification should be
                generated on the insertion of a Flash device.
                
                If the value of this object is 'true' then the
                ciscoFlashDeviceInsertedNotif notification
                will be generated.
                
                If the value of this object is 'false' then the
                ciscoFlashDeviceInsertedNotif notification
                will not be generated.
                
                It is the responsibility of the management entity to
                ensure that the SNMP administrative model is
                configured in such a way as to allow the
                notification to be delivered.
                ''',
                'ciscoflashcfgdevinsnotifenable',
                'CISCO-FLASH-MIB', False),
            _MetaInfoClassMember('ciscoFlashCfgDevRemNotifEnable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Specifies whether or not a notification should be
                generated on the removal of a Flash device.
                
                If the value of this object is 'true' then the
                ciscoFlashDeviceRemovedNotif notification
                will be generated.
                
                If the value of this object is 'false' then the
                ciscoFlashDeviceRemovedNotif notification
                will not be generated.
                
                It is the responsibility of the management entity to
                ensure that the SNMP administrative model is
                configured in such a way as to allow the
                notification to be delivered.
                ''',
                'ciscoflashcfgdevremnotifenable',
                'CISCO-FLASH-MIB', False),
            _MetaInfoClassMember('ciscoFlashPartitionLowSpaceNotifEnable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This object specifies whether or not a notification should be
                generated when the free space falls below the threshold value on
                a flash partition and on recovery from low space.
                
                If the value of this object is 'true' then
                ciscoFlashPartitionLowSpaceNotif and
                ciscoFlashPartitionLowSpaceRecoveryNotif notifications will be
                generated.
                
                If the value of this object is 'false' then the
                ciscoFlashPartitionLowSpaceNotif  and
                ciscoFlashPartitionLowSpaceRecoveryNotif notifications
                will not be generated.
                
                It is the responsibility of the management entity to
                ensure that the SNMP administrative model is
                configured in such a way as to allow the
                notifications to be delivered.
                ''',
                'ciscoflashpartitionlowspacenotifenable',
                'CISCO-FLASH-MIB', False),
            ],
            'CISCO-FLASH-MIB',
            'ciscoFlashCfg',
            _yang_ns._namespaces['CISCO-FLASH-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_FLASH_MIB'
        ),
    },
    'CiscoFlashMib.Ciscoflashdevicetable.Ciscoflashdeviceentry.CiscoflashdeviceprogrammingjumperEnum' : _MetaInfoEnum('CiscoflashdeviceprogrammingjumperEnum', 'ydk.models.cisco_ios_xe.CISCO_FLASH_MIB',
        {
            'installed':'installed',
            'notInstalled':'notInstalled',
            'unknown':'unknown',
        }, 'CISCO-FLASH-MIB', _yang_ns._namespaces['CISCO-FLASH-MIB']),
    'CiscoFlashMib.Ciscoflashdevicetable.Ciscoflashdeviceentry' : {
        'meta_info' : _MetaInfoClass('CiscoFlashMib.Ciscoflashdevicetable.Ciscoflashdeviceentry',
            False, 
            [
            _MetaInfoClassMember('ciscoFlashDeviceIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                Flash device sequence number to index within the
                table of initialized flash devices.
                The lowest value should be 1. The highest should be
                less than or equal to the value of the
                ciscoFlashDevicesSupported object.
                ''',
                'ciscoflashdeviceindex',
                'CISCO-FLASH-MIB', True),
            _MetaInfoClassMember('ciscoFlashDeviceCard', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-1](\\.[1-3]?[0-9]))|(2\\.(0|([1-9]\\d*))))(\\.(0|([1-9]\\d*)))*'], 
                '''                This object will point to an instance of a card entry
                in the cardTable. The card entry will give details about
                the card on which the Flash device is actually located.
                For most systems, this is usually the main processor board.
                On the AGS+ systems, Flash is located on a separate multibus
                card such as the MC.
                This object will therefore be used to essentially index
                into cardTable to retrieve details about the card such as
                cardDescr, cardSlotNumber, etc.
                ''',
                'ciscoflashdevicecard',
                'CISCO-FLASH-MIB', False),
            _MetaInfoClassMember('ciscoFlashDeviceChipCount', ATTRIBUTE, 'int' , None, None, 
                [('0', '64')], [], 
                '''                Total number of chips within the Flash device.
                The purpose of this object is to provide information
                upfront to a management station on how much chip info
                to expect and possibly help double check the chip index
                against an upper limit when randomly retrieving chip
                info for a partition.
                ''',
                'ciscoflashdevicechipcount',
                'CISCO-FLASH-MIB', False),
            _MetaInfoClassMember('ciscoFlashDeviceController', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                Flash device controller. The h/w card that actually
                controls Flash read/write/erase. Relevant for the AGS+
                systems where Flash may be controlled by the MC+, STR or
                the ENVM cards, cards that may not actually contain the
                Flash chips.
                For systems that have removable PCMCIA flash cards that
                are controlled by a PCMCIA controller chip, this object
                may contain a description of that controller chip.
                Where irrelevant (Flash is a direct memory mapped device
                accessed directly by the main processor), this object will
                have an empty (NULL) string.
                ''',
                'ciscoflashdevicecontroller',
                'CISCO-FLASH-MIB', False),
            _MetaInfoClassMember('ciscoFlashDeviceDescr', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                Description of a Flash device. The description is meant
                to explain what the Flash device and its purpose is.
                Current values are:
                  System flash - for the primary Flash used to store full
                                 system images.
                  Boot flash   - for the secondary Flash used to store
                                 bootstrap images.
                The ciscoFlashDeviceDescr, ciscoFlashDeviceController
                (if applicable), and ciscoFlashPhyEntIndex objects are
                expected to collectively give all information about a
                Flash device.
                The device description will always be available for a
                removable device, even when the device has been removed.
                ''',
                'ciscoflashdevicedescr',
                'CISCO-FLASH-MIB', False),
            _MetaInfoClassMember('ciscoFlashDeviceInitTime', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                System time at which device was initialized.
                For fixed devices, this will be the system time at
                boot up.
                For removable devices, it will be the time at which
                the device was inserted, which may be boot up time,
                or a later time (if device was inserted later).
                If a device (fixed or removable) was repartitioned,
                it will be the time of repartitioning.
                The purpose of this object is to help a management
                station determine if a removable device has been
                changed. The application should retrieve this
                object prior to any operation and compare with
                the previously retrieved value.
                Note that this time will not be real time but a
                running time maintained by the system. This running
                time starts from zero when the system boots up.
                For a removable device that has been removed, this
                value will be zero.
                ''',
                'ciscoflashdeviceinittime',
                'CISCO-FLASH-MIB', False),
            _MetaInfoClassMember('ciscoFlashDeviceMaxPartitions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Max number of partitions supported by the system for
                this Flash device. Default will be 1, which actually
                means that partitioning is not supported. Note that
                this value will be defined by system limitations, not
                by the flash device itself (for eg., the system may
                impose a limit of 2 partitions even though the device
                may be large enough to be partitioned into 4 based on
                the smallest partition unit supported).
                On systems that execute code out of Flash, partitioning
                is a way of creating multiple file systems in the Flash
                device so that writing into or erasing of one file system
                can be done while executing code residing in another file
                system.
                For systems executing code out of DRAM, partitioning
                gives a way of sub-dividing a large Flash device for
                easier management of files.
                ''',
                'ciscoflashdevicemaxpartitions',
                'CISCO-FLASH-MIB', False),
            _MetaInfoClassMember('ciscoFlashDeviceMinPartitionSize', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object will give the minimum partition size
                supported for this device. For systems that execute code
                directly out of Flash, the minimum partition size needs
                to be the bank size. (Bank size is equal to the size of a
                chip multiplied by the width of the device. In most cases,
                the device width is 4 bytes, and so the bank size would be
                four times the size of a chip). This has to be so because
                all programming commands affect the operation of an
                entire chip (in our case, an entire bank because all
                operations are done on the entire width of the device)
                even though the actual command may be localized to a small
                portion of each chip. So when executing code out of Flash,
                one needs to be able to write and erase some portion of
                Flash without affecting the code execution.
                For systems that execute code out of DRAM or ROM, it is
                possible to partition Flash with a finer granularity (for
                eg., at erase sector boundaries) if the system code supports
                such granularity.
                
                This object will let a management entity know the
                minimum partition size as defined by the system.
                If the system does not support partitioning, the value
                will be equal to the device size in ciscoFlashDeviceSize.
                The maximum number of partitions that could be configured
                will be equal to the minimum of
                ciscoFlashDeviceMaxPartitions
                and
                (ciscoFlashDeviceSize / ciscoFlashDeviceMinPartitionSize).
                
                If the total size of the flash device is greater than the
                maximum value reportable by this object then this object should
                report its maximum value(4,294,967,295) and
                ciscoFlashDeviceMinPartitionSizeExtended must be used to report
                the flash device's minimum partition size.
                ''',
                'ciscoflashdeviceminpartitionsize',
                'CISCO-FLASH-MIB', False),
            _MetaInfoClassMember('ciscoFlashDeviceMinPartitionSizeExtended', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                This object provides the minimum partition size supported for
                this device. This object is a 64-bit version of 
                ciscoFlashDeviceMinPatitionSize.
                ''',
                'ciscoflashdeviceminpartitionsizeextended',
                'CISCO-FLASH-MIB', False),
            _MetaInfoClassMember('ciscoFlashDeviceName', ATTRIBUTE, 'str' , None, None, 
                [(0, 16)], [], 
                '''                Flash device name. This name is used to refer to the
                device within the system. Flash operations get directed
                to a device based on this name.
                The system has a concept of a default device.
                This would be the primary or most used device in case of
                multiple devices. The system directs an operation to the
                default device whenever a device name is not specified.
                The device name is therefore mandatory except when the
                operation is being done on the default device, or,
                the system supports only a single Flash device.
                The device name will always be available for a
                removable device, even when the device has been removed.
                ''',
                'ciscoflashdevicename',
                'CISCO-FLASH-MIB', False),
            _MetaInfoClassMember('ciscoFlashDeviceNameExtended', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                Extended Flash device name whose size can be upto
                255 characters. This name is used to refer to the
                device within the system. Flash operations get directed
                to a device based on this name.
                The system has a concept of a default device.
                This would be the primary or most used device in case
                of multiple devices. The system directs an operation
                to the default device whenever a device name is not
                specified. The device name is therefore mandatory
                except when the operation is being done on the
                default device, or, the system supports only a single
                Flash device. The device name will always be available
                for a removable device, even when the device has been
                removed.
                ''',
                'ciscoflashdevicenameextended',
                'CISCO-FLASH-MIB', False),
            _MetaInfoClassMember('ciscoFlashDevicePartitions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Flash device partitions actually present. Number of
                partitions cannot exceed the minimum of
                ciscoFlashDeviceMaxPartitions
                and
                (ciscoFlashDeviceSize / ciscoFlashDeviceMinPartitionSize).
                Will be equal to at least 1, the case where the partition
                spans the entire device (actually no partitioning).
                A partition will contain one or more minimum partition
                units (where a minimum partition unit is defined by
                ciscoFlashDeviceMinPartitionSize).
                ''',
                'ciscoflashdevicepartitions',
                'CISCO-FLASH-MIB', False),
            _MetaInfoClassMember('ciscoFlashDeviceProgrammingJumper', REFERENCE_ENUM_CLASS, 'CiscoflashdeviceprogrammingjumperEnum' , 'ydk.models.cisco_ios_xe.CISCO_FLASH_MIB', 'CiscoFlashMib.Ciscoflashdevicetable.Ciscoflashdeviceentry.CiscoflashdeviceprogrammingjumperEnum', 
                [], [], 
                '''                This object gives the state of a jumper (if present and can be
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
                ''',
                'ciscoflashdeviceprogrammingjumper',
                'CISCO-FLASH-MIB', False),
            _MetaInfoClassMember('ciscoFlashDeviceRemovable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Whether Flash device is removable. Generally, only PCMCIA
                Flash cards will be treated as removable. Socketed Flash
                chips and Flash SIMM modules will not be treated as removable.
                Simply put, only those Flash devices that can be inserted
                or removed without opening the hardware casing will be
                considered removable.
                Further, removable Flash devices are expected to have
                the necessary hardware support -
                  1. on-line removal and insertion
                  2. interrupt generation on removal or insertion.
                ''',
                'ciscoflashdeviceremovable',
                'CISCO-FLASH-MIB', False),
            _MetaInfoClassMember('ciscoFlashDeviceSize', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total size of the Flash device.
                For a removable device, the size will be zero if
                the device has been removed.
                
                If the total size of the flash device is greater than the
                maximum value reportable by this object then this object
                should report its maximum value(4,294,967,295) and
                ciscoFlashDeviceSizeExtended must be used to report the
                flash device's size.
                ''',
                'ciscoflashdevicesize',
                'CISCO-FLASH-MIB', False),
            _MetaInfoClassMember('ciscoFlashDeviceSizeExtended', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Total size of the Flash device.
                For a removable device, the size will be zero if
                the device has been removed.
                
                This object is a 64-bit version of ciscoFlashDeviceSize.
                ''',
                'ciscoflashdevicesizeextended',
                'CISCO-FLASH-MIB', False),
            _MetaInfoClassMember('ciscoFlashPhyEntIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                This object indicates the physical entity index of a
                physical entity in entPhysicalTable which the flash
                device actually located.
                ''',
                'ciscoflashphyentindex',
                'CISCO-FLASH-MIB', False),
            ],
            'CISCO-FLASH-MIB',
            'ciscoFlashDeviceEntry',
            _yang_ns._namespaces['CISCO-FLASH-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_FLASH_MIB'
        ),
    },
    'CiscoFlashMib.Ciscoflashdevicetable' : {
        'meta_info' : _MetaInfoClass('CiscoFlashMib.Ciscoflashdevicetable',
            False, 
            [
            _MetaInfoClassMember('ciscoFlashDeviceEntry', REFERENCE_LIST, 'Ciscoflashdeviceentry' , 'ydk.models.cisco_ios_xe.CISCO_FLASH_MIB', 'CiscoFlashMib.Ciscoflashdevicetable.Ciscoflashdeviceentry', 
                [], [], 
                '''                An entry in the table of flash device properties for
                each initialized flash device.
                Each entry can be randomly accessed by using
                ciscoFlashDeviceIndex as an index into the table.
                Note that removable devices will have an entry in
                the table even when they have been removed. However,
                a non-removable device that has not been installed
                will not have an entry in the table.
                ''',
                'ciscoflashdeviceentry',
                'CISCO-FLASH-MIB', False),
            ],
            'CISCO-FLASH-MIB',
            'ciscoFlashDeviceTable',
            _yang_ns._namespaces['CISCO-FLASH-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_FLASH_MIB'
        ),
    },
    'CiscoFlashMib.Ciscoflashchiptable.Ciscoflashchipentry' : {
        'meta_info' : _MetaInfoClass('CiscoFlashMib.Ciscoflashchiptable.Ciscoflashchipentry',
            False, 
            [
            _MetaInfoClassMember('ciscoFlashDeviceIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                ''',
                'ciscoflashdeviceindex',
                'CISCO-FLASH-MIB', True),
            _MetaInfoClassMember('ciscoFlashChipIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '64')], [], 
                '''                Chip sequence number within selected flash device.
                Used to index within chip info table.
                Value starts from 1 and should not be greater than
                ciscoFlashDeviceChipCount for that device.
                When retrieving chip information for chips within a
                partition, the sequence number should lie between
                ciscoFlashPartitionStartChip & ciscoFlashPartitionEndChip
                (both inclusive).
                ''',
                'ciscoflashchipindex',
                'CISCO-FLASH-MIB', True),
            _MetaInfoClassMember('ciscoFlashChipCode', ATTRIBUTE, 'str' , None, None, 
                [(0, 5)], [], 
                '''                Manufacturer and device code for a chip.
                Lower byte will contain the device code.
                Upper byte will contain the manufacturer code.
                If a chip code is unknown because it could not
                be queried out of the chip, the value of this
                object will be 00:00.
                Since programming algorithms differ from chip type to
                chip type, this chip code should be used to determine
                which algorithms to use (and thereby whether the chip
                is supported in the first place).
                ''',
                'ciscoflashchipcode',
                'CISCO-FLASH-MIB', False),
            _MetaInfoClassMember('ciscoFlashChipDescr', ATTRIBUTE, 'str' , None, None, 
                [(0, 32)], [], 
                '''                Flash chip name corresponding to the chip code.
                The name will contain the manufacturer and the
                chip type. It will be of the form :
                  Intel 27F008SA.
                In the case where a chip code is unknown, this
                object will be an empty (NULL) string.
                In the case where the chip code is known but the
                chip is not supported by the system, this object
                will be an empty (NULL) string.
                A management station is therefore expected to use the
                chip code and the chip description in conjunction
                to provide additional information whenever the
                ciscoFlashPartitionStatus object has the readOnly(1)
                value.
                ''',
                'ciscoflashchipdescr',
                'CISCO-FLASH-MIB', False),
            _MetaInfoClassMember('ciscoFlashChipEraseRetries', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object will provide a cumulative count
                (since last system boot up or initialization) of
                the number of erase retries that were done in the chip.
                Typically, a maximum of 2000 retries are done in a
                single erase zone (which may be a full chip or a
                portion, depending on the chip technology) before
                flagging an erase error.
                A management station is expected to get this object
                for each chip in a partition after an erase failure
                in that partition. To keep a track of retries for
                a given erase operation, the management station would
                have to retrieve the values for the concerned chips
                before and after any erase operation.
                Note that erase may be done through an independent
                command, or through a copy-to-flash command.
                ''',
                'ciscoflashchiperaseretries',
                'CISCO-FLASH-MIB', False),
            _MetaInfoClassMember('ciscoFlashChipMaxEraseRetries', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The maximum number of erase retries done within
                an erase sector before declaring an erase failure.
                ''',
                'ciscoflashchipmaxeraseretries',
                'CISCO-FLASH-MIB', False),
            _MetaInfoClassMember('ciscoFlashChipMaxWriteRetries', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The maximum number of write retries done at any
                single location before declaring a write failure.
                ''',
                'ciscoflashchipmaxwriteretries',
                'CISCO-FLASH-MIB', False),
            _MetaInfoClassMember('ciscoFlashChipWriteRetries', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object will provide a cumulative count
                (since last system boot up or initialization) of
                the number of write retries that were done in the chip.
                If no writes have been done to Flash, the count
                will be zero. Typically, a maximum of 25 retries are
                done on a single location before flagging a write
                error.
                A management station is expected to get this object
                for each chip in a partition after a write failure
                in that partition. To keep a track of retries for
                a given write operation, the management station would
                have to retrieve the values for the concerned chips
                before and after any write operation.
                ''',
                'ciscoflashchipwriteretries',
                'CISCO-FLASH-MIB', False),
            ],
            'CISCO-FLASH-MIB',
            'ciscoFlashChipEntry',
            _yang_ns._namespaces['CISCO-FLASH-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_FLASH_MIB'
        ),
    },
    'CiscoFlashMib.Ciscoflashchiptable' : {
        'meta_info' : _MetaInfoClass('CiscoFlashMib.Ciscoflashchiptable',
            False, 
            [
            _MetaInfoClassMember('ciscoFlashChipEntry', REFERENCE_LIST, 'Ciscoflashchipentry' , 'ydk.models.cisco_ios_xe.CISCO_FLASH_MIB', 'CiscoFlashMib.Ciscoflashchiptable.Ciscoflashchipentry', 
                [], [], 
                '''                An entry in the table of chip info for each
                flash device initialized in the system.
                An entry is indexed by two objects - the
                device index and the chip index within that
                device.
                ''',
                'ciscoflashchipentry',
                'CISCO-FLASH-MIB', False),
            ],
            'CISCO-FLASH-MIB',
            'ciscoFlashChipTable',
            _yang_ns._namespaces['CISCO-FLASH-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_FLASH_MIB'
        ),
    },
    'CiscoFlashMib.Ciscoflashpartitiontable.Ciscoflashpartitionentry.CiscoflashpartitionchecksumalgorithmEnum' : _MetaInfoEnum('CiscoflashpartitionchecksumalgorithmEnum', 'ydk.models.cisco_ios_xe.CISCO_FLASH_MIB',
        {
            'simpleChecksum':'simpleChecksum',
            'undefined':'undefined',
            'simpleCRC':'simpleCRC',
        }, 'CISCO-FLASH-MIB', _yang_ns._namespaces['CISCO-FLASH-MIB']),
    'CiscoFlashMib.Ciscoflashpartitiontable.Ciscoflashpartitionentry.CiscoflashpartitionstatusEnum' : _MetaInfoEnum('CiscoflashpartitionstatusEnum', 'ydk.models.cisco_ios_xe.CISCO_FLASH_MIB',
        {
            'readOnly':'readOnly',
            'runFromFlash':'runFromFlash',
            'readWrite':'readWrite',
        }, 'CISCO-FLASH-MIB', _yang_ns._namespaces['CISCO-FLASH-MIB']),
    'CiscoFlashMib.Ciscoflashpartitiontable.Ciscoflashpartitionentry.CiscoflashpartitionupgrademethodEnum' : _MetaInfoEnum('CiscoflashpartitionupgrademethodEnum', 'ydk.models.cisco_ios_xe.CISCO_FLASH_MIB',
        {
            'unknown':'unknown',
            'rxbootFLH':'rxbootFLH',
            'direct':'direct',
        }, 'CISCO-FLASH-MIB', _yang_ns._namespaces['CISCO-FLASH-MIB']),
    'CiscoFlashMib.Ciscoflashpartitiontable.Ciscoflashpartitionentry' : {
        'meta_info' : _MetaInfoClass('CiscoFlashMib.Ciscoflashpartitiontable.Ciscoflashpartitionentry',
            False, 
            [
            _MetaInfoClassMember('ciscoFlashDeviceIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                ''',
                'ciscoflashdeviceindex',
                'CISCO-FLASH-MIB', True),
            _MetaInfoClassMember('ciscoFlashPartitionIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                Flash partition sequence number used to index within
                table of initialized flash partitions.
                ''',
                'ciscoflashpartitionindex',
                'CISCO-FLASH-MIB', True),
            _MetaInfoClassMember('ciscoFlashPartitionChecksumAlgorithm', REFERENCE_ENUM_CLASS, 'CiscoflashpartitionchecksumalgorithmEnum' , 'ydk.models.cisco_ios_xe.CISCO_FLASH_MIB', 'CiscoFlashMib.Ciscoflashpartitiontable.Ciscoflashpartitionentry.CiscoflashpartitionchecksumalgorithmEnum', 
                [], [], 
                '''                Checksum algorithm identifier for checksum method
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
                ''',
                'ciscoflashpartitionchecksumalgorithm',
                'CISCO-FLASH-MIB', False),
            _MetaInfoClassMember('ciscoFlashPartitionEndChip', ATTRIBUTE, 'int' , None, None, 
                [('1', '64')], [], 
                '''                Chip sequence number of last chip in partition.
                Used as an index into the chip table.
                ''',
                'ciscoflashpartitionendchip',
                'CISCO-FLASH-MIB', False),
            _MetaInfoClassMember('ciscoFlashPartitionFileCount', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Count of all files in a flash partition. Both
                good and bad (deleted or invalid checksum) files
                will be included in this count.
                ''',
                'ciscoflashpartitionfilecount',
                'CISCO-FLASH-MIB', False),
            _MetaInfoClassMember('ciscoFlashPartitionFileNameLength', ATTRIBUTE, 'int' , None, None, 
                [('1', '256')], [], 
                '''                Maximum file name length supported by the file
                system.
                Max file name length will depend on the file
                system implemented. Today, all file systems
                support a max length of at least 48 bytes.
                A management entity must use this object when
                prompting a user for, or deriving the Flash file
                name length.
                ''',
                'ciscoflashpartitionfilenamelength',
                'CISCO-FLASH-MIB', False),
            _MetaInfoClassMember('ciscoFlashPartitionFreeSpace', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Free space within a Flash partition.
                Note that the actual size of a file in Flash includes
                a small overhead that represents the file system's
                file header.
                Certain file systems may also have a partition or
                device header overhead to be considered when
                computing the free space.
                Free space will be computed as total partition size
                less size of all existing files (valid/invalid/deleted
                files and including file header of each file),
                less size of any partition header, less size of
                header of next file to be copied in. In short, this
                object will give the size of the largest file that
                can be copied in. The management entity will not be
                expected to know or use any overheads such as file
                and partition header lengths, since such overheads
                may vary from file system to file system.
                Deleted files in Flash do not free up space.
                A partition may have to be erased in order to reclaim
                the space occupied by files.
                
                If the free space within a flash partition is greater than
                the maximum value reportable by this object then this object
                should report its maximum value(4,294,967,295) and
                ciscoFlashPartitionFreeSpaceExtended
                must be used to report the flash partition's free space.
                ''',
                'ciscoflashpartitionfreespace',
                'CISCO-FLASH-MIB', False),
            _MetaInfoClassMember('ciscoFlashPartitionFreeSpaceExtended', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Free space within a Flash partition.
                Note that the actual size of a file in Flash includes
                a small overhead that represents the file system's
                file header.
                Certain file systems may also have a partition or
                device header overhead to be considered when
                computing the free space.
                Free space will be computed as total partition size
                less size of all existing files (valid/invalid/deleted
                files and including file header of each file),
                less size of any partition header, less size of
                header of next file to be copied in. In short, this
                object will give the size of the largest file that
                can be copied in. The management entity will not be
                expected to know or use any overheads such as file
                and partition header lengths, since such overheads
                may vary from file system to file system.
                Deleted files in Flash do not free up space.
                A partition may have to be erased in order to reclaim
                the space occupied by files.
                
                This object is a 64-bit version of ciscoFlashPartitionFreeSpace
                ''',
                'ciscoflashpartitionfreespaceextended',
                'CISCO-FLASH-MIB', False),
            _MetaInfoClassMember('ciscoFlashPartitionLowSpaceNotifThreshold', ATTRIBUTE, 'int' , None, None, 
                [('0', '100')], [], 
                '''                This object specifies the minimum threshold value in percentage
                of free space for each partition. If the free space available
                goes below this threshold value and if
                ciscoFlashPartionLowSpaceNotifEnable is set to true,
                ciscoFlashPartitionLowSpaceNotif will be generated. When the
                available free space comes back to the threshold value
                ciscoFlashPartionLowSpaceRecoveryNotif will be generated.
                ''',
                'ciscoflashpartitionlowspacenotifthreshold',
                'CISCO-FLASH-MIB', False),
            _MetaInfoClassMember('ciscoFlashPartitionName', ATTRIBUTE, 'str' , None, None, 
                [(0, 16)], [], 
                '''                Flash partition name used to refer to a partition
                by the system. This can be any alpha-numeric character
                string of the form AAAAAAAAnn, where A represents an
                optional alpha character and n a numeric character.
                Any numeric characters must always form the trailing
                part of the string. The system will strip off the alpha
                characters and use the numeric portion to map to a
                partition index.
                Flash operations get directed to a device partition
                based on this name.
                The system has a concept of a default partition. This
                would be the first partition in the device. The system
                directs an operation to the default partition whenever
                a partition name is not specified.
                The partition name is therefore mandatory except when
                the operation is being done on the default partition, or
                the device has just one partition (is not partitioned).
                ''',
                'ciscoflashpartitionname',
                'CISCO-FLASH-MIB', False),
            _MetaInfoClassMember('ciscoFlashPartitionNeedErasure', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This object indicates whether a partition requires
                erasure before any write operations can be done in it.
                A management station should therefore retrieve this
                object prior to attempting any write operation.
                A partition requires erasure after it becomes full
                free space left is less than or equal to the
                (filesystem file header size).
                A partition also requires erasure if the system does
                not find the existence of any file system when it
                boots up.
                The partition may be erased explicitly through the
                erase(5) command, or by using the copyToFlashWithErase(1)
                command.
                If a copyToFlashWithoutErase(2) command is issued
                when this object has the TRUE value, the command
                will fail.
                ''',
                'ciscoflashpartitionneederasure',
                'CISCO-FLASH-MIB', False),
            _MetaInfoClassMember('ciscoFlashPartitionSize', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                Flash partition size. It should be an integral
                multiple of ciscoFlashDeviceMinPartitionSize.
                If there is a single partition, this size will be equal
                to ciscoFlashDeviceSize.
                
                If the size of the flash partition is greater than the
                maximum value reportable by this object then this object
                should report its maximum value(4,294,967,295) and
                ciscoFlashPartitionSizeExtended must be used to report the
                flash partition's size.
                ''',
                'ciscoflashpartitionsize',
                'CISCO-FLASH-MIB', False),
            _MetaInfoClassMember('ciscoFlashPartitionSizeExtended', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Flash partition size. It should be an integral
                multiple of ciscoFlashDeviceMinPartitionSize.
                If there is a single partition, this size will be equal
                to ciscoFlashDeviceSize.
                
                This object is a 64-bit version of ciscoFlashPartitionSize
                ''',
                'ciscoflashpartitionsizeextended',
                'CISCO-FLASH-MIB', False),
            _MetaInfoClassMember('ciscoFlashPartitionStartChip', ATTRIBUTE, 'int' , None, None, 
                [('1', '64')], [], 
                '''                Chip sequence number of first chip in partition.
                Used as an index into the chip table.
                ''',
                'ciscoflashpartitionstartchip',
                'CISCO-FLASH-MIB', False),
            _MetaInfoClassMember('ciscoFlashPartitionStatus', REFERENCE_ENUM_CLASS, 'CiscoflashpartitionstatusEnum' , 'ydk.models.cisco_ios_xe.CISCO_FLASH_MIB', 'CiscoFlashMib.Ciscoflashpartitiontable.Ciscoflashpartitionentry.CiscoflashpartitionstatusEnum', 
                [], [], 
                '''                Flash partition status can be :
                
                * readOnly if device is not programmable either because
                chips could not be recognized or an erroneous mismatch
                of chips was detected. Chip recognition may fail either
                because the chips are not supported by the system,
                or because the Vpp voltage required to identify chips
                has been disabled via the programming jumper.
                The ciscoFlashDeviceProgrammingJumper, ciscoFlashChipCode,
                and ciscoFlashChipDescr objects can be examined to get
                more details on the cause of this status
                * runFromFlash (RFF) if current image is running from
                this partition.
                The ciscoFlashPartitionUpgradeMethod object will then
                indicate whether the Flash Load Helper can be used
                to write a file to this partition or not.
                
                * readWrite if partition is programmable.
                ''',
                'ciscoflashpartitionstatus',
                'CISCO-FLASH-MIB', False),
            _MetaInfoClassMember('ciscoFlashPartitionUpgradeMethod', REFERENCE_ENUM_CLASS, 'CiscoflashpartitionupgrademethodEnum' , 'ydk.models.cisco_ios_xe.CISCO_FLASH_MIB', 'CiscoFlashMib.Ciscoflashpartitiontable.Ciscoflashpartitionentry.CiscoflashpartitionupgrademethodEnum', 
                [], [], 
                '''                Flash partition upgrade method, ie., method by which
                new files can be downloaded into the partition.
                FLH stands for Flash Load Helper, a feature provided
                on run-from-Flash systems for upgrading Flash. This
                feature uses the bootstrap code in ROMs to help in
                automatic download.
                This object should be retrieved if the partition
                status is runFromFlash(2).
                If the partition status is readOnly(1), the upgrade
                method would depend on the reason for the readOnly
                status. For eg., it may simply be a matter of installing
                the programming jumper, or it may require execution of a
                later version of software that supports the Flash chips.
                
                unknown      -  the current system image does not know
                                how Flash can be programmed. A possible
                                method would be to reload the ROM image
                                and perform the upgrade manually.
                rxbootFLH    -  the Flash Load Helper is available to
                                download files to Flash. A copy-to-flash
                                command can be used and this system image
                                will automatically reload the Rxboot image
                                in ROM and direct it to carry out the
                                download request.
                direct       -  will be done directly by this image.
                ''',
                'ciscoflashpartitionupgrademethod',
                'CISCO-FLASH-MIB', False),
            ],
            'CISCO-FLASH-MIB',
            'ciscoFlashPartitionEntry',
            _yang_ns._namespaces['CISCO-FLASH-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_FLASH_MIB'
        ),
    },
    'CiscoFlashMib.Ciscoflashpartitiontable' : {
        'meta_info' : _MetaInfoClass('CiscoFlashMib.Ciscoflashpartitiontable',
            False, 
            [
            _MetaInfoClassMember('ciscoFlashPartitionEntry', REFERENCE_LIST, 'Ciscoflashpartitionentry' , 'ydk.models.cisco_ios_xe.CISCO_FLASH_MIB', 'CiscoFlashMib.Ciscoflashpartitiontable.Ciscoflashpartitionentry', 
                [], [], 
                '''                An entry in the table of flash partition properties
                for each initialized flash partition. Each entry
                will be indexed by a device number and a partition
                number within the device.
                ''',
                'ciscoflashpartitionentry',
                'CISCO-FLASH-MIB', False),
            ],
            'CISCO-FLASH-MIB',
            'ciscoFlashPartitionTable',
            _yang_ns._namespaces['CISCO-FLASH-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_FLASH_MIB'
        ),
    },
    'CiscoFlashMib.Ciscoflashfiletable.Ciscoflashfileentry.CiscoflashfilestatusEnum' : _MetaInfoEnum('CiscoflashfilestatusEnum', 'ydk.models.cisco_ios_xe.CISCO_FLASH_MIB',
        {
            'deleted':'deleted',
            'invalidChecksum':'invalidChecksum',
            'valid':'valid',
        }, 'CISCO-FLASH-MIB', _yang_ns._namespaces['CISCO-FLASH-MIB']),
    'CiscoFlashMib.Ciscoflashfiletable.Ciscoflashfileentry' : {
        'meta_info' : _MetaInfoClass('CiscoFlashMib.Ciscoflashfiletable.Ciscoflashfileentry',
            False, 
            [
            _MetaInfoClassMember('ciscoFlashDeviceIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                ''',
                'ciscoflashdeviceindex',
                'CISCO-FLASH-MIB', True),
            _MetaInfoClassMember('ciscoFlashPartitionIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                ''',
                'ciscoflashpartitionindex',
                'CISCO-FLASH-MIB', True),
            _MetaInfoClassMember('ciscoFlashFileIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                Flash file sequence number used to index within
                a Flash partition directory table.
                ''',
                'ciscoflashfileindex',
                'CISCO-FLASH-MIB', True),
            _MetaInfoClassMember('ciscoFlashFileChecksum', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                File checksum stored in the file header. This
                checksum is computed and stored when the file is
                written into Flash. It serves to validate the data
                written into Flash.
                Whereas the system will generate and store the checksum
                internally in hexadecimal form, this object will
                provide the checksum in a string form.
                The checksum will be available for all valid and
                invalid-checksum files.
                ''',
                'ciscoflashfilechecksum',
                'CISCO-FLASH-MIB', False),
            _MetaInfoClassMember('ciscoFlashFileDate', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The time at which this file was created.
                ''',
                'ciscoflashfiledate',
                'CISCO-FLASH-MIB', False),
            _MetaInfoClassMember('ciscoFlashFileName', ATTRIBUTE, 'str' , None, None, 
                [(1, 255)], [], 
                '''                Flash file name as specified by the user copying in
                the file. The name should not include the colon (:)
                character as it is a special separator character used
                to delineate the device name, partition name, and the
                file name.
                ''',
                'ciscoflashfilename',
                'CISCO-FLASH-MIB', False),
            _MetaInfoClassMember('ciscoFlashFileSize', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Size of the file in bytes. Note that this size does
                not include the size of the filesystem file header.
                File size will always be non-zero.
                ''',
                'ciscoflashfilesize',
                'CISCO-FLASH-MIB', False),
            _MetaInfoClassMember('ciscoFlashFileStatus', REFERENCE_ENUM_CLASS, 'CiscoflashfilestatusEnum' , 'ydk.models.cisco_ios_xe.CISCO_FLASH_MIB', 'CiscoFlashMib.Ciscoflashfiletable.Ciscoflashfileentry.CiscoflashfilestatusEnum', 
                [], [], 
                '''                Status of a file.
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
                ''',
                'ciscoflashfilestatus',
                'CISCO-FLASH-MIB', False),
            _MetaInfoClassMember('ciscoFlashFileType', REFERENCE_ENUM_CLASS, 'FlashfiletypeEnum' , 'ydk.models.cisco_ios_xe.CISCO_FLASH_MIB', 'FlashfiletypeEnum', 
                [], [], 
                '''                Type of the file.
                ''',
                'ciscoflashfiletype',
                'CISCO-FLASH-MIB', False),
            ],
            'CISCO-FLASH-MIB',
            'ciscoFlashFileEntry',
            _yang_ns._namespaces['CISCO-FLASH-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_FLASH_MIB'
        ),
    },
    'CiscoFlashMib.Ciscoflashfiletable' : {
        'meta_info' : _MetaInfoClass('CiscoFlashMib.Ciscoflashfiletable',
            False, 
            [
            _MetaInfoClassMember('ciscoFlashFileEntry', REFERENCE_LIST, 'Ciscoflashfileentry' , 'ydk.models.cisco_ios_xe.CISCO_FLASH_MIB', 'CiscoFlashMib.Ciscoflashfiletable.Ciscoflashfileentry', 
                [], [], 
                '''                An entry in the table of Flash file properties
                for each initialized Flash partition. Each entry
                represents a file and gives details about the file.
                An entry is indexed using the device number,
                partition number within the device, and file
                number within the partition.
                ''',
                'ciscoflashfileentry',
                'CISCO-FLASH-MIB', False),
            ],
            'CISCO-FLASH-MIB',
            'ciscoFlashFileTable',
            _yang_ns._namespaces['CISCO-FLASH-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_FLASH_MIB'
        ),
    },
    'CiscoFlashMib.Ciscoflashfilebytypetable.Ciscoflashfilebytypeentry.CiscoflashfilebytypestatusEnum' : _MetaInfoEnum('CiscoflashfilebytypestatusEnum', 'ydk.models.cisco_ios_xe.CISCO_FLASH_MIB',
        {
            'deleted':'deleted',
            'invalidChecksum':'invalidChecksum',
            'valid':'valid',
        }, 'CISCO-FLASH-MIB', _yang_ns._namespaces['CISCO-FLASH-MIB']),
    'CiscoFlashMib.Ciscoflashfilebytypetable.Ciscoflashfilebytypeentry' : {
        'meta_info' : _MetaInfoClass('CiscoFlashMib.Ciscoflashfilebytypetable.Ciscoflashfilebytypeentry',
            False, 
            [
            _MetaInfoClassMember('ciscoFlashFileType', REFERENCE_ENUM_CLASS, 'FlashfiletypeEnum' , 'ydk.models.cisco_ios_xe.CISCO_FLASH_MIB', 'FlashfiletypeEnum', 
                [], [], 
                '''                ''',
                'ciscoflashfiletype',
                'CISCO-FLASH-MIB', True),
            _MetaInfoClassMember('ciscoFlashDeviceIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                ''',
                'ciscoflashdeviceindex',
                'CISCO-FLASH-MIB', True),
            _MetaInfoClassMember('ciscoFlashPartitionIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                ''',
                'ciscoflashpartitionindex',
                'CISCO-FLASH-MIB', True),
            _MetaInfoClassMember('ciscoFlashFileIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                ''',
                'ciscoflashfileindex',
                'CISCO-FLASH-MIB', True),
            _MetaInfoClassMember('ciscoFlashFileByTypeChecksum', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                This object represents exactly the
                same info as ciscoFlashFileChecksum
                object in ciscoFlashFileTable.
                ''',
                'ciscoflashfilebytypechecksum',
                'CISCO-FLASH-MIB', False),
            _MetaInfoClassMember('ciscoFlashFileByTypeDate', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                This object represents exactly the
                same info as ciscoFlashFileDate
                object in ciscoFlashFileTable.
                ''',
                'ciscoflashfilebytypedate',
                'CISCO-FLASH-MIB', False),
            _MetaInfoClassMember('ciscoFlashFileByTypeName', ATTRIBUTE, 'str' , None, None, 
                [(1, 255)], [], 
                '''                This object represents exactly the
                same info as ciscoFlashFileName
                object in ciscoFlashFileTable.
                ''',
                'ciscoflashfilebytypename',
                'CISCO-FLASH-MIB', False),
            _MetaInfoClassMember('ciscoFlashFileByTypeSize', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object represents exactly the
                same info as ciscoFlashFileSize
                object in ciscoFlashFileTable.
                ''',
                'ciscoflashfilebytypesize',
                'CISCO-FLASH-MIB', False),
            _MetaInfoClassMember('ciscoFlashFileByTypeStatus', REFERENCE_ENUM_CLASS, 'CiscoflashfilebytypestatusEnum' , 'ydk.models.cisco_ios_xe.CISCO_FLASH_MIB', 'CiscoFlashMib.Ciscoflashfilebytypetable.Ciscoflashfilebytypeentry.CiscoflashfilebytypestatusEnum', 
                [], [], 
                '''                This object represents exactly the
                same info as ciscoFlashFileStatus
                object in ciscoFlashFileTable.
                ''',
                'ciscoflashfilebytypestatus',
                'CISCO-FLASH-MIB', False),
            ],
            'CISCO-FLASH-MIB',
            'ciscoFlashFileByTypeEntry',
            _yang_ns._namespaces['CISCO-FLASH-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_FLASH_MIB'
        ),
    },
    'CiscoFlashMib.Ciscoflashfilebytypetable' : {
        'meta_info' : _MetaInfoClass('CiscoFlashMib.Ciscoflashfilebytypetable',
            False, 
            [
            _MetaInfoClassMember('ciscoFlashFileByTypeEntry', REFERENCE_LIST, 'Ciscoflashfilebytypeentry' , 'ydk.models.cisco_ios_xe.CISCO_FLASH_MIB', 'CiscoFlashMib.Ciscoflashfilebytypetable.Ciscoflashfilebytypeentry', 
                [], [], 
                '''                An entry in the table of Flash file properties
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
                ''',
                'ciscoflashfilebytypeentry',
                'CISCO-FLASH-MIB', False),
            ],
            'CISCO-FLASH-MIB',
            'ciscoFlashFileByTypeTable',
            _yang_ns._namespaces['CISCO-FLASH-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_FLASH_MIB'
        ),
    },
    'CiscoFlashMib.Ciscoflashcopytable.Ciscoflashcopyentry.CiscoflashcopycommandEnum' : _MetaInfoEnum('CiscoflashcopycommandEnum', 'ydk.models.cisco_ios_xe.CISCO_FLASH_MIB',
        {
            'copyToFlashWithErase':'copyToFlashWithErase',
            'copyToFlashWithoutErase':'copyToFlashWithoutErase',
            'copyFromFlash':'copyFromFlash',
            'copyFromFlhLog':'copyFromFlhLog',
        }, 'CISCO-FLASH-MIB', _yang_ns._namespaces['CISCO-FLASH-MIB']),
    'CiscoFlashMib.Ciscoflashcopytable.Ciscoflashcopyentry.CiscoflashcopyprotocolEnum' : _MetaInfoEnum('CiscoflashcopyprotocolEnum', 'ydk.models.cisco_ios_xe.CISCO_FLASH_MIB',
        {
            'tftp':'tftp',
            'rcp':'rcp',
            'lex':'lex',
            'ftp':'ftp',
            'scp':'scp',
            'sftp':'sftp',
        }, 'CISCO-FLASH-MIB', _yang_ns._namespaces['CISCO-FLASH-MIB']),
    'CiscoFlashMib.Ciscoflashcopytable.Ciscoflashcopyentry.CiscoflashcopystatusEnum' : _MetaInfoEnum('CiscoflashcopystatusEnum', 'ydk.models.cisco_ios_xe.CISCO_FLASH_MIB',
        {
            'copyOperationPending':'copyOperationPending',
            'copyInProgress':'copyInProgress',
            'copyOperationSuccess':'copyOperationSuccess',
            'copyInvalidOperation':'copyInvalidOperation',
            'copyInvalidProtocol':'copyInvalidProtocol',
            'copyInvalidSourceName':'copyInvalidSourceName',
            'copyInvalidDestName':'copyInvalidDestName',
            'copyInvalidServerAddress':'copyInvalidServerAddress',
            'copyDeviceBusy':'copyDeviceBusy',
            'copyDeviceOpenError':'copyDeviceOpenError',
            'copyDeviceError':'copyDeviceError',
            'copyDeviceNotProgrammable':'copyDeviceNotProgrammable',
            'copyDeviceFull':'copyDeviceFull',
            'copyFileOpenError':'copyFileOpenError',
            'copyFileTransferError':'copyFileTransferError',
            'copyFileChecksumError':'copyFileChecksumError',
            'copyNoMemory':'copyNoMemory',
            'copyUnknownFailure':'copyUnknownFailure',
            'copyInvalidSignature':'copyInvalidSignature',
            'copyProhibited':'copyProhibited',
        }, 'CISCO-FLASH-MIB', _yang_ns._namespaces['CISCO-FLASH-MIB']),
    'CiscoFlashMib.Ciscoflashcopytable.Ciscoflashcopyentry' : {
        'meta_info' : _MetaInfoClass('CiscoFlashMib.Ciscoflashcopytable.Ciscoflashcopyentry',
            False, 
            [
            _MetaInfoClassMember('ciscoFlashCopySerialNumber', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                Object which specifies a unique entry in the
                table. A management station wishing to initiate a
                copy operation should use a pseudo-random value for
                this object when creating or modifying an instance of
                a ciscoFlashCopyEntry.
                ''',
                'ciscoflashcopyserialnumber',
                'CISCO-FLASH-MIB', True),
            _MetaInfoClassMember('ciscoFlashCopyCommand', REFERENCE_ENUM_CLASS, 'CiscoflashcopycommandEnum' , 'ydk.models.cisco_ios_xe.CISCO_FLASH_MIB', 'CiscoFlashMib.Ciscoflashcopytable.Ciscoflashcopyentry.CiscoflashcopycommandEnum', 
                [], [], 
                '''                The copy command to be executed. Mandatory.
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
                ''',
                'ciscoflashcopycommand',
                'CISCO-FLASH-MIB', False),
            _MetaInfoClassMember('ciscoFlashCopyDestinationName', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                Destination file name.
                
                For a copy to Flash:
                File name must be of the form
                        {device>:][<partition>:]<file>
                where <device> is a value obtained from FlashDeviceName,
                      <partition> is obtained from FlashPartitionName
                  and <file> is any character string that does not have
                embedded colon characters.
                A management station could derive its own partition name
                as per the description for the ciscoFlashPartitionName
                object.
                If <device> is not specified, the default Flash device
                will be assumed.
                If <partition> is not specified, the default partition
                will be assumed. If a device is not partitioned into 2
                or more partitions, this value may be left out.
                If <file> is not specified, it will default to <file>
                specified in ciscoFlashCopySourceName.
                
                For a copy from Flash via tftp or rcp, the file name will be
                as per the file naming conventions and destination sub-directory
                on the server. If not specified, <file> from the source
                file name will be used.
                For a copy from Flash via lex, this string will consist
                of numeric characters specifying the interface on the
                lex box that will receive the source flash image.
                ''',
                'ciscoflashcopydestinationname',
                'CISCO-FLASH-MIB', False),
            _MetaInfoClassMember('ciscoFlashCopyEntryStatus', REFERENCE_ENUM_CLASS, 'RowstatusEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowstatusEnum', 
                [], [], 
                '''                The status of this table entry.
                ''',
                'ciscoflashcopyentrystatus',
                'CISCO-FLASH-MIB', False),
            _MetaInfoClassMember('ciscoFlashCopyNotifyOnCompletion', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Specifies whether or not a notification should be
                generated on the completion of the copy operation.
                If specified, ciscoFlashCopyCompletionTrap
                will be generated. It is the responsibility of the
                management entity to ensure that the SNMP administrative
                model is configured in such a way as to allow the
                notification to be delivered.
                ''',
                'ciscoflashcopynotifyoncompletion',
                'CISCO-FLASH-MIB', False),
            _MetaInfoClassMember('ciscoFlashCopyProtocol', REFERENCE_ENUM_CLASS, 'CiscoflashcopyprotocolEnum' , 'ydk.models.cisco_ios_xe.CISCO_FLASH_MIB', 'CiscoFlashMib.Ciscoflashcopytable.Ciscoflashcopyentry.CiscoflashcopyprotocolEnum', 
                [], [], 
                '''                The protocol to be used for any copy. Optional.
                Will default to tftp if not specified.
                
                Since feature support depends on a software release,
                version number within the release, platform, and
                maybe the image type (subset type), a management
                station would be expected to somehow determine
                the protocol support for a command.
                ''',
                'ciscoflashcopyprotocol',
                'CISCO-FLASH-MIB', False),
            _MetaInfoClassMember('ciscoFlashCopyRemotePassword', ATTRIBUTE, 'str' , None, None, 
                [(1, 40)], [], 
                '''                Password used by ftp, sftp or scp for copying a file
                to/from an ftp/sftp/scp server. This object must be
                created when the ciscoFlashCopyProtocol is ftp, sftp or
                scp. Reading it returns a zero-length string for
                security reasons.
                ''',
                'ciscoflashcopyremotepassword',
                'CISCO-FLASH-MIB', False),
            _MetaInfoClassMember('ciscoFlashCopyRemoteUserName', ATTRIBUTE, 'str' , None, None, 
                [(1, 255)], [], 
                '''                Remote user name for copy via rcp protocol. Optional.
                This object will be ignored for protocols other than
                rcp.
                If specified, it will override the remote user-name
                configured through the
                        rcmd remote-username
                configuration command.
                The remote user-name is sent as the server user-name
                in an rcp command request sent by the system to a
                remote rcp server.
                ''',
                'ciscoflashcopyremoteusername',
                'CISCO-FLASH-MIB', False),
            _MetaInfoClassMember('ciscoFlashCopyServerAddress', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The server address to be used for any copy. Optional.
                Will default to 'FFFFFFFF'H  (or 255.255.255.255).
                
                Since this object can just hold only IPv4 Transport
                type, it is deprecated and replaced by
                ciscoFlashCopyServerAddrRev1.
                ''',
                'ciscoflashcopyserveraddress',
                'CISCO-FLASH-MIB', False),
            _MetaInfoClassMember('ciscoFlashCopyServerAddrRev1', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                The server address to be used for any copy. Optional.
                Will default to 'FFFFFFFF'H  (or 255.255.255.255).
                
                The Format of this address depends on the value of the
                ciscoFlashCopyServerAddrType.
                
                This object deprecates the old
                ciscoFlashCopyServerAddress object.
                ''',
                'ciscoflashcopyserveraddrrev1',
                'CISCO-FLASH-MIB', False),
            _MetaInfoClassMember('ciscoFlashCopyServerAddrType', REFERENCE_ENUM_CLASS, 'InetaddresstypeEnum' , 'ydk.models.cisco_ios_xe.INET_ADDRESS_MIB', 'InetaddresstypeEnum', 
                [], [], 
                '''                This object indicates the transport type of the
                address contained in
                ciscoFlashCopyServerAddrRev1. Optional.
                Will default to '1' (IPv4 address type).
                ''',
                'ciscoflashcopyserveraddrtype',
                'CISCO-FLASH-MIB', False),
            _MetaInfoClassMember('ciscoFlashCopySourceName', ATTRIBUTE, 'str' , None, None, 
                [(1, 255)], [], 
                '''                Source file name, either in Flash or on a server,
                depending on the type of copy command. Mandatory.
                
                For a copy from Flash:
                File name must be of the form
                        [device>:][:]
                where  is a value obtained from FlashDeviceName,
                         is obtained from FlashPartitionName
                    and  is the name of a file in Flash.
                A management station could derive its own partition name
                as per the description for the ciscoFlashPartitionName
                object.
                If <device> is not specified, the default Flash device
                will be assumed.
                If <partition> is not specified, the default partition
                will be assumed. If a device is not partitioned into 2
                or more partitions, this value may be left out.
                
                For a copy to Flash, the file name will be as per
                the file naming conventions and path to the file on
                the server.
                ''',
                'ciscoflashcopysourcename',
                'CISCO-FLASH-MIB', False),
            _MetaInfoClassMember('ciscoFlashCopyStatus', REFERENCE_ENUM_CLASS, 'CiscoflashcopystatusEnum' , 'ydk.models.cisco_ios_xe.CISCO_FLASH_MIB', 'CiscoFlashMib.Ciscoflashcopytable.Ciscoflashcopyentry.CiscoflashcopystatusEnum', 
                [], [], 
                '''                The status of the specified copy operation.
                
                copyOperationPending :
                        operation request is received and
                        pending for validation and process
                
                copyInProgress :
                        specified operation is active
                
                copyOperationSuccess :
                        specified operation is supported and
                        completed successfully
                
                copyInvalidOperation :
                        command invalid or command-protocol-device
                        combination unsupported
                
                copyInvalidProtocol :
                        invalid protocol specified
                
                copyInvalidSourceName :
                        invalid source file name specified
                        For the  copy from flash to lex operation, this
                        error code will be returned when the source file
                        is not a valid lex image.
                
                copyInvalidDestName :
                        invalid target name (file or partition or
                        device name) specified
                        For the  copy from flash to lex operation, this
                        error code will be returned when no lex devices
                        are connected to the router or when an invalid
                        lex interface number has been specified in
                        the destination string.
                
                copyInvalidServerAddress :
                        invalid server address specified
                
                copyDeviceBusy :
                        specified device is in use and locked by
                        another process
                
                copyDeviceOpenError :
                        invalid device name
                
                copyDeviceError :
                        device read, write or erase error
                
                copyDeviceNotProgrammable :
                        device is read-only but a write or erase
                        operation was specified
                
                copyDeviceFull :
                        device is filled to capacity
                
                copyFileOpenError :
                        invalid file name; file not found in partition
                
                copyFileTransferError :
                        file transfer was unsuccessfull; network failure
                
                copyFileChecksumError :
                        file checksum in Flash failed
                
                copyNoMemory :
                        system running low on memory
                
                copyUnknownFailure :
                        failure unknown
                
                copyProhibited:
                      stop user from overwriting current boot image file.
                ''',
                'ciscoflashcopystatus',
                'CISCO-FLASH-MIB', False),
            _MetaInfoClassMember('ciscoFlashCopyTime', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Time taken for the copy operation. This object will
                be like a stopwatch, starting when the operation
                starts, stopping when the operation completes.
                If a management entity keeps a database of completion
                times for various operations, it can then use the
                stopwatch capability to display percentage completion
                time.
                ''',
                'ciscoflashcopytime',
                'CISCO-FLASH-MIB', False),
            _MetaInfoClassMember('ciscoFlashCopyVerify', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Specifies whether the file that is copied need to
                be verified for integrity / authenticity, after
                copy succeeds. If it is set to true, and if the
                file that is copied doesn't have integrity /authenticity
                attachement, or the integrity / authenticity check
                fails, then the command will be aborted, and the file
                that is copied will be deleted from the destination
                file system.
                ''',
                'ciscoflashcopyverify',
                'CISCO-FLASH-MIB', False),
            ],
            'CISCO-FLASH-MIB',
            'ciscoFlashCopyEntry',
            _yang_ns._namespaces['CISCO-FLASH-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_FLASH_MIB'
        ),
    },
    'CiscoFlashMib.Ciscoflashcopytable' : {
        'meta_info' : _MetaInfoClass('CiscoFlashMib.Ciscoflashcopytable',
            False, 
            [
            _MetaInfoClassMember('ciscoFlashCopyEntry', REFERENCE_LIST, 'Ciscoflashcopyentry' , 'ydk.models.cisco_ios_xe.CISCO_FLASH_MIB', 'CiscoFlashMib.Ciscoflashcopytable.Ciscoflashcopyentry', 
                [], [], 
                '''                A Flash copy operation entry. Each entry consists
                of a command, a source, and optional parameters such
                as protocol to be used, a destination, a server address,
                etc.
                
                A management station wishing to create an entry should
                first generate a pseudo-random serial number to be used
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
                valid values for the non-defaulted parameter objects.
                
                Once an operation has been activated, it cannot be
                stopped.
                
                Once the operation completes, the management station should
                retrieve the value of the status object (and time if
                desired), and delete the entry.  In order to prevent old
                entries from clogging the table, entries will be aged out,
                but an entry will never be deleted within 5 minutes of
                completing.
                ''',
                'ciscoflashcopyentry',
                'CISCO-FLASH-MIB', False),
            ],
            'CISCO-FLASH-MIB',
            'ciscoFlashCopyTable',
            _yang_ns._namespaces['CISCO-FLASH-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_FLASH_MIB'
        ),
    },
    'CiscoFlashMib.Ciscoflashpartitioningtable.Ciscoflashpartitioningentry.CiscoflashpartitioningcommandEnum' : _MetaInfoEnum('CiscoflashpartitioningcommandEnum', 'ydk.models.cisco_ios_xe.CISCO_FLASH_MIB',
        {
            'partition':'partition',
        }, 'CISCO-FLASH-MIB', _yang_ns._namespaces['CISCO-FLASH-MIB']),
    'CiscoFlashMib.Ciscoflashpartitioningtable.Ciscoflashpartitioningentry.CiscoflashpartitioningstatusEnum' : _MetaInfoEnum('CiscoflashpartitioningstatusEnum', 'ydk.models.cisco_ios_xe.CISCO_FLASH_MIB',
        {
            'partitioningInProgress':'partitioningInProgress',
            'partitioningOperationSuccess':'partitioningOperationSuccess',
            'partitioningInvalidOperation':'partitioningInvalidOperation',
            'partitioningInvalidDestName':'partitioningInvalidDestName',
            'partitioningInvalidPartitionCount':'partitioningInvalidPartitionCount',
            'partitioningInvalidPartitionSizes':'partitioningInvalidPartitionSizes',
            'partitioningDeviceBusy':'partitioningDeviceBusy',
            'partitioningDeviceOpenError':'partitioningDeviceOpenError',
            'partitioningDeviceError':'partitioningDeviceError',
            'partitioningNoMemory':'partitioningNoMemory',
            'partitioningUnknownFailure':'partitioningUnknownFailure',
        }, 'CISCO-FLASH-MIB', _yang_ns._namespaces['CISCO-FLASH-MIB']),
    'CiscoFlashMib.Ciscoflashpartitioningtable.Ciscoflashpartitioningentry' : {
        'meta_info' : _MetaInfoClass('CiscoFlashMib.Ciscoflashpartitioningtable.Ciscoflashpartitioningentry',
            False, 
            [
            _MetaInfoClassMember('ciscoFlashPartitioningSerialNumber', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                Object which specifies a unique entry in the partitioning
                operations table. A management station wishing to initiate
                a partitioning operation should use a pseudo-random value
                for this object when creating or modifying an instance of
                a ciscoFlashPartitioningEntry.
                ''',
                'ciscoflashpartitioningserialnumber',
                'CISCO-FLASH-MIB', True),
            _MetaInfoClassMember('ciscoFlashPartitioningCommand', REFERENCE_ENUM_CLASS, 'CiscoflashpartitioningcommandEnum' , 'ydk.models.cisco_ios_xe.CISCO_FLASH_MIB', 'CiscoFlashMib.Ciscoflashpartitioningtable.Ciscoflashpartitioningentry.CiscoflashpartitioningcommandEnum', 
                [], [], 
                '''                The partitioning command to be executed. Mandatory.
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
                ''',
                'ciscoflashpartitioningcommand',
                'CISCO-FLASH-MIB', False),
            _MetaInfoClassMember('ciscoFlashPartitioningDestinationName', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                Destination device name. This name will be the value
                obtained from FlashDeviceName.
                If the name is not specified, the default Flash device
                will be assumed.
                ''',
                'ciscoflashpartitioningdestinationname',
                'CISCO-FLASH-MIB', False),
            _MetaInfoClassMember('ciscoFlashPartitioningEntryStatus', REFERENCE_ENUM_CLASS, 'RowstatusEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowstatusEnum', 
                [], [], 
                '''                The status of this table entry.
                ''',
                'ciscoflashpartitioningentrystatus',
                'CISCO-FLASH-MIB', False),
            _MetaInfoClassMember('ciscoFlashPartitioningNotifyOnCompletion', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Specifies whether or not a notification should be
                generated on the completion of the partitioning operation.
                If specified, ciscoFlashPartitioningCompletionTrap
                will be generated. It is the responsibility of the
                management entity to ensure that the SNMP administrative
                model is configured in such a way as to allow the
                notification to be delivered.
                ''',
                'ciscoflashpartitioningnotifyoncompletion',
                'CISCO-FLASH-MIB', False),
            _MetaInfoClassMember('ciscoFlashPartitioningPartitionCount', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                This object is used to specify the number of
                partitions to be created. Its value cannot exceed
                the value of ciscoFlashDeviceMaxPartitions.
                
                To undo partitioning (revert to a single partition),
                this object must have the value 1.
                ''',
                'ciscoflashpartitioningpartitioncount',
                'CISCO-FLASH-MIB', False),
            _MetaInfoClassMember('ciscoFlashPartitioningPartitionSizes', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                This object is used to explicitly specify the size
                of each partition to be created.
                The size of each partition will be in units of
                ciscoFlashDeviceMinPartitionSize.
                The value of this object will be in the form:
                        <part1>:<part2>...:<partn>
                
                If partition sizes are not specified, the system
                will calculate default sizes based on the partition
                count, the minimum partition size, and the device
                size. Partition size need not be specified when
                undoing partitioning (partition count is 1).
                If partition sizes are specified, the number of
                sizes specified must exactly match the partition
                count. If not, the partitioning command will be
                rejected with the invalidPartitionSizes error .
                ''',
                'ciscoflashpartitioningpartitionsizes',
                'CISCO-FLASH-MIB', False),
            _MetaInfoClassMember('ciscoFlashPartitioningStatus', REFERENCE_ENUM_CLASS, 'CiscoflashpartitioningstatusEnum' , 'ydk.models.cisco_ios_xe.CISCO_FLASH_MIB', 'CiscoFlashMib.Ciscoflashpartitioningtable.Ciscoflashpartitioningentry.CiscoflashpartitioningstatusEnum', 
                [], [], 
                '''                The status of the specified partitioning operation.
                partitioningInProgress :
                        specified operation is active
                
                partitioningOperationSuccess :
                        specified operation is supported and completed
                        successfully
                
                partitioningInvalidOperation :
                        command invalid or command-protocol-device
                        combination unsupported
                
                partitioningInvalidDestName :
                        invalid target name (file or partition or
                        device name) specified
                
                partitioningInvalidPartitionCount :
                        invalid partition count specified for the
                        partitioning command
                
                partitioningInvalidPartitionSizes :
                        invalid partition size, or invalid count of
                        partition sizes
                
                partitioningDeviceBusy :
                        specified device is in use and locked by
                        another process
                
                partitioningDeviceOpenError :
                        invalid device name
                
                partitioningDeviceError :
                        device read, write or erase error
                
                partitioningNoMemory :
                        system running low on memory
                
                partitioningUnknownFailure :
                        failure unknown
                ''',
                'ciscoflashpartitioningstatus',
                'CISCO-FLASH-MIB', False),
            _MetaInfoClassMember('ciscoFlashPartitioningTime', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Time taken for the operation. This object will
                be like a stopwatch, starting when the operation
                starts, stopping when the operation completes.
                If a management entity keeps a database of completion
                times for various operations, it can then use the
                stopwatch capability to display percentage completion
                time.
                ''',
                'ciscoflashpartitioningtime',
                'CISCO-FLASH-MIB', False),
            ],
            'CISCO-FLASH-MIB',
            'ciscoFlashPartitioningEntry',
            _yang_ns._namespaces['CISCO-FLASH-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_FLASH_MIB'
        ),
    },
    'CiscoFlashMib.Ciscoflashpartitioningtable' : {
        'meta_info' : _MetaInfoClass('CiscoFlashMib.Ciscoflashpartitioningtable',
            False, 
            [
            _MetaInfoClassMember('ciscoFlashPartitioningEntry', REFERENCE_LIST, 'Ciscoflashpartitioningentry' , 'ydk.models.cisco_ios_xe.CISCO_FLASH_MIB', 'CiscoFlashMib.Ciscoflashpartitioningtable.Ciscoflashpartitioningentry', 
                [], [], 
                '''                A Flash partitioning operation entry. Each entry
                consists of the command, the target device, the
                partition count, and optionally the partition sizes.
                
                A management station wishing to create an entry should
                first generate a pseudo-random serial number to be used
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
                valid values for the non-defaulted parameter objects.
                
                Once an operation has been activated, it cannot be
                stopped.
                
                Once the operation completes, the management station should
                retrieve the value of the status object (and time if
                desired), and delete the entry.  In order to prevent old
                entries from clogging the table, entries will be aged out,
                but an entry will never be deleted within 5 minutes of
                completing.
                ''',
                'ciscoflashpartitioningentry',
                'CISCO-FLASH-MIB', False),
            ],
            'CISCO-FLASH-MIB',
            'ciscoFlashPartitioningTable',
            _yang_ns._namespaces['CISCO-FLASH-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_FLASH_MIB'
        ),
    },
    'CiscoFlashMib.Ciscoflashmiscoptable.Ciscoflashmiscopentry.CiscoflashmiscopcommandEnum' : _MetaInfoEnum('CiscoflashmiscopcommandEnum', 'ydk.models.cisco_ios_xe.CISCO_FLASH_MIB',
        {
            'erase':'erase',
            'verify':'verify',
            'delete':'delete',
            'undelete':'undelete',
            'squeeze':'squeeze',
            'format':'format',
        }, 'CISCO-FLASH-MIB', _yang_ns._namespaces['CISCO-FLASH-MIB']),
    'CiscoFlashMib.Ciscoflashmiscoptable.Ciscoflashmiscopentry.CiscoflashmiscopstatusEnum' : _MetaInfoEnum('CiscoflashmiscopstatusEnum', 'ydk.models.cisco_ios_xe.CISCO_FLASH_MIB',
        {
            'miscOpInProgress':'miscOpInProgress',
            'miscOpOperationSuccess':'miscOpOperationSuccess',
            'miscOpInvalidOperation':'miscOpInvalidOperation',
            'miscOpInvalidDestName':'miscOpInvalidDestName',
            'miscOpDeviceBusy':'miscOpDeviceBusy',
            'miscOpDeviceOpenError':'miscOpDeviceOpenError',
            'miscOpDeviceError':'miscOpDeviceError',
            'miscOpDeviceNotProgrammable':'miscOpDeviceNotProgrammable',
            'miscOpFileOpenError':'miscOpFileOpenError',
            'miscOpFileDeleteFailure':'miscOpFileDeleteFailure',
            'miscOpFileUndeleteFailure':'miscOpFileUndeleteFailure',
            'miscOpFileChecksumError':'miscOpFileChecksumError',
            'miscOpNoMemory':'miscOpNoMemory',
            'miscOpUnknownFailure':'miscOpUnknownFailure',
            'miscOpSqueezeFailure':'miscOpSqueezeFailure',
            'miscOpNoSuchFile':'miscOpNoSuchFile',
            'miscOpFormatFailure':'miscOpFormatFailure',
        }, 'CISCO-FLASH-MIB', _yang_ns._namespaces['CISCO-FLASH-MIB']),
    'CiscoFlashMib.Ciscoflashmiscoptable.Ciscoflashmiscopentry' : {
        'meta_info' : _MetaInfoClass('CiscoFlashMib.Ciscoflashmiscoptable.Ciscoflashmiscopentry',
            False, 
            [
            _MetaInfoClassMember('ciscoFlashMiscOpSerialNumber', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                Object which specifies a unique entry in the
                table. A management station wishing to initiate a
                flash operation should use a pseudo-random value for
                this object when creating or modifying an instance of
                a ciscoFlashMiscOpEntry.
                ''',
                'ciscoflashmiscopserialnumber',
                'CISCO-FLASH-MIB', True),
            _MetaInfoClassMember('ciscoFlashMiscOpCommand', REFERENCE_ENUM_CLASS, 'CiscoflashmiscopcommandEnum' , 'ydk.models.cisco_ios_xe.CISCO_FLASH_MIB', 'CiscoFlashMib.Ciscoflashmiscoptable.Ciscoflashmiscopentry.CiscoflashmiscopcommandEnum', 
                [], [], 
                '''                The command to be executed. Mandatory.
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
                ''',
                'ciscoflashmiscopcommand',
                'CISCO-FLASH-MIB', False),
            _MetaInfoClassMember('ciscoFlashMiscOpDestinationName', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                Destination file, or partition name.
                File name must be of the form
                        [device>:][<partition>:]<file>
                where <device> is a value obtained from FlashDeviceName,
                      <partition> is obtained from FlashPartitionName
                  and <file> is the name of a file in Flash.
                While leading and/or trailing whitespaces are acceptable,
                no whitespaces are allowed within the path itself.
                
                A management station could derive its own partition name
                as per the description for the ciscoFlashPartitionName
                object.
                If <device> is not specified, the default Flash device
                will be assumed.
                If <partition> is not specified, the default partition
                will be assumed. If a device is not partitioned into 2
                or more partitions, this value may be left out.
                
                For an operation on a partition, eg., the erase
                command, this object would specify the partition name
                in the form:
                        [device>:][<partition>:]
                ''',
                'ciscoflashmiscopdestinationname',
                'CISCO-FLASH-MIB', False),
            _MetaInfoClassMember('ciscoFlashMiscOpEntryStatus', REFERENCE_ENUM_CLASS, 'RowstatusEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowstatusEnum', 
                [], [], 
                '''                The status of this table entry.
                ''',
                'ciscoflashmiscopentrystatus',
                'CISCO-FLASH-MIB', False),
            _MetaInfoClassMember('ciscoFlashMiscOpNotifyOnCompletion', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Specifies whether or not a notification should be
                generated on the completion of an operation.
                If specified, ciscoFlashMiscOpCompletionTrap
                will be generated. It is the responsibility of the
                management entity to ensure that the SNMP administrative
                model is configured in such a way as to allow the
                notification to be delivered.
                ''',
                'ciscoflashmiscopnotifyoncompletion',
                'CISCO-FLASH-MIB', False),
            _MetaInfoClassMember('ciscoFlashMiscOpStatus', REFERENCE_ENUM_CLASS, 'CiscoflashmiscopstatusEnum' , 'ydk.models.cisco_ios_xe.CISCO_FLASH_MIB', 'CiscoFlashMib.Ciscoflashmiscoptable.Ciscoflashmiscopentry.CiscoflashmiscopstatusEnum', 
                [], [], 
                '''                The status of the specified operation.
                miscOpInProgress :
                        specified operation is active
                
                miscOpOperationSuccess :
                        specified operation is supported and completed
                        successfully
                
                miscOpInvalidOperation :
                        command invalid or command-protocol-device
                        combination unsupported
                
                miscOpInvalidDestName :
                        invalid target name (file or partition or
                        device name) specified
                
                miscOpDeviceBusy :
                        specified device is in use and locked by another
                        process
                
                miscOpDeviceOpenError :
                        invalid device name
                
                miscOpDeviceError :
                        device read, write or erase error
                
                miscOpDeviceNotProgrammable :
                        device is read-only but a write or erase
                        operation was specified
                
                miscOpFileOpenError :
                        invalid file name; file not found in partition
                
                miscOpFileDeleteFailure :
                        file could not be deleted; delete count exceeded
                
                miscOpFileUndeleteFailure :
                        file could not be undeleted; undelete count
                        exceeded
                
                miscOpFileChecksumError :
                        file has a bad checksum
                
                miscOpNoMemory :
                        system running low on memory
                
                miscOpUnknownFailure :
                        failure unknown
                
                miscOpSqueezeFailure :
                        the squeeze operation failed
                
                miscOpNoSuchFile :
                        a valid but nonexistent file name was specified
                
                miscOpFormatFailure :
                        the format operation failed
                ''',
                'ciscoflashmiscopstatus',
                'CISCO-FLASH-MIB', False),
            _MetaInfoClassMember('ciscoFlashMiscOpTime', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Time taken for the operation. This object will
                be like a stopwatch, starting when the operation
                starts, stopping when the operation completes.
                If a management entity keeps a database of completion
                times for various operations, it can then use the
                stopwatch capability to display percentage completion
                time.
                ''',
                'ciscoflashmiscoptime',
                'CISCO-FLASH-MIB', False),
            ],
            'CISCO-FLASH-MIB',
            'ciscoFlashMiscOpEntry',
            _yang_ns._namespaces['CISCO-FLASH-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_FLASH_MIB'
        ),
    },
    'CiscoFlashMib.Ciscoflashmiscoptable' : {
        'meta_info' : _MetaInfoClass('CiscoFlashMib.Ciscoflashmiscoptable',
            False, 
            [
            _MetaInfoClassMember('ciscoFlashMiscOpEntry', REFERENCE_LIST, 'Ciscoflashmiscopentry' , 'ydk.models.cisco_ios_xe.CISCO_FLASH_MIB', 'CiscoFlashMib.Ciscoflashmiscoptable.Ciscoflashmiscopentry', 
                [], [], 
                '''                A Flash operation entry. Each entry consists of a
                command, a target, and any optional parameters.
                
                A management station wishing to create an entry should
                first generate a pseudo-random serial number to be used
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
                valid values for the non-defaulted parameter objects.
                
                Once an operation has been activated, it cannot be
                stopped.
                
                Once the operation completes, the management station should
                retrieve the value of the status object (and time if
                desired), and delete the entry.  In order to prevent old
                entries from clogging the table, entries will be aged out,
                but an entry will never be deleted within 5 minutes of
                completing.
                ''',
                'ciscoflashmiscopentry',
                'CISCO-FLASH-MIB', False),
            ],
            'CISCO-FLASH-MIB',
            'ciscoFlashMiscOpTable',
            _yang_ns._namespaces['CISCO-FLASH-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_FLASH_MIB'
        ),
    },
    'CiscoFlashMib' : {
        'meta_info' : _MetaInfoClass('CiscoFlashMib',
            False, 
            [
            _MetaInfoClassMember('ciscoFlashCfg', REFERENCE_CLASS, 'Ciscoflashcfg' , 'ydk.models.cisco_ios_xe.CISCO_FLASH_MIB', 'CiscoFlashMib.Ciscoflashcfg', 
                [], [], 
                '''                ''',
                'ciscoflashcfg',
                'CISCO-FLASH-MIB', False),
            _MetaInfoClassMember('ciscoFlashChipTable', REFERENCE_CLASS, 'Ciscoflashchiptable' , 'ydk.models.cisco_ios_xe.CISCO_FLASH_MIB', 'CiscoFlashMib.Ciscoflashchiptable', 
                [], [], 
                '''                Table of Flash device chip properties for each
                initialized Flash device.
                This table is meant primarily for aiding error
                diagnosis.
                ''',
                'ciscoflashchiptable',
                'CISCO-FLASH-MIB', False),
            _MetaInfoClassMember('ciscoFlashCopyTable', REFERENCE_CLASS, 'Ciscoflashcopytable' , 'ydk.models.cisco_ios_xe.CISCO_FLASH_MIB', 'CiscoFlashMib.Ciscoflashcopytable', 
                [], [], 
                '''                A table of Flash copy operation entries. Each
                entry represents a Flash copy operation (to or
                from Flash) that has been initiated.
                ''',
                'ciscoflashcopytable',
                'CISCO-FLASH-MIB', False),
            _MetaInfoClassMember('ciscoFlashDevice', REFERENCE_CLASS, 'Ciscoflashdevice' , 'ydk.models.cisco_ios_xe.CISCO_FLASH_MIB', 'CiscoFlashMib.Ciscoflashdevice', 
                [], [], 
                '''                ''',
                'ciscoflashdevice',
                'CISCO-FLASH-MIB', False),
            _MetaInfoClassMember('ciscoFlashDeviceTable', REFERENCE_CLASS, 'Ciscoflashdevicetable' , 'ydk.models.cisco_ios_xe.CISCO_FLASH_MIB', 'CiscoFlashMib.Ciscoflashdevicetable', 
                [], [], 
                '''                Table of Flash device properties for each initialized
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
                an indeterminate value:
                        ciscoFlashDeviceMinPartitionSize,
                        ciscoFlashDeviceMaxPartitions,
                        ciscoFlashDevicePartitions, and
                        ciscoFlashDeviceChipCount.
                ciscoFlashDeviceRemovable will be
                true to indicate it is removable.
                ''',
                'ciscoflashdevicetable',
                'CISCO-FLASH-MIB', False),
            _MetaInfoClassMember('ciscoFlashFileByTypeTable', REFERENCE_CLASS, 'Ciscoflashfilebytypetable' , 'ydk.models.cisco_ios_xe.CISCO_FLASH_MIB', 'CiscoFlashMib.Ciscoflashfilebytypetable', 
                [], [], 
                '''                Table of information for files on the manageable
                flash devices sorted by File Types.
                ''',
                'ciscoflashfilebytypetable',
                'CISCO-FLASH-MIB', False),
            _MetaInfoClassMember('ciscoFlashFileTable', REFERENCE_CLASS, 'Ciscoflashfiletable' , 'ydk.models.cisco_ios_xe.CISCO_FLASH_MIB', 'CiscoFlashMib.Ciscoflashfiletable', 
                [], [], 
                '''                Table of information for files in a Flash partition.
                ''',
                'ciscoflashfiletable',
                'CISCO-FLASH-MIB', False),
            _MetaInfoClassMember('ciscoFlashMiscOpTable', REFERENCE_CLASS, 'Ciscoflashmiscoptable' , 'ydk.models.cisco_ios_xe.CISCO_FLASH_MIB', 'CiscoFlashMib.Ciscoflashmiscoptable', 
                [], [], 
                '''                A table of misc Flash operation entries. Each
                entry represents a Flash operation that
                has been initiated.
                ''',
                'ciscoflashmiscoptable',
                'CISCO-FLASH-MIB', False),
            _MetaInfoClassMember('ciscoFlashPartitioningTable', REFERENCE_CLASS, 'Ciscoflashpartitioningtable' , 'ydk.models.cisco_ios_xe.CISCO_FLASH_MIB', 'CiscoFlashMib.Ciscoflashpartitioningtable', 
                [], [], 
                '''                A table of Flash partitioning operation entries. Each
                entry represents a Flash partitioning operation that
                has been initiated.
                ''',
                'ciscoflashpartitioningtable',
                'CISCO-FLASH-MIB', False),
            _MetaInfoClassMember('ciscoFlashPartitionTable', REFERENCE_CLASS, 'Ciscoflashpartitiontable' , 'ydk.models.cisco_ios_xe.CISCO_FLASH_MIB', 'CiscoFlashMib.Ciscoflashpartitiontable', 
                [], [], 
                '''                Table of flash device partition properties for each
                initialized flash partition. Whenever there is no
                explicit partitioning done, a single partition spanning
                the entire device will be assumed to exist. There will
                therefore always be atleast one partition on a device.
                ''',
                'ciscoflashpartitiontable',
                'CISCO-FLASH-MIB', False),
            ],
            'CISCO-FLASH-MIB',
            'CISCO-FLASH-MIB',
            _yang_ns._namespaces['CISCO-FLASH-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_FLASH_MIB'
        ),
    },
}
_meta_table['CiscoFlashMib.Ciscoflashdevicetable.Ciscoflashdeviceentry']['meta_info'].parent =_meta_table['CiscoFlashMib.Ciscoflashdevicetable']['meta_info']
_meta_table['CiscoFlashMib.Ciscoflashchiptable.Ciscoflashchipentry']['meta_info'].parent =_meta_table['CiscoFlashMib.Ciscoflashchiptable']['meta_info']
_meta_table['CiscoFlashMib.Ciscoflashpartitiontable.Ciscoflashpartitionentry']['meta_info'].parent =_meta_table['CiscoFlashMib.Ciscoflashpartitiontable']['meta_info']
_meta_table['CiscoFlashMib.Ciscoflashfiletable.Ciscoflashfileentry']['meta_info'].parent =_meta_table['CiscoFlashMib.Ciscoflashfiletable']['meta_info']
_meta_table['CiscoFlashMib.Ciscoflashfilebytypetable.Ciscoflashfilebytypeentry']['meta_info'].parent =_meta_table['CiscoFlashMib.Ciscoflashfilebytypetable']['meta_info']
_meta_table['CiscoFlashMib.Ciscoflashcopytable.Ciscoflashcopyentry']['meta_info'].parent =_meta_table['CiscoFlashMib.Ciscoflashcopytable']['meta_info']
_meta_table['CiscoFlashMib.Ciscoflashpartitioningtable.Ciscoflashpartitioningentry']['meta_info'].parent =_meta_table['CiscoFlashMib.Ciscoflashpartitioningtable']['meta_info']
_meta_table['CiscoFlashMib.Ciscoflashmiscoptable.Ciscoflashmiscopentry']['meta_info'].parent =_meta_table['CiscoFlashMib.Ciscoflashmiscoptable']['meta_info']
_meta_table['CiscoFlashMib.Ciscoflashdevice']['meta_info'].parent =_meta_table['CiscoFlashMib']['meta_info']
_meta_table['CiscoFlashMib.Ciscoflashcfg']['meta_info'].parent =_meta_table['CiscoFlashMib']['meta_info']
_meta_table['CiscoFlashMib.Ciscoflashdevicetable']['meta_info'].parent =_meta_table['CiscoFlashMib']['meta_info']
_meta_table['CiscoFlashMib.Ciscoflashchiptable']['meta_info'].parent =_meta_table['CiscoFlashMib']['meta_info']
_meta_table['CiscoFlashMib.Ciscoflashpartitiontable']['meta_info'].parent =_meta_table['CiscoFlashMib']['meta_info']
_meta_table['CiscoFlashMib.Ciscoflashfiletable']['meta_info'].parent =_meta_table['CiscoFlashMib']['meta_info']
_meta_table['CiscoFlashMib.Ciscoflashfilebytypetable']['meta_info'].parent =_meta_table['CiscoFlashMib']['meta_info']
_meta_table['CiscoFlashMib.Ciscoflashcopytable']['meta_info'].parent =_meta_table['CiscoFlashMib']['meta_info']
_meta_table['CiscoFlashMib.Ciscoflashpartitioningtable']['meta_info'].parent =_meta_table['CiscoFlashMib']['meta_info']
_meta_table['CiscoFlashMib.Ciscoflashmiscoptable']['meta_info'].parent =_meta_table['CiscoFlashMib']['meta_info']
