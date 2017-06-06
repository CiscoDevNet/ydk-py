


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'Ipv6MaIfAddrStateEnum' : _MetaInfoEnum('Ipv6MaIfAddrStateEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper',
        {
            'active':'active',
            'deprecated':'deprecated',
            'duplicate':'duplicate',
            'inaccessible':'inaccessible',
            'tentative':'tentative',
        }, 'Cisco-IOS-XR-ipv6-ma-oper', _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ma-oper']),
    'Ipv6MaIfLineStateEnum' : _MetaInfoEnum('Ipv6MaIfLineStateEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper',
        {
            'down':'down',
            'up':'up',
            'unknown':'unknown',
            'error':'error',
        }, 'Cisco-IOS-XR-ipv6-ma-oper', _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ma-oper']),
    'Ipv6MaOperStateEnum' : _MetaInfoEnum('Ipv6MaOperStateEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper',
        {
            'oper-up':'oper_up',
            'oper-down':'oper_down',
        }, 'Cisco-IOS-XR-ipv6-ma-oper', _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ma-oper']),
    'Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Briefs.Brief.LinkLocalAddress' : {
        'meta_info' : _MetaInfoClass('Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Briefs.Brief.LinkLocalAddress',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 Address
                ''',
                'address',
                'Cisco-IOS-XR-ipv6-ma-oper', False),
            _MetaInfoClassMember('address-state', REFERENCE_ENUM_CLASS, 'Ipv6MaIfAddrStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper', 'Ipv6MaIfAddrStateEnum', 
                [], [], 
                '''                State of Address
                ''',
                'address_state',
                'Cisco-IOS-XR-ipv6-ma-oper', False),
            _MetaInfoClassMember('is-anycast', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Anycast address
                ''',
                'is_anycast',
                'Cisco-IOS-XR-ipv6-ma-oper', False),
            _MetaInfoClassMember('prefix-length', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Prefix Length of IPv6 Address
                ''',
                'prefix_length',
                'Cisco-IOS-XR-ipv6-ma-oper', False),
            _MetaInfoClassMember('route-tag', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Route-tag of the Address
                ''',
                'route_tag',
                'Cisco-IOS-XR-ipv6-ma-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-ma-oper',
            'link-local-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ma-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper'
        ),
    },
    'Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Briefs.Brief.Address' : {
        'meta_info' : _MetaInfoClass('Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Briefs.Brief.Address',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 Address
                ''',
                'address',
                'Cisco-IOS-XR-ipv6-ma-oper', False),
            _MetaInfoClassMember('address-state', REFERENCE_ENUM_CLASS, 'Ipv6MaIfAddrStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper', 'Ipv6MaIfAddrStateEnum', 
                [], [], 
                '''                State of Address
                ''',
                'address_state',
                'Cisco-IOS-XR-ipv6-ma-oper', False),
            _MetaInfoClassMember('is-anycast', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Anycast address
                ''',
                'is_anycast',
                'Cisco-IOS-XR-ipv6-ma-oper', False),
            _MetaInfoClassMember('prefix-length', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Prefix Length of IPv6 Address
                ''',
                'prefix_length',
                'Cisco-IOS-XR-ipv6-ma-oper', False),
            _MetaInfoClassMember('route-tag', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Route-tag of the Address
                ''',
                'route_tag',
                'Cisco-IOS-XR-ipv6-ma-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-ma-oper',
            'address',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ma-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper'
        ),
    },
    'Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Briefs.Brief' : {
        'meta_info' : _MetaInfoClass('Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Briefs.Brief',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                The name of the interface
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv6-ma-oper', True),
            _MetaInfoClassMember('address', REFERENCE_LIST, 'Address' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper', 'Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Briefs.Brief.Address', 
                [], [], 
                '''                Address List
                ''',
                'address',
                'Cisco-IOS-XR-ipv6-ma-oper', False),
            _MetaInfoClassMember('line-state', REFERENCE_ENUM_CLASS, 'Ipv6MaIfLineStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper', 'Ipv6MaIfLineStateEnum', 
                [], [], 
                '''                State of Interface Line
                ''',
                'line_state',
                'Cisco-IOS-XR-ipv6-ma-oper', False),
            _MetaInfoClassMember('link-local-address', REFERENCE_CLASS, 'LinkLocalAddress' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper', 'Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Briefs.Brief.LinkLocalAddress', 
                [], [], 
                '''                Link Local Address
                ''',
                'link_local_address',
                'Cisco-IOS-XR-ipv6-ma-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-ma-oper',
            'brief',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ma-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper'
        ),
    },
    'Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Briefs' : {
        'meta_info' : _MetaInfoClass('Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Briefs',
            False, 
            [
            _MetaInfoClassMember('brief', REFERENCE_LIST, 'Brief' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper', 'Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Briefs.Brief', 
                [], [], 
                '''                Brief interface IPv6 network operational
                data for an interface
                ''',
                'brief',
                'Cisco-IOS-XR-ipv6-ma-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-ma-oper',
            'briefs',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ma-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper'
        ),
    },
    'Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.LinkLocalAddress' : {
        'meta_info' : _MetaInfoClass('Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.LinkLocalAddress',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 Address
                ''',
                'address',
                'Cisco-IOS-XR-ipv6-ma-oper', False),
            _MetaInfoClassMember('address-state', REFERENCE_ENUM_CLASS, 'Ipv6MaIfAddrStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper', 'Ipv6MaIfAddrStateEnum', 
                [], [], 
                '''                State of Address
                ''',
                'address_state',
                'Cisco-IOS-XR-ipv6-ma-oper', False),
            _MetaInfoClassMember('is-anycast', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Anycast address
                ''',
                'is_anycast',
                'Cisco-IOS-XR-ipv6-ma-oper', False),
            _MetaInfoClassMember('prefix-length', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Prefix Length of IPv6 Address
                ''',
                'prefix_length',
                'Cisco-IOS-XR-ipv6-ma-oper', False),
            _MetaInfoClassMember('route-tag', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Route-tag of the Address
                ''',
                'route_tag',
                'Cisco-IOS-XR-ipv6-ma-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-ma-oper',
            'link-local-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ma-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper'
        ),
    },
    'Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.AccessControlList' : {
        'meta_info' : _MetaInfoClass('Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.AccessControlList',
            False, 
            [
            _MetaInfoClassMember('common-in-bound', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Common ACL applied to incoming packets
                ''',
                'common_in_bound',
                'Cisco-IOS-XR-ipv6-ma-oper', False),
            _MetaInfoClassMember('common-out-bound', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Common ACL applied to outgoing packets
                ''',
                'common_out_bound',
                'Cisco-IOS-XR-ipv6-ma-oper', False),
            _MetaInfoClassMember('in-bound', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                ACL applied to incoming packets
                ''',
                'in_bound',
                'Cisco-IOS-XR-ipv6-ma-oper', False),
            _MetaInfoClassMember('out-bound', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                ACL applied to outgoing packets
                ''',
                'out_bound',
                'Cisco-IOS-XR-ipv6-ma-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-ma-oper',
            'access-control-list',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ma-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper'
        ),
    },
    'Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.MultiAccessControlList' : {
        'meta_info' : _MetaInfoClass('Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.MultiAccessControlList',
            False, 
            [
            _MetaInfoClassMember('common', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [], 
                '''                Common ACLs
                ''',
                'common',
                'Cisco-IOS-XR-ipv6-ma-oper', False, max_elements=5),
            _MetaInfoClassMember('inbound', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [], 
                '''                Inbound ACLs
                ''',
                'inbound',
                'Cisco-IOS-XR-ipv6-ma-oper', False, max_elements=5),
            _MetaInfoClassMember('outbound', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [], 
                '''                Outbound ACLs
                ''',
                'outbound',
                'Cisco-IOS-XR-ipv6-ma-oper', False, max_elements=5),
            ],
            'Cisco-IOS-XR-ipv6-ma-oper',
            'multi-access-control-list',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ma-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper'
        ),
    },
    'Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.Rpf' : {
        'meta_info' : _MetaInfoClass('Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.Rpf',
            False, 
            [
            _MetaInfoClassMember('allow-default-route', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Allow Default Route
                ''',
                'allow_default_route',
                'Cisco-IOS-XR-ipv6-ma-oper', False),
            _MetaInfoClassMember('allow-self-ping', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Allow Self Ping
                ''',
                'allow_self_ping',
                'Cisco-IOS-XR-ipv6-ma-oper', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable RPF config
                ''',
                'enable',
                'Cisco-IOS-XR-ipv6-ma-oper', False),
            _MetaInfoClassMember('mode', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                RPF Mode (loose/strict)
                ''',
                'mode',
                'Cisco-IOS-XR-ipv6-ma-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-ma-oper',
            'rpf',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ma-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper'
        ),
    },
    'Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.BgpPa.Input' : {
        'meta_info' : _MetaInfoClass('Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.BgpPa.Input',
            False, 
            [
            _MetaInfoClassMember('destination', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable destination accouting
                ''',
                'destination',
                'Cisco-IOS-XR-ipv6-ma-oper', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Enable BGP PA for ingress/egress
                ''',
                'enable',
                'Cisco-IOS-XR-ipv6-ma-oper', False),
            _MetaInfoClassMember('source', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable source accouting
                ''',
                'source',
                'Cisco-IOS-XR-ipv6-ma-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-ma-oper',
            'input',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ma-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper'
        ),
    },
    'Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.BgpPa.Output' : {
        'meta_info' : _MetaInfoClass('Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.BgpPa.Output',
            False, 
            [
            _MetaInfoClassMember('destination', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable destination accouting
                ''',
                'destination',
                'Cisco-IOS-XR-ipv6-ma-oper', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Enable BGP PA for ingress/egress
                ''',
                'enable',
                'Cisco-IOS-XR-ipv6-ma-oper', False),
            _MetaInfoClassMember('source', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable source accouting
                ''',
                'source',
                'Cisco-IOS-XR-ipv6-ma-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-ma-oper',
            'output',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ma-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper'
        ),
    },
    'Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.BgpPa' : {
        'meta_info' : _MetaInfoClass('Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.BgpPa',
            False, 
            [
            _MetaInfoClassMember('input', REFERENCE_CLASS, 'Input' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper', 'Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.BgpPa.Input', 
                [], [], 
                '''                BGP PA input config
                ''',
                'input',
                'Cisco-IOS-XR-ipv6-ma-oper', False),
            _MetaInfoClassMember('output', REFERENCE_CLASS, 'Output' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper', 'Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.BgpPa.Output', 
                [], [], 
                '''                BGP PA output config
                ''',
                'output',
                'Cisco-IOS-XR-ipv6-ma-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-ma-oper',
            'bgp-pa',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ma-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper'
        ),
    },
    'Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.Utime' : {
        'meta_info' : _MetaInfoClass('Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.Utime',
            False, 
            [
            ],
            'Cisco-IOS-XR-ipv6-ma-oper',
            'utime',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ma-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper'
        ),
    },
    'Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.IdbUtime' : {
        'meta_info' : _MetaInfoClass('Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.IdbUtime',
            False, 
            [
            ],
            'Cisco-IOS-XR-ipv6-ma-oper',
            'idb-utime',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ma-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper'
        ),
    },
    'Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.CapsUtime' : {
        'meta_info' : _MetaInfoClass('Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.CapsUtime',
            False, 
            [
            ],
            'Cisco-IOS-XR-ipv6-ma-oper',
            'caps-utime',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ma-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper'
        ),
    },
    'Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.FwdEnUtime' : {
        'meta_info' : _MetaInfoClass('Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.FwdEnUtime',
            False, 
            [
            ],
            'Cisco-IOS-XR-ipv6-ma-oper',
            'fwd-en-utime',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ma-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper'
        ),
    },
    'Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.FwdDisUtime' : {
        'meta_info' : _MetaInfoClass('Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.FwdDisUtime',
            False, 
            [
            ],
            'Cisco-IOS-XR-ipv6-ma-oper',
            'fwd-dis-utime',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ma-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper'
        ),
    },
    'Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.MulticastGroup' : {
        'meta_info' : _MetaInfoClass('Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.MulticastGroup',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 Address of Multicast Group
                ''',
                'address',
                'Cisco-IOS-XR-ipv6-ma-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-ma-oper',
            'multicast-group',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ma-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper'
        ),
    },
    'Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.Address' : {
        'meta_info' : _MetaInfoClass('Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.Address',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 Address
                ''',
                'address',
                'Cisco-IOS-XR-ipv6-ma-oper', False),
            _MetaInfoClassMember('address-state', REFERENCE_ENUM_CLASS, 'Ipv6MaIfAddrStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper', 'Ipv6MaIfAddrStateEnum', 
                [], [], 
                '''                State of Address
                ''',
                'address_state',
                'Cisco-IOS-XR-ipv6-ma-oper', False),
            _MetaInfoClassMember('is-anycast', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Anycast address
                ''',
                'is_anycast',
                'Cisco-IOS-XR-ipv6-ma-oper', False),
            _MetaInfoClassMember('prefix-length', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Prefix Length of IPv6 Address
                ''',
                'prefix_length',
                'Cisco-IOS-XR-ipv6-ma-oper', False),
            _MetaInfoClassMember('route-tag', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Route-tag of the Address
                ''',
                'route_tag',
                'Cisco-IOS-XR-ipv6-ma-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-ma-oper',
            'address',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ma-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper'
        ),
    },
    'Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.ClientMulticastGroup' : {
        'meta_info' : _MetaInfoClass('Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.ClientMulticastGroup',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 Address of Multicast Group
                ''',
                'address',
                'Cisco-IOS-XR-ipv6-ma-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-ma-oper',
            'client-multicast-group',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ma-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper'
        ),
    },
    'Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail' : {
        'meta_info' : _MetaInfoClass('Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                The name of the interface
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv6-ma-oper', True),
            _MetaInfoClassMember('access-control-list', REFERENCE_CLASS, 'AccessControlList' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper', 'Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.AccessControlList', 
                [], [], 
                '''                IPv6 Access Control List
                ''',
                'access_control_list',
                'Cisco-IOS-XR-ipv6-ma-oper', False),
            _MetaInfoClassMember('address', REFERENCE_LIST, 'Address' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper', 'Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.Address', 
                [], [], 
                '''                Address List
                ''',
                'address',
                'Cisco-IOS-XR-ipv6-ma-oper', False),
            _MetaInfoClassMember('bgp-pa', REFERENCE_CLASS, 'BgpPa' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper', 'Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.BgpPa', 
                [], [], 
                '''                BGP PA config on the interface
                ''',
                'bgp_pa',
                'Cisco-IOS-XR-ipv6-ma-oper', False),
            _MetaInfoClassMember('caps-utime', REFERENCE_CLASS, 'CapsUtime' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper', 'Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.CapsUtime', 
                [], [], 
                '''                CAPS Add Time
                ''',
                'caps_utime',
                'Cisco-IOS-XR-ipv6-ma-oper', False),
            _MetaInfoClassMember('client-multicast-group', REFERENCE_LIST, 'ClientMulticastGroup' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper', 'Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.ClientMulticastGroup', 
                [], [], 
                '''                IPv6 Client Multicast Group
                ''',
                'client_multicast_group',
                'Cisco-IOS-XR-ipv6-ma-oper', False),
            _MetaInfoClassMember('flow-tag-dst', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is BGP Flow Tag Destination is enable
                ''',
                'flow_tag_dst',
                'Cisco-IOS-XR-ipv6-ma-oper', False),
            _MetaInfoClassMember('flow-tag-src', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is BGP Flow Tag Source is enable
                ''',
                'flow_tag_src',
                'Cisco-IOS-XR-ipv6-ma-oper', False),
            _MetaInfoClassMember('fwd-dis-utime', REFERENCE_CLASS, 'FwdDisUtime' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper', 'Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.FwdDisUtime', 
                [], [], 
                '''                FWD DISABLE Time
                ''',
                'fwd_dis_utime',
                'Cisco-IOS-XR-ipv6-ma-oper', False),
            _MetaInfoClassMember('fwd-en-utime', REFERENCE_CLASS, 'FwdEnUtime' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper', 'Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.FwdEnUtime', 
                [], [], 
                '''                FWD ENABLE Time
                ''',
                'fwd_en_utime',
                'Cisco-IOS-XR-ipv6-ma-oper', False),
            _MetaInfoClassMember('idb-utime', REFERENCE_CLASS, 'IdbUtime' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper', 'Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.IdbUtime', 
                [], [], 
                '''                IDB Create Time
                ''',
                'idb_utime',
                'Cisco-IOS-XR-ipv6-ma-oper', False),
            _MetaInfoClassMember('is-icmp-unreach-enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                ICMP unreach Enable
                ''',
                'is_icmp_unreach_enabled',
                'Cisco-IOS-XR-ipv6-ma-oper', False),
            _MetaInfoClassMember('line-state', REFERENCE_ENUM_CLASS, 'Ipv6MaIfLineStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper', 'Ipv6MaIfLineStateEnum', 
                [], [], 
                '''                State of Interface Line
                ''',
                'line_state',
                'Cisco-IOS-XR-ipv6-ma-oper', False),
            _MetaInfoClassMember('link-local-address', REFERENCE_CLASS, 'LinkLocalAddress' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper', 'Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.LinkLocalAddress', 
                [], [], 
                '''                Link Local Address
                ''',
                'link_local_address',
                'Cisco-IOS-XR-ipv6-ma-oper', False),
            _MetaInfoClassMember('mlacp-active', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is mLACP state Active (valid if RG ID exists)
                ''',
                'mlacp_active',
                'Cisco-IOS-XR-ipv6-ma-oper', False),
            _MetaInfoClassMember('mtu', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                IPv6 MTU
                ''',
                'mtu',
                'Cisco-IOS-XR-ipv6-ma-oper', False),
            _MetaInfoClassMember('multi-access-control-list', REFERENCE_CLASS, 'MultiAccessControlList' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper', 'Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.MultiAccessControlList', 
                [], [], 
                '''                Multi IPv6 Access Control List
                ''',
                'multi_access_control_list',
                'Cisco-IOS-XR-ipv6-ma-oper', False),
            _MetaInfoClassMember('multicast-group', REFERENCE_LIST, 'MulticastGroup' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper', 'Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.MulticastGroup', 
                [], [], 
                '''                IPv6 Multicast Group
                ''',
                'multicast_group',
                'Cisco-IOS-XR-ipv6-ma-oper', False),
            _MetaInfoClassMember('operation-state', REFERENCE_ENUM_CLASS, 'Ipv6MaOperStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper', 'Ipv6MaOperStateEnum', 
                [], [], 
                '''                IPv6 Operation State
                ''',
                'operation_state',
                'Cisco-IOS-XR-ipv6-ma-oper', False),
            _MetaInfoClassMember('rg-id-exists', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Does ICCP RG ID exist on the interface?
                ''',
                'rg_id_exists',
                'Cisco-IOS-XR-ipv6-ma-oper', False),
            _MetaInfoClassMember('rpf', REFERENCE_CLASS, 'Rpf' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper', 'Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.Rpf', 
                [], [], 
                '''                RPF config on the interface
                ''',
                'rpf',
                'Cisco-IOS-XR-ipv6-ma-oper', False),
            _MetaInfoClassMember('utime', REFERENCE_CLASS, 'Utime' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper', 'Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.Utime', 
                [], [], 
                '''                Address Publish Time
                ''',
                'utime',
                'Cisco-IOS-XR-ipv6-ma-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-ma-oper',
            'global-detail',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ma-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper'
        ),
    },
    'Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails' : {
        'meta_info' : _MetaInfoClass('Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails',
            False, 
            [
            _MetaInfoClassMember('global-detail', REFERENCE_LIST, 'GlobalDetail' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper', 'Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail', 
                [], [], 
                '''                Detail interface IPv6 network operational
                data for an interface
                ''',
                'global_detail',
                'Cisco-IOS-XR-ipv6-ma-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-ma-oper',
            'global-details',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ma-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper'
        ),
    },
    'Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalBriefs.GlobalBrief.LinkLocalAddress' : {
        'meta_info' : _MetaInfoClass('Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalBriefs.GlobalBrief.LinkLocalAddress',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 Address
                ''',
                'address',
                'Cisco-IOS-XR-ipv6-ma-oper', False),
            _MetaInfoClassMember('address-state', REFERENCE_ENUM_CLASS, 'Ipv6MaIfAddrStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper', 'Ipv6MaIfAddrStateEnum', 
                [], [], 
                '''                State of Address
                ''',
                'address_state',
                'Cisco-IOS-XR-ipv6-ma-oper', False),
            _MetaInfoClassMember('is-anycast', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Anycast address
                ''',
                'is_anycast',
                'Cisco-IOS-XR-ipv6-ma-oper', False),
            _MetaInfoClassMember('prefix-length', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Prefix Length of IPv6 Address
                ''',
                'prefix_length',
                'Cisco-IOS-XR-ipv6-ma-oper', False),
            _MetaInfoClassMember('route-tag', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Route-tag of the Address
                ''',
                'route_tag',
                'Cisco-IOS-XR-ipv6-ma-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-ma-oper',
            'link-local-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ma-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper'
        ),
    },
    'Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalBriefs.GlobalBrief.Address' : {
        'meta_info' : _MetaInfoClass('Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalBriefs.GlobalBrief.Address',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 Address
                ''',
                'address',
                'Cisco-IOS-XR-ipv6-ma-oper', False),
            _MetaInfoClassMember('address-state', REFERENCE_ENUM_CLASS, 'Ipv6MaIfAddrStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper', 'Ipv6MaIfAddrStateEnum', 
                [], [], 
                '''                State of Address
                ''',
                'address_state',
                'Cisco-IOS-XR-ipv6-ma-oper', False),
            _MetaInfoClassMember('is-anycast', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Anycast address
                ''',
                'is_anycast',
                'Cisco-IOS-XR-ipv6-ma-oper', False),
            _MetaInfoClassMember('prefix-length', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Prefix Length of IPv6 Address
                ''',
                'prefix_length',
                'Cisco-IOS-XR-ipv6-ma-oper', False),
            _MetaInfoClassMember('route-tag', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Route-tag of the Address
                ''',
                'route_tag',
                'Cisco-IOS-XR-ipv6-ma-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-ma-oper',
            'address',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ma-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper'
        ),
    },
    'Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalBriefs.GlobalBrief' : {
        'meta_info' : _MetaInfoClass('Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalBriefs.GlobalBrief',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                The name of the interface
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv6-ma-oper', True),
            _MetaInfoClassMember('address', REFERENCE_LIST, 'Address' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper', 'Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalBriefs.GlobalBrief.Address', 
                [], [], 
                '''                Address List
                ''',
                'address',
                'Cisco-IOS-XR-ipv6-ma-oper', False),
            _MetaInfoClassMember('line-state', REFERENCE_ENUM_CLASS, 'Ipv6MaIfLineStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper', 'Ipv6MaIfLineStateEnum', 
                [], [], 
                '''                State of Interface Line
                ''',
                'line_state',
                'Cisco-IOS-XR-ipv6-ma-oper', False),
            _MetaInfoClassMember('link-local-address', REFERENCE_CLASS, 'LinkLocalAddress' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper', 'Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalBriefs.GlobalBrief.LinkLocalAddress', 
                [], [], 
                '''                Link Local Address
                ''',
                'link_local_address',
                'Cisco-IOS-XR-ipv6-ma-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-ma-oper',
            'global-brief',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ma-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper'
        ),
    },
    'Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalBriefs' : {
        'meta_info' : _MetaInfoClass('Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalBriefs',
            False, 
            [
            _MetaInfoClassMember('global-brief', REFERENCE_LIST, 'GlobalBrief' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper', 'Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalBriefs.GlobalBrief', 
                [], [], 
                '''                Brief interface IPv6 network operational
                data for an interface
                ''',
                'global_brief',
                'Cisco-IOS-XR-ipv6-ma-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-ma-oper',
            'global-briefs',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ma-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper'
        ),
    },
    'Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.LinkLocalAddress' : {
        'meta_info' : _MetaInfoClass('Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.LinkLocalAddress',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 Address
                ''',
                'address',
                'Cisco-IOS-XR-ipv6-ma-oper', False),
            _MetaInfoClassMember('address-state', REFERENCE_ENUM_CLASS, 'Ipv6MaIfAddrStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper', 'Ipv6MaIfAddrStateEnum', 
                [], [], 
                '''                State of Address
                ''',
                'address_state',
                'Cisco-IOS-XR-ipv6-ma-oper', False),
            _MetaInfoClassMember('is-anycast', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Anycast address
                ''',
                'is_anycast',
                'Cisco-IOS-XR-ipv6-ma-oper', False),
            _MetaInfoClassMember('prefix-length', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Prefix Length of IPv6 Address
                ''',
                'prefix_length',
                'Cisco-IOS-XR-ipv6-ma-oper', False),
            _MetaInfoClassMember('route-tag', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Route-tag of the Address
                ''',
                'route_tag',
                'Cisco-IOS-XR-ipv6-ma-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-ma-oper',
            'link-local-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ma-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper'
        ),
    },
    'Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.AccessControlList' : {
        'meta_info' : _MetaInfoClass('Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.AccessControlList',
            False, 
            [
            _MetaInfoClassMember('common-in-bound', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Common ACL applied to incoming packets
                ''',
                'common_in_bound',
                'Cisco-IOS-XR-ipv6-ma-oper', False),
            _MetaInfoClassMember('common-out-bound', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Common ACL applied to outgoing packets
                ''',
                'common_out_bound',
                'Cisco-IOS-XR-ipv6-ma-oper', False),
            _MetaInfoClassMember('in-bound', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                ACL applied to incoming packets
                ''',
                'in_bound',
                'Cisco-IOS-XR-ipv6-ma-oper', False),
            _MetaInfoClassMember('out-bound', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                ACL applied to outgoing packets
                ''',
                'out_bound',
                'Cisco-IOS-XR-ipv6-ma-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-ma-oper',
            'access-control-list',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ma-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper'
        ),
    },
    'Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.MultiAccessControlList' : {
        'meta_info' : _MetaInfoClass('Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.MultiAccessControlList',
            False, 
            [
            _MetaInfoClassMember('common', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [], 
                '''                Common ACLs
                ''',
                'common',
                'Cisco-IOS-XR-ipv6-ma-oper', False, max_elements=5),
            _MetaInfoClassMember('inbound', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [], 
                '''                Inbound ACLs
                ''',
                'inbound',
                'Cisco-IOS-XR-ipv6-ma-oper', False, max_elements=5),
            _MetaInfoClassMember('outbound', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [], 
                '''                Outbound ACLs
                ''',
                'outbound',
                'Cisco-IOS-XR-ipv6-ma-oper', False, max_elements=5),
            ],
            'Cisco-IOS-XR-ipv6-ma-oper',
            'multi-access-control-list',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ma-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper'
        ),
    },
    'Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.Rpf' : {
        'meta_info' : _MetaInfoClass('Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.Rpf',
            False, 
            [
            _MetaInfoClassMember('allow-default-route', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Allow Default Route
                ''',
                'allow_default_route',
                'Cisco-IOS-XR-ipv6-ma-oper', False),
            _MetaInfoClassMember('allow-self-ping', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Allow Self Ping
                ''',
                'allow_self_ping',
                'Cisco-IOS-XR-ipv6-ma-oper', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable RPF config
                ''',
                'enable',
                'Cisco-IOS-XR-ipv6-ma-oper', False),
            _MetaInfoClassMember('mode', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                RPF Mode (loose/strict)
                ''',
                'mode',
                'Cisco-IOS-XR-ipv6-ma-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-ma-oper',
            'rpf',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ma-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper'
        ),
    },
    'Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.BgpPa.Input' : {
        'meta_info' : _MetaInfoClass('Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.BgpPa.Input',
            False, 
            [
            _MetaInfoClassMember('destination', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable destination accouting
                ''',
                'destination',
                'Cisco-IOS-XR-ipv6-ma-oper', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Enable BGP PA for ingress/egress
                ''',
                'enable',
                'Cisco-IOS-XR-ipv6-ma-oper', False),
            _MetaInfoClassMember('source', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable source accouting
                ''',
                'source',
                'Cisco-IOS-XR-ipv6-ma-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-ma-oper',
            'input',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ma-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper'
        ),
    },
    'Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.BgpPa.Output' : {
        'meta_info' : _MetaInfoClass('Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.BgpPa.Output',
            False, 
            [
            _MetaInfoClassMember('destination', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable destination accouting
                ''',
                'destination',
                'Cisco-IOS-XR-ipv6-ma-oper', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Enable BGP PA for ingress/egress
                ''',
                'enable',
                'Cisco-IOS-XR-ipv6-ma-oper', False),
            _MetaInfoClassMember('source', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable source accouting
                ''',
                'source',
                'Cisco-IOS-XR-ipv6-ma-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-ma-oper',
            'output',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ma-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper'
        ),
    },
    'Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.BgpPa' : {
        'meta_info' : _MetaInfoClass('Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.BgpPa',
            False, 
            [
            _MetaInfoClassMember('input', REFERENCE_CLASS, 'Input' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper', 'Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.BgpPa.Input', 
                [], [], 
                '''                BGP PA input config
                ''',
                'input',
                'Cisco-IOS-XR-ipv6-ma-oper', False),
            _MetaInfoClassMember('output', REFERENCE_CLASS, 'Output' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper', 'Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.BgpPa.Output', 
                [], [], 
                '''                BGP PA output config
                ''',
                'output',
                'Cisco-IOS-XR-ipv6-ma-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-ma-oper',
            'bgp-pa',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ma-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper'
        ),
    },
    'Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.Utime' : {
        'meta_info' : _MetaInfoClass('Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.Utime',
            False, 
            [
            ],
            'Cisco-IOS-XR-ipv6-ma-oper',
            'utime',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ma-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper'
        ),
    },
    'Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.IdbUtime' : {
        'meta_info' : _MetaInfoClass('Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.IdbUtime',
            False, 
            [
            ],
            'Cisco-IOS-XR-ipv6-ma-oper',
            'idb-utime',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ma-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper'
        ),
    },
    'Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.CapsUtime' : {
        'meta_info' : _MetaInfoClass('Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.CapsUtime',
            False, 
            [
            ],
            'Cisco-IOS-XR-ipv6-ma-oper',
            'caps-utime',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ma-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper'
        ),
    },
    'Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.FwdEnUtime' : {
        'meta_info' : _MetaInfoClass('Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.FwdEnUtime',
            False, 
            [
            ],
            'Cisco-IOS-XR-ipv6-ma-oper',
            'fwd-en-utime',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ma-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper'
        ),
    },
    'Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.FwdDisUtime' : {
        'meta_info' : _MetaInfoClass('Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.FwdDisUtime',
            False, 
            [
            ],
            'Cisco-IOS-XR-ipv6-ma-oper',
            'fwd-dis-utime',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ma-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper'
        ),
    },
    'Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.MulticastGroup' : {
        'meta_info' : _MetaInfoClass('Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.MulticastGroup',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 Address of Multicast Group
                ''',
                'address',
                'Cisco-IOS-XR-ipv6-ma-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-ma-oper',
            'multicast-group',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ma-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper'
        ),
    },
    'Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.Address' : {
        'meta_info' : _MetaInfoClass('Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.Address',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 Address
                ''',
                'address',
                'Cisco-IOS-XR-ipv6-ma-oper', False),
            _MetaInfoClassMember('address-state', REFERENCE_ENUM_CLASS, 'Ipv6MaIfAddrStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper', 'Ipv6MaIfAddrStateEnum', 
                [], [], 
                '''                State of Address
                ''',
                'address_state',
                'Cisco-IOS-XR-ipv6-ma-oper', False),
            _MetaInfoClassMember('is-anycast', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Anycast address
                ''',
                'is_anycast',
                'Cisco-IOS-XR-ipv6-ma-oper', False),
            _MetaInfoClassMember('prefix-length', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Prefix Length of IPv6 Address
                ''',
                'prefix_length',
                'Cisco-IOS-XR-ipv6-ma-oper', False),
            _MetaInfoClassMember('route-tag', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Route-tag of the Address
                ''',
                'route_tag',
                'Cisco-IOS-XR-ipv6-ma-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-ma-oper',
            'address',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ma-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper'
        ),
    },
    'Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.ClientMulticastGroup' : {
        'meta_info' : _MetaInfoClass('Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.ClientMulticastGroup',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 Address of Multicast Group
                ''',
                'address',
                'Cisco-IOS-XR-ipv6-ma-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-ma-oper',
            'client-multicast-group',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ma-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper'
        ),
    },
    'Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail' : {
        'meta_info' : _MetaInfoClass('Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                The name of the interface
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv6-ma-oper', True),
            _MetaInfoClassMember('access-control-list', REFERENCE_CLASS, 'AccessControlList' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper', 'Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.AccessControlList', 
                [], [], 
                '''                IPv6 Access Control List
                ''',
                'access_control_list',
                'Cisco-IOS-XR-ipv6-ma-oper', False),
            _MetaInfoClassMember('address', REFERENCE_LIST, 'Address' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper', 'Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.Address', 
                [], [], 
                '''                Address List
                ''',
                'address',
                'Cisco-IOS-XR-ipv6-ma-oper', False),
            _MetaInfoClassMember('bgp-pa', REFERENCE_CLASS, 'BgpPa' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper', 'Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.BgpPa', 
                [], [], 
                '''                BGP PA config on the interface
                ''',
                'bgp_pa',
                'Cisco-IOS-XR-ipv6-ma-oper', False),
            _MetaInfoClassMember('caps-utime', REFERENCE_CLASS, 'CapsUtime' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper', 'Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.CapsUtime', 
                [], [], 
                '''                CAPS Add Time
                ''',
                'caps_utime',
                'Cisco-IOS-XR-ipv6-ma-oper', False),
            _MetaInfoClassMember('client-multicast-group', REFERENCE_LIST, 'ClientMulticastGroup' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper', 'Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.ClientMulticastGroup', 
                [], [], 
                '''                IPv6 Client Multicast Group
                ''',
                'client_multicast_group',
                'Cisco-IOS-XR-ipv6-ma-oper', False),
            _MetaInfoClassMember('flow-tag-dst', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is BGP Flow Tag Destination is enable
                ''',
                'flow_tag_dst',
                'Cisco-IOS-XR-ipv6-ma-oper', False),
            _MetaInfoClassMember('flow-tag-src', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is BGP Flow Tag Source is enable
                ''',
                'flow_tag_src',
                'Cisco-IOS-XR-ipv6-ma-oper', False),
            _MetaInfoClassMember('fwd-dis-utime', REFERENCE_CLASS, 'FwdDisUtime' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper', 'Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.FwdDisUtime', 
                [], [], 
                '''                FWD DISABLE Time
                ''',
                'fwd_dis_utime',
                'Cisco-IOS-XR-ipv6-ma-oper', False),
            _MetaInfoClassMember('fwd-en-utime', REFERENCE_CLASS, 'FwdEnUtime' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper', 'Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.FwdEnUtime', 
                [], [], 
                '''                FWD ENABLE Time
                ''',
                'fwd_en_utime',
                'Cisco-IOS-XR-ipv6-ma-oper', False),
            _MetaInfoClassMember('idb-utime', REFERENCE_CLASS, 'IdbUtime' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper', 'Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.IdbUtime', 
                [], [], 
                '''                IDB Create Time
                ''',
                'idb_utime',
                'Cisco-IOS-XR-ipv6-ma-oper', False),
            _MetaInfoClassMember('is-icmp-unreach-enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                ICMP unreach Enable
                ''',
                'is_icmp_unreach_enabled',
                'Cisco-IOS-XR-ipv6-ma-oper', False),
            _MetaInfoClassMember('line-state', REFERENCE_ENUM_CLASS, 'Ipv6MaIfLineStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper', 'Ipv6MaIfLineStateEnum', 
                [], [], 
                '''                State of Interface Line
                ''',
                'line_state',
                'Cisco-IOS-XR-ipv6-ma-oper', False),
            _MetaInfoClassMember('link-local-address', REFERENCE_CLASS, 'LinkLocalAddress' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper', 'Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.LinkLocalAddress', 
                [], [], 
                '''                Link Local Address
                ''',
                'link_local_address',
                'Cisco-IOS-XR-ipv6-ma-oper', False),
            _MetaInfoClassMember('mlacp-active', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is mLACP state Active (valid if RG ID exists)
                ''',
                'mlacp_active',
                'Cisco-IOS-XR-ipv6-ma-oper', False),
            _MetaInfoClassMember('mtu', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                IPv6 MTU
                ''',
                'mtu',
                'Cisco-IOS-XR-ipv6-ma-oper', False),
            _MetaInfoClassMember('multi-access-control-list', REFERENCE_CLASS, 'MultiAccessControlList' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper', 'Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.MultiAccessControlList', 
                [], [], 
                '''                Multi IPv6 Access Control List
                ''',
                'multi_access_control_list',
                'Cisco-IOS-XR-ipv6-ma-oper', False),
            _MetaInfoClassMember('multicast-group', REFERENCE_LIST, 'MulticastGroup' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper', 'Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.MulticastGroup', 
                [], [], 
                '''                IPv6 Multicast Group
                ''',
                'multicast_group',
                'Cisco-IOS-XR-ipv6-ma-oper', False),
            _MetaInfoClassMember('operation-state', REFERENCE_ENUM_CLASS, 'Ipv6MaOperStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper', 'Ipv6MaOperStateEnum', 
                [], [], 
                '''                IPv6 Operation State
                ''',
                'operation_state',
                'Cisco-IOS-XR-ipv6-ma-oper', False),
            _MetaInfoClassMember('rg-id-exists', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Does ICCP RG ID exist on the interface?
                ''',
                'rg_id_exists',
                'Cisco-IOS-XR-ipv6-ma-oper', False),
            _MetaInfoClassMember('rpf', REFERENCE_CLASS, 'Rpf' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper', 'Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.Rpf', 
                [], [], 
                '''                RPF config on the interface
                ''',
                'rpf',
                'Cisco-IOS-XR-ipv6-ma-oper', False),
            _MetaInfoClassMember('utime', REFERENCE_CLASS, 'Utime' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper', 'Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.Utime', 
                [], [], 
                '''                Address Publish Time
                ''',
                'utime',
                'Cisco-IOS-XR-ipv6-ma-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-ma-oper',
            'detail',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ma-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper'
        ),
    },
    'Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details' : {
        'meta_info' : _MetaInfoClass('Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details',
            False, 
            [
            _MetaInfoClassMember('detail', REFERENCE_LIST, 'Detail' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper', 'Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail', 
                [], [], 
                '''                Detail interface IPv6 network operational
                data for an interface
                ''',
                'detail',
                'Cisco-IOS-XR-ipv6-ma-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-ma-oper',
            'details',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ma-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper'
        ),
    },
    'Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf' : {
        'meta_info' : _MetaInfoClass('Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf',
            False, 
            [
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The VRF name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-ipv6-ma-oper', True),
            _MetaInfoClassMember('briefs', REFERENCE_CLASS, 'Briefs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper', 'Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Briefs', 
                [], [], 
                '''                Brief interface IPv6 network operational
                data for a node
                ''',
                'briefs',
                'Cisco-IOS-XR-ipv6-ma-oper', False),
            _MetaInfoClassMember('details', REFERENCE_CLASS, 'Details' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper', 'Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details', 
                [], [], 
                '''                Detail interface IPv4 network operational
                data for a node
                ''',
                'details',
                'Cisco-IOS-XR-ipv6-ma-oper', False),
            _MetaInfoClassMember('global-briefs', REFERENCE_CLASS, 'GlobalBriefs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper', 'Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalBriefs', 
                [], [], 
                '''                Brief interface IPv6 network operational
                data from global data
                ''',
                'global_briefs',
                'Cisco-IOS-XR-ipv6-ma-oper', False),
            _MetaInfoClassMember('global-details', REFERENCE_CLASS, 'GlobalDetails' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper', 'Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails', 
                [], [], 
                '''                Detail interface IPv4 network operational
                data for global data
                ''',
                'global_details',
                'Cisco-IOS-XR-ipv6-ma-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-ma-oper',
            'vrf',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ma-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper'
        ),
    },
    'Ipv6Network.Nodes.Node.InterfaceData.Vrfs' : {
        'meta_info' : _MetaInfoClass('Ipv6Network.Nodes.Node.InterfaceData.Vrfs',
            False, 
            [
            _MetaInfoClassMember('vrf', REFERENCE_LIST, 'Vrf' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper', 'Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf', 
                [], [], 
                '''                VRF ID of an interface belong to
                ''',
                'vrf',
                'Cisco-IOS-XR-ipv6-ma-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-ma-oper',
            'vrfs',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ma-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper'
        ),
    },
    'Ipv6Network.Nodes.Node.InterfaceData.Summary.IfUpUp' : {
        'meta_info' : _MetaInfoClass('Ipv6Network.Nodes.Node.InterfaceData.Summary.IfUpUp',
            False, 
            [
            _MetaInfoClassMember('ip-assigned', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of interfaces with explicit addresses
                ''',
                'ip_assigned',
                'Cisco-IOS-XR-ipv6-ma-oper', False),
            _MetaInfoClassMember('ip-unassigned', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of unassigned interfaces without explicit
                address
                ''',
                'ip_unassigned',
                'Cisco-IOS-XR-ipv6-ma-oper', False),
            _MetaInfoClassMember('ip-unnumbered', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of unnumbered interfaces with explicit
                addresses
                ''',
                'ip_unnumbered',
                'Cisco-IOS-XR-ipv6-ma-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-ma-oper',
            'if-up-up',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ma-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper'
        ),
    },
    'Ipv6Network.Nodes.Node.InterfaceData.Summary.IfUpDown' : {
        'meta_info' : _MetaInfoClass('Ipv6Network.Nodes.Node.InterfaceData.Summary.IfUpDown',
            False, 
            [
            _MetaInfoClassMember('ip-assigned', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of interfaces with explicit addresses
                ''',
                'ip_assigned',
                'Cisco-IOS-XR-ipv6-ma-oper', False),
            _MetaInfoClassMember('ip-unassigned', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of unassigned interfaces without explicit
                address
                ''',
                'ip_unassigned',
                'Cisco-IOS-XR-ipv6-ma-oper', False),
            _MetaInfoClassMember('ip-unnumbered', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of unnumbered interfaces with explicit
                addresses
                ''',
                'ip_unnumbered',
                'Cisco-IOS-XR-ipv6-ma-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-ma-oper',
            'if-up-down',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ma-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper'
        ),
    },
    'Ipv6Network.Nodes.Node.InterfaceData.Summary.IfDownDown' : {
        'meta_info' : _MetaInfoClass('Ipv6Network.Nodes.Node.InterfaceData.Summary.IfDownDown',
            False, 
            [
            _MetaInfoClassMember('ip-assigned', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of interfaces with explicit addresses
                ''',
                'ip_assigned',
                'Cisco-IOS-XR-ipv6-ma-oper', False),
            _MetaInfoClassMember('ip-unassigned', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of unassigned interfaces without explicit
                address
                ''',
                'ip_unassigned',
                'Cisco-IOS-XR-ipv6-ma-oper', False),
            _MetaInfoClassMember('ip-unnumbered', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of unnumbered interfaces with explicit
                addresses
                ''',
                'ip_unnumbered',
                'Cisco-IOS-XR-ipv6-ma-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-ma-oper',
            'if-down-down',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ma-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper'
        ),
    },
    'Ipv6Network.Nodes.Node.InterfaceData.Summary.IfShutdownDown' : {
        'meta_info' : _MetaInfoClass('Ipv6Network.Nodes.Node.InterfaceData.Summary.IfShutdownDown',
            False, 
            [
            _MetaInfoClassMember('ip-assigned', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of interfaces with explicit addresses
                ''',
                'ip_assigned',
                'Cisco-IOS-XR-ipv6-ma-oper', False),
            _MetaInfoClassMember('ip-unassigned', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of unassigned interfaces without explicit
                address
                ''',
                'ip_unassigned',
                'Cisco-IOS-XR-ipv6-ma-oper', False),
            _MetaInfoClassMember('ip-unnumbered', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of unnumbered interfaces with explicit
                addresses
                ''',
                'ip_unnumbered',
                'Cisco-IOS-XR-ipv6-ma-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-ma-oper',
            'if-shutdown-down',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ma-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper'
        ),
    },
    'Ipv6Network.Nodes.Node.InterfaceData.Summary' : {
        'meta_info' : _MetaInfoClass('Ipv6Network.Nodes.Node.InterfaceData.Summary',
            False, 
            [
            _MetaInfoClassMember('if-down-down', REFERENCE_CLASS, 'IfDownDown' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper', 'Ipv6Network.Nodes.Node.InterfaceData.Summary.IfDownDown', 
                [], [], 
                '''                Number of interfaces (down,down)
                ''',
                'if_down_down',
                'Cisco-IOS-XR-ipv6-ma-oper', False),
            _MetaInfoClassMember('if-shutdown-down', REFERENCE_CLASS, 'IfShutdownDown' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper', 'Ipv6Network.Nodes.Node.InterfaceData.Summary.IfShutdownDown', 
                [], [], 
                '''                Number of interfaces (shutdown,down)
                ''',
                'if_shutdown_down',
                'Cisco-IOS-XR-ipv6-ma-oper', False),
            _MetaInfoClassMember('if-up-down', REFERENCE_CLASS, 'IfUpDown' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper', 'Ipv6Network.Nodes.Node.InterfaceData.Summary.IfUpDown', 
                [], [], 
                '''                Number of interfaces (up,down)
                ''',
                'if_up_down',
                'Cisco-IOS-XR-ipv6-ma-oper', False),
            _MetaInfoClassMember('if-up-down-basecaps-up', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of interfaces (up,down) with basecaps up
                ''',
                'if_up_down_basecaps_up',
                'Cisco-IOS-XR-ipv6-ma-oper', False),
            _MetaInfoClassMember('if-up-up', REFERENCE_CLASS, 'IfUpUp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper', 'Ipv6Network.Nodes.Node.InterfaceData.Summary.IfUpUp', 
                [], [], 
                '''                Number of interfaces (up,up)
                ''',
                'if_up_up',
                'Cisco-IOS-XR-ipv6-ma-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-ma-oper',
            'summary',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ma-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper'
        ),
    },
    'Ipv6Network.Nodes.Node.InterfaceData' : {
        'meta_info' : _MetaInfoClass('Ipv6Network.Nodes.Node.InterfaceData',
            False, 
            [
            _MetaInfoClassMember('summary', REFERENCE_CLASS, 'Summary' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper', 'Ipv6Network.Nodes.Node.InterfaceData.Summary', 
                [], [], 
                '''                Summary of IPv6 network operational interface
                data on a node
                ''',
                'summary',
                'Cisco-IOS-XR-ipv6-ma-oper', False),
            _MetaInfoClassMember('vrfs', REFERENCE_CLASS, 'Vrfs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper', 'Ipv6Network.Nodes.Node.InterfaceData.Vrfs', 
                [], [], 
                '''                VRF specific IPv6 network operational
                interface data
                ''',
                'vrfs',
                'Cisco-IOS-XR-ipv6-ma-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-ma-oper',
            'interface-data',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ma-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper'
        ),
    },
    'Ipv6Network.Nodes.Node' : {
        'meta_info' : _MetaInfoClass('Ipv6Network.Nodes.Node',
            False, 
            [
            _MetaInfoClassMember('node-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                The node name
                ''',
                'node_name',
                'Cisco-IOS-XR-ipv6-ma-oper', True),
            _MetaInfoClassMember('interface-data', REFERENCE_CLASS, 'InterfaceData' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper', 'Ipv6Network.Nodes.Node.InterfaceData', 
                [], [], 
                '''                IPv6 network operational interface data
                ''',
                'interface_data',
                'Cisco-IOS-XR-ipv6-ma-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-ma-oper',
            'node',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ma-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper'
        ),
    },
    'Ipv6Network.Nodes' : {
        'meta_info' : _MetaInfoClass('Ipv6Network.Nodes',
            False, 
            [
            _MetaInfoClassMember('node', REFERENCE_LIST, 'Node' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper', 'Ipv6Network.Nodes.Node', 
                [], [], 
                '''                IPv6 network operational data for a particular
                node
                ''',
                'node',
                'Cisco-IOS-XR-ipv6-ma-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-ma-oper',
            'nodes',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ma-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper'
        ),
    },
    'Ipv6Network' : {
        'meta_info' : _MetaInfoClass('Ipv6Network',
            False, 
            [
            _MetaInfoClassMember('nodes', REFERENCE_CLASS, 'Nodes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper', 'Ipv6Network.Nodes', 
                [], [], 
                '''                Node-specific IPv6 network operational data
                ''',
                'nodes',
                'Cisco-IOS-XR-ipv6-ma-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-ma-oper',
            'ipv6-network',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ma-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ma_oper'
        ),
    },
}
_meta_table['Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Briefs.Brief.LinkLocalAddress']['meta_info'].parent =_meta_table['Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Briefs.Brief']['meta_info']
_meta_table['Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Briefs.Brief.Address']['meta_info'].parent =_meta_table['Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Briefs.Brief']['meta_info']
_meta_table['Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Briefs.Brief']['meta_info'].parent =_meta_table['Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Briefs']['meta_info']
_meta_table['Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.BgpPa.Input']['meta_info'].parent =_meta_table['Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.BgpPa']['meta_info']
_meta_table['Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.BgpPa.Output']['meta_info'].parent =_meta_table['Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.BgpPa']['meta_info']
_meta_table['Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.LinkLocalAddress']['meta_info'].parent =_meta_table['Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail']['meta_info']
_meta_table['Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.AccessControlList']['meta_info'].parent =_meta_table['Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail']['meta_info']
_meta_table['Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.MultiAccessControlList']['meta_info'].parent =_meta_table['Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail']['meta_info']
_meta_table['Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.Rpf']['meta_info'].parent =_meta_table['Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail']['meta_info']
_meta_table['Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.BgpPa']['meta_info'].parent =_meta_table['Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail']['meta_info']
_meta_table['Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.Utime']['meta_info'].parent =_meta_table['Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail']['meta_info']
_meta_table['Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.IdbUtime']['meta_info'].parent =_meta_table['Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail']['meta_info']
_meta_table['Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.CapsUtime']['meta_info'].parent =_meta_table['Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail']['meta_info']
_meta_table['Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.FwdEnUtime']['meta_info'].parent =_meta_table['Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail']['meta_info']
_meta_table['Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.FwdDisUtime']['meta_info'].parent =_meta_table['Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail']['meta_info']
_meta_table['Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.MulticastGroup']['meta_info'].parent =_meta_table['Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail']['meta_info']
_meta_table['Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.Address']['meta_info'].parent =_meta_table['Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail']['meta_info']
_meta_table['Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail.ClientMulticastGroup']['meta_info'].parent =_meta_table['Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail']['meta_info']
_meta_table['Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails.GlobalDetail']['meta_info'].parent =_meta_table['Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails']['meta_info']
_meta_table['Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalBriefs.GlobalBrief.LinkLocalAddress']['meta_info'].parent =_meta_table['Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalBriefs.GlobalBrief']['meta_info']
_meta_table['Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalBriefs.GlobalBrief.Address']['meta_info'].parent =_meta_table['Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalBriefs.GlobalBrief']['meta_info']
_meta_table['Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalBriefs.GlobalBrief']['meta_info'].parent =_meta_table['Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalBriefs']['meta_info']
_meta_table['Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.BgpPa.Input']['meta_info'].parent =_meta_table['Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.BgpPa']['meta_info']
_meta_table['Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.BgpPa.Output']['meta_info'].parent =_meta_table['Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.BgpPa']['meta_info']
_meta_table['Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.LinkLocalAddress']['meta_info'].parent =_meta_table['Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail']['meta_info']
_meta_table['Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.AccessControlList']['meta_info'].parent =_meta_table['Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail']['meta_info']
_meta_table['Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.MultiAccessControlList']['meta_info'].parent =_meta_table['Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail']['meta_info']
_meta_table['Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.Rpf']['meta_info'].parent =_meta_table['Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail']['meta_info']
_meta_table['Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.BgpPa']['meta_info'].parent =_meta_table['Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail']['meta_info']
_meta_table['Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.Utime']['meta_info'].parent =_meta_table['Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail']['meta_info']
_meta_table['Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.IdbUtime']['meta_info'].parent =_meta_table['Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail']['meta_info']
_meta_table['Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.CapsUtime']['meta_info'].parent =_meta_table['Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail']['meta_info']
_meta_table['Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.FwdEnUtime']['meta_info'].parent =_meta_table['Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail']['meta_info']
_meta_table['Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.FwdDisUtime']['meta_info'].parent =_meta_table['Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail']['meta_info']
_meta_table['Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.MulticastGroup']['meta_info'].parent =_meta_table['Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail']['meta_info']
_meta_table['Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.Address']['meta_info'].parent =_meta_table['Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail']['meta_info']
_meta_table['Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail.ClientMulticastGroup']['meta_info'].parent =_meta_table['Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail']['meta_info']
_meta_table['Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details.Detail']['meta_info'].parent =_meta_table['Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details']['meta_info']
_meta_table['Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Briefs']['meta_info'].parent =_meta_table['Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf']['meta_info']
_meta_table['Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalDetails']['meta_info'].parent =_meta_table['Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf']['meta_info']
_meta_table['Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.GlobalBriefs']['meta_info'].parent =_meta_table['Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf']['meta_info']
_meta_table['Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf.Details']['meta_info'].parent =_meta_table['Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf']['meta_info']
_meta_table['Ipv6Network.Nodes.Node.InterfaceData.Vrfs.Vrf']['meta_info'].parent =_meta_table['Ipv6Network.Nodes.Node.InterfaceData.Vrfs']['meta_info']
_meta_table['Ipv6Network.Nodes.Node.InterfaceData.Summary.IfUpUp']['meta_info'].parent =_meta_table['Ipv6Network.Nodes.Node.InterfaceData.Summary']['meta_info']
_meta_table['Ipv6Network.Nodes.Node.InterfaceData.Summary.IfUpDown']['meta_info'].parent =_meta_table['Ipv6Network.Nodes.Node.InterfaceData.Summary']['meta_info']
_meta_table['Ipv6Network.Nodes.Node.InterfaceData.Summary.IfDownDown']['meta_info'].parent =_meta_table['Ipv6Network.Nodes.Node.InterfaceData.Summary']['meta_info']
_meta_table['Ipv6Network.Nodes.Node.InterfaceData.Summary.IfShutdownDown']['meta_info'].parent =_meta_table['Ipv6Network.Nodes.Node.InterfaceData.Summary']['meta_info']
_meta_table['Ipv6Network.Nodes.Node.InterfaceData.Vrfs']['meta_info'].parent =_meta_table['Ipv6Network.Nodes.Node.InterfaceData']['meta_info']
_meta_table['Ipv6Network.Nodes.Node.InterfaceData.Summary']['meta_info'].parent =_meta_table['Ipv6Network.Nodes.Node.InterfaceData']['meta_info']
_meta_table['Ipv6Network.Nodes.Node.InterfaceData']['meta_info'].parent =_meta_table['Ipv6Network.Nodes.Node']['meta_info']
_meta_table['Ipv6Network.Nodes.Node']['meta_info'].parent =_meta_table['Ipv6Network.Nodes']['meta_info']
_meta_table['Ipv6Network.Nodes']['meta_info'].parent =_meta_table['Ipv6Network']['meta_info']
