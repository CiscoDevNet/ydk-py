


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'Ipv4MaOperLineStateEnum' : _MetaInfoEnum('Ipv4MaOperLineStateEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper',
        {
            'unknown':'unknown',
            'shutdown':'shutdown',
            'down':'down',
            'up':'up',
        }, 'Cisco-IOS-XR-ipv4-io-oper', _yang_ns._namespaces['Cisco-IOS-XR-ipv4-io-oper']),
    'RpfModeEnum' : _MetaInfoEnum('RpfModeEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper',
        {
            'strict':'strict',
            'loose':'loose',
        }, 'Cisco-IOS-XR-ipv4-io-oper', _yang_ns._namespaces['Cisco-IOS-XR-ipv4-io-oper']),
    'Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Briefs.Brief' : {
        'meta_info' : _MetaInfoClass('Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Briefs.Brief',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                The name of the interface
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv4-io-oper', True),
            _MetaInfoClassMember('line-state', REFERENCE_ENUM_CLASS, 'Ipv4MaOperLineStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper', 'Ipv4MaOperLineStateEnum', 
                [], [], 
                '''                Line state of the interface
                ''',
                'line_state',
                'Cisco-IOS-XR-ipv4-io-oper', False),
            _MetaInfoClassMember('primary-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Primary address
                ''',
                'primary_address',
                'Cisco-IOS-XR-ipv4-io-oper', False),
            _MetaInfoClassMember('vrf-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                VRF ID of the interface
                ''',
                'vrf_id',
                'Cisco-IOS-XR-ipv4-io-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-io-oper',
            'brief',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-io-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper'
        ),
    },
    'Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Briefs' : {
        'meta_info' : _MetaInfoClass('Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Briefs',
            False, 
            [
            _MetaInfoClassMember('brief', REFERENCE_LIST, 'Brief' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper', 'Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Briefs.Brief', 
                [], [], 
                '''                Brief interface IPv4 network operational
                data for an interface
                ''',
                'brief',
                'Cisco-IOS-XR-ipv4-io-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-io-oper',
            'briefs',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-io-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper'
        ),
    },
    'Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.Acl' : {
        'meta_info' : _MetaInfoClass('Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.Acl',
            False, 
            [
            _MetaInfoClassMember('common-in-bound', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Common ACL applied to incoming packets
                ''',
                'common_in_bound',
                'Cisco-IOS-XR-ipv4-io-oper', False),
            _MetaInfoClassMember('common-out-bound', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Common ACL applied to outgoing packets
                ''',
                'common_out_bound',
                'Cisco-IOS-XR-ipv4-io-oper', False),
            _MetaInfoClassMember('inbound', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                ACL applied to incoming packets
                ''',
                'inbound',
                'Cisco-IOS-XR-ipv4-io-oper', False),
            _MetaInfoClassMember('outbound', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                ACL applied to outgoing packets
                ''',
                'outbound',
                'Cisco-IOS-XR-ipv4-io-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-io-oper',
            'acl',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-io-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper'
        ),
    },
    'Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.MultiAcl' : {
        'meta_info' : _MetaInfoClass('Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.MultiAcl',
            False, 
            [
            _MetaInfoClassMember('common', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [], 
                '''                Common ACLs
                ''',
                'common',
                'Cisco-IOS-XR-ipv4-io-oper', False, max_elements=5),
            _MetaInfoClassMember('inbound', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [], 
                '''                Inbound ACLs
                ''',
                'inbound',
                'Cisco-IOS-XR-ipv4-io-oper', False, max_elements=5),
            _MetaInfoClassMember('outbound', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [], 
                '''                Outbound ACLs
                ''',
                'outbound',
                'Cisco-IOS-XR-ipv4-io-oper', False, max_elements=5),
            ],
            'Cisco-IOS-XR-ipv4-io-oper',
            'multi-acl',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-io-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper'
        ),
    },
    'Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.HelperAddress' : {
        'meta_info' : _MetaInfoClass('Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.HelperAddress',
            False, 
            [
            _MetaInfoClassMember('address-array', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Helper address
                ''',
                'address_array',
                'Cisco-IOS-XR-ipv4-io-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-io-oper',
            'helper-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-io-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper'
        ),
    },
    'Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.Rpf' : {
        'meta_info' : _MetaInfoClass('Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.Rpf',
            False, 
            [
            _MetaInfoClassMember('allow-default-route', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Allow Default Route
                ''',
                'allow_default_route',
                'Cisco-IOS-XR-ipv4-io-oper', False),
            _MetaInfoClassMember('allow-self-ping', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Allow Self Ping
                ''',
                'allow_self_ping',
                'Cisco-IOS-XR-ipv4-io-oper', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable RPF config
                ''',
                'enable',
                'Cisco-IOS-XR-ipv4-io-oper', False),
            _MetaInfoClassMember('mode', REFERENCE_ENUM_CLASS, 'RpfModeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper', 'RpfModeEnum', 
                [], [], 
                '''                RPF Mode (loose/strict)
                ''',
                'mode',
                'Cisco-IOS-XR-ipv4-io-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-io-oper',
            'rpf',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-io-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper'
        ),
    },
    'Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.BgpPa.Input' : {
        'meta_info' : _MetaInfoClass('Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.BgpPa.Input',
            False, 
            [
            _MetaInfoClassMember('destination', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable destination accouting
                ''',
                'destination',
                'Cisco-IOS-XR-ipv4-io-oper', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable BGP PA for ingress/egress
                ''',
                'enable',
                'Cisco-IOS-XR-ipv4-io-oper', False),
            _MetaInfoClassMember('source', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable source accouting
                ''',
                'source',
                'Cisco-IOS-XR-ipv4-io-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-io-oper',
            'input',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-io-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper'
        ),
    },
    'Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.BgpPa.Output' : {
        'meta_info' : _MetaInfoClass('Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.BgpPa.Output',
            False, 
            [
            _MetaInfoClassMember('destination', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable destination accouting
                ''',
                'destination',
                'Cisco-IOS-XR-ipv4-io-oper', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable BGP PA for ingress/egress
                ''',
                'enable',
                'Cisco-IOS-XR-ipv4-io-oper', False),
            _MetaInfoClassMember('source', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable source accouting
                ''',
                'source',
                'Cisco-IOS-XR-ipv4-io-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-io-oper',
            'output',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-io-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper'
        ),
    },
    'Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.BgpPa' : {
        'meta_info' : _MetaInfoClass('Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.BgpPa',
            False, 
            [
            _MetaInfoClassMember('input', REFERENCE_CLASS, 'Input' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper', 'Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.BgpPa.Input', 
                [], [], 
                '''                BGP PA input config
                ''',
                'input',
                'Cisco-IOS-XR-ipv4-io-oper', False),
            _MetaInfoClassMember('output', REFERENCE_CLASS, 'Output' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper', 'Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.BgpPa.Output', 
                [], [], 
                '''                BGP PA output config
                ''',
                'output',
                'Cisco-IOS-XR-ipv4-io-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-io-oper',
            'bgp-pa',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-io-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper'
        ),
    },
    'Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.PubUtime' : {
        'meta_info' : _MetaInfoClass('Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.PubUtime',
            False, 
            [
            ],
            'Cisco-IOS-XR-ipv4-io-oper',
            'pub-utime',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-io-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper'
        ),
    },
    'Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.IdbUtime' : {
        'meta_info' : _MetaInfoClass('Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.IdbUtime',
            False, 
            [
            ],
            'Cisco-IOS-XR-ipv4-io-oper',
            'idb-utime',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-io-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper'
        ),
    },
    'Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.CapsUtime' : {
        'meta_info' : _MetaInfoClass('Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.CapsUtime',
            False, 
            [
            ],
            'Cisco-IOS-XR-ipv4-io-oper',
            'caps-utime',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-io-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper'
        ),
    },
    'Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.FwdEnUtime' : {
        'meta_info' : _MetaInfoClass('Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.FwdEnUtime',
            False, 
            [
            ],
            'Cisco-IOS-XR-ipv4-io-oper',
            'fwd-en-utime',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-io-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper'
        ),
    },
    'Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.FwdDisUtime' : {
        'meta_info' : _MetaInfoClass('Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.FwdDisUtime',
            False, 
            [
            ],
            'Cisco-IOS-XR-ipv4-io-oper',
            'fwd-dis-utime',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-io-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper'
        ),
    },
    'Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.MulticastGroup' : {
        'meta_info' : _MetaInfoClass('Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.MulticastGroup',
            False, 
            [
            _MetaInfoClassMember('group-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Address of multicast group
                ''',
                'group_address',
                'Cisco-IOS-XR-ipv4-io-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-io-oper',
            'multicast-group',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-io-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper'
        ),
    },
    'Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.SecondaryAddress' : {
        'meta_info' : _MetaInfoClass('Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.SecondaryAddress',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Address
                ''',
                'address',
                'Cisco-IOS-XR-ipv4-io-oper', False),
            _MetaInfoClassMember('prefix-length', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Prefix length of address
                ''',
                'prefix_length',
                'Cisco-IOS-XR-ipv4-io-oper', False),
            _MetaInfoClassMember('route-tag', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Route Tag associated with this address (0 = no
                tag)
                ''',
                'route_tag',
                'Cisco-IOS-XR-ipv4-io-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-io-oper',
            'secondary-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-io-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper'
        ),
    },
    'Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail' : {
        'meta_info' : _MetaInfoClass('Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                The name of the interface
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv4-io-oper', True),
            _MetaInfoClassMember('acl', REFERENCE_CLASS, 'Acl' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper', 'Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.Acl', 
                [], [], 
                '''                ACLs configured on the interface
                ''',
                'acl',
                'Cisco-IOS-XR-ipv4-io-oper', False),
            _MetaInfoClassMember('bgp-pa', REFERENCE_CLASS, 'BgpPa' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper', 'Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.BgpPa', 
                [], [], 
                '''                BGP PA config on the interface
                ''',
                'bgp_pa',
                'Cisco-IOS-XR-ipv4-io-oper', False),
            _MetaInfoClassMember('caps-utime', REFERENCE_CLASS, 'CapsUtime' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper', 'Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.CapsUtime', 
                [], [], 
                '''                CAPS Add Time
                ''',
                'caps_utime',
                'Cisco-IOS-XR-ipv4-io-oper', False),
            _MetaInfoClassMember('direct-broadcast', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Are direct broadcasts sent on the interface?
                ''',
                'direct_broadcast',
                'Cisco-IOS-XR-ipv4-io-oper', False),
            _MetaInfoClassMember('flow-tag-dst', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is BGP Flow Tag Destination is enable
                ''',
                'flow_tag_dst',
                'Cisco-IOS-XR-ipv4-io-oper', False),
            _MetaInfoClassMember('flow-tag-src', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is BGP Flow Tag Source is enable
                ''',
                'flow_tag_src',
                'Cisco-IOS-XR-ipv4-io-oper', False),
            _MetaInfoClassMember('fwd-dis-utime', REFERENCE_CLASS, 'FwdDisUtime' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper', 'Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.FwdDisUtime', 
                [], [], 
                '''                FWD DISABLE Time
                ''',
                'fwd_dis_utime',
                'Cisco-IOS-XR-ipv4-io-oper', False),
            _MetaInfoClassMember('fwd-en-utime', REFERENCE_CLASS, 'FwdEnUtime' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper', 'Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.FwdEnUtime', 
                [], [], 
                '''                FWD ENABLE Time
                ''',
                'fwd_en_utime',
                'Cisco-IOS-XR-ipv4-io-oper', False),
            _MetaInfoClassMember('helper-address', REFERENCE_CLASS, 'HelperAddress' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper', 'Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.HelperAddress', 
                [], [], 
                '''                Helper Addresses configured on the interface
                ''',
                'helper_address',
                'Cisco-IOS-XR-ipv4-io-oper', False),
            _MetaInfoClassMember('idb-utime', REFERENCE_CLASS, 'IdbUtime' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper', 'Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.IdbUtime', 
                [], [], 
                '''                IDB Create Time
                ''',
                'idb_utime',
                'Cisco-IOS-XR-ipv4-io-oper', False),
            _MetaInfoClassMember('line-state', REFERENCE_ENUM_CLASS, 'Ipv4MaOperLineStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper', 'Ipv4MaOperLineStateEnum', 
                [], [], 
                '''                Line state of the interface
                ''',
                'line_state',
                'Cisco-IOS-XR-ipv4-io-oper', False),
            _MetaInfoClassMember('mask-reply', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Are mask replies sent on the interface?
                ''',
                'mask_reply',
                'Cisco-IOS-XR-ipv4-io-oper', False),
            _MetaInfoClassMember('mlacp-active', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is mLACP state Active (valid if RG ID exists)
                ''',
                'mlacp_active',
                'Cisco-IOS-XR-ipv4-io-oper', False),
            _MetaInfoClassMember('mtu', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                IP MTU of the interface
                ''',
                'mtu',
                'Cisco-IOS-XR-ipv4-io-oper', False),
            _MetaInfoClassMember('multi-acl', REFERENCE_CLASS, 'MultiAcl' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper', 'Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.MultiAcl', 
                [], [], 
                '''                Multi ACLs configured on the interface
                ''',
                'multi_acl',
                'Cisco-IOS-XR-ipv4-io-oper', False),
            _MetaInfoClassMember('multicast-group', REFERENCE_LIST, 'MulticastGroup' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper', 'Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.MulticastGroup', 
                [], [], 
                '''                Multicast groups joined on the interface
                ''',
                'multicast_group',
                'Cisco-IOS-XR-ipv4-io-oper', False),
            _MetaInfoClassMember('prefix-length', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Prefix length of primary address
                ''',
                'prefix_length',
                'Cisco-IOS-XR-ipv4-io-oper', False),
            _MetaInfoClassMember('primary-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Primary address
                ''',
                'primary_address',
                'Cisco-IOS-XR-ipv4-io-oper', False),
            _MetaInfoClassMember('proxy-arp-disabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is Proxy ARP disabled on the interface?
                ''',
                'proxy_arp_disabled',
                'Cisco-IOS-XR-ipv4-io-oper', False),
            _MetaInfoClassMember('pub-utime', REFERENCE_CLASS, 'PubUtime' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper', 'Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.PubUtime', 
                [], [], 
                '''                Address Publish Time
                ''',
                'pub_utime',
                'Cisco-IOS-XR-ipv4-io-oper', False),
            _MetaInfoClassMember('redirect', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Are ICMP redirects sent on the interface?
                ''',
                'redirect',
                'Cisco-IOS-XR-ipv4-io-oper', False),
            _MetaInfoClassMember('rg-id-exists', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Does ICCP RG ID exist on the interface?
                ''',
                'rg_id_exists',
                'Cisco-IOS-XR-ipv4-io-oper', False),
            _MetaInfoClassMember('route-tag', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Route tag associated with the primary address (0
                = no tag)
                ''',
                'route_tag',
                'Cisco-IOS-XR-ipv4-io-oper', False),
            _MetaInfoClassMember('rpf', REFERENCE_CLASS, 'Rpf' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper', 'Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.Rpf', 
                [], [], 
                '''                RPF config on the interface
                ''',
                'rpf',
                'Cisco-IOS-XR-ipv4-io-oper', False),
            _MetaInfoClassMember('secondary-address', REFERENCE_LIST, 'SecondaryAddress' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper', 'Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.SecondaryAddress', 
                [], [], 
                '''                Secondary addresses on the interface
                ''',
                'secondary_address',
                'Cisco-IOS-XR-ipv4-io-oper', False),
            _MetaInfoClassMember('unnumbered-interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of referenced interface (valid if
                unnumbered)
                ''',
                'unnumbered_interface_name',
                'Cisco-IOS-XR-ipv4-io-oper', False),
            _MetaInfoClassMember('unreachable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Are ICMP unreachables sent on the interface?
                ''',
                'unreachable',
                'Cisco-IOS-XR-ipv4-io-oper', False),
            _MetaInfoClassMember('vrf-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                VRF ID of the interface
                ''',
                'vrf_id',
                'Cisco-IOS-XR-ipv4-io-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-io-oper',
            'detail',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-io-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper'
        ),
    },
    'Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details' : {
        'meta_info' : _MetaInfoClass('Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details',
            False, 
            [
            _MetaInfoClassMember('detail', REFERENCE_LIST, 'Detail' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper', 'Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail', 
                [], [], 
                '''                Detail interface IPv4 network operational
                data for an interface
                ''',
                'detail',
                'Cisco-IOS-XR-ipv4-io-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-io-oper',
            'details',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-io-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper'
        ),
    },
    'Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf' : {
        'meta_info' : _MetaInfoClass('Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf',
            False, 
            [
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The VRF name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-ipv4-io-oper', True),
            _MetaInfoClassMember('briefs', REFERENCE_CLASS, 'Briefs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper', 'Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Briefs', 
                [], [], 
                '''                Brief interface IPv4 network operational
                data for a node
                ''',
                'briefs',
                'Cisco-IOS-XR-ipv4-io-oper', False),
            _MetaInfoClassMember('details', REFERENCE_CLASS, 'Details' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper', 'Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details', 
                [], [], 
                '''                Detail interface IPv4 network operational
                data for a node
                ''',
                'details',
                'Cisco-IOS-XR-ipv4-io-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-io-oper',
            'vrf',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-io-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper'
        ),
    },
    'Ipv4Network.Nodes.Node.InterfaceData.Vrfs' : {
        'meta_info' : _MetaInfoClass('Ipv4Network.Nodes.Node.InterfaceData.Vrfs',
            False, 
            [
            _MetaInfoClassMember('vrf', REFERENCE_LIST, 'Vrf' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper', 'Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf', 
                [], [], 
                '''                VRF name of an interface belong to
                ''',
                'vrf',
                'Cisco-IOS-XR-ipv4-io-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-io-oper',
            'vrfs',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-io-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper'
        ),
    },
    'Ipv4Network.Nodes.Node.InterfaceData.Summary.IfUpUp' : {
        'meta_info' : _MetaInfoClass('Ipv4Network.Nodes.Node.InterfaceData.Summary.IfUpUp',
            False, 
            [
            _MetaInfoClassMember('ip-assigned', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of interfaces with explicit addresses
                ''',
                'ip_assigned',
                'Cisco-IOS-XR-ipv4-io-oper', False),
            _MetaInfoClassMember('ip-unassigned', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of unassigned interfaces with explicit
                addresses
                ''',
                'ip_unassigned',
                'Cisco-IOS-XR-ipv4-io-oper', False),
            _MetaInfoClassMember('ip-unnumbered', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of unnumbered interfaces with explicit
                addresses
                ''',
                'ip_unnumbered',
                'Cisco-IOS-XR-ipv4-io-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-io-oper',
            'if-up-up',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-io-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper'
        ),
    },
    'Ipv4Network.Nodes.Node.InterfaceData.Summary.IfUpDown' : {
        'meta_info' : _MetaInfoClass('Ipv4Network.Nodes.Node.InterfaceData.Summary.IfUpDown',
            False, 
            [
            _MetaInfoClassMember('ip-assigned', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of interfaces with explicit addresses
                ''',
                'ip_assigned',
                'Cisco-IOS-XR-ipv4-io-oper', False),
            _MetaInfoClassMember('ip-unassigned', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of unassigned interfaces with explicit
                addresses
                ''',
                'ip_unassigned',
                'Cisco-IOS-XR-ipv4-io-oper', False),
            _MetaInfoClassMember('ip-unnumbered', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of unnumbered interfaces with explicit
                addresses
                ''',
                'ip_unnumbered',
                'Cisco-IOS-XR-ipv4-io-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-io-oper',
            'if-up-down',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-io-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper'
        ),
    },
    'Ipv4Network.Nodes.Node.InterfaceData.Summary.IfDownDown' : {
        'meta_info' : _MetaInfoClass('Ipv4Network.Nodes.Node.InterfaceData.Summary.IfDownDown',
            False, 
            [
            _MetaInfoClassMember('ip-assigned', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of interfaces with explicit addresses
                ''',
                'ip_assigned',
                'Cisco-IOS-XR-ipv4-io-oper', False),
            _MetaInfoClassMember('ip-unassigned', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of unassigned interfaces with explicit
                addresses
                ''',
                'ip_unassigned',
                'Cisco-IOS-XR-ipv4-io-oper', False),
            _MetaInfoClassMember('ip-unnumbered', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of unnumbered interfaces with explicit
                addresses
                ''',
                'ip_unnumbered',
                'Cisco-IOS-XR-ipv4-io-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-io-oper',
            'if-down-down',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-io-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper'
        ),
    },
    'Ipv4Network.Nodes.Node.InterfaceData.Summary.IfShutdownDown' : {
        'meta_info' : _MetaInfoClass('Ipv4Network.Nodes.Node.InterfaceData.Summary.IfShutdownDown',
            False, 
            [
            _MetaInfoClassMember('ip-assigned', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of interfaces with explicit addresses
                ''',
                'ip_assigned',
                'Cisco-IOS-XR-ipv4-io-oper', False),
            _MetaInfoClassMember('ip-unassigned', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of unassigned interfaces with explicit
                addresses
                ''',
                'ip_unassigned',
                'Cisco-IOS-XR-ipv4-io-oper', False),
            _MetaInfoClassMember('ip-unnumbered', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of unnumbered interfaces with explicit
                addresses
                ''',
                'ip_unnumbered',
                'Cisco-IOS-XR-ipv4-io-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-io-oper',
            'if-shutdown-down',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-io-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper'
        ),
    },
    'Ipv4Network.Nodes.Node.InterfaceData.Summary' : {
        'meta_info' : _MetaInfoClass('Ipv4Network.Nodes.Node.InterfaceData.Summary',
            False, 
            [
            _MetaInfoClassMember('if-down-down', REFERENCE_CLASS, 'IfDownDown' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper', 'Ipv4Network.Nodes.Node.InterfaceData.Summary.IfDownDown', 
                [], [], 
                '''                Number of interfaces (down,down)
                ''',
                'if_down_down',
                'Cisco-IOS-XR-ipv4-io-oper', False),
            _MetaInfoClassMember('if-shutdown-down', REFERENCE_CLASS, 'IfShutdownDown' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper', 'Ipv4Network.Nodes.Node.InterfaceData.Summary.IfShutdownDown', 
                [], [], 
                '''                Number of interfaces (shutdown,down)
                ''',
                'if_shutdown_down',
                'Cisco-IOS-XR-ipv4-io-oper', False),
            _MetaInfoClassMember('if-up-down', REFERENCE_CLASS, 'IfUpDown' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper', 'Ipv4Network.Nodes.Node.InterfaceData.Summary.IfUpDown', 
                [], [], 
                '''                Number of interfaces (up,down)
                ''',
                'if_up_down',
                'Cisco-IOS-XR-ipv4-io-oper', False),
            _MetaInfoClassMember('if-up-down-basecaps-up', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of interfaces (up,down) with basecaps up
                ''',
                'if_up_down_basecaps_up',
                'Cisco-IOS-XR-ipv4-io-oper', False),
            _MetaInfoClassMember('if-up-up', REFERENCE_CLASS, 'IfUpUp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper', 'Ipv4Network.Nodes.Node.InterfaceData.Summary.IfUpUp', 
                [], [], 
                '''                Number of interfaces (up,up)
                ''',
                'if_up_up',
                'Cisco-IOS-XR-ipv4-io-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-io-oper',
            'summary',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-io-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper'
        ),
    },
    'Ipv4Network.Nodes.Node.InterfaceData' : {
        'meta_info' : _MetaInfoClass('Ipv4Network.Nodes.Node.InterfaceData',
            False, 
            [
            _MetaInfoClassMember('summary', REFERENCE_CLASS, 'Summary' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper', 'Ipv4Network.Nodes.Node.InterfaceData.Summary', 
                [], [], 
                '''                Summary of IPv4 network operational interface
                data on a node
                ''',
                'summary',
                'Cisco-IOS-XR-ipv4-io-oper', False),
            _MetaInfoClassMember('vrfs', REFERENCE_CLASS, 'Vrfs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper', 'Ipv4Network.Nodes.Node.InterfaceData.Vrfs', 
                [], [], 
                '''                VRF specific IPv4 network operational
                interface data
                ''',
                'vrfs',
                'Cisco-IOS-XR-ipv4-io-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-io-oper',
            'interface-data',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-io-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper'
        ),
    },
    'Ipv4Network.Nodes.Node.Statistics.Traffic.Ipv4Stats' : {
        'meta_info' : _MetaInfoClass('Ipv4Network.Nodes.Node.Statistics.Traffic.Ipv4Stats',
            False, 
            [
            _MetaInfoClassMember('bad-header', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Bad Header
                ''',
                'bad_header',
                'Cisco-IOS-XR-ipv4-io-oper', False),
            _MetaInfoClassMember('bad-hop-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Bad Hop Count
                ''',
                'bad_hop_count',
                'Cisco-IOS-XR-ipv4-io-oper', False),
            _MetaInfoClassMember('bad-option', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Bad Option
                ''',
                'bad_option',
                'Cisco-IOS-XR-ipv4-io-oper', False),
            _MetaInfoClassMember('bad-security-option', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Bad Security Option
                ''',
                'bad_security_option',
                'Cisco-IOS-XR-ipv4-io-oper', False),
            _MetaInfoClassMember('bad-source-address', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Bad Source Address
                ''',
                'bad_source_address',
                'Cisco-IOS-XR-ipv4-io-oper', False),
            _MetaInfoClassMember('basic-security-option', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Basic Security Option
                ''',
                'basic_security_option',
                'Cisco-IOS-XR-ipv4-io-oper', False),
            _MetaInfoClassMember('broadcast-in', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Broadcast In
                ''',
                'broadcast_in',
                'Cisco-IOS-XR-ipv4-io-oper', False),
            _MetaInfoClassMember('broadcast-out', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Broadcast Out
                ''',
                'broadcast_out',
                'Cisco-IOS-XR-ipv4-io-oper', False),
            _MetaInfoClassMember('cipso-option', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Cipso Option
                ''',
                'cipso_option',
                'Cisco-IOS-XR-ipv4-io-oper', False),
            _MetaInfoClassMember('encapsulation-failed', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Encapsulation Failed
                ''',
                'encapsulation_failed',
                'Cisco-IOS-XR-ipv4-io-oper', False),
            _MetaInfoClassMember('end-option', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                End Option
                ''',
                'end_option',
                'Cisco-IOS-XR-ipv4-io-oper', False),
            _MetaInfoClassMember('extended-security-option', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Extended Security Option
                ''',
                'extended_security_option',
                'Cisco-IOS-XR-ipv4-io-oper', False),
            _MetaInfoClassMember('format-errors', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Format Errors
                ''',
                'format_errors',
                'Cisco-IOS-XR-ipv4-io-oper', False),
            _MetaInfoClassMember('fragment-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Fragment Count
                ''',
                'fragment_count',
                'Cisco-IOS-XR-ipv4-io-oper', False),
            _MetaInfoClassMember('input-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Input Packets
                ''',
                'input_packets',
                'Cisco-IOS-XR-ipv4-io-oper', False),
            _MetaInfoClassMember('lisp-decap-error', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Lisp decap errors
                ''',
                'lisp_decap_error',
                'Cisco-IOS-XR-ipv4-io-oper', False),
            _MetaInfoClassMember('lisp-encap-error', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Lisp encap errors
                ''',
                'lisp_encap_error',
                'Cisco-IOS-XR-ipv4-io-oper', False),
            _MetaInfoClassMember('lisp-v4-decap', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Lisp IPv4 decapped packets
                ''',
                'lisp_v4_decap',
                'Cisco-IOS-XR-ipv4-io-oper', False),
            _MetaInfoClassMember('lisp-v4-encap', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Lisp IPv4 encapped packets
                ''',
                'lisp_v4_encap',
                'Cisco-IOS-XR-ipv4-io-oper', False),
            _MetaInfoClassMember('lisp-v6-decap', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Lisp IPv6 decapped packets
                ''',
                'lisp_v6_decap',
                'Cisco-IOS-XR-ipv4-io-oper', False),
            _MetaInfoClassMember('lisp-v6-encap', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Lisp IPv6 encapped packets
                ''',
                'lisp_v6_encap',
                'Cisco-IOS-XR-ipv4-io-oper', False),
            _MetaInfoClassMember('loose-source-route-option', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Loose Source Route Option
                ''',
                'loose_source_route_option',
                'Cisco-IOS-XR-ipv4-io-oper', False),
            _MetaInfoClassMember('multicast-in', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Multicast In
                ''',
                'multicast_in',
                'Cisco-IOS-XR-ipv4-io-oper', False),
            _MetaInfoClassMember('multicast-out', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Multicast Out
                ''',
                'multicast_out',
                'Cisco-IOS-XR-ipv4-io-oper', False),
            _MetaInfoClassMember('no-gateway', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                No Gateway
                ''',
                'no_gateway',
                'Cisco-IOS-XR-ipv4-io-oper', False),
            _MetaInfoClassMember('no-protocol', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                No Protocol
                ''',
                'no_protocol',
                'Cisco-IOS-XR-ipv4-io-oper', False),
            _MetaInfoClassMember('no-router', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                No Router
                ''',
                'no_router',
                'Cisco-IOS-XR-ipv4-io-oper', False),
            _MetaInfoClassMember('noop-option', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Noop Option
                ''',
                'noop_option',
                'Cisco-IOS-XR-ipv4-io-oper', False),
            _MetaInfoClassMember('options-present', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                IP Options Present
                ''',
                'options_present',
                'Cisco-IOS-XR-ipv4-io-oper', False),
            _MetaInfoClassMember('packet-too-big', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Packet Too Big
                ''',
                'packet_too_big',
                'Cisco-IOS-XR-ipv4-io-oper', False),
            _MetaInfoClassMember('packets-forwarded', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Packets Forwarded
                ''',
                'packets_forwarded',
                'Cisco-IOS-XR-ipv4-io-oper', False),
            _MetaInfoClassMember('packets-fragmented', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Packets Fragmented
                ''',
                'packets_fragmented',
                'Cisco-IOS-XR-ipv4-io-oper', False),
            _MetaInfoClassMember('packets-output', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Packets Output
                ''',
                'packets_output',
                'Cisco-IOS-XR-ipv4-io-oper', False),
            _MetaInfoClassMember('reassemble-failed', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Reassembly Failed
                ''',
                'reassemble_failed',
                'Cisco-IOS-XR-ipv4-io-oper', False),
            _MetaInfoClassMember('reassemble-input', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                RaInput
                ''',
                'reassemble_input',
                'Cisco-IOS-XR-ipv4-io-oper', False),
            _MetaInfoClassMember('reassemble-max-drop', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Reassembly Max Drop
                ''',
                'reassemble_max_drop',
                'Cisco-IOS-XR-ipv4-io-oper', False),
            _MetaInfoClassMember('reassemble-timeout', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Reassembly Timeout
                ''',
                'reassemble_timeout',
                'Cisco-IOS-XR-ipv4-io-oper', False),
            _MetaInfoClassMember('reassembled', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Reassembled
                ''',
                'reassembled',
                'Cisco-IOS-XR-ipv4-io-oper', False),
            _MetaInfoClassMember('received-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Received Packets
                ''',
                'received_packets',
                'Cisco-IOS-XR-ipv4-io-oper', False),
            _MetaInfoClassMember('record-route-option', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Record Route Option
                ''',
                'record_route_option',
                'Cisco-IOS-XR-ipv4-io-oper', False),
            _MetaInfoClassMember('router-alert-option', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Router Alert Option
                ''',
                'router_alert_option',
                'Cisco-IOS-XR-ipv4-io-oper', False),
            _MetaInfoClassMember('sid-option', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                SID Option
                ''',
                'sid_option',
                'Cisco-IOS-XR-ipv4-io-oper', False),
            _MetaInfoClassMember('strict-source-route-option', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Strict Source Route Option
                ''',
                'strict_source_route_option',
                'Cisco-IOS-XR-ipv4-io-oper', False),
            _MetaInfoClassMember('timestamp-option', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Timestamp Option
                ''',
                'timestamp_option',
                'Cisco-IOS-XR-ipv4-io-oper', False),
            _MetaInfoClassMember('unknown-option', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Unknown Option
                ''',
                'unknown_option',
                'Cisco-IOS-XR-ipv4-io-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-io-oper',
            'ipv4-stats',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-io-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper'
        ),
    },
    'Ipv4Network.Nodes.Node.Statistics.Traffic.IcmpStats' : {
        'meta_info' : _MetaInfoClass('Ipv4Network.Nodes.Node.Statistics.Traffic.IcmpStats',
            False, 
            [
            _MetaInfoClassMember('admin-unreachable-received', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ICMP Admin Unreachable Received
                ''',
                'admin_unreachable_received',
                'Cisco-IOS-XR-ipv4-io-oper', False),
            _MetaInfoClassMember('admin-unreachable-sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ICMP Admin Unreachable Sent
                ''',
                'admin_unreachable_sent',
                'Cisco-IOS-XR-ipv4-io-oper', False),
            _MetaInfoClassMember('checksum-error', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ICMP Checksum Errors
                ''',
                'checksum_error',
                'Cisco-IOS-XR-ipv4-io-oper', False),
            _MetaInfoClassMember('echo-reply-received', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ICMP Echo Reply Received
                ''',
                'echo_reply_received',
                'Cisco-IOS-XR-ipv4-io-oper', False),
            _MetaInfoClassMember('echo-reply-sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ICMP Echo Reply Sent
                ''',
                'echo_reply_sent',
                'Cisco-IOS-XR-ipv4-io-oper', False),
            _MetaInfoClassMember('echo-request-received', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ICMP Echo Request Sent
                ''',
                'echo_request_received',
                'Cisco-IOS-XR-ipv4-io-oper', False),
            _MetaInfoClassMember('echo-request-sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ICMP Echo Request Sent
                ''',
                'echo_request_sent',
                'Cisco-IOS-XR-ipv4-io-oper', False),
            _MetaInfoClassMember('fragment-unreachable-received', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ICMP Fragment Unreachable Received
                ''',
                'fragment_unreachable_received',
                'Cisco-IOS-XR-ipv4-io-oper', False),
            _MetaInfoClassMember('fragment-unreachable-sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ICMP Fragment Unreachable Sent
                ''',
                'fragment_unreachable_sent',
                'Cisco-IOS-XR-ipv4-io-oper', False),
            _MetaInfoClassMember('hopcount-received', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ICMP Hopcount Received
                ''',
                'hopcount_received',
                'Cisco-IOS-XR-ipv4-io-oper', False),
            _MetaInfoClassMember('hopcount-sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ICMP Hopcount Sent
                ''',
                'hopcount_sent',
                'Cisco-IOS-XR-ipv4-io-oper', False),
            _MetaInfoClassMember('host-unreachable-received', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ICMP Host Unreachable Received
                ''',
                'host_unreachable_received',
                'Cisco-IOS-XR-ipv4-io-oper', False),
            _MetaInfoClassMember('host-unreachable-sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ICMP Host Unreachable Sent
                ''',
                'host_unreachable_sent',
                'Cisco-IOS-XR-ipv4-io-oper', False),
            _MetaInfoClassMember('mask-reply-received', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ICMP Mask Received
                ''',
                'mask_reply_received',
                'Cisco-IOS-XR-ipv4-io-oper', False),
            _MetaInfoClassMember('mask-reply-sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ICMP Mask Sent
                ''',
                'mask_reply_sent',
                'Cisco-IOS-XR-ipv4-io-oper', False),
            _MetaInfoClassMember('mask-request-received', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ICMP Mask Received
                ''',
                'mask_request_received',
                'Cisco-IOS-XR-ipv4-io-oper', False),
            _MetaInfoClassMember('mask-request-sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ICMP Mask Sent
                ''',
                'mask_request_sent',
                'Cisco-IOS-XR-ipv4-io-oper', False),
            _MetaInfoClassMember('network-unreachable-received', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ICMP Network Unreachable Received
                ''',
                'network_unreachable_received',
                'Cisco-IOS-XR-ipv4-io-oper', False),
            _MetaInfoClassMember('network-unreachable-sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ICMP Network Unreachable Sent
                ''',
                'network_unreachable_sent',
                'Cisco-IOS-XR-ipv4-io-oper', False),
            _MetaInfoClassMember('output', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ICMP Transmitted
                ''',
                'output',
                'Cisco-IOS-XR-ipv4-io-oper', False),
            _MetaInfoClassMember('param-error-received', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ICMP Parameter Error Received
                ''',
                'param_error_received',
                'Cisco-IOS-XR-ipv4-io-oper', False),
            _MetaInfoClassMember('param-error-send', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ICMP Parameter Error Sent
                ''',
                'param_error_send',
                'Cisco-IOS-XR-ipv4-io-oper', False),
            _MetaInfoClassMember('port-unreachable-received', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ICMP Port Unreachable Received
                ''',
                'port_unreachable_received',
                'Cisco-IOS-XR-ipv4-io-oper', False),
            _MetaInfoClassMember('port-unreachable-sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ICMP Port Unreachable Sent
                ''',
                'port_unreachable_sent',
                'Cisco-IOS-XR-ipv4-io-oper', False),
            _MetaInfoClassMember('protocol-unreachable-received', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ICMP Protocol Unreachable Received
                ''',
                'protocol_unreachable_received',
                'Cisco-IOS-XR-ipv4-io-oper', False),
            _MetaInfoClassMember('protocol-unreachable-sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ICMP Protocol Unreachable Sent
                ''',
                'protocol_unreachable_sent',
                'Cisco-IOS-XR-ipv4-io-oper', False),
            _MetaInfoClassMember('reassebly-received', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ICMP Reassembly Received
                ''',
                'reassebly_received',
                'Cisco-IOS-XR-ipv4-io-oper', False),
            _MetaInfoClassMember('reassembly-sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ICMP Reassembly Sent
                ''',
                'reassembly_sent',
                'Cisco-IOS-XR-ipv4-io-oper', False),
            _MetaInfoClassMember('received', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ICMP Received
                ''',
                'received',
                'Cisco-IOS-XR-ipv4-io-oper', False),
            _MetaInfoClassMember('redirect-received', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ICMP Redirect Received
                ''',
                'redirect_received',
                'Cisco-IOS-XR-ipv4-io-oper', False),
            _MetaInfoClassMember('redirect-send', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ICMP Redirect Sent
                ''',
                'redirect_send',
                'Cisco-IOS-XR-ipv4-io-oper', False),
            _MetaInfoClassMember('router-advert-received', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ICMP Router Advertisement Received
                ''',
                'router_advert_received',
                'Cisco-IOS-XR-ipv4-io-oper', False),
            _MetaInfoClassMember('router-solicit-received', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ICMP Router Solicited Received
                ''',
                'router_solicit_received',
                'Cisco-IOS-XR-ipv4-io-oper', False),
            _MetaInfoClassMember('source-quench-received', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ICMP Source Quench
                ''',
                'source_quench_received',
                'Cisco-IOS-XR-ipv4-io-oper', False),
            _MetaInfoClassMember('timestamp-received', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ICMP Timestamp Received
                ''',
                'timestamp_received',
                'Cisco-IOS-XR-ipv4-io-oper', False),
            _MetaInfoClassMember('timestamp-reply-received', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ICMP Timestamp Reply Received
                ''',
                'timestamp_reply_received',
                'Cisco-IOS-XR-ipv4-io-oper', False),
            _MetaInfoClassMember('unknown', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ICMP Unknown
                ''',
                'unknown',
                'Cisco-IOS-XR-ipv4-io-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-io-oper',
            'icmp-stats',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-io-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper'
        ),
    },
    'Ipv4Network.Nodes.Node.Statistics.Traffic' : {
        'meta_info' : _MetaInfoClass('Ipv4Network.Nodes.Node.Statistics.Traffic',
            False, 
            [
            _MetaInfoClassMember('icmp-stats', REFERENCE_CLASS, 'IcmpStats' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper', 'Ipv4Network.Nodes.Node.Statistics.Traffic.IcmpStats', 
                [], [], 
                '''                ICMP Stats
                ''',
                'icmp_stats',
                'Cisco-IOS-XR-ipv4-io-oper', False),
            _MetaInfoClassMember('ipv4-stats', REFERENCE_CLASS, 'Ipv4Stats' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper', 'Ipv4Network.Nodes.Node.Statistics.Traffic.Ipv4Stats', 
                [], [], 
                '''                IPv4 Network Stats
                ''',
                'ipv4_stats',
                'Cisco-IOS-XR-ipv4-io-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-io-oper',
            'traffic',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-io-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper'
        ),
    },
    'Ipv4Network.Nodes.Node.Statistics' : {
        'meta_info' : _MetaInfoClass('Ipv4Network.Nodes.Node.Statistics',
            False, 
            [
            _MetaInfoClassMember('traffic', REFERENCE_CLASS, 'Traffic' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper', 'Ipv4Network.Nodes.Node.Statistics.Traffic', 
                [], [], 
                '''                Traffic statistics for a node
                ''',
                'traffic',
                'Cisco-IOS-XR-ipv4-io-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-io-oper',
            'statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-io-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper'
        ),
    },
    'Ipv4Network.Nodes.Node' : {
        'meta_info' : _MetaInfoClass('Ipv4Network.Nodes.Node',
            False, 
            [
            _MetaInfoClassMember('node-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                The node name
                ''',
                'node_name',
                'Cisco-IOS-XR-ipv4-io-oper', True),
            _MetaInfoClassMember('interface-data', REFERENCE_CLASS, 'InterfaceData' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper', 'Ipv4Network.Nodes.Node.InterfaceData', 
                [], [], 
                '''                IPv4 network operational interface data
                ''',
                'interface_data',
                'Cisco-IOS-XR-ipv4-io-oper', False),
            _MetaInfoClassMember('statistics', REFERENCE_CLASS, 'Statistics' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper', 'Ipv4Network.Nodes.Node.Statistics', 
                [], [], 
                '''                Statistical IPv4 network operational data for
                a node
                ''',
                'statistics',
                'Cisco-IOS-XR-ipv4-io-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-io-oper',
            'node',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-io-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper'
        ),
    },
    'Ipv4Network.Nodes' : {
        'meta_info' : _MetaInfoClass('Ipv4Network.Nodes',
            False, 
            [
            _MetaInfoClassMember('node', REFERENCE_LIST, 'Node' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper', 'Ipv4Network.Nodes.Node', 
                [], [], 
                '''                IPv4 network operational data for a particular
                node
                ''',
                'node',
                'Cisco-IOS-XR-ipv4-io-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-io-oper',
            'nodes',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-io-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper'
        ),
    },
    'Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.Acl' : {
        'meta_info' : _MetaInfoClass('Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.Acl',
            False, 
            [
            _MetaInfoClassMember('common-in-bound', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Common ACL applied to incoming packets
                ''',
                'common_in_bound',
                'Cisco-IOS-XR-ipv4-ma-oper', False),
            _MetaInfoClassMember('common-out-bound', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Common ACL applied to outgoing packets
                ''',
                'common_out_bound',
                'Cisco-IOS-XR-ipv4-ma-oper', False),
            _MetaInfoClassMember('inbound', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                ACL applied to incoming packets
                ''',
                'inbound',
                'Cisco-IOS-XR-ipv4-ma-oper', False),
            _MetaInfoClassMember('outbound', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                ACL applied to outgoing packets
                ''',
                'outbound',
                'Cisco-IOS-XR-ipv4-ma-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-ma-oper',
            'acl',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ma-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper'
        ),
    },
    'Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.MultiAcl' : {
        'meta_info' : _MetaInfoClass('Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.MultiAcl',
            False, 
            [
            _MetaInfoClassMember('common', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [], 
                '''                Common ACLs
                ''',
                'common',
                'Cisco-IOS-XR-ipv4-ma-oper', False, max_elements=5),
            _MetaInfoClassMember('inbound', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [], 
                '''                Inbound ACLs
                ''',
                'inbound',
                'Cisco-IOS-XR-ipv4-ma-oper', False, max_elements=5),
            _MetaInfoClassMember('outbound', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [], 
                '''                Outbound ACLs
                ''',
                'outbound',
                'Cisco-IOS-XR-ipv4-ma-oper', False, max_elements=5),
            ],
            'Cisco-IOS-XR-ipv4-ma-oper',
            'multi-acl',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ma-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper'
        ),
    },
    'Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.HelperAddress' : {
        'meta_info' : _MetaInfoClass('Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.HelperAddress',
            False, 
            [
            _MetaInfoClassMember('address-array', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Helper address
                ''',
                'address_array',
                'Cisco-IOS-XR-ipv4-ma-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-ma-oper',
            'helper-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ma-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper'
        ),
    },
    'Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.Rpf' : {
        'meta_info' : _MetaInfoClass('Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.Rpf',
            False, 
            [
            _MetaInfoClassMember('allow-default-route', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Allow Default Route
                ''',
                'allow_default_route',
                'Cisco-IOS-XR-ipv4-ma-oper', False),
            _MetaInfoClassMember('allow-self-ping', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Allow Self Ping
                ''',
                'allow_self_ping',
                'Cisco-IOS-XR-ipv4-ma-oper', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable RPF config
                ''',
                'enable',
                'Cisco-IOS-XR-ipv4-ma-oper', False),
            _MetaInfoClassMember('mode', REFERENCE_ENUM_CLASS, 'RpfModeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ma_oper', 'RpfModeEnum', 
                [], [], 
                '''                RPF Mode (loose/strict)
                ''',
                'mode',
                'Cisco-IOS-XR-ipv4-ma-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-ma-oper',
            'rpf',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ma-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper'
        ),
    },
    'Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.BgpPa.Input' : {
        'meta_info' : _MetaInfoClass('Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.BgpPa.Input',
            False, 
            [
            _MetaInfoClassMember('destination', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable destination accouting
                ''',
                'destination',
                'Cisco-IOS-XR-ipv4-ma-oper', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable BGP PA for ingress/egress
                ''',
                'enable',
                'Cisco-IOS-XR-ipv4-ma-oper', False),
            _MetaInfoClassMember('source', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable source accouting
                ''',
                'source',
                'Cisco-IOS-XR-ipv4-ma-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-ma-oper',
            'input',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ma-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper'
        ),
    },
    'Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.BgpPa.Output' : {
        'meta_info' : _MetaInfoClass('Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.BgpPa.Output',
            False, 
            [
            _MetaInfoClassMember('destination', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable destination accouting
                ''',
                'destination',
                'Cisco-IOS-XR-ipv4-ma-oper', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable BGP PA for ingress/egress
                ''',
                'enable',
                'Cisco-IOS-XR-ipv4-ma-oper', False),
            _MetaInfoClassMember('source', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable source accouting
                ''',
                'source',
                'Cisco-IOS-XR-ipv4-ma-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-ma-oper',
            'output',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ma-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper'
        ),
    },
    'Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.BgpPa' : {
        'meta_info' : _MetaInfoClass('Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.BgpPa',
            False, 
            [
            _MetaInfoClassMember('input', REFERENCE_CLASS, 'Input' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper', 'Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.BgpPa.Input', 
                [], [], 
                '''                BGP PA input config
                ''',
                'input',
                'Cisco-IOS-XR-ipv4-ma-oper', False),
            _MetaInfoClassMember('output', REFERENCE_CLASS, 'Output' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper', 'Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.BgpPa.Output', 
                [], [], 
                '''                BGP PA output config
                ''',
                'output',
                'Cisco-IOS-XR-ipv4-ma-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-ma-oper',
            'bgp-pa',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ma-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper'
        ),
    },
    'Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.PubUtime' : {
        'meta_info' : _MetaInfoClass('Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.PubUtime',
            False, 
            [
            ],
            'Cisco-IOS-XR-ipv4-ma-oper',
            'pub-utime',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ma-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper'
        ),
    },
    'Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.IdbUtime' : {
        'meta_info' : _MetaInfoClass('Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.IdbUtime',
            False, 
            [
            ],
            'Cisco-IOS-XR-ipv4-ma-oper',
            'idb-utime',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ma-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper'
        ),
    },
    'Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.CapsUtime' : {
        'meta_info' : _MetaInfoClass('Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.CapsUtime',
            False, 
            [
            ],
            'Cisco-IOS-XR-ipv4-ma-oper',
            'caps-utime',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ma-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper'
        ),
    },
    'Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.FwdEnUtime' : {
        'meta_info' : _MetaInfoClass('Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.FwdEnUtime',
            False, 
            [
            ],
            'Cisco-IOS-XR-ipv4-ma-oper',
            'fwd-en-utime',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ma-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper'
        ),
    },
    'Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.FwdDisUtime' : {
        'meta_info' : _MetaInfoClass('Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.FwdDisUtime',
            False, 
            [
            ],
            'Cisco-IOS-XR-ipv4-ma-oper',
            'fwd-dis-utime',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ma-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper'
        ),
    },
    'Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.MulticastGroup' : {
        'meta_info' : _MetaInfoClass('Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.MulticastGroup',
            False, 
            [
            _MetaInfoClassMember('group-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Address of multicast group
                ''',
                'group_address',
                'Cisco-IOS-XR-ipv4-ma-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-ma-oper',
            'multicast-group',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ma-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper'
        ),
    },
    'Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.SecondaryAddress' : {
        'meta_info' : _MetaInfoClass('Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.SecondaryAddress',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Address
                ''',
                'address',
                'Cisco-IOS-XR-ipv4-ma-oper', False),
            _MetaInfoClassMember('prefix-length', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Prefix length of address
                ''',
                'prefix_length',
                'Cisco-IOS-XR-ipv4-ma-oper', False),
            _MetaInfoClassMember('route-tag', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Route Tag associated with this address (0 = no
                tag)
                ''',
                'route_tag',
                'Cisco-IOS-XR-ipv4-ma-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-ma-oper',
            'secondary-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ma-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper'
        ),
    },
    'Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail' : {
        'meta_info' : _MetaInfoClass('Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail',
            False, 
            [
            _MetaInfoClassMember('acl', REFERENCE_CLASS, 'Acl' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper', 'Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.Acl', 
                [], [], 
                '''                ACLs configured on the interface
                ''',
                'acl',
                'Cisco-IOS-XR-ipv4-ma-oper', False),
            _MetaInfoClassMember('bgp-pa', REFERENCE_CLASS, 'BgpPa' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper', 'Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.BgpPa', 
                [], [], 
                '''                BGP PA config on the interface
                ''',
                'bgp_pa',
                'Cisco-IOS-XR-ipv4-ma-oper', False),
            _MetaInfoClassMember('caps-utime', REFERENCE_CLASS, 'CapsUtime' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper', 'Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.CapsUtime', 
                [], [], 
                '''                CAPS Add Time
                ''',
                'caps_utime',
                'Cisco-IOS-XR-ipv4-ma-oper', False),
            _MetaInfoClassMember('direct-broadcast', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Are direct broadcasts sent on the interface?
                ''',
                'direct_broadcast',
                'Cisco-IOS-XR-ipv4-ma-oper', False),
            _MetaInfoClassMember('flow-tag-dst', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is BGP Flow Tag Destination is enable
                ''',
                'flow_tag_dst',
                'Cisco-IOS-XR-ipv4-ma-oper', False),
            _MetaInfoClassMember('flow-tag-src', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is BGP Flow Tag Source is enable
                ''',
                'flow_tag_src',
                'Cisco-IOS-XR-ipv4-ma-oper', False),
            _MetaInfoClassMember('fwd-dis-utime', REFERENCE_CLASS, 'FwdDisUtime' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper', 'Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.FwdDisUtime', 
                [], [], 
                '''                FWD DISABLE Time
                ''',
                'fwd_dis_utime',
                'Cisco-IOS-XR-ipv4-ma-oper', False),
            _MetaInfoClassMember('fwd-en-utime', REFERENCE_CLASS, 'FwdEnUtime' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper', 'Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.FwdEnUtime', 
                [], [], 
                '''                FWD ENABLE Time
                ''',
                'fwd_en_utime',
                'Cisco-IOS-XR-ipv4-ma-oper', False),
            _MetaInfoClassMember('helper-address', REFERENCE_CLASS, 'HelperAddress' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper', 'Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.HelperAddress', 
                [], [], 
                '''                Helper Addresses configured on the interface
                ''',
                'helper_address',
                'Cisco-IOS-XR-ipv4-ma-oper', False),
            _MetaInfoClassMember('idb-utime', REFERENCE_CLASS, 'IdbUtime' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper', 'Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.IdbUtime', 
                [], [], 
                '''                IDB Create Time
                ''',
                'idb_utime',
                'Cisco-IOS-XR-ipv4-ma-oper', False),
            _MetaInfoClassMember('line-state', REFERENCE_ENUM_CLASS, 'Ipv4MaOperLineStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ma_oper', 'Ipv4MaOperLineStateEnum', 
                [], [], 
                '''                Line state of the interface
                ''',
                'line_state',
                'Cisco-IOS-XR-ipv4-ma-oper', False),
            _MetaInfoClassMember('mask-reply', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Are mask replies sent on the interface?
                ''',
                'mask_reply',
                'Cisco-IOS-XR-ipv4-ma-oper', False),
            _MetaInfoClassMember('mlacp-active', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is mLACP state Active (valid if RG ID exists)
                ''',
                'mlacp_active',
                'Cisco-IOS-XR-ipv4-ma-oper', False),
            _MetaInfoClassMember('mtu', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                IP MTU of the interface
                ''',
                'mtu',
                'Cisco-IOS-XR-ipv4-ma-oper', False),
            _MetaInfoClassMember('multi-acl', REFERENCE_CLASS, 'MultiAcl' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper', 'Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.MultiAcl', 
                [], [], 
                '''                Multi ACLs configured on the interface
                ''',
                'multi_acl',
                'Cisco-IOS-XR-ipv4-ma-oper', False),
            _MetaInfoClassMember('multicast-group', REFERENCE_LIST, 'MulticastGroup' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper', 'Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.MulticastGroup', 
                [], [], 
                '''                Multicast groups joined on the interface
                ''',
                'multicast_group',
                'Cisco-IOS-XR-ipv4-ma-oper', False),
            _MetaInfoClassMember('prefix-length', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Prefix length of primary address
                ''',
                'prefix_length',
                'Cisco-IOS-XR-ipv4-ma-oper', False),
            _MetaInfoClassMember('primary-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Primary address
                ''',
                'primary_address',
                'Cisco-IOS-XR-ipv4-ma-oper', False),
            _MetaInfoClassMember('proxy-arp-disabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is Proxy ARP disabled on the interface?
                ''',
                'proxy_arp_disabled',
                'Cisco-IOS-XR-ipv4-ma-oper', False),
            _MetaInfoClassMember('pub-utime', REFERENCE_CLASS, 'PubUtime' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper', 'Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.PubUtime', 
                [], [], 
                '''                Address Publish Time
                ''',
                'pub_utime',
                'Cisco-IOS-XR-ipv4-ma-oper', False),
            _MetaInfoClassMember('redirect', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Are ICMP redirects sent on the interface?
                ''',
                'redirect',
                'Cisco-IOS-XR-ipv4-ma-oper', False),
            _MetaInfoClassMember('rg-id-exists', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Does ICCP RG ID exist on the interface?
                ''',
                'rg_id_exists',
                'Cisco-IOS-XR-ipv4-ma-oper', False),
            _MetaInfoClassMember('route-tag', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Route tag associated with the primary address (0
                = no tag)
                ''',
                'route_tag',
                'Cisco-IOS-XR-ipv4-ma-oper', False),
            _MetaInfoClassMember('rpf', REFERENCE_CLASS, 'Rpf' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper', 'Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.Rpf', 
                [], [], 
                '''                RPF config on the interface
                ''',
                'rpf',
                'Cisco-IOS-XR-ipv4-ma-oper', False),
            _MetaInfoClassMember('secondary-address', REFERENCE_LIST, 'SecondaryAddress' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper', 'Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.SecondaryAddress', 
                [], [], 
                '''                Secondary addresses on the interface
                ''',
                'secondary_address',
                'Cisco-IOS-XR-ipv4-ma-oper', False),
            _MetaInfoClassMember('unnumbered-interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of referenced interface (valid if
                unnumbered)
                ''',
                'unnumbered_interface_name',
                'Cisco-IOS-XR-ipv4-ma-oper', False),
            _MetaInfoClassMember('unreachable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Are ICMP unreachables sent on the interface?
                ''',
                'unreachable',
                'Cisco-IOS-XR-ipv4-ma-oper', False),
            _MetaInfoClassMember('vrf-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                VRF ID of the interface
                ''',
                'vrf_id',
                'Cisco-IOS-XR-ipv4-ma-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-ma-oper',
            'detail',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ma-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper'
        ),
    },
    'Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Brief' : {
        'meta_info' : _MetaInfoClass('Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Brief',
            False, 
            [
            _MetaInfoClassMember('line-state', REFERENCE_ENUM_CLASS, 'Ipv4MaOperLineStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_ma_oper', 'Ipv4MaOperLineStateEnum', 
                [], [], 
                '''                Line state of the interface
                ''',
                'line_state',
                'Cisco-IOS-XR-ipv4-ma-oper', False),
            _MetaInfoClassMember('primary-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Primary address
                ''',
                'primary_address',
                'Cisco-IOS-XR-ipv4-ma-oper', False),
            _MetaInfoClassMember('vrf-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                VRF ID of the interface
                ''',
                'vrf_id',
                'Cisco-IOS-XR-ipv4-ma-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-ma-oper',
            'brief',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ma-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper'
        ),
    },
    'Ipv4Network.Interfaces.Interface.Vrfs.Vrf' : {
        'meta_info' : _MetaInfoClass('Ipv4Network.Interfaces.Interface.Vrfs.Vrf',
            False, 
            [
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The VRF name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-ipv4-ma-oper', True),
            _MetaInfoClassMember('brief', REFERENCE_CLASS, 'Brief' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper', 'Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Brief', 
                [], [], 
                '''                Brief IPv4 network operational data for an
                interface
                ''',
                'brief',
                'Cisco-IOS-XR-ipv4-ma-oper', False),
            _MetaInfoClassMember('detail', REFERENCE_CLASS, 'Detail' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper', 'Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail', 
                [], [], 
                '''                Detail IPv4 network operational data for an
                interface
                ''',
                'detail',
                'Cisco-IOS-XR-ipv4-ma-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-ma-oper',
            'vrf',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ma-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper'
        ),
    },
    'Ipv4Network.Interfaces.Interface.Vrfs' : {
        'meta_info' : _MetaInfoClass('Ipv4Network.Interfaces.Interface.Vrfs',
            False, 
            [
            _MetaInfoClassMember('vrf', REFERENCE_LIST, 'Vrf' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper', 'Ipv4Network.Interfaces.Interface.Vrfs.Vrf', 
                [], [], 
                '''                VRF information on the interface
                ''',
                'vrf',
                'Cisco-IOS-XR-ipv4-ma-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-ma-oper',
            'vrfs',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ma-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper'
        ),
    },
    'Ipv4Network.Interfaces.Interface' : {
        'meta_info' : _MetaInfoClass('Ipv4Network.Interfaces.Interface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                The name of the interface
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv4-ma-oper', True),
            _MetaInfoClassMember('vrfs', REFERENCE_CLASS, 'Vrfs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper', 'Ipv4Network.Interfaces.Interface.Vrfs', 
                [], [], 
                '''                List of VRF on the interface
                ''',
                'vrfs',
                'Cisco-IOS-XR-ipv4-ma-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-ma-oper',
            'interface',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ma-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper'
        ),
    },
    'Ipv4Network.Interfaces' : {
        'meta_info' : _MetaInfoClass('Ipv4Network.Interfaces',
            False, 
            [
            _MetaInfoClassMember('interface', REFERENCE_LIST, 'Interface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper', 'Ipv4Network.Interfaces.Interface', 
                [], [], 
                '''                Interface names with VRF
                ''',
                'interface',
                'Cisco-IOS-XR-ipv4-ma-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-ma-oper',
            'interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ma-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper'
        ),
    },
    'Ipv4Network' : {
        'meta_info' : _MetaInfoClass('Ipv4Network',
            False, 
            [
            _MetaInfoClassMember('interfaces', REFERENCE_CLASS, 'Interfaces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper', 'Ipv4Network.Interfaces', 
                [], [], 
                '''                IPv4 network operational interface data
                ''',
                'interfaces',
                'Cisco-IOS-XR-ipv4-ma-oper', False),
            _MetaInfoClassMember('nodes', REFERENCE_CLASS, 'Nodes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper', 'Ipv4Network.Nodes', 
                [], [], 
                '''                Node-specific IPv4 network operational data
                ''',
                'nodes',
                'Cisco-IOS-XR-ipv4-io-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-io-oper',
            'ipv4-network',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-io-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_io_oper'
        ),
    },
}
_meta_table['Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Briefs.Brief']['meta_info'].parent =_meta_table['Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Briefs']['meta_info']
_meta_table['Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.BgpPa.Input']['meta_info'].parent =_meta_table['Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.BgpPa']['meta_info']
_meta_table['Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.BgpPa.Output']['meta_info'].parent =_meta_table['Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.BgpPa']['meta_info']
_meta_table['Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.Acl']['meta_info'].parent =_meta_table['Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail']['meta_info']
_meta_table['Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.MultiAcl']['meta_info'].parent =_meta_table['Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail']['meta_info']
_meta_table['Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.HelperAddress']['meta_info'].parent =_meta_table['Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail']['meta_info']
_meta_table['Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.Rpf']['meta_info'].parent =_meta_table['Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail']['meta_info']
_meta_table['Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.BgpPa']['meta_info'].parent =_meta_table['Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail']['meta_info']
_meta_table['Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.PubUtime']['meta_info'].parent =_meta_table['Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail']['meta_info']
_meta_table['Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.IdbUtime']['meta_info'].parent =_meta_table['Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail']['meta_info']
_meta_table['Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.CapsUtime']['meta_info'].parent =_meta_table['Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail']['meta_info']
_meta_table['Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.FwdEnUtime']['meta_info'].parent =_meta_table['Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail']['meta_info']
_meta_table['Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.FwdDisUtime']['meta_info'].parent =_meta_table['Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail']['meta_info']
_meta_table['Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.MulticastGroup']['meta_info'].parent =_meta_table['Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail']['meta_info']
_meta_table['Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.SecondaryAddress']['meta_info'].parent =_meta_table['Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail']['meta_info']
_meta_table['Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail']['meta_info'].parent =_meta_table['Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details']['meta_info']
_meta_table['Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Briefs']['meta_info'].parent =_meta_table['Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf']['meta_info']
_meta_table['Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details']['meta_info'].parent =_meta_table['Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf']['meta_info']
_meta_table['Ipv4Network.Nodes.Node.InterfaceData.Vrfs.Vrf']['meta_info'].parent =_meta_table['Ipv4Network.Nodes.Node.InterfaceData.Vrfs']['meta_info']
_meta_table['Ipv4Network.Nodes.Node.InterfaceData.Summary.IfUpUp']['meta_info'].parent =_meta_table['Ipv4Network.Nodes.Node.InterfaceData.Summary']['meta_info']
_meta_table['Ipv4Network.Nodes.Node.InterfaceData.Summary.IfUpDown']['meta_info'].parent =_meta_table['Ipv4Network.Nodes.Node.InterfaceData.Summary']['meta_info']
_meta_table['Ipv4Network.Nodes.Node.InterfaceData.Summary.IfDownDown']['meta_info'].parent =_meta_table['Ipv4Network.Nodes.Node.InterfaceData.Summary']['meta_info']
_meta_table['Ipv4Network.Nodes.Node.InterfaceData.Summary.IfShutdownDown']['meta_info'].parent =_meta_table['Ipv4Network.Nodes.Node.InterfaceData.Summary']['meta_info']
_meta_table['Ipv4Network.Nodes.Node.InterfaceData.Vrfs']['meta_info'].parent =_meta_table['Ipv4Network.Nodes.Node.InterfaceData']['meta_info']
_meta_table['Ipv4Network.Nodes.Node.InterfaceData.Summary']['meta_info'].parent =_meta_table['Ipv4Network.Nodes.Node.InterfaceData']['meta_info']
_meta_table['Ipv4Network.Nodes.Node.Statistics.Traffic.Ipv4Stats']['meta_info'].parent =_meta_table['Ipv4Network.Nodes.Node.Statistics.Traffic']['meta_info']
_meta_table['Ipv4Network.Nodes.Node.Statistics.Traffic.IcmpStats']['meta_info'].parent =_meta_table['Ipv4Network.Nodes.Node.Statistics.Traffic']['meta_info']
_meta_table['Ipv4Network.Nodes.Node.Statistics.Traffic']['meta_info'].parent =_meta_table['Ipv4Network.Nodes.Node.Statistics']['meta_info']
_meta_table['Ipv4Network.Nodes.Node.InterfaceData']['meta_info'].parent =_meta_table['Ipv4Network.Nodes.Node']['meta_info']
_meta_table['Ipv4Network.Nodes.Node.Statistics']['meta_info'].parent =_meta_table['Ipv4Network.Nodes.Node']['meta_info']
_meta_table['Ipv4Network.Nodes.Node']['meta_info'].parent =_meta_table['Ipv4Network.Nodes']['meta_info']
_meta_table['Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.BgpPa.Input']['meta_info'].parent =_meta_table['Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.BgpPa']['meta_info']
_meta_table['Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.BgpPa.Output']['meta_info'].parent =_meta_table['Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.BgpPa']['meta_info']
_meta_table['Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.Acl']['meta_info'].parent =_meta_table['Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail']['meta_info']
_meta_table['Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.MultiAcl']['meta_info'].parent =_meta_table['Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail']['meta_info']
_meta_table['Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.HelperAddress']['meta_info'].parent =_meta_table['Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail']['meta_info']
_meta_table['Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.Rpf']['meta_info'].parent =_meta_table['Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail']['meta_info']
_meta_table['Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.BgpPa']['meta_info'].parent =_meta_table['Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail']['meta_info']
_meta_table['Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.PubUtime']['meta_info'].parent =_meta_table['Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail']['meta_info']
_meta_table['Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.IdbUtime']['meta_info'].parent =_meta_table['Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail']['meta_info']
_meta_table['Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.CapsUtime']['meta_info'].parent =_meta_table['Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail']['meta_info']
_meta_table['Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.FwdEnUtime']['meta_info'].parent =_meta_table['Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail']['meta_info']
_meta_table['Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.FwdDisUtime']['meta_info'].parent =_meta_table['Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail']['meta_info']
_meta_table['Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.MulticastGroup']['meta_info'].parent =_meta_table['Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail']['meta_info']
_meta_table['Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail.SecondaryAddress']['meta_info'].parent =_meta_table['Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail']['meta_info']
_meta_table['Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Detail']['meta_info'].parent =_meta_table['Ipv4Network.Interfaces.Interface.Vrfs.Vrf']['meta_info']
_meta_table['Ipv4Network.Interfaces.Interface.Vrfs.Vrf.Brief']['meta_info'].parent =_meta_table['Ipv4Network.Interfaces.Interface.Vrfs.Vrf']['meta_info']
_meta_table['Ipv4Network.Interfaces.Interface.Vrfs.Vrf']['meta_info'].parent =_meta_table['Ipv4Network.Interfaces.Interface.Vrfs']['meta_info']
_meta_table['Ipv4Network.Interfaces.Interface.Vrfs']['meta_info'].parent =_meta_table['Ipv4Network.Interfaces.Interface']['meta_info']
_meta_table['Ipv4Network.Interfaces.Interface']['meta_info'].parent =_meta_table['Ipv4Network.Interfaces']['meta_info']
_meta_table['Ipv4Network.Nodes']['meta_info'].parent =_meta_table['Ipv4Network']['meta_info']
_meta_table['Ipv4Network.Interfaces']['meta_info'].parent =_meta_table['Ipv4Network']['meta_info']
