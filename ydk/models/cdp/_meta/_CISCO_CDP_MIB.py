


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum, _dm_validate_value
from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYDataValidationError
from ydk.models import _yang_ns

_meta_table = {
    'CISCOCDPMIB.CdpCacheTable.CdpCacheEntry.CdpCacheDuplex_Enum' : _MetaInfoEnum('CdpCacheDuplex_Enum', 'ydk.models.cdp.CISCO_CDP_MIB',
        {
            'unknown':'UNKNOWN',
            'halfduplex':'HALFDUPLEX',
            'fullduplex':'FULLDUPLEX',
        }, 'CISCO-CDP-MIB', _yang_ns._namespaces['CISCO-CDP-MIB']),
    'CISCOCDPMIB.CdpCacheTable.CdpCacheEntry' : {
        'meta_info' : _MetaInfoClass('CISCOCDPMIB.CdpCacheTable.CdpCacheEntry',
            False, 
            [
            _MetaInfoClassMember('cdpCacheDeviceIndex', ATTRIBUTE, 'int' , None, None, 
                [(0, 2147483647)], [], 
                '''                A unique value for each device from which CDP messages
                are being received.
                ''',
                'cdpcachedeviceindex',
                'CISCO-CDP-MIB', True),
            _MetaInfoClassMember('cdpCacheIfIndex', ATTRIBUTE, 'int' , None, None, 
                [(0, 2147483647)], [], 
                '''                Normally, the ifIndex value of the local interface.
                For 802.3 Repeaters for which the repeater ports do not
                have ifIndex values assigned, this value is a unique
                value for the port, and greater than any ifIndex value
                supported by the repeater; the specific port number in
                this case, is given by the corresponding value of
                cdpInterfacePort.
                ''',
                'cdpcacheifindex',
                'CISCO-CDP-MIB', True),
            _MetaInfoClassMember('cdpCacheAddress', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The (first) network-layer address of the device
                as reported in the Address TLV of the most recently received
                CDP message.  For example, if the corresponding instance of
                cacheAddressType had the value 'ip(1)', then this object 
                would be an IPv4-address.  If the neighbor device is 
                SNMP-manageable, it is supposed to generate its CDP messages
                such that this address is one at which it will receive SNMP
                messages. Use cdpCtAddressTable to extract the remaining
                addresses from the Address TLV received most recently.
                ''',
                'cdpcacheaddress',
                'CISCO-CDP-MIB', False),
            _MetaInfoClassMember('cdpCacheAddressType', REFERENCE_ENUM_CLASS, 'CiscoNetworkProtocol_Enum' , 'ydk.models.tc.CISCO_TC', 'CiscoNetworkProtocol_Enum', 
                [], [], 
                '''                An indication of the type of address contained in the
                corresponding instance of cdpCacheAddress.
                ''',
                'cdpcacheaddresstype',
                'CISCO-CDP-MIB', False),
            _MetaInfoClassMember('cdpCacheApplianceID', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                The remote device's Appliance ID, as reported in the 
                most recent CDP message. This object is not instantiated if
                no Appliance VLAN-ID field (TLV) was reported in the most
                recently received CDP message.
                ''',
                'cdpcacheapplianceid',
                'CISCO-CDP-MIB', False),
            _MetaInfoClassMember('cdpCacheCapabilities', ATTRIBUTE, 'str' , None, None, 
                [(0, 4)], [], 
                '''                The Device's Functional Capabilities as reported in the
                most recent CDP message.  For latest set of specific
                values, see the latest version of the CDP specification.
                The zero-length string indicates no Capabilities field
                (TLV) was reported in the most recent CDP message.
                ''',
                'cdpcachecapabilities',
                'CISCO-CDP-MIB', False),
            _MetaInfoClassMember('cdpCacheDeviceId', ATTRIBUTE, 'str' , None, None, 
                [], ['\\p{IsBasicLatin}{0,255}'], 
                '''                The Device-ID string as reported in the most recent CDP
                message.  The zero-length string indicates no Device-ID
                field (TLV) was reported in the most recent CDP
                message.
                ''',
                'cdpcachedeviceid',
                'CISCO-CDP-MIB', False),
            _MetaInfoClassMember('cdpCacheDevicePort', ATTRIBUTE, 'str' , None, None, 
                [], ['\\p{IsBasicLatin}{0,255}'], 
                '''                The Port-ID string as reported in the most recent CDP
                message.  This will typically be the value of the ifName
                object (e.g., 'Ethernet0').  The zero-length string
                indicates no Port-ID field (TLV) was reported in the
                most recent CDP message.
                ''',
                'cdpcachedeviceport',
                'CISCO-CDP-MIB', False),
            _MetaInfoClassMember('cdpCacheDuplex', REFERENCE_ENUM_CLASS, 'CdpCacheDuplex_Enum' , 'ydk.models.cdp.CISCO_CDP_MIB', 'CISCOCDPMIB.CdpCacheTable.CdpCacheEntry.CdpCacheDuplex_Enum', 
                [], [], 
                '''                The remote device's interface's duplex mode, as reported in the 
                most recent CDP message.  The value unknown(1) indicates
                no duplex mode field (TLV) was reported in the most
                recent CDP message.
                ''',
                'cdpcacheduplex',
                'CISCO-CDP-MIB', False),
            _MetaInfoClassMember('cdpCacheLastChange', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Indicates the time when this cache entry was last changed.
                This object is initialised to the current time when the entry
                gets created and updated to the current time whenever the value
                of any (other) object instance in the corresponding row is
                modified.
                ''',
                'cdpcachelastchange',
                'CISCO-CDP-MIB', False),
            _MetaInfoClassMember('cdpCacheMTU', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Indicates the size of the largest datagram that can be
                sent/received by remote device, as reported in the most recent
                CDP message. This object is not instantiated if no MTU field
                (TLV) was reported in the most recently received CDP message.
                ''',
                'cdpcachemtu',
                'CISCO-CDP-MIB', False),
            _MetaInfoClassMember('cdpCacheNativeVLAN', ATTRIBUTE, 'int' , None, None, 
                [(0, 4095)], [], 
                '''                The remote device's interface's native VLAN, as reported in the 
                most recent CDP message.  The value 0 indicates
                no native VLAN field (TLV) was reported in the most
                recent CDP message.
                ''',
                'cdpcachenativevlan',
                'CISCO-CDP-MIB', False),
            _MetaInfoClassMember('cdpCachePhysLocation', ATTRIBUTE, 'str' , None, None, 
                [], ['\\p{IsBasicLatin}{0,255}'], 
                '''                Indicates the physical location, as reported by the most recent
                CDP message, of a connector which is on, or physically connected
                to, the remote device's interface over which the CDP packet is
                sent. This object is not instantiated if no Physical Location
                field (TLV) was reported by the most recently received CDP
                message.
                ''',
                'cdpcachephyslocation',
                'CISCO-CDP-MIB', False),
            _MetaInfoClassMember('cdpCachePlatform', ATTRIBUTE, 'str' , None, None, 
                [], ['\\p{IsBasicLatin}{0,255}'], 
                '''                The Device's Hardware Platform as reported in the most
                recent CDP message.  The zero-length string indicates
                that no Platform field (TLV) was reported in the most
                recent CDP message.
                ''',
                'cdpcacheplatform',
                'CISCO-CDP-MIB', False),
            _MetaInfoClassMember('cdpCachePowerConsumption', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The amount of power consumed by remote device, as reported
                in the most recent CDP message. This object is not instantiated
                if no Power Consumption field (TLV) was reported in the most
                recently received CDP message.
                ''',
                'cdpcachepowerconsumption',
                'CISCO-CDP-MIB', False),
            _MetaInfoClassMember('cdpCachePrimaryMgmtAddr', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                This object indicates the (first) network layer
                address at which the device will accept SNMP messages
                as reported in the first address in the 
                Management-Address TLV of the most recently received
                CDP message.  If the corresponding instance of 
                cdpCachePrimaryMgmtAddrType has the value 'ip(1)',
                then this object would be an IP-address. If the 
                remote device is not currently manageable via any 
                network protocol, then it reports the special value 
                of the IPv4 address 0.0.0.0, and that address is 
                recorded in this object.  If the most recently received
                CDP message did not contain the Management-Address
                TLV, then this object is not instanstiated.
                ''',
                'cdpcacheprimarymgmtaddr',
                'CISCO-CDP-MIB', False),
            _MetaInfoClassMember('cdpCachePrimaryMgmtAddrType', REFERENCE_ENUM_CLASS, 'CiscoNetworkProtocol_Enum' , 'ydk.models.tc.CISCO_TC', 'CiscoNetworkProtocol_Enum', 
                [], [], 
                '''                An indication of the type of address contained in the
                corresponding instance of cdpCachePrimaryMgmtAddress.
                ''',
                'cdpcacheprimarymgmtaddrtype',
                'CISCO-CDP-MIB', False),
            _MetaInfoClassMember('cdpCacheSecondaryMgmtAddr', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                This object indicates the alternate network layer
                address at which the device will accept SNMP messages
                as reported in the second address in the 
                Management-Address TLV of the most recently received
                CDP message.  If the corresponding instance of
                cdpCacheSecondaryMgmtAddrType has the value 'ip(1)',
                then this object would be an IP-address. If the 
                remote device reports the special value of the 
                IPv4 address 0.0.0.0, that address is recorded in 
                this object.  If the most recently received CDP
                message did not contain the Management-Address
                TLV, or if that TLV contained only one address, then
                this object is not instanstiated.
                ''',
                'cdpcachesecondarymgmtaddr',
                'CISCO-CDP-MIB', False),
            _MetaInfoClassMember('cdpCacheSecondaryMgmtAddrType', REFERENCE_ENUM_CLASS, 'CiscoNetworkProtocol_Enum' , 'ydk.models.tc.CISCO_TC', 'CiscoNetworkProtocol_Enum', 
                [], [], 
                '''                An indication of the type of address contained in the
                corresponding instance of cdpCacheSecondaryMgmtAddress.
                ''',
                'cdpcachesecondarymgmtaddrtype',
                'CISCO-CDP-MIB', False),
            _MetaInfoClassMember('cdpCacheSysName', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                Indicates the value of the remote device's sysName MIB object.
                By convention, it is the device's fully qualified domain name.
                This object is not instantiated if no sysName field (TLV) was
                reported in the most recently received CDP message.
                ''',
                'cdpcachesysname',
                'CISCO-CDP-MIB', False),
            _MetaInfoClassMember('cdpCacheSysObjectID', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-1](\\.[1-3]?[0-9]))|(2\\.(0|([1-9]\\d*))))(\\.(0|([1-9]\\d*)))*'], 
                '''                Indicates the value of the remote device's sysObjectID MIB
                object. This object is not instantiated if no sysObjectID field
                (TLV) was reported in the most recently received CDP message.
                ''',
                'cdpcachesysobjectid',
                'CISCO-CDP-MIB', False),
            _MetaInfoClassMember('cdpCacheVersion', ATTRIBUTE, 'str' , None, None, 
                [], ['\\p{IsBasicLatin}{0,255}'], 
                '''                The Version string as reported in the most recent CDP
                message.  The zero-length string indicates no Version
                field (TLV) was reported in the most recent CDP
                message.
                ''',
                'cdpcacheversion',
                'CISCO-CDP-MIB', False),
            _MetaInfoClassMember('cdpCacheVlanID', ATTRIBUTE, 'int' , None, None, 
                [(0, 4095)], [], 
                '''                The remote device's VoIP VLAN ID, as reported in the 
                most recent CDP message. This object is not instantiated if
                no Appliance VLAN-ID field (TLV) was reported in the most
                recently received CDP message.
                ''',
                'cdpcachevlanid',
                'CISCO-CDP-MIB', False),
            _MetaInfoClassMember('cdpCacheVTPMgmtDomain', ATTRIBUTE, 'str' , None, None, 
                [(0, 32)], [], 
                '''                The VTP Management Domain for the remote device's interface, 
                as reported in the most recently received CDP message.
                This object is not instantiated if no VTP Management Domain field
                (TLV) was reported in the most recently received CDP message.
                ''',
                'cdpcachevtpmgmtdomain',
                'CISCO-CDP-MIB', False),
            ],
            'CISCO-CDP-MIB',
            'cdpCacheEntry',
            _yang_ns._namespaces['CISCO-CDP-MIB'],
        'ydk.models.cdp.CISCO_CDP_MIB'
        ),
    },
    'CISCOCDPMIB.CdpCacheTable' : {
        'meta_info' : _MetaInfoClass('CISCOCDPMIB.CdpCacheTable',
            False, 
            [
            _MetaInfoClassMember('cdpCacheEntry', REFERENCE_LIST, 'CdpCacheEntry' , 'ydk.models.cdp.CISCO_CDP_MIB', 'CISCOCDPMIB.CdpCacheTable.CdpCacheEntry', 
                [], [], 
                '''                An entry (conceptual row) in the cdpCacheTable,
                containing the information received via CDP on one
                interface from one device.  Entries appear when
                a CDP advertisement is received from a neighbor
                device.  Entries disappear when CDP is disabled
                on the interface, or globally.
                ''',
                'cdpcacheentry',
                'CISCO-CDP-MIB', False),
            ],
            'CISCO-CDP-MIB',
            'cdpCacheTable',
            _yang_ns._namespaces['CISCO-CDP-MIB'],
        'ydk.models.cdp.CISCO_CDP_MIB'
        ),
    },
    'CISCOCDPMIB.CdpCtAddressTable.CdpCtAddressEntry' : {
        'meta_info' : _MetaInfoClass('CISCOCDPMIB.CdpCtAddressTable.CdpCtAddressEntry',
            False, 
            [
            _MetaInfoClassMember('cdpCacheDeviceIndex', ATTRIBUTE, 'int' , None, None, 
                [(0, 2147483647)], [], 
                '''                ''',
                'cdpcachedeviceindex',
                'CISCO-CDP-MIB', True),
            _MetaInfoClassMember('cdpCacheIfIndex', ATTRIBUTE, 'int' , None, None, 
                [(0, 2147483647)], [], 
                '''                ''',
                'cdpcacheifindex',
                'CISCO-CDP-MIB', True),
            _MetaInfoClassMember('cdpCtAddressIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                The index of the address entry for a given 
                cdpCacheIfIndex,cdpCacheDeviceIndex pair. It
                has the value N-1 for the N-th address in the
                Address TLV
                ''',
                'cdpctaddressindex',
                'CISCO-CDP-MIB', True),
            _MetaInfoClassMember('cdpCtAddress', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The N-th network-layer address of the device as reported
                in the most recent CDP message's Address TLV, where N-1 is
                given by the value of cdpCtAddressIndex. For example, if
                the the corresponding instance of cdpCtAddressType had the
                value 'ip(1)', then this object would be an IPv4-address.
                NOTE - The 1st address received in the Address TLV is
                       available using cdpCacheAddress
                ''',
                'cdpctaddress',
                'CISCO-CDP-MIB', False),
            _MetaInfoClassMember('cdpCtAddressType', REFERENCE_ENUM_CLASS, 'CiscoNetworkProtocol_Enum' , 'ydk.models.tc.CISCO_TC', 'CiscoNetworkProtocol_Enum', 
                [], [], 
                '''                An indication of the type of address contained in the
                corresponding instance of cdpCtAddress.
                ''',
                'cdpctaddresstype',
                'CISCO-CDP-MIB', False),
            ],
            'CISCO-CDP-MIB',
            'cdpCtAddressEntry',
            _yang_ns._namespaces['CISCO-CDP-MIB'],
        'ydk.models.cdp.CISCO_CDP_MIB'
        ),
    },
    'CISCOCDPMIB.CdpCtAddressTable' : {
        'meta_info' : _MetaInfoClass('CISCOCDPMIB.CdpCtAddressTable',
            False, 
            [
            _MetaInfoClassMember('cdpCtAddressEntry', REFERENCE_LIST, 'CdpCtAddressEntry' , 'ydk.models.cdp.CISCO_CDP_MIB', 'CISCOCDPMIB.CdpCtAddressTable.CdpCtAddressEntry', 
                [], [], 
                '''                An entry (conceptual row) in the cdpCtAddressTable,
                containing the information on one address received via CDP 
                on one interface from one device.  Entries appear 
                when a CDP advertisement is received from a neighbor
                device, with an Address TLV.  Entries disappear when
                CDP is disabled on the interface, or globally. An entry 
                or entries would also disappear if the most recently
                received CDP packet contain fewer address entries in the
                Address TLV, than are currently present in the CDP cache.
                ''',
                'cdpctaddressentry',
                'CISCO-CDP-MIB', False),
            ],
            'CISCO-CDP-MIB',
            'cdpCtAddressTable',
            _yang_ns._namespaces['CISCO-CDP-MIB'],
        'ydk.models.cdp.CISCO_CDP_MIB'
        ),
    },
    'CISCOCDPMIB.CdpGlobal.CdpGlobalDeviceIdFormat_Enum' : _MetaInfoEnum('CdpGlobalDeviceIdFormat_Enum', 'ydk.models.cdp.CISCO_CDP_MIB',
        {
            'serialNumber':'SERIALNUMBER',
            'macAddress':'MACADDRESS',
            'other':'OTHER',
        }, 'CISCO-CDP-MIB', _yang_ns._namespaces['CISCO-CDP-MIB']),
    'CISCOCDPMIB.CdpGlobal' : {
        'meta_info' : _MetaInfoClass('CISCOCDPMIB.CdpGlobal',
            False, 
            [
            _MetaInfoClassMember('cdpGlobalDeviceId', ATTRIBUTE, 'str' , None, None, 
                [], ['\\p{IsBasicLatin}{0,255}'], 
                '''                The device ID advertised by this device. The format of this
                device id is characterized by the value of 
                cdpGlobalDeviceIdFormat object.
                ''',
                'cdpglobaldeviceid',
                'CISCO-CDP-MIB', False),
            _MetaInfoClassMember('cdpGlobalDeviceIdFormat', REFERENCE_ENUM_CLASS, 'CdpGlobalDeviceIdFormat_Enum' , 'ydk.models.cdp.CISCO_CDP_MIB', 'CISCOCDPMIB.CdpGlobal.CdpGlobalDeviceIdFormat_Enum', 
                [], [], 
                '''                An indication of the format of Device-Id contained in the
                corresponding instance of cdpGlobalDeviceId. User can only
                specify the formats that the device is capable of as
                denoted in cdpGlobalDeviceIdFormatCpb object.
                
                serialNumber(1) indicates that the value of cdpGlobalDeviceId 
                object is in the form of an ASCII string contain the device
                serial number. 
                
                macAddress(2) indicates that the value of cdpGlobalDeviceId 
                object is in the form of Layer 2 MAC address.
                
                other(3) indicates that the value of cdpGlobalDeviceId object
                is in the form of a platform specific ASCII string contain
                info that identifies the device. For example: ASCII string
                contains serialNumber appended/prepened with system name.
                ''',
                'cdpglobaldeviceidformat',
                'CISCO-CDP-MIB', False),
            _MetaInfoClassMember('cdpGlobalDeviceIdFormatCpb', REFERENCE_BITS, 'CdpGlobalDeviceIdFormatCpb_Bits' , 'ydk.models.cdp.CISCO_CDP_MIB', 'CISCOCDPMIB.CdpGlobal.CdpGlobalDeviceIdFormatCpb_Bits', 
                [], [], 
                '''                Indicate the Device-Id format capability of the device.
                
                serialNumber(0) indicates that the device supports using
                serial number as the format for its DeviceId.
                
                macAddress(1) indicates that the device supports using
                layer 2 MAC address as the format for its DeviceId.
                
                other(2) indicates that the device supports using its
                platform specific format as the format for its DeviceId.
                ''',
                'cdpglobaldeviceidformatcpb',
                'CISCO-CDP-MIB', False),
            _MetaInfoClassMember('cdpGlobalHoldTime', ATTRIBUTE, 'int' , None, None, 
                [(10, 255)], [], 
                '''                The time for the receiving device holds CDP message.
                The default value is 180 seconds.
                ''',
                'cdpglobalholdtime',
                'CISCO-CDP-MIB', False),
            _MetaInfoClassMember('cdpGlobalLastChange', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Indicates the time when the cache table was last changed. It
                is the most recent time at which any row was last created,
                modified or deleted.
                ''',
                'cdpgloballastchange',
                'CISCO-CDP-MIB', False),
            _MetaInfoClassMember('cdpGlobalMessageInterval', ATTRIBUTE, 'int' , None, None, 
                [(5, 254)], [], 
                '''                The interval at which CDP messages are to be generated.
                The default value is 60 seconds.
                ''',
                'cdpglobalmessageinterval',
                'CISCO-CDP-MIB', False),
            _MetaInfoClassMember('cdpGlobalRun', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                An indication of whether the Cisco Discovery Protocol
                is currently running.  Entries in cdpCacheTable are
                deleted when CDP is disabled.
                ''',
                'cdpglobalrun',
                'CISCO-CDP-MIB', False),
            ],
            'CISCO-CDP-MIB',
            'cdpGlobal',
            _yang_ns._namespaces['CISCO-CDP-MIB'],
        'ydk.models.cdp.CISCO_CDP_MIB'
        ),
    },
    'CISCOCDPMIB.CdpInterfaceExtTable.CdpInterfaceExtEntry.CdpInterfaceExtendedTrust_Enum' : _MetaInfoEnum('CdpInterfaceExtendedTrust_Enum', 'ydk.models.cdp.CISCO_CDP_MIB',
        {
            'trusted':'TRUSTED',
            'noTrust':'NOTRUST',
        }, 'CISCO-CDP-MIB', _yang_ns._namespaces['CISCO-CDP-MIB']),
    'CISCOCDPMIB.CdpInterfaceExtTable.CdpInterfaceExtEntry' : {
        'meta_info' : _MetaInfoClass('CISCOCDPMIB.CdpInterfaceExtTable.CdpInterfaceExtEntry',
            False, 
            [
            _MetaInfoClassMember('ifIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                ''',
                'ifindex',
                'CISCO-CDP-MIB', True),
            _MetaInfoClassMember('cdpInterfaceCosForUntrustedPort', ATTRIBUTE, 'int' , None, None, 
                [(0, 7)], [], 
                '''                Indicates the value to be sent by COS for Untrusted Ports TLV.
                ''',
                'cdpinterfacecosforuntrustedport',
                'CISCO-CDP-MIB', False),
            _MetaInfoClassMember('cdpInterfaceExtendedTrust', REFERENCE_ENUM_CLASS, 'CdpInterfaceExtendedTrust_Enum' , 'ydk.models.cdp.CISCO_CDP_MIB', 'CISCOCDPMIB.CdpInterfaceExtTable.CdpInterfaceExtEntry.CdpInterfaceExtendedTrust_Enum', 
                [], [], 
                '''                Indicates the value to be sent by Extended Trust TLV.
                
                If trusted(1) is configured, the value of Extended Trust TLV
                is one byte in length with its least significant bit equal to
                1 to indicate extended trust. All other bits are 0.
                
                If noTrust(2) is configured, the value of Extended Trust TLV
                is one byte in length with its least significant bit equal to
                0 to indicate no extended trust. All other bits are 0.
                ''',
                'cdpinterfaceextendedtrust',
                'CISCO-CDP-MIB', False),
            ],
            'CISCO-CDP-MIB',
            'cdpInterfaceExtEntry',
            _yang_ns._namespaces['CISCO-CDP-MIB'],
        'ydk.models.cdp.CISCO_CDP_MIB'
        ),
    },
    'CISCOCDPMIB.CdpInterfaceExtTable' : {
        'meta_info' : _MetaInfoClass('CISCOCDPMIB.CdpInterfaceExtTable',
            False, 
            [
            _MetaInfoClassMember('cdpInterfaceExtEntry', REFERENCE_LIST, 'CdpInterfaceExtEntry' , 'ydk.models.cdp.CISCO_CDP_MIB', 'CISCOCDPMIB.CdpInterfaceExtTable.CdpInterfaceExtEntry', 
                [], [], 
                '''                An entry in the cdpInterfaceExtTable contains the values
                configured for Extented Trust TLV and COS (Class of Service)
                for Untrusted Ports TLV on an interface which supports the
                sending of these TLVs.
                ''',
                'cdpinterfaceextentry',
                'CISCO-CDP-MIB', False),
            ],
            'CISCO-CDP-MIB',
            'cdpInterfaceExtTable',
            _yang_ns._namespaces['CISCO-CDP-MIB'],
        'ydk.models.cdp.CISCO_CDP_MIB'
        ),
    },
    'CISCOCDPMIB.CdpInterfaceTable.CdpInterfaceEntry' : {
        'meta_info' : _MetaInfoClass('CISCOCDPMIB.CdpInterfaceTable.CdpInterfaceEntry',
            False, 
            [
            _MetaInfoClassMember('cdpInterfaceIfIndex', ATTRIBUTE, 'int' , None, None, 
                [(0, 2147483647)], [], 
                '''                The ifIndex value of the local interface.
                
                For 802.3 Repeaters on which the repeater ports do not
                have ifIndex values assigned, this value is a unique
                value for the port, and greater than any ifIndex value
                supported by the repeater; in this case, the specific
                port is indicated by corresponding values of
                cdpInterfaceGroup and cdpInterfacePort, where these
                values correspond to the group number and port number
                values of RFC 1516.
                ''',
                'cdpinterfaceifindex',
                'CISCO-CDP-MIB', True),
            _MetaInfoClassMember('cdpInterfaceEnable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                An indication of whether the Cisco Discovery Protocol
                is currently running on this interface.  This variable
                has no effect when CDP is disabled (cdpGlobalRun = FALSE).
                ''',
                'cdpinterfaceenable',
                'CISCO-CDP-MIB', False),
            _MetaInfoClassMember('cdpInterfaceGroup', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                This object is only relevant to interfaces which are
                repeater ports on 802.3 repeaters.  In this situation,
                it indicates the RFC1516 group number of the repeater
                port which corresponds to this interface.
                ''',
                'cdpinterfacegroup',
                'CISCO-CDP-MIB', False),
            _MetaInfoClassMember('cdpInterfaceMessageInterval', ATTRIBUTE, 'int' , None, None, 
                [(5, 254)], [], 
                '''                The interval at which CDP messages are to be generated
                on this interface.  The default value is 60 seconds.
                ''',
                'cdpinterfacemessageinterval',
                'CISCO-CDP-MIB', False),
            _MetaInfoClassMember('cdpInterfaceName', ATTRIBUTE, 'str' , None, None, 
                [], ['\\p{IsBasicLatin}{0,255}'], 
                '''                The name of the local interface as advertised by
                CDP in the Port-ID TLV
                ''',
                'cdpinterfacename',
                'CISCO-CDP-MIB', False),
            _MetaInfoClassMember('cdpInterfacePort', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                This object is only relevant to interfaces which are
                repeater ports on 802.3 repeaters.  In this situation,
                it indicates the RFC1516 port number of the repeater
                port which corresponds to this interface.
                ''',
                'cdpinterfaceport',
                'CISCO-CDP-MIB', False),
            ],
            'CISCO-CDP-MIB',
            'cdpInterfaceEntry',
            _yang_ns._namespaces['CISCO-CDP-MIB'],
        'ydk.models.cdp.CISCO_CDP_MIB'
        ),
    },
    'CISCOCDPMIB.CdpInterfaceTable' : {
        'meta_info' : _MetaInfoClass('CISCOCDPMIB.CdpInterfaceTable',
            False, 
            [
            _MetaInfoClassMember('cdpInterfaceEntry', REFERENCE_LIST, 'CdpInterfaceEntry' , 'ydk.models.cdp.CISCO_CDP_MIB', 'CISCOCDPMIB.CdpInterfaceTable.CdpInterfaceEntry', 
                [], [], 
                '''                An entry (conceptual row) in the cdpInterfaceTable,
                containing the status of CDP on an interface.
                ''',
                'cdpinterfaceentry',
                'CISCO-CDP-MIB', False),
            ],
            'CISCO-CDP-MIB',
            'cdpInterfaceTable',
            _yang_ns._namespaces['CISCO-CDP-MIB'],
        'ydk.models.cdp.CISCO_CDP_MIB'
        ),
    },
    'CISCOCDPMIB' : {
        'meta_info' : _MetaInfoClass('CISCOCDPMIB',
            False, 
            [
            _MetaInfoClassMember('cdpCacheTable', REFERENCE_CLASS, 'CdpCacheTable' , 'ydk.models.cdp.CISCO_CDP_MIB', 'CISCOCDPMIB.CdpCacheTable', 
                [], [], 
                '''                The (conceptual) table containing the cached
                information obtained via receiving CDP messages.
                ''',
                'cdpcachetable',
                'CISCO-CDP-MIB', False),
            _MetaInfoClassMember('cdpCtAddressTable', REFERENCE_CLASS, 'CdpCtAddressTable' , 'ydk.models.cdp.CISCO_CDP_MIB', 'CISCOCDPMIB.CdpCtAddressTable', 
                [], [], 
                '''                The (conceptual) table containing the list of 
                network-layer addresses of a neighbor interface,
                as reported in the Address TLV of the most recently
                received CDP message. The first address included in
                the Address TLV is saved in cdpCacheAddress.  This
                table contains the remainder of the addresses in the
                Address TLV.
                ''',
                'cdpctaddresstable',
                'CISCO-CDP-MIB', False),
            _MetaInfoClassMember('cdpGlobal', REFERENCE_CLASS, 'CdpGlobal' , 'ydk.models.cdp.CISCO_CDP_MIB', 'CISCOCDPMIB.CdpGlobal', 
                [], [], 
                '''                ''',
                'cdpglobal',
                'CISCO-CDP-MIB', False),
            _MetaInfoClassMember('cdpInterfaceExtTable', REFERENCE_CLASS, 'CdpInterfaceExtTable' , 'ydk.models.cdp.CISCO_CDP_MIB', 'CISCOCDPMIB.CdpInterfaceExtTable', 
                [], [], 
                '''                This table contains the additional CDP configuration on
                the device's interfaces.
                ''',
                'cdpinterfaceexttable',
                'CISCO-CDP-MIB', False),
            _MetaInfoClassMember('cdpInterfaceTable', REFERENCE_CLASS, 'CdpInterfaceTable' , 'ydk.models.cdp.CISCO_CDP_MIB', 'CISCOCDPMIB.CdpInterfaceTable', 
                [], [], 
                '''                The (conceptual) table containing the status of CDP on
                the device's interfaces.
                ''',
                'cdpinterfacetable',
                'CISCO-CDP-MIB', False),
            ],
            'CISCO-CDP-MIB',
            'CISCO-CDP-MIB',
            _yang_ns._namespaces['CISCO-CDP-MIB'],
        'ydk.models.cdp.CISCO_CDP_MIB'
        ),
    },
}
_meta_table['CISCOCDPMIB.CdpCacheTable.CdpCacheEntry']['meta_info'].parent =_meta_table['CISCOCDPMIB.CdpCacheTable']['meta_info']
_meta_table['CISCOCDPMIB.CdpCtAddressTable.CdpCtAddressEntry']['meta_info'].parent =_meta_table['CISCOCDPMIB.CdpCtAddressTable']['meta_info']
_meta_table['CISCOCDPMIB.CdpInterfaceExtTable.CdpInterfaceExtEntry']['meta_info'].parent =_meta_table['CISCOCDPMIB.CdpInterfaceExtTable']['meta_info']
_meta_table['CISCOCDPMIB.CdpInterfaceTable.CdpInterfaceEntry']['meta_info'].parent =_meta_table['CISCOCDPMIB.CdpInterfaceTable']['meta_info']
_meta_table['CISCOCDPMIB.CdpCacheTable']['meta_info'].parent =_meta_table['CISCOCDPMIB']['meta_info']
_meta_table['CISCOCDPMIB.CdpCtAddressTable']['meta_info'].parent =_meta_table['CISCOCDPMIB']['meta_info']
_meta_table['CISCOCDPMIB.CdpGlobal']['meta_info'].parent =_meta_table['CISCOCDPMIB']['meta_info']
_meta_table['CISCOCDPMIB.CdpInterfaceExtTable']['meta_info'].parent =_meta_table['CISCOCDPMIB']['meta_info']
_meta_table['CISCOCDPMIB.CdpInterfaceTable']['meta_info'].parent =_meta_table['CISCOCDPMIB']['meta_info']
