


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'Lldp.TlvSelect.SystemName' : {
        'meta_info' : _MetaInfoClass('Lldp.TlvSelect.SystemName',
            False, 
            [
            _MetaInfoClassMember('disable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                disable System Name TLV
                ''',
                'disable',
                'Cisco-IOS-XR-ethernet-lldp-cfg', False),
            ],
            'Cisco-IOS-XR-ethernet-lldp-cfg',
            'system-name',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-lldp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_cfg'
        ),
    },
    'Lldp.TlvSelect.PortDescription' : {
        'meta_info' : _MetaInfoClass('Lldp.TlvSelect.PortDescription',
            False, 
            [
            _MetaInfoClassMember('disable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                disable Port Description TLV
                ''',
                'disable',
                'Cisco-IOS-XR-ethernet-lldp-cfg', False),
            ],
            'Cisco-IOS-XR-ethernet-lldp-cfg',
            'port-description',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-lldp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_cfg'
        ),
    },
    'Lldp.TlvSelect.SystemDescription' : {
        'meta_info' : _MetaInfoClass('Lldp.TlvSelect.SystemDescription',
            False, 
            [
            _MetaInfoClassMember('disable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                disable System Description TLV
                ''',
                'disable',
                'Cisco-IOS-XR-ethernet-lldp-cfg', False),
            ],
            'Cisco-IOS-XR-ethernet-lldp-cfg',
            'system-description',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-lldp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_cfg'
        ),
    },
    'Lldp.TlvSelect.SystemCapabilities' : {
        'meta_info' : _MetaInfoClass('Lldp.TlvSelect.SystemCapabilities',
            False, 
            [
            _MetaInfoClassMember('disable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                disable System Capabilities TLV
                ''',
                'disable',
                'Cisco-IOS-XR-ethernet-lldp-cfg', False),
            ],
            'Cisco-IOS-XR-ethernet-lldp-cfg',
            'system-capabilities',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-lldp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_cfg'
        ),
    },
    'Lldp.TlvSelect.ManagementAddress' : {
        'meta_info' : _MetaInfoClass('Lldp.TlvSelect.ManagementAddress',
            False, 
            [
            _MetaInfoClassMember('disable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                disable Management Address TLV
                ''',
                'disable',
                'Cisco-IOS-XR-ethernet-lldp-cfg', False),
            ],
            'Cisco-IOS-XR-ethernet-lldp-cfg',
            'management-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-lldp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_cfg'
        ),
    },
    'Lldp.TlvSelect' : {
        'meta_info' : _MetaInfoClass('Lldp.TlvSelect',
            False, 
            [
            _MetaInfoClassMember('management-address', REFERENCE_CLASS, 'ManagementAddress' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_cfg', 'Lldp.TlvSelect.ManagementAddress', 
                [], [], 
                '''                Management Address TLV
                ''',
                'management_address',
                'Cisco-IOS-XR-ethernet-lldp-cfg', False),
            _MetaInfoClassMember('port-description', REFERENCE_CLASS, 'PortDescription' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_cfg', 'Lldp.TlvSelect.PortDescription', 
                [], [], 
                '''                Port Description TLV
                ''',
                'port_description',
                'Cisco-IOS-XR-ethernet-lldp-cfg', False),
            _MetaInfoClassMember('system-capabilities', REFERENCE_CLASS, 'SystemCapabilities' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_cfg', 'Lldp.TlvSelect.SystemCapabilities', 
                [], [], 
                '''                System Capabilities TLV
                ''',
                'system_capabilities',
                'Cisco-IOS-XR-ethernet-lldp-cfg', False),
            _MetaInfoClassMember('system-description', REFERENCE_CLASS, 'SystemDescription' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_cfg', 'Lldp.TlvSelect.SystemDescription', 
                [], [], 
                '''                System Description TLV
                ''',
                'system_description',
                'Cisco-IOS-XR-ethernet-lldp-cfg', False),
            _MetaInfoClassMember('system-name', REFERENCE_CLASS, 'SystemName' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_cfg', 'Lldp.TlvSelect.SystemName', 
                [], [], 
                '''                System Name TLV
                ''',
                'system_name',
                'Cisco-IOS-XR-ethernet-lldp-cfg', False),
            _MetaInfoClassMember('tlv-select-enter', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                enter lldp tlv-select submode
                ''',
                'tlv_select_enter',
                'Cisco-IOS-XR-ethernet-lldp-cfg', False),
            ],
            'Cisco-IOS-XR-ethernet-lldp-cfg',
            'tlv-select',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-lldp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_cfg'
        ),
    },
    'Lldp' : {
        'meta_info' : _MetaInfoClass('Lldp',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable or disable LLDP globally
                ''',
                'enable',
                'Cisco-IOS-XR-ethernet-lldp-cfg', False),
            _MetaInfoClassMember('enable-subintf', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable or disable LLDP on Sub-interfaces as well
                globally
                ''',
                'enable_subintf',
                'Cisco-IOS-XR-ethernet-lldp-cfg', False),
            _MetaInfoClassMember('extended-show-width', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable or disable LLDP Show LLDP Neighbor
                Extended Width
                ''',
                'extended_show_width',
                'Cisco-IOS-XR-ethernet-lldp-cfg', False),
            _MetaInfoClassMember('holdtime', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Length  of time  (in sec) that receiver must
                keep this packet
                ''',
                'holdtime',
                'Cisco-IOS-XR-ethernet-lldp-cfg', False),
            _MetaInfoClassMember('reinit', ATTRIBUTE, 'int' , None, None, 
                [('2', '5')], [], 
                '''                Delay (in sec) for LLDP initialization on any
                interface
                ''',
                'reinit',
                'Cisco-IOS-XR-ethernet-lldp-cfg', False),
            _MetaInfoClassMember('timer', ATTRIBUTE, 'int' , None, None, 
                [('5', '65534')], [], 
                '''                Specify the rate at which LLDP packets are sent
                (in sec)
                ''',
                'timer',
                'Cisco-IOS-XR-ethernet-lldp-cfg', False),
            _MetaInfoClassMember('tlv-select', REFERENCE_CLASS, 'TlvSelect' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_cfg', 'Lldp.TlvSelect', 
                [], [], 
                '''                Selection of LLDP TLVs to disable
                ''',
                'tlv_select',
                'Cisco-IOS-XR-ethernet-lldp-cfg', False),
            ],
            'Cisco-IOS-XR-ethernet-lldp-cfg',
            'lldp',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-lldp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_cfg'
        ),
    },
}
_meta_table['Lldp.TlvSelect.SystemName']['meta_info'].parent =_meta_table['Lldp.TlvSelect']['meta_info']
_meta_table['Lldp.TlvSelect.PortDescription']['meta_info'].parent =_meta_table['Lldp.TlvSelect']['meta_info']
_meta_table['Lldp.TlvSelect.SystemDescription']['meta_info'].parent =_meta_table['Lldp.TlvSelect']['meta_info']
_meta_table['Lldp.TlvSelect.SystemCapabilities']['meta_info'].parent =_meta_table['Lldp.TlvSelect']['meta_info']
_meta_table['Lldp.TlvSelect.ManagementAddress']['meta_info'].parent =_meta_table['Lldp.TlvSelect']['meta_info']
_meta_table['Lldp.TlvSelect']['meta_info'].parent =_meta_table['Lldp']['meta_info']
