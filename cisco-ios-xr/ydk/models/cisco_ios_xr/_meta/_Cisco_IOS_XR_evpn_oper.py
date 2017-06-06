


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'L2VpnEvpnMfModeEnum' : _MetaInfoEnum('L2VpnEvpnMfModeEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper',
        {
            'invalid':'invalid',
            'tcn-stp':'tcn_stp',
            'mvrp':'mvrp',
        }, 'Cisco-IOS-XR-evpn-oper', _yang_ns._namespaces['Cisco-IOS-XR-evpn-oper']),
    'BgpRouteTargetFormatEnum' : _MetaInfoEnum('BgpRouteTargetFormatEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper',
        {
            'none':'none',
            'two-byte-as':'two_byte_as',
            'four-byte-as':'four_byte_as',
            'ipv4-address':'ipv4_address',
        }, 'Cisco-IOS-XR-evpn-oper', _yang_ns._namespaces['Cisco-IOS-XR-evpn-oper']),
    'L2VpnRgStateEnum' : _MetaInfoEnum('L2VpnRgStateEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper',
        {
            'unknown':'unknown',
            'active':'active',
            'standby':'standby',
        }, 'Cisco-IOS-XR-evpn-oper', _yang_ns._namespaces['Cisco-IOS-XR-evpn-oper']),
    'L2VpnEvpnScModeEnum' : _MetaInfoEnum('L2VpnEvpnScModeEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper',
        {
            'invalid':'invalid',
            'auto':'auto',
            'manual':'manual',
        }, 'Cisco-IOS-XR-evpn-oper', _yang_ns._namespaces['Cisco-IOS-XR-evpn-oper']),
    'L2VpnAdRtEnum' : _MetaInfoEnum('L2VpnAdRtEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper',
        {
            'l2vpn-ad-rt-none':'l2vpn_ad_rt_none',
            'l2vpn-ad-rt-as':'l2vpn_ad_rt_as',
            'l2vpn-ad-rt-4byte-as':'l2vpn_ad_rt_4byte_as',
            'l2vpn-ad-rt-v4-addr':'l2vpn_ad_rt_v4_addr',
            'es-import':'es_import',
        }, 'Cisco-IOS-XR-evpn-oper', _yang_ns._namespaces['Cisco-IOS-XR-evpn-oper']),
    'L2VpnEvpnScEnum' : _MetaInfoEnum('L2VpnEvpnScEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper',
        {
            'not-applicable':'not_applicable',
            'evi':'evi',
            'isid':'isid',
            'evpn-bag-sc-type-max':'evpn_bag_sc_type_max',
        }, 'Cisco-IOS-XR-evpn-oper', _yang_ns._namespaces['Cisco-IOS-XR-evpn-oper']),
    'L2VpnEvpnRtOriginEnum' : _MetaInfoEnum('L2VpnEvpnRtOriginEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper',
        {
            'invalid':'invalid',
            'extracted':'extracted',
            'configured':'configured',
        }, 'Cisco-IOS-XR-evpn-oper', _yang_ns._namespaces['Cisco-IOS-XR-evpn-oper']),
    'L2VpnEvpnSmacSrcEnum' : _MetaInfoEnum('L2VpnEvpnSmacSrcEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper',
        {
            'invalid':'invalid',
            'not-applicable':'not_applicable',
            'local':'local',
            'pbb-bsa':'pbb_bsa',
            'esi':'esi',
            'esi-invalid':'esi_invalid',
            'pbb-bsa-overrride':'pbb_bsa_overrride',
        }, 'Cisco-IOS-XR-evpn-oper', _yang_ns._namespaces['Cisco-IOS-XR-evpn-oper']),
    'EvpnEnum' : _MetaInfoEnum('EvpnEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper',
        {
            'evpn-type-invalid':'evpn_type_invalid',
            'evpn-type-evpn':'evpn_type_evpn',
            'evpn-type-pbb-evpn':'evpn_type_pbb_evpn',
            'evpn-type-evpn-vpws-vlan-unaware':'evpn_type_evpn_vpws_vlan_unaware',
            'evpn-type-evpn-vpws-vlan-aware':'evpn_type_evpn_vpws_vlan_aware',
            'evpn-type-max':'evpn_type_max',
        }, 'Cisco-IOS-XR-evpn-oper', _yang_ns._namespaces['Cisco-IOS-XR-evpn-oper']),
    'L2VpnAdRdEnum' : _MetaInfoEnum('L2VpnAdRdEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper',
        {
            'l2vpn-ad-rd-none':'l2vpn_ad_rd_none',
            'l2vpn-ad-rd-auto':'l2vpn_ad_rd_auto',
            'l2vpn-ad-rd-as':'l2vpn_ad_rd_as',
            'l2vpn-ad-rd-4byte-as':'l2vpn_ad_rd_4byte_as',
            'l2vpn-ad-rd-v4-addr':'l2vpn_ad_rd_v4_addr',
        }, 'Cisco-IOS-XR-evpn-oper', _yang_ns._namespaces['Cisco-IOS-XR-evpn-oper']),
    'BgpRouteTargetEnum' : _MetaInfoEnum('BgpRouteTargetEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper',
        {
            'no-stitching':'no_stitching',
            'stitching':'stitching',
        }, 'Cisco-IOS-XR-evpn-oper', _yang_ns._namespaces['Cisco-IOS-XR-evpn-oper']),
    'BgpRouteTargetRoleEnum' : _MetaInfoEnum('BgpRouteTargetRoleEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper',
        {
            'both':'both',
            'import':'import_',
            'export':'export',
        }, 'Cisco-IOS-XR-evpn-oper', _yang_ns._namespaces['Cisco-IOS-XR-evpn-oper']),
    'L2VpnEvpnEsiEnum' : _MetaInfoEnum('L2VpnEvpnEsiEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper',
        {
            'esi-type0':'esi_type0',
            'esi-type1':'esi_type1',
            'esi-type2':'esi_type2',
            'esi-type3':'esi_type3',
            'esi-type4':'esi_type4',
            'esi-type5':'esi_type5',
            'l2vpn-evpn-esi-type-legacy':'l2vpn_evpn_esi_type_legacy',
            'l2vpn-evpn-esi-type-override':'l2vpn_evpn_esi_type_override',
            'esi-type-invalid':'esi_type_invalid',
        }, 'Cisco-IOS-XR-evpn-oper', _yang_ns._namespaces['Cisco-IOS-XR-evpn-oper']),
    'L2VpnAdRtRoleEnum' : _MetaInfoEnum('L2VpnAdRtRoleEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper',
        {
            'both':'both',
            'import':'import_',
            'export':'export',
        }, 'Cisco-IOS-XR-evpn-oper', _yang_ns._namespaces['Cisco-IOS-XR-evpn-oper']),
    'L2VpnEvpnLbModeEnum' : _MetaInfoEnum('L2VpnEvpnLbModeEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper',
        {
            'invalid-load-balancing':'invalid_load_balancing',
            'single-homed':'single_homed',
            'multi-homed-aa-per-flow':'multi_homed_aa_per_flow',
            'multi-homed-aa-per-service':'multi_homed_aa_per_service',
        }, 'Cisco-IOS-XR-evpn-oper', _yang_ns._namespaces['Cisco-IOS-XR-evpn-oper']),
    'Evpn.Nodes.Node.Evis.Evi' : {
        'meta_info' : _MetaInfoClass('Evpn.Nodes.Node.Evis.Evi',
            False, 
            [
            _MetaInfoClassMember('evi', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                EVPN id
                ''',
                'evi',
                'Cisco-IOS-XR-evpn-oper', True),
            _MetaInfoClassMember('bd-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Bridge domain name
                ''',
                'bd_name',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('evi-xr', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                E-VPN id
                ''',
                'evi_xr',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('type', REFERENCE_ENUM_CLASS, 'EvpnEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'EvpnEnum', 
                [], [], 
                '''                Service Type
                ''',
                'type',
                'Cisco-IOS-XR-evpn-oper', False),
            ],
            'Cisco-IOS-XR-evpn-oper',
            'evi',
            _yang_ns._namespaces['Cisco-IOS-XR-evpn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper'
        ),
    },
    'Evpn.Nodes.Node.Evis' : {
        'meta_info' : _MetaInfoClass('Evpn.Nodes.Node.Evis',
            False, 
            [
            _MetaInfoClassMember('evi', REFERENCE_LIST, 'Evi' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'Evpn.Nodes.Node.Evis.Evi', 
                [], [], 
                '''                L2VPN EVPN EVI Entry
                ''',
                'evi',
                'Cisco-IOS-XR-evpn-oper', False),
            ],
            'Cisco-IOS-XR-evpn-oper',
            'evis',
            _yang_ns._namespaces['Cisco-IOS-XR-evpn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper'
        ),
    },
    'Evpn.Nodes.Node.Summary' : {
        'meta_info' : _MetaInfoClass('Evpn.Nodes.Node.Summary',
            False, 
            [
            _MetaInfoClassMember('as', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                BGP AS number
                ''',
                'as_',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('es-entries', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of ES Entries in DB
                ''',
                'es_entries',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('es-global-mac-routes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of ES:Global MAC Routes
                ''',
                'es_global_mac_routes',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('ev-is', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of EVI DB Entries
                ''',
                'ev_is',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('global-source-mac', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                Global Source MAC Address
                ''',
                'global_source_mac',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('l2rib-throttle', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Send to L2RIB Throttled
                ''',
                'l2rib_throttle',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('labels', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Internal Labels
                ''',
                'labels',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('local-ead-routes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Local EAD Entries in DB
                ''',
                'local_ead_routes',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('local-imcast-routes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Local IMCAST Routes
                ''',
                'local_imcast_routes',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('local-ipv4-mac-routes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Local IPv4 MAC-IP Routes
                ''',
                'local_ipv4_mac_routes',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('local-ipv6-mac-routes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Local IPv6 MAC-IP Routes
                ''',
                'local_ipv6_mac_routes',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('local-mac-routes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Local MAC Routes
                ''',
                'local_mac_routes',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('logging-df-election-enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Logging EVPN Designated Forwarder changes
                enabled
                ''',
                'logging_df_election_enabled',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('neighbor-entries', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of neighbor Entries in DB
                ''',
                'neighbor_entries',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('peering-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                EVPN ES Peering Time (seconds)
                ''',
                'peering_time',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('recovery-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                EVPN ES Recovery Time (seconds)
                ''',
                'recovery_time',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('remote-ead-routes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Remote EAD Entries in DB
                ''',
                'remote_ead_routes',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('remote-imcast-routes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Remote IMCAST Routes
                ''',
                'remote_imcast_routes',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('remote-ipv4-mac-routes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Remote IPv4 MAC-IP Routes
                ''',
                'remote_ipv4_mac_routes',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('remote-ipv6-mac-routes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Remote IPv6 MAC-IP Routes
                ''',
                'remote_ipv6_mac_routes',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('remote-mac-routes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Remote MAC Routes
                ''',
                'remote_mac_routes',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('remote-soo-mac-routes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Remote Soo MAC Routes
                ''',
                'remote_soo_mac_routes',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('router-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                EVPN Router ID
                ''',
                'router_id',
                'Cisco-IOS-XR-evpn-oper', False),
            ],
            'Cisco-IOS-XR-evpn-oper',
            'summary',
            _yang_ns._namespaces['Cisco-IOS-XR-evpn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper'
        ),
    },
    'Evpn.Nodes.Node.EviDetail.Elements.Element.FlowLabel' : {
        'meta_info' : _MetaInfoClass('Evpn.Nodes.Node.EviDetail.Elements.Element.FlowLabel',
            False, 
            [
            _MetaInfoClassMember('global-flow-label', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Globally configured flow label
                ''',
                'global_flow_label',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('static-flow-label', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Static flow label
                ''',
                'static_flow_label',
                'Cisco-IOS-XR-evpn-oper', False),
            ],
            'Cisco-IOS-XR-evpn-oper',
            'flow-label',
            _yang_ns._namespaces['Cisco-IOS-XR-evpn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper'
        ),
    },
    'Evpn.Nodes.Node.EviDetail.Elements.Element.RdAuto.Auto' : {
        'meta_info' : _MetaInfoClass('Evpn.Nodes.Node.EviDetail.Elements.Element.RdAuto.Auto',
            False, 
            [
            _MetaInfoClassMember('auto-index', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Auto-generated Index
                ''',
                'auto_index',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('router-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                BGP Router ID
                ''',
                'router_id',
                'Cisco-IOS-XR-evpn-oper', False),
            ],
            'Cisco-IOS-XR-evpn-oper',
            'auto',
            _yang_ns._namespaces['Cisco-IOS-XR-evpn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper'
        ),
    },
    'Evpn.Nodes.Node.EviDetail.Elements.Element.RdAuto.TwoByteAs' : {
        'meta_info' : _MetaInfoClass('Evpn.Nodes.Node.EviDetail.Elements.Element.RdAuto.TwoByteAs',
            False, 
            [
            _MetaInfoClassMember('four-byte-index', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                4 Byte Index
                ''',
                'four_byte_index',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('two-byte-as', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                2 Byte AS Number
                ''',
                'two_byte_as',
                'Cisco-IOS-XR-evpn-oper', False),
            ],
            'Cisco-IOS-XR-evpn-oper',
            'two-byte-as',
            _yang_ns._namespaces['Cisco-IOS-XR-evpn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper'
        ),
    },
    'Evpn.Nodes.Node.EviDetail.Elements.Element.RdAuto.FourByteAs' : {
        'meta_info' : _MetaInfoClass('Evpn.Nodes.Node.EviDetail.Elements.Element.RdAuto.FourByteAs',
            False, 
            [
            _MetaInfoClassMember('four-byte-as', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                4 Byte AS Number
                ''',
                'four_byte_as',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('two-byte-index', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                2 Byte Index
                ''',
                'two_byte_index',
                'Cisco-IOS-XR-evpn-oper', False),
            ],
            'Cisco-IOS-XR-evpn-oper',
            'four-byte-as',
            _yang_ns._namespaces['Cisco-IOS-XR-evpn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper'
        ),
    },
    'Evpn.Nodes.Node.EviDetail.Elements.Element.RdAuto.V4Addr' : {
        'meta_info' : _MetaInfoClass('Evpn.Nodes.Node.EviDetail.Elements.Element.RdAuto.V4Addr',
            False, 
            [
            _MetaInfoClassMember('ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 Address
                ''',
                'ipv4_address',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('two-byte-index', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                2 Byte Index
                ''',
                'two_byte_index',
                'Cisco-IOS-XR-evpn-oper', False),
            ],
            'Cisco-IOS-XR-evpn-oper',
            'v4-addr',
            _yang_ns._namespaces['Cisco-IOS-XR-evpn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper'
        ),
    },
    'Evpn.Nodes.Node.EviDetail.Elements.Element.RdAuto' : {
        'meta_info' : _MetaInfoClass('Evpn.Nodes.Node.EviDetail.Elements.Element.RdAuto',
            False, 
            [
            _MetaInfoClassMember('auto', REFERENCE_CLASS, 'Auto' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'Evpn.Nodes.Node.EviDetail.Elements.Element.RdAuto.Auto', 
                [], [], 
                '''                auto
                ''',
                'auto',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('four-byte-as', REFERENCE_CLASS, 'FourByteAs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'Evpn.Nodes.Node.EviDetail.Elements.Element.RdAuto.FourByteAs', 
                [], [], 
                '''                four byte as
                ''',
                'four_byte_as',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('rd', REFERENCE_ENUM_CLASS, 'L2VpnAdRdEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'L2VpnAdRdEnum', 
                [], [], 
                '''                RD
                ''',
                'rd',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('two-byte-as', REFERENCE_CLASS, 'TwoByteAs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'Evpn.Nodes.Node.EviDetail.Elements.Element.RdAuto.TwoByteAs', 
                [], [], 
                '''                two byte as
                ''',
                'two_byte_as',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('v4-addr', REFERENCE_CLASS, 'V4Addr' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'Evpn.Nodes.Node.EviDetail.Elements.Element.RdAuto.V4Addr', 
                [], [], 
                '''                v4 addr
                ''',
                'v4_addr',
                'Cisco-IOS-XR-evpn-oper', False),
            ],
            'Cisco-IOS-XR-evpn-oper',
            'rd-auto',
            _yang_ns._namespaces['Cisco-IOS-XR-evpn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper'
        ),
    },
    'Evpn.Nodes.Node.EviDetail.Elements.Element.RdConfigured.Auto' : {
        'meta_info' : _MetaInfoClass('Evpn.Nodes.Node.EviDetail.Elements.Element.RdConfigured.Auto',
            False, 
            [
            _MetaInfoClassMember('auto-index', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Auto-generated Index
                ''',
                'auto_index',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('router-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                BGP Router ID
                ''',
                'router_id',
                'Cisco-IOS-XR-evpn-oper', False),
            ],
            'Cisco-IOS-XR-evpn-oper',
            'auto',
            _yang_ns._namespaces['Cisco-IOS-XR-evpn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper'
        ),
    },
    'Evpn.Nodes.Node.EviDetail.Elements.Element.RdConfigured.TwoByteAs' : {
        'meta_info' : _MetaInfoClass('Evpn.Nodes.Node.EviDetail.Elements.Element.RdConfigured.TwoByteAs',
            False, 
            [
            _MetaInfoClassMember('four-byte-index', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                4 Byte Index
                ''',
                'four_byte_index',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('two-byte-as', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                2 Byte AS Number
                ''',
                'two_byte_as',
                'Cisco-IOS-XR-evpn-oper', False),
            ],
            'Cisco-IOS-XR-evpn-oper',
            'two-byte-as',
            _yang_ns._namespaces['Cisco-IOS-XR-evpn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper'
        ),
    },
    'Evpn.Nodes.Node.EviDetail.Elements.Element.RdConfigured.FourByteAs' : {
        'meta_info' : _MetaInfoClass('Evpn.Nodes.Node.EviDetail.Elements.Element.RdConfigured.FourByteAs',
            False, 
            [
            _MetaInfoClassMember('four-byte-as', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                4 Byte AS Number
                ''',
                'four_byte_as',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('two-byte-index', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                2 Byte Index
                ''',
                'two_byte_index',
                'Cisco-IOS-XR-evpn-oper', False),
            ],
            'Cisco-IOS-XR-evpn-oper',
            'four-byte-as',
            _yang_ns._namespaces['Cisco-IOS-XR-evpn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper'
        ),
    },
    'Evpn.Nodes.Node.EviDetail.Elements.Element.RdConfigured.V4Addr' : {
        'meta_info' : _MetaInfoClass('Evpn.Nodes.Node.EviDetail.Elements.Element.RdConfigured.V4Addr',
            False, 
            [
            _MetaInfoClassMember('ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 Address
                ''',
                'ipv4_address',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('two-byte-index', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                2 Byte Index
                ''',
                'two_byte_index',
                'Cisco-IOS-XR-evpn-oper', False),
            ],
            'Cisco-IOS-XR-evpn-oper',
            'v4-addr',
            _yang_ns._namespaces['Cisco-IOS-XR-evpn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper'
        ),
    },
    'Evpn.Nodes.Node.EviDetail.Elements.Element.RdConfigured' : {
        'meta_info' : _MetaInfoClass('Evpn.Nodes.Node.EviDetail.Elements.Element.RdConfigured',
            False, 
            [
            _MetaInfoClassMember('auto', REFERENCE_CLASS, 'Auto' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'Evpn.Nodes.Node.EviDetail.Elements.Element.RdConfigured.Auto', 
                [], [], 
                '''                auto
                ''',
                'auto',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('four-byte-as', REFERENCE_CLASS, 'FourByteAs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'Evpn.Nodes.Node.EviDetail.Elements.Element.RdConfigured.FourByteAs', 
                [], [], 
                '''                four byte as
                ''',
                'four_byte_as',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('rd', REFERENCE_ENUM_CLASS, 'L2VpnAdRdEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'L2VpnAdRdEnum', 
                [], [], 
                '''                RD
                ''',
                'rd',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('two-byte-as', REFERENCE_CLASS, 'TwoByteAs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'Evpn.Nodes.Node.EviDetail.Elements.Element.RdConfigured.TwoByteAs', 
                [], [], 
                '''                two byte as
                ''',
                'two_byte_as',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('v4-addr', REFERENCE_CLASS, 'V4Addr' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'Evpn.Nodes.Node.EviDetail.Elements.Element.RdConfigured.V4Addr', 
                [], [], 
                '''                v4 addr
                ''',
                'v4_addr',
                'Cisco-IOS-XR-evpn-oper', False),
            ],
            'Cisco-IOS-XR-evpn-oper',
            'rd-configured',
            _yang_ns._namespaces['Cisco-IOS-XR-evpn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper'
        ),
    },
    'Evpn.Nodes.Node.EviDetail.Elements.Element.RtAuto.TwoByteAs' : {
        'meta_info' : _MetaInfoClass('Evpn.Nodes.Node.EviDetail.Elements.Element.RtAuto.TwoByteAs',
            False, 
            [
            _MetaInfoClassMember('four-byte-index', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                4 Byte Index
                ''',
                'four_byte_index',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('two-byte-as', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                2 Byte AS Number
                ''',
                'two_byte_as',
                'Cisco-IOS-XR-evpn-oper', False),
            ],
            'Cisco-IOS-XR-evpn-oper',
            'two-byte-as',
            _yang_ns._namespaces['Cisco-IOS-XR-evpn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper'
        ),
    },
    'Evpn.Nodes.Node.EviDetail.Elements.Element.RtAuto.FourByteAs' : {
        'meta_info' : _MetaInfoClass('Evpn.Nodes.Node.EviDetail.Elements.Element.RtAuto.FourByteAs',
            False, 
            [
            _MetaInfoClassMember('four-byte-as', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                4 Byte AS Number
                ''',
                'four_byte_as',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('two-byte-index', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                2 Byte Index
                ''',
                'two_byte_index',
                'Cisco-IOS-XR-evpn-oper', False),
            ],
            'Cisco-IOS-XR-evpn-oper',
            'four-byte-as',
            _yang_ns._namespaces['Cisco-IOS-XR-evpn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper'
        ),
    },
    'Evpn.Nodes.Node.EviDetail.Elements.Element.RtAuto.V4Addr' : {
        'meta_info' : _MetaInfoClass('Evpn.Nodes.Node.EviDetail.Elements.Element.RtAuto.V4Addr',
            False, 
            [
            _MetaInfoClassMember('ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 Address
                ''',
                'ipv4_address',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('two-byte-index', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                2 Byte Index
                ''',
                'two_byte_index',
                'Cisco-IOS-XR-evpn-oper', False),
            ],
            'Cisco-IOS-XR-evpn-oper',
            'v4-addr',
            _yang_ns._namespaces['Cisco-IOS-XR-evpn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper'
        ),
    },
    'Evpn.Nodes.Node.EviDetail.Elements.Element.RtAuto.EsImport' : {
        'meta_info' : _MetaInfoClass('Evpn.Nodes.Node.EviDetail.Elements.Element.RtAuto.EsImport',
            False, 
            [
            _MetaInfoClassMember('high-bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Top 4 bytes of ES Import
                ''',
                'high_bytes',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('low-bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Low 2 bytes of ES Import
                ''',
                'low_bytes',
                'Cisco-IOS-XR-evpn-oper', False),
            ],
            'Cisco-IOS-XR-evpn-oper',
            'es-import',
            _yang_ns._namespaces['Cisco-IOS-XR-evpn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper'
        ),
    },
    'Evpn.Nodes.Node.EviDetail.Elements.Element.RtAuto' : {
        'meta_info' : _MetaInfoClass('Evpn.Nodes.Node.EviDetail.Elements.Element.RtAuto',
            False, 
            [
            _MetaInfoClassMember('es-import', REFERENCE_CLASS, 'EsImport' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'Evpn.Nodes.Node.EviDetail.Elements.Element.RtAuto.EsImport', 
                [], [], 
                '''                es import
                ''',
                'es_import',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('four-byte-as', REFERENCE_CLASS, 'FourByteAs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'Evpn.Nodes.Node.EviDetail.Elements.Element.RtAuto.FourByteAs', 
                [], [], 
                '''                four byte as
                ''',
                'four_byte_as',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('rt', REFERENCE_ENUM_CLASS, 'L2VpnAdRtEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'L2VpnAdRtEnum', 
                [], [], 
                '''                RT
                ''',
                'rt',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('two-byte-as', REFERENCE_CLASS, 'TwoByteAs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'Evpn.Nodes.Node.EviDetail.Elements.Element.RtAuto.TwoByteAs', 
                [], [], 
                '''                two byte as
                ''',
                'two_byte_as',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('v4-addr', REFERENCE_CLASS, 'V4Addr' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'Evpn.Nodes.Node.EviDetail.Elements.Element.RtAuto.V4Addr', 
                [], [], 
                '''                v4 addr
                ''',
                'v4_addr',
                'Cisco-IOS-XR-evpn-oper', False),
            ],
            'Cisco-IOS-XR-evpn-oper',
            'rt-auto',
            _yang_ns._namespaces['Cisco-IOS-XR-evpn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper'
        ),
    },
    'Evpn.Nodes.Node.EviDetail.Elements.Element.RtAutoStitching.TwoByteAs' : {
        'meta_info' : _MetaInfoClass('Evpn.Nodes.Node.EviDetail.Elements.Element.RtAutoStitching.TwoByteAs',
            False, 
            [
            _MetaInfoClassMember('four-byte-index', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                4 Byte Index
                ''',
                'four_byte_index',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('two-byte-as', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                2 Byte AS Number
                ''',
                'two_byte_as',
                'Cisco-IOS-XR-evpn-oper', False),
            ],
            'Cisco-IOS-XR-evpn-oper',
            'two-byte-as',
            _yang_ns._namespaces['Cisco-IOS-XR-evpn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper'
        ),
    },
    'Evpn.Nodes.Node.EviDetail.Elements.Element.RtAutoStitching.FourByteAs' : {
        'meta_info' : _MetaInfoClass('Evpn.Nodes.Node.EviDetail.Elements.Element.RtAutoStitching.FourByteAs',
            False, 
            [
            _MetaInfoClassMember('four-byte-as', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                4 Byte AS Number
                ''',
                'four_byte_as',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('two-byte-index', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                2 Byte Index
                ''',
                'two_byte_index',
                'Cisco-IOS-XR-evpn-oper', False),
            ],
            'Cisco-IOS-XR-evpn-oper',
            'four-byte-as',
            _yang_ns._namespaces['Cisco-IOS-XR-evpn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper'
        ),
    },
    'Evpn.Nodes.Node.EviDetail.Elements.Element.RtAutoStitching.V4Addr' : {
        'meta_info' : _MetaInfoClass('Evpn.Nodes.Node.EviDetail.Elements.Element.RtAutoStitching.V4Addr',
            False, 
            [
            _MetaInfoClassMember('ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 Address
                ''',
                'ipv4_address',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('two-byte-index', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                2 Byte Index
                ''',
                'two_byte_index',
                'Cisco-IOS-XR-evpn-oper', False),
            ],
            'Cisco-IOS-XR-evpn-oper',
            'v4-addr',
            _yang_ns._namespaces['Cisco-IOS-XR-evpn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper'
        ),
    },
    'Evpn.Nodes.Node.EviDetail.Elements.Element.RtAutoStitching.EsImport' : {
        'meta_info' : _MetaInfoClass('Evpn.Nodes.Node.EviDetail.Elements.Element.RtAutoStitching.EsImport',
            False, 
            [
            _MetaInfoClassMember('high-bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Top 4 bytes of ES Import
                ''',
                'high_bytes',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('low-bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Low 2 bytes of ES Import
                ''',
                'low_bytes',
                'Cisco-IOS-XR-evpn-oper', False),
            ],
            'Cisco-IOS-XR-evpn-oper',
            'es-import',
            _yang_ns._namespaces['Cisco-IOS-XR-evpn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper'
        ),
    },
    'Evpn.Nodes.Node.EviDetail.Elements.Element.RtAutoStitching' : {
        'meta_info' : _MetaInfoClass('Evpn.Nodes.Node.EviDetail.Elements.Element.RtAutoStitching',
            False, 
            [
            _MetaInfoClassMember('es-import', REFERENCE_CLASS, 'EsImport' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'Evpn.Nodes.Node.EviDetail.Elements.Element.RtAutoStitching.EsImport', 
                [], [], 
                '''                es import
                ''',
                'es_import',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('four-byte-as', REFERENCE_CLASS, 'FourByteAs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'Evpn.Nodes.Node.EviDetail.Elements.Element.RtAutoStitching.FourByteAs', 
                [], [], 
                '''                four byte as
                ''',
                'four_byte_as',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('rt', REFERENCE_ENUM_CLASS, 'L2VpnAdRtEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'L2VpnAdRtEnum', 
                [], [], 
                '''                RT
                ''',
                'rt',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('two-byte-as', REFERENCE_CLASS, 'TwoByteAs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'Evpn.Nodes.Node.EviDetail.Elements.Element.RtAutoStitching.TwoByteAs', 
                [], [], 
                '''                two byte as
                ''',
                'two_byte_as',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('v4-addr', REFERENCE_CLASS, 'V4Addr' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'Evpn.Nodes.Node.EviDetail.Elements.Element.RtAutoStitching.V4Addr', 
                [], [], 
                '''                v4 addr
                ''',
                'v4_addr',
                'Cisco-IOS-XR-evpn-oper', False),
            ],
            'Cisco-IOS-XR-evpn-oper',
            'rt-auto-stitching',
            _yang_ns._namespaces['Cisco-IOS-XR-evpn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper'
        ),
    },
    'Evpn.Nodes.Node.EviDetail.Elements.Element' : {
        'meta_info' : _MetaInfoClass('Evpn.Nodes.Node.EviDetail.Elements.Element',
            False, 
            [
            _MetaInfoClassMember('evi', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                EVPN id
                ''',
                'evi',
                'Cisco-IOS-XR-evpn-oper', True),
            _MetaInfoClassMember('advertise-mac', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Advertise MAC-only routes on this EVI
                ''',
                'advertise_mac',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('aliasing-disabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Route Aliasing is disabled
                ''',
                'aliasing_disabled',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('bd-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Bridge domain name
                ''',
                'bd_name',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('cw-disable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Control-Word Disable
                ''',
                'cw_disable',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('description', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                EVI description
                ''',
                'description',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('evi-xr', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                E-VPN id
                ''',
                'evi_xr',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('flow-label', REFERENCE_CLASS, 'FlowLabel' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'Evpn.Nodes.Node.EviDetail.Elements.Element.FlowLabel', 
                [], [], 
                '''                Flow Label Information
                ''',
                'flow_label',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('forward-class', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Forward Class attribute
                ''',
                'forward_class',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('multicast-label', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Multicast Label
                ''',
                'multicast_label',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('rd-auto', REFERENCE_CLASS, 'RdAuto' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'Evpn.Nodes.Node.EviDetail.Elements.Element.RdAuto', 
                [], [], 
                '''                Automatic Route Distingtuisher
                ''',
                'rd_auto',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('rd-configured', REFERENCE_CLASS, 'RdConfigured' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'Evpn.Nodes.Node.EviDetail.Elements.Element.RdConfigured', 
                [], [], 
                '''                Configured Route Distinguisher
                ''',
                'rd_configured',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('reoriginate-disabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Route Re-origination is disabled
                ''',
                'reoriginate_disabled',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('rt-auto', REFERENCE_CLASS, 'RtAuto' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'Evpn.Nodes.Node.EviDetail.Elements.Element.RtAuto', 
                [], [], 
                '''                Automatic Route Target
                ''',
                'rt_auto',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('rt-auto-stitching', REFERENCE_CLASS, 'RtAutoStitching' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'Evpn.Nodes.Node.EviDetail.Elements.Element.RtAutoStitching', 
                [], [], 
                '''                Automatic Route Target Stitching
                ''',
                'rt_auto_stitching',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('rt-export-block-set', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is Export RT None set
                ''',
                'rt_export_block_set',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('rt-import-block-set', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is Import RT None set
                ''',
                'rt_import_block_set',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('stitching', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                RT Stitching for MPLS Fabric is enabled
                ''',
                'stitching',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('table-policy-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Table-policy Name
                ''',
                'table_policy_name',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('type', REFERENCE_ENUM_CLASS, 'EvpnEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'EvpnEnum', 
                [], [], 
                '''                Service Type
                ''',
                'type',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('unicast-label', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Unicast Label
                ''',
                'unicast_label',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('unknown-unicast-flooding-disabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Unknown-unicast flooding is disabled
                ''',
                'unknown_unicast_flooding_disabled',
                'Cisco-IOS-XR-evpn-oper', False),
            ],
            'Cisco-IOS-XR-evpn-oper',
            'element',
            _yang_ns._namespaces['Cisco-IOS-XR-evpn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper'
        ),
    },
    'Evpn.Nodes.Node.EviDetail.Elements' : {
        'meta_info' : _MetaInfoClass('Evpn.Nodes.Node.EviDetail.Elements',
            False, 
            [
            _MetaInfoClassMember('element', REFERENCE_LIST, 'Element' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'Evpn.Nodes.Node.EviDetail.Elements.Element', 
                [], [], 
                '''                EVI BGP RT Detail Info
                ''',
                'element',
                'Cisco-IOS-XR-evpn-oper', False),
            ],
            'Cisco-IOS-XR-evpn-oper',
            'elements',
            _yang_ns._namespaces['Cisco-IOS-XR-evpn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper'
        ),
    },
    'Evpn.Nodes.Node.EviDetail.EviChildren.Neighbors.Neighbor' : {
        'meta_info' : _MetaInfoClass('Evpn.Nodes.Node.EviDetail.EviChildren.Neighbors.Neighbor',
            False, 
            [
            _MetaInfoClassMember('evi', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                EVPN id
                ''',
                'evi',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('evi-xr', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                E-VPN id
                ''',
                'evi_xr',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('neighbor', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                Neighbor IP
                ''',
                'neighbor',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('neighbor-ip', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Neighbor IP
                ''',
                'neighbor_ip',
                'Cisco-IOS-XR-evpn-oper', False, [
                    _MetaInfoClassMember('neighbor-ip', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Neighbor IP
                        ''',
                        'neighbor_ip',
                        'Cisco-IOS-XR-evpn-oper', False),
                    _MetaInfoClassMember('neighbor-ip', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Neighbor IP
                        ''',
                        'neighbor_ip',
                        'Cisco-IOS-XR-evpn-oper', False),
                ]),
            ],
            'Cisco-IOS-XR-evpn-oper',
            'neighbor',
            _yang_ns._namespaces['Cisco-IOS-XR-evpn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper'
        ),
    },
    'Evpn.Nodes.Node.EviDetail.EviChildren.Neighbors' : {
        'meta_info' : _MetaInfoClass('Evpn.Nodes.Node.EviDetail.EviChildren.Neighbors',
            False, 
            [
            _MetaInfoClassMember('neighbor', REFERENCE_LIST, 'Neighbor' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'Evpn.Nodes.Node.EviDetail.EviChildren.Neighbors.Neighbor', 
                [], [], 
                '''                EVPN Neighbor table
                ''',
                'neighbor',
                'Cisco-IOS-XR-evpn-oper', False),
            ],
            'Cisco-IOS-XR-evpn-oper',
            'neighbors',
            _yang_ns._namespaces['Cisco-IOS-XR-evpn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper'
        ),
    },
    'Evpn.Nodes.Node.EviDetail.EviChildren.EthernetAutoDiscoveries.EthernetAutoDiscovery.PathBuffer' : {
        'meta_info' : _MetaInfoClass('Evpn.Nodes.Node.EviDetail.EviChildren.EthernetAutoDiscoveries.EthernetAutoDiscovery.PathBuffer',
            False, 
            [
            _MetaInfoClassMember('next-hop', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                Next-hop IP address (v6 format)
                ''',
                'next_hop',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('output-label', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Output Label
                ''',
                'output_label',
                'Cisco-IOS-XR-evpn-oper', False),
            ],
            'Cisco-IOS-XR-evpn-oper',
            'path-buffer',
            _yang_ns._namespaces['Cisco-IOS-XR-evpn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper'
        ),
    },
    'Evpn.Nodes.Node.EviDetail.EviChildren.EthernetAutoDiscoveries.EthernetAutoDiscovery' : {
        'meta_info' : _MetaInfoClass('Evpn.Nodes.Node.EviDetail.EviChildren.EthernetAutoDiscoveries.EthernetAutoDiscovery',
            False, 
            [
            _MetaInfoClassMember('encap', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Encap type of local or remote EAD
                ''',
                'encap',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('esi1', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{1,8}'], 
                '''                ES id (part 1/5)
                ''',
                'esi1',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('esi2', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{1,8}'], 
                '''                ES id (part 2/5)
                ''',
                'esi2',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('esi3', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{1,8}'], 
                '''                ES id (part 3/5)
                ''',
                'esi3',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('esi4', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{1,8}'], 
                '''                ES id (part 4/5)
                ''',
                'esi4',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('esi5', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{1,8}'], 
                '''                ES id (part 5/5)
                ''',
                'esi5',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('ethernet-segment-identifier', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Ethernet Segment id
                ''',
                'ethernet_segment_identifier',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('ethernet-tag', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Ethernet Tag ID
                ''',
                'ethernet_tag',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('ethernet-tag-xr', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Ethernet Tag
                ''',
                'ethernet_tag_xr',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('ethernet-vpnid', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                E-VPN id
                ''',
                'ethernet_vpnid',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('evi', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                EVPN id
                ''',
                'evi',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('is-local-ead', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Indication of EthernetAutoDiscovery Route is
                local
                ''',
                'is_local_ead',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('local-label', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Associated local label
                ''',
                'local_label',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('local-next-hop', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                Local nexthop IP
                ''',
                'local_next_hop',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('num-paths', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                 Number of items in path list buffer
                ''',
                'num_paths',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('path-buffer', REFERENCE_LIST, 'PathBuffer' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'Evpn.Nodes.Node.EviDetail.EviChildren.EthernetAutoDiscoveries.EthernetAutoDiscovery.PathBuffer', 
                [], [], 
                '''                Path List Buffer
                ''',
                'path_buffer',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('redundancy-single-active', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Single-active redundancy configured at remote
                EAD
                ''',
                'redundancy_single_active',
                'Cisco-IOS-XR-evpn-oper', False),
            ],
            'Cisco-IOS-XR-evpn-oper',
            'ethernet-auto-discovery',
            _yang_ns._namespaces['Cisco-IOS-XR-evpn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper'
        ),
    },
    'Evpn.Nodes.Node.EviDetail.EviChildren.EthernetAutoDiscoveries' : {
        'meta_info' : _MetaInfoClass('Evpn.Nodes.Node.EviDetail.EviChildren.EthernetAutoDiscoveries',
            False, 
            [
            _MetaInfoClassMember('ethernet-auto-discovery', REFERENCE_LIST, 'EthernetAutoDiscovery' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'Evpn.Nodes.Node.EviDetail.EviChildren.EthernetAutoDiscoveries.EthernetAutoDiscovery', 
                [], [], 
                '''                EVPN Ethernet Auto-Discovery Entry
                ''',
                'ethernet_auto_discovery',
                'Cisco-IOS-XR-evpn-oper', False),
            ],
            'Cisco-IOS-XR-evpn-oper',
            'ethernet-auto-discoveries',
            _yang_ns._namespaces['Cisco-IOS-XR-evpn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper'
        ),
    },
    'Evpn.Nodes.Node.EviDetail.EviChildren.InclusiveMulticasts.InclusiveMulticast' : {
        'meta_info' : _MetaInfoClass('Evpn.Nodes.Node.EviDetail.EviChildren.InclusiveMulticasts.InclusiveMulticast',
            False, 
            [
            _MetaInfoClassMember('ethernet-tag', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Ethernet Tag
                ''',
                'ethernet_tag',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('ethernet-tag-xr', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Ethernet Tag
                ''',
                'ethernet_tag_xr',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('evi', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                EVPN id
                ''',
                'evi',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('evi-xr', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                E-VPN id
                ''',
                'evi_xr',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('is-local-entry', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Local entry
                ''',
                'is_local_entry',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('next-hop', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IP of nexthop
                ''',
                'next_hop',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('originating-ip', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Originating IP
                ''',
                'originating_ip',
                'Cisco-IOS-XR-evpn-oper', False, [
                    _MetaInfoClassMember('originating-ip', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Originating IP
                        ''',
                        'originating_ip',
                        'Cisco-IOS-XR-evpn-oper', False),
                    _MetaInfoClassMember('originating-ip', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Originating IP
                        ''',
                        'originating_ip',
                        'Cisco-IOS-XR-evpn-oper', False),
                ]),
            _MetaInfoClassMember('originating-ip-xr', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                Originating IP
                ''',
                'originating_ip_xr',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('output-label', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Output label
                ''',
                'output_label',
                'Cisco-IOS-XR-evpn-oper', False),
            ],
            'Cisco-IOS-XR-evpn-oper',
            'inclusive-multicast',
            _yang_ns._namespaces['Cisco-IOS-XR-evpn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper'
        ),
    },
    'Evpn.Nodes.Node.EviDetail.EviChildren.InclusiveMulticasts' : {
        'meta_info' : _MetaInfoClass('Evpn.Nodes.Node.EviDetail.EviChildren.InclusiveMulticasts',
            False, 
            [
            _MetaInfoClassMember('inclusive-multicast', REFERENCE_LIST, 'InclusiveMulticast' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'Evpn.Nodes.Node.EviDetail.EviChildren.InclusiveMulticasts.InclusiveMulticast', 
                [], [], 
                '''                L2VPN EVPN IMCAST table
                ''',
                'inclusive_multicast',
                'Cisco-IOS-XR-evpn-oper', False),
            ],
            'Cisco-IOS-XR-evpn-oper',
            'inclusive-multicasts',
            _yang_ns._namespaces['Cisco-IOS-XR-evpn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper'
        ),
    },
    'Evpn.Nodes.Node.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_.TwoByteAs' : {
        'meta_info' : _MetaInfoClass('Evpn.Nodes.Node.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_.TwoByteAs',
            False, 
            [
            _MetaInfoClassMember('four-byte-index', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                4 Byte Index
                ''',
                'four_byte_index',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('two-byte-as', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                2 Byte AS Number
                ''',
                'two_byte_as',
                'Cisco-IOS-XR-evpn-oper', False),
            ],
            'Cisco-IOS-XR-evpn-oper',
            'two-byte-as',
            _yang_ns._namespaces['Cisco-IOS-XR-evpn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper'
        ),
    },
    'Evpn.Nodes.Node.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_.FourByteAs' : {
        'meta_info' : _MetaInfoClass('Evpn.Nodes.Node.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_.FourByteAs',
            False, 
            [
            _MetaInfoClassMember('four-byte-as', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                4 Byte AS Number
                ''',
                'four_byte_as',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('two-byte-index', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                2 Byte Index
                ''',
                'two_byte_index',
                'Cisco-IOS-XR-evpn-oper', False),
            ],
            'Cisco-IOS-XR-evpn-oper',
            'four-byte-as',
            _yang_ns._namespaces['Cisco-IOS-XR-evpn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper'
        ),
    },
    'Evpn.Nodes.Node.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_.V4Addr' : {
        'meta_info' : _MetaInfoClass('Evpn.Nodes.Node.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_.V4Addr',
            False, 
            [
            _MetaInfoClassMember('ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 Address
                ''',
                'ipv4_address',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('two-byte-index', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                2 Byte Index
                ''',
                'two_byte_index',
                'Cisco-IOS-XR-evpn-oper', False),
            ],
            'Cisco-IOS-XR-evpn-oper',
            'v4-addr',
            _yang_ns._namespaces['Cisco-IOS-XR-evpn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper'
        ),
    },
    'Evpn.Nodes.Node.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_.EsImport' : {
        'meta_info' : _MetaInfoClass('Evpn.Nodes.Node.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_.EsImport',
            False, 
            [
            _MetaInfoClassMember('high-bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Top 4 bytes of ES Import
                ''',
                'high_bytes',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('low-bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Low 2 bytes of ES Import
                ''',
                'low_bytes',
                'Cisco-IOS-XR-evpn-oper', False),
            ],
            'Cisco-IOS-XR-evpn-oper',
            'es-import',
            _yang_ns._namespaces['Cisco-IOS-XR-evpn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper'
        ),
    },
    'Evpn.Nodes.Node.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_' : {
        'meta_info' : _MetaInfoClass('Evpn.Nodes.Node.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_',
            False, 
            [
            _MetaInfoClassMember('es-import', REFERENCE_CLASS, 'EsImport' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'Evpn.Nodes.Node.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_.EsImport', 
                [], [], 
                '''                es import
                ''',
                'es_import',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('four-byte-as', REFERENCE_CLASS, 'FourByteAs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'Evpn.Nodes.Node.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_.FourByteAs', 
                [], [], 
                '''                four byte as
                ''',
                'four_byte_as',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('rt', REFERENCE_ENUM_CLASS, 'L2VpnAdRtEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'L2VpnAdRtEnum', 
                [], [], 
                '''                RT
                ''',
                'rt',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('two-byte-as', REFERENCE_CLASS, 'TwoByteAs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'Evpn.Nodes.Node.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_.TwoByteAs', 
                [], [], 
                '''                two byte as
                ''',
                'two_byte_as',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('v4-addr', REFERENCE_CLASS, 'V4Addr' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'Evpn.Nodes.Node.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_.V4Addr', 
                [], [], 
                '''                v4 addr
                ''',
                'v4_addr',
                'Cisco-IOS-XR-evpn-oper', False),
            ],
            'Cisco-IOS-XR-evpn-oper',
            'route-target',
            _yang_ns._namespaces['Cisco-IOS-XR-evpn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper'
        ),
    },
    'Evpn.Nodes.Node.EviDetail.EviChildren.RouteTargets.RouteTarget' : {
        'meta_info' : _MetaInfoClass('Evpn.Nodes.Node.EviDetail.EviChildren.RouteTargets.RouteTarget',
            False, 
            [
            _MetaInfoClassMember('addr-index', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                RT IP Index
                ''',
                'addr_index',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                RT IPv4 Address
                ''',
                'address',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('as', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                Two or Four byte AS Number
                ''',
                'as_',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('as-index', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                RT AS Index
                ''',
                'as_index',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('bd-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Bridge Domain Name
                ''',
                'bd_name',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('evi', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                EVPN id
                ''',
                'evi',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('evi-xr', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                VPN ID
                ''',
                'evi_xr',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('format', REFERENCE_ENUM_CLASS, 'BgpRouteTargetFormatEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'BgpRouteTargetFormatEnum', 
                [], [], 
                '''                Format of the route target
                ''',
                'format',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('role', REFERENCE_ENUM_CLASS, 'BgpRouteTargetRoleEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'BgpRouteTargetRoleEnum', 
                [], [], 
                '''                Role of the route target
                ''',
                'role',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('route-target', REFERENCE_CLASS, 'RouteTarget_' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'Evpn.Nodes.Node.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_', 
                [], [], 
                '''                Route Target
                ''',
                'route_target',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('route-target-role', REFERENCE_ENUM_CLASS, 'L2VpnAdRtRoleEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'L2VpnAdRtRoleEnum', 
                [], [], 
                '''                RT Role
                ''',
                'route_target_role',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('route-target-stitching', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                RT Stitching
                ''',
                'route_target_stitching',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('type', REFERENCE_ENUM_CLASS, 'BgpRouteTargetEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'BgpRouteTargetEnum', 
                [], [], 
                '''                Type of the route target
                ''',
                'type',
                'Cisco-IOS-XR-evpn-oper', False),
            ],
            'Cisco-IOS-XR-evpn-oper',
            'route-target',
            _yang_ns._namespaces['Cisco-IOS-XR-evpn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper'
        ),
    },
    'Evpn.Nodes.Node.EviDetail.EviChildren.RouteTargets' : {
        'meta_info' : _MetaInfoClass('Evpn.Nodes.Node.EviDetail.EviChildren.RouteTargets',
            False, 
            [
            _MetaInfoClassMember('route-target', REFERENCE_LIST, 'RouteTarget' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'Evpn.Nodes.Node.EviDetail.EviChildren.RouteTargets.RouteTarget', 
                [], [], 
                '''                L2VPN EVPN EVI RT Table
                ''',
                'route_target',
                'Cisco-IOS-XR-evpn-oper', False),
            ],
            'Cisco-IOS-XR-evpn-oper',
            'route-targets',
            _yang_ns._namespaces['Cisco-IOS-XR-evpn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper'
        ),
    },
    'Evpn.Nodes.Node.EviDetail.EviChildren.Macs.Mac.PathBuffer' : {
        'meta_info' : _MetaInfoClass('Evpn.Nodes.Node.EviDetail.EviChildren.Macs.Mac.PathBuffer',
            False, 
            [
            _MetaInfoClassMember('next-hop', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                Next-hop IP address (v6 format)
                ''',
                'next_hop',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('output-label', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Output Label
                ''',
                'output_label',
                'Cisco-IOS-XR-evpn-oper', False),
            ],
            'Cisco-IOS-XR-evpn-oper',
            'path-buffer',
            _yang_ns._namespaces['Cisco-IOS-XR-evpn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper'
        ),
    },
    'Evpn.Nodes.Node.EviDetail.EviChildren.Macs.Mac' : {
        'meta_info' : _MetaInfoClass('Evpn.Nodes.Node.EviDetail.EviChildren.Macs.Mac',
            False, 
            [
            _MetaInfoClassMember('esi-port-key', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                ESI port key
                ''',
                'esi_port_key',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('ethernet-tag', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Ethernet Tag ID
                ''',
                'ethernet_tag',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('ethernet-tag-xr', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Ethernet Tag
                ''',
                'ethernet_tag_xr',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('evi', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                EVPN id
                ''',
                'evi',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('internal-label', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                MPLS Internal Label
                ''',
                'internal_label',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('ip-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                IP Address
                ''',
                'ip_address',
                'Cisco-IOS-XR-evpn-oper', False, [
                    _MetaInfoClassMember('ip-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP Address
                        ''',
                        'ip_address',
                        'Cisco-IOS-XR-evpn-oper', False),
                    _MetaInfoClassMember('ip-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP Address
                        ''',
                        'ip_address',
                        'Cisco-IOS-XR-evpn-oper', False),
                ]),
            _MetaInfoClassMember('ip-address-xr', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IP address (v6 format)
                ''',
                'ip_address_xr',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('is-local-mac', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Indication of MAC being locally generated
                ''',
                'is_local_mac',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('is-remote-mac', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Indication of MAC being remotely generated
                ''',
                'is_remote_mac',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('is-static', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Indication if MAC is statically configured
                ''',
                'is_static',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('learned-bridge-port-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Port the MAC was learned on
                ''',
                'learned_bridge_port_name',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('local-encap-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Encap type of local MAC
                ''',
                'local_encap_type',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('local-ethernet-segment-identifier', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Local Ethernet Segment id
                ''',
                'local_ethernet_segment_identifier',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('local-label', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Associated local label
                ''',
                'local_label',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('local-seq-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                local seq id
                ''',
                'local_seq_id',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('mac-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                MAC address
                ''',
                'mac_address',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('mac-address-xr', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                MAC address
                ''',
                'mac_address_xr',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('mac-flush-received', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Number of flushes received 
                ''',
                'mac_flush_received',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('mac-flush-requested', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Number of flushes requested 
                ''',
                'mac_flush_requested',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('num-paths', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                 Number of items in path list buffer
                ''',
                'num_paths',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('path-buffer', REFERENCE_LIST, 'PathBuffer' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'Evpn.Nodes.Node.EviDetail.EviChildren.Macs.Mac.PathBuffer', 
                [], [], 
                '''                Path List Buffer
                ''',
                'path_buffer',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('remote-encap-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Encap type of remote MAC
                ''',
                'remote_encap_type',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('remote-ethernet-segment-identifier', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Remote Ethernet Segment id
                ''',
                'remote_ethernet_segment_identifier',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('remote-seq-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                remote seq id
                ''',
                'remote_seq_id',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('resolved', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Internal Label has resolved per-ES EAD and
                per-EVI EAD or MAC routes
                ''',
                'resolved',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('soo-nexthop', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                SOO nexthop (v6 format)
                ''',
                'soo_nexthop',
                'Cisco-IOS-XR-evpn-oper', False),
            ],
            'Cisco-IOS-XR-evpn-oper',
            'mac',
            _yang_ns._namespaces['Cisco-IOS-XR-evpn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper'
        ),
    },
    'Evpn.Nodes.Node.EviDetail.EviChildren.Macs' : {
        'meta_info' : _MetaInfoClass('Evpn.Nodes.Node.EviDetail.EviChildren.Macs',
            False, 
            [
            _MetaInfoClassMember('mac', REFERENCE_LIST, 'Mac' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'Evpn.Nodes.Node.EviDetail.EviChildren.Macs.Mac', 
                [], [], 
                '''                L2VPN EVPN MAC table
                ''',
                'mac',
                'Cisco-IOS-XR-evpn-oper', False),
            ],
            'Cisco-IOS-XR-evpn-oper',
            'macs',
            _yang_ns._namespaces['Cisco-IOS-XR-evpn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper'
        ),
    },
    'Evpn.Nodes.Node.EviDetail.EviChildren' : {
        'meta_info' : _MetaInfoClass('Evpn.Nodes.Node.EviDetail.EviChildren',
            False, 
            [
            _MetaInfoClassMember('ethernet-auto-discoveries', REFERENCE_CLASS, 'EthernetAutoDiscoveries' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'Evpn.Nodes.Node.EviDetail.EviChildren.EthernetAutoDiscoveries', 
                [], [], 
                '''                EVPN Ethernet Auto-Discovery table
                ''',
                'ethernet_auto_discoveries',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('inclusive-multicasts', REFERENCE_CLASS, 'InclusiveMulticasts' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'Evpn.Nodes.Node.EviDetail.EviChildren.InclusiveMulticasts', 
                [], [], 
                '''                L2VPN EVPN IMCAST table
                ''',
                'inclusive_multicasts',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('macs', REFERENCE_CLASS, 'Macs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'Evpn.Nodes.Node.EviDetail.EviChildren.Macs', 
                [], [], 
                '''                L2VPN EVPN EVI MAC table
                ''',
                'macs',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('neighbors', REFERENCE_CLASS, 'Neighbors' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'Evpn.Nodes.Node.EviDetail.EviChildren.Neighbors', 
                [], [], 
                '''                EVPN Neighbor table
                ''',
                'neighbors',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('route-targets', REFERENCE_CLASS, 'RouteTargets' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'Evpn.Nodes.Node.EviDetail.EviChildren.RouteTargets', 
                [], [], 
                '''                L2VPN EVPN EVI RT Child Table
                ''',
                'route_targets',
                'Cisco-IOS-XR-evpn-oper', False),
            ],
            'Cisco-IOS-XR-evpn-oper',
            'evi-children',
            _yang_ns._namespaces['Cisco-IOS-XR-evpn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper'
        ),
    },
    'Evpn.Nodes.Node.EviDetail' : {
        'meta_info' : _MetaInfoClass('Evpn.Nodes.Node.EviDetail',
            False, 
            [
            _MetaInfoClassMember('elements', REFERENCE_CLASS, 'Elements' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'Evpn.Nodes.Node.EviDetail.Elements', 
                [], [], 
                '''                EVI BGP RT Detail Info Elements
                ''',
                'elements',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('evi-children', REFERENCE_CLASS, 'EviChildren' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'Evpn.Nodes.Node.EviDetail.EviChildren', 
                [], [], 
                '''                Container for all EVI detail info
                ''',
                'evi_children',
                'Cisco-IOS-XR-evpn-oper', False),
            ],
            'Cisco-IOS-XR-evpn-oper',
            'evi-detail',
            _yang_ns._namespaces['Cisco-IOS-XR-evpn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper'
        ),
    },
    'Evpn.Nodes.Node.EthernetSegments.EthernetSegment.NextHop' : {
        'meta_info' : _MetaInfoClass('Evpn.Nodes.Node.EthernetSegments.EthernetSegment.NextHop',
            False, 
            [
            _MetaInfoClassMember('next-hop', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                Next-hop IP address (v6 format)
                ''',
                'next_hop',
                'Cisco-IOS-XR-evpn-oper', False),
            ],
            'Cisco-IOS-XR-evpn-oper',
            'next-hop',
            _yang_ns._namespaces['Cisco-IOS-XR-evpn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper'
        ),
    },
    'Evpn.Nodes.Node.EthernetSegments.EthernetSegment.RemoteSplitHorizonGroupLabel' : {
        'meta_info' : _MetaInfoClass('Evpn.Nodes.Node.EthernetSegments.EthernetSegment.RemoteSplitHorizonGroupLabel',
            False, 
            [
            _MetaInfoClassMember('label', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Split horizon label associated with next-hop
                address
                ''',
                'label',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('next-hop', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                Next-hop IP address (v6 format)
                ''',
                'next_hop',
                'Cisco-IOS-XR-evpn-oper', False),
            ],
            'Cisco-IOS-XR-evpn-oper',
            'remote-split-horizon-group-label',
            _yang_ns._namespaces['Cisco-IOS-XR-evpn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper'
        ),
    },
    'Evpn.Nodes.Node.EthernetSegments.EthernetSegment' : {
        'meta_info' : _MetaInfoClass('Evpn.Nodes.Node.EthernetSegments.EthernetSegment',
            False, 
            [
            _MetaInfoClassMember('elected-d-fs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Count of service carving results - elected
                ''',
                'elected_d_fs',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('es-bgp-gates', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                ES BGP Gates
                ''',
                'es_bgp_gates',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('es-l2fib-gates', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                ES L2FIB Gates
                ''',
                'es_l2fib_gates',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('esi1', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{1,8}'], 
                '''                ES id (part 1/5)
                ''',
                'esi1',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('esi2', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{1,8}'], 
                '''                ES id (part 2/5)
                ''',
                'esi2',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('esi3', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{1,8}'], 
                '''                ES id (part 3/5)
                ''',
                'esi3',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('esi4', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{1,8}'], 
                '''                ES id (part 4/5)
                ''',
                'esi4',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('esi5', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{1,8}'], 
                '''                ES id (part 5/5)
                ''',
                'esi5',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('esi-type', REFERENCE_ENUM_CLASS, 'L2VpnEvpnEsiEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'L2VpnEvpnEsiEnum', 
                [], [], 
                '''                ESI Type
                ''',
                'esi_type',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('ethernet-segment-identifier', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Ethernet Segment id
                ''',
                'ethernet_segment_identifier',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('ethernet-segment-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Ethernet Segment Name
                ''',
                'ethernet_segment_name',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('ethernet-segment-state', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                State of the ethernet segment
                ''',
                'ethernet_segment_state',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('force-single-home', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Ethernet-Segment forced to single home
                ''',
                'force_single_home',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('forwarder-ports', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Count of Forwarders (AC, AC PW, VFI PW)
                ''',
                'forwarder_ports',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('if-handle', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Main port ifhandle
                ''',
                'if_handle',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface
                ''',
                'interface_name',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('load-balance-mode-config', REFERENCE_ENUM_CLASS, 'L2VpnEvpnLbModeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'L2VpnEvpnLbModeEnum', 
                [], [], 
                '''                Configured load balancing mode
                ''',
                'load_balance_mode_config',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('load-balance-mode-is-default', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Load balancing mode is default
                ''',
                'load_balance_mode_is_default',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('load-balance-mode-oper', REFERENCE_ENUM_CLASS, 'L2VpnEvpnLbModeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'L2VpnEvpnLbModeEnum', 
                [], [], 
                '''                Operational load balancing mode
                ''',
                'load_balance_mode_oper',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('local-split-horizon-group-label', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Local split horizon group label
                ''',
                'local_split_horizon_group_label',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('mac-flushing-mode-config', REFERENCE_ENUM_CLASS, 'L2VpnEvpnMfModeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'L2VpnEvpnMfModeEnum', 
                [], [], 
                '''                Configured MAC Flushing mode
                ''',
                'mac_flushing_mode_config',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('main-port-mac', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                Main Port MAC Address
                ''',
                'main_port_mac',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('main-port-role', REFERENCE_ENUM_CLASS, 'L2VpnRgStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'L2VpnRgStateEnum', 
                [], [], 
                '''                Main port redundancy group role
                ''',
                'main_port_role',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('mp-protected', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                MP is protected and not under EVPN control
                ''',
                'mp_protected',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('next-hop', REFERENCE_LIST, 'NextHop' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'Evpn.Nodes.Node.EthernetSegments.EthernetSegment.NextHop', 
                [], [], 
                '''                List of nexthop IPv6 addresses
                ''',
                'next_hop',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('not-config-d-fs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Count of service carving results - missing
                config detected
                ''',
                'not_config_d_fs',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('not-elected-d-fs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Count of service carving results - not elected
                ''',
                'not_elected_d_fs',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('num-up-p-ws', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of PWs in Up state
                ''',
                'num_up_p_ws',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('peering-timer', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Configured timer for triggering DF election
                (seconds)
                ''',
                'peering_timer',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('peering-timer-left', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Milliseconds left on DF election timer
                ''',
                'peering_timer_left',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('primary-service', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                List of Primary services ESI/I-SIDs
                ''',
                'primary_service',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('primary-services-input', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Input string of Primary services ESI/I-SIDs
                ''',
                'primary_services_input',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('recovery-timer', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Configured timer for (STP) recovery (seconds)
                ''',
                'recovery_timer',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('recovery-timer-left', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Milliseconds left on (STP) recovery timer
                ''',
                'recovery_timer_left',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('remote-split-horizon-group-label', REFERENCE_LIST, 'RemoteSplitHorizonGroupLabel' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'Evpn.Nodes.Node.EthernetSegments.EthernetSegment.RemoteSplitHorizonGroupLabel', 
                [], [], 
                '''                Remote split horizon group labels
                ''',
                'remote_split_horizon_group_label',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('route-target', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                ES-Import Route Target
                ''',
                'route_target',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('rt-origin', REFERENCE_ENUM_CLASS, 'L2VpnEvpnRtOriginEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'L2VpnEvpnRtOriginEnum', 
                [], [], 
                '''                Origin of operational ES-Import RT
                ''',
                'rt_origin',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('secondary-service', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                List of Secondary services ESI/I-SIDs
                ''',
                'secondary_service',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('secondary-services-input', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Input string of Secondary services ESI/I-SIDs
                ''',
                'secondary_services_input',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('service-carving-mode', REFERENCE_ENUM_CLASS, 'L2VpnEvpnScModeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'L2VpnEvpnScModeEnum', 
                [], [], 
                '''                Service carving mode
                ''',
                'service_carving_mode',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('service-carving-result', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Service carving results
                ''',
                'service_carving_result',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('service-carving-type', REFERENCE_ENUM_CLASS, 'L2VpnEvpnScEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'L2VpnEvpnScEnum', 
                [], [], 
                '''                Service Carving Type
                ''',
                'service_carving_type',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('source-mac-oper', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                Operational Source MAC address
                ''',
                'source_mac_oper',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('source-mac-origin', REFERENCE_ENUM_CLASS, 'L2VpnEvpnSmacSrcEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'L2VpnEvpnSmacSrcEnum', 
                [], [], 
                '''                Origin of operational source MAC address
                ''',
                'source_mac_origin',
                'Cisco-IOS-XR-evpn-oper', False),
            ],
            'Cisco-IOS-XR-evpn-oper',
            'ethernet-segment',
            _yang_ns._namespaces['Cisco-IOS-XR-evpn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper'
        ),
    },
    'Evpn.Nodes.Node.EthernetSegments' : {
        'meta_info' : _MetaInfoClass('Evpn.Nodes.Node.EthernetSegments',
            False, 
            [
            _MetaInfoClassMember('ethernet-segment', REFERENCE_LIST, 'EthernetSegment' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'Evpn.Nodes.Node.EthernetSegments.EthernetSegment', 
                [], [], 
                '''                EVPN Ethernet-Segment Entry
                ''',
                'ethernet_segment',
                'Cisco-IOS-XR-evpn-oper', False),
            ],
            'Cisco-IOS-XR-evpn-oper',
            'ethernet-segments',
            _yang_ns._namespaces['Cisco-IOS-XR-evpn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper'
        ),
    },
    'Evpn.Nodes.Node.AcIds.AcId' : {
        'meta_info' : _MetaInfoClass('Evpn.Nodes.Node.AcIds.AcId',
            False, 
            [
            _MetaInfoClassMember('ac-id', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                AC ID
                ''',
                'ac_id',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('evi', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                EVPN id
                ''',
                'evi',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('evi-xr', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                E-VPN id
                ''',
                'evi_xr',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('neighbor', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                Neighbor IP
                ''',
                'neighbor',
                'Cisco-IOS-XR-evpn-oper', False),
            ],
            'Cisco-IOS-XR-evpn-oper',
            'ac-id',
            _yang_ns._namespaces['Cisco-IOS-XR-evpn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper'
        ),
    },
    'Evpn.Nodes.Node.AcIds' : {
        'meta_info' : _MetaInfoClass('Evpn.Nodes.Node.AcIds',
            False, 
            [
            _MetaInfoClassMember('ac-id', REFERENCE_LIST, 'AcId' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'Evpn.Nodes.Node.AcIds.AcId', 
                [], [], 
                '''                EVPN AC ID table
                ''',
                'ac_id',
                'Cisco-IOS-XR-evpn-oper', False),
            ],
            'Cisco-IOS-XR-evpn-oper',
            'ac-ids',
            _yang_ns._namespaces['Cisco-IOS-XR-evpn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper'
        ),
    },
    'Evpn.Nodes.Node' : {
        'meta_info' : _MetaInfoClass('Evpn.Nodes.Node',
            False, 
            [
            _MetaInfoClassMember('node-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Location
                ''',
                'node_id',
                'Cisco-IOS-XR-evpn-oper', True),
            _MetaInfoClassMember('ac-ids', REFERENCE_CLASS, 'AcIds' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'Evpn.Nodes.Node.AcIds', 
                [], [], 
                '''                EVPN AC ID table
                ''',
                'ac_ids',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('ethernet-segments', REFERENCE_CLASS, 'EthernetSegments' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'Evpn.Nodes.Node.EthernetSegments', 
                [], [], 
                '''                EVPN Ethernet-Segment Table
                ''',
                'ethernet_segments',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('evi-detail', REFERENCE_CLASS, 'EviDetail' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'Evpn.Nodes.Node.EviDetail', 
                [], [], 
                '''                L2VPN EVI Detail Table
                ''',
                'evi_detail',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('evis', REFERENCE_CLASS, 'Evis' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'Evpn.Nodes.Node.Evis', 
                [], [], 
                '''                L2VPN EVPN EVI Table
                ''',
                'evis',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('summary', REFERENCE_CLASS, 'Summary' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'Evpn.Nodes.Node.Summary', 
                [], [], 
                '''                L2VPN EVPN Summary
                ''',
                'summary',
                'Cisco-IOS-XR-evpn-oper', False),
            ],
            'Cisco-IOS-XR-evpn-oper',
            'node',
            _yang_ns._namespaces['Cisco-IOS-XR-evpn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper'
        ),
    },
    'Evpn.Nodes' : {
        'meta_info' : _MetaInfoClass('Evpn.Nodes',
            False, 
            [
            _MetaInfoClassMember('node', REFERENCE_LIST, 'Node' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'Evpn.Nodes.Node', 
                [], [], 
                '''                EVPN operational data for a particular node
                ''',
                'node',
                'Cisco-IOS-XR-evpn-oper', False),
            ],
            'Cisco-IOS-XR-evpn-oper',
            'nodes',
            _yang_ns._namespaces['Cisco-IOS-XR-evpn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper'
        ),
    },
    'Evpn.Active.Evis.Evi' : {
        'meta_info' : _MetaInfoClass('Evpn.Active.Evis.Evi',
            False, 
            [
            _MetaInfoClassMember('evi', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                EVPN id
                ''',
                'evi',
                'Cisco-IOS-XR-evpn-oper', True),
            _MetaInfoClassMember('bd-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Bridge domain name
                ''',
                'bd_name',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('evi-xr', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                E-VPN id
                ''',
                'evi_xr',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('type', REFERENCE_ENUM_CLASS, 'EvpnEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'EvpnEnum', 
                [], [], 
                '''                Service Type
                ''',
                'type',
                'Cisco-IOS-XR-evpn-oper', False),
            ],
            'Cisco-IOS-XR-evpn-oper',
            'evi',
            _yang_ns._namespaces['Cisco-IOS-XR-evpn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper'
        ),
    },
    'Evpn.Active.Evis' : {
        'meta_info' : _MetaInfoClass('Evpn.Active.Evis',
            False, 
            [
            _MetaInfoClassMember('evi', REFERENCE_LIST, 'Evi' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'Evpn.Active.Evis.Evi', 
                [], [], 
                '''                L2VPN EVPN EVI Entry
                ''',
                'evi',
                'Cisco-IOS-XR-evpn-oper', False),
            ],
            'Cisco-IOS-XR-evpn-oper',
            'evis',
            _yang_ns._namespaces['Cisco-IOS-XR-evpn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper'
        ),
    },
    'Evpn.Active.Summary' : {
        'meta_info' : _MetaInfoClass('Evpn.Active.Summary',
            False, 
            [
            _MetaInfoClassMember('as', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                BGP AS number
                ''',
                'as_',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('es-entries', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of ES Entries in DB
                ''',
                'es_entries',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('es-global-mac-routes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of ES:Global MAC Routes
                ''',
                'es_global_mac_routes',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('ev-is', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of EVI DB Entries
                ''',
                'ev_is',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('global-source-mac', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                Global Source MAC Address
                ''',
                'global_source_mac',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('l2rib-throttle', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Send to L2RIB Throttled
                ''',
                'l2rib_throttle',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('labels', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Internal Labels
                ''',
                'labels',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('local-ead-routes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Local EAD Entries in DB
                ''',
                'local_ead_routes',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('local-imcast-routes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Local IMCAST Routes
                ''',
                'local_imcast_routes',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('local-ipv4-mac-routes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Local IPv4 MAC-IP Routes
                ''',
                'local_ipv4_mac_routes',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('local-ipv6-mac-routes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Local IPv6 MAC-IP Routes
                ''',
                'local_ipv6_mac_routes',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('local-mac-routes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Local MAC Routes
                ''',
                'local_mac_routes',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('logging-df-election-enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Logging EVPN Designated Forwarder changes
                enabled
                ''',
                'logging_df_election_enabled',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('neighbor-entries', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of neighbor Entries in DB
                ''',
                'neighbor_entries',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('peering-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                EVPN ES Peering Time (seconds)
                ''',
                'peering_time',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('recovery-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                EVPN ES Recovery Time (seconds)
                ''',
                'recovery_time',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('remote-ead-routes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Remote EAD Entries in DB
                ''',
                'remote_ead_routes',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('remote-imcast-routes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Remote IMCAST Routes
                ''',
                'remote_imcast_routes',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('remote-ipv4-mac-routes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Remote IPv4 MAC-IP Routes
                ''',
                'remote_ipv4_mac_routes',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('remote-ipv6-mac-routes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Remote IPv6 MAC-IP Routes
                ''',
                'remote_ipv6_mac_routes',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('remote-mac-routes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Remote MAC Routes
                ''',
                'remote_mac_routes',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('remote-soo-mac-routes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Remote Soo MAC Routes
                ''',
                'remote_soo_mac_routes',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('router-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                EVPN Router ID
                ''',
                'router_id',
                'Cisco-IOS-XR-evpn-oper', False),
            ],
            'Cisco-IOS-XR-evpn-oper',
            'summary',
            _yang_ns._namespaces['Cisco-IOS-XR-evpn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper'
        ),
    },
    'Evpn.Active.EviDetail.Elements.Element.FlowLabel' : {
        'meta_info' : _MetaInfoClass('Evpn.Active.EviDetail.Elements.Element.FlowLabel',
            False, 
            [
            _MetaInfoClassMember('global-flow-label', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Globally configured flow label
                ''',
                'global_flow_label',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('static-flow-label', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Static flow label
                ''',
                'static_flow_label',
                'Cisco-IOS-XR-evpn-oper', False),
            ],
            'Cisco-IOS-XR-evpn-oper',
            'flow-label',
            _yang_ns._namespaces['Cisco-IOS-XR-evpn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper'
        ),
    },
    'Evpn.Active.EviDetail.Elements.Element.RdAuto.Auto' : {
        'meta_info' : _MetaInfoClass('Evpn.Active.EviDetail.Elements.Element.RdAuto.Auto',
            False, 
            [
            _MetaInfoClassMember('auto-index', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Auto-generated Index
                ''',
                'auto_index',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('router-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                BGP Router ID
                ''',
                'router_id',
                'Cisco-IOS-XR-evpn-oper', False),
            ],
            'Cisco-IOS-XR-evpn-oper',
            'auto',
            _yang_ns._namespaces['Cisco-IOS-XR-evpn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper'
        ),
    },
    'Evpn.Active.EviDetail.Elements.Element.RdAuto.TwoByteAs' : {
        'meta_info' : _MetaInfoClass('Evpn.Active.EviDetail.Elements.Element.RdAuto.TwoByteAs',
            False, 
            [
            _MetaInfoClassMember('four-byte-index', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                4 Byte Index
                ''',
                'four_byte_index',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('two-byte-as', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                2 Byte AS Number
                ''',
                'two_byte_as',
                'Cisco-IOS-XR-evpn-oper', False),
            ],
            'Cisco-IOS-XR-evpn-oper',
            'two-byte-as',
            _yang_ns._namespaces['Cisco-IOS-XR-evpn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper'
        ),
    },
    'Evpn.Active.EviDetail.Elements.Element.RdAuto.FourByteAs' : {
        'meta_info' : _MetaInfoClass('Evpn.Active.EviDetail.Elements.Element.RdAuto.FourByteAs',
            False, 
            [
            _MetaInfoClassMember('four-byte-as', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                4 Byte AS Number
                ''',
                'four_byte_as',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('two-byte-index', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                2 Byte Index
                ''',
                'two_byte_index',
                'Cisco-IOS-XR-evpn-oper', False),
            ],
            'Cisco-IOS-XR-evpn-oper',
            'four-byte-as',
            _yang_ns._namespaces['Cisco-IOS-XR-evpn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper'
        ),
    },
    'Evpn.Active.EviDetail.Elements.Element.RdAuto.V4Addr' : {
        'meta_info' : _MetaInfoClass('Evpn.Active.EviDetail.Elements.Element.RdAuto.V4Addr',
            False, 
            [
            _MetaInfoClassMember('ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 Address
                ''',
                'ipv4_address',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('two-byte-index', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                2 Byte Index
                ''',
                'two_byte_index',
                'Cisco-IOS-XR-evpn-oper', False),
            ],
            'Cisco-IOS-XR-evpn-oper',
            'v4-addr',
            _yang_ns._namespaces['Cisco-IOS-XR-evpn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper'
        ),
    },
    'Evpn.Active.EviDetail.Elements.Element.RdAuto' : {
        'meta_info' : _MetaInfoClass('Evpn.Active.EviDetail.Elements.Element.RdAuto',
            False, 
            [
            _MetaInfoClassMember('auto', REFERENCE_CLASS, 'Auto' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'Evpn.Active.EviDetail.Elements.Element.RdAuto.Auto', 
                [], [], 
                '''                auto
                ''',
                'auto',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('four-byte-as', REFERENCE_CLASS, 'FourByteAs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'Evpn.Active.EviDetail.Elements.Element.RdAuto.FourByteAs', 
                [], [], 
                '''                four byte as
                ''',
                'four_byte_as',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('rd', REFERENCE_ENUM_CLASS, 'L2VpnAdRdEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'L2VpnAdRdEnum', 
                [], [], 
                '''                RD
                ''',
                'rd',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('two-byte-as', REFERENCE_CLASS, 'TwoByteAs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'Evpn.Active.EviDetail.Elements.Element.RdAuto.TwoByteAs', 
                [], [], 
                '''                two byte as
                ''',
                'two_byte_as',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('v4-addr', REFERENCE_CLASS, 'V4Addr' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'Evpn.Active.EviDetail.Elements.Element.RdAuto.V4Addr', 
                [], [], 
                '''                v4 addr
                ''',
                'v4_addr',
                'Cisco-IOS-XR-evpn-oper', False),
            ],
            'Cisco-IOS-XR-evpn-oper',
            'rd-auto',
            _yang_ns._namespaces['Cisco-IOS-XR-evpn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper'
        ),
    },
    'Evpn.Active.EviDetail.Elements.Element.RdConfigured.Auto' : {
        'meta_info' : _MetaInfoClass('Evpn.Active.EviDetail.Elements.Element.RdConfigured.Auto',
            False, 
            [
            _MetaInfoClassMember('auto-index', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Auto-generated Index
                ''',
                'auto_index',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('router-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                BGP Router ID
                ''',
                'router_id',
                'Cisco-IOS-XR-evpn-oper', False),
            ],
            'Cisco-IOS-XR-evpn-oper',
            'auto',
            _yang_ns._namespaces['Cisco-IOS-XR-evpn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper'
        ),
    },
    'Evpn.Active.EviDetail.Elements.Element.RdConfigured.TwoByteAs' : {
        'meta_info' : _MetaInfoClass('Evpn.Active.EviDetail.Elements.Element.RdConfigured.TwoByteAs',
            False, 
            [
            _MetaInfoClassMember('four-byte-index', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                4 Byte Index
                ''',
                'four_byte_index',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('two-byte-as', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                2 Byte AS Number
                ''',
                'two_byte_as',
                'Cisco-IOS-XR-evpn-oper', False),
            ],
            'Cisco-IOS-XR-evpn-oper',
            'two-byte-as',
            _yang_ns._namespaces['Cisco-IOS-XR-evpn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper'
        ),
    },
    'Evpn.Active.EviDetail.Elements.Element.RdConfigured.FourByteAs' : {
        'meta_info' : _MetaInfoClass('Evpn.Active.EviDetail.Elements.Element.RdConfigured.FourByteAs',
            False, 
            [
            _MetaInfoClassMember('four-byte-as', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                4 Byte AS Number
                ''',
                'four_byte_as',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('two-byte-index', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                2 Byte Index
                ''',
                'two_byte_index',
                'Cisco-IOS-XR-evpn-oper', False),
            ],
            'Cisco-IOS-XR-evpn-oper',
            'four-byte-as',
            _yang_ns._namespaces['Cisco-IOS-XR-evpn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper'
        ),
    },
    'Evpn.Active.EviDetail.Elements.Element.RdConfigured.V4Addr' : {
        'meta_info' : _MetaInfoClass('Evpn.Active.EviDetail.Elements.Element.RdConfigured.V4Addr',
            False, 
            [
            _MetaInfoClassMember('ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 Address
                ''',
                'ipv4_address',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('two-byte-index', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                2 Byte Index
                ''',
                'two_byte_index',
                'Cisco-IOS-XR-evpn-oper', False),
            ],
            'Cisco-IOS-XR-evpn-oper',
            'v4-addr',
            _yang_ns._namespaces['Cisco-IOS-XR-evpn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper'
        ),
    },
    'Evpn.Active.EviDetail.Elements.Element.RdConfigured' : {
        'meta_info' : _MetaInfoClass('Evpn.Active.EviDetail.Elements.Element.RdConfigured',
            False, 
            [
            _MetaInfoClassMember('auto', REFERENCE_CLASS, 'Auto' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'Evpn.Active.EviDetail.Elements.Element.RdConfigured.Auto', 
                [], [], 
                '''                auto
                ''',
                'auto',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('four-byte-as', REFERENCE_CLASS, 'FourByteAs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'Evpn.Active.EviDetail.Elements.Element.RdConfigured.FourByteAs', 
                [], [], 
                '''                four byte as
                ''',
                'four_byte_as',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('rd', REFERENCE_ENUM_CLASS, 'L2VpnAdRdEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'L2VpnAdRdEnum', 
                [], [], 
                '''                RD
                ''',
                'rd',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('two-byte-as', REFERENCE_CLASS, 'TwoByteAs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'Evpn.Active.EviDetail.Elements.Element.RdConfigured.TwoByteAs', 
                [], [], 
                '''                two byte as
                ''',
                'two_byte_as',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('v4-addr', REFERENCE_CLASS, 'V4Addr' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'Evpn.Active.EviDetail.Elements.Element.RdConfigured.V4Addr', 
                [], [], 
                '''                v4 addr
                ''',
                'v4_addr',
                'Cisco-IOS-XR-evpn-oper', False),
            ],
            'Cisco-IOS-XR-evpn-oper',
            'rd-configured',
            _yang_ns._namespaces['Cisco-IOS-XR-evpn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper'
        ),
    },
    'Evpn.Active.EviDetail.Elements.Element.RtAuto.TwoByteAs' : {
        'meta_info' : _MetaInfoClass('Evpn.Active.EviDetail.Elements.Element.RtAuto.TwoByteAs',
            False, 
            [
            _MetaInfoClassMember('four-byte-index', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                4 Byte Index
                ''',
                'four_byte_index',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('two-byte-as', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                2 Byte AS Number
                ''',
                'two_byte_as',
                'Cisco-IOS-XR-evpn-oper', False),
            ],
            'Cisco-IOS-XR-evpn-oper',
            'two-byte-as',
            _yang_ns._namespaces['Cisco-IOS-XR-evpn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper'
        ),
    },
    'Evpn.Active.EviDetail.Elements.Element.RtAuto.FourByteAs' : {
        'meta_info' : _MetaInfoClass('Evpn.Active.EviDetail.Elements.Element.RtAuto.FourByteAs',
            False, 
            [
            _MetaInfoClassMember('four-byte-as', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                4 Byte AS Number
                ''',
                'four_byte_as',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('two-byte-index', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                2 Byte Index
                ''',
                'two_byte_index',
                'Cisco-IOS-XR-evpn-oper', False),
            ],
            'Cisco-IOS-XR-evpn-oper',
            'four-byte-as',
            _yang_ns._namespaces['Cisco-IOS-XR-evpn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper'
        ),
    },
    'Evpn.Active.EviDetail.Elements.Element.RtAuto.V4Addr' : {
        'meta_info' : _MetaInfoClass('Evpn.Active.EviDetail.Elements.Element.RtAuto.V4Addr',
            False, 
            [
            _MetaInfoClassMember('ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 Address
                ''',
                'ipv4_address',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('two-byte-index', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                2 Byte Index
                ''',
                'two_byte_index',
                'Cisco-IOS-XR-evpn-oper', False),
            ],
            'Cisco-IOS-XR-evpn-oper',
            'v4-addr',
            _yang_ns._namespaces['Cisco-IOS-XR-evpn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper'
        ),
    },
    'Evpn.Active.EviDetail.Elements.Element.RtAuto.EsImport' : {
        'meta_info' : _MetaInfoClass('Evpn.Active.EviDetail.Elements.Element.RtAuto.EsImport',
            False, 
            [
            _MetaInfoClassMember('high-bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Top 4 bytes of ES Import
                ''',
                'high_bytes',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('low-bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Low 2 bytes of ES Import
                ''',
                'low_bytes',
                'Cisco-IOS-XR-evpn-oper', False),
            ],
            'Cisco-IOS-XR-evpn-oper',
            'es-import',
            _yang_ns._namespaces['Cisco-IOS-XR-evpn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper'
        ),
    },
    'Evpn.Active.EviDetail.Elements.Element.RtAuto' : {
        'meta_info' : _MetaInfoClass('Evpn.Active.EviDetail.Elements.Element.RtAuto',
            False, 
            [
            _MetaInfoClassMember('es-import', REFERENCE_CLASS, 'EsImport' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'Evpn.Active.EviDetail.Elements.Element.RtAuto.EsImport', 
                [], [], 
                '''                es import
                ''',
                'es_import',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('four-byte-as', REFERENCE_CLASS, 'FourByteAs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'Evpn.Active.EviDetail.Elements.Element.RtAuto.FourByteAs', 
                [], [], 
                '''                four byte as
                ''',
                'four_byte_as',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('rt', REFERENCE_ENUM_CLASS, 'L2VpnAdRtEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'L2VpnAdRtEnum', 
                [], [], 
                '''                RT
                ''',
                'rt',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('two-byte-as', REFERENCE_CLASS, 'TwoByteAs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'Evpn.Active.EviDetail.Elements.Element.RtAuto.TwoByteAs', 
                [], [], 
                '''                two byte as
                ''',
                'two_byte_as',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('v4-addr', REFERENCE_CLASS, 'V4Addr' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'Evpn.Active.EviDetail.Elements.Element.RtAuto.V4Addr', 
                [], [], 
                '''                v4 addr
                ''',
                'v4_addr',
                'Cisco-IOS-XR-evpn-oper', False),
            ],
            'Cisco-IOS-XR-evpn-oper',
            'rt-auto',
            _yang_ns._namespaces['Cisco-IOS-XR-evpn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper'
        ),
    },
    'Evpn.Active.EviDetail.Elements.Element.RtAutoStitching.TwoByteAs' : {
        'meta_info' : _MetaInfoClass('Evpn.Active.EviDetail.Elements.Element.RtAutoStitching.TwoByteAs',
            False, 
            [
            _MetaInfoClassMember('four-byte-index', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                4 Byte Index
                ''',
                'four_byte_index',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('two-byte-as', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                2 Byte AS Number
                ''',
                'two_byte_as',
                'Cisco-IOS-XR-evpn-oper', False),
            ],
            'Cisco-IOS-XR-evpn-oper',
            'two-byte-as',
            _yang_ns._namespaces['Cisco-IOS-XR-evpn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper'
        ),
    },
    'Evpn.Active.EviDetail.Elements.Element.RtAutoStitching.FourByteAs' : {
        'meta_info' : _MetaInfoClass('Evpn.Active.EviDetail.Elements.Element.RtAutoStitching.FourByteAs',
            False, 
            [
            _MetaInfoClassMember('four-byte-as', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                4 Byte AS Number
                ''',
                'four_byte_as',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('two-byte-index', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                2 Byte Index
                ''',
                'two_byte_index',
                'Cisco-IOS-XR-evpn-oper', False),
            ],
            'Cisco-IOS-XR-evpn-oper',
            'four-byte-as',
            _yang_ns._namespaces['Cisco-IOS-XR-evpn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper'
        ),
    },
    'Evpn.Active.EviDetail.Elements.Element.RtAutoStitching.V4Addr' : {
        'meta_info' : _MetaInfoClass('Evpn.Active.EviDetail.Elements.Element.RtAutoStitching.V4Addr',
            False, 
            [
            _MetaInfoClassMember('ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 Address
                ''',
                'ipv4_address',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('two-byte-index', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                2 Byte Index
                ''',
                'two_byte_index',
                'Cisco-IOS-XR-evpn-oper', False),
            ],
            'Cisco-IOS-XR-evpn-oper',
            'v4-addr',
            _yang_ns._namespaces['Cisco-IOS-XR-evpn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper'
        ),
    },
    'Evpn.Active.EviDetail.Elements.Element.RtAutoStitching.EsImport' : {
        'meta_info' : _MetaInfoClass('Evpn.Active.EviDetail.Elements.Element.RtAutoStitching.EsImport',
            False, 
            [
            _MetaInfoClassMember('high-bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Top 4 bytes of ES Import
                ''',
                'high_bytes',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('low-bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Low 2 bytes of ES Import
                ''',
                'low_bytes',
                'Cisco-IOS-XR-evpn-oper', False),
            ],
            'Cisco-IOS-XR-evpn-oper',
            'es-import',
            _yang_ns._namespaces['Cisco-IOS-XR-evpn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper'
        ),
    },
    'Evpn.Active.EviDetail.Elements.Element.RtAutoStitching' : {
        'meta_info' : _MetaInfoClass('Evpn.Active.EviDetail.Elements.Element.RtAutoStitching',
            False, 
            [
            _MetaInfoClassMember('es-import', REFERENCE_CLASS, 'EsImport' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'Evpn.Active.EviDetail.Elements.Element.RtAutoStitching.EsImport', 
                [], [], 
                '''                es import
                ''',
                'es_import',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('four-byte-as', REFERENCE_CLASS, 'FourByteAs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'Evpn.Active.EviDetail.Elements.Element.RtAutoStitching.FourByteAs', 
                [], [], 
                '''                four byte as
                ''',
                'four_byte_as',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('rt', REFERENCE_ENUM_CLASS, 'L2VpnAdRtEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'L2VpnAdRtEnum', 
                [], [], 
                '''                RT
                ''',
                'rt',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('two-byte-as', REFERENCE_CLASS, 'TwoByteAs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'Evpn.Active.EviDetail.Elements.Element.RtAutoStitching.TwoByteAs', 
                [], [], 
                '''                two byte as
                ''',
                'two_byte_as',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('v4-addr', REFERENCE_CLASS, 'V4Addr' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'Evpn.Active.EviDetail.Elements.Element.RtAutoStitching.V4Addr', 
                [], [], 
                '''                v4 addr
                ''',
                'v4_addr',
                'Cisco-IOS-XR-evpn-oper', False),
            ],
            'Cisco-IOS-XR-evpn-oper',
            'rt-auto-stitching',
            _yang_ns._namespaces['Cisco-IOS-XR-evpn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper'
        ),
    },
    'Evpn.Active.EviDetail.Elements.Element' : {
        'meta_info' : _MetaInfoClass('Evpn.Active.EviDetail.Elements.Element',
            False, 
            [
            _MetaInfoClassMember('evi', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                EVPN id
                ''',
                'evi',
                'Cisco-IOS-XR-evpn-oper', True),
            _MetaInfoClassMember('advertise-mac', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Advertise MAC-only routes on this EVI
                ''',
                'advertise_mac',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('aliasing-disabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Route Aliasing is disabled
                ''',
                'aliasing_disabled',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('bd-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Bridge domain name
                ''',
                'bd_name',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('cw-disable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Control-Word Disable
                ''',
                'cw_disable',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('description', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                EVI description
                ''',
                'description',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('evi-xr', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                E-VPN id
                ''',
                'evi_xr',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('flow-label', REFERENCE_CLASS, 'FlowLabel' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'Evpn.Active.EviDetail.Elements.Element.FlowLabel', 
                [], [], 
                '''                Flow Label Information
                ''',
                'flow_label',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('forward-class', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Forward Class attribute
                ''',
                'forward_class',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('multicast-label', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Multicast Label
                ''',
                'multicast_label',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('rd-auto', REFERENCE_CLASS, 'RdAuto' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'Evpn.Active.EviDetail.Elements.Element.RdAuto', 
                [], [], 
                '''                Automatic Route Distingtuisher
                ''',
                'rd_auto',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('rd-configured', REFERENCE_CLASS, 'RdConfigured' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'Evpn.Active.EviDetail.Elements.Element.RdConfigured', 
                [], [], 
                '''                Configured Route Distinguisher
                ''',
                'rd_configured',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('reoriginate-disabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Route Re-origination is disabled
                ''',
                'reoriginate_disabled',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('rt-auto', REFERENCE_CLASS, 'RtAuto' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'Evpn.Active.EviDetail.Elements.Element.RtAuto', 
                [], [], 
                '''                Automatic Route Target
                ''',
                'rt_auto',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('rt-auto-stitching', REFERENCE_CLASS, 'RtAutoStitching' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'Evpn.Active.EviDetail.Elements.Element.RtAutoStitching', 
                [], [], 
                '''                Automatic Route Target Stitching
                ''',
                'rt_auto_stitching',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('rt-export-block-set', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is Export RT None set
                ''',
                'rt_export_block_set',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('rt-import-block-set', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is Import RT None set
                ''',
                'rt_import_block_set',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('stitching', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                RT Stitching for MPLS Fabric is enabled
                ''',
                'stitching',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('table-policy-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Table-policy Name
                ''',
                'table_policy_name',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('type', REFERENCE_ENUM_CLASS, 'EvpnEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'EvpnEnum', 
                [], [], 
                '''                Service Type
                ''',
                'type',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('unicast-label', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Unicast Label
                ''',
                'unicast_label',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('unknown-unicast-flooding-disabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Unknown-unicast flooding is disabled
                ''',
                'unknown_unicast_flooding_disabled',
                'Cisco-IOS-XR-evpn-oper', False),
            ],
            'Cisco-IOS-XR-evpn-oper',
            'element',
            _yang_ns._namespaces['Cisco-IOS-XR-evpn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper'
        ),
    },
    'Evpn.Active.EviDetail.Elements' : {
        'meta_info' : _MetaInfoClass('Evpn.Active.EviDetail.Elements',
            False, 
            [
            _MetaInfoClassMember('element', REFERENCE_LIST, 'Element' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'Evpn.Active.EviDetail.Elements.Element', 
                [], [], 
                '''                EVI BGP RT Detail Info
                ''',
                'element',
                'Cisco-IOS-XR-evpn-oper', False),
            ],
            'Cisco-IOS-XR-evpn-oper',
            'elements',
            _yang_ns._namespaces['Cisco-IOS-XR-evpn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper'
        ),
    },
    'Evpn.Active.EviDetail.EviChildren.Neighbors.Neighbor' : {
        'meta_info' : _MetaInfoClass('Evpn.Active.EviDetail.EviChildren.Neighbors.Neighbor',
            False, 
            [
            _MetaInfoClassMember('evi', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                EVPN id
                ''',
                'evi',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('evi-xr', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                E-VPN id
                ''',
                'evi_xr',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('neighbor', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                Neighbor IP
                ''',
                'neighbor',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('neighbor-ip', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Neighbor IP
                ''',
                'neighbor_ip',
                'Cisco-IOS-XR-evpn-oper', False, [
                    _MetaInfoClassMember('neighbor-ip', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Neighbor IP
                        ''',
                        'neighbor_ip',
                        'Cisco-IOS-XR-evpn-oper', False),
                    _MetaInfoClassMember('neighbor-ip', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Neighbor IP
                        ''',
                        'neighbor_ip',
                        'Cisco-IOS-XR-evpn-oper', False),
                ]),
            ],
            'Cisco-IOS-XR-evpn-oper',
            'neighbor',
            _yang_ns._namespaces['Cisco-IOS-XR-evpn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper'
        ),
    },
    'Evpn.Active.EviDetail.EviChildren.Neighbors' : {
        'meta_info' : _MetaInfoClass('Evpn.Active.EviDetail.EviChildren.Neighbors',
            False, 
            [
            _MetaInfoClassMember('neighbor', REFERENCE_LIST, 'Neighbor' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'Evpn.Active.EviDetail.EviChildren.Neighbors.Neighbor', 
                [], [], 
                '''                EVPN Neighbor table
                ''',
                'neighbor',
                'Cisco-IOS-XR-evpn-oper', False),
            ],
            'Cisco-IOS-XR-evpn-oper',
            'neighbors',
            _yang_ns._namespaces['Cisco-IOS-XR-evpn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper'
        ),
    },
    'Evpn.Active.EviDetail.EviChildren.EthernetAutoDiscoveries.EthernetAutoDiscovery.PathBuffer' : {
        'meta_info' : _MetaInfoClass('Evpn.Active.EviDetail.EviChildren.EthernetAutoDiscoveries.EthernetAutoDiscovery.PathBuffer',
            False, 
            [
            _MetaInfoClassMember('next-hop', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                Next-hop IP address (v6 format)
                ''',
                'next_hop',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('output-label', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Output Label
                ''',
                'output_label',
                'Cisco-IOS-XR-evpn-oper', False),
            ],
            'Cisco-IOS-XR-evpn-oper',
            'path-buffer',
            _yang_ns._namespaces['Cisco-IOS-XR-evpn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper'
        ),
    },
    'Evpn.Active.EviDetail.EviChildren.EthernetAutoDiscoveries.EthernetAutoDiscovery' : {
        'meta_info' : _MetaInfoClass('Evpn.Active.EviDetail.EviChildren.EthernetAutoDiscoveries.EthernetAutoDiscovery',
            False, 
            [
            _MetaInfoClassMember('encap', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Encap type of local or remote EAD
                ''',
                'encap',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('esi1', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{1,8}'], 
                '''                ES id (part 1/5)
                ''',
                'esi1',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('esi2', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{1,8}'], 
                '''                ES id (part 2/5)
                ''',
                'esi2',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('esi3', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{1,8}'], 
                '''                ES id (part 3/5)
                ''',
                'esi3',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('esi4', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{1,8}'], 
                '''                ES id (part 4/5)
                ''',
                'esi4',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('esi5', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{1,8}'], 
                '''                ES id (part 5/5)
                ''',
                'esi5',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('ethernet-segment-identifier', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Ethernet Segment id
                ''',
                'ethernet_segment_identifier',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('ethernet-tag', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Ethernet Tag ID
                ''',
                'ethernet_tag',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('ethernet-tag-xr', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Ethernet Tag
                ''',
                'ethernet_tag_xr',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('ethernet-vpnid', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                E-VPN id
                ''',
                'ethernet_vpnid',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('evi', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                EVPN id
                ''',
                'evi',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('is-local-ead', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Indication of EthernetAutoDiscovery Route is
                local
                ''',
                'is_local_ead',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('local-label', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Associated local label
                ''',
                'local_label',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('local-next-hop', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                Local nexthop IP
                ''',
                'local_next_hop',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('num-paths', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                 Number of items in path list buffer
                ''',
                'num_paths',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('path-buffer', REFERENCE_LIST, 'PathBuffer' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'Evpn.Active.EviDetail.EviChildren.EthernetAutoDiscoveries.EthernetAutoDiscovery.PathBuffer', 
                [], [], 
                '''                Path List Buffer
                ''',
                'path_buffer',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('redundancy-single-active', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Single-active redundancy configured at remote
                EAD
                ''',
                'redundancy_single_active',
                'Cisco-IOS-XR-evpn-oper', False),
            ],
            'Cisco-IOS-XR-evpn-oper',
            'ethernet-auto-discovery',
            _yang_ns._namespaces['Cisco-IOS-XR-evpn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper'
        ),
    },
    'Evpn.Active.EviDetail.EviChildren.EthernetAutoDiscoveries' : {
        'meta_info' : _MetaInfoClass('Evpn.Active.EviDetail.EviChildren.EthernetAutoDiscoveries',
            False, 
            [
            _MetaInfoClassMember('ethernet-auto-discovery', REFERENCE_LIST, 'EthernetAutoDiscovery' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'Evpn.Active.EviDetail.EviChildren.EthernetAutoDiscoveries.EthernetAutoDiscovery', 
                [], [], 
                '''                EVPN Ethernet Auto-Discovery Entry
                ''',
                'ethernet_auto_discovery',
                'Cisco-IOS-XR-evpn-oper', False),
            ],
            'Cisco-IOS-XR-evpn-oper',
            'ethernet-auto-discoveries',
            _yang_ns._namespaces['Cisco-IOS-XR-evpn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper'
        ),
    },
    'Evpn.Active.EviDetail.EviChildren.InclusiveMulticasts.InclusiveMulticast' : {
        'meta_info' : _MetaInfoClass('Evpn.Active.EviDetail.EviChildren.InclusiveMulticasts.InclusiveMulticast',
            False, 
            [
            _MetaInfoClassMember('ethernet-tag', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Ethernet Tag
                ''',
                'ethernet_tag',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('ethernet-tag-xr', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Ethernet Tag
                ''',
                'ethernet_tag_xr',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('evi', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                EVPN id
                ''',
                'evi',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('evi-xr', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                E-VPN id
                ''',
                'evi_xr',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('is-local-entry', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Local entry
                ''',
                'is_local_entry',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('next-hop', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IP of nexthop
                ''',
                'next_hop',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('originating-ip', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Originating IP
                ''',
                'originating_ip',
                'Cisco-IOS-XR-evpn-oper', False, [
                    _MetaInfoClassMember('originating-ip', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Originating IP
                        ''',
                        'originating_ip',
                        'Cisco-IOS-XR-evpn-oper', False),
                    _MetaInfoClassMember('originating-ip', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Originating IP
                        ''',
                        'originating_ip',
                        'Cisco-IOS-XR-evpn-oper', False),
                ]),
            _MetaInfoClassMember('originating-ip-xr', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                Originating IP
                ''',
                'originating_ip_xr',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('output-label', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Output label
                ''',
                'output_label',
                'Cisco-IOS-XR-evpn-oper', False),
            ],
            'Cisco-IOS-XR-evpn-oper',
            'inclusive-multicast',
            _yang_ns._namespaces['Cisco-IOS-XR-evpn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper'
        ),
    },
    'Evpn.Active.EviDetail.EviChildren.InclusiveMulticasts' : {
        'meta_info' : _MetaInfoClass('Evpn.Active.EviDetail.EviChildren.InclusiveMulticasts',
            False, 
            [
            _MetaInfoClassMember('inclusive-multicast', REFERENCE_LIST, 'InclusiveMulticast' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'Evpn.Active.EviDetail.EviChildren.InclusiveMulticasts.InclusiveMulticast', 
                [], [], 
                '''                L2VPN EVPN IMCAST table
                ''',
                'inclusive_multicast',
                'Cisco-IOS-XR-evpn-oper', False),
            ],
            'Cisco-IOS-XR-evpn-oper',
            'inclusive-multicasts',
            _yang_ns._namespaces['Cisco-IOS-XR-evpn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper'
        ),
    },
    'Evpn.Active.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_.TwoByteAs' : {
        'meta_info' : _MetaInfoClass('Evpn.Active.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_.TwoByteAs',
            False, 
            [
            _MetaInfoClassMember('four-byte-index', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                4 Byte Index
                ''',
                'four_byte_index',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('two-byte-as', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                2 Byte AS Number
                ''',
                'two_byte_as',
                'Cisco-IOS-XR-evpn-oper', False),
            ],
            'Cisco-IOS-XR-evpn-oper',
            'two-byte-as',
            _yang_ns._namespaces['Cisco-IOS-XR-evpn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper'
        ),
    },
    'Evpn.Active.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_.FourByteAs' : {
        'meta_info' : _MetaInfoClass('Evpn.Active.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_.FourByteAs',
            False, 
            [
            _MetaInfoClassMember('four-byte-as', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                4 Byte AS Number
                ''',
                'four_byte_as',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('two-byte-index', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                2 Byte Index
                ''',
                'two_byte_index',
                'Cisco-IOS-XR-evpn-oper', False),
            ],
            'Cisco-IOS-XR-evpn-oper',
            'four-byte-as',
            _yang_ns._namespaces['Cisco-IOS-XR-evpn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper'
        ),
    },
    'Evpn.Active.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_.V4Addr' : {
        'meta_info' : _MetaInfoClass('Evpn.Active.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_.V4Addr',
            False, 
            [
            _MetaInfoClassMember('ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 Address
                ''',
                'ipv4_address',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('two-byte-index', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                2 Byte Index
                ''',
                'two_byte_index',
                'Cisco-IOS-XR-evpn-oper', False),
            ],
            'Cisco-IOS-XR-evpn-oper',
            'v4-addr',
            _yang_ns._namespaces['Cisco-IOS-XR-evpn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper'
        ),
    },
    'Evpn.Active.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_.EsImport' : {
        'meta_info' : _MetaInfoClass('Evpn.Active.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_.EsImport',
            False, 
            [
            _MetaInfoClassMember('high-bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Top 4 bytes of ES Import
                ''',
                'high_bytes',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('low-bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Low 2 bytes of ES Import
                ''',
                'low_bytes',
                'Cisco-IOS-XR-evpn-oper', False),
            ],
            'Cisco-IOS-XR-evpn-oper',
            'es-import',
            _yang_ns._namespaces['Cisco-IOS-XR-evpn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper'
        ),
    },
    'Evpn.Active.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_' : {
        'meta_info' : _MetaInfoClass('Evpn.Active.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_',
            False, 
            [
            _MetaInfoClassMember('es-import', REFERENCE_CLASS, 'EsImport' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'Evpn.Active.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_.EsImport', 
                [], [], 
                '''                es import
                ''',
                'es_import',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('four-byte-as', REFERENCE_CLASS, 'FourByteAs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'Evpn.Active.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_.FourByteAs', 
                [], [], 
                '''                four byte as
                ''',
                'four_byte_as',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('rt', REFERENCE_ENUM_CLASS, 'L2VpnAdRtEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'L2VpnAdRtEnum', 
                [], [], 
                '''                RT
                ''',
                'rt',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('two-byte-as', REFERENCE_CLASS, 'TwoByteAs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'Evpn.Active.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_.TwoByteAs', 
                [], [], 
                '''                two byte as
                ''',
                'two_byte_as',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('v4-addr', REFERENCE_CLASS, 'V4Addr' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'Evpn.Active.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_.V4Addr', 
                [], [], 
                '''                v4 addr
                ''',
                'v4_addr',
                'Cisco-IOS-XR-evpn-oper', False),
            ],
            'Cisco-IOS-XR-evpn-oper',
            'route-target',
            _yang_ns._namespaces['Cisco-IOS-XR-evpn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper'
        ),
    },
    'Evpn.Active.EviDetail.EviChildren.RouteTargets.RouteTarget' : {
        'meta_info' : _MetaInfoClass('Evpn.Active.EviDetail.EviChildren.RouteTargets.RouteTarget',
            False, 
            [
            _MetaInfoClassMember('addr-index', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                RT IP Index
                ''',
                'addr_index',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                RT IPv4 Address
                ''',
                'address',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('as', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                Two or Four byte AS Number
                ''',
                'as_',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('as-index', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                RT AS Index
                ''',
                'as_index',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('bd-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Bridge Domain Name
                ''',
                'bd_name',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('evi', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                EVPN id
                ''',
                'evi',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('evi-xr', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                VPN ID
                ''',
                'evi_xr',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('format', REFERENCE_ENUM_CLASS, 'BgpRouteTargetFormatEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'BgpRouteTargetFormatEnum', 
                [], [], 
                '''                Format of the route target
                ''',
                'format',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('role', REFERENCE_ENUM_CLASS, 'BgpRouteTargetRoleEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'BgpRouteTargetRoleEnum', 
                [], [], 
                '''                Role of the route target
                ''',
                'role',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('route-target', REFERENCE_CLASS, 'RouteTarget_' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'Evpn.Active.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_', 
                [], [], 
                '''                Route Target
                ''',
                'route_target',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('route-target-role', REFERENCE_ENUM_CLASS, 'L2VpnAdRtRoleEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'L2VpnAdRtRoleEnum', 
                [], [], 
                '''                RT Role
                ''',
                'route_target_role',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('route-target-stitching', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                RT Stitching
                ''',
                'route_target_stitching',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('type', REFERENCE_ENUM_CLASS, 'BgpRouteTargetEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'BgpRouteTargetEnum', 
                [], [], 
                '''                Type of the route target
                ''',
                'type',
                'Cisco-IOS-XR-evpn-oper', False),
            ],
            'Cisco-IOS-XR-evpn-oper',
            'route-target',
            _yang_ns._namespaces['Cisco-IOS-XR-evpn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper'
        ),
    },
    'Evpn.Active.EviDetail.EviChildren.RouteTargets' : {
        'meta_info' : _MetaInfoClass('Evpn.Active.EviDetail.EviChildren.RouteTargets',
            False, 
            [
            _MetaInfoClassMember('route-target', REFERENCE_LIST, 'RouteTarget' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'Evpn.Active.EviDetail.EviChildren.RouteTargets.RouteTarget', 
                [], [], 
                '''                L2VPN EVPN EVI RT Table
                ''',
                'route_target',
                'Cisco-IOS-XR-evpn-oper', False),
            ],
            'Cisco-IOS-XR-evpn-oper',
            'route-targets',
            _yang_ns._namespaces['Cisco-IOS-XR-evpn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper'
        ),
    },
    'Evpn.Active.EviDetail.EviChildren.Macs.Mac.PathBuffer' : {
        'meta_info' : _MetaInfoClass('Evpn.Active.EviDetail.EviChildren.Macs.Mac.PathBuffer',
            False, 
            [
            _MetaInfoClassMember('next-hop', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                Next-hop IP address (v6 format)
                ''',
                'next_hop',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('output-label', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Output Label
                ''',
                'output_label',
                'Cisco-IOS-XR-evpn-oper', False),
            ],
            'Cisco-IOS-XR-evpn-oper',
            'path-buffer',
            _yang_ns._namespaces['Cisco-IOS-XR-evpn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper'
        ),
    },
    'Evpn.Active.EviDetail.EviChildren.Macs.Mac' : {
        'meta_info' : _MetaInfoClass('Evpn.Active.EviDetail.EviChildren.Macs.Mac',
            False, 
            [
            _MetaInfoClassMember('esi-port-key', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                ESI port key
                ''',
                'esi_port_key',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('ethernet-tag', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Ethernet Tag ID
                ''',
                'ethernet_tag',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('ethernet-tag-xr', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Ethernet Tag
                ''',
                'ethernet_tag_xr',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('evi', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                EVPN id
                ''',
                'evi',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('internal-label', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                MPLS Internal Label
                ''',
                'internal_label',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('ip-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                IP Address
                ''',
                'ip_address',
                'Cisco-IOS-XR-evpn-oper', False, [
                    _MetaInfoClassMember('ip-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP Address
                        ''',
                        'ip_address',
                        'Cisco-IOS-XR-evpn-oper', False),
                    _MetaInfoClassMember('ip-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP Address
                        ''',
                        'ip_address',
                        'Cisco-IOS-XR-evpn-oper', False),
                ]),
            _MetaInfoClassMember('ip-address-xr', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IP address (v6 format)
                ''',
                'ip_address_xr',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('is-local-mac', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Indication of MAC being locally generated
                ''',
                'is_local_mac',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('is-remote-mac', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Indication of MAC being remotely generated
                ''',
                'is_remote_mac',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('is-static', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Indication if MAC is statically configured
                ''',
                'is_static',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('learned-bridge-port-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Port the MAC was learned on
                ''',
                'learned_bridge_port_name',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('local-encap-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Encap type of local MAC
                ''',
                'local_encap_type',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('local-ethernet-segment-identifier', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Local Ethernet Segment id
                ''',
                'local_ethernet_segment_identifier',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('local-label', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Associated local label
                ''',
                'local_label',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('local-seq-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                local seq id
                ''',
                'local_seq_id',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('mac-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                MAC address
                ''',
                'mac_address',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('mac-address-xr', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                MAC address
                ''',
                'mac_address_xr',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('mac-flush-received', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Number of flushes received 
                ''',
                'mac_flush_received',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('mac-flush-requested', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Number of flushes requested 
                ''',
                'mac_flush_requested',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('num-paths', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                 Number of items in path list buffer
                ''',
                'num_paths',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('path-buffer', REFERENCE_LIST, 'PathBuffer' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'Evpn.Active.EviDetail.EviChildren.Macs.Mac.PathBuffer', 
                [], [], 
                '''                Path List Buffer
                ''',
                'path_buffer',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('remote-encap-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Encap type of remote MAC
                ''',
                'remote_encap_type',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('remote-ethernet-segment-identifier', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Remote Ethernet Segment id
                ''',
                'remote_ethernet_segment_identifier',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('remote-seq-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                remote seq id
                ''',
                'remote_seq_id',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('resolved', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Internal Label has resolved per-ES EAD and
                per-EVI EAD or MAC routes
                ''',
                'resolved',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('soo-nexthop', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                SOO nexthop (v6 format)
                ''',
                'soo_nexthop',
                'Cisco-IOS-XR-evpn-oper', False),
            ],
            'Cisco-IOS-XR-evpn-oper',
            'mac',
            _yang_ns._namespaces['Cisco-IOS-XR-evpn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper'
        ),
    },
    'Evpn.Active.EviDetail.EviChildren.Macs' : {
        'meta_info' : _MetaInfoClass('Evpn.Active.EviDetail.EviChildren.Macs',
            False, 
            [
            _MetaInfoClassMember('mac', REFERENCE_LIST, 'Mac' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'Evpn.Active.EviDetail.EviChildren.Macs.Mac', 
                [], [], 
                '''                L2VPN EVPN MAC table
                ''',
                'mac',
                'Cisco-IOS-XR-evpn-oper', False),
            ],
            'Cisco-IOS-XR-evpn-oper',
            'macs',
            _yang_ns._namespaces['Cisco-IOS-XR-evpn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper'
        ),
    },
    'Evpn.Active.EviDetail.EviChildren' : {
        'meta_info' : _MetaInfoClass('Evpn.Active.EviDetail.EviChildren',
            False, 
            [
            _MetaInfoClassMember('ethernet-auto-discoveries', REFERENCE_CLASS, 'EthernetAutoDiscoveries' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'Evpn.Active.EviDetail.EviChildren.EthernetAutoDiscoveries', 
                [], [], 
                '''                EVPN Ethernet Auto-Discovery table
                ''',
                'ethernet_auto_discoveries',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('inclusive-multicasts', REFERENCE_CLASS, 'InclusiveMulticasts' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'Evpn.Active.EviDetail.EviChildren.InclusiveMulticasts', 
                [], [], 
                '''                L2VPN EVPN IMCAST table
                ''',
                'inclusive_multicasts',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('macs', REFERENCE_CLASS, 'Macs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'Evpn.Active.EviDetail.EviChildren.Macs', 
                [], [], 
                '''                L2VPN EVPN EVI MAC table
                ''',
                'macs',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('neighbors', REFERENCE_CLASS, 'Neighbors' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'Evpn.Active.EviDetail.EviChildren.Neighbors', 
                [], [], 
                '''                EVPN Neighbor table
                ''',
                'neighbors',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('route-targets', REFERENCE_CLASS, 'RouteTargets' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'Evpn.Active.EviDetail.EviChildren.RouteTargets', 
                [], [], 
                '''                L2VPN EVPN EVI RT Child Table
                ''',
                'route_targets',
                'Cisco-IOS-XR-evpn-oper', False),
            ],
            'Cisco-IOS-XR-evpn-oper',
            'evi-children',
            _yang_ns._namespaces['Cisco-IOS-XR-evpn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper'
        ),
    },
    'Evpn.Active.EviDetail' : {
        'meta_info' : _MetaInfoClass('Evpn.Active.EviDetail',
            False, 
            [
            _MetaInfoClassMember('elements', REFERENCE_CLASS, 'Elements' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'Evpn.Active.EviDetail.Elements', 
                [], [], 
                '''                EVI BGP RT Detail Info Elements
                ''',
                'elements',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('evi-children', REFERENCE_CLASS, 'EviChildren' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'Evpn.Active.EviDetail.EviChildren', 
                [], [], 
                '''                Container for all EVI detail info
                ''',
                'evi_children',
                'Cisco-IOS-XR-evpn-oper', False),
            ],
            'Cisco-IOS-XR-evpn-oper',
            'evi-detail',
            _yang_ns._namespaces['Cisco-IOS-XR-evpn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper'
        ),
    },
    'Evpn.Active.EthernetSegments.EthernetSegment.NextHop' : {
        'meta_info' : _MetaInfoClass('Evpn.Active.EthernetSegments.EthernetSegment.NextHop',
            False, 
            [
            _MetaInfoClassMember('next-hop', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                Next-hop IP address (v6 format)
                ''',
                'next_hop',
                'Cisco-IOS-XR-evpn-oper', False),
            ],
            'Cisco-IOS-XR-evpn-oper',
            'next-hop',
            _yang_ns._namespaces['Cisco-IOS-XR-evpn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper'
        ),
    },
    'Evpn.Active.EthernetSegments.EthernetSegment.RemoteSplitHorizonGroupLabel' : {
        'meta_info' : _MetaInfoClass('Evpn.Active.EthernetSegments.EthernetSegment.RemoteSplitHorizonGroupLabel',
            False, 
            [
            _MetaInfoClassMember('label', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Split horizon label associated with next-hop
                address
                ''',
                'label',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('next-hop', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                Next-hop IP address (v6 format)
                ''',
                'next_hop',
                'Cisco-IOS-XR-evpn-oper', False),
            ],
            'Cisco-IOS-XR-evpn-oper',
            'remote-split-horizon-group-label',
            _yang_ns._namespaces['Cisco-IOS-XR-evpn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper'
        ),
    },
    'Evpn.Active.EthernetSegments.EthernetSegment' : {
        'meta_info' : _MetaInfoClass('Evpn.Active.EthernetSegments.EthernetSegment',
            False, 
            [
            _MetaInfoClassMember('elected-d-fs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Count of service carving results - elected
                ''',
                'elected_d_fs',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('es-bgp-gates', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                ES BGP Gates
                ''',
                'es_bgp_gates',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('es-l2fib-gates', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                ES L2FIB Gates
                ''',
                'es_l2fib_gates',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('esi1', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{1,8}'], 
                '''                ES id (part 1/5)
                ''',
                'esi1',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('esi2', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{1,8}'], 
                '''                ES id (part 2/5)
                ''',
                'esi2',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('esi3', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{1,8}'], 
                '''                ES id (part 3/5)
                ''',
                'esi3',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('esi4', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{1,8}'], 
                '''                ES id (part 4/5)
                ''',
                'esi4',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('esi5', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{1,8}'], 
                '''                ES id (part 5/5)
                ''',
                'esi5',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('esi-type', REFERENCE_ENUM_CLASS, 'L2VpnEvpnEsiEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'L2VpnEvpnEsiEnum', 
                [], [], 
                '''                ESI Type
                ''',
                'esi_type',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('ethernet-segment-identifier', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Ethernet Segment id
                ''',
                'ethernet_segment_identifier',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('ethernet-segment-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Ethernet Segment Name
                ''',
                'ethernet_segment_name',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('ethernet-segment-state', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                State of the ethernet segment
                ''',
                'ethernet_segment_state',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('force-single-home', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Ethernet-Segment forced to single home
                ''',
                'force_single_home',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('forwarder-ports', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Count of Forwarders (AC, AC PW, VFI PW)
                ''',
                'forwarder_ports',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('if-handle', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Main port ifhandle
                ''',
                'if_handle',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface
                ''',
                'interface_name',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('load-balance-mode-config', REFERENCE_ENUM_CLASS, 'L2VpnEvpnLbModeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'L2VpnEvpnLbModeEnum', 
                [], [], 
                '''                Configured load balancing mode
                ''',
                'load_balance_mode_config',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('load-balance-mode-is-default', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Load balancing mode is default
                ''',
                'load_balance_mode_is_default',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('load-balance-mode-oper', REFERENCE_ENUM_CLASS, 'L2VpnEvpnLbModeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'L2VpnEvpnLbModeEnum', 
                [], [], 
                '''                Operational load balancing mode
                ''',
                'load_balance_mode_oper',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('local-split-horizon-group-label', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Local split horizon group label
                ''',
                'local_split_horizon_group_label',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('mac-flushing-mode-config', REFERENCE_ENUM_CLASS, 'L2VpnEvpnMfModeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'L2VpnEvpnMfModeEnum', 
                [], [], 
                '''                Configured MAC Flushing mode
                ''',
                'mac_flushing_mode_config',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('main-port-mac', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                Main Port MAC Address
                ''',
                'main_port_mac',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('main-port-role', REFERENCE_ENUM_CLASS, 'L2VpnRgStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'L2VpnRgStateEnum', 
                [], [], 
                '''                Main port redundancy group role
                ''',
                'main_port_role',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('mp-protected', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                MP is protected and not under EVPN control
                ''',
                'mp_protected',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('next-hop', REFERENCE_LIST, 'NextHop' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'Evpn.Active.EthernetSegments.EthernetSegment.NextHop', 
                [], [], 
                '''                List of nexthop IPv6 addresses
                ''',
                'next_hop',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('not-config-d-fs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Count of service carving results - missing
                config detected
                ''',
                'not_config_d_fs',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('not-elected-d-fs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Count of service carving results - not elected
                ''',
                'not_elected_d_fs',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('num-up-p-ws', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of PWs in Up state
                ''',
                'num_up_p_ws',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('peering-timer', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Configured timer for triggering DF election
                (seconds)
                ''',
                'peering_timer',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('peering-timer-left', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Milliseconds left on DF election timer
                ''',
                'peering_timer_left',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('primary-service', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                List of Primary services ESI/I-SIDs
                ''',
                'primary_service',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('primary-services-input', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Input string of Primary services ESI/I-SIDs
                ''',
                'primary_services_input',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('recovery-timer', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Configured timer for (STP) recovery (seconds)
                ''',
                'recovery_timer',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('recovery-timer-left', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Milliseconds left on (STP) recovery timer
                ''',
                'recovery_timer_left',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('remote-split-horizon-group-label', REFERENCE_LIST, 'RemoteSplitHorizonGroupLabel' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'Evpn.Active.EthernetSegments.EthernetSegment.RemoteSplitHorizonGroupLabel', 
                [], [], 
                '''                Remote split horizon group labels
                ''',
                'remote_split_horizon_group_label',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('route-target', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                ES-Import Route Target
                ''',
                'route_target',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('rt-origin', REFERENCE_ENUM_CLASS, 'L2VpnEvpnRtOriginEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'L2VpnEvpnRtOriginEnum', 
                [], [], 
                '''                Origin of operational ES-Import RT
                ''',
                'rt_origin',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('secondary-service', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                List of Secondary services ESI/I-SIDs
                ''',
                'secondary_service',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('secondary-services-input', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Input string of Secondary services ESI/I-SIDs
                ''',
                'secondary_services_input',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('service-carving-mode', REFERENCE_ENUM_CLASS, 'L2VpnEvpnScModeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'L2VpnEvpnScModeEnum', 
                [], [], 
                '''                Service carving mode
                ''',
                'service_carving_mode',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('service-carving-result', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Service carving results
                ''',
                'service_carving_result',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('service-carving-type', REFERENCE_ENUM_CLASS, 'L2VpnEvpnScEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'L2VpnEvpnScEnum', 
                [], [], 
                '''                Service Carving Type
                ''',
                'service_carving_type',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('source-mac-oper', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                Operational Source MAC address
                ''',
                'source_mac_oper',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('source-mac-origin', REFERENCE_ENUM_CLASS, 'L2VpnEvpnSmacSrcEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'L2VpnEvpnSmacSrcEnum', 
                [], [], 
                '''                Origin of operational source MAC address
                ''',
                'source_mac_origin',
                'Cisco-IOS-XR-evpn-oper', False),
            ],
            'Cisco-IOS-XR-evpn-oper',
            'ethernet-segment',
            _yang_ns._namespaces['Cisco-IOS-XR-evpn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper'
        ),
    },
    'Evpn.Active.EthernetSegments' : {
        'meta_info' : _MetaInfoClass('Evpn.Active.EthernetSegments',
            False, 
            [
            _MetaInfoClassMember('ethernet-segment', REFERENCE_LIST, 'EthernetSegment' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'Evpn.Active.EthernetSegments.EthernetSegment', 
                [], [], 
                '''                EVPN Ethernet-Segment Entry
                ''',
                'ethernet_segment',
                'Cisco-IOS-XR-evpn-oper', False),
            ],
            'Cisco-IOS-XR-evpn-oper',
            'ethernet-segments',
            _yang_ns._namespaces['Cisco-IOS-XR-evpn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper'
        ),
    },
    'Evpn.Active.AcIds.AcId' : {
        'meta_info' : _MetaInfoClass('Evpn.Active.AcIds.AcId',
            False, 
            [
            _MetaInfoClassMember('ac-id', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                AC ID
                ''',
                'ac_id',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('evi', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                EVPN id
                ''',
                'evi',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('evi-xr', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                E-VPN id
                ''',
                'evi_xr',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('neighbor', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                Neighbor IP
                ''',
                'neighbor',
                'Cisco-IOS-XR-evpn-oper', False),
            ],
            'Cisco-IOS-XR-evpn-oper',
            'ac-id',
            _yang_ns._namespaces['Cisco-IOS-XR-evpn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper'
        ),
    },
    'Evpn.Active.AcIds' : {
        'meta_info' : _MetaInfoClass('Evpn.Active.AcIds',
            False, 
            [
            _MetaInfoClassMember('ac-id', REFERENCE_LIST, 'AcId' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'Evpn.Active.AcIds.AcId', 
                [], [], 
                '''                EVPN AC ID table
                ''',
                'ac_id',
                'Cisco-IOS-XR-evpn-oper', False),
            ],
            'Cisco-IOS-XR-evpn-oper',
            'ac-ids',
            _yang_ns._namespaces['Cisco-IOS-XR-evpn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper'
        ),
    },
    'Evpn.Active' : {
        'meta_info' : _MetaInfoClass('Evpn.Active',
            False, 
            [
            _MetaInfoClassMember('ac-ids', REFERENCE_CLASS, 'AcIds' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'Evpn.Active.AcIds', 
                [], [], 
                '''                EVPN AC ID table
                ''',
                'ac_ids',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('ethernet-segments', REFERENCE_CLASS, 'EthernetSegments' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'Evpn.Active.EthernetSegments', 
                [], [], 
                '''                EVPN Ethernet-Segment Table
                ''',
                'ethernet_segments',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('evi-detail', REFERENCE_CLASS, 'EviDetail' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'Evpn.Active.EviDetail', 
                [], [], 
                '''                L2VPN EVI Detail Table
                ''',
                'evi_detail',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('evis', REFERENCE_CLASS, 'Evis' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'Evpn.Active.Evis', 
                [], [], 
                '''                L2VPN EVPN EVI Table
                ''',
                'evis',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('summary', REFERENCE_CLASS, 'Summary' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'Evpn.Active.Summary', 
                [], [], 
                '''                L2VPN EVPN Summary
                ''',
                'summary',
                'Cisco-IOS-XR-evpn-oper', False),
            ],
            'Cisco-IOS-XR-evpn-oper',
            'active',
            _yang_ns._namespaces['Cisco-IOS-XR-evpn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper'
        ),
    },
    'Evpn.Standby.Evis.Evi' : {
        'meta_info' : _MetaInfoClass('Evpn.Standby.Evis.Evi',
            False, 
            [
            _MetaInfoClassMember('evi', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                EVPN id
                ''',
                'evi',
                'Cisco-IOS-XR-evpn-oper', True),
            _MetaInfoClassMember('bd-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Bridge domain name
                ''',
                'bd_name',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('evi-xr', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                E-VPN id
                ''',
                'evi_xr',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('type', REFERENCE_ENUM_CLASS, 'EvpnEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'EvpnEnum', 
                [], [], 
                '''                Service Type
                ''',
                'type',
                'Cisco-IOS-XR-evpn-oper', False),
            ],
            'Cisco-IOS-XR-evpn-oper',
            'evi',
            _yang_ns._namespaces['Cisco-IOS-XR-evpn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper'
        ),
    },
    'Evpn.Standby.Evis' : {
        'meta_info' : _MetaInfoClass('Evpn.Standby.Evis',
            False, 
            [
            _MetaInfoClassMember('evi', REFERENCE_LIST, 'Evi' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'Evpn.Standby.Evis.Evi', 
                [], [], 
                '''                L2VPN EVPN EVI Entry
                ''',
                'evi',
                'Cisco-IOS-XR-evpn-oper', False),
            ],
            'Cisco-IOS-XR-evpn-oper',
            'evis',
            _yang_ns._namespaces['Cisco-IOS-XR-evpn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper'
        ),
    },
    'Evpn.Standby.Summary' : {
        'meta_info' : _MetaInfoClass('Evpn.Standby.Summary',
            False, 
            [
            _MetaInfoClassMember('as', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                BGP AS number
                ''',
                'as_',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('es-entries', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of ES Entries in DB
                ''',
                'es_entries',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('es-global-mac-routes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of ES:Global MAC Routes
                ''',
                'es_global_mac_routes',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('ev-is', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of EVI DB Entries
                ''',
                'ev_is',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('global-source-mac', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                Global Source MAC Address
                ''',
                'global_source_mac',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('l2rib-throttle', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Send to L2RIB Throttled
                ''',
                'l2rib_throttle',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('labels', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Internal Labels
                ''',
                'labels',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('local-ead-routes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Local EAD Entries in DB
                ''',
                'local_ead_routes',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('local-imcast-routes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Local IMCAST Routes
                ''',
                'local_imcast_routes',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('local-ipv4-mac-routes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Local IPv4 MAC-IP Routes
                ''',
                'local_ipv4_mac_routes',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('local-ipv6-mac-routes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Local IPv6 MAC-IP Routes
                ''',
                'local_ipv6_mac_routes',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('local-mac-routes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Local MAC Routes
                ''',
                'local_mac_routes',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('logging-df-election-enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Logging EVPN Designated Forwarder changes
                enabled
                ''',
                'logging_df_election_enabled',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('neighbor-entries', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of neighbor Entries in DB
                ''',
                'neighbor_entries',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('peering-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                EVPN ES Peering Time (seconds)
                ''',
                'peering_time',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('recovery-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                EVPN ES Recovery Time (seconds)
                ''',
                'recovery_time',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('remote-ead-routes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Remote EAD Entries in DB
                ''',
                'remote_ead_routes',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('remote-imcast-routes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Remote IMCAST Routes
                ''',
                'remote_imcast_routes',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('remote-ipv4-mac-routes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Remote IPv4 MAC-IP Routes
                ''',
                'remote_ipv4_mac_routes',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('remote-ipv6-mac-routes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Remote IPv6 MAC-IP Routes
                ''',
                'remote_ipv6_mac_routes',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('remote-mac-routes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Remote MAC Routes
                ''',
                'remote_mac_routes',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('remote-soo-mac-routes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Remote Soo MAC Routes
                ''',
                'remote_soo_mac_routes',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('router-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                EVPN Router ID
                ''',
                'router_id',
                'Cisco-IOS-XR-evpn-oper', False),
            ],
            'Cisco-IOS-XR-evpn-oper',
            'summary',
            _yang_ns._namespaces['Cisco-IOS-XR-evpn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper'
        ),
    },
    'Evpn.Standby.EviDetail.Elements.Element.FlowLabel' : {
        'meta_info' : _MetaInfoClass('Evpn.Standby.EviDetail.Elements.Element.FlowLabel',
            False, 
            [
            _MetaInfoClassMember('global-flow-label', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Globally configured flow label
                ''',
                'global_flow_label',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('static-flow-label', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Static flow label
                ''',
                'static_flow_label',
                'Cisco-IOS-XR-evpn-oper', False),
            ],
            'Cisco-IOS-XR-evpn-oper',
            'flow-label',
            _yang_ns._namespaces['Cisco-IOS-XR-evpn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper'
        ),
    },
    'Evpn.Standby.EviDetail.Elements.Element.RdAuto.Auto' : {
        'meta_info' : _MetaInfoClass('Evpn.Standby.EviDetail.Elements.Element.RdAuto.Auto',
            False, 
            [
            _MetaInfoClassMember('auto-index', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Auto-generated Index
                ''',
                'auto_index',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('router-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                BGP Router ID
                ''',
                'router_id',
                'Cisco-IOS-XR-evpn-oper', False),
            ],
            'Cisco-IOS-XR-evpn-oper',
            'auto',
            _yang_ns._namespaces['Cisco-IOS-XR-evpn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper'
        ),
    },
    'Evpn.Standby.EviDetail.Elements.Element.RdAuto.TwoByteAs' : {
        'meta_info' : _MetaInfoClass('Evpn.Standby.EviDetail.Elements.Element.RdAuto.TwoByteAs',
            False, 
            [
            _MetaInfoClassMember('four-byte-index', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                4 Byte Index
                ''',
                'four_byte_index',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('two-byte-as', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                2 Byte AS Number
                ''',
                'two_byte_as',
                'Cisco-IOS-XR-evpn-oper', False),
            ],
            'Cisco-IOS-XR-evpn-oper',
            'two-byte-as',
            _yang_ns._namespaces['Cisco-IOS-XR-evpn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper'
        ),
    },
    'Evpn.Standby.EviDetail.Elements.Element.RdAuto.FourByteAs' : {
        'meta_info' : _MetaInfoClass('Evpn.Standby.EviDetail.Elements.Element.RdAuto.FourByteAs',
            False, 
            [
            _MetaInfoClassMember('four-byte-as', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                4 Byte AS Number
                ''',
                'four_byte_as',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('two-byte-index', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                2 Byte Index
                ''',
                'two_byte_index',
                'Cisco-IOS-XR-evpn-oper', False),
            ],
            'Cisco-IOS-XR-evpn-oper',
            'four-byte-as',
            _yang_ns._namespaces['Cisco-IOS-XR-evpn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper'
        ),
    },
    'Evpn.Standby.EviDetail.Elements.Element.RdAuto.V4Addr' : {
        'meta_info' : _MetaInfoClass('Evpn.Standby.EviDetail.Elements.Element.RdAuto.V4Addr',
            False, 
            [
            _MetaInfoClassMember('ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 Address
                ''',
                'ipv4_address',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('two-byte-index', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                2 Byte Index
                ''',
                'two_byte_index',
                'Cisco-IOS-XR-evpn-oper', False),
            ],
            'Cisco-IOS-XR-evpn-oper',
            'v4-addr',
            _yang_ns._namespaces['Cisco-IOS-XR-evpn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper'
        ),
    },
    'Evpn.Standby.EviDetail.Elements.Element.RdAuto' : {
        'meta_info' : _MetaInfoClass('Evpn.Standby.EviDetail.Elements.Element.RdAuto',
            False, 
            [
            _MetaInfoClassMember('auto', REFERENCE_CLASS, 'Auto' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'Evpn.Standby.EviDetail.Elements.Element.RdAuto.Auto', 
                [], [], 
                '''                auto
                ''',
                'auto',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('four-byte-as', REFERENCE_CLASS, 'FourByteAs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'Evpn.Standby.EviDetail.Elements.Element.RdAuto.FourByteAs', 
                [], [], 
                '''                four byte as
                ''',
                'four_byte_as',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('rd', REFERENCE_ENUM_CLASS, 'L2VpnAdRdEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'L2VpnAdRdEnum', 
                [], [], 
                '''                RD
                ''',
                'rd',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('two-byte-as', REFERENCE_CLASS, 'TwoByteAs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'Evpn.Standby.EviDetail.Elements.Element.RdAuto.TwoByteAs', 
                [], [], 
                '''                two byte as
                ''',
                'two_byte_as',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('v4-addr', REFERENCE_CLASS, 'V4Addr' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'Evpn.Standby.EviDetail.Elements.Element.RdAuto.V4Addr', 
                [], [], 
                '''                v4 addr
                ''',
                'v4_addr',
                'Cisco-IOS-XR-evpn-oper', False),
            ],
            'Cisco-IOS-XR-evpn-oper',
            'rd-auto',
            _yang_ns._namespaces['Cisco-IOS-XR-evpn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper'
        ),
    },
    'Evpn.Standby.EviDetail.Elements.Element.RdConfigured.Auto' : {
        'meta_info' : _MetaInfoClass('Evpn.Standby.EviDetail.Elements.Element.RdConfigured.Auto',
            False, 
            [
            _MetaInfoClassMember('auto-index', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Auto-generated Index
                ''',
                'auto_index',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('router-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                BGP Router ID
                ''',
                'router_id',
                'Cisco-IOS-XR-evpn-oper', False),
            ],
            'Cisco-IOS-XR-evpn-oper',
            'auto',
            _yang_ns._namespaces['Cisco-IOS-XR-evpn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper'
        ),
    },
    'Evpn.Standby.EviDetail.Elements.Element.RdConfigured.TwoByteAs' : {
        'meta_info' : _MetaInfoClass('Evpn.Standby.EviDetail.Elements.Element.RdConfigured.TwoByteAs',
            False, 
            [
            _MetaInfoClassMember('four-byte-index', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                4 Byte Index
                ''',
                'four_byte_index',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('two-byte-as', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                2 Byte AS Number
                ''',
                'two_byte_as',
                'Cisco-IOS-XR-evpn-oper', False),
            ],
            'Cisco-IOS-XR-evpn-oper',
            'two-byte-as',
            _yang_ns._namespaces['Cisco-IOS-XR-evpn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper'
        ),
    },
    'Evpn.Standby.EviDetail.Elements.Element.RdConfigured.FourByteAs' : {
        'meta_info' : _MetaInfoClass('Evpn.Standby.EviDetail.Elements.Element.RdConfigured.FourByteAs',
            False, 
            [
            _MetaInfoClassMember('four-byte-as', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                4 Byte AS Number
                ''',
                'four_byte_as',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('two-byte-index', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                2 Byte Index
                ''',
                'two_byte_index',
                'Cisco-IOS-XR-evpn-oper', False),
            ],
            'Cisco-IOS-XR-evpn-oper',
            'four-byte-as',
            _yang_ns._namespaces['Cisco-IOS-XR-evpn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper'
        ),
    },
    'Evpn.Standby.EviDetail.Elements.Element.RdConfigured.V4Addr' : {
        'meta_info' : _MetaInfoClass('Evpn.Standby.EviDetail.Elements.Element.RdConfigured.V4Addr',
            False, 
            [
            _MetaInfoClassMember('ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 Address
                ''',
                'ipv4_address',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('two-byte-index', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                2 Byte Index
                ''',
                'two_byte_index',
                'Cisco-IOS-XR-evpn-oper', False),
            ],
            'Cisco-IOS-XR-evpn-oper',
            'v4-addr',
            _yang_ns._namespaces['Cisco-IOS-XR-evpn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper'
        ),
    },
    'Evpn.Standby.EviDetail.Elements.Element.RdConfigured' : {
        'meta_info' : _MetaInfoClass('Evpn.Standby.EviDetail.Elements.Element.RdConfigured',
            False, 
            [
            _MetaInfoClassMember('auto', REFERENCE_CLASS, 'Auto' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'Evpn.Standby.EviDetail.Elements.Element.RdConfigured.Auto', 
                [], [], 
                '''                auto
                ''',
                'auto',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('four-byte-as', REFERENCE_CLASS, 'FourByteAs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'Evpn.Standby.EviDetail.Elements.Element.RdConfigured.FourByteAs', 
                [], [], 
                '''                four byte as
                ''',
                'four_byte_as',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('rd', REFERENCE_ENUM_CLASS, 'L2VpnAdRdEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'L2VpnAdRdEnum', 
                [], [], 
                '''                RD
                ''',
                'rd',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('two-byte-as', REFERENCE_CLASS, 'TwoByteAs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'Evpn.Standby.EviDetail.Elements.Element.RdConfigured.TwoByteAs', 
                [], [], 
                '''                two byte as
                ''',
                'two_byte_as',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('v4-addr', REFERENCE_CLASS, 'V4Addr' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'Evpn.Standby.EviDetail.Elements.Element.RdConfigured.V4Addr', 
                [], [], 
                '''                v4 addr
                ''',
                'v4_addr',
                'Cisco-IOS-XR-evpn-oper', False),
            ],
            'Cisco-IOS-XR-evpn-oper',
            'rd-configured',
            _yang_ns._namespaces['Cisco-IOS-XR-evpn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper'
        ),
    },
    'Evpn.Standby.EviDetail.Elements.Element.RtAuto.TwoByteAs' : {
        'meta_info' : _MetaInfoClass('Evpn.Standby.EviDetail.Elements.Element.RtAuto.TwoByteAs',
            False, 
            [
            _MetaInfoClassMember('four-byte-index', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                4 Byte Index
                ''',
                'four_byte_index',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('two-byte-as', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                2 Byte AS Number
                ''',
                'two_byte_as',
                'Cisco-IOS-XR-evpn-oper', False),
            ],
            'Cisco-IOS-XR-evpn-oper',
            'two-byte-as',
            _yang_ns._namespaces['Cisco-IOS-XR-evpn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper'
        ),
    },
    'Evpn.Standby.EviDetail.Elements.Element.RtAuto.FourByteAs' : {
        'meta_info' : _MetaInfoClass('Evpn.Standby.EviDetail.Elements.Element.RtAuto.FourByteAs',
            False, 
            [
            _MetaInfoClassMember('four-byte-as', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                4 Byte AS Number
                ''',
                'four_byte_as',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('two-byte-index', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                2 Byte Index
                ''',
                'two_byte_index',
                'Cisco-IOS-XR-evpn-oper', False),
            ],
            'Cisco-IOS-XR-evpn-oper',
            'four-byte-as',
            _yang_ns._namespaces['Cisco-IOS-XR-evpn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper'
        ),
    },
    'Evpn.Standby.EviDetail.Elements.Element.RtAuto.V4Addr' : {
        'meta_info' : _MetaInfoClass('Evpn.Standby.EviDetail.Elements.Element.RtAuto.V4Addr',
            False, 
            [
            _MetaInfoClassMember('ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 Address
                ''',
                'ipv4_address',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('two-byte-index', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                2 Byte Index
                ''',
                'two_byte_index',
                'Cisco-IOS-XR-evpn-oper', False),
            ],
            'Cisco-IOS-XR-evpn-oper',
            'v4-addr',
            _yang_ns._namespaces['Cisco-IOS-XR-evpn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper'
        ),
    },
    'Evpn.Standby.EviDetail.Elements.Element.RtAuto.EsImport' : {
        'meta_info' : _MetaInfoClass('Evpn.Standby.EviDetail.Elements.Element.RtAuto.EsImport',
            False, 
            [
            _MetaInfoClassMember('high-bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Top 4 bytes of ES Import
                ''',
                'high_bytes',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('low-bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Low 2 bytes of ES Import
                ''',
                'low_bytes',
                'Cisco-IOS-XR-evpn-oper', False),
            ],
            'Cisco-IOS-XR-evpn-oper',
            'es-import',
            _yang_ns._namespaces['Cisco-IOS-XR-evpn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper'
        ),
    },
    'Evpn.Standby.EviDetail.Elements.Element.RtAuto' : {
        'meta_info' : _MetaInfoClass('Evpn.Standby.EviDetail.Elements.Element.RtAuto',
            False, 
            [
            _MetaInfoClassMember('es-import', REFERENCE_CLASS, 'EsImport' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'Evpn.Standby.EviDetail.Elements.Element.RtAuto.EsImport', 
                [], [], 
                '''                es import
                ''',
                'es_import',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('four-byte-as', REFERENCE_CLASS, 'FourByteAs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'Evpn.Standby.EviDetail.Elements.Element.RtAuto.FourByteAs', 
                [], [], 
                '''                four byte as
                ''',
                'four_byte_as',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('rt', REFERENCE_ENUM_CLASS, 'L2VpnAdRtEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'L2VpnAdRtEnum', 
                [], [], 
                '''                RT
                ''',
                'rt',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('two-byte-as', REFERENCE_CLASS, 'TwoByteAs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'Evpn.Standby.EviDetail.Elements.Element.RtAuto.TwoByteAs', 
                [], [], 
                '''                two byte as
                ''',
                'two_byte_as',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('v4-addr', REFERENCE_CLASS, 'V4Addr' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'Evpn.Standby.EviDetail.Elements.Element.RtAuto.V4Addr', 
                [], [], 
                '''                v4 addr
                ''',
                'v4_addr',
                'Cisco-IOS-XR-evpn-oper', False),
            ],
            'Cisco-IOS-XR-evpn-oper',
            'rt-auto',
            _yang_ns._namespaces['Cisco-IOS-XR-evpn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper'
        ),
    },
    'Evpn.Standby.EviDetail.Elements.Element.RtAutoStitching.TwoByteAs' : {
        'meta_info' : _MetaInfoClass('Evpn.Standby.EviDetail.Elements.Element.RtAutoStitching.TwoByteAs',
            False, 
            [
            _MetaInfoClassMember('four-byte-index', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                4 Byte Index
                ''',
                'four_byte_index',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('two-byte-as', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                2 Byte AS Number
                ''',
                'two_byte_as',
                'Cisco-IOS-XR-evpn-oper', False),
            ],
            'Cisco-IOS-XR-evpn-oper',
            'two-byte-as',
            _yang_ns._namespaces['Cisco-IOS-XR-evpn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper'
        ),
    },
    'Evpn.Standby.EviDetail.Elements.Element.RtAutoStitching.FourByteAs' : {
        'meta_info' : _MetaInfoClass('Evpn.Standby.EviDetail.Elements.Element.RtAutoStitching.FourByteAs',
            False, 
            [
            _MetaInfoClassMember('four-byte-as', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                4 Byte AS Number
                ''',
                'four_byte_as',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('two-byte-index', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                2 Byte Index
                ''',
                'two_byte_index',
                'Cisco-IOS-XR-evpn-oper', False),
            ],
            'Cisco-IOS-XR-evpn-oper',
            'four-byte-as',
            _yang_ns._namespaces['Cisco-IOS-XR-evpn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper'
        ),
    },
    'Evpn.Standby.EviDetail.Elements.Element.RtAutoStitching.V4Addr' : {
        'meta_info' : _MetaInfoClass('Evpn.Standby.EviDetail.Elements.Element.RtAutoStitching.V4Addr',
            False, 
            [
            _MetaInfoClassMember('ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 Address
                ''',
                'ipv4_address',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('two-byte-index', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                2 Byte Index
                ''',
                'two_byte_index',
                'Cisco-IOS-XR-evpn-oper', False),
            ],
            'Cisco-IOS-XR-evpn-oper',
            'v4-addr',
            _yang_ns._namespaces['Cisco-IOS-XR-evpn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper'
        ),
    },
    'Evpn.Standby.EviDetail.Elements.Element.RtAutoStitching.EsImport' : {
        'meta_info' : _MetaInfoClass('Evpn.Standby.EviDetail.Elements.Element.RtAutoStitching.EsImport',
            False, 
            [
            _MetaInfoClassMember('high-bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Top 4 bytes of ES Import
                ''',
                'high_bytes',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('low-bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Low 2 bytes of ES Import
                ''',
                'low_bytes',
                'Cisco-IOS-XR-evpn-oper', False),
            ],
            'Cisco-IOS-XR-evpn-oper',
            'es-import',
            _yang_ns._namespaces['Cisco-IOS-XR-evpn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper'
        ),
    },
    'Evpn.Standby.EviDetail.Elements.Element.RtAutoStitching' : {
        'meta_info' : _MetaInfoClass('Evpn.Standby.EviDetail.Elements.Element.RtAutoStitching',
            False, 
            [
            _MetaInfoClassMember('es-import', REFERENCE_CLASS, 'EsImport' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'Evpn.Standby.EviDetail.Elements.Element.RtAutoStitching.EsImport', 
                [], [], 
                '''                es import
                ''',
                'es_import',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('four-byte-as', REFERENCE_CLASS, 'FourByteAs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'Evpn.Standby.EviDetail.Elements.Element.RtAutoStitching.FourByteAs', 
                [], [], 
                '''                four byte as
                ''',
                'four_byte_as',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('rt', REFERENCE_ENUM_CLASS, 'L2VpnAdRtEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'L2VpnAdRtEnum', 
                [], [], 
                '''                RT
                ''',
                'rt',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('two-byte-as', REFERENCE_CLASS, 'TwoByteAs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'Evpn.Standby.EviDetail.Elements.Element.RtAutoStitching.TwoByteAs', 
                [], [], 
                '''                two byte as
                ''',
                'two_byte_as',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('v4-addr', REFERENCE_CLASS, 'V4Addr' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'Evpn.Standby.EviDetail.Elements.Element.RtAutoStitching.V4Addr', 
                [], [], 
                '''                v4 addr
                ''',
                'v4_addr',
                'Cisco-IOS-XR-evpn-oper', False),
            ],
            'Cisco-IOS-XR-evpn-oper',
            'rt-auto-stitching',
            _yang_ns._namespaces['Cisco-IOS-XR-evpn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper'
        ),
    },
    'Evpn.Standby.EviDetail.Elements.Element' : {
        'meta_info' : _MetaInfoClass('Evpn.Standby.EviDetail.Elements.Element',
            False, 
            [
            _MetaInfoClassMember('evi', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                EVPN id
                ''',
                'evi',
                'Cisco-IOS-XR-evpn-oper', True),
            _MetaInfoClassMember('advertise-mac', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Advertise MAC-only routes on this EVI
                ''',
                'advertise_mac',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('aliasing-disabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Route Aliasing is disabled
                ''',
                'aliasing_disabled',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('bd-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Bridge domain name
                ''',
                'bd_name',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('cw-disable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Control-Word Disable
                ''',
                'cw_disable',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('description', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                EVI description
                ''',
                'description',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('evi-xr', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                E-VPN id
                ''',
                'evi_xr',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('flow-label', REFERENCE_CLASS, 'FlowLabel' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'Evpn.Standby.EviDetail.Elements.Element.FlowLabel', 
                [], [], 
                '''                Flow Label Information
                ''',
                'flow_label',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('forward-class', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Forward Class attribute
                ''',
                'forward_class',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('multicast-label', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Multicast Label
                ''',
                'multicast_label',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('rd-auto', REFERENCE_CLASS, 'RdAuto' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'Evpn.Standby.EviDetail.Elements.Element.RdAuto', 
                [], [], 
                '''                Automatic Route Distingtuisher
                ''',
                'rd_auto',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('rd-configured', REFERENCE_CLASS, 'RdConfigured' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'Evpn.Standby.EviDetail.Elements.Element.RdConfigured', 
                [], [], 
                '''                Configured Route Distinguisher
                ''',
                'rd_configured',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('reoriginate-disabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Route Re-origination is disabled
                ''',
                'reoriginate_disabled',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('rt-auto', REFERENCE_CLASS, 'RtAuto' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'Evpn.Standby.EviDetail.Elements.Element.RtAuto', 
                [], [], 
                '''                Automatic Route Target
                ''',
                'rt_auto',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('rt-auto-stitching', REFERENCE_CLASS, 'RtAutoStitching' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'Evpn.Standby.EviDetail.Elements.Element.RtAutoStitching', 
                [], [], 
                '''                Automatic Route Target Stitching
                ''',
                'rt_auto_stitching',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('rt-export-block-set', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is Export RT None set
                ''',
                'rt_export_block_set',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('rt-import-block-set', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is Import RT None set
                ''',
                'rt_import_block_set',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('stitching', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                RT Stitching for MPLS Fabric is enabled
                ''',
                'stitching',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('table-policy-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Table-policy Name
                ''',
                'table_policy_name',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('type', REFERENCE_ENUM_CLASS, 'EvpnEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'EvpnEnum', 
                [], [], 
                '''                Service Type
                ''',
                'type',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('unicast-label', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Unicast Label
                ''',
                'unicast_label',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('unknown-unicast-flooding-disabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Unknown-unicast flooding is disabled
                ''',
                'unknown_unicast_flooding_disabled',
                'Cisco-IOS-XR-evpn-oper', False),
            ],
            'Cisco-IOS-XR-evpn-oper',
            'element',
            _yang_ns._namespaces['Cisco-IOS-XR-evpn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper'
        ),
    },
    'Evpn.Standby.EviDetail.Elements' : {
        'meta_info' : _MetaInfoClass('Evpn.Standby.EviDetail.Elements',
            False, 
            [
            _MetaInfoClassMember('element', REFERENCE_LIST, 'Element' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'Evpn.Standby.EviDetail.Elements.Element', 
                [], [], 
                '''                EVI BGP RT Detail Info
                ''',
                'element',
                'Cisco-IOS-XR-evpn-oper', False),
            ],
            'Cisco-IOS-XR-evpn-oper',
            'elements',
            _yang_ns._namespaces['Cisco-IOS-XR-evpn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper'
        ),
    },
    'Evpn.Standby.EviDetail.EviChildren.Neighbors.Neighbor' : {
        'meta_info' : _MetaInfoClass('Evpn.Standby.EviDetail.EviChildren.Neighbors.Neighbor',
            False, 
            [
            _MetaInfoClassMember('evi', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                EVPN id
                ''',
                'evi',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('evi-xr', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                E-VPN id
                ''',
                'evi_xr',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('neighbor', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                Neighbor IP
                ''',
                'neighbor',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('neighbor-ip', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Neighbor IP
                ''',
                'neighbor_ip',
                'Cisco-IOS-XR-evpn-oper', False, [
                    _MetaInfoClassMember('neighbor-ip', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Neighbor IP
                        ''',
                        'neighbor_ip',
                        'Cisco-IOS-XR-evpn-oper', False),
                    _MetaInfoClassMember('neighbor-ip', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Neighbor IP
                        ''',
                        'neighbor_ip',
                        'Cisco-IOS-XR-evpn-oper', False),
                ]),
            ],
            'Cisco-IOS-XR-evpn-oper',
            'neighbor',
            _yang_ns._namespaces['Cisco-IOS-XR-evpn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper'
        ),
    },
    'Evpn.Standby.EviDetail.EviChildren.Neighbors' : {
        'meta_info' : _MetaInfoClass('Evpn.Standby.EviDetail.EviChildren.Neighbors',
            False, 
            [
            _MetaInfoClassMember('neighbor', REFERENCE_LIST, 'Neighbor' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'Evpn.Standby.EviDetail.EviChildren.Neighbors.Neighbor', 
                [], [], 
                '''                EVPN Neighbor table
                ''',
                'neighbor',
                'Cisco-IOS-XR-evpn-oper', False),
            ],
            'Cisco-IOS-XR-evpn-oper',
            'neighbors',
            _yang_ns._namespaces['Cisco-IOS-XR-evpn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper'
        ),
    },
    'Evpn.Standby.EviDetail.EviChildren.EthernetAutoDiscoveries.EthernetAutoDiscovery.PathBuffer' : {
        'meta_info' : _MetaInfoClass('Evpn.Standby.EviDetail.EviChildren.EthernetAutoDiscoveries.EthernetAutoDiscovery.PathBuffer',
            False, 
            [
            _MetaInfoClassMember('next-hop', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                Next-hop IP address (v6 format)
                ''',
                'next_hop',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('output-label', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Output Label
                ''',
                'output_label',
                'Cisco-IOS-XR-evpn-oper', False),
            ],
            'Cisco-IOS-XR-evpn-oper',
            'path-buffer',
            _yang_ns._namespaces['Cisco-IOS-XR-evpn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper'
        ),
    },
    'Evpn.Standby.EviDetail.EviChildren.EthernetAutoDiscoveries.EthernetAutoDiscovery' : {
        'meta_info' : _MetaInfoClass('Evpn.Standby.EviDetail.EviChildren.EthernetAutoDiscoveries.EthernetAutoDiscovery',
            False, 
            [
            _MetaInfoClassMember('encap', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Encap type of local or remote EAD
                ''',
                'encap',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('esi1', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{1,8}'], 
                '''                ES id (part 1/5)
                ''',
                'esi1',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('esi2', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{1,8}'], 
                '''                ES id (part 2/5)
                ''',
                'esi2',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('esi3', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{1,8}'], 
                '''                ES id (part 3/5)
                ''',
                'esi3',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('esi4', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{1,8}'], 
                '''                ES id (part 4/5)
                ''',
                'esi4',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('esi5', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{1,8}'], 
                '''                ES id (part 5/5)
                ''',
                'esi5',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('ethernet-segment-identifier', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Ethernet Segment id
                ''',
                'ethernet_segment_identifier',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('ethernet-tag', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Ethernet Tag ID
                ''',
                'ethernet_tag',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('ethernet-tag-xr', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Ethernet Tag
                ''',
                'ethernet_tag_xr',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('ethernet-vpnid', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                E-VPN id
                ''',
                'ethernet_vpnid',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('evi', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                EVPN id
                ''',
                'evi',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('is-local-ead', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Indication of EthernetAutoDiscovery Route is
                local
                ''',
                'is_local_ead',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('local-label', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Associated local label
                ''',
                'local_label',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('local-next-hop', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                Local nexthop IP
                ''',
                'local_next_hop',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('num-paths', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                 Number of items in path list buffer
                ''',
                'num_paths',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('path-buffer', REFERENCE_LIST, 'PathBuffer' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'Evpn.Standby.EviDetail.EviChildren.EthernetAutoDiscoveries.EthernetAutoDiscovery.PathBuffer', 
                [], [], 
                '''                Path List Buffer
                ''',
                'path_buffer',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('redundancy-single-active', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Single-active redundancy configured at remote
                EAD
                ''',
                'redundancy_single_active',
                'Cisco-IOS-XR-evpn-oper', False),
            ],
            'Cisco-IOS-XR-evpn-oper',
            'ethernet-auto-discovery',
            _yang_ns._namespaces['Cisco-IOS-XR-evpn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper'
        ),
    },
    'Evpn.Standby.EviDetail.EviChildren.EthernetAutoDiscoveries' : {
        'meta_info' : _MetaInfoClass('Evpn.Standby.EviDetail.EviChildren.EthernetAutoDiscoveries',
            False, 
            [
            _MetaInfoClassMember('ethernet-auto-discovery', REFERENCE_LIST, 'EthernetAutoDiscovery' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'Evpn.Standby.EviDetail.EviChildren.EthernetAutoDiscoveries.EthernetAutoDiscovery', 
                [], [], 
                '''                EVPN Ethernet Auto-Discovery Entry
                ''',
                'ethernet_auto_discovery',
                'Cisco-IOS-XR-evpn-oper', False),
            ],
            'Cisco-IOS-XR-evpn-oper',
            'ethernet-auto-discoveries',
            _yang_ns._namespaces['Cisco-IOS-XR-evpn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper'
        ),
    },
    'Evpn.Standby.EviDetail.EviChildren.InclusiveMulticasts.InclusiveMulticast' : {
        'meta_info' : _MetaInfoClass('Evpn.Standby.EviDetail.EviChildren.InclusiveMulticasts.InclusiveMulticast',
            False, 
            [
            _MetaInfoClassMember('ethernet-tag', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Ethernet Tag
                ''',
                'ethernet_tag',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('ethernet-tag-xr', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Ethernet Tag
                ''',
                'ethernet_tag_xr',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('evi', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                EVPN id
                ''',
                'evi',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('evi-xr', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                E-VPN id
                ''',
                'evi_xr',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('is-local-entry', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Local entry
                ''',
                'is_local_entry',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('next-hop', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IP of nexthop
                ''',
                'next_hop',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('originating-ip', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Originating IP
                ''',
                'originating_ip',
                'Cisco-IOS-XR-evpn-oper', False, [
                    _MetaInfoClassMember('originating-ip', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Originating IP
                        ''',
                        'originating_ip',
                        'Cisco-IOS-XR-evpn-oper', False),
                    _MetaInfoClassMember('originating-ip', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Originating IP
                        ''',
                        'originating_ip',
                        'Cisco-IOS-XR-evpn-oper', False),
                ]),
            _MetaInfoClassMember('originating-ip-xr', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                Originating IP
                ''',
                'originating_ip_xr',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('output-label', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Output label
                ''',
                'output_label',
                'Cisco-IOS-XR-evpn-oper', False),
            ],
            'Cisco-IOS-XR-evpn-oper',
            'inclusive-multicast',
            _yang_ns._namespaces['Cisco-IOS-XR-evpn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper'
        ),
    },
    'Evpn.Standby.EviDetail.EviChildren.InclusiveMulticasts' : {
        'meta_info' : _MetaInfoClass('Evpn.Standby.EviDetail.EviChildren.InclusiveMulticasts',
            False, 
            [
            _MetaInfoClassMember('inclusive-multicast', REFERENCE_LIST, 'InclusiveMulticast' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'Evpn.Standby.EviDetail.EviChildren.InclusiveMulticasts.InclusiveMulticast', 
                [], [], 
                '''                L2VPN EVPN IMCAST table
                ''',
                'inclusive_multicast',
                'Cisco-IOS-XR-evpn-oper', False),
            ],
            'Cisco-IOS-XR-evpn-oper',
            'inclusive-multicasts',
            _yang_ns._namespaces['Cisco-IOS-XR-evpn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper'
        ),
    },
    'Evpn.Standby.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_.TwoByteAs' : {
        'meta_info' : _MetaInfoClass('Evpn.Standby.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_.TwoByteAs',
            False, 
            [
            _MetaInfoClassMember('four-byte-index', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                4 Byte Index
                ''',
                'four_byte_index',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('two-byte-as', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                2 Byte AS Number
                ''',
                'two_byte_as',
                'Cisco-IOS-XR-evpn-oper', False),
            ],
            'Cisco-IOS-XR-evpn-oper',
            'two-byte-as',
            _yang_ns._namespaces['Cisco-IOS-XR-evpn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper'
        ),
    },
    'Evpn.Standby.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_.FourByteAs' : {
        'meta_info' : _MetaInfoClass('Evpn.Standby.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_.FourByteAs',
            False, 
            [
            _MetaInfoClassMember('four-byte-as', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                4 Byte AS Number
                ''',
                'four_byte_as',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('two-byte-index', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                2 Byte Index
                ''',
                'two_byte_index',
                'Cisco-IOS-XR-evpn-oper', False),
            ],
            'Cisco-IOS-XR-evpn-oper',
            'four-byte-as',
            _yang_ns._namespaces['Cisco-IOS-XR-evpn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper'
        ),
    },
    'Evpn.Standby.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_.V4Addr' : {
        'meta_info' : _MetaInfoClass('Evpn.Standby.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_.V4Addr',
            False, 
            [
            _MetaInfoClassMember('ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 Address
                ''',
                'ipv4_address',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('two-byte-index', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                2 Byte Index
                ''',
                'two_byte_index',
                'Cisco-IOS-XR-evpn-oper', False),
            ],
            'Cisco-IOS-XR-evpn-oper',
            'v4-addr',
            _yang_ns._namespaces['Cisco-IOS-XR-evpn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper'
        ),
    },
    'Evpn.Standby.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_.EsImport' : {
        'meta_info' : _MetaInfoClass('Evpn.Standby.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_.EsImport',
            False, 
            [
            _MetaInfoClassMember('high-bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Top 4 bytes of ES Import
                ''',
                'high_bytes',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('low-bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Low 2 bytes of ES Import
                ''',
                'low_bytes',
                'Cisco-IOS-XR-evpn-oper', False),
            ],
            'Cisco-IOS-XR-evpn-oper',
            'es-import',
            _yang_ns._namespaces['Cisco-IOS-XR-evpn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper'
        ),
    },
    'Evpn.Standby.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_' : {
        'meta_info' : _MetaInfoClass('Evpn.Standby.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_',
            False, 
            [
            _MetaInfoClassMember('es-import', REFERENCE_CLASS, 'EsImport' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'Evpn.Standby.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_.EsImport', 
                [], [], 
                '''                es import
                ''',
                'es_import',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('four-byte-as', REFERENCE_CLASS, 'FourByteAs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'Evpn.Standby.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_.FourByteAs', 
                [], [], 
                '''                four byte as
                ''',
                'four_byte_as',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('rt', REFERENCE_ENUM_CLASS, 'L2VpnAdRtEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'L2VpnAdRtEnum', 
                [], [], 
                '''                RT
                ''',
                'rt',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('two-byte-as', REFERENCE_CLASS, 'TwoByteAs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'Evpn.Standby.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_.TwoByteAs', 
                [], [], 
                '''                two byte as
                ''',
                'two_byte_as',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('v4-addr', REFERENCE_CLASS, 'V4Addr' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'Evpn.Standby.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_.V4Addr', 
                [], [], 
                '''                v4 addr
                ''',
                'v4_addr',
                'Cisco-IOS-XR-evpn-oper', False),
            ],
            'Cisco-IOS-XR-evpn-oper',
            'route-target',
            _yang_ns._namespaces['Cisco-IOS-XR-evpn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper'
        ),
    },
    'Evpn.Standby.EviDetail.EviChildren.RouteTargets.RouteTarget' : {
        'meta_info' : _MetaInfoClass('Evpn.Standby.EviDetail.EviChildren.RouteTargets.RouteTarget',
            False, 
            [
            _MetaInfoClassMember('addr-index', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                RT IP Index
                ''',
                'addr_index',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                RT IPv4 Address
                ''',
                'address',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('as', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                Two or Four byte AS Number
                ''',
                'as_',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('as-index', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                RT AS Index
                ''',
                'as_index',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('bd-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Bridge Domain Name
                ''',
                'bd_name',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('evi', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                EVPN id
                ''',
                'evi',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('evi-xr', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                VPN ID
                ''',
                'evi_xr',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('format', REFERENCE_ENUM_CLASS, 'BgpRouteTargetFormatEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'BgpRouteTargetFormatEnum', 
                [], [], 
                '''                Format of the route target
                ''',
                'format',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('role', REFERENCE_ENUM_CLASS, 'BgpRouteTargetRoleEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'BgpRouteTargetRoleEnum', 
                [], [], 
                '''                Role of the route target
                ''',
                'role',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('route-target', REFERENCE_CLASS, 'RouteTarget_' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'Evpn.Standby.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_', 
                [], [], 
                '''                Route Target
                ''',
                'route_target',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('route-target-role', REFERENCE_ENUM_CLASS, 'L2VpnAdRtRoleEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'L2VpnAdRtRoleEnum', 
                [], [], 
                '''                RT Role
                ''',
                'route_target_role',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('route-target-stitching', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                RT Stitching
                ''',
                'route_target_stitching',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('type', REFERENCE_ENUM_CLASS, 'BgpRouteTargetEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'BgpRouteTargetEnum', 
                [], [], 
                '''                Type of the route target
                ''',
                'type',
                'Cisco-IOS-XR-evpn-oper', False),
            ],
            'Cisco-IOS-XR-evpn-oper',
            'route-target',
            _yang_ns._namespaces['Cisco-IOS-XR-evpn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper'
        ),
    },
    'Evpn.Standby.EviDetail.EviChildren.RouteTargets' : {
        'meta_info' : _MetaInfoClass('Evpn.Standby.EviDetail.EviChildren.RouteTargets',
            False, 
            [
            _MetaInfoClassMember('route-target', REFERENCE_LIST, 'RouteTarget' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'Evpn.Standby.EviDetail.EviChildren.RouteTargets.RouteTarget', 
                [], [], 
                '''                L2VPN EVPN EVI RT Table
                ''',
                'route_target',
                'Cisco-IOS-XR-evpn-oper', False),
            ],
            'Cisco-IOS-XR-evpn-oper',
            'route-targets',
            _yang_ns._namespaces['Cisco-IOS-XR-evpn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper'
        ),
    },
    'Evpn.Standby.EviDetail.EviChildren.Macs.Mac.PathBuffer' : {
        'meta_info' : _MetaInfoClass('Evpn.Standby.EviDetail.EviChildren.Macs.Mac.PathBuffer',
            False, 
            [
            _MetaInfoClassMember('next-hop', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                Next-hop IP address (v6 format)
                ''',
                'next_hop',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('output-label', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Output Label
                ''',
                'output_label',
                'Cisco-IOS-XR-evpn-oper', False),
            ],
            'Cisco-IOS-XR-evpn-oper',
            'path-buffer',
            _yang_ns._namespaces['Cisco-IOS-XR-evpn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper'
        ),
    },
    'Evpn.Standby.EviDetail.EviChildren.Macs.Mac' : {
        'meta_info' : _MetaInfoClass('Evpn.Standby.EviDetail.EviChildren.Macs.Mac',
            False, 
            [
            _MetaInfoClassMember('esi-port-key', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                ESI port key
                ''',
                'esi_port_key',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('ethernet-tag', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Ethernet Tag ID
                ''',
                'ethernet_tag',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('ethernet-tag-xr', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Ethernet Tag
                ''',
                'ethernet_tag_xr',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('evi', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                EVPN id
                ''',
                'evi',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('internal-label', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                MPLS Internal Label
                ''',
                'internal_label',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('ip-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                IP Address
                ''',
                'ip_address',
                'Cisco-IOS-XR-evpn-oper', False, [
                    _MetaInfoClassMember('ip-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP Address
                        ''',
                        'ip_address',
                        'Cisco-IOS-XR-evpn-oper', False),
                    _MetaInfoClassMember('ip-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP Address
                        ''',
                        'ip_address',
                        'Cisco-IOS-XR-evpn-oper', False),
                ]),
            _MetaInfoClassMember('ip-address-xr', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IP address (v6 format)
                ''',
                'ip_address_xr',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('is-local-mac', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Indication of MAC being locally generated
                ''',
                'is_local_mac',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('is-remote-mac', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Indication of MAC being remotely generated
                ''',
                'is_remote_mac',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('is-static', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Indication if MAC is statically configured
                ''',
                'is_static',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('learned-bridge-port-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Port the MAC was learned on
                ''',
                'learned_bridge_port_name',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('local-encap-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Encap type of local MAC
                ''',
                'local_encap_type',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('local-ethernet-segment-identifier', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Local Ethernet Segment id
                ''',
                'local_ethernet_segment_identifier',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('local-label', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Associated local label
                ''',
                'local_label',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('local-seq-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                local seq id
                ''',
                'local_seq_id',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('mac-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                MAC address
                ''',
                'mac_address',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('mac-address-xr', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                MAC address
                ''',
                'mac_address_xr',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('mac-flush-received', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Number of flushes received 
                ''',
                'mac_flush_received',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('mac-flush-requested', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Number of flushes requested 
                ''',
                'mac_flush_requested',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('num-paths', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                 Number of items in path list buffer
                ''',
                'num_paths',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('path-buffer', REFERENCE_LIST, 'PathBuffer' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'Evpn.Standby.EviDetail.EviChildren.Macs.Mac.PathBuffer', 
                [], [], 
                '''                Path List Buffer
                ''',
                'path_buffer',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('remote-encap-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Encap type of remote MAC
                ''',
                'remote_encap_type',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('remote-ethernet-segment-identifier', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Remote Ethernet Segment id
                ''',
                'remote_ethernet_segment_identifier',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('remote-seq-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                remote seq id
                ''',
                'remote_seq_id',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('resolved', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Internal Label has resolved per-ES EAD and
                per-EVI EAD or MAC routes
                ''',
                'resolved',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('soo-nexthop', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                SOO nexthop (v6 format)
                ''',
                'soo_nexthop',
                'Cisco-IOS-XR-evpn-oper', False),
            ],
            'Cisco-IOS-XR-evpn-oper',
            'mac',
            _yang_ns._namespaces['Cisco-IOS-XR-evpn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper'
        ),
    },
    'Evpn.Standby.EviDetail.EviChildren.Macs' : {
        'meta_info' : _MetaInfoClass('Evpn.Standby.EviDetail.EviChildren.Macs',
            False, 
            [
            _MetaInfoClassMember('mac', REFERENCE_LIST, 'Mac' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'Evpn.Standby.EviDetail.EviChildren.Macs.Mac', 
                [], [], 
                '''                L2VPN EVPN MAC table
                ''',
                'mac',
                'Cisco-IOS-XR-evpn-oper', False),
            ],
            'Cisco-IOS-XR-evpn-oper',
            'macs',
            _yang_ns._namespaces['Cisco-IOS-XR-evpn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper'
        ),
    },
    'Evpn.Standby.EviDetail.EviChildren' : {
        'meta_info' : _MetaInfoClass('Evpn.Standby.EviDetail.EviChildren',
            False, 
            [
            _MetaInfoClassMember('ethernet-auto-discoveries', REFERENCE_CLASS, 'EthernetAutoDiscoveries' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'Evpn.Standby.EviDetail.EviChildren.EthernetAutoDiscoveries', 
                [], [], 
                '''                EVPN Ethernet Auto-Discovery table
                ''',
                'ethernet_auto_discoveries',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('inclusive-multicasts', REFERENCE_CLASS, 'InclusiveMulticasts' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'Evpn.Standby.EviDetail.EviChildren.InclusiveMulticasts', 
                [], [], 
                '''                L2VPN EVPN IMCAST table
                ''',
                'inclusive_multicasts',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('macs', REFERENCE_CLASS, 'Macs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'Evpn.Standby.EviDetail.EviChildren.Macs', 
                [], [], 
                '''                L2VPN EVPN EVI MAC table
                ''',
                'macs',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('neighbors', REFERENCE_CLASS, 'Neighbors' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'Evpn.Standby.EviDetail.EviChildren.Neighbors', 
                [], [], 
                '''                EVPN Neighbor table
                ''',
                'neighbors',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('route-targets', REFERENCE_CLASS, 'RouteTargets' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'Evpn.Standby.EviDetail.EviChildren.RouteTargets', 
                [], [], 
                '''                L2VPN EVPN EVI RT Child Table
                ''',
                'route_targets',
                'Cisco-IOS-XR-evpn-oper', False),
            ],
            'Cisco-IOS-XR-evpn-oper',
            'evi-children',
            _yang_ns._namespaces['Cisco-IOS-XR-evpn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper'
        ),
    },
    'Evpn.Standby.EviDetail' : {
        'meta_info' : _MetaInfoClass('Evpn.Standby.EviDetail',
            False, 
            [
            _MetaInfoClassMember('elements', REFERENCE_CLASS, 'Elements' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'Evpn.Standby.EviDetail.Elements', 
                [], [], 
                '''                EVI BGP RT Detail Info Elements
                ''',
                'elements',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('evi-children', REFERENCE_CLASS, 'EviChildren' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'Evpn.Standby.EviDetail.EviChildren', 
                [], [], 
                '''                Container for all EVI detail info
                ''',
                'evi_children',
                'Cisco-IOS-XR-evpn-oper', False),
            ],
            'Cisco-IOS-XR-evpn-oper',
            'evi-detail',
            _yang_ns._namespaces['Cisco-IOS-XR-evpn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper'
        ),
    },
    'Evpn.Standby.EthernetSegments.EthernetSegment.NextHop' : {
        'meta_info' : _MetaInfoClass('Evpn.Standby.EthernetSegments.EthernetSegment.NextHop',
            False, 
            [
            _MetaInfoClassMember('next-hop', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                Next-hop IP address (v6 format)
                ''',
                'next_hop',
                'Cisco-IOS-XR-evpn-oper', False),
            ],
            'Cisco-IOS-XR-evpn-oper',
            'next-hop',
            _yang_ns._namespaces['Cisco-IOS-XR-evpn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper'
        ),
    },
    'Evpn.Standby.EthernetSegments.EthernetSegment.RemoteSplitHorizonGroupLabel' : {
        'meta_info' : _MetaInfoClass('Evpn.Standby.EthernetSegments.EthernetSegment.RemoteSplitHorizonGroupLabel',
            False, 
            [
            _MetaInfoClassMember('label', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Split horizon label associated with next-hop
                address
                ''',
                'label',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('next-hop', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                Next-hop IP address (v6 format)
                ''',
                'next_hop',
                'Cisco-IOS-XR-evpn-oper', False),
            ],
            'Cisco-IOS-XR-evpn-oper',
            'remote-split-horizon-group-label',
            _yang_ns._namespaces['Cisco-IOS-XR-evpn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper'
        ),
    },
    'Evpn.Standby.EthernetSegments.EthernetSegment' : {
        'meta_info' : _MetaInfoClass('Evpn.Standby.EthernetSegments.EthernetSegment',
            False, 
            [
            _MetaInfoClassMember('elected-d-fs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Count of service carving results - elected
                ''',
                'elected_d_fs',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('es-bgp-gates', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                ES BGP Gates
                ''',
                'es_bgp_gates',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('es-l2fib-gates', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                ES L2FIB Gates
                ''',
                'es_l2fib_gates',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('esi1', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{1,8}'], 
                '''                ES id (part 1/5)
                ''',
                'esi1',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('esi2', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{1,8}'], 
                '''                ES id (part 2/5)
                ''',
                'esi2',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('esi3', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{1,8}'], 
                '''                ES id (part 3/5)
                ''',
                'esi3',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('esi4', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{1,8}'], 
                '''                ES id (part 4/5)
                ''',
                'esi4',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('esi5', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{1,8}'], 
                '''                ES id (part 5/5)
                ''',
                'esi5',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('esi-type', REFERENCE_ENUM_CLASS, 'L2VpnEvpnEsiEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'L2VpnEvpnEsiEnum', 
                [], [], 
                '''                ESI Type
                ''',
                'esi_type',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('ethernet-segment-identifier', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Ethernet Segment id
                ''',
                'ethernet_segment_identifier',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('ethernet-segment-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Ethernet Segment Name
                ''',
                'ethernet_segment_name',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('ethernet-segment-state', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                State of the ethernet segment
                ''',
                'ethernet_segment_state',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('force-single-home', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Ethernet-Segment forced to single home
                ''',
                'force_single_home',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('forwarder-ports', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Count of Forwarders (AC, AC PW, VFI PW)
                ''',
                'forwarder_ports',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('if-handle', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Main port ifhandle
                ''',
                'if_handle',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface
                ''',
                'interface_name',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('load-balance-mode-config', REFERENCE_ENUM_CLASS, 'L2VpnEvpnLbModeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'L2VpnEvpnLbModeEnum', 
                [], [], 
                '''                Configured load balancing mode
                ''',
                'load_balance_mode_config',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('load-balance-mode-is-default', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Load balancing mode is default
                ''',
                'load_balance_mode_is_default',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('load-balance-mode-oper', REFERENCE_ENUM_CLASS, 'L2VpnEvpnLbModeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'L2VpnEvpnLbModeEnum', 
                [], [], 
                '''                Operational load balancing mode
                ''',
                'load_balance_mode_oper',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('local-split-horizon-group-label', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Local split horizon group label
                ''',
                'local_split_horizon_group_label',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('mac-flushing-mode-config', REFERENCE_ENUM_CLASS, 'L2VpnEvpnMfModeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'L2VpnEvpnMfModeEnum', 
                [], [], 
                '''                Configured MAC Flushing mode
                ''',
                'mac_flushing_mode_config',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('main-port-mac', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                Main Port MAC Address
                ''',
                'main_port_mac',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('main-port-role', REFERENCE_ENUM_CLASS, 'L2VpnRgStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'L2VpnRgStateEnum', 
                [], [], 
                '''                Main port redundancy group role
                ''',
                'main_port_role',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('mp-protected', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                MP is protected and not under EVPN control
                ''',
                'mp_protected',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('next-hop', REFERENCE_LIST, 'NextHop' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'Evpn.Standby.EthernetSegments.EthernetSegment.NextHop', 
                [], [], 
                '''                List of nexthop IPv6 addresses
                ''',
                'next_hop',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('not-config-d-fs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Count of service carving results - missing
                config detected
                ''',
                'not_config_d_fs',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('not-elected-d-fs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Count of service carving results - not elected
                ''',
                'not_elected_d_fs',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('num-up-p-ws', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of PWs in Up state
                ''',
                'num_up_p_ws',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('peering-timer', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Configured timer for triggering DF election
                (seconds)
                ''',
                'peering_timer',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('peering-timer-left', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Milliseconds left on DF election timer
                ''',
                'peering_timer_left',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('primary-service', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                List of Primary services ESI/I-SIDs
                ''',
                'primary_service',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('primary-services-input', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Input string of Primary services ESI/I-SIDs
                ''',
                'primary_services_input',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('recovery-timer', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Configured timer for (STP) recovery (seconds)
                ''',
                'recovery_timer',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('recovery-timer-left', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Milliseconds left on (STP) recovery timer
                ''',
                'recovery_timer_left',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('remote-split-horizon-group-label', REFERENCE_LIST, 'RemoteSplitHorizonGroupLabel' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'Evpn.Standby.EthernetSegments.EthernetSegment.RemoteSplitHorizonGroupLabel', 
                [], [], 
                '''                Remote split horizon group labels
                ''',
                'remote_split_horizon_group_label',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('route-target', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                ES-Import Route Target
                ''',
                'route_target',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('rt-origin', REFERENCE_ENUM_CLASS, 'L2VpnEvpnRtOriginEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'L2VpnEvpnRtOriginEnum', 
                [], [], 
                '''                Origin of operational ES-Import RT
                ''',
                'rt_origin',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('secondary-service', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                List of Secondary services ESI/I-SIDs
                ''',
                'secondary_service',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('secondary-services-input', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Input string of Secondary services ESI/I-SIDs
                ''',
                'secondary_services_input',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('service-carving-mode', REFERENCE_ENUM_CLASS, 'L2VpnEvpnScModeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'L2VpnEvpnScModeEnum', 
                [], [], 
                '''                Service carving mode
                ''',
                'service_carving_mode',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('service-carving-result', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Service carving results
                ''',
                'service_carving_result',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('service-carving-type', REFERENCE_ENUM_CLASS, 'L2VpnEvpnScEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'L2VpnEvpnScEnum', 
                [], [], 
                '''                Service Carving Type
                ''',
                'service_carving_type',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('source-mac-oper', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                Operational Source MAC address
                ''',
                'source_mac_oper',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('source-mac-origin', REFERENCE_ENUM_CLASS, 'L2VpnEvpnSmacSrcEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'L2VpnEvpnSmacSrcEnum', 
                [], [], 
                '''                Origin of operational source MAC address
                ''',
                'source_mac_origin',
                'Cisco-IOS-XR-evpn-oper', False),
            ],
            'Cisco-IOS-XR-evpn-oper',
            'ethernet-segment',
            _yang_ns._namespaces['Cisco-IOS-XR-evpn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper'
        ),
    },
    'Evpn.Standby.EthernetSegments' : {
        'meta_info' : _MetaInfoClass('Evpn.Standby.EthernetSegments',
            False, 
            [
            _MetaInfoClassMember('ethernet-segment', REFERENCE_LIST, 'EthernetSegment' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'Evpn.Standby.EthernetSegments.EthernetSegment', 
                [], [], 
                '''                EVPN Ethernet-Segment Entry
                ''',
                'ethernet_segment',
                'Cisco-IOS-XR-evpn-oper', False),
            ],
            'Cisco-IOS-XR-evpn-oper',
            'ethernet-segments',
            _yang_ns._namespaces['Cisco-IOS-XR-evpn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper'
        ),
    },
    'Evpn.Standby.AcIds.AcId' : {
        'meta_info' : _MetaInfoClass('Evpn.Standby.AcIds.AcId',
            False, 
            [
            _MetaInfoClassMember('ac-id', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                AC ID
                ''',
                'ac_id',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('evi', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                EVPN id
                ''',
                'evi',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('evi-xr', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                E-VPN id
                ''',
                'evi_xr',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('neighbor', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                Neighbor IP
                ''',
                'neighbor',
                'Cisco-IOS-XR-evpn-oper', False),
            ],
            'Cisco-IOS-XR-evpn-oper',
            'ac-id',
            _yang_ns._namespaces['Cisco-IOS-XR-evpn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper'
        ),
    },
    'Evpn.Standby.AcIds' : {
        'meta_info' : _MetaInfoClass('Evpn.Standby.AcIds',
            False, 
            [
            _MetaInfoClassMember('ac-id', REFERENCE_LIST, 'AcId' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'Evpn.Standby.AcIds.AcId', 
                [], [], 
                '''                EVPN AC ID table
                ''',
                'ac_id',
                'Cisco-IOS-XR-evpn-oper', False),
            ],
            'Cisco-IOS-XR-evpn-oper',
            'ac-ids',
            _yang_ns._namespaces['Cisco-IOS-XR-evpn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper'
        ),
    },
    'Evpn.Standby' : {
        'meta_info' : _MetaInfoClass('Evpn.Standby',
            False, 
            [
            _MetaInfoClassMember('ac-ids', REFERENCE_CLASS, 'AcIds' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'Evpn.Standby.AcIds', 
                [], [], 
                '''                EVPN AC ID table
                ''',
                'ac_ids',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('ethernet-segments', REFERENCE_CLASS, 'EthernetSegments' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'Evpn.Standby.EthernetSegments', 
                [], [], 
                '''                EVPN Ethernet-Segment Table
                ''',
                'ethernet_segments',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('evi-detail', REFERENCE_CLASS, 'EviDetail' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'Evpn.Standby.EviDetail', 
                [], [], 
                '''                L2VPN EVI Detail Table
                ''',
                'evi_detail',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('evis', REFERENCE_CLASS, 'Evis' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'Evpn.Standby.Evis', 
                [], [], 
                '''                L2VPN EVPN EVI Table
                ''',
                'evis',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('summary', REFERENCE_CLASS, 'Summary' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'Evpn.Standby.Summary', 
                [], [], 
                '''                L2VPN EVPN Summary
                ''',
                'summary',
                'Cisco-IOS-XR-evpn-oper', False),
            ],
            'Cisco-IOS-XR-evpn-oper',
            'standby',
            _yang_ns._namespaces['Cisco-IOS-XR-evpn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper'
        ),
    },
    'Evpn' : {
        'meta_info' : _MetaInfoClass('Evpn',
            False, 
            [
            _MetaInfoClassMember('active', REFERENCE_CLASS, 'Active' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'Evpn.Active', 
                [], [], 
                '''                Active EVPN operational data
                ''',
                'active',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('nodes', REFERENCE_CLASS, 'Nodes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'Evpn.Nodes', 
                [], [], 
                '''                Table of EVPN operational data for a particular
                node
                ''',
                'nodes',
                'Cisco-IOS-XR-evpn-oper', False),
            _MetaInfoClassMember('standby', REFERENCE_CLASS, 'Standby' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper', 'Evpn.Standby', 
                [], [], 
                '''                Standby EVPN operational data
                ''',
                'standby',
                'Cisco-IOS-XR-evpn-oper', False),
            ],
            'Cisco-IOS-XR-evpn-oper',
            'evpn',
            _yang_ns._namespaces['Cisco-IOS-XR-evpn-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_evpn_oper'
        ),
    },
}
_meta_table['Evpn.Nodes.Node.Evis.Evi']['meta_info'].parent =_meta_table['Evpn.Nodes.Node.Evis']['meta_info']
_meta_table['Evpn.Nodes.Node.EviDetail.Elements.Element.RdAuto.Auto']['meta_info'].parent =_meta_table['Evpn.Nodes.Node.EviDetail.Elements.Element.RdAuto']['meta_info']
_meta_table['Evpn.Nodes.Node.EviDetail.Elements.Element.RdAuto.TwoByteAs']['meta_info'].parent =_meta_table['Evpn.Nodes.Node.EviDetail.Elements.Element.RdAuto']['meta_info']
_meta_table['Evpn.Nodes.Node.EviDetail.Elements.Element.RdAuto.FourByteAs']['meta_info'].parent =_meta_table['Evpn.Nodes.Node.EviDetail.Elements.Element.RdAuto']['meta_info']
_meta_table['Evpn.Nodes.Node.EviDetail.Elements.Element.RdAuto.V4Addr']['meta_info'].parent =_meta_table['Evpn.Nodes.Node.EviDetail.Elements.Element.RdAuto']['meta_info']
_meta_table['Evpn.Nodes.Node.EviDetail.Elements.Element.RdConfigured.Auto']['meta_info'].parent =_meta_table['Evpn.Nodes.Node.EviDetail.Elements.Element.RdConfigured']['meta_info']
_meta_table['Evpn.Nodes.Node.EviDetail.Elements.Element.RdConfigured.TwoByteAs']['meta_info'].parent =_meta_table['Evpn.Nodes.Node.EviDetail.Elements.Element.RdConfigured']['meta_info']
_meta_table['Evpn.Nodes.Node.EviDetail.Elements.Element.RdConfigured.FourByteAs']['meta_info'].parent =_meta_table['Evpn.Nodes.Node.EviDetail.Elements.Element.RdConfigured']['meta_info']
_meta_table['Evpn.Nodes.Node.EviDetail.Elements.Element.RdConfigured.V4Addr']['meta_info'].parent =_meta_table['Evpn.Nodes.Node.EviDetail.Elements.Element.RdConfigured']['meta_info']
_meta_table['Evpn.Nodes.Node.EviDetail.Elements.Element.RtAuto.TwoByteAs']['meta_info'].parent =_meta_table['Evpn.Nodes.Node.EviDetail.Elements.Element.RtAuto']['meta_info']
_meta_table['Evpn.Nodes.Node.EviDetail.Elements.Element.RtAuto.FourByteAs']['meta_info'].parent =_meta_table['Evpn.Nodes.Node.EviDetail.Elements.Element.RtAuto']['meta_info']
_meta_table['Evpn.Nodes.Node.EviDetail.Elements.Element.RtAuto.V4Addr']['meta_info'].parent =_meta_table['Evpn.Nodes.Node.EviDetail.Elements.Element.RtAuto']['meta_info']
_meta_table['Evpn.Nodes.Node.EviDetail.Elements.Element.RtAuto.EsImport']['meta_info'].parent =_meta_table['Evpn.Nodes.Node.EviDetail.Elements.Element.RtAuto']['meta_info']
_meta_table['Evpn.Nodes.Node.EviDetail.Elements.Element.RtAutoStitching.TwoByteAs']['meta_info'].parent =_meta_table['Evpn.Nodes.Node.EviDetail.Elements.Element.RtAutoStitching']['meta_info']
_meta_table['Evpn.Nodes.Node.EviDetail.Elements.Element.RtAutoStitching.FourByteAs']['meta_info'].parent =_meta_table['Evpn.Nodes.Node.EviDetail.Elements.Element.RtAutoStitching']['meta_info']
_meta_table['Evpn.Nodes.Node.EviDetail.Elements.Element.RtAutoStitching.V4Addr']['meta_info'].parent =_meta_table['Evpn.Nodes.Node.EviDetail.Elements.Element.RtAutoStitching']['meta_info']
_meta_table['Evpn.Nodes.Node.EviDetail.Elements.Element.RtAutoStitching.EsImport']['meta_info'].parent =_meta_table['Evpn.Nodes.Node.EviDetail.Elements.Element.RtAutoStitching']['meta_info']
_meta_table['Evpn.Nodes.Node.EviDetail.Elements.Element.FlowLabel']['meta_info'].parent =_meta_table['Evpn.Nodes.Node.EviDetail.Elements.Element']['meta_info']
_meta_table['Evpn.Nodes.Node.EviDetail.Elements.Element.RdAuto']['meta_info'].parent =_meta_table['Evpn.Nodes.Node.EviDetail.Elements.Element']['meta_info']
_meta_table['Evpn.Nodes.Node.EviDetail.Elements.Element.RdConfigured']['meta_info'].parent =_meta_table['Evpn.Nodes.Node.EviDetail.Elements.Element']['meta_info']
_meta_table['Evpn.Nodes.Node.EviDetail.Elements.Element.RtAuto']['meta_info'].parent =_meta_table['Evpn.Nodes.Node.EviDetail.Elements.Element']['meta_info']
_meta_table['Evpn.Nodes.Node.EviDetail.Elements.Element.RtAutoStitching']['meta_info'].parent =_meta_table['Evpn.Nodes.Node.EviDetail.Elements.Element']['meta_info']
_meta_table['Evpn.Nodes.Node.EviDetail.Elements.Element']['meta_info'].parent =_meta_table['Evpn.Nodes.Node.EviDetail.Elements']['meta_info']
_meta_table['Evpn.Nodes.Node.EviDetail.EviChildren.Neighbors.Neighbor']['meta_info'].parent =_meta_table['Evpn.Nodes.Node.EviDetail.EviChildren.Neighbors']['meta_info']
_meta_table['Evpn.Nodes.Node.EviDetail.EviChildren.EthernetAutoDiscoveries.EthernetAutoDiscovery.PathBuffer']['meta_info'].parent =_meta_table['Evpn.Nodes.Node.EviDetail.EviChildren.EthernetAutoDiscoveries.EthernetAutoDiscovery']['meta_info']
_meta_table['Evpn.Nodes.Node.EviDetail.EviChildren.EthernetAutoDiscoveries.EthernetAutoDiscovery']['meta_info'].parent =_meta_table['Evpn.Nodes.Node.EviDetail.EviChildren.EthernetAutoDiscoveries']['meta_info']
_meta_table['Evpn.Nodes.Node.EviDetail.EviChildren.InclusiveMulticasts.InclusiveMulticast']['meta_info'].parent =_meta_table['Evpn.Nodes.Node.EviDetail.EviChildren.InclusiveMulticasts']['meta_info']
_meta_table['Evpn.Nodes.Node.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_.TwoByteAs']['meta_info'].parent =_meta_table['Evpn.Nodes.Node.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_']['meta_info']
_meta_table['Evpn.Nodes.Node.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_.FourByteAs']['meta_info'].parent =_meta_table['Evpn.Nodes.Node.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_']['meta_info']
_meta_table['Evpn.Nodes.Node.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_.V4Addr']['meta_info'].parent =_meta_table['Evpn.Nodes.Node.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_']['meta_info']
_meta_table['Evpn.Nodes.Node.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_.EsImport']['meta_info'].parent =_meta_table['Evpn.Nodes.Node.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_']['meta_info']
_meta_table['Evpn.Nodes.Node.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_']['meta_info'].parent =_meta_table['Evpn.Nodes.Node.EviDetail.EviChildren.RouteTargets.RouteTarget']['meta_info']
_meta_table['Evpn.Nodes.Node.EviDetail.EviChildren.RouteTargets.RouteTarget']['meta_info'].parent =_meta_table['Evpn.Nodes.Node.EviDetail.EviChildren.RouteTargets']['meta_info']
_meta_table['Evpn.Nodes.Node.EviDetail.EviChildren.Macs.Mac.PathBuffer']['meta_info'].parent =_meta_table['Evpn.Nodes.Node.EviDetail.EviChildren.Macs.Mac']['meta_info']
_meta_table['Evpn.Nodes.Node.EviDetail.EviChildren.Macs.Mac']['meta_info'].parent =_meta_table['Evpn.Nodes.Node.EviDetail.EviChildren.Macs']['meta_info']
_meta_table['Evpn.Nodes.Node.EviDetail.EviChildren.Neighbors']['meta_info'].parent =_meta_table['Evpn.Nodes.Node.EviDetail.EviChildren']['meta_info']
_meta_table['Evpn.Nodes.Node.EviDetail.EviChildren.EthernetAutoDiscoveries']['meta_info'].parent =_meta_table['Evpn.Nodes.Node.EviDetail.EviChildren']['meta_info']
_meta_table['Evpn.Nodes.Node.EviDetail.EviChildren.InclusiveMulticasts']['meta_info'].parent =_meta_table['Evpn.Nodes.Node.EviDetail.EviChildren']['meta_info']
_meta_table['Evpn.Nodes.Node.EviDetail.EviChildren.RouteTargets']['meta_info'].parent =_meta_table['Evpn.Nodes.Node.EviDetail.EviChildren']['meta_info']
_meta_table['Evpn.Nodes.Node.EviDetail.EviChildren.Macs']['meta_info'].parent =_meta_table['Evpn.Nodes.Node.EviDetail.EviChildren']['meta_info']
_meta_table['Evpn.Nodes.Node.EviDetail.Elements']['meta_info'].parent =_meta_table['Evpn.Nodes.Node.EviDetail']['meta_info']
_meta_table['Evpn.Nodes.Node.EviDetail.EviChildren']['meta_info'].parent =_meta_table['Evpn.Nodes.Node.EviDetail']['meta_info']
_meta_table['Evpn.Nodes.Node.EthernetSegments.EthernetSegment.NextHop']['meta_info'].parent =_meta_table['Evpn.Nodes.Node.EthernetSegments.EthernetSegment']['meta_info']
_meta_table['Evpn.Nodes.Node.EthernetSegments.EthernetSegment.RemoteSplitHorizonGroupLabel']['meta_info'].parent =_meta_table['Evpn.Nodes.Node.EthernetSegments.EthernetSegment']['meta_info']
_meta_table['Evpn.Nodes.Node.EthernetSegments.EthernetSegment']['meta_info'].parent =_meta_table['Evpn.Nodes.Node.EthernetSegments']['meta_info']
_meta_table['Evpn.Nodes.Node.AcIds.AcId']['meta_info'].parent =_meta_table['Evpn.Nodes.Node.AcIds']['meta_info']
_meta_table['Evpn.Nodes.Node.Evis']['meta_info'].parent =_meta_table['Evpn.Nodes.Node']['meta_info']
_meta_table['Evpn.Nodes.Node.Summary']['meta_info'].parent =_meta_table['Evpn.Nodes.Node']['meta_info']
_meta_table['Evpn.Nodes.Node.EviDetail']['meta_info'].parent =_meta_table['Evpn.Nodes.Node']['meta_info']
_meta_table['Evpn.Nodes.Node.EthernetSegments']['meta_info'].parent =_meta_table['Evpn.Nodes.Node']['meta_info']
_meta_table['Evpn.Nodes.Node.AcIds']['meta_info'].parent =_meta_table['Evpn.Nodes.Node']['meta_info']
_meta_table['Evpn.Nodes.Node']['meta_info'].parent =_meta_table['Evpn.Nodes']['meta_info']
_meta_table['Evpn.Active.Evis.Evi']['meta_info'].parent =_meta_table['Evpn.Active.Evis']['meta_info']
_meta_table['Evpn.Active.EviDetail.Elements.Element.RdAuto.Auto']['meta_info'].parent =_meta_table['Evpn.Active.EviDetail.Elements.Element.RdAuto']['meta_info']
_meta_table['Evpn.Active.EviDetail.Elements.Element.RdAuto.TwoByteAs']['meta_info'].parent =_meta_table['Evpn.Active.EviDetail.Elements.Element.RdAuto']['meta_info']
_meta_table['Evpn.Active.EviDetail.Elements.Element.RdAuto.FourByteAs']['meta_info'].parent =_meta_table['Evpn.Active.EviDetail.Elements.Element.RdAuto']['meta_info']
_meta_table['Evpn.Active.EviDetail.Elements.Element.RdAuto.V4Addr']['meta_info'].parent =_meta_table['Evpn.Active.EviDetail.Elements.Element.RdAuto']['meta_info']
_meta_table['Evpn.Active.EviDetail.Elements.Element.RdConfigured.Auto']['meta_info'].parent =_meta_table['Evpn.Active.EviDetail.Elements.Element.RdConfigured']['meta_info']
_meta_table['Evpn.Active.EviDetail.Elements.Element.RdConfigured.TwoByteAs']['meta_info'].parent =_meta_table['Evpn.Active.EviDetail.Elements.Element.RdConfigured']['meta_info']
_meta_table['Evpn.Active.EviDetail.Elements.Element.RdConfigured.FourByteAs']['meta_info'].parent =_meta_table['Evpn.Active.EviDetail.Elements.Element.RdConfigured']['meta_info']
_meta_table['Evpn.Active.EviDetail.Elements.Element.RdConfigured.V4Addr']['meta_info'].parent =_meta_table['Evpn.Active.EviDetail.Elements.Element.RdConfigured']['meta_info']
_meta_table['Evpn.Active.EviDetail.Elements.Element.RtAuto.TwoByteAs']['meta_info'].parent =_meta_table['Evpn.Active.EviDetail.Elements.Element.RtAuto']['meta_info']
_meta_table['Evpn.Active.EviDetail.Elements.Element.RtAuto.FourByteAs']['meta_info'].parent =_meta_table['Evpn.Active.EviDetail.Elements.Element.RtAuto']['meta_info']
_meta_table['Evpn.Active.EviDetail.Elements.Element.RtAuto.V4Addr']['meta_info'].parent =_meta_table['Evpn.Active.EviDetail.Elements.Element.RtAuto']['meta_info']
_meta_table['Evpn.Active.EviDetail.Elements.Element.RtAuto.EsImport']['meta_info'].parent =_meta_table['Evpn.Active.EviDetail.Elements.Element.RtAuto']['meta_info']
_meta_table['Evpn.Active.EviDetail.Elements.Element.RtAutoStitching.TwoByteAs']['meta_info'].parent =_meta_table['Evpn.Active.EviDetail.Elements.Element.RtAutoStitching']['meta_info']
_meta_table['Evpn.Active.EviDetail.Elements.Element.RtAutoStitching.FourByteAs']['meta_info'].parent =_meta_table['Evpn.Active.EviDetail.Elements.Element.RtAutoStitching']['meta_info']
_meta_table['Evpn.Active.EviDetail.Elements.Element.RtAutoStitching.V4Addr']['meta_info'].parent =_meta_table['Evpn.Active.EviDetail.Elements.Element.RtAutoStitching']['meta_info']
_meta_table['Evpn.Active.EviDetail.Elements.Element.RtAutoStitching.EsImport']['meta_info'].parent =_meta_table['Evpn.Active.EviDetail.Elements.Element.RtAutoStitching']['meta_info']
_meta_table['Evpn.Active.EviDetail.Elements.Element.FlowLabel']['meta_info'].parent =_meta_table['Evpn.Active.EviDetail.Elements.Element']['meta_info']
_meta_table['Evpn.Active.EviDetail.Elements.Element.RdAuto']['meta_info'].parent =_meta_table['Evpn.Active.EviDetail.Elements.Element']['meta_info']
_meta_table['Evpn.Active.EviDetail.Elements.Element.RdConfigured']['meta_info'].parent =_meta_table['Evpn.Active.EviDetail.Elements.Element']['meta_info']
_meta_table['Evpn.Active.EviDetail.Elements.Element.RtAuto']['meta_info'].parent =_meta_table['Evpn.Active.EviDetail.Elements.Element']['meta_info']
_meta_table['Evpn.Active.EviDetail.Elements.Element.RtAutoStitching']['meta_info'].parent =_meta_table['Evpn.Active.EviDetail.Elements.Element']['meta_info']
_meta_table['Evpn.Active.EviDetail.Elements.Element']['meta_info'].parent =_meta_table['Evpn.Active.EviDetail.Elements']['meta_info']
_meta_table['Evpn.Active.EviDetail.EviChildren.Neighbors.Neighbor']['meta_info'].parent =_meta_table['Evpn.Active.EviDetail.EviChildren.Neighbors']['meta_info']
_meta_table['Evpn.Active.EviDetail.EviChildren.EthernetAutoDiscoveries.EthernetAutoDiscovery.PathBuffer']['meta_info'].parent =_meta_table['Evpn.Active.EviDetail.EviChildren.EthernetAutoDiscoveries.EthernetAutoDiscovery']['meta_info']
_meta_table['Evpn.Active.EviDetail.EviChildren.EthernetAutoDiscoveries.EthernetAutoDiscovery']['meta_info'].parent =_meta_table['Evpn.Active.EviDetail.EviChildren.EthernetAutoDiscoveries']['meta_info']
_meta_table['Evpn.Active.EviDetail.EviChildren.InclusiveMulticasts.InclusiveMulticast']['meta_info'].parent =_meta_table['Evpn.Active.EviDetail.EviChildren.InclusiveMulticasts']['meta_info']
_meta_table['Evpn.Active.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_.TwoByteAs']['meta_info'].parent =_meta_table['Evpn.Active.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_']['meta_info']
_meta_table['Evpn.Active.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_.FourByteAs']['meta_info'].parent =_meta_table['Evpn.Active.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_']['meta_info']
_meta_table['Evpn.Active.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_.V4Addr']['meta_info'].parent =_meta_table['Evpn.Active.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_']['meta_info']
_meta_table['Evpn.Active.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_.EsImport']['meta_info'].parent =_meta_table['Evpn.Active.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_']['meta_info']
_meta_table['Evpn.Active.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_']['meta_info'].parent =_meta_table['Evpn.Active.EviDetail.EviChildren.RouteTargets.RouteTarget']['meta_info']
_meta_table['Evpn.Active.EviDetail.EviChildren.RouteTargets.RouteTarget']['meta_info'].parent =_meta_table['Evpn.Active.EviDetail.EviChildren.RouteTargets']['meta_info']
_meta_table['Evpn.Active.EviDetail.EviChildren.Macs.Mac.PathBuffer']['meta_info'].parent =_meta_table['Evpn.Active.EviDetail.EviChildren.Macs.Mac']['meta_info']
_meta_table['Evpn.Active.EviDetail.EviChildren.Macs.Mac']['meta_info'].parent =_meta_table['Evpn.Active.EviDetail.EviChildren.Macs']['meta_info']
_meta_table['Evpn.Active.EviDetail.EviChildren.Neighbors']['meta_info'].parent =_meta_table['Evpn.Active.EviDetail.EviChildren']['meta_info']
_meta_table['Evpn.Active.EviDetail.EviChildren.EthernetAutoDiscoveries']['meta_info'].parent =_meta_table['Evpn.Active.EviDetail.EviChildren']['meta_info']
_meta_table['Evpn.Active.EviDetail.EviChildren.InclusiveMulticasts']['meta_info'].parent =_meta_table['Evpn.Active.EviDetail.EviChildren']['meta_info']
_meta_table['Evpn.Active.EviDetail.EviChildren.RouteTargets']['meta_info'].parent =_meta_table['Evpn.Active.EviDetail.EviChildren']['meta_info']
_meta_table['Evpn.Active.EviDetail.EviChildren.Macs']['meta_info'].parent =_meta_table['Evpn.Active.EviDetail.EviChildren']['meta_info']
_meta_table['Evpn.Active.EviDetail.Elements']['meta_info'].parent =_meta_table['Evpn.Active.EviDetail']['meta_info']
_meta_table['Evpn.Active.EviDetail.EviChildren']['meta_info'].parent =_meta_table['Evpn.Active.EviDetail']['meta_info']
_meta_table['Evpn.Active.EthernetSegments.EthernetSegment.NextHop']['meta_info'].parent =_meta_table['Evpn.Active.EthernetSegments.EthernetSegment']['meta_info']
_meta_table['Evpn.Active.EthernetSegments.EthernetSegment.RemoteSplitHorizonGroupLabel']['meta_info'].parent =_meta_table['Evpn.Active.EthernetSegments.EthernetSegment']['meta_info']
_meta_table['Evpn.Active.EthernetSegments.EthernetSegment']['meta_info'].parent =_meta_table['Evpn.Active.EthernetSegments']['meta_info']
_meta_table['Evpn.Active.AcIds.AcId']['meta_info'].parent =_meta_table['Evpn.Active.AcIds']['meta_info']
_meta_table['Evpn.Active.Evis']['meta_info'].parent =_meta_table['Evpn.Active']['meta_info']
_meta_table['Evpn.Active.Summary']['meta_info'].parent =_meta_table['Evpn.Active']['meta_info']
_meta_table['Evpn.Active.EviDetail']['meta_info'].parent =_meta_table['Evpn.Active']['meta_info']
_meta_table['Evpn.Active.EthernetSegments']['meta_info'].parent =_meta_table['Evpn.Active']['meta_info']
_meta_table['Evpn.Active.AcIds']['meta_info'].parent =_meta_table['Evpn.Active']['meta_info']
_meta_table['Evpn.Standby.Evis.Evi']['meta_info'].parent =_meta_table['Evpn.Standby.Evis']['meta_info']
_meta_table['Evpn.Standby.EviDetail.Elements.Element.RdAuto.Auto']['meta_info'].parent =_meta_table['Evpn.Standby.EviDetail.Elements.Element.RdAuto']['meta_info']
_meta_table['Evpn.Standby.EviDetail.Elements.Element.RdAuto.TwoByteAs']['meta_info'].parent =_meta_table['Evpn.Standby.EviDetail.Elements.Element.RdAuto']['meta_info']
_meta_table['Evpn.Standby.EviDetail.Elements.Element.RdAuto.FourByteAs']['meta_info'].parent =_meta_table['Evpn.Standby.EviDetail.Elements.Element.RdAuto']['meta_info']
_meta_table['Evpn.Standby.EviDetail.Elements.Element.RdAuto.V4Addr']['meta_info'].parent =_meta_table['Evpn.Standby.EviDetail.Elements.Element.RdAuto']['meta_info']
_meta_table['Evpn.Standby.EviDetail.Elements.Element.RdConfigured.Auto']['meta_info'].parent =_meta_table['Evpn.Standby.EviDetail.Elements.Element.RdConfigured']['meta_info']
_meta_table['Evpn.Standby.EviDetail.Elements.Element.RdConfigured.TwoByteAs']['meta_info'].parent =_meta_table['Evpn.Standby.EviDetail.Elements.Element.RdConfigured']['meta_info']
_meta_table['Evpn.Standby.EviDetail.Elements.Element.RdConfigured.FourByteAs']['meta_info'].parent =_meta_table['Evpn.Standby.EviDetail.Elements.Element.RdConfigured']['meta_info']
_meta_table['Evpn.Standby.EviDetail.Elements.Element.RdConfigured.V4Addr']['meta_info'].parent =_meta_table['Evpn.Standby.EviDetail.Elements.Element.RdConfigured']['meta_info']
_meta_table['Evpn.Standby.EviDetail.Elements.Element.RtAuto.TwoByteAs']['meta_info'].parent =_meta_table['Evpn.Standby.EviDetail.Elements.Element.RtAuto']['meta_info']
_meta_table['Evpn.Standby.EviDetail.Elements.Element.RtAuto.FourByteAs']['meta_info'].parent =_meta_table['Evpn.Standby.EviDetail.Elements.Element.RtAuto']['meta_info']
_meta_table['Evpn.Standby.EviDetail.Elements.Element.RtAuto.V4Addr']['meta_info'].parent =_meta_table['Evpn.Standby.EviDetail.Elements.Element.RtAuto']['meta_info']
_meta_table['Evpn.Standby.EviDetail.Elements.Element.RtAuto.EsImport']['meta_info'].parent =_meta_table['Evpn.Standby.EviDetail.Elements.Element.RtAuto']['meta_info']
_meta_table['Evpn.Standby.EviDetail.Elements.Element.RtAutoStitching.TwoByteAs']['meta_info'].parent =_meta_table['Evpn.Standby.EviDetail.Elements.Element.RtAutoStitching']['meta_info']
_meta_table['Evpn.Standby.EviDetail.Elements.Element.RtAutoStitching.FourByteAs']['meta_info'].parent =_meta_table['Evpn.Standby.EviDetail.Elements.Element.RtAutoStitching']['meta_info']
_meta_table['Evpn.Standby.EviDetail.Elements.Element.RtAutoStitching.V4Addr']['meta_info'].parent =_meta_table['Evpn.Standby.EviDetail.Elements.Element.RtAutoStitching']['meta_info']
_meta_table['Evpn.Standby.EviDetail.Elements.Element.RtAutoStitching.EsImport']['meta_info'].parent =_meta_table['Evpn.Standby.EviDetail.Elements.Element.RtAutoStitching']['meta_info']
_meta_table['Evpn.Standby.EviDetail.Elements.Element.FlowLabel']['meta_info'].parent =_meta_table['Evpn.Standby.EviDetail.Elements.Element']['meta_info']
_meta_table['Evpn.Standby.EviDetail.Elements.Element.RdAuto']['meta_info'].parent =_meta_table['Evpn.Standby.EviDetail.Elements.Element']['meta_info']
_meta_table['Evpn.Standby.EviDetail.Elements.Element.RdConfigured']['meta_info'].parent =_meta_table['Evpn.Standby.EviDetail.Elements.Element']['meta_info']
_meta_table['Evpn.Standby.EviDetail.Elements.Element.RtAuto']['meta_info'].parent =_meta_table['Evpn.Standby.EviDetail.Elements.Element']['meta_info']
_meta_table['Evpn.Standby.EviDetail.Elements.Element.RtAutoStitching']['meta_info'].parent =_meta_table['Evpn.Standby.EviDetail.Elements.Element']['meta_info']
_meta_table['Evpn.Standby.EviDetail.Elements.Element']['meta_info'].parent =_meta_table['Evpn.Standby.EviDetail.Elements']['meta_info']
_meta_table['Evpn.Standby.EviDetail.EviChildren.Neighbors.Neighbor']['meta_info'].parent =_meta_table['Evpn.Standby.EviDetail.EviChildren.Neighbors']['meta_info']
_meta_table['Evpn.Standby.EviDetail.EviChildren.EthernetAutoDiscoveries.EthernetAutoDiscovery.PathBuffer']['meta_info'].parent =_meta_table['Evpn.Standby.EviDetail.EviChildren.EthernetAutoDiscoveries.EthernetAutoDiscovery']['meta_info']
_meta_table['Evpn.Standby.EviDetail.EviChildren.EthernetAutoDiscoveries.EthernetAutoDiscovery']['meta_info'].parent =_meta_table['Evpn.Standby.EviDetail.EviChildren.EthernetAutoDiscoveries']['meta_info']
_meta_table['Evpn.Standby.EviDetail.EviChildren.InclusiveMulticasts.InclusiveMulticast']['meta_info'].parent =_meta_table['Evpn.Standby.EviDetail.EviChildren.InclusiveMulticasts']['meta_info']
_meta_table['Evpn.Standby.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_.TwoByteAs']['meta_info'].parent =_meta_table['Evpn.Standby.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_']['meta_info']
_meta_table['Evpn.Standby.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_.FourByteAs']['meta_info'].parent =_meta_table['Evpn.Standby.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_']['meta_info']
_meta_table['Evpn.Standby.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_.V4Addr']['meta_info'].parent =_meta_table['Evpn.Standby.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_']['meta_info']
_meta_table['Evpn.Standby.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_.EsImport']['meta_info'].parent =_meta_table['Evpn.Standby.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_']['meta_info']
_meta_table['Evpn.Standby.EviDetail.EviChildren.RouteTargets.RouteTarget.RouteTarget_']['meta_info'].parent =_meta_table['Evpn.Standby.EviDetail.EviChildren.RouteTargets.RouteTarget']['meta_info']
_meta_table['Evpn.Standby.EviDetail.EviChildren.RouteTargets.RouteTarget']['meta_info'].parent =_meta_table['Evpn.Standby.EviDetail.EviChildren.RouteTargets']['meta_info']
_meta_table['Evpn.Standby.EviDetail.EviChildren.Macs.Mac.PathBuffer']['meta_info'].parent =_meta_table['Evpn.Standby.EviDetail.EviChildren.Macs.Mac']['meta_info']
_meta_table['Evpn.Standby.EviDetail.EviChildren.Macs.Mac']['meta_info'].parent =_meta_table['Evpn.Standby.EviDetail.EviChildren.Macs']['meta_info']
_meta_table['Evpn.Standby.EviDetail.EviChildren.Neighbors']['meta_info'].parent =_meta_table['Evpn.Standby.EviDetail.EviChildren']['meta_info']
_meta_table['Evpn.Standby.EviDetail.EviChildren.EthernetAutoDiscoveries']['meta_info'].parent =_meta_table['Evpn.Standby.EviDetail.EviChildren']['meta_info']
_meta_table['Evpn.Standby.EviDetail.EviChildren.InclusiveMulticasts']['meta_info'].parent =_meta_table['Evpn.Standby.EviDetail.EviChildren']['meta_info']
_meta_table['Evpn.Standby.EviDetail.EviChildren.RouteTargets']['meta_info'].parent =_meta_table['Evpn.Standby.EviDetail.EviChildren']['meta_info']
_meta_table['Evpn.Standby.EviDetail.EviChildren.Macs']['meta_info'].parent =_meta_table['Evpn.Standby.EviDetail.EviChildren']['meta_info']
_meta_table['Evpn.Standby.EviDetail.Elements']['meta_info'].parent =_meta_table['Evpn.Standby.EviDetail']['meta_info']
_meta_table['Evpn.Standby.EviDetail.EviChildren']['meta_info'].parent =_meta_table['Evpn.Standby.EviDetail']['meta_info']
_meta_table['Evpn.Standby.EthernetSegments.EthernetSegment.NextHop']['meta_info'].parent =_meta_table['Evpn.Standby.EthernetSegments.EthernetSegment']['meta_info']
_meta_table['Evpn.Standby.EthernetSegments.EthernetSegment.RemoteSplitHorizonGroupLabel']['meta_info'].parent =_meta_table['Evpn.Standby.EthernetSegments.EthernetSegment']['meta_info']
_meta_table['Evpn.Standby.EthernetSegments.EthernetSegment']['meta_info'].parent =_meta_table['Evpn.Standby.EthernetSegments']['meta_info']
_meta_table['Evpn.Standby.AcIds.AcId']['meta_info'].parent =_meta_table['Evpn.Standby.AcIds']['meta_info']
_meta_table['Evpn.Standby.Evis']['meta_info'].parent =_meta_table['Evpn.Standby']['meta_info']
_meta_table['Evpn.Standby.Summary']['meta_info'].parent =_meta_table['Evpn.Standby']['meta_info']
_meta_table['Evpn.Standby.EviDetail']['meta_info'].parent =_meta_table['Evpn.Standby']['meta_info']
_meta_table['Evpn.Standby.EthernetSegments']['meta_info'].parent =_meta_table['Evpn.Standby']['meta_info']
_meta_table['Evpn.Standby.AcIds']['meta_info'].parent =_meta_table['Evpn.Standby']['meta_info']
_meta_table['Evpn.Nodes']['meta_info'].parent =_meta_table['Evpn']['meta_info']
_meta_table['Evpn.Active']['meta_info'].parent =_meta_table['Evpn']['meta_info']
_meta_table['Evpn.Standby']['meta_info'].parent =_meta_table['Evpn']['meta_info']
