


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'MplsLdpAdvertiseBgpaclEnum' : _MetaInfoEnum('MplsLdpAdvertiseBgpaclEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg',
        {
            'peer-acl':'peer_acl',
        }, 'Cisco-IOS-XR-mpls-ldp-cfg', _yang_ns._namespaces['Cisco-IOS-XR-mpls-ldp-cfg']),
    'MplsLdpLabelAllocationEnum' : _MetaInfoEnum('MplsLdpLabelAllocationEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg',
        {
            'acl':'acl',
            'host':'host',
        }, 'Cisco-IOS-XR-mpls-ldp-cfg', _yang_ns._namespaces['Cisco-IOS-XR-mpls-ldp-cfg']),
    'MplsLdpTransportAddressEnum' : _MetaInfoEnum('MplsLdpTransportAddressEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg',
        {
            'interface':'interface',
            'address':'address',
        }, 'Cisco-IOS-XR-mpls-ldp-cfg', _yang_ns._namespaces['Cisco-IOS-XR-mpls-ldp-cfg']),
    'MldpPolicyModeEnum' : _MetaInfoEnum('MldpPolicyModeEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg',
        {
            'inbound':'inbound',
            'outbound':'outbound',
        }, 'Cisco-IOS-XR-mpls-ldp-cfg', _yang_ns._namespaces['Cisco-IOS-XR-mpls-ldp-cfg']),
    'MplsLdpExpNullEnum' : _MetaInfoEnum('MplsLdpExpNullEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg',
        {
            'all':'all',
            'for':'for_',
            'to':'to',
            'for-to':'for_to',
        }, 'Cisco-IOS-XR-mpls-ldp-cfg', _yang_ns._namespaces['Cisco-IOS-XR-mpls-ldp-cfg']),
    'MplsLdpTargetedAcceptEnum' : _MetaInfoEnum('MplsLdpTargetedAcceptEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg',
        {
            'all':'all',
            'from':'from_',
        }, 'Cisco-IOS-XR-mpls-ldp-cfg', _yang_ns._namespaces['Cisco-IOS-XR-mpls-ldp-cfg']),
    'MplsLdpDownstreamOnDemandEnum' : _MetaInfoEnum('MplsLdpDownstreamOnDemandEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg',
        {
            'peer-acl':'peer_acl',
        }, 'Cisco-IOS-XR-mpls-ldp-cfg', _yang_ns._namespaces['Cisco-IOS-XR-mpls-ldp-cfg']),
    'MplsLdpafNameEnum' : _MetaInfoEnum('MplsLdpafNameEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg',
        {
            'ipv4':'ipv4',
            'ipv6':'ipv6',
        }, 'Cisco-IOS-XR-mpls-ldp-cfg', _yang_ns._namespaces['Cisco-IOS-XR-mpls-ldp-cfg']),
    'MplsLdpLabelAdvertiseEnum' : _MetaInfoEnum('MplsLdpLabelAdvertiseEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg',
        {
            'for':'for_',
            'for-to':'for_to',
        }, 'Cisco-IOS-XR-mpls-ldp-cfg', _yang_ns._namespaces['Cisco-IOS-XR-mpls-ldp-cfg']),
    'MplsLdpNbrPasswordEnum' : _MetaInfoEnum('MplsLdpNbrPasswordEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg',
        {
            'disable':'disable',
            'specified':'specified',
        }, 'Cisco-IOS-XR-mpls-ldp-cfg', _yang_ns._namespaces['Cisco-IOS-XR-mpls-ldp-cfg']),
    'MplsLdpSessionProtectionEnum' : _MetaInfoEnum('MplsLdpSessionProtectionEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg',
        {
            'all':'all',
            'for':'for_',
            'all-with-duration':'all_with_duration',
            'for-with-duration':'for_with_duration',
            'all-with-forever':'all_with_forever',
            'for-with-forever':'for_with_forever',
        }, 'Cisco-IOS-XR-mpls-ldp-cfg', _yang_ns._namespaces['Cisco-IOS-XR-mpls-ldp-cfg']),
    'MplsLdp.DefaultVrf.Afs.Af.Label.Remote.Accept.PeerAcceptPolicies.PeerAcceptPolicy' : {
        'meta_info' : _MetaInfoClass('MplsLdp.DefaultVrf.Afs.Af.Label.Remote.Accept.PeerAcceptPolicies.PeerAcceptPolicy',
            False, 
            [
            _MetaInfoClassMember('lsr-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                LSR ID of neighbor
                ''',
                'lsr_id',
                'Cisco-IOS-XR-mpls-ldp-cfg', True),
            _MetaInfoClassMember('label-space-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Label space ID of neighbor
                ''',
                'label_space_id',
                'Cisco-IOS-XR-mpls-ldp-cfg', True),
            _MetaInfoClassMember('prefix-acl-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of prefix ACL
                ''',
                'prefix_acl_name',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-ldp-cfg',
            'peer-accept-policy',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-ldp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg'
        ),
    },
    'MplsLdp.DefaultVrf.Afs.Af.Label.Remote.Accept.PeerAcceptPolicies' : {
        'meta_info' : _MetaInfoClass('MplsLdp.DefaultVrf.Afs.Af.Label.Remote.Accept.PeerAcceptPolicies',
            False, 
            [
            _MetaInfoClassMember('peer-accept-policy', REFERENCE_LIST, 'PeerAcceptPolicy' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg', 'MplsLdp.DefaultVrf.Afs.Af.Label.Remote.Accept.PeerAcceptPolicies.PeerAcceptPolicy', 
                [], [], 
                '''                Control acceptance of labels from a
                neighbor for prefix(es) using ACL
                ''',
                'peer_accept_policy',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-ldp-cfg',
            'peer-accept-policies',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-ldp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg'
        ),
    },
    'MplsLdp.DefaultVrf.Afs.Af.Label.Remote.Accept' : {
        'meta_info' : _MetaInfoClass('MplsLdp.DefaultVrf.Afs.Af.Label.Remote.Accept',
            False, 
            [
            _MetaInfoClassMember('peer-accept-policies', REFERENCE_CLASS, 'PeerAcceptPolicies' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg', 'MplsLdp.DefaultVrf.Afs.Af.Label.Remote.Accept.PeerAcceptPolicies', 
                [], [], 
                '''                Configuration related to neighbors for
                inbound label acceptance
                ''',
                'peer_accept_policies',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-ldp-cfg',
            'accept',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-ldp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg'
        ),
    },
    'MplsLdp.DefaultVrf.Afs.Af.Label.Remote' : {
        'meta_info' : _MetaInfoClass('MplsLdp.DefaultVrf.Afs.Af.Label.Remote',
            False, 
            [
            _MetaInfoClassMember('accept', REFERENCE_CLASS, 'Accept' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg', 'MplsLdp.DefaultVrf.Afs.Af.Label.Remote.Accept', 
                [], [], 
                '''                Configure inbound label acceptance
                ''',
                'accept',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-ldp-cfg',
            'remote',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-ldp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg'
        ),
    },
    'MplsLdp.DefaultVrf.Afs.Af.Label.Local.Advertise.PeerAdvertisePolicies.PeerAdvertisePolicy' : {
        'meta_info' : _MetaInfoClass('MplsLdp.DefaultVrf.Afs.Af.Label.Local.Advertise.PeerAdvertisePolicies.PeerAdvertisePolicy',
            False, 
            [
            _MetaInfoClassMember('lsr-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                LSR ID of neighbor
                ''',
                'lsr_id',
                'Cisco-IOS-XR-mpls-ldp-cfg', True),
            _MetaInfoClassMember('label-space-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Label space ID of neighbor
                ''',
                'label_space_id',
                'Cisco-IOS-XR-mpls-ldp-cfg', True),
            _MetaInfoClassMember('prefix-acl-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of prefix ACL
                ''',
                'prefix_acl_name',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-ldp-cfg',
            'peer-advertise-policy',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-ldp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg'
        ),
    },
    'MplsLdp.DefaultVrf.Afs.Af.Label.Local.Advertise.PeerAdvertisePolicies' : {
        'meta_info' : _MetaInfoClass('MplsLdp.DefaultVrf.Afs.Af.Label.Local.Advertise.PeerAdvertisePolicies',
            False, 
            [
            _MetaInfoClassMember('peer-advertise-policy', REFERENCE_LIST, 'PeerAdvertisePolicy' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg', 'MplsLdp.DefaultVrf.Afs.Af.Label.Local.Advertise.PeerAdvertisePolicies.PeerAdvertisePolicy', 
                [], [], 
                '''                Control advertisement of prefix(es) using
                ACL
                ''',
                'peer_advertise_policy',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-ldp-cfg',
            'peer-advertise-policies',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-ldp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg'
        ),
    },
    'MplsLdp.DefaultVrf.Afs.Af.Label.Local.Advertise.PrefixAdvertisePolicies.PrefixAdvertisePolicy' : {
        'meta_info' : _MetaInfoClass('MplsLdp.DefaultVrf.Afs.Af.Label.Local.Advertise.PrefixAdvertisePolicies.PrefixAdvertisePolicy',
            False, 
            [
            _MetaInfoClassMember('prefix-acl-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Name of prefix ACL
                ''',
                'prefix_acl_name',
                'Cisco-IOS-XR-mpls-ldp-cfg', True),
            _MetaInfoClassMember('advertise-type', REFERENCE_ENUM_CLASS, 'MplsLdpLabelAdvertiseEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg', 'MplsLdpLabelAdvertiseEnum', 
                [], [], 
                '''                Label advertise type
                ''',
                'advertise_type',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            _MetaInfoClassMember('peer-acl-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of peer ACL
                ''',
                'peer_acl_name',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-ldp-cfg',
            'prefix-advertise-policy',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-ldp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg'
        ),
    },
    'MplsLdp.DefaultVrf.Afs.Af.Label.Local.Advertise.PrefixAdvertisePolicies' : {
        'meta_info' : _MetaInfoClass('MplsLdp.DefaultVrf.Afs.Af.Label.Local.Advertise.PrefixAdvertisePolicies',
            False, 
            [
            _MetaInfoClassMember('prefix-advertise-policy', REFERENCE_LIST, 'PrefixAdvertisePolicy' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg', 'MplsLdp.DefaultVrf.Afs.Af.Label.Local.Advertise.PrefixAdvertisePolicies.PrefixAdvertisePolicy', 
                [], [], 
                '''                Control advertisement of prefix(es) using
                ACL
                ''',
                'prefix_advertise_policy',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-ldp-cfg',
            'prefix-advertise-policies',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-ldp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg'
        ),
    },
    'MplsLdp.DefaultVrf.Afs.Af.Label.Local.Advertise.ExplicitNull' : {
        'meta_info' : _MetaInfoClass('MplsLdp.DefaultVrf.Afs.Af.Label.Local.Advertise.ExplicitNull',
            False, 
            [
            _MetaInfoClassMember('explicit-null-type', REFERENCE_ENUM_CLASS, 'MplsLdpExpNullEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg', 'MplsLdpExpNullEnum', 
                [], [], 
                '''                Explicit Null command variant
                ''',
                'explicit_null_type',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            _MetaInfoClassMember('peer-acl-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of peer ACL
                ''',
                'peer_acl_name',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            _MetaInfoClassMember('prefix-acl-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of prefix ACL
                ''',
                'prefix_acl_name',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-ldp-cfg',
            'explicit-null',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-ldp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg'
        ),
    },
    'MplsLdp.DefaultVrf.Afs.Af.Label.Local.Advertise.Interfaces.Interface' : {
        'meta_info' : _MetaInfoClass('MplsLdp.DefaultVrf.Afs.Af.Label.Local.Advertise.Interfaces.Interface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Name of interface
                ''',
                'interface_name',
                'Cisco-IOS-XR-mpls-ldp-cfg', True),
            ],
            'Cisco-IOS-XR-mpls-ldp-cfg',
            'interface',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-ldp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg'
        ),
    },
    'MplsLdp.DefaultVrf.Afs.Af.Label.Local.Advertise.Interfaces' : {
        'meta_info' : _MetaInfoClass('MplsLdp.DefaultVrf.Afs.Af.Label.Local.Advertise.Interfaces',
            False, 
            [
            _MetaInfoClassMember('interface', REFERENCE_LIST, 'Interface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg', 'MplsLdp.DefaultVrf.Afs.Af.Label.Local.Advertise.Interfaces.Interface', 
                [], [], 
                '''                Control advertisement of interface's host
                IP address
                ''',
                'interface',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-ldp-cfg',
            'interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-ldp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg'
        ),
    },
    'MplsLdp.DefaultVrf.Afs.Af.Label.Local.Advertise' : {
        'meta_info' : _MetaInfoClass('MplsLdp.DefaultVrf.Afs.Af.Label.Local.Advertise',
            False, 
            [
            _MetaInfoClassMember('disable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Disable label advertisement
                ''',
                'disable',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            _MetaInfoClassMember('explicit-null', REFERENCE_CLASS, 'ExplicitNull' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg', 'MplsLdp.DefaultVrf.Afs.Af.Label.Local.Advertise.ExplicitNull', 
                [], [], 
                '''                Configure advertisment of explicit-null
                for connected prefixes.
                ''',
                'explicit_null',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            _MetaInfoClassMember('interfaces', REFERENCE_CLASS, 'Interfaces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg', 'MplsLdp.DefaultVrf.Afs.Af.Label.Local.Advertise.Interfaces', 
                [], [], 
                '''                Configure outbound label advertisement for
                an interface
                ''',
                'interfaces',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            _MetaInfoClassMember('peer-advertise-policies', REFERENCE_CLASS, 'PeerAdvertisePolicies' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg', 'MplsLdp.DefaultVrf.Afs.Af.Label.Local.Advertise.PeerAdvertisePolicies', 
                [], [], 
                '''                Configure peer centric outbound label
                advertisement using ACL
                ''',
                'peer_advertise_policies',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            _MetaInfoClassMember('prefix-advertise-policies', REFERENCE_CLASS, 'PrefixAdvertisePolicies' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg', 'MplsLdp.DefaultVrf.Afs.Af.Label.Local.Advertise.PrefixAdvertisePolicies', 
                [], [], 
                '''                Configure prefix centric outbound label
                advertisement using ACL
                ''',
                'prefix_advertise_policies',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-ldp-cfg',
            'advertise',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-ldp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg'
        ),
    },
    'MplsLdp.DefaultVrf.Afs.Af.Label.Local.Allocate' : {
        'meta_info' : _MetaInfoClass('MplsLdp.DefaultVrf.Afs.Af.Label.Local.Allocate',
            False, 
            [
            _MetaInfoClassMember('allocation-type', REFERENCE_ENUM_CLASS, 'MplsLdpLabelAllocationEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg', 'MplsLdpLabelAllocationEnum', 
                [], [], 
                '''                Label allocation type
                ''',
                'allocation_type',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            _MetaInfoClassMember('prefix-acl-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of prefix ACL
                ''',
                'prefix_acl_name',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-ldp-cfg',
            'allocate',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-ldp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg'
        ),
    },
    'MplsLdp.DefaultVrf.Afs.Af.Label.Local' : {
        'meta_info' : _MetaInfoClass('MplsLdp.DefaultVrf.Afs.Af.Label.Local',
            False, 
            [
            _MetaInfoClassMember('advertise', REFERENCE_CLASS, 'Advertise' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg', 'MplsLdp.DefaultVrf.Afs.Af.Label.Local.Advertise', 
                [], [], 
                '''                Configure outbound label advertisement
                ''',
                'advertise',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            _MetaInfoClassMember('allocate', REFERENCE_CLASS, 'Allocate' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg', 'MplsLdp.DefaultVrf.Afs.Af.Label.Local.Allocate', 
                [], [], 
                '''                Control local label allocation for
                prefix(es)
                ''',
                'allocate',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            _MetaInfoClassMember('default-route', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable MPLS forwarding for default route
                ''',
                'default_route',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            _MetaInfoClassMember('implicit-null-override', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Control use of implicit-null label for set
                of prefix(es)
                ''',
                'implicit_null_override',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-ldp-cfg',
            'local',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-ldp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg'
        ),
    },
    'MplsLdp.DefaultVrf.Afs.Af.Label' : {
        'meta_info' : _MetaInfoClass('MplsLdp.DefaultVrf.Afs.Af.Label',
            False, 
            [
            _MetaInfoClassMember('local', REFERENCE_CLASS, 'Local' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg', 'MplsLdp.DefaultVrf.Afs.Af.Label.Local', 
                [], [], 
                '''                Configure local label policies and control
                ''',
                'local',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            _MetaInfoClassMember('remote', REFERENCE_CLASS, 'Remote' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg', 'MplsLdp.DefaultVrf.Afs.Af.Label.Remote', 
                [], [], 
                '''                Configure remote/peer label policies and
                control
                ''',
                'remote',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-ldp-cfg',
            'label',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-ldp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg'
        ),
    },
    'MplsLdp.DefaultVrf.Afs.Af.Discovery.TargetedHelloAccept' : {
        'meta_info' : _MetaInfoClass('MplsLdp.DefaultVrf.Afs.Af.Discovery.TargetedHelloAccept',
            False, 
            [
            _MetaInfoClassMember('accept-type', REFERENCE_ENUM_CLASS, 'MplsLdpTargetedAcceptEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg', 'MplsLdpTargetedAcceptEnum', 
                [], [], 
                '''                Type of acceptance
                ''',
                'accept_type',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            _MetaInfoClassMember('peer-acl-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of peer ACL
                ''',
                'peer_acl_name',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-ldp-cfg',
            'targeted-hello-accept',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-ldp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg'
        ),
    },
    'MplsLdp.DefaultVrf.Afs.Af.Discovery' : {
        'meta_info' : _MetaInfoClass('MplsLdp.DefaultVrf.Afs.Af.Discovery',
            False, 
            [
            _MetaInfoClassMember('targeted-hello-accept', REFERENCE_CLASS, 'TargetedHelloAccept' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg', 'MplsLdp.DefaultVrf.Afs.Af.Discovery.TargetedHelloAccept', 
                [], [], 
                '''                Configure acceptance from and responding to
                targeted hellos.
                ''',
                'targeted_hello_accept',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            _MetaInfoClassMember('transport-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Global discovery transport address for
                address family
                ''',
                'transport_address',
                'Cisco-IOS-XR-mpls-ldp-cfg', False, [
                    _MetaInfoClassMember('transport-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Global discovery transport address for
                        address family
                        ''',
                        'transport_address',
                        'Cisco-IOS-XR-mpls-ldp-cfg', False),
                    _MetaInfoClassMember('transport-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Global discovery transport address for
                        address family
                        ''',
                        'transport_address',
                        'Cisco-IOS-XR-mpls-ldp-cfg', False),
                ]),
            ],
            'Cisco-IOS-XR-mpls-ldp-cfg',
            'discovery',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-ldp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg'
        ),
    },
    'MplsLdp.DefaultVrf.Afs.Af.TrafficEngineering.AutoTunnelMesh.GroupIds.GroupId' : {
        'meta_info' : _MetaInfoClass('MplsLdp.DefaultVrf.Afs.Af.TrafficEngineering.AutoTunnelMesh.GroupIds.GroupId',
            False, 
            [
            _MetaInfoClassMember('mesh-group-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Mesh group ID
                ''',
                'mesh_group_id',
                'Cisco-IOS-XR-mpls-ldp-cfg', True),
            ],
            'Cisco-IOS-XR-mpls-ldp-cfg',
            'group-id',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-ldp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg'
        ),
    },
    'MplsLdp.DefaultVrf.Afs.Af.TrafficEngineering.AutoTunnelMesh.GroupIds' : {
        'meta_info' : _MetaInfoClass('MplsLdp.DefaultVrf.Afs.Af.TrafficEngineering.AutoTunnelMesh.GroupIds',
            False, 
            [
            _MetaInfoClassMember('group-id', REFERENCE_LIST, 'GroupId' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg', 'MplsLdp.DefaultVrf.Afs.Af.TrafficEngineering.AutoTunnelMesh.GroupIds.GroupId', 
                [], [], 
                '''                Auto-mesh group identifier to enable
                ''',
                'group_id',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-ldp-cfg',
            'group-ids',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-ldp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg'
        ),
    },
    'MplsLdp.DefaultVrf.Afs.Af.TrafficEngineering.AutoTunnelMesh' : {
        'meta_info' : _MetaInfoClass('MplsLdp.DefaultVrf.Afs.Af.TrafficEngineering.AutoTunnelMesh',
            False, 
            [
            _MetaInfoClassMember('group-all', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable all MPLS TE auto-tunnel mesh-group
                interfaces
                ''',
                'group_all',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            _MetaInfoClassMember('group-ids', REFERENCE_CLASS, 'GroupIds' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg', 'MplsLdp.DefaultVrf.Afs.Af.TrafficEngineering.AutoTunnelMesh.GroupIds', 
                [], [], 
                '''                Enable interfaces in specific MPLS TE
                auto-tunnel mesh-groups
                ''',
                'group_ids',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-ldp-cfg',
            'auto-tunnel-mesh',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-ldp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg'
        ),
    },
    'MplsLdp.DefaultVrf.Afs.Af.TrafficEngineering' : {
        'meta_info' : _MetaInfoClass('MplsLdp.DefaultVrf.Afs.Af.TrafficEngineering',
            False, 
            [
            _MetaInfoClassMember('auto-tunnel-mesh', REFERENCE_CLASS, 'AutoTunnelMesh' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg', 'MplsLdp.DefaultVrf.Afs.Af.TrafficEngineering.AutoTunnelMesh', 
                [], [], 
                '''                MPLS Traffic Engineering auto-tunnel mesh
                parameters for LDP
                ''',
                'auto_tunnel_mesh',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-ldp-cfg',
            'traffic-engineering',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-ldp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg'
        ),
    },
    'MplsLdp.DefaultVrf.Afs.Af.Neighbor.Addresses.Address' : {
        'meta_info' : _MetaInfoClass('MplsLdp.DefaultVrf.Afs.Af.Neighbor.Addresses.Address',
            False, 
            [
            _MetaInfoClassMember('ip-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                The IP address
                ''',
                'ip_address',
                'Cisco-IOS-XR-mpls-ldp-cfg', True, [
                    _MetaInfoClassMember('ip-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        The IP address
                        ''',
                        'ip_address',
                        'Cisco-IOS-XR-mpls-ldp-cfg', True),
                    _MetaInfoClassMember('ip-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        The IP address
                        ''',
                        'ip_address',
                        'Cisco-IOS-XR-mpls-ldp-cfg', True),
                ]),
            _MetaInfoClassMember('targeted', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Establish targeted session with given
                address
                ''',
                'targeted',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-ldp-cfg',
            'address',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-ldp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg'
        ),
    },
    'MplsLdp.DefaultVrf.Afs.Af.Neighbor.Addresses' : {
        'meta_info' : _MetaInfoClass('MplsLdp.DefaultVrf.Afs.Af.Neighbor.Addresses',
            False, 
            [
            _MetaInfoClassMember('address', REFERENCE_LIST, 'Address' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg', 'MplsLdp.DefaultVrf.Afs.Af.Neighbor.Addresses.Address', 
                [], [], 
                '''                IP address based configuration related to a
                neighbor
                ''',
                'address',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-ldp-cfg',
            'addresses',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-ldp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg'
        ),
    },
    'MplsLdp.DefaultVrf.Afs.Af.Neighbor' : {
        'meta_info' : _MetaInfoClass('MplsLdp.DefaultVrf.Afs.Af.Neighbor',
            False, 
            [
            _MetaInfoClassMember('addresses', REFERENCE_CLASS, 'Addresses' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg', 'MplsLdp.DefaultVrf.Afs.Af.Neighbor.Addresses', 
                [], [], 
                '''                Configuration related to neighbors using
                neighbor address
                ''',
                'addresses',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-ldp-cfg',
            'neighbor',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-ldp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg'
        ),
    },
    'MplsLdp.DefaultVrf.Afs.Af.RedistributionProtocol.Bgp.As_' : {
        'meta_info' : _MetaInfoClass('MplsLdp.DefaultVrf.Afs.Af.RedistributionProtocol.Bgp.As_',
            False, 
            [
            _MetaInfoClassMember('as-xx', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                First half of BGP AS number in XX.YY
                format.  Mandatory Must be a non-zero
                value if second half is zero.
                ''',
                'as_xx',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            _MetaInfoClassMember('as-yy', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Second half of BGP AS number in XX.YY
                format. Mandatory Must be a non-zero value
                if first half is zero.
                ''',
                'as_yy',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-ldp-cfg',
            'as',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-ldp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg'
        ),
    },
    'MplsLdp.DefaultVrf.Afs.Af.RedistributionProtocol.Bgp.AdvertiseTo' : {
        'meta_info' : _MetaInfoClass('MplsLdp.DefaultVrf.Afs.Af.RedistributionProtocol.Bgp.AdvertiseTo',
            False, 
            [
            _MetaInfoClassMember('peer-acl-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of peer ACL
                ''',
                'peer_acl_name',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            _MetaInfoClassMember('type', REFERENCE_ENUM_CLASS, 'MplsLdpAdvertiseBgpaclEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg', 'MplsLdpAdvertiseBgpaclEnum', 
                [], [], 
                '''                advertise to peer acl type
                ''',
                'type',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-ldp-cfg',
            'advertise-to',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-ldp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg'
        ),
    },
    'MplsLdp.DefaultVrf.Afs.Af.RedistributionProtocol.Bgp' : {
        'meta_info' : _MetaInfoClass('MplsLdp.DefaultVrf.Afs.Af.RedistributionProtocol.Bgp',
            False, 
            [
            _MetaInfoClassMember('advertise-to', REFERENCE_CLASS, 'AdvertiseTo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg', 'MplsLdp.DefaultVrf.Afs.Af.RedistributionProtocol.Bgp.AdvertiseTo', 
                [], [], 
                '''                ACL containing list of neighbors for BGP
                route redistribution
                ''',
                'advertise_to',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            _MetaInfoClassMember('as', REFERENCE_CLASS, 'As_' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg', 'MplsLdp.DefaultVrf.Afs.Af.RedistributionProtocol.Bgp.As_', 
                [], [], 
                '''                MPLS LDP configuration for protocol
                redistribution
                ''',
                'as_',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-ldp-cfg',
            'bgp',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-ldp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg'
        ),
    },
    'MplsLdp.DefaultVrf.Afs.Af.RedistributionProtocol' : {
        'meta_info' : _MetaInfoClass('MplsLdp.DefaultVrf.Afs.Af.RedistributionProtocol',
            False, 
            [
            _MetaInfoClassMember('bgp', REFERENCE_CLASS, 'Bgp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg', 'MplsLdp.DefaultVrf.Afs.Af.RedistributionProtocol.Bgp', 
                [], [], 
                '''                MPLS LDP configuration for protocol
                redistribution
                ''',
                'bgp',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-ldp-cfg',
            'redistribution-protocol',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-ldp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg'
        ),
    },
    'MplsLdp.DefaultVrf.Afs.Af' : {
        'meta_info' : _MetaInfoClass('MplsLdp.DefaultVrf.Afs.Af',
            False, 
            [
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'MplsLdpafNameEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg', 'MplsLdpafNameEnum', 
                [], [], 
                '''                Address Family type
                ''',
                'af_name',
                'Cisco-IOS-XR-mpls-ldp-cfg', True),
            _MetaInfoClassMember('discovery', REFERENCE_CLASS, 'Discovery' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg', 'MplsLdp.DefaultVrf.Afs.Af.Discovery', 
                [], [], 
                '''                Configure Discovery parameters
                ''',
                'discovery',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable Address Family
                ''',
                'enable',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            _MetaInfoClassMember('label', REFERENCE_CLASS, 'Label' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg', 'MplsLdp.DefaultVrf.Afs.Af.Label', 
                [], [], 
                '''                Configure Label policies and control
                ''',
                'label',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            _MetaInfoClassMember('neighbor', REFERENCE_CLASS, 'Neighbor' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg', 'MplsLdp.DefaultVrf.Afs.Af.Neighbor', 
                [], [], 
                '''                Configuration related to Neighbors
                ''',
                'neighbor',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            _MetaInfoClassMember('redistribution-protocol', REFERENCE_CLASS, 'RedistributionProtocol' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg', 'MplsLdp.DefaultVrf.Afs.Af.RedistributionProtocol', 
                [], [], 
                '''                MPLS LDP configuration for protocol
                redistribution
                ''',
                'redistribution_protocol',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            _MetaInfoClassMember('traffic-engineering', REFERENCE_CLASS, 'TrafficEngineering' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg', 'MplsLdp.DefaultVrf.Afs.Af.TrafficEngineering', 
                [], [], 
                '''                MPLS Traffic Engingeering parameters for LDP
                ''',
                'traffic_engineering',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-ldp-cfg',
            'af',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-ldp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg'
        ),
    },
    'MplsLdp.DefaultVrf.Afs' : {
        'meta_info' : _MetaInfoClass('MplsLdp.DefaultVrf.Afs',
            False, 
            [
            _MetaInfoClassMember('af', REFERENCE_LIST, 'Af' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg', 'MplsLdp.DefaultVrf.Afs.Af', 
                [], [], 
                '''                Configure data for given Address Family
                ''',
                'af',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-ldp-cfg',
            'afs',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-ldp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg'
        ),
    },
    'MplsLdp.DefaultVrf.Global_.Session.Protection' : {
        'meta_info' : _MetaInfoClass('MplsLdp.DefaultVrf.Global_.Session.Protection',
            False, 
            [
            _MetaInfoClassMember('duration', ATTRIBUTE, 'int' , None, None, 
                [('30', '2147483')], [], 
                '''                Holdup duration
                ''',
                'duration',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            _MetaInfoClassMember('peer-acl-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of peer ACL
                ''',
                'peer_acl_name',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            _MetaInfoClassMember('protection-type', REFERENCE_ENUM_CLASS, 'MplsLdpSessionProtectionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg', 'MplsLdpSessionProtectionEnum', 
                [], [], 
                '''                Session protection type
                ''',
                'protection_type',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-ldp-cfg',
            'protection',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-ldp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg'
        ),
    },
    'MplsLdp.DefaultVrf.Global_.Session.DownstreamOnDemand' : {
        'meta_info' : _MetaInfoClass('MplsLdp.DefaultVrf.Global_.Session.DownstreamOnDemand',
            False, 
            [
            _MetaInfoClassMember('peer-acl-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of peer ACL
                ''',
                'peer_acl_name',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            _MetaInfoClassMember('type', REFERENCE_ENUM_CLASS, 'MplsLdpDownstreamOnDemandEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg', 'MplsLdpDownstreamOnDemandEnum', 
                [], [], 
                '''                Downstream on demand type
                ''',
                'type',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-ldp-cfg',
            'downstream-on-demand',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-ldp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg'
        ),
    },
    'MplsLdp.DefaultVrf.Global_.Session' : {
        'meta_info' : _MetaInfoClass('MplsLdp.DefaultVrf.Global_.Session',
            False, 
            [
            _MetaInfoClassMember('downstream-on-demand', REFERENCE_CLASS, 'DownstreamOnDemand' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg', 'MplsLdp.DefaultVrf.Global_.Session.DownstreamOnDemand', 
                [], [], 
                '''                ACL with the list of neighbors configured for
                Downstream on Demand
                ''',
                'downstream_on_demand',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            _MetaInfoClassMember('protection', REFERENCE_CLASS, 'Protection' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg', 'MplsLdp.DefaultVrf.Global_.Session.Protection', 
                [], [], 
                '''                Configure Session Protection parameters
                ''',
                'protection',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-ldp-cfg',
            'session',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-ldp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg'
        ),
    },
    'MplsLdp.DefaultVrf.Global_.Neighbor.LdpIds.LdpId.Password' : {
        'meta_info' : _MetaInfoClass('MplsLdp.DefaultVrf.Global_.Neighbor.LdpIds.LdpId.Password',
            False, 
            [
            _MetaInfoClassMember('command-type', REFERENCE_ENUM_CLASS, 'MplsLdpNbrPasswordEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg', 'MplsLdpNbrPasswordEnum', 
                [], [], 
                '''                Command type for password configuration
                ''',
                'command_type',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            _MetaInfoClassMember('password', ATTRIBUTE, 'str' , None, None, 
                [], [b'(!.+)|([^!].+)'], 
                '''                The neighbor password
                ''',
                'password',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-ldp-cfg',
            'password',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-ldp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg'
        ),
    },
    'MplsLdp.DefaultVrf.Global_.Neighbor.LdpIds.LdpId' : {
        'meta_info' : _MetaInfoClass('MplsLdp.DefaultVrf.Global_.Neighbor.LdpIds.LdpId',
            False, 
            [
            _MetaInfoClassMember('lsr-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                LSR ID of neighbor
                ''',
                'lsr_id',
                'Cisco-IOS-XR-mpls-ldp-cfg', True),
            _MetaInfoClassMember('label-space-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Label space ID of neighbor
                ''',
                'label_space_id',
                'Cisco-IOS-XR-mpls-ldp-cfg', True),
            _MetaInfoClassMember('password', REFERENCE_CLASS, 'Password' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg', 'MplsLdp.DefaultVrf.Global_.Neighbor.LdpIds.LdpId.Password', 
                [], [], 
                '''                Password for MD5 authentication for this
                neighbor
                ''',
                'password',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-ldp-cfg',
            'ldp-id',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-ldp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg'
        ),
    },
    'MplsLdp.DefaultVrf.Global_.Neighbor.LdpIds' : {
        'meta_info' : _MetaInfoClass('MplsLdp.DefaultVrf.Global_.Neighbor.LdpIds',
            False, 
            [
            _MetaInfoClassMember('ldp-id', REFERENCE_LIST, 'LdpId' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg', 'MplsLdp.DefaultVrf.Global_.Neighbor.LdpIds.LdpId', 
                [], [], 
                '''                LDP ID based configuration related to a
                neigbor
                ''',
                'ldp_id',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-ldp-cfg',
            'ldp-ids',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-ldp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg'
        ),
    },
    'MplsLdp.DefaultVrf.Global_.Neighbor.DualStack.TransportConnection.Prefer' : {
        'meta_info' : _MetaInfoClass('MplsLdp.DefaultVrf.Global_.Neighbor.DualStack.TransportConnection.Prefer',
            False, 
            [
            _MetaInfoClassMember('ipv4', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Configuration related to neighbor
                dual-stack xport-connection preference
                ipv4
                ''',
                'ipv4',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-ldp-cfg',
            'prefer',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-ldp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg'
        ),
    },
    'MplsLdp.DefaultVrf.Global_.Neighbor.DualStack.TransportConnection' : {
        'meta_info' : _MetaInfoClass('MplsLdp.DefaultVrf.Global_.Neighbor.DualStack.TransportConnection',
            False, 
            [
            _MetaInfoClassMember('max-wait', ATTRIBUTE, 'int' , None, None, 
                [('0', '60')], [], 
                '''                Configuration related to neighbor
                dual-stack xport-connection max-wait
                ''',
                'max_wait',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            _MetaInfoClassMember('prefer', REFERENCE_CLASS, 'Prefer' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg', 'MplsLdp.DefaultVrf.Global_.Neighbor.DualStack.TransportConnection.Prefer', 
                [], [], 
                '''                Configuration related to neighbor
                dual-stack xport-connection preference
                ''',
                'prefer',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-ldp-cfg',
            'transport-connection',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-ldp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg'
        ),
    },
    'MplsLdp.DefaultVrf.Global_.Neighbor.DualStack' : {
        'meta_info' : _MetaInfoClass('MplsLdp.DefaultVrf.Global_.Neighbor.DualStack',
            False, 
            [
            _MetaInfoClassMember('tlv-compliance', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Configuration to enable neighbor dual-stack
                tlv-compliance
                ''',
                'tlv_compliance',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            _MetaInfoClassMember('transport-connection', REFERENCE_CLASS, 'TransportConnection' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg', 'MplsLdp.DefaultVrf.Global_.Neighbor.DualStack.TransportConnection', 
                [], [], 
                '''                Configuration related to neighbor transport
                ''',
                'transport_connection',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-ldp-cfg',
            'dual-stack',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-ldp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg'
        ),
    },
    'MplsLdp.DefaultVrf.Global_.Neighbor' : {
        'meta_info' : _MetaInfoClass('MplsLdp.DefaultVrf.Global_.Neighbor',
            False, 
            [
            _MetaInfoClassMember('dual-stack', REFERENCE_CLASS, 'DualStack' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg', 'MplsLdp.DefaultVrf.Global_.Neighbor.DualStack', 
                [], [], 
                '''                Configuration related to neighbor transport
                ''',
                'dual_stack',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            _MetaInfoClassMember('ldp-ids', REFERENCE_CLASS, 'LdpIds' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg', 'MplsLdp.DefaultVrf.Global_.Neighbor.LdpIds', 
                [], [], 
                '''                Configuration related to Neighbors using LDP
                Id
                ''',
                'ldp_ids',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            _MetaInfoClassMember('password', ATTRIBUTE, 'str' , None, None, 
                [], [b'(!.+)|([^!].+)'], 
                '''                Default password for all neigbors
                ''',
                'password',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-ldp-cfg',
            'neighbor',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-ldp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg'
        ),
    },
    'MplsLdp.DefaultVrf.Global_.GracefulRestart.HelperPeer' : {
        'meta_info' : _MetaInfoClass('MplsLdp.DefaultVrf.Global_.GracefulRestart.HelperPeer',
            False, 
            [
            _MetaInfoClassMember('maintain-on-local-reset', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Maintain the state of a GR peer upon a local
                reset
                ''',
                'maintain_on_local_reset',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-ldp-cfg',
            'helper-peer',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-ldp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg'
        ),
    },
    'MplsLdp.DefaultVrf.Global_.GracefulRestart' : {
        'meta_info' : _MetaInfoClass('MplsLdp.DefaultVrf.Global_.GracefulRestart',
            False, 
            [
            _MetaInfoClassMember('helper-peer', REFERENCE_CLASS, 'HelperPeer' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg', 'MplsLdp.DefaultVrf.Global_.GracefulRestart.HelperPeer', 
                [], [], 
                '''                Configure parameters related to GR peer(s)
                opearating in helper mode
                ''',
                'helper_peer',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-ldp-cfg',
            'graceful-restart',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-ldp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg'
        ),
    },
    'MplsLdp.DefaultVrf.Global_' : {
        'meta_info' : _MetaInfoClass('MplsLdp.DefaultVrf.Global_',
            False, 
            [
            _MetaInfoClassMember('graceful-restart', REFERENCE_CLASS, 'GracefulRestart' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg', 'MplsLdp.DefaultVrf.Global_.GracefulRestart', 
                [], [], 
                '''                Configuration for per-VRF LDP Graceful Restart
                parameters
                ''',
                'graceful_restart',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            _MetaInfoClassMember('neighbor', REFERENCE_CLASS, 'Neighbor' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg', 'MplsLdp.DefaultVrf.Global_.Neighbor', 
                [], [], 
                '''                Configuration related to Neighbors
                ''',
                'neighbor',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            _MetaInfoClassMember('router-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Configuration for LDP Router ID (LDP ID)
                ''',
                'router_id',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            _MetaInfoClassMember('session', REFERENCE_CLASS, 'Session' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg', 'MplsLdp.DefaultVrf.Global_.Session', 
                [], [], 
                '''                LDP Session parameters
                ''',
                'session',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-ldp-cfg',
            'global',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-ldp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg'
        ),
    },
    'MplsLdp.DefaultVrf.Interfaces.Interface.Afs.Af.Discovery.TransportAddress' : {
        'meta_info' : _MetaInfoClass('MplsLdp.DefaultVrf.Interfaces.Interface.Afs.Af.Discovery.TransportAddress',
            False, 
            [
            _MetaInfoClassMember('address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                IP address
                ''',
                'address',
                'Cisco-IOS-XR-mpls-ldp-cfg', False, [
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP address
                        ''',
                        'address',
                        'Cisco-IOS-XR-mpls-ldp-cfg', False),
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP address
                        ''',
                        'address',
                        'Cisco-IOS-XR-mpls-ldp-cfg', False),
                ]),
            _MetaInfoClassMember('address-type', REFERENCE_ENUM_CLASS, 'MplsLdpTransportAddressEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg', 'MplsLdpTransportAddressEnum', 
                [], [], 
                '''                Transport address option
                ''',
                'address_type',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-ldp-cfg',
            'transport-address',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-ldp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg'
        ),
    },
    'MplsLdp.DefaultVrf.Interfaces.Interface.Afs.Af.Discovery' : {
        'meta_info' : _MetaInfoClass('MplsLdp.DefaultVrf.Interfaces.Interface.Afs.Af.Discovery',
            False, 
            [
            _MetaInfoClassMember('transport-address', REFERENCE_CLASS, 'TransportAddress' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg', 'MplsLdp.DefaultVrf.Interfaces.Interface.Afs.Af.Discovery.TransportAddress', 
                [], [], 
                '''                MPLS LDP configuration for interface
                discovery transportaddress.
                ''',
                'transport_address',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-ldp-cfg',
            'discovery',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-ldp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg'
        ),
    },
    'MplsLdp.DefaultVrf.Interfaces.Interface.Afs.Af.Igp' : {
        'meta_info' : _MetaInfoClass('MplsLdp.DefaultVrf.Interfaces.Interface.Afs.Af.Igp',
            False, 
            [
            _MetaInfoClassMember('disable-auto-config', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Disable IGP Auto-config on this interface
                ''',
                'disable_auto_config',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-ldp-cfg',
            'igp',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-ldp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg'
        ),
    },
    'MplsLdp.DefaultVrf.Interfaces.Interface.Afs.Af.Mldp' : {
        'meta_info' : _MetaInfoClass('MplsLdp.DefaultVrf.Interfaces.Interface.Afs.Af.Mldp',
            False, 
            [
            _MetaInfoClassMember('disable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Disable mLDP on LDP enabled interface
                ''',
                'disable',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-ldp-cfg',
            'mldp',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-ldp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg'
        ),
    },
    'MplsLdp.DefaultVrf.Interfaces.Interface.Afs.Af' : {
        'meta_info' : _MetaInfoClass('MplsLdp.DefaultVrf.Interfaces.Interface.Afs.Af',
            False, 
            [
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'MplsLdpafNameEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg', 'MplsLdpafNameEnum', 
                [], [], 
                '''                Address Family name
                ''',
                'af_name',
                'Cisco-IOS-XR-mpls-ldp-cfg', True),
            _MetaInfoClassMember('discovery', REFERENCE_CLASS, 'Discovery' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg', 'MplsLdp.DefaultVrf.Interfaces.Interface.Afs.Af.Discovery', 
                [], [], 
                '''                Configure interface discovery parameters
                ''',
                'discovery',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable Address Family
                ''',
                'enable',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            _MetaInfoClassMember('igp', REFERENCE_CLASS, 'Igp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg', 'MplsLdp.DefaultVrf.Interfaces.Interface.Afs.Af.Igp', 
                [], [], 
                '''                LDP interface IGP configuration
                ''',
                'igp',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            _MetaInfoClassMember('mldp', REFERENCE_CLASS, 'Mldp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg', 'MplsLdp.DefaultVrf.Interfaces.Interface.Afs.Af.Mldp', 
                [], [], 
                '''                Interface configuration parameters for mLDP
                ''',
                'mldp',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-ldp-cfg',
            'af',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-ldp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg'
        ),
    },
    'MplsLdp.DefaultVrf.Interfaces.Interface.Afs' : {
        'meta_info' : _MetaInfoClass('MplsLdp.DefaultVrf.Interfaces.Interface.Afs',
            False, 
            [
            _MetaInfoClassMember('af', REFERENCE_LIST, 'Af' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg', 'MplsLdp.DefaultVrf.Interfaces.Interface.Afs.Af', 
                [], [], 
                '''                Configure data for given Address Family
                ''',
                'af',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-ldp-cfg',
            'afs',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-ldp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg'
        ),
    },
    'MplsLdp.DefaultVrf.Interfaces.Interface.Global_.Discovery.LinkHello' : {
        'meta_info' : _MetaInfoClass('MplsLdp.DefaultVrf.Interfaces.Interface.Global_.Discovery.LinkHello',
            False, 
            [
            _MetaInfoClassMember('dual-stack', REFERENCE_ENUM_CLASS, 'MplsLdpafNameEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg', 'MplsLdpafNameEnum', 
                [], [], 
                '''                Dual Stack Address Family Preference
                ''',
                'dual_stack',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            _MetaInfoClassMember('hold-time', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                Time (seconds) - 65535 implies infinite
                ''',
                'hold_time',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            _MetaInfoClassMember('interval', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                Link Hello interval
                ''',
                'interval',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-ldp-cfg',
            'link-hello',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-ldp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg'
        ),
    },
    'MplsLdp.DefaultVrf.Interfaces.Interface.Global_.Discovery' : {
        'meta_info' : _MetaInfoClass('MplsLdp.DefaultVrf.Interfaces.Interface.Global_.Discovery',
            False, 
            [
            _MetaInfoClassMember('disable-quick-start', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Disable discovery's quick start mode
                ''',
                'disable_quick_start',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            _MetaInfoClassMember('link-hello', REFERENCE_CLASS, 'LinkHello' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg', 'MplsLdp.DefaultVrf.Interfaces.Interface.Global_.Discovery.LinkHello', 
                [], [], 
                '''                LDP Link Hellos
                ''',
                'link_hello',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-ldp-cfg',
            'discovery',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-ldp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg'
        ),
    },
    'MplsLdp.DefaultVrf.Interfaces.Interface.Global_.Igp.Sync.Delay.OnSessionUp' : {
        'meta_info' : _MetaInfoClass('MplsLdp.DefaultVrf.Interfaces.Interface.Global_.Igp.Sync.Delay.OnSessionUp',
            False, 
            [
            _MetaInfoClassMember('disable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Disable delay after session up
                ''',
                'disable',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            _MetaInfoClassMember('timeout', ATTRIBUTE, 'int' , None, None, 
                [('5', '300')], [], 
                '''                Time (seconds)
                ''',
                'timeout',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-ldp-cfg',
            'on-session-up',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-ldp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg'
        ),
    },
    'MplsLdp.DefaultVrf.Interfaces.Interface.Global_.Igp.Sync.Delay' : {
        'meta_info' : _MetaInfoClass('MplsLdp.DefaultVrf.Interfaces.Interface.Global_.Igp.Sync.Delay',
            False, 
            [
            _MetaInfoClassMember('on-session-up', REFERENCE_CLASS, 'OnSessionUp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg', 'MplsLdp.DefaultVrf.Interfaces.Interface.Global_.Igp.Sync.Delay.OnSessionUp', 
                [], [], 
                '''                Interface sync up delay after session up
                ''',
                'on_session_up',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-ldp-cfg',
            'delay',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-ldp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg'
        ),
    },
    'MplsLdp.DefaultVrf.Interfaces.Interface.Global_.Igp.Sync' : {
        'meta_info' : _MetaInfoClass('MplsLdp.DefaultVrf.Interfaces.Interface.Global_.Igp.Sync',
            False, 
            [
            _MetaInfoClassMember('delay', REFERENCE_CLASS, 'Delay' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg', 'MplsLdp.DefaultVrf.Interfaces.Interface.Global_.Igp.Sync.Delay', 
                [], [], 
                '''                LDP IGP synchronization delay time
                ''',
                'delay',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-ldp-cfg',
            'sync',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-ldp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg'
        ),
    },
    'MplsLdp.DefaultVrf.Interfaces.Interface.Global_.Igp' : {
        'meta_info' : _MetaInfoClass('MplsLdp.DefaultVrf.Interfaces.Interface.Global_.Igp',
            False, 
            [
            _MetaInfoClassMember('sync', REFERENCE_CLASS, 'Sync' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg', 'MplsLdp.DefaultVrf.Interfaces.Interface.Global_.Igp.Sync', 
                [], [], 
                '''                LDP IGP synchronization
                ''',
                'sync',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-ldp-cfg',
            'igp',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-ldp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg'
        ),
    },
    'MplsLdp.DefaultVrf.Interfaces.Interface.Global_' : {
        'meta_info' : _MetaInfoClass('MplsLdp.DefaultVrf.Interfaces.Interface.Global_',
            False, 
            [
            _MetaInfoClassMember('discovery', REFERENCE_CLASS, 'Discovery' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg', 'MplsLdp.DefaultVrf.Interfaces.Interface.Global_.Discovery', 
                [], [], 
                '''                Configure interface discovery parameters
                ''',
                'discovery',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            _MetaInfoClassMember('igp', REFERENCE_CLASS, 'Igp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg', 'MplsLdp.DefaultVrf.Interfaces.Interface.Global_.Igp', 
                [], [], 
                '''                LDP IGP configuration
                ''',
                'igp',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-ldp-cfg',
            'global',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-ldp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg'
        ),
    },
    'MplsLdp.DefaultVrf.Interfaces.Interface' : {
        'meta_info' : _MetaInfoClass('MplsLdp.DefaultVrf.Interfaces.Interface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Name of interface
                ''',
                'interface_name',
                'Cisco-IOS-XR-mpls-ldp-cfg', True),
            _MetaInfoClassMember('afs', REFERENCE_CLASS, 'Afs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg', 'MplsLdp.DefaultVrf.Interfaces.Interface.Afs', 
                [], [], 
                '''                Address Family specific configuration for
                MPLS LDP intf
                ''',
                'afs',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable Label Distribution Protocol (LDP) on
                thisinterface
                ''',
                'enable',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            _MetaInfoClassMember('global', REFERENCE_CLASS, 'Global_' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg', 'MplsLdp.DefaultVrf.Interfaces.Interface.Global_', 
                [], [], 
                '''                Per VRF interface Global configuration for
                MPLS LDP
                ''',
                'global_',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-ldp-cfg',
            'interface',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-ldp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg'
        ),
    },
    'MplsLdp.DefaultVrf.Interfaces' : {
        'meta_info' : _MetaInfoClass('MplsLdp.DefaultVrf.Interfaces',
            False, 
            [
            _MetaInfoClassMember('interface', REFERENCE_LIST, 'Interface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg', 'MplsLdp.DefaultVrf.Interfaces.Interface', 
                [], [], 
                '''                MPLS LDP configuration for a particular
                interface
                ''',
                'interface',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-ldp-cfg',
            'interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-ldp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg'
        ),
    },
    'MplsLdp.DefaultVrf' : {
        'meta_info' : _MetaInfoClass('MplsLdp.DefaultVrf',
            False, 
            [
            _MetaInfoClassMember('afs', REFERENCE_CLASS, 'Afs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg', 'MplsLdp.DefaultVrf.Afs', 
                [], [], 
                '''                Address Family specific configuration for MPLS
                LDP
                ''',
                'afs',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            _MetaInfoClassMember('global', REFERENCE_CLASS, 'Global_' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg', 'MplsLdp.DefaultVrf.Global_', 
                [], [], 
                '''                Default VRF Global configuration for MPLS LDP
                ''',
                'global_',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            _MetaInfoClassMember('interfaces', REFERENCE_CLASS, 'Interfaces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg', 'MplsLdp.DefaultVrf.Interfaces', 
                [], [], 
                '''                MPLS LDP configuration pertaining to interfaces
                ''',
                'interfaces',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-ldp-cfg',
            'default-vrf',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-ldp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg'
        ),
    },
    'MplsLdp.Vrfs.Vrf.Global_.Session.DownstreamOnDemand' : {
        'meta_info' : _MetaInfoClass('MplsLdp.Vrfs.Vrf.Global_.Session.DownstreamOnDemand',
            False, 
            [
            _MetaInfoClassMember('peer-acl-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of peer ACL
                ''',
                'peer_acl_name',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            _MetaInfoClassMember('type', REFERENCE_ENUM_CLASS, 'MplsLdpDownstreamOnDemandEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg', 'MplsLdpDownstreamOnDemandEnum', 
                [], [], 
                '''                Downstream on demand type
                ''',
                'type',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-ldp-cfg',
            'downstream-on-demand',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-ldp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg'
        ),
    },
    'MplsLdp.Vrfs.Vrf.Global_.Session' : {
        'meta_info' : _MetaInfoClass('MplsLdp.Vrfs.Vrf.Global_.Session',
            False, 
            [
            _MetaInfoClassMember('downstream-on-demand', REFERENCE_CLASS, 'DownstreamOnDemand' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg', 'MplsLdp.Vrfs.Vrf.Global_.Session.DownstreamOnDemand', 
                [], [], 
                '''                ACL with the list of neighbors configured
                for Downstream on Demand
                ''',
                'downstream_on_demand',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-ldp-cfg',
            'session',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-ldp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg'
        ),
    },
    'MplsLdp.Vrfs.Vrf.Global_.Neighbor.LdpIds.LdpId.Password' : {
        'meta_info' : _MetaInfoClass('MplsLdp.Vrfs.Vrf.Global_.Neighbor.LdpIds.LdpId.Password',
            False, 
            [
            _MetaInfoClassMember('command-type', REFERENCE_ENUM_CLASS, 'MplsLdpNbrPasswordEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg', 'MplsLdpNbrPasswordEnum', 
                [], [], 
                '''                Command type for password configuration
                ''',
                'command_type',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            _MetaInfoClassMember('password', ATTRIBUTE, 'str' , None, None, 
                [], [b'(!.+)|([^!].+)'], 
                '''                The neighbor password
                ''',
                'password',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-ldp-cfg',
            'password',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-ldp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg'
        ),
    },
    'MplsLdp.Vrfs.Vrf.Global_.Neighbor.LdpIds.LdpId' : {
        'meta_info' : _MetaInfoClass('MplsLdp.Vrfs.Vrf.Global_.Neighbor.LdpIds.LdpId',
            False, 
            [
            _MetaInfoClassMember('lsr-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                LSR ID of neighbor
                ''',
                'lsr_id',
                'Cisco-IOS-XR-mpls-ldp-cfg', True),
            _MetaInfoClassMember('label-space-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Label space ID of neighbor
                ''',
                'label_space_id',
                'Cisco-IOS-XR-mpls-ldp-cfg', True),
            _MetaInfoClassMember('password', REFERENCE_CLASS, 'Password' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg', 'MplsLdp.Vrfs.Vrf.Global_.Neighbor.LdpIds.LdpId.Password', 
                [], [], 
                '''                Password for MD5 authentication for this
                neighbor
                ''',
                'password',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-ldp-cfg',
            'ldp-id',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-ldp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg'
        ),
    },
    'MplsLdp.Vrfs.Vrf.Global_.Neighbor.LdpIds' : {
        'meta_info' : _MetaInfoClass('MplsLdp.Vrfs.Vrf.Global_.Neighbor.LdpIds',
            False, 
            [
            _MetaInfoClassMember('ldp-id', REFERENCE_LIST, 'LdpId' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg', 'MplsLdp.Vrfs.Vrf.Global_.Neighbor.LdpIds.LdpId', 
                [], [], 
                '''                LDP ID based configuration related to a
                neigbor
                ''',
                'ldp_id',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-ldp-cfg',
            'ldp-ids',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-ldp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg'
        ),
    },
    'MplsLdp.Vrfs.Vrf.Global_.Neighbor' : {
        'meta_info' : _MetaInfoClass('MplsLdp.Vrfs.Vrf.Global_.Neighbor',
            False, 
            [
            _MetaInfoClassMember('ldp-ids', REFERENCE_CLASS, 'LdpIds' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg', 'MplsLdp.Vrfs.Vrf.Global_.Neighbor.LdpIds', 
                [], [], 
                '''                Configuration related to Neighbors using LDP
                Id
                ''',
                'ldp_ids',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            _MetaInfoClassMember('password', ATTRIBUTE, 'str' , None, None, 
                [], [b'(!.+)|([^!].+)'], 
                '''                Default password for all neigbors
                ''',
                'password',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-ldp-cfg',
            'neighbor',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-ldp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg'
        ),
    },
    'MplsLdp.Vrfs.Vrf.Global_.GracefulRestart.HelperPeer' : {
        'meta_info' : _MetaInfoClass('MplsLdp.Vrfs.Vrf.Global_.GracefulRestart.HelperPeer',
            False, 
            [
            _MetaInfoClassMember('maintain-on-local-reset', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Maintain the state of a GR peer upon a
                local reset
                ''',
                'maintain_on_local_reset',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-ldp-cfg',
            'helper-peer',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-ldp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg'
        ),
    },
    'MplsLdp.Vrfs.Vrf.Global_.GracefulRestart' : {
        'meta_info' : _MetaInfoClass('MplsLdp.Vrfs.Vrf.Global_.GracefulRestart',
            False, 
            [
            _MetaInfoClassMember('helper-peer', REFERENCE_CLASS, 'HelperPeer' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg', 'MplsLdp.Vrfs.Vrf.Global_.GracefulRestart.HelperPeer', 
                [], [], 
                '''                Configure parameters related to GR peer(s)
                opearating in helper mode
                ''',
                'helper_peer',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-ldp-cfg',
            'graceful-restart',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-ldp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg'
        ),
    },
    'MplsLdp.Vrfs.Vrf.Global_' : {
        'meta_info' : _MetaInfoClass('MplsLdp.Vrfs.Vrf.Global_',
            False, 
            [
            _MetaInfoClassMember('graceful-restart', REFERENCE_CLASS, 'GracefulRestart' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg', 'MplsLdp.Vrfs.Vrf.Global_.GracefulRestart', 
                [], [], 
                '''                Configuration for per-VRF LDP Graceful
                Restart parameters
                ''',
                'graceful_restart',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            _MetaInfoClassMember('neighbor', REFERENCE_CLASS, 'Neighbor' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg', 'MplsLdp.Vrfs.Vrf.Global_.Neighbor', 
                [], [], 
                '''                Configuration related to Neighbors
                ''',
                'neighbor',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            _MetaInfoClassMember('router-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Configuration for LDP Router ID (LDP ID)
                ''',
                'router_id',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            _MetaInfoClassMember('session', REFERENCE_CLASS, 'Session' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg', 'MplsLdp.Vrfs.Vrf.Global_.Session', 
                [], [], 
                '''                LDP Session parameters
                ''',
                'session',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-ldp-cfg',
            'global',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-ldp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg'
        ),
    },
    'MplsLdp.Vrfs.Vrf.Afs.Af.Discovery' : {
        'meta_info' : _MetaInfoClass('MplsLdp.Vrfs.Vrf.Afs.Af.Discovery',
            False, 
            [
            _MetaInfoClassMember('transport-address', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Global discovery transport address for
                address family
                ''',
                'transport_address',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-ldp-cfg',
            'discovery',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-ldp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg'
        ),
    },
    'MplsLdp.Vrfs.Vrf.Afs.Af.Label.Remote.Accept.PeerAcceptPolicies.PeerAcceptPolicy.PeerAcceptPolicyData' : {
        'meta_info' : _MetaInfoClass('MplsLdp.Vrfs.Vrf.Afs.Af.Label.Remote.Accept.PeerAcceptPolicies.PeerAcceptPolicy.PeerAcceptPolicyData',
            False, 
            [
            _MetaInfoClassMember('prefix-acl-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of prefix ACL
                ''',
                'prefix_acl_name',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-ldp-cfg',
            'peer-accept-policy-data',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-ldp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg'
        ),
    },
    'MplsLdp.Vrfs.Vrf.Afs.Af.Label.Remote.Accept.PeerAcceptPolicies.PeerAcceptPolicy.LsrId' : {
        'meta_info' : _MetaInfoClass('MplsLdp.Vrfs.Vrf.Afs.Af.Label.Remote.Accept.PeerAcceptPolicies.PeerAcceptPolicy.LsrId',
            False, 
            [
            _MetaInfoClassMember('lsr-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                LSR ID of neighbor
                ''',
                'lsr_id',
                'Cisco-IOS-XR-mpls-ldp-cfg', True),
            _MetaInfoClassMember('prefix-acl-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of prefix ACL
                ''',
                'prefix_acl_name',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-ldp-cfg',
            'lsr-id',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-ldp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg'
        ),
    },
    'MplsLdp.Vrfs.Vrf.Afs.Af.Label.Remote.Accept.PeerAcceptPolicies.PeerAcceptPolicy' : {
        'meta_info' : _MetaInfoClass('MplsLdp.Vrfs.Vrf.Afs.Af.Label.Remote.Accept.PeerAcceptPolicies.PeerAcceptPolicy',
            False, 
            [
            _MetaInfoClassMember('label-space-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Label space ID of neighbor
                ''',
                'label_space_id',
                'Cisco-IOS-XR-mpls-ldp-cfg', True),
            _MetaInfoClassMember('lsr-id', REFERENCE_LIST, 'LsrId' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg', 'MplsLdp.Vrfs.Vrf.Afs.Af.Label.Remote.Accept.PeerAcceptPolicies.PeerAcceptPolicy.LsrId', 
                [], [], 
                '''                keys: lsr-id
                ''',
                'lsr_id',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            _MetaInfoClassMember('peer-accept-policy-data', REFERENCE_CLASS, 'PeerAcceptPolicyData' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg', 'MplsLdp.Vrfs.Vrf.Afs.Af.Label.Remote.Accept.PeerAcceptPolicies.PeerAcceptPolicy.PeerAcceptPolicyData', 
                [], [], 
                '''                Data container.
                ''',
                'peer_accept_policy_data',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-ldp-cfg',
            'peer-accept-policy',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-ldp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg'
        ),
    },
    'MplsLdp.Vrfs.Vrf.Afs.Af.Label.Remote.Accept.PeerAcceptPolicies' : {
        'meta_info' : _MetaInfoClass('MplsLdp.Vrfs.Vrf.Afs.Af.Label.Remote.Accept.PeerAcceptPolicies',
            False, 
            [
            _MetaInfoClassMember('peer-accept-policy', REFERENCE_LIST, 'PeerAcceptPolicy' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg', 'MplsLdp.Vrfs.Vrf.Afs.Af.Label.Remote.Accept.PeerAcceptPolicies.PeerAcceptPolicy', 
                [], [], 
                '''                Control acceptasnce of labels from a
                neighbor for prefix(es) using ACL
                ''',
                'peer_accept_policy',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-ldp-cfg',
            'peer-accept-policies',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-ldp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg'
        ),
    },
    'MplsLdp.Vrfs.Vrf.Afs.Af.Label.Remote.Accept' : {
        'meta_info' : _MetaInfoClass('MplsLdp.Vrfs.Vrf.Afs.Af.Label.Remote.Accept',
            False, 
            [
            _MetaInfoClassMember('peer-accept-policies', REFERENCE_CLASS, 'PeerAcceptPolicies' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg', 'MplsLdp.Vrfs.Vrf.Afs.Af.Label.Remote.Accept.PeerAcceptPolicies', 
                [], [], 
                '''                Configuration related to Neighbors for
                inbound label acceptance
                ''',
                'peer_accept_policies',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-ldp-cfg',
            'accept',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-ldp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg'
        ),
    },
    'MplsLdp.Vrfs.Vrf.Afs.Af.Label.Remote' : {
        'meta_info' : _MetaInfoClass('MplsLdp.Vrfs.Vrf.Afs.Af.Label.Remote',
            False, 
            [
            _MetaInfoClassMember('accept', REFERENCE_CLASS, 'Accept' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg', 'MplsLdp.Vrfs.Vrf.Afs.Af.Label.Remote.Accept', 
                [], [], 
                '''                Configure inbound label acceptance
                ''',
                'accept',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-ldp-cfg',
            'remote',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-ldp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg'
        ),
    },
    'MplsLdp.Vrfs.Vrf.Afs.Af.Label.Local.Advertise.PeerAdvertisePolicies.PeerAdvertisePolicy.PeerAdvertisePolicyData' : {
        'meta_info' : _MetaInfoClass('MplsLdp.Vrfs.Vrf.Afs.Af.Label.Local.Advertise.PeerAdvertisePolicies.PeerAdvertisePolicy.PeerAdvertisePolicyData',
            False, 
            [
            _MetaInfoClassMember('prefix-acl-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of prefix ACL
                ''',
                'prefix_acl_name',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-ldp-cfg',
            'peer-advertise-policy-data',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-ldp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg'
        ),
    },
    'MplsLdp.Vrfs.Vrf.Afs.Af.Label.Local.Advertise.PeerAdvertisePolicies.PeerAdvertisePolicy.LsrId' : {
        'meta_info' : _MetaInfoClass('MplsLdp.Vrfs.Vrf.Afs.Af.Label.Local.Advertise.PeerAdvertisePolicies.PeerAdvertisePolicy.LsrId',
            False, 
            [
            _MetaInfoClassMember('lsr-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                LSR ID of neighbor
                ''',
                'lsr_id',
                'Cisco-IOS-XR-mpls-ldp-cfg', True),
            _MetaInfoClassMember('prefix-acl-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of prefix ACL
                ''',
                'prefix_acl_name',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-ldp-cfg',
            'lsr-id',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-ldp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg'
        ),
    },
    'MplsLdp.Vrfs.Vrf.Afs.Af.Label.Local.Advertise.PeerAdvertisePolicies.PeerAdvertisePolicy' : {
        'meta_info' : _MetaInfoClass('MplsLdp.Vrfs.Vrf.Afs.Af.Label.Local.Advertise.PeerAdvertisePolicies.PeerAdvertisePolicy',
            False, 
            [
            _MetaInfoClassMember('label-space-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Label space ID of neighbor
                ''',
                'label_space_id',
                'Cisco-IOS-XR-mpls-ldp-cfg', True),
            _MetaInfoClassMember('lsr-id', REFERENCE_LIST, 'LsrId' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg', 'MplsLdp.Vrfs.Vrf.Afs.Af.Label.Local.Advertise.PeerAdvertisePolicies.PeerAdvertisePolicy.LsrId', 
                [], [], 
                '''                keys: lsr-id
                ''',
                'lsr_id',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            _MetaInfoClassMember('peer-advertise-policy-data', REFERENCE_CLASS, 'PeerAdvertisePolicyData' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg', 'MplsLdp.Vrfs.Vrf.Afs.Af.Label.Local.Advertise.PeerAdvertisePolicies.PeerAdvertisePolicy.PeerAdvertisePolicyData', 
                [], [], 
                '''                Data container.
                ''',
                'peer_advertise_policy_data',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-ldp-cfg',
            'peer-advertise-policy',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-ldp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg'
        ),
    },
    'MplsLdp.Vrfs.Vrf.Afs.Af.Label.Local.Advertise.PeerAdvertisePolicies' : {
        'meta_info' : _MetaInfoClass('MplsLdp.Vrfs.Vrf.Afs.Af.Label.Local.Advertise.PeerAdvertisePolicies',
            False, 
            [
            _MetaInfoClassMember('peer-advertise-policy', REFERENCE_LIST, 'PeerAdvertisePolicy' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg', 'MplsLdp.Vrfs.Vrf.Afs.Af.Label.Local.Advertise.PeerAdvertisePolicies.PeerAdvertisePolicy', 
                [], [], 
                '''                Control advertisement of prefix(es)
                using ACL
                ''',
                'peer_advertise_policy',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-ldp-cfg',
            'peer-advertise-policies',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-ldp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg'
        ),
    },
    'MplsLdp.Vrfs.Vrf.Afs.Af.Label.Local.Advertise.Interfaces.Interface' : {
        'meta_info' : _MetaInfoClass('MplsLdp.Vrfs.Vrf.Afs.Af.Label.Local.Advertise.Interfaces.Interface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Name of interface
                ''',
                'interface_name',
                'Cisco-IOS-XR-mpls-ldp-cfg', True),
            ],
            'Cisco-IOS-XR-mpls-ldp-cfg',
            'interface',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-ldp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg'
        ),
    },
    'MplsLdp.Vrfs.Vrf.Afs.Af.Label.Local.Advertise.Interfaces' : {
        'meta_info' : _MetaInfoClass('MplsLdp.Vrfs.Vrf.Afs.Af.Label.Local.Advertise.Interfaces',
            False, 
            [
            _MetaInfoClassMember('interface', REFERENCE_LIST, 'Interface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg', 'MplsLdp.Vrfs.Vrf.Afs.Af.Label.Local.Advertise.Interfaces.Interface', 
                [], [], 
                '''                Control advertisement of interface's
                host IP address
                ''',
                'interface',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-ldp-cfg',
            'interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-ldp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg'
        ),
    },
    'MplsLdp.Vrfs.Vrf.Afs.Af.Label.Local.Advertise.ExplicitNull' : {
        'meta_info' : _MetaInfoClass('MplsLdp.Vrfs.Vrf.Afs.Af.Label.Local.Advertise.ExplicitNull',
            False, 
            [
            _MetaInfoClassMember('explicit-null-type', REFERENCE_ENUM_CLASS, 'MplsLdpExpNullEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg', 'MplsLdpExpNullEnum', 
                [], [], 
                '''                Explicit Null command variant
                ''',
                'explicit_null_type',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            _MetaInfoClassMember('peer-acl-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of peer ACL
                ''',
                'peer_acl_name',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            _MetaInfoClassMember('prefix-acl-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of prefix ACL
                ''',
                'prefix_acl_name',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-ldp-cfg',
            'explicit-null',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-ldp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg'
        ),
    },
    'MplsLdp.Vrfs.Vrf.Afs.Af.Label.Local.Advertise' : {
        'meta_info' : _MetaInfoClass('MplsLdp.Vrfs.Vrf.Afs.Af.Label.Local.Advertise',
            False, 
            [
            _MetaInfoClassMember('disable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Disable label advertisement
                ''',
                'disable',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            _MetaInfoClassMember('explicit-null', REFERENCE_CLASS, 'ExplicitNull' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg', 'MplsLdp.Vrfs.Vrf.Afs.Af.Label.Local.Advertise.ExplicitNull', 
                [], [], 
                '''                Configure advertisment of explicit-null
                for connected prefixes.
                ''',
                'explicit_null',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            _MetaInfoClassMember('interfaces', REFERENCE_CLASS, 'Interfaces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg', 'MplsLdp.Vrfs.Vrf.Afs.Af.Label.Local.Advertise.Interfaces', 
                [], [], 
                '''                Configure outbound label advertisement
                for an interface
                ''',
                'interfaces',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            _MetaInfoClassMember('peer-advertise-policies', REFERENCE_CLASS, 'PeerAdvertisePolicies' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg', 'MplsLdp.Vrfs.Vrf.Afs.Af.Label.Local.Advertise.PeerAdvertisePolicies', 
                [], [], 
                '''                Configure peer centric outbound label
                advertisement using ACL
                ''',
                'peer_advertise_policies',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-ldp-cfg',
            'advertise',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-ldp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg'
        ),
    },
    'MplsLdp.Vrfs.Vrf.Afs.Af.Label.Local.Allocate' : {
        'meta_info' : _MetaInfoClass('MplsLdp.Vrfs.Vrf.Afs.Af.Label.Local.Allocate',
            False, 
            [
            _MetaInfoClassMember('allocation-type', REFERENCE_ENUM_CLASS, 'MplsLdpLabelAllocationEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg', 'MplsLdpLabelAllocationEnum', 
                [], [], 
                '''                Label allocation type
                ''',
                'allocation_type',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            _MetaInfoClassMember('prefix-acl-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of prefix ACL
                ''',
                'prefix_acl_name',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-ldp-cfg',
            'allocate',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-ldp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg'
        ),
    },
    'MplsLdp.Vrfs.Vrf.Afs.Af.Label.Local' : {
        'meta_info' : _MetaInfoClass('MplsLdp.Vrfs.Vrf.Afs.Af.Label.Local',
            False, 
            [
            _MetaInfoClassMember('advertise', REFERENCE_CLASS, 'Advertise' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg', 'MplsLdp.Vrfs.Vrf.Afs.Af.Label.Local.Advertise', 
                [], [], 
                '''                Configure outbound label advertisement
                ''',
                'advertise',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            _MetaInfoClassMember('allocate', REFERENCE_CLASS, 'Allocate' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg', 'MplsLdp.Vrfs.Vrf.Afs.Af.Label.Local.Allocate', 
                [], [], 
                '''                Control local label allocation for
                prefix(es)
                ''',
                'allocate',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            _MetaInfoClassMember('default-route', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable MPLS forwarding for default route
                ''',
                'default_route',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            _MetaInfoClassMember('implicit-null-override', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Control use of implicit-null label for set
                of prefix(es)
                ''',
                'implicit_null_override',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-ldp-cfg',
            'local',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-ldp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg'
        ),
    },
    'MplsLdp.Vrfs.Vrf.Afs.Af.Label' : {
        'meta_info' : _MetaInfoClass('MplsLdp.Vrfs.Vrf.Afs.Af.Label',
            False, 
            [
            _MetaInfoClassMember('local', REFERENCE_CLASS, 'Local' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg', 'MplsLdp.Vrfs.Vrf.Afs.Af.Label.Local', 
                [], [], 
                '''                Configure local label policies and control
                ''',
                'local',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            _MetaInfoClassMember('remote', REFERENCE_CLASS, 'Remote' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg', 'MplsLdp.Vrfs.Vrf.Afs.Af.Label.Remote', 
                [], [], 
                '''                Configure remote/peer label policies and
                control
                ''',
                'remote',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-ldp-cfg',
            'label',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-ldp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg'
        ),
    },
    'MplsLdp.Vrfs.Vrf.Afs.Af' : {
        'meta_info' : _MetaInfoClass('MplsLdp.Vrfs.Vrf.Afs.Af',
            False, 
            [
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'MplsLdpafNameEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg', 'MplsLdpafNameEnum', 
                [], [], 
                '''                Address Family name
                ''',
                'af_name',
                'Cisco-IOS-XR-mpls-ldp-cfg', True),
            _MetaInfoClassMember('discovery', REFERENCE_CLASS, 'Discovery' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg', 'MplsLdp.Vrfs.Vrf.Afs.Af.Discovery', 
                [], [], 
                '''                Configure Discovery parameters
                ''',
                'discovery',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable Address Family
                ''',
                'enable',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            _MetaInfoClassMember('label', REFERENCE_CLASS, 'Label' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg', 'MplsLdp.Vrfs.Vrf.Afs.Af.Label', 
                [], [], 
                '''                Configure Label policies and control
                ''',
                'label',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-ldp-cfg',
            'af',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-ldp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg'
        ),
    },
    'MplsLdp.Vrfs.Vrf.Afs' : {
        'meta_info' : _MetaInfoClass('MplsLdp.Vrfs.Vrf.Afs',
            False, 
            [
            _MetaInfoClassMember('af', REFERENCE_LIST, 'Af' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg', 'MplsLdp.Vrfs.Vrf.Afs.Af', 
                [], [], 
                '''                Configure data for given Address Family
                ''',
                'af',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-ldp-cfg',
            'afs',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-ldp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg'
        ),
    },
    'MplsLdp.Vrfs.Vrf.Interfaces.Interface.Afs.Af.Discovery.TransportAddress' : {
        'meta_info' : _MetaInfoClass('MplsLdp.Vrfs.Vrf.Interfaces.Interface.Afs.Af.Discovery.TransportAddress',
            False, 
            [
            _MetaInfoClassMember('address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                IP address
                ''',
                'address',
                'Cisco-IOS-XR-mpls-ldp-cfg', False, [
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP address
                        ''',
                        'address',
                        'Cisco-IOS-XR-mpls-ldp-cfg', False),
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP address
                        ''',
                        'address',
                        'Cisco-IOS-XR-mpls-ldp-cfg', False),
                ]),
            _MetaInfoClassMember('address-type', REFERENCE_ENUM_CLASS, 'MplsLdpTransportAddressEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg', 'MplsLdpTransportAddressEnum', 
                [], [], 
                '''                Transport address option
                ''',
                'address_type',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-ldp-cfg',
            'transport-address',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-ldp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg'
        ),
    },
    'MplsLdp.Vrfs.Vrf.Interfaces.Interface.Afs.Af.Discovery' : {
        'meta_info' : _MetaInfoClass('MplsLdp.Vrfs.Vrf.Interfaces.Interface.Afs.Af.Discovery',
            False, 
            [
            _MetaInfoClassMember('transport-address', REFERENCE_CLASS, 'TransportAddress' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg', 'MplsLdp.Vrfs.Vrf.Interfaces.Interface.Afs.Af.Discovery.TransportAddress', 
                [], [], 
                '''                MPLS LDP configuration for interface
                discovery transportaddress.
                ''',
                'transport_address',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-ldp-cfg',
            'discovery',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-ldp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg'
        ),
    },
    'MplsLdp.Vrfs.Vrf.Interfaces.Interface.Afs.Af' : {
        'meta_info' : _MetaInfoClass('MplsLdp.Vrfs.Vrf.Interfaces.Interface.Afs.Af',
            False, 
            [
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'MplsLdpafNameEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg', 'MplsLdpafNameEnum', 
                [], [], 
                '''                Address Family name
                ''',
                'af_name',
                'Cisco-IOS-XR-mpls-ldp-cfg', True),
            _MetaInfoClassMember('discovery', REFERENCE_CLASS, 'Discovery' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg', 'MplsLdp.Vrfs.Vrf.Interfaces.Interface.Afs.Af.Discovery', 
                [], [], 
                '''                Configure interface discovery parameters
                ''',
                'discovery',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable Address Family
                ''',
                'enable',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-ldp-cfg',
            'af',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-ldp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg'
        ),
    },
    'MplsLdp.Vrfs.Vrf.Interfaces.Interface.Afs' : {
        'meta_info' : _MetaInfoClass('MplsLdp.Vrfs.Vrf.Interfaces.Interface.Afs',
            False, 
            [
            _MetaInfoClassMember('af', REFERENCE_LIST, 'Af' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg', 'MplsLdp.Vrfs.Vrf.Interfaces.Interface.Afs.Af', 
                [], [], 
                '''                Configure data for given Address Family
                ''',
                'af',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-ldp-cfg',
            'afs',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-ldp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg'
        ),
    },
    'MplsLdp.Vrfs.Vrf.Interfaces.Interface' : {
        'meta_info' : _MetaInfoClass('MplsLdp.Vrfs.Vrf.Interfaces.Interface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Name of interface
                ''',
                'interface_name',
                'Cisco-IOS-XR-mpls-ldp-cfg', True),
            _MetaInfoClassMember('afs', REFERENCE_CLASS, 'Afs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg', 'MplsLdp.Vrfs.Vrf.Interfaces.Interface.Afs', 
                [], [], 
                '''                Address Family specific configuration for
                MPLS LDP vrf intf
                ''',
                'afs',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable Label Distribution Protocol (LDP) on
                thisinterface
                ''',
                'enable',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-ldp-cfg',
            'interface',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-ldp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg'
        ),
    },
    'MplsLdp.Vrfs.Vrf.Interfaces' : {
        'meta_info' : _MetaInfoClass('MplsLdp.Vrfs.Vrf.Interfaces',
            False, 
            [
            _MetaInfoClassMember('interface', REFERENCE_LIST, 'Interface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg', 'MplsLdp.Vrfs.Vrf.Interfaces.Interface', 
                [], [], 
                '''                MPLS LDP configuration for a particular
                interface
                ''',
                'interface',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-ldp-cfg',
            'interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-ldp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg'
        ),
    },
    'MplsLdp.Vrfs.Vrf' : {
        'meta_info' : _MetaInfoClass('MplsLdp.Vrfs.Vrf',
            False, 
            [
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                VRF Name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-mpls-ldp-cfg', True),
            _MetaInfoClassMember('afs', REFERENCE_CLASS, 'Afs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg', 'MplsLdp.Vrfs.Vrf.Afs', 
                [], [], 
                '''                Address Family specific configuration for MPLS
                LDP vrf
                ''',
                'afs',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable VRF
                ''',
                'enable',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            _MetaInfoClassMember('global', REFERENCE_CLASS, 'Global_' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg', 'MplsLdp.Vrfs.Vrf.Global_', 
                [], [], 
                '''                Per VRF Global configuration for MPLS LDP
                ''',
                'global_',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            _MetaInfoClassMember('interfaces', REFERENCE_CLASS, 'Interfaces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg', 'MplsLdp.Vrfs.Vrf.Interfaces', 
                [], [], 
                '''                MPLS LDP configuration pertaining to
                interfaces
                ''',
                'interfaces',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-ldp-cfg',
            'vrf',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-ldp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg'
        ),
    },
    'MplsLdp.Vrfs' : {
        'meta_info' : _MetaInfoClass('MplsLdp.Vrfs',
            False, 
            [
            _MetaInfoClassMember('vrf', REFERENCE_LIST, 'Vrf' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg', 'MplsLdp.Vrfs.Vrf', 
                [], [], 
                '''                VRF attribute configuration for MPLS LDP
                ''',
                'vrf',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-ldp-cfg',
            'vrfs',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-ldp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg'
        ),
    },
    'MplsLdp.Global_.EntropyLabel' : {
        'meta_info' : _MetaInfoClass('MplsLdp.Global_.EntropyLabel',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                none
                ''',
                'enable',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-ldp-cfg',
            'entropy-label',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-ldp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg'
        ),
    },
    'MplsLdp.Global_.Session.BackoffTime' : {
        'meta_info' : _MetaInfoClass('MplsLdp.Global_.Session.BackoffTime',
            False, 
            [
            _MetaInfoClassMember('initial-backoff-time', ATTRIBUTE, 'int' , None, None, 
                [('5', '2147483')], [], 
                '''                Initial session backoff time (seconds)
                ''',
                'initial_backoff_time',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            _MetaInfoClassMember('max-backoff-time', ATTRIBUTE, 'int' , None, None, 
                [('5', '2147483')], [], 
                '''                Maximum session backoff time (seconds)
                ''',
                'max_backoff_time',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-ldp-cfg',
            'backoff-time',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-ldp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg'
        ),
    },
    'MplsLdp.Global_.Session' : {
        'meta_info' : _MetaInfoClass('MplsLdp.Global_.Session',
            False, 
            [
            _MetaInfoClassMember('backoff-time', REFERENCE_CLASS, 'BackoffTime' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg', 'MplsLdp.Global_.Session.BackoffTime', 
                [], [], 
                '''                Configure Session Backoff parameters
                ''',
                'backoff_time',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            _MetaInfoClassMember('hold-time', ATTRIBUTE, 'int' , None, None, 
                [('15', '65535')], [], 
                '''                LDP Session holdtime
                ''',
                'hold_time',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-ldp-cfg',
            'session',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-ldp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg'
        ),
    },
    'MplsLdp.Global_.Igp.Sync.Delay' : {
        'meta_info' : _MetaInfoClass('MplsLdp.Global_.Igp.Sync.Delay',
            False, 
            [
            _MetaInfoClassMember('on-proc-restart', ATTRIBUTE, 'int' , None, None, 
                [('60', '600')], [], 
                '''                Global sync up delay to be used after
                process restart
                ''',
                'on_proc_restart',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            _MetaInfoClassMember('on-session-up', ATTRIBUTE, 'int' , None, None, 
                [('5', '300')], [], 
                '''                Interface sync up delay after session up
                ''',
                'on_session_up',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-ldp-cfg',
            'delay',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-ldp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg'
        ),
    },
    'MplsLdp.Global_.Igp.Sync' : {
        'meta_info' : _MetaInfoClass('MplsLdp.Global_.Igp.Sync',
            False, 
            [
            _MetaInfoClassMember('delay', REFERENCE_CLASS, 'Delay' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg', 'MplsLdp.Global_.Igp.Sync.Delay', 
                [], [], 
                '''                LDP IGP synchronization delay time
                ''',
                'delay',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-ldp-cfg',
            'sync',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-ldp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg'
        ),
    },
    'MplsLdp.Global_.Igp' : {
        'meta_info' : _MetaInfoClass('MplsLdp.Global_.Igp',
            False, 
            [
            _MetaInfoClassMember('sync', REFERENCE_CLASS, 'Sync' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg', 'MplsLdp.Global_.Igp.Sync', 
                [], [], 
                '''                LDP IGP synchronization
                ''',
                'sync',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-ldp-cfg',
            'igp',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-ldp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg'
        ),
    },
    'MplsLdp.Global_.EnableLogging' : {
        'meta_info' : _MetaInfoClass('MplsLdp.Global_.EnableLogging',
            False, 
            [
            _MetaInfoClassMember('adjacency', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable logging of adjacency events
                ''',
                'adjacency',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            _MetaInfoClassMember('gr-session-changes', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable logging of Graceful Restart (GR) events
                ''',
                'gr_session_changes',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            _MetaInfoClassMember('neighbor-changes', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable logging of neighbor events
                ''',
                'neighbor_changes',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            _MetaInfoClassMember('nsr', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable logging of NSR events
                ''',
                'nsr',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            _MetaInfoClassMember('session-protection', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable logging of session protection events
                ''',
                'session_protection',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-ldp-cfg',
            'enable-logging',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-ldp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg'
        ),
    },
    'MplsLdp.Global_.Signalling' : {
        'meta_info' : _MetaInfoClass('MplsLdp.Global_.Signalling',
            False, 
            [
            _MetaInfoClassMember('dscp', ATTRIBUTE, 'int' , None, None, 
                [('0', '63')], [], 
                '''                DSCP for control packets
                ''',
                'dscp',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-ldp-cfg',
            'signalling',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-ldp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg'
        ),
    },
    'MplsLdp.Global_.Nsr' : {
        'meta_info' : _MetaInfoClass('MplsLdp.Global_.Nsr',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                none
                ''',
                'enable',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-ldp-cfg',
            'nsr',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-ldp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg'
        ),
    },
    'MplsLdp.Global_.GracefulRestart' : {
        'meta_info' : _MetaInfoClass('MplsLdp.Global_.GracefulRestart',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                none
                ''',
                'enable',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            _MetaInfoClassMember('forwarding-hold-time', ATTRIBUTE, 'int' , None, None, 
                [('60', '1800')], [], 
                '''                Configure Graceful Restart Session holdtime
                ''',
                'forwarding_hold_time',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            _MetaInfoClassMember('reconnect-timeout', ATTRIBUTE, 'int' , None, None, 
                [('60', '1800')], [], 
                '''                Configure Graceful Restart Reconnect Timeout
                value
                ''',
                'reconnect_timeout',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-ldp-cfg',
            'graceful-restart',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-ldp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg'
        ),
    },
    'MplsLdp.Global_.Discovery.LinkHello' : {
        'meta_info' : _MetaInfoClass('MplsLdp.Global_.Discovery.LinkHello',
            False, 
            [
            _MetaInfoClassMember('hold-time', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                Time (seconds) - 65535 implies infinite
                ''',
                'hold_time',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            _MetaInfoClassMember('interval', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                Link Hello interval
                ''',
                'interval',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-ldp-cfg',
            'link-hello',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-ldp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg'
        ),
    },
    'MplsLdp.Global_.Discovery.TargetedHello' : {
        'meta_info' : _MetaInfoClass('MplsLdp.Global_.Discovery.TargetedHello',
            False, 
            [
            _MetaInfoClassMember('hold-time', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                Time (seconds) - 65535 implies infinite
                ''',
                'hold_time',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            _MetaInfoClassMember('interval', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                Targeted Hello interval
                ''',
                'interval',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-ldp-cfg',
            'targeted-hello',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-ldp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg'
        ),
    },
    'MplsLdp.Global_.Discovery' : {
        'meta_info' : _MetaInfoClass('MplsLdp.Global_.Discovery',
            False, 
            [
            _MetaInfoClassMember('disable-instance-tlv', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Disable transmit and receive processing for
                private Instance TLV in LDP discovery hello
                messages
                ''',
                'disable_instance_tlv',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            _MetaInfoClassMember('disable-quick-start', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Disable discovery's quick start mode
                ''',
                'disable_quick_start',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            _MetaInfoClassMember('link-hello', REFERENCE_CLASS, 'LinkHello' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg', 'MplsLdp.Global_.Discovery.LinkHello', 
                [], [], 
                '''                LDP Link Hellos
                ''',
                'link_hello',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            _MetaInfoClassMember('targeted-hello', REFERENCE_CLASS, 'TargetedHello' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg', 'MplsLdp.Global_.Discovery.TargetedHello', 
                [], [], 
                '''                LDP Targeted Hellos
                ''',
                'targeted_hello',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-ldp-cfg',
            'discovery',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-ldp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg'
        ),
    },
    'MplsLdp.Global_.Mldp.Vrfs.Vrf.Afs.Af.RecursiveForwarding' : {
        'meta_info' : _MetaInfoClass('MplsLdp.Global_.Mldp.Vrfs.Vrf.Afs.Af.RecursiveForwarding',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable recursive forwarding
                ''',
                'enable',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            _MetaInfoClassMember('policy', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                Recursive forwarding policy name
                ''',
                'policy',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-ldp-cfg',
            'recursive-forwarding',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-ldp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg'
        ),
    },
    'MplsLdp.Global_.Mldp.Vrfs.Vrf.Afs.Af.MldpRecursiveFec' : {
        'meta_info' : _MetaInfoClass('MplsLdp.Global_.Mldp.Vrfs.Vrf.Afs.Af.MldpRecursiveFec',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable MPLS mLDP Recursive FEC
                ''',
                'enable',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            _MetaInfoClassMember('policy', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                Route policy name
                ''',
                'policy',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-ldp-cfg',
            'mldp-recursive-fec',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-ldp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg'
        ),
    },
    'MplsLdp.Global_.Mldp.Vrfs.Vrf.Afs.Af.NeighborPolicies.NeighborPolicy' : {
        'meta_info' : _MetaInfoClass('MplsLdp.Global_.Mldp.Vrfs.Vrf.Afs.Af.NeighborPolicies.NeighborPolicy',
            False, 
            [
            _MetaInfoClassMember('root-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Neighbor Address
                ''',
                'root_address',
                'Cisco-IOS-XR-mpls-ldp-cfg', True, [
                    _MetaInfoClassMember('root-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Neighbor Address
                        ''',
                        'root_address',
                        'Cisco-IOS-XR-mpls-ldp-cfg', True),
                    _MetaInfoClassMember('root-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Neighbor Address
                        ''',
                        'root_address',
                        'Cisco-IOS-XR-mpls-ldp-cfg', True),
                ]),
            _MetaInfoClassMember('policy-mode', REFERENCE_ENUM_CLASS, 'MldpPolicyModeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg', 'MldpPolicyModeEnum', 
                [], [], 
                '''                Inbound/Outbound Policy
                ''',
                'policy_mode',
                'Cisco-IOS-XR-mpls-ldp-cfg', True),
            _MetaInfoClassMember('route-policy', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                Route policy name
                ''',
                'route_policy',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-ldp-cfg',
            'neighbor-policy',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-ldp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg'
        ),
    },
    'MplsLdp.Global_.Mldp.Vrfs.Vrf.Afs.Af.NeighborPolicies' : {
        'meta_info' : _MetaInfoClass('MplsLdp.Global_.Mldp.Vrfs.Vrf.Afs.Af.NeighborPolicies',
            False, 
            [
            _MetaInfoClassMember('neighbor-policy', REFERENCE_LIST, 'NeighborPolicy' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg', 'MplsLdp.Global_.Mldp.Vrfs.Vrf.Afs.Af.NeighborPolicies.NeighborPolicy', 
                [], [], 
                '''                Route Policy
                ''',
                'neighbor_policy',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-ldp-cfg',
            'neighbor-policies',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-ldp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg'
        ),
    },
    'MplsLdp.Global_.Mldp.Vrfs.Vrf.Afs.Af.MoFrr' : {
        'meta_info' : _MetaInfoClass('MplsLdp.Global_.Mldp.Vrfs.Vrf.Afs.Af.MoFrr',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable MPLS mLDP MoFRR
                ''',
                'enable',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            _MetaInfoClassMember('policy', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                Route policy name
                ''',
                'policy',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-ldp-cfg',
            'mo-frr',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-ldp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg'
        ),
    },
    'MplsLdp.Global_.Mldp.Vrfs.Vrf.Afs.Af.MakeBeforeBreak.Signaling' : {
        'meta_info' : _MetaInfoClass('MplsLdp.Global_.Mldp.Vrfs.Vrf.Afs.Af.MakeBeforeBreak.Signaling',
            False, 
            [
            _MetaInfoClassMember('delete-delay', ATTRIBUTE, 'int' , None, None, 
                [('0', '60')], [], 
                '''                Delete Delay in seconds
                ''',
                'delete_delay',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            _MetaInfoClassMember('forward-delay', ATTRIBUTE, 'int' , None, None, 
                [('0', '600')], [], 
                '''                Forwarding Delay in Seconds
                ''',
                'forward_delay',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-ldp-cfg',
            'signaling',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-ldp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg'
        ),
    },
    'MplsLdp.Global_.Mldp.Vrfs.Vrf.Afs.Af.MakeBeforeBreak' : {
        'meta_info' : _MetaInfoClass('MplsLdp.Global_.Mldp.Vrfs.Vrf.Afs.Af.MakeBeforeBreak',
            False, 
            [
            _MetaInfoClassMember('policy', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                Route policy name
                ''',
                'policy',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            _MetaInfoClassMember('signaling', REFERENCE_CLASS, 'Signaling' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg', 'MplsLdp.Global_.Mldp.Vrfs.Vrf.Afs.Af.MakeBeforeBreak.Signaling', 
                [], [], 
                '''                Enable MPLS mLDP MBB signaling
                ''',
                'signaling',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-ldp-cfg',
            'make-before-break',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-ldp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg'
        ),
    },
    'MplsLdp.Global_.Mldp.Vrfs.Vrf.Afs.Af.Csc' : {
        'meta_info' : _MetaInfoClass('MplsLdp.Global_.Mldp.Vrfs.Vrf.Afs.Af.Csc',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable MPLS mLDP CSC
                ''',
                'enable',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-ldp-cfg',
            'csc',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-ldp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg'
        ),
    },
    'MplsLdp.Global_.Mldp.Vrfs.Vrf.Afs.Af' : {
        'meta_info' : _MetaInfoClass('MplsLdp.Global_.Mldp.Vrfs.Vrf.Afs.Af',
            False, 
            [
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'MplsLdpafNameEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg', 'MplsLdpafNameEnum', 
                [], [], 
                '''                Address Family name
                ''',
                'af_name',
                'Cisco-IOS-XR-mpls-ldp-cfg', True),
            _MetaInfoClassMember('csc', REFERENCE_CLASS, 'Csc' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg', 'MplsLdp.Global_.Mldp.Vrfs.Vrf.Afs.Af.Csc', 
                [], [], 
                '''                MPLS mLDP CSC
                ''',
                'csc',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable Multicast Label Distribution Protocol
                (mLDP) under AF.
                ''',
                'enable',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            _MetaInfoClassMember('make-before-break', REFERENCE_CLASS, 'MakeBeforeBreak' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg', 'MplsLdp.Global_.Mldp.Vrfs.Vrf.Afs.Af.MakeBeforeBreak', 
                [], [], 
                '''                MPLS mLDP Make-Before-Break configuration
                ''',
                'make_before_break',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            _MetaInfoClassMember('mldp-recursive-fec', REFERENCE_CLASS, 'MldpRecursiveFec' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg', 'MplsLdp.Global_.Mldp.Vrfs.Vrf.Afs.Af.MldpRecursiveFec', 
                [], [], 
                '''                MPLS mLDP Recursive FEC
                ''',
                'mldp_recursive_fec',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            _MetaInfoClassMember('mldp-rib-unicast-always', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable MPLS MLDP RIB unicast-always
                configuration
                ''',
                'mldp_rib_unicast_always',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            _MetaInfoClassMember('mo-frr', REFERENCE_CLASS, 'MoFrr' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg', 'MplsLdp.Global_.Mldp.Vrfs.Vrf.Afs.Af.MoFrr', 
                [], [], 
                '''                MPLS mLDP MoFRR
                ''',
                'mo_frr',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            _MetaInfoClassMember('neighbor-policies', REFERENCE_CLASS, 'NeighborPolicies' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg', 'MplsLdp.Global_.Mldp.Vrfs.Vrf.Afs.Af.NeighborPolicies', 
                [], [], 
                '''                MLDP neighbor policies
                ''',
                'neighbor_policies',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            _MetaInfoClassMember('recursive-forwarding', REFERENCE_CLASS, 'RecursiveForwarding' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg', 'MplsLdp.Global_.Mldp.Vrfs.Vrf.Afs.Af.RecursiveForwarding', 
                [], [], 
                '''                Enable recursive forwarding
                ''',
                'recursive_forwarding',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-ldp-cfg',
            'af',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-ldp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg'
        ),
    },
    'MplsLdp.Global_.Mldp.Vrfs.Vrf.Afs' : {
        'meta_info' : _MetaInfoClass('MplsLdp.Global_.Mldp.Vrfs.Vrf.Afs',
            False, 
            [
            _MetaInfoClassMember('af', REFERENCE_LIST, 'Af' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg', 'MplsLdp.Global_.Mldp.Vrfs.Vrf.Afs.Af', 
                [], [], 
                '''                Operational data for given Address Family
                ''',
                'af',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-ldp-cfg',
            'afs',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-ldp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg'
        ),
    },
    'MplsLdp.Global_.Mldp.Vrfs.Vrf' : {
        'meta_info' : _MetaInfoClass('MplsLdp.Global_.Mldp.Vrfs.Vrf',
            False, 
            [
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                VRF Name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-mpls-ldp-cfg', True),
            _MetaInfoClassMember('afs', REFERENCE_CLASS, 'Afs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg', 'MplsLdp.Global_.Mldp.Vrfs.Vrf.Afs', 
                [], [], 
                '''                Address Family specific operational data
                ''',
                'afs',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable Multicast Label Distribution Protocol
                (mLDP)
                ''',
                'enable',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-ldp-cfg',
            'vrf',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-ldp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg'
        ),
    },
    'MplsLdp.Global_.Mldp.Vrfs' : {
        'meta_info' : _MetaInfoClass('MplsLdp.Global_.Mldp.Vrfs',
            False, 
            [
            _MetaInfoClassMember('vrf', REFERENCE_LIST, 'Vrf' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg', 'MplsLdp.Global_.Mldp.Vrfs.Vrf', 
                [], [], 
                '''                VRF attribute configuration for MPLS LDP
                ''',
                'vrf',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-ldp-cfg',
            'vrfs',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-ldp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg'
        ),
    },
    'MplsLdp.Global_.Mldp.DefaultVrf.Afs.Af.RecursiveForwarding' : {
        'meta_info' : _MetaInfoClass('MplsLdp.Global_.Mldp.DefaultVrf.Afs.Af.RecursiveForwarding',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable recursive forwarding
                ''',
                'enable',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            _MetaInfoClassMember('policy', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                Recursive forwarding policy name
                ''',
                'policy',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-ldp-cfg',
            'recursive-forwarding',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-ldp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg'
        ),
    },
    'MplsLdp.Global_.Mldp.DefaultVrf.Afs.Af.MldpRecursiveFec' : {
        'meta_info' : _MetaInfoClass('MplsLdp.Global_.Mldp.DefaultVrf.Afs.Af.MldpRecursiveFec',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable MPLS mLDP Recursive FEC
                ''',
                'enable',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            _MetaInfoClassMember('policy', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                Route policy name
                ''',
                'policy',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-ldp-cfg',
            'mldp-recursive-fec',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-ldp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg'
        ),
    },
    'MplsLdp.Global_.Mldp.DefaultVrf.Afs.Af.NeighborPolicies.NeighborPolicy' : {
        'meta_info' : _MetaInfoClass('MplsLdp.Global_.Mldp.DefaultVrf.Afs.Af.NeighborPolicies.NeighborPolicy',
            False, 
            [
            _MetaInfoClassMember('root-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Neighbor Address
                ''',
                'root_address',
                'Cisco-IOS-XR-mpls-ldp-cfg', True, [
                    _MetaInfoClassMember('root-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Neighbor Address
                        ''',
                        'root_address',
                        'Cisco-IOS-XR-mpls-ldp-cfg', True),
                    _MetaInfoClassMember('root-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Neighbor Address
                        ''',
                        'root_address',
                        'Cisco-IOS-XR-mpls-ldp-cfg', True),
                ]),
            _MetaInfoClassMember('policy-mode', REFERENCE_ENUM_CLASS, 'MldpPolicyModeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg', 'MldpPolicyModeEnum', 
                [], [], 
                '''                Inbound/Outbound Policy
                ''',
                'policy_mode',
                'Cisco-IOS-XR-mpls-ldp-cfg', True),
            _MetaInfoClassMember('route-policy', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                Route policy name
                ''',
                'route_policy',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-ldp-cfg',
            'neighbor-policy',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-ldp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg'
        ),
    },
    'MplsLdp.Global_.Mldp.DefaultVrf.Afs.Af.NeighborPolicies' : {
        'meta_info' : _MetaInfoClass('MplsLdp.Global_.Mldp.DefaultVrf.Afs.Af.NeighborPolicies',
            False, 
            [
            _MetaInfoClassMember('neighbor-policy', REFERENCE_LIST, 'NeighborPolicy' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg', 'MplsLdp.Global_.Mldp.DefaultVrf.Afs.Af.NeighborPolicies.NeighborPolicy', 
                [], [], 
                '''                Route Policy
                ''',
                'neighbor_policy',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-ldp-cfg',
            'neighbor-policies',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-ldp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg'
        ),
    },
    'MplsLdp.Global_.Mldp.DefaultVrf.Afs.Af.MoFrr' : {
        'meta_info' : _MetaInfoClass('MplsLdp.Global_.Mldp.DefaultVrf.Afs.Af.MoFrr',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable MPLS mLDP MoFRR
                ''',
                'enable',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            _MetaInfoClassMember('policy', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                Route policy name
                ''',
                'policy',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-ldp-cfg',
            'mo-frr',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-ldp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg'
        ),
    },
    'MplsLdp.Global_.Mldp.DefaultVrf.Afs.Af.MakeBeforeBreak.Signaling' : {
        'meta_info' : _MetaInfoClass('MplsLdp.Global_.Mldp.DefaultVrf.Afs.Af.MakeBeforeBreak.Signaling',
            False, 
            [
            _MetaInfoClassMember('delete-delay', ATTRIBUTE, 'int' , None, None, 
                [('0', '60')], [], 
                '''                Delete Delay in seconds
                ''',
                'delete_delay',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            _MetaInfoClassMember('forward-delay', ATTRIBUTE, 'int' , None, None, 
                [('0', '600')], [], 
                '''                Forwarding Delay in Seconds
                ''',
                'forward_delay',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-ldp-cfg',
            'signaling',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-ldp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg'
        ),
    },
    'MplsLdp.Global_.Mldp.DefaultVrf.Afs.Af.MakeBeforeBreak' : {
        'meta_info' : _MetaInfoClass('MplsLdp.Global_.Mldp.DefaultVrf.Afs.Af.MakeBeforeBreak',
            False, 
            [
            _MetaInfoClassMember('policy', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                Route policy name
                ''',
                'policy',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            _MetaInfoClassMember('signaling', REFERENCE_CLASS, 'Signaling' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg', 'MplsLdp.Global_.Mldp.DefaultVrf.Afs.Af.MakeBeforeBreak.Signaling', 
                [], [], 
                '''                Enable MPLS mLDP MBB signaling
                ''',
                'signaling',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-ldp-cfg',
            'make-before-break',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-ldp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg'
        ),
    },
    'MplsLdp.Global_.Mldp.DefaultVrf.Afs.Af.Csc' : {
        'meta_info' : _MetaInfoClass('MplsLdp.Global_.Mldp.DefaultVrf.Afs.Af.Csc',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable MPLS mLDP CSC
                ''',
                'enable',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-ldp-cfg',
            'csc',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-ldp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg'
        ),
    },
    'MplsLdp.Global_.Mldp.DefaultVrf.Afs.Af' : {
        'meta_info' : _MetaInfoClass('MplsLdp.Global_.Mldp.DefaultVrf.Afs.Af',
            False, 
            [
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'MplsLdpafNameEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg', 'MplsLdpafNameEnum', 
                [], [], 
                '''                Address Family name
                ''',
                'af_name',
                'Cisco-IOS-XR-mpls-ldp-cfg', True),
            _MetaInfoClassMember('csc', REFERENCE_CLASS, 'Csc' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg', 'MplsLdp.Global_.Mldp.DefaultVrf.Afs.Af.Csc', 
                [], [], 
                '''                MPLS mLDP CSC
                ''',
                'csc',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable Multicast Label Distribution Protocol
                (mLDP) under AF.
                ''',
                'enable',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            _MetaInfoClassMember('make-before-break', REFERENCE_CLASS, 'MakeBeforeBreak' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg', 'MplsLdp.Global_.Mldp.DefaultVrf.Afs.Af.MakeBeforeBreak', 
                [], [], 
                '''                MPLS mLDP Make-Before-Break configuration
                ''',
                'make_before_break',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            _MetaInfoClassMember('mldp-recursive-fec', REFERENCE_CLASS, 'MldpRecursiveFec' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg', 'MplsLdp.Global_.Mldp.DefaultVrf.Afs.Af.MldpRecursiveFec', 
                [], [], 
                '''                MPLS mLDP Recursive FEC
                ''',
                'mldp_recursive_fec',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            _MetaInfoClassMember('mldp-rib-unicast-always', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable MPLS MLDP RIB unicast-always
                configuration
                ''',
                'mldp_rib_unicast_always',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            _MetaInfoClassMember('mo-frr', REFERENCE_CLASS, 'MoFrr' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg', 'MplsLdp.Global_.Mldp.DefaultVrf.Afs.Af.MoFrr', 
                [], [], 
                '''                MPLS mLDP MoFRR
                ''',
                'mo_frr',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            _MetaInfoClassMember('neighbor-policies', REFERENCE_CLASS, 'NeighborPolicies' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg', 'MplsLdp.Global_.Mldp.DefaultVrf.Afs.Af.NeighborPolicies', 
                [], [], 
                '''                MLDP neighbor policies
                ''',
                'neighbor_policies',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            _MetaInfoClassMember('recursive-forwarding', REFERENCE_CLASS, 'RecursiveForwarding' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg', 'MplsLdp.Global_.Mldp.DefaultVrf.Afs.Af.RecursiveForwarding', 
                [], [], 
                '''                Enable recursive forwarding
                ''',
                'recursive_forwarding',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-ldp-cfg',
            'af',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-ldp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg'
        ),
    },
    'MplsLdp.Global_.Mldp.DefaultVrf.Afs' : {
        'meta_info' : _MetaInfoClass('MplsLdp.Global_.Mldp.DefaultVrf.Afs',
            False, 
            [
            _MetaInfoClassMember('af', REFERENCE_LIST, 'Af' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg', 'MplsLdp.Global_.Mldp.DefaultVrf.Afs.Af', 
                [], [], 
                '''                Operational data for given Address Family
                ''',
                'af',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-ldp-cfg',
            'afs',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-ldp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg'
        ),
    },
    'MplsLdp.Global_.Mldp.DefaultVrf' : {
        'meta_info' : _MetaInfoClass('MplsLdp.Global_.Mldp.DefaultVrf',
            False, 
            [
            _MetaInfoClassMember('afs', REFERENCE_CLASS, 'Afs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg', 'MplsLdp.Global_.Mldp.DefaultVrf.Afs', 
                [], [], 
                '''                Address Family specific operational data
                ''',
                'afs',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-ldp-cfg',
            'default-vrf',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-ldp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg'
        ),
    },
    'MplsLdp.Global_.Mldp.MldpGlobal.Logging' : {
        'meta_info' : _MetaInfoClass('MplsLdp.Global_.Mldp.MldpGlobal.Logging',
            False, 
            [
            _MetaInfoClassMember('notifications', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                MPLS mLDP logging notifications
                ''',
                'notifications',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-ldp-cfg',
            'logging',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-ldp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg'
        ),
    },
    'MplsLdp.Global_.Mldp.MldpGlobal' : {
        'meta_info' : _MetaInfoClass('MplsLdp.Global_.Mldp.MldpGlobal',
            False, 
            [
            _MetaInfoClassMember('logging', REFERENCE_CLASS, 'Logging' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg', 'MplsLdp.Global_.Mldp.MldpGlobal.Logging', 
                [], [], 
                '''                MPLS mLDP logging
                ''',
                'logging',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-ldp-cfg',
            'mldp-global',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-ldp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg'
        ),
    },
    'MplsLdp.Global_.Mldp' : {
        'meta_info' : _MetaInfoClass('MplsLdp.Global_.Mldp',
            False, 
            [
            _MetaInfoClassMember('default-vrf', REFERENCE_CLASS, 'DefaultVrf' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg', 'MplsLdp.Global_.Mldp.DefaultVrf', 
                [], [], 
                '''                Default VRF attribute configuration for mLDP
                ''',
                'default_vrf',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable Multicast Label Distribution Protocol
                (mLDP)
                ''',
                'enable',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            _MetaInfoClassMember('mldp-global', REFERENCE_CLASS, 'MldpGlobal' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg', 'MplsLdp.Global_.Mldp.MldpGlobal', 
                [], [], 
                '''                Global configuration for mLDP
                ''',
                'mldp_global',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            _MetaInfoClassMember('vrfs', REFERENCE_CLASS, 'Vrfs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg', 'MplsLdp.Global_.Mldp.Vrfs', 
                [], [], 
                '''                VRF Table attribute configuration for MPLS LDP
                ''',
                'vrfs',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-ldp-cfg',
            'mldp',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-ldp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg'
        ),
    },
    'MplsLdp.Global_' : {
        'meta_info' : _MetaInfoClass('MplsLdp.Global_',
            False, 
            [
            _MetaInfoClassMember('disable-implicit-ipv4', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Disable the implicit enabling for IPv4 address
                family
                ''',
                'disable_implicit_ipv4',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            _MetaInfoClassMember('discovery', REFERENCE_CLASS, 'Discovery' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg', 'MplsLdp.Global_.Discovery', 
                [], [], 
                '''                Configure Discovery parameters
                ''',
                'discovery',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            _MetaInfoClassMember('enable-logging', REFERENCE_CLASS, 'EnableLogging' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg', 'MplsLdp.Global_.EnableLogging', 
                [], [], 
                '''                Enable logging of events
                ''',
                'enable_logging',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            _MetaInfoClassMember('entropy-label', REFERENCE_CLASS, 'EntropyLabel' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg', 'MplsLdp.Global_.EntropyLabel', 
                [], [], 
                '''                Configure for LDP Entropy-Label
                ''',
                'entropy_label',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            _MetaInfoClassMember('graceful-restart', REFERENCE_CLASS, 'GracefulRestart' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg', 'MplsLdp.Global_.GracefulRestart', 
                [], [], 
                '''                Configuration for LDP Graceful Restart
                parameters
                ''',
                'graceful_restart',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            _MetaInfoClassMember('igp', REFERENCE_CLASS, 'Igp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg', 'MplsLdp.Global_.Igp', 
                [], [], 
                '''                LDP IGP configuration
                ''',
                'igp',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            _MetaInfoClassMember('ltrace-buf-multiplier', ATTRIBUTE, 'int' , None, None, 
                [('1', '5')], [], 
                '''                Configure Ltrace Buffer Multiplier
                ''',
                'ltrace_buf_multiplier',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            _MetaInfoClassMember('mldp', REFERENCE_CLASS, 'Mldp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg', 'MplsLdp.Global_.Mldp', 
                [], [], 
                '''                MPLS mLDP configuration
                ''',
                'mldp',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            _MetaInfoClassMember('nsr', REFERENCE_CLASS, 'Nsr' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg', 'MplsLdp.Global_.Nsr', 
                [], [], 
                '''                Configure LDP Non-Stop Routing
                ''',
                'nsr',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            _MetaInfoClassMember('session', REFERENCE_CLASS, 'Session' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg', 'MplsLdp.Global_.Session', 
                [], [], 
                '''                LDP Session parameters
                ''',
                'session',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            _MetaInfoClassMember('signalling', REFERENCE_CLASS, 'Signalling' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg', 'MplsLdp.Global_.Signalling', 
                [], [], 
                '''                Configure LDP signalling parameters
                ''',
                'signalling',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-ldp-cfg',
            'global',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-ldp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg'
        ),
    },
    'MplsLdp' : {
        'meta_info' : _MetaInfoClass('MplsLdp',
            False, 
            [
            _MetaInfoClassMember('default-vrf', REFERENCE_CLASS, 'DefaultVrf' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg', 'MplsLdp.DefaultVrf', 
                [], [], 
                '''                Global VRF attribute configuration for MPLS LDP
                ''',
                'default_vrf',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable Label Distribution Protocol (LDP)
                globally.Without creating this object the LDP
                feature will not be enabled. Deleting this
                object will stop the LDP feature.
                ''',
                'enable',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            _MetaInfoClassMember('global', REFERENCE_CLASS, 'Global_' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg', 'MplsLdp.Global_', 
                [], [], 
                '''                Global configuration for MPLS LDP
                ''',
                'global_',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            _MetaInfoClassMember('vrfs', REFERENCE_CLASS, 'Vrfs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg', 'MplsLdp.Vrfs', 
                [], [], 
                '''                VRF Table attribute configuration for MPLS LDP
                ''',
                'vrfs',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-ldp-cfg',
            'mpls-ldp',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-ldp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_ldp_cfg'
        ),
    },
}
_meta_table['MplsLdp.DefaultVrf.Afs.Af.Label.Remote.Accept.PeerAcceptPolicies.PeerAcceptPolicy']['meta_info'].parent =_meta_table['MplsLdp.DefaultVrf.Afs.Af.Label.Remote.Accept.PeerAcceptPolicies']['meta_info']
_meta_table['MplsLdp.DefaultVrf.Afs.Af.Label.Remote.Accept.PeerAcceptPolicies']['meta_info'].parent =_meta_table['MplsLdp.DefaultVrf.Afs.Af.Label.Remote.Accept']['meta_info']
_meta_table['MplsLdp.DefaultVrf.Afs.Af.Label.Remote.Accept']['meta_info'].parent =_meta_table['MplsLdp.DefaultVrf.Afs.Af.Label.Remote']['meta_info']
_meta_table['MplsLdp.DefaultVrf.Afs.Af.Label.Local.Advertise.PeerAdvertisePolicies.PeerAdvertisePolicy']['meta_info'].parent =_meta_table['MplsLdp.DefaultVrf.Afs.Af.Label.Local.Advertise.PeerAdvertisePolicies']['meta_info']
_meta_table['MplsLdp.DefaultVrf.Afs.Af.Label.Local.Advertise.PrefixAdvertisePolicies.PrefixAdvertisePolicy']['meta_info'].parent =_meta_table['MplsLdp.DefaultVrf.Afs.Af.Label.Local.Advertise.PrefixAdvertisePolicies']['meta_info']
_meta_table['MplsLdp.DefaultVrf.Afs.Af.Label.Local.Advertise.Interfaces.Interface']['meta_info'].parent =_meta_table['MplsLdp.DefaultVrf.Afs.Af.Label.Local.Advertise.Interfaces']['meta_info']
_meta_table['MplsLdp.DefaultVrf.Afs.Af.Label.Local.Advertise.PeerAdvertisePolicies']['meta_info'].parent =_meta_table['MplsLdp.DefaultVrf.Afs.Af.Label.Local.Advertise']['meta_info']
_meta_table['MplsLdp.DefaultVrf.Afs.Af.Label.Local.Advertise.PrefixAdvertisePolicies']['meta_info'].parent =_meta_table['MplsLdp.DefaultVrf.Afs.Af.Label.Local.Advertise']['meta_info']
_meta_table['MplsLdp.DefaultVrf.Afs.Af.Label.Local.Advertise.ExplicitNull']['meta_info'].parent =_meta_table['MplsLdp.DefaultVrf.Afs.Af.Label.Local.Advertise']['meta_info']
_meta_table['MplsLdp.DefaultVrf.Afs.Af.Label.Local.Advertise.Interfaces']['meta_info'].parent =_meta_table['MplsLdp.DefaultVrf.Afs.Af.Label.Local.Advertise']['meta_info']
_meta_table['MplsLdp.DefaultVrf.Afs.Af.Label.Local.Advertise']['meta_info'].parent =_meta_table['MplsLdp.DefaultVrf.Afs.Af.Label.Local']['meta_info']
_meta_table['MplsLdp.DefaultVrf.Afs.Af.Label.Local.Allocate']['meta_info'].parent =_meta_table['MplsLdp.DefaultVrf.Afs.Af.Label.Local']['meta_info']
_meta_table['MplsLdp.DefaultVrf.Afs.Af.Label.Remote']['meta_info'].parent =_meta_table['MplsLdp.DefaultVrf.Afs.Af.Label']['meta_info']
_meta_table['MplsLdp.DefaultVrf.Afs.Af.Label.Local']['meta_info'].parent =_meta_table['MplsLdp.DefaultVrf.Afs.Af.Label']['meta_info']
_meta_table['MplsLdp.DefaultVrf.Afs.Af.Discovery.TargetedHelloAccept']['meta_info'].parent =_meta_table['MplsLdp.DefaultVrf.Afs.Af.Discovery']['meta_info']
_meta_table['MplsLdp.DefaultVrf.Afs.Af.TrafficEngineering.AutoTunnelMesh.GroupIds.GroupId']['meta_info'].parent =_meta_table['MplsLdp.DefaultVrf.Afs.Af.TrafficEngineering.AutoTunnelMesh.GroupIds']['meta_info']
_meta_table['MplsLdp.DefaultVrf.Afs.Af.TrafficEngineering.AutoTunnelMesh.GroupIds']['meta_info'].parent =_meta_table['MplsLdp.DefaultVrf.Afs.Af.TrafficEngineering.AutoTunnelMesh']['meta_info']
_meta_table['MplsLdp.DefaultVrf.Afs.Af.TrafficEngineering.AutoTunnelMesh']['meta_info'].parent =_meta_table['MplsLdp.DefaultVrf.Afs.Af.TrafficEngineering']['meta_info']
_meta_table['MplsLdp.DefaultVrf.Afs.Af.Neighbor.Addresses.Address']['meta_info'].parent =_meta_table['MplsLdp.DefaultVrf.Afs.Af.Neighbor.Addresses']['meta_info']
_meta_table['MplsLdp.DefaultVrf.Afs.Af.Neighbor.Addresses']['meta_info'].parent =_meta_table['MplsLdp.DefaultVrf.Afs.Af.Neighbor']['meta_info']
_meta_table['MplsLdp.DefaultVrf.Afs.Af.RedistributionProtocol.Bgp.As_']['meta_info'].parent =_meta_table['MplsLdp.DefaultVrf.Afs.Af.RedistributionProtocol.Bgp']['meta_info']
_meta_table['MplsLdp.DefaultVrf.Afs.Af.RedistributionProtocol.Bgp.AdvertiseTo']['meta_info'].parent =_meta_table['MplsLdp.DefaultVrf.Afs.Af.RedistributionProtocol.Bgp']['meta_info']
_meta_table['MplsLdp.DefaultVrf.Afs.Af.RedistributionProtocol.Bgp']['meta_info'].parent =_meta_table['MplsLdp.DefaultVrf.Afs.Af.RedistributionProtocol']['meta_info']
_meta_table['MplsLdp.DefaultVrf.Afs.Af.Label']['meta_info'].parent =_meta_table['MplsLdp.DefaultVrf.Afs.Af']['meta_info']
_meta_table['MplsLdp.DefaultVrf.Afs.Af.Discovery']['meta_info'].parent =_meta_table['MplsLdp.DefaultVrf.Afs.Af']['meta_info']
_meta_table['MplsLdp.DefaultVrf.Afs.Af.TrafficEngineering']['meta_info'].parent =_meta_table['MplsLdp.DefaultVrf.Afs.Af']['meta_info']
_meta_table['MplsLdp.DefaultVrf.Afs.Af.Neighbor']['meta_info'].parent =_meta_table['MplsLdp.DefaultVrf.Afs.Af']['meta_info']
_meta_table['MplsLdp.DefaultVrf.Afs.Af.RedistributionProtocol']['meta_info'].parent =_meta_table['MplsLdp.DefaultVrf.Afs.Af']['meta_info']
_meta_table['MplsLdp.DefaultVrf.Afs.Af']['meta_info'].parent =_meta_table['MplsLdp.DefaultVrf.Afs']['meta_info']
_meta_table['MplsLdp.DefaultVrf.Global_.Session.Protection']['meta_info'].parent =_meta_table['MplsLdp.DefaultVrf.Global_.Session']['meta_info']
_meta_table['MplsLdp.DefaultVrf.Global_.Session.DownstreamOnDemand']['meta_info'].parent =_meta_table['MplsLdp.DefaultVrf.Global_.Session']['meta_info']
_meta_table['MplsLdp.DefaultVrf.Global_.Neighbor.LdpIds.LdpId.Password']['meta_info'].parent =_meta_table['MplsLdp.DefaultVrf.Global_.Neighbor.LdpIds.LdpId']['meta_info']
_meta_table['MplsLdp.DefaultVrf.Global_.Neighbor.LdpIds.LdpId']['meta_info'].parent =_meta_table['MplsLdp.DefaultVrf.Global_.Neighbor.LdpIds']['meta_info']
_meta_table['MplsLdp.DefaultVrf.Global_.Neighbor.DualStack.TransportConnection.Prefer']['meta_info'].parent =_meta_table['MplsLdp.DefaultVrf.Global_.Neighbor.DualStack.TransportConnection']['meta_info']
_meta_table['MplsLdp.DefaultVrf.Global_.Neighbor.DualStack.TransportConnection']['meta_info'].parent =_meta_table['MplsLdp.DefaultVrf.Global_.Neighbor.DualStack']['meta_info']
_meta_table['MplsLdp.DefaultVrf.Global_.Neighbor.LdpIds']['meta_info'].parent =_meta_table['MplsLdp.DefaultVrf.Global_.Neighbor']['meta_info']
_meta_table['MplsLdp.DefaultVrf.Global_.Neighbor.DualStack']['meta_info'].parent =_meta_table['MplsLdp.DefaultVrf.Global_.Neighbor']['meta_info']
_meta_table['MplsLdp.DefaultVrf.Global_.GracefulRestart.HelperPeer']['meta_info'].parent =_meta_table['MplsLdp.DefaultVrf.Global_.GracefulRestart']['meta_info']
_meta_table['MplsLdp.DefaultVrf.Global_.Session']['meta_info'].parent =_meta_table['MplsLdp.DefaultVrf.Global_']['meta_info']
_meta_table['MplsLdp.DefaultVrf.Global_.Neighbor']['meta_info'].parent =_meta_table['MplsLdp.DefaultVrf.Global_']['meta_info']
_meta_table['MplsLdp.DefaultVrf.Global_.GracefulRestart']['meta_info'].parent =_meta_table['MplsLdp.DefaultVrf.Global_']['meta_info']
_meta_table['MplsLdp.DefaultVrf.Interfaces.Interface.Afs.Af.Discovery.TransportAddress']['meta_info'].parent =_meta_table['MplsLdp.DefaultVrf.Interfaces.Interface.Afs.Af.Discovery']['meta_info']
_meta_table['MplsLdp.DefaultVrf.Interfaces.Interface.Afs.Af.Discovery']['meta_info'].parent =_meta_table['MplsLdp.DefaultVrf.Interfaces.Interface.Afs.Af']['meta_info']
_meta_table['MplsLdp.DefaultVrf.Interfaces.Interface.Afs.Af.Igp']['meta_info'].parent =_meta_table['MplsLdp.DefaultVrf.Interfaces.Interface.Afs.Af']['meta_info']
_meta_table['MplsLdp.DefaultVrf.Interfaces.Interface.Afs.Af.Mldp']['meta_info'].parent =_meta_table['MplsLdp.DefaultVrf.Interfaces.Interface.Afs.Af']['meta_info']
_meta_table['MplsLdp.DefaultVrf.Interfaces.Interface.Afs.Af']['meta_info'].parent =_meta_table['MplsLdp.DefaultVrf.Interfaces.Interface.Afs']['meta_info']
_meta_table['MplsLdp.DefaultVrf.Interfaces.Interface.Global_.Discovery.LinkHello']['meta_info'].parent =_meta_table['MplsLdp.DefaultVrf.Interfaces.Interface.Global_.Discovery']['meta_info']
_meta_table['MplsLdp.DefaultVrf.Interfaces.Interface.Global_.Igp.Sync.Delay.OnSessionUp']['meta_info'].parent =_meta_table['MplsLdp.DefaultVrf.Interfaces.Interface.Global_.Igp.Sync.Delay']['meta_info']
_meta_table['MplsLdp.DefaultVrf.Interfaces.Interface.Global_.Igp.Sync.Delay']['meta_info'].parent =_meta_table['MplsLdp.DefaultVrf.Interfaces.Interface.Global_.Igp.Sync']['meta_info']
_meta_table['MplsLdp.DefaultVrf.Interfaces.Interface.Global_.Igp.Sync']['meta_info'].parent =_meta_table['MplsLdp.DefaultVrf.Interfaces.Interface.Global_.Igp']['meta_info']
_meta_table['MplsLdp.DefaultVrf.Interfaces.Interface.Global_.Discovery']['meta_info'].parent =_meta_table['MplsLdp.DefaultVrf.Interfaces.Interface.Global_']['meta_info']
_meta_table['MplsLdp.DefaultVrf.Interfaces.Interface.Global_.Igp']['meta_info'].parent =_meta_table['MplsLdp.DefaultVrf.Interfaces.Interface.Global_']['meta_info']
_meta_table['MplsLdp.DefaultVrf.Interfaces.Interface.Afs']['meta_info'].parent =_meta_table['MplsLdp.DefaultVrf.Interfaces.Interface']['meta_info']
_meta_table['MplsLdp.DefaultVrf.Interfaces.Interface.Global_']['meta_info'].parent =_meta_table['MplsLdp.DefaultVrf.Interfaces.Interface']['meta_info']
_meta_table['MplsLdp.DefaultVrf.Interfaces.Interface']['meta_info'].parent =_meta_table['MplsLdp.DefaultVrf.Interfaces']['meta_info']
_meta_table['MplsLdp.DefaultVrf.Afs']['meta_info'].parent =_meta_table['MplsLdp.DefaultVrf']['meta_info']
_meta_table['MplsLdp.DefaultVrf.Global_']['meta_info'].parent =_meta_table['MplsLdp.DefaultVrf']['meta_info']
_meta_table['MplsLdp.DefaultVrf.Interfaces']['meta_info'].parent =_meta_table['MplsLdp.DefaultVrf']['meta_info']
_meta_table['MplsLdp.Vrfs.Vrf.Global_.Session.DownstreamOnDemand']['meta_info'].parent =_meta_table['MplsLdp.Vrfs.Vrf.Global_.Session']['meta_info']
_meta_table['MplsLdp.Vrfs.Vrf.Global_.Neighbor.LdpIds.LdpId.Password']['meta_info'].parent =_meta_table['MplsLdp.Vrfs.Vrf.Global_.Neighbor.LdpIds.LdpId']['meta_info']
_meta_table['MplsLdp.Vrfs.Vrf.Global_.Neighbor.LdpIds.LdpId']['meta_info'].parent =_meta_table['MplsLdp.Vrfs.Vrf.Global_.Neighbor.LdpIds']['meta_info']
_meta_table['MplsLdp.Vrfs.Vrf.Global_.Neighbor.LdpIds']['meta_info'].parent =_meta_table['MplsLdp.Vrfs.Vrf.Global_.Neighbor']['meta_info']
_meta_table['MplsLdp.Vrfs.Vrf.Global_.GracefulRestart.HelperPeer']['meta_info'].parent =_meta_table['MplsLdp.Vrfs.Vrf.Global_.GracefulRestart']['meta_info']
_meta_table['MplsLdp.Vrfs.Vrf.Global_.Session']['meta_info'].parent =_meta_table['MplsLdp.Vrfs.Vrf.Global_']['meta_info']
_meta_table['MplsLdp.Vrfs.Vrf.Global_.Neighbor']['meta_info'].parent =_meta_table['MplsLdp.Vrfs.Vrf.Global_']['meta_info']
_meta_table['MplsLdp.Vrfs.Vrf.Global_.GracefulRestart']['meta_info'].parent =_meta_table['MplsLdp.Vrfs.Vrf.Global_']['meta_info']
_meta_table['MplsLdp.Vrfs.Vrf.Afs.Af.Label.Remote.Accept.PeerAcceptPolicies.PeerAcceptPolicy.PeerAcceptPolicyData']['meta_info'].parent =_meta_table['MplsLdp.Vrfs.Vrf.Afs.Af.Label.Remote.Accept.PeerAcceptPolicies.PeerAcceptPolicy']['meta_info']
_meta_table['MplsLdp.Vrfs.Vrf.Afs.Af.Label.Remote.Accept.PeerAcceptPolicies.PeerAcceptPolicy.LsrId']['meta_info'].parent =_meta_table['MplsLdp.Vrfs.Vrf.Afs.Af.Label.Remote.Accept.PeerAcceptPolicies.PeerAcceptPolicy']['meta_info']
_meta_table['MplsLdp.Vrfs.Vrf.Afs.Af.Label.Remote.Accept.PeerAcceptPolicies.PeerAcceptPolicy']['meta_info'].parent =_meta_table['MplsLdp.Vrfs.Vrf.Afs.Af.Label.Remote.Accept.PeerAcceptPolicies']['meta_info']
_meta_table['MplsLdp.Vrfs.Vrf.Afs.Af.Label.Remote.Accept.PeerAcceptPolicies']['meta_info'].parent =_meta_table['MplsLdp.Vrfs.Vrf.Afs.Af.Label.Remote.Accept']['meta_info']
_meta_table['MplsLdp.Vrfs.Vrf.Afs.Af.Label.Remote.Accept']['meta_info'].parent =_meta_table['MplsLdp.Vrfs.Vrf.Afs.Af.Label.Remote']['meta_info']
_meta_table['MplsLdp.Vrfs.Vrf.Afs.Af.Label.Local.Advertise.PeerAdvertisePolicies.PeerAdvertisePolicy.PeerAdvertisePolicyData']['meta_info'].parent =_meta_table['MplsLdp.Vrfs.Vrf.Afs.Af.Label.Local.Advertise.PeerAdvertisePolicies.PeerAdvertisePolicy']['meta_info']
_meta_table['MplsLdp.Vrfs.Vrf.Afs.Af.Label.Local.Advertise.PeerAdvertisePolicies.PeerAdvertisePolicy.LsrId']['meta_info'].parent =_meta_table['MplsLdp.Vrfs.Vrf.Afs.Af.Label.Local.Advertise.PeerAdvertisePolicies.PeerAdvertisePolicy']['meta_info']
_meta_table['MplsLdp.Vrfs.Vrf.Afs.Af.Label.Local.Advertise.PeerAdvertisePolicies.PeerAdvertisePolicy']['meta_info'].parent =_meta_table['MplsLdp.Vrfs.Vrf.Afs.Af.Label.Local.Advertise.PeerAdvertisePolicies']['meta_info']
_meta_table['MplsLdp.Vrfs.Vrf.Afs.Af.Label.Local.Advertise.Interfaces.Interface']['meta_info'].parent =_meta_table['MplsLdp.Vrfs.Vrf.Afs.Af.Label.Local.Advertise.Interfaces']['meta_info']
_meta_table['MplsLdp.Vrfs.Vrf.Afs.Af.Label.Local.Advertise.PeerAdvertisePolicies']['meta_info'].parent =_meta_table['MplsLdp.Vrfs.Vrf.Afs.Af.Label.Local.Advertise']['meta_info']
_meta_table['MplsLdp.Vrfs.Vrf.Afs.Af.Label.Local.Advertise.Interfaces']['meta_info'].parent =_meta_table['MplsLdp.Vrfs.Vrf.Afs.Af.Label.Local.Advertise']['meta_info']
_meta_table['MplsLdp.Vrfs.Vrf.Afs.Af.Label.Local.Advertise.ExplicitNull']['meta_info'].parent =_meta_table['MplsLdp.Vrfs.Vrf.Afs.Af.Label.Local.Advertise']['meta_info']
_meta_table['MplsLdp.Vrfs.Vrf.Afs.Af.Label.Local.Advertise']['meta_info'].parent =_meta_table['MplsLdp.Vrfs.Vrf.Afs.Af.Label.Local']['meta_info']
_meta_table['MplsLdp.Vrfs.Vrf.Afs.Af.Label.Local.Allocate']['meta_info'].parent =_meta_table['MplsLdp.Vrfs.Vrf.Afs.Af.Label.Local']['meta_info']
_meta_table['MplsLdp.Vrfs.Vrf.Afs.Af.Label.Remote']['meta_info'].parent =_meta_table['MplsLdp.Vrfs.Vrf.Afs.Af.Label']['meta_info']
_meta_table['MplsLdp.Vrfs.Vrf.Afs.Af.Label.Local']['meta_info'].parent =_meta_table['MplsLdp.Vrfs.Vrf.Afs.Af.Label']['meta_info']
_meta_table['MplsLdp.Vrfs.Vrf.Afs.Af.Discovery']['meta_info'].parent =_meta_table['MplsLdp.Vrfs.Vrf.Afs.Af']['meta_info']
_meta_table['MplsLdp.Vrfs.Vrf.Afs.Af.Label']['meta_info'].parent =_meta_table['MplsLdp.Vrfs.Vrf.Afs.Af']['meta_info']
_meta_table['MplsLdp.Vrfs.Vrf.Afs.Af']['meta_info'].parent =_meta_table['MplsLdp.Vrfs.Vrf.Afs']['meta_info']
_meta_table['MplsLdp.Vrfs.Vrf.Interfaces.Interface.Afs.Af.Discovery.TransportAddress']['meta_info'].parent =_meta_table['MplsLdp.Vrfs.Vrf.Interfaces.Interface.Afs.Af.Discovery']['meta_info']
_meta_table['MplsLdp.Vrfs.Vrf.Interfaces.Interface.Afs.Af.Discovery']['meta_info'].parent =_meta_table['MplsLdp.Vrfs.Vrf.Interfaces.Interface.Afs.Af']['meta_info']
_meta_table['MplsLdp.Vrfs.Vrf.Interfaces.Interface.Afs.Af']['meta_info'].parent =_meta_table['MplsLdp.Vrfs.Vrf.Interfaces.Interface.Afs']['meta_info']
_meta_table['MplsLdp.Vrfs.Vrf.Interfaces.Interface.Afs']['meta_info'].parent =_meta_table['MplsLdp.Vrfs.Vrf.Interfaces.Interface']['meta_info']
_meta_table['MplsLdp.Vrfs.Vrf.Interfaces.Interface']['meta_info'].parent =_meta_table['MplsLdp.Vrfs.Vrf.Interfaces']['meta_info']
_meta_table['MplsLdp.Vrfs.Vrf.Global_']['meta_info'].parent =_meta_table['MplsLdp.Vrfs.Vrf']['meta_info']
_meta_table['MplsLdp.Vrfs.Vrf.Afs']['meta_info'].parent =_meta_table['MplsLdp.Vrfs.Vrf']['meta_info']
_meta_table['MplsLdp.Vrfs.Vrf.Interfaces']['meta_info'].parent =_meta_table['MplsLdp.Vrfs.Vrf']['meta_info']
_meta_table['MplsLdp.Vrfs.Vrf']['meta_info'].parent =_meta_table['MplsLdp.Vrfs']['meta_info']
_meta_table['MplsLdp.Global_.Session.BackoffTime']['meta_info'].parent =_meta_table['MplsLdp.Global_.Session']['meta_info']
_meta_table['MplsLdp.Global_.Igp.Sync.Delay']['meta_info'].parent =_meta_table['MplsLdp.Global_.Igp.Sync']['meta_info']
_meta_table['MplsLdp.Global_.Igp.Sync']['meta_info'].parent =_meta_table['MplsLdp.Global_.Igp']['meta_info']
_meta_table['MplsLdp.Global_.Discovery.LinkHello']['meta_info'].parent =_meta_table['MplsLdp.Global_.Discovery']['meta_info']
_meta_table['MplsLdp.Global_.Discovery.TargetedHello']['meta_info'].parent =_meta_table['MplsLdp.Global_.Discovery']['meta_info']
_meta_table['MplsLdp.Global_.Mldp.Vrfs.Vrf.Afs.Af.NeighborPolicies.NeighborPolicy']['meta_info'].parent =_meta_table['MplsLdp.Global_.Mldp.Vrfs.Vrf.Afs.Af.NeighborPolicies']['meta_info']
_meta_table['MplsLdp.Global_.Mldp.Vrfs.Vrf.Afs.Af.MakeBeforeBreak.Signaling']['meta_info'].parent =_meta_table['MplsLdp.Global_.Mldp.Vrfs.Vrf.Afs.Af.MakeBeforeBreak']['meta_info']
_meta_table['MplsLdp.Global_.Mldp.Vrfs.Vrf.Afs.Af.RecursiveForwarding']['meta_info'].parent =_meta_table['MplsLdp.Global_.Mldp.Vrfs.Vrf.Afs.Af']['meta_info']
_meta_table['MplsLdp.Global_.Mldp.Vrfs.Vrf.Afs.Af.MldpRecursiveFec']['meta_info'].parent =_meta_table['MplsLdp.Global_.Mldp.Vrfs.Vrf.Afs.Af']['meta_info']
_meta_table['MplsLdp.Global_.Mldp.Vrfs.Vrf.Afs.Af.NeighborPolicies']['meta_info'].parent =_meta_table['MplsLdp.Global_.Mldp.Vrfs.Vrf.Afs.Af']['meta_info']
_meta_table['MplsLdp.Global_.Mldp.Vrfs.Vrf.Afs.Af.MoFrr']['meta_info'].parent =_meta_table['MplsLdp.Global_.Mldp.Vrfs.Vrf.Afs.Af']['meta_info']
_meta_table['MplsLdp.Global_.Mldp.Vrfs.Vrf.Afs.Af.MakeBeforeBreak']['meta_info'].parent =_meta_table['MplsLdp.Global_.Mldp.Vrfs.Vrf.Afs.Af']['meta_info']
_meta_table['MplsLdp.Global_.Mldp.Vrfs.Vrf.Afs.Af.Csc']['meta_info'].parent =_meta_table['MplsLdp.Global_.Mldp.Vrfs.Vrf.Afs.Af']['meta_info']
_meta_table['MplsLdp.Global_.Mldp.Vrfs.Vrf.Afs.Af']['meta_info'].parent =_meta_table['MplsLdp.Global_.Mldp.Vrfs.Vrf.Afs']['meta_info']
_meta_table['MplsLdp.Global_.Mldp.Vrfs.Vrf.Afs']['meta_info'].parent =_meta_table['MplsLdp.Global_.Mldp.Vrfs.Vrf']['meta_info']
_meta_table['MplsLdp.Global_.Mldp.Vrfs.Vrf']['meta_info'].parent =_meta_table['MplsLdp.Global_.Mldp.Vrfs']['meta_info']
_meta_table['MplsLdp.Global_.Mldp.DefaultVrf.Afs.Af.NeighborPolicies.NeighborPolicy']['meta_info'].parent =_meta_table['MplsLdp.Global_.Mldp.DefaultVrf.Afs.Af.NeighborPolicies']['meta_info']
_meta_table['MplsLdp.Global_.Mldp.DefaultVrf.Afs.Af.MakeBeforeBreak.Signaling']['meta_info'].parent =_meta_table['MplsLdp.Global_.Mldp.DefaultVrf.Afs.Af.MakeBeforeBreak']['meta_info']
_meta_table['MplsLdp.Global_.Mldp.DefaultVrf.Afs.Af.RecursiveForwarding']['meta_info'].parent =_meta_table['MplsLdp.Global_.Mldp.DefaultVrf.Afs.Af']['meta_info']
_meta_table['MplsLdp.Global_.Mldp.DefaultVrf.Afs.Af.MldpRecursiveFec']['meta_info'].parent =_meta_table['MplsLdp.Global_.Mldp.DefaultVrf.Afs.Af']['meta_info']
_meta_table['MplsLdp.Global_.Mldp.DefaultVrf.Afs.Af.NeighborPolicies']['meta_info'].parent =_meta_table['MplsLdp.Global_.Mldp.DefaultVrf.Afs.Af']['meta_info']
_meta_table['MplsLdp.Global_.Mldp.DefaultVrf.Afs.Af.MoFrr']['meta_info'].parent =_meta_table['MplsLdp.Global_.Mldp.DefaultVrf.Afs.Af']['meta_info']
_meta_table['MplsLdp.Global_.Mldp.DefaultVrf.Afs.Af.MakeBeforeBreak']['meta_info'].parent =_meta_table['MplsLdp.Global_.Mldp.DefaultVrf.Afs.Af']['meta_info']
_meta_table['MplsLdp.Global_.Mldp.DefaultVrf.Afs.Af.Csc']['meta_info'].parent =_meta_table['MplsLdp.Global_.Mldp.DefaultVrf.Afs.Af']['meta_info']
_meta_table['MplsLdp.Global_.Mldp.DefaultVrf.Afs.Af']['meta_info'].parent =_meta_table['MplsLdp.Global_.Mldp.DefaultVrf.Afs']['meta_info']
_meta_table['MplsLdp.Global_.Mldp.DefaultVrf.Afs']['meta_info'].parent =_meta_table['MplsLdp.Global_.Mldp.DefaultVrf']['meta_info']
_meta_table['MplsLdp.Global_.Mldp.MldpGlobal.Logging']['meta_info'].parent =_meta_table['MplsLdp.Global_.Mldp.MldpGlobal']['meta_info']
_meta_table['MplsLdp.Global_.Mldp.Vrfs']['meta_info'].parent =_meta_table['MplsLdp.Global_.Mldp']['meta_info']
_meta_table['MplsLdp.Global_.Mldp.DefaultVrf']['meta_info'].parent =_meta_table['MplsLdp.Global_.Mldp']['meta_info']
_meta_table['MplsLdp.Global_.Mldp.MldpGlobal']['meta_info'].parent =_meta_table['MplsLdp.Global_.Mldp']['meta_info']
_meta_table['MplsLdp.Global_.EntropyLabel']['meta_info'].parent =_meta_table['MplsLdp.Global_']['meta_info']
_meta_table['MplsLdp.Global_.Session']['meta_info'].parent =_meta_table['MplsLdp.Global_']['meta_info']
_meta_table['MplsLdp.Global_.Igp']['meta_info'].parent =_meta_table['MplsLdp.Global_']['meta_info']
_meta_table['MplsLdp.Global_.EnableLogging']['meta_info'].parent =_meta_table['MplsLdp.Global_']['meta_info']
_meta_table['MplsLdp.Global_.Signalling']['meta_info'].parent =_meta_table['MplsLdp.Global_']['meta_info']
_meta_table['MplsLdp.Global_.Nsr']['meta_info'].parent =_meta_table['MplsLdp.Global_']['meta_info']
_meta_table['MplsLdp.Global_.GracefulRestart']['meta_info'].parent =_meta_table['MplsLdp.Global_']['meta_info']
_meta_table['MplsLdp.Global_.Discovery']['meta_info'].parent =_meta_table['MplsLdp.Global_']['meta_info']
_meta_table['MplsLdp.Global_.Mldp']['meta_info'].parent =_meta_table['MplsLdp.Global_']['meta_info']
_meta_table['MplsLdp.DefaultVrf']['meta_info'].parent =_meta_table['MplsLdp']['meta_info']
_meta_table['MplsLdp.Vrfs']['meta_info'].parent =_meta_table['MplsLdp']['meta_info']
_meta_table['MplsLdp.Global_']['meta_info'].parent =_meta_table['MplsLdp']['meta_info']
