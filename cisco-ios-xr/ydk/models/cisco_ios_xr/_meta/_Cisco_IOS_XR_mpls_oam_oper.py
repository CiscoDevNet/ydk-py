


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'LspvBagInterfaceStateEnum' : _MetaInfoEnum('LspvBagInterfaceStateEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper',
        {
            'not-ready':'not_ready',
            'admin-down':'admin_down',
            'down':'down',
            'up':'up',
            'shutdown':'shutdown',
            'error-disable':'error_disable',
            'down-immediate':'down_immediate',
            'admin-immediate':'admin_immediate',
            'graceful-down':'graceful_down',
            'begin-shutdown':'begin_shutdown',
            'end-shutdown':'end_shutdown',
            'begin-error-disable':'begin_error_disable',
            'end-error-disable':'end_error_disable',
            'begin-graceful-down':'begin_graceful_down',
            'reset':'reset',
            'operational':'operational',
            'not-operational':'not_operational',
            'not-known':'not_known',
        }, 'Cisco-IOS-XR-mpls-oam-oper', _yang_ns._namespaces['Cisco-IOS-XR-mpls-oam-oper']),
    'MplsOam.Interface.Briefs.Brief' : {
        'meta_info' : _MetaInfoClass('MplsOam.Interface.Briefs.Brief',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface name
                ''',
                'interface_name',
                'Cisco-IOS-XR-mpls-oam-oper', True),
            _MetaInfoClassMember('interface-name-xr', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface name
                ''',
                'interface_name_xr',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            _MetaInfoClassMember('mtu', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Interface MTU
                ''',
                'mtu',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            _MetaInfoClassMember('prefix-length', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Prefix length (IPv4)
                ''',
                'prefix_length',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            _MetaInfoClassMember('prefix-length-v6', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Prefix length (IPv6)
                ''',
                'prefix_length_v6',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            _MetaInfoClassMember('primary-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Primary interface address (IPv4)
                ''',
                'primary_address',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            _MetaInfoClassMember('primary-address-v6', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                Primary interface address (IPv6)
                ''',
                'primary_address_v6',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            _MetaInfoClassMember('state', REFERENCE_ENUM_CLASS, 'LspvBagInterfaceStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper', 'LspvBagInterfaceStateEnum', 
                [], [], 
                '''                Interface state
                ''',
                'state',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            ],
            'Cisco-IOS-XR-mpls-oam-oper',
            'brief',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-oam-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper'
        ),
    },
    'MplsOam.Interface.Briefs' : {
        'meta_info' : _MetaInfoClass('MplsOam.Interface.Briefs',
            False, 
            [
            _MetaInfoClassMember('brief', REFERENCE_LIST, 'Brief' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper', 'MplsOam.Interface.Briefs.Brief', 
                [], [], 
                '''                MPLS OAM interface operational data
                ''',
                'brief',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            ],
            'Cisco-IOS-XR-mpls-oam-oper',
            'briefs',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-oam-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper'
        ),
    },
    'MplsOam.Interface.Details.Detail.InterfaceBrief' : {
        'meta_info' : _MetaInfoClass('MplsOam.Interface.Details.Detail.InterfaceBrief',
            False, 
            [
            _MetaInfoClassMember('interface-name-xr', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface name
                ''',
                'interface_name_xr',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            _MetaInfoClassMember('mtu', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Interface MTU
                ''',
                'mtu',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            _MetaInfoClassMember('prefix-length', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Prefix length (IPv4)
                ''',
                'prefix_length',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            _MetaInfoClassMember('prefix-length-v6', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Prefix length (IPv6)
                ''',
                'prefix_length_v6',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            _MetaInfoClassMember('primary-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Primary interface address (IPv4)
                ''',
                'primary_address',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            _MetaInfoClassMember('primary-address-v6', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                Primary interface address (IPv6)
                ''',
                'primary_address_v6',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            _MetaInfoClassMember('state', REFERENCE_ENUM_CLASS, 'LspvBagInterfaceStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper', 'LspvBagInterfaceStateEnum', 
                [], [], 
                '''                Interface state
                ''',
                'state',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            ],
            'Cisco-IOS-XR-mpls-oam-oper',
            'interface-brief',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-oam-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper'
        ),
    },
    'MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedGoodRequest' : {
        'meta_info' : _MetaInfoClass('MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedGoodRequest',
            False, 
            [
            _MetaInfoClassMember('bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Byte counter
                ''',
                'bytes',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            _MetaInfoClassMember('packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Packet counter
                ''',
                'packets',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            ],
            'Cisco-IOS-XR-mpls-oam-oper',
            'received-good-request',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-oam-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper'
        ),
    },
    'MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedGoodReply' : {
        'meta_info' : _MetaInfoClass('MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedGoodReply',
            False, 
            [
            _MetaInfoClassMember('bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Byte counter
                ''',
                'bytes',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            _MetaInfoClassMember('packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Packet counter
                ''',
                'packets',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            ],
            'Cisco-IOS-XR-mpls-oam-oper',
            'received-good-reply',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-oam-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper'
        ),
    },
    'MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedUnknown' : {
        'meta_info' : _MetaInfoClass('MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedUnknown',
            False, 
            [
            _MetaInfoClassMember('bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Byte counter
                ''',
                'bytes',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            _MetaInfoClassMember('packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Packet counter
                ''',
                'packets',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            ],
            'Cisco-IOS-XR-mpls-oam-oper',
            'received-unknown',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-oam-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper'
        ),
    },
    'MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedErrorIpHeader' : {
        'meta_info' : _MetaInfoClass('MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedErrorIpHeader',
            False, 
            [
            _MetaInfoClassMember('bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Byte counter
                ''',
                'bytes',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            _MetaInfoClassMember('packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Packet counter
                ''',
                'packets',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            ],
            'Cisco-IOS-XR-mpls-oam-oper',
            'received-error-ip-header',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-oam-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper'
        ),
    },
    'MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedErrorUdpHeader' : {
        'meta_info' : _MetaInfoClass('MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedErrorUdpHeader',
            False, 
            [
            _MetaInfoClassMember('bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Byte counter
                ''',
                'bytes',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            _MetaInfoClassMember('packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Packet counter
                ''',
                'packets',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            ],
            'Cisco-IOS-XR-mpls-oam-oper',
            'received-error-udp-header',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-oam-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper'
        ),
    },
    'MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedErrorRunt' : {
        'meta_info' : _MetaInfoClass('MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedErrorRunt',
            False, 
            [
            _MetaInfoClassMember('bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Byte counter
                ''',
                'bytes',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            _MetaInfoClassMember('packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Packet counter
                ''',
                'packets',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            ],
            'Cisco-IOS-XR-mpls-oam-oper',
            'received-error-runt',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-oam-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper'
        ),
    },
    'MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedErrorQueueFull' : {
        'meta_info' : _MetaInfoClass('MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedErrorQueueFull',
            False, 
            [
            _MetaInfoClassMember('bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Byte counter
                ''',
                'bytes',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            _MetaInfoClassMember('packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Packet counter
                ''',
                'packets',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            ],
            'Cisco-IOS-XR-mpls-oam-oper',
            'received-error-queue-full',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-oam-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper'
        ),
    },
    'MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedErrorGeneral' : {
        'meta_info' : _MetaInfoClass('MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedErrorGeneral',
            False, 
            [
            _MetaInfoClassMember('bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Byte counter
                ''',
                'bytes',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            _MetaInfoClassMember('packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Packet counter
                ''',
                'packets',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            ],
            'Cisco-IOS-XR-mpls-oam-oper',
            'received-error-general',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-oam-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper'
        ),
    },
    'MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedErrorNoInterface' : {
        'meta_info' : _MetaInfoClass('MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedErrorNoInterface',
            False, 
            [
            _MetaInfoClassMember('bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Byte counter
                ''',
                'bytes',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            _MetaInfoClassMember('packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Packet counter
                ''',
                'packets',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            ],
            'Cisco-IOS-XR-mpls-oam-oper',
            'received-error-no-interface',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-oam-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper'
        ),
    },
    'MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedErrorNoMemory' : {
        'meta_info' : _MetaInfoClass('MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedErrorNoMemory',
            False, 
            [
            _MetaInfoClassMember('bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Byte counter
                ''',
                'bytes',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            _MetaInfoClassMember('packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Packet counter
                ''',
                'packets',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            ],
            'Cisco-IOS-XR-mpls-oam-oper',
            'received-error-no-memory',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-oam-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper'
        ),
    },
    'MplsOam.Interface.Details.Detail.PacketStatistics.Received.ProtectProtocolReceivedGoodRequest' : {
        'meta_info' : _MetaInfoClass('MplsOam.Interface.Details.Detail.PacketStatistics.Received.ProtectProtocolReceivedGoodRequest',
            False, 
            [
            _MetaInfoClassMember('bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Byte counter
                ''',
                'bytes',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            _MetaInfoClassMember('packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Packet counter
                ''',
                'packets',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            ],
            'Cisco-IOS-XR-mpls-oam-oper',
            'protect-protocol-received-good-request',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-oam-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper'
        ),
    },
    'MplsOam.Interface.Details.Detail.PacketStatistics.Received.ProtectProtocolReceivedGoodReply' : {
        'meta_info' : _MetaInfoClass('MplsOam.Interface.Details.Detail.PacketStatistics.Received.ProtectProtocolReceivedGoodReply',
            False, 
            [
            _MetaInfoClassMember('bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Byte counter
                ''',
                'bytes',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            _MetaInfoClassMember('packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Packet counter
                ''',
                'packets',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            ],
            'Cisco-IOS-XR-mpls-oam-oper',
            'protect-protocol-received-good-reply',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-oam-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper'
        ),
    },
    'MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedGoodBfdRequest' : {
        'meta_info' : _MetaInfoClass('MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedGoodBfdRequest',
            False, 
            [
            _MetaInfoClassMember('bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Byte counter
                ''',
                'bytes',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            _MetaInfoClassMember('packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Packet counter
                ''',
                'packets',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            ],
            'Cisco-IOS-XR-mpls-oam-oper',
            'received-good-bfd-request',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-oam-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper'
        ),
    },
    'MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedGoodBfdReply' : {
        'meta_info' : _MetaInfoClass('MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedGoodBfdReply',
            False, 
            [
            _MetaInfoClassMember('bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Byte counter
                ''',
                'bytes',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            _MetaInfoClassMember('packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Packet counter
                ''',
                'packets',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            ],
            'Cisco-IOS-XR-mpls-oam-oper',
            'received-good-bfd-reply',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-oam-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper'
        ),
    },
    'MplsOam.Interface.Details.Detail.PacketStatistics.Received' : {
        'meta_info' : _MetaInfoClass('MplsOam.Interface.Details.Detail.PacketStatistics.Received',
            False, 
            [
            _MetaInfoClassMember('protect-protocol-received-good-reply', REFERENCE_CLASS, 'ProtectProtocolReceivedGoodReply' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper', 'MplsOam.Interface.Details.Detail.PacketStatistics.Received.ProtectProtocolReceivedGoodReply', 
                [], [], 
                '''                Protect Protocol Received good reply
                ''',
                'protect_protocol_received_good_reply',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            _MetaInfoClassMember('protect-protocol-received-good-request', REFERENCE_CLASS, 'ProtectProtocolReceivedGoodRequest' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper', 'MplsOam.Interface.Details.Detail.PacketStatistics.Received.ProtectProtocolReceivedGoodRequest', 
                [], [], 
                '''                Protect Protocol Received good request
                ''',
                'protect_protocol_received_good_request',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            _MetaInfoClassMember('received-error-general', REFERENCE_CLASS, 'ReceivedErrorGeneral' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper', 'MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedErrorGeneral', 
                [], [], 
                '''                General error
                ''',
                'received_error_general',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            _MetaInfoClassMember('received-error-ip-header', REFERENCE_CLASS, 'ReceivedErrorIpHeader' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper', 'MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedErrorIpHeader', 
                [], [], 
                '''                IP header error
                ''',
                'received_error_ip_header',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            _MetaInfoClassMember('received-error-no-interface', REFERENCE_CLASS, 'ReceivedErrorNoInterface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper', 'MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedErrorNoInterface', 
                [], [], 
                '''                Error no Interfaces
                ''',
                'received_error_no_interface',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            _MetaInfoClassMember('received-error-no-memory', REFERENCE_CLASS, 'ReceivedErrorNoMemory' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper', 'MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedErrorNoMemory', 
                [], [], 
                '''                Error no memory
                ''',
                'received_error_no_memory',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            _MetaInfoClassMember('received-error-queue-full', REFERENCE_CLASS, 'ReceivedErrorQueueFull' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper', 'MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedErrorQueueFull', 
                [], [], 
                '''                Dropped queue full
                ''',
                'received_error_queue_full',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            _MetaInfoClassMember('received-error-runt', REFERENCE_CLASS, 'ReceivedErrorRunt' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper', 'MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedErrorRunt', 
                [], [], 
                '''                RUNT error
                ''',
                'received_error_runt',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            _MetaInfoClassMember('received-error-udp-header', REFERENCE_CLASS, 'ReceivedErrorUdpHeader' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper', 'MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedErrorUdpHeader', 
                [], [], 
                '''                UDP header error
                ''',
                'received_error_udp_header',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            _MetaInfoClassMember('received-good-bfd-reply', REFERENCE_CLASS, 'ReceivedGoodBfdReply' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper', 'MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedGoodBfdReply', 
                [], [], 
                '''                Received Reply with BFD TLV
                ''',
                'received_good_bfd_reply',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            _MetaInfoClassMember('received-good-bfd-request', REFERENCE_CLASS, 'ReceivedGoodBfdRequest' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper', 'MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedGoodBfdRequest', 
                [], [], 
                '''                Received Reqeust with BFD TLV
                ''',
                'received_good_bfd_request',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            _MetaInfoClassMember('received-good-reply', REFERENCE_CLASS, 'ReceivedGoodReply' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper', 'MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedGoodReply', 
                [], [], 
                '''                Received good reply
                ''',
                'received_good_reply',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            _MetaInfoClassMember('received-good-request', REFERENCE_CLASS, 'ReceivedGoodRequest' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper', 'MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedGoodRequest', 
                [], [], 
                '''                Received good request
                ''',
                'received_good_request',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            _MetaInfoClassMember('received-unknown', REFERENCE_CLASS, 'ReceivedUnknown' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper', 'MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedUnknown', 
                [], [], 
                '''                Received unknown packets
                ''',
                'received_unknown',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            ],
            'Cisco-IOS-XR-mpls-oam-oper',
            'received',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-oam-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper'
        ),
    },
    'MplsOam.Interface.Details.Detail.PacketStatistics.Sent.TransmitGood' : {
        'meta_info' : _MetaInfoClass('MplsOam.Interface.Details.Detail.PacketStatistics.Sent.TransmitGood',
            False, 
            [
            _MetaInfoClassMember('bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Byte counter
                ''',
                'bytes',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            _MetaInfoClassMember('packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Packet counter
                ''',
                'packets',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            ],
            'Cisco-IOS-XR-mpls-oam-oper',
            'transmit-good',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-oam-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper'
        ),
    },
    'MplsOam.Interface.Details.Detail.PacketStatistics.Sent.TransmitDrop' : {
        'meta_info' : _MetaInfoClass('MplsOam.Interface.Details.Detail.PacketStatistics.Sent.TransmitDrop',
            False, 
            [
            _MetaInfoClassMember('bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Byte counter
                ''',
                'bytes',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            _MetaInfoClassMember('packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Packet counter
                ''',
                'packets',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            ],
            'Cisco-IOS-XR-mpls-oam-oper',
            'transmit-drop',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-oam-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper'
        ),
    },
    'MplsOam.Interface.Details.Detail.PacketStatistics.Sent.TransmitBfdGood' : {
        'meta_info' : _MetaInfoClass('MplsOam.Interface.Details.Detail.PacketStatistics.Sent.TransmitBfdGood',
            False, 
            [
            _MetaInfoClassMember('bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Byte counter
                ''',
                'bytes',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            _MetaInfoClassMember('packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Packet counter
                ''',
                'packets',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            ],
            'Cisco-IOS-XR-mpls-oam-oper',
            'transmit-bfd-good',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-oam-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper'
        ),
    },
    'MplsOam.Interface.Details.Detail.PacketStatistics.Sent.BfdNoReply' : {
        'meta_info' : _MetaInfoClass('MplsOam.Interface.Details.Detail.PacketStatistics.Sent.BfdNoReply',
            False, 
            [
            _MetaInfoClassMember('bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Byte counter
                ''',
                'bytes',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            _MetaInfoClassMember('packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Packet counter
                ''',
                'packets',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            ],
            'Cisco-IOS-XR-mpls-oam-oper',
            'bfd-no-reply',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-oam-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper'
        ),
    },
    'MplsOam.Interface.Details.Detail.PacketStatistics.Sent' : {
        'meta_info' : _MetaInfoClass('MplsOam.Interface.Details.Detail.PacketStatistics.Sent',
            False, 
            [
            _MetaInfoClassMember('bfd-no-reply', REFERENCE_CLASS, 'BfdNoReply' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper', 'MplsOam.Interface.Details.Detail.PacketStatistics.Sent.BfdNoReply', 
                [], [], 
                '''                No Reply action for echo reqeust of BFD
                bootstrap
                ''',
                'bfd_no_reply',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            _MetaInfoClassMember('transmit-bfd-good', REFERENCE_CLASS, 'TransmitBfdGood' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper', 'MplsOam.Interface.Details.Detail.PacketStatistics.Sent.TransmitBfdGood', 
                [], [], 
                '''                Transmit good BFD request packets
                ''',
                'transmit_bfd_good',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            _MetaInfoClassMember('transmit-drop', REFERENCE_CLASS, 'TransmitDrop' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper', 'MplsOam.Interface.Details.Detail.PacketStatistics.Sent.TransmitDrop', 
                [], [], 
                '''                Transmit drop packets
                ''',
                'transmit_drop',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            _MetaInfoClassMember('transmit-good', REFERENCE_CLASS, 'TransmitGood' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper', 'MplsOam.Interface.Details.Detail.PacketStatistics.Sent.TransmitGood', 
                [], [], 
                '''                Transmit good packets
                ''',
                'transmit_good',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            ],
            'Cisco-IOS-XR-mpls-oam-oper',
            'sent',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-oam-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper'
        ),
    },
    'MplsOam.Interface.Details.Detail.PacketStatistics.WorkingReqSent.TransmitGood' : {
        'meta_info' : _MetaInfoClass('MplsOam.Interface.Details.Detail.PacketStatistics.WorkingReqSent.TransmitGood',
            False, 
            [
            _MetaInfoClassMember('bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Byte counter
                ''',
                'bytes',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            _MetaInfoClassMember('packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Packet counter
                ''',
                'packets',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            ],
            'Cisco-IOS-XR-mpls-oam-oper',
            'transmit-good',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-oam-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper'
        ),
    },
    'MplsOam.Interface.Details.Detail.PacketStatistics.WorkingReqSent.TransmitDrop' : {
        'meta_info' : _MetaInfoClass('MplsOam.Interface.Details.Detail.PacketStatistics.WorkingReqSent.TransmitDrop',
            False, 
            [
            _MetaInfoClassMember('bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Byte counter
                ''',
                'bytes',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            _MetaInfoClassMember('packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Packet counter
                ''',
                'packets',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            ],
            'Cisco-IOS-XR-mpls-oam-oper',
            'transmit-drop',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-oam-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper'
        ),
    },
    'MplsOam.Interface.Details.Detail.PacketStatistics.WorkingReqSent.TransmitBfdGood' : {
        'meta_info' : _MetaInfoClass('MplsOam.Interface.Details.Detail.PacketStatistics.WorkingReqSent.TransmitBfdGood',
            False, 
            [
            _MetaInfoClassMember('bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Byte counter
                ''',
                'bytes',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            _MetaInfoClassMember('packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Packet counter
                ''',
                'packets',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            ],
            'Cisco-IOS-XR-mpls-oam-oper',
            'transmit-bfd-good',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-oam-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper'
        ),
    },
    'MplsOam.Interface.Details.Detail.PacketStatistics.WorkingReqSent.BfdNoReply' : {
        'meta_info' : _MetaInfoClass('MplsOam.Interface.Details.Detail.PacketStatistics.WorkingReqSent.BfdNoReply',
            False, 
            [
            _MetaInfoClassMember('bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Byte counter
                ''',
                'bytes',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            _MetaInfoClassMember('packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Packet counter
                ''',
                'packets',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            ],
            'Cisco-IOS-XR-mpls-oam-oper',
            'bfd-no-reply',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-oam-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper'
        ),
    },
    'MplsOam.Interface.Details.Detail.PacketStatistics.WorkingReqSent' : {
        'meta_info' : _MetaInfoClass('MplsOam.Interface.Details.Detail.PacketStatistics.WorkingReqSent',
            False, 
            [
            _MetaInfoClassMember('bfd-no-reply', REFERENCE_CLASS, 'BfdNoReply' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper', 'MplsOam.Interface.Details.Detail.PacketStatistics.WorkingReqSent.BfdNoReply', 
                [], [], 
                '''                No Reply action for echo reqeust of BFD
                bootstrap
                ''',
                'bfd_no_reply',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            _MetaInfoClassMember('transmit-bfd-good', REFERENCE_CLASS, 'TransmitBfdGood' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper', 'MplsOam.Interface.Details.Detail.PacketStatistics.WorkingReqSent.TransmitBfdGood', 
                [], [], 
                '''                Transmit good BFD request packets
                ''',
                'transmit_bfd_good',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            _MetaInfoClassMember('transmit-drop', REFERENCE_CLASS, 'TransmitDrop' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper', 'MplsOam.Interface.Details.Detail.PacketStatistics.WorkingReqSent.TransmitDrop', 
                [], [], 
                '''                Transmit drop packets
                ''',
                'transmit_drop',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            _MetaInfoClassMember('transmit-good', REFERENCE_CLASS, 'TransmitGood' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper', 'MplsOam.Interface.Details.Detail.PacketStatistics.WorkingReqSent.TransmitGood', 
                [], [], 
                '''                Transmit good packets
                ''',
                'transmit_good',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            ],
            'Cisco-IOS-XR-mpls-oam-oper',
            'working-req-sent',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-oam-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper'
        ),
    },
    'MplsOam.Interface.Details.Detail.PacketStatistics.WorkingRepSent.TransmitGood' : {
        'meta_info' : _MetaInfoClass('MplsOam.Interface.Details.Detail.PacketStatistics.WorkingRepSent.TransmitGood',
            False, 
            [
            _MetaInfoClassMember('bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Byte counter
                ''',
                'bytes',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            _MetaInfoClassMember('packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Packet counter
                ''',
                'packets',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            ],
            'Cisco-IOS-XR-mpls-oam-oper',
            'transmit-good',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-oam-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper'
        ),
    },
    'MplsOam.Interface.Details.Detail.PacketStatistics.WorkingRepSent.TransmitDrop' : {
        'meta_info' : _MetaInfoClass('MplsOam.Interface.Details.Detail.PacketStatistics.WorkingRepSent.TransmitDrop',
            False, 
            [
            _MetaInfoClassMember('bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Byte counter
                ''',
                'bytes',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            _MetaInfoClassMember('packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Packet counter
                ''',
                'packets',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            ],
            'Cisco-IOS-XR-mpls-oam-oper',
            'transmit-drop',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-oam-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper'
        ),
    },
    'MplsOam.Interface.Details.Detail.PacketStatistics.WorkingRepSent.TransmitBfdGood' : {
        'meta_info' : _MetaInfoClass('MplsOam.Interface.Details.Detail.PacketStatistics.WorkingRepSent.TransmitBfdGood',
            False, 
            [
            _MetaInfoClassMember('bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Byte counter
                ''',
                'bytes',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            _MetaInfoClassMember('packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Packet counter
                ''',
                'packets',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            ],
            'Cisco-IOS-XR-mpls-oam-oper',
            'transmit-bfd-good',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-oam-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper'
        ),
    },
    'MplsOam.Interface.Details.Detail.PacketStatistics.WorkingRepSent.BfdNoReply' : {
        'meta_info' : _MetaInfoClass('MplsOam.Interface.Details.Detail.PacketStatistics.WorkingRepSent.BfdNoReply',
            False, 
            [
            _MetaInfoClassMember('bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Byte counter
                ''',
                'bytes',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            _MetaInfoClassMember('packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Packet counter
                ''',
                'packets',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            ],
            'Cisco-IOS-XR-mpls-oam-oper',
            'bfd-no-reply',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-oam-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper'
        ),
    },
    'MplsOam.Interface.Details.Detail.PacketStatistics.WorkingRepSent' : {
        'meta_info' : _MetaInfoClass('MplsOam.Interface.Details.Detail.PacketStatistics.WorkingRepSent',
            False, 
            [
            _MetaInfoClassMember('bfd-no-reply', REFERENCE_CLASS, 'BfdNoReply' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper', 'MplsOam.Interface.Details.Detail.PacketStatistics.WorkingRepSent.BfdNoReply', 
                [], [], 
                '''                No Reply action for echo reqeust of BFD
                bootstrap
                ''',
                'bfd_no_reply',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            _MetaInfoClassMember('transmit-bfd-good', REFERENCE_CLASS, 'TransmitBfdGood' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper', 'MplsOam.Interface.Details.Detail.PacketStatistics.WorkingRepSent.TransmitBfdGood', 
                [], [], 
                '''                Transmit good BFD request packets
                ''',
                'transmit_bfd_good',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            _MetaInfoClassMember('transmit-drop', REFERENCE_CLASS, 'TransmitDrop' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper', 'MplsOam.Interface.Details.Detail.PacketStatistics.WorkingRepSent.TransmitDrop', 
                [], [], 
                '''                Transmit drop packets
                ''',
                'transmit_drop',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            _MetaInfoClassMember('transmit-good', REFERENCE_CLASS, 'TransmitGood' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper', 'MplsOam.Interface.Details.Detail.PacketStatistics.WorkingRepSent.TransmitGood', 
                [], [], 
                '''                Transmit good packets
                ''',
                'transmit_good',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            ],
            'Cisco-IOS-XR-mpls-oam-oper',
            'working-rep-sent',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-oam-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper'
        ),
    },
    'MplsOam.Interface.Details.Detail.PacketStatistics.ProtectReqSent.TransmitGood' : {
        'meta_info' : _MetaInfoClass('MplsOam.Interface.Details.Detail.PacketStatistics.ProtectReqSent.TransmitGood',
            False, 
            [
            _MetaInfoClassMember('bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Byte counter
                ''',
                'bytes',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            _MetaInfoClassMember('packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Packet counter
                ''',
                'packets',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            ],
            'Cisco-IOS-XR-mpls-oam-oper',
            'transmit-good',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-oam-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper'
        ),
    },
    'MplsOam.Interface.Details.Detail.PacketStatistics.ProtectReqSent.TransmitDrop' : {
        'meta_info' : _MetaInfoClass('MplsOam.Interface.Details.Detail.PacketStatistics.ProtectReqSent.TransmitDrop',
            False, 
            [
            _MetaInfoClassMember('bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Byte counter
                ''',
                'bytes',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            _MetaInfoClassMember('packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Packet counter
                ''',
                'packets',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            ],
            'Cisco-IOS-XR-mpls-oam-oper',
            'transmit-drop',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-oam-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper'
        ),
    },
    'MplsOam.Interface.Details.Detail.PacketStatistics.ProtectReqSent.TransmitBfdGood' : {
        'meta_info' : _MetaInfoClass('MplsOam.Interface.Details.Detail.PacketStatistics.ProtectReqSent.TransmitBfdGood',
            False, 
            [
            _MetaInfoClassMember('bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Byte counter
                ''',
                'bytes',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            _MetaInfoClassMember('packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Packet counter
                ''',
                'packets',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            ],
            'Cisco-IOS-XR-mpls-oam-oper',
            'transmit-bfd-good',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-oam-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper'
        ),
    },
    'MplsOam.Interface.Details.Detail.PacketStatistics.ProtectReqSent.BfdNoReply' : {
        'meta_info' : _MetaInfoClass('MplsOam.Interface.Details.Detail.PacketStatistics.ProtectReqSent.BfdNoReply',
            False, 
            [
            _MetaInfoClassMember('bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Byte counter
                ''',
                'bytes',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            _MetaInfoClassMember('packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Packet counter
                ''',
                'packets',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            ],
            'Cisco-IOS-XR-mpls-oam-oper',
            'bfd-no-reply',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-oam-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper'
        ),
    },
    'MplsOam.Interface.Details.Detail.PacketStatistics.ProtectReqSent' : {
        'meta_info' : _MetaInfoClass('MplsOam.Interface.Details.Detail.PacketStatistics.ProtectReqSent',
            False, 
            [
            _MetaInfoClassMember('bfd-no-reply', REFERENCE_CLASS, 'BfdNoReply' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper', 'MplsOam.Interface.Details.Detail.PacketStatistics.ProtectReqSent.BfdNoReply', 
                [], [], 
                '''                No Reply action for echo reqeust of BFD
                bootstrap
                ''',
                'bfd_no_reply',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            _MetaInfoClassMember('transmit-bfd-good', REFERENCE_CLASS, 'TransmitBfdGood' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper', 'MplsOam.Interface.Details.Detail.PacketStatistics.ProtectReqSent.TransmitBfdGood', 
                [], [], 
                '''                Transmit good BFD request packets
                ''',
                'transmit_bfd_good',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            _MetaInfoClassMember('transmit-drop', REFERENCE_CLASS, 'TransmitDrop' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper', 'MplsOam.Interface.Details.Detail.PacketStatistics.ProtectReqSent.TransmitDrop', 
                [], [], 
                '''                Transmit drop packets
                ''',
                'transmit_drop',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            _MetaInfoClassMember('transmit-good', REFERENCE_CLASS, 'TransmitGood' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper', 'MplsOam.Interface.Details.Detail.PacketStatistics.ProtectReqSent.TransmitGood', 
                [], [], 
                '''                Transmit good packets
                ''',
                'transmit_good',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            ],
            'Cisco-IOS-XR-mpls-oam-oper',
            'protect-req-sent',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-oam-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper'
        ),
    },
    'MplsOam.Interface.Details.Detail.PacketStatistics.ProtectRepSent.TransmitGood' : {
        'meta_info' : _MetaInfoClass('MplsOam.Interface.Details.Detail.PacketStatistics.ProtectRepSent.TransmitGood',
            False, 
            [
            _MetaInfoClassMember('bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Byte counter
                ''',
                'bytes',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            _MetaInfoClassMember('packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Packet counter
                ''',
                'packets',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            ],
            'Cisco-IOS-XR-mpls-oam-oper',
            'transmit-good',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-oam-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper'
        ),
    },
    'MplsOam.Interface.Details.Detail.PacketStatistics.ProtectRepSent.TransmitDrop' : {
        'meta_info' : _MetaInfoClass('MplsOam.Interface.Details.Detail.PacketStatistics.ProtectRepSent.TransmitDrop',
            False, 
            [
            _MetaInfoClassMember('bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Byte counter
                ''',
                'bytes',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            _MetaInfoClassMember('packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Packet counter
                ''',
                'packets',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            ],
            'Cisco-IOS-XR-mpls-oam-oper',
            'transmit-drop',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-oam-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper'
        ),
    },
    'MplsOam.Interface.Details.Detail.PacketStatistics.ProtectRepSent.TransmitBfdGood' : {
        'meta_info' : _MetaInfoClass('MplsOam.Interface.Details.Detail.PacketStatistics.ProtectRepSent.TransmitBfdGood',
            False, 
            [
            _MetaInfoClassMember('bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Byte counter
                ''',
                'bytes',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            _MetaInfoClassMember('packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Packet counter
                ''',
                'packets',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            ],
            'Cisco-IOS-XR-mpls-oam-oper',
            'transmit-bfd-good',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-oam-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper'
        ),
    },
    'MplsOam.Interface.Details.Detail.PacketStatistics.ProtectRepSent.BfdNoReply' : {
        'meta_info' : _MetaInfoClass('MplsOam.Interface.Details.Detail.PacketStatistics.ProtectRepSent.BfdNoReply',
            False, 
            [
            _MetaInfoClassMember('bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Byte counter
                ''',
                'bytes',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            _MetaInfoClassMember('packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Packet counter
                ''',
                'packets',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            ],
            'Cisco-IOS-XR-mpls-oam-oper',
            'bfd-no-reply',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-oam-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper'
        ),
    },
    'MplsOam.Interface.Details.Detail.PacketStatistics.ProtectRepSent' : {
        'meta_info' : _MetaInfoClass('MplsOam.Interface.Details.Detail.PacketStatistics.ProtectRepSent',
            False, 
            [
            _MetaInfoClassMember('bfd-no-reply', REFERENCE_CLASS, 'BfdNoReply' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper', 'MplsOam.Interface.Details.Detail.PacketStatistics.ProtectRepSent.BfdNoReply', 
                [], [], 
                '''                No Reply action for echo reqeust of BFD
                bootstrap
                ''',
                'bfd_no_reply',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            _MetaInfoClassMember('transmit-bfd-good', REFERENCE_CLASS, 'TransmitBfdGood' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper', 'MplsOam.Interface.Details.Detail.PacketStatistics.ProtectRepSent.TransmitBfdGood', 
                [], [], 
                '''                Transmit good BFD request packets
                ''',
                'transmit_bfd_good',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            _MetaInfoClassMember('transmit-drop', REFERENCE_CLASS, 'TransmitDrop' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper', 'MplsOam.Interface.Details.Detail.PacketStatistics.ProtectRepSent.TransmitDrop', 
                [], [], 
                '''                Transmit drop packets
                ''',
                'transmit_drop',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            _MetaInfoClassMember('transmit-good', REFERENCE_CLASS, 'TransmitGood' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper', 'MplsOam.Interface.Details.Detail.PacketStatistics.ProtectRepSent.TransmitGood', 
                [], [], 
                '''                Transmit good packets
                ''',
                'transmit_good',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            ],
            'Cisco-IOS-XR-mpls-oam-oper',
            'protect-rep-sent',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-oam-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper'
        ),
    },
    'MplsOam.Interface.Details.Detail.PacketStatistics' : {
        'meta_info' : _MetaInfoClass('MplsOam.Interface.Details.Detail.PacketStatistics',
            False, 
            [
            _MetaInfoClassMember('protect-rep-sent', REFERENCE_CLASS, 'ProtectRepSent' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper', 'MplsOam.Interface.Details.Detail.PacketStatistics.ProtectRepSent', 
                [], [], 
                '''                Protect Reply Packet transmit counts
                ''',
                'protect_rep_sent',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            _MetaInfoClassMember('protect-req-sent', REFERENCE_CLASS, 'ProtectReqSent' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper', 'MplsOam.Interface.Details.Detail.PacketStatistics.ProtectReqSent', 
                [], [], 
                '''                Protect Request Packet transmit counts
                ''',
                'protect_req_sent',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            _MetaInfoClassMember('received', REFERENCE_CLASS, 'Received' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper', 'MplsOam.Interface.Details.Detail.PacketStatistics.Received', 
                [], [], 
                '''                Packet reception counts
                ''',
                'received',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            _MetaInfoClassMember('sent', REFERENCE_CLASS, 'Sent' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper', 'MplsOam.Interface.Details.Detail.PacketStatistics.Sent', 
                [], [], 
                '''                Packet transmit counts
                ''',
                'sent',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            _MetaInfoClassMember('working-rep-sent', REFERENCE_CLASS, 'WorkingRepSent' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper', 'MplsOam.Interface.Details.Detail.PacketStatistics.WorkingRepSent', 
                [], [], 
                '''                Working Reply Packet transmit counts
                ''',
                'working_rep_sent',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            _MetaInfoClassMember('working-req-sent', REFERENCE_CLASS, 'WorkingReqSent' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper', 'MplsOam.Interface.Details.Detail.PacketStatistics.WorkingReqSent', 
                [], [], 
                '''                Working Request Packet transmit counts
                ''',
                'working_req_sent',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            ],
            'Cisco-IOS-XR-mpls-oam-oper',
            'packet-statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-oam-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper'
        ),
    },
    'MplsOam.Interface.Details.Detail' : {
        'meta_info' : _MetaInfoClass('MplsOam.Interface.Details.Detail',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface name
                ''',
                'interface_name',
                'Cisco-IOS-XR-mpls-oam-oper', True),
            _MetaInfoClassMember('interface-brief', REFERENCE_CLASS, 'InterfaceBrief' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper', 'MplsOam.Interface.Details.Detail.InterfaceBrief', 
                [], [], 
                '''                Interface brief
                ''',
                'interface_brief',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            _MetaInfoClassMember('packet-statistics', REFERENCE_CLASS, 'PacketStatistics' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper', 'MplsOam.Interface.Details.Detail.PacketStatistics', 
                [], [], 
                '''                Packet statistics
                ''',
                'packet_statistics',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            ],
            'Cisco-IOS-XR-mpls-oam-oper',
            'detail',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-oam-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper'
        ),
    },
    'MplsOam.Interface.Details' : {
        'meta_info' : _MetaInfoClass('MplsOam.Interface.Details',
            False, 
            [
            _MetaInfoClassMember('detail', REFERENCE_LIST, 'Detail' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper', 'MplsOam.Interface.Details.Detail', 
                [], [], 
                '''                MPLS OAM interface operational data
                ''',
                'detail',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            ],
            'Cisco-IOS-XR-mpls-oam-oper',
            'details',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-oam-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper'
        ),
    },
    'MplsOam.Interface' : {
        'meta_info' : _MetaInfoClass('MplsOam.Interface',
            False, 
            [
            _MetaInfoClassMember('briefs', REFERENCE_CLASS, 'Briefs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper', 'MplsOam.Interface.Briefs', 
                [], [], 
                '''                MPLS OAM interface detail data
                ''',
                'briefs',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            _MetaInfoClassMember('details', REFERENCE_CLASS, 'Details' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper', 'MplsOam.Interface.Details', 
                [], [], 
                '''                MPLS OAM interface detail data
                ''',
                'details',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            ],
            'Cisco-IOS-XR-mpls-oam-oper',
            'interface',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-oam-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper'
        ),
    },
    'MplsOam.Packet.Received.ReceivedGoodRequest' : {
        'meta_info' : _MetaInfoClass('MplsOam.Packet.Received.ReceivedGoodRequest',
            False, 
            [
            _MetaInfoClassMember('bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Byte counter
                ''',
                'bytes',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            _MetaInfoClassMember('packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Packet counter
                ''',
                'packets',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            ],
            'Cisco-IOS-XR-mpls-oam-oper',
            'received-good-request',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-oam-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper'
        ),
    },
    'MplsOam.Packet.Received.ReceivedGoodReply' : {
        'meta_info' : _MetaInfoClass('MplsOam.Packet.Received.ReceivedGoodReply',
            False, 
            [
            _MetaInfoClassMember('bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Byte counter
                ''',
                'bytes',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            _MetaInfoClassMember('packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Packet counter
                ''',
                'packets',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            ],
            'Cisco-IOS-XR-mpls-oam-oper',
            'received-good-reply',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-oam-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper'
        ),
    },
    'MplsOam.Packet.Received.ReceivedUnknown' : {
        'meta_info' : _MetaInfoClass('MplsOam.Packet.Received.ReceivedUnknown',
            False, 
            [
            _MetaInfoClassMember('bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Byte counter
                ''',
                'bytes',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            _MetaInfoClassMember('packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Packet counter
                ''',
                'packets',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            ],
            'Cisco-IOS-XR-mpls-oam-oper',
            'received-unknown',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-oam-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper'
        ),
    },
    'MplsOam.Packet.Received.ReceivedErrorIpHeader' : {
        'meta_info' : _MetaInfoClass('MplsOam.Packet.Received.ReceivedErrorIpHeader',
            False, 
            [
            _MetaInfoClassMember('bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Byte counter
                ''',
                'bytes',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            _MetaInfoClassMember('packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Packet counter
                ''',
                'packets',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            ],
            'Cisco-IOS-XR-mpls-oam-oper',
            'received-error-ip-header',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-oam-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper'
        ),
    },
    'MplsOam.Packet.Received.ReceivedErrorUdpHeader' : {
        'meta_info' : _MetaInfoClass('MplsOam.Packet.Received.ReceivedErrorUdpHeader',
            False, 
            [
            _MetaInfoClassMember('bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Byte counter
                ''',
                'bytes',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            _MetaInfoClassMember('packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Packet counter
                ''',
                'packets',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            ],
            'Cisco-IOS-XR-mpls-oam-oper',
            'received-error-udp-header',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-oam-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper'
        ),
    },
    'MplsOam.Packet.Received.ReceivedErrorRunt' : {
        'meta_info' : _MetaInfoClass('MplsOam.Packet.Received.ReceivedErrorRunt',
            False, 
            [
            _MetaInfoClassMember('bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Byte counter
                ''',
                'bytes',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            _MetaInfoClassMember('packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Packet counter
                ''',
                'packets',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            ],
            'Cisco-IOS-XR-mpls-oam-oper',
            'received-error-runt',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-oam-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper'
        ),
    },
    'MplsOam.Packet.Received.ReceivedErrorQueueFull' : {
        'meta_info' : _MetaInfoClass('MplsOam.Packet.Received.ReceivedErrorQueueFull',
            False, 
            [
            _MetaInfoClassMember('bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Byte counter
                ''',
                'bytes',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            _MetaInfoClassMember('packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Packet counter
                ''',
                'packets',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            ],
            'Cisco-IOS-XR-mpls-oam-oper',
            'received-error-queue-full',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-oam-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper'
        ),
    },
    'MplsOam.Packet.Received.ReceivedErrorGeneral' : {
        'meta_info' : _MetaInfoClass('MplsOam.Packet.Received.ReceivedErrorGeneral',
            False, 
            [
            _MetaInfoClassMember('bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Byte counter
                ''',
                'bytes',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            _MetaInfoClassMember('packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Packet counter
                ''',
                'packets',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            ],
            'Cisco-IOS-XR-mpls-oam-oper',
            'received-error-general',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-oam-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper'
        ),
    },
    'MplsOam.Packet.Received.ReceivedErrorNoInterface' : {
        'meta_info' : _MetaInfoClass('MplsOam.Packet.Received.ReceivedErrorNoInterface',
            False, 
            [
            _MetaInfoClassMember('bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Byte counter
                ''',
                'bytes',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            _MetaInfoClassMember('packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Packet counter
                ''',
                'packets',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            ],
            'Cisco-IOS-XR-mpls-oam-oper',
            'received-error-no-interface',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-oam-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper'
        ),
    },
    'MplsOam.Packet.Received.ReceivedErrorNoMemory' : {
        'meta_info' : _MetaInfoClass('MplsOam.Packet.Received.ReceivedErrorNoMemory',
            False, 
            [
            _MetaInfoClassMember('bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Byte counter
                ''',
                'bytes',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            _MetaInfoClassMember('packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Packet counter
                ''',
                'packets',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            ],
            'Cisco-IOS-XR-mpls-oam-oper',
            'received-error-no-memory',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-oam-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper'
        ),
    },
    'MplsOam.Packet.Received.ProtectProtocolReceivedGoodRequest' : {
        'meta_info' : _MetaInfoClass('MplsOam.Packet.Received.ProtectProtocolReceivedGoodRequest',
            False, 
            [
            _MetaInfoClassMember('bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Byte counter
                ''',
                'bytes',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            _MetaInfoClassMember('packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Packet counter
                ''',
                'packets',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            ],
            'Cisco-IOS-XR-mpls-oam-oper',
            'protect-protocol-received-good-request',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-oam-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper'
        ),
    },
    'MplsOam.Packet.Received.ProtectProtocolReceivedGoodReply' : {
        'meta_info' : _MetaInfoClass('MplsOam.Packet.Received.ProtectProtocolReceivedGoodReply',
            False, 
            [
            _MetaInfoClassMember('bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Byte counter
                ''',
                'bytes',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            _MetaInfoClassMember('packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Packet counter
                ''',
                'packets',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            ],
            'Cisco-IOS-XR-mpls-oam-oper',
            'protect-protocol-received-good-reply',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-oam-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper'
        ),
    },
    'MplsOam.Packet.Received.ReceivedGoodBfdRequest' : {
        'meta_info' : _MetaInfoClass('MplsOam.Packet.Received.ReceivedGoodBfdRequest',
            False, 
            [
            _MetaInfoClassMember('bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Byte counter
                ''',
                'bytes',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            _MetaInfoClassMember('packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Packet counter
                ''',
                'packets',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            ],
            'Cisco-IOS-XR-mpls-oam-oper',
            'received-good-bfd-request',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-oam-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper'
        ),
    },
    'MplsOam.Packet.Received.ReceivedGoodBfdReply' : {
        'meta_info' : _MetaInfoClass('MplsOam.Packet.Received.ReceivedGoodBfdReply',
            False, 
            [
            _MetaInfoClassMember('bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Byte counter
                ''',
                'bytes',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            _MetaInfoClassMember('packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Packet counter
                ''',
                'packets',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            ],
            'Cisco-IOS-XR-mpls-oam-oper',
            'received-good-bfd-reply',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-oam-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper'
        ),
    },
    'MplsOam.Packet.Received' : {
        'meta_info' : _MetaInfoClass('MplsOam.Packet.Received',
            False, 
            [
            _MetaInfoClassMember('protect-protocol-received-good-reply', REFERENCE_CLASS, 'ProtectProtocolReceivedGoodReply' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper', 'MplsOam.Packet.Received.ProtectProtocolReceivedGoodReply', 
                [], [], 
                '''                Protect Protocol Received good reply
                ''',
                'protect_protocol_received_good_reply',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            _MetaInfoClassMember('protect-protocol-received-good-request', REFERENCE_CLASS, 'ProtectProtocolReceivedGoodRequest' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper', 'MplsOam.Packet.Received.ProtectProtocolReceivedGoodRequest', 
                [], [], 
                '''                Protect Protocol Received good request
                ''',
                'protect_protocol_received_good_request',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            _MetaInfoClassMember('received-error-general', REFERENCE_CLASS, 'ReceivedErrorGeneral' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper', 'MplsOam.Packet.Received.ReceivedErrorGeneral', 
                [], [], 
                '''                General error
                ''',
                'received_error_general',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            _MetaInfoClassMember('received-error-ip-header', REFERENCE_CLASS, 'ReceivedErrorIpHeader' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper', 'MplsOam.Packet.Received.ReceivedErrorIpHeader', 
                [], [], 
                '''                IP header error
                ''',
                'received_error_ip_header',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            _MetaInfoClassMember('received-error-no-interface', REFERENCE_CLASS, 'ReceivedErrorNoInterface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper', 'MplsOam.Packet.Received.ReceivedErrorNoInterface', 
                [], [], 
                '''                Error no Interfaces
                ''',
                'received_error_no_interface',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            _MetaInfoClassMember('received-error-no-memory', REFERENCE_CLASS, 'ReceivedErrorNoMemory' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper', 'MplsOam.Packet.Received.ReceivedErrorNoMemory', 
                [], [], 
                '''                Error no memory
                ''',
                'received_error_no_memory',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            _MetaInfoClassMember('received-error-queue-full', REFERENCE_CLASS, 'ReceivedErrorQueueFull' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper', 'MplsOam.Packet.Received.ReceivedErrorQueueFull', 
                [], [], 
                '''                Dropped queue full
                ''',
                'received_error_queue_full',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            _MetaInfoClassMember('received-error-runt', REFERENCE_CLASS, 'ReceivedErrorRunt' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper', 'MplsOam.Packet.Received.ReceivedErrorRunt', 
                [], [], 
                '''                RUNT error
                ''',
                'received_error_runt',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            _MetaInfoClassMember('received-error-udp-header', REFERENCE_CLASS, 'ReceivedErrorUdpHeader' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper', 'MplsOam.Packet.Received.ReceivedErrorUdpHeader', 
                [], [], 
                '''                UDP header error
                ''',
                'received_error_udp_header',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            _MetaInfoClassMember('received-good-bfd-reply', REFERENCE_CLASS, 'ReceivedGoodBfdReply' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper', 'MplsOam.Packet.Received.ReceivedGoodBfdReply', 
                [], [], 
                '''                Received Reply with BFD TLV
                ''',
                'received_good_bfd_reply',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            _MetaInfoClassMember('received-good-bfd-request', REFERENCE_CLASS, 'ReceivedGoodBfdRequest' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper', 'MplsOam.Packet.Received.ReceivedGoodBfdRequest', 
                [], [], 
                '''                Received Reqeust with BFD TLV
                ''',
                'received_good_bfd_request',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            _MetaInfoClassMember('received-good-reply', REFERENCE_CLASS, 'ReceivedGoodReply' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper', 'MplsOam.Packet.Received.ReceivedGoodReply', 
                [], [], 
                '''                Received good reply
                ''',
                'received_good_reply',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            _MetaInfoClassMember('received-good-request', REFERENCE_CLASS, 'ReceivedGoodRequest' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper', 'MplsOam.Packet.Received.ReceivedGoodRequest', 
                [], [], 
                '''                Received good request
                ''',
                'received_good_request',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            _MetaInfoClassMember('received-unknown', REFERENCE_CLASS, 'ReceivedUnknown' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper', 'MplsOam.Packet.Received.ReceivedUnknown', 
                [], [], 
                '''                Received unknown packets
                ''',
                'received_unknown',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            ],
            'Cisco-IOS-XR-mpls-oam-oper',
            'received',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-oam-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper'
        ),
    },
    'MplsOam.Packet.Sent.TransmitGood' : {
        'meta_info' : _MetaInfoClass('MplsOam.Packet.Sent.TransmitGood',
            False, 
            [
            _MetaInfoClassMember('bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Byte counter
                ''',
                'bytes',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            _MetaInfoClassMember('packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Packet counter
                ''',
                'packets',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            ],
            'Cisco-IOS-XR-mpls-oam-oper',
            'transmit-good',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-oam-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper'
        ),
    },
    'MplsOam.Packet.Sent.TransmitDrop' : {
        'meta_info' : _MetaInfoClass('MplsOam.Packet.Sent.TransmitDrop',
            False, 
            [
            _MetaInfoClassMember('bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Byte counter
                ''',
                'bytes',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            _MetaInfoClassMember('packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Packet counter
                ''',
                'packets',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            ],
            'Cisco-IOS-XR-mpls-oam-oper',
            'transmit-drop',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-oam-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper'
        ),
    },
    'MplsOam.Packet.Sent.TransmitBfdGood' : {
        'meta_info' : _MetaInfoClass('MplsOam.Packet.Sent.TransmitBfdGood',
            False, 
            [
            _MetaInfoClassMember('bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Byte counter
                ''',
                'bytes',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            _MetaInfoClassMember('packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Packet counter
                ''',
                'packets',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            ],
            'Cisco-IOS-XR-mpls-oam-oper',
            'transmit-bfd-good',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-oam-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper'
        ),
    },
    'MplsOam.Packet.Sent.BfdNoReply' : {
        'meta_info' : _MetaInfoClass('MplsOam.Packet.Sent.BfdNoReply',
            False, 
            [
            _MetaInfoClassMember('bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Byte counter
                ''',
                'bytes',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            _MetaInfoClassMember('packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Packet counter
                ''',
                'packets',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            ],
            'Cisco-IOS-XR-mpls-oam-oper',
            'bfd-no-reply',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-oam-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper'
        ),
    },
    'MplsOam.Packet.Sent' : {
        'meta_info' : _MetaInfoClass('MplsOam.Packet.Sent',
            False, 
            [
            _MetaInfoClassMember('bfd-no-reply', REFERENCE_CLASS, 'BfdNoReply' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper', 'MplsOam.Packet.Sent.BfdNoReply', 
                [], [], 
                '''                No Reply action for echo reqeust of BFD
                bootstrap
                ''',
                'bfd_no_reply',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            _MetaInfoClassMember('transmit-bfd-good', REFERENCE_CLASS, 'TransmitBfdGood' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper', 'MplsOam.Packet.Sent.TransmitBfdGood', 
                [], [], 
                '''                Transmit good BFD request packets
                ''',
                'transmit_bfd_good',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            _MetaInfoClassMember('transmit-drop', REFERENCE_CLASS, 'TransmitDrop' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper', 'MplsOam.Packet.Sent.TransmitDrop', 
                [], [], 
                '''                Transmit drop packets
                ''',
                'transmit_drop',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            _MetaInfoClassMember('transmit-good', REFERENCE_CLASS, 'TransmitGood' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper', 'MplsOam.Packet.Sent.TransmitGood', 
                [], [], 
                '''                Transmit good packets
                ''',
                'transmit_good',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            ],
            'Cisco-IOS-XR-mpls-oam-oper',
            'sent',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-oam-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper'
        ),
    },
    'MplsOam.Packet.WorkingReqSent.TransmitGood' : {
        'meta_info' : _MetaInfoClass('MplsOam.Packet.WorkingReqSent.TransmitGood',
            False, 
            [
            _MetaInfoClassMember('bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Byte counter
                ''',
                'bytes',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            _MetaInfoClassMember('packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Packet counter
                ''',
                'packets',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            ],
            'Cisco-IOS-XR-mpls-oam-oper',
            'transmit-good',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-oam-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper'
        ),
    },
    'MplsOam.Packet.WorkingReqSent.TransmitDrop' : {
        'meta_info' : _MetaInfoClass('MplsOam.Packet.WorkingReqSent.TransmitDrop',
            False, 
            [
            _MetaInfoClassMember('bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Byte counter
                ''',
                'bytes',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            _MetaInfoClassMember('packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Packet counter
                ''',
                'packets',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            ],
            'Cisco-IOS-XR-mpls-oam-oper',
            'transmit-drop',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-oam-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper'
        ),
    },
    'MplsOam.Packet.WorkingReqSent.TransmitBfdGood' : {
        'meta_info' : _MetaInfoClass('MplsOam.Packet.WorkingReqSent.TransmitBfdGood',
            False, 
            [
            _MetaInfoClassMember('bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Byte counter
                ''',
                'bytes',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            _MetaInfoClassMember('packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Packet counter
                ''',
                'packets',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            ],
            'Cisco-IOS-XR-mpls-oam-oper',
            'transmit-bfd-good',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-oam-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper'
        ),
    },
    'MplsOam.Packet.WorkingReqSent.BfdNoReply' : {
        'meta_info' : _MetaInfoClass('MplsOam.Packet.WorkingReqSent.BfdNoReply',
            False, 
            [
            _MetaInfoClassMember('bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Byte counter
                ''',
                'bytes',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            _MetaInfoClassMember('packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Packet counter
                ''',
                'packets',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            ],
            'Cisco-IOS-XR-mpls-oam-oper',
            'bfd-no-reply',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-oam-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper'
        ),
    },
    'MplsOam.Packet.WorkingReqSent' : {
        'meta_info' : _MetaInfoClass('MplsOam.Packet.WorkingReqSent',
            False, 
            [
            _MetaInfoClassMember('bfd-no-reply', REFERENCE_CLASS, 'BfdNoReply' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper', 'MplsOam.Packet.WorkingReqSent.BfdNoReply', 
                [], [], 
                '''                No Reply action for echo reqeust of BFD
                bootstrap
                ''',
                'bfd_no_reply',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            _MetaInfoClassMember('transmit-bfd-good', REFERENCE_CLASS, 'TransmitBfdGood' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper', 'MplsOam.Packet.WorkingReqSent.TransmitBfdGood', 
                [], [], 
                '''                Transmit good BFD request packets
                ''',
                'transmit_bfd_good',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            _MetaInfoClassMember('transmit-drop', REFERENCE_CLASS, 'TransmitDrop' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper', 'MplsOam.Packet.WorkingReqSent.TransmitDrop', 
                [], [], 
                '''                Transmit drop packets
                ''',
                'transmit_drop',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            _MetaInfoClassMember('transmit-good', REFERENCE_CLASS, 'TransmitGood' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper', 'MplsOam.Packet.WorkingReqSent.TransmitGood', 
                [], [], 
                '''                Transmit good packets
                ''',
                'transmit_good',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            ],
            'Cisco-IOS-XR-mpls-oam-oper',
            'working-req-sent',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-oam-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper'
        ),
    },
    'MplsOam.Packet.WorkingRepSent.TransmitGood' : {
        'meta_info' : _MetaInfoClass('MplsOam.Packet.WorkingRepSent.TransmitGood',
            False, 
            [
            _MetaInfoClassMember('bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Byte counter
                ''',
                'bytes',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            _MetaInfoClassMember('packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Packet counter
                ''',
                'packets',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            ],
            'Cisco-IOS-XR-mpls-oam-oper',
            'transmit-good',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-oam-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper'
        ),
    },
    'MplsOam.Packet.WorkingRepSent.TransmitDrop' : {
        'meta_info' : _MetaInfoClass('MplsOam.Packet.WorkingRepSent.TransmitDrop',
            False, 
            [
            _MetaInfoClassMember('bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Byte counter
                ''',
                'bytes',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            _MetaInfoClassMember('packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Packet counter
                ''',
                'packets',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            ],
            'Cisco-IOS-XR-mpls-oam-oper',
            'transmit-drop',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-oam-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper'
        ),
    },
    'MplsOam.Packet.WorkingRepSent.TransmitBfdGood' : {
        'meta_info' : _MetaInfoClass('MplsOam.Packet.WorkingRepSent.TransmitBfdGood',
            False, 
            [
            _MetaInfoClassMember('bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Byte counter
                ''',
                'bytes',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            _MetaInfoClassMember('packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Packet counter
                ''',
                'packets',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            ],
            'Cisco-IOS-XR-mpls-oam-oper',
            'transmit-bfd-good',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-oam-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper'
        ),
    },
    'MplsOam.Packet.WorkingRepSent.BfdNoReply' : {
        'meta_info' : _MetaInfoClass('MplsOam.Packet.WorkingRepSent.BfdNoReply',
            False, 
            [
            _MetaInfoClassMember('bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Byte counter
                ''',
                'bytes',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            _MetaInfoClassMember('packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Packet counter
                ''',
                'packets',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            ],
            'Cisco-IOS-XR-mpls-oam-oper',
            'bfd-no-reply',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-oam-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper'
        ),
    },
    'MplsOam.Packet.WorkingRepSent' : {
        'meta_info' : _MetaInfoClass('MplsOam.Packet.WorkingRepSent',
            False, 
            [
            _MetaInfoClassMember('bfd-no-reply', REFERENCE_CLASS, 'BfdNoReply' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper', 'MplsOam.Packet.WorkingRepSent.BfdNoReply', 
                [], [], 
                '''                No Reply action for echo reqeust of BFD
                bootstrap
                ''',
                'bfd_no_reply',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            _MetaInfoClassMember('transmit-bfd-good', REFERENCE_CLASS, 'TransmitBfdGood' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper', 'MplsOam.Packet.WorkingRepSent.TransmitBfdGood', 
                [], [], 
                '''                Transmit good BFD request packets
                ''',
                'transmit_bfd_good',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            _MetaInfoClassMember('transmit-drop', REFERENCE_CLASS, 'TransmitDrop' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper', 'MplsOam.Packet.WorkingRepSent.TransmitDrop', 
                [], [], 
                '''                Transmit drop packets
                ''',
                'transmit_drop',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            _MetaInfoClassMember('transmit-good', REFERENCE_CLASS, 'TransmitGood' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper', 'MplsOam.Packet.WorkingRepSent.TransmitGood', 
                [], [], 
                '''                Transmit good packets
                ''',
                'transmit_good',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            ],
            'Cisco-IOS-XR-mpls-oam-oper',
            'working-rep-sent',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-oam-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper'
        ),
    },
    'MplsOam.Packet.ProtectReqSent.TransmitGood' : {
        'meta_info' : _MetaInfoClass('MplsOam.Packet.ProtectReqSent.TransmitGood',
            False, 
            [
            _MetaInfoClassMember('bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Byte counter
                ''',
                'bytes',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            _MetaInfoClassMember('packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Packet counter
                ''',
                'packets',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            ],
            'Cisco-IOS-XR-mpls-oam-oper',
            'transmit-good',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-oam-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper'
        ),
    },
    'MplsOam.Packet.ProtectReqSent.TransmitDrop' : {
        'meta_info' : _MetaInfoClass('MplsOam.Packet.ProtectReqSent.TransmitDrop',
            False, 
            [
            _MetaInfoClassMember('bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Byte counter
                ''',
                'bytes',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            _MetaInfoClassMember('packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Packet counter
                ''',
                'packets',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            ],
            'Cisco-IOS-XR-mpls-oam-oper',
            'transmit-drop',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-oam-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper'
        ),
    },
    'MplsOam.Packet.ProtectReqSent.TransmitBfdGood' : {
        'meta_info' : _MetaInfoClass('MplsOam.Packet.ProtectReqSent.TransmitBfdGood',
            False, 
            [
            _MetaInfoClassMember('bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Byte counter
                ''',
                'bytes',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            _MetaInfoClassMember('packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Packet counter
                ''',
                'packets',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            ],
            'Cisco-IOS-XR-mpls-oam-oper',
            'transmit-bfd-good',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-oam-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper'
        ),
    },
    'MplsOam.Packet.ProtectReqSent.BfdNoReply' : {
        'meta_info' : _MetaInfoClass('MplsOam.Packet.ProtectReqSent.BfdNoReply',
            False, 
            [
            _MetaInfoClassMember('bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Byte counter
                ''',
                'bytes',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            _MetaInfoClassMember('packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Packet counter
                ''',
                'packets',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            ],
            'Cisco-IOS-XR-mpls-oam-oper',
            'bfd-no-reply',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-oam-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper'
        ),
    },
    'MplsOam.Packet.ProtectReqSent' : {
        'meta_info' : _MetaInfoClass('MplsOam.Packet.ProtectReqSent',
            False, 
            [
            _MetaInfoClassMember('bfd-no-reply', REFERENCE_CLASS, 'BfdNoReply' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper', 'MplsOam.Packet.ProtectReqSent.BfdNoReply', 
                [], [], 
                '''                No Reply action for echo reqeust of BFD
                bootstrap
                ''',
                'bfd_no_reply',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            _MetaInfoClassMember('transmit-bfd-good', REFERENCE_CLASS, 'TransmitBfdGood' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper', 'MplsOam.Packet.ProtectReqSent.TransmitBfdGood', 
                [], [], 
                '''                Transmit good BFD request packets
                ''',
                'transmit_bfd_good',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            _MetaInfoClassMember('transmit-drop', REFERENCE_CLASS, 'TransmitDrop' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper', 'MplsOam.Packet.ProtectReqSent.TransmitDrop', 
                [], [], 
                '''                Transmit drop packets
                ''',
                'transmit_drop',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            _MetaInfoClassMember('transmit-good', REFERENCE_CLASS, 'TransmitGood' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper', 'MplsOam.Packet.ProtectReqSent.TransmitGood', 
                [], [], 
                '''                Transmit good packets
                ''',
                'transmit_good',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            ],
            'Cisco-IOS-XR-mpls-oam-oper',
            'protect-req-sent',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-oam-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper'
        ),
    },
    'MplsOam.Packet.ProtectRepSent.TransmitGood' : {
        'meta_info' : _MetaInfoClass('MplsOam.Packet.ProtectRepSent.TransmitGood',
            False, 
            [
            _MetaInfoClassMember('bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Byte counter
                ''',
                'bytes',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            _MetaInfoClassMember('packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Packet counter
                ''',
                'packets',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            ],
            'Cisco-IOS-XR-mpls-oam-oper',
            'transmit-good',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-oam-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper'
        ),
    },
    'MplsOam.Packet.ProtectRepSent.TransmitDrop' : {
        'meta_info' : _MetaInfoClass('MplsOam.Packet.ProtectRepSent.TransmitDrop',
            False, 
            [
            _MetaInfoClassMember('bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Byte counter
                ''',
                'bytes',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            _MetaInfoClassMember('packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Packet counter
                ''',
                'packets',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            ],
            'Cisco-IOS-XR-mpls-oam-oper',
            'transmit-drop',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-oam-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper'
        ),
    },
    'MplsOam.Packet.ProtectRepSent.TransmitBfdGood' : {
        'meta_info' : _MetaInfoClass('MplsOam.Packet.ProtectRepSent.TransmitBfdGood',
            False, 
            [
            _MetaInfoClassMember('bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Byte counter
                ''',
                'bytes',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            _MetaInfoClassMember('packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Packet counter
                ''',
                'packets',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            ],
            'Cisco-IOS-XR-mpls-oam-oper',
            'transmit-bfd-good',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-oam-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper'
        ),
    },
    'MplsOam.Packet.ProtectRepSent.BfdNoReply' : {
        'meta_info' : _MetaInfoClass('MplsOam.Packet.ProtectRepSent.BfdNoReply',
            False, 
            [
            _MetaInfoClassMember('bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Byte counter
                ''',
                'bytes',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            _MetaInfoClassMember('packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Packet counter
                ''',
                'packets',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            ],
            'Cisco-IOS-XR-mpls-oam-oper',
            'bfd-no-reply',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-oam-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper'
        ),
    },
    'MplsOam.Packet.ProtectRepSent' : {
        'meta_info' : _MetaInfoClass('MplsOam.Packet.ProtectRepSent',
            False, 
            [
            _MetaInfoClassMember('bfd-no-reply', REFERENCE_CLASS, 'BfdNoReply' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper', 'MplsOam.Packet.ProtectRepSent.BfdNoReply', 
                [], [], 
                '''                No Reply action for echo reqeust of BFD
                bootstrap
                ''',
                'bfd_no_reply',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            _MetaInfoClassMember('transmit-bfd-good', REFERENCE_CLASS, 'TransmitBfdGood' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper', 'MplsOam.Packet.ProtectRepSent.TransmitBfdGood', 
                [], [], 
                '''                Transmit good BFD request packets
                ''',
                'transmit_bfd_good',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            _MetaInfoClassMember('transmit-drop', REFERENCE_CLASS, 'TransmitDrop' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper', 'MplsOam.Packet.ProtectRepSent.TransmitDrop', 
                [], [], 
                '''                Transmit drop packets
                ''',
                'transmit_drop',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            _MetaInfoClassMember('transmit-good', REFERENCE_CLASS, 'TransmitGood' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper', 'MplsOam.Packet.ProtectRepSent.TransmitGood', 
                [], [], 
                '''                Transmit good packets
                ''',
                'transmit_good',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            ],
            'Cisco-IOS-XR-mpls-oam-oper',
            'protect-rep-sent',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-oam-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper'
        ),
    },
    'MplsOam.Packet' : {
        'meta_info' : _MetaInfoClass('MplsOam.Packet',
            False, 
            [
            _MetaInfoClassMember('protect-rep-sent', REFERENCE_CLASS, 'ProtectRepSent' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper', 'MplsOam.Packet.ProtectRepSent', 
                [], [], 
                '''                Protect Reply Packet transmit counts
                ''',
                'protect_rep_sent',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            _MetaInfoClassMember('protect-req-sent', REFERENCE_CLASS, 'ProtectReqSent' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper', 'MplsOam.Packet.ProtectReqSent', 
                [], [], 
                '''                Protect Request Packet transmit counts
                ''',
                'protect_req_sent',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            _MetaInfoClassMember('received', REFERENCE_CLASS, 'Received' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper', 'MplsOam.Packet.Received', 
                [], [], 
                '''                Packet reception counts
                ''',
                'received',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            _MetaInfoClassMember('sent', REFERENCE_CLASS, 'Sent' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper', 'MplsOam.Packet.Sent', 
                [], [], 
                '''                Packet transmit counts
                ''',
                'sent',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            _MetaInfoClassMember('working-rep-sent', REFERENCE_CLASS, 'WorkingRepSent' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper', 'MplsOam.Packet.WorkingRepSent', 
                [], [], 
                '''                Working Reply Packet transmit counts
                ''',
                'working_rep_sent',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            _MetaInfoClassMember('working-req-sent', REFERENCE_CLASS, 'WorkingReqSent' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper', 'MplsOam.Packet.WorkingReqSent', 
                [], [], 
                '''                Working Request Packet transmit counts
                ''',
                'working_req_sent',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            ],
            'Cisco-IOS-XR-mpls-oam-oper',
            'packet',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-oam-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper'
        ),
    },
    'MplsOam.Global_.MessageStatistics' : {
        'meta_info' : _MetaInfoClass('MplsOam.Global_.MessageStatistics',
            False, 
            [
            _MetaInfoClassMember('echo-cancel-messages', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Message echo cancel count
                ''',
                'echo_cancel_messages',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            _MetaInfoClassMember('echo-submit-messages', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Message echo submit count
                ''',
                'echo_submit_messages',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            _MetaInfoClassMember('get-config-messages', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Message get configiuration count
                ''',
                'get_config_messages',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            _MetaInfoClassMember('get-response-messages', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Message get response count
                ''',
                'get_response_messages',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            _MetaInfoClassMember('get-result-messages', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Message get results count
                ''',
                'get_result_messages',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            _MetaInfoClassMember('property-block-messages', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Message property block count
                ''',
                'property_block_messages',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            _MetaInfoClassMember('property-request-messages', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Message property request count
                ''',
                'property_request_messages',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            _MetaInfoClassMember('property-response-messages', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Message property response count
                ''',
                'property_response_messages',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            _MetaInfoClassMember('register-messages', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Message register count
                ''',
                'register_messages',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            _MetaInfoClassMember('thread-request-messages', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Message thread request count
                ''',
                'thread_request_messages',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            _MetaInfoClassMember('unregister-messages', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Message unregister count
                ''',
                'unregister_messages',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            ],
            'Cisco-IOS-XR-mpls-oam-oper',
            'message-statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-oam-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper'
        ),
    },
    'MplsOam.Global_.CollaboratorStatistics.CollaboratorIParm' : {
        'meta_info' : _MetaInfoClass('MplsOam.Global_.CollaboratorStatistics.CollaboratorIParm',
            False, 
            [
            _MetaInfoClassMember('downs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Collaborator down counter
                ''',
                'downs',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            _MetaInfoClassMember('ups', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Collaborator up counter
                ''',
                'ups',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            ],
            'Cisco-IOS-XR-mpls-oam-oper',
            'collaborator-i-parm',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-oam-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper'
        ),
    },
    'MplsOam.Global_.CollaboratorStatistics.CollaboratorIm' : {
        'meta_info' : _MetaInfoClass('MplsOam.Global_.CollaboratorStatistics.CollaboratorIm',
            False, 
            [
            _MetaInfoClassMember('downs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Collaborator down counter
                ''',
                'downs',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            _MetaInfoClassMember('ups', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Collaborator up counter
                ''',
                'ups',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            ],
            'Cisco-IOS-XR-mpls-oam-oper',
            'collaborator-im',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-oam-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper'
        ),
    },
    'MplsOam.Global_.CollaboratorStatistics.CollaboratorNetIo' : {
        'meta_info' : _MetaInfoClass('MplsOam.Global_.CollaboratorStatistics.CollaboratorNetIo',
            False, 
            [
            _MetaInfoClassMember('downs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Collaborator down counter
                ''',
                'downs',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            _MetaInfoClassMember('ups', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Collaborator up counter
                ''',
                'ups',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            ],
            'Cisco-IOS-XR-mpls-oam-oper',
            'collaborator-net-io',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-oam-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper'
        ),
    },
    'MplsOam.Global_.CollaboratorStatistics.CollaboratorRib' : {
        'meta_info' : _MetaInfoClass('MplsOam.Global_.CollaboratorStatistics.CollaboratorRib',
            False, 
            [
            _MetaInfoClassMember('downs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Collaborator down counter
                ''',
                'downs',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            _MetaInfoClassMember('ups', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Collaborator up counter
                ''',
                'ups',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            ],
            'Cisco-IOS-XR-mpls-oam-oper',
            'collaborator-rib',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-oam-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper'
        ),
    },
    'MplsOam.Global_.CollaboratorStatistics' : {
        'meta_info' : _MetaInfoClass('MplsOam.Global_.CollaboratorStatistics',
            False, 
            [
            _MetaInfoClassMember('collaborator-i-parm', REFERENCE_CLASS, 'CollaboratorIParm' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper', 'MplsOam.Global_.CollaboratorStatistics.CollaboratorIParm', 
                [], [], 
                '''                Collaborator IPARM counts
                ''',
                'collaborator_i_parm',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            _MetaInfoClassMember('collaborator-im', REFERENCE_CLASS, 'CollaboratorIm' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper', 'MplsOam.Global_.CollaboratorStatistics.CollaboratorIm', 
                [], [], 
                '''                Collaborator IM counts
                ''',
                'collaborator_im',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            _MetaInfoClassMember('collaborator-net-io', REFERENCE_CLASS, 'CollaboratorNetIo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper', 'MplsOam.Global_.CollaboratorStatistics.CollaboratorNetIo', 
                [], [], 
                '''                Collaborator NetIO counts
                ''',
                'collaborator_net_io',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            _MetaInfoClassMember('collaborator-rib', REFERENCE_CLASS, 'CollaboratorRib' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper', 'MplsOam.Global_.CollaboratorStatistics.CollaboratorRib', 
                [], [], 
                '''                Collaborator RIB counts
                ''',
                'collaborator_rib',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            ],
            'Cisco-IOS-XR-mpls-oam-oper',
            'collaborator-statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-oam-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper'
        ),
    },
    'MplsOam.Global_' : {
        'meta_info' : _MetaInfoClass('MplsOam.Global_',
            False, 
            [
            _MetaInfoClassMember('collaborator-statistics', REFERENCE_CLASS, 'CollaboratorStatistics' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper', 'MplsOam.Global_.CollaboratorStatistics', 
                [], [], 
                '''                Collaborator statistics
                ''',
                'collaborator_statistics',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            _MetaInfoClassMember('message-statistics', REFERENCE_CLASS, 'MessageStatistics' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper', 'MplsOam.Global_.MessageStatistics', 
                [], [], 
                '''                Message statistics
                ''',
                'message_statistics',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            _MetaInfoClassMember('total-clients', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of clients
                ''',
                'total_clients',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            ],
            'Cisco-IOS-XR-mpls-oam-oper',
            'global',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-oam-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper'
        ),
    },
    'MplsOam' : {
        'meta_info' : _MetaInfoClass('MplsOam',
            False, 
            [
            _MetaInfoClassMember('global', REFERENCE_CLASS, 'Global_' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper', 'MplsOam.Global_', 
                [], [], 
                '''                LSPV global counters operational data
                ''',
                'global_',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            _MetaInfoClassMember('interface', REFERENCE_CLASS, 'Interface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper', 'MplsOam.Interface', 
                [], [], 
                '''                MPLS OAM interface operational data
                ''',
                'interface',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            _MetaInfoClassMember('packet', REFERENCE_CLASS, 'Packet' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper', 'MplsOam.Packet', 
                [], [], 
                '''                LSPV packet counters operational data
                ''',
                'packet',
                'Cisco-IOS-XR-mpls-oam-oper', False),
            ],
            'Cisco-IOS-XR-mpls-oam-oper',
            'mpls-oam',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-oam-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_oam_oper'
        ),
    },
}
_meta_table['MplsOam.Interface.Briefs.Brief']['meta_info'].parent =_meta_table['MplsOam.Interface.Briefs']['meta_info']
_meta_table['MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedGoodRequest']['meta_info'].parent =_meta_table['MplsOam.Interface.Details.Detail.PacketStatistics.Received']['meta_info']
_meta_table['MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedGoodReply']['meta_info'].parent =_meta_table['MplsOam.Interface.Details.Detail.PacketStatistics.Received']['meta_info']
_meta_table['MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedUnknown']['meta_info'].parent =_meta_table['MplsOam.Interface.Details.Detail.PacketStatistics.Received']['meta_info']
_meta_table['MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedErrorIpHeader']['meta_info'].parent =_meta_table['MplsOam.Interface.Details.Detail.PacketStatistics.Received']['meta_info']
_meta_table['MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedErrorUdpHeader']['meta_info'].parent =_meta_table['MplsOam.Interface.Details.Detail.PacketStatistics.Received']['meta_info']
_meta_table['MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedErrorRunt']['meta_info'].parent =_meta_table['MplsOam.Interface.Details.Detail.PacketStatistics.Received']['meta_info']
_meta_table['MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedErrorQueueFull']['meta_info'].parent =_meta_table['MplsOam.Interface.Details.Detail.PacketStatistics.Received']['meta_info']
_meta_table['MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedErrorGeneral']['meta_info'].parent =_meta_table['MplsOam.Interface.Details.Detail.PacketStatistics.Received']['meta_info']
_meta_table['MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedErrorNoInterface']['meta_info'].parent =_meta_table['MplsOam.Interface.Details.Detail.PacketStatistics.Received']['meta_info']
_meta_table['MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedErrorNoMemory']['meta_info'].parent =_meta_table['MplsOam.Interface.Details.Detail.PacketStatistics.Received']['meta_info']
_meta_table['MplsOam.Interface.Details.Detail.PacketStatistics.Received.ProtectProtocolReceivedGoodRequest']['meta_info'].parent =_meta_table['MplsOam.Interface.Details.Detail.PacketStatistics.Received']['meta_info']
_meta_table['MplsOam.Interface.Details.Detail.PacketStatistics.Received.ProtectProtocolReceivedGoodReply']['meta_info'].parent =_meta_table['MplsOam.Interface.Details.Detail.PacketStatistics.Received']['meta_info']
_meta_table['MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedGoodBfdRequest']['meta_info'].parent =_meta_table['MplsOam.Interface.Details.Detail.PacketStatistics.Received']['meta_info']
_meta_table['MplsOam.Interface.Details.Detail.PacketStatistics.Received.ReceivedGoodBfdReply']['meta_info'].parent =_meta_table['MplsOam.Interface.Details.Detail.PacketStatistics.Received']['meta_info']
_meta_table['MplsOam.Interface.Details.Detail.PacketStatistics.Sent.TransmitGood']['meta_info'].parent =_meta_table['MplsOam.Interface.Details.Detail.PacketStatistics.Sent']['meta_info']
_meta_table['MplsOam.Interface.Details.Detail.PacketStatistics.Sent.TransmitDrop']['meta_info'].parent =_meta_table['MplsOam.Interface.Details.Detail.PacketStatistics.Sent']['meta_info']
_meta_table['MplsOam.Interface.Details.Detail.PacketStatistics.Sent.TransmitBfdGood']['meta_info'].parent =_meta_table['MplsOam.Interface.Details.Detail.PacketStatistics.Sent']['meta_info']
_meta_table['MplsOam.Interface.Details.Detail.PacketStatistics.Sent.BfdNoReply']['meta_info'].parent =_meta_table['MplsOam.Interface.Details.Detail.PacketStatistics.Sent']['meta_info']
_meta_table['MplsOam.Interface.Details.Detail.PacketStatistics.WorkingReqSent.TransmitGood']['meta_info'].parent =_meta_table['MplsOam.Interface.Details.Detail.PacketStatistics.WorkingReqSent']['meta_info']
_meta_table['MplsOam.Interface.Details.Detail.PacketStatistics.WorkingReqSent.TransmitDrop']['meta_info'].parent =_meta_table['MplsOam.Interface.Details.Detail.PacketStatistics.WorkingReqSent']['meta_info']
_meta_table['MplsOam.Interface.Details.Detail.PacketStatistics.WorkingReqSent.TransmitBfdGood']['meta_info'].parent =_meta_table['MplsOam.Interface.Details.Detail.PacketStatistics.WorkingReqSent']['meta_info']
_meta_table['MplsOam.Interface.Details.Detail.PacketStatistics.WorkingReqSent.BfdNoReply']['meta_info'].parent =_meta_table['MplsOam.Interface.Details.Detail.PacketStatistics.WorkingReqSent']['meta_info']
_meta_table['MplsOam.Interface.Details.Detail.PacketStatistics.WorkingRepSent.TransmitGood']['meta_info'].parent =_meta_table['MplsOam.Interface.Details.Detail.PacketStatistics.WorkingRepSent']['meta_info']
_meta_table['MplsOam.Interface.Details.Detail.PacketStatistics.WorkingRepSent.TransmitDrop']['meta_info'].parent =_meta_table['MplsOam.Interface.Details.Detail.PacketStatistics.WorkingRepSent']['meta_info']
_meta_table['MplsOam.Interface.Details.Detail.PacketStatistics.WorkingRepSent.TransmitBfdGood']['meta_info'].parent =_meta_table['MplsOam.Interface.Details.Detail.PacketStatistics.WorkingRepSent']['meta_info']
_meta_table['MplsOam.Interface.Details.Detail.PacketStatistics.WorkingRepSent.BfdNoReply']['meta_info'].parent =_meta_table['MplsOam.Interface.Details.Detail.PacketStatistics.WorkingRepSent']['meta_info']
_meta_table['MplsOam.Interface.Details.Detail.PacketStatistics.ProtectReqSent.TransmitGood']['meta_info'].parent =_meta_table['MplsOam.Interface.Details.Detail.PacketStatistics.ProtectReqSent']['meta_info']
_meta_table['MplsOam.Interface.Details.Detail.PacketStatistics.ProtectReqSent.TransmitDrop']['meta_info'].parent =_meta_table['MplsOam.Interface.Details.Detail.PacketStatistics.ProtectReqSent']['meta_info']
_meta_table['MplsOam.Interface.Details.Detail.PacketStatistics.ProtectReqSent.TransmitBfdGood']['meta_info'].parent =_meta_table['MplsOam.Interface.Details.Detail.PacketStatistics.ProtectReqSent']['meta_info']
_meta_table['MplsOam.Interface.Details.Detail.PacketStatistics.ProtectReqSent.BfdNoReply']['meta_info'].parent =_meta_table['MplsOam.Interface.Details.Detail.PacketStatistics.ProtectReqSent']['meta_info']
_meta_table['MplsOam.Interface.Details.Detail.PacketStatistics.ProtectRepSent.TransmitGood']['meta_info'].parent =_meta_table['MplsOam.Interface.Details.Detail.PacketStatistics.ProtectRepSent']['meta_info']
_meta_table['MplsOam.Interface.Details.Detail.PacketStatistics.ProtectRepSent.TransmitDrop']['meta_info'].parent =_meta_table['MplsOam.Interface.Details.Detail.PacketStatistics.ProtectRepSent']['meta_info']
_meta_table['MplsOam.Interface.Details.Detail.PacketStatistics.ProtectRepSent.TransmitBfdGood']['meta_info'].parent =_meta_table['MplsOam.Interface.Details.Detail.PacketStatistics.ProtectRepSent']['meta_info']
_meta_table['MplsOam.Interface.Details.Detail.PacketStatistics.ProtectRepSent.BfdNoReply']['meta_info'].parent =_meta_table['MplsOam.Interface.Details.Detail.PacketStatistics.ProtectRepSent']['meta_info']
_meta_table['MplsOam.Interface.Details.Detail.PacketStatistics.Received']['meta_info'].parent =_meta_table['MplsOam.Interface.Details.Detail.PacketStatistics']['meta_info']
_meta_table['MplsOam.Interface.Details.Detail.PacketStatistics.Sent']['meta_info'].parent =_meta_table['MplsOam.Interface.Details.Detail.PacketStatistics']['meta_info']
_meta_table['MplsOam.Interface.Details.Detail.PacketStatistics.WorkingReqSent']['meta_info'].parent =_meta_table['MplsOam.Interface.Details.Detail.PacketStatistics']['meta_info']
_meta_table['MplsOam.Interface.Details.Detail.PacketStatistics.WorkingRepSent']['meta_info'].parent =_meta_table['MplsOam.Interface.Details.Detail.PacketStatistics']['meta_info']
_meta_table['MplsOam.Interface.Details.Detail.PacketStatistics.ProtectReqSent']['meta_info'].parent =_meta_table['MplsOam.Interface.Details.Detail.PacketStatistics']['meta_info']
_meta_table['MplsOam.Interface.Details.Detail.PacketStatistics.ProtectRepSent']['meta_info'].parent =_meta_table['MplsOam.Interface.Details.Detail.PacketStatistics']['meta_info']
_meta_table['MplsOam.Interface.Details.Detail.InterfaceBrief']['meta_info'].parent =_meta_table['MplsOam.Interface.Details.Detail']['meta_info']
_meta_table['MplsOam.Interface.Details.Detail.PacketStatistics']['meta_info'].parent =_meta_table['MplsOam.Interface.Details.Detail']['meta_info']
_meta_table['MplsOam.Interface.Details.Detail']['meta_info'].parent =_meta_table['MplsOam.Interface.Details']['meta_info']
_meta_table['MplsOam.Interface.Briefs']['meta_info'].parent =_meta_table['MplsOam.Interface']['meta_info']
_meta_table['MplsOam.Interface.Details']['meta_info'].parent =_meta_table['MplsOam.Interface']['meta_info']
_meta_table['MplsOam.Packet.Received.ReceivedGoodRequest']['meta_info'].parent =_meta_table['MplsOam.Packet.Received']['meta_info']
_meta_table['MplsOam.Packet.Received.ReceivedGoodReply']['meta_info'].parent =_meta_table['MplsOam.Packet.Received']['meta_info']
_meta_table['MplsOam.Packet.Received.ReceivedUnknown']['meta_info'].parent =_meta_table['MplsOam.Packet.Received']['meta_info']
_meta_table['MplsOam.Packet.Received.ReceivedErrorIpHeader']['meta_info'].parent =_meta_table['MplsOam.Packet.Received']['meta_info']
_meta_table['MplsOam.Packet.Received.ReceivedErrorUdpHeader']['meta_info'].parent =_meta_table['MplsOam.Packet.Received']['meta_info']
_meta_table['MplsOam.Packet.Received.ReceivedErrorRunt']['meta_info'].parent =_meta_table['MplsOam.Packet.Received']['meta_info']
_meta_table['MplsOam.Packet.Received.ReceivedErrorQueueFull']['meta_info'].parent =_meta_table['MplsOam.Packet.Received']['meta_info']
_meta_table['MplsOam.Packet.Received.ReceivedErrorGeneral']['meta_info'].parent =_meta_table['MplsOam.Packet.Received']['meta_info']
_meta_table['MplsOam.Packet.Received.ReceivedErrorNoInterface']['meta_info'].parent =_meta_table['MplsOam.Packet.Received']['meta_info']
_meta_table['MplsOam.Packet.Received.ReceivedErrorNoMemory']['meta_info'].parent =_meta_table['MplsOam.Packet.Received']['meta_info']
_meta_table['MplsOam.Packet.Received.ProtectProtocolReceivedGoodRequest']['meta_info'].parent =_meta_table['MplsOam.Packet.Received']['meta_info']
_meta_table['MplsOam.Packet.Received.ProtectProtocolReceivedGoodReply']['meta_info'].parent =_meta_table['MplsOam.Packet.Received']['meta_info']
_meta_table['MplsOam.Packet.Received.ReceivedGoodBfdRequest']['meta_info'].parent =_meta_table['MplsOam.Packet.Received']['meta_info']
_meta_table['MplsOam.Packet.Received.ReceivedGoodBfdReply']['meta_info'].parent =_meta_table['MplsOam.Packet.Received']['meta_info']
_meta_table['MplsOam.Packet.Sent.TransmitGood']['meta_info'].parent =_meta_table['MplsOam.Packet.Sent']['meta_info']
_meta_table['MplsOam.Packet.Sent.TransmitDrop']['meta_info'].parent =_meta_table['MplsOam.Packet.Sent']['meta_info']
_meta_table['MplsOam.Packet.Sent.TransmitBfdGood']['meta_info'].parent =_meta_table['MplsOam.Packet.Sent']['meta_info']
_meta_table['MplsOam.Packet.Sent.BfdNoReply']['meta_info'].parent =_meta_table['MplsOam.Packet.Sent']['meta_info']
_meta_table['MplsOam.Packet.WorkingReqSent.TransmitGood']['meta_info'].parent =_meta_table['MplsOam.Packet.WorkingReqSent']['meta_info']
_meta_table['MplsOam.Packet.WorkingReqSent.TransmitDrop']['meta_info'].parent =_meta_table['MplsOam.Packet.WorkingReqSent']['meta_info']
_meta_table['MplsOam.Packet.WorkingReqSent.TransmitBfdGood']['meta_info'].parent =_meta_table['MplsOam.Packet.WorkingReqSent']['meta_info']
_meta_table['MplsOam.Packet.WorkingReqSent.BfdNoReply']['meta_info'].parent =_meta_table['MplsOam.Packet.WorkingReqSent']['meta_info']
_meta_table['MplsOam.Packet.WorkingRepSent.TransmitGood']['meta_info'].parent =_meta_table['MplsOam.Packet.WorkingRepSent']['meta_info']
_meta_table['MplsOam.Packet.WorkingRepSent.TransmitDrop']['meta_info'].parent =_meta_table['MplsOam.Packet.WorkingRepSent']['meta_info']
_meta_table['MplsOam.Packet.WorkingRepSent.TransmitBfdGood']['meta_info'].parent =_meta_table['MplsOam.Packet.WorkingRepSent']['meta_info']
_meta_table['MplsOam.Packet.WorkingRepSent.BfdNoReply']['meta_info'].parent =_meta_table['MplsOam.Packet.WorkingRepSent']['meta_info']
_meta_table['MplsOam.Packet.ProtectReqSent.TransmitGood']['meta_info'].parent =_meta_table['MplsOam.Packet.ProtectReqSent']['meta_info']
_meta_table['MplsOam.Packet.ProtectReqSent.TransmitDrop']['meta_info'].parent =_meta_table['MplsOam.Packet.ProtectReqSent']['meta_info']
_meta_table['MplsOam.Packet.ProtectReqSent.TransmitBfdGood']['meta_info'].parent =_meta_table['MplsOam.Packet.ProtectReqSent']['meta_info']
_meta_table['MplsOam.Packet.ProtectReqSent.BfdNoReply']['meta_info'].parent =_meta_table['MplsOam.Packet.ProtectReqSent']['meta_info']
_meta_table['MplsOam.Packet.ProtectRepSent.TransmitGood']['meta_info'].parent =_meta_table['MplsOam.Packet.ProtectRepSent']['meta_info']
_meta_table['MplsOam.Packet.ProtectRepSent.TransmitDrop']['meta_info'].parent =_meta_table['MplsOam.Packet.ProtectRepSent']['meta_info']
_meta_table['MplsOam.Packet.ProtectRepSent.TransmitBfdGood']['meta_info'].parent =_meta_table['MplsOam.Packet.ProtectRepSent']['meta_info']
_meta_table['MplsOam.Packet.ProtectRepSent.BfdNoReply']['meta_info'].parent =_meta_table['MplsOam.Packet.ProtectRepSent']['meta_info']
_meta_table['MplsOam.Packet.Received']['meta_info'].parent =_meta_table['MplsOam.Packet']['meta_info']
_meta_table['MplsOam.Packet.Sent']['meta_info'].parent =_meta_table['MplsOam.Packet']['meta_info']
_meta_table['MplsOam.Packet.WorkingReqSent']['meta_info'].parent =_meta_table['MplsOam.Packet']['meta_info']
_meta_table['MplsOam.Packet.WorkingRepSent']['meta_info'].parent =_meta_table['MplsOam.Packet']['meta_info']
_meta_table['MplsOam.Packet.ProtectReqSent']['meta_info'].parent =_meta_table['MplsOam.Packet']['meta_info']
_meta_table['MplsOam.Packet.ProtectRepSent']['meta_info'].parent =_meta_table['MplsOam.Packet']['meta_info']
_meta_table['MplsOam.Global_.CollaboratorStatistics.CollaboratorIParm']['meta_info'].parent =_meta_table['MplsOam.Global_.CollaboratorStatistics']['meta_info']
_meta_table['MplsOam.Global_.CollaboratorStatistics.CollaboratorIm']['meta_info'].parent =_meta_table['MplsOam.Global_.CollaboratorStatistics']['meta_info']
_meta_table['MplsOam.Global_.CollaboratorStatistics.CollaboratorNetIo']['meta_info'].parent =_meta_table['MplsOam.Global_.CollaboratorStatistics']['meta_info']
_meta_table['MplsOam.Global_.CollaboratorStatistics.CollaboratorRib']['meta_info'].parent =_meta_table['MplsOam.Global_.CollaboratorStatistics']['meta_info']
_meta_table['MplsOam.Global_.MessageStatistics']['meta_info'].parent =_meta_table['MplsOam.Global_']['meta_info']
_meta_table['MplsOam.Global_.CollaboratorStatistics']['meta_info'].parent =_meta_table['MplsOam.Global_']['meta_info']
_meta_table['MplsOam.Interface']['meta_info'].parent =_meta_table['MplsOam']['meta_info']
_meta_table['MplsOam.Packet']['meta_info'].parent =_meta_table['MplsOam']['meta_info']
_meta_table['MplsOam.Global_']['meta_info'].parent =_meta_table['MplsOam']['meta_info']
