


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'VrfAddressFamilyEnum' : _MetaInfoEnum('VrfAddressFamilyEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg',
        {
            'ipv4':'ipv4',
            'ipv6':'ipv6',
        }, 'Cisco-IOS-XR-infra-rsi-cfg', _yang_ns._namespaces['Cisco-IOS-XR-infra-rsi-cfg']),
    'VrfSubAddressFamilyEnum' : _MetaInfoEnum('VrfSubAddressFamilyEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg',
        {
            'unicast':'unicast',
            'multicast':'multicast',
            'flow-spec':'flow_spec',
        }, 'Cisco-IOS-XR-infra-rsi-cfg', _yang_ns._namespaces['Cisco-IOS-XR-infra-rsi-cfg']),
    'SrlgPriorityEnum' : _MetaInfoEnum('SrlgPriorityEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg',
        {
            'critical':'critical',
            'high':'high',
            'default':'default',
            'low':'low',
            'very-low':'very_low',
        }, 'Cisco-IOS-XR-infra-rsi-cfg', _yang_ns._namespaces['Cisco-IOS-XR-infra-rsi-cfg']),
    'Vrfs.Vrf.VpnId' : {
        'meta_info' : _MetaInfoClass('Vrfs.Vrf.VpnId',
            False, 
            [
            _MetaInfoClassMember('vpn-index', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Index of VPNID Index
                ''',
                'vpn_index',
                'Cisco-IOS-XR-infra-rsi-cfg', False),
            _MetaInfoClassMember('vpn-oui', ATTRIBUTE, 'int' , None, None, 
                [('0', '16777215')], [], 
                '''                OUI of VPNID OUI
                ''',
                'vpn_oui',
                'Cisco-IOS-XR-infra-rsi-cfg', False),
            ],
            'Cisco-IOS-XR-infra-rsi-cfg',
            'vpn-id',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rsi-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg'
        ),
    },
    'Vrfs.Vrf.Afs.Af.MaximumPrefix' : {
        'meta_info' : _MetaInfoClass('Vrfs.Vrf.Afs.Af.MaximumPrefix',
            False, 
            [
            _MetaInfoClassMember('mid-threshold', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                Mid-threshold (% of maximum)
                ''',
                'mid_threshold',
                'Cisco-IOS-XR-ip-rib-cfg', False),
            _MetaInfoClassMember('prefix-limit', ATTRIBUTE, 'int' , None, None, 
                [('32', '5000000')], [], 
                '''                Set table's maximum prefix limit
                ''',
                'prefix_limit',
                'Cisco-IOS-XR-ip-rib-cfg', False),
            ],
            'Cisco-IOS-XR-ip-rib-cfg',
            'maximum-prefix',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-rib-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg'
        ),
    },
    'Vrfs.Vrf.Afs.Af.Bgp.ImportRouteTargets.RouteTargets.RouteTarget.AsOrFourByteAs' : {
        'meta_info' : _MetaInfoClass('Vrfs.Vrf.Afs.Af.Bgp.ImportRouteTargets.RouteTargets.RouteTarget.AsOrFourByteAs',
            False, 
            [
            _MetaInfoClassMember('as-xx', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                AS number
                ''',
                'as_xx',
                'Cisco-IOS-XR-ipv4-bgp-cfg', True),
            _MetaInfoClassMember('as', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                AS number
                ''',
                'as_',
                'Cisco-IOS-XR-ipv4-bgp-cfg', True),
            _MetaInfoClassMember('as-index', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                AS number Index
                ''',
                'as_index',
                'Cisco-IOS-XR-ipv4-bgp-cfg', True),
            _MetaInfoClassMember('stitching-rt', ATTRIBUTE, 'int' , None, None, 
                [('0', '1')], [], 
                '''                Stitching RT
                ''',
                'stitching_rt',
                'Cisco-IOS-XR-ipv4-bgp-cfg', True),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'as-or-four-byte-as',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg'
        ),
    },
    'Vrfs.Vrf.Afs.Af.Bgp.ImportRouteTargets.RouteTargets.RouteTarget.Ipv4Address' : {
        'meta_info' : _MetaInfoClass('Vrfs.Vrf.Afs.Af.Bgp.ImportRouteTargets.RouteTargets.RouteTarget.Ipv4Address',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IP address
                ''',
                'address',
                'Cisco-IOS-XR-ipv4-bgp-cfg', True),
            _MetaInfoClassMember('address-index', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                IP address Index
                ''',
                'address_index',
                'Cisco-IOS-XR-ipv4-bgp-cfg', True),
            _MetaInfoClassMember('stitching-rt', ATTRIBUTE, 'int' , None, None, 
                [('0', '1')], [], 
                '''                Stitching RT
                ''',
                'stitching_rt',
                'Cisco-IOS-XR-ipv4-bgp-cfg', True),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'ipv4-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg'
        ),
    },
    'Vrfs.Vrf.Afs.Af.Bgp.ImportRouteTargets.RouteTargets.RouteTarget' : {
        'meta_info' : _MetaInfoClass('Vrfs.Vrf.Afs.Af.Bgp.ImportRouteTargets.RouteTargets.RouteTarget',
            False, 
            [
            _MetaInfoClassMember('type', REFERENCE_ENUM_CLASS, 'BgpVrfRouteTargetEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpVrfRouteTargetEnum', 
                [], [], 
                '''                Type of RT
                ''',
                'type',
                'Cisco-IOS-XR-ipv4-bgp-cfg', True),
            _MetaInfoClassMember('as-or-four-byte-as', REFERENCE_LIST, 'AsOrFourByteAs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg', 'Vrfs.Vrf.Afs.Af.Bgp.ImportRouteTargets.RouteTargets.RouteTarget.AsOrFourByteAs', 
                [], [], 
                '''                as or four byte as
                ''',
                'as_or_four_byte_as',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('ipv4-address', REFERENCE_LIST, 'Ipv4Address' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg', 'Vrfs.Vrf.Afs.Af.Bgp.ImportRouteTargets.RouteTargets.RouteTarget.Ipv4Address', 
                [], [], 
                '''                ipv4 address
                ''',
                'ipv4_address',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'route-target',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg'
        ),
    },
    'Vrfs.Vrf.Afs.Af.Bgp.ImportRouteTargets.RouteTargets' : {
        'meta_info' : _MetaInfoClass('Vrfs.Vrf.Afs.Af.Bgp.ImportRouteTargets.RouteTargets',
            False, 
            [
            _MetaInfoClassMember('route-target', REFERENCE_LIST, 'RouteTarget' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg', 'Vrfs.Vrf.Afs.Af.Bgp.ImportRouteTargets.RouteTargets.RouteTarget', 
                [], [], 
                '''                Route target
                ''',
                'route_target',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'route-targets',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg'
        ),
    },
    'Vrfs.Vrf.Afs.Af.Bgp.ImportRouteTargets' : {
        'meta_info' : _MetaInfoClass('Vrfs.Vrf.Afs.Af.Bgp.ImportRouteTargets',
            False, 
            [
            _MetaInfoClassMember('route-targets', REFERENCE_CLASS, 'RouteTargets' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg', 'Vrfs.Vrf.Afs.Af.Bgp.ImportRouteTargets.RouteTargets', 
                [], [], 
                '''                Route target table
                ''',
                'route_targets',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'import-route-targets',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg'
        ),
    },
    'Vrfs.Vrf.Afs.Af.Bgp.ExportRouteTargets.RouteTargets.RouteTarget.AsOrFourByteAs' : {
        'meta_info' : _MetaInfoClass('Vrfs.Vrf.Afs.Af.Bgp.ExportRouteTargets.RouteTargets.RouteTarget.AsOrFourByteAs',
            False, 
            [
            _MetaInfoClassMember('as-xx', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                AS number
                ''',
                'as_xx',
                'Cisco-IOS-XR-ipv4-bgp-cfg', True),
            _MetaInfoClassMember('as', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                AS number
                ''',
                'as_',
                'Cisco-IOS-XR-ipv4-bgp-cfg', True),
            _MetaInfoClassMember('as-index', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                AS number Index
                ''',
                'as_index',
                'Cisco-IOS-XR-ipv4-bgp-cfg', True),
            _MetaInfoClassMember('stitching-rt', ATTRIBUTE, 'int' , None, None, 
                [('0', '1')], [], 
                '''                Stitching RT
                ''',
                'stitching_rt',
                'Cisco-IOS-XR-ipv4-bgp-cfg', True),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'as-or-four-byte-as',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg'
        ),
    },
    'Vrfs.Vrf.Afs.Af.Bgp.ExportRouteTargets.RouteTargets.RouteTarget.Ipv4Address' : {
        'meta_info' : _MetaInfoClass('Vrfs.Vrf.Afs.Af.Bgp.ExportRouteTargets.RouteTargets.RouteTarget.Ipv4Address',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IP address
                ''',
                'address',
                'Cisco-IOS-XR-ipv4-bgp-cfg', True),
            _MetaInfoClassMember('address-index', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                IP address Index
                ''',
                'address_index',
                'Cisco-IOS-XR-ipv4-bgp-cfg', True),
            _MetaInfoClassMember('stitching-rt', ATTRIBUTE, 'int' , None, None, 
                [('0', '1')], [], 
                '''                Stitching RT
                ''',
                'stitching_rt',
                'Cisco-IOS-XR-ipv4-bgp-cfg', True),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'ipv4-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg'
        ),
    },
    'Vrfs.Vrf.Afs.Af.Bgp.ExportRouteTargets.RouteTargets.RouteTarget' : {
        'meta_info' : _MetaInfoClass('Vrfs.Vrf.Afs.Af.Bgp.ExportRouteTargets.RouteTargets.RouteTarget',
            False, 
            [
            _MetaInfoClassMember('type', REFERENCE_ENUM_CLASS, 'BgpVrfRouteTargetEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpVrfRouteTargetEnum', 
                [], [], 
                '''                Type of RT
                ''',
                'type',
                'Cisco-IOS-XR-ipv4-bgp-cfg', True),
            _MetaInfoClassMember('as-or-four-byte-as', REFERENCE_LIST, 'AsOrFourByteAs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg', 'Vrfs.Vrf.Afs.Af.Bgp.ExportRouteTargets.RouteTargets.RouteTarget.AsOrFourByteAs', 
                [], [], 
                '''                as or four byte as
                ''',
                'as_or_four_byte_as',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('ipv4-address', REFERENCE_LIST, 'Ipv4Address' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg', 'Vrfs.Vrf.Afs.Af.Bgp.ExportRouteTargets.RouteTargets.RouteTarget.Ipv4Address', 
                [], [], 
                '''                ipv4 address
                ''',
                'ipv4_address',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'route-target',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg'
        ),
    },
    'Vrfs.Vrf.Afs.Af.Bgp.ExportRouteTargets.RouteTargets' : {
        'meta_info' : _MetaInfoClass('Vrfs.Vrf.Afs.Af.Bgp.ExportRouteTargets.RouteTargets',
            False, 
            [
            _MetaInfoClassMember('route-target', REFERENCE_LIST, 'RouteTarget' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg', 'Vrfs.Vrf.Afs.Af.Bgp.ExportRouteTargets.RouteTargets.RouteTarget', 
                [], [], 
                '''                Route target
                ''',
                'route_target',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'route-targets',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg'
        ),
    },
    'Vrfs.Vrf.Afs.Af.Bgp.ExportRouteTargets' : {
        'meta_info' : _MetaInfoClass('Vrfs.Vrf.Afs.Af.Bgp.ExportRouteTargets',
            False, 
            [
            _MetaInfoClassMember('route-targets', REFERENCE_CLASS, 'RouteTargets' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg', 'Vrfs.Vrf.Afs.Af.Bgp.ExportRouteTargets.RouteTargets', 
                [], [], 
                '''                Route target table
                ''',
                'route_targets',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'export-route-targets',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg'
        ),
    },
    'Vrfs.Vrf.Afs.Af.Bgp.VrfToGlobalExportRoutePolicy' : {
        'meta_info' : _MetaInfoClass('Vrfs.Vrf.Afs.Af.Bgp.VrfToGlobalExportRoutePolicy',
            False, 
            [
            _MetaInfoClassMember('allow-imported-vpn', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE Enable imported VPN paths to be exported
                to Default VRF.FALSE Disable imported VPN
                paths to be exported to Default VRF.
                ''',
                'allow_imported_vpn',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Vrf to global export route policy
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'vrf-to-global-export-route-policy',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg'
        ),
    },
    'Vrfs.Vrf.Afs.Af.Bgp.ExportVrfOptions' : {
        'meta_info' : _MetaInfoClass('Vrfs.Vrf.Afs.Af.Bgp.ExportVrfOptions',
            False, 
            [
            _MetaInfoClassMember('allow-imported-vpn', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE Enable imported VPN paths to be exported
                to non-default VRFFALSE Disable imported VPN
                paths to be exported to non-default VRF
                ''',
                'allow_imported_vpn',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('import-stitching-rt', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE Use stitchng RTs to import extranet
                pathsFALSE Use regular RTs to import extranet
                paths
                ''',
                'import_stitching_rt',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'export-vrf-options',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg'
        ),
    },
    'Vrfs.Vrf.Afs.Af.Bgp.GlobalToVrfImportRoutePolicy' : {
        'meta_info' : _MetaInfoClass('Vrfs.Vrf.Afs.Af.Bgp.GlobalToVrfImportRoutePolicy',
            False, 
            [
            _MetaInfoClassMember('advertise-as-vpn', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE Enable advertising imported paths to
                PEsFALSE Disable advertising imported paths to
                PEs
                ''',
                'advertise_as_vpn',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Global to vrf import route policy
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'global-to-vrf-import-route-policy',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg'
        ),
    },
    'Vrfs.Vrf.Afs.Af.Bgp' : {
        'meta_info' : _MetaInfoClass('Vrfs.Vrf.Afs.Af.Bgp',
            False, 
            [
            _MetaInfoClassMember('export-route-policy', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Route policy for export filtering
                ''',
                'export_route_policy',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('export-route-targets', REFERENCE_CLASS, 'ExportRouteTargets' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg', 'Vrfs.Vrf.Afs.Af.Bgp.ExportRouteTargets', 
                [], [], 
                '''                Export Route targets
                ''',
                'export_route_targets',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('export-vrf-options', REFERENCE_CLASS, 'ExportVrfOptions' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg', 'Vrfs.Vrf.Afs.Af.Bgp.ExportVrfOptions', 
                [], [], 
                '''                Export VRF options
                ''',
                'export_vrf_options',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('global-to-vrf-import-route-policy', REFERENCE_CLASS, 'GlobalToVrfImportRoutePolicy' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg', 'Vrfs.Vrf.Afs.Af.Bgp.GlobalToVrfImportRoutePolicy', 
                [], [], 
                '''                Route policy for global to vrf import filtering
                ''',
                'global_to_vrf_import_route_policy',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('import-route-policy', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Route policy for import filtering
                ''',
                'import_route_policy',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('import-route-targets', REFERENCE_CLASS, 'ImportRouteTargets' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg', 'Vrfs.Vrf.Afs.Af.Bgp.ImportRouteTargets', 
                [], [], 
                '''                Import Route targets
                ''',
                'import_route_targets',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('import-vrf-options', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE Enable advertising imported paths to
                PEsFALSE Disable advertising imported paths to
                PEs
                ''',
                'import_vrf_options',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('vrf-to-global-export-route-policy', REFERENCE_CLASS, 'VrfToGlobalExportRoutePolicy' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg', 'Vrfs.Vrf.Afs.Af.Bgp.VrfToGlobalExportRoutePolicy', 
                [], [], 
                '''                Route policy for vrf to global export filtering
                ''',
                'vrf_to_global_export_route_policy',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'bgp',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg'
        ),
    },
    'Vrfs.Vrf.Afs.Af' : {
        'meta_info' : _MetaInfoClass('Vrfs.Vrf.Afs.Af',
            False, 
            [
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'VrfAddressFamilyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg', 'VrfAddressFamilyEnum', 
                [], [], 
                '''                Address family
                ''',
                'af_name',
                'Cisco-IOS-XR-infra-rsi-cfg', True),
            _MetaInfoClassMember('saf-name', REFERENCE_ENUM_CLASS, 'VrfSubAddressFamilyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg', 'VrfSubAddressFamilyEnum', 
                [], [], 
                '''                Sub-Address family
                ''',
                'saf_name',
                'Cisco-IOS-XR-infra-rsi-cfg', True),
            _MetaInfoClassMember('topology-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 244)], [], 
                '''                Topology name
                ''',
                'topology_name',
                'Cisco-IOS-XR-infra-rsi-cfg', True),
            _MetaInfoClassMember('bgp', REFERENCE_CLASS, 'Bgp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg', 'Vrfs.Vrf.Afs.Af.Bgp', 
                [], [], 
                '''                BGP AF VRF config
                ''',
                'bgp',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('create', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                VRF configuration for a particular address
                family
                ''',
                'create',
                'Cisco-IOS-XR-infra-rsi-cfg', False),
            _MetaInfoClassMember('maximum-prefix', REFERENCE_CLASS, 'MaximumPrefix' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg', 'Vrfs.Vrf.Afs.Af.MaximumPrefix', 
                [], [], 
                '''                Set maximum prefix limits
                ''',
                'maximum_prefix',
                'Cisco-IOS-XR-ip-rib-cfg', False),
            ],
            'Cisco-IOS-XR-infra-rsi-cfg',
            'af',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rsi-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg'
        ),
    },
    'Vrfs.Vrf.Afs' : {
        'meta_info' : _MetaInfoClass('Vrfs.Vrf.Afs',
            False, 
            [
            _MetaInfoClassMember('af', REFERENCE_LIST, 'Af' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg', 'Vrfs.Vrf.Afs.Af', 
                [], [], 
                '''                VRF address family configuration
                ''',
                'af',
                'Cisco-IOS-XR-infra-rsi-cfg', False),
            ],
            'Cisco-IOS-XR-infra-rsi-cfg',
            'afs',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rsi-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg'
        ),
    },
    'Vrfs.Vrf.MulticastHost.Ipv4' : {
        'meta_info' : _MetaInfoClass('Vrfs.Vrf.MulticastHost.Ipv4',
            False, 
            [
            _MetaInfoClassMember('interface', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Default multicast host interface name
                ''',
                'interface',
                'Cisco-IOS-XR-ip-iarm-vrf-cfg', False),
            ],
            'Cisco-IOS-XR-ip-iarm-vrf-cfg',
            'ipv4',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-iarm-vrf-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg'
        ),
    },
    'Vrfs.Vrf.MulticastHost.Ipv6' : {
        'meta_info' : _MetaInfoClass('Vrfs.Vrf.MulticastHost.Ipv6',
            False, 
            [
            _MetaInfoClassMember('interface', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Default multicast host interface name
                ''',
                'interface',
                'Cisco-IOS-XR-ip-iarm-vrf-cfg', False),
            ],
            'Cisco-IOS-XR-ip-iarm-vrf-cfg',
            'ipv6',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-iarm-vrf-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg'
        ),
    },
    'Vrfs.Vrf.MulticastHost' : {
        'meta_info' : _MetaInfoClass('Vrfs.Vrf.MulticastHost',
            False, 
            [
            _MetaInfoClassMember('ipv4', REFERENCE_CLASS, 'Ipv4' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg', 'Vrfs.Vrf.MulticastHost.Ipv4', 
                [], [], 
                '''                IPv4 configuration
                ''',
                'ipv4',
                'Cisco-IOS-XR-ip-iarm-vrf-cfg', False),
            _MetaInfoClassMember('ipv6', REFERENCE_CLASS, 'Ipv6' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg', 'Vrfs.Vrf.MulticastHost.Ipv6', 
                [], [], 
                '''                IPv6 configuration
                ''',
                'ipv6',
                'Cisco-IOS-XR-ip-iarm-vrf-cfg', False),
            ],
            'Cisco-IOS-XR-ip-iarm-vrf-cfg',
            'multicast-host',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-iarm-vrf-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg'
        ),
    },
    'Vrfs.Vrf' : {
        'meta_info' : _MetaInfoClass('Vrfs.Vrf',
            False, 
            [
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                VRF name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-infra-rsi-cfg', True),
            _MetaInfoClassMember('afs', REFERENCE_CLASS, 'Afs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg', 'Vrfs.Vrf.Afs', 
                [], [], 
                '''                VRF address family configuration
                ''',
                'afs',
                'Cisco-IOS-XR-infra-rsi-cfg', False),
            _MetaInfoClassMember('create', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                VRF global configuration
                ''',
                'create',
                'Cisco-IOS-XR-infra-rsi-cfg', False),
            _MetaInfoClassMember('description', ATTRIBUTE, 'str' , None, None, 
                [(1, 244)], [], 
                '''                A textual description of the VRF
                ''',
                'description',
                'Cisco-IOS-XR-infra-rsi-cfg', False),
            _MetaInfoClassMember('fallback-vrf', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                Fallback VRF
                ''',
                'fallback_vrf',
                'Cisco-IOS-XR-infra-rsi-cfg', False),
            _MetaInfoClassMember('mode-big', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Configuration enable of big VRF
                ''',
                'mode_big',
                'Cisco-IOS-XR-infra-rsi-cfg', False),
            _MetaInfoClassMember('multicast-host', REFERENCE_CLASS, 'MulticastHost' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg', 'Vrfs.Vrf.MulticastHost', 
                [], [], 
                '''                Multicast host stack configuration
                ''',
                'multicast_host',
                'Cisco-IOS-XR-ip-iarm-vrf-cfg', False),
            _MetaInfoClassMember('remote-route-filter-disable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                For disabling remote route filtering for this
                VRF on core-facing card
                ''',
                'remote_route_filter_disable',
                'Cisco-IOS-XR-infra-rsi-cfg', False),
            _MetaInfoClassMember('vpn-id', REFERENCE_CLASS, 'VpnId' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg', 'Vrfs.Vrf.VpnId', 
                [], [], 
                '''                VPN-ID for the VRF
                ''',
                'vpn_id',
                'Cisco-IOS-XR-infra-rsi-cfg', False),
            ],
            'Cisco-IOS-XR-infra-rsi-cfg',
            'vrf',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rsi-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg'
        ),
    },
    'Vrfs' : {
        'meta_info' : _MetaInfoClass('Vrfs',
            False, 
            [
            _MetaInfoClassMember('vrf', REFERENCE_LIST, 'Vrf' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg', 'Vrfs.Vrf', 
                [], [], 
                '''                VRF configuration
                ''',
                'vrf',
                'Cisco-IOS-XR-infra-rsi-cfg', False),
            ],
            'Cisco-IOS-XR-infra-rsi-cfg',
            'vrfs',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rsi-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg'
        ),
    },
    'GlobalAf.Afs.Af' : {
        'meta_info' : _MetaInfoClass('GlobalAf.Afs.Af',
            False, 
            [
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'VrfAddressFamilyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg', 'VrfAddressFamilyEnum', 
                [], [], 
                '''                Address family
                ''',
                'af_name',
                'Cisco-IOS-XR-infra-rsi-cfg', True),
            _MetaInfoClassMember('saf-name', REFERENCE_ENUM_CLASS, 'VrfSubAddressFamilyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg', 'VrfSubAddressFamilyEnum', 
                [], [], 
                '''                Sub-Address family
                ''',
                'saf_name',
                'Cisco-IOS-XR-infra-rsi-cfg', True),
            _MetaInfoClassMember('topology-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 244)], [], 
                '''                Topology name
                ''',
                'topology_name',
                'Cisco-IOS-XR-infra-rsi-cfg', True),
            _MetaInfoClassMember('create', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                VRF configuration for a particular address
                family
                ''',
                'create',
                'Cisco-IOS-XR-infra-rsi-cfg', False),
            ],
            'Cisco-IOS-XR-infra-rsi-cfg',
            'af',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rsi-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg'
        ),
    },
    'GlobalAf.Afs' : {
        'meta_info' : _MetaInfoClass('GlobalAf.Afs',
            False, 
            [
            _MetaInfoClassMember('af', REFERENCE_LIST, 'Af' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg', 'GlobalAf.Afs.Af', 
                [], [], 
                '''                VRF address family configuration
                ''',
                'af',
                'Cisco-IOS-XR-infra-rsi-cfg', False),
            ],
            'Cisco-IOS-XR-infra-rsi-cfg',
            'afs',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rsi-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg'
        ),
    },
    'GlobalAf' : {
        'meta_info' : _MetaInfoClass('GlobalAf',
            False, 
            [
            _MetaInfoClassMember('afs', REFERENCE_CLASS, 'Afs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg', 'GlobalAf.Afs', 
                [], [], 
                '''                VRF address family configuration
                ''',
                'afs',
                'Cisco-IOS-XR-infra-rsi-cfg', False),
            ],
            'Cisco-IOS-XR-infra-rsi-cfg',
            'global-af',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rsi-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg'
        ),
    },
    'Srlg.Interfaces.Interface.IncludeOptical' : {
        'meta_info' : _MetaInfoClass('Srlg.Interfaces.Interface.IncludeOptical',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable SRLG interface include optical
                ''',
                'enable',
                'Cisco-IOS-XR-infra-rsi-cfg', False),
            _MetaInfoClassMember('priority', REFERENCE_ENUM_CLASS, 'SrlgPriorityEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg', 'SrlgPriorityEnum', 
                [], [], 
                '''                Priority for optical domain values
                ''',
                'priority',
                'Cisco-IOS-XR-infra-rsi-cfg', False),
            ],
            'Cisco-IOS-XR-infra-rsi-cfg',
            'include-optical',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rsi-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg'
        ),
    },
    'Srlg.Interfaces.Interface.InterfaceGroup.GroupNames.GroupName' : {
        'meta_info' : _MetaInfoClass('Srlg.Interfaces.Interface.InterfaceGroup.GroupNames.GroupName',
            False, 
            [
            _MetaInfoClassMember('group-name-index', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Group name index
                ''',
                'group_name_index',
                'Cisco-IOS-XR-infra-rsi-cfg', True),
            _MetaInfoClassMember('group-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Group name
                ''',
                'group_name',
                'Cisco-IOS-XR-infra-rsi-cfg', False),
            _MetaInfoClassMember('srlg-priority', REFERENCE_ENUM_CLASS, 'SrlgPriorityEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg', 'SrlgPriorityEnum', 
                [], [], 
                '''                SRLG priority
                ''',
                'srlg_priority',
                'Cisco-IOS-XR-infra-rsi-cfg', False),
            ],
            'Cisco-IOS-XR-infra-rsi-cfg',
            'group-name',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rsi-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg'
        ),
    },
    'Srlg.Interfaces.Interface.InterfaceGroup.GroupNames' : {
        'meta_info' : _MetaInfoClass('Srlg.Interfaces.Interface.InterfaceGroup.GroupNames',
            False, 
            [
            _MetaInfoClassMember('group-name', REFERENCE_LIST, 'GroupName' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg', 'Srlg.Interfaces.Interface.InterfaceGroup.GroupNames.GroupName', 
                [], [], 
                '''                Group name included under interface
                ''',
                'group_name',
                'Cisco-IOS-XR-infra-rsi-cfg', False),
            ],
            'Cisco-IOS-XR-infra-rsi-cfg',
            'group-names',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rsi-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg'
        ),
    },
    'Srlg.Interfaces.Interface.InterfaceGroup' : {
        'meta_info' : _MetaInfoClass('Srlg.Interfaces.Interface.InterfaceGroup',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable SRLG interface group submode
                ''',
                'enable',
                'Cisco-IOS-XR-infra-rsi-cfg', False),
            _MetaInfoClassMember('group-names', REFERENCE_CLASS, 'GroupNames' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg', 'Srlg.Interfaces.Interface.InterfaceGroup.GroupNames', 
                [], [], 
                '''                Set of group name under an interface
                ''',
                'group_names',
                'Cisco-IOS-XR-infra-rsi-cfg', False),
            ],
            'Cisco-IOS-XR-infra-rsi-cfg',
            'interface-group',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rsi-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg'
        ),
    },
    'Srlg.Interfaces.Interface.Values.Value' : {
        'meta_info' : _MetaInfoClass('Srlg.Interfaces.Interface.Values.Value',
            False, 
            [
            _MetaInfoClassMember('srlg-index', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                SRLG index
                ''',
                'srlg_index',
                'Cisco-IOS-XR-infra-rsi-cfg', True),
            _MetaInfoClassMember('srlg-priority', REFERENCE_ENUM_CLASS, 'SrlgPriorityEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg', 'SrlgPriorityEnum', 
                [], [], 
                '''                SRLG priority
                ''',
                'srlg_priority',
                'Cisco-IOS-XR-infra-rsi-cfg', False),
            _MetaInfoClassMember('srlg-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                SRLG value
                ''',
                'srlg_value',
                'Cisco-IOS-XR-infra-rsi-cfg', False),
            ],
            'Cisco-IOS-XR-infra-rsi-cfg',
            'value',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rsi-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg'
        ),
    },
    'Srlg.Interfaces.Interface.Values' : {
        'meta_info' : _MetaInfoClass('Srlg.Interfaces.Interface.Values',
            False, 
            [
            _MetaInfoClassMember('value', REFERENCE_LIST, 'Value' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg', 'Srlg.Interfaces.Interface.Values.Value', 
                [], [], 
                '''                SRLG value data
                ''',
                'value',
                'Cisco-IOS-XR-infra-rsi-cfg', False),
            ],
            'Cisco-IOS-XR-infra-rsi-cfg',
            'values',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rsi-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg'
        ),
    },
    'Srlg.Interfaces.Interface.InterfaceSrlgNames.InterfaceSrlgName' : {
        'meta_info' : _MetaInfoClass('Srlg.Interfaces.Interface.InterfaceSrlgNames.InterfaceSrlgName',
            False, 
            [
            _MetaInfoClassMember('srlg-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                SRLG name
                ''',
                'srlg_name',
                'Cisco-IOS-XR-infra-rsi-cfg', True),
            ],
            'Cisco-IOS-XR-infra-rsi-cfg',
            'interface-srlg-name',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rsi-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg'
        ),
    },
    'Srlg.Interfaces.Interface.InterfaceSrlgNames' : {
        'meta_info' : _MetaInfoClass('Srlg.Interfaces.Interface.InterfaceSrlgNames',
            False, 
            [
            _MetaInfoClassMember('interface-srlg-name', REFERENCE_LIST, 'InterfaceSrlgName' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg', 'Srlg.Interfaces.Interface.InterfaceSrlgNames.InterfaceSrlgName', 
                [], [], 
                '''                SRLG name data
                ''',
                'interface_srlg_name',
                'Cisco-IOS-XR-infra-rsi-cfg', False),
            ],
            'Cisco-IOS-XR-infra-rsi-cfg',
            'interface-srlg-names',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rsi-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg'
        ),
    },
    'Srlg.Interfaces.Interface' : {
        'meta_info' : _MetaInfoClass('Srlg.Interfaces.Interface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface name
                ''',
                'interface_name',
                'Cisco-IOS-XR-infra-rsi-cfg', True),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable SRLG interface
                ''',
                'enable',
                'Cisco-IOS-XR-infra-rsi-cfg', False),
            _MetaInfoClassMember('include-optical', REFERENCE_CLASS, 'IncludeOptical' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg', 'Srlg.Interfaces.Interface.IncludeOptical', 
                [], [], 
                '''                Include optical configuration for an interface
                ''',
                'include_optical',
                'Cisco-IOS-XR-infra-rsi-cfg', False),
            _MetaInfoClassMember('interface-group', REFERENCE_CLASS, 'InterfaceGroup' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg', 'Srlg.Interfaces.Interface.InterfaceGroup', 
                [], [], 
                '''                Group configuration for an interface
                ''',
                'interface_group',
                'Cisco-IOS-XR-infra-rsi-cfg', False),
            _MetaInfoClassMember('interface-srlg-names', REFERENCE_CLASS, 'InterfaceSrlgNames' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg', 'Srlg.Interfaces.Interface.InterfaceSrlgNames', 
                [], [], 
                '''                SRLG Name configuration for an interface
                ''',
                'interface_srlg_names',
                'Cisco-IOS-XR-infra-rsi-cfg', False),
            _MetaInfoClassMember('values', REFERENCE_CLASS, 'Values' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg', 'Srlg.Interfaces.Interface.Values', 
                [], [], 
                '''                SRLG Value configuration for an interface
                ''',
                'values',
                'Cisco-IOS-XR-infra-rsi-cfg', False),
            ],
            'Cisco-IOS-XR-infra-rsi-cfg',
            'interface',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rsi-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg'
        ),
    },
    'Srlg.Interfaces' : {
        'meta_info' : _MetaInfoClass('Srlg.Interfaces',
            False, 
            [
            _MetaInfoClassMember('interface', REFERENCE_LIST, 'Interface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg', 'Srlg.Interfaces.Interface', 
                [], [], 
                '''                Interface configurations
                ''',
                'interface',
                'Cisco-IOS-XR-infra-rsi-cfg', False),
            ],
            'Cisco-IOS-XR-infra-rsi-cfg',
            'interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rsi-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg'
        ),
    },
    'Srlg.SrlgNames.SrlgName' : {
        'meta_info' : _MetaInfoClass('Srlg.SrlgNames.SrlgName',
            False, 
            [
            _MetaInfoClassMember('srlg-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                SRLG name
                ''',
                'srlg_name',
                'Cisco-IOS-XR-infra-rsi-cfg', True),
            _MetaInfoClassMember('srlg-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                SRLG value
                ''',
                'srlg_value',
                'Cisco-IOS-XR-infra-rsi-cfg', False),
            ],
            'Cisco-IOS-XR-infra-rsi-cfg',
            'srlg-name',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rsi-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg'
        ),
    },
    'Srlg.SrlgNames' : {
        'meta_info' : _MetaInfoClass('Srlg.SrlgNames',
            False, 
            [
            _MetaInfoClassMember('srlg-name', REFERENCE_LIST, 'SrlgName' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg', 'Srlg.SrlgNames.SrlgName', 
                [], [], 
                '''                SRLG name configuration
                ''',
                'srlg_name',
                'Cisco-IOS-XR-infra-rsi-cfg', False),
            ],
            'Cisco-IOS-XR-infra-rsi-cfg',
            'srlg-names',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rsi-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg'
        ),
    },
    'Srlg.Groups.Group.GroupValues.GroupValue' : {
        'meta_info' : _MetaInfoClass('Srlg.Groups.Group.GroupValues.GroupValue',
            False, 
            [
            _MetaInfoClassMember('srlg-index', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                SRLG index
                ''',
                'srlg_index',
                'Cisco-IOS-XR-infra-rsi-cfg', True),
            _MetaInfoClassMember('srlg-priority', REFERENCE_ENUM_CLASS, 'SrlgPriorityEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg', 'SrlgPriorityEnum', 
                [], [], 
                '''                SRLG priority
                ''',
                'srlg_priority',
                'Cisco-IOS-XR-infra-rsi-cfg', False),
            _MetaInfoClassMember('srlg-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                SRLG value
                ''',
                'srlg_value',
                'Cisco-IOS-XR-infra-rsi-cfg', False),
            ],
            'Cisco-IOS-XR-infra-rsi-cfg',
            'group-value',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rsi-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg'
        ),
    },
    'Srlg.Groups.Group.GroupValues' : {
        'meta_info' : _MetaInfoClass('Srlg.Groups.Group.GroupValues',
            False, 
            [
            _MetaInfoClassMember('group-value', REFERENCE_LIST, 'GroupValue' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg', 'Srlg.Groups.Group.GroupValues.GroupValue', 
                [], [], 
                '''                Group SRLG values with attribute
                ''',
                'group_value',
                'Cisco-IOS-XR-infra-rsi-cfg', False),
            ],
            'Cisco-IOS-XR-infra-rsi-cfg',
            'group-values',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rsi-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg'
        ),
    },
    'Srlg.Groups.Group' : {
        'meta_info' : _MetaInfoClass('Srlg.Groups.Group',
            False, 
            [
            _MetaInfoClassMember('group-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Group name
                ''',
                'group_name',
                'Cisco-IOS-XR-infra-rsi-cfg', True),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable SRLG group
                ''',
                'enable',
                'Cisco-IOS-XR-infra-rsi-cfg', False),
            _MetaInfoClassMember('group-values', REFERENCE_CLASS, 'GroupValues' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg', 'Srlg.Groups.Group.GroupValues', 
                [], [], 
                '''                Set of SRLG values configured under a group
                ''',
                'group_values',
                'Cisco-IOS-XR-infra-rsi-cfg', False),
            ],
            'Cisco-IOS-XR-infra-rsi-cfg',
            'group',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rsi-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg'
        ),
    },
    'Srlg.Groups' : {
        'meta_info' : _MetaInfoClass('Srlg.Groups',
            False, 
            [
            _MetaInfoClassMember('group', REFERENCE_LIST, 'Group' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg', 'Srlg.Groups.Group', 
                [], [], 
                '''                Group configurations
                ''',
                'group',
                'Cisco-IOS-XR-infra-rsi-cfg', False),
            ],
            'Cisco-IOS-XR-infra-rsi-cfg',
            'groups',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rsi-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg'
        ),
    },
    'Srlg.InheritNodes.InheritNode.InheritNodeValues.InheritNodeValue' : {
        'meta_info' : _MetaInfoClass('Srlg.InheritNodes.InheritNode.InheritNodeValues.InheritNodeValue',
            False, 
            [
            _MetaInfoClassMember('srlg-index', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                SRLG index
                ''',
                'srlg_index',
                'Cisco-IOS-XR-infra-rsi-cfg', True),
            _MetaInfoClassMember('srlg-priority', REFERENCE_ENUM_CLASS, 'SrlgPriorityEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg', 'SrlgPriorityEnum', 
                [], [], 
                '''                SRLG priority
                ''',
                'srlg_priority',
                'Cisco-IOS-XR-infra-rsi-cfg', False),
            _MetaInfoClassMember('srlg-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                SRLG value
                ''',
                'srlg_value',
                'Cisco-IOS-XR-infra-rsi-cfg', False),
            ],
            'Cisco-IOS-XR-infra-rsi-cfg',
            'inherit-node-value',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rsi-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg'
        ),
    },
    'Srlg.InheritNodes.InheritNode.InheritNodeValues' : {
        'meta_info' : _MetaInfoClass('Srlg.InheritNodes.InheritNode.InheritNodeValues',
            False, 
            [
            _MetaInfoClassMember('inherit-node-value', REFERENCE_LIST, 'InheritNodeValue' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg', 'Srlg.InheritNodes.InheritNode.InheritNodeValues.InheritNodeValue', 
                [], [], 
                '''                Inherit node SRLG value with attributes
                ''',
                'inherit_node_value',
                'Cisco-IOS-XR-infra-rsi-cfg', False),
            ],
            'Cisco-IOS-XR-infra-rsi-cfg',
            'inherit-node-values',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rsi-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg'
        ),
    },
    'Srlg.InheritNodes.InheritNode' : {
        'meta_info' : _MetaInfoClass('Srlg.InheritNodes.InheritNode',
            False, 
            [
            _MetaInfoClassMember('inherit-node-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'((([a-zA-Z0-9_]*\\d+)|(\\*))/){2}(([a-zA-Z0-9_]*\\d+)|(\\*))'], 
                '''                The inherit node name
                ''',
                'inherit_node_name',
                'Cisco-IOS-XR-infra-rsi-cfg', True),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable SRLG inherit node
                ''',
                'enable',
                'Cisco-IOS-XR-infra-rsi-cfg', False),
            _MetaInfoClassMember('inherit-node-values', REFERENCE_CLASS, 'InheritNodeValues' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg', 'Srlg.InheritNodes.InheritNode.InheritNodeValues', 
                [], [], 
                '''                Set of SRLG values configured under an inherit
                node
                ''',
                'inherit_node_values',
                'Cisco-IOS-XR-infra-rsi-cfg', False),
            ],
            'Cisco-IOS-XR-infra-rsi-cfg',
            'inherit-node',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rsi-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg'
        ),
    },
    'Srlg.InheritNodes' : {
        'meta_info' : _MetaInfoClass('Srlg.InheritNodes',
            False, 
            [
            _MetaInfoClassMember('inherit-node', REFERENCE_LIST, 'InheritNode' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg', 'Srlg.InheritNodes.InheritNode', 
                [], [], 
                '''                Inherit node configurations
                ''',
                'inherit_node',
                'Cisco-IOS-XR-infra-rsi-cfg', False),
            ],
            'Cisco-IOS-XR-infra-rsi-cfg',
            'inherit-nodes',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rsi-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg'
        ),
    },
    'Srlg' : {
        'meta_info' : _MetaInfoClass('Srlg',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable SRLG
                ''',
                'enable',
                'Cisco-IOS-XR-infra-rsi-cfg', False),
            _MetaInfoClassMember('groups', REFERENCE_CLASS, 'Groups' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg', 'Srlg.Groups', 
                [], [], 
                '''                Set of groups configured with SRLG
                ''',
                'groups',
                'Cisco-IOS-XR-infra-rsi-cfg', False),
            _MetaInfoClassMember('inherit-nodes', REFERENCE_CLASS, 'InheritNodes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg', 'Srlg.InheritNodes', 
                [], [], 
                '''                Set of inherit nodes configured with SRLG
                ''',
                'inherit_nodes',
                'Cisco-IOS-XR-infra-rsi-cfg', False),
            _MetaInfoClassMember('interfaces', REFERENCE_CLASS, 'Interfaces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg', 'Srlg.Interfaces', 
                [], [], 
                '''                Set of interfaces configured with SRLG
                ''',
                'interfaces',
                'Cisco-IOS-XR-infra-rsi-cfg', False),
            _MetaInfoClassMember('srlg-names', REFERENCE_CLASS, 'SrlgNames' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg', 'Srlg.SrlgNames', 
                [], [], 
                '''                Set of SRLG name configuration
                ''',
                'srlg_names',
                'Cisco-IOS-XR-infra-rsi-cfg', False),
            ],
            'Cisco-IOS-XR-infra-rsi-cfg',
            'srlg',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rsi-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg'
        ),
    },
    'VrfGroups.VrfGroup.Vrfs.Vrf' : {
        'meta_info' : _MetaInfoClass('VrfGroups.VrfGroup.Vrfs.Vrf',
            False, 
            [
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                VRF name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-infra-rsi-cfg', True),
            ],
            'Cisco-IOS-XR-infra-rsi-cfg',
            'vrf',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rsi-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg'
        ),
    },
    'VrfGroups.VrfGroup.Vrfs' : {
        'meta_info' : _MetaInfoClass('VrfGroups.VrfGroup.Vrfs',
            False, 
            [
            _MetaInfoClassMember('vrf', REFERENCE_LIST, 'Vrf' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg', 'VrfGroups.VrfGroup.Vrfs.Vrf', 
                [], [], 
                '''                VRF configuration
                ''',
                'vrf',
                'Cisco-IOS-XR-infra-rsi-cfg', False),
            ],
            'Cisco-IOS-XR-infra-rsi-cfg',
            'vrfs',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rsi-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg'
        ),
    },
    'VrfGroups.VrfGroup' : {
        'meta_info' : _MetaInfoClass('VrfGroups.VrfGroup',
            False, 
            [
            _MetaInfoClassMember('vrf-group-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                VRF group name
                ''',
                'vrf_group_name',
                'Cisco-IOS-XR-infra-rsi-cfg', True),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable VRF group
                ''',
                'enable',
                'Cisco-IOS-XR-infra-rsi-cfg', False),
            _MetaInfoClassMember('vrfs', REFERENCE_CLASS, 'Vrfs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg', 'VrfGroups.VrfGroup.Vrfs', 
                [], [], 
                '''                Set of VRFs configured under a VRF group
                ''',
                'vrfs',
                'Cisco-IOS-XR-infra-rsi-cfg', False),
            ],
            'Cisco-IOS-XR-infra-rsi-cfg',
            'vrf-group',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rsi-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg'
        ),
    },
    'VrfGroups' : {
        'meta_info' : _MetaInfoClass('VrfGroups',
            False, 
            [
            _MetaInfoClassMember('vrf-group', REFERENCE_LIST, 'VrfGroup' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg', 'VrfGroups.VrfGroup', 
                [], [], 
                '''                VRF group configuration
                ''',
                'vrf_group',
                'Cisco-IOS-XR-infra-rsi-cfg', False),
            ],
            'Cisco-IOS-XR-infra-rsi-cfg',
            'vrf-groups',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rsi-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg'
        ),
    },
    'SelectiveVrfDownload' : {
        'meta_info' : _MetaInfoClass('SelectiveVrfDownload',
            False, 
            [
            _MetaInfoClassMember('disable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Disable selective VRF download
                ''',
                'disable',
                'Cisco-IOS-XR-infra-rsi-cfg', False),
            ],
            'Cisco-IOS-XR-infra-rsi-cfg',
            'selective-vrf-download',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rsi-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rsi_cfg'
        ),
    },
}
_meta_table['Vrfs.Vrf.Afs.Af.Bgp.ImportRouteTargets.RouteTargets.RouteTarget.AsOrFourByteAs']['meta_info'].parent =_meta_table['Vrfs.Vrf.Afs.Af.Bgp.ImportRouteTargets.RouteTargets.RouteTarget']['meta_info']
_meta_table['Vrfs.Vrf.Afs.Af.Bgp.ImportRouteTargets.RouteTargets.RouteTarget.Ipv4Address']['meta_info'].parent =_meta_table['Vrfs.Vrf.Afs.Af.Bgp.ImportRouteTargets.RouteTargets.RouteTarget']['meta_info']
_meta_table['Vrfs.Vrf.Afs.Af.Bgp.ImportRouteTargets.RouteTargets.RouteTarget']['meta_info'].parent =_meta_table['Vrfs.Vrf.Afs.Af.Bgp.ImportRouteTargets.RouteTargets']['meta_info']
_meta_table['Vrfs.Vrf.Afs.Af.Bgp.ImportRouteTargets.RouteTargets']['meta_info'].parent =_meta_table['Vrfs.Vrf.Afs.Af.Bgp.ImportRouteTargets']['meta_info']
_meta_table['Vrfs.Vrf.Afs.Af.Bgp.ExportRouteTargets.RouteTargets.RouteTarget.AsOrFourByteAs']['meta_info'].parent =_meta_table['Vrfs.Vrf.Afs.Af.Bgp.ExportRouteTargets.RouteTargets.RouteTarget']['meta_info']
_meta_table['Vrfs.Vrf.Afs.Af.Bgp.ExportRouteTargets.RouteTargets.RouteTarget.Ipv4Address']['meta_info'].parent =_meta_table['Vrfs.Vrf.Afs.Af.Bgp.ExportRouteTargets.RouteTargets.RouteTarget']['meta_info']
_meta_table['Vrfs.Vrf.Afs.Af.Bgp.ExportRouteTargets.RouteTargets.RouteTarget']['meta_info'].parent =_meta_table['Vrfs.Vrf.Afs.Af.Bgp.ExportRouteTargets.RouteTargets']['meta_info']
_meta_table['Vrfs.Vrf.Afs.Af.Bgp.ExportRouteTargets.RouteTargets']['meta_info'].parent =_meta_table['Vrfs.Vrf.Afs.Af.Bgp.ExportRouteTargets']['meta_info']
_meta_table['Vrfs.Vrf.Afs.Af.Bgp.ImportRouteTargets']['meta_info'].parent =_meta_table['Vrfs.Vrf.Afs.Af.Bgp']['meta_info']
_meta_table['Vrfs.Vrf.Afs.Af.Bgp.ExportRouteTargets']['meta_info'].parent =_meta_table['Vrfs.Vrf.Afs.Af.Bgp']['meta_info']
_meta_table['Vrfs.Vrf.Afs.Af.Bgp.VrfToGlobalExportRoutePolicy']['meta_info'].parent =_meta_table['Vrfs.Vrf.Afs.Af.Bgp']['meta_info']
_meta_table['Vrfs.Vrf.Afs.Af.Bgp.ExportVrfOptions']['meta_info'].parent =_meta_table['Vrfs.Vrf.Afs.Af.Bgp']['meta_info']
_meta_table['Vrfs.Vrf.Afs.Af.Bgp.GlobalToVrfImportRoutePolicy']['meta_info'].parent =_meta_table['Vrfs.Vrf.Afs.Af.Bgp']['meta_info']
_meta_table['Vrfs.Vrf.Afs.Af.MaximumPrefix']['meta_info'].parent =_meta_table['Vrfs.Vrf.Afs.Af']['meta_info']
_meta_table['Vrfs.Vrf.Afs.Af.Bgp']['meta_info'].parent =_meta_table['Vrfs.Vrf.Afs.Af']['meta_info']
_meta_table['Vrfs.Vrf.Afs.Af']['meta_info'].parent =_meta_table['Vrfs.Vrf.Afs']['meta_info']
_meta_table['Vrfs.Vrf.MulticastHost.Ipv4']['meta_info'].parent =_meta_table['Vrfs.Vrf.MulticastHost']['meta_info']
_meta_table['Vrfs.Vrf.MulticastHost.Ipv6']['meta_info'].parent =_meta_table['Vrfs.Vrf.MulticastHost']['meta_info']
_meta_table['Vrfs.Vrf.VpnId']['meta_info'].parent =_meta_table['Vrfs.Vrf']['meta_info']
_meta_table['Vrfs.Vrf.Afs']['meta_info'].parent =_meta_table['Vrfs.Vrf']['meta_info']
_meta_table['Vrfs.Vrf.MulticastHost']['meta_info'].parent =_meta_table['Vrfs.Vrf']['meta_info']
_meta_table['Vrfs.Vrf']['meta_info'].parent =_meta_table['Vrfs']['meta_info']
_meta_table['GlobalAf.Afs.Af']['meta_info'].parent =_meta_table['GlobalAf.Afs']['meta_info']
_meta_table['GlobalAf.Afs']['meta_info'].parent =_meta_table['GlobalAf']['meta_info']
_meta_table['Srlg.Interfaces.Interface.InterfaceGroup.GroupNames.GroupName']['meta_info'].parent =_meta_table['Srlg.Interfaces.Interface.InterfaceGroup.GroupNames']['meta_info']
_meta_table['Srlg.Interfaces.Interface.InterfaceGroup.GroupNames']['meta_info'].parent =_meta_table['Srlg.Interfaces.Interface.InterfaceGroup']['meta_info']
_meta_table['Srlg.Interfaces.Interface.Values.Value']['meta_info'].parent =_meta_table['Srlg.Interfaces.Interface.Values']['meta_info']
_meta_table['Srlg.Interfaces.Interface.InterfaceSrlgNames.InterfaceSrlgName']['meta_info'].parent =_meta_table['Srlg.Interfaces.Interface.InterfaceSrlgNames']['meta_info']
_meta_table['Srlg.Interfaces.Interface.IncludeOptical']['meta_info'].parent =_meta_table['Srlg.Interfaces.Interface']['meta_info']
_meta_table['Srlg.Interfaces.Interface.InterfaceGroup']['meta_info'].parent =_meta_table['Srlg.Interfaces.Interface']['meta_info']
_meta_table['Srlg.Interfaces.Interface.Values']['meta_info'].parent =_meta_table['Srlg.Interfaces.Interface']['meta_info']
_meta_table['Srlg.Interfaces.Interface.InterfaceSrlgNames']['meta_info'].parent =_meta_table['Srlg.Interfaces.Interface']['meta_info']
_meta_table['Srlg.Interfaces.Interface']['meta_info'].parent =_meta_table['Srlg.Interfaces']['meta_info']
_meta_table['Srlg.SrlgNames.SrlgName']['meta_info'].parent =_meta_table['Srlg.SrlgNames']['meta_info']
_meta_table['Srlg.Groups.Group.GroupValues.GroupValue']['meta_info'].parent =_meta_table['Srlg.Groups.Group.GroupValues']['meta_info']
_meta_table['Srlg.Groups.Group.GroupValues']['meta_info'].parent =_meta_table['Srlg.Groups.Group']['meta_info']
_meta_table['Srlg.Groups.Group']['meta_info'].parent =_meta_table['Srlg.Groups']['meta_info']
_meta_table['Srlg.InheritNodes.InheritNode.InheritNodeValues.InheritNodeValue']['meta_info'].parent =_meta_table['Srlg.InheritNodes.InheritNode.InheritNodeValues']['meta_info']
_meta_table['Srlg.InheritNodes.InheritNode.InheritNodeValues']['meta_info'].parent =_meta_table['Srlg.InheritNodes.InheritNode']['meta_info']
_meta_table['Srlg.InheritNodes.InheritNode']['meta_info'].parent =_meta_table['Srlg.InheritNodes']['meta_info']
_meta_table['Srlg.Interfaces']['meta_info'].parent =_meta_table['Srlg']['meta_info']
_meta_table['Srlg.SrlgNames']['meta_info'].parent =_meta_table['Srlg']['meta_info']
_meta_table['Srlg.Groups']['meta_info'].parent =_meta_table['Srlg']['meta_info']
_meta_table['Srlg.InheritNodes']['meta_info'].parent =_meta_table['Srlg']['meta_info']
_meta_table['VrfGroups.VrfGroup.Vrfs.Vrf']['meta_info'].parent =_meta_table['VrfGroups.VrfGroup.Vrfs']['meta_info']
_meta_table['VrfGroups.VrfGroup.Vrfs']['meta_info'].parent =_meta_table['VrfGroups.VrfGroup']['meta_info']
_meta_table['VrfGroups.VrfGroup']['meta_info'].parent =_meta_table['VrfGroups']['meta_info']
