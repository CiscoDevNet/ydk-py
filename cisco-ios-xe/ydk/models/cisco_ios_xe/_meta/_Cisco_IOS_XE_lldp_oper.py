


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'LldpEntries.LldpEntry.Capabilities' : {
        'meta_info' : _MetaInfoClass('LldpEntries.LldpEntry.Capabilities',
            False, 
            [
            _MetaInfoClassMember('access-point', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                ''',
                'access_point',
                'Cisco-IOS-XE-lldp-oper', False),
            _MetaInfoClassMember('bridge', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                ''',
                'bridge',
                'Cisco-IOS-XE-lldp-oper', False),
            _MetaInfoClassMember('docsis', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                ''',
                'docsis',
                'Cisco-IOS-XE-lldp-oper', False),
            _MetaInfoClassMember('other', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                ''',
                'other',
                'Cisco-IOS-XE-lldp-oper', False),
            _MetaInfoClassMember('repeater', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                ''',
                'repeater',
                'Cisco-IOS-XE-lldp-oper', False),
            _MetaInfoClassMember('router', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                ''',
                'router',
                'Cisco-IOS-XE-lldp-oper', False),
            _MetaInfoClassMember('station', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                ''',
                'station',
                'Cisco-IOS-XE-lldp-oper', False),
            _MetaInfoClassMember('telephone', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                ''',
                'telephone',
                'Cisco-IOS-XE-lldp-oper', False),
            ],
            'Cisco-IOS-XE-lldp-oper',
            'capabilities',
            _yang_ns._namespaces['Cisco-IOS-XE-lldp-oper'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_lldp_oper'
        ),
    },
    'LldpEntries.LldpEntry' : {
        'meta_info' : _MetaInfoClass('LldpEntries.LldpEntry',
            False, 
            [
            _MetaInfoClassMember('device-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The device ID of the link.
                ''',
                'device_id',
                'Cisco-IOS-XE-lldp-oper', True),
            _MetaInfoClassMember('local-interface', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The name of the local interface on the current device.
                ''',
                'local_interface',
                'Cisco-IOS-XE-lldp-oper', True),
            _MetaInfoClassMember('connecting-interface', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The name of the connected interface to 'local-interface'.
                ''',
                'connecting_interface',
                'Cisco-IOS-XE-lldp-oper', True),
            _MetaInfoClassMember('capabilities', REFERENCE_CLASS, 'Capabilities' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_lldp_oper', 'LldpEntries.LldpEntry.Capabilities', 
                [], [], 
                '''                ''',
                'capabilities',
                'Cisco-IOS-XE-lldp-oper', False),
            _MetaInfoClassMember('ttl', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                TTL denoting hold-time of this link entry.
                ''',
                'ttl',
                'Cisco-IOS-XE-lldp-oper', False),
            ],
            'Cisco-IOS-XE-lldp-oper',
            'lldp-entry',
            _yang_ns._namespaces['Cisco-IOS-XE-lldp-oper'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_lldp_oper'
        ),
    },
    'LldpEntries' : {
        'meta_info' : _MetaInfoClass('LldpEntries',
            False, 
            [
            _MetaInfoClassMember('lldp-entry', REFERENCE_LIST, 'LldpEntry' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_lldp_oper', 'LldpEntries.LldpEntry', 
                [], [], 
                '''                The list of LLDP entries.
                ''',
                'lldp_entry',
                'Cisco-IOS-XE-lldp-oper', False),
            ],
            'Cisco-IOS-XE-lldp-oper',
            'lldp-entries',
            _yang_ns._namespaces['Cisco-IOS-XE-lldp-oper'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_lldp_oper'
        ),
    },
}
_meta_table['LldpEntries.LldpEntry.Capabilities']['meta_info'].parent =_meta_table['LldpEntries.LldpEntry']['meta_info']
_meta_table['LldpEntries.LldpEntry']['meta_info'].parent =_meta_table['LldpEntries']['meta_info']
