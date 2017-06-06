


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'MplsVpnAfiEnum' : _MetaInfoEnum('MplsVpnAfiEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_vpn_oper',
        {
            'ipv4':'ipv4',
            'ipv6':'ipv6',
        }, 'Cisco-IOS-XR-mpls-vpn-oper', _yang_ns._namespaces['Cisco-IOS-XR-mpls-vpn-oper']),
    'MplsVpnRtEnum' : _MetaInfoEnum('MplsVpnRtEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_vpn_oper',
        {
            'import':'import_',
            'export':'export',
            'both':'both',
        }, 'Cisco-IOS-XR-mpls-vpn-oper', _yang_ns._namespaces['Cisco-IOS-XR-mpls-vpn-oper']),
    'MplsVpnSafiEnum' : _MetaInfoEnum('MplsVpnSafiEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_vpn_oper',
        {
            'unicast':'unicast',
            'multicast':'multicast',
            'flowspec':'flowspec',
        }, 'Cisco-IOS-XR-mpls-vpn-oper', _yang_ns._namespaces['Cisco-IOS-XR-mpls-vpn-oper']),
    'L3Vpn.InvalidVrfs.InvalidVrf.Interface' : {
        'meta_info' : _MetaInfoClass('L3Vpn.InvalidVrfs.InvalidVrf.Interface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-mpls-vpn-oper', False),
            ],
            'Cisco-IOS-XR-mpls-vpn-oper',
            'interface',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-vpn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_vpn_oper'
        ),
    },
    'L3Vpn.InvalidVrfs.InvalidVrf.Af.RouteTarget' : {
        'meta_info' : _MetaInfoClass('L3Vpn.InvalidVrfs.InvalidVrf.Af.RouteTarget',
            False, 
            [
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'MplsVpnAfiEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_vpn_oper', 'MplsVpnAfiEnum', 
                [], [], 
                '''                AF name
                ''',
                'af_name',
                'Cisco-IOS-XR-mpls-vpn-oper', False),
            _MetaInfoClassMember('route-target-type', REFERENCE_ENUM_CLASS, 'MplsVpnRtEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_vpn_oper', 'MplsVpnRtEnum', 
                [], [], 
                '''                Route Target Type
                ''',
                'route_target_type',
                'Cisco-IOS-XR-mpls-vpn-oper', False),
            _MetaInfoClassMember('route-target-value', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Route Target Value
                ''',
                'route_target_value',
                'Cisco-IOS-XR-mpls-vpn-oper', False),
            _MetaInfoClassMember('saf-name', REFERENCE_ENUM_CLASS, 'MplsVpnSafiEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_vpn_oper', 'MplsVpnSafiEnum', 
                [], [], 
                '''                SAF name
                ''',
                'saf_name',
                'Cisco-IOS-XR-mpls-vpn-oper', False),
            ],
            'Cisco-IOS-XR-mpls-vpn-oper',
            'route-target',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-vpn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_vpn_oper'
        ),
    },
    'L3Vpn.InvalidVrfs.InvalidVrf.Af' : {
        'meta_info' : _MetaInfoClass('L3Vpn.InvalidVrfs.InvalidVrf.Af',
            False, 
            [
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'MplsVpnAfiEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_vpn_oper', 'MplsVpnAfiEnum', 
                [], [], 
                '''                AF name
                ''',
                'af_name',
                'Cisco-IOS-XR-mpls-vpn-oper', False),
            _MetaInfoClassMember('export-route-policy', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Export Route Policy
                ''',
                'export_route_policy',
                'Cisco-IOS-XR-mpls-vpn-oper', False),
            _MetaInfoClassMember('import-route-policy', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Import Route Policy
                ''',
                'import_route_policy',
                'Cisco-IOS-XR-mpls-vpn-oper', False),
            _MetaInfoClassMember('route-target', REFERENCE_LIST, 'RouteTarget' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_vpn_oper', 'L3Vpn.InvalidVrfs.InvalidVrf.Af.RouteTarget', 
                [], [], 
                '''                Route Targets
                ''',
                'route_target',
                'Cisco-IOS-XR-mpls-vpn-oper', False),
            _MetaInfoClassMember('saf-name', REFERENCE_ENUM_CLASS, 'MplsVpnSafiEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_vpn_oper', 'MplsVpnSafiEnum', 
                [], [], 
                '''                SAF name
                ''',
                'saf_name',
                'Cisco-IOS-XR-mpls-vpn-oper', False),
            ],
            'Cisco-IOS-XR-mpls-vpn-oper',
            'af',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-vpn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_vpn_oper'
        ),
    },
    'L3Vpn.InvalidVrfs.InvalidVrf' : {
        'meta_info' : _MetaInfoClass('L3Vpn.InvalidVrfs.InvalidVrf',
            False, 
            [
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The Name for an invalid VRF
                ''',
                'vrf_name',
                'Cisco-IOS-XR-mpls-vpn-oper', True),
            _MetaInfoClassMember('af', REFERENCE_LIST, 'Af' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_vpn_oper', 'L3Vpn.InvalidVrfs.InvalidVrf.Af', 
                [], [], 
                '''                AF/SAF information
                ''',
                'af',
                'Cisco-IOS-XR-mpls-vpn-oper', False),
            _MetaInfoClassMember('interface', REFERENCE_LIST, 'Interface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_vpn_oper', 'L3Vpn.InvalidVrfs.InvalidVrf.Interface', 
                [], [], 
                '''                Interfaces in VRF
                ''',
                'interface',
                'Cisco-IOS-XR-mpls-vpn-oper', False),
            _MetaInfoClassMember('is-big-vrf', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                VRF mode information
                ''',
                'is_big_vrf',
                'Cisco-IOS-XR-mpls-vpn-oper', False),
            _MetaInfoClassMember('route-distinguisher', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Route Distinguisher
                ''',
                'route_distinguisher',
                'Cisco-IOS-XR-mpls-vpn-oper', False),
            _MetaInfoClassMember('vrf-description', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                VRF Description
                ''',
                'vrf_description',
                'Cisco-IOS-XR-mpls-vpn-oper', False),
            _MetaInfoClassMember('vrf-name-xr', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                VRF Name
                ''',
                'vrf_name_xr',
                'Cisco-IOS-XR-mpls-vpn-oper', False),
            ],
            'Cisco-IOS-XR-mpls-vpn-oper',
            'invalid-vrf',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-vpn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_vpn_oper'
        ),
    },
    'L3Vpn.InvalidVrfs' : {
        'meta_info' : _MetaInfoClass('L3Vpn.InvalidVrfs',
            False, 
            [
            _MetaInfoClassMember('invalid-vrf', REFERENCE_LIST, 'InvalidVrf' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_vpn_oper', 'L3Vpn.InvalidVrfs.InvalidVrf', 
                [], [], 
                '''                Invalid VRF (VRF that is forward referenced)
                ''',
                'invalid_vrf',
                'Cisco-IOS-XR-mpls-vpn-oper', False),
            ],
            'Cisco-IOS-XR-mpls-vpn-oper',
            'invalid-vrfs',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-vpn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_vpn_oper'
        ),
    },
    'L3Vpn.Vrfs.Vrf.Interface' : {
        'meta_info' : _MetaInfoClass('L3Vpn.Vrfs.Vrf.Interface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-mpls-vpn-oper', False),
            ],
            'Cisco-IOS-XR-mpls-vpn-oper',
            'interface',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-vpn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_vpn_oper'
        ),
    },
    'L3Vpn.Vrfs.Vrf.Af.RouteTarget' : {
        'meta_info' : _MetaInfoClass('L3Vpn.Vrfs.Vrf.Af.RouteTarget',
            False, 
            [
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'MplsVpnAfiEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_vpn_oper', 'MplsVpnAfiEnum', 
                [], [], 
                '''                AF name
                ''',
                'af_name',
                'Cisco-IOS-XR-mpls-vpn-oper', False),
            _MetaInfoClassMember('route-target-type', REFERENCE_ENUM_CLASS, 'MplsVpnRtEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_vpn_oper', 'MplsVpnRtEnum', 
                [], [], 
                '''                Route Target Type
                ''',
                'route_target_type',
                'Cisco-IOS-XR-mpls-vpn-oper', False),
            _MetaInfoClassMember('route-target-value', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Route Target Value
                ''',
                'route_target_value',
                'Cisco-IOS-XR-mpls-vpn-oper', False),
            _MetaInfoClassMember('saf-name', REFERENCE_ENUM_CLASS, 'MplsVpnSafiEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_vpn_oper', 'MplsVpnSafiEnum', 
                [], [], 
                '''                SAF name
                ''',
                'saf_name',
                'Cisco-IOS-XR-mpls-vpn-oper', False),
            ],
            'Cisco-IOS-XR-mpls-vpn-oper',
            'route-target',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-vpn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_vpn_oper'
        ),
    },
    'L3Vpn.Vrfs.Vrf.Af' : {
        'meta_info' : _MetaInfoClass('L3Vpn.Vrfs.Vrf.Af',
            False, 
            [
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'MplsVpnAfiEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_vpn_oper', 'MplsVpnAfiEnum', 
                [], [], 
                '''                AF name
                ''',
                'af_name',
                'Cisco-IOS-XR-mpls-vpn-oper', False),
            _MetaInfoClassMember('export-route-policy', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Export Route Policy
                ''',
                'export_route_policy',
                'Cisco-IOS-XR-mpls-vpn-oper', False),
            _MetaInfoClassMember('import-route-policy', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Import Route Policy
                ''',
                'import_route_policy',
                'Cisco-IOS-XR-mpls-vpn-oper', False),
            _MetaInfoClassMember('route-target', REFERENCE_LIST, 'RouteTarget' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_vpn_oper', 'L3Vpn.Vrfs.Vrf.Af.RouteTarget', 
                [], [], 
                '''                Route Targets
                ''',
                'route_target',
                'Cisco-IOS-XR-mpls-vpn-oper', False),
            _MetaInfoClassMember('saf-name', REFERENCE_ENUM_CLASS, 'MplsVpnSafiEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_vpn_oper', 'MplsVpnSafiEnum', 
                [], [], 
                '''                SAF name
                ''',
                'saf_name',
                'Cisco-IOS-XR-mpls-vpn-oper', False),
            ],
            'Cisco-IOS-XR-mpls-vpn-oper',
            'af',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-vpn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_vpn_oper'
        ),
    },
    'L3Vpn.Vrfs.Vrf' : {
        'meta_info' : _MetaInfoClass('L3Vpn.Vrfs.Vrf',
            False, 
            [
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The Name for a VRF
                ''',
                'vrf_name',
                'Cisco-IOS-XR-mpls-vpn-oper', True),
            _MetaInfoClassMember('af', REFERENCE_LIST, 'Af' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_vpn_oper', 'L3Vpn.Vrfs.Vrf.Af', 
                [], [], 
                '''                AF/SAF information
                ''',
                'af',
                'Cisco-IOS-XR-mpls-vpn-oper', False),
            _MetaInfoClassMember('interface', REFERENCE_LIST, 'Interface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_vpn_oper', 'L3Vpn.Vrfs.Vrf.Interface', 
                [], [], 
                '''                Interfaces in VRF
                ''',
                'interface',
                'Cisco-IOS-XR-mpls-vpn-oper', False),
            _MetaInfoClassMember('is-big-vrf', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                VRF mode information
                ''',
                'is_big_vrf',
                'Cisco-IOS-XR-mpls-vpn-oper', False),
            _MetaInfoClassMember('route-distinguisher', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Route Distinguisher
                ''',
                'route_distinguisher',
                'Cisco-IOS-XR-mpls-vpn-oper', False),
            _MetaInfoClassMember('vrf-description', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                VRF Description
                ''',
                'vrf_description',
                'Cisco-IOS-XR-mpls-vpn-oper', False),
            _MetaInfoClassMember('vrf-name-xr', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                VRF Name
                ''',
                'vrf_name_xr',
                'Cisco-IOS-XR-mpls-vpn-oper', False),
            ],
            'Cisco-IOS-XR-mpls-vpn-oper',
            'vrf',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-vpn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_vpn_oper'
        ),
    },
    'L3Vpn.Vrfs' : {
        'meta_info' : _MetaInfoClass('L3Vpn.Vrfs',
            False, 
            [
            _MetaInfoClassMember('vrf', REFERENCE_LIST, 'Vrf' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_vpn_oper', 'L3Vpn.Vrfs.Vrf', 
                [], [], 
                '''                VRF
                ''',
                'vrf',
                'Cisco-IOS-XR-mpls-vpn-oper', False),
            ],
            'Cisco-IOS-XR-mpls-vpn-oper',
            'vrfs',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-vpn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_vpn_oper'
        ),
    },
    'L3Vpn' : {
        'meta_info' : _MetaInfoClass('L3Vpn',
            False, 
            [
            _MetaInfoClassMember('invalid-vrfs', REFERENCE_CLASS, 'InvalidVrfs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_vpn_oper', 'L3Vpn.InvalidVrfs', 
                [], [], 
                '''                Invalid VRF Table (VRFs that are forward
                referenced)
                ''',
                'invalid_vrfs',
                'Cisco-IOS-XR-mpls-vpn-oper', False),
            _MetaInfoClassMember('vrfs', REFERENCE_CLASS, 'Vrfs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_vpn_oper', 'L3Vpn.Vrfs', 
                [], [], 
                '''                VRF Table
                ''',
                'vrfs',
                'Cisco-IOS-XR-mpls-vpn-oper', False),
            ],
            'Cisco-IOS-XR-mpls-vpn-oper',
            'l3vpn',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-vpn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_vpn_oper'
        ),
    },
}
_meta_table['L3Vpn.InvalidVrfs.InvalidVrf.Af.RouteTarget']['meta_info'].parent =_meta_table['L3Vpn.InvalidVrfs.InvalidVrf.Af']['meta_info']
_meta_table['L3Vpn.InvalidVrfs.InvalidVrf.Interface']['meta_info'].parent =_meta_table['L3Vpn.InvalidVrfs.InvalidVrf']['meta_info']
_meta_table['L3Vpn.InvalidVrfs.InvalidVrf.Af']['meta_info'].parent =_meta_table['L3Vpn.InvalidVrfs.InvalidVrf']['meta_info']
_meta_table['L3Vpn.InvalidVrfs.InvalidVrf']['meta_info'].parent =_meta_table['L3Vpn.InvalidVrfs']['meta_info']
_meta_table['L3Vpn.Vrfs.Vrf.Af.RouteTarget']['meta_info'].parent =_meta_table['L3Vpn.Vrfs.Vrf.Af']['meta_info']
_meta_table['L3Vpn.Vrfs.Vrf.Interface']['meta_info'].parent =_meta_table['L3Vpn.Vrfs.Vrf']['meta_info']
_meta_table['L3Vpn.Vrfs.Vrf.Af']['meta_info'].parent =_meta_table['L3Vpn.Vrfs.Vrf']['meta_info']
_meta_table['L3Vpn.Vrfs.Vrf']['meta_info'].parent =_meta_table['L3Vpn.Vrfs']['meta_info']
_meta_table['L3Vpn.InvalidVrfs']['meta_info'].parent =_meta_table['L3Vpn']['meta_info']
_meta_table['L3Vpn.Vrfs']['meta_info'].parent =_meta_table['L3Vpn']['meta_info']
