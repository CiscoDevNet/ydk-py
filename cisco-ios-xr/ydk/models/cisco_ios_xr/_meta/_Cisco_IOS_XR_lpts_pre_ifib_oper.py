


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'LptsPifibEnum' : _MetaInfoEnum('LptsPifibEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_oper',
        {
            'isis':'isis',
            'ipv4-frag':'ipv4_frag',
            'ipv4-echo':'ipv4_echo',
            'ipv4-any':'ipv4_any',
            'ipv6-frag':'ipv6_frag',
            'ipv6-echo':'ipv6_echo',
            'ipv6-nd':'ipv6_nd',
            'ipv6-any':'ipv6_any',
            'bfd-any':'bfd_any',
            'all':'all',
        }, 'Cisco-IOS-XR-lpts-pre-ifib-oper', _yang_ns._namespaces['Cisco-IOS-XR-lpts-pre-ifib-oper']),
    'LptsPifib.Nodes.Node.TypeValues.TypeValue.Entry' : {
        'meta_info' : _MetaInfoClass('LptsPifib.Nodes.Node.TypeValues.TypeValue.Entry',
            False, 
            [
            _MetaInfoClassMember('entry', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Single Pre-ifib entry
                ''',
                'entry',
                'Cisco-IOS-XR-lpts-pre-ifib-oper', True),
            _MetaInfoClassMember('accepts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Packets matched to accept
                ''',
                'accepts',
                'Cisco-IOS-XR-lpts-pre-ifib-oper', False),
            _MetaInfoClassMember('deliver-list-long', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Deliver List Long Format
                ''',
                'deliver_list_long',
                'Cisco-IOS-XR-lpts-pre-ifib-oper', False),
            _MetaInfoClassMember('deliver-list-short', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Deliver List Short Format
                ''',
                'deliver_list_short',
                'Cisco-IOS-XR-lpts-pre-ifib-oper', False),
            _MetaInfoClassMember('destination-addr', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Destination IP Address
                ''',
                'destination_addr',
                'Cisco-IOS-XR-lpts-pre-ifib-oper', False),
            _MetaInfoClassMember('destination-type', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Destination Key Type
                ''',
                'destination_type',
                'Cisco-IOS-XR-lpts-pre-ifib-oper', False),
            _MetaInfoClassMember('destination-value', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Destination Port/ICMP Type/IGMP Type
                ''',
                'destination_value',
                'Cisco-IOS-XR-lpts-pre-ifib-oper', False),
            _MetaInfoClassMember('drops', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Packets matched for drop
                ''',
                'drops',
                'Cisco-IOS-XR-lpts-pre-ifib-oper', False),
            _MetaInfoClassMember('flow-type', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Flow type
                ''',
                'flow_type',
                'Cisco-IOS-XR-lpts-pre-ifib-oper', False),
            _MetaInfoClassMember('intf-handle', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Interface Handle
                ''',
                'intf_handle',
                'Cisco-IOS-XR-lpts-pre-ifib-oper', False),
            _MetaInfoClassMember('intf-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Interface Name
                ''',
                'intf_name',
                'Cisco-IOS-XR-lpts-pre-ifib-oper', False),
            _MetaInfoClassMember('is-fgid', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Is FGID or not
                ''',
                'is_fgid',
                'Cisco-IOS-XR-lpts-pre-ifib-oper', False),
            _MetaInfoClassMember('is-frag', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Is Fragment
                ''',
                'is_frag',
                'Cisco-IOS-XR-lpts-pre-ifib-oper', False),
            _MetaInfoClassMember('is-syn', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Is SYN
                ''',
                'is_syn',
                'Cisco-IOS-XR-lpts-pre-ifib-oper', False),
            _MetaInfoClassMember('l3protocol', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Layer 3 Protocol
                ''',
                'l3protocol',
                'Cisco-IOS-XR-lpts-pre-ifib-oper', False),
            _MetaInfoClassMember('l4protocol', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Layer 4 Protocol
                ''',
                'l4protocol',
                'Cisco-IOS-XR-lpts-pre-ifib-oper', False),
            _MetaInfoClassMember('listener-tag', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Listener Tag
                ''',
                'listener_tag',
                'Cisco-IOS-XR-lpts-pre-ifib-oper', False),
            _MetaInfoClassMember('local-flag', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Local Flag
                ''',
                'local_flag',
                'Cisco-IOS-XR-lpts-pre-ifib-oper', False),
            _MetaInfoClassMember('min-ttl', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Minimum TTL
                ''',
                'min_ttl',
                'Cisco-IOS-XR-lpts-pre-ifib-oper', False),
            _MetaInfoClassMember('opcode', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Opcode
                ''',
                'opcode',
                'Cisco-IOS-XR-lpts-pre-ifib-oper', False),
            _MetaInfoClassMember('pifib-program-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Creation or Update Time
                ''',
                'pifib_program_time',
                'Cisco-IOS-XR-lpts-pre-ifib-oper', False),
            _MetaInfoClassMember('pifib-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                sub Pre-IFIB type
                ''',
                'pifib_type',
                'Cisco-IOS-XR-lpts-pre-ifib-oper', False),
            _MetaInfoClassMember('source-addr', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Source IP Address
                ''',
                'source_addr',
                'Cisco-IOS-XR-lpts-pre-ifib-oper', False),
            _MetaInfoClassMember('source-port', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Source port
                ''',
                'source_port',
                'Cisco-IOS-XR-lpts-pre-ifib-oper', False),
            _MetaInfoClassMember('stale', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Is Stale
                ''',
                'stale',
                'Cisco-IOS-XR-lpts-pre-ifib-oper', False),
            _MetaInfoClassMember('vid', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                VRF ID
                ''',
                'vid',
                'Cisco-IOS-XR-lpts-pre-ifib-oper', False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                VRF Name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-lpts-pre-ifib-oper', False),
            ],
            'Cisco-IOS-XR-lpts-pre-ifib-oper',
            'entry',
            _yang_ns._namespaces['Cisco-IOS-XR-lpts-pre-ifib-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_oper'
        ),
    },
    'LptsPifib.Nodes.Node.TypeValues.TypeValue' : {
        'meta_info' : _MetaInfoClass('LptsPifib.Nodes.Node.TypeValues.TypeValue',
            False, 
            [
            _MetaInfoClassMember('pifib-type', REFERENCE_ENUM_CLASS, 'LptsPifibEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_oper', 'LptsPifibEnum', 
                [], [], 
                '''                Type value
                ''',
                'pifib_type',
                'Cisco-IOS-XR-lpts-pre-ifib-oper', True),
            _MetaInfoClassMember('entry', REFERENCE_LIST, 'Entry' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_oper', 'LptsPifib.Nodes.Node.TypeValues.TypeValue.Entry', 
                [], [], 
                '''                Data for single pre-ifib entry
                ''',
                'entry',
                'Cisco-IOS-XR-lpts-pre-ifib-oper', False),
            ],
            'Cisco-IOS-XR-lpts-pre-ifib-oper',
            'type-value',
            _yang_ns._namespaces['Cisco-IOS-XR-lpts-pre-ifib-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_oper'
        ),
    },
    'LptsPifib.Nodes.Node.TypeValues' : {
        'meta_info' : _MetaInfoClass('LptsPifib.Nodes.Node.TypeValues',
            False, 
            [
            _MetaInfoClassMember('type-value', REFERENCE_LIST, 'TypeValue' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_oper', 'LptsPifib.Nodes.Node.TypeValues.TypeValue', 
                [], [], 
                '''                pifib types
                ''',
                'type_value',
                'Cisco-IOS-XR-lpts-pre-ifib-oper', False),
            ],
            'Cisco-IOS-XR-lpts-pre-ifib-oper',
            'type-values',
            _yang_ns._namespaces['Cisco-IOS-XR-lpts-pre-ifib-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_oper'
        ),
    },
    'LptsPifib.Nodes.Node.Hardware.UsageEntries.UsageEntry.UsageInfo' : {
        'meta_info' : _MetaInfoClass('LptsPifib.Nodes.Node.Hardware.UsageEntries.UsageEntry.UsageInfo',
            False, 
            [
            _MetaInfoClassMember('pipe-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Pipe ID
                ''',
                'pipe_id',
                'Cisco-IOS-XR-platform-pifib-oper', False),
            _MetaInfoClassMember('region', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Region Type
                ''',
                'region',
                'Cisco-IOS-XR-platform-pifib-oper', False),
            _MetaInfoClassMember('region-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Region ID
                ''',
                'region_id',
                'Cisco-IOS-XR-platform-pifib-oper', False),
            _MetaInfoClassMember('size', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum Number of Entries in the Region
                ''',
                'size',
                'Cisco-IOS-XR-platform-pifib-oper', False),
            _MetaInfoClassMember('used', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Used Number of Entries in the Region
                ''',
                'used',
                'Cisco-IOS-XR-platform-pifib-oper', False),
            ],
            'Cisco-IOS-XR-platform-pifib-oper',
            'usage-info',
            _yang_ns._namespaces['Cisco-IOS-XR-platform-pifib-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_oper'
        ),
    },
    'LptsPifib.Nodes.Node.Hardware.UsageEntries.UsageEntry' : {
        'meta_info' : _MetaInfoClass('LptsPifib.Nodes.Node.Hardware.UsageEntries.UsageEntry',
            False, 
            [
            _MetaInfoClassMember('region-id', REFERENCE_ENUM_CLASS, 'UsageAddressFamilyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_platform_pifib_oper', 'UsageAddressFamilyEnum', 
                [], [], 
                '''                Region ID
                ''',
                'region_id',
                'Cisco-IOS-XR-platform-pifib-oper', True),
            _MetaInfoClassMember('usage-info', REFERENCE_LIST, 'UsageInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_oper', 'LptsPifib.Nodes.Node.Hardware.UsageEntries.UsageEntry.UsageInfo', 
                [], [], 
                '''                Per TCAM type usage info
                ''',
                'usage_info',
                'Cisco-IOS-XR-platform-pifib-oper', False),
            ],
            'Cisco-IOS-XR-platform-pifib-oper',
            'usage-entry',
            _yang_ns._namespaces['Cisco-IOS-XR-platform-pifib-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_oper'
        ),
    },
    'LptsPifib.Nodes.Node.Hardware.UsageEntries' : {
        'meta_info' : _MetaInfoClass('LptsPifib.Nodes.Node.Hardware.UsageEntries',
            False, 
            [
            _MetaInfoClassMember('usage-entry', REFERENCE_LIST, 'UsageEntry' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_oper', 'LptsPifib.Nodes.Node.Hardware.UsageEntries.UsageEntry', 
                [], [], 
                '''                Usage details
                ''',
                'usage_entry',
                'Cisco-IOS-XR-platform-pifib-oper', False),
            ],
            'Cisco-IOS-XR-platform-pifib-oper',
            'usage-entries',
            _yang_ns._namespaces['Cisco-IOS-XR-platform-pifib-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_oper'
        ),
    },
    'LptsPifib.Nodes.Node.Hardware.Police.PoliceInfo' : {
        'meta_info' : _MetaInfoClass('LptsPifib.Nodes.Node.Hardware.Police.PoliceInfo',
            False, 
            [
            _MetaInfoClassMember('accepted-stats', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                accepted stats
                ''',
                'accepted_stats',
                'Cisco-IOS-XR-platform-pifib-oper', False),
            _MetaInfoClassMember('acl-config', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                acl config
                ''',
                'acl_config',
                'Cisco-IOS-XR-platform-pifib-oper', False),
            _MetaInfoClassMember('acl-str', ATTRIBUTE, 'str' , None, None, 
                [], [b'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                acl str
                ''',
                'acl_str',
                'Cisco-IOS-XR-platform-pifib-oper', False),
            _MetaInfoClassMember('avgrate', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                avgrate
                ''',
                'avgrate',
                'Cisco-IOS-XR-platform-pifib-oper', False),
            _MetaInfoClassMember('avgrate-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                avgrate type
                ''',
                'avgrate_type',
                'Cisco-IOS-XR-platform-pifib-oper', False),
            _MetaInfoClassMember('burst', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                burst
                ''',
                'burst',
                'Cisco-IOS-XR-platform-pifib-oper', False),
            _MetaInfoClassMember('change-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                change type
                ''',
                'change_type',
                'Cisco-IOS-XR-platform-pifib-oper', False),
            _MetaInfoClassMember('dropped-stats', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                dropped stats
                ''',
                'dropped_stats',
                'Cisco-IOS-XR-platform-pifib-oper', False),
            _MetaInfoClassMember('iptos-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                iptos value
                ''',
                'iptos_value',
                'Cisco-IOS-XR-platform-pifib-oper', False),
            _MetaInfoClassMember('policer', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                policer
                ''',
                'policer',
                'Cisco-IOS-XR-platform-pifib-oper', False),
            _MetaInfoClassMember('static-avgrate', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                static avgrate
                ''',
                'static_avgrate',
                'Cisco-IOS-XR-platform-pifib-oper', False),
            ],
            'Cisco-IOS-XR-platform-pifib-oper',
            'police-info',
            _yang_ns._namespaces['Cisco-IOS-XR-platform-pifib-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_oper'
        ),
    },
    'LptsPifib.Nodes.Node.Hardware.Police' : {
        'meta_info' : _MetaInfoClass('LptsPifib.Nodes.Node.Hardware.Police',
            False, 
            [
            _MetaInfoClassMember('police-info', REFERENCE_LIST, 'PoliceInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_oper', 'LptsPifib.Nodes.Node.Hardware.Police.PoliceInfo', 
                [], [], 
                '''                Per flow type police info
                ''',
                'police_info',
                'Cisco-IOS-XR-platform-pifib-oper', False),
            ],
            'Cisco-IOS-XR-platform-pifib-oper',
            'police',
            _yang_ns._namespaces['Cisco-IOS-XR-platform-pifib-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_oper'
        ),
    },
    'LptsPifib.Nodes.Node.Hardware.StaticPolice.StaticInfo' : {
        'meta_info' : _MetaInfoClass('LptsPifib.Nodes.Node.Hardware.StaticPolice.StaticInfo',
            False, 
            [
            _MetaInfoClassMember('accepted', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                accepted
                ''',
                'accepted',
                'Cisco-IOS-XR-platform-pifib-oper', False),
            _MetaInfoClassMember('burst-rate', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                burst rate
                ''',
                'burst_rate',
                'Cisco-IOS-XR-platform-pifib-oper', False),
            _MetaInfoClassMember('change-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                change type
                ''',
                'change_type',
                'Cisco-IOS-XR-platform-pifib-oper', False),
            _MetaInfoClassMember('dropped', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                dropped
                ''',
                'dropped',
                'Cisco-IOS-XR-platform-pifib-oper', False),
            _MetaInfoClassMember('flow-rate', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                flow rate
                ''',
                'flow_rate',
                'Cisco-IOS-XR-platform-pifib-oper', False),
            _MetaInfoClassMember('punt-reason', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                punt reason
                ''',
                'punt_reason',
                'Cisco-IOS-XR-platform-pifib-oper', False),
            _MetaInfoClassMember('punt-reason-string', ATTRIBUTE, 'str' , None, None, 
                [], [b'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                punt reason string
                ''',
                'punt_reason_string',
                'Cisco-IOS-XR-platform-pifib-oper', False),
            _MetaInfoClassMember('sid', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                sid
                ''',
                'sid',
                'Cisco-IOS-XR-platform-pifib-oper', False),
            ],
            'Cisco-IOS-XR-platform-pifib-oper',
            'static-info',
            _yang_ns._namespaces['Cisco-IOS-XR-platform-pifib-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_oper'
        ),
    },
    'LptsPifib.Nodes.Node.Hardware.StaticPolice' : {
        'meta_info' : _MetaInfoClass('LptsPifib.Nodes.Node.Hardware.StaticPolice',
            False, 
            [
            _MetaInfoClassMember('static-info', REFERENCE_LIST, 'StaticInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_oper', 'LptsPifib.Nodes.Node.Hardware.StaticPolice.StaticInfo', 
                [], [], 
                '''                Per punt reason info
                ''',
                'static_info',
                'Cisco-IOS-XR-platform-pifib-oper', False),
            ],
            'Cisco-IOS-XR-platform-pifib-oper',
            'static-police',
            _yang_ns._namespaces['Cisco-IOS-XR-platform-pifib-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_oper'
        ),
    },
    'LptsPifib.Nodes.Node.Hardware.Bfd.BfdEntryInfo' : {
        'meta_info' : _MetaInfoClass('LptsPifib.Nodes.Node.Hardware.Bfd.BfdEntryInfo',
            False, 
            [
            _MetaInfoClassMember('fgid-or-vqi', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                fgid or vqi
                ''',
                'fgid_or_vqi',
                'Cisco-IOS-XR-platform-pifib-oper', False),
            _MetaInfoClassMember('index', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                index
                ''',
                'index',
                'Cisco-IOS-XR-platform-pifib-oper', False),
            _MetaInfoClassMember('is-mcast', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                is mcast
                ''',
                'is_mcast',
                'Cisco-IOS-XR-platform-pifib-oper', False),
            _MetaInfoClassMember('is-valid', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                is valid
                ''',
                'is_valid',
                'Cisco-IOS-XR-platform-pifib-oper', False),
            _MetaInfoClassMember('policer-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                policer id
                ''',
                'policer_id',
                'Cisco-IOS-XR-platform-pifib-oper', False),
            ],
            'Cisco-IOS-XR-platform-pifib-oper',
            'bfd-entry-info',
            _yang_ns._namespaces['Cisco-IOS-XR-platform-pifib-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_oper'
        ),
    },
    'LptsPifib.Nodes.Node.Hardware.Bfd' : {
        'meta_info' : _MetaInfoClass('LptsPifib.Nodes.Node.Hardware.Bfd',
            False, 
            [
            _MetaInfoClassMember('bfd-entry-info', REFERENCE_LIST, 'BfdEntryInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_oper', 'LptsPifib.Nodes.Node.Hardware.Bfd.BfdEntryInfo', 
                [], [], 
                '''                Per bfd disc entry info
                ''',
                'bfd_entry_info',
                'Cisco-IOS-XR-platform-pifib-oper', False),
            ],
            'Cisco-IOS-XR-platform-pifib-oper',
            'bfd',
            _yang_ns._namespaces['Cisco-IOS-XR-platform-pifib-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_oper'
        ),
    },
    'LptsPifib.Nodes.Node.Hardware.Statistics' : {
        'meta_info' : _MetaInfoClass('LptsPifib.Nodes.Node.Hardware.Statistics',
            False, 
            [
            _MetaInfoClassMember('accepted', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Deleted-entry accepted packets counter
                ''',
                'accepted',
                'Cisco-IOS-XR-platform-pifib-oper', False),
            _MetaInfoClassMember('clear-ts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Statistics clear timestamp
                ''',
                'clear_ts',
                'Cisco-IOS-XR-platform-pifib-oper', False),
            _MetaInfoClassMember('dropped', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Deleted-entry dropped packets counter
                ''',
                'dropped',
                'Cisco-IOS-XR-platform-pifib-oper', False),
            _MetaInfoClassMember('no-stats-mem-err', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                No statistics memory error
                ''',
                'no_stats_mem_err',
                'Cisco-IOS-XR-platform-pifib-oper', False),
            ],
            'Cisco-IOS-XR-platform-pifib-oper',
            'statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-platform-pifib-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_oper'
        ),
    },
    'LptsPifib.Nodes.Node.Hardware.IndexEntries.IndexEntry.HwInfo' : {
        'meta_info' : _MetaInfoClass('LptsPifib.Nodes.Node.Hardware.IndexEntries.IndexEntry.HwInfo',
            False, 
            [
            _MetaInfoClassMember('accepted', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Accepted Packets Counter
                ''',
                'accepted',
                'Cisco-IOS-XR-platform-pifib-oper', False),
            _MetaInfoClassMember('dropped', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Dropped Packets Counter
                ''',
                'dropped',
                'Cisco-IOS-XR-platform-pifib-oper', False),
            _MetaInfoClassMember('policer', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Policer Pointer
                ''',
                'policer',
                'Cisco-IOS-XR-platform-pifib-oper', False),
            _MetaInfoClassMember('sort-start-offset', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Relative position in sorting order
                ''',
                'sort_start_offset',
                'Cisco-IOS-XR-platform-pifib-oper', False),
            _MetaInfoClassMember('stats-ptr', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Stats Pointer
                ''',
                'stats_ptr',
                'Cisco-IOS-XR-platform-pifib-oper', False),
            _MetaInfoClassMember('tm-start-offset', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Relative position in TCAM
                ''',
                'tm_start_offset',
                'Cisco-IOS-XR-platform-pifib-oper', False),
            ],
            'Cisco-IOS-XR-platform-pifib-oper',
            'hw-info',
            _yang_ns._namespaces['Cisco-IOS-XR-platform-pifib-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_oper'
        ),
    },
    'LptsPifib.Nodes.Node.Hardware.IndexEntries.IndexEntry' : {
        'meta_info' : _MetaInfoClass('LptsPifib.Nodes.Node.Hardware.IndexEntries.IndexEntry',
            False, 
            [
            _MetaInfoClassMember('index', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Index
                ''',
                'index',
                'Cisco-IOS-XR-platform-pifib-oper', True),
            _MetaInfoClassMember('acl-str', ATTRIBUTE, 'str' , None, None, 
                [], [b'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                Acl name
                ''',
                'acl_str',
                'Cisco-IOS-XR-platform-pifib-oper', False),
            _MetaInfoClassMember('action', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Action
                ''',
                'action',
                'Cisco-IOS-XR-platform-pifib-oper', False),
            _MetaInfoClassMember('action-string', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Action String
                ''',
                'action_string',
                'Cisco-IOS-XR-platform-pifib-oper', False),
            _MetaInfoClassMember('cir', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Committed Information Rate
                ''',
                'cir',
                'Cisco-IOS-XR-platform-pifib-oper', False),
            _MetaInfoClassMember('entry-ptr', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ptr to ifib_entry_st
                ''',
                'entry_ptr',
                'Cisco-IOS-XR-platform-pifib-oper', False),
            _MetaInfoClassMember('entry-shadow-ptr', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ptr to ifib_entry_shadow_st
                ''',
                'entry_shadow_ptr',
                'Cisco-IOS-XR-platform-pifib-oper', False),
            _MetaInfoClassMember('fgid-or-sfp', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                fabric group id or swith fabric port
                ''',
                'fgid_or_sfp',
                'Cisco-IOS-XR-platform-pifib-oper', False),
            _MetaInfoClassMember('flow-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Flow type
                ''',
                'flow_type',
                'Cisco-IOS-XR-platform-pifib-oper', False),
            _MetaInfoClassMember('hw-info', REFERENCE_LIST, 'HwInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_oper', 'LptsPifib.Nodes.Node.Hardware.IndexEntries.IndexEntry.HwInfo', 
                [], [], 
                '''                Per pipe type hardware info
                ''',
                'hw_info',
                'Cisco-IOS-XR-platform-pifib-oper', False),
            _MetaInfoClassMember('intf-handle', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Interface Handle
                ''',
                'intf_handle',
                'Cisco-IOS-XR-platform-pifib-oper', False),
            _MetaInfoClassMember('intf-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Interface Name
                ''',
                'intf_name',
                'Cisco-IOS-XR-platform-pifib-oper', False),
            _MetaInfoClassMember('is-fgid', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Is FGID or not
                ''',
                'is_fgid',
                'Cisco-IOS-XR-platform-pifib-oper', False),
            _MetaInfoClassMember('is-frag', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Is Fragment
                ''',
                'is_frag',
                'Cisco-IOS-XR-platform-pifib-oper', False),
            _MetaInfoClassMember('is-optimized', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Is optimized or not
                ''',
                'is_optimized',
                'Cisco-IOS-XR-platform-pifib-oper', False),
            _MetaInfoClassMember('is-syn', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Is SYN
                ''',
                'is_syn',
                'Cisco-IOS-XR-platform-pifib-oper', False),
            _MetaInfoClassMember('is-uidb-opt-bit', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Is uidb set for optimized entry or not
                ''',
                'is_uidb_opt_bit',
                'Cisco-IOS-XR-platform-pifib-oper', False),
            _MetaInfoClassMember('is-vrf', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Is VRF or not
                ''',
                'is_vrf',
                'Cisco-IOS-XR-platform-pifib-oper', False),
            _MetaInfoClassMember('l3protocol', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Layer 3 Protocol
                ''',
                'l3protocol',
                'Cisco-IOS-XR-platform-pifib-oper', False),
            _MetaInfoClassMember('l4protocol', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Layer 4 Protocol
                ''',
                'l4protocol',
                'Cisco-IOS-XR-platform-pifib-oper', False),
            _MetaInfoClassMember('list-node-ptr', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ptr to dlqueue list node
                ''',
                'list_node_ptr',
                'Cisco-IOS-XR-platform-pifib-oper', False),
            _MetaInfoClassMember('listener-tag', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Listener Tag
                ''',
                'listener_tag',
                'Cisco-IOS-XR-platform-pifib-oper', False),
            _MetaInfoClassMember('local-addr', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Local IP Address
                ''',
                'local_addr',
                'Cisco-IOS-XR-platform-pifib-oper', False),
            _MetaInfoClassMember('local-port', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Local port
                ''',
                'local_port',
                'Cisco-IOS-XR-platform-pifib-oper', False),
            _MetaInfoClassMember('local-prefix-len', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Local Prefix Length
                ''',
                'local_prefix_len',
                'Cisco-IOS-XR-platform-pifib-oper', False),
            _MetaInfoClassMember('lookup-priority', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Lookup priority
                ''',
                'lookup_priority',
                'Cisco-IOS-XR-platform-pifib-oper', False),
            _MetaInfoClassMember('min-ttl', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Minimum TTL
                ''',
                'min_ttl',
                'Cisco-IOS-XR-platform-pifib-oper', False),
            _MetaInfoClassMember('no-stats', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Stats not available
                ''',
                'no_stats',
                'Cisco-IOS-XR-platform-pifib-oper', False),
            _MetaInfoClassMember('num-retries', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                retries count
                ''',
                'num_retries',
                'Cisco-IOS-XR-platform-pifib-oper', False),
            _MetaInfoClassMember('num-tm-entries', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Number of TCAM entries used
                ''',
                'num_tm_entries',
                'Cisco-IOS-XR-platform-pifib-oper', False),
            _MetaInfoClassMember('policer-avgrate', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Policer avg. rate limit
                ''',
                'policer_avgrate',
                'Cisco-IOS-XR-platform-pifib-oper', False),
            _MetaInfoClassMember('policer-burst', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Policer burst
                ''',
                'policer_burst',
                'Cisco-IOS-XR-platform-pifib-oper', False),
            _MetaInfoClassMember('priority', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Flow priority or COS
                ''',
                'priority',
                'Cisco-IOS-XR-platform-pifib-oper', False),
            _MetaInfoClassMember('rack-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Remote racknum if remote
                ''',
                'rack_id',
                'Cisco-IOS-XR-platform-pifib-oper', False),
            _MetaInfoClassMember('remote-addr', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Remote IP Address
                ''',
                'remote_addr',
                'Cisco-IOS-XR-platform-pifib-oper', False),
            _MetaInfoClassMember('remote-fgid', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Remote FGID
                ''',
                'remote_fgid',
                'Cisco-IOS-XR-platform-pifib-oper', False),
            _MetaInfoClassMember('remote-prefix-len', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Remote Prefix Length
                ''',
                'remote_prefix_len',
                'Cisco-IOS-XR-platform-pifib-oper', False),
            _MetaInfoClassMember('remote-rack', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Is entry remote or not
                ''',
                'remote_rack',
                'Cisco-IOS-XR-platform-pifib-oper', False),
            _MetaInfoClassMember('retry-fail-cause', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                failure cause
                ''',
                'retry_fail_cause',
                'Cisco-IOS-XR-platform-pifib-oper', False),
            _MetaInfoClassMember('rslot', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Remote slotnum if remote
                ''',
                'rslot',
                'Cisco-IOS-XR-platform-pifib-oper', False),
            _MetaInfoClassMember('sid', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Stream ID
                ''',
                'sid',
                'Cisco-IOS-XR-platform-pifib-oper', False),
            _MetaInfoClassMember('state', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                state of pifib entry
                ''',
                'state',
                'Cisco-IOS-XR-platform-pifib-oper', False),
            _MetaInfoClassMember('storage-priority', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Storage priority
                ''',
                'storage_priority',
                'Cisco-IOS-XR-platform-pifib-oper', False),
            _MetaInfoClassMember('u-len', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Union Key Length
                ''',
                'u_len',
                'Cisco-IOS-XR-platform-pifib-oper', False),
            _MetaInfoClassMember('u-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Union Key Type
                ''',
                'u_type',
                'Cisco-IOS-XR-platform-pifib-oper', False),
            _MetaInfoClassMember('u-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Remote Port/ICMP Type/IGMP Type
                ''',
                'u_value',
                'Cisco-IOS-XR-platform-pifib-oper', False),
            _MetaInfoClassMember('uidb-index', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Interface uidb index
                ''',
                'uidb_index',
                'Cisco-IOS-XR-platform-pifib-oper', False),
            _MetaInfoClassMember('vrf-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                VRF ID
                ''',
                'vrf_id',
                'Cisco-IOS-XR-platform-pifib-oper', False),
            ],
            'Cisco-IOS-XR-platform-pifib-oper',
            'index-entry',
            _yang_ns._namespaces['Cisco-IOS-XR-platform-pifib-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_oper'
        ),
    },
    'LptsPifib.Nodes.Node.Hardware.IndexEntries' : {
        'meta_info' : _MetaInfoClass('LptsPifib.Nodes.Node.Hardware.IndexEntries',
            False, 
            [
            _MetaInfoClassMember('index-entry', REFERENCE_LIST, 'IndexEntry' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_oper', 'LptsPifib.Nodes.Node.Hardware.IndexEntries.IndexEntry', 
                [], [], 
                '''                Entry options
                ''',
                'index_entry',
                'Cisco-IOS-XR-platform-pifib-oper', False),
            ],
            'Cisco-IOS-XR-platform-pifib-oper',
            'index-entries',
            _yang_ns._namespaces['Cisco-IOS-XR-platform-pifib-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_oper'
        ),
    },
    'LptsPifib.Nodes.Node.Hardware' : {
        'meta_info' : _MetaInfoClass('LptsPifib.Nodes.Node.Hardware',
            False, 
            [
            _MetaInfoClassMember('bfd', REFERENCE_CLASS, 'Bfd' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_oper', 'LptsPifib.Nodes.Node.Hardware.Bfd', 
                [], [], 
                '''                Bfd details
                ''',
                'bfd',
                'Cisco-IOS-XR-platform-pifib-oper', False),
            _MetaInfoClassMember('index-entries', REFERENCE_CLASS, 'IndexEntries' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_oper', 'LptsPifib.Nodes.Node.Hardware.IndexEntries', 
                [], [], 
                '''                Hardware Entry options
                ''',
                'index_entries',
                'Cisco-IOS-XR-platform-pifib-oper', False),
            _MetaInfoClassMember('police', REFERENCE_CLASS, 'Police' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_oper', 'LptsPifib.Nodes.Node.Hardware.Police', 
                [], [], 
                '''                Police details
                ''',
                'police',
                'Cisco-IOS-XR-platform-pifib-oper', False),
            _MetaInfoClassMember('static-police', REFERENCE_CLASS, 'StaticPolice' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_oper', 'LptsPifib.Nodes.Node.Hardware.StaticPolice', 
                [], [], 
                '''                Static Police details
                ''',
                'static_police',
                'Cisco-IOS-XR-platform-pifib-oper', False),
            _MetaInfoClassMember('statistics', REFERENCE_CLASS, 'Statistics' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_oper', 'LptsPifib.Nodes.Node.Hardware.Statistics', 
                [], [], 
                '''                Hardware Entry type
                ''',
                'statistics',
                'Cisco-IOS-XR-platform-pifib-oper', False),
            _MetaInfoClassMember('usage-entries', REFERENCE_CLASS, 'UsageEntries' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_oper', 'LptsPifib.Nodes.Node.Hardware.UsageEntries', 
                [], [], 
                '''                Usage Table options
                ''',
                'usage_entries',
                'Cisco-IOS-XR-platform-pifib-oper', False),
            ],
            'Cisco-IOS-XR-platform-pifib-oper',
            'hardware',
            _yang_ns._namespaces['Cisco-IOS-XR-platform-pifib-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_oper'
        ),
    },
    'LptsPifib.Nodes.Node' : {
        'meta_info' : _MetaInfoClass('LptsPifib.Nodes.Node',
            False, 
            [
            _MetaInfoClassMember('node-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                The node name
                ''',
                'node_name',
                'Cisco-IOS-XR-lpts-pre-ifib-oper', True),
            _MetaInfoClassMember('hardware', REFERENCE_CLASS, 'Hardware' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_oper', 'LptsPifib.Nodes.Node.Hardware', 
                [], [], 
                '''                Hardware specific
                ''',
                'hardware',
                'Cisco-IOS-XR-platform-pifib-oper', False),
            _MetaInfoClassMember('type-values', REFERENCE_CLASS, 'TypeValues' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_oper', 'LptsPifib.Nodes.Node.TypeValues', 
                [], [], 
                '''                Type specific
                ''',
                'type_values',
                'Cisco-IOS-XR-lpts-pre-ifib-oper', False),
            ],
            'Cisco-IOS-XR-lpts-pre-ifib-oper',
            'node',
            _yang_ns._namespaces['Cisco-IOS-XR-lpts-pre-ifib-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_oper'
        ),
    },
    'LptsPifib.Nodes' : {
        'meta_info' : _MetaInfoClass('LptsPifib.Nodes',
            False, 
            [
            _MetaInfoClassMember('node', REFERENCE_LIST, 'Node' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_oper', 'LptsPifib.Nodes.Node', 
                [], [], 
                '''                Pre-ifib data for particular node
                ''',
                'node',
                'Cisco-IOS-XR-lpts-pre-ifib-oper', False),
            ],
            'Cisco-IOS-XR-lpts-pre-ifib-oper',
            'nodes',
            _yang_ns._namespaces['Cisco-IOS-XR-lpts-pre-ifib-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_oper'
        ),
    },
    'LptsPifib' : {
        'meta_info' : _MetaInfoClass('LptsPifib',
            False, 
            [
            _MetaInfoClassMember('nodes', REFERENCE_CLASS, 'Nodes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_oper', 'LptsPifib.Nodes', 
                [], [], 
                '''                List of Pre-ifib Nodes
                ''',
                'nodes',
                'Cisco-IOS-XR-lpts-pre-ifib-oper', False),
            ],
            'Cisco-IOS-XR-lpts-pre-ifib-oper',
            'lpts-pifib',
            _yang_ns._namespaces['Cisco-IOS-XR-lpts-pre-ifib-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_oper'
        ),
    },
}
_meta_table['LptsPifib.Nodes.Node.TypeValues.TypeValue.Entry']['meta_info'].parent =_meta_table['LptsPifib.Nodes.Node.TypeValues.TypeValue']['meta_info']
_meta_table['LptsPifib.Nodes.Node.TypeValues.TypeValue']['meta_info'].parent =_meta_table['LptsPifib.Nodes.Node.TypeValues']['meta_info']
_meta_table['LptsPifib.Nodes.Node.Hardware.UsageEntries.UsageEntry.UsageInfo']['meta_info'].parent =_meta_table['LptsPifib.Nodes.Node.Hardware.UsageEntries.UsageEntry']['meta_info']
_meta_table['LptsPifib.Nodes.Node.Hardware.UsageEntries.UsageEntry']['meta_info'].parent =_meta_table['LptsPifib.Nodes.Node.Hardware.UsageEntries']['meta_info']
_meta_table['LptsPifib.Nodes.Node.Hardware.Police.PoliceInfo']['meta_info'].parent =_meta_table['LptsPifib.Nodes.Node.Hardware.Police']['meta_info']
_meta_table['LptsPifib.Nodes.Node.Hardware.StaticPolice.StaticInfo']['meta_info'].parent =_meta_table['LptsPifib.Nodes.Node.Hardware.StaticPolice']['meta_info']
_meta_table['LptsPifib.Nodes.Node.Hardware.Bfd.BfdEntryInfo']['meta_info'].parent =_meta_table['LptsPifib.Nodes.Node.Hardware.Bfd']['meta_info']
_meta_table['LptsPifib.Nodes.Node.Hardware.IndexEntries.IndexEntry.HwInfo']['meta_info'].parent =_meta_table['LptsPifib.Nodes.Node.Hardware.IndexEntries.IndexEntry']['meta_info']
_meta_table['LptsPifib.Nodes.Node.Hardware.IndexEntries.IndexEntry']['meta_info'].parent =_meta_table['LptsPifib.Nodes.Node.Hardware.IndexEntries']['meta_info']
_meta_table['LptsPifib.Nodes.Node.Hardware.UsageEntries']['meta_info'].parent =_meta_table['LptsPifib.Nodes.Node.Hardware']['meta_info']
_meta_table['LptsPifib.Nodes.Node.Hardware.Police']['meta_info'].parent =_meta_table['LptsPifib.Nodes.Node.Hardware']['meta_info']
_meta_table['LptsPifib.Nodes.Node.Hardware.StaticPolice']['meta_info'].parent =_meta_table['LptsPifib.Nodes.Node.Hardware']['meta_info']
_meta_table['LptsPifib.Nodes.Node.Hardware.Bfd']['meta_info'].parent =_meta_table['LptsPifib.Nodes.Node.Hardware']['meta_info']
_meta_table['LptsPifib.Nodes.Node.Hardware.Statistics']['meta_info'].parent =_meta_table['LptsPifib.Nodes.Node.Hardware']['meta_info']
_meta_table['LptsPifib.Nodes.Node.Hardware.IndexEntries']['meta_info'].parent =_meta_table['LptsPifib.Nodes.Node.Hardware']['meta_info']
_meta_table['LptsPifib.Nodes.Node.TypeValues']['meta_info'].parent =_meta_table['LptsPifib.Nodes.Node']['meta_info']
_meta_table['LptsPifib.Nodes.Node.Hardware']['meta_info'].parent =_meta_table['LptsPifib.Nodes.Node']['meta_info']
_meta_table['LptsPifib.Nodes.Node']['meta_info'].parent =_meta_table['LptsPifib.Nodes']['meta_info']
_meta_table['LptsPifib.Nodes']['meta_info'].parent =_meta_table['LptsPifib']['meta_info']
