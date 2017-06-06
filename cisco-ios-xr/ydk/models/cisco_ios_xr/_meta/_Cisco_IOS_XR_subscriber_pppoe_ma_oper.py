


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'PppoeMaThrottleStateEnum' : _MetaInfoEnum('PppoeMaThrottleStateEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper',
        {
            'idle':'idle',
            'monitor':'monitor',
            'block':'block',
        }, 'Cisco-IOS-XR-subscriber-pppoe-ma-oper', _yang_ns._namespaces['Cisco-IOS-XR-subscriber-pppoe-ma-oper']),
    'PppoeMaLimitStateEnum' : _MetaInfoEnum('PppoeMaLimitStateEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper',
        {
            'ok':'ok',
            'warning':'warning',
            'block':'block',
        }, 'Cisco-IOS-XR-subscriber-pppoe-ma-oper', _yang_ns._namespaces['Cisco-IOS-XR-subscriber-pppoe-ma-oper']),
    'PppoeMaSessionIdbSrgStateEnum' : _MetaInfoEnum('PppoeMaSessionIdbSrgStateEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper',
        {
            'none':'none',
            'active':'active',
            'standby':'standby',
        }, 'Cisco-IOS-XR-subscriber-pppoe-ma-oper', _yang_ns._namespaces['Cisco-IOS-XR-subscriber-pppoe-ma-oper']),
    'Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.Padi' : {
        'meta_info' : _MetaInfoClass('Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.Padi',
            False, 
            [
            _MetaInfoClassMember('dropped', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Dropped
                ''',
                'dropped',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('received', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Received
                ''',
                'received',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sent
                ''',
                'sent',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            ],
            'Cisco-IOS-XR-subscriber-pppoe-ma-oper',
            'padi',
            _yang_ns._namespaces['Cisco-IOS-XR-subscriber-pppoe-ma-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper'
        ),
    },
    'Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.Pado' : {
        'meta_info' : _MetaInfoClass('Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.Pado',
            False, 
            [
            _MetaInfoClassMember('dropped', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Dropped
                ''',
                'dropped',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('received', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Received
                ''',
                'received',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sent
                ''',
                'sent',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            ],
            'Cisco-IOS-XR-subscriber-pppoe-ma-oper',
            'pado',
            _yang_ns._namespaces['Cisco-IOS-XR-subscriber-pppoe-ma-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper'
        ),
    },
    'Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.Padr' : {
        'meta_info' : _MetaInfoClass('Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.Padr',
            False, 
            [
            _MetaInfoClassMember('dropped', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Dropped
                ''',
                'dropped',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('received', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Received
                ''',
                'received',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sent
                ''',
                'sent',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            ],
            'Cisco-IOS-XR-subscriber-pppoe-ma-oper',
            'padr',
            _yang_ns._namespaces['Cisco-IOS-XR-subscriber-pppoe-ma-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper'
        ),
    },
    'Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.PadsSuccess' : {
        'meta_info' : _MetaInfoClass('Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.PadsSuccess',
            False, 
            [
            _MetaInfoClassMember('dropped', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Dropped
                ''',
                'dropped',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('received', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Received
                ''',
                'received',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sent
                ''',
                'sent',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            ],
            'Cisco-IOS-XR-subscriber-pppoe-ma-oper',
            'pads-success',
            _yang_ns._namespaces['Cisco-IOS-XR-subscriber-pppoe-ma-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper'
        ),
    },
    'Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.PadsError' : {
        'meta_info' : _MetaInfoClass('Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.PadsError',
            False, 
            [
            _MetaInfoClassMember('dropped', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Dropped
                ''',
                'dropped',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('received', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Received
                ''',
                'received',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sent
                ''',
                'sent',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            ],
            'Cisco-IOS-XR-subscriber-pppoe-ma-oper',
            'pads-error',
            _yang_ns._namespaces['Cisco-IOS-XR-subscriber-pppoe-ma-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper'
        ),
    },
    'Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.Padt' : {
        'meta_info' : _MetaInfoClass('Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.Padt',
            False, 
            [
            _MetaInfoClassMember('dropped', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Dropped
                ''',
                'dropped',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('received', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Received
                ''',
                'received',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sent
                ''',
                'sent',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            ],
            'Cisco-IOS-XR-subscriber-pppoe-ma-oper',
            'padt',
            _yang_ns._namespaces['Cisco-IOS-XR-subscriber-pppoe-ma-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper'
        ),
    },
    'Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.SessionState' : {
        'meta_info' : _MetaInfoClass('Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.SessionState',
            False, 
            [
            _MetaInfoClassMember('dropped', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Dropped
                ''',
                'dropped',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('received', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Received
                ''',
                'received',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sent
                ''',
                'sent',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            ],
            'Cisco-IOS-XR-subscriber-pppoe-ma-oper',
            'session-state',
            _yang_ns._namespaces['Cisco-IOS-XR-subscriber-pppoe-ma-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper'
        ),
    },
    'Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.Other' : {
        'meta_info' : _MetaInfoClass('Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.Other',
            False, 
            [
            _MetaInfoClassMember('dropped', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Dropped
                ''',
                'dropped',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('received', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Received
                ''',
                'received',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sent
                ''',
                'sent',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            ],
            'Cisco-IOS-XR-subscriber-pppoe-ma-oper',
            'other',
            _yang_ns._namespaces['Cisco-IOS-XR-subscriber-pppoe-ma-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper'
        ),
    },
    'Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts' : {
        'meta_info' : _MetaInfoClass('Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts',
            False, 
            [
            _MetaInfoClassMember('other', REFERENCE_CLASS, 'Other' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper', 'Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.Other', 
                [], [], 
                '''                Other counts
                ''',
                'other',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('padi', REFERENCE_CLASS, 'Padi' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper', 'Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.Padi', 
                [], [], 
                '''                PADI counts
                ''',
                'padi',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('pado', REFERENCE_CLASS, 'Pado' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper', 'Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.Pado', 
                [], [], 
                '''                PADO counts
                ''',
                'pado',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('padr', REFERENCE_CLASS, 'Padr' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper', 'Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.Padr', 
                [], [], 
                '''                PADR counts
                ''',
                'padr',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('pads-error', REFERENCE_CLASS, 'PadsError' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper', 'Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.PadsError', 
                [], [], 
                '''                PADS Error counts
                ''',
                'pads_error',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('pads-success', REFERENCE_CLASS, 'PadsSuccess' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper', 'Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.PadsSuccess', 
                [], [], 
                '''                PADS Success counts
                ''',
                'pads_success',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('padt', REFERENCE_CLASS, 'Padt' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper', 'Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.Padt', 
                [], [], 
                '''                PADT counts
                ''',
                'padt',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('session-state', REFERENCE_CLASS, 'SessionState' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper', 'Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.SessionState', 
                [], [], 
                '''                Session Stage counts
                ''',
                'session_state',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            ],
            'Cisco-IOS-XR-subscriber-pppoe-ma-oper',
            'packet-counts',
            _yang_ns._namespaces['Cisco-IOS-XR-subscriber-pppoe-ma-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper'
        ),
    },
    'Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic' : {
        'meta_info' : _MetaInfoClass('Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                PPPoE Access Interface
                ''',
                'interface_name',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', True),
            _MetaInfoClassMember('packet-counts', REFERENCE_CLASS, 'PacketCounts' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper', 'Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts', 
                [], [], 
                '''                Packet Counts
                ''',
                'packet_counts',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            ],
            'Cisco-IOS-XR-subscriber-pppoe-ma-oper',
            'access-interface-statistic',
            _yang_ns._namespaces['Cisco-IOS-XR-subscriber-pppoe-ma-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper'
        ),
    },
    'Pppoe.AccessInterfaceStatistics' : {
        'meta_info' : _MetaInfoClass('Pppoe.AccessInterfaceStatistics',
            False, 
            [
            _MetaInfoClassMember('access-interface-statistic', REFERENCE_LIST, 'AccessInterfaceStatistic' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper', 'Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic', 
                [], [], 
                '''                Statistics information for a PPPoE-enabled
                access interface
                ''',
                'access_interface_statistic',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            ],
            'Cisco-IOS-XR-subscriber-pppoe-ma-oper',
            'access-interface-statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-subscriber-pppoe-ma-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper'
        ),
    },
    'Pppoe.Nodes.Node.Statistics.PacketCounts.Padi' : {
        'meta_info' : _MetaInfoClass('Pppoe.Nodes.Node.Statistics.PacketCounts.Padi',
            False, 
            [
            _MetaInfoClassMember('dropped', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Dropped
                ''',
                'dropped',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('received', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Received
                ''',
                'received',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sent
                ''',
                'sent',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            ],
            'Cisco-IOS-XR-subscriber-pppoe-ma-oper',
            'padi',
            _yang_ns._namespaces['Cisco-IOS-XR-subscriber-pppoe-ma-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper'
        ),
    },
    'Pppoe.Nodes.Node.Statistics.PacketCounts.Pado' : {
        'meta_info' : _MetaInfoClass('Pppoe.Nodes.Node.Statistics.PacketCounts.Pado',
            False, 
            [
            _MetaInfoClassMember('dropped', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Dropped
                ''',
                'dropped',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('received', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Received
                ''',
                'received',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sent
                ''',
                'sent',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            ],
            'Cisco-IOS-XR-subscriber-pppoe-ma-oper',
            'pado',
            _yang_ns._namespaces['Cisco-IOS-XR-subscriber-pppoe-ma-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper'
        ),
    },
    'Pppoe.Nodes.Node.Statistics.PacketCounts.Padr' : {
        'meta_info' : _MetaInfoClass('Pppoe.Nodes.Node.Statistics.PacketCounts.Padr',
            False, 
            [
            _MetaInfoClassMember('dropped', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Dropped
                ''',
                'dropped',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('received', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Received
                ''',
                'received',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sent
                ''',
                'sent',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            ],
            'Cisco-IOS-XR-subscriber-pppoe-ma-oper',
            'padr',
            _yang_ns._namespaces['Cisco-IOS-XR-subscriber-pppoe-ma-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper'
        ),
    },
    'Pppoe.Nodes.Node.Statistics.PacketCounts.PadsSuccess' : {
        'meta_info' : _MetaInfoClass('Pppoe.Nodes.Node.Statistics.PacketCounts.PadsSuccess',
            False, 
            [
            _MetaInfoClassMember('dropped', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Dropped
                ''',
                'dropped',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('received', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Received
                ''',
                'received',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sent
                ''',
                'sent',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            ],
            'Cisco-IOS-XR-subscriber-pppoe-ma-oper',
            'pads-success',
            _yang_ns._namespaces['Cisco-IOS-XR-subscriber-pppoe-ma-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper'
        ),
    },
    'Pppoe.Nodes.Node.Statistics.PacketCounts.PadsError' : {
        'meta_info' : _MetaInfoClass('Pppoe.Nodes.Node.Statistics.PacketCounts.PadsError',
            False, 
            [
            _MetaInfoClassMember('dropped', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Dropped
                ''',
                'dropped',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('received', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Received
                ''',
                'received',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sent
                ''',
                'sent',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            ],
            'Cisco-IOS-XR-subscriber-pppoe-ma-oper',
            'pads-error',
            _yang_ns._namespaces['Cisco-IOS-XR-subscriber-pppoe-ma-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper'
        ),
    },
    'Pppoe.Nodes.Node.Statistics.PacketCounts.Padt' : {
        'meta_info' : _MetaInfoClass('Pppoe.Nodes.Node.Statistics.PacketCounts.Padt',
            False, 
            [
            _MetaInfoClassMember('dropped', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Dropped
                ''',
                'dropped',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('received', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Received
                ''',
                'received',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sent
                ''',
                'sent',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            ],
            'Cisco-IOS-XR-subscriber-pppoe-ma-oper',
            'padt',
            _yang_ns._namespaces['Cisco-IOS-XR-subscriber-pppoe-ma-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper'
        ),
    },
    'Pppoe.Nodes.Node.Statistics.PacketCounts.SessionState' : {
        'meta_info' : _MetaInfoClass('Pppoe.Nodes.Node.Statistics.PacketCounts.SessionState',
            False, 
            [
            _MetaInfoClassMember('dropped', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Dropped
                ''',
                'dropped',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('received', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Received
                ''',
                'received',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sent
                ''',
                'sent',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            ],
            'Cisco-IOS-XR-subscriber-pppoe-ma-oper',
            'session-state',
            _yang_ns._namespaces['Cisco-IOS-XR-subscriber-pppoe-ma-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper'
        ),
    },
    'Pppoe.Nodes.Node.Statistics.PacketCounts.Other' : {
        'meta_info' : _MetaInfoClass('Pppoe.Nodes.Node.Statistics.PacketCounts.Other',
            False, 
            [
            _MetaInfoClassMember('dropped', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Dropped
                ''',
                'dropped',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('received', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Received
                ''',
                'received',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sent
                ''',
                'sent',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            ],
            'Cisco-IOS-XR-subscriber-pppoe-ma-oper',
            'other',
            _yang_ns._namespaces['Cisco-IOS-XR-subscriber-pppoe-ma-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper'
        ),
    },
    'Pppoe.Nodes.Node.Statistics.PacketCounts' : {
        'meta_info' : _MetaInfoClass('Pppoe.Nodes.Node.Statistics.PacketCounts',
            False, 
            [
            _MetaInfoClassMember('other', REFERENCE_CLASS, 'Other' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper', 'Pppoe.Nodes.Node.Statistics.PacketCounts.Other', 
                [], [], 
                '''                Other counts
                ''',
                'other',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('padi', REFERENCE_CLASS, 'Padi' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper', 'Pppoe.Nodes.Node.Statistics.PacketCounts.Padi', 
                [], [], 
                '''                PADI counts
                ''',
                'padi',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('pado', REFERENCE_CLASS, 'Pado' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper', 'Pppoe.Nodes.Node.Statistics.PacketCounts.Pado', 
                [], [], 
                '''                PADO counts
                ''',
                'pado',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('padr', REFERENCE_CLASS, 'Padr' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper', 'Pppoe.Nodes.Node.Statistics.PacketCounts.Padr', 
                [], [], 
                '''                PADR counts
                ''',
                'padr',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('pads-error', REFERENCE_CLASS, 'PadsError' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper', 'Pppoe.Nodes.Node.Statistics.PacketCounts.PadsError', 
                [], [], 
                '''                PADS Error counts
                ''',
                'pads_error',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('pads-success', REFERENCE_CLASS, 'PadsSuccess' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper', 'Pppoe.Nodes.Node.Statistics.PacketCounts.PadsSuccess', 
                [], [], 
                '''                PADS Success counts
                ''',
                'pads_success',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('padt', REFERENCE_CLASS, 'Padt' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper', 'Pppoe.Nodes.Node.Statistics.PacketCounts.Padt', 
                [], [], 
                '''                PADT counts
                ''',
                'padt',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('session-state', REFERENCE_CLASS, 'SessionState' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper', 'Pppoe.Nodes.Node.Statistics.PacketCounts.SessionState', 
                [], [], 
                '''                Session Stage counts
                ''',
                'session_state',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            ],
            'Cisco-IOS-XR-subscriber-pppoe-ma-oper',
            'packet-counts',
            _yang_ns._namespaces['Cisco-IOS-XR-subscriber-pppoe-ma-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper'
        ),
    },
    'Pppoe.Nodes.Node.Statistics.PacketErrorCounts' : {
        'meta_info' : _MetaInfoClass('Pppoe.Nodes.Node.Statistics.PacketErrorCounts',
            False, 
            [
            _MetaInfoClassMember('bad-packet-length', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Bad packet length
                ''',
                'bad_packet_length',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('bad-tag-length-field', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Bad tag-length field
                ''',
                'bad_tag_length_field',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('bad-vendor-tag-length-field', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Bad vendor tag length field
                ''',
                'bad_vendor_tag_length_field',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('duplicate-host-uniq-tag-received', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Duplicate Host-Uniq tag received
                ''',
                'duplicate_host_uniq_tag_received',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('duplicate-relay-session-id-tag-received', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Duplicate Relay Session ID tag received
                ''',
                'duplicate_relay_session_id_tag_received',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('invalid-ale-tag', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Invalid ALE tag
                ''',
                'invalid_ale_tag',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('invalid-dsl-tag', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Invalid DSL tag
                ''',
                'invalid_dsl_tag',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('invalid-iana-code-invendor-tag', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Invalid IANA code in vendor tag
                ''',
                'invalid_iana_code_invendor_tag',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('invalid-iwf-tag', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Invalid IWF tag
                ''',
                'invalid_iwf_tag',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('invalid-max-payload-tag', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Invalid Max-Payload tag
                ''',
                'invalid_max_payload_tag',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('invalid-peer-mac', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Invalid Peer MAC
                ''',
                'invalid_peer_mac',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('invalid-service-name', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Invalid Service Name
                ''',
                'invalid_service_name',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('invalid-version-type-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Invalid version-type value
                ''',
                'invalid_version_type_value',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('invalid-vlan-tags', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Invalid VLAN Tags
                ''',
                'invalid_vlan_tags',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('multiple-ale-tags', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Multiple ALE tags
                ''',
                'multiple_ale_tags',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('multiple-circuit-id-tags', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Multiple Circuit-ID tags
                ''',
                'multiple_circuit_id_tags',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('multiple-host-uniq-tags', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Multiple Host-Uniq tags
                ''',
                'multiple_host_uniq_tags',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('multiple-iwf-tags', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Multiple IWF tags
                ''',
                'multiple_iwf_tags',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('multiple-max-payload-tags', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Multiple Max-Payload tags
                ''',
                'multiple_max_payload_tags',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('multiple-of-the-same-dsl-tag', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Multiple of the same DSL tag
                ''',
                'multiple_of_the_same_dsl_tag',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('multiple-relay-session-id-tags', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Multiple relay-session-id tags
                ''',
                'multiple_relay_session_id_tags',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('multiple-remote-id-tags', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Multiple Remote-ID tags
                ''',
                'multiple_remote_id_tags',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('multiple-service-name-tags', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Multiple Service-Name tags
                ''',
                'multiple_service_name_tags',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('multiple-vendor-specific-tags', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Multiple Vendor-specific tags
                ''',
                'multiple_vendor_specific_tags',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('no-iana-code-invendor-tag', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                No IANA code in vendor tag
                ''',
                'no_iana_code_invendor_tag',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('no-interface-handle', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                No interface handle
                ''',
                'no_interface_handle',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('no-packet-mac-address', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                No packet mac-address
                ''',
                'no_packet_mac_address',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('no-packet-payload', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                No packet payload
                ''',
                'no_packet_payload',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('no-service-name-tag', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                No Service-Name Tag
                ''',
                'no_service_name_tag',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('no-space-left-in-packet', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                No space left in packet
                ''',
                'no_space_left_in_packet',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('packet-on-srg-slave', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Packet Received on SRG Slave
                ''',
                'packet_on_srg_slave',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('packet-too-long', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Packet too long
                ''',
                'packet_too_long',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('pado-received', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                PADO received
                ''',
                'pado_received',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('pads-received', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                PADS received
                ''',
                'pads_received',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('padt-before-pads-sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                PADT before PADS sent
                ''',
                'padt_before_pads_sent',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('padt-for-unknown-session', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                PADT for unknown session
                ''',
                'padt_for_unknown_session',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('padt-with-wrong-peer-mac', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                PADT with wrong peer-mac
                ''',
                'padt_with_wrong_peer_mac',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('padt-with-wrong-vlan-tags', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                PADT with wrong VLAN tags
                ''',
                'padt_with_wrong_vlan_tags',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('session-stage-packet-for-unknown-session', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Session-stage packet for unknown session
                ''',
                'session_stage_packet_for_unknown_session',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('session-stage-packet-with-no-error', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Session-stage packet with no error
                ''',
                'session_stage_packet_with_no_error',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('session-stage-packet-with-wrong-mac', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Session-stage packet with wrong mac
                ''',
                'session_stage_packet_with_wrong_mac',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('session-stage-packet-with-wrong-vlan-tags', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Session-stage packet with wrong VLAN tags
                ''',
                'session_stage_packet_with_wrong_vlan_tags',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('tag-too-short', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Tag too short
                ''',
                'tag_too_short',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('unexpected-ac-name-tag', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Unexpected AC-Name tag
                ''',
                'unexpected_ac_name_tag',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('unexpected-error-tags', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Unexpected error tags
                ''',
                'unexpected_error_tags',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('unexpected-session-id-in-packet', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Unexpected Session-ID in packet
                ''',
                'unexpected_session_id_in_packet',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('unknown-interface', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Unknown interface
                ''',
                'unknown_interface',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('unknown-packet-type-received', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Unknown packet type received
                ''',
                'unknown_packet_type_received',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('unknown-tag-received', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Unknown tag received
                ''',
                'unknown_tag_received',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('unknownvendor-tag', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Unknown vendor-tag
                ''',
                'unknownvendor_tag',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('vendor-tag-too-short', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Vendor tag too short
                ''',
                'vendor_tag_too_short',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('zero-length-host-uniq', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Zero-length Host-Uniq tag
                ''',
                'zero_length_host_uniq',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            ],
            'Cisco-IOS-XR-subscriber-pppoe-ma-oper',
            'packet-error-counts',
            _yang_ns._namespaces['Cisco-IOS-XR-subscriber-pppoe-ma-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper'
        ),
    },
    'Pppoe.Nodes.Node.Statistics' : {
        'meta_info' : _MetaInfoClass('Pppoe.Nodes.Node.Statistics',
            False, 
            [
            _MetaInfoClassMember('packet-counts', REFERENCE_CLASS, 'PacketCounts' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper', 'Pppoe.Nodes.Node.Statistics.PacketCounts', 
                [], [], 
                '''                Packet Counts
                ''',
                'packet_counts',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('packet-error-counts', REFERENCE_CLASS, 'PacketErrorCounts' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper', 'Pppoe.Nodes.Node.Statistics.PacketErrorCounts', 
                [], [], 
                '''                Packet Error Counts
                ''',
                'packet_error_counts',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            ],
            'Cisco-IOS-XR-subscriber-pppoe-ma-oper',
            'statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-subscriber-pppoe-ma-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper'
        ),
    },
    'Pppoe.Nodes.Node.AccessInterface.Summaries.Summary' : {
        'meta_info' : _MetaInfoClass('Pppoe.Nodes.Node.AccessInterface.Summaries.Summary',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                PPPoE Access Interface
                ''',
                'interface_name',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', True),
            _MetaInfoClassMember('bba-group-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                BBA Group
                ''',
                'bba_group_name',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('incomplete-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Incomplete Session Count
                ''',
                'incomplete_sessions',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('interface-name-xr', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface
                ''',
                'interface_name_xr',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('interface-state', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Interface State
                ''',
                'interface_state',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('is-ready', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Is Ready
                ''',
                'is_ready',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('mac-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                Mac Address
                ''',
                'mac_address',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Session Count
                ''',
                'sessions',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            ],
            'Cisco-IOS-XR-subscriber-pppoe-ma-oper',
            'summary',
            _yang_ns._namespaces['Cisco-IOS-XR-subscriber-pppoe-ma-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper'
        ),
    },
    'Pppoe.Nodes.Node.AccessInterface.Summaries' : {
        'meta_info' : _MetaInfoClass('Pppoe.Nodes.Node.AccessInterface.Summaries',
            False, 
            [
            _MetaInfoClassMember('summary', REFERENCE_LIST, 'Summary' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper', 'Pppoe.Nodes.Node.AccessInterface.Summaries.Summary', 
                [], [], 
                '''                Summary information for a PPPoE-enabled
                access interface
                ''',
                'summary',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            ],
            'Cisco-IOS-XR-subscriber-pppoe-ma-oper',
            'summaries',
            _yang_ns._namespaces['Cisco-IOS-XR-subscriber-pppoe-ma-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper'
        ),
    },
    'Pppoe.Nodes.Node.AccessInterface' : {
        'meta_info' : _MetaInfoClass('Pppoe.Nodes.Node.AccessInterface',
            False, 
            [
            _MetaInfoClassMember('summaries', REFERENCE_CLASS, 'Summaries' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper', 'Pppoe.Nodes.Node.AccessInterface.Summaries', 
                [], [], 
                '''                PPPoE access interface summary information
                ''',
                'summaries',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            ],
            'Cisco-IOS-XR-subscriber-pppoe-ma-oper',
            'access-interface',
            _yang_ns._namespaces['Cisco-IOS-XR-subscriber-pppoe-ma-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper'
        ),
    },
    'Pppoe.Nodes.Node.Interfaces.Interface.Tags.AccessLoopEncapsulation' : {
        'meta_info' : _MetaInfoClass('Pppoe.Nodes.Node.Interfaces.Interface.Tags.AccessLoopEncapsulation',
            False, 
            [
            _MetaInfoClassMember('data-link', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Data Link
                ''',
                'data_link',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('encaps1', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Encaps 1
                ''',
                'encaps1',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('encaps2', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Encaps 2
                ''',
                'encaps2',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            ],
            'Cisco-IOS-XR-subscriber-pppoe-ma-oper',
            'access-loop-encapsulation',
            _yang_ns._namespaces['Cisco-IOS-XR-subscriber-pppoe-ma-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper'
        ),
    },
    'Pppoe.Nodes.Node.Interfaces.Interface.Tags' : {
        'meta_info' : _MetaInfoClass('Pppoe.Nodes.Node.Interfaces.Interface.Tags',
            False, 
            [
            _MetaInfoClassMember('access-loop-encapsulation', REFERENCE_CLASS, 'AccessLoopEncapsulation' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper', 'Pppoe.Nodes.Node.Interfaces.Interface.Tags.AccessLoopEncapsulation', 
                [], [], 
                '''                Access Loop Encapsulation
                ''',
                'access_loop_encapsulation',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('circuit-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Circuit ID
                ''',
                'circuit_id',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('dsl-actual-delay-down', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                DSL Actual Delay Down
                ''',
                'dsl_actual_delay_down',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('dsl-actual-delay-up', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                DSL Actual Delay Up
                ''',
                'dsl_actual_delay_up',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('dsl-actual-down', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                DSL Actual Down
                ''',
                'dsl_actual_down',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('dsl-actual-up', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                DSL Actual Up
                ''',
                'dsl_actual_up',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('dsl-attain-down', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                DSL Attain Down
                ''',
                'dsl_attain_down',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('dsl-attain-up', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                DSL Attain Up
                ''',
                'dsl_attain_up',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('dsl-max-delay-down', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                DSL Max Delay Down
                ''',
                'dsl_max_delay_down',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('dsl-max-delay-up', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                DSL Max Delay Up
                ''',
                'dsl_max_delay_up',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('dsl-max-down', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                DSL Max Down
                ''',
                'dsl_max_down',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('dsl-max-up', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                DSL Max Up
                ''',
                'dsl_max_up',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('dsl-min-down', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                DSL Min Down
                ''',
                'dsl_min_down',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('dsl-min-down-low', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                DSL Min Down Low
                ''',
                'dsl_min_down_low',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('dsl-min-up', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                DSL Min Up
                ''',
                'dsl_min_up',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('dsl-min-up-low', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                DSL Min Up Low
                ''',
                'dsl_min_up_low',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('host-uniq', ATTRIBUTE, 'str' , None, None, 
                [], [b'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                Host Uniq
                ''',
                'host_uniq',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('is-iwf', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Is IWF
                ''',
                'is_iwf',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('max-payload', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Max Payload
                ''',
                'max_payload',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('relay-session-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                Relay Session ID
                ''',
                'relay_session_id',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('remote-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Remote ID
                ''',
                'remote_id',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('service-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Service Name
                ''',
                'service_name',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            ],
            'Cisco-IOS-XR-subscriber-pppoe-ma-oper',
            'tags',
            _yang_ns._namespaces['Cisco-IOS-XR-subscriber-pppoe-ma-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper'
        ),
    },
    'Pppoe.Nodes.Node.Interfaces.Interface' : {
        'meta_info' : _MetaInfoClass('Pppoe.Nodes.Node.Interfaces.Interface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                PPPoE Interface
                ''',
                'interface_name',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', True),
            _MetaInfoClassMember('access-interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Access Interface
                ''',
                'access_interface_name',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('bba-group-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                BBA Group
                ''',
                'bba_group_name',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('interface-name-xr', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface
                ''',
                'interface_name_xr',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('is-complete', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Is Complete
                ''',
                'is_complete',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('local-mac-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                Local Mac-Address
                ''',
                'local_mac_address',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('peer-mac-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                Peer Mac-Address
                ''',
                'peer_mac_address',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('session-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Session ID
                ''',
                'session_id',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('srg-state', REFERENCE_ENUM_CLASS, 'PppoeMaSessionIdbSrgStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper', 'PppoeMaSessionIdbSrgStateEnum', 
                [], [], 
                '''                SRG state
                ''',
                'srg_state',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('tags', REFERENCE_CLASS, 'Tags' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper', 'Pppoe.Nodes.Node.Interfaces.Interface.Tags', 
                [], [], 
                '''                Tags
                ''',
                'tags',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('vlan-inner-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                VLAN Inner ID
                ''',
                'vlan_inner_id',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('vlan-outer-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                VLAN Outer ID
                ''',
                'vlan_outer_id',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            ],
            'Cisco-IOS-XR-subscriber-pppoe-ma-oper',
            'interface',
            _yang_ns._namespaces['Cisco-IOS-XR-subscriber-pppoe-ma-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper'
        ),
    },
    'Pppoe.Nodes.Node.Interfaces' : {
        'meta_info' : _MetaInfoClass('Pppoe.Nodes.Node.Interfaces',
            False, 
            [
            _MetaInfoClassMember('interface', REFERENCE_LIST, 'Interface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper', 'Pppoe.Nodes.Node.Interfaces.Interface', 
                [], [], 
                '''                Data for a PPPoE interface
                ''',
                'interface',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            ],
            'Cisco-IOS-XR-subscriber-pppoe-ma-oper',
            'interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-subscriber-pppoe-ma-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper'
        ),
    },
    'Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.Card' : {
        'meta_info' : _MetaInfoClass('Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.Card',
            False, 
            [
            _MetaInfoClassMember('max-limit', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Max Limit
                ''',
                'max_limit',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('radius-override-enabled', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Radius override is enabled
                ''',
                'radius_override_enabled',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('threshold', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold
                ''',
                'threshold',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            ],
            'Cisco-IOS-XR-subscriber-pppoe-ma-oper',
            'card',
            _yang_ns._namespaces['Cisco-IOS-XR-subscriber-pppoe-ma-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper'
        ),
    },
    'Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.AccessIntf' : {
        'meta_info' : _MetaInfoClass('Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.AccessIntf',
            False, 
            [
            _MetaInfoClassMember('max-limit', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Max Limit
                ''',
                'max_limit',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('radius-override-enabled', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Radius override is enabled
                ''',
                'radius_override_enabled',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('threshold', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold
                ''',
                'threshold',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            ],
            'Cisco-IOS-XR-subscriber-pppoe-ma-oper',
            'access-intf',
            _yang_ns._namespaces['Cisco-IOS-XR-subscriber-pppoe-ma-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper'
        ),
    },
    'Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.Mac' : {
        'meta_info' : _MetaInfoClass('Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.Mac',
            False, 
            [
            _MetaInfoClassMember('max-limit', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Max Limit
                ''',
                'max_limit',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('radius-override-enabled', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Radius override is enabled
                ''',
                'radius_override_enabled',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('threshold', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold
                ''',
                'threshold',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            ],
            'Cisco-IOS-XR-subscriber-pppoe-ma-oper',
            'mac',
            _yang_ns._namespaces['Cisco-IOS-XR-subscriber-pppoe-ma-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper'
        ),
    },
    'Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.MacIwf' : {
        'meta_info' : _MetaInfoClass('Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.MacIwf',
            False, 
            [
            _MetaInfoClassMember('max-limit', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Max Limit
                ''',
                'max_limit',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('radius-override-enabled', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Radius override is enabled
                ''',
                'radius_override_enabled',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('threshold', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold
                ''',
                'threshold',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            ],
            'Cisco-IOS-XR-subscriber-pppoe-ma-oper',
            'mac-iwf',
            _yang_ns._namespaces['Cisco-IOS-XR-subscriber-pppoe-ma-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper'
        ),
    },
    'Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.MacAccessInterface' : {
        'meta_info' : _MetaInfoClass('Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.MacAccessInterface',
            False, 
            [
            _MetaInfoClassMember('max-limit', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Max Limit
                ''',
                'max_limit',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('radius-override-enabled', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Radius override is enabled
                ''',
                'radius_override_enabled',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('threshold', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold
                ''',
                'threshold',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            ],
            'Cisco-IOS-XR-subscriber-pppoe-ma-oper',
            'mac-access-interface',
            _yang_ns._namespaces['Cisco-IOS-XR-subscriber-pppoe-ma-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper'
        ),
    },
    'Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.MacIwfAccessInterface' : {
        'meta_info' : _MetaInfoClass('Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.MacIwfAccessInterface',
            False, 
            [
            _MetaInfoClassMember('max-limit', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Max Limit
                ''',
                'max_limit',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('radius-override-enabled', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Radius override is enabled
                ''',
                'radius_override_enabled',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('threshold', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold
                ''',
                'threshold',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            ],
            'Cisco-IOS-XR-subscriber-pppoe-ma-oper',
            'mac-iwf-access-interface',
            _yang_ns._namespaces['Cisco-IOS-XR-subscriber-pppoe-ma-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper'
        ),
    },
    'Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.CircuitId' : {
        'meta_info' : _MetaInfoClass('Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.CircuitId',
            False, 
            [
            _MetaInfoClassMember('max-limit', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Max Limit
                ''',
                'max_limit',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('radius-override-enabled', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Radius override is enabled
                ''',
                'radius_override_enabled',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('threshold', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold
                ''',
                'threshold',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            ],
            'Cisco-IOS-XR-subscriber-pppoe-ma-oper',
            'circuit-id',
            _yang_ns._namespaces['Cisco-IOS-XR-subscriber-pppoe-ma-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper'
        ),
    },
    'Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.RemoteId' : {
        'meta_info' : _MetaInfoClass('Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.RemoteId',
            False, 
            [
            _MetaInfoClassMember('max-limit', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Max Limit
                ''',
                'max_limit',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('radius-override-enabled', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Radius override is enabled
                ''',
                'radius_override_enabled',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('threshold', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold
                ''',
                'threshold',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            ],
            'Cisco-IOS-XR-subscriber-pppoe-ma-oper',
            'remote-id',
            _yang_ns._namespaces['Cisco-IOS-XR-subscriber-pppoe-ma-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper'
        ),
    },
    'Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.CircuitIdAndRemoteId' : {
        'meta_info' : _MetaInfoClass('Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.CircuitIdAndRemoteId',
            False, 
            [
            _MetaInfoClassMember('max-limit', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Max Limit
                ''',
                'max_limit',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('radius-override-enabled', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Radius override is enabled
                ''',
                'radius_override_enabled',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('threshold', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold
                ''',
                'threshold',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            ],
            'Cisco-IOS-XR-subscriber-pppoe-ma-oper',
            'circuit-id-and-remote-id',
            _yang_ns._namespaces['Cisco-IOS-XR-subscriber-pppoe-ma-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper'
        ),
    },
    'Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.OuterVlanId' : {
        'meta_info' : _MetaInfoClass('Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.OuterVlanId',
            False, 
            [
            _MetaInfoClassMember('max-limit', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Max Limit
                ''',
                'max_limit',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('radius-override-enabled', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Radius override is enabled
                ''',
                'radius_override_enabled',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('threshold', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold
                ''',
                'threshold',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            ],
            'Cisco-IOS-XR-subscriber-pppoe-ma-oper',
            'outer-vlan-id',
            _yang_ns._namespaces['Cisco-IOS-XR-subscriber-pppoe-ma-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper'
        ),
    },
    'Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.InnerVlanId' : {
        'meta_info' : _MetaInfoClass('Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.InnerVlanId',
            False, 
            [
            _MetaInfoClassMember('max-limit', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Max Limit
                ''',
                'max_limit',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('radius-override-enabled', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Radius override is enabled
                ''',
                'radius_override_enabled',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('threshold', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold
                ''',
                'threshold',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            ],
            'Cisco-IOS-XR-subscriber-pppoe-ma-oper',
            'inner-vlan-id',
            _yang_ns._namespaces['Cisco-IOS-XR-subscriber-pppoe-ma-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper'
        ),
    },
    'Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.VlanId' : {
        'meta_info' : _MetaInfoClass('Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.VlanId',
            False, 
            [
            _MetaInfoClassMember('max-limit', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Max Limit
                ''',
                'max_limit',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('radius-override-enabled', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Radius override is enabled
                ''',
                'radius_override_enabled',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('threshold', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold
                ''',
                'threshold',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            ],
            'Cisco-IOS-XR-subscriber-pppoe-ma-oper',
            'vlan-id',
            _yang_ns._namespaces['Cisco-IOS-XR-subscriber-pppoe-ma-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper'
        ),
    },
    'Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig' : {
        'meta_info' : _MetaInfoClass('Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig',
            False, 
            [
            _MetaInfoClassMember('access-intf', REFERENCE_CLASS, 'AccessIntf' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper', 'Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.AccessIntf', 
                [], [], 
                '''                Access Interface
                ''',
                'access_intf',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('card', REFERENCE_CLASS, 'Card' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper', 'Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.Card', 
                [], [], 
                '''                Card
                ''',
                'card',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('circuit-id', REFERENCE_CLASS, 'CircuitId' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper', 'Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.CircuitId', 
                [], [], 
                '''                Circuit ID
                ''',
                'circuit_id',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('circuit-id-and-remote-id', REFERENCE_CLASS, 'CircuitIdAndRemoteId' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper', 'Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.CircuitIdAndRemoteId', 
                [], [], 
                '''                Circuit ID and Remote ID
                ''',
                'circuit_id_and_remote_id',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('inner-vlan-id', REFERENCE_CLASS, 'InnerVlanId' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper', 'Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.InnerVlanId', 
                [], [], 
                '''                Inner VLAN ID
                ''',
                'inner_vlan_id',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('mac', REFERENCE_CLASS, 'Mac' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper', 'Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.Mac', 
                [], [], 
                '''                MAC
                ''',
                'mac',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('mac-access-interface', REFERENCE_CLASS, 'MacAccessInterface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper', 'Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.MacAccessInterface', 
                [], [], 
                '''                MAC Access Interface
                ''',
                'mac_access_interface',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('mac-iwf', REFERENCE_CLASS, 'MacIwf' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper', 'Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.MacIwf', 
                [], [], 
                '''                MAC IWF
                ''',
                'mac_iwf',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('mac-iwf-access-interface', REFERENCE_CLASS, 'MacIwfAccessInterface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper', 'Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.MacIwfAccessInterface', 
                [], [], 
                '''                MAC IWF Access Interface
                ''',
                'mac_iwf_access_interface',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('outer-vlan-id', REFERENCE_CLASS, 'OuterVlanId' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper', 'Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.OuterVlanId', 
                [], [], 
                '''                Outer VLAN ID
                ''',
                'outer_vlan_id',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('remote-id', REFERENCE_CLASS, 'RemoteId' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper', 'Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.RemoteId', 
                [], [], 
                '''                Remote ID
                ''',
                'remote_id',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('vlan-id', REFERENCE_CLASS, 'VlanId' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper', 'Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.VlanId', 
                [], [], 
                '''                VLAN ID
                ''',
                'vlan_id',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            ],
            'Cisco-IOS-XR-subscriber-pppoe-ma-oper',
            'limit-config',
            _yang_ns._namespaces['Cisco-IOS-XR-subscriber-pppoe-ma-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper'
        ),
    },
    'Pppoe.Nodes.Node.BbaGroups.BbaGroup.Limits.Limit' : {
        'meta_info' : _MetaInfoClass('Pppoe.Nodes.Node.BbaGroups.BbaGroup.Limits.Limit',
            False, 
            [
            _MetaInfoClassMember('circuit-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Circuit ID
                ''',
                'circuit_id',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('inner-vlan-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4095')], [], 
                '''                Inner VLAN ID
                ''',
                'inner_vlan_id',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Access Interface
                ''',
                'interface_name',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('iwf', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                IWF flag
                ''',
                'iwf',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('mac-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                MAC address
                ''',
                'mac_address',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('outer-vlan-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4095')], [], 
                '''                Outer VLAN ID
                ''',
                'outer_vlan_id',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('override-limit', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Overridden limit if set
                ''',
                'override_limit',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('radius-override-set', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Overridden limit has been set
                ''',
                'radius_override_set',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('remote-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Remote ID
                ''',
                'remote_id',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('session-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Session Count
                ''',
                'session_count',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('state', REFERENCE_ENUM_CLASS, 'PppoeMaLimitStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper', 'PppoeMaLimitStateEnum', 
                [], [], 
                '''                State
                ''',
                'state',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            ],
            'Cisco-IOS-XR-subscriber-pppoe-ma-oper',
            'limit',
            _yang_ns._namespaces['Cisco-IOS-XR-subscriber-pppoe-ma-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper'
        ),
    },
    'Pppoe.Nodes.Node.BbaGroups.BbaGroup.Limits' : {
        'meta_info' : _MetaInfoClass('Pppoe.Nodes.Node.BbaGroups.BbaGroup.Limits',
            False, 
            [
            _MetaInfoClassMember('limit', REFERENCE_LIST, 'Limit' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper', 'Pppoe.Nodes.Node.BbaGroups.BbaGroup.Limits.Limit', 
                [], [], 
                '''                PPPoE session limit state
                ''',
                'limit',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            ],
            'Cisco-IOS-XR-subscriber-pppoe-ma-oper',
            'limits',
            _yang_ns._namespaces['Cisco-IOS-XR-subscriber-pppoe-ma-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper'
        ),
    },
    'Pppoe.Nodes.Node.BbaGroups.BbaGroup.Throttles.Throttle' : {
        'meta_info' : _MetaInfoClass('Pppoe.Nodes.Node.BbaGroups.BbaGroup.Throttles.Throttle',
            False, 
            [
            _MetaInfoClassMember('circuit-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Circuit ID
                ''',
                'circuit_id',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('inner-vlan-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4095')], [], 
                '''                Inner VLAN ID
                ''',
                'inner_vlan_id',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Access Interface
                ''',
                'interface_name',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('iwf', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                IWF flag
                ''',
                'iwf',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('mac-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                MAC address
                ''',
                'mac_address',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('outer-vlan-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4095')], [], 
                '''                Outer VLAN ID
                ''',
                'outer_vlan_id',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('padi-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                PADI Count
                ''',
                'padi_count',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('padr-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                PADR Count
                ''',
                'padr_count',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('remote-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Remote ID
                ''',
                'remote_id',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('since-reset', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of seconds since counters reset
                ''',
                'since_reset',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('state', REFERENCE_ENUM_CLASS, 'PppoeMaThrottleStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper', 'PppoeMaThrottleStateEnum', 
                [], [], 
                '''                State
                ''',
                'state',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('time-left', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Time left in seconds
                ''',
                'time_left',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            ],
            'Cisco-IOS-XR-subscriber-pppoe-ma-oper',
            'throttle',
            _yang_ns._namespaces['Cisco-IOS-XR-subscriber-pppoe-ma-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper'
        ),
    },
    'Pppoe.Nodes.Node.BbaGroups.BbaGroup.Throttles' : {
        'meta_info' : _MetaInfoClass('Pppoe.Nodes.Node.BbaGroups.BbaGroup.Throttles',
            False, 
            [
            _MetaInfoClassMember('throttle', REFERENCE_LIST, 'Throttle' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper', 'Pppoe.Nodes.Node.BbaGroups.BbaGroup.Throttles.Throttle', 
                [], [], 
                '''                PPPoE session throttle state
                ''',
                'throttle',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            ],
            'Cisco-IOS-XR-subscriber-pppoe-ma-oper',
            'throttles',
            _yang_ns._namespaces['Cisco-IOS-XR-subscriber-pppoe-ma-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper'
        ),
    },
    'Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.Mac' : {
        'meta_info' : _MetaInfoClass('Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.Mac',
            False, 
            [
            _MetaInfoClassMember('blocking-period', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Blocking Period
                ''',
                'blocking_period',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('limit', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Limit
                ''',
                'limit',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('request-period', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Request Period
                ''',
                'request_period',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            ],
            'Cisco-IOS-XR-subscriber-pppoe-ma-oper',
            'mac',
            _yang_ns._namespaces['Cisco-IOS-XR-subscriber-pppoe-ma-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper'
        ),
    },
    'Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.MacAccessInterface' : {
        'meta_info' : _MetaInfoClass('Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.MacAccessInterface',
            False, 
            [
            _MetaInfoClassMember('blocking-period', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Blocking Period
                ''',
                'blocking_period',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('limit', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Limit
                ''',
                'limit',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('request-period', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Request Period
                ''',
                'request_period',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            ],
            'Cisco-IOS-XR-subscriber-pppoe-ma-oper',
            'mac-access-interface',
            _yang_ns._namespaces['Cisco-IOS-XR-subscriber-pppoe-ma-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper'
        ),
    },
    'Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.MacIwfAccessInterface' : {
        'meta_info' : _MetaInfoClass('Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.MacIwfAccessInterface',
            False, 
            [
            _MetaInfoClassMember('blocking-period', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Blocking Period
                ''',
                'blocking_period',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('limit', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Limit
                ''',
                'limit',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('request-period', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Request Period
                ''',
                'request_period',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            ],
            'Cisco-IOS-XR-subscriber-pppoe-ma-oper',
            'mac-iwf-access-interface',
            _yang_ns._namespaces['Cisco-IOS-XR-subscriber-pppoe-ma-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper'
        ),
    },
    'Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.CircuitId' : {
        'meta_info' : _MetaInfoClass('Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.CircuitId',
            False, 
            [
            _MetaInfoClassMember('blocking-period', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Blocking Period
                ''',
                'blocking_period',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('limit', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Limit
                ''',
                'limit',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('request-period', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Request Period
                ''',
                'request_period',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            ],
            'Cisco-IOS-XR-subscriber-pppoe-ma-oper',
            'circuit-id',
            _yang_ns._namespaces['Cisco-IOS-XR-subscriber-pppoe-ma-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper'
        ),
    },
    'Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.RemoteId' : {
        'meta_info' : _MetaInfoClass('Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.RemoteId',
            False, 
            [
            _MetaInfoClassMember('blocking-period', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Blocking Period
                ''',
                'blocking_period',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('limit', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Limit
                ''',
                'limit',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('request-period', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Request Period
                ''',
                'request_period',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            ],
            'Cisco-IOS-XR-subscriber-pppoe-ma-oper',
            'remote-id',
            _yang_ns._namespaces['Cisco-IOS-XR-subscriber-pppoe-ma-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper'
        ),
    },
    'Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.CircuitIdAndRemoteId' : {
        'meta_info' : _MetaInfoClass('Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.CircuitIdAndRemoteId',
            False, 
            [
            _MetaInfoClassMember('blocking-period', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Blocking Period
                ''',
                'blocking_period',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('limit', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Limit
                ''',
                'limit',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('request-period', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Request Period
                ''',
                'request_period',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            ],
            'Cisco-IOS-XR-subscriber-pppoe-ma-oper',
            'circuit-id-and-remote-id',
            _yang_ns._namespaces['Cisco-IOS-XR-subscriber-pppoe-ma-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper'
        ),
    },
    'Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.OuterVlanId' : {
        'meta_info' : _MetaInfoClass('Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.OuterVlanId',
            False, 
            [
            _MetaInfoClassMember('blocking-period', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Blocking Period
                ''',
                'blocking_period',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('limit', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Limit
                ''',
                'limit',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('request-period', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Request Period
                ''',
                'request_period',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            ],
            'Cisco-IOS-XR-subscriber-pppoe-ma-oper',
            'outer-vlan-id',
            _yang_ns._namespaces['Cisco-IOS-XR-subscriber-pppoe-ma-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper'
        ),
    },
    'Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.InnerVlanId' : {
        'meta_info' : _MetaInfoClass('Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.InnerVlanId',
            False, 
            [
            _MetaInfoClassMember('blocking-period', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Blocking Period
                ''',
                'blocking_period',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('limit', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Limit
                ''',
                'limit',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('request-period', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Request Period
                ''',
                'request_period',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            ],
            'Cisco-IOS-XR-subscriber-pppoe-ma-oper',
            'inner-vlan-id',
            _yang_ns._namespaces['Cisco-IOS-XR-subscriber-pppoe-ma-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper'
        ),
    },
    'Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.VlanId' : {
        'meta_info' : _MetaInfoClass('Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.VlanId',
            False, 
            [
            _MetaInfoClassMember('blocking-period', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Blocking Period
                ''',
                'blocking_period',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('limit', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Limit
                ''',
                'limit',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('request-period', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Request Period
                ''',
                'request_period',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            ],
            'Cisco-IOS-XR-subscriber-pppoe-ma-oper',
            'vlan-id',
            _yang_ns._namespaces['Cisco-IOS-XR-subscriber-pppoe-ma-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper'
        ),
    },
    'Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig' : {
        'meta_info' : _MetaInfoClass('Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig',
            False, 
            [
            _MetaInfoClassMember('circuit-id', REFERENCE_CLASS, 'CircuitId' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper', 'Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.CircuitId', 
                [], [], 
                '''                Circuit ID
                ''',
                'circuit_id',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('circuit-id-and-remote-id', REFERENCE_CLASS, 'CircuitIdAndRemoteId' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper', 'Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.CircuitIdAndRemoteId', 
                [], [], 
                '''                Circuit ID and Remote ID
                ''',
                'circuit_id_and_remote_id',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('inner-vlan-id', REFERENCE_CLASS, 'InnerVlanId' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper', 'Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.InnerVlanId', 
                [], [], 
                '''                Inner VLAN ID
                ''',
                'inner_vlan_id',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('mac', REFERENCE_CLASS, 'Mac' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper', 'Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.Mac', 
                [], [], 
                '''                MAC
                ''',
                'mac',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('mac-access-interface', REFERENCE_CLASS, 'MacAccessInterface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper', 'Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.MacAccessInterface', 
                [], [], 
                '''                MAC Access Interface
                ''',
                'mac_access_interface',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('mac-iwf-access-interface', REFERENCE_CLASS, 'MacIwfAccessInterface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper', 'Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.MacIwfAccessInterface', 
                [], [], 
                '''                MAC IWF Access Interface
                ''',
                'mac_iwf_access_interface',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('outer-vlan-id', REFERENCE_CLASS, 'OuterVlanId' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper', 'Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.OuterVlanId', 
                [], [], 
                '''                Outer VLAN ID
                ''',
                'outer_vlan_id',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('remote-id', REFERENCE_CLASS, 'RemoteId' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper', 'Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.RemoteId', 
                [], [], 
                '''                Remote ID
                ''',
                'remote_id',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('vlan-id', REFERENCE_CLASS, 'VlanId' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper', 'Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.VlanId', 
                [], [], 
                '''                VLAN ID
                ''',
                'vlan_id',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            ],
            'Cisco-IOS-XR-subscriber-pppoe-ma-oper',
            'throttle-config',
            _yang_ns._namespaces['Cisco-IOS-XR-subscriber-pppoe-ma-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper'
        ),
    },
    'Pppoe.Nodes.Node.BbaGroups.BbaGroup' : {
        'meta_info' : _MetaInfoClass('Pppoe.Nodes.Node.BbaGroups.BbaGroup',
            False, 
            [
            _MetaInfoClassMember('bba-group-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                BBA Group
                ''',
                'bba_group_name',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', True),
            _MetaInfoClassMember('limit-config', REFERENCE_CLASS, 'LimitConfig' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper', 'Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig', 
                [], [], 
                '''                BBA-Group limit configuration information
                ''',
                'limit_config',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('limits', REFERENCE_CLASS, 'Limits' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper', 'Pppoe.Nodes.Node.BbaGroups.BbaGroup.Limits', 
                [], [], 
                '''                PPPoE session limit information
                ''',
                'limits',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('throttle-config', REFERENCE_CLASS, 'ThrottleConfig' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper', 'Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig', 
                [], [], 
                '''                BBA-Group throttle configuration information
                ''',
                'throttle_config',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('throttles', REFERENCE_CLASS, 'Throttles' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper', 'Pppoe.Nodes.Node.BbaGroups.BbaGroup.Throttles', 
                [], [], 
                '''                PPPoE throttle information
                ''',
                'throttles',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            ],
            'Cisco-IOS-XR-subscriber-pppoe-ma-oper',
            'bba-group',
            _yang_ns._namespaces['Cisco-IOS-XR-subscriber-pppoe-ma-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper'
        ),
    },
    'Pppoe.Nodes.Node.BbaGroups' : {
        'meta_info' : _MetaInfoClass('Pppoe.Nodes.Node.BbaGroups',
            False, 
            [
            _MetaInfoClassMember('bba-group', REFERENCE_LIST, 'BbaGroup' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper', 'Pppoe.Nodes.Node.BbaGroups.BbaGroup', 
                [], [], 
                '''                PPPoE BBA-Group information
                ''',
                'bba_group',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            ],
            'Cisco-IOS-XR-subscriber-pppoe-ma-oper',
            'bba-groups',
            _yang_ns._namespaces['Cisco-IOS-XR-subscriber-pppoe-ma-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper'
        ),
    },
    'Pppoe.Nodes.Node.SummaryTotal' : {
        'meta_info' : _MetaInfoClass('Pppoe.Nodes.Node.SummaryTotal',
            False, 
            [
            _MetaInfoClassMember('complete-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Complete Session Count
                ''',
                'complete_sessions',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('flow-control-disconnected-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Flow Control Disconnected Count
                ''',
                'flow_control_disconnected_sessions',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('flow-control-dropped-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Flow Control Drop Count
                ''',
                'flow_control_dropped_sessions',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('flow-control-in-flight-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Flow Control In-Flight Count
                ''',
                'flow_control_in_flight_sessions',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('flow-control-limit', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Flow Control credit limit
                ''',
                'flow_control_limit',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('flow-control-successful-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Flow Control Success Count, sessions completing
                call flow
                ''',
                'flow_control_successful_sessions',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('incomplete-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Incomplete Session Count
                ''',
                'incomplete_sessions',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('not-ready-access-interfaces', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Not Ready Access Interface Count
                ''',
                'not_ready_access_interfaces',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('pppoema-subscriber-infra-flow-control', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                PPPoEMASubscriberInfraFlowControl
                ''',
                'pppoema_subscriber_infra_flow_control',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('ready-access-interfaces', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Ready Access Interface Count
                ''',
                'ready_access_interfaces',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            ],
            'Cisco-IOS-XR-subscriber-pppoe-ma-oper',
            'summary-total',
            _yang_ns._namespaces['Cisco-IOS-XR-subscriber-pppoe-ma-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper'
        ),
    },
    'Pppoe.Nodes.Node' : {
        'meta_info' : _MetaInfoClass('Pppoe.Nodes.Node',
            False, 
            [
            _MetaInfoClassMember('node-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Node
                ''',
                'node_name',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', True),
            _MetaInfoClassMember('access-interface', REFERENCE_CLASS, 'AccessInterface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper', 'Pppoe.Nodes.Node.AccessInterface', 
                [], [], 
                '''                PPPoE access interface information
                ''',
                'access_interface',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('bba-groups', REFERENCE_CLASS, 'BbaGroups' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper', 'Pppoe.Nodes.Node.BbaGroups', 
                [], [], 
                '''                PPPoE BBA-Group information
                ''',
                'bba_groups',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('interfaces', REFERENCE_CLASS, 'Interfaces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper', 'Pppoe.Nodes.Node.Interfaces', 
                [], [], 
                '''                Per interface PPPoE operational data
                ''',
                'interfaces',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('statistics', REFERENCE_CLASS, 'Statistics' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper', 'Pppoe.Nodes.Node.Statistics', 
                [], [], 
                '''                PPPoE statistics for a given node
                ''',
                'statistics',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('summary-total', REFERENCE_CLASS, 'SummaryTotal' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper', 'Pppoe.Nodes.Node.SummaryTotal', 
                [], [], 
                '''                PPPoE statistics for a given node
                ''',
                'summary_total',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            ],
            'Cisco-IOS-XR-subscriber-pppoe-ma-oper',
            'node',
            _yang_ns._namespaces['Cisco-IOS-XR-subscriber-pppoe-ma-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper'
        ),
    },
    'Pppoe.Nodes' : {
        'meta_info' : _MetaInfoClass('Pppoe.Nodes',
            False, 
            [
            _MetaInfoClassMember('node', REFERENCE_LIST, 'Node' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper', 'Pppoe.Nodes.Node', 
                [], [], 
                '''                PPPoE operational data for a particular node
                ''',
                'node',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            ],
            'Cisco-IOS-XR-subscriber-pppoe-ma-oper',
            'nodes',
            _yang_ns._namespaces['Cisco-IOS-XR-subscriber-pppoe-ma-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper'
        ),
    },
    'Pppoe' : {
        'meta_info' : _MetaInfoClass('Pppoe',
            False, 
            [
            _MetaInfoClassMember('access-interface-statistics', REFERENCE_CLASS, 'AccessInterfaceStatistics' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper', 'Pppoe.AccessInterfaceStatistics', 
                [], [], 
                '''                PPPoE access interface statistics information
                ''',
                'access_interface_statistics',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            _MetaInfoClassMember('nodes', REFERENCE_CLASS, 'Nodes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper', 'Pppoe.Nodes', 
                [], [], 
                '''                Per-node PPPoE operational data
                ''',
                'nodes',
                'Cisco-IOS-XR-subscriber-pppoe-ma-oper', False),
            ],
            'Cisco-IOS-XR-subscriber-pppoe-ma-oper',
            'pppoe',
            _yang_ns._namespaces['Cisco-IOS-XR-subscriber-pppoe-ma-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_pppoe_ma_oper'
        ),
    },
}
_meta_table['Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.Padi']['meta_info'].parent =_meta_table['Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts']['meta_info']
_meta_table['Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.Pado']['meta_info'].parent =_meta_table['Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts']['meta_info']
_meta_table['Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.Padr']['meta_info'].parent =_meta_table['Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts']['meta_info']
_meta_table['Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.PadsSuccess']['meta_info'].parent =_meta_table['Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts']['meta_info']
_meta_table['Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.PadsError']['meta_info'].parent =_meta_table['Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts']['meta_info']
_meta_table['Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.Padt']['meta_info'].parent =_meta_table['Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts']['meta_info']
_meta_table['Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.SessionState']['meta_info'].parent =_meta_table['Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts']['meta_info']
_meta_table['Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts.Other']['meta_info'].parent =_meta_table['Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts']['meta_info']
_meta_table['Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic.PacketCounts']['meta_info'].parent =_meta_table['Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic']['meta_info']
_meta_table['Pppoe.AccessInterfaceStatistics.AccessInterfaceStatistic']['meta_info'].parent =_meta_table['Pppoe.AccessInterfaceStatistics']['meta_info']
_meta_table['Pppoe.Nodes.Node.Statistics.PacketCounts.Padi']['meta_info'].parent =_meta_table['Pppoe.Nodes.Node.Statistics.PacketCounts']['meta_info']
_meta_table['Pppoe.Nodes.Node.Statistics.PacketCounts.Pado']['meta_info'].parent =_meta_table['Pppoe.Nodes.Node.Statistics.PacketCounts']['meta_info']
_meta_table['Pppoe.Nodes.Node.Statistics.PacketCounts.Padr']['meta_info'].parent =_meta_table['Pppoe.Nodes.Node.Statistics.PacketCounts']['meta_info']
_meta_table['Pppoe.Nodes.Node.Statistics.PacketCounts.PadsSuccess']['meta_info'].parent =_meta_table['Pppoe.Nodes.Node.Statistics.PacketCounts']['meta_info']
_meta_table['Pppoe.Nodes.Node.Statistics.PacketCounts.PadsError']['meta_info'].parent =_meta_table['Pppoe.Nodes.Node.Statistics.PacketCounts']['meta_info']
_meta_table['Pppoe.Nodes.Node.Statistics.PacketCounts.Padt']['meta_info'].parent =_meta_table['Pppoe.Nodes.Node.Statistics.PacketCounts']['meta_info']
_meta_table['Pppoe.Nodes.Node.Statistics.PacketCounts.SessionState']['meta_info'].parent =_meta_table['Pppoe.Nodes.Node.Statistics.PacketCounts']['meta_info']
_meta_table['Pppoe.Nodes.Node.Statistics.PacketCounts.Other']['meta_info'].parent =_meta_table['Pppoe.Nodes.Node.Statistics.PacketCounts']['meta_info']
_meta_table['Pppoe.Nodes.Node.Statistics.PacketCounts']['meta_info'].parent =_meta_table['Pppoe.Nodes.Node.Statistics']['meta_info']
_meta_table['Pppoe.Nodes.Node.Statistics.PacketErrorCounts']['meta_info'].parent =_meta_table['Pppoe.Nodes.Node.Statistics']['meta_info']
_meta_table['Pppoe.Nodes.Node.AccessInterface.Summaries.Summary']['meta_info'].parent =_meta_table['Pppoe.Nodes.Node.AccessInterface.Summaries']['meta_info']
_meta_table['Pppoe.Nodes.Node.AccessInterface.Summaries']['meta_info'].parent =_meta_table['Pppoe.Nodes.Node.AccessInterface']['meta_info']
_meta_table['Pppoe.Nodes.Node.Interfaces.Interface.Tags.AccessLoopEncapsulation']['meta_info'].parent =_meta_table['Pppoe.Nodes.Node.Interfaces.Interface.Tags']['meta_info']
_meta_table['Pppoe.Nodes.Node.Interfaces.Interface.Tags']['meta_info'].parent =_meta_table['Pppoe.Nodes.Node.Interfaces.Interface']['meta_info']
_meta_table['Pppoe.Nodes.Node.Interfaces.Interface']['meta_info'].parent =_meta_table['Pppoe.Nodes.Node.Interfaces']['meta_info']
_meta_table['Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.Card']['meta_info'].parent =_meta_table['Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig']['meta_info']
_meta_table['Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.AccessIntf']['meta_info'].parent =_meta_table['Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig']['meta_info']
_meta_table['Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.Mac']['meta_info'].parent =_meta_table['Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig']['meta_info']
_meta_table['Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.MacIwf']['meta_info'].parent =_meta_table['Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig']['meta_info']
_meta_table['Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.MacAccessInterface']['meta_info'].parent =_meta_table['Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig']['meta_info']
_meta_table['Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.MacIwfAccessInterface']['meta_info'].parent =_meta_table['Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig']['meta_info']
_meta_table['Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.CircuitId']['meta_info'].parent =_meta_table['Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig']['meta_info']
_meta_table['Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.RemoteId']['meta_info'].parent =_meta_table['Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig']['meta_info']
_meta_table['Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.CircuitIdAndRemoteId']['meta_info'].parent =_meta_table['Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig']['meta_info']
_meta_table['Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.OuterVlanId']['meta_info'].parent =_meta_table['Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig']['meta_info']
_meta_table['Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.InnerVlanId']['meta_info'].parent =_meta_table['Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig']['meta_info']
_meta_table['Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig.VlanId']['meta_info'].parent =_meta_table['Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig']['meta_info']
_meta_table['Pppoe.Nodes.Node.BbaGroups.BbaGroup.Limits.Limit']['meta_info'].parent =_meta_table['Pppoe.Nodes.Node.BbaGroups.BbaGroup.Limits']['meta_info']
_meta_table['Pppoe.Nodes.Node.BbaGroups.BbaGroup.Throttles.Throttle']['meta_info'].parent =_meta_table['Pppoe.Nodes.Node.BbaGroups.BbaGroup.Throttles']['meta_info']
_meta_table['Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.Mac']['meta_info'].parent =_meta_table['Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig']['meta_info']
_meta_table['Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.MacAccessInterface']['meta_info'].parent =_meta_table['Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig']['meta_info']
_meta_table['Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.MacIwfAccessInterface']['meta_info'].parent =_meta_table['Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig']['meta_info']
_meta_table['Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.CircuitId']['meta_info'].parent =_meta_table['Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig']['meta_info']
_meta_table['Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.RemoteId']['meta_info'].parent =_meta_table['Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig']['meta_info']
_meta_table['Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.CircuitIdAndRemoteId']['meta_info'].parent =_meta_table['Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig']['meta_info']
_meta_table['Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.OuterVlanId']['meta_info'].parent =_meta_table['Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig']['meta_info']
_meta_table['Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.InnerVlanId']['meta_info'].parent =_meta_table['Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig']['meta_info']
_meta_table['Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig.VlanId']['meta_info'].parent =_meta_table['Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig']['meta_info']
_meta_table['Pppoe.Nodes.Node.BbaGroups.BbaGroup.LimitConfig']['meta_info'].parent =_meta_table['Pppoe.Nodes.Node.BbaGroups.BbaGroup']['meta_info']
_meta_table['Pppoe.Nodes.Node.BbaGroups.BbaGroup.Limits']['meta_info'].parent =_meta_table['Pppoe.Nodes.Node.BbaGroups.BbaGroup']['meta_info']
_meta_table['Pppoe.Nodes.Node.BbaGroups.BbaGroup.Throttles']['meta_info'].parent =_meta_table['Pppoe.Nodes.Node.BbaGroups.BbaGroup']['meta_info']
_meta_table['Pppoe.Nodes.Node.BbaGroups.BbaGroup.ThrottleConfig']['meta_info'].parent =_meta_table['Pppoe.Nodes.Node.BbaGroups.BbaGroup']['meta_info']
_meta_table['Pppoe.Nodes.Node.BbaGroups.BbaGroup']['meta_info'].parent =_meta_table['Pppoe.Nodes.Node.BbaGroups']['meta_info']
_meta_table['Pppoe.Nodes.Node.Statistics']['meta_info'].parent =_meta_table['Pppoe.Nodes.Node']['meta_info']
_meta_table['Pppoe.Nodes.Node.AccessInterface']['meta_info'].parent =_meta_table['Pppoe.Nodes.Node']['meta_info']
_meta_table['Pppoe.Nodes.Node.Interfaces']['meta_info'].parent =_meta_table['Pppoe.Nodes.Node']['meta_info']
_meta_table['Pppoe.Nodes.Node.BbaGroups']['meta_info'].parent =_meta_table['Pppoe.Nodes.Node']['meta_info']
_meta_table['Pppoe.Nodes.Node.SummaryTotal']['meta_info'].parent =_meta_table['Pppoe.Nodes.Node']['meta_info']
_meta_table['Pppoe.Nodes.Node']['meta_info'].parent =_meta_table['Pppoe.Nodes']['meta_info']
_meta_table['Pppoe.AccessInterfaceStatistics']['meta_info'].parent =_meta_table['Pppoe']['meta_info']
_meta_table['Pppoe.Nodes']['meta_info'].parent =_meta_table['Pppoe']['meta_info']
