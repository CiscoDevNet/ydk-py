


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'Ipv4QppbEnum' : _MetaInfoEnum('Ipv4QppbEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ma_cfg',
        {
            'none':'none',
            'ip-prec':'ip_prec',
            'qos-grp':'qos_grp',
            'both':'both',
        }, 'Cisco-IOS-XR-ipv4-ma-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ma-cfg']),
    'Ipv4NetworkGlobal.Unnumbered.Mpls.Te' : {
        'meta_info' : _MetaInfoClass('Ipv4NetworkGlobal.Unnumbered.Mpls.Te',
            False, 
            [
            _MetaInfoClassMember('interface', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Enable IP processing without an explicit
                address on MPLS Traffic-Eng
                ''',
                'interface',
                'Cisco-IOS-XR-ipv4-ma-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ma-cfg',
            'te',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ma-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ma_cfg'
        ),
    },
    'Ipv4NetworkGlobal.Unnumbered.Mpls' : {
        'meta_info' : _MetaInfoClass('Ipv4NetworkGlobal.Unnumbered.Mpls',
            False, 
            [
            _MetaInfoClassMember('te', REFERENCE_CLASS, 'Te' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ma_cfg', 'Ipv4NetworkGlobal.Unnumbered.Mpls.Te', 
                [], [], 
                '''                IPv4 commands for MPLS Traffic Engineering
                ''',
                'te',
                'Cisco-IOS-XR-ipv4-ma-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ma-cfg',
            'mpls',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ma-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ma_cfg'
        ),
    },
    'Ipv4NetworkGlobal.Unnumbered' : {
        'meta_info' : _MetaInfoClass('Ipv4NetworkGlobal.Unnumbered',
            False, 
            [
            _MetaInfoClassMember('mpls', REFERENCE_CLASS, 'Mpls' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ma_cfg', 'Ipv4NetworkGlobal.Unnumbered.Mpls', 
                [], [], 
                '''                Configure MPLS routing protocol parameters
                ''',
                'mpls',
                'Cisco-IOS-XR-ipv4-ma-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ma-cfg',
            'unnumbered',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ma-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ma_cfg'
        ),
    },
    'Ipv4NetworkGlobal.Qppb' : {
        'meta_info' : _MetaInfoClass('Ipv4NetworkGlobal.Qppb',
            False, 
            [
            _MetaInfoClassMember('destination', REFERENCE_ENUM_CLASS, 'Ipv4QppbEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ma_cfg', 'Ipv4QppbEnum', 
                [], [], 
                '''                QPPB configuration on destination
                ''',
                'destination',
                'Cisco-IOS-XR-ipv4-ma-cfg', False),
            _MetaInfoClassMember('source', REFERENCE_ENUM_CLASS, 'Ipv4QppbEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ma_cfg', 'Ipv4QppbEnum', 
                [], [], 
                '''                QPPB configuration on source
                ''',
                'source',
                'Cisco-IOS-XR-ipv4-ma-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ma-cfg',
            'qppb',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ma-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ma_cfg'
        ),
    },
    'Ipv4NetworkGlobal' : {
        'meta_info' : _MetaInfoClass('Ipv4NetworkGlobal',
            False, 
            [
            _MetaInfoClassMember('qppb', REFERENCE_CLASS, 'Qppb' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ma_cfg', 'Ipv4NetworkGlobal.Qppb', 
                [], [], 
                '''                QPPB
                ''',
                'qppb',
                'Cisco-IOS-XR-ipv4-ma-cfg', False),
            _MetaInfoClassMember('reassemble-max-packets', ATTRIBUTE, 'int' , None, None, 
                [('1', '50')], [], 
                '''                Percentage of total packets available in the
                system
                ''',
                'reassemble_max_packets',
                'Cisco-IOS-XR-ipv4-ma-cfg', False),
            _MetaInfoClassMember('reassemble-time-out', ATTRIBUTE, 'int' , None, None, 
                [('1', '120')], [], 
                '''                Number of seconds a reassembly queue will hold
                before timeout
                ''',
                'reassemble_time_out',
                'Cisco-IOS-XR-ipv4-ma-cfg', False),
            _MetaInfoClassMember('source-route', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                The flag for enabling whether to process packets
                with source routing header options
                ''',
                'source_route',
                'Cisco-IOS-XR-ipv4-ma-cfg', False),
            _MetaInfoClassMember('unnumbered', REFERENCE_CLASS, 'Unnumbered' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ma_cfg', 'Ipv4NetworkGlobal.Unnumbered', 
                [], [], 
                '''                Enable IPv4 processing without an explicit
                address
                ''',
                'unnumbered',
                'Cisco-IOS-XR-ipv4-ma-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ma-cfg',
            'ipv4-network-global',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ma-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ma_cfg'
        ),
    },
    'SubscriberPta' : {
        'meta_info' : _MetaInfoClass('SubscriberPta',
            False, 
            [
            _MetaInfoClassMember('tcp-mss-adjust', ATTRIBUTE, 'int' , None, None, 
                [('1280', '1536')], [], 
                '''                TCP MSS Adjust (bytes)
                ''',
                'tcp_mss_adjust',
                'Cisco-IOS-XR-ipv4-ma-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ma-cfg',
            'subscriber-pta',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ma-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ma_cfg'
        ),
    },
}
_meta_table['Ipv4NetworkGlobal.Unnumbered.Mpls.Te']['meta_info'].parent =_meta_table['Ipv4NetworkGlobal.Unnumbered.Mpls']['meta_info']
_meta_table['Ipv4NetworkGlobal.Unnumbered.Mpls']['meta_info'].parent =_meta_table['Ipv4NetworkGlobal.Unnumbered']['meta_info']
_meta_table['Ipv4NetworkGlobal.Unnumbered']['meta_info'].parent =_meta_table['Ipv4NetworkGlobal']['meta_info']
_meta_table['Ipv4NetworkGlobal.Qppb']['meta_info'].parent =_meta_table['Ipv4NetworkGlobal']['meta_info']
